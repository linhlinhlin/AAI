"""Paired feature ablation on the existing three cohorts; no new cohort or label selection."""

import hashlib
import json
from collections import Counter
from pathlib import Path

import numpy as np
from sklearn.metrics import adjusted_rand_score

from misconceptions.adapters import load_dataset
from misconceptions.cli import build_provenance
from misconceptions.pipeline import run_experiment

MODES = {"A": "outcomes", "B": "structural", "C": "combined"}
SEEDS = (7, 42, 91)


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False), encoding="utf-8"
    )


def summarize(problem, arm, seed, rows, result):
    train = result.get("train_assignments", {})
    held = result.get("holdout_assignments", {})
    explanation = result.get("explanation", {})
    split = result.get("split", {})
    train_sizes = Counter(train.values())
    return {
        "problem_id": problem,
        "arm": arm,
        "mode": MODES[arm],
        "seed": seed,
        "n_input": len(rows),
        "n_eligible": result["n_eligible"],
        "n_train": len(split.get("train_ids", [])),
        "n_holdout": len(split.get("holdout_ids", [])),
        "status": result["status"],
        "reason": result.get("reason"),
        "n_clusters": result.get("n_clusters"),
        "n_features": len(result.get("features", [])),
        "train_cluster_sizes": dict(sorted(train_sizes.items())),
        "holdout_cluster_sizes": dict(sorted(Counter(held.values()).items())),
        "combined_cluster_sizes": dict(sorted(Counter((train | held).values()).items())),
        "train_singleton_clusters": sum(size == 1 for size in train_sizes.values())
        if train
        else None,
        "silhouette_train": result.get("silhouette_train"),
        "ari_vs_exact_signature_train": result.get("ari_vs_exact_signature_train"),
        "rule_train_fidelity": explanation.get("train_fidelity"),
        "rule_holdout_fidelity": explanation.get("holdout_fidelity"),
        "majority_holdout_fidelity": explanation.get("holdout_majority_baseline_fidelity"),
        "holdout_ties": result.get("holdout_assignment_ties"),
        "mean_holdout_distance": float(np.mean(list(result["holdout_distance_to_medoid"].values())))
        if held
        else None,
        "feature_weights": result.get("features", []),
        "routing": result["route_counts"],
        "identity": result["identity"],
    }


def main():
    root = Path(__file__).resolve().parents[1]
    output = root / "results/itsp"
    selection_path = output / "selection.json"
    selected = json.loads(selection_path.read_text())["cohorts"]
    problems = [item["problem_id"] for item in selected if item["selected"]]
    template = output / "annotation_template.jsonl"
    review_rows = [json.loads(line) for line in template.read_text().splitlines() if line.strip()]
    review_hash = hashlib.sha256(template.read_bytes()).hexdigest()
    results, records, agreement = {}, [], []
    for problem in problems:
        directory = root / "data/itsp/cohorts" / problem
        manifest, rows = load_dataset(directory / "manifest.json", directory / "submissions.jsonl")
        provenance = build_provenance(
            manifest, directory / "manifest.json", directory / "submissions.jsonl"
        )
        for seed in SEEDS:
            reference = None
            for arm, mode in MODES.items():
                result = run_experiment(
                    rows,
                    test_ids=manifest["test_ids"],
                    feature_mode=mode,
                    method="agglomerative",
                    k=3,
                    seed=seed,
                    test_weight=0.8,
                )
                if reference is not None:
                    assert result["split"] == reference["split"], "A/B/C split mismatch"
                    assert result["routes"] == reference["routes"], "A/B/C routing mismatch"
                reference = result
                result["provenance"] = provenance
                # A/C must reproduce the pre-existing runs on these exact same files.
                if arm in ("A", "C"):
                    legacy_path = output / problem / f"agglomerative_{mode}_k3_w0.8_seed{seed}.json"
                    legacy = json.loads(legacy_path.read_text())
                    assert legacy["provenance"]["input_sha256"] == provenance["input_sha256"]
                    for field in (
                        "split",
                        "features",
                        "train_assignments",
                        "holdout_assignments",
                        "explanation",
                    ):
                        assert result.get(field) == legacy.get(field), f"Legacy regression: {field}"
                save(output / "abc" / f"{problem}_{arm}_seed{seed}.json", result)
                records.append(summarize(problem, arm, seed, rows, result))
                results[problem, arm, seed] = result
            for left, right in (("A", "B"), ("A", "C"), ("B", "C")):
                first, second = results[problem, left, seed], results[problem, right, seed]
                ids = first["split"]["train_ids"]
                score = None
                if first["status"] == second["status"] == "ok":
                    score = float(
                        adjusted_rand_score(
                            [first["train_assignments"][sid] for sid in ids],
                            [second["train_assignments"][sid] for sid in ids],
                        )
                    )
                agreement.append(
                    {
                        "problem_id": problem,
                        "seed": seed,
                        "pair": left + right,
                        "train_partition_ari": score,
                    }
                )

    review_clusters = []
    for row in review_rows:
        sid, problem = row["submission_id"], row["problem_id"]
        original = results[problem, "C", 42]
        split = "train" if sid in original["split"]["train_ids"] else "holdout"
        reason = (
            "training_medoid" if sid in original["medoids"].values() else "farthest_holdout_member"
        )
        if reason == "farthest_holdout_member":
            cluster = original["holdout_assignments"][sid]
            members = [
                key for key, value in original["holdout_assignments"].items() if value == cluster
            ]
            assert sid == max(
                members, key=lambda key: (original["holdout_distance_to_medoid"][key], key)
            )
        review_clusters.append(
            {
                "submission_id": sid,
                "problem_id": problem,
                "split": split,
                "selection_reason": reason,
                "clusters_seed42": {
                    arm: results[problem, arm, 42].get(f"{split}_assignments", {}).get(sid)
                    for arm in MODES
                },
            }
        )
    # Reconstruct the complete candidate set, not just membership of listed examples.
    expected_ids = set()
    for problem in problems:
        run = results[problem, "C", 42]
        expected_ids.update(run["medoids"].values())
        for label in set(run["holdout_assignments"].values()):
            members = [sid for sid, value in run["holdout_assignments"].items() if value == label]
            expected_ids.add(
                max(members, key=lambda sid: (run["holdout_distance_to_medoid"][sid], sid))
            )
    assert (
        len(review_rows) == len(expected_ids) == len({row["submission_id"] for row in review_rows})
    )
    assert expected_ids == {row["submission_id"] for row in review_rows}
    assert hashlib.sha256(template.read_bytes()).hexdigest() == review_hash
    save(output / "abc_review_assignments.json", review_clusters)
    protocol = {
        "problems": problems,
        "arms": MODES,
        "method": "agglomerative",
        "linkage": "average",
        "k": 3,
        "seeds": SEEDS,
        "test_fraction": 0.25,
        "combined_test_mass": 0.8,
        "routing_and_splits_asserted_identical": True,
        "legacy_A_C_asserted_unchanged": True,
        "selection_sha256": hashlib.sha256(selection_path.read_bytes()).hexdigest(),
        "review_template_sha256": review_hash,
        "metric_caveat": "Silhouette and medoid distances use different feature geometries in A/B/C; not a direct educational-quality ranking.",
        "identity_caveat": "No student IDs: no unseen-student generalization claim.",
        "review_sampling": "9 train medoids + 8 farthest holdout members from original C seed42; purposive, not random or representative.",
    }
    save(
        output / "abc_summary.json",
        {"protocol": protocol, "experiments": records, "partition_agreement": agreement},
    )
    save(
        output / "expert_metric_readiness.json",
        {
            "n_review_candidates": len(review_rows),
            "n_pending": sum(row["status"] == "pending_expert_review" for row in review_rows),
            "n_candidates_with_labels": sum(bool(row["labels"]) for row in review_rows),
            "cluster_purity": None,
            "inter_rater_agreement": None,
            "reason": "No independently completed expert annotations or agreed label taxonomy available; assistant hypotheses are not gold.",
            "required": [
                "Agreed label codebook and single/multi-label policy",
                "Independent expert labels with reviewer IDs",
                "Adjudicated labels for purity; two pre-adjudication raters for agreement",
                "Per-problem/configuration results and coverage; no population claim from purposive sample",
            ],
        },
    )
    lines = [
        "## Validation A/B/C trên cùng dữ liệu",
        "",
        "Giữ 59 mẫu thuộc ba bài cũ; agglomerative average-linkage, k=3, seeds 7/42/91, holdout 25% theo nhóm source.",
        "A = test only; B = structural only; C = test 0,8 + structural 0,2. Feature cấu trúc hằng chỉ bỏ theo train.",
        "OAV là cách biểu diễn, không phải đồng nghĩa với structural. Không có ID sinh viên hoặc expert gold.",
        "Silhouette dùng không gian riêng từng cấu hình; không xếp hạng chất lượng misconception bằng các số này.",
        "",
        "Bảng seed=42 (cấu hình minh họa có sẵn, không chọn lại theo kết quả):",
        "",
        "| Bài | Arm | Input/eligible | Train/holdout | Features | Clusters | Kích thước train | Silhouette | Fidelity / majority |",
        "|---|---|---|---|---:|---:|---|---:|---|",
    ]
    for item in records:
        if item["seed"] == 42:
            fmt = lambda x: "N/A" if x is None else f"{x:.3f}"
            lines.append(
                f"| {item['problem_id']} | {item['arm']} | {item['n_input']}/{item['n_eligible']} | "
                f"{item['n_train']}/{item['n_holdout']} | {item['n_features']} | {item['n_clusters']} | "
                f"{item['train_cluster_sizes']} | {fmt(item['silhouette_train'])} | "
                f"{fmt(item['rule_holdout_fidelity'])} / {fmt(item['majority_holdout_fidelity'])} |"
            )
    lines += [
        "",
        "### Độ nhạy qua 3 seed",
        "",
        "Mean [min, max] là mô tả ba split, không phải confidence interval hoặc ba lớp độc lập.",
        "",
        "| Bài | Arm | Runs ok/total | Silhouette mean [min,max] | Holdout fidelity mean [min,max] |",
        "|---|---|---|---|---|",
    ]
    for problem in problems:
        for arm in MODES:
            subset = [r for r in records if r["problem_id"] == problem and r["arm"] == arm]
            values = []
            for metric in ("silhouette_train", "rule_holdout_fidelity"):
                samples = [r[metric] for r in subset if r[metric] is not None]
                values.append(
                    f"{np.mean(samples):.3f} [{min(samples):.3f}, {max(samples):.3f}]"
                    if samples
                    else "N/A"
                )
            lines.append(
                f"| {problem} | {arm} | {sum(r['status'] == 'ok' for r in subset)}/{len(subset)} | {' | '.join(values)} |"
            )
    lines += [
        "",
        "### Diễn giải",
        "",
        "Seed42: A và C cho cùng phân hoạch train/holdout cả ba bài; B tạo cụm train lớn kèm cụm nhỏ/singleton.",
        "Fidelity B seed42 bằng baseline majority cả ba bài (1,0; 1,0; 0,8), nên điểm cao không chứng minh chẩn đoán tốt.",
        "A/C khác phân hoạch ở 2825 seed7 và 2833 seed91; chưa có gold để xác định thay đổi nào hữu ích.",
        "Không kết luận structural/OAV tốt hơn. Giới hạn áp dụng cho feature presence và trọng số hiện tại.",
        "[Protocol, feature, metric và limitations](../../docs/itsp_validation.md).",
        "",
        (
            "[JSON đầy đủ](abc_summary.json) · [Assignments 17 mẫu](abc_review_assignments.json) · "
            "[Phân tích review](../../docs/itsp_expert_review.md) · [Điều kiện tính purity/agreement](expert_metric_readiness.json)"
        ),
        "",
        "Purity và agreement chuyên gia hiện là N/A: 17 mẫu vẫn chờ annotation; không dùng giả thuyết của trợ lý làm gold.",
        "Train partition ARI trong JSON chỉ đo mức giống nhau giữa phân hoạch; không phải inter-rater agreement.",
        "",
    ]
    text = "\n".join(lines)
    (output / "abc_summary.md").write_text(text, encoding="utf-8")
    # Preserve the previous experiment table while updating a bounded generated section.
    summary_path = output / "summary.md"
    start, end = "<!-- ABC_VALIDATION_START -->", "<!-- ABC_VALIDATION_END -->"
    previous = summary_path.read_text(encoding="utf-8")
    if start in previous:
        previous = previous.split(start)[0] + previous.split(end, 1)[1]
    summary_path.write_text(
        previous.rstrip() + "\n\n" + start + "\n" + text + end + "\n", encoding="utf-8"
    )
    print(
        f"Saved {len(records)} paired runs and {len(review_clusters)} unchanged review candidates"
    )


if __name__ == "__main__":
    main()

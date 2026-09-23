"""Small CPU ablation on audited public ITSP cohorts, without executing student code."""

import argparse
import json
import time
from collections import Counter
from pathlib import Path

from misconceptions.adapters import load_dataset
from misconceptions.cli import build_provenance
from misconceptions.features import extract_oav, route_submission
from misconceptions.pipeline import run_experiment


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False), encoding="utf-8"
    )


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=root / "data/itsp")
    parser.add_argument("--output", type=Path, default=root / "results/itsp")
    parser.add_argument(
        "--problems", nargs="*", help="Optional problem IDs; otherwise top 3 by size"
    )
    args = parser.parse_args()
    candidates, empty_cohorts = [], []
    for path in sorted(args.data.rglob("manifest.json")):
        if not path.with_name("submissions.jsonl").read_text(encoding="utf-8").strip():
            empty_cohorts.append(
                {"manifest": str(path), "reason": "no_imported_rows_see_data_audit"}
            )
            continue
        manifest, rows = load_dataset(path, path.with_name("submissions.jsonl"))
        eligible = [r for r in rows if route_submission(r, manifest["test_ids"]) == "eligible"]
        signatures = {tuple(r.outcomes[t] for t in manifest["test_ids"]) for r in eligible}
        candidates.append((len(eligible), len(signatures), path, manifest, rows))
    candidates.sort(key=lambda item: (-item[0], str(item[3]["problem_id"])))
    if args.problems:
        selected = [item for item in candidates if item[3]["problem_id"] in args.problems]
        if {item[3]["problem_id"] for item in selected} != set(args.problems):
            parser.error("Some requested problems were not found in prepared data")
    else:
        selected = [item for item in candidates if item[0] >= 12 and item[1] >= 3][:3]
    if not selected:
        parser.error("No cohorts with enough eligible rows and distinct outcome signatures")
    write_json(
        args.output / "selection.json",
        {
            "policy": "Top 3 by eligible count, >=12 eligible and >=3 outcome signatures; no metric tuning",
            "explicit_problem_override": args.problems,
            "empty_cohorts": empty_cohorts,
            "cohorts": [
                {
                    "problem_id": item[3]["problem_id"],
                    "eligible": item[0],
                    "signatures": item[1],
                    "selected": item in selected,
                }
                for item in candidates
            ],
        },
    )
    annotation_records = {}
    summaries, review = (
        [],
        [
            "# ITSP — hồ sơ duyệt cụm",
            "",
            "Cụm/luật là biểu hiện lỗi, chưa phải misconception đã được chuyên gia xác nhận.",
            "Báo cáo minh họa dùng agglomerative + cấu trúc, k=3, seed=42 định trước; không chọn theo holdout.",
            "ID sinh viên không có: split chỉ chống trùng source chính xác, chưa bảo đảm độc lập người học.",
            "Đọc kèm data/itsp audit và bản *_correct.c; không dùng bản sửa đúng làm feature.",
            "",
        ],
    )
    for eligible_count, signatures, manifest_path, manifest, rows in selected:
        problem = manifest["problem_id"]
        review_path = manifest_path.with_name("review.jsonl")
        evidence = {
            entry["submission_id"]: entry
            for entry in (
                json.loads(line)
                for line in review_path.read_text(encoding="utf-8").splitlines()
                if line.strip()
            )
        }
        provenance = build_provenance(
            manifest, manifest_path, manifest_path.with_name("submissions.jsonl")
        )
        configurations = [("exact", "outcomes", 2, 1.0)]
        configurations += [
            (method, mode, k, 0.8)
            for method in ("agglomerative", "kmeans")
            for mode in ("outcomes", "combined")
            for k in (2, 3, 4)
        ]
        # A fixed alternative weight checks sensitivity without selecting on holdout.
        configurations.append(("agglomerative", "combined", 3, 0.6))
        for method, mode, k, weight in configurations:
            for seed in (7, 42, 91):
                started = time.perf_counter()
                result = run_experiment(
                    rows,
                    test_ids=manifest["test_ids"],
                    method=method,
                    feature_mode=mode,
                    k=k,
                    seed=seed,
                    test_weight=weight,
                )
                result["provenance"] = provenance
                result["elapsed_seconds"] = time.perf_counter() - started
                filename = f"{method}_{mode}_k{k}_w{weight}_seed{seed}.json"
                write_json(args.output / problem / filename, result)
                explanation = result.get("explanation", {})
                assignments = result.get("train_assignments", {})
                summaries.append(
                    {
                        "problem_id": problem,
                        "method": method,
                        "mode": mode,
                        "k": k,
                        "test_weight": weight,
                        "seed": seed,
                        "status": result["status"],
                        "reason": result.get("reason"),
                        "eligible": eligible_count,
                        "outcome_signatures": signatures,
                        "n_clusters": result.get("n_clusters"),
                        "train_cluster_sizes": dict(Counter(assignments.values())),
                        "silhouette_train": result.get("silhouette_train"),
                        "holdout_fidelity": explanation.get("holdout_fidelity"),
                        "majority_fidelity": explanation.get("holdout_majority_baseline_fidelity"),
                        "holdout_ties": result.get("holdout_assignment_ties"),
                        "seconds": result["elapsed_seconds"],
                    }
                )
                if (method, mode, k, weight, seed) == ("agglomerative", "combined", 3, 0.8, 42):
                    review += [f"## Bài {problem}", "", f"Trạng thái: {result['status']}", ""]
                    lookup = {row.submission_id: row for row in rows}
                    selected_ids = set(result.get("medoids", {}).values())
                    # Add the farthest holdout member of each cluster as a contrast case.
                    distances = result.get("holdout_distance_to_medoid", {})
                    held_assignments = result.get("holdout_assignments", {})
                    for label in set(held_assignments.values()):
                        members = [sid for sid, value in held_assignments.items() if value == label]
                        selected_ids.add(max(members, key=lambda sid: (distances[sid], sid)))
                    for sid in sorted(selected_ids):
                        annotation_records[sid] = {
                            "submission_id": sid,
                            "problem_id": problem,
                            "raw_path": evidence[sid]["raw_path"],
                            "paired_correct_path": evidence[sid].get("paired_correct_path"),
                            "labels": [],
                            "status": "pending_expert_review",
                            "reviewer": None,
                            "evidence": None,
                            "confidence": None,
                        }
                    for cluster, sid in result.get("medoids", {}).items():
                        row = lookup[sid]
                        details = evidence[sid]
                        review += [
                            f"### Cụm {cluster} — bài đại diện {sid}",
                            "",
                            f"Nguồn: `{row.provenance}`",
                            "",
                            f"Bài gốc: `{details['raw_path']}`",
                            f"Bản sửa cùng cặp: `{details.get('paired_correct_path')}`",
                            f"Test nghi lỗi định dạng: `{details.get('formatting_suspected_test_ids', [])}`",
                            "",
                            "```json",
                            json.dumps(extract_oav(row), ensure_ascii=False, indent=2),
                            "```",
                            "",
                            "```c",
                            row.source_code,
                            "```",
                            "",
                            (
                                "Nhận xét chuyên gia: CHƯA GÁN NHÃN. Kiểm tra test, định dạng output, "
                                "runtime và bản sửa trước khi kết luận nguyên nhân."
                            ),
                            "",
                        ]
                    review += [
                        "### Luật mô tả cụm",
                        "",
                        "```json",
                        json.dumps(explanation, ensure_ascii=False, indent=2),
                        "```",
                        "",
                    ]
        print(f"Finished {problem}: {eligible_count} eligible", flush=True)
    write_json(
        args.output / "summary.json",
        {
            "warning": "Exploratory public-data analysis; no expert gold or verified student-disjoint holdout",
            "selection": "selection.json",
            "experiments": summaries,
        },
    )
    (args.output / "cluster_review.md").write_text("\n".join(review), encoding="utf-8")
    # A template, not annotations. Keep the filled copy separately so reruns cannot erase labels.
    (args.output / "annotation_template.jsonl").write_text(
        "".join(
            json.dumps(entry, ensure_ascii=False) + "\n"
            for _, entry in sorted(annotation_records.items())
        ),
        encoding="utf-8",
    )
    lines = [
        "# ITSP — kết quả thí nghiệm",
        "",
        "Không dùng silhouette hoặc fidelity để tuyên bố độ chính xác misconception.",
        "Mỗi dòng dưới đây là seed=42; JSON giữ toàn bộ seeds 7, 42, 91 và mọi lần abstain.",
        "Exact bỏ qua k; trọng số trong bảng là cấu hình. Outcomes-only luôn dành toàn bộ trọng số cho test.",
        "",
        "| Bài | Thuật toán | Feature | k | Trọng số test | Trạng thái | Silhouette train | Fidelity holdout | Majority |",
        "|---|---|---|---:|---:|---|---:|---:|---:|",
    ]
    for item in summaries:
        if item["seed"] != 42:
            continue
        metrics = [
            "—" if item[key] is None else f"{item[key]:.3f}"
            for key in ("silhouette_train", "holdout_fidelity", "majority_fidelity")
        ]
        lines.append(
            f"| {item['problem_id']} | {item['method']} | {item['mode']} | {item['k']} | "
            f"{item['test_weight']} | {item['status']} | {' | '.join(metrics)} |"
        )
    (args.output / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

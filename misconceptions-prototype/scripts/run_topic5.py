"""Locked validation ablations and teaching reports; never evaluates the sealed test partition."""

import argparse
import json
import time
from collections import Counter
from pathlib import Path
from zipfile import ZipFile

from misconceptions.cli import build_provenance
from misconceptions.pipeline import run_experiment
from misconceptions.research_io import digest, implementation_fingerprint, read_cohorts, write_json
from misconceptions.semantic_rules import build_teaching_report
from misconceptions.splits import validate_lock
from misconceptions.teaching_report import load_evidence

MODES = ("outcomes", "combined", "outcomes_stdout", "combined_stdout")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--split-lock", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--problems", nargs="+")
    parser.add_argument("--seeds", nargs="+", type=int, default=[7, 42, 91])
    parser.add_argument("--k", type=int, default=3)
    args = parser.parse_args()
    cohorts = read_cohorts(args.data)
    lock = json.loads(args.split_lock.read_text(encoding="utf-8"))
    validate_lock([row for _, _, rows in cohorts for row in rows], lock)
    if args.problems and set(args.problems) - {m["problem_id"] for _, m, _ in cohorts}:
        parser.error("Unknown requested problem")
    args.output.mkdir(parents=True, exist_ok=False)
    root = Path(__file__).resolve().parents[2]
    provenance = implementation_fingerprint(root)
    provenance["split_lock_sha256"] = digest(args.split_lock)
    provenance["split_policy"] = lock["policy"]
    provenance["seeds"] = args.seeds
    provenance["k"] = args.k
    provenance["problems"] = args.problems
    snapshot = args.output / "code_snapshot.zip"
    with ZipFile(snapshot, "w") as archive:
        for name, expected in provenance["files_sha256"].items():
            if digest(root / name) != expected:
                raise RuntimeError("Implementation changed while recording the run")
            archive.write(root / name, name)
    provenance["code_snapshot_sha256"] = digest(snapshot)
    write_json(args.output / "run_manifest.json", provenance)
    summaries = []
    markdown = ["# Đề 5 — ablation trên validation", "",
                "Log lịch sử; test partition chưa đánh giá. Chưa có nhãn cơ chế độc lập.", "",
                "Silhouette/fidelity mô tả hình học cụm và khả năng cây bắt chước cụm,",
                "không phải độ chính xác phát hiện quan niệm sai.", ""]
    for folder, manifest, rows in cohorts:
        problem = manifest["problem_id"]
        if args.problems and problem not in args.problems:
            continue
        logs = load_evidence(folder / "review.jsonl", rows)
        assignments = {row.submission_id: lock["assignments"][row.submission_id] for row in rows}
        # Even hand-authored diagnostic rules must not inspect sealed-test programs.
        visible_rows = [row for row in rows if assignments[row.submission_id] != "test"]
        visible_logs = {row.submission_id: logs.get(row.submission_id, []) for row in visible_rows}
        input_provenance = build_provenance(manifest, folder / "manifest.json",
                                            folder / "submissions.jsonl")
        input_provenance["evidence_sha256"] = digest(folder / "review.jsonl")
        configurations = [("exact", "outcomes")] + [
            (method, mode) for method in ("agglomerative", "kmeans") for mode in MODES]
        markdown += [f"## {problem}", ""]
        for method, mode in configurations:
            for seed in args.seeds:
                started = time.perf_counter()
                result = run_experiment(rows, test_ids=manifest["test_ids"], method=method,
                                        feature_mode=mode, k=args.k, seed=seed, logs=logs,
                                        split_assignments=assignments)
                result["elapsed_seconds"] = time.perf_counter() - started
                result["provenance"] = input_provenance
                result["run_manifest"] = "run_manifest.json"
                result["teaching"] = build_teaching_report(visible_rows, visible_logs, result)
                filename = f"{folder.name}/{method}_{mode}_seed{seed}.json"
                write_json(args.output / filename, result)
                summaries.append({"problem": problem, "method": method, "mode": mode,
                                  "seed": seed, "status": result["status"], "reason": result.get("reason"),
                                  "silhouette": result.get("silhouette_train"),
                                  "fidelity": result.get("explanation", {}).get("holdout_fidelity"),
                                  "artifact": filename})
                if seed == args.seeds[0]:
                    markdown += [f"### {method} / {mode}", "",
                                 f"Trạng thái: `{result['status']}`; {result.get('reason', '')}", ""]
                    cluster_sizes = Counter(result.get("train_assignments", {}).values())
                    markdown += [f"Quy mô cụm train: {dict(cluster_sizes)}.", ""]
                    for rule in result.get("explanation", {}).get("rules", []):
                        markdown.append(f"- IF {' AND '.join(rule['if'])} THEN cụm {rule['then_cluster']}; "
                                        f"train n={rule['train_support']}, validation n={rule['holdout_support']}, "
                                        f"precision={rule['holdout_precision']}.")
                    markdown += [""]
        teaching = result["teaching"]
        markdown += ["### Phản hồi giảng dạy từ luật có dẫn chứng", "",
                     f"{teaching['n_matched']}/{teaching['n_analyzed']} bài train/validation khớp luật.",
                     "Số bài khác số sinh viên; một người có thể nộp nhiều lần.", ""]
        for item in teaching["summaries"]:
            markdown += [f"- {item['then_vi']} ({item['n_submissions']} bài); cần người đánh giá."]
        if not teaching["summaries"]:
            markdown += ["Chưa có luật cơ chế chuyên biệt khớp; dùng medoid và test lỗi để rà soát."]
        markdown += ["", "Xem trường `teaching.findings` trong JSON để truy đến code và test cụ thể.", ""]
        print(f"Completed {problem}", flush=True)
    write_json(args.output / "summary.json", {"evaluation": "validation_only",
               "human_validated": False, "mechanism_accuracy": None, "runs": summaries})
    (args.output / "summary.md").write_text("\n".join(markdown), encoding="utf-8")
    print(f"Saved {len(summaries)} runs to {args.output}")


if __name__ == "__main__":
    main()

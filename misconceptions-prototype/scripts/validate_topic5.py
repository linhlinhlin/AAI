"""Summarize ablations, prepare blind teacher packets, or score returned human labels."""

import argparse
import json
from pathlib import Path

from misconceptions.ai_labeling import fingerprint
from misconceptions.benchmark_validation import load_runs, summarize_runs
from misconceptions.research_io import digest, implementation_fingerprint, read_cohorts, write_json
from misconceptions.splits import leakage_groups
from misconceptions.teacher_validation import adjudicated_labels, evaluate_report, forms
from misconceptions.teaching_report import load_evidence


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def prepare(run, data, output, max_per_partition):
    cohorts = read_cohorts(data)
    runs = load_runs(run)
    inventory = summarize_runs(run)["input_sha256"]
    rows = [r for _, _, members in cohorts for r in members]
    groups = {r.submission_id: int(g) for r, g in zip(rows, leakage_groups(rows))}
    cases, bindings = [], {}
    for folder, manifest, members in cohorts:
        candidates = [(item, report) for item, report in runs
                      if item["problem"] == manifest["problem_id"] and report["status"] == "ok"]
        if not candidates:
            continue
        selected = {"train": set(), "validation": set()}
        expected = {"input_sha256": digest(folder / "submissions.jsonl"),
                    "manifest_sha256": digest(folder / "manifest.json"),
                    "evidence_sha256": digest(folder / "review.jsonl")}
        for _, report in candidates:
            if any(report["provenance"][key] != value for key, value in expected.items()):
                raise ValueError("Run data/evidence differs from the annotation corpus")
            for partition, field in (("train", "train_assignments"), ("validation", "holdout_assignments")):
                ids = set(report[field])
                if selected[partition] and selected[partition] != ids:
                    raise ValueError("All variants must use identical eligible train/validation populations")
                selected[partition] = ids
        if selected["train"] & selected["validation"]:
            raise ValueError("Train and validation overlap")
        logs = load_evidence(folder / "review.jsonl", members)
        by_id = {r.submission_id: r for r in members}
        for partition, ids in selected.items():
            # Selection is deterministic, independent of clusters and mechanism hypotheses.
            for sid in sorted(ids, key=lambda value: fingerprint(value))[:max_per_partition]:
                row = by_id[sid]
                alias = "case_" + fingerprint([manifest["problem_id"], sid])[:16]
                cases.append({"case_id": alias, "problem_id": row.problem_id,
                              "language": row.language, "source_code": row.source_code,
                              "outcomes": row.outcomes, "logged_tests": logs.get(sid, []),
                              "problem_statement": manifest.get("specification"),
                              "evidence_kind": "recorded_logs_not_fresh_execution"})
                bindings[alias] = {"submission_id": sid, "problem_id": row.problem_id,
                                   "partition": partition, "independence_group": groups[sid],
                                   "student_identity_available": row.student_id is not None}
    if not cases:
        raise ValueError("No successful validation cohorts to annotate")
    evidence = {"schema_version": 1, "scope": "development_train_validation_only",
                "sampling": f"SHA256 order, at most {max_per_partition} per problem/partition; blind to arms",
                "cases": sorted(cases, key=lambda case: case["case_id"])}
    review, adjudication = forms(evidence)
    output.mkdir(parents=True, exist_ok=False)
    write_json(output / "evidence.json", evidence)
    write_json(output / "reviewer_1.json", review)
    write_json(output / "reviewer_2.json", review)
    write_json(output / "adjudication.json", adjudication)
    write_json(output / "coordinator.json", {"packet_id": fingerprint(evidence), "bindings": bindings,
               "run_sha256": inventory, "warning": "Do not send this mapping or run outputs to blind reviewers."})
    (output / "README.md").write_text(
        "# Gói đánh giá độc lập\n\nGửi evidence.json và một reviewer_N.json riêng cho mỗi giảng viên. "
        "Không gửi coordinator.json, kết quả cụm/luật hay gợi ý AI.\n\n"
        "Chốt cùng codebook (version, approved_by, labels) trước khi gán nhãn; hai người điền độc lập. "
        "Người thứ ba xử lý bất đồng trong adjudication.json, ghi coordinator_verified_by.\n\n"
        "status: pending / supported / uncertain / multiple / no_target_error. supported yêu cầu "
        "mechanism trong codebook, rationale, source_lines (từ 1), test_ids có trong evidence. "
        "Các trạng thái khác giữ mechanism=null. Không đủ dữ liệu thì ghi uncertain.\n\n"
        "cognitive_status mặc định unassessed. Chỉ supported/rejected khi có learner_explanation "
        "và follow_up_observation thật, được người điều phối xác minh; code sai đơn thuần không đủ. "
        "Public logs thường không có dữ liệu này. Không điền bằng AI.\n\n"
        "Nếu problem_statement=null, điều phối viên cần cung cấp đề gốc đã kiểm chứng riêng; "
        "không suy đoán đề từ lời giải mẫu. Giữ dữ liệu thật/nhãn giảng viên ngoài Git.\n",
        encoding="utf-8")
    return {"packet_id": fingerprint(evidence), "n_cases": len(cases), "status": "waiting_for_teachers"}


def evaluate(run, packet, review_paths, adjudication_path):
    evidence, index = read(packet / "evidence.json"), read(packet / "coordinator.json")
    if index["packet_id"] != fingerprint(evidence):
        raise ValueError("Evidence packet was modified")
    for name, expected in index["run_sha256"].items():
        path = (run / name).resolve()
        if not path.is_relative_to(run.resolve()) or digest(path) != expected:
            raise ValueError("Run changed after the blind packet was frozen")
    reviews, adjudication = [read(p) for p in review_paths], read(adjudication_path)
    labels, cognitive, audit = adjudicated_labels(evidence, reviews, adjudication)
    bindings = index["bindings"]
    if set(bindings) != {c["case_id"] for c in evidence["cases"]}:
        raise ValueError("Coordinator bindings do not match evidence")
    for case in evidence["cases"]:
        binding = bindings[case["case_id"]]
        expected_alias = "case_" + fingerprint([case["problem_id"], binding["submission_id"]])[:16]
        if case["case_id"] != expected_alias or binding["problem_id"] != case["problem_id"]:
            raise ValueError("Coordinator changed a case-to-submission binding")
    external = {bindings[c]["submission_id"]: label for c, label in labels.items()}
    cognitive_labels = {bindings[c]["submission_id"]: label for c, label in cognitive.items()}
    results = []
    for item, report in load_runs(run):
        results.append({"artifact": item["artifact"], "problem": item["problem"],
                        "method": item["method"], "mode": item["mode"], "seed": item["seed"],
                        "mechanism_evaluation": evaluate_report(report, external),
                        "cognitive_evaluation": evaluate_report(report, cognitive_labels)})
    return {"schema_version": 1, "packet_id": index["packet_id"],
            "status": "scored_selected_human_sample" if labels else "waiting_for_teacher_labels",
            "misconception_validated": bool(cognitive), "annotation_audit": audit,
            "limitations": ["Selected development sample; not sealed-test generalization.",
                            "Metrics condition on adjudicated single-primary labels; report coverage.",
                            "Identity and cognitive evidence attestations require coordinator verification.",
                            "No confidence intervals or superiority claims from these descriptive scores."],
            "input_sha256": {str(p): digest(p) for p in
                             [packet / "evidence.json", packet / "coordinator.json",
                              *review_paths, adjudication_path]}, "runs": results}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for command in ("summarize", "prepare", "evaluate"):
        child = sub.add_parser(command)
        child.add_argument("--run", type=Path, required=True)
        child.add_argument("--output", type=Path, required=True)
        if command == "prepare":
            child.add_argument("--data", type=Path, required=True)
            child.add_argument("--max-per-partition", type=int, default=20)
        if command == "evaluate":
            child.add_argument("--packet", type=Path, required=True)
            child.add_argument("--reviews", type=Path, nargs="+", required=True)
            child.add_argument("--adjudication", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("Output already exists; use a new versioned path")
    if args.command == "prepare":
        if args.max_per_partition < 1:
            parser.error("max-per-partition must be positive")
        result = prepare(args.run, args.data, args.output, args.max_per_partition)
    else:
        result = (summarize_runs(args.run) if args.command == "summarize" else
                  evaluate(args.run, args.packet, args.reviews, args.adjudication))
        result["implementation"] = implementation_fingerprint(Path(__file__).resolve().parents[2])
        write_json(args.output, result)
    print(json.dumps({k: result[k] for k in ("status", "n_runs", "n_cases", "packet_id") if k in result}))


if __name__ == "__main__":
    main()

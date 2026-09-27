"""Verify a completed topic-5 run against its dataset, split and archived implementation."""

import argparse
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile

from misconceptions.research_io import digest, read_cohorts
from misconceptions.splits import validate_lock


def audit(data, run, split_path):
    cohorts = read_cohorts(data)
    lock = json.loads(split_path.read_text(encoding="utf-8"))
    validate_lock([row for _, _, rows in cohorts for row in rows], lock)
    manifest = json.loads((run / "run_manifest.json").read_text(encoding="utf-8"))
    if manifest["split_lock_sha256"] != digest(split_path):
        raise ValueError("Run refers to a different split lock")
    if manifest["code_snapshot_sha256"] != digest(run / "code_snapshot.zip"):
        raise ValueError("Code snapshot checksum mismatch")
    with ZipFile(run / "code_snapshot.zip") as archive:
        for name, expected in manifest["files_sha256"].items():
            if hashlib.sha256(archive.read(name)).hexdigest() != expected:
                raise ValueError(f"Archived implementation mismatch: {name}")
    inputs = {}
    for folder, description, _ in cohorts:
        inputs[description["problem_id"]] = {
            "manifest_sha256": digest(folder / "manifest.json"),
            "input_sha256": digest(folder / "submissions.jsonl"),
            "evidence_sha256": digest(folder / "review.jsonl"),
        }
    summary = json.loads((run / "summary.json").read_text(encoding="utf-8"))
    if summary.get("evaluation") != "validation_only" or summary.get("human_validated") is not False:
        raise ValueError("Unexpected evaluation or validation claim")
    if summary.get("mechanism_accuracy") is not None:
        raise ValueError("This unlabeled run cannot claim mechanism accuracy")
    configurations = {("exact", "outcomes")} | {
        (method, mode) for method in ("agglomerative", "kmeans")
        for mode in ("outcomes", "combined", "outcomes_stdout", "combined_stdout")}
    problems = manifest["problems"] or list(inputs)
    expected_runs = {(p, method, mode, seed) for p in problems
                     for method, mode in configurations for seed in manifest["seeds"]}
    observed, counts, report_files = set(), {"ok": 0, "abstained": 0}, {}
    for item in summary["runs"]:
        identity = (item["problem"], item["method"], item["mode"], item["seed"])
        if identity in observed:
            raise ValueError("Duplicate run in summary")
        observed.add(identity)
        path = (run / item["artifact"]).resolve()
        if not path.is_relative_to(run.resolve()):
            raise ValueError("Report path escapes run directory")
        result = json.loads(path.read_text(encoding="utf-8"))
        for field, expected in inputs[item["problem"]].items():
            if result["provenance"][field] != expected:
                raise ValueError(f"Input hash mismatch in {item['artifact']}: {field}")
        if (result["method"], result["feature_mode"], result["seed"], result["status"]) != (
            item["method"], item["mode"], item["seed"], item["status"]
        ):
            raise ValueError("Summary does not match detailed result")
        counts[result["status"]] += 1
        if result["status"] == "ok":
            train, validation = result["train_assignments"], result["holdout_assignments"]
            for assignments, partition in ((train, "train"), (validation, "validation")):
                if any(lock["assignments"][sid] != partition for sid in assignments):
                    raise ValueError("Report contains a row outside its declared split")
            if set(result["oav"]) != set(train) | set(validation):
                raise ValueError("OAV membership differs from fitted/evaluated rows")
            if any(sid not in train or train[sid] != int(label)
                   for label, sid in result["medoids"].items()):
                raise ValueError("Medoid is not a member of its training cluster")
            rules = result["explanation"]["rules"]
            if sum(r["train_support"] for r in rules) != len(train) or sum(
                r["holdout_support"] for r in rules
            ) != len(validation):
                raise ValueError("IF-THEN rule supports do not cover the reported split")
        elif not result.get("reason"):
            raise ValueError("Abstention has no reason")
        if result["teaching"]["human_validated"] is not False:
            raise ValueError("Teaching hypotheses cannot be marked human-validated by this runner")
        if any(lock["assignments"][finding["submission_id"]] == "test"
               for finding in result["teaching"]["findings"]):
            raise ValueError("Teaching report exposes sealed-test findings")
        report_files[item["artifact"]] = digest(path)
    if observed != expected_runs:
        raise ValueError("Missing or unexpected configurations")
    return {"status": "passed", "checks": "input_and_snapshot_hashes_split_membership_rules_coverage",
            "auditor_sha256": digest(Path(__file__)),
            "counts": counts, "split_sha256": digest(split_path),
            "run_manifest_sha256": digest(run / "run_manifest.json"),
            "reports_sha256": report_files,
            "scope": "artifact integrity; does not establish scientific accuracy"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--run", type=Path, required=True)
    parser.add_argument("--split-lock", type=Path, required=True)
    args = parser.parse_args()
    result = audit(args.data, args.run, args.split_lock)
    (args.run / "integrity_audit.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "reports_sha256"}))


if __name__ == "__main__":
    main()

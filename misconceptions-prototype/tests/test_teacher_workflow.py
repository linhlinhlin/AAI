"""End-to-end packet intake with authored labels, never reported as expert gold."""

import json
import runpy
from pathlib import Path

import pytest

from misconceptions.domain import Submission
from misconceptions.research_io import digest, write_json


def test_packet_prepare_evaluate_and_tampering(tmp_path, monkeypatch):
    module = runpy.run_path(str(Path(__file__).resolve().parents[1] / "scripts/validate_topic5.py"))
    prepare, evaluate = module["prepare"], module["evaluate"]
    folder = tmp_path / "data/cohorts/fixture"
    for name in ("manifest.json", "submissions.jsonl", "review.jsonl"):
        write_json(folder / name, {})
    rows = [Submission(sid, sid, "fixture", "c", f"int main(){{return {i};}}", "v1", {"t1": "fail"}, "authored")
            for i, sid in enumerate(("a", "b", "c", "x", "y"))]
    monkeypatch.setitem(prepare.__globals__, "read_cohorts", lambda _: [(folder, {"problem_id": "fixture"}, rows)])
    monkeypatch.setitem(prepare.__globals__, "load_evidence", lambda *_: {
        row.submission_id: [{"test_id": "t1", "input": "1", "expected": "2", "output": "0"}] for row in rows})
    run = tmp_path / "run"
    report = {"status": "ok", "split": {"evaluation_partition": "validation", "holdout_ids": ["x", "y"]},
              "train_assignments": {"a": 0, "b": 0, "c": 1}, "holdout_assignments": {"x": 0, "y": 1},
              "holdout_assignment_ties": 0, "silhouette_train": .5,
              "explanation": {"holdout_fidelity": 1, "holdout_majority_baseline_fidelity": .5,
                              "holdout_leaf_ids": [1, 2], "rules": [
                                  {"rule_id": 1, "if": ["test:t1=fail"], "then_cluster": 0, "holdout_support": 1},
                                  {"rule_id": 2, "if": ["NOT (test:t1=fail)"], "then_cluster": 1, "holdout_support": 1}]},
              "provenance": {"manifest_sha256": digest(folder / "manifest.json"),
                             "input_sha256": digest(folder / "submissions.jsonl"),
                             "evidence_sha256": digest(folder / "review.jsonl")}}
    write_json(run / "report.json", report)
    write_json(run / "run_manifest.json", {})
    write_json(run / "summary.json", {"evaluation": "validation_only", "runs": [
        {"artifact": "report.json", "problem": "fixture", "method": "kmeans", "mode": "outcomes", "seed": 42}]})
    packet = tmp_path / "packet"
    assert prepare(run, tmp_path / "data", packet, 20)["n_cases"] == 5
    evidence = json.loads((packet / "evidence.json").read_text())
    assert "train_assignments" not in json.dumps(evidence) and "student_id" not in json.dumps(evidence)
    review_paths = [packet / "reviewer_1.json", packet / "reviewer_2.json"]
    final_path = packet / "adjudication.json"
    result = evaluate(run, packet, review_paths, final_path)
    assert result["status"] == "waiting_for_teacher_labels"
    assert result["runs"][0]["mechanism_evaluation"]["clustering"]["ari"] is None
    for number, path in enumerate([*review_paths, final_path]):
        form = json.loads(path.read_text())
        form["reviewer_id"] = f"fixture-human-{number}"
        form["codebook"] = {"version": "fixture-v1", "approved_by": "fixture-coordinator",
                            "labels": ["fixture-mechanism"], "label_policy": "single_primary"}
        if path == final_path:
            form["coordinator_verified_by"] = "fixture-coordinator"
        for rating in form["ratings"]:
            rating.update(status="supported", mechanism="fixture-mechanism", rationale="Authored test only",
                          source_lines=[1], test_ids=["t1"])
        write_json(path, form)
    result = evaluate(run, packet, review_paths, final_path)
    assert result["annotation_audit"]["n_supported_mechanisms"] == 5
    assert not result["misconception_validated"]
    assert [r["mechanism_precision"] for r in result["runs"][0]["mechanism_evaluation"]["rules"]] == [1, 1]
    write_json(run / "report.json", report | {"silhouette_train": .9})
    with pytest.raises(ValueError, match="Run changed"):
        evaluate(run, packet, review_paths, final_path)

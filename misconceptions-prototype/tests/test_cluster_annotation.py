"""Authored fixtures for offline AI packets, never teacher/gold annotations."""

import json
from copy import deepcopy
from dataclasses import asdict, replace

import pytest

from misconceptions.ai_labeling import fingerprint
from misconceptions.cluster_annotation import (
    cluster_record,
    export_packet,
    problem_statement,
    render_cluster,
    response_schema,
    validate_response,
)
from misconceptions.cluster_annotation import (
    test_statistics as compute_test_statistics,
)
from misconceptions.domain import Submission
from misconceptions.research_io import digest, write_json
from misconceptions.splits import create_lock


@pytest.fixture
def corpus():
    rows = [Submission(f"private-id-{i}", f"private-student-{i}", "fixture", "c",
                       '#include <stdio.h>\nint main(){int n;scanf("%d",&n);'
                       f'printf("{i}");return 0;}}', "fixture-suite",
                       {"t1": "fail", "t2": "fail", "t3": "not_run"}, "authored fixture")
            for i in range(4)]
    report = {"status": "ok", "method": "kmeans", "feature_mode": "combined_stdout", "seed": 42,
              "train_assignments": {r.submission_id: 0 for r in rows[:3]},
              "holdout_assignments": {rows[3].submission_id: 0},
              "medoids": {"0": rows[0].submission_id},
              "oav": {r.submission_id: {"test:t1": "fail", "ast:c_return": "1"} for r in rows},
              "features": [{"name": "test:t1", "weight": 1.0}],
              "explanation": {"rules": [{"rule_id": 0, "if": ["test:t1=fail"], "then_cluster": 0,
                                         "train_support": 3, "train_precision": 1,
                                         "holdout_support": 1, "holdout_precision": 1}]}}
    logs = {r.submission_id: [{"test_id": "t1", "input": "9", "expected": "45", "output": str(i)},
                             {"test_id": "t2", "input": "10", "expected": "55", "output": str(i)}]
            for i, r in enumerate(rows)}
    manifest = {"schema_version": 2, "dataset_name": "Authored fixture", "provenance": "fixture",
                "problem_id": "fixture", "language": "c", "suite_version": "fixture-suite",
                "test_ids": ["t1", "t2", "t3"], "specification": "Print sum from 1 to n."}
    return report, manifest, rows, logs


def record(corpus):
    report, manifest, rows, logs = corpus
    result, excluded = cluster_record(report, manifest, rows, logs, 0, {"text": "Sum 1..n"})
    assert excluded is None
    return result


def packet_and_response(corpus):
    cluster = record(corpus)
    packet = {"clusters": [cluster], "annotation_status": "pending_annotation"}
    packet["packet_id"] = fingerprint(packet)
    response = {"packet_id": packet["packet_id"], "annotation_source": "ai", "reviews": [{
        "cluster_id": cluster["cluster_id"], "misconception_label": "In hằng số",
        "evidence_supported": True, "confidence": 0.8, "reasoning": "Authored test reasoning",
        "alternative_explanations": ["Placeholder code, not a cognitive belief"],
        "decision": "supported", "notes": "Fixture only",
        "evidence_refs": ["members/sample_001/raw_code", "members/sample_001/tests/t1"]}]}
    return packet, response


def test_packet_preserves_all_code_logs_rules_and_pending_without_private_ids(corpus):
    cluster = record(corpus)
    report, _, rows, logs = corpus
    assert cluster["annotation_status"] == "pending_annotation"
    assert cluster["human_validated"] is False
    assert cluster["n_submissions"] == 4
    assert cluster["learned_if_then_rules"] == report["explanation"]["rules"]
    assert "In hằng số" in cluster["candidate_misconception"]["misconception_name"]
    assert len(cluster["representative_sample_ids"]) == 4
    assert cluster["representative_sample_ids"][0] == "sample_001"
    for member, row in zip(cluster["members"], rows):
        assert member["raw_code"] == row.source_code
        assert member["logged_tests"] == logs[row.submission_id]
    serialized = json.dumps(cluster)
    assert "private-id" not in serialized and "private-student" not in serialized
    assert "gold_label" not in serialized
    markdown = render_cluster(cluster, "fixture-packet")
    assert all(row.source_code in markdown for row in rows)


def test_missing_test_is_never_a_pass(corpus):
    rows = corpus[2]
    rows[0] = replace(rows[0], outcomes={"t1": "not_run"})
    stats = {r["test_id"]: r for r in compute_test_statistics(rows, ["t1", "t3"])}
    assert stats["t1"]["n_observed"] == 3
    assert stats["t1"]["failure_rate_observed"] == 1
    assert stats["t1"]["failure_rate_cluster"] == 0.75
    assert stats["t3"]["failure_rate_observed"] is None
    assert stats["t3"]["outcome_counts"] == {"not_run": 4}


@pytest.mark.parametrize("problem,expected", [
    ("small", "cluster_too_small"), ("duplicate", "fewer_than_3_distinct_sources"),
    ("source", "missing_source_or_failed_test_logs"),
    ("logs", "missing_source_or_failed_test_logs"),
    ("no_common", "no_failed_test_shared_by_half_the_cluster"),
])
def test_insufficient_evidence_is_excluded(corpus, problem, expected):
    report, manifest, rows, logs = corpus
    if problem == "small":
        rows.pop()
    elif problem == "duplicate":
        rows[:] = [replace(row, source_code=rows[0].source_code) for row in rows]
    elif problem == "source":
        rows[0] = replace(rows[0], source_code="")
    elif problem == "logs":
        logs[rows[0].submission_id].pop()
    else:
        rows[:] = [replace(row, outcomes={f"t{i}": "fail"}) for i, row in enumerate(rows)]
        manifest["test_ids"] = [f"t{i}" for i in range(4)]
    cluster, exclusion = cluster_record(report, manifest, rows, logs, 0, {"text": "fixture"})
    assert cluster is None and expected in exclusion["reasons"]


def test_reference_solution_is_not_exported_as_problem_statement(tmp_path):
    path = tmp_path / "misconceptions-prototype/data/raw/itsp/dataset/Lab-3/2812/Main.c"
    path.parent.mkdir(parents=True)
    path.write_text("/* Exact task statement. */\nint reference_solution(){return 42;}", encoding="utf-8")
    result = problem_statement({"dataset_name": "ITSP public prototype", "lab": "Lab-3",
                                "problem_id": "2812"}, tmp_path)
    assert result["text"] == "Exact task statement."
    assert "reference_solution" not in json.dumps(result)


def test_ai_review_is_separate_and_never_becomes_gold(corpus):
    packet, response = packet_and_response(corpus)
    original = deepcopy(packet)
    result = validate_response(packet, response, require_complete=True)
    assert result["status"] == "ai_reviewed_pending_human_validation"
    assert result["mechanism_accuracy"] is None and result["human_validated"] is False
    assert packet == original
    assert set(response_schema()["properties"]["reviews"]["items"]["required"]) == set(response["reviews"][0])


@pytest.mark.parametrize("field,value", [
    ("cluster_id", "invented"), ("confidence", True), ("confidence", float("nan")),
    ("confidence", 1.1), ("evidence_supported", False), ("decision", "approved"),
    ("misconception_label", None), ("reasoning", " "), ("notes", None),
    ("alternative_explanations", "none"), ("evidence_refs", ["invented"]),
    ("evidence_refs", []), ("gold_label", "bad"),
])
def test_reject_invalid_ai_reviews(corpus, field, value):
    packet, response = packet_and_response(corpus)
    response["reviews"][0][field] = value
    with pytest.raises((ValueError, TypeError)):
        validate_response(packet, response)


def test_uncertain_null_label_partial_review_and_hash_guards(corpus):
    packet, response = packet_and_response(corpus)
    other = deepcopy(packet["clusters"][0])
    other["cluster_id"] = "other-cluster"
    packet["clusters"].append(other)
    packet["packet_id"] = fingerprint({k: v for k, v in packet.items() if k != "packet_id"})
    response["packet_id"] = packet["packet_id"]
    response["reviews"][0].update(decision="uncertain", evidence_supported=False, misconception_label=None)
    assert validate_response(packet, response)["missing_cluster_ids"] == ["other-cluster"]
    with pytest.raises(ValueError, match="Missing 1"):
        validate_response(packet, response, require_complete=True)
    duplicate = deepcopy(response)
    duplicate["reviews"] *= 2
    with pytest.raises(ValueError, match="duplicate"):
        validate_response(packet, duplicate)
    packet["clusters"][0]["n_submissions"] = 99
    with pytest.raises(ValueError, match="fingerprint"):
        validate_response(packet, response)


def audited_fixture(tmp_path, corpus):
    report, manifest, rows, logs = corpus
    # Larger authored corpus exercises real corpus lock validation, including sealed test IDs.
    rows = [replace(rows[i % 4], submission_id=f"fixture-{i}", student_id=f"learner-{i}",
                    source_code=rows[i % 4].source_code + f"\n/* authored variant {i} */")
            for i in range(30)]
    logs = {r.submission_id: logs[corpus[2][i % 4].submission_id] for i, r in enumerate(rows)}
    folder = tmp_path / "data/cohorts/fixture"
    write_json(folder / "manifest.json", manifest)
    (folder / "submissions.jsonl").write_text(
        "\n".join(json.dumps(asdict(r)) for r in rows), encoding="utf-8")
    (folder / "review.jsonl").write_text("\n".join(json.dumps({"submission_id": sid,
        "logged_tests": tests}) for sid, tests in logs.items()), encoding="utf-8")
    lock = create_lock(rows)
    split_path = tmp_path / "split.json"
    write_json(split_path, lock)
    report["train_assignments"] = {sid: 0 for sid, p in lock["assignments"].items() if p == "train"}
    report["holdout_assignments"] = {sid: 0 for sid, p in lock["assignments"].items() if p == "validation"}
    report["oav"] = {r.submission_id: {"test:t1": "fail"} for r in rows}
    report["medoids"] = {"0": next(iter(report["train_assignments"]))}
    report["split"] = {"evaluation_partition": "validation"}
    report["provenance"] = {key: digest(folder / name) for key, name in (
        ("input_sha256", "submissions.jsonl"), ("manifest_sha256", "manifest.json"),
        ("evidence_sha256", "review.jsonl"))}
    run = tmp_path / "run"
    artifact = "fixture/kmeans_combined_stdout_seed42.json"
    write_json(run / artifact, report)
    write_json(run / "summary.json", {"evaluation": "validation_only", "runs": [{
        "problem": "fixture", "method": "kmeans", "mode": "combined_stdout", "seed": 42,
        "artifact": artifact}]})
    (run / "code_snapshot.zip").write_bytes(b"fixture snapshot")
    write_json(run / "run_manifest.json", {"split_lock_sha256": digest(split_path),
               "code_snapshot_sha256": digest(run / "code_snapshot.zip")})
    write_json(run / "integrity_audit.json", {"status": "passed", "split_sha256": digest(split_path),
        "run_manifest_sha256": digest(run / "run_manifest.json"),
        "reports_sha256": {artifact: digest(run / artifact)}})
    return run, tmp_path / "data", split_path, lock, report


def test_export_end_to_end_preserves_sealed_partition_and_existing_outputs(tmp_path, corpus):
    run, data, split, lock, _ = audited_fixture(tmp_path, corpus)
    output = tmp_path / "packet"
    packet = export_packet(run, data, split, output, tmp_path)
    cluster = packet["clusters"][0]
    assert cluster["n_submissions"] == sum(p != "test" for p in lock["assignments"].values())
    assert all(m["partition"] != "test" for m in cluster["members"])
    assert len(cluster["representative_sample_ids"]) == 4
    assert (output / "response.schema.json").exists()
    assert json.loads((output / "response.template.json").read_text(encoding="utf-8"))[
        "pending_clusters"][0]["result"] is None
    with pytest.raises(ValueError, match="already exists"):
        export_packet(run, data, split, output, tmp_path)
    # Even re-audited data cannot place a test member into a development packet.
    artifact = "fixture/kmeans_combined_stdout_seed42.json"
    report = json.loads((run / artifact).read_text(encoding="utf-8"))
    test_id = next(sid for sid, p in lock["assignments"].items() if p == "test")
    report["holdout_assignments"][test_id] = 0
    write_json(run / artifact, report)
    with pytest.raises(ValueError, match="hash differs"):
        export_packet(run, data, split, tmp_path / "bad", tmp_path)
    audit = json.loads((run / "integrity_audit.json").read_text(encoding="utf-8"))
    audit["reports_sha256"][artifact] = digest(run / artifact)
    write_json(run / "integrity_audit.json", audit)
    with pytest.raises(ValueError, match="locked split"):
        export_packet(run, data, split, tmp_path / "bad", tmp_path)

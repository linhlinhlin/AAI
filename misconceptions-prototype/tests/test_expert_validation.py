import copy
import json
from pathlib import Path

import pytest

from misconceptions.expert_validation import agreement, score_annotation_sources, score_annotations


def test_ai_reviews_are_separate_from_human_validation():
    document, rows = fixture()
    document["codebook"]["approved_by"] = None
    before = copy.deepcopy(document)
    for sample, kind in zip(document["samples"], ["x", "x", "y", "y"]):
        complete(sample["reviews"][0], kind=kind, reviewer="ai:codex:test")
    rated = copy.deepcopy(document)
    result = score_annotation_sources(document, rows)
    assert document == rated
    assert result["n_completed_records"] == result["n_adjudicated"] == 0
    assert result["cluster_purity"] is result["agreement"] is None
    assert result["status"] == "waiting_for_human_expert_annotation"
    ai = result["ai_annotation"][0]
    assert ai["n_completed"] == 4
    assert ai["raw_agreement"] is ai["cohen_kappa"] is None
    assert ai["cluster_purity"] is None
    assert "purity_details" not in ai
    assert document["codebook"] == before["codebook"]
    complete(document["samples"][2]["reviews"][0], "No", None, "ai:codex:test")
    ai = score_annotation_sources(document, rows)["ai_annotation"][0]
    assert ai["decision_counts"] == {"Yes": 3, "No": 1}
    assert ai["cluster_purity"] is None


def test_ai_cannot_form_human_agreement_or_approve_human_codebook():
    document, rows = fixture()
    for sample in document["samples"]:
        human = sample["reviews"][0]
        complete(human, reviewer="human")
        human["independent_blind_review"] = True
        ai = copy.deepcopy(human)
        ai["reviewer_id"] = "ai:codex:test"
        sample["reviews"].append(ai)
        complete(sample["adjudication"], reviewer="ai:codex:test")
    document["codebook"]["approved_by"] = "ai:codex:test"
    result = score_annotation_sources(document, rows)
    assert result["n_completed_records"] == 4
    assert result["n_adjudicated"] == 0
    assert result["codebook_ready"] is False
    assert result["cluster_purity"] is result["agreement"] is None


def test_human_codebook_does_not_relabel_ai_reference_types():
    document, rows = fixture()
    sample = document["samples"][0]
    complete(sample["reviews"][0], kind="historical_ai_type", reviewer="ai:codex:test")
    complete(sample["adjudication"], kind="x", reviewer="human")
    result = score_annotation_sources(document, rows)
    assert result["purity_details"][0]["n_typed_adjudicated_yes"] == 1
    assert result["ai_annotation"][0]["cluster_purity"] is None


def fixture():
    rows = [
        {
            "submission_id": str(i),
            "problem_id": "p",
            "clusters_seed42": dict.fromkeys("ABC", 0 if i < 3 else 1),
        }
        for i in range(4)
    ]
    blank = {
        "status": "pending",
        "reviewer_id": None,
        "misconception": None,
        "misconception_type": None,
        "confidence": None,
        "evidence": None,
    }
    document = {
        "schema_version": 1,
        "codebook": {
            "approved_by": "expert",
            "version": "1",
            "label_policy": "single_primary",
            "misconception_types": ["x", "y"],
        },
        "samples": [],
    }
    for row in rows:
        review = dict(
            blank, independent_blind_review=False, same_cause_as_cluster=dict.fromkeys("ABC")
        )
        document["samples"].append(
            {
                "submission_id": row["submission_id"],
                "problem_id": "p",
                "reviews": [review],
                "adjudication": copy.deepcopy(blank),
            }
        )
    return document, rows


def complete(rating, decision="Yes", kind="x", reviewer="human"):
    rating.update(
        status="complete",
        reviewer_id=reviewer,
        misconception=decision,
        misconception_type=kind,
        confidence=4,
        evidence="synthetic test evidence",
    )


def test_empty_template_has_no_invented_labels():
    document, rows = fixture()
    result = score_annotations(document, rows)
    assert result["n_candidates"] == 4
    assert result["cluster_purity"] is result["agreement"] is None
    assert result["status"] == "waiting_for_annotation"
    assert result["n_completed_records"] == result["n_adjudicated"] == 0


def test_purity_known_value_and_positive_only_denominator():
    document, rows = fixture()
    for sample, kind in zip(document["samples"], ["x", "x", "y", "y"]):
        complete(sample["adjudication"], kind=kind)
    result = score_annotations(document, rows)
    assert all(r["cluster_purity"] == 0.75 for r in result["purity_details"])
    complete(document["samples"][2]["adjudication"], decision="No", kind=None)
    result = score_annotations(document, rows)["purity_details"][0]
    assert result["cluster_purity"] == 1
    assert result["n_typed_adjudicated_yes"] == 3
    assert result["type_coverage_of_candidates"] == 0.75
    assert result["decision_counts"] == {"Yes": 3, "No": 1}


def test_unapproved_codebook_blocks_type_purity():
    document, rows = fixture()
    complete(document["samples"][0]["adjudication"])
    document["codebook"]["approved_by"] = None
    assert score_annotations(document, rows)["cluster_purity"] is None


def test_agreement_known_and_degenerate_cases():
    result = agreement(["Yes", "Yes", "No", "No"], ["Yes", "No", "Yes", "No"])
    assert result["raw_agreement"] == 0.5
    assert result["cohen_kappa"] == 0
    assert agreement([], [])["raw_agreement"] is None
    assert agreement(["Yes"], ["Yes"])["cohen_kappa"] is None
    with pytest.raises(ValueError):
        agreement(["Yes"], [])


def test_independent_pairs_and_optional_cluster_ratings():
    document, rows = fixture()
    for sample in document["samples"]:
        first = sample["reviews"][0]
        complete(first, reviewer="one")
        first["independent_blind_review"] = True
        second = copy.deepcopy(first)
        second["reviewer_id"] = "two"
        sample["reviews"].append(second)
    result = score_annotations(document, rows)["agreement"][0]
    assert result["misconception_decision"]["n_paired"] == 4
    assert result["misconception_type_both_yes"]["raw_agreement"] == 1
    assert result["same_cause_as_cluster"]["A"]["raw_agreement"] is None
    for sample in document["samples"]:
        sample["reviews"][1]["independent_blind_review"] = False
    assert score_annotations(document, rows)["agreement"] is None


@pytest.mark.parametrize(
    "field,value",
    [
        ("confidence", True),
        ("confidence", 6),
        ("misconception", "unknown"),
        ("misconception_type", "absent"),
        ("evidence", ""),
    ],
)
def test_invalid_complete_rating_rejected(field, value):
    document, rows = fixture()
    rating = document["samples"][0]["reviews"][0]
    complete(rating)
    rating[field] = value
    with pytest.raises(ValueError):
        score_annotations(document, rows)


def test_duplicate_reviewer_and_missing_candidate_rejected():
    document, rows = fixture()
    complete(document["samples"][0]["reviews"][0])
    document["samples"][0]["reviews"].append(copy.deepcopy(document["samples"][0]["reviews"][0]))
    with pytest.raises(ValueError):
        score_annotations(document, rows)
    document, rows = fixture()
    document["samples"].pop()
    with pytest.raises(ValueError):
        score_annotations(document, rows)


def test_pending_fields_not_scored_and_problems_not_merged():
    document, rows = fixture()
    document["samples"][0]["adjudication"]["misconception"] = "Yes"
    assert score_annotations(document, rows)["cluster_purity"] is None
    for sample, row, kind in zip(document["samples"], rows, ["x", "x", "y", "y"]):
        complete(sample["adjudication"], kind=kind)
        sample["problem_id"] = row["problem_id"] = "p" if kind == "x" else "q"
    result = score_annotations(document, rows)
    assert len(result["purity_details"]) == 6
    assert all(r["cluster_purity"] == 1 for r in result["purity_details"])


def test_cli_provenance_and_input_protection(tmp_path):
    import hashlib
    import subprocess
    import sys

    root = Path(__file__).resolve().parents[1]
    document, rows = fixture()
    assignments = tmp_path / "assignments.json"
    annotations = tmp_path / "annotations.json"
    output = tmp_path / "metrics.json"
    assignments.write_text(json.dumps(rows), encoding="utf-8")
    document["assignments_sha256"] = hashlib.sha256(assignments.read_bytes()).hexdigest()
    annotations.write_text(json.dumps(document), encoding="utf-8")
    before = annotations.read_bytes()
    command = [
        sys.executable,
        str(root / "scripts/score_itsp_experts.py"),
        "--annotations",
        str(annotations),
        "--assignments",
        str(assignments),
    ]
    validated = subprocess.run(
        command + ["--validate-only", "--output", str(output)], capture_output=True, check=False
    )
    assert validated.returncode == 0, validated.stderr
    assert not output.exists()
    assert annotations.read_bytes() == before
    success = subprocess.run(command + ["--output", str(output)], capture_output=True, check=False)
    assert success.returncode == 0, success.stderr
    assert json.loads(output.read_text())["cluster_purity"] is None
    assert annotations.read_bytes() == before
    protected = subprocess.run(
        command + ["--output", str(annotations)], capture_output=True, check=False
    )
    assert protected.returncode != 0
    assert annotations.read_bytes() == before
    assignments.write_text("[]", encoding="utf-8")
    changed = subprocess.run(command + ["--output", str(output)], capture_output=True, check=False)
    assert changed.returncode != 0
    assert b"assignments changed" in changed.stderr

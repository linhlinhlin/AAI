import copy
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import pytest
from test_expert_validation import complete, fixture

from misconceptions.annotation_intake import merge_round_one
from misconceptions.expert_validation import score_annotation_sources, validate_annotations


def returned(reviewer="one"):
    document, rows = fixture()
    document["assignments_sha256"] = "test-hash"
    for sample in document["samples"]:
        complete(sample["reviews"][0], reviewer=reviewer)
        sample["reviews"][0]["independent_blind_review"] = True
    return document, rows


def test_merge_by_id_keeps_disagreement_and_inputs_unchanged():
    one, rows = returned()
    two, _ = returned("two")
    two["samples"][0]["reviews"][0]["misconception_type"] = "y"
    two["samples"].reverse()
    inputs = copy.deepcopy([one, two])
    merged = merge_round_one([one, two], rows)
    assert [one, two] == inputs
    assert merged["intake"]["adjudication_queue"][0]["disagreement"] is True
    assert all(s["adjudication"]["status"] == "pending" for s in merged["samples"])
    assert score_annotation_sources(merged, rows)["cluster_purity"] is None
    assert (
        score_annotation_sources(merged, rows)["agreement"][0]["misconception_decision"]["n_paired"]
        == 4
    )


def test_partial_return_does_not_invent_reviewer_or_completion():
    one, rows = returned()
    blank, _ = fixture()
    one["samples"][0]["reviews"] = blank["samples"][0]["reviews"]
    merged = merge_round_one([one], rows)
    assert merged["samples"][0]["reviews"] == []
    assert merged["intake"]["adjudication_queue"][0]["disagreement"] is None
    assert score_annotation_sources(merged, rows)["n_completed_records"] == 3


@pytest.mark.parametrize(
    "problem", ["ai", "codebook", "duplicate", "hash", "adjudication", "cluster", "mixed_reviewer"]
)
def test_reject_unsafe_merge(problem):
    one, rows = returned()
    two, _ = returned("two")
    if problem == "ai":
        two["samples"][0]["reviews"][0]["reviewer_id"] = "ai:test"
    elif problem == "codebook":
        two["codebook"]["version"] = "different"
    elif problem == "duplicate":
        two = copy.deepcopy(one)
    elif problem == "hash":
        two["assignments_sha256"] = "changed"
    elif problem == "adjudication":
        complete(two["samples"][0]["adjudication"])
    elif problem == "cluster":
        two["samples"][0]["reviews"][0]["same_cause_as_cluster"]["A"] = "Yes"
    else:
        two["samples"][0]["reviews"][0]["reviewer_id"] = "three"
    with pytest.raises(ValueError):
        merge_round_one([one, two], rows)


def test_reject_empty_or_unapproved_inputs():
    one, rows = returned()
    with pytest.raises(ValueError):
        merge_round_one([], rows)
    one["codebook"]["approved_by"] = None
    with pytest.raises(ValueError):
        merge_round_one([one], rows)


def test_cluster_summary_ties_and_unannotated_cluster():
    document, rows = returned()
    complete(document["samples"][0]["adjudication"], kind="x")
    complete(document["samples"][1]["adjudication"], kind="y")
    complete(document["samples"][2]["adjudication"], decision="Unclear", kind=None)
    result = score_annotation_sources(document, rows)
    arm = result["purity_details"][0]
    assert arm["cluster_purity"] == 0.5
    assert arm["purity_numerator"] == 1
    first, second = arm["cluster_details"]
    assert first["modal_types"] == ["x", "y"]
    assert first["typed_coverage"] == pytest.approx(2 / 3)
    assert first["multiple_observed_types"] is True
    assert second["multiple_observed_types"] is None
    assert second["modal_types"] == []


def test_duplicate_or_invalid_assignment_rejected():
    doc, rows = returned()
    with pytest.raises(ValueError):
        validate_annotations(doc, rows + [rows[0]])
    rows[0]["clusters_seed42"]["A"] = True
    with pytest.raises(ValueError):
        validate_annotations(doc, rows)


def test_merge_and_report_cli_preserve_files(tmp_path):
    root = Path(__file__).resolve().parents[1]
    document, rows = returned()
    assignments = tmp_path / "assignments.json"
    assignments.write_text(json.dumps(rows), encoding="utf-8")
    document["assignments_sha256"] = hashlib.sha256(assignments.read_bytes()).hexdigest()
    source = tmp_path / "one.json"
    source.write_text(json.dumps(document), encoding="utf-8")
    before = source.read_bytes()
    output = tmp_path / "merged.json"
    command = [
        sys.executable,
        str(root / "scripts/merge_itsp_annotations.py"),
        str(source),
        "--assignments",
        str(assignments),
        "--output",
        str(output),
    ]
    result = subprocess.run(command, capture_output=True, check=False)
    assert result.returncode == 0, result.stderr
    merged = json.loads(output.read_text(encoding="utf-8"))
    assert merged["intake"]["sources"][0]["sha256"] == hashlib.sha256(before).hexdigest()
    assert source.read_bytes() == before
    output_before = output.read_bytes()
    assert subprocess.run(command, capture_output=True, check=False).returncode != 0
    assert output.read_bytes() == output_before
    report = tmp_path / "report.md"
    command = [
        sys.executable,
        str(root / "scripts/report_itsp_experts.py"),
        "--annotations",
        str(output),
        "--assignments",
        str(assignments),
        "--output",
        str(report),
    ]
    result = subprocess.run(command, capture_output=True, check=False)
    assert result.returncode == 0, result.stderr
    assert "purity=null" in report.read_text(encoding="utf-8")
    assert subprocess.run(command, capture_output=True, check=False).returncode != 0

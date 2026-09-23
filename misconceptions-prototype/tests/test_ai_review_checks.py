"""Reject corrupted evidence and AI-to-human promotion, not just happy-path JSON."""

import importlib.util
import json
import zipfile
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("review_checks", ROOT / "scripts/check_itsp_review.py")
checks = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checks)


@pytest.fixture
def documents():
    return (
        checks.read_json(ROOT / checks.REVIEW),
        checks.read_json(ROOT / "data/itsp/expert_annotations.json"),
        checks.read_json(ROOT / checks.COMPARISON),
    )


def test_current_snapshot(documents):
    new, old, comparison = documents
    with zipfile.ZipFile(ROOT / "results/itsp/human_review_packet.zip") as archive:
        assert checks.check_review(new, archive) == {"Yes": 6, "No": 8, "Unclear": 3}
    differences = checks.check_comparison(new, old, comparison)
    assert {row["submission_id"] for row in differences} == {
        "itsp-2825-271154_buggy", "itsp-2825-271188_buggy", "itsp-2825-271213_buggy"}
    checks.check_human_pending(
        old, checks.read_json(ROOT / "results/itsp/expert_validation_metrics.json"))


@pytest.mark.parametrize("corruption", [
    "duplicate", "missing", "human_identity", "expert_eligible", "type_on_unclear",
    "bool_confidence", "invented_test", "missing_evidence_file", "wrong_evidence_hash",
    "invalid_line", "cluster_leak", "empty_evidence",
])
def test_reject_review_corruption(documents, corruption):
    new, _, _ = documents
    review = new["reviews"][0]
    if corruption == "duplicate":
        new["reviews"][1] = review
    elif corruption == "missing":
        new["reviews"].pop()
    elif corruption == "human_identity":
        review["reviewer_id"] = "reviewer_01"
    elif corruption == "expert_eligible":
        new["eligible_for_expert_metrics"] = True
    elif corruption == "type_on_unclear":
        review["misconception_type"] = "C_IO_CONTRACT"
    elif corruption == "bool_confidence":
        review["confidence"] = True
    elif corruption == "invented_test":
        review["logged_test_evidence"][0]["output"] = "invented"
    elif corruption == "missing_evidence_file":
        review["evidence_files"].pop()
    elif corruption == "wrong_evidence_hash":
        review["evidence_files"][0]["sha256"] = "0" * 64
    elif corruption == "invalid_line":
        review["source_lines"] = [99999]
    elif corruption == "cluster_leak":
        review["same_cause_as_cluster"]["A"] = "Yes"
    else:
        review["evidence"] = " "
    with (
        zipfile.ZipFile(ROOT / "results/itsp/human_review_packet.zip") as archive,
        pytest.raises(ValueError),
    ):
        checks.check_review(new, archive)


@pytest.mark.parametrize("corruption", [
    "decision_flag", "total", "priority", "old_label", "new_label", "duplicate",
    "mapping", "confidence", "order",
])
def test_recompute_comparison_instead_of_trusting_report(documents, corruption):
    new, old, comparison = documents
    row = comparison["comparisons"][0]
    if corruption == "decision_flag":
        row["decision_disagreement"] = True
    elif corruption == "total":
        comparison["n_decision_disagreements"] = 0
    elif corruption == "priority":
        row["priority"] = "P3"
    elif corruption == "old_label":
        row["old_ai"]["misconception"] = "Yes"
    elif corruption == "new_label":
        row["new_ai"]["misconception"] = "Yes"
    elif corruption == "duplicate":
        comparison["comparisons"][1] = row
    elif corruption == "mapping":
        row["old_type_mapped_to_draft"] = "MATH_MODEL"
    elif corruption == "confidence":
        row["confidence_difference"] = 99
    else:
        comparison["human_priority_order"].reverse()
    with pytest.raises(ValueError):
        checks.check_comparison(new, old, comparison)


@pytest.mark.parametrize("corruption", ["human", "adjudication", "purity", "ai_kappa"])
def test_cannot_promote_ai_into_human_ground_truth(documents, corruption):
    _, old, _ = documents
    metrics = checks.read_json(ROOT / "results/itsp/expert_validation_metrics.json")
    if corruption == "human":
        old["samples"][0]["reviews"][1]["misconception"] = "Yes"
    elif corruption == "adjudication":
        old["samples"][0]["adjudication"]["status"] = "complete"
    elif corruption == "purity":
        metrics["purity_details"][0]["cluster_purity"] = 1.0
    else:
        metrics["ai_annotation"][0]["cohen_kappa"] = 1.0
    with pytest.raises(ValueError):
        checks.check_human_pending(old, metrics)


@pytest.mark.parametrize("missing", [False, True])
def test_changed_or_missing_protected_file_is_reported(tmp_path, missing):
    folder = tmp_path / "results/itsp"
    folder.mkdir(parents=True)
    protected = tmp_path / "assignments.json"
    protected.write_text("original")
    baseline = folder / "ai_review_integrity_baseline.json"
    baseline.write_text(json.dumps({"assignments.json": checks.sha(protected)}))
    (folder / "ai_independent_review_verification.json").write_text(json.dumps({
        "baseline_sha256": checks.sha(baseline), "protected_existing_files_checked": 1,
    }))
    if missing:
        protected.unlink()
    else:
        protected.write_text("changed")
    with pytest.raises(ValueError, match="Protected files changed/missing: assignments.json"):
        checks.check_integrity(tmp_path)


def test_runner_continues_after_failure_and_returns_nonzero(tmp_path, monkeypatch, capsys):
    (tmp_path / "results/itsp").mkdir(parents=True)
    monkeypatch.setattr(checks, "ROOT", tmp_path)
    commands = []

    def fake_run(args, **kwargs):
        commands.append(args)
        return checks.subprocess.CompletedProcess(args, 0, stdout="test output", stderr="")

    monkeypatch.setattr(checks.subprocess, "run", fake_run)
    assert checks.main() == 1
    assert len(commands) == 3
    report = checks.read_json(tmp_path / "results/itsp/ai_review_check_latest.json")
    assert report["passed"] is False
    assert len(report["checks"]) == 6
    assert "KHÔNG ĐẠT" in capsys.readouterr().out

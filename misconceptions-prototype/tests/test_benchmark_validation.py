from copy import deepcopy

import pytest

from misconceptions.benchmark_validation import summarize_runs
from misconceptions.research_io import write_json


def fixture_run(tmp_path):
    report = {"status": "ok", "split": {"evaluation_partition": "validation"},
              "train_assignments": {"a": 0, "b": 1, "c": 1},
              "holdout_assignments": {"x": 0, "y": 1, "z": 1},
              "holdout_assignment_ties": 1, "silhouette_train": .5,
              "explanation": {"holdout_fidelity": 1 / 3,
                              "holdout_majority_baseline_fidelity": 2 / 3,
                              "rules": [{"if": ["TRUE"], "holdout_support": 3}]}}
    second = deepcopy(report)
    second["holdout_assignments"] = {"x": 1, "y": 0, "z": 0}
    write_json(tmp_path / "a.json", report)
    write_json(tmp_path / "b.json", second)
    write_json(tmp_path / "run_manifest.json", {})
    write_json(tmp_path / "summary.json", {"evaluation": "validation_only", "runs": [
        {"problem": "fixture", "method": "kmeans", "mode": "outcomes", "seed": 1, "artifact": "a.json"},
        {"problem": "fixture", "method": "kmeans", "mode": "outcomes", "seed": 2, "artifact": "b.json"}]})
    return second


def test_stability_ignores_label_ids_and_fidelity_can_lose_to_majority(tmp_path):
    fixture_run(tmp_path)
    result = summarize_runs(tmp_path)
    assert result["stability"][0]["mean_validation_ari"] == 1
    assert result["aggregate"][0]["fidelity_gain_over_majority"] == pytest.approx(-1 / 3)
    assert result["aggregate"][0]["validation_coverage"] == 1
    assert result["misconception_accuracy"] is None
    assert len(result["input_sha256"]) == 4


def test_different_splits_and_sealed_test_cannot_be_compared(tmp_path):
    second = fixture_run(tmp_path)
    second["holdout_assignments"] = {"unknown": 0}
    write_json(tmp_path / "b.json", second)
    with pytest.raises(ValueError, match="same locked split"):
        summarize_runs(tmp_path)
    second["split"]["evaluation_partition"] = "test"
    write_json(tmp_path / "b.json", second)
    with pytest.raises(ValueError, match="Sealed test"):
        summarize_runs(tmp_path)

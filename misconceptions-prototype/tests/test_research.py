"""Research regressions: distinguish evidence, preserve splits, exclude sealed test."""

from dataclasses import replace
from pathlib import Path

import numpy as np
import pytest
from test_core import row

from misconceptions import output_features
from misconceptions.adapters import load_dataset
from misconceptions.features import FeatureSpace, extract_oav, weighted_hamming
from misconceptions.output_features import output_oav, validate_output_logs
from misconceptions.pipeline import run_experiment
from misconceptions.splits import create_lock, leakage_groups, validate_assignments, validate_lock
from misconceptions.teaching_report import load_evidence


def test_observed_itsp_collision_resolved_by_output_without_labels():
    folder = Path(__file__).resolve().parents[1] / "data/itsp/cohorts/2825"
    manifest, rows = load_dataset(folder / "manifest.json", folder / "submissions.jsonl")
    logs = load_evidence(folder / "review.jsonl", rows)
    pair = [next(r for r in rows if r.submission_id == f"itsp-2825-{sid}_buggy")
            for sid in (271173, 271188)]
    assert extract_oav(pair[0]) == extract_oav(pair[1])
    validate_output_logs(pair, manifest["test_ids"], logs)
    assert output_oav(pair[0], logs)["stdout:1:relation"] == "different"
    assert output_oav(pair[1], logs)["stdout:1:relation"] == "other_oracle"
    space = FeatureSpace.fit(pair, manifest["test_ids"], feature_mode="combined_stdout", logs=logs)
    values = space.transform(pair, logs)
    distance = weighted_hamming(values, values, space.weights)
    assert distance[0, 1] > 0
    encoded = space.onehot(values)
    assert np.sum((encoded[0] - encoded[1]) ** 2) == pytest.approx(distance[0, 1])


def test_output_features_fit_only_train_and_do_not_relabel_verdicts():
    rows = [row(i) for i in range(3)]
    logs = {r.submission_id: [{"test_id": "a", "input": "", "expected": "hi", "output": "hi "}]
            for r in rows}
    logs[rows[-1].submission_id][0]["output"] = "different"
    space = FeatureSpace.fit(rows[:2], ["a", "b"], feature_mode="outcomes_stdout", logs=logs)
    assert not any(n.startswith("stdout:") for n in space.names)
    assert rows[0].outcomes["a"] == "fail"
    assert output_oav(rows[0], logs)["stdout:a:relation"] == "whitespace"


def test_no_fabrication_of_missing_output():
    r = row()
    with pytest.raises(ValueError, match="Incomplete"):
        validate_output_logs([r], ["a", "b"], {})
    logs = {r.submission_id: [{"test_id": "a", "input": "", "expected": "hi", "output": ""}]}
    validate_output_logs([r], ["a", "b"], logs)  # passed b need not have recorded stdout
    assert output_oav(r, logs)["stdout:a:relation"] == "empty"
    assert "stdout:b:relation" not in output_oav(r, logs)
    logs[r.submission_id].append(dict(logs[r.submission_id][0]))
    with pytest.raises(ValueError, match="duplicate"):
        validate_output_logs([r], ["a", "b"], logs)


def test_global_lock_preserves_cross_problem_and_excluded_bridges():
    rows = [row(i, i % 2) for i in range(80)]
    rows[1] = replace(rows[1], student_id=rows[0].student_id, problem_id="other")
    rows[2] = replace(rows[2], source_code=rows[1].source_code, outcomes={})
    lock = create_lock(rows)
    assert len({lock["assignments"][r.submission_id] for r in rows[:3]}) == 1
    assert lock == create_lock(list(reversed(rows)))
    validate_lock(rows, lock)
    altered = dict(lock["assignments"])
    altered[rows[2].submission_id] = "test" if altered[rows[0].submission_id] != "test" else "train"
    with pytest.raises(ValueError, match="component"):
        validate_assignments(rows, altered)
    with pytest.raises(ValueError, match="exact corpus"):
        validate_lock(rows + [row(999)], lock)


def test_locked_evaluation_never_fits_or_assigns_sealed_test():
    rows = [row(i, i % 2) for i in range(80)]
    lock = create_lock(rows)
    result = run_experiment(rows, test_ids=["a", "b"], split_assignments=lock["assignments"])
    assert result["status"] == "ok"
    assert all(lock["assignments"][sid] == "train" for sid in result["train_assignments"])
    assert all(lock["assignments"][sid] == "validation" for sid in result["holdout_assignments"])
    assert all(lock["assignments"][sid] != "test" for sid in result["oav"])
    changed = [replace(r, source_code=f"for x in range({i}):\n print(x)\n")
               if lock["assignments"][r.submission_id] == "test" else r
               for i, r in enumerate(rows)]
    rerun = run_experiment(changed, test_ids=["a", "b"], split_assignments=lock["assignments"])
    assert result["features"] == rerun["features"]
    assert result["train_assignments"] == rerun["train_assignments"]


def test_tampered_lock_and_oracle_rejected():
    rows = [row(i) for i in range(8)]
    lock = create_lock(rows)
    lock["policy"] = "cherry_picked"
    with pytest.raises(ValueError, match="policy"):
        validate_lock(rows, lock)
    logs = {r.submission_id: [{"test_id": "a", "input": "x", "expected": str(i), "output": ""}]
            for i, r in enumerate(rows)}
    with pytest.raises(ValueError, match="inconsistent"):
        validate_output_logs(rows, ["a", "b"], logs)


def test_empty_source_does_not_merge_distinct_students():
    rows = [replace(row(i), source_code="", outcomes={}) for i in range(2)]
    assert len(set(leakage_groups(rows))) == 2


def test_very_long_output_has_explicit_bounded_similarity_status(monkeypatch):
    r = row()
    actual = "x" * 327670
    logs = {r.submission_id: [{"test_id": "a", "input": "", "expected": "x", "output": actual}]}
    def should_not_compare(*args, **kwargs):
        raise AssertionError("Quadratic comparison must not run on large logged output")
    monkeypatch.setattr(output_features, "SequenceMatcher", should_not_compare)
    values = output_oav(r, logs)
    assert values["stdout:a:edit_band"] == "not_computed_large_output"
    assert values["stdout:a:relation"] == "different"
    assert logs[r.submission_id][0]["output"] == actual

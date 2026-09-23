from dataclasses import replace

import numpy as np
import pytest
from sklearn.metrics import adjusted_rand_score

from misconceptions.domain import Submission
from misconceptions.features import FeatureSpace, weighted_hamming
from misconceptions.pipeline import run_experiment


def rows():
    bodies = ("return n;", "while(n > 0) --n; return n;", "for(int j=0;j<n;j++) {} return n;")
    return [
        Submission(
            str(i),
            None,
            "p",
            "c",
            f"int f(int n) {{ {bodies[i % 3]} }} /*{i}*/",
            "v1",
            {"a": "fail", "b": "pass" if i % 2 else "fail"},
            "fixture",
        )
        for i in range(30)
    ]


def test_structural_excludes_tests_and_balances_weights():
    data = rows()
    space = FeatureSpace.fit(data, ["a", "b"], feature_mode="structural")
    assert space.names and all(name.startswith("ast:") for name in space.names)
    np.testing.assert_allclose(space.weights.sum(), 1)
    # No hidden fallback to outcomes, even when outcomes are changed in-place conceptually.
    altered = [replace(row, outcomes={"a": "pass", "b": "fail"}) for row in data]
    np.testing.assert_array_equal(space.transform(data), space.transform(altered))
    values = space.transform(data)
    onehot = space.onehot(values)
    distance = weighted_hamming(values, values, space.weights)
    np.testing.assert_allclose(distance, ((onehot[:, None] - onehot[None, :]) ** 2).sum(axis=2))
    combined = FeatureSpace.fit(data, ["a", "b"], feature_mode="combined")
    assert space.names == [name for name in combined.names if name.startswith("ast:")]


def test_no_varying_structure_abstains_without_falling_back_to_tests():
    data = [
        replace(row, source_code=f"int f(void) {{ return {i}; }}") for i, row in enumerate(rows())
    ]
    result = run_experiment(data, test_ids=["a", "b"], feature_mode="structural", k=2)
    assert result["status"] == "abstained"
    assert result["reason"] == "no_varying_structural_features"
    assert result["features"] == []
    assert run_experiment(data, test_ids=["a", "b"], feature_mode="outcomes", k=2)["status"] == "ok"


@pytest.mark.parametrize("method", ["agglomerative", "kmeans"])
def test_same_split_routing_and_correct_exact_baseline_for_structure(method):
    data = rows()
    runs = [
        run_experiment(data, test_ids=["a", "b"], feature_mode=mode, k=2, method=method)
        for mode in ("outcomes", "structural", "combined")
    ]
    assert all(run["status"] == "ok" for run in runs)
    assert all(
        run["split"] == runs[0]["split"] and run["routes"] == runs[0]["routes"] for run in runs
    )
    structural = runs[1]
    ids = structural["split"]["train_ids"]
    lookup = {row.submission_id: row for row in data}
    expected = adjusted_rand_score(
        [lookup[sid].outcomes["b"] for sid in ids],
        [structural["train_assignments"][sid] for sid in ids],
    )
    assert structural["ari_vs_exact_signature_train"] == pytest.approx(expected)
    assert all(name.startswith("ast:") for name in structural["oav"][ids[0]])
    assert structural["identity"]["missing_student_ids"] == len(data)


def test_structure_fit_cannot_select_holdout_only_feature():
    data = rows()
    train = [
        replace(row, source_code=f"int f(int n) {{ return n+{i}; }}") for i, row in enumerate(data)
    ]
    space = FeatureSpace.fit(train, ["a", "b"], feature_mode="structural")
    assert space.names == []
    # Held-out loops cannot change a train-fitted empty space.
    assert space.transform([data[1]]).shape == (1, 0)

import unittest
from dataclasses import replace

import numpy as np

from misconceptions.domain import Submission
from misconceptions.features import FeatureSpace, extract_oav, route_submission, weighted_hamming
from misconceptions.pipeline import leakage_groups, run_experiment


def row(i=0, pattern=0):
    return Submission(
        str(i),
        f"s{i}",
        "p",
        "python",
        f"def f(n):\n    return n + {i}\n",
        "v1",
        {"a": "fail", "b": "fail" if pattern else "pass"},
        "unit_fixture",
    )


class FeatureTests(unittest.TestCase):
    def test_oav_excludes_identity_and_provenance(self):
        observation = extract_oav(row())
        self.assertTrue(all(key.startswith(("test:", "ast:")) for key in observation))
        self.assertEqual(
            observation, extract_oav(replace(row(), student_id="SECRET", provenance="label"))
        )

    def test_missing_is_not_pass(self):
        self.assertEqual(
            route_submission(replace(row(), outcomes={"a": "fail"}), ["a", "b"]), "incomplete"
        )
        self.assertEqual(
            route_submission(replace(row(), outcomes={"a": "timeout"}), ["a"]), "execution_error"
        )

    def test_parse_unknown_is_distinct(self):
        malformed = replace(row(), source_code="def !")
        self.assertEqual(route_submission(malformed, ["a", "b"]), "parse_error")
        unsupported = extract_oav(replace(row(), language="java", source_code="class Main {}"))
        self.assertEqual(unsupported["ast:parse"], "unsupported")
        self.assertEqual(unsupported["ast:for"], "__unknown__")
        self.assertEqual(extract_oav(row())["ast:for"], "0")

    def test_ast_constant_selection_only_uses_training(self):
        space = FeatureSpace.fit([row(), row(1)], ["a", "b"])
        self.assertFalse(any(name.startswith("ast:") for name in space.names))
        held = replace(row(2), source_code="for i in range(3):\n    print(i)")
        self.assertEqual(space.transform([held]).shape[1], 2)

    def test_weighted_hamming_and_euclidean_identity(self):
        first, second = row(), replace(row(1, 1), source_code="for i in range(3):\n    print(i)")
        space = FeatureSpace.fit([first, second], ["a", "b"])
        values = space.transform([first, second])
        distance = weighted_hamming(values, values, space.weights)
        encoded = space.onehot(values)
        self.assertAlmostEqual(distance[0, 1], float(np.sum((encoded[0] - encoded[1]) ** 2)))
        np.testing.assert_allclose(np.diag(distance), 0)
        self.assertAlmostEqual(float(space.weights.sum()), 1)
        self.assertAlmostEqual(
            sum(w for n, w in zip(space.names, space.weights) if n.startswith("test:")), 0.8
        )

    def test_unknown_has_own_onehot_category(self):
        space = FeatureSpace.fit([row()], ["a", "b"], feature_mode="outcomes")
        unknown = space.transform([replace(row(), outcomes={})])
        self.assertEqual(float(space.onehot(unknown, False).sum()), 2)

    def test_bad_weights_rejected(self):
        values = np.asarray([["pass"]], dtype=object)
        with self.assertRaises(ValueError):
            weighted_hamming(values, values, np.asarray([float("nan")]))


class PipelineTests(unittest.TestCase):
    def test_routed_rows_preserve_group_bridges(self):
        eligible = [row(i, i % 2) for i in range(4)]
        bridges = [
            replace(
                row(i + 10),
                student_id=eligible[i].student_id,
                source_code=eligible[i + 1].source_code,
                outcomes={},
            )
            for i in range(3)
        ]
        result = run_experiment(eligible + bridges, test_ids=["a", "b"])
        self.assertEqual(result["reason"], "fewer_than_two_independent_groups")

    def test_connected_group_transitivity(self):
        a, b = row(0), replace(row(1), student_id="s0")
        c = replace(row(2), source_code=b.source_code)
        groups = leakage_groups([a, b, c, row(3)])
        self.assertEqual(len(set(groups[:3])), 1)
        self.assertNotEqual(groups[0], groups[3])

    def test_split_has_no_student_or_exact_source_leakage(self):
        rows = [row(i, i % 2) for i in range(24)]
        rows[1] = replace(rows[1], student_id=rows[0].student_id)
        rows[2] = replace(rows[2], source_code=rows[1].source_code)
        result = run_experiment(rows, test_ids=["a", "b"])
        self.assertEqual(result["status"], "ok")
        lookup = {r.submission_id: r for r in rows}
        train = [lookup[i] for i in result["split"]["train_ids"]]
        held = [lookup[i] for i in result["split"]["holdout_ids"]]
        self.assertFalse({r.student_id for r in train} & {r.student_id for r in held})
        self.assertFalse({r.source_code for r in train} & {r.source_code for r in held})
        self.assertEqual(
            sum(rule["holdout_support"] for rule in result["explanation"]["rules"]), len(held)
        )
        self.assertEqual(
            result["explanation"]["target"], "cluster_id_only_not_validated_misconception"
        )

    def test_all_methods_and_determinism(self):
        rows = [row(i, i % 2) for i in range(24)]
        for method in ("exact", "agglomerative", "kmeans"):
            with self.subTest(method=method):
                result = run_experiment(rows, test_ids=["a", "b"], method=method)
                self.assertEqual(result["status"], "ok")
                self.assertEqual(result["n_clusters"], 2)
                self.assertAlmostEqual(result["silhouette_train"], 1)
                self.assertEqual(result, run_experiment(rows, test_ids=["a", "b"], method=method))

    def test_identical_and_one_group_abstain(self):
        result = run_experiment([row(i) for i in range(12)], test_ids=["a", "b"])
        self.assertEqual(result["reason"], "identical_training_features")
        result = run_experiment(
            [replace(row(i), student_id="same") for i in range(12)], test_ids=["a", "b"]
        )
        self.assertEqual(result["reason"], "fewer_than_two_independent_groups")

    def test_invalid_k_and_cohorts(self):
        rows = [row(i, i % 2) for i in range(12)]
        with self.assertRaises(ValueError):
            run_experiment(rows, test_ids=["a", "b"], k=1)
        with self.assertRaises(ValueError):
            run_experiment(rows + [replace(row(13), suite_version="v2")], test_ids=["a", "b"])
        result = run_experiment(rows, test_ids=["a", "b"], k=3)
        self.assertEqual(result["status"], "abstained")

    def test_all_pass_not_clustered(self):
        rows = [replace(row(i), outcomes={"a": "pass", "b": "pass"}) for i in range(8)]
        result = run_experiment(rows, test_ids=["a", "b"])
        self.assertEqual(result["n_eligible"], 0)
        self.assertEqual(result["route_counts"]["no_failure"], 8)


if __name__ == "__main__":
    unittest.main()

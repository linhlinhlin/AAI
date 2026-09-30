import random

import numpy as np
import pytest

from misconceptions import ila
from misconceptions.deviation_features import code_cues, deviation, deviation_oav
from misconceptions.mechanism_eval import CategoricalSpace, ceiling, pairwise_scores, score
from misconceptions.mechanism_inject import apply_site, one_mutant_per_category, sites
from misconceptions.repair_labels import classify_repair
from misconceptions.replay import outcomes_from_record, relation, request_for

PROGRAM = """#include <stdio.h>
int main()
{
    int i, n, x, soma = 0;
    float media;
    scanf("%d", &n);
    for (i = 0; i < n; i++) {
        scanf("%d", &x);
        if (x > 0 && x < 100) {
            soma = soma + x;
        }
    }
    media = (float) soma / n;
    printf("Media: %.2f\\n", media);
    return 0;
}
"""


def test_every_injected_site_changes_one_place_and_matches_its_repair_category():
    seen = set()
    for site in sites(PROGRAM):
        mutated = apply_site(PROGRAM, site)
        assert mutated != PROGRAM
        category = site[0]
        seen.add(category)
        # The inverse edit, classified as a repair, must land in the injected category.
        assert category in classify_repair(mutated, PROGRAM)["categories"], site[:2]
    assert {"LOOP_BOUNDARY", "BRANCH_CONDITION", "INITIALIZATION", "COMPUTATION", "NUMERIC_TYPE",
            "OUTPUT_FORMAT", "OUTPUT_TEXT", "MISSING_STATEMENT", "EXTRA_STATEMENT"} <= seen


def test_one_mutant_per_category_is_seeded_and_unique_per_category():
    first = one_mutant_per_category(PROGRAM, random.Random(3))
    again = one_mutant_per_category(PROGRAM, random.Random(3))
    assert first == again
    categories = [category for category, _, _ in first]
    assert len(categories) == len(set(categories))


@pytest.mark.parametrize("actual,expected,key,value", [
    ("5\n", "4\n", "numbers", "off_by_one"),
    ("3\n", "3.75\n", "numbers", "truncated"),
    ("3.8\n", "3.75\n", "numbers", "precision"),
    ("4", "4\n", "newline_end", "missing"),
    ("media: 4\n", "Media: 4\n", "text", "case_only"),
    ("1\n2\n", "1\n2\n3\n", "prefix", "truncated"),
    ("1 2 3\n", "1\n2\n3\n", "whitespace_only", "yes"),
])
def test_deviation_descriptors(actual, expected, key, value):
    assert deviation(actual, expected, {expected}, "fail")[key] == value


def test_deviation_is_not_computed_for_non_failures_and_aggregates_are_label_free():
    runs = {"t0": ("pass", "4\n", "4\n"), "t1": ("fail", "5\n", "4\n"), "t2": ("timeout", "", "9\n")}
    values = deviation_oav(runs, {"4\n", "9\n"})
    assert values["dev:t0:status"] == "pass" and values["dev:t0:numbers"] == "n/a"
    assert values["agg:fail_fraction"] == "most"
    assert all(not key.startswith(("label", "repair")) for key in values)


def test_code_cues_describe_structure_only():
    cues = code_cues(PROGRAM, {"Media: 2.00\n"})
    assert cues["code:loop_strict"] == "1" and cues["code:float_cast"] == "1"
    assert cues["code:printf_precision"] == "2"
    assert cues["code:words_outside_oracle"] == "no"


def test_ila_induces_consistent_rules_and_abstains_when_nothing_matches():
    rows = [{"a": "x", "b": "p"}, {"a": "x", "b": "q"}, {"a": "y", "b": "p"}, {"a": "y", "b": "q"},
            {"a": "x", "b": "p"}, {"a": "y", "b": "q"}]
    labels = ["L", "L", "M", "M", "L", "M"]
    rules = ila.induce(rows, labels, min_support=2)
    assert all(rule["train_false_positives"] == 0 for rule in rules)
    assert ila.predict(rules, [{"a": "x", "b": "q"}, {"a": "z", "b": "z"}]) == ["L", "abstain"]


def test_ila2_penalty_tolerates_a_noisy_example_that_blocks_original_ila():
    rows = [{"a": "x"}] * 5 + [{"a": "y"}] * 4
    labels = ["L"] * 4 + ["M"] + ["M"] * 4
    assert not [r for r in ila.induce(rows, labels, min_support=2) if r["then"] == "L"]
    noisy = ila.induce(rows, labels, penalty=1.0, min_support=2)
    assert any(r["then"] == "L" and r["if"] == {"a": "x"} for r in noisy)
    result = ila.evaluate(noisy, rows, labels)
    assert result["coverage"] == 1.0 and result["selective_accuracy"] == pytest.approx(8 / 9)


def test_categorical_space_uses_training_vocabulary_only():
    train = [{"test:t": "fail", "dev:t:numbers": "off_by_one", "code:x": "1"},
             {"test:t": "pass", "dev:t:numbers": "n/a", "code:x": "1"}]
    space = CategoricalSpace.fit(train, {"test": 0.5, "dev": 0.5, "code": 0.0})
    assert space.names == ["test:t", "dev:t:numbers"] or space.names == ["dev:t:numbers", "test:t"]
    values = space.transform([{"test:t": "timeout", "dev:t:numbers": "off_by_one"}])
    assert "__unknown__" in values[0].tolist()
    assert np.isclose(space.weights.sum(), 1.0)


def test_ceiling_and_pairwise_scores():
    values = np.asarray([["a"], ["a"], ["a"], ["b"]], dtype=object)
    assert ceiling(values, ["L", "L", "M", "M"]) == pytest.approx(3 / 4)
    precision, recall, f1 = pairwise_scores([0, 0, 1, 1], ["L", "L", "M", "M"])
    assert precision == recall == f1 == 1.0
    assert score([0, 0, 0, 0], ["L", "L", "M", "M"])["ari"] == 0.0


def test_replay_relation_and_missing_evidence_is_never_a_pass():
    assert relation(b"4\n", "4\n") == "exact"
    assert relation(b"4\r\n", "4\n") == "exact"
    assert relation(b"4", "4\n") == "trailing_whitespace"
    assert relation(b"\xff", "4\n") == "invalid_utf8"
    tests = {"t0": {"input": "", "expected": "4\n"}, "t1": {"input": "", "expected": "5\n"}}
    ok = {"compile": {"returncode": 0}, "tests": [
        {"test_id": "t0", "relation": "exact", "exit_code": 0, "signal": None, "timeout": False,
         "output_truncated": False}]}
    assert outcomes_from_record(ok, tests) is None  # t1 was not executed
    assert outcomes_from_record({"compile": {"returncode": 1}, "tests": []}, tests) is None
    assert outcomes_from_record({"submission_id": "x", "skipped": "empty_source"}, tests) is None
    assert outcomes_from_record({"submission_id": "x", "infrastructure_error": "e"}, tests) is None
    ok["tests"].append({"test_id": "t1", "relation": "exact", "exit_code": 3, "signal": None,
                        "timeout": False, "output_truncated": False})
    assert outcomes_from_record(ok, tests) == {"t0": "pass", "t1": "runtime_error"}
    request = request_for("id", "int main(){}", tests)
    assert [t["id"] for t in request["tests"]] == ["t0", "t1"]
    assert all("expected" not in t for t in request["tests"])  # Oracles never enter the sandbox.

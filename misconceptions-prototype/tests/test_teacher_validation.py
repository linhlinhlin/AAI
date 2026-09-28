"""Authored ratings only: these fixtures are not real teacher validation."""

from copy import deepcopy

import pytest

from misconceptions.teacher_validation import (
    adjudicated_labels,
    evaluate_report,
    forms,
    pair_scores,
    validate_form,
)


@pytest.fixture
def evidence():
    return {"cases": [{"case_id": f"case_{i}", "source_code": "int main(){return 0;}\n",
                       "logged_tests": [{"test_id": "t1"}]} for i in range(4)]}


def complete(form, reviewer):
    form = deepcopy(form)
    form["reviewer_id"] = reviewer
    form["codebook"] = {"version": "fixture-v1", "approved_by": "fixture-coordinator",
                        "labels": ["loop", "boundary"], "label_policy": "single_primary"}
    for rating in form["ratings"]:
        rating.update(status="supported", mechanism="loop", rationale="Authored fixture evidence",
                      source_lines=[1], test_ids=["t1"])
    return form


def test_empty_reviews_stay_null_and_unknown_pairs_do_not_become_correct(evidence):
    review, adjudication = forms(evidence)
    labels, cognitive, audit = adjudicated_labels(evidence, [review, deepcopy(review)], adjudication)
    assert labels == cognitive == {}
    assert audit["agreement"] == []
    result = pair_scores({"a": 0, "b": 0}, {})
    assert result["pair_precision"] is result["ari"] is None
    assert result["label_coverage"] == 0


def test_cognitive_claim_requires_more_than_code_and_test(evidence):
    review, _ = forms(evidence)
    review = complete(review, "fixture-teacher")
    review["ratings"][0]["cognitive_status"] = "supported"
    with pytest.raises(ValueError, match="learner explanation"):
        validate_form(review, evidence)
    review["ratings"][0].update(learner_explanation="Fixture interview quotation",
                                follow_up_observation="Fixture follow-up response")
    validate_form(review, evidence)


@pytest.mark.parametrize("corruption", ["ai", "line", "test", "hash", "not_blind"])
def test_invalid_evidence_and_ai_cannot_enter_gold(evidence, corruption):
    review = complete(forms(evidence)[0], "fixture-reviewer")
    if corruption == "ai":
        review["annotation_source"] = "AI"
    elif corruption == "line":
        review["ratings"][0]["source_lines"] = [2]
    elif corruption == "test":
        review["ratings"][0]["test_ids"] = ["imaginary"]
    elif corruption == "hash":
        evidence["cases"][0]["source_code"] = "changed"
    else:
        review["independent_blind_review"] = False
    with pytest.raises(ValueError):
        validate_form(review, evidence)


def test_two_reviewers_and_separate_adjudicator_required(evidence):
    review, adjudication = forms(evidence)
    a, b = complete(review, "fixture-A"), complete(review, "fixture-B")
    final = complete(adjudication, "fixture-C")
    final["coordinator_verified_by"] = "fixture-coordinator"
    with pytest.raises(ValueError, match="two independent"):
        adjudicated_labels(evidence, [a], final)
    with pytest.raises(ValueError, match="same reviewer"):
        adjudicated_labels(evidence, [a, a], final)
    b["ratings"][0]["mechanism"] = "boundary"
    labels, cognitive, audit = adjudicated_labels(evidence, [a, b], final)
    assert len(labels) == 4 and not cognitive
    assert audit["queue"][0]["disagreement"]
    assert audit["agreement"][0]["raw_agreement"] == 0.75
    final["reviewer_id"] = "fixture-A"
    with pytest.raises(ValueError, match="separate adjudicator"):
        adjudicated_labels(evidence, [a, b], final)


def test_pair_metrics_are_label_permutation_invariant():
    assignments = {"a": 10, "b": 10, "c": 20, "d": 20}
    labels = {"a": "loop", "b": "loop", "c": "boundary", "d": "loop"}
    score = pair_scores(assignments, labels)
    assert (score["pair_tp"], score["pair_fp"], score["pair_fn"]) == (1, 1, 2)
    assert score["pair_precision"] == 0.5
    assert score["pair_recall"] == pytest.approx(1 / 3)
    assert score["pair_f1"] == 0.4
    assert score == pair_scores({i: 30 - c for i, c in assignments.items()}, labels)


def report():
    return {"status": "ok", "split": {"evaluation_partition": "validation", "holdout_ids": ["x", "y"]},
            "train_assignments": {"a": 0, "b": 0, "c": 1}, "holdout_assignments": {"x": 0, "y": 1},
            "explanation": {"holdout_leaf_ids": [1, 2], "rules": [
                {"rule_id": 1, "if": ["test:1=fail"], "then_cluster": 0},
                {"rule_id": 2, "if": ["NOT (test:1=fail)"], "then_cluster": 1}]}}


def test_rule_mapping_never_learns_from_validation_labels():
    r = report()
    labels = {"a": "loop", "b": "loop", "c": "boundary", "x": "boundary", "y": "loop"}
    result = evaluate_report(r, labels)
    assert result["cluster_to_mechanism_train_only"] == {0: "loop", 1: "boundary"}
    assert [rule["mechanism_precision"] for rule in result["rules"]] == [0, 0]
    assert sum(rule["coverage_of_validation"] for rule in result["rules"]) == 1
    missing = evaluate_report(r, {"x": "boundary", "y": "loop"})
    assert all(rule["mechanism_precision"] is None for rule in missing["rules"])
    tie = evaluate_report(r, labels | {"b": "boundary"})
    assert tie["rules"][0]["mechanism_from_train_only"] is None
    r["split"]["evaluation_partition"] = "test"
    with pytest.raises(ValueError, match="sealed test"):
        evaluate_report(r, labels)

"""Blinded, evidence-bound human mechanism review, separate from dashboard opinions.

Version 1 deliberately evaluates single-primary mechanisms only. Multiple causes,
uncertainty and missing ratings abstain; they are never coerced to negative labels.
"""

from collections import Counter
from copy import deepcopy
from itertools import combinations

from sklearn.metrics import adjusted_rand_score

from .ai_labeling import fingerprint
from .expert_validation import agreement

STATUSES = {"pending", "supported", "uncertain", "multiple", "no_target_error"}
COGNITIVE = {"unassessed", "supported", "rejected", "insufficient_evidence"}


def blank_rating(case_id):
    return {"case_id": case_id, "status": "pending", "mechanism": None,
            "rationale": "", "source_lines": [], "test_ids": [],
            "cognitive_status": "unassessed", "learner_explanation": "", "follow_up_observation": ""}


def forms(evidence):
    packet_id = fingerprint(evidence)
    ratings = [blank_rating(case["case_id"]) for case in evidence["cases"]]
    base = {"schema_version": 1, "packet_id": packet_id, "annotation_source": "human",
            "reviewer_id": "", "independent_blind_review": True,
            "codebook": {"version": "", "approved_by": "", "labels": [],
                         "label_policy": "single_primary"}, "ratings": ratings}
    adjudication = deepcopy(base)
    adjudication["independent_blind_review"] = False
    adjudication["coordinator_verified_by"] = ""
    return base, adjudication


def human_id(value):
    return isinstance(value, str) and bool(value.strip()) and not value.lower().startswith("ai:")


def validate_form(form, evidence, adjudication=False):
    if form.get("schema_version") != 1 or form.get("packet_id") != fingerprint(evidence):
        raise ValueError("Annotation packet/evidence hash mismatch")
    if form.get("annotation_source") != "human":
        raise ValueError("AI suggestions cannot be submitted as human gold")
    cases = {c["case_id"]: c for c in evidence["cases"]}
    ratings = form["ratings"]
    if len(ratings) != len(cases) or {r["case_id"] for r in ratings} != set(cases):
        raise ValueError("Rating IDs must match the packet exactly without duplicates")
    completed = any(r["status"] != "pending" for r in ratings)
    book = form["codebook"]
    if completed:
        if not human_id(form["reviewer_id"]) or not human_id(book["approved_by"]):
            raise ValueError("Completed forms require human reviewer and codebook approver IDs")
        if not book["version"] or book["label_policy"] != "single_primary":
            raise ValueError("Approve a versioned single-primary codebook before scoring")
        labels = book["labels"]
        if not isinstance(labels, list) or not labels or any(not isinstance(x, str) or not x.strip() for x in labels):
            raise ValueError("Codebook requires nonempty labels")
        if len(set(labels)) != len(labels):
            raise ValueError("Duplicate codebook labels")
        if not adjudication and form.get("independent_blind_review") is not True:
            raise ValueError("Round-one ratings must be independent and blind to clusters/AI")
        if adjudication and not human_id(form.get("coordinator_verified_by")):
            raise ValueError("Coordinator must verify human identity, independence and evidence")
    for rating in ratings:
        case = cases[rating["case_id"]]
        if rating["status"] not in STATUSES or rating["cognitive_status"] not in COGNITIVE:
            raise ValueError("Unknown mechanism or cognitive validation status")
        if rating["status"] == "pending":
            if rating != blank_rating(rating["case_id"]):
                raise ValueError("Pending slots must stay blank")
            continue
        if not isinstance(rating["rationale"], str) or not rating["rationale"].strip():
            raise ValueError("Completed ratings need a rationale")
        if rating["status"] == "supported":
            if rating["mechanism"] not in book["labels"]:
                raise ValueError("Mechanism is absent from approved codebook")
            if not rating["source_lines"] or not rating["test_ids"]:
                raise ValueError("Supported mechanism needs source lines and observed test evidence")
        elif rating["mechanism"] is not None:
            raise ValueError("Uncertain/multiple/no-target ratings must not carry a single gold label")
        if not isinstance(rating["source_lines"], list) or any(
            type(line) is not int or not 1 <= line <= len(case["source_code"].splitlines())
            for line in rating["source_lines"]
        ):
            raise ValueError("Evidence references an invalid source line")
        observed = {t["test_id"] for t in case["logged_tests"]}
        if not isinstance(rating["test_ids"], list) or any(t not in observed for t in rating["test_ids"]):
            raise ValueError("Evidence references a test absent from the packet")
        if rating["cognitive_status"] in {"supported", "rejected"} and not all(
            isinstance(rating[k], str) and rating[k].strip()
            for k in ("learner_explanation", "follow_up_observation")
        ):
            raise ValueError("Cognitive validation needs learner explanation and a follow-up observation")
        if rating["cognitive_status"] == "supported" and rating["status"] != "supported":
            raise ValueError("Cognitive support also requires an evidence-supported mechanism")


def adjudicated_labels(evidence, reviews, adjudication):
    validate_form(adjudication, evidence, adjudication=True)
    active = []
    for form in reviews:
        validate_form(form, evidence)
        if any(r["status"] != "pending" for r in form["ratings"]):
            active.append(form)
    ids = [f["reviewer_id"] for f in active]
    if len(set(ids)) != len(ids):
        raise ValueError("The same reviewer cannot count as two independent reviewers")
    if active and any(f["codebook"] != active[0]["codebook"] for f in active):
        raise ValueError("Reviewer codebooks differ")
    lookups = [{r["case_id"]: r for r in f["ratings"]} for f in active]
    labels, cognitive, queue = {}, {}, []
    for rating in adjudication["ratings"]:
        case = rating["case_id"]
        completed = [lookup[case] for lookup in lookups if lookup[case]["status"] != "pending"]
        if rating["status"] != "pending":
            if len(completed) < 2 or adjudication["reviewer_id"] in ids:
                raise ValueError("Adjudication requires two independent reviewers and a separate adjudicator")
            if adjudication["codebook"] != active[0]["codebook"]:
                raise ValueError("Adjudicator and reviewers must use the same codebook")
            if rating["status"] == "supported":
                labels[case] = rating["mechanism"]
                if rating["cognitive_status"] == "supported":
                    cognitive[case] = rating["mechanism"]
        queue.append({"case_id": case, "n_reviews": len(completed),
                      "disagreement": len({(r["status"], r["mechanism"]) for r in completed}) > 1
                      if len(completed) >= 2 else None,
                      "adjudication_status": rating["status"]})
    agreements = []
    for i, j in combinations(range(len(active)), 2):
        common = [c for c in lookups[i] if lookups[i][c]["status"] != "pending"
                  and lookups[j][c]["status"] != "pending"]
        def value(r):
            return str((r["status"], r["mechanism"]))
        agreements.append({"reviewers": [ids[i], ids[j]], **agreement(
            [value(lookups[i][c]) for c in common], [value(lookups[j][c]) for c in common])})
    return labels, cognitive, {"queue": queue, "agreement": agreements,
                               "n_supported_mechanisms": len(labels),
                               "n_cognitively_supported": len(cognitive)}


def pair_scores(assignments, labels):
    ids = sorted(set(assignments) & set(labels))
    tp = fp = fn = 0
    for a, b in combinations(ids, 2):
        predicted, actual = assignments[a] == assignments[b], labels[a] == labels[b]
        tp += int(predicted and actual)
        fp += int(predicted and not actual)
        fn += int(not predicted and actual)
    return {"n_labeled": len(ids), "n_assigned": len(assignments),
            "label_coverage": len(ids) / len(assignments) if assignments else None,
            "pair_tp": tp, "pair_fp": fp, "pair_fn": fn,
            "pair_precision": tp / (tp + fp) if tp + fp else None,
            "pair_recall": tp / (tp + fn) if tp + fn else None,
            "pair_f1": 2 * tp / (2 * tp + fp + fn) if 2 * tp + fp + fn else None,
            "ari": float(adjusted_rand_score([labels[i] for i in ids], [assignments[i] for i in ids]))
            if len(ids) >= 2 else None}


def evaluate_report(report, labels):
    if report["status"] != "ok":
        return {"status": "abstained", "reason": report["reason"], "clustering": None, "rules": None}
    if report["split"]["evaluation_partition"] != "validation":
        raise ValueError("This evaluator does not open the sealed test")
    train, held = report["train_assignments"], report["holdout_assignments"]
    mapping = {}
    for cluster in set(train.values()):
        counts = Counter(labels[i] for i, c in train.items() if c == cluster and i in labels)
        winners = [label for label, count in counts.items() if count == max(counts.values())] if counts else []
        mapping[cluster] = winners[0] if len(winners) == 1 else None
    explanation = report["explanation"]
    leaves = explanation.get("holdout_leaf_ids")
    held_ids = report["split"]["holdout_ids"]
    rules = []
    if leaves is not None:
        if len(leaves) != len(held_ids) or set(held_ids) != set(held):
            raise ValueError("Rule leaf assignments do not match validation IDs")
        for rule in explanation["rules"]:
            members = [i for i, leaf in zip(held_ids, leaves) if leaf == rule["rule_id"]]
            known = [i for i in members if i in labels]
            target = mapping[rule["then_cluster"]]
            rules.append({"rule_id": rule["rule_id"], "if": rule["if"],
                          "mechanism_from_train_only": target, "n_validation": len(members),
                          "n_labeled_validation": len(known),
                          "coverage_of_validation": len(members) / len(held_ids),
                          "mechanism_precision": sum(labels[i] == target for i in known) / len(known)
                          if target is not None and known else None,
                          "reason": "no_unique_train_label" if target is None else
                          ("no_validation_labels" if not known else None)})
    return {"status": "evaluated" if any(i in labels for i in held) else "waiting_for_teacher_labels",
            "scope": "adjudicated_single_primary_mechanisms_only",
            "cluster_to_mechanism_train_only": mapping, "clustering": pair_scores(held, labels),
            "rules": rules if leaves is not None else None,
            "rule_status": "available" if leaves is not None else "rerun_needed_for_leaf_membership"}

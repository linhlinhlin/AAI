"""Checked mechanism hypotheses for classroom clusters (never diagnoses).

Frozen ILA-2 rules, induced on repair-grounded labels of a public corpus and measured on
students they never saw, are applied to the execution-deviation OAV of each submission.
A cluster receives the hypotheses of its members together with how well the rules held
out of sample, so the instructor sees a checkable claim with its evidence and its limits.
"""

import json
from collections import Counter
from pathlib import Path

from .deviation_features import code_cues, deviation_oav
from .mechanism_feedback import CAVEAT, FEEDBACK

RULES = Path(__file__).with_name("data") / "mechanism_rules.json"


def load_rules(path=RULES):
    if not path.exists():
        return None
    rules = json.loads(path.read_text(encoding="utf-8"))
    if rules.get("schema") != "mechanism_rules_v1" or rules.get("status") != "hypothesis_rules_not_diagnoses":
        raise ValueError("Unexpected mechanism rule file")
    return rules


def agnostic_values(row, logs, tests):
    oracles = {test["expected"] for test in tests}
    by_test = {entry["test_id"]: entry for entry in logs}
    runs = {test["test_id"]: (row.outcomes.get(test["test_id"], "not_run"),
                              by_test.get(test["test_id"], {}).get("output") or "", test["expected"])
            for test in tests}
    values = deviation_oav(runs, oracles) | code_cues(row.source_code, oracles)
    return {k: v for k, v in values.items() if k.startswith(("agg:", "code:"))}


def match(rules, values):
    return next((rule for rule in rules["rules"]
                 if all(values.get(attribute) == value for attribute, value in rule["if"].items())), None)


def mechanism_report(rows, logs, tests, assignments, rules=None):
    rules = load_rules() if rules is None else rules
    if rules is None:
        return {"status": "unavailable", "reason": "Chưa có bộ luật cơ chế đã kiểm chứng."}
    per_submission = {}
    for row in rows:
        if all(outcome == "pass" for outcome in row.outcomes.values()):
            continue
        rule = match(rules, agnostic_values(row, logs.get(row.submission_id, []), tests))
        per_submission[row.submission_id] = {
            "category": rule["then"] if rule else None,
            "rule": {"if": rule["if"], "then": rule["then"],
                     "train_precision": rule["train_precision"],
                     "train_support": rule["train_true_positives"]} if rule else None}
    clusters = {}
    for sid, cluster in assignments.items():
        if sid not in per_submission:
            continue
        entry = clusters.setdefault(str(cluster), {"members": 0, "abstained": 0, "categories": Counter()})
        entry["members"] += 1
        category = per_submission[sid]["category"]
        if category is None:
            entry["abstained"] += 1
        else:
            entry["categories"][category] += 1
    summary = []
    for cluster, entry in sorted(clusters.items()):
        top = entry["categories"].most_common(1)
        category, count = top[0] if top else (None, 0)
        summary.append({
            "cluster": cluster, "members": entry["members"], "abstained": entry["abstained"],
            "categories": dict(entry["categories"]),
            "top_category": category, "top_share": count / entry["members"] if entry["members"] else 0,
            "feedback": FEEDBACK.get(category) if category else None})
    return {"status": "hypothesis", "caveat": CAVEAT, "algorithm": rules["algorithm"],
            "held_out": rules.get("held_out"), "trained_on": rules.get("trained_on"),
            "submissions": per_submission, "clusters": summary}

"""ILA and ILA-2 production-rule induction over categorical OAV (supervised).

Tolun & Abu-Soud (1998) ILA induces, class by class, the most frequent attribute-value
combinations that occur in unmarked examples of the class and in no other class.
ILA-2 (Tolun et al., 1999) tolerates noise by scoring a combination as
`true_positives - penalty * false_positives`. Rules form an ordered list; examples that
match no rule receive `abstain`, never a silent default class.
"""

from collections import Counter
from itertools import combinations


def induce(rows, labels, *, max_conditions=2, penalty=None, min_support=2, attributes=None):
    """rows: list of dict attribute->value. penalty=None is the original, consistent ILA."""
    if len(rows) != len(labels) or not rows:
        raise ValueError("Rows and labels must be nonempty and aligned")
    attributes = sorted(attributes or {name for row in rows for name in row})
    rules = []
    classes = sorted(set(labels), key=lambda c: (-labels.count(c), str(c)))
    for target in classes:
        inside = [i for i, label in enumerate(labels) if label == target]
        outside = [i for i, label in enumerate(labels) if label != target]
        unmarked = set(inside)
        size = 1
        negatives_cache = {}  # The other classes never change while this class is covered.
        while unmarked and size <= max_conditions:
            best = None
            for subset in combinations(attributes, size):
                counts = Counter(tuple(rows[i].get(a) for a in subset) for i in unmarked)
                if not counts:
                    continue
                if subset not in negatives_cache:
                    negatives_cache[subset] = Counter(
                        tuple(rows[i].get(a) for a in subset) for i in outside)
                negatives = negatives_cache[subset]
                for values, positives in counts.items():
                    if positives < min_support or None in values:
                        continue
                    false = negatives.get(values, 0)
                    if penalty is None:
                        if false:
                            continue
                        score = positives
                    else:
                        score = positives - penalty * false
                        if score <= 0:
                            continue
                    key = (score, positives, -len(subset))
                    if best is None or key > best[0]:
                        best = (key, subset, values, positives, false)
            if best is None:
                size += 1
                continue
            _, subset, values, positives, false = best
            condition = dict(zip(subset, values))
            covered = {i for i in unmarked if all(rows[i].get(a) == v for a, v in condition.items())}
            unmarked -= covered
            support = sum(all(rows[i].get(a) == v for a, v in condition.items()) for i in inside)
            rules.append({"if": condition, "then": target, "train_true_positives": support,
                          "train_false_positives": false,
                          "train_precision": support / (support + false) if support + false else None})
    # First-match order: most precise, then best supported rules fire first.
    return sorted(rules, key=lambda r: (-(r["train_precision"] or 0), -r["train_true_positives"]))


def predict(rules, rows):
    predictions = []
    for row in rows:
        for rule in rules:
            if all(row.get(a) == v for a, v in rule["if"].items()):
                predictions.append(rule["then"])
                break
        else:
            predictions.append("abstain")
    return predictions


def evaluate(rules, rows, labels):
    predictions = predict(rules, rows)
    answered = [(p, y) for p, y in zip(predictions, labels) if p != "abstain"]
    classes = sorted(set(labels))
    per_class = {}
    for c in classes:
        tp = sum(p == c and y == c for p, y in answered)
        fp = sum(p == c and y != c for p, y in answered)
        fn = sum(y == c and p != c for p, y in zip(predictions, labels))
        precision = tp / (tp + fp) if tp + fp else None
        recall = tp / (tp + fn) if tp + fn else None
        f1 = 2 * precision * recall / (precision + recall) if precision and recall else 0.0
        per_class[c] = {"precision": precision, "recall": recall, "f1": f1, "support": tp + fn}
    return {"n": len(labels), "coverage": len(answered) / len(labels) if labels else None,
            "selective_accuracy": sum(p == y for p, y in answered) / len(answered) if answered else None,
            "accuracy_abstain_as_error": sum(p == y for p, y in zip(predictions, labels)) / len(labels)
            if labels else None,
            "macro_f1": sum(v["f1"] for v in per_class.values()) / len(per_class) if per_class else None,
            "per_class": per_class, "predictions": predictions}

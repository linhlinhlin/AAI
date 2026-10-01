"""Label-free analysis of one cohort of failing C programs for AAI Lab.

Clusters use the registered deviation OAV (test outcomes plus how each output deviates
from its oracle). Each group gets the test results and output deviations its members
share, one IF-THEN rule induced by ILA-2 on this cohort, and at most one mechanism
hypothesis. Hypotheses come from hand-written rules or from frozen ILA-2 rules learned
on C-Pack repairs; when neither covers most members the group says so instead of guessing.
"""

from collections import Counter

import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

from .. import ila
from ..deviation_features import deviation_oav
from ..domain import Submission
from ..mechanism_eval import CategoricalSpace
from ..mechanism_feedback import FEEDBACK
from ..mechanism_hypotheses import agnostic_values, load_rules, match
from ..semantic_rules import diagnose
from .phrases import ORDER, WEAK, condition_phrase, deviation_phrase, quoted
from .teaching import CATEGORY, advice

MASSES = {"test": 0.3, "dev": 0.4, "agg": 0.3}  # The registered 'deviation' representation.
MAX_K = 6
SHARED = 0.6  # Evidence shown for a group must hold for at least this share of members.
MAJORITY = 0.5  # A hypothesis must cover at least half of a group.
AUTHORED_CATEGORY = {
    "SUM_INPUT": "COMPUTATION", "SUM_SQUARE": "COMPUTATION", "SUM_PREVIOUS": "LOOP_BOUNDARY",
    "COUNT_ZERO": "BRANCH_CONDITION", "MAX_ZERO": "INITIALIZATION", "ARRAY_LAST": "LOOP_BOUNDARY",
    "CIRCLE_RADIUS": "COMPUTATION", "SWAP_COPY": "PARAMETER_PASSING",
    "SWAP_OVERWRITE": "MISSING_STATEMENT", "C_HARDCODED_OUTPUT": "MISSING_STATEMENT",
    "C_BRANCH_ATTACHMENT": "BRANCH_CONDITION", "C_SWAP_BY_VALUE": "PARAMETER_PASSING",
    "OUTPUT_PRESENTATION": "OUTPUT_TEXT",
}
# Lab wording for the general C rules; exercise rules keep their own titles.
TITLES = {
    "C_HARDCODED_OUTPUT": "In ra hằng số, không tính theo dữ liệu nhập",
    "C_BRANCH_ATTACHMENT": "Nhầm quan hệ if–else nên nhiều nhánh cùng chạy",
    "C_SWAP_BY_VALUE": "Hoán vị trên bản sao tham số nên a, b ở main không đổi",
    "OUTPUT_PRESENTATION": "Chỉ lệch cách trình bày output",
}
_RULES = None


def sentence(text):
    return text[:1].upper() + text[1:] if text else text


def frozen_rules():
    global _RULES
    if _RULES is None:
        _RULES = load_rules() or {"rules": []}
    return _RULES


def test_names(tests):
    return {t["test_id"]: t.get("name") or f"Test {i}" for i, t in enumerate(tests, 1)}


def logs_of(item, tests):
    return [{"test_id": t["test_id"], "input": t["input"], "expected": t["expected"],
             "output": item["outputs"].get(t["test_id"]) or ""} for t in tests]


def item_values(item, tests):
    runs = {t["test_id"]: (item["outcomes"].get(t["test_id"], "not_run"),
                           item["outputs"].get(t["test_id"]) or "", t["expected"]) for t in tests}
    values = {f"test:{t['test_id']}": item["outcomes"].get(t["test_id"], "not_run") for t in tests}
    values.update(deviation_oav(runs, {t["expected"] for t in tests}))
    return values


def submission_row(item, problem_id):
    return Submission(item["id"], item.get("author"), problem_id, "c", item["code"], "suite",
                      dict(item["outcomes"]), "")


def hand_written(findings):
    """Exercise rules first, then general C rules; presentation only when nothing else fired."""
    ranked = sorted(findings, key=lambda f: (f["rule_id"] == "OUTPUT_PRESENTATION",
                                             f["rule_id"].startswith("C_")))
    if not ranked:
        return None
    finding = ranked[0]
    rule_id = finding["rule_id"]
    category = AUTHORED_CATEGORY.get(rule_id, "COMPUTATION")
    general = rule_id.startswith("C_") or rule_id == "OUTPUT_PRESENTATION"
    return {"rule_id": rule_id, "category": category,
            "source": "c_rule" if general else "exercise_rule",
            "title": TITLES.get(rule_id) or sentence(finding["then_vi"].removeprefix("Có dấu hiệu ")),
            **advice(category, rule_id)}


def hypotheses_for(item, problem_id, tests):
    """Hand-written finding (if any) and frozen ILA-2 category (if any) for one item."""
    row = submission_row(item, problem_id)
    logs = logs_of(item, tests)
    authored = hand_written(diagnose(row, logs))
    rule = match(frozen_rules(), agnostic_values(row, logs, tests)) if frozen_rules()["rules"] else None
    generic = {"category": rule["then"], "if": rule["if"]} if rule else None
    return authored, generic


def learned(category):
    feedback = FEEDBACK[category]
    return {"source": "cpack_rule", "title": CATEGORY[category]["title"], "category": category,
            "statement": feedback["hypothesis"], **advice(category)}


def choose_k(matrix, distances, requested, n, patterns):
    limit = min(MAX_K, patterns, n - 1)
    if limit < 2:
        return 1, None
    if requested != "auto":
        return max(2, min(int(requested), limit)), None
    best = (None, 2)
    for k in range(2, limit + 1):
        labels = KMeans(n_clusters=k, n_init=10, random_state=42).fit_predict(matrix)
        if 1 < len(set(labels.tolist())) < n:
            score = float(silhouette_score(distances, labels, metric="precomputed"))
            if best[0] is None or score > best[0]:
                best = (score, k)
    return best[1], best[0]


def test_rows(members, values, tests, names):
    rows = []
    for test in tests:
        outcomes = Counter(values[i].get(f"test:{test['test_id']}", "not_run") for i in members)
        failing = len(members) - outcomes.get("pass", 0)
        worst = next((o for o, _ in outcomes.most_common() if o != "pass"), None)
        rows.append({"test_id": test["test_id"], "name": names[test["test_id"]],
                     "failing": failing, "size": len(members), "outcome": worst})
    return rows


def observations(members, values):
    size = len(members)
    numeric = Counter(values[i].get("agg:numbers") for i in members).most_common(1)[0][0] != "none"
    found = []
    for attribute in ORDER:
        if attribute == "other_oracle" and numeric:
            continue  # A number equal to another test's answer is usually a coincidence.
        value, count = Counter(values[i].get(f"agg:{attribute}") for i in members).most_common(1)[0]
        phrase = deviation_phrase(attribute, value)
        if phrase and count / size >= SHARED:
            found.append({"text": phrase, "count": count, "size": size,
                          "weak": (attribute, value) in WEAK})
    return found


def listing(rows):
    names = [quoted(r["name"]) for r in rows]
    return ", ".join(names) if len(names) <= 3 else f"{', '.join(names[:2])} và {len(names) - 2} test khác"


def headline(rows, found):
    """A name for a group without a hypothesis, built only from what its members share."""
    strong = [o["text"] for o in found if not o["weak"]]
    if strong:
        return strong[0]
    failing = [r for r in rows if r["failing"] / r["size"] >= SHARED]
    passing = [r for r in rows if r["failing"] == 0]
    if failing and passing:
        rest = len(failing) + len(passing) == len(rows)
        return f"Đạt {listing(passing)} nhưng sai {'các test còn lại' if rest else listing(failing)}"
    if failing:
        return f"Sai cả {len(rows)} test" if len(failing) == len(rows) else f"Sai {listing(failing)}"
    return found[0]["text"] if found else "Không có biểu hiện chung rõ ràng"


def induced_rules(members_by_group, values, names):
    """ILA-2 on this cohort: attribute-value conditions that single out each group."""
    rows, labels = [], []
    for group, members in members_by_group.items():
        for i in members:
            rows.append({k: v for k, v in values[i].items() if condition_phrase(k, v, names)})
            labels.append(group)
    if len(set(labels)) < 2:
        return {}
    best = {}
    for rule in ila.induce(rows, labels, max_conditions=2, penalty=1.0, min_support=2):
        key = (rule["train_true_positives"], rule["train_precision"] or 0)
        if rule["then"] not in best or key > best[rule["then"]][0]:
            best[rule["then"]] = (key, rule)
    return {group: {"conditions": [condition_phrase(a, v, names) for a, v in rule["if"].items()],
                    "support": rule["train_true_positives"],
                    "matched": rule["train_true_positives"] + rule["train_false_positives"],
                    "size": len(members_by_group[group])}
            for group, (_, rule) in best.items()}


def own_hypothesis(pair):
    authored, generic = pair
    if authored:
        return {"title": authored["title"], "category": authored["category"]}
    if generic and generic["category"] in CATEGORY:
        return {"title": CATEGORY[generic["category"]]["title"], "category": generic["category"]}
    return None


def hypothesis_for_group(members, per_item):
    size = len(members)
    authored = Counter(per_item[i][0]["title"] for i in members if per_item[i][0])
    if authored:
        title, count = authored.most_common(1)[0]
        if count / size >= MAJORITY:
            sample = next(per_item[i][0] for i in members
                          if per_item[i][0] and per_item[i][0]["title"] == title)
            return {key: sample[key] for key in ("source", "title", "category", "question", "activity")} | {
                "family": FEEDBACK[sample["category"]]["name"], "matched": count, "size": size}
    generic = Counter(per_item[i][1]["category"] for i in members if per_item[i][1])
    if generic:
        category, count = generic.most_common(1)[0]
        if count / size >= MAJORITY and category in CATEGORY:
            return learned(category) | {"family": FEEDBACK[category]["name"], "matched": count,
                                        "size": size}
    return None


def analyze(items, tests, problem_id, requested_k="auto"):
    """items: failing submissions {id, author, code, outcomes, outputs[, label]}."""
    names = test_names(tests)
    if not items:
        return {"status": "empty", "n_failing": 0, "k": 0, "silhouette": None, "groups": []}
    values = [item_values(item, tests) for item in items]
    per_item = [hypotheses_for(item, problem_id, tests) for item in items]
    space = CategoricalSpace.fit(values, MASSES)
    categorical = space.transform(values)
    matrix, distances = space.onehot(categorical), space.distances(categorical)
    patterns = len(np.unique(np.round(matrix, 12), axis=0)) if matrix.shape[1] else 1
    n = len(items)
    k, silhouette = (1, None) if n < 4 or patterns < 2 else \
        choose_k(matrix, distances, requested_k, n, patterns)
    labels = np.zeros(n, dtype=int) if k <= 1 else \
        KMeans(n_clusters=k, n_init=10, random_state=42).fit_predict(matrix)
    order = [label for label, _ in Counter(labels.tolist()).most_common()]
    members_by_group = {rank: [i for i in range(n) if labels[i] == label]
                        for rank, label in enumerate(order)}
    rules = induced_rules(members_by_group, values, names) if len(members_by_group) > 1 else {}
    groups = []
    for rank, members in members_by_group.items():
        medoid = members[int(np.argmin(distances[np.ix_(members, members)].sum(axis=1)))]
        hypothesis = hypothesis_for_group(members, per_item)
        rows, found = test_rows(members, values, tests, names), observations(members, values)
        labelled = Counter(items[i]["label"] for i in members if items[i].get("label"))
        owns = Counter(own["title"] for own in (own_hypothesis(per_item[i]) for i in members) if own)
        groups.append({
            "index": rank + 1, "size": len(members), "share": len(members) / n,
            "key": f"{hypothesis['category']}:{hypothesis['title']}" if hypothesis
            else "medoid:" + items[medoid]["id"],
            "title": hypothesis["title"] if hypothesis else headline(rows, found),
            "hypothesis": hypothesis, "tests": rows, "observations": found, "rule": rules.get(rank),
            # Members matched by different hand-written or learned rules: the group mixes mechanisms.
            "mixed": [{"title": title, "count": n} for title, n in owns.most_common()]
            if not hypothesis and len(owns) > 1 else None,
            "representative": items[medoid]["id"],
            "members": [{"id": items[i]["id"], "author": items[i].get("author"),
                         "passed": sum(v == "pass" for v in items[i]["outcomes"].values()),
                         "total": len(items[i]["outcomes"]), "label": items[i].get("label"),
                         "own": own_hypothesis(per_item[i])}
                        for i in sorted(members, key=lambda i: (i != medoid, items[i].get("author") or ""))],
            "verified": {"labelled": sum(labelled.values()), "counts": dict(labelled.most_common())}
            if labelled else None})
    return {"status": "ok", "n_failing": n, "k": len(groups), "silhouette": silhouette,
            "groups": groups}


def describe_submission(item, tests, problem_id):
    names = test_names(tests)
    authored, generic = hypotheses_for(item, problem_id, tests)
    values = item_values(item, tests)
    rows = []
    for test in tests:
        tid = test["test_id"]
        found = [(attribute, values.get(f"dev:{tid}:{attribute}")) for attribute in ORDER]
        found = [pair for pair in found if deviation_phrase(*pair)]
        chosen = [pair for pair in found if pair not in WEAK] or found[:1]
        rows.append({"test_id": tid, "name": names[tid], "input": test["input"],
                     "expected": test["expected"], "output": item["outputs"].get(tid),
                     "outcome": item["outcomes"].get(tid, "not_run"),
                     "observations": [deviation_phrase(*pair) for pair in chosen]})
    hypothesis = None
    if authored:
        hypothesis = {key: authored[key] for key in ("source", "title", "category", "question", "activity")}
        hypothesis["family"] = FEEDBACK[authored["category"]]["name"]
    elif generic and generic["category"] in CATEGORY:
        hypothesis = learned(generic["category"]) | {"family": FEEDBACK[generic["category"]]["name"]}
    return {"id": item["id"], "author": item.get("author"), "code": item["code"], "tests": rows,
            "passed": sum(r["outcome"] == "pass" for r in rows), "total": len(rows),
            "hypothesis": hypothesis, "label": item.get("label")}

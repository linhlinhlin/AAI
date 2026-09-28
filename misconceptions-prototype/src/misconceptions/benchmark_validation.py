"""Validation-only diagnostics. No human labels enter representation or cluster fitting."""

import json
from collections import Counter, defaultdict
from itertools import combinations

import numpy as np
from sklearn.metrics import adjusted_rand_score

from .research_io import digest


def load_runs(folder):
    summary = json.loads((folder / "summary.json").read_text(encoding="utf-8"))
    if summary.get("evaluation") != "validation_only":
        raise ValueError("Only validation runs are allowed by this development protocol")
    runs = []
    for item in summary["runs"]:
        path = (folder / item["artifact"]).resolve()
        if not path.is_relative_to(folder.resolve()):
            raise ValueError("Run path escapes the run directory")
        report = json.loads(path.read_text(encoding="utf-8"))
        if report.get("status") == "ok" and report["split"]["evaluation_partition"] != "validation":
            raise ValueError("Sealed test results are not accepted")
        runs.append((item, report))
    return runs


def mean(values):
    values = [v for v in values if v is not None]
    return float(np.mean(values)) if values else None


def summarize_runs(folder):
    runs = load_runs(folder)
    groups = defaultdict(list)
    hashes = {"summary.json": digest(folder / "summary.json"),
              "run_manifest.json": digest(folder / "run_manifest.json")}
    rows = []
    for item, report in runs:
        hashes[item["artifact"]] = digest(folder / item["artifact"])
        if report["status"] != "ok":
            continue
        explanation = report["explanation"]
        rules = explanation["rules"]
        n = len(report["holdout_assignments"])
        groups[(item["problem"], item["method"], item["mode"])].append((item, report))
        rows.append({"problem": item["problem"], "method": item["method"], "mode": item["mode"],
                     "seed": item["seed"], "n_train": len(report["train_assignments"]), "n_validation": n,
                     "silhouette_train": report["silhouette_train"],
                     "rule_fidelity": explanation["holdout_fidelity"],
                     "majority_fidelity": explanation["holdout_majority_baseline_fidelity"],
                     "fidelity_gain_over_majority": explanation["holdout_fidelity"] -
                     explanation["holdout_majority_baseline_fidelity"],
                     "n_rules": len(rules), "mean_conditions": mean([len(r["if"]) for r in rules]),
                     "validation_coverage": sum(r["holdout_support"] for r in rules) / n,
                     "rules_without_validation_support": sum(r["holdout_support"] == 0 for r in rules),
                     "assignment_tie_rate": report["holdout_assignment_ties"] / n})
    stability = []
    for (problem, method, mode), items in sorted(groups.items()):
        pairs = []
        for (li, left), (ri, right) in combinations(items, 2):
            a, b = left["holdout_assignments"], right["holdout_assignments"]
            if set(a) != set(b) or set(left["train_assignments"]) != set(right["train_assignments"]):
                raise ValueError("Seed comparisons require exactly the same locked split")
            ids = sorted(a)
            pairs.append({"seeds": [li["seed"], ri["seed"]], "n": len(ids),
                          "ari": float(adjusted_rand_score([a[i] for i in ids], [b[i] for i in ids]))
                          if len(ids) >= 2 else None})
        stability.append({"problem": problem, "method": method, "mode": mode,
                          "seed_pairs": pairs, "mean_validation_ari": mean([p["ari"] for p in pairs])})
    aggregate = []
    for method, mode in sorted({(r["method"], r["mode"]) for r in rows}):
        group = [r for r in rows if (r["method"], r["mode"]) == (method, mode)]
        aggregate.append({"method": method, "mode": mode, "n_ok": len(group),
                          **{key: mean([r[key] for r in group]) for key in
                             ("rule_fidelity", "majority_fidelity", "fidelity_gain_over_majority",
                              "validation_coverage", "assignment_tie_rate")}})
    return {"schema_version": 1, "scope": "validation_only_development_diagnostics",
            "n_runs": len(runs), "statuses": dict(Counter(r["status"] for _, r in runs)),
            "mechanism_accuracy": None, "misconception_accuracy": None,
            "reason": "Independent human annotations are required for external quality metrics.",
            "aggregation": "unweighted means across successful problem/seed runs; not independent replicates",
            "input_sha256": hashes, "per_run": rows, "aggregate": aggregate, "stability": stability}

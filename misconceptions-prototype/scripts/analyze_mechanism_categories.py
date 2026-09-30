"""Exploratory per-category analysis of the registered test run (amendment A7).

For each benchmark's primary scope and representation, a category counts as recovered
for an item when the item's cluster has that category as its majority label. Also counts
signature collisions: pairs in one cohort with identical test signatures but different
mechanisms. Nothing here is a registered hypothesis.
"""

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

from misconceptions.research_io import write_json

SCOPE = {"real": "full", "injected": "partition"}
REPS = ("exact_signature", "outcomes", "combined_stdout", "deviation", "evidence", "embedding")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = json.loads(args.results.read_text(encoding="utf-8"))
    out = {"status": "exploratory_not_registered", "benchmarks": {}}
    lines = ["# Exploratory per-category recovery (test run)", "",
             "Share of items whose K-means cluster (oracle k, seed 42) has their category as majority.", ""]
    for benchmark, result in report["benchmarks"].items():
        scope = result["scopes"].get(SCOPE[benchmark])
        if not scope or not scope["cohorts"]:
            continue
        recovered = {rep: Counter() for rep in REPS}
        totals = Counter()
        collisions = Counter()
        pairs_same_signature = 0
        for cohort in scope["cohorts"]:
            labels = [item["label"] for item in cohort["items"]]
            totals.update(labels)
            for rep in REPS:
                assignment = cohort["assignments"].get(rep)
                if assignment is None:
                    continue
                majority = {}
                for cluster in set(assignment):
                    members = [labels[i] for i, c in enumerate(assignment) if c == cluster]
                    majority[cluster] = Counter(members).most_common(1)[0][0]
                for i, cluster in enumerate(assignment):
                    recovered[rep][labels[i]] += majority[cluster] == labels[i]
            signature = cohort["assignments"]["exact_signature"]
            groups = defaultdict(list)
            for i, key in enumerate(signature):
                groups[key].append(labels[i])
            for members in groups.values():
                for a in range(len(members)):
                    for b in range(a + 1, len(members)):
                        pairs_same_signature += 1
                        if members[a] != members[b]:
                            collisions[tuple(sorted((members[a], members[b])))] += 1
        table = {rep: {category: recovered[rep][category] / totals[category] for category in totals}
                 for rep in REPS}
        out["benchmarks"][benchmark] = {
            "scope": SCOPE[benchmark], "items_per_category": dict(totals.most_common()),
            "recovered_share": table,
            "same_signature_pairs": pairs_same_signature,
            "same_signature_different_mechanism_pairs": sum(collisions.values()),
            "top_collisions": [{"pair": list(k), "count": v} for k, v in collisions.most_common(10)]}
        lines += [f"## {benchmark} ({SCOPE[benchmark]} scope)", "",
                  "| Category | n | " + " | ".join(REPS) + " |", "|---|---:|" + "---:|" * len(REPS)]
        for category, n in totals.most_common():
            lines.append(f"| {category} | {n} | " + " | ".join(
                f"{table[rep].get(category, 0):.2f}" for rep in REPS) + " |")
        share = sum(collisions.values()) / pairs_same_signature if pairs_same_signature else 0
        sentence = (f"Pairs with identical test signatures: {pairs_same_signature}; "
                    f"with different mechanisms: {sum(collisions.values())} ({share:.1%}).")
        lines += ["", sentence, ""]
    args.output.mkdir(parents=True, exist_ok=True)
    write_json(args.output / "categories.json", out)
    (args.output / "categories.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

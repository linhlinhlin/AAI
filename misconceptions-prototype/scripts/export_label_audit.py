"""Export a stratified audit packet of repair-grounded labels (train/validation only).

Each case shows the failing program, the unified diff of its verified minimal repair and
the assigned category. Reviewers record `agree`, `disagree` (with the category they would
assign) or `unclear`. Test-partition items are never exported.
"""

import argparse
import difflib
import json
import random
from collections import defaultdict
from pathlib import Path

from misconceptions.research_io import digest, read_cohorts, write_json


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--bench", type=Path, required=True)
    parser.add_argument("--per-category", type=int, default=5)
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    sources = {row.submission_id: row.source_code
               for _, _, rows in read_cohorts(args.data) for row in rows}
    by_category = defaultdict(list)
    for line in (args.bench / "real_repairs.jsonl").read_text(encoding="utf-8").splitlines():
        repair = json.loads(line)
        if repair.get("status") == "ok" and repair["partition"] in ("train", "validation") \
                and repair.get("one_minimal"):
            by_category[repair["primary"]].append(repair)
    rng = random.Random(args.seed)
    cases = []
    for category in sorted(by_category):
        pool = sorted(by_category[category], key=lambda r: r["item_id"])
        for repair in rng.sample(pool, min(args.per_category, len(pool))):
            failing = sources[repair["item_id"]]
            diff = "".join(difflib.unified_diff(
                failing.splitlines(keepends=True), repair["patched_source"].splitlines(keepends=True),
                "failing.c", "minimal_repair.c", n=2))
            cases.append({"case_id": f"audit-{len(cases) + 1:03d}", "item_id": repair["item_id"],
                          "problem_id": repair["problem_id"], "partition": repair["partition"],
                          "assigned_primary": repair["primary"], "assigned_categories": repair["categories"],
                          "details": repair["details"], "hunks_minimal": repair["hunks_minimal"],
                          "diff": diff, "failing_source": failing,
                          "review": {"decision": None, "reviewer_category": None, "note": None}})
    packet = {"schema": "repair_label_audit_v1", "bench_manifest_sha256": digest(args.bench / "manifest.json"),
              "sampling": {"per_category": args.per_category, "seed": args.seed,
                           "partitions": ["train", "validation"]},
              "instructions": "Judge only whether the category describes what the minimal repair changes "
                              "in the program. Do not judge the student's beliefs.",
              "cases": cases}
    args.output.mkdir(parents=True, exist_ok=True)
    write_json(args.output / "audit_packet.json", packet)
    lines = ["# Repair-label audit packet", "", packet["instructions"], ""]
    for case in cases:
        lines += [f"## {case['case_id']} · {case['problem_id']} · assigned {case['assigned_primary']}", "",
                  f"Details: {', '.join(case['details'][:4])}", "", "```diff", case["diff"].rstrip(), "```", ""]
    (args.output / "audit_packet.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{len(cases)} cases from {len(by_category)} categories")


if __name__ == "__main__":
    main()

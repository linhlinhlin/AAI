"""Descriptive statistics of the mechanism benchmarks (label counts, repair sizes, cohorts)."""

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

from misconceptions.research_io import digest, read_cohorts, write_json

EXCLUDED = ("MULTI", "OTHER", "NO_CHANGE")


def eligible(items, key):
    per = defaultdict(list)
    for item in items:
        per[item["problem_id"]].append(item[key])
    return sum(1 for labels in per.values() if len(labels) >= 6 and len(set(labels)) >= 2)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bench", type=Path, required=True)
    parser.add_argument("--unstable", type=Path, required=True)
    parser.add_argument("--data", type=Path, help="imported corpus for corpus-level facts")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    unstable = set(json.loads(args.unstable.read_text(encoding="utf-8"))["outcome_differing_ids"])
    real = [json.loads(line) for line in (args.bench / "real_repairs.jsonl").read_text(encoding="utf-8").splitlines()]
    injected = [json.loads(line) for line in (args.bench / "injected.jsonl").read_text(encoding="utf-8").splitlines()]
    ok = [r for r in real if r["status"] == "ok"]
    gold = [r for r in ok if r["one_minimal"] and r["primary"] not in EXCLUDED and r["item_id"] not in unstable]
    injected = [m for m in injected if m["source_submission_id"] not in unstable]
    stats = {
        "bench_manifest_sha256": digest(args.bench / "manifest.json"),
        "real": {
            "repair_events": len(real), "status": dict(Counter(r["status"] for r in real)),
            "one_minimal": sum(r["one_minimal"] for r in ok),
            "hunks_minimal": dict(sorted(Counter(min(r["hunks_minimal"], 5) for r in ok).items())),
            "hunks_total_mean": sum(r["hunks_total"] for r in ok) / len(ok),
            "hunks_minimal_mean": sum(r["hunks_minimal"] for r in ok) / len(ok),
            "probes_total": sum(r["probes"] for r in ok),
            "primary_all": dict(Counter(r["primary"] for r in ok).most_common()),
            "gold": len(gold), "gold_by_partition": dict(Counter(r["partition"] for r in gold)),
            "gold_labels": dict(Counter(r["primary"] for r in gold).most_common()),
            "gold_labels_by_partition": {p: dict(Counter(r["primary"] for r in gold if r["partition"] == p))
                                         for p in ("train", "validation", "test")},
            "eligible_cohorts": {p: eligible([r for r in gold if r["partition"] == p], "primary")
                                 for p in ("train", "validation", "test")} | {"full": eligible(gold, "primary")},
            "unstable_excluded": sum(1 for r in real if r["item_id"] in unstable),
        },
        "injected": {
            "mutants": len(injected), "by_partition": dict(Counter(m["partition"] for m in injected)),
            "labels": dict(Counter(m["category"] for m in injected).most_common()),
            "operators": dict(Counter(m["operator"] for m in injected).most_common()),
            "sources": len({m["source_submission_id"] for m in injected}),
            "eligible_cohorts": {p: eligible([m for m in injected if m["partition"] == p], "category")
                                 for p in ("train", "validation", "test")},
        },
    }
    manifest = json.loads((args.bench / "manifest.json").read_text(encoding="utf-8"))
    if "summary" in manifest:
        stats["injected"]["build_status"] = manifest["summary"].get("injected", {}).get("status")
    parent = args.bench.parent / "mechanism-bench-v1" / "manifest.json"
    if parent.exists():
        build = json.loads(parent.read_text(encoding="utf-8"))
        stats["injected"]["build_status"] = build["summary"]["injected"]["status"]
        stats["build"] = {"image": build["image"], "budget": build["budget"], "seed": build["seed"],
                          "max_sources": build["max_sources"], "elapsed_seconds": build["elapsed_seconds"]}
    if "label_transitions" in manifest:
        stats["relabel"] = {"transitions": manifest["label_transitions"], "audit": manifest["audit"]}
    if args.data:
        rows = [row for _, _, cohort in read_cohorts(args.data) for row in cohort]
        suites = {row.problem_id: len(row.outcomes) for row in rows}
        stats["corpus"] = {
            "submissions": len(rows), "students": len({row.student_id for row in rows}),
            "problems": len(suites), "tests": sum(suites.values()),
            "historical_cells": sum(len(row.outcomes) for row in rows),
            "historical_not_run_cells": sum(v == "not_run" for row in rows for v in row.outcomes.values()),
            "empty_sources": sum(not row.source_code.strip() for row in rows)}
    write_json(args.output, stats)
    print(json.dumps({k: v for k, v in stats["real"].items() if k != "primary_all"}, indent=1))


if __name__ == "__main__":
    main()

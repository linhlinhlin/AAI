"""Compare two independent replays of the same corpus (reproducibility check)."""

import argparse
import json
from collections import Counter
from pathlib import Path

from misconceptions.replay import POLICY_DEFAULT, outcomes_from_record
from misconceptions.research_io import write_json


def records(folder):
    result = {}
    for path in sorted((folder / "cohorts").glob("*/replay.jsonl")):
        for line in path.read_text(encoding="utf-8").splitlines():
            record = json.loads(line)
            result[record["submission_id"]] = (path.parent.name, record)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--first", type=Path, required=True)
    parser.add_argument("--second", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    first, second = records(args.first), records(args.second)
    if set(first) != set(second):
        raise ValueError("Replays cover different submissions")
    tests = {path.parent.name: json.loads(path.read_text(encoding="utf-8"))
             for path in (args.data / "cohorts").glob("*/tests.json")}
    counts, differing = Counter(), []
    for sid in sorted(first):
        problem, a = first[sid]
        _, b = second[sid]
        oa = outcomes_from_record(a, tests[problem], **POLICY_DEFAULT)
        ob = outcomes_from_record(b, tests[problem], **POLICY_DEFAULT)
        if oa is None and ob is None:
            counts["no_evidence_both"] += 1
            continue
        if oa is None or ob is None:
            counts["evidence_in_one_run_only"] += 1
            differing.append(sid)
            continue
        sa = {t["test_id"]: t["stdout_sha256"] for t in a["tests"]}
        sb = {t["test_id"]: t["stdout_sha256"] for t in b["tests"]}
        if oa == ob and sa == sb:
            counts["identical_outcomes_and_stdout"] += 1
        elif oa == ob:
            counts["identical_outcomes_stdout_differs"] += 1
        else:
            counts["outcomes_differ"] += 1
            differing.append(sid)
        for tid in oa:
            counts["cells_total"] += 1
            counts["cells_equal"] += oa[tid] == ob[tid]
    report = {"counts": dict(counts), "outcome_differing_ids": differing,
              "cell_agreement": counts["cells_equal"] / max(1, counts["cells_total"])}
    write_json(args.output, report)
    print(json.dumps({k: v for k, v in report.items() if k != "outcome_differing_ids"}, indent=1))


if __name__ == "__main__":
    main()

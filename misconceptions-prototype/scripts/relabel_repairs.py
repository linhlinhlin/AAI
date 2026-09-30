"""Re-classify stored verified minimal repairs with the current classifier (no execution).

Writes a new benchmark directory: real_repairs.jsonl with updated categories, the
unchanged injected.jsonl, label transitions and, if given, agreement with an audit.
The minimal repairs themselves (hunks, probes, patched sources) are copied unchanged.
"""

import argparse
import hashlib
import json
import shutil
from collections import Counter
from pathlib import Path

from misconceptions.repair_labels import classify_repair
from misconceptions.research_io import digest, implementation_fingerprint, read_cohorts, write_json

ROOT = Path(__file__).resolve().parents[2]
CLASSIFIER = ROOT / "misconceptions-prototype/src/misconceptions/repair_labels.py"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--bench", type=Path, required=True)
    parser.add_argument("--audit", type=Path, help="audit_decisions.json to score before/after")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    implementation = implementation_fingerprint(ROOT)
    args.output.mkdir(parents=True, exist_ok=False)
    sources = {row.submission_id: row.source_code for _, _, rows in read_cohorts(args.data) for row in rows}
    old_rows = [json.loads(line) for line in
                (args.bench / "real_repairs.jsonl").read_text(encoding="utf-8").splitlines()]
    new_rows, transitions = [], Counter()
    for row in old_rows:
        updated = dict(row)
        if row["status"] == "ok":
            label = classify_repair(sources[row["item_id"]], row["patched_source"])
            updated.update(categories=label["categories"], details=label["details"],
                           primary=label["primary"])
            transitions[f"{row['primary']}->{updated['primary']}"] += 1
        new_rows.append(updated)
    (args.output / "real_repairs.jsonl").write_text(
        "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in new_rows), encoding="utf-8")
    shutil.copy(args.bench / "injected.jsonl", args.output / "injected.jsonl")
    audit = None
    if args.audit:
        decisions = json.loads(args.audit.read_text(encoding="utf-8"))["decisions"]
        packet = json.loads((args.audit.parent / "audit_packet.json").read_text(encoding="utf-8"))
        by_item = {r["item_id"]: r for r in new_rows}
        audit = {"cases": len(packet["cases"]), "before": Counter(), "after": Counter()}
        for case in packet["cases"]:
            expected = decisions[case["case_id"]]["category"]
            audit["before"]["agree" if case["assigned_primary"] == expected else "disagree"] += 1
            audit["after"]["agree" if by_item[case["item_id"]]["primary"] == expected else "disagree"] += 1
        single = [c for c in packet["cases"] if c["assigned_primary"] not in ("MULTI", "OTHER", "NO_CHANGE")]
        audit["single_label_precision_before"] = sum(
            c["assigned_primary"] == decisions[c["case_id"]]["category"] for c in single) / len(single)
        audit["before"], audit["after"] = dict(audit["before"]), dict(audit["after"])
    parent = json.loads((args.bench / "manifest.json").read_text(encoding="utf-8"))
    write_json(args.output / "manifest.json", {
        "schema_version": 1, "derived_from": str(args.bench.name),
        "parent_manifest_sha256": digest(args.bench / "manifest.json"),
        "parent_image": parent.get("image"), "classifier_sha256": digest(CLASSIFIER),
        "label_transitions": dict(transitions.most_common()), "audit": audit,
        "primary": dict(Counter(r.get("primary") for r in new_rows if r["status"] == "ok")),
        "implementation": implementation,
        "files_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in sorted(args.output.glob("*.jsonl"))}})
    print(json.dumps({"transitions": {k: v for k, v in transitions.items() if k.split("->")[0] != k.split("->")[1]},
                      "audit": audit}, indent=1))


if __name__ == "__main__":
    main()

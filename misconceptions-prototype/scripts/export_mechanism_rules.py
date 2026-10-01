"""Export the frozen ILA-2 mechanism rules for the learning app.

Rules are induced exactly as in the registered run (training-partition real items,
problem-agnostic evidence attributes, frozen penalty) and are shipped with their
held-out measurements, so the app can show a rule as a checked hypothesis.
"""

import argparse
import importlib.util
import json
from pathlib import Path

from misconceptions import ila
from misconceptions.research_io import digest, write_json

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("run_mechanism_eval", HERE / "run_mechanism_eval.py")
rme = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rme)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--replay", type=Path, required=True)
    parser.add_argument("--bench", type=Path, required=True)
    parser.add_argument("--split-lock", type=Path, required=True)
    parser.add_argument("--unstable", type=Path, required=True)
    parser.add_argument("--test-results", type=Path, required=True,
                        help="results.json of the registered test run (for held-out metrics)")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    results = json.loads(args.test_results.read_text(encoding="utf-8"))
    manifest = json.loads((args.test_results.parent / "run_manifest.json").read_text(encoding="utf-8"))
    penalty = manifest["penalty"]
    rme.SPLIT.update(json.loads(args.split_lock.read_text(encoding="utf-8"))["assignments"])
    unstable = frozenset(json.loads(args.unstable.read_text(encoding="utf-8"))["outcome_differing_ids"])
    items, _, _, _ = rme.load_items(args.data, args.replay, args.bench, unstable)
    train = [i for i in items["real"] if i["partition"] == "train"]
    rows = [{k: v for k, v in i["values"].items() if k.startswith(("agg:", "code:"))} for i in train]
    rules = ila.induce(rows, [i["label"] for i in train], max_conditions=2, penalty=penalty,
                       min_support=3)
    held_out = results["benchmarks"]["real"]["rules"]
    write_json(args.output, {
        "schema": "mechanism_rules_v1", "algorithm": "ILA-2", "penalty": penalty,
        "attributes": "problem-agnostic evidence (agg:*, code:*)",
        "trained_on": f"{len(train)} training-partition repair-grounded items of C-Pack-IPAs",
        "held_out": {track: {k: held_out[f"{track}|evidence|ila2"].get(k)
                             for k in ("macro_f1", "coverage", "selective_accuracy", "n")}
                     for track in ("seen_problems", "unseen_problems")
                     if f"{track}|evidence|ila2" in held_out},
        "test_results_sha256": digest(args.test_results),
        "status": "hypothesis_rules_not_diagnoses",
        "rules": rules})
    print(f"{len(rules)} rules exported")


if __name__ == "__main__":
    main()

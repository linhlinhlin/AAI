"""Replay every imported C-Pack-IPAs submission in the isolated research runner.

Produces per-cohort replay records, a determinism re-run on a seeded sample and an
oracle audit against the historical verdicts. The historical import is never edited.
"""

import argparse
import hashlib
import json
import platform
import random
import subprocess
import time
from collections import Counter, defaultdict
from pathlib import Path

from misconceptions.cpack import VERDICTS
from misconceptions.replay import (
    CPACK_FLAGS,
    SERVER,
    image_id,
    outcomes_from_record,
    request_for,
    run_requests,
    stored_test,
)
from misconceptions.research_io import digest, implementation_fingerprint, read_cohorts, write_json

ROOT = Path(__file__).resolve().parents[2]
POLICIES = {
    "exact_exit0": {"pass_relations": ("exact",), "exit_code_matters": True},
    "exact_any_exit": {"pass_relations": ("exact",), "exit_code_matters": False},
    "trailing_ws_exit0": {"pass_relations": ("exact", "trailing_whitespace"), "exit_code_matters": True},
    "tokens_exit0": {"pass_relations": ("exact", "trailing_whitespace", "whitespace"),
                     "exit_code_matters": True},
}


def load(data):
    cohorts = {}
    for folder, manifest, rows in read_cohorts(data):
        tests = json.loads((folder / "tests.json").read_text(encoding="utf-8"))
        reviews = {}
        for line in (folder / "review.jsonl").read_text(encoding="utf-8").splitlines():
            record = json.loads(line)
            reviews[record["submission_id"]] = record
        cohorts[manifest["problem_id"]] = {"tests": tests, "rows": rows, "reviews": reviews,
                                           "manifest": manifest}
    return cohorts


def normalize(response, tests):
    if "infrastructure_error" in response:
        return {"submission_id": response["id"], "infrastructure_error": response["infrastructure_error"]}
    compile_info = response["compile"]
    return {"submission_id": response["id"],
            "compile": {"returncode": compile_info["returncode"], "signal": compile_info["signal"],
                        "timeout": compile_info["timeout"],
                        "warning_free": compile_info["warning_free"],
                        "diagnostics": compile_info["diagnostics"][:2000]},
            "tests": [stored_test(test, tests[test["test_id"]]["expected"])
                      for test in response["tests"]]}


def audit(cohorts, records, split):
    report = {"policies": {}, "compile": Counter(), "stdout_reproduction": Counter(),
              "stdout_mismatch_examples": []}
    historical_cells = []
    for problem, cohort in cohorts.items():
        for row in cohort["rows"]:
            review = cohort["reviews"][row.submission_id]
            record = records[row.submission_id]
            replay_ok = "compile" in record and record["compile"]["returncode"] == 0
            werror_ok = replay_ok and record["compile"]["warning_free"]
            historical = review["compile_status"]
            if historical in ("compile_error", "compiled_in_historical_run"):
                report["compile"][f"historical={historical}|replay_compiles={replay_ok}"
                                  f"|warning_free={werror_ok}"] += 1
            if historical != "compiled_in_historical_run" or not replay_ok:
                continue
            by_test = {test["test_id"]: test for test in record["tests"]}
            for logged in review["logged_tests"]:
                if logged["verdict"] != "WRONG_ANSWER":
                    continue
                test = by_test.get(logged["test_id"])
                same = test is not None and test["stdout"] == logged["output"]
                report["stdout_reproduction"]["same" if same else "different"] += 1
                if not same and len(report["stdout_mismatch_examples"]) < 20:
                    report["stdout_mismatch_examples"].append(
                        {"submission_id": row.submission_id, "test_id": logged["test_id"]})
            historical_cells.append((row.submission_id, problem, review["historical_verdicts"]))
    for name, policy in POLICIES.items():
        agreement = defaultdict(Counter)
        confusion = Counter()
        for submission_id, problem, verdicts in historical_cells:
            outcomes = outcomes_from_record(records[submission_id], cohorts[problem]["tests"], **policy)
            if outcomes is None:
                continue
            for tid, verdict in verdicts.items():
                expected = VERDICTS.get(verdict, "runtime_error")
                if expected == "not_run":
                    continue
                partition = split[submission_id]
                agreement[partition]["agree" if outcomes[tid] == expected else "disagree"] += 1
                confusion[f"{expected}->{outcomes[tid]}"] += 1
        report["policies"][name] = {
            "policy": {key: list(value) if isinstance(value, tuple) else value
                       for key, value in policy.items()},
            "agreement_by_partition": {part: dict(counts) for part, counts in agreement.items()},
            "confusion_historical_to_replay": dict(confusion.most_common())}
    train = {name: value["agreement_by_partition"].get("train", {})
             for name, value in report["policies"].items()}
    # Policy choice uses train cells only; validation/test agreement is reported, not tuned on.
    report["selected_policy"] = max(train, key=lambda name: (
        train[name].get("agree", 0) / max(1, sum(train[name].values())), name == "exact_exit0"))
    report["selection_rule"] = "highest train-partition cell agreement with historical verdicts"
    report["compile"] = dict(report["compile"])
    report["stdout_reproduction"] = dict(report["stdout_reproduction"])
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--split-lock", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--determinism-fraction", type=float, default=0.1)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--problems", nargs="*", help="Development subset; omit for the full corpus")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    cohorts = load(args.data)
    if args.problems:
        cohorts = {problem: cohorts[problem] for problem in args.problems}
    split = json.loads(args.split_lock.read_text(encoding="utf-8"))["assignments"]
    image = image_id()
    gcc = subprocess.run(["docker", "run", "--rm", "--network=none", image, "gcc", "--version"],
                         capture_output=True, text=True, check=True).stdout.splitlines()[0]
    tests_of = {row.submission_id: cohort["tests"] for cohort in cohorts.values()
                for row in cohort["rows"]}
    requests, skipped = [], {}
    for cohort in cohorts.values():
        for row in cohort["rows"]:
            if not row.source_code.strip():
                skipped[row.submission_id] = "empty_source"
                continue
            requests.append(request_for(row.submission_id, row.source_code, cohort["tests"]))
    started = time.time()
    records = {sid: {"submission_id": sid, "skipped": reason} for sid, reason in skipped.items()}
    for response in run_requests(requests, args.workers, image,
                                 progress=lambda d, t: print(f"replay {d}/{t}", flush=True)):
        records[response["id"]] = normalize(response, tests_of[response["id"]])
    elapsed = time.time() - started
    # Determinism: a seeded sample of compiled programs is executed a second time.
    compiled = sorted(sid for sid, record in records.items()
                      if record.get("compile", {}).get("returncode") == 0)
    sample = sorted(random.Random(args.seed).sample(
        compiled, round(len(compiled) * args.determinism_fraction)))
    by_id = {request["id"]: request for request in requests}
    determinism = Counter()
    unstable = []
    for response in run_requests([by_id[sid] for sid in sample], args.workers, image):
        second = normalize(response, tests_of[response["id"]])
        first = records[response["id"]]
        if "infrastructure_error" in second:
            determinism["rerun_infrastructure_error"] += 1
            continue
        a = {t["test_id"]: (t["stdout_sha256"], t["exit_code"], t["signal"], t["timeout"])
             for t in first["tests"]}
        b = {t["test_id"]: (t["stdout_sha256"], t["exit_code"], t["signal"], t["timeout"])
             for t in second["tests"]}
        if a == b:
            determinism["identical"] += 1
        else:
            determinism["different"] += 1
            unstable.append(response["id"])
    for problem, cohort in cohorts.items():
        lines = [json.dumps(records[row.submission_id], ensure_ascii=False)
                 for row in sorted(cohort["rows"], key=lambda r: r.submission_id)]
        target = args.output / "cohorts" / problem
        target.mkdir(parents=True, exist_ok=True)
        (target / "replay.jsonl").write_text("\n".join(lines) + "\n", encoding="utf-8")
    report = audit(cohorts, records, split)
    report["determinism"] = {"sample_size": len(sample), **determinism, "unstable_ids": unstable}
    status = Counter()
    for record in records.values():
        if "skipped" in record:
            status[record["skipped"]] += 1
        elif "infrastructure_error" in record:
            status["infrastructure_error"] += 1
        elif record["compile"]["returncode"] != 0:
            status["compile_error"] += 1
        else:
            status["compiled"] += 1
    report["status"] = dict(status)
    write_json(args.output / "oracle_audit.json", report)
    write_json(args.output / "replay_manifest.json", {
        "schema_version": 1, "problems": sorted(cohorts), "input_dataset": str(args.data.resolve().name),
        "input_dataset_complete_sha256": digest(args.data / "dataset_complete.json"),
        "split_lock_sha256": digest(args.split_lock), "image": image, "compiler": gcc,
        "flags": CPACK_FLAGS, "flags_note": "historical command also used -Werror; recorded "
        "as compile.warning_free instead of rejecting", "server_sha256": digest(SERVER),
        "limits": {"run_wall_seconds": 5, "run_cpu_seconds": 3, "address_space_bytes": 512 << 20,
                   "stdout_cap_bytes": 2 << 20, "stored_stdout_bytes": 65536,
                   "container": "network none, read-only root, cap-drop ALL + CHOWN/SETUID/SETGID/KILL,"
                                " no-new-privileges, pids 128, 1 CPU, 1 GiB"},
        "workers": args.workers, "elapsed_seconds": round(elapsed, 1),
        "host": {"platform": platform.platform(), "python": platform.python_version()},
        "implementation": implementation_fingerprint(ROOT),
        "records_sha256": {p.parent.name: hashlib.sha256(p.read_bytes()).hexdigest()
                           for p in sorted((args.output / "cohorts").glob("*/replay.jsonl"))}})
    print(json.dumps({"status": report["status"], "determinism": determinism,
                      "selected_policy": report["selected_policy"]}, indent=1))


if __name__ == "__main__":
    main()

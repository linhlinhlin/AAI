"""Build the two mechanism benchmarks from the replayed C-Pack-IPAs corpus.

real:     failing submission + the same student's next passing submission, reduced by
          hunk-level delta debugging to a verified minimal repair and classified by AST.
injected: one controlled single-mechanism edit applied to an accepted program, kept only
          when it compiles without warnings and fails at least one test.

Both label sets are evaluation data. Split partitions are inherited from the corpus lock.
"""

import argparse
import hashlib
import json
import random
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from misconceptions.mechanism_inject import one_mutant_per_category
from misconceptions.repair_labels import (
    apply_hunks,
    classify_repair,
    ddmin,
    line_hunks,
    pair_repairs,
)
from misconceptions.replay import (
    POLICY_DEFAULT,
    ReplayPool,
    image_id,
    outcomes_from_record,
    request_for,
    stored_test,
)
from misconceptions.research_io import digest, implementation_fingerprint, read_cohorts, write_json

ROOT = Path(__file__).resolve().parents[2]
POLICY = POLICY_DEFAULT


def load(data, replay):
    cohorts = {}
    for folder, manifest, rows in read_cohorts(data):
        problem = manifest["problem_id"]
        tests = json.loads((folder / "tests.json").read_text(encoding="utf-8"))
        reviews = {json.loads(line)["submission_id"]: json.loads(line)
                   for line in (folder / "review.jsonl").read_text(encoding="utf-8").splitlines()}
        records = {json.loads(line)["submission_id"]: json.loads(line) for line in
                   (replay / "cohorts" / problem / "replay.jsonl").read_text(encoding="utf-8").splitlines()}
        cohorts[problem] = {"tests": tests, "rows": rows, "reviews": reviews, "records": records}
    return cohorts


def response_outcomes(response, tests):
    if "infrastructure_error" in response:
        return None
    record = {"compile": response["compile"],
              "tests": [stored_test(t, tests[t["test_id"]]["expected"]) for t in response["tests"]]}
    return outcomes_from_record(record, tests, **POLICY), record


def minimal_repair(pool, row, later, tests, budget):
    old, new, opcodes = line_hunks(row.source_code, later.source_code)
    hunks = [i for i, op in enumerate(opcodes) if op[0] != "equal"]
    cache, counter = {}, [0]

    def passes(candidates):
        pending = {}
        for candidate in candidates:
            key = tuple(sorted(candidate))
            if key not in cache and key not in pending:
                counter[0] += 1
                source = apply_hunks(old, new, opcodes, set(key))
                pending[key] = pool.submit(request_for(f"{row.submission_id}#p{counter[0]}", source, tests))
        for key, future in pending.items():
            outcome = response_outcomes(future.result(), tests)
            cache[key] = bool(outcome and outcome[0] and all(v == "pass" for v in outcome[0].values()))
        return [cache[tuple(sorted(candidate))] for candidate in candidates]

    if not hunks:
        return None
    # Verify the endpoints in the same runner before searching between them.
    full_ok, empty_ok = passes([hunks, []])
    if not full_ok or empty_ok:
        return {"status": "endpoint_check_failed", "full_passes": full_ok, "empty_passes": empty_ok,
                "hunks_total": len(hunks)}
    subset, probes, minimal = ddmin(hunks, passes, budget)
    patched = apply_hunks(old, new, opcodes, set(subset))
    label = classify_repair(row.source_code, patched)
    changed = sum(max(opcodes[i][2] - opcodes[i][1], opcodes[i][4] - opcodes[i][3]) for i in subset)
    return {"status": "ok", "hunks_total": len(hunks), "hunks_minimal": len(subset),
            "one_minimal": minimal, "probes": probes + 2, "changed_lines": changed,
            "patched_sha256": hashlib.sha256(patched.encode()).hexdigest(),
            "patched_source": patched, **label}


def build_real(cohorts, pool, split, budget, threads):
    jobs = []
    for problem, cohort in cohorts.items():
        outcomes = {sid: outcomes_from_record(record, cohort["tests"], **POLICY)
                    for sid, record in cohort["records"].items()}
        for row, later in pair_repairs(cohort["rows"], cohort["reviews"], outcomes):
            jobs.append((problem, row, later))
    print(f"real: {len(jobs)} failing->repaired pairs", flush=True)
    results = []

    def work(job):
        problem, row, later = job
        tests = cohorts[problem]["tests"]
        repair = minimal_repair(pool, row, later, tests, budget)
        return {"item_id": row.submission_id, "problem_id": problem, "student_id": row.student_id,
                "partition": split[row.submission_id], "repair_submission_id": later.submission_id,
                "source_sha256": hashlib.sha256(row.source_code.encode()).hexdigest(),
                **(repair or {"status": "no_line_difference"})}

    started = time.time()
    with ThreadPoolExecutor(threads) as executor:
        for index, result in enumerate(executor.map(work, jobs), 1):
            results.append(result)
            if index % 100 == 0:
                print(f"real {index}/{len(jobs)} ({time.time() - started:.0f}s)", flush=True)
    return results


def build_injected(cohorts, pool, split, seed, max_sources):
    rng = random.Random(seed)
    candidates = []
    for problem, cohort in sorted(cohorts.items()):
        accepted = []
        for row in cohort["rows"]:
            record = cohort["records"][row.submission_id]
            outcome = outcomes_from_record(record, cohort["tests"], **POLICY)
            if outcome and all(v == "pass" for v in outcome.values()) and record["compile"]["warning_free"]:
                accepted.append(row)
        # One accepted program per student and year keeps authors from dominating a cohort.
        seen, sources = set(), []
        for row in sorted(accepted, key=lambda r: r.submission_id):
            key = (row.student_id, cohort["reviews"][row.submission_id]["year"])
            if key not in seen:
                seen.add(key)
                sources.append(row)
        rng.shuffle(sources)
        for row in sources[:max_sources]:
            for category, operator, mutated in one_mutant_per_category(row.source_code, rng):
                candidates.append((problem, row, category, operator, mutated))
    print(f"injected: {len(candidates)} candidate mutants", flush=True)
    futures = [pool.submit(request_for(f"{row.submission_id}#m{i}", mutated, cohorts[problem]["tests"]))
               for i, (problem, row, _, _, mutated) in enumerate(candidates)]
    results, status = [], Counter()
    for index, ((problem, row, category, operator, mutated), future) in enumerate(zip(candidates, futures)):
        tests = cohorts[problem]["tests"]
        response = future.result()
        outcome = response_outcomes(response, tests)
        if outcome is None:
            status["infrastructure_error"] += 1
            continue
        outcomes, record = outcome
        if record["compile"]["returncode"] != 0:
            status["compile_error"] += 1
            continue
        if not record["compile"]["warning_free"]:
            status["compile_warning"] += 1
            continue
        if outcomes is None or all(v == "pass" for v in outcomes.values()):
            status["equivalent_on_suite"] += 1
            continue
        status["kept"] += 1
        results.append({"item_id": f"inj-{row.submission_id}-{operator}", "problem_id": problem,
                        "student_id": row.student_id, "partition": split[row.submission_id],
                        "source_submission_id": row.submission_id, "category": category,
                        "operator": operator, "source_code": mutated, "outcomes": outcomes,
                        "replay": record})
        if (index + 1) % 1000 == 0:
            print(f"injected {index + 1}/{len(candidates)} {dict(status)}", flush=True)
    return results, dict(status)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--replay", type=Path, required=True)
    parser.add_argument("--split-lock", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--threads", type=int, default=16)
    parser.add_argument("--budget", type=int, default=64)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--max-sources", type=int, default=40)
    parser.add_argument("--only", choices=("real", "injected"))
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    cohorts = load(args.data, args.replay)
    split = json.loads(args.split_lock.read_text(encoding="utf-8"))["assignments"]
    image = image_id()
    started = time.time()
    summary = {}
    with ReplayPool(args.workers, image) as pool:
        if args.only != "injected":
            real = build_real(cohorts, pool, split, args.budget, args.threads)
            (args.output / "real_repairs.jsonl").write_text(
                "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in real), encoding="utf-8")
            summary["real"] = {"pairs": len(real), "status": dict(Counter(r["status"] for r in real)),
                               "primary": dict(Counter(r.get("primary") for r in real if r["status"] == "ok"))}
        if args.only != "real":
            injected, status = build_injected(cohorts, pool, split, args.seed, args.max_sources)
            (args.output / "injected.jsonl").write_text(
                "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in injected), encoding="utf-8")
            summary["injected"] = {"status": status,
                                   "category": dict(Counter(r["category"] for r in injected))}
    write_json(args.output / "manifest.json", {
        "schema_version": 1, "image": image, "policy": {k: list(v) if isinstance(v, tuple) else v
                                                        for k, v in POLICY.items()},
        "budget": args.budget, "seed": args.seed, "max_sources": args.max_sources,
        "input_dataset_complete_sha256": digest(args.data / "dataset_complete.json"),
        "replay_manifest_sha256": digest(args.replay / "replay_manifest.json"),
        "split_lock_sha256": digest(args.split_lock), "elapsed_seconds": round(time.time() - started, 1),
        "summary": summary, "implementation": implementation_fingerprint(ROOT),
        "files_sha256": {p.name: digest(p) for p in sorted(args.output.glob("*.jsonl"))}})
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()

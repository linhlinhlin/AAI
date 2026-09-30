"""Run the registered mechanism-recovery evaluation (research/protocol-mechanism-v1.json).

Validation and test partitions are reported separately; `--partition test` is the sealed
evaluation and must be run once with the frozen configuration.
"""

import argparse
import hashlib
import json
import time
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
from sklearn.metrics import adjusted_rand_score
from sklearn.tree import DecisionTreeClassifier

from misconceptions import ila
from misconceptions.deviation_features import code_cues, deviation_oav
from misconceptions.domain import Submission
from misconceptions.features import extract_oav
from misconceptions.mechanism_eval import (
    REPRESENTATIONS,
    CategoricalSpace,
    ceiling,
    choose_k_silhouette,
    cluster,
    distinct_patterns,
    paired_summary,
    score,
)
from misconceptions.output_features import output_oav
from misconceptions.replay import POLICY_DEFAULT, outcomes_from_record
from misconceptions.research_io import digest, implementation_fingerprint, read_cohorts, write_json

ROOT = Path(__file__).resolve().parents[2]
SEEDS = (7, 42, 91)
EMBED_MODEL = "qwen3-embedding:0.6b"
AGNOSTIC_OUTCOME = ("agg:status", "agg:fail_fraction")


def runs_of(record, tests, outcomes):
    by_id = {t["test_id"]: t for t in record["tests"]}
    return {tid: (outcomes[tid], by_id[tid]["stdout"] or "", tests[tid]["expected"]) for tid in tests}


def features(problem, source, outcomes, record, tests):
    oracles = {definition["expected"] for definition in tests.values()}
    row = Submission("item", None, problem, "c", source, "suite", outcomes, "")
    logs = {"item": [{"test_id": t["test_id"], "input": tests[t["test_id"]]["input"],
                      "expected": tests[t["test_id"]]["expected"], "output": t["stdout"]}
                     for t in record["tests"] if outcomes[t["test_id"]] in ("pass", "fail")
                     and t["stdout"] is not None]}
    values = {name: str(value) for name, value in extract_oav(row).items()}
    values.update(output_oav(row, logs))
    values.update(deviation_oav(runs_of(record, tests, outcomes), oracles))
    values.update(code_cues(source, oracles))
    return values


def load_items(data, replay, bench):
    cohorts = {}
    for folder, manifest, rows in read_cohorts(data):
        problem = manifest["problem_id"]
        tests = json.loads((folder / "tests.json").read_text(encoding="utf-8"))
        records = {json.loads(line)["submission_id"]: json.loads(line) for line in
                   (replay / "cohorts" / problem / "replay.jsonl").read_text(encoding="utf-8").splitlines()}
        cohorts[problem] = {"tests": tests, "rows": {r.submission_id: r for r in rows}, "records": records}
    items = {"real": [], "injected": []}
    for line in (bench / "real_repairs.jsonl").read_text(encoding="utf-8").splitlines():
        repair = json.loads(line)
        if repair["status"] != "ok" or not repair["one_minimal"] or repair["primary"] in (
                "MULTI", "OTHER", "NO_CHANGE"):
            continue
        cohort = cohorts[repair["problem_id"]]
        row, record = cohort["rows"][repair["item_id"]], cohort["records"][repair["item_id"]]
        outcomes = outcomes_from_record(record, cohort["tests"], **POLICY_DEFAULT)
        items["real"].append({"id": row.submission_id, "problem": row.problem_id, "student": row.student_id,
                              "partition": repair["partition"], "label": repair["primary"],
                              "source_key": row.submission_id, "code": row.source_code,
                              "outcomes": outcomes, "record": record})
    for line in (bench / "injected.jsonl").read_text(encoding="utf-8").splitlines():
        mutant = json.loads(line)
        items["injected"].append({"id": mutant["item_id"], "problem": mutant["problem_id"],
                                  "student": mutant["student_id"], "partition": mutant["partition"],
                                  "label": mutant["category"], "source_key": mutant["source_submission_id"],
                                  "code": mutant["source_code"], "outcomes": mutant["outcomes"],
                                  "record": mutant["replay"]})
    for benchmark in items.values():
        for item in benchmark:
            item["values"] = features(item["problem"], item["code"], item["outcomes"], item["record"],
                                      cohorts[item["problem"]]["tests"])
    # Label-free vocabulary pool: every failing replayed submission of the training partition.
    pool = defaultdict(list)
    for problem, cohort in cohorts.items():
        for sid, record in cohort["records"].items():
            outcomes = outcomes_from_record(record, cohort["tests"], **POLICY_DEFAULT)
            if outcomes is None or all(v == "pass" for v in outcomes.values()):
                continue
            pool[problem].append((sid, cohort["rows"][sid].source_code, outcomes, record))
    return items, cohorts, pool


def embed(texts, cache_path):
    cache = {}
    if cache_path.exists():
        for line in cache_path.read_text(encoding="utf-8").splitlines():
            entry = json.loads(line)
            cache[entry["sha256"]] = entry["vector"]
    missing = sorted({hashlib.sha256(t.encode()).hexdigest(): t for t in texts
                      if hashlib.sha256(t.encode()).hexdigest() not in cache}.items())
    with cache_path.open("a", encoding="utf-8") as stream:
        for start in range(0, len(missing), 16):
            batch = missing[start:start + 16]
            body = json.dumps({"model": EMBED_MODEL, "input": [t for _, t in batch],
                               "truncate": True}).encode()
            request = urllib.request.Request("http://127.0.0.1:11434/api/embed", data=body,
                                             headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(request, timeout=600) as response:
                vectors = json.loads(response.read())["embeddings"]
            for (key, _), vector in zip(batch, vectors):
                cache[key] = vector
                stream.write(json.dumps({"sha256": key, "vector": vector}) + "\n")
    return {t: np.asarray(cache[hashlib.sha256(t.encode()).hexdigest()]) for t in texts}


def evaluate_cohort(items, space_by_rep, embeddings):
    gold = [item["label"] for item in items]
    n_labels = len(set(gold))
    result = {"n": len(items), "labels": dict(Counter(gold)), "reps": {}}
    for rep, space in space_by_rep.items():
        values = space.transform([item["values"] for item in items])
        matrix, distances = space.onehot(values), space.distances(values)
        patterns = distinct_patterns(matrix) if matrix.shape[1] else 1
        entry = {"ceiling": ceiling(values, gold), "patterns": patterns}
        for method in ("kmeans", "hac"):
            for mode in ("oracle", "silhouette"):
                runs = []
                for seed in (SEEDS if method == "kmeans" else SEEDS[:1]):
                    k = min(n_labels, patterns) if mode == "oracle" else \
                        choose_k_silhouette(matrix, distances, method, seed) if patterns > 1 else 1
                    labels = cluster(matrix, distances, method, k, seed) if patterns > 1 else \
                        np.zeros(len(items), dtype=int)
                    runs.append(score(labels, gold))
                entry[f"{method}_{mode}"] = {m: _mean([r[m] for r in runs]) for m in runs[0]}
        result["reps"][rep] = entry
    signature = [tuple(item["outcomes"][t] for t in sorted(item["outcomes"])) for item in items]
    _, exact = np.unique(np.asarray([str(s) for s in signature]), return_inverse=True)
    result["reps"]["exact_signature"] = {"exact": score(exact, gold)}
    if embeddings is not None:
        vectors = np.stack([embeddings[item["code"]] for item in items])
        vectors = vectors / np.linalg.norm(vectors, axis=1, keepdims=True)
        distances = np.clip(1 - vectors @ vectors.T, 0, 2)
        entry = {}
        sources = [item["source_key"] for item in items]
        for method in ("kmeans", "hac"):
            for mode in ("oracle", "silhouette"):
                runs, source_ari = [], []
                for seed in (SEEDS if method == "kmeans" else SEEDS[:1]):
                    k = n_labels if mode == "oracle" else choose_k_silhouette(vectors, distances, method, seed)
                    labels = cluster(vectors, distances, method, k, seed)
                    runs.append(score(labels, gold))
                    source_ari.append(adjusted_rand_score(sources, labels))
                entry[f"{method}_{mode}"] = {m: _mean([r[m] for r in runs]) for m in runs[0]}
                entry[f"{method}_{mode}"]["ari_vs_source"] = _mean(source_ari)
        result["reps"]["embedding"] = entry
    return result


def _mean(values):
    values = [v for v in values if v is not None]
    return float(np.mean(values)) if values else None


def cohort_spaces(problem, benchmark, items, pool, cohorts):
    """Fit vocabularies on training-partition rows of this problem (labels unused)."""
    if benchmark == "real":
        tests = cohorts[problem]["tests"]
        train_rows = [features(problem, code, outcomes, record, tests)
                      for sid, code, outcomes, record in pool[problem]
                      if SPLIT[sid] == "train"]
    else:
        train_rows = [item["values"] for item in items if item["partition"] == "train"
                      and item["problem"] == problem]
    return {rep: CategoricalSpace.fit(train_rows, masses) for rep, masses in REPRESENTATIONS.items()}


def summarize(cohort_results, reference="outcomes"):
    table = defaultdict(dict)
    comparisons = {}
    for key in ("kmeans_oracle", "hac_oracle", "kmeans_silhouette", "hac_silhouette", "exact"):
        for rep in sorted({r for c in cohort_results for r in c["reps"]}):
            scores = [c["reps"][rep].get(key) for c in cohort_results if rep in c["reps"]]
            scores = [s for s in scores if s]
            if scores:
                table[key][rep] = {m: _mean([s[m] for s in scores]) for m in scores[0]} | {"cohorts": len(scores)}
    for base in (reference, "combined_stdout"):
        for rep in ("deviation", "evidence", "combined_stdout", "outcomes_stdout", "structural",
                    "code_cues", "embedding"):
            if rep == base:
                continue
            for key in ("kmeans_oracle", "hac_oracle"):
                diffs = [c["reps"][rep][key]["ari"] - c["reps"][base][key]["ari"]
                         for c in cohort_results if rep in c["reps"] and key in c["reps"][rep]]
                comparisons[f"{rep}-{base}|{key}|ari"] = paired_summary(diffs)
    ceilings = {rep: _mean([c["reps"][rep]["ceiling"] for c in cohort_results if rep in c["reps"]
                            and "ceiling" in c["reps"][rep]]) for rep in REPRESENTATIONS}
    comparisons["ceiling:deviation-outcomes"] = paired_summary(
        [c["reps"]["deviation"]["ceiling"] - c["reps"]["outcomes"]["ceiling"] for c in cohort_results])
    comparisons["ceiling:evidence-outcomes"] = paired_summary(
        [c["reps"]["evidence"]["ceiling"] - c["reps"]["outcomes"]["ceiling"] for c in cohort_results])
    if any("embedding" in c["reps"] for c in cohort_results):
        comparisons["embedding:ari_source-ari_mechanism|kmeans_oracle"] = paired_summary(
            [c["reps"]["embedding"]["kmeans_oracle"]["ari_vs_source"] - c["reps"]["embedding"]["kmeans_oracle"]["ari"]
             for c in cohort_results if "embedding" in c["reps"]])
    return {"table": table, "ceilings": ceilings, "comparisons": comparisons}


def rule_experiments(items, partition, penalty=None):
    """ILA / ILA-2 / CART over problem-agnostic attributes; labels from the train partition."""
    def view(item, kind):
        if kind == "evidence":
            return {k: v for k, v in item["values"].items() if k.startswith(("agg:", "code:"))}
        return {k: item["values"][k] for k in AGNOSTIC_OUTCOME}

    results = {}
    train = [i for i in items if i["partition"] == "train"]
    tracks = {"seen_problems": (train, [i for i in items if i["partition"] == partition]),
              "unseen_problems": ([i for i in train if not i["problem"].startswith("lab04")],
                                  [i for i in items if i["partition"] == partition
                                   and i["problem"].startswith("lab04")])}
    for track, (fit_items, eval_items) in tracks.items():
        if not fit_items or not eval_items:
            continue
        y_fit, y_eval = [i["label"] for i in fit_items], [i["label"] for i in eval_items]
        for name in ("evidence", "outcome_summary"):
            x_fit = [view(i, name) for i in fit_items]
            x_eval = [view(i, name) for i in eval_items]
            for algorithm, pf in (("ila", None), ("ila2", penalty)):
                if algorithm == "ila2" and pf is None:
                    continue
                rules = ila.induce(x_fit, y_fit, max_conditions=2, penalty=pf, min_support=3)
                evaluation = ila.evaluate(rules, x_eval, y_eval)
                evaluation["bootstrap_macro_f1"] = student_bootstrap(eval_items, evaluation["predictions"])
                results[f"{track}|{name}|{algorithm}"] = {
                    "penalty": pf, "n_rules": len(rules), "rules": rules[:25],
                    **{k: v for k, v in evaluation.items() if k != "predictions"},
                    "predictions": evaluation["predictions"]}
            results[f"{track}|{name}|cart"] = cart_eval(cart_predict(x_fit, y_fit, x_eval), y_eval, eval_items)
        majority = Counter(y_fit).most_common(1)[0][0]
        results[f"{track}|majority"] = cart_eval([majority] * len(y_eval), y_eval, eval_items)
        results[f"{track}|n"] = {"fit": len(fit_items), "eval": len(eval_items),
                                 "eval_labels": dict(Counter(y_eval))}
    return results


def cart_predict(x_fit, y_fit, x_eval):
    names = sorted({f"{k}={v}" for row in x_fit for k, v in row.items()})
    index = {n: i for i, n in enumerate(names)}

    def encode(rows):
        matrix = np.zeros((len(rows), len(names)))
        for r, row in enumerate(rows):
            for k, v in row.items():
                if f"{k}={v}" in index:
                    matrix[r, index[f"{k}={v}"]] = 1
        return matrix
    tree = DecisionTreeClassifier(max_depth=4, min_samples_leaf=3, random_state=0)
    tree.fit(encode(x_fit), y_fit)
    return list(tree.predict(encode(x_eval)))


def cart_eval(predictions, labels, items):
    classes = sorted(set(labels))
    f1s = []
    for c in classes:
        tp = sum(p == c and y == c for p, y in zip(predictions, labels))
        fp = sum(p == c and y != c for p, y in zip(predictions, labels))
        fn = sum(y == c and p != c for p, y in zip(predictions, labels))
        precision = tp / (tp + fp) if tp + fp else 0
        recall = tp / (tp + fn) if tp + fn else 0
        f1s.append(2 * precision * recall / (precision + recall) if precision + recall else 0)
    return {"n": len(labels), "coverage": 1.0, "accuracy_abstain_as_error":
            sum(p == y for p, y in zip(predictions, labels)) / len(labels),
            "macro_f1": sum(f1s) / len(f1s), "bootstrap_macro_f1": student_bootstrap(items, predictions)}


def macro_f1(predictions, labels):
    classes = sorted(set(labels))
    total = 0.0
    for c in classes:
        tp = sum(p == c and y == c for p, y in zip(predictions, labels))
        fp = sum(p == c and y != c for p, y in zip(predictions, labels))
        fn = sum(y == c and p != c for p, y in zip(predictions, labels))
        precision = tp / (tp + fp) if tp + fp else 0
        recall = tp / (tp + fn) if tp + fn else 0
        total += 2 * precision * recall / (precision + recall) if precision + recall else 0
    return total / len(classes)


def student_bootstrap(items, predictions, resamples=2000, seed=0):
    by_student = defaultdict(list)
    for index, item in enumerate(items):
        by_student[item["student"]].append(index)
    students = sorted(by_student)
    rng = np.random.default_rng(seed)
    values = []
    for _ in range(resamples):
        chosen = [i for s in rng.choice(students, len(students), replace=True) for i in by_student[s]]
        labels = [items[i]["label"] for i in chosen]
        if len(set(labels)) > 1:
            values.append(macro_f1([predictions[i] for i in chosen], labels))
    return [float(np.quantile(values, 0.025)), float(np.quantile(values, 0.975))] if values else None


def paired_rule_difference(items, first, second, resamples=2000, seed=0):
    by_student = defaultdict(list)
    for index, item in enumerate(items):
        by_student[item["student"]].append(index)
    students = sorted(by_student)
    rng = np.random.default_rng(seed)
    values = []
    for _ in range(resamples):
        chosen = [i for s in rng.choice(students, len(students), replace=True) for i in by_student[s]]
        labels = [items[i]["label"] for i in chosen]
        values.append(macro_f1([first[i] for i in chosen], labels) - macro_f1([second[i] for i in chosen], labels))
    return {"mean": float(np.mean(values)), "ci95": [float(np.quantile(values, 0.025)),
                                                       float(np.quantile(values, 0.975))]}


SPLIT = {}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--replay", type=Path, required=True)
    parser.add_argument("--bench", type=Path, required=True)
    parser.add_argument("--split-lock", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--partition", choices=("validation", "test"), required=True)
    parser.add_argument("--penalty", type=float, help="ILA-2 penalty frozen after validation")
    parser.add_argument("--embed-cache", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    SPLIT.update(json.loads(args.split_lock.read_text(encoding="utf-8"))["assignments"])
    audit = json.loads((args.replay / "oracle_audit.json").read_text(encoding="utf-8"))
    if audit["selected_policy"] != "exact_exit0":
        raise ValueError("Replay audit selected a different outcome policy; update POLICY_DEFAULT first")
    started = time.time()
    items, cohorts, pool = load_items(args.data, args.replay, args.bench)
    embeddings = None
    if args.embed_cache:
        texts = sorted({item["code"] for benchmark in items.values() for item in benchmark
                        if item["partition"] == args.partition})
        embeddings = embed(texts, args.embed_cache)
    report = {"partition": args.partition, "benchmarks": {}}
    for benchmark, benchmark_items in items.items():
        by_problem = defaultdict(list)
        for item in benchmark_items:
            if item["partition"] == args.partition:
                by_problem[item["problem"]].append(item)
        cohort_results, skipped = [], {}
        for problem in sorted(by_problem):
            cohort = by_problem[problem]
            if len(cohort) < 6 or len({i["label"] for i in cohort}) < 2:
                skipped[problem] = {"n": len(cohort), "labels": len({i["label"] for i in cohort})}
                continue
            spaces = cohort_spaces(problem, benchmark, benchmark_items, pool, cohorts)
            result = evaluate_cohort(cohort, spaces, embeddings)
            result["problem"] = problem
            cohort_results.append(result)
            print(f"{benchmark} {problem}: n={result['n']} labels={len(result['labels'])}", flush=True)
        penalties = {}
        if args.partition == "validation":
            for pf in (1.0, 2.0, 5.0):
                penalties[pf] = rule_experiments(benchmark_items, "validation", pf)
            best = max(penalties, key=lambda pf: penalties[pf]["seen_problems|evidence|ila2"]["macro_f1"])
            rules = penalties[best]
            rules["selected_penalty"] = best
            rules["penalty_scan"] = {pf: r["seen_problems|evidence|ila2"]["macro_f1"] for pf, r in penalties.items()}
        else:
            rules = rule_experiments(benchmark_items, "test", args.penalty)
        eval_items = [i for i in benchmark_items if i["partition"] == args.partition]
        for track in ("seen_problems",):
            a, b = rules.get(f"{track}|evidence|ila2"), rules.get(f"{track}|outcome_summary|ila2")
            if a and b:
                rules[f"{track}|H4_difference"] = paired_rule_difference(eval_items, a["predictions"], b["predictions"])
        for key in list(rules):
            if isinstance(rules[key], dict):
                rules[key].pop("predictions", None)
        report["benchmarks"][benchmark] = {
            "items_total": len(benchmark_items),
            "items_by_partition": dict(Counter(i["partition"] for i in benchmark_items)),
            "labels_in_partition": dict(Counter(i["label"] for i in eval_items)),
            "cohorts": cohort_results, "skipped_cohorts": skipped,
            "summary": summarize(cohort_results), "rules": rules}
    write_json(args.output / "results.json", report)
    write_json(args.output / "run_manifest.json", {
        "protocol_sha256": digest(args.protocol), "partition": args.partition, "penalty": args.penalty,
        "bench_manifest_sha256": digest(args.bench / "manifest.json"),
        "replay_manifest_sha256": digest(args.replay / "replay_manifest.json"),
        "split_lock_sha256": digest(args.split_lock), "embedding_model": EMBED_MODEL if embeddings else None,
        "elapsed_seconds": round(time.time() - started, 1), "implementation": implementation_fingerprint(ROOT)})
    print(json.dumps({b: v["summary"]["comparisons"] for b, v in report["benchmarks"].items()}, indent=1)[:6000])


if __name__ == "__main__":
    main()

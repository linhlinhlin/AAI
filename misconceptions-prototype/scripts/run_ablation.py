"""Reproducible fixture experiments. Scores are software checks, not educational evidence."""

import json
import time
from pathlib import Path

from sklearn.metrics import adjusted_rand_score

from misconceptions.adapters import load_dataset
from misconceptions.pipeline import run_experiment


def main():
    root = Path(__file__).resolve().parents[1]
    data, output = root / "data" / "demo", root / "results"
    output.mkdir(exist_ok=True)
    manifest, rows = load_dataset(data / "manifest.json", data / "submissions.jsonl")
    summaries = []
    for mode, method, k in [
        ("outcomes", "exact", 2),
        ("outcomes", "agglomerative", 2),
        ("combined", "agglomerative", 3),
        ("combined", "kmeans", 3),
    ]:
        runs = []
        for seed in (7, 42, 91):
            started = time.perf_counter()
            result = run_experiment(
                rows,
                test_ids=manifest["test_ids"],
                method=method,
                feature_mode=mode,
                k=k,
                seed=seed,
            )
            result["elapsed_seconds"] = time.perf_counter() - started
            result["data_kind"] = "synthetic_integration_fixture"
            filename = f"{method}_{mode}_{seed}.json"
            (output / filename).write_text(
                json.dumps(result, indent=2, allow_nan=False), encoding="utf-8"
            )
            if result["status"] != "ok":
                raise RuntimeError(f"Fixture experiment unexpectedly abstained: {result}")
            runs.append(result)
        # Common training subset only; cross-split sensitivity, not population bootstrap stability.
        first, second = runs[0]["train_assignments"], runs[1]["train_assignments"]
        common = sorted(first.keys() & second.keys())
        sensitivity = adjusted_rand_score([first[s] for s in common], [second[s] for s in common])
        summaries.append(
            {
                "method": method,
                "features": mode,
                "k_configured": k,
                "seeds": [7, 42, 91],
                "clusters": [r["n_clusters"] for r in runs],
                "silhouette_train": [r["silhouette_train"] for r in runs],
                "rule_holdout_fidelity": [r["explanation"]["holdout_fidelity"] for r in runs],
                "elapsed_seconds": [r["elapsed_seconds"] for r in runs],
                "common_train_count_seed7_42": len(common),
                "common_train_ARI_seed7_42": float(sensitivity),
            }
        )
    (output / "ablation_summary.json").write_text(
        json.dumps(
            {
                "warning": "Synthetic near-duplicate variants; NOT an unbiased generalization benchmark.",
                "experiments": summaries,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(json.dumps(summaries, indent=2))


if __name__ == "__main__":
    main()

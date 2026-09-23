"""Small command-line boundary; no student program execution."""

import argparse
import hashlib
import importlib.metadata
import json
import platform
from pathlib import Path

from .adapters import load_dataset
from .pipeline import run_experiment
from .teaching_report import attach_teaching_report


def build_provenance(manifest: dict, manifest_path: Path, submissions_path: Path) -> dict:
    """Record exact inputs and installed runtime for both CLI and batch experiments."""
    return {
        "dataset": manifest,
        "input_sha256": hashlib.sha256(submissions_path.read_bytes()).hexdigest(),
        "manifest_sha256": hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
        "python": platform.python_version(),
        "packages": {
            name: importlib.metadata.version(name)
            for name in ["numpy", "scipy", "scikit-learn", "tree-sitter", "tree-sitter-c"]
        },
        "interpretation": "Clusters are observable error patterns, not verified misconceptions.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--submissions", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--evidence", type=Path, help="Optional test-evidence JSONL for teaching rules")
    parser.add_argument(
        "--method", choices=["exact", "agglomerative", "kmeans"], default="kmeans"
    )
    parser.add_argument("--k", type=int, default=3)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--feature-mode", choices=["outcomes", "structural", "combined"], default="combined"
    )
    parser.add_argument("--test-weight", type=float, default=0.8)
    args = parser.parse_args()
    try:
        manifest, rows = load_dataset(args.manifest, args.submissions)
        result = run_experiment(
            rows,
            test_ids=manifest["test_ids"],
            method=args.method,
            k=args.k,
            seed=args.seed,
            feature_mode=args.feature_mode,
            test_weight=args.test_weight,
        )
        if args.evidence and not args.evidence.is_file():
            raise ValueError("Evidence file does not exist")
        attach_teaching_report(result, rows, args.evidence or args.submissions.with_name("review.jsonl"))
    except (ValueError, TypeError, OSError) as error:
        parser.error(str(error))
    result["provenance"] = build_provenance(manifest, args.manifest, args.submissions)
    result["provenance"]["seed"] = args.seed
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False), encoding="utf-8"
    )
    print(f"Saved report: {args.output}")


if __name__ == "__main__":
    main()

"""Validate and merge returned human round-one files; never overwrite a snapshot."""

import argparse
import hashlib
import json
from pathlib import Path

from misconceptions.annotation_intake import merge_round_one


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", nargs="+", type=Path)
    parser.add_argument(
        "--assignments", type=Path, default=root / "results/itsp/abc_review_assignments.json"
    )
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        assignments_bytes = args.assignments.read_bytes()
        assignments = json.loads(assignments_bytes)
        digest = hashlib.sha256(assignments_bytes).hexdigest()
        documents, sources = [], []
        for path in args.inputs:
            raw = path.read_bytes()
            document = json.loads(raw)
            if document["assignments_sha256"] != digest:
                raise ValueError(f"Assignment hash mismatch in {path}")
            documents.append(document)
            sources.append(
                {
                    "path": str(path.resolve()),
                    "sha256": hashlib.sha256(raw).hexdigest(),
                    "reviewer_id": next(
                        (
                            r["reviewer_id"]
                            for s in document["samples"]
                            for r in s["reviews"]
                            if r["reviewer_id"]
                        ),
                        None,
                    ),
                }
            )
        result = merge_round_one(documents, assignments)
        result["intake"]["sources"] = sources
        encoded = json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x", encoding="utf-8") as stream:
            stream.write(encoded)
    except (ValueError, KeyError, TypeError, OSError) as error:
        parser.error(str(error))
    print(f"Merged {len(documents)} reviewer files; adjudication remains pending: {args.output}")


if __name__ == "__main__":
    main()

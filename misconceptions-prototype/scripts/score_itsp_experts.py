"""Score human and explicitly identified AI reviews separately; never modify clustering."""

import argparse
import hashlib
import json
from pathlib import Path

from misconceptions.expert_validation import score_annotation_sources, validate_annotations


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--annotations", type=Path, default=root / "data/itsp/expert_annotations.json"
    )
    parser.add_argument(
        "--assignments", type=Path, default=root / "results/itsp/abc_review_assignments.json"
    )
    parser.add_argument(
        "--output", type=Path, default=root / "results/itsp/expert_validation_metrics.json"
    )
    parser.add_argument(
        "--validate-only", action="store_true", help="Validate without computing or writing metrics"
    )
    args = parser.parse_args()
    if args.output.resolve() in (args.annotations.resolve(), args.assignments.resolve()):
        parser.error("Output must not overwrite input files")
    try:
        document = json.loads(args.annotations.read_text(encoding="utf-8"))
        assignments = json.loads(args.assignments.read_text(encoding="utf-8"))
        actual_hash = hashlib.sha256(args.assignments.read_bytes()).hexdigest()
        if document["assignments_sha256"] != actual_hash:
            raise ValueError("Cluster assignments changed; review context must be revalidated")
        if args.validate_only:
            validate_annotations(document, assignments)
            print("Annotation schema, sample IDs and assignment hash are valid; no metrics computed")
            return
        result = score_annotation_sources(document, assignments)
    except (ValueError, KeyError, TypeError, OSError) as error:
        parser.error(str(error))
    result["provenance"] = {
        "annotations_sha256": hashlib.sha256(args.annotations.read_bytes()).hexdigest(),
        "assignments_sha256": actual_hash,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False), encoding="utf-8"
    )
    print(
        f"{result['status']}: {result['n_completed_records']} completed reviews, "
        f"{result['n_adjudicated']} adjudications; saved {args.output}"
    )


if __name__ == "__main__":
    main()

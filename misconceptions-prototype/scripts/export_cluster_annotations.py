"""Export evidence-rich clusters or validate AI reviews, without creating human gold."""

import argparse
from pathlib import Path

from misconceptions.cluster_annotation import export_packet, read, validate_response
from misconceptions.research_io import write_json


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    export = sub.add_parser("export")
    for flag in ("run", "data", "split-lock", "output"):
        export.add_argument("--" + flag, type=Path, required=True)
    export.add_argument("--min-cluster-size", type=int, default=4)
    validate = sub.add_parser("validate")
    for flag in ("packet", "output"):
        validate.add_argument("--" + flag, type=Path, required=True)
    validate.add_argument("--response", type=Path, nargs="+", required=True)
    validate.add_argument("--require-complete", action="store_true")
    args = parser.parse_args()
    try:
        if args.command == "export":
            packet = export_packet(args.run, args.data, args.split_lock, args.output,
                                   Path(__file__).resolve().parents[2], args.min_cluster_size)
            print(f"Exported {len(packet['clusters'])} pending clusters; "
                  f"excluded {len(packet['excluded_clusters'])}. {args.output}")
        else:
            if args.output.exists():
                raise ValueError("Output already exists; use a new path")
            packet = read(args.packet)
            responses = [read(path) for path in args.response]
            # Validate each envelope before combining; do not discard mismatched packet/source IDs.
            for response in responses:
                validate_response(packet, response)
            combined = {"packet_id": packet["packet_id"], "annotation_source": "ai",
                        "reviews": [r for response in responses for r in response["reviews"]]}
            result = validate_response(packet, combined, args.require_complete)
            write_json(args.output, result)
            print(f"Validated {len(result['reviews'])} AI reviews; "
                  f"missing {len(result['missing_cluster_ids'])}. No gold labels created.")
    except (ValueError, KeyError, OSError, TypeError) as exc:
        parser.exit(2, f"Error: {exc}\n")


if __name__ == "__main__":
    main()

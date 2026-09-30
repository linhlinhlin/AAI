"""Create standalone review pages from an existing blinded evidence packet."""

import argparse
import json
from pathlib import Path

from misconceptions.annotation_editor import render_editor
from misconceptions.teacher_validation import validate_form


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--packet", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check", type=Path, help="Validate a downloaded reviewer JSON")
    args = parser.parse_args()
    evidence = json.loads((args.packet / "evidence.json").read_text(encoding="utf-8"))
    if args.check:
        form = json.loads(args.check.read_text(encoding="utf-8"))
        validate_form(form, evidence)
        print(f"Valid review: {sum(r['status'] != 'pending' for r in form['ratings'])} completed. "
              "This is one review, not adjudicated gold.")
        return
    if not args.output:
        parser.error("--output is required when creating pages")
    args.output.mkdir(parents=True, exist_ok=True)
    for slot in ("reviewer_1", "reviewer_2"):
        path = args.output / f"{slot}.html"
        with path.open("x", encoding="utf-8") as handle:
            handle.write(render_editor(evidence, slot))
    print(f"Created two independent forms, {len(evidence['cases'])} cases each: {args.output}")


if __name__ == "__main__":
    main()

"""Create an immutable corpus-wide split before selecting individual problems."""

import argparse
import json
from pathlib import Path

from misconceptions.research_io import read_cohorts
from misconceptions.splits import create_lock


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    rows = [row for _, _, cohort in read_cohorts(args.data) for row in cohort]
    lock = create_lock(rows, args.seed)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as stream:
        json.dump(lock, stream, ensure_ascii=False, indent=2, allow_nan=False)
    print(json.dumps({key: value for key, value in lock.items() if key != "assignments"}))


if __name__ == "__main__":
    main()

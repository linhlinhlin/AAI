"""Convert audited ITSP historical logs; does not compile or run submissions."""

import argparse
from pathlib import Path

from misconceptions.itsp import prepare

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--raw", type=Path, default=Path("data/raw/itsp"))
    parser.add_argument("--output", type=Path, default=Path("data/itsp"))
    args = parser.parse_args()
    result = prepare(args.raw, args.output)
    print(
        f"Imported {result['total_imported']}/{result['total_raw_buggy']} buggy programs "
        f"across {len(result['cohorts'])} cohorts; {len(result['exclusions'])} exclusions"
    )

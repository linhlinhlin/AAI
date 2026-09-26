"""Convert the pinned public C-Pack-IPAs snapshot into auditable cohorts."""

import argparse
from pathlib import Path

from misconceptions.cpack import prepare


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--raw", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    audit = prepare(args.raw, args.output)
    print(f"Imported {audit['total_submissions']} original submissions; no student program executed")


if __name__ == "__main__":
    main()

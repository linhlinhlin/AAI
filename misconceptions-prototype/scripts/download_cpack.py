"""Fetch only the canonical C-Pack-IPAs snapshot and verify its pinned commit."""

import argparse
import subprocess
from pathlib import Path

from misconceptions.cpack import COMMIT, REPOSITORY


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("Output already exists; choose a new snapshot directory")
    subprocess.run(["git", "clone", "-c", "core.autocrlf=false", "--no-checkout", "--depth", "1",
                    "--branch", "C-Pack-IPAs-26", REPOSITORY, str(args.output)], check=True)
    head = subprocess.check_output(["git", "-C", str(args.output), "rev-parse", "HEAD"], text=True).strip()
    if head != COMMIT:
        raise ValueError(f"Release tag moved: expected {COMMIT}, got {head}")
    subprocess.run(["git", "-C", str(args.output), "sparse-checkout", "set",
                    "all_submissions", "tests", "IPAs_description"], check=True)
    subprocess.run(["git", "-C", str(args.output), "checkout", "--detach", COMMIT], check=True)
    print(f"Pinned snapshot: {args.output}")


if __name__ == "__main__":
    main()

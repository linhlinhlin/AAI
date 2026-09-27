"""Project checks. Invoke with the installed project environment's Python."""

import argparse
import importlib.metadata
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "misconceptions-prototype"


def run(*args, cwd=PROJECT):
    print("+", sys.executable, *map(str, args), flush=True)
    subprocess.run([sys.executable, *map(str, args)], cwd=cwd, check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("doctor", "check", "smoke"))
    args = parser.parse_args()
    if args.command == "doctor":
        print("Python:", sys.executable, sys.version)
        for name in ("pytest", "ruff", "numpy", "scikit-learn", "tree-sitter", "tree-sitter-c"):
            print(name, importlib.metadata.version(name))
        print("No API keys, GPU or student-code execution required for check/smoke.")
    elif args.command == "check":
        run("-m", "ruff", "check", "src", "tests", "scripts", "../scripts")
        run("-m", "pytest", "-q")
    else:
        with tempfile.TemporaryDirectory(prefix="aai-smoke-") as tmp:
            root = Path(tmp)
            run("scripts/lock_splits.py", "--data", "data/itsp", "--output", root / "split.json")
            run("scripts/run_topic5.py", "--data", "data/itsp", "--split-lock", root / "split.json",
                "--problems", "2812", "2825", "2833", "--seeds", "42", "--output", root / "run")
            result = json.loads((root / "run/summary.json").read_text(encoding="utf-8"))
            ok = [run for run in result["runs"] if run["status"] == "ok"]
            if len(result["runs"]) != 27 or len(ok) != 27:
                raise RuntimeError("Topic 5 smoke requires all 27 recorded-data experiments to succeed")
            for item in ok:
                report = json.loads((root / "run" / item["artifact"]).read_text(encoding="utf-8"))
                if not report.get("oav") or not report["explanation"]["rules"]:
                    raise RuntimeError("Missing OAV or IF-THEN rules")
                if report["teaching"]["human_validated"]:
                    raise RuntimeError("Recorded logs cannot establish human validation")
            print(f"Topic 5 smoke: {len(ok)}/27 runs produced OAV, clusters, rules and feedback.")


if __name__ == "__main__":
    main()

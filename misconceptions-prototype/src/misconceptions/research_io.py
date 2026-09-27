"""Small shared boundaries for reproducible, offline research runs."""

import hashlib
import json
import subprocess

from .adapters import load_dataset


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n",
                    encoding="utf-8")


def read_cohorts(data):
    cohorts = []
    for manifest in sorted((data / "cohorts").glob("*/manifest.json")):
        description, rows = load_dataset(manifest, manifest.with_name("submissions.jsonl"))
        cohorts.append((manifest.parent, description, rows))
    if not cohorts:
        raise ValueError("No data/cohorts/*/manifest.json found")
    if any(manifest["dataset_name"] == "C-Pack-IPAs-26" for _, manifest, _ in cohorts):
        complete = data / "dataset_complete.json"
        if not complete.exists():
            raise ValueError("C-Pack import incomplete: no dataset_complete.json")
        inventory = json.loads(complete.read_text(encoding="utf-8"))
        if inventory["cohorts"] != len(cohorts) or inventory["submissions"] != sum(
            len(rows) for _, _, rows in cohorts
        ):
            raise ValueError("C-Pack import inventory mismatch")
        for name, expected in inventory["files_sha256"].items():
            if digest(data / name) != expected:
                raise ValueError(f"C-Pack imported file hash mismatch: {name}")
    return cohorts


def implementation_fingerprint(root):
    files = {}
    for folder in ("misconceptions-prototype/src", "misconceptions-prototype/scripts", "scripts"):
        for path in sorted((root / folder).rglob("*.py")):
            files[path.relative_to(root).as_posix()] = digest(path)
    for name in ("misconceptions-prototype/requirements-lock.txt",
                 "misconceptions-prototype/pyproject.toml", "research/protocol.json"):
        path = root / name
        if path.exists():
            files[name] = digest(path)
    def git(*args):
        return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()
    return {"base_commit": git("rev-parse", "HEAD"), "working_tree_dirty": bool(git("status", "--porcelain")),
            "files_sha256": files,
            "implementation_sha256": hashlib.sha256(json.dumps(files, sort_keys=True).encode()).hexdigest()}

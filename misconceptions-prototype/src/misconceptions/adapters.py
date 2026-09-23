"""JSON boundary: providers translate into this contract; core never reads provider files."""

import json
from dataclasses import fields
from pathlib import Path

from .domain import Submission

STATES = {"pass", "fail", "runtime_error", "timeout", "not_run"}


def load_dataset(manifest_path: Path, submissions_path: Path):
    manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
    if (
        not isinstance(manifest, dict)
        or type(manifest.get("schema_version")) is not int
        or manifest["schema_version"] not in (1, 2)
    ):
        raise ValueError("manifest.schema_version must be 1 or 2")
    for key in ("dataset_name", "provenance", "problem_id", "language", "suite_version"):
        if not isinstance(manifest.get(key), str) or not manifest[key].strip():
            raise ValueError(f"manifest.{key} must be a nonempty string")
    test_ids = manifest.get("test_ids")
    if (
        not isinstance(test_ids, list)
        or not test_ids
        or any(not isinstance(t, str) or not t.strip() for t in test_ids)
        or len(set(test_ids)) != len(test_ids)
    ):
        raise ValueError("manifest.test_ids must be unique nonempty strings")
    required = {field.name for field in fields(Submission)}
    rows, seen = [], set()
    with submissions_path.open(encoding="utf-8-sig") as stream:
        for line_number, line in enumerate(stream, 1):
            if not line.strip():
                continue
            row = json.loads(line)
            if not isinstance(row, dict) or set(row) != required:
                raise ValueError(f"line {line_number}: expected exactly fields {sorted(required)}")
            for key in required - {"outcomes"}:
                if key == "student_id" and manifest["schema_version"] == 2 and row[key] is None:
                    continue
                if not isinstance(row[key], str) or not row[key].strip():
                    raise ValueError(f"line {line_number}: {key} must be a nonempty string")
            sid = row["submission_id"]
            if sid in seen:
                raise ValueError(f"duplicate submission_id: {sid}")
            seen.add(sid)
            for key in ("problem_id", "language", "suite_version"):
                if row[key] != manifest[key]:
                    raise ValueError(f"line {line_number}: mixed {key}; use separate cohorts")
            outcomes = row["outcomes"]
            if not isinstance(outcomes, dict) or not set(outcomes) <= set(test_ids):
                raise ValueError(f"line {line_number}: unknown test IDs or invalid outcomes")
            if any(
                not isinstance(value, str) or value not in STATES for value in outcomes.values()
            ):
                raise ValueError(f"line {line_number}: invalid outcome state")
            # Absent test is explicitly unobserved, never a pass.
            row["outcomes"] = {test: outcomes.get(test, "not_run") for test in test_ids}
            rows.append(Submission(**row))
    if not rows:
        raise ValueError("dataset is empty")
    return manifest, rows

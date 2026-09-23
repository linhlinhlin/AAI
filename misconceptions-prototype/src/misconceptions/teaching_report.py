"""Read optional test evidence and attach a teaching report without changing clustering."""

import hashlib
import json
from pathlib import Path

from .semantic_rules import build_teaching_report


def load_evidence(path, rows):
    if not path.exists():
        return {}
    known = {row.submission_id: row for row in rows}
    logs = {}
    definitions = {}
    verdicts = {"pass": "ACCEPTED", "fail": "WRONG_ANSWER", "runtime_error": "RUNTIME_ERROR",
                "timeout": "TIME_LIMIT_EXCEEDED", "not_run": "NOT_RUN"}
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        if not line.strip():
            continue
        record = json.loads(line)
        if not isinstance(record, dict):
            raise TypeError("Evidence records must be JSON objects")
        sid = record.get("submission_id")
        if sid not in known or sid in logs:
            raise ValueError("Evidence: unknown or duplicate submission ID")
        tests = record.get("logged_tests")
        if not isinstance(tests, list):
            raise TypeError("Evidence: logged_tests must be a list")
        selected, seen = [], set()
        for test in tests:
            if not isinstance(test, dict) or any(not isinstance(test.get(k), str)
                                                for k in ("test_id", "input", "expected", "output")):
                raise ValueError("Evidence: test_id/input/expected/output must be strings")
            tid = test["test_id"]
            if tid not in known[sid].outcomes or tid in seen:
                raise ValueError("Evidence: unknown or duplicate test ID")
            seen.add(tid)
            definition = (test["input"], test["expected"])
            if tid in definitions and definitions[tid] != definition:
                raise ValueError("Evidence: inconsistent input/oracle for the same test ID")
            definitions[tid] = definition
            outcome = known[sid].outcomes[tid]
            if "verdict" in test and test["verdict"] != verdicts[outcome]:
                raise ValueError("Evidence verdict contradicts submission outcome")
            selected.append({key: test[key] for key in ("test_id", "input", "expected", "output")})
        logs[sid] = selected
    return logs


def attach_teaching_report(report, rows, evidence_path):
    logs = load_evidence(evidence_path, rows)
    report["teaching"] = build_teaching_report(rows, logs, report)
    report["teaching"]["evidence_sha256"] = (
        hashlib.sha256(evidence_path.read_bytes()).hexdigest() if evidence_path.exists() else None
    )
    report["teaching"]["source_line_basis"] = "normalized_submission_source_1_based"
    report["teaching"]["rules_source_sha256"] = hashlib.sha256(
        Path(__file__).with_name("semantic_rules.py").read_bytes()
    ).hexdigest()
    report["teaching"]["style_source_sha256"] = hashlib.sha256(
        Path(__file__).with_name("rule_style.py").read_bytes()
    ).hexdigest()

"""Import pinned C-Pack-IPAs historical logs without compiling student code."""

import hashlib
import json
import re
import subprocess
from collections import Counter, defaultdict
from dataclasses import asdict
from pathlib import Path

from .domain import Submission
from .features import route_submission
from .research_io import digest, write_json

COMMIT = "76901e1223b250a093a02d5e29113ad735c3d2b9"
REPOSITORY = "https://github.com/pmorvalho/C-Pack-IPAs"
VERDICTS = {
    "Accepted": "pass", "Wrong Answer": "fail", "Presentation Error": "fail",
    "Time Limit Exceeded": "timeout", "Runtime Error": "runtime_error",
    "Memory Limit Exceeded": "runtime_error", "Output Limit Exceeded": "runtime_error",
    "Internal Error": "not_run",
}
NORMALIZED = {"pass": "ACCEPTED", "fail": "WRONG_ANSWER", "timeout": "TIME_LIMIT_EXCEEDED",
              "runtime_error": "RUNTIME_ERROR"}


def parse_metadata(text, test_ids, student, attempt):
    if not re.search(rf"^# student: {re.escape(student)}$", text, re.MULTILINE) or not re.search(
        rf"^# submission: {re.escape(attempt)}$", text, re.MULTILINE
    ):
        raise ValueError("metadata_identity_mismatch")
    if "- Compile Time Error" in text:
        return {tid: "not_run" for tid in test_ids}, {}, "compile_error"
    records = re.findall(r"^(?:[+!\-]|@@) (ex\d+_\d+): ([^\r\n]+)$", text, re.MULTILINE)
    if len(records) != len(test_ids) or {tid for tid, _ in records} != set(test_ids):
        raise ValueError("metadata_test_ids_mismatch")
    historical = dict(records)
    outcomes = {}
    for tid, verdict in records:
        if verdict in VERDICTS:
            outcomes[tid] = VERDICTS[verdict]
        elif re.fullmatch(r"Command exited with non-zero status \(-?\d+\)", verdict) or re.fullmatch(
            r"Command terminated by signal \(\d+: SIG[A-Z]+\)", verdict
        ):
            outcomes[tid] = "runtime_error"
        else:
            raise ValueError("unsupported_historical_verdict")
    correct = re.search(r"^#correct=(\d+)$", text, re.MULTILINE)
    incorrect = re.search(r"^#incorrect=(\d+)$", text, re.MULTILINE)
    n_correct = sum(state == "pass" for state in outcomes.values())
    if (not correct or not incorrect or int(correct[1]) != n_correct
            or int(incorrect[1]) != len(test_ids) - n_correct):
        raise ValueError("metadata_count_mismatch")
    return outcomes, historical, "compiled_in_historical_run"


def prepare(raw: Path, output: Path):
    head = subprocess.check_output(["git", "-C", str(raw), "rev-parse", "HEAD"], text=True).strip()
    if head != COMMIT:
        raise ValueError(f"Expected C-Pack-IPAs commit {COMMIT}, found {head}")
    status = subprocess.check_output(["git", "-C", str(raw), "status", "--porcelain",
                                      "--untracked-files=all"], text=True)
    if status.strip():
        raise ValueError("C-Pack-IPAs checkout is dirty; use the pinned clean snapshot")
    output.mkdir(parents=True, exist_ok=False)
    used_files = {}

    def read(path):
        data = path.read_bytes()
        used_files[path.relative_to(raw).as_posix()] = hashlib.sha256(data).hexdigest()
        return data.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")

    for name in ("README.md", "LICENSE.md"):
        (output / name).write_text(read(raw / name), encoding="utf-8")
    cohorts = defaultdict(list)
    # Only canonical originals; repairs and duplicated category directories are excluded by design.
    for path in sorted((raw / "all_submissions").glob("year-*/lab*/ex*/stu_*/sub_*/*.c")):
        parts = path.relative_to(raw / "all_submissions").parts
        if len(parts) != 6 or path.stem != f"{parts[2]}-{parts[3]}-{parts[4]}":
            raise ValueError(f"Unexpected canonical submission path: {path}")
        cohorts[f"{parts[1]}-{parts[2]}"].append((path, parts))
    if not cohorts:
        raise ValueError("No canonical all_submissions programs found")
    audit = {"repository": REPOSITORY, "commit": COMMIT, "execution": "historical_logs_only",
             "scope": "all_submissions_only", "cohorts": [], "metadata_issues": [],
             "missing_failed_output": [], "non_utf8_output": [], "historical_verdicts": Counter(),
             "identity": "consistent_anonymized_student_id_across_years_and_problems",
             "limitations": ["No fresh execution or cognitive labels",
                             "Accepted tests often have no recorded stdout; none is fabricated",
                             "Missing failed stdout routes the submission as incomplete"]}
    for problem, entries in sorted(cohorts.items()):
        lab, exercise = problem.split("-")
        tests = {}
        for source in sorted((raw / "tests" / lab / exercise).glob("*.in")):
            tests[source.stem] = {"input": read(source), "expected": read(source.with_suffix(".out"))}
        if not tests:
            raise ValueError(f"Missing suite for {problem}")
        suite_hash = hashlib.sha256(json.dumps(tests, sort_keys=True,
                                               ensure_ascii=False).encode("utf-8")).hexdigest()
        version = "cpack-" + suite_hash
        rows, reviews, routes = [], [], Counter()
        for path, parts in entries:
            year, _, _, student, attempt, _ = parts
            sid = f"cpack-{year}-{problem}-{student}-{attempt}"
            code = read(path)
            try:
                outcomes, historical, compile_status = parse_metadata(
                    read(path.with_suffix(".md")), tests, student, attempt)
            except (ValueError, FileNotFoundError) as error:
                # Retain source and identity bridges even when the logs cannot be used.
                outcomes, historical, compile_status = dict.fromkeys(tests, "not_run"), {}, "unknown"
                audit["metadata_issues"].append({"id": sid, "reason": str(error)})
            audit["historical_verdicts"].update(historical.values())
            logged = []
            for tid, definition in tests.items():
                actual_path = path.parent / "outputs" / f"{tid}.out"
                if actual_path.exists() and outcomes[tid] in ("pass", "fail"):
                    try:
                        actual = read(actual_path)
                    except UnicodeDecodeError:
                        outcomes[tid] = "not_run"
                        audit["non_utf8_output"].append({"id": sid, "test_id": tid,
                                                        "path": actual_path.relative_to(raw).as_posix()})
                    else:
                        logged.append({"test_id": tid, **definition, "output": actual,
                                       "verdict": NORMALIZED[outcomes[tid]]})
                elif outcomes[tid] == "fail":
                    audit["missing_failed_output"].append({"id": sid, "test_id": tid})
                    outcomes[tid] = "not_run"
            row = Submission(sid, f"cpack:{student}", problem, "c", code, version, outcomes,
                             f"{REPOSITORY}@{COMMIT}:{path.relative_to(raw).as_posix()}")
            rows.append(row)
            routes[route_submission(row, list(tests))] += 1
            reviews.append({"submission_id": sid, "raw_path": path.relative_to(raw).as_posix(),
                            "year": year, "attempt": attempt, "compile_status": compile_status,
                            "historical_verdicts": historical, "logged_tests": logged})
        target = output / "cohorts" / problem
        write_json(target / "manifest.json", {"schema_version": 2, "dataset_name": "C-Pack-IPAs-26",
                   "provenance": REPOSITORY, "source_commit": COMMIT, "problem_id": problem,
                   "language": "c", "suite_version": version, "test_ids": list(tests),
                   "suite_sha256": suite_hash, "execution": "historical_logs_only"})
        for filename, records in (("submissions.jsonl", [asdict(row) for row in rows]),
                                  ("review.jsonl", reviews)):
            (target / filename).write_text("".join(json.dumps(record, ensure_ascii=False) + "\n"
                                                   for record in records), encoding="utf-8")
        write_json(target / "tests.json", tests)
        audit["cohorts"].append({"problem": problem, "submissions": len(rows), "routes": dict(routes)})
        print(f"Imported {problem}: {len(rows)} submissions, {dict(routes)}", flush=True)
    audit["total_submissions"] = sum(item["submissions"] for item in audit["cohorts"])
    write_json(output / "audit.json", audit)
    write_json(output / "provenance.json", {"commit": COMMIT, "repository": REPOSITORY,
               "files_sha256": used_files, "adapter_sha256": digest(Path(__file__))})
    files = {p.relative_to(output).as_posix(): digest(p)
             for p in sorted(output.rglob("*")) if p.is_file()}
    write_json(output / "dataset_complete.json", {"submissions": audit["total_submissions"],
               "cohorts": len(cohorts), "files_sha256": files})
    return audit

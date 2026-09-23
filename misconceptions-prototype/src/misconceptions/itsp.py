"""ITSP evidence adapter. Logged outcomes are observations, never misconception labels."""

import hashlib
import json
import re
from collections import Counter
from pathlib import Path

from .domain import Submission
from .features import route_submission

VERDICTS = {"ACCEPTED": "pass", "WRONG_ANSWER": "fail"}


def load_suite(test_directory: Path, problem_id: str):
    suite = {}
    digest = hashlib.sha256()
    for source in sorted(test_directory.glob(f"in.{problem_id}.*.txt")):
        test_id = source.name.split(".")[2]
        expected = source.with_name(f"out.{problem_id}.{test_id}.txt")
        if not expected.exists():
            raise ValueError(f"Missing oracle: {expected.name}")
        for path in (source, expected):
            data = path.read_bytes()
            digest.update(path.name.encode() + b"\0" + str(len(data)).encode() + b"\0" + data)
        suite[test_id] = (source.read_text(encoding="utf-8"), expected.read_text(encoding="utf-8"))
    if not suite:
        raise ValueError("No canonical tests")
    return suite, "itsp-" + digest.hexdigest()[:16]


def parse_submission(text: str, suite: dict):
    """Match literal input AND oracle, rather than position or quote-based splitting.

    ITSP embeds raw (not JSON escaped) multiline strings in a C comment. Matching
    canonical prefixes also handles literal double quotes in test inputs/oracles.
    """
    header = re.match(r"/\*numPass=(\d+), numTotal=(\d+)\r?\n", text)
    if not header:
        raise ValueError("missing_log_header")
    end = text.find("*/", header.end())
    if end < 0:
        raise ValueError("unterminated_log_header")
    source = text[end + 2 :].lstrip("\r\n")
    if not source.strip():
        raise ValueError("empty_source")
    content = text[header.end() : end]
    starts = list(
        re.finditer(r"^Verdict:([^,\r\n]+), Visibility:([01]), Input:", content, re.MULTILINE)
    )
    if not starts or content[: starts[0].start()].strip():
        raise ValueError("malformed_log")
    observed = {}
    evidence = []
    for index, start in enumerate(starts):
        stop = starts[index + 1].start() if index + 1 < len(starts) else len(content)
        chunk = content[start.end() : stop].rstrip("\r\n")
        verdict = start.group(1)
        if verdict not in VERDICTS:
            raise ValueError("unsupported_verdict:" + verdict)
        matches = []
        for test_id, (test_input, expected) in suite.items():
            prefix = f'"{test_input}", ExpOutput:"{expected}", Output:"'
            if chunk.startswith(prefix) and chunk.endswith('"'):
                matches.append((test_id, test_input, expected, chunk[len(prefix) : -1]))
        if len(matches) != 1:
            raise ValueError("test_evidence_unmatched_or_ambiguous")
        test_id, test_input, expected, actual = matches[0]
        if test_id in observed:
            raise ValueError("duplicate_test_log")
        observed[test_id] = VERDICTS[verdict]
        # Diagnostic only: whitespace deletion can conceal meaningful token boundaries.
        formatting = verdict == "WRONG_ANSWER" and re.sub(r"\s+", "", expected) == re.sub(
            r"\s+", "", actual
        )
        evidence.append(
            {
                "test_id": test_id,
                "verdict": verdict,
                "input": test_input,
                "expected": expected,
                "output": actual,
                "formatting_suspected": formatting,
            }
        )
    num_pass, num_total = map(int, header.groups())
    if len(observed) != num_total or num_total != len(suite):
        raise ValueError(
            f"test_count_mismatch: logged={len(observed)}, declared={num_total}, "
            f"canonical={len(suite)}"
        )
    if sum(state == "pass" for state in observed.values()) != num_pass:
        raise ValueError("pass_count_mismatch")
    return source, observed, evidence


def prepare(raw: Path, output: Path):
    provenance = json.loads((raw / "provenance.json").read_text(encoding="utf-8"))
    listed_paths = {record["path"] for record in provenance["files"]}
    actual_paths = {
        path.relative_to(raw).as_posix() for path in (raw / "dataset").rglob("*") if path.is_file()
    }
    actual_paths.update(name for name in ("README.md", "LICENSE") if (raw / name).is_file())
    if actual_paths != listed_paths:
        raise ValueError(
            "Raw provenance file set mismatch: "
            f"unlisted={sorted(actual_paths - listed_paths)}, "
            f"missing={sorted(listed_paths - actual_paths)}"
        )
    for record in provenance["files"]:
        if hashlib.sha256((raw / record["path"]).read_bytes()).hexdigest() != record["sha256"]:
            raise ValueError(f"Raw provenance hash mismatch: {record['path']}")
    audit = {
        "source_commit": provenance["commit"],
        "cohorts": [],
        "exclusions": [],
        "identity": "student_id unavailable; source grouping is not student-disjoint",
        "formatting_policy": "Whitespace-deletion diagnostic only; verdicts unchanged",
        "execution": "Historical logs only; student code never executed",
        "verdict_caveat": (
            "Historical WRONG_ANSWER does not establish normal termination or a logic-only error; "
            "empty failed outputs are flagged for human review, not reclassified."
        ),
    }
    for folder in sorted((raw / "dataset").glob("Lab-*/*")):
        problem_id = folder.name
        suite, version = load_suite(raw / "dataset/test", problem_id)
        rows, review, signatures = [], [], Counter()
        for path in sorted(folder.glob("*_buggy.c")):
            try:
                source, outcomes, evidence = parse_submission(
                    path.read_text(encoding="utf-8"), suite
                )
            except (ValueError, UnicodeError) as exc:
                audit["exclusions"].append(
                    {"raw_path": path.as_posix(), "problem_id": problem_id, "reason": str(exc)}
                )
                continue
            submission_id = f"itsp-{problem_id}-{path.stem}"
            rows.append(
                {
                    "submission_id": submission_id,
                    "student_id": None,
                    "problem_id": problem_id,
                    "language": "c",
                    "source_code": source,
                    "suite_version": version,
                    "outcomes": outcomes,
                    "provenance": f"ITSP@{provenance['commit']}:{path.relative_to(raw).as_posix()}",
                }
            )
            paired = path.with_name(path.name.replace("_buggy.c", "_correct.c"))
            suspected = [item["test_id"] for item in evidence if item["formatting_suspected"]]
            review.append(
                {
                    "submission_id": submission_id,
                    "raw_path": path.resolve().as_posix(),
                    "paired_correct_path": paired.resolve().as_posix() if paired.exists() else None,
                    "formatting_suspected_test_ids": suspected,
                    "empty_output_failed_test_ids": [
                        item["test_id"]
                        for item in evidence
                        if item["verdict"] == "WRONG_ANSWER" and not item["output"].strip()
                    ],
                    "all_failures_formatting_suspected": bool(suspected)
                    and len(suspected) == sum(value == "fail" for value in outcomes.values()),
                    "logged_tests": evidence,
                }
            )
            signatures[tuple(outcomes[test] for test in suite)] += 1
        target = output / "cohorts" / problem_id
        target.mkdir(parents=True, exist_ok=True)
        manifest = {
            "schema_version": 2,
            "dataset_name": "ITSP public prototype",
            "provenance": provenance["repository"],
            "source_commit": provenance["commit"],
            "problem_id": problem_id,
            "language": "c",
            "suite_version": version,
            "test_ids": list(suite),
            "official_course_dataset": False,
            "identity_policy": "unknown; source-hash-grouped split only",
            "outcome_policy": "unaltered historical verdicts; exact canonical input/oracle matching",
            "license": "MIT repository LICENSE; cite Yi et al., ESEC/FSE 2017",
            "compiler_runtime": "historical environment, not replayed",
            "lab": folder.parent.name,
            "problem_reference": (folder / "Main.c").resolve().as_posix(),
        }
        (target / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
        for filename, records in (("submissions.jsonl", rows), ("review.jsonl", review)):
            (target / filename).write_text(
                "".join(json.dumps(row) + "\n" for row in records), encoding="utf-8"
            )
        audit["cohorts"].append(
            {
                "problem_id": problem_id,
                "lab": folder.parent.name,
                "raw_buggy": len(list(folder.glob("*_buggy.c"))),
                "imported": len(rows),
                "tests": len(suite),
                "outcome_signatures": len(signatures),
                "routing": dict(
                    Counter(route_submission(Submission(**row), list(suite)) for row in rows)
                ),
                "all_pass": sum(all(s == "pass" for s in row["outcomes"].values()) for row in rows),
                "formatting_only_suspected": sum(
                    item["all_failures_formatting_suspected"] for item in review
                ),
                "formatting_any_suspected": sum(
                    bool(item["formatting_suspected_test_ids"]) for item in review
                ),
                "empty_failed_output_submissions": sum(
                    bool(item["empty_output_failed_test_ids"]) for item in review
                ),
            }
        )
    audit["total_raw_buggy"] = sum(item["raw_buggy"] for item in audit["cohorts"])
    audit["total_imported"] = sum(item["imported"] for item in audit["cohorts"])
    (output / "audit.json").write_text(json.dumps(audit, indent=2), encoding="utf-8")
    return audit

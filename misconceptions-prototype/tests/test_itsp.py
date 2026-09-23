"""Evidence tests: ordering, raw quoted strings, inconsistent logs and no label leakage."""

import hashlib
import json

import pytest

from misconceptions.itsp import load_suite, parse_submission, prepare


def logged(entries, total=None, passed=None):
    count = sum(verdict == "ACCEPTED" for verdict, _, _, _ in entries)
    head = f"/*numPass={count if passed is None else passed}, "
    head += f"numTotal={len(entries) if total is None else total}\n"
    for verdict, inp, expected, actual in entries:
        head += (
            f'Verdict:{verdict}, Visibility:1, Input:"{inp}", '
            f'ExpOutput:"{expected}", Output:"{actual}"\n'
        )
    return head + "*/\nint main(void) { return 0; }\n"


def test_match_canonical_test_identity_not_log_order():
    suite = {"1": ("one", "1\n"), "2": ("two", "2\n")}
    text = logged([("WRONG_ANSWER", "two", "2\n", "3"), ("ACCEPTED", "one", "1\n", "1\n")])
    source, outcomes, _ = parse_submission(text, suite)
    assert outcomes == {"2": "fail", "1": "pass"}
    assert source == "int main(void) { return 0; }\n"
    assert "Verdict" not in source and "numPass" not in source


def test_literal_quotes_newlines_backslashes_are_not_json_decoded():
    inp = 'say "hello"\npath \\n'
    expected = 'the "answer"\n'
    actual = 'my "wrong" answer\n'
    _, outcomes, evidence = parse_submission(
        logged([("WRONG_ANSWER", inp, expected, actual)]), {"quoted": (inp, expected)}
    )
    assert outcomes == {"quoted": "fail"}
    assert evidence[0]["output"] == actual


def test_formatting_diagnostic_preserves_failure():
    _, outcomes, evidence = parse_submission(
        logged([("WRONG_ANSWER", "a", "hello world\n", "helloworld")]),
        {"test": ("a", "hello world\n")},
    )
    assert outcomes["test"] == "fail"
    assert evidence[0]["formatting_suspected"]


@pytest.mark.parametrize(
    "text,suite,reason",
    [
        (logged([("ACCEPTED", "a", "x", "x")], passed=0), {"1": ("a", "x")}, "pass_count_mismatch"),
        (
            logged([("ACCEPTED", "a", "x", "x")]),
            {"1": ("a", "changed")},
            "test_evidence_unmatched_or_ambiguous",
        ),
        (
            logged([("ACCEPTED", "a", "x", "x")]),
            {"1": ("a", "x"), "2": ("a", "x")},
            "test_evidence_unmatched_or_ambiguous",
        ),
        (
            logged([("ACCEPTED", "a", "x", "x")]),
            {"1": ("a", "x"), "2": ("b", "y")},
            "test_count_mismatch",
        ),
        (
            logged([("ACCEPTED", "a", "x", "x"), ("ACCEPTED", "a", "x", "x")]),
            {"1": ("a", "x")},
            "duplicate_test_log",
        ),
        (logged([("MYSTERY", "a", "x", "x")]), {"1": ("a", "x")}, "unsupported_verdict"),
    ],
)
def test_inconsistent_evidence_rejected(text, suite, reason):
    with pytest.raises(ValueError, match=reason):
        parse_submission(text, suite)


def test_full_adapter_keeps_correct_pair_outside_features_and_verifies_hashes(tmp_path):
    raw, output = tmp_path / "raw", tmp_path / "prepared"
    folder = raw / "dataset/Lab-1/100"
    folder.mkdir(parents=True)
    tests = raw / "dataset/test"
    tests.mkdir()
    (tests / "in.100.1.txt").write_text("a", encoding="utf-8")
    (tests / "out.100.1.txt").write_text("x\n", encoding="utf-8")
    buggy = folder / "42_buggy.c"
    buggy.write_text(logged([("WRONG_ANSWER", "a", "x\n", "x")]), encoding="utf-8")
    (folder / "42_correct.c").write_text("/* corrected evidence */", encoding="utf-8")
    records = [
        {
            "path": p.relative_to(raw).as_posix(),
            "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
        }
        for p in raw.rglob("*")
        if p.is_file()
    ]
    (raw / "provenance.json").write_text(
        json.dumps({"commit": "pinned", "repository": "source", "files": records}), encoding="utf-8"
    )
    audit = prepare(raw, output)
    assert audit["total_imported"] == 1
    cohort = output / "cohorts/100"
    row = json.loads((cohort / "submissions.jsonl").read_text())
    review = json.loads((cohort / "review.jsonl").read_text())
    assert row["student_id"] is None
    assert "corrected evidence" not in row["source_code"]
    assert review["paired_correct_path"].endswith("42_correct.c")
    assert review["all_failures_formatting_suspected"]
    unlisted = folder / "43_buggy.c"
    unlisted.write_text(buggy.read_text(encoding="utf-8"), encoding="utf-8")
    with pytest.raises(ValueError, match="file set mismatch: unlisted=.*43_buggy"):
        prepare(raw, output)
    unlisted.unlink()
    suite, version = load_suite(tests, "100")
    assert suite == {"1": ("a", "x\n")}
    (tests / "out.100.1.txt").write_text("y", encoding="utf-8")
    assert load_suite(tests, "100")[1] != version
    with pytest.raises(ValueError, match="provenance hash mismatch"):
        prepare(raw, output)

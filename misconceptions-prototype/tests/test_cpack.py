import pytest

from misconceptions import cpack
from misconceptions.cpack import parse_metadata
from misconceptions.research_io import read_cohorts


def test_cpack_compilation_failure_is_not_pass():
    text = "# student: stu_001\n# submission: sub_001\n\n```diff\n- Compile Time Error\n```\n"
    outcomes, historical, status = parse_metadata(text, ["ex01_0"], "stu_001", "sub_001")
    assert outcomes == {"ex01_0": "not_run"}
    assert historical == {}
    assert status == "compile_error"


def test_cpack_presentation_is_failure_not_cognitive_label():
    text = ("# student: stu_001\n# submission: sub_002\n```diff\n"
            "+ ex01_0: Accepted\n! ex01_1: Presentation Error\n```\n#incorrect=1\n#correct=1\n")
    outcomes, historical, _ = parse_metadata(text, ["ex01_0", "ex01_1"], "stu_001", "sub_002")
    assert outcomes == {"ex01_0": "pass", "ex01_1": "fail"}
    assert historical["ex01_1"] == "Presentation Error"
    with pytest.raises(ValueError, match="identity"):
        parse_metadata(text, ["ex01_0", "ex01_1"], "stu_999", "sub_002")
    with pytest.raises(ValueError, match="test_ids"):
        parse_metadata(text, ["ex01_0"], "stu_001", "sub_002")
    with pytest.raises(ValueError, match="count"):
        parse_metadata(text.replace("#correct=1", "#correct=2"),
                       ["ex01_0", "ex01_1"], "stu_001", "sub_002")


def test_adapter_retains_identity_when_stdout_or_source_unusable(tmp_path, monkeypatch):
    raw = tmp_path / "raw"
    raw.mkdir()
    for name in ("README.md", "LICENSE.md"):
        (raw / name).write_text("Synthetic test fixture", encoding="utf-8")
    tests = raw / "tests/lab02/ex01"
    tests.mkdir(parents=True)
    (tests / "ex01_0.in").write_text("1\n", encoding="utf-8")
    (tests / "ex01_0.out").write_text("2\n", encoding="utf-8")
    for i, output in enumerate((b"3\n", None, b"\xff", b""), 1):
        student = f"stu_{i:03d}"
        folder = raw / "all_submissions/year-1/lab02/ex01" / student / "sub_001"
        folder.mkdir(parents=True)
        stem = f"ex01-{student}-sub_001"
        (folder / f"{stem}.c").write_text("int main(void) { return 0; }" if i != 4 else "",
                                          encoding="utf-8")
        (folder / f"{stem}.md").write_text(
            f"# student: {student}\n# submission: sub_001\n```diff\n"
            "- ex01_0: Wrong Answer\n```\n#incorrect=1\n#correct=0\n", encoding="utf-8")
        if output is not None:
            (folder / "outputs").mkdir()
            (folder / "outputs/ex01_0.out").write_bytes(output)
    monkeypatch.setattr(cpack.subprocess, "check_output",
                        lambda args, **kwargs: cpack.COMMIT if "rev-parse" in args else "")
    target = tmp_path / "prepared"
    audit = cpack.prepare(raw, target)
    assert audit["total_submissions"] == 4
    assert len(audit["missing_failed_output"]) == 1
    assert len(audit["non_utf8_output"]) == 1
    cohorts = read_cohorts(target)
    rows = cohorts[0][2]
    assert rows[1].outcomes["ex01_0"] == "not_run"
    assert rows[2].outcomes["ex01_0"] == "not_run"
    assert rows[3].source_code == ""
    assert len({r.student_id for r in rows}) == 4
    # A partial or subsequently modified import cannot receive a valid split lock.
    (target / "cohorts/lab02-ex01/review.jsonl").write_text("", encoding="utf-8")
    with pytest.raises(ValueError, match="hash mismatch"):
        read_cohorts(target)


@pytest.mark.parametrize("verdict, outcome", [
    ("Time Limit Exceeded", "timeout"),
    ("Output Limit Exceeded", "runtime_error"),
    ("Command exited with non-zero status (3)", "runtime_error"),
    ("Command terminated by signal (11: SIGSEGV)", "runtime_error"),
    ("Command terminated by signal (8: SIGFPE)", "runtime_error"),
    ("Internal Error", "not_run"),
])
def test_cpack_atat_diff_markers_preserve_execution_outcomes(verdict, outcome):
    text = ("# student: stu_001\n# submission: sub_001\n```diff\n"
            f"@@ ex01_0: {verdict}\n```\n#incorrect=1\n#correct=0\n")
    outcomes, historical, _ = parse_metadata(text, ["ex01_0"], "stu_001", "sub_001")
    assert outcomes == {"ex01_0": outcome}
    assert historical == {"ex01_0": verdict}

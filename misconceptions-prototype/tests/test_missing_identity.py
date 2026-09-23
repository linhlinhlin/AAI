from dataclasses import replace

from misconceptions.domain import Submission
from misconceptions.pipeline import leakage_groups, run_experiment


def test_missing_identity_does_not_merge_unrelated_sources():
    rows = [
        Submission(
            str(i),
            None,
            "p",
            "python",
            f"x = {i}",
            "v1",
            {"a": "fail", "b": "pass" if i % 2 else "fail"},
            "fixture",
        )
        for i in range(20)
    ]
    rows[1] = replace(rows[1], source_code=rows[0].source_code)
    groups = leakage_groups(rows)
    assert groups[0] == groups[1]
    assert len(set(groups)) == 19
    result = run_experiment(rows, test_ids=["a", "b"], k=2)
    assert result["status"] == "ok"
    assert result["identity"]["missing_student_ids"] == 20
    assert "unverified" in result["identity"]["split_guarantee"]
    assert any("not a student-disjoint" in warning for warning in result["warnings"])

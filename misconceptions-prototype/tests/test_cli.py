"""Integration checks for provider replacement and reproducible exported evidence."""

import json
import sys

from misconceptions.cli import main


def test_cli_accepts_another_cohort_without_core_changes(tmp_path, monkeypatch):
    manifest = {
        "schema_version": 1,
        "dataset_name": "second-synthetic-provider",
        "provenance": "test fixture only",
        "problem_id": "another_task",
        "language": "c",
        "suite_version": "suite-209",
        "test_ids": ["x", "y"],
    }
    rows = [
        {
            "submission_id": f"id-{i}",
            "student_id": f"person-{i}",
            "problem_id": "another_task",
            "language": "c",
            "suite_version": "suite-209",
            "source_code": f"int main(void) {{ return {i}; }}",
            "outcomes": {"x": "fail", "y": "fail" if i % 2 else "pass"},
            "provenance": "artificial adapter fixture",
        }
        for i in range(24)
    ]
    m, s, o = tmp_path / "manifest.json", tmp_path / "data.jsonl", tmp_path / "result.json"
    m.write_text(json.dumps(manifest), encoding="utf-8")
    s.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "misconceptions",
            "--manifest",
            str(m),
            "--submissions",
            str(s),
            "--output",
            str(o),
            "--k",
            "2",
        ],
    )
    main()
    result = json.loads(o.read_text(encoding="utf-8"))
    assert result["status"] == "ok"
    assert result["n_clusters"] == 2
    assert all(feature["name"].startswith("test:") for feature in result["features"])
    assert len(result["provenance"]["input_sha256"]) == 64
    main()
    assert json.loads(o.read_text(encoding="utf-8")) == result

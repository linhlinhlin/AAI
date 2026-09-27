import json

import pytest

from misconceptions.adapters import load_dataset


def write_data(tmp_path, **changes):
    manifest = {
        "schema_version": 1,
        "dataset_name": "fixture",
        "provenance": "synthetic",
        "problem_id": "p",
        "language": "python",
        "suite_version": "v1",
        "test_ids": ["a", "b"],
    }
    row = {
        "submission_id": "s",
        "student_id": "u",
        "problem_id": "p",
        "language": "python",
        "suite_version": "v1",
        "source_code": "x = 1",
        "outcomes": {"a": "fail"},
        "provenance": "synthetic",
    }
    row.update(changes)
    m, s = tmp_path / "manifest.json", tmp_path / "submissions.jsonl"
    m.write_text(json.dumps(manifest), encoding="utf-8")
    s.write_text(json.dumps(row) + "\n", encoding="utf-8")
    return m, s


def test_missing_test_is_not_pass(tmp_path):
    m, s = write_data(tmp_path)
    _, rows = load_dataset(m, s)
    assert rows[0].outcomes == {"a": "fail", "b": "not_run"}


@pytest.mark.parametrize(
    "changes",
    [
        {"problem_id": "other"},
        {"suite_version": "other"},
        {"student_id": ""},
        {"outcomes": {"c": "pass"}},
        {"outcomes": {"a": False}},
        {"misconception_label": "must_not_be_a_feature"},
    ],
)
def test_reject_invalid_contract(tmp_path, changes):
    m, s = write_data(tmp_path, **changes)
    with pytest.raises(ValueError):
        load_dataset(m, s)


def test_duplicate_ids_rejected(tmp_path):
    m, s = write_data(tmp_path)
    s.write_text(s.read_text() * 2, encoding="utf-8")
    with pytest.raises(ValueError, match="duplicate"):
        load_dataset(m, s)


def test_invalid_manifest_container(tmp_path):
    m, s = write_data(tmp_path)
    m.write_text("[]", encoding="utf-8")
    with pytest.raises(ValueError, match="schema_version"):
        load_dataset(m, s)


def test_v2_allows_explicit_unknown_identity_but_v1_does_not(tmp_path):
    m, s = write_data(tmp_path, student_id=None)
    with pytest.raises(ValueError, match="student_id"):
        load_dataset(m, s)
    manifest = json.loads(m.read_text())
    manifest["schema_version"] = 2
    m.write_text(json.dumps(manifest))
    _, rows = load_dataset(m, s)
    assert rows[0].student_id is None


def test_boolean_schema_version_rejected(tmp_path):
    m, s = write_data(tmp_path)
    manifest = json.loads(m.read_text())
    manifest["schema_version"] = True
    m.write_text(json.dumps(manifest))
    with pytest.raises(ValueError, match="schema_version"):
        load_dataset(m, s)


def test_v2_retains_empty_program_for_identity_audit(tmp_path):
    m, s = write_data(tmp_path, source_code="", outcomes={})
    manifest = json.loads(m.read_text())
    manifest["schema_version"] = 2
    m.write_text(json.dumps(manifest))
    _, rows = load_dataset(m, s)
    assert rows[0].source_code == ""
    assert set(rows[0].outcomes.values()) == {"not_run"}

import json

import pytest

from misconceptions.annotation_editor import render_editor
from misconceptions.teacher_validation import validate_form


def evidence():
    return {"schema_version": 1, "cases": [{
        "case_id": "case_1", "problem_id": "p1", "language": "c",
        "source_code": 'int main(){/* </script><script>alert(1)</script> */}',
        "outcomes": {"t1": "fail"},
        "logged_tests": [{"test_id": "t1", "input": "1", "expected": "2", "output": "1"}],
        "problem_statement": None, "evidence_kind": "recorded_logs_not_fresh_execution",
    }]}


def test_editor_keeps_blind_evidence_and_blank_compatible_form():
    packet = evidence()
    html = render_editor(packet)
    encoded = html.split('<script id="packet" type="application/json">')[1].split('</script>')[0]
    payload = json.loads(encoded)
    assert payload["cases"] == packet["cases"]
    validate_form(payload["form"], packet)
    assert all(r["status"] == "pending" and r["mechanism"] is None
               for r in payload["form"]["ratings"])
    assert "</script><script>alert(1)" not in html
    assert render_editor(packet, "reviewer_2") != html


def test_editor_rejects_cluster_annotations_and_duplicate_cases():
    packet = evidence()
    packet["cases"][0]["candidate_misconception"] = "should never enter blind form"
    with pytest.raises(ValueError, match="blind"):
        render_editor(packet)
    packet = evidence()
    packet["cases"] *= 2
    with pytest.raises(ValueError, match="Duplicate"):
        render_editor(packet)

import pytest

from misconceptions.teacher_dashboard import build_dashboard, oav_conditions, validate_mapping


def report():
    return {"population": {"s1": "a", "s2": "a", "s3": "b", "s4": "c"},
            "train_assignments": {"s1": 0, "s3": 1}, "holdout_assignments": {"s2": 0},
            "explanation": {"rules": [{"if": ["NOT (test:1=pass)", "ast:c_if=1"], "then_cluster": 0}]}}


def mapping(status="confirmed"):
    return {"cluster": "0", "status": status, "category": "misconception", "label": "Lỗi nhánh",
            "rationale": "Đối chiếu các bài và log", "follow_up": "Truy vết if"}


def test_oav_preserves_negation_and_attribute():
    result = oav_conditions(["NOT (test:1=pass)", "ast:c_if=1", "TRUE"])
    assert result[0]["operator"] == "≠" and result[0]["value"] == "pass"
    assert result[1]["attribute"] == "ast:c_if"
    assert result[2]["value"] == "Không có"


def test_denominator_includes_unassigned_and_students_are_deduplicated():
    d = build_dashboard(report(), [mapping()])
    assert d["total_submissions"] == 4 and d["unmapped_submissions"] == 2
    assert d["excluded_submissions"] == 1
    assert d["bars"][0]["submission_percent"] == 50
    assert d["bars"][0]["students"] == 1 and d["total_students"] == 3
    assert d["rules"][0]["conclusion"] == "Lỗi nhánh"


def test_missing_identity_never_becomes_student_percentage():
    r = report()
    r["population"]["s4"] = None
    d = build_dashboard(r, [mapping()])
    assert d["total_students"] is None and d["bars"][0]["student_percent"] is None


def test_drafts_are_not_counted_as_confirmed_and_mapping_is_not_carried_over():
    d = build_dashboard(report(), [mapping("draft")])
    assert d["bars"] == [] and d["confirmed_submissions"] == 0
    assert d["rules"][0]["status"] == "draft"
    assert build_dashboard(report())["rules"][0]["status"] == "unreviewed"


@pytest.mark.parametrize("change", [{"cluster": "99"}, {"rationale": ""}, {"follow_up": ""},
                                    {"status": "auto_approved"}, {"label": ""}])
def test_mapping_validation_rejects_unjustified_or_foreign_labels(change):
    with pytest.raises(ValueError):
        validate_mapping(report(), [mapping() | change], "Reviewer")


def test_multiple_clusters_with_same_label_are_aggregated():
    d = build_dashboard(report(), [mapping(), mapping() | {"cluster": "1"}])
    assert len(d["bars"]) == 1 and d["bars"][0]["submissions"] == 3

import json
from dataclasses import replace
from pathlib import Path

import pytest

from misconceptions.adapters import load_dataset
from misconceptions.domain import Submission
from misconceptions.rule_style import explanation_for, validate_explanation
from misconceptions.semantic_rules import build_teaching_report, describe_condition, diagnose
from misconceptions.teaching_report import load_evidence

SWAP = 'void swap(int a,int b){int t=a; a=b; b=t;} int main(){int x=2,y=7;swap(x,y);}'
BRANCH = ('int main(){int d=1,r=5;if(d<r) printf("Point is inside the Circle.");'
          'if(d>r) printf("Point is outside the Circle.");'
          'else printf("Point is on the Circle.");}')


def row(source):
    return Submission("s1", "student1", "p1", "c", source, "v1", {"t1": "fail"}, "synthetic")


def log(expected="7 2", output="2 7", input_text="2 7"):
    return {"test_id": "t1", "input": input_text, "expected": expected, "output": output}


def test_value_swap_requires_structure_call_and_observed_unchanged_output():
    findings = diagnose(row(SWAP), [log()])
    assert [f["rule_id"] for f in findings] == ["C_SWAP_BY_VALUE"]
    assert findings[0]["source"][0]["line_start"] == 1
    assert findings[0]["status"] == "candidate_requires_human_review"
    assert not diagnose(row(SWAP), [])
    assert not diagnose(row(SWAP), [log(output="7 2")])
    assert not diagnose(row(SWAP), [log(expected="4 5")])
    assert not diagnose(row(SWAP.replace("swap(x,y);", "")), [log()])


def test_pointer_swap_and_unrelated_assignment_are_not_value_swap():
    correct = ('void swap(int *a,int *b){int t=*a; *a=*b; *b=t;}'
               'int main(){int x=2,y=7;swap(&x,&y);}')
    assert not diagnose(row(correct), [log()])
    assert not diagnose(row(SWAP.replace("b=t", "b=a")), [log()])
    assert not diagnose(row('int main(){/* ' + SWAP + ' */}'), [log()])
    assert not diagnose(replace(row(SWAP), language="python"), [log()])
    assert not diagnose(replace(row(SWAP), outcomes={"t1": "pass"}), [log()])


def test_independent_if_requires_multiple_observed_messages():
    evidence = log("Point is inside the Circle.",
                   "Point is inside the Circle.Point is on the Circle.")
    assert [f["rule_id"] for f in diagnose(row(BRANCH), [evidence])] == ["C_BRANCH_ATTACHMENT"]
    assert not diagnose(row(BRANCH.replace('if(d>r)', 'else if(d>r)')), [evidence])
    assert not diagnose(row(BRANCH), [log("Point is inside the Circle.", "wrong")])


def test_presentation_does_not_erase_signs_or_decimal_points():
    evidence = log("Point is on the Circle.", "Point is on the Circle")
    findings = diagnose(row('int main(){printf("Point is on the Circle");}'), [evidence])
    assert findings[0]["category"] == "presentation_issue"
    for expected, actual in [("1.2", "12"), ("-2", "2"), ("0", "")]:
        assert not diagnose(row(f'int main(){{printf("{actual}");}}'), [log(expected, actual)])


def test_translation_preserves_negation_and_unknown_state():
    text = describe_condition("NOT (test:1=pass)", {})
    assert "không thỏa điều kiện" in text and "đạt" in text and "không đạt" not in text
    assert "chưa xác định" in describe_condition("ast:c_while=__unknown__", {})
    assert "con trỏ" in describe_condition("ast:c_pointer_parameter=1", {})


def test_unmatched_and_support_are_not_ground_truth():
    rows = [row(SWAP), replace(row('int main(){}'), submission_id="s2")]
    report = {"train_assignments": {"s1": 4}, "holdout_assignments": {"s2": 4}}
    result = build_teaching_report(rows, {"s1": [log()]}, report)
    assert result["n_matched"] == 1 and result["unmatched_ids"] == ["s2"]
    assert result["summaries"][0]["by_cluster"] == {"4": 1}
    assert result["human_validated"] is False
    assert "precision" not in result["summaries"][0]


def test_evidence_rejects_duplicates_and_conflicting_verdict(tmp_path):
    path = tmp_path / "review.jsonl"
    for tests in [[log(), log()], [log() | {"verdict": "ACCEPTED"}], [log() | {"test_id": "other"}]]:
        path.write_text(json.dumps({"submission_id": "s1", "logged_tests": tests}))
        with pytest.raises(ValueError):
            load_evidence(path, [row(SWAP)])


def test_itsp_branch_evidence_is_read_from_original_logs():
    cohort = Path(__file__).resolve().parents[1] / "data/itsp/cohorts/2825"
    _, rows = load_dataset(cohort / "manifest.json", cohort / "submissions.jsonl")
    logs = load_evidence(cohort / "review.jsonl", rows)
    result = build_teaching_report(rows, logs, {})
    branches = {f["submission_id"] for f in result["findings"] if f["rule_id"] == "C_BRANCH_ATTACHMENT"}
    assert branches == {"itsp-2825-271203_buggy", "itsp-2825-271205_buggy"}
    assert not any(f["rule_id"] == "C_SWAP_BY_VALUE" for f in result["findings"])


def test_all_current_rules_share_the_six_section_contract():
    examples = [(row(SWAP), [log()]),
                (row(BRANCH), [log("Point is inside the Circle.",
                                  "Point is inside the Circle.Point is on the Circle.")]),
                (row('int main(){printf("Point is on the Circle");}'),
                 [log("Point is on the Circle.", "Point is on the Circle")])]
    seen = set()
    for submission, evidence in examples:
        for finding in diagnose(submission, evidence):
            seen.add(finding["rule_id"])
            validate_explanation(finding["explanation"])
            assert finding["explanation"]["code_pattern"] == finding["if_vi"][:1]
            assert finding["explanation"]["behavioral_pattern"] == finding["if_vi"][1:]
    assert seen == {"C_SWAP_BY_VALUE", "C_BRANCH_ATTACHMENT", "OUTPUT_PRESENTATION"}


@pytest.mark.parametrize("invalid", [{"caveat": []}, {"hypothesis": ["Sinh viên chắc chắn hiểu sai."]},
                                     {"code_pattern": "Mã có if"}, {"title": ""}])
def test_rule_contract_rejects_missing_context_or_certain_diagnosis(invalid):
    value = explanation_for("C_SWAP_BY_VALUE", ["Mã có tham số thường", "Log không đổi"],
                            "Cần kiểm tra vị trí in", "Truy vết biến")
    with pytest.raises(ValueError):
        validate_explanation(value | invalid)
    del value["behavioral_pattern"]
    with pytest.raises(ValueError):
        validate_explanation(value)

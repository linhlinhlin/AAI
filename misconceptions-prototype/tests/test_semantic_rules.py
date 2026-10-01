import json
from dataclasses import replace
from pathlib import Path

import pytest

from misconceptions.adapters import load_dataset
from misconceptions.domain import Submission
from misconceptions.rule_style import explanation_for, validate_explanation
from misconceptions.semantic_rules import (
    build_teaching_report,
    describe_condition,
    diagnose,
    refresh_rule_descriptions,
)
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
    assert "không thỏa điều kiện" not in text
    assert "sai kết quả" in text and "chưa chạy" in text and "lỗi thực thi" in text
    assert "chưa xác định" in describe_condition("ast:c_while=__unknown__", {})
    assert "con trỏ" in describe_condition("ast:c_pointer_parameter=1", {})


def test_binary_test_negation_only_when_routing_guarantees_complete_execution():
    labels = {"t4": "Ca «Tọa độ âm»"}
    assert describe_condition("NOT (test:t4=fail)", labels, eligible_tests=True) == 'Ca «Tọa độ âm»: đạt'
    assert describe_condition("NOT (test:t4=pass)", labels, eligible_tests=True) == 'Ca «Tọa độ âm»: sai kết quả'
    assert "chưa chạy" in describe_condition("NOT (test:t4=fail)", labels)
    assert describe_condition("NOT (NOT (test:t4=fail))", labels) == 'Ca «Tọa độ âm»: sai kết quả'


@pytest.mark.parametrize('condition', [
    'NOT (ast:c_pointer_parameter=0)', 'NOT (ast:c_pointer_parameter=1)',
    'NOT (stdout:t1:relation=exact)', 'NOT (stdout:t1:relation=empty)',
    'NOT (stdout:t1:edit_band=zero)', 'NOT (stdout:t1:edit_band=large)',
])
def test_categorical_negation_keeps_unknown_as_an_alternative(condition):
    text = describe_condition(condition, {}, eligible_tests=True)
    assert 'HOẶC' in text
    assert 'chưa' in text
    assert 'không thỏa điều kiện' not in text


def test_saved_report_translation_preserves_original_rule_and_scope():
    report = {'train_assignments': {'a': 0}, 'holdout_assignments': {},
              'routes': {'a': 'eligible'},
              'problem': {'tests': [{'test_id': 't4', 'name': 'Tọa độ âm'}]},
              'teaching': {'cluster_rules': [{'if': ['NOT (test:t4=fail)'],
                                            'if_vi': ['old wording'], 'then_cluster': 0,
                                            'train_support': 2}]}}
    refresh_rule_descriptions(report)
    rule = report['teaching']['cluster_rules'][0]
    assert rule['if_vi'] == ['Ca «Tọa độ âm»: đạt']
    assert rule['if'] == ['NOT (test:t4=fail)'] and rule['train_support'] == 2
    report['routes']['a'] = 'incomplete'
    refresh_rule_descriptions(report)
    assert 'chưa chạy' in rule['if_vi'][0]


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


def test_dynamic_printf_presentation_requires_failed_observed_log():
    source = 'int main(){int a=2;printf("%d",a);}'
    found = diagnose(row(source), [log("2\n", "2")])
    assert [f["rule_id"] for f in found] == ["OUTPUT_PRESENTATION"]
    assert found[0]["source"][0]["code"] == 'printf("%d",a)'
    assert not diagnose(row(source), [log("12", "1 2")])
    assert not diagnose(row(source), [log("-2", "2")])
    assert not diagnose(row('int main(){/* printf("2"); */}'), [log("2\n", "2")])


def test_short_circle_messages_require_independent_branches_and_multiple_positions():
    source = 'int main(){int d=1,r=5;if(d<r) puts("INSIDE");if(d>r) puts("OUTSIDE");else puts("ON");}'
    found = diagnose(row(source), [log("INSIDE\n", "INSIDE\nON\n")])
    assert [f["rule_id"] for f in found] == ["C_BRANCH_ATTACHMENT"]
    assert not diagnose(row(source.replace('if(d>r)', 'else if(d>r)')),
                        [log("INSIDE\n", "INSIDE\nON\n")])
    assert not diagnose(row(source), [log("INSIDE\n", "OUTSIDE\n")])


def test_refresh_old_diagnostics_preserves_assignments_and_input_snapshot():
    from copy import deepcopy
    from dataclasses import asdict

    submission = row('int main(){int a=2;printf("%d",a);}')
    original = {"teaching": {"version": "old", "findings": []},
                "train_assignments": {"s1": 0}, "holdout_assignments": {},
                "submissions": [asdict(submission) | {"logged_tests": [log("2\n", "2")]}]}
    display = deepcopy(original)
    refresh_rule_descriptions(display)
    assert display["teaching"]["findings"][0]["rule_id"] == "OUTPUT_PRESENTATION"
    assert display["train_assignments"] == original["train_assignments"]
    assert original["teaching"]["findings"] == []


@pytest.mark.parametrize("problem,source,inputs,expected,actual,key", [
    ("sum-range", 'int main(){int n;scanf("%d",&n);printf("%d",n);}', "3", "6", "3", "SUM_INPUT"),
    ("sum-range", 'int main(){int n;scanf("%d",&n);printf("%d",n*n);}', "3", "6", "9", "SUM_SQUARE"),
    ("sum-range", 'int main(){int n;scanf("%d",&n);printf("%d",n*(n-1)/2);}', "3", "6", "3", "SUM_PREVIOUS"),
    ("count-positive", 'int main(){int a[2],n;int answer=0;for(int i=0;i<n;i++){if(a[i]>=0)answer++;}}',
     "2 0 1", "1", "2", "COUNT_ZERO"),
    ("max-array", 'int main(){int a[2];int answer=0;for(int i=0;i<2;i++){if(a[i]>answer)answer=a[i];}}',
     "2 -3 -1", "-1", "0", "MAX_ZERO"),
    ("max-array", 'int main(){int a[2],n;int answer=a[0];for(int i=0;i<n-1;i++){if(a[i]>answer)answer=a[i];}}',
     "2 1 3", "3", "1", "ARRAY_LAST"),
    ("circle-position", 'int main(){int x,y,r;int distance=x*x+y*y;int limit=r;if(distance<limit)puts("INSIDE");else if(distance>limit)puts("OUTSIDE");else puts("ON");}',
     "2 0 3", "INSIDE", "OUTSIDE", "CIRCLE_RADIUS"),
    ("swap", 'void f(int a,int b){int c=b;b=a;a=c;} int main(){int a=2,b=7;f(a,b);}',
     "2 7", "7 2", "2 7", "SWAP_COPY"),
    ("swap", 'void f(int *a,int *b){*a=*b;*b=*a;} int main(){int a=2,b=7;f(&a,&b);}',
     "2 7", "7 2", "7 7", "SWAP_OVERWRITE"),
])
def test_exercise_hypotheses_require_problem_code_and_concordant_failed_log(problem, source, inputs, expected, actual, key):
    submission = replace(row(source), problem_id=problem)
    logs = [log(expected, actual, inputs)]
    found = [f for f in diagnose(submission, logs) if f["rule_id"] == key]
    assert len(found) == 1
    validate_explanation(found[0]["explanation"])
    assert not any(f["rule_id"] == key for f in diagnose(replace(submission, problem_id="lab02-ex03"), logs))
    assert not diagnose(replace(submission, outcomes={"t1": "pass"}), logs)
    assert not any(f["rule_id"] == key for f in diagnose(submission, [log(expected, "99999", inputs)]))
    assert not diagnose(replace(submission, source_code="int main(){return 0;}"), logs)

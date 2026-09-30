from misconceptions.domain import Submission
from misconceptions.mechanism_hypotheses import mechanism_report

TESTS = [{"test_id": "t1", "input": "", "expected": "4\n"}, {"test_id": "t2", "input": "", "expected": "7\n"}]
RULES = {"schema": "mechanism_rules_v1", "status": "hypothesis_rules_not_diagnoses", "algorithm": "ILA-2",
         "held_out": {"seen_problems": {"macro_f1": 0.5, "coverage": 0.8, "selective_accuracy": 0.9}},
         "rules": [{"if": {"agg:newline_end": "missing"}, "then": "OUTPUT_TEXT",
                    "train_precision": 1.0, "train_true_positives": 12, "train_false_positives": 0}]}


def row(sid, outcomes, source='int main(void){printf("%d", 4); return 0;}'):
    return Submission(sid, "u", "p", "c", source, "v", outcomes, "")


def test_clusters_get_rule_hypotheses_abstentions_and_no_passing_rows():
    rows = [row("a", {"t1": "fail", "t2": "fail"}), row("b", {"t1": "fail", "t2": "fail"}),
            row("c", {"t1": "fail", "t2": "pass"}), row("d", {"t1": "pass", "t2": "pass"})]
    logs = {"a": [{"test_id": "t1", "output": "4"}, {"test_id": "t2", "output": "7"}],
            "b": [{"test_id": "t1", "output": "4"}, {"test_id": "t2", "output": "7"}],
            "c": [{"test_id": "t1", "output": "5\n"}, {"test_id": "t2", "output": "7\n"}],
            "d": [{"test_id": "t1", "output": "4\n"}, {"test_id": "t2", "output": "7\n"}]}
    report = mechanism_report(rows, logs, TESTS, {"a": 0, "b": 0, "c": 1, "d": 1}, RULES)
    assert report["status"] == "hypothesis" and "d" not in report["submissions"]
    first, second = report["clusters"]
    assert first["top_category"] == "OUTPUT_TEXT" and first["members"] == 2 and first["top_share"] == 1
    assert first["feedback"]["name"]
    assert second["top_category"] is None and second["abstained"] == 1


def test_missing_rule_file_is_reported_not_guessed(tmp_path):
    from misconceptions.mechanism_hypotheses import load_rules
    assert load_rules(tmp_path / "absent.json") is None

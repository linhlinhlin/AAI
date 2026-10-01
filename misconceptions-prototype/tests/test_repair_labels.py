import pytest

from misconceptions.domain import Submission
from misconceptions.repair_labels import (
    apply_hunks,
    classify_repair,
    ddmin,
    line_hunks,
    pair_repairs,
)

BASE = """#include <stdio.h>
int main()
{
    int i, n, s = 0, m;
    float media;
    scanf("%d", &n);
    for (i = 0; i < n; i++) {
        s = s + i;
    }
    if (s > 10) {
        printf("grande\\n");
    }
    media = s / n;
    printf("%d %.2f\\n", s, media);
    return 0;
}
"""


@pytest.mark.parametrize("old,new,expected", [
    ("i < n; i++", "i <= n; i++", "LOOP_BOUNDARY"),
    ("for (i = 0;", "for (i = 1;", "LOOP_BOUNDARY"),
    ("if (s > 10)", "if (s >= 10)", "BRANCH_CONDITION"),
    ("s = 0, m;", "s = 1, m;", "INITIALIZATION"),
    ("s = s + i;", "s = s + 2 * i;", "COMPUTATION"),
    ("media = s / n;", "media = (float) s / n;", "NUMERIC_TYPE"),
    ("    float media;", "    double media;", "NUMERIC_TYPE"),
    ('printf("%d %.2f\\n"', 'printf("%d %.1f\\n"', "OUTPUT_FORMAT"),
    ('printf("grande\\n");', 'printf("Grande\\n");', "OUTPUT_TEXT"),
    ('scanf("%d", &n);', 'scanf("%d\\n", &n);', "INPUT"),
    ("        s = s + i;\n", "        s = s + i;\n        m = i;\n", "MISSING_STATEMENT"),
    ("        s = s + i;\n", "", "EXTRA_STATEMENT"),
    ("    }\n    if (s > 10)", "        if (s > 10)", "STATEMENT_PLACEMENT"),
])
def test_single_mechanism_repairs_are_classified(old, new, expected):
    assert old in BASE
    result = classify_repair(BASE, BASE.replace(old, new, 1))
    assert result["primary"] == expected
    assert result["categories"] == [expected]


def test_moved_statement_is_placement_not_two_edits():
    moved = BASE.replace("    media = s / n;\n", "").replace(
        "        s = s + i;\n", "        s = s + i;\n    media = s / n;\n")
    assert classify_repair(BASE, moved)["categories"] == ["STATEMENT_PLACEMENT"]


def test_two_mechanisms_are_multi_not_forced_into_one():
    changed = BASE.replace("i < n; i++", "i <= n; i++").replace("s = 0, m;", "s = 1, m;")
    result = classify_repair(BASE, changed)
    assert result["primary"] == "MULTI"
    assert result["categories"] == ["INITIALIZATION", "LOOP_BOUNDARY"]


def test_apply_hunks_reconstructs_both_endpoints_and_subsets():
    new_source = BASE.replace("i < n", "i <= n").replace("grande", "Grande")
    old, new, opcodes = line_hunks(BASE, new_source)
    hunks = [i for i, op in enumerate(opcodes) if op[0] != "equal"]
    assert len(hunks) == 2
    assert apply_hunks(old, new, opcodes, set()) == BASE
    assert apply_hunks(old, new, opcodes, set(hunks)) == new_source
    assert "Grande" not in apply_hunks(old, new, opcodes, {hunks[0]})


def test_ddmin_finds_one_minimal_subset_and_respects_budget():
    needed = {3, 7}
    calls = []

    def passes(candidates):
        calls.append(len(candidates))
        return [needed <= set(candidate) for candidate in candidates]

    subset, probes, minimal = ddmin(list(range(10)), passes, budget=200)
    assert set(subset) == needed and minimal
    assert probes == sum(calls)
    _, _, minimal = ddmin(list(range(10)), passes, budget=2)
    assert not minimal


def _row(sid, student, source="int main(){return 0;}"):
    return Submission(sid, student, "p", "c", source, "v", {"t": "fail"}, "")


def test_pairs_use_the_next_passing_attempt_of_the_same_student_and_year():
    rows = [_row("a1", "s1"), _row("a2", "s1"), _row("a3", "s1"), _row("b1", "s2"), _row("c1", "s1")]
    reviews = {"a1": {"year": "y1", "attempt": "sub_001"}, "a2": {"year": "y1", "attempt": "sub_002"},
               "a3": {"year": "y1", "attempt": "sub_003"}, "b1": {"year": "y1", "attempt": "sub_001"},
               "c1": {"year": "y2", "attempt": "sub_001"}}
    outcomes = {"a1": {"t": "fail"}, "a2": {"t": "pass"}, "a3": {"t": "pass"}, "b1": {"t": "fail"},
                "c1": {"t": "pass"}}
    pairs = [(f.submission_id, r.submission_id) for f, r in pair_repairs(rows, reviews, outcomes)]
    # b1 has no later pass; c1 is another year and must not repair a1.
    assert pairs == [("a1", "a2")]


def test_missing_outcomes_never_become_a_repair_or_a_failure():
    rows = [_row("a1", "s1"), _row("a2", "s1")]
    reviews = {"a1": {"year": "y", "attempt": "sub_001"}, "a2": {"year": "y", "attempt": "sub_002"}}
    assert pair_repairs(rows, reviews, {"a1": None, "a2": {"t": "pass"}}) == []
    assert pair_repairs(rows, reviews, {"a1": {"t": "fail"}, "a2": None}) == []


def test_deleting_a_prompt_line_is_output_text_not_a_mixture():
    scan = '    scanf("%d", &n);\n'
    prompt = BASE.replace(scan, '    printf("Introduza n:\\n");\n' + scan)
    result = classify_repair(prompt, BASE)
    assert result["categories"] == ["OUTPUT_TEXT"]
    assert result["details"] == ["delete:output_literal_statement"]


def test_indentation_changes_are_not_repairs_or_moves():
    reindented = BASE.replace("        s = s + i;", "  s = s + i;").replace("i < n; i++", "i <= n; i++")
    result = classify_repair(BASE, reindented)
    assert result["categories"] == ["LOOP_BOUNDARY"]
    _, _, opcodes = line_hunks(BASE, BASE.replace("        s = s + i;", "s = s + i;"))
    assert all(op[0] == "equal" for op in opcodes)


def test_adding_an_else_branch_is_branch_structure():
    source = "int f(int x)\n{\n    int y = 0;\n    if (x > 0)\n        y = 1;\n    return y;\n}\n"
    repaired = source.replace("        y = 1;\n", "        y = 1;\n    else\n        y = 2;\n")
    assert "CONTROL_FLOW" not in classify_repair(source, repaired)["categories"]


# Regression cases from the train/validation label audit (research/runs/label-audit-20260930).
AUDIT_BASE = (
    "#include <stdio.h>\n#define HOURS 360\nint main()\n{\n"
    "    int n, num, div;\n    long n1 = 0;\n    int soma;\n"
    "    scanf(\"%d,%d\", &n, &num);\n    printf(\"%d\\n\", n / HOURS + div + soma);\n"
    "    return 0;\n}\n"
)


@pytest.mark.parametrize("old,new,expected", [
    ("int n, num, div;", "int n, num, div = 0;", ["INITIALIZATION"]),
    ("    long n1 = 0;\n    int soma;\n", "    long soma, n1 = 0;\n", ["NUMERIC_TYPE"]),
    ("#define HOURS 360", "#define HOURS 3600", ["COMPUTATION"]),
])
def test_audited_declaration_and_macro_repairs(old, new, expected):
    assert old in AUDIT_BASE
    assert classify_repair(AUDIT_BASE, AUDIT_BASE.replace(old, new, 1))["categories"] == expected


def test_initializer_moved_into_an_assignment_is_not_an_initialization_repair():
    old = "int main()\n{\n    int a, b;\n    scanf(\"%d,%d\", &a, &b);\n    int m = a;\n    return m;\n}\n"
    new = "int main()\n{\n    int a, b, m;\n    scanf(\"%d %d\", &a, &b);\n    m = a;\n    return m;\n}\n"
    assert classify_repair(old, new)["categories"] == ["INPUT"]


def test_inserting_a_whole_function_is_a_missing_statement():
    old = "#include <stdio.h>\nint main()\n{\n    return 0;\n}\n"
    new = ("#include <stdio.h>\n#define MAX 80\nint twice(int x)\n{\n    return 2 * x;\n}\n"
           "int main()\n{\n    return 0;\n}\n")
    assert classify_repair(old, new)["categories"] == ["MISSING_STATEMENT"]


def test_a_new_helper_declaration_alone_is_scaffolding():
    old = "int main()\n{\n    int a = 1;\n    return a;\n}\n"
    new = "#define MAX 80\nint main()\n{\n    int a = 1;\n    int unused;\n    return a;\n}\n"
    assert classify_repair(old, new)["primary"] == "NO_CHANGE"

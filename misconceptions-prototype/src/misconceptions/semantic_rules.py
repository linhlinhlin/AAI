"""Small, evidence-gated teaching hypotheses; never human annotation or ground truth."""

import re
from collections import Counter
from itertools import pairwise

import tree_sitter_c
from tree_sitter import Language, Parser

from .rule_style import STYLE_VERSION, explanation_for

VERSION = "teaching-rules-v2"
RULE_OAV = {
    "C_BRANCH_ATTACHMENT": [
        ("Khối lệnh trong bài", "Có hai if liên tiếp, if đầu không có else", "Có"),
        ("Khối lệnh trong bài", "Else thuộc if thứ hai", "Có"),
        ("Ca kiểm thử trượt", "Yêu cầu một vị trí nhưng output có nhiều vị trí", "Có"),
    ],
    "C_SWAP_BY_VALUE": [
        ("Hàm hoán vị trong bài", "Kiểu trả về", "void"),
        ("Hàm hoán vị trong bài", "Tham số", "Hai tham số số học thường cùng kiểu"),
        ("Hàm hoán vị trong bài", "Thân hàm", "Hoán vị qua biến tạm"),
        ("Lời gọi hàm trong bài", "Đối số", "Hai biến thường"),
        ("Ca kiểm thử trượt", "Output giữ nguyên input trong khi expected đảo thứ tự", "Có"),
    ],
    "OUTPUT_PRESENTATION": [
        ("Mã bài làm", "Chứa chuỗi output quan sát được", "Có"),
        ("Ca kiểm thử trượt", "Sai khác expected và actual",
         "Chỉ hoa/thường, khoảng trắng hoặc dấu chấm cuối thông báo đường tròn"),
    ],
}
CIRCLE = {f"Point is {position} the Circle.": label for position, label in
          [("inside", "trong"), ("on", "trên biên"), ("outside", "ngoài")]}
AST_LABELS = {
    "for": "vòng lặp for", "while": "vòng lặp while", "do": "vòng lặp do",
    "if": "câu lệnh if", "range": "lời gọi range", "return": "lệnh return",
    "inclusive_comparison": "phép so sánh ≤ hoặc ≥", "strict_comparison": "phép so sánh < hoặc >",
    "subscript": "truy cập phần tử bằng chỉ số", "zero_index": "truy cập chỉ số 0",
    "one_index": "truy cập chỉ số 1", "pointer_declarator": "khai báo con trỏ",
    "pointer_parameter": "tham số con trỏ", "array_parameter": "tham số mảng",
    "address_of": "toán tử lấy địa chỉ &", "dereference": "toán tử giải tham chiếu *",
    "update": "phép tăng/giảm ++ hoặc --", "augassign": "phép gán kết hợp như +=",
}
STATES = {"pass": "đạt", "fail": "không đạt", "not_run": "chưa chạy",
          "runtime_error": "lỗi thực thi", "timeout": "hết thời gian",
          "__unknown__": "chưa xác định"}


def walk(node):
    stack = [node]
    while stack:
        current = stack.pop()
        if current.type == "comment":
            continue
        yield current
        stack.extend(reversed(current.named_children))


def source_evidence(node):
    return {"line_start": node.start_point.row + 1, "line_end": node.end_point.row + 1,
            "code": node.text.decode("utf-8")}


def describe_condition(condition, test_labels):
    if condition == "TRUE":
        return "mọi bài trong phạm vi của luật"
    if condition.startswith("NOT (") and condition.endswith(")"):
        return "không thỏa điều kiện: [" + describe_condition(condition[5:-1], test_labels) + "]"
    feature, _, value = condition.rpartition("=")
    if feature.startswith("test:"):
        test = feature[5:]
        return f"{test_labels.get(test, 'Ca kiểm thử ' + test)}: {STATES.get(value, value)}"
    if feature.startswith("ast:"):
        name = feature[4:].removeprefix("c_")
        label = AST_LABELS.get(name, name)
        if value in {"0", "1"}:
            return ("mã có " if value == "1" else "không ghi nhận trong mã: ") + label
        return f"{label}: {STATES.get(value, value)}"
    return condition


def _independent_branches(root):
    matches = []
    for block in walk(root):
        if block.type != "compound_statement":
            continue
        statements = [n for n in block.named_children if n.type != "comment"]
        for first, second in pairwise(statements):
            if (first.type == second.type == "if_statement"
                    and first.child_by_field_name("alternative") is None
                    and second.child_by_field_name("alternative") is not None):
                matches.extend([source_evidence(first), source_evidence(second)])
    return matches


def _value_swap(root):
    """Recognize only a straight-line scalar swap with a temporary and a direct call."""
    nodes = list(walk(root))
    matches = []
    for function in nodes:
        if function.type != "function_definition":
            continue
        declarator = function.child_by_field_name("declarator")
        if declarator.type != "function_declarator":
            continue
        name = declarator.child_by_field_name("declarator")
        if name.type != "identifier" or function.child_by_field_name("type").text != b"void":
            continue
        params = declarator.child_by_field_name("parameters").named_children
        if len(params) != 2 or any(p.type != "parameter_declaration" for p in params):
            continue
        identifiers = [p.child_by_field_name("declarator") for p in params]
        types = [p.child_by_field_name("type") for p in params]
        if (any(p is None or p.type != "identifier" for p in identifiers)
                or any(t is None or t.text not in {b"int", b"float", b"double"} for t in types)
                or types[0].text != types[1].text):
            continue
        a, b = [re.escape(p.text.decode()) for p in identifiers]
        primitive = types[0].text.decode()
        body = function.child_by_field_name("body")
        # Strip comments through AST byte ranges, not a regex that could alter string literals.
        text = body.text.decode()
        for comment in reversed([n for n in body.named_children if n.type == "comment"]):
            # Canonical bodies below contain ASCII only; comments can have arbitrary UTF-8.
            text = text.replace(comment.text.decode(), "")
        pattern = (rf"\{{\s*{primitive}\s+([A-Za-z_]\w*)\s*=\s*{a}\s*;"
                   rf"\s*{a}\s*=\s*{b}\s*;\s*{b}\s*=\s*\1\s*;\s*\}}")
        matched = re.fullmatch(pattern, text)
        if not matched or matched[1] in [p.text.decode() for p in identifiers]:
            continue
        for call in nodes:
            if call.type != "call_expression":
                continue
            callee = call.child_by_field_name("function")
            args = call.child_by_field_name("arguments").named_children
            if (callee.text == name.text and call.parent.type == "expression_statement"
                    and len(args) == 2 and all(n.type == "identifier" for n in args)):
                matches.extend([source_evidence(function), source_evidence(call)])
    return matches


def _output_form(text):
    # Do not erase numeric signs, decimal points or arbitrary punctuation.
    return " ".join(text.split()).casefold()


def _swap_log(test):
    source, expected, actual = [test[key].split() for key in ("input", "expected", "output")]
    return (len(source) == 2 and source[0] != source[1]
            and all(re.fullmatch(r"-?\d+", x) for x in source)
            and expected == source[::-1] and actual == source)


def diagnose(row, logs):
    failed = [t for t in logs if row.outcomes.get(t["test_id"]) == "fail"]
    if row.language.lower() != "c" or not failed:
        return []
    root = Parser(Language(tree_sitter_c.language())).parse(row.source_code.encode()).root_node
    if root.has_error:
        return []
    findings = []

    def add(rule_id, conditions, conclusion, category, code, tests, alternative, suggestion):
        if not code or not tests:
            return
        findings.append({"rule_id": rule_id, "submission_id": row.submission_id,
                         "if_vi": conditions, "then_vi": conclusion, "category": category,
                         "status": "candidate_requires_human_review", "source": code,
                         "explanation": explanation_for(rule_id, conditions, alternative, suggestion),
                         "conditions_oav": [{"object": obj, "attribute": attr,
                                             "operator": "=", "value": value}
                                            for obj, attr, value in RULE_OAV[rule_id]],
                         "tests": tests, "alternative": alternative, "suggestion": suggestion})

    branch_tests = []
    for test in failed:
        messages = re.findall(r"Point is (?:inside|on|outside) the Circle\.", test["output"])
        if test["expected"] in CIRCLE and len(set(messages)) >= 2:
            branch_tests.append(test)
    add("C_BRANCH_ATTACHMENT", ["mã có hai if liên tiếp; else thuộc if thứ hai",
                                "một test yêu cầu một vị trí nhưng output chứa nhiều vị trí"],
        "Nghi vấn nhầm quan hệ if–else và tính loại trừ giữa các nhánh",
        "conceptual_hypothesis", _independent_branches(root), branch_tests,
        "Có thể là thiếu từ khóa else do sơ suất; chưa chứng minh sinh viên hiểu sai.",
        "Yêu cầu sinh viên truy vết từng if với chính input đã trượt; đối chiếu if / else if / else.")
    add("C_SWAP_BY_VALUE", ["hàm void hoán vị hai tham số số học thường qua biến tạm",
                           ("hàm được gọi bằng hai biến; log test cho output giữ nguyên input, "
                            "trong khi expected đảo thứ tự")],
        "Nghi vấn chưa hiểu truyền tham trị: đổi tham số cục bộ không đổi biến ở hàm gọi",
        "conceptual_hypothesis", _value_swap(root), [t for t in failed if _swap_log(t)],
        "Cần kiểm tra vị trí in, luồng gọi và việc gán lại biến; chưa có trace trạng thái sau lời gọi.",
        "Truy vết bản sao tham số và biến của hàm gọi; thử hoán vị qua địa chỉ và giải tham chiếu.")
    formatting = [t for t in failed if t["expected"] != t["output"] and (
        _output_form(t["expected"]) == _output_form(t["output"])
        or (t["expected"] in CIRCLE
            and _output_form(t["expected"]).removesuffix(".")
            == _output_form(t["output"]).removesuffix(".")))]
    literals = [source_evidence(n) for n in walk(root) if n.type == "string_literal"
                and any(t["output"].strip() and t["output"].strip() in n.text.decode()
                        for t in formatting)]
    add("OUTPUT_PRESENTATION", ["mã chứa chuỗi được in trong test trượt",
                                 ("expected và actual chỉ khác chữ hoa/thường, khoảng trắng "
                                  "hoặc dấu chấm cuối thông báo vị trí đường tròn")],
        "Sai khác trình bày output; chưa có bằng chứng về lỗi khái niệm từ sai khác này",
        "presentation_issue", literals, formatting,
        "Các test khác vẫn có thể chứa lỗi logic; không gán kết luận cho toàn bộ bài.",
        "Đối chiếu chuỗi output với yêu cầu chấm trước khi diễn giải thành misconception.")
    return findings


def build_teaching_report(rows, logs, report):
    findings = [finding for row in rows for finding in diagnose(row, logs.get(row.submission_id, []))]
    by_id = {row.submission_id: row for row in rows}
    assignments = report.get("train_assignments", {}) | report.get("holdout_assignments", {})
    for finding in findings:
        finding["cluster"] = assignments.get(finding["submission_id"])
        finding["split"] = ("train" if finding["submission_id"] in report.get("train_assignments", {})
                            else "holdout" if finding["submission_id"] in assignments else "unassigned")
    summaries = []
    for rule_id in sorted({f["rule_id"] for f in findings}):
        matched = [f for f in findings if f["rule_id"] == rule_id]
        summaries.append({"rule_id": rule_id, "if_vi": matched[0]["if_vi"],
                          "then_vi": matched[0]["then_vi"], "category": matched[0]["category"],
                          "explanation": matched[0]["explanation"],
                          "n_submissions": len({f["submission_id"] for f in matched}),
                          "by_split": dict(Counter(f["split"] for f in matched)),
                          "by_cluster": dict(Counter(str(f["cluster"]) for f in matched))})
    labels = {}
    for test in {t for row in rows for t in row.outcomes}:
        expected = {t["expected"] for tests in logs.values() for t in tests if t["test_id"] == test}
        if len(expected) == 1 and next(iter(expected)) in CIRCLE:
            labels[test] = f"Ca {test} — yêu cầu thông báo điểm {CIRCLE[next(iter(expected))]} đường tròn"
    translated = [dict(rule, if_vi=[describe_condition(c, labels) for c in rule["if"]])
                  for rule in report.get("explanation", {}).get("rules", [])]
    matched_ids = {f["submission_id"] for f in findings}
    return {"version": VERSION, "style_version": STYLE_VERSION,
            "origin": "hand_authored_evidence_rules_not_learned_labels",
            "human_validated": False, "findings": findings, "summaries": summaries,
            "cluster_rules": translated, "n_analyzed": len(by_id),
            "n_with_logs": sum(bool(logs.get(sid)) for sid in by_id),
            "n_matched": len(matched_ids), "unmatched_ids": sorted(set(by_id) - matched_ids),
            "interpretation": "Số bài khớp điều kiện, không phải precision hay số sinh viên hiểu sai. "
            "Không có luật khớp không có nghĩa bài đúng. Không dùng làm nhãn đánh giá clustering."}

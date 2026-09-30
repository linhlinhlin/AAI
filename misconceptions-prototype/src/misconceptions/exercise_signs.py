"""Narrow hypotheses for authored app exercises, gated by AST and recorded failures.

These rules do not apply to public corpus problem IDs or alter clustering features.
"""
import re


def exercise_signs(problem, nodes, failed):
    def text(node):
        return re.sub(r"\s+", "", node.text.decode()) if node is not None else ""

    def evidence(selected):
        return [{"line_start": n.start_point.row + 1, "line_end": n.end_point.row + 1,
                 "code": n.text.decode()} for n in selected]

    def numbers(test):
        try:
            return [int(x) for x in test["input"].split()], int(test["expected"]), int(test["output"])
        except ValueError:
            return None

    numeric = [(t, numbers(t)) for t in failed if numbers(t) is not None]
    found = []

    def add(key, title, pattern, selected, tests, hint):
        if selected and tests:
            found.append((key, title, pattern, evidence(selected), tests, hint))

    if problem == "sum-range":
        calls = [n for n in nodes if n.type == "call_expression"
                 and n.child_by_field_name("function").text == b"printf"]
        for key, expr, title, compute in [
            ("SUM_INPUT", "n", "In lại n, chưa tính tổng từ 1 đến n", lambda n: n),
            ("SUM_SQUARE", "n*n", "Dùng n nhân n thay cho tổng từ 1 đến n", lambda n: n*n),
            ("SUM_PREVIOUS", "n*(n-1)/2", "Công thức đang tính tổng đến n−1, thiếu số n", lambda n: n*(n-1)//2),
        ]:
            selected = [n for n in calls if len(n.child_by_field_name("arguments").named_children) == 2
                        and text(n.child_by_field_name("arguments").named_children[1]) == expr]
            tests = [t for t, (xs, expected, actual) in numeric if len(xs) == 1 and xs[0] >= 0
                     and expected == xs[0]*(xs[0]+1)//2 and actual == compute(xs[0]) and actual != expected]
            add(key, title, f"Lệnh printf dùng biểu thức {expr}", selected, tests,
                "Truy vết với n=3: tổng cần là 1+2+3; đối chiếu biểu thức được in.")

    if problem in {"max-array", "count-positive"}:
        arrays = [(t, xs[1:], expected, actual) for t, (xs, expected, actual) in numeric
                  if xs and xs[0] == len(xs)-1 and xs[0] > 0]
        if problem == "count-positive":
            selected = [n for n in nodes if n.type == "if_statement"
                        and re.fullmatch(r"\([A-Za-z_]\w*\[[A-Za-z_]\w*\]>=0\)",
                                         text(n.child_by_field_name("condition")))]
            tests = [t for t, xs, expected, actual in arrays if 0 in xs
                     and expected == sum(x > 0 for x in xs)
                     and actual == sum(x >= 0 for x in xs) and actual != expected]
            add("COUNT_ZERO", "Có dấu hiệu đếm cả số 0 vào số dương",
                "Nhánh kiểm tra phần tử mảng dùng >= 0", selected, tests,
                "So sánh > 0 với >= 0 trên mảng có số 0.")
        else:
            # Tie the zero initializer to the variable updated from an array element.
            selected = []
            for n in nodes:
                if n.type != "init_declarator" or text(n.child_by_field_name("value")) != "0":
                    continue
                name = text(n.child_by_field_name("declarator"))
                updates = [a for a in nodes if a.type == "assignment_expression"
                           and text(a.child_by_field_name("left")) == name
                           and a.child_by_field_name("right").type == "subscript_expression"]
                if updates:
                    selected.extend([n, *updates])
            tests = [t for t, xs, expected, actual in arrays
                     if max(xs) < 0 and expected == max(xs) and actual == 0]
            add("MAX_ZERO", "Có dấu hiệu khởi tạo giá trị lớn nhất bằng 0 nên sai với mảng toàn âm",
                "Biến nhận phần tử mảng được khởi tạo bằng 0", selected, tests,
                "Khởi tạo từ phần tử đầu tiên và truy vết mảng toàn số âm.")
        loops = [n for n in nodes if n.type in {"for_statement", "while_statement", "do_statement"}
                 and "scanf" not in text(n)
                 and (re.search(r"<n-1\)?$", text(n.child_by_field_name("condition")))
                      or (n.type == "for_statement" and "=(n-1)-1" in text(n)))]
        tests = [t for t, xs, expected, actual in arrays if len(xs) > 1 and actual != expected
                 and ((problem == "max-array" and expected == max(xs) and actual == max(xs[:-1]))
                      or (problem == "count-positive" and expected == sum(x > 0 for x in xs)
                          and actual == sum(x > 0 for x in xs[:-1]))) ]
        add("ARRAY_LAST", "Có dấu hiệu bỏ sót phần tử cuối mảng",
            "Vòng xử lý có cận n−1 hoặc bắt đầu duyệt ngược từ n−2", loops, tests,
            "Truy vết chỉ số cuối n−1, đặt phần tử quyết định kết quả ở cuối mảng.")
    if problem == "circle-position":
        limits = [n for n in nodes if n.type == "init_declarator" and text(n) == "limit=r"]
        distances = [n for n in nodes if n.type == "init_declarator"
                     and text(n).replace("(", "").replace(")", "")
                     in {"distance=x*x+y*y", "distance=y*y+x*x"}]
        comparisons = [n for n in nodes if n.type == "binary_expression"
                       and text(n) in {"distance<limit", "distance>limit"}]
        tests = []
        for t in failed:
            try:
                x, y, radius = map(int, t["input"].split())
            except ValueError:
                continue
            distance = x*x + y*y
            def classify(limit, distance=distance):
                return "INSIDE" if distance < limit else "OUTSIDE" if distance > limit else "ON"
            if (radius > 1 and t["expected"].strip() == classify(radius*radius)
                    and t["output"].strip() == classify(radius)
                    and t["expected"].strip() != t["output"].strip()):
                tests.append(t)
        add("CIRCLE_RADIUS", "Có dấu hiệu so sánh bình phương khoảng cách với r thay vì r²",
            "Code tính distance=x*x+y*y, gán limit=r rồi so sánh distance với limit",
            limits + distances + comparisons if limits and distances and comparisons else [], tests,
            "So sánh hai đại lượng cùng đơn vị: x²+y² với r²; thử r lớn hơn 1.")
    return found

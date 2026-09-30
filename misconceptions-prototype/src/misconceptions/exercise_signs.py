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
    if problem == "swap":
        pairs = []
        for t in failed:
            try:
                given, shown = ([int(x) for x in t[key].split()] for key in ("input", "output"))
            except ValueError:
                continue
            if len(given) == 2 and given[0] != given[1] and len(shown) == 2:
                pairs.append((t, given, shown))

        def parameters(node):
            declarator = node.child_by_field_name("declarator")
            if (node.type != "function_definition" or declarator is None
                    or declarator.type != "function_declarator"
                    or text(node.child_by_field_name("type")) != "void"):
                return []
            params = [p for p in declarator.child_by_field_name("parameters").named_children
                      if p.type == "parameter_declaration"]
            found_params = [p.child_by_field_name("declarator") for p in params]
            return found_params if len(found_params) == 2 and None not in found_params else []

        functions = [(n, [p.type for p in parameters(n)]) for n in nodes]
        add("SWAP_COPY", "Có dấu hiệu hoán vị trên bản sao tham số nên a, b ở main không đổi",
            "Hàm void nhận hai tham số thường, không nhận địa chỉ",
            [n for n, kinds in functions if kinds == ["identifier", "identifier"]],
            [t for t, given, shown in pairs if shown == given],
            "Hỏi a và b trong main bằng bao nhiêu ngay sau lời gọi hàm, với input 2 7.")
        add("SWAP_OVERWRITE", "Có dấu hiệu ghi đè một giá trị trước khi lưu lại nên hai số in ra trùng nhau",
            "Hàm void nhận hai con trỏ và gán giá trị qua chúng",
            [n for n, kinds in functions if kinds == ["pointer_declarator", "pointer_declarator"]],
            [t for t, given, shown in pairs if shown[0] == shown[1] and shown[0] in given],
            "Hỏi *a và *b bằng bao nhiêu ngay sau lệnh gán đầu tiên, với input 2 7.")
    return found

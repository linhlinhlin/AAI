"""Label-free, problem-agnostic OAV describing *how* output deviates from the oracle.

Inputs are only the failing program, its own replayed runs and the task's oracles.
No later submission, repair, label, reviewer note or source path is read here.
"""

import math
import re
from collections import Counter

import tree_sitter_c
from tree_sitter import Language, Parser

NUMBER = re.compile(r"-?\d+(?:\.\d+)?")
WORD = re.compile(r"[^\W\d_]+", re.UNICODE)
SPEC = re.compile(r"%[-+ #0]*(\d+|\*)?(\.(\d+|\*))?(hh|h|ll|l|L|j|z|t)?[diouxXeEfFgGaAcspn%]")
OUTPUT_FUNCS = {"printf", "puts", "putchar", "fprintf", "fputs"}
LOOPS = {"for_statement", "while_statement", "do_statement"}
_PARSER = Parser(Language(tree_sitter_c.language()))

DEVIATION_ATTRIBUTES = ("status", "lines", "newline_end", "whitespace_only", "numbers", "text",
                        "first_diff", "prefix", "other_oracle")


def _numbers(text):
    return [m.group(0) for m in NUMBER.finditer(text)]


def _number_relation(actual, expected):
    try:
        a, e = float(actual), float(expected)
    except ValueError:
        return "other"
    if a == e:
        return "format_only"  # Same value, different spelling (e.g. 2 vs 2.00).
    if "." in expected and a == math.trunc(e):
        return "truncated"
    if "." in expected or "." in actual:
        decimals = len(expected.split(".")[1]) if "." in expected else 0
        if decimals and round(a, decimals) == round(e, decimals) or abs(a - e) < 0.05 * max(1, abs(e)):
            return "precision"
    if abs(a - e) == 1:
        return "off_by_one"
    if a == -e:
        return "sign"
    if a == 0:
        return "zero"
    if e != 0 and (a / e) in (2, 0.5, 10, 0.1):
        return "scale"
    return "other"


def _edit_distance(a, b, limit=3):
    if abs(len(a) - len(b)) > limit:
        return limit + 1
    previous = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        current = [i]
        for j, cb in enumerate(b, 1):
            current.append(min(previous[j] + 1, current[j - 1] + 1, previous[j - 1] + (ca != cb)))
        previous = current
    return previous[-1]


def _text_relation(actual, expected):
    aw, ew = WORD.findall(actual), WORD.findall(expected)
    if aw == ew:
        return "same"
    if [w.lower() for w in aw] == [w.lower() for w in ew]:
        return "case_only"
    if len(aw) == len(ew) and all(_edit_distance(x.lower(), y.lower()) <= 2 for x, y in zip(aw, ew)):
        return "typo"
    if len(aw) < len(ew) and all(w in ew for w in aw):
        return "missing_words"
    if len(aw) > len(ew) and all(w in aw for w in ew):
        return "extra_words"
    return "different"


def deviation(actual, expected, oracles, outcome):
    """Descriptor dict for one test run."""
    if outcome != "fail":
        return dict.fromkeys(DEVIATION_ATTRIBUTES, "n/a") | {"status": outcome}
    a_lines, e_lines = actual.rstrip("\n").split("\n"), expected.rstrip("\n").split("\n")
    lines = "same" if len(a_lines) == len(e_lines) else "fewer" if len(a_lines) < len(e_lines) else "more"
    if expected.endswith("\n") and not actual.endswith("\n"):
        newline_end = "missing"
    elif actual.endswith("\n\n") and not expected.endswith("\n\n"):
        newline_end = "extra"
    else:
        newline_end = "same"
    whitespace_only = "yes" if actual.split() == expected.split() else "no"
    a_num, e_num = _numbers(actual), _numbers(expected)
    if not e_num and not a_num:
        numbers = "none"
    elif len(a_num) != len(e_num):
        numbers = "fewer" if len(a_num) < len(e_num) else "more"
    else:
        kinds = {_number_relation(x, y) for x, y in zip(a_num, e_num) if x != y}
        numbers = "equal" if not kinds else kinds.pop() if len(kinds) == 1 else "mixed"
    first = next((i for i, (x, y) in enumerate(zip(a_lines, e_lines)) if x != y), None)
    if first is None:
        first_diff = "after_common_prefix"
    elif first == 0:
        first_diff = "first_line"
    elif first == len(e_lines) - 1:
        first_diff = "last_line"
    else:
        first_diff = "middle"
    if actual and expected.startswith(actual):
        prefix = "truncated"
    elif expected and actual.startswith(expected):
        prefix = "extended"
    elif not actual:
        prefix = "empty"
    else:
        prefix = "neither"
    return {"status": "fail", "lines": lines, "newline_end": newline_end,
            "whitespace_only": whitespace_only, "numbers": numbers,
            "text": _text_relation(actual, expected), "first_diff": first_diff, "prefix": prefix,
            "other_oracle": "yes" if actual in oracles and actual != expected else "no"}


def deviation_oav(runs, oracles):
    """Per-test and aggregated deviation OAV. `runs`: test_id -> (outcome, stdout, expected)."""
    values = {}
    failing = []
    for tid, (outcome, actual, expected) in sorted(runs.items()):
        descriptor = deviation(actual or "", expected, oracles, outcome)
        for name, value in descriptor.items():
            values[f"dev:{tid}:{name}"] = value
        if outcome != "pass":
            failing.append(descriptor)
    # Problem-agnostic summary: the most frequent value across non-passing tests.
    for name in DEVIATION_ATTRIBUTES:
        counts = Counter(d[name] for d in failing)
        values[f"agg:{name}"] = counts.most_common(1)[0][0] if counts else "none"
    values["agg:fail_fraction"] = _bucket(len(failing) / max(1, len(runs)))
    return values


def _bucket(fraction):
    return "all" if fraction == 1 else "most" if fraction >= 0.5 else "some" if fraction > 0 else "none"


def code_cues(source, oracles):
    """Static relational cues: generic, defined before evaluation, never learned from labels."""
    data = source.encode("utf-8")
    root = _PARSER.parse(data).root_node
    oracle_words = {w.lower() for text in oracles for w in WORD.findall(text)}
    cues = Counter()
    literals = []
    for node in _walk(root):
        parent = node.parent
        if node.type == "binary_expression" and parent is not None:
            op = node.child_by_field_name("operator")
            text = op.text.decode() if op is not None else ""
            owner = _owner(node)
            if owner in LOOPS and text in ("<", ">"):
                cues["loop_strict"] = 1
            if owner in LOOPS and text in ("<=", ">="):
                cues["loop_inclusive"] = 1
            if text == "/":
                cues["division"] = 1
                if not any(n.type == "cast_expression" or n.type == "number_literal" and b"." in n.text
                           for n in _walk(node)):
                    cues["division_without_float"] = 1
            if text == "%":
                cues["modulo"] = 1
        elif node.type == "for_statement":
            init = node.child_by_field_name("initializer")
            if init is not None and init.type == "assignment_expression":
                value = init.child_by_field_name("right")
                if value is not None and value.type == "number_literal" and value.text != b"0":
                    cues["loop_starts_nonzero"] = 1
        elif node.type == "init_declarator":
            value = node.child_by_field_name("value")
            if value is not None and value.type == "number_literal":
                cues["init_" + ("zero" if value.text == b"0" else "one" if value.text == b"1" else "other")] = 1
        elif node.type == "cast_expression":
            cues["float_cast"] = 1
        elif node.type == "primitive_type" and node.text in (b"float", b"double"):
            cues["float_declared"] = 1
        elif node.type == "call_expression":
            name = node.child_by_field_name("function")
            name = name.text.decode() if name is not None else ""
            if name in OUTPUT_FUNCS:
                cues["n_output_calls"] += 1
                if any(a.type in LOOPS for a in _ancestors(node)):
                    cues["output_in_loop"] = 1
                arguments = node.child_by_field_name("arguments")
                literal = next((a for a in arguments.named_children if a.type == "string_literal"),
                               None) if arguments is not None else None
                if literal is not None:
                    literals.append(literal.text.decode("utf-8", errors="replace"))
            elif name in ("scanf", "getchar", "fgets", "getc"):
                cues["n_input_calls"] += 1
        elif node.type in ("break_statement", "return_statement") and _in_loop(node):
            cues["exit_inside_loop"] = 1
    precisions = sorted({m.group(3) for text in literals for m in SPEC.finditer(text) if m.group(3)})
    words = {w.lower() for text in literals for w in WORD.findall(text.replace("\\n", " "))}
    words -= {"d", "f", "lf", "c", "s", "n", "i", "u", "x", "ld", "lu"}
    result = {f"code:{name}": "1" if cues.get(name) else "0" for name in (
        "loop_strict", "loop_inclusive", "division", "division_without_float", "modulo",
        "loop_starts_nonzero", "init_zero", "init_one", "init_other", "float_cast", "float_declared",
        "output_in_loop", "exit_inside_loop")}
    result["code:output_calls"] = _count_bucket(cues["n_output_calls"])
    result["code:input_calls"] = _count_bucket(cues["n_input_calls"])
    result["code:printf_precision"] = ",".join(precisions) or "none"
    result["code:last_literal_newline"] = ("yes" if literals and literals[-1].endswith('\\n"') else
                                           "no" if literals else "none")
    result["code:words_outside_oracle"] = "yes" if words - oracle_words else "no"
    return result


def _count_bucket(count):
    return "0" if count == 0 else "1" if count == 1 else "2" if count == 2 else "3-5" if count <= 5 else "6+"


def _walk(node):
    stack = [node]
    while stack:
        current = stack.pop()
        yield current
        stack.extend(current.children)


def _ancestors(node):
    node = node.parent
    while node is not None:
        yield node
        node = node.parent


def _owner(node):
    """Statement kind whose condition contains `node`, if any."""
    current = node
    for parent in _ancestors(node):
        if parent.type in LOOPS or parent.type == "if_statement":
            condition = parent.child_by_field_name("condition")
            if condition is not None and condition.start_byte <= current.start_byte and \
                    current.end_byte <= condition.end_byte:
                return parent.type
            return None
        current = parent
    return None


def _in_loop(node):
    return any(parent.type in LOOPS for parent in _ancestors(node))

"""Controlled mechanism injection into accepted student programs (known ground truth).

Each operator performs exactly one syntactic edit whose mechanism category is known by
construction and uses the taxonomy of `repair_labels`. Mutants are candidate failures
only after the isolated runner shows they compile without warnings and fail a test.
"""

import random
import re

import tree_sitter_c
from tree_sitter import Language, Parser

from .repair_labels import LOOPS, OUTPUT_FUNCS, SPEC, _call_name, _field_of, _inside_loop_body

_PARSER = Parser(Language(tree_sitter_c.language()))
STRICT = {"<": "<=", "<=": "<", ">": ">=", ">=": ">"}
ARITH = {"+": "-", "-": "+", "*": "+", "/": "*", "%": "/"}


def _nodes(root):
    stack = [root]
    while stack:
        node = stack.pop()
        yield node
        stack.extend(reversed(node.children))


def _in_field(node, kinds, fields):
    current = node
    while current.parent is not None:
        parent = current.parent
        if parent.type in kinds and _field_of(current, parent) in fields:
            return True
        if parent.type in ("compound_statement", "function_definition"):
            return False
        current = parent
    return False


def _edit(data, start, end, replacement):
    return data[:start] + replacement + data[end:]


def _operator(node):
    operator = node.child_by_field_name("operator")
    return operator if operator is not None else None


def sites(source):
    """All candidate single edits: (category, operator_id, start, end, replacement bytes)."""
    data = source.encode("utf-8")
    root = _PARSER.parse(data).root_node
    if root.has_error:
        return []
    found = []
    for node in _nodes(root):
        if node.type == "binary_expression" and (op := _operator(node)) is not None:
            text = op.text.decode()
            in_loop = _in_field(node, LOOPS, ("condition",))
            in_branch = _in_field(node, ("if_statement", "conditional_expression", "switch_statement"),
                                  ("condition",))
            if text in STRICT and in_loop:
                found.append(("LOOP_BOUNDARY", "loop_strictness", op.start_byte, op.end_byte,
                              STRICT[text].encode()))
            elif text in STRICT and in_branch:
                found.append(("BRANCH_CONDITION", "branch_strictness", op.start_byte, op.end_byte,
                              STRICT[text].encode()))
            elif text in ("&&", "||") and in_branch:
                found.append(("BRANCH_CONDITION", "branch_connective", op.start_byte, op.end_byte,
                              b"||" if text == "&&" else b"&&"))
            elif text in ARITH and not in_loop and not in_branch and _computation_context(node):
                found.append(("COMPUTATION", "arithmetic_operator", op.start_byte, op.end_byte,
                              ARITH[text].encode()))
        elif node.type == "for_statement":
            initializer = node.child_by_field_name("initializer")
            if initializer is not None and initializer.type == "assignment_expression":
                value = initializer.child_by_field_name("right")
                if value is not None and value.type == "number_literal" and value.text.isdigit():
                    found.append(("LOOP_BOUNDARY", "loop_start", value.start_byte, value.end_byte,
                                  str(int(value.text) + 1).encode()))
        elif node.type == "init_declarator" or node.type == "assignment_expression" and \
                node.parent is not None and node.parent.type == "expression_statement":
            value = node.child_by_field_name("value" if node.type == "init_declarator" else "right")
            statement = node.parent
            if value is not None and value.type == "number_literal" and value.text.isdigit() \
                    and not _inside_loop_body(statement) and not _in_field(node, LOOPS, ("initializer",)):
                new = b"1" if value.text == b"0" else b"0" if value.text == b"1" else \
                    str(int(value.text) + 1).encode()
                found.append(("INITIALIZATION", "constant_initializer", value.start_byte,
                              value.end_byte, new))
        elif node.type == "cast_expression":
            value = node.child_by_field_name("value")
            if value is not None and b"float" in node.text[:node.text.find(b")") + 1] or \
                    b"double" in node.text[:node.text.find(b")") + 1]:
                found.append(("NUMERIC_TYPE", "remove_cast", node.start_byte, node.end_byte,
                              value.text if value is not None else b""))
        elif node.type == "number_literal" and re.fullmatch(rb"\d+\.0*", node.text) and \
                node.parent is not None and node.parent.type == "binary_expression":
            found.append(("NUMERIC_TYPE", "float_literal_to_int", node.start_byte, node.end_byte,
                          node.text.split(b".")[0] or b"0"))
        elif node.type == "call_expression" and _call_name(node) in OUTPUT_FUNCS:
            arguments = node.child_by_field_name("arguments")
            literal = next((a for a in arguments.named_children if a.type == "string_literal"), None) \
                if arguments is not None else None
            if literal is not None:
                found.extend(_literal_sites(literal))
        elif node.type == "expression_statement" and node.parent is not None and \
                node.parent.type == "compound_statement":
            found.extend(_statement_sites(node, data))
    return found


def _computation_context(node):
    current = node
    while current.parent is not None:
        parent = current.parent
        if parent.type in ("assignment_expression", "return_statement", "init_declarator"):
            return True
        if parent.type == "argument_list":
            call = parent.parent
            return call is not None and _call_name(call) in OUTPUT_FUNCS
        if parent.type in ("expression_statement", "compound_statement"):
            return False
        current = parent
    return False


def _literal_sites(literal):
    text = literal.text
    start = literal.start_byte
    result = []
    for match in SPEC.finditer(text.decode("utf-8", errors="replace")):
        spec = match.group(0)
        precision = re.fullmatch(r"%([-+ #0]*\d*)\.(\d+)([lL]?[fFeEgG])", spec)
        if precision:
            digits = int(precision.group(2))
            new = f"%{precision.group(1)}.{digits + 1 if digits < 3 else digits - 1}{precision.group(3)}"
            offset = len(text.decode("utf-8", errors="replace")[:match.start()].encode())
            result.append(("OUTPUT_FORMAT", "precision", start + offset,
                           start + offset + len(spec.encode()), new.encode()))
    if text.endswith(b'\\n"'):
        result.append(("OUTPUT_TEXT", "drop_newline", start + len(text) - 3, start + len(text) - 1, b""))
    words = [m for m in re.finditer(rb"[A-Za-z]{3,}", text) if not _inside_spec(text, m.start())]
    if words:
        word = words[0]
        first = word.group(0)[:1]
        result.append(("OUTPUT_TEXT", "letter_case", start + word.start(), start + word.start() + 1,
                       first.swapcase()))
    return result


def _inside_spec(text, position):
    return position > 0 and text[position - 1:position] in (b"%", b"\\")


def _statement_sites(statement, data):
    result = []
    body = statement.parent
    owner = body.parent
    line_start = data.rfind(b"\n", 0, statement.start_byte) + 1
    indent = data[line_start:statement.start_byte]
    line_end = data.find(b"\n", statement.end_byte)
    line_end = len(data) if line_end < 0 else line_end + 1
    if owner is not None and (owner.type in LOOPS or owner.type == "if_statement") and \
            data[line_start:statement.start_byte].strip() == b"" and \
            data[statement.end_byte:line_end].strip() == b"":
        if not any(c.type == "call_expression" and _call_name(c) in OUTPUT_FUNCS
                   for c in _walk(statement)):
            result.append(("MISSING_STATEMENT", "delete_statement", line_start, line_end, b""))
        if owner.type in LOOPS:
            result.append(("EXTRA_STATEMENT", "duplicate_statement", line_start, line_end,
                           data[line_start:line_end] * 2))
    sibling = statement.next_named_sibling
    if sibling is not None and sibling.type in LOOPS and statement.child_count and \
            statement.named_children[0].type == "assignment_expression" and \
            data[line_start:statement.start_byte].strip() == b"":
        loop_body = sibling.child_by_field_name("body")
        if loop_body is not None and loop_body.type == "compound_statement":
            insert_at = loop_body.start_byte + 1
            moved = b"\n" + indent + b"    " + statement.text
            result.append(("STATEMENT_PLACEMENT", "move_into_loop", line_start, line_end, b"",
                           insert_at, moved))
    previous = statement.prev_named_sibling
    if previous is not None and previous.type in LOOPS and any(
            c.type == "call_expression" and _call_name(c) in OUTPUT_FUNCS for c in _walk(statement)):
        loop_body = previous.child_by_field_name("body")
        if loop_body is not None and loop_body.type == "compound_statement":
            insert_at = loop_body.end_byte - 1
            moved = indent + b"    " + statement.text + b"\n" + indent
            result.append(("STATEMENT_PLACEMENT", "move_output_into_loop", line_start, line_end, b"",
                           insert_at, moved))
    return result


def _walk(node):
    stack = [node]
    while stack:
        current = stack.pop()
        yield current
        stack.extend(current.children)


def apply_site(source, site):
    data = source.encode("utf-8")
    _, _, start, end, replacement, *move = site
    if move:
        insert_at, moved = move
        # Apply the later edit first so earlier byte offsets stay valid.
        if insert_at >= end:
            data = _edit(data, insert_at, insert_at, moved)
            data = _edit(data, start, end, replacement)
        else:
            data = _edit(data, start, end, replacement)
            data = _edit(data, insert_at, insert_at, moved)
    else:
        data = _edit(data, start, end, replacement)
    return data.decode("utf-8")


def one_mutant_per_category(source, rng: random.Random):
    """At most one randomly chosen site per category, in a fixed category order."""
    by_category = {}
    for site in sites(source):
        by_category.setdefault(site[0], []).append(site)
    chosen = []
    for category in sorted(by_category):
        site = rng.choice(by_category[category])
        mutated = apply_site(source, site)
        if mutated != source:
            chosen.append((category, site[1], mutated))
    return chosen

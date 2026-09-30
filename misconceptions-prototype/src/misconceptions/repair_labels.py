"""Repair-grounded mechanism labels: verified minimal student repairs, classified by AST.

A label describes the *program-level* change that the same student later made and that
the isolated runner verified to be sufficient. It is evaluation data only: the repair,
the later submission and the label never enter clustering features. A label is not
evidence of what the student believed.
"""

import re
from collections import defaultdict
from difflib import SequenceMatcher

import tree_sitter_c
from tree_sitter import Language, Parser

CATEGORIES = (
    "LOOP_BOUNDARY", "BRANCH_CONDITION", "INITIALIZATION", "COMPUTATION", "NUMERIC_TYPE",
    "OUTPUT_FORMAT", "OUTPUT_TEXT", "INPUT", "STATEMENT_PLACEMENT", "MISSING_STATEMENT",
    "EXTRA_STATEMENT", "CONTROL_FLOW",
)
OUTPUT_FUNCS = {"printf", "puts", "putchar", "fprintf", "fputs", "putc", "fputc"}
INPUT_FUNCS = {"scanf", "getchar", "fgets", "gets", "fscanf", "getc", "fgetc", "sscanf"}
MATH_FUNCS = {"floor", "ceil", "round", "abs", "fabs", "sqrt", "pow", "trunc", "lround", "rint"}
LOOPS = {"for_statement", "while_statement", "do_statement"}
STATEMENTS = {"expression_statement", "if_statement", "for_statement", "while_statement",
              "do_statement", "return_statement", "break_statement", "continue_statement",
              "compound_statement", "switch_statement", "declaration", "goto_statement",
              "labeled_statement", "case_statement"}
TYPE_NODES = {"primitive_type", "sized_type_specifier", "type_descriptor"}
SPEC = re.compile(r"%[-+ #0]*(\d+|\*)?(\.(\d+|\*))?(hh|h|ll|l|L|j|z|t)?[diouxXeEfFgGaAcspn%]")
_PARSER = Parser(Language(tree_sitter_c.language()))


def pair_repairs(rows, reviews, outcomes):
    """Pair each failing run with the same student's next passing run (same problem, year).

    `outcomes[sid]` is the replayed outcome dict or None. Attempt numbers `sub_NNN` are
    taken as submission order within one student, problem and year.
    """
    groups = defaultdict(list)
    for row in rows:
        review = reviews[row.submission_id]
        groups[(row.student_id, review["year"])].append((review["attempt"], row))
    pairs = []
    for key in sorted(groups):
        attempts = sorted(groups[key], key=lambda item: item[0])
        for index, (_, row) in enumerate(attempts):
            state = outcomes.get(row.submission_id)
            if not state or all(value == "pass" for value in state.values()):
                continue
            for _, later in attempts[index + 1:]:
                later_state = outcomes.get(later.submission_id)
                if later_state and all(value == "pass" for value in later_state.values()):
                    pairs.append((row, later))
                    break
    return pairs


def line_hunks(old_source, new_source):
    old = old_source.splitlines(keepends=True)
    new = new_source.splitlines(keepends=True)
    # Leading/trailing whitespace carries no meaning in C; spaces inside a line are kept
    # because they may sit inside a string literal.
    matcher = SequenceMatcher(None, [line.strip() for line in old],
                              [line.strip() for line in new], autojunk=False)
    return old, new, matcher.get_opcodes()


def apply_hunks(old, new, opcodes, selected):
    parts = []
    for index, (tag, i1, i2, j1, j2) in enumerate(opcodes):
        parts.extend(new[j1:j2] if tag != "equal" and index in selected else old[i1:i2])
    return "".join(parts)


def ddmin(changes, passes, budget):
    """1-minimal subset of `changes` for which `passes(subset_tuple_list)` holds.

    `passes` receives a list of candidate subsets and returns their booleans, so the
    caller may evaluate one level in parallel. Returns (subset, probes, minimal_flag).
    """
    current, n, probes = list(changes), 2, 0
    if len(current) == 1:
        return current, probes, True
    while len(current) >= 2:
        size = len(current)
        chunks = [current[i * size // n:(i + 1) * size // n] for i in range(n)]
        chunks = [chunk for chunk in chunks if chunk]
        complements = [[c for c in current if c not in chunk] for chunk in chunks]
        candidates = chunks + (complements if n > 2 else [])
        if probes + len(candidates) > budget:
            return current, probes, False
        results = passes(candidates)
        probes += len(candidates)
        passing = [candidate for candidate, ok in zip(candidates, results) if ok and candidate]
        if passing and passing[0] in chunks:
            current, n = passing[0], 2
        elif passing:
            current, n = passing[0], max(n - 1, 2)
        elif n < size:
            n = min(2 * n, size)
        else:
            break
    return current, probes, True


def _tokens(source):
    """Leaf-level tokens; each string/char literal is kept as one token."""
    data = source.encode("utf-8")
    root = _PARSER.parse(data).root_node
    tokens, stack = [], [root]
    while stack:
        node = stack.pop()
        if node.type == "comment":
            continue
        if node.child_count == 0 or node.type in ("string_literal", "char_literal"):
            if node.end_byte > node.start_byte:
                tokens.append(node)
            continue
        stack.extend(reversed(node.children))
    return root, tokens


def _ancestors(node):
    while node is not None:
        yield node
        node = node.parent


def _field_of(child, parent):
    for name in ("condition", "initializer", "update", "value", "type", "left", "right",
                 "arguments", "function", "body", "consequence", "alternative"):
        field = parent.child_by_field_name(name)
        if field is not None and field.start_byte <= child.start_byte and child.end_byte <= field.end_byte:
            return name
    return None


def _call_name(node):
    function = node.child_by_field_name("function")
    return function.text.decode("utf-8", errors="replace") if function is not None else ""


def _inside_loop_body(node):
    for ancestor in _ancestors(node.parent):
        if ancestor.type in LOOPS and _field_of(node, ancestor) == "body":
            return True
    return False


def token_context(token):
    """Innermost role-defining ancestor of a changed token (label-side analysis only).

    Expression nodes (binary, unary, parenthesized) are transparent: `i < n` inside a
    `for` condition is a loop-header change, not a generic computation change.
    """
    if token.type in ("break", "continue", "return", "goto"):
        return "control_flow"
    if token.type == "else":
        return "branch_condition"  # Adding or removing an else changes branch structure.
    if token.type in (";", ","):
        return "separator"
    for ancestor in _ancestors(token):
        if ancestor.type == "call_expression":
            name = _call_name(ancestor)
            if name in OUTPUT_FUNCS:
                return "output_literal" if token.type in ("string_literal", "char_literal")                     else "output_argument"
            if name in INPUT_FUNCS:
                return "input"
            if name in MATH_FUNCS:
                return "numeric_type"
        if ancestor.type in TYPE_NODES or ancestor.type == "cast_expression" and                 token.parent == ancestor and token.type in ("(", ")"):
            return "numeric_type"
        parent = ancestor.parent
        if parent is None:
            break
        field = _field_of(ancestor, parent)
        if parent.type == "cast_expression" and field == "type":
            return "numeric_type"
        if parent.type in LOOPS and field in ("condition", "initializer", "update"):
            return "loop_header"
        if parent.type in ("if_statement", "switch_statement", "conditional_expression")                 and field == "condition":
            return "branch_condition"
        if parent.type == "init_declarator" and field == "value":
            return "initializer"
        if parent.type == "assignment_expression" and field == "right":
            statement = next((a for a in _ancestors(parent) if a.type in STATEMENTS), None)
            if _in_loop_header(parent):
                return "loop_header"
            if statement is not None and not _inside_loop_body(statement) and _is_constant(ancestor):
                return "initializer"
            return "computation"
        if parent.type in ("assignment_expression", "update_expression", "return_statement",
                           "expression_statement", "subscript_expression"):
            return "computation"
    if token.type in ("{", "}"):
        return "structure"
    return "other"


def _in_loop_header(node):
    for ancestor in _ancestors(node):
        parent = ancestor.parent
        if parent is not None and parent.type in LOOPS:
            return _field_of(ancestor, parent) in ("condition", "initializer", "update")
    return False


def _is_constant(node):
    return node.type in ("number_literal", "char_literal") or (
        node.type == "unary_expression" and node.named_child_count == 1
        and node.named_children[0].type == "number_literal")


def _complete_statements(tokens, root):
    """Statement nodes fully covered by `tokens` (used for pure insertions/deletions)."""
    if not tokens:
        return []
    start, end = min(t.start_byte for t in tokens), max(t.end_byte for t in tokens)
    found, stack = [], [root]
    while stack:
        node = stack.pop()
        if node.end_byte <= start or node.start_byte >= end:
            continue
        if node.type in STATEMENTS and start <= node.start_byte and node.end_byte <= end:
            found.append(node)
            continue
        stack.extend(node.children)
    return found


def _output_only(statement):
    calls = [n for n in _walk(statement) if n.type == "call_expression"]
    return bool(calls) and all(_call_name(call) in OUTPUT_FUNCS for call in calls) and all(
        argument.type in ("string_literal", "char_literal")
        for call in calls for argument in call.child_by_field_name("arguments").named_children)


def _walk(node):
    stack = [node]
    while stack:
        current = stack.pop()
        yield current
        stack.extend(current.children)


def _format_kind(old_literal, new_literal):
    old_specs = [m.group(0) for m in SPEC.finditer(old_literal)]
    new_specs = [m.group(0) for m in SPEC.finditer(new_literal)]
    return "OUTPUT_FORMAT" if old_specs != new_specs else "OUTPUT_TEXT"


CONTEXT_CATEGORY = {"loop_header": "LOOP_BOUNDARY", "branch_condition": "BRANCH_CONDITION",
                    "initializer": "INITIALIZATION", "computation": "COMPUTATION",
                    "numeric_type": "NUMERIC_TYPE", "input": "INPUT",
                    "output_argument": "COMPUTATION", "control_flow": "CONTROL_FLOW"}


def _statement_change(tokens, root, tag):
    """Category for tokens that were wholly inserted or deleted, or None if not whole statements."""
    statements = [s for s in _complete_statements(tokens, root) if s.type != "declaration"]
    covered = all(t.type in ("{", "}", ";") or any(
        s.start_byte <= t.start_byte and t.end_byte <= s.end_byte for s in statements) for t in tokens)
    if statements and covered:
        if all(_output_only(s) for s in statements):
            return "OUTPUT_TEXT", f"{tag}:output_literal_statement"
        if len(statements) == 1 and statements[0].type in (
                "break_statement", "continue_statement", "return_statement"):
            return "CONTROL_FLOW", f"{tag}:{statements[0].type}"
        kind = "MISSING_STATEMENT" if tag == "insert" else "EXTRA_STATEMENT"
        return kind, f"{tag}:" + "+".join(sorted({s.type for s in statements}))
    if tokens and all(t.type in ("{", "}") for t in tokens):
        return "STATEMENT_PLACEMENT", f"{tag}:brace"
    if tokens and all(_inside_declaration(t) or t.type == ";" for t in tokens):
        return "", "declaration_scaffolding"  # A helper declaration serves another change.
    return None


def _slides(texts, start, end):
    """Equivalent positions of a pure insertion/deletion run inside `texts`."""
    positions = [(start, end)]
    a, b = start, end
    while b < len(texts) and texts[a] == texts[b]:
        a, b = a + 1, b + 1
        positions.append((a, b))
    a, b = start, end
    while a > 0 and texts[a - 1] == texts[b - 1]:
        a, b = a - 1, b - 1
        positions.append((a, b))
    return positions


def _context_changes(changed_old, changed_new):
    found = []
    contexts = [token_context(t) for t in changed_old] + [token_context(t) for t in changed_new]
    if any(o.type == n.type == "number_literal" and _is_float(o.text) != _is_float(n.text)
           for o, n in zip(changed_old, changed_new)):
        contexts = ["numeric_type"]
    literal_pairs = [(o, n) for o, n in zip(changed_old, changed_new)
                     if o.type == n.type == "string_literal"]
    text = (b" ".join(t.text for t in changed_old).decode(errors="replace")[:40] + "->"
            + b" ".join(t.text for t in changed_new).decode(errors="replace")[:40])
    for context in contexts:
        if context == "output_literal":
            if literal_pairs:
                for o, n in literal_pairs:
                    old_text, new_text = o.text.decode(errors="replace"), n.text.decode(errors="replace")
                    kind = _format_kind(old_text, new_text)
                    found.append((kind, f"{kind.lower()}:{old_text[:30]}->{new_text[:30]}"))
            else:
                found.append(("OUTPUT_TEXT", "output_literal"))
        elif context in CONTEXT_CATEGORY:
            found.append((CONTEXT_CATEGORY[context], f"{context}:{text}"))
        elif context == "structure":
            found.append(("STATEMENT_PLACEMENT", "structure"))
        elif context != "separator":
            found.append(("OTHER", f"other:{text}"))
    return found


def classify_repair(old_source, new_source):
    """Categories of the change old -> new (a verified minimal repair).

    Works hunk by hunk on the same line hunks that delta debugging verified. Identical
    lines deleted in one place and inserted in another are a placement change.
    """
    old_root, old_tokens = _tokens(old_source)
    new_root, new_tokens = _tokens(new_source)
    old_lines, new_lines, opcodes = line_hunks(old_source, new_source)
    hunks = [op for op in opcodes if op[0] != "equal"]
    deleted = {}
    inserted = {}
    for _, i1, i2, j1, j2 in hunks:
        for i in range(i1, i2):
            deleted.setdefault(old_lines[i].strip(), []).append(i)
        for j in range(j1, j2):
            inserted.setdefault(new_lines[j].strip(), []).append(j)
    moved_old, moved_new, found = set(), set(), []
    for text, rows in deleted.items():
        if text and text in inserted:
            pairs = min(len(rows), len(inserted[text]))
            moved_old.update(rows[:pairs])
            moved_new.update(inserted[text][:pairs])
            found.append(("STATEMENT_PLACEMENT", "moved:" + text[:60]))
    for _, i1, i2, j1, j2 in hunks:
        old_rows = {i for i in range(i1, i2) if i not in moved_old}
        new_rows = {j for j in range(j1, j2) if j not in moved_new}
        old_part = [t for t in old_tokens if t.start_point[0] in old_rows]
        new_part = [t for t in new_tokens if t.start_point[0] in new_rows]
        if not old_part and not new_part:
            continue
        if not new_part or not old_part:
            tag = "delete" if not new_part else "insert"
            side, root = (old_part, old_root) if tag == "delete" else (new_part, new_root)
            change = _statement_change(side, root, tag)
            if change is not None:
                found.append(change)
            else:
                found.extend(_context_changes(old_part, new_part))
            continue
        old_text = [t.text for t in old_part]
        new_text = [t.text for t in new_part]
        for tag, a1, a2, b1, b2 in SequenceMatcher(None, old_text, new_text,
                                                   autojunk=False).get_opcodes():
            if tag == "equal":
                continue
            if tag in ("insert", "delete"):
                texts, part, root = (new_text, new_part, new_root) if tag == "insert" else                     (old_text, old_part, old_root)
                start, end = (b1, b2) if tag == "insert" else (a1, a2)
                change = None
                for s1, s2 in _slides(texts, start, end):
                    change = _statement_change(part[s1:s2], root, tag)
                    if change is not None:
                        break
                if change is not None:
                    found.append(change)
                    continue
            found.extend(_context_changes(old_part[a1:a2], new_part[b1:b2]))
    categories = {category for category, _ in found if category}
    if not categories and hunks and not all(detail == "declaration_scaffolding" for _, detail in found):
        categories.add("OTHER")
    details = list(dict.fromkeys(detail for _, detail in found))
    return {"categories": sorted(categories), "details": details,
            "primary": next(iter(categories)) if len(categories) == 1 else
            ("MULTI" if categories else "NO_CHANGE"),
            "hunks": len(hunks)}


def _is_float(text):
    return bool(re.fullmatch(rb"(\d+\.\d*|\.\d+)([eE][-+]?\d+)?[fFlL]?|\d+[eE][-+]?\d+[fFlL]?", text))


def _inside_declaration(token):
    for ancestor in _ancestors(token):
        if ancestor.type == "declaration":
            return ancestor.parent is not None and ancestor.parent.type in (
                "compound_statement", "translation_unit")
        if ancestor.type in STATEMENTS:
            return False
    return False

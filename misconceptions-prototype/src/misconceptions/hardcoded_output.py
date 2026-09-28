"""Conservative straight-line C output analysis, not a general data-flow engine."""

import re

import tree_sitter_c
from tree_sitter import Language, Parser

LABEL = "In hằng số / Chưa tính toán theo đầu vào"


def hardcoded_output(source, outcomes):
    """Return print-site evidence only when >=2 observed failures corroborate the AST.

    False means not established by this bounded rule, not proven input-dependent.
    Branches/loops, macros, helpers, aliases and unsupported constructs abstain.
    """
    if sum(value == "fail" for value in outcomes.values()) < 2:
        return []
    root = Parser(Language(tree_sitter_c.language())).parse(source.encode()).root_node
    if root.has_error or any(n.type.startswith("preproc_") and n.type != "preproc_include"
                             for n in root.named_children):
        return []
    functions = [n for n in root.named_children if n.type == "function_definition"]
    if len(functions) != 1:
        return []
    declarator = functions[0].child_by_field_name("declarator")
    name = declarator.child_by_field_name("declarator")
    if name is None or name.text != b"main":
        return []
    constants, printed = {}, []

    def safe_expression(node):
        return node is None or (node.type in {
            "identifier", "number_literal", "char_literal", "string_literal", "escape_sequence",
            "string_content", "parenthesized_expression", "binary_expression", "unary_expression",
        } and all(safe_expression(n) for n in node.named_children if n.type != "comment"))

    def constant(node):
        if node is None:
            return False
        if node.type in {"number_literal", "char_literal", "string_literal"}:
            return True
        if node.type == "identifier":
            return constants.get(node.text, False)
        if node.type in {"parenthesized_expression", "binary_expression", "unary_expression"}:
            return all(constant(n) for n in node.named_children if n.type != "comment")
        return False

    for statement in functions[0].child_by_field_name("body").named_children:
        if statement.type == "comment":
            continue
        if statement.type == "return_statement":
            if not all(safe_expression(n) for n in statement.named_children):
                return []
            break
        if statement.type == "declaration":
            for declaration in statement.children_by_field_name("declarator"):
                target = declaration.child_by_field_name("declarator") if declaration.type == "init_declarator" else declaration
                if target.type != "identifier":
                    return []
                value = declaration.child_by_field_name("value")
                if not safe_expression(value):
                    return []
                constants[target.text] = constant(value)
            continue
        if statement.type != "expression_statement" or len(statement.named_children) != 1:
            return []
        expression = statement.named_children[0]
        if expression.type == "assignment_expression":
            left = expression.child_by_field_name("left")
            if left.type != "identifier" or expression.child_by_field_name("operator").text != b"=":
                return []
            value = expression.child_by_field_name("right")
            if not safe_expression(value):
                return []
            constants[left.text] = constant(value)
            continue
        if expression.type != "call_expression":
            return []
        function = expression.child_by_field_name("function").text
        args = [n for n in expression.child_by_field_name("arguments").named_children if n.type != "comment"]
        if function == b"scanf":
            if not args or args[0].type != "string_literal":
                return []
            for arg in args[1:]:
                if arg.type != "pointer_expression" or arg.child_by_field_name("operator").text != b"&":
                    return []
                target = arg.child_by_field_name("argument")
                if target is None or target.type != "identifier":
                    return []
                constants[target.text] = False
            continue
        if function not in {b"printf", b"puts"} or not args or args[0].type != "string_literal":
            return []
        if not all(constant(arg) for arg in args):
            return []
        if function == b"printf":
            fmt = args[0].text.decode()[1:-1]
            conversions = re.findall(r"%(?:%|[-+ #0]*\d*(?:\.\d+)?[hlL]*[diuoxXfFeEgGaAcsp])", fmt)
            if "%" in re.sub(r"%(?:%|[-+ #0]*\d*(?:\.\d+)?[hlL]*[diuoxXfFeEgGaAcsp])", "", fmt):
                return []
            if sum(c != "%%" for c in conversions) != len(args) - 1:
                return []
        elif len(args) != 1:
            return []
        printed.append({"line_start": expression.start_point.row + 1,
                        "line_end": expression.end_point.row + 1, "code": expression.text.decode()})
    return printed

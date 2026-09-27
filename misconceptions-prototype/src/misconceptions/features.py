"""Inspectable categorical OAV and block-balanced distances."""

import ast
from collections.abc import Iterator
from dataclasses import dataclass

import numpy as np
import tree_sitter_c
from tree_sitter import Language, Node, Parser

from .domain import Submission
from .output_features import OUTPUT_CATEGORIES, output_oav

AST_NAMES = ("for", "while", "range", "inclusive_comparison", "subscript", "return", "augassign")
C_AST_NAMES = (
    "for",
    "while",
    "do",
    "if",
    "inclusive_comparison",
    "strict_comparison",
    "subscript",
    "zero_index",
    "one_index",
    "pointer_declarator",
    "pointer_parameter",
    "array_parameter",
    "address_of",
    "dereference",
    "update",
    "return",
)
STATES = ("pass", "fail", "runtime_error", "timeout", "not_run", "__unknown__")


def _c_nodes(root: Node) -> Iterator[Node]:
    """Walk named syntax nodes without recursion; comments/strings are never code."""
    stack = [root]
    while stack:
        node = stack.pop()
        yield node
        # Do not mistake a preprocessor condition for a runtime comparison.
        condition = (
            node.child_by_field_name("condition") if node.type.startswith("preproc_") else None
        )
        stack.extend(child for child in reversed(node.named_children) if child != condition)


def _extract_c(source: str) -> dict[str, str]:
    """Syntactic presence only: no preprocessing, execution, or misconception inference."""
    values = {f"ast:c_{name}": "__unknown__" for name in C_AST_NAMES}
    root = Parser(Language(tree_sitter_c.language())).parse(source.encode("utf-8")).root_node
    if root.has_error:
        return values | {"ast:parse": "error"}
    nodes = list(_c_nodes(root))
    types = {node.type for node in nodes}
    flags = {
        "for": "for_statement" in types,
        "while": "while_statement" in types,
        "do": "do_statement" in types,
        "if": "if_statement" in types,
        "subscript": "subscript_expression" in types,
        "pointer_declarator": "pointer_declarator" in types,
        "update": "update_expression" in types,
        "return": "return_statement" in types,
    }
    for name, operators, kind in (
        ("inclusive_comparison", {"<=", ">="}, "binary_expression"),
        ("strict_comparison", {"<", ">"}, "binary_expression"),
        ("address_of", {"&"}, "pointer_expression"),
        ("dereference", {"*"}, "pointer_expression"),
    ):
        flags[name] = any(
            node.type == kind
            and (operator := node.child_by_field_name("operator")) is not None
            and operator.type in operators
            for node in nodes
        )
    for name, literal in (("zero_index", b"0"), ("one_index", b"1")):
        flags[name] = any(
            node.type == "subscript_expression"
            and (index := node.child_by_field_name("index")) is not None
            and index.type == "number_literal"
            and index.text == literal
            for node in nodes
        )
    for name, kind in (
        ("pointer_parameter", "pointer_declarator"),
        ("array_parameter", "array_declarator"),
    ):
        flags[name] = any(
            node.type == "parameter_declaration"
            and (declarator := node.child_by_field_name("declarator")) is not None
            and any(part.type == kind for part in _c_nodes(declarator))
            for node in nodes
        )
    return {f"ast:c_{name}": str(int(flags[name])) for name in C_AST_NAMES} | {"ast:parse": "ok"}


def extract_oav(row: Submission) -> dict[str, str]:
    values = {f"test:{name}": value for name, value in row.outcomes.items()}
    if row.language.lower() == "c":
        return values | _extract_c(row.source_code)
    values.update({f"ast:{name}": "__unknown__" for name in AST_NAMES})
    if row.language.lower() not in ("python", "python3", "py"):
        values["ast:parse"] = "unsupported"
        return values
    try:
        nodes = list(ast.walk(ast.parse(row.source_code)))
    except (SyntaxError, ValueError, RecursionError):
        values["ast:parse"] = "error"
        return values
    values["ast:parse"] = "ok"
    predicates = {
        "for": lambda n: isinstance(n, (ast.For, ast.AsyncFor)),
        "while": lambda n: isinstance(n, ast.While),
        "range": lambda n: (
            isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "range"
        ),
        "inclusive_comparison": lambda n: isinstance(n, (ast.LtE, ast.GtE)),
        "subscript": lambda n: isinstance(n, ast.Subscript),
        "return": lambda n: isinstance(n, ast.Return),
        "augassign": lambda n: isinstance(n, ast.AugAssign),
    }
    values.update(
        {
            f"ast:{name}": str(int(any(predicate(n) for n in nodes)))
            for name, predicate in predicates.items()
        }
    )
    return values


def route_submission(row: Submission, expected_tests: list[str]) -> str:
    if extract_oav(row)["ast:parse"] == "error":
        return "parse_error"
    states = [row.outcomes.get(name, "not_run") for name in expected_tests]
    if any(state == "not_run" for state in states):
        return "incomplete"
    if any(state in ("runtime_error", "timeout") for state in states):
        return "execution_error"
    return "eligible" if "fail" in states else "no_failure"


@dataclass
class FeatureSpace:
    names: list[str]
    weights: np.ndarray
    categories: list[tuple[str, ...]]
    include_stdout: bool = False

    @classmethod
    def fit(
        cls,
        train: list[Submission],
        test_ids: list[str],
        test_weight: float = 0.8,
        feature_mode: str = "combined",
        logs: dict | None = None,
    ) -> "FeatureSpace":
        if not train or not test_ids or len(test_ids) != len(set(test_ids)):
            raise ValueError("Nonempty training rows and unique test IDs are required")
        include_stdout = feature_mode.endswith("_stdout")
        base_mode = feature_mode.removesuffix("_stdout")
        if feature_mode not in (
            "outcomes", "structural", "combined", "outcomes_stdout", "combined_stdout"
        ) or not 0 < test_weight <= 1:
            raise ValueError("Invalid feature mode or test weight")
        feature_mode = base_mode
        names = (
            [] if feature_mode == "structural" else [f"test:{name}" for name in sorted(test_ids)]
        )
        categories = [STATES] * len(names)
        # Drop constant AST indicators using training evidence only.
        observed = [extract_oav(row) for row in train]
        ast_names = (
            [f"ast:{name}" for name in AST_NAMES] + [f"ast:c_{name}" for name in C_AST_NAMES]
            if feature_mode == "structural" or (feature_mode == "combined" and test_weight < 1)
            else []
        )
        ast_names = [
            name for name in ast_names if len({o.get(name, "__unknown__") for o in observed}) > 1
        ]
        outcome_mass = 0.0 if feature_mode == "structural" else (test_weight if ast_names else 1.0)
        weights = [outcome_mass / len(names)] * len(names) if names else []
        if ast_names:
            weights += [(1 - outcome_mass) / len(ast_names)] * len(ast_names)
            categories += [("0", "1", "__unknown__")] * len(ast_names)
        names += ast_names
        if include_stdout:
            observed_outputs = [output_oav(row, logs or {}) for row in train]
            output_names = [
                f"stdout:{tid}:{descriptor}"
                for tid in sorted(test_ids) for descriptor in OUTPUT_CATEGORIES
                if len({o.get(f"stdout:{tid}:{descriptor}", "__unknown__")
                        for o in observed_outputs}) > 1
            ]
            if output_names:
                weights = [weight * 0.6 for weight in weights]
                weights += [0.4 / len(output_names)] * len(output_names)
                categories += [OUTPUT_CATEGORIES[name.rsplit(":", 1)[1]] for name in output_names]
                names += output_names
        return cls(names, np.asarray(weights), categories, include_stdout)

    def transform(self, rows: list[Submission], logs: dict | None = None) -> np.ndarray:
        observations = [
            extract_oav(row) | (output_oav(row, logs or {}) if self.include_stdout else {})
            for row in rows
        ]
        return np.asarray(
            [[values.get(name, "__unknown__") for name in self.names] for values in observations],
            dtype=object,
        ).reshape(len(rows), len(self.names))

    def onehot(self, values: np.ndarray, weighted: bool = True) -> np.ndarray:
        blocks = []
        for index, categories in enumerate(self.categories):
            column = values[:, index]
            column = np.where(np.isin(column, categories), column, "__unknown__")
            block = (column[:, None] == np.asarray(categories)[None, :]).astype(float)
            blocks.append(block * np.sqrt(self.weights[index] / 2) if weighted else block)
        return np.concatenate(blocks, axis=1)

    @property
    def onehot_names(self) -> list[str]:
        return [
            f"{name}={value}"
            for name, categories in zip(self.names, self.categories)
            for value in categories
        ]


def weighted_hamming(left: np.ndarray, right: np.ndarray, weights: np.ndarray) -> np.ndarray:
    if left.ndim != 2 or right.ndim != 2 or left.shape[1] != right.shape[1]:
        raise ValueError("Categorical matrices must have matching feature dimensions")
    if (
        len(weights) != left.shape[1]
        or np.any(weights < 0)
        or not np.isfinite(weights).all()
        or weights.sum() <= 0
    ):
        raise ValueError("Weights must be finite, nonnegative and have positive sum")
    # Accumulate by feature to avoid an n*n*d intermediate allocation.
    result = np.zeros((len(left), len(right)), dtype=float)
    for j, weight in enumerate(weights / weights.sum()):
        result += weight * (left[:, j, None] != right[None, :, j])
    return result

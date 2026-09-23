"""C syntax evidence, exclusion of inert text, and train-only feature selection."""

from dataclasses import replace

import numpy as np

from misconceptions.domain import Submission
from misconceptions.features import FeatureSpace, extract_oav, route_submission, weighted_hamming


def c_row(source: str) -> Submission:
    return Submission("1", "s1", "p", "c", source, "v1", {"a": "fail", "b": "pass"}, "test")


def test_c_syntax_features():
    values = extract_oav(
        c_row("""
        #include <stdio.h>
        int f(int *p, int a[]) {
            for (int i = 0; i <= 3; i++) { a[i] = *p; }
            while (a[0] < a[1]) { ++a[0]; }
            do { p = &a[0]; } while (0);
            if (*p > 0) return a[1];
            return 0;
        }
    """)
    )
    assert values["ast:parse"] == "ok"
    assert all(value == "1" for key, value in values.items() if key.startswith("ast:c_"))


def test_comments_strings_and_macros_do_not_invent_code():
    values = extract_oav(
        c_row("""
        #define TEXT "for while *p &x a[0] <="
        #if VERSION >= 2
        int version;
        #endif
        /* int f(int *p) { while (a[0] <= a[1]) return *p; } */
        int main(void) { puts("for (;;) { *p = &x; }"); }
    """)
    )
    assert values["ast:parse"] == "ok"
    assert all(value == "0" for key, value in values.items() if key.startswith("ast:c_"))


def test_arithmetic_is_not_pointer_evidence():
    values = extract_oav(c_row("int f(int a, int b) { return (a * b) + (a & b); }"))
    for name in ("pointer_declarator", "pointer_parameter", "address_of", "dereference"):
        assert values[f"ast:c_{name}"] == "0"


def test_local_pointer_is_not_pointer_parameter():
    values = extract_oav(c_row("int f(int a) { int *p = &a; return *p; }"))
    assert values["ast:c_pointer_declarator"] == "1"
    assert values["ast:c_pointer_parameter"] == "0"


def test_parse_errors_are_unknown_and_routed():
    row = c_row("int main( { return ;")
    values = extract_oav(row)
    assert values["ast:parse"] == "error"
    assert values["ast:c_for"] == "__unknown__"
    assert route_submission(row, ["a", "b"]) == "parse_error"


def test_train_only_c_selection_and_distance_geometry():
    first = c_row("int f(int n) { return n; }")
    second = replace(
        c_row("int f(int n) { while(n > 0) --n; return n; }"), outcomes={"a": "fail", "b": "fail"}
    )
    space = FeatureSpace.fit([first, second], ["a", "b"])
    assert "ast:c_while" in space.names
    assert "ast:c_return" not in space.names
    assert "ast:parse" not in space.names
    values = space.transform([first, second])
    encoded = space.onehot(values)
    distance = weighted_hamming(values, values, space.weights)
    np.testing.assert_allclose(distance[0, 1], np.sum((encoded[0] - encoded[1]) ** 2))
    np.testing.assert_allclose(
        sum(w for n, w in zip(space.names, space.weights) if n.startswith("test:")), 0.8
    )
    held = c_row("int f(int *p) { return *p; }")
    assert space.transform([held]).shape[1] == len(space.names)
    assert "ast:c_pointer_parameter" not in space.names
    outcomes = FeatureSpace.fit([first, second], ["a", "b"], feature_mode="outcomes")
    assert outcomes.names == ["test:a", "test:b"]
    test_only_weight = FeatureSpace.fit([first, second], ["a", "b"], test_weight=1)
    assert test_only_weight.names == ["test:a", "test:b"]
    assert all(name.startswith("test:") for name in test_only_weight.onehot_names)

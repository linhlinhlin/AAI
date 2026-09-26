"""Fixed, label-free descriptors of logged output relative to the test oracle."""

from difflib import SequenceMatcher

MAX_SIMILARITY_CHARS = 4096
OUTPUT_CATEGORIES = {
    "relation": ("exact", "whitespace", "empty", "other_oracle", "different", "__unknown__"),
    "edit_band": ("zero", "small", "medium", "large", "not_computed_large_output", "__unknown__"),
}


def validate_output_logs(rows, test_ids, logs):
    """Check every eligible row; unknown outputs must not masquerade as evidence."""
    definitions = {}
    for row in rows:
        seen = set()
        for test in logs.get(row.submission_id, []):
            if not isinstance(test, dict) or any(
                not isinstance(test.get(key), str)
                for key in ("test_id", "input", "expected", "output")
            ):
                raise ValueError("stdout features require string test evidence")
            tid = test["test_id"]
            if tid in seen or tid not in test_ids:
                raise ValueError("stdout evidence has duplicate or unknown test IDs")
            seen.add(tid)
            definition = (test["input"], test["expected"])
            if tid in definitions and definitions[tid] != definition:
                raise ValueError("stdout evidence has inconsistent test definitions")
            definitions[tid] = definition
        required = {tid for tid, state in row.outcomes.items() if state == "fail"}
        if not required <= seen:
            raise ValueError(f"Incomplete stdout evidence for {row.submission_id}")


def output_oav(row, logs):
    tests = logs.get(row.submission_id, [])
    # These are task oracles, never outputs or vocabulary learned from other students.
    oracles = {test["expected"] for test in tests}
    values = {}
    for test in tests:
        expected, actual = test["expected"], test["output"]
        if actual == expected:
            relation = "exact"
        elif actual.split() == expected.split():
            relation = "whitespace"
        elif not actual:
            relation = "empty"
        elif actual in oracles:
            relation = "other_oracle"
        else:
            relation = "different"
        if max(len(expected), len(actual)) > MAX_SIMILARITY_CHARS:
            band = "not_computed_large_output"
        else:
            difference = 1 - SequenceMatcher(None, expected, actual, autojunk=False).ratio()
            band = (
                "zero" if difference == 0 else "small" if difference <= 0.1
                else "medium" if difference <= 0.4 else "large"
            )
        prefix = f"stdout:{test['test_id']}:"
        values[prefix + "relation"] = relation
        values[prefix + "edit_band"] = band
    return values

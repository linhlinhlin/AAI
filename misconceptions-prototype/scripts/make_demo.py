"""Generate explicitly synthetic integration fixtures, never execute supplied student code."""

import json
from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[1] / "data" / "demo"
    root.mkdir(parents=True, exist_ok=True)
    inputs = [0, 1, 2, 3, 5, 8]
    tests = {f"n_{n}": n for n in inputs}
    manifest = {
        "schema_version": 1,
        "dataset_name": "synthetic-sum-demo-NOT-student-data",
        "provenance": "Hand-authored synthetic fixtures; integration testing only.",
        "problem_id": "demo_sum_0_through_n",
        "language": "python",
        "suite_version": "sum-v1",
        "test_ids": list(tests),
        "test_inputs": tests,
        "specification": "For integer n >= 0, return sum of integers 0 through n inclusive.",
    }
    rows, oracle = [], []
    # These trusted formulas correspond to the hand-authored sources below.
    patterns = [
        ("exclude_upper", "sum(range({v}))", lambda n: sum(range(n))),
        ("square", "{v} * {v}", lambda n: n * n),
        (
            "odd_only",
            "sum(i for i in range({v}+1) if i % 2)",
            lambda n: sum(i for i in range(n + 1) if i % 2),
        ),
    ]
    for family, expression, formula in patterns:
        for index in range(16):
            variable = f"value_{index}"
            sid = f"demo_{family}_{index:02d}"
            rows.append(
                {
                    "submission_id": sid,
                    "student_id": f"synthetic_person_{family}_{index:02d}",
                    "problem_id": manifest["problem_id"],
                    "language": "python",
                    "source_code": f"def solve({variable}):\n    return {expression.format(v=variable)}\n",
                    "suite_version": manifest["suite_version"],
                    "outcomes": {
                        tid: "pass" if formula(n) == n * (n + 1) // 2 else "fail"
                        for tid, n in tests.items()
                    },
                    "provenance": "synthetic_hand_authored_v1",
                }
            )
            oracle.append({"submission_id": sid, "injected_pattern": family})
    # Deliberately exercise routing of partial runs, runtime errors, correct and invalid syntax.
    extras = [
        ("partial", "def solve(n):\n    return n\n", {t: "not_run" for t in tests}),
        ("runtime", "def solve(n):\n    return 1/0\n", {t: "runtime_error" for t in tests}),
        ("correct", "def solve(n):\n    return n*(n+1)//2\n", {t: "pass" for t in tests}),
        ("syntax", "def solve(n)\n    return n\n", {t: "not_run" for t in tests}),
    ]
    for name, source, outcomes in extras:
        rows.append(
            {
                **rows[0],
                "submission_id": f"demo_{name}",
                "student_id": f"synthetic_person_{name}",
                "source_code": source,
                "outcomes": outcomes,
            }
        )
    (root / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    (root / "submissions.jsonl").write_text(
        "".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8"
    )
    (root / "oracle_DO_NOT_USE_AS_FEATURES.jsonl").write_text(
        "".join(json.dumps(row) + "\n" for row in oracle), encoding="utf-8"
    )
    print(f"Wrote {len(rows)} synthetic fixtures to {root}")


if __name__ == "__main__":
    main()

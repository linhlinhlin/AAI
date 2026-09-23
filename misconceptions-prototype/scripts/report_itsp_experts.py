"""Render human-only cluster/type evidence; do not infer mechanisms or label outliers."""

import argparse
import hashlib
import json
from pathlib import Path

from misconceptions.expert_validation import score_annotation_sources


def render(result):
    def cell(value):
        return str(value).replace("|", "\\|").replace("\n", " ").replace("\r", " ")

    lines = [
        "# Human expert validation — cluster review",
        "",
        (
            f"Status: **{result['status']}**. Completed human reviews: "
            f"{result['n_completed_records']}; adjudications: {result['n_adjudicated']}."
        ),
        "",
        (
            "Scope: selected review samples only, not whole-cluster or whole-cohort estimates. "
            "Types are codebook categories, not confirmed mechanisms. Multiple observed types "
            "flag cases for human inspection; a single type does not establish a shared cause. "
            "Ties list all modal types; no automatic majority adjudication or outlier labels."
        ),
        "",
        (
            "No/Unclear/pending/untyped Yes are excluded from type purity. "
            "AI annotations never supply these metrics. No student-level generalization."
        ),
        "",
        (
            "| Problem | Arm | Cluster | Selected | Typed Yes | Coverage | Decisions | "
            "Type counts | Modal types | Multiple types |"
        ),
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for arm in result["purity_details"]:
        for cluster in arm["cluster_details"]:
            values = [
                arm["problem_id"],
                arm["arm"],
                cluster["cluster_id"],
                cluster["n_candidates"],
                cluster["n_typed_yes"],
                f"{cluster['typed_coverage']:.3f}",
                json.dumps(cluster["decision_counts"], ensure_ascii=False),
                json.dumps(cluster["type_counts"], ensure_ascii=False),
                ", ".join(cluster["modal_types"]) or "null",
                json.dumps(cluster["multiple_observed_types"]),
            ]
            lines.append("| " + " | ".join(cell(v) for v in values) + " |")
    lines.extend(["", "## Purity by problem and arm", ""])
    for arm in result["purity_details"]:
        lines.append(
            f"- {cell(arm['problem_id'])}/{arm['arm']}: "
            f"purity={json.dumps(arm['cluster_purity'])}; "
            f"numerator={arm['purity_numerator']}; typed denominator="
            f"{arm['n_typed_adjudicated_yes']}/{arm['n_review_candidates']} candidates."
        )
    lines.extend(
        [
            "",
            "## Agreement",
            "",
            "```json",
            json.dumps(result["agreement"], ensure_ascii=False, indent=2),
            "```",
            "",
            "## Trace selected members",
            "",
        ]
    )
    for arm in result["purity_details"]:
        for cluster in arm["cluster_details"]:
            lines.append(
                f"- {cell(arm['problem_id'])}/{arm['arm']}/{cluster['cluster_id']}: "
                + ", ".join(cell(sid) for sid in cluster["reviewed_sample_ids"])
            )
    return "\n".join(lines) + "\n"


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--annotations", type=Path, required=True)
    parser.add_argument(
        "--assignments", type=Path, default=root / "results/itsp/abc_review_assignments.json"
    )
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        raw = args.annotations.read_bytes()
        assignment_bytes = args.assignments.read_bytes()
        document = json.loads(raw)
        digest = hashlib.sha256(assignment_bytes).hexdigest()
        if document["assignments_sha256"] != digest:
            raise ValueError("Assignment hash mismatch")
        result = score_annotation_sources(document, json.loads(assignment_bytes))
        text = render(result) + (
            f"\nAnnotation SHA-256: `{hashlib.sha256(raw).hexdigest()}`. "
            f"Assignment SHA-256: `{digest}`.\n"
        )
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x", encoding="utf-8") as stream:
            stream.write(text)
    except (ValueError, KeyError, TypeError, OSError) as error:
        parser.error(str(error))
    print(f"Saved {args.output}; status={result['status']}")


if __name__ == "__main__":
    main()

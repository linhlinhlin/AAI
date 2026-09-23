"""Merge returned human round-one forms without inventing adjudication."""

from copy import deepcopy

from .expert_validation import validate_annotations


def merge_round_one(documents, assignments):
    """Require one real reviewer per file and a common approved codebook.

    Identity and blind-review attestations still require coordinator verification.
    Conflicts are queued, never resolved by majority vote or confidence.
    """
    if not documents:
        raise ValueError("At least one returned reviewer file is required")
    merged = deepcopy(documents[0])
    merged.pop("intake", None)
    for sample in merged["samples"]:
        sample["reviews"] = []
    by_id = {s["submission_id"]: s for s in merged["samples"]}
    reviewers = set()
    for document in documents:
        if not validate_annotations(document, assignments):
            raise ValueError("Round-one intake requires an approved common codebook")
        if document["codebook"]["approved_by"].startswith("ai:"):
            raise ValueError("AI cannot approve the human codebook")
        if document["codebook"] != merged["codebook"]:
            raise ValueError("Codebooks differ; do not merge incompatible annotation rounds")
        if document["assignments_sha256"] != merged["assignments_sha256"]:
            raise ValueError("Assignment hashes differ")
        named = set()
        for sample in document["samples"]:
            if len(sample["reviews"]) != 1:
                raise ValueError("Each returned file must contain one review slot per sample")
            review = sample["reviews"][0]
            reviewer = review["reviewer_id"]
            if reviewer is not None:
                if reviewer.startswith("ai:"):
                    raise ValueError("AI reviews are not human round-one input")
                named.add(reviewer)
            if any(v is not None for v in review["same_cause_as_cluster"].values()):
                raise ValueError("Round-one input must not contain cluster judgments")
            adjudication = sample["adjudication"]
            if adjudication["status"] != "pending" or any(
                adjudication[k] is not None
                for k in (
                    "reviewer_id",
                    "misconception",
                    "misconception_type",
                    "confidence",
                    "evidence",
                )
            ):
                raise ValueError("Round-one input must have blank pending adjudication")
        if len(named) != 1:
            raise ValueError("Each returned file must identify exactly one human reviewer")
        reviewer = named.pop()
        if reviewer in reviewers:
            raise ValueError(
                "Duplicate reviewer across files; choose a verified version explicitly"
            )
        reviewers.add(reviewer)
        for sample in document["samples"]:
            review = sample["reviews"][0]
            if review["reviewer_id"] is None:
                if any(
                    review[k] is not None
                    for k in ("misconception", "misconception_type", "confidence", "evidence")
                ):
                    raise ValueError("Partially filled reviews must identify their reviewer")
                continue  # Leave genuinely unfilled slots absent; do not assign an identity.
            by_id[sample["submission_id"]]["reviews"].append(deepcopy(review))
    queue = []
    for sample in merged["samples"]:
        completed = [r for r in sample["reviews"] if r["status"] == "complete"]
        decisions = {(r["misconception"], r["misconception_type"]) for r in completed}
        queue.append(
            {
                "submission_id": sample["submission_id"],
                "n_completed": len(completed),
                "n_independent": sum(r["independent_blind_review"] for r in completed),
                "disagreement": len(decisions) > 1 if len(completed) >= 2 else None,
                "status": "awaiting_human_adjudication"
                if len(completed) >= 2
                else "insufficient_completed_reviews",
            }
        )
    merged["intake"] = {"round": 1, "reviewers": sorted(reviewers), "adjudication_queue": queue}
    validate_annotations(merged, assignments)
    return merged

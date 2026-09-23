"""Offline scoring of human annotations. Never used by the clustering pipeline."""

from collections import Counter, defaultdict
from copy import deepcopy
from itertools import combinations

DECISIONS = {"Yes", "No", "Unclear"}
CAUSES = {"Yes", "Partially", "No"}
ARMS = ("A", "B", "C")


def score_annotation_sources(document, assignments):
    """Schema v1 reserves reviewer IDs starting with 'ai:' for AI, never human gold.

    AI records are reference-only: no purity or agreement is calculated for them.
    They never populate human adjudication or approve the human codebook.
    """
    validate_annotations(document, assignments)

    def is_ai(reviewer):
        return isinstance(reviewer, str) and reviewer.startswith("ai:")

    human = deepcopy(document)
    ai_reviews = defaultdict(list)
    for sample, original in zip(human["samples"], document["samples"]):
        sample["reviews"] = [r for r in original["reviews"] if not is_ai(r["reviewer_id"])]
        for rating in original["reviews"]:
            if is_ai(rating["reviewer_id"]) and rating["status"] == "complete":
                ai_reviews[rating["reviewer_id"]].append((original, rating))
        if is_ai(sample["adjudication"]["reviewer_id"]):
            sample["adjudication"]["status"] = "pending"
    if is_ai(human["codebook"]["approved_by"]):
        human["codebook"]["approved_by"] = None
    result = score_annotations(human, assignments)
    result["annotation_source"] = "human_expert_annotation"
    result["status"] = (
        "waiting_for_human_expert_annotation"
        if result["status"] == "waiting_for_annotation"
        else result["status"]
    )
    reports = []
    for reviewer, reviews in sorted(ai_reviews.items()):
        reports.append(
            {
                "annotation_source": "AI annotation",
                "reviewer_id": reviewer,
                "status": "reference_only_not_expert_validated",
                "n_completed": len(reviews),
                "n_independent_blind": sum(r["independent_blind_review"] for _, r in reviews),
                "decision_counts": dict(Counter(r["misconception"] for _, r in reviews)),
                "cluster_purity": None,
                "raw_agreement": None,
                "cohen_kappa": None,
                "reason": "AI reference annotations are not eligible for expert validation metrics.",
            }
        )
    result["ai_annotation"] = reports
    return result


def agreement(left, right):
    """Nominal raw agreement and Cohen kappa; undefined denominators remain null."""
    if len(left) != len(right):
        raise ValueError("Paired ratings must have equal length")
    n = len(left)
    if not n:
        return {
            "n_paired": 0,
            "raw_agreement": None,
            "cohen_kappa": None,
            "reason": "no_paired_completed_ratings",
        }
    observed = sum(a == b for a, b in zip(left, right)) / n
    lc, rc = Counter(left), Counter(right)
    expected = sum(lc[label] * rc[label] for label in lc.keys() | rc.keys()) / n**2
    return {
        "n_paired": n,
        "raw_agreement": observed,
        "cohen_kappa": (observed - expected) / (1 - expected) if expected < 1 else None,
        "reason": "constant_marginals_kappa_undefined" if expected == 1 else None,
        "left_counts": dict(lc),
        "right_counts": dict(rc),
    }


def validate_annotations(document, assignments):
    if document.get("schema_version") != 1:
        raise ValueError("Unsupported annotation schema_version")
    lookup = {row["submission_id"]: row for row in assignments}
    if not assignments or len(lookup) != len(assignments):
        raise ValueError("Assignments must be nonempty with unique submission IDs")
    for row in assignments:
        clusters = row["clusters_seed42"]
        if set(clusters) != set(ARMS) or any(
            type(v) is not int or v < 0 for v in clusters.values()
        ):
            raise ValueError("Assignments must have nonnegative integer clusters for A/B/C")
    samples = document["samples"]
    ids = [row["submission_id"] for row in samples]
    if len(ids) != len(set(ids)) or set(ids) != set(lookup):
        raise ValueError(
            "Annotation IDs must match the fixed review sample exactly, without duplicates"
        )
    codebook = document["codebook"]
    if codebook["label_policy"] not in (None, "single_primary"):
        raise ValueError("Multi-label purity is not implemented; agree a protocol before scoring")
    for key in ("approved_by", "version"):
        value = codebook[key]
        if value is not None and (not isinstance(value, str) or not value.strip()):
            raise ValueError(f"Codebook {key} must be a nonempty string or null")
    types = codebook["misconception_types"]
    if (
        not isinstance(types, list)
        or any(not isinstance(t, str) or not t.strip() for t in types)
        or len(types) != len(set(types))
    ):
        raise ValueError("Codebook types must be unique nonempty strings")
    ready = bool(
        codebook["approved_by"]
        and codebook["version"]
        and codebook["label_policy"] == "single_primary"
        and types
    )
    for sample in samples:
        if sample["problem_id"] != lookup[sample["submission_id"]]["problem_id"]:
            raise ValueError("Problem ID mismatch")
        seen = set()
        for rating in sample["reviews"] + [sample["adjudication"]]:
            if rating["status"] not in ("pending", "complete"):
                raise ValueError("Rating status must be pending or complete")
            decision, kind, confidence = (
                rating[key] for key in ("misconception", "misconception_type", "confidence")
            )
            if decision is not None and decision not in DECISIONS:
                raise ValueError("Misconception must be Yes/No/Unclear or null")
            if kind is not None and (not isinstance(kind, str) or not kind.strip()):
                raise ValueError("Type must be a nonempty string or null")
            if kind is not None and decision in ("No", "Unclear"):
                raise ValueError("No/Unclear must not carry a misconception type")
            ai_rating = str(rating.get("reviewer_id", "")).startswith("ai:")
            if kind is not None and ready and not ai_rating and kind not in types:
                raise ValueError("Type absent from approved codebook")
            if confidence is not None and (type(confidence) is not int or not 1 <= confidence <= 5):
                raise ValueError("Confidence must be an integer 1..5 or null")
            if rating["status"] == "complete":
                for key in ("reviewer_id", "evidence"):
                    if not isinstance(rating[key], str) or not rating[key].strip():
                        raise ValueError(f"Completed rating requires {key}")
                if decision is None or confidence is None:
                    raise ValueError("Completed rating requires decision and confidence")
        for rating in sample["reviews"]:
            reviewer = rating["reviewer_id"]
            if reviewer is not None:
                if not isinstance(reviewer, str) or not reviewer.strip() or reviewer in seen:
                    raise ValueError("Reviewer ID must be nonempty and unique per submission")
                seen.add(reviewer)
            if type(rating["independent_blind_review"]) is not bool:
                raise ValueError("independent_blind_review must be boolean")
            if set(rating["same_cause_as_cluster"]) != set(ARMS):
                raise ValueError("Cluster ratings require exactly A/B/C")
            if any(
                v is not None and v not in CAUSES for v in rating["same_cause_as_cluster"].values()
            ):
                raise ValueError("Same-cause rating must be Yes/Partially/No or null")
    return ready


def score_annotations(document, assignments):
    ready = validate_annotations(document, assignments)
    lookup = {row["submission_id"]: row for row in assignments}
    samples = document["samples"]
    completed = [r for s in samples for r in s["reviews"] if r["status"] == "complete"]
    adjudicated = [s for s in samples if s["adjudication"]["status"] == "complete"]
    purity_results, agreement_results = [], []
    for problem in sorted({s["problem_id"] for s in samples}):
        subset = [s for s in samples if s["problem_id"] == problem]
        for arm in ARMS:
            counts = defaultdict(Counter)
            coverage = Counter()
            decisions = Counter()
            cluster_decisions = defaultdict(Counter)
            members = defaultdict(list)
            for sample in subset:
                cluster = str(lookup[sample["submission_id"]]["clusters_seed42"][arm])
                coverage[cluster] += 1
                rating = sample["adjudication"]
                category = rating["misconception"] if rating["status"] == "complete" else "pending"
                decisions[category] += 1
                cluster_decisions[cluster][category] += 1
                members[cluster].append(sample["submission_id"])
                if ready and category == "Yes" and rating["misconception_type"] is not None:
                    counts[cluster][rating["misconception_type"]] += 1
            n = sum(sum(c.values()) for c in counts.values())
            purity_results.append(
                {
                    "problem_id": problem,
                    "arm": arm,
                    "n_review_candidates": len(subset),
                    "decision_counts": dict(decisions),
                    "n_typed_adjudicated_yes": n,
                    "n_yes_without_type": sum(
                        s["adjudication"]["status"] == "complete"
                        and s["adjudication"]["misconception"] == "Yes"
                        and s["adjudication"]["misconception_type"] is None
                        for s in subset
                    ),
                    "type_coverage_of_candidates": n / len(subset),
                    "review_candidates_per_cluster": dict(coverage),
                    "typed_counts_per_cluster": {key: dict(value) for key, value in counts.items()},
                    "purity_numerator": sum(max(c.values()) for c in counts.values())
                    if n
                    else None,
                    "cluster_details": [
                        {
                            "cluster_id": key,
                            "reviewed_sample_ids": sorted(members[key]),
                            "n_candidates": coverage[key],
                            "decision_counts": dict(cluster_decisions[key]),
                            "n_typed_yes": sum(counts.get(key, Counter()).values()),
                            "typed_coverage": sum(counts.get(key, Counter()).values())
                            / coverage[key],
                            "type_counts": dict(counts.get(key, Counter())),
                            "modal_types": sorted(
                                t
                                for t, number in counts.get(key, Counter()).items()
                                if number == max(counts.get(key, Counter()).values())
                            )
                            if counts.get(key, Counter())
                            else [],
                            "multiple_observed_types": len(counts.get(key, Counter())) > 1
                            if counts.get(key, Counter())
                            else None,
                        }
                        for key in sorted(coverage)
                    ],
                    "cluster_purity": sum(max(c.values()) for c in counts.values()) / n
                    if n
                    else None,
                    "reason": None
                    if n
                    else ("codebook_not_approved" if not ready else "no_typed_adjudicated_yes"),
                    "scope": "misconception_type_purity_among_adjudicated_Yes_only_in_selected_sample",
                }
            )
        independent = defaultdict(dict)
        for sample in subset:
            for rating in sample["reviews"]:
                if rating["status"] == "complete" and rating["independent_blind_review"]:
                    independent[rating["reviewer_id"]][sample["submission_id"]] = rating
        for first, second in combinations(sorted(independent), 2):
            ids = sorted(independent[first].keys() & independent[second].keys())
            left = [independent[first][sid] for sid in ids]
            right = [independent[second][sid] for sid in ids]
            typed = [
                (a["misconception_type"], b["misconception_type"])
                for a, b in zip(left, right)
                if ready
                and a["misconception"] == b["misconception"] == "Yes"
                and a["misconception_type"] is not None
                and b["misconception_type"] is not None
            ]
            agreement_results.append(
                {
                    "problem_id": problem,
                    "reviewer_pair": [first, second],
                    "misconception_decision": agreement(
                        [r["misconception"] for r in left], [r["misconception"] for r in right]
                    ),
                    "misconception_type_both_yes": agreement(
                        [a for a, _ in typed], [b for _, b in typed]
                    ),
                    "same_cause_as_cluster": {
                        arm: agreement(
                            [
                                a["same_cause_as_cluster"][arm]
                                for a, b in zip(left, right)
                                if a["same_cause_as_cluster"][arm] is not None
                                and b["same_cause_as_cluster"][arm] is not None
                            ],
                            [
                                b["same_cause_as_cluster"][arm]
                                for a, b in zip(left, right)
                                if a["same_cause_as_cluster"][arm] is not None
                                and b["same_cause_as_cluster"][arm] is not None
                            ],
                        )
                        for arm in ARMS
                    },
                }
            )
    return {
        "status": "waiting_for_annotation"
        if not completed and not adjudicated
        else "partial_expert_validation",
        "n_candidates": len(samples),
        "n_completed_independent_records": sum(r["independent_blind_review"] for r in completed),
        "n_completed_records": len(completed),
        "n_adjudicated": len(adjudicated),
        "codebook_ready": ready,
        "cluster_purity": purity_results
        if any(r["cluster_purity"] is not None for r in purity_results)
        else None,
        "purity_details": purity_results,
        "agreement": agreement_results
        if any(r["misconception_decision"]["n_paired"] for r in agreement_results)
        else None,
        "agreement_details": agreement_results,
        "limitations": [
            "Purposive 17-sample selection from C, not whole-cohort purity.",
            "No student IDs; no unseen-student generalization.",
            "No/Unclear/pending are excluded from TYPE purity; inspect coverage and decision counts.",
            "Confidence is recorded but not used as a statistical weight.",
            "Same-cause ratings are post-cluster judgments, not independent misconception labels.",
        ],
    }

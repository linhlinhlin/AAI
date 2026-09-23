"""Small offline experiment: split, fit clusters, freeze medoids, explain."""

import hashlib
from collections import Counter

import numpy as np
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn.metrics import accuracy_score, adjusted_rand_score, silhouette_score
from sklearn.model_selection import GroupShuffleSplit
from sklearn.tree import DecisionTreeClassifier

from .domain import Submission
from .features import FeatureSpace, route_submission, weighted_hamming


def leakage_groups(rows: list[Submission]) -> np.ndarray:
    """Connected components of shared student OR exact UTF-8 source hash."""
    parents = list(range(len(rows)))

    def root(i: int) -> int:
        while parents[i] != i:
            parents[i] = parents[parents[i]]
            i = parents[i]
        return i

    seen = {}
    for i, row in enumerate(rows):
        digest = hashlib.sha256(row.source_code.encode("utf-8")).hexdigest()
        keys = [("source", digest)]
        if row.student_id is not None:
            keys.append(("student", row.student_id))
        for key in keys:
            if key in seen:
                parents[root(i)] = root(seen[key])
            seen[key] = i
    return np.asarray([root(i) for i in range(len(rows))])


def cluster_labels(
    values: np.ndarray, space: FeatureSpace, method: str, k: int, seed: int
) -> tuple[np.ndarray, np.ndarray]:
    distance = weighted_hamming(values, values, space.weights)
    if method == "exact":
        # Exact baseline groups error signatures only, regardless of AST mode.
        columns = [i for i, name in enumerate(space.names) if name.startswith("test:")]
        _, labels = np.unique(values[:, columns].astype(str), axis=0, return_inverse=True)
    elif method == "agglomerative":
        labels = AgglomerativeClustering(
            n_clusters=k, metric="precomputed", linkage="average"
        ).fit_predict(distance)
    elif method == "kmeans":
        labels = KMeans(n_clusters=k, n_init=10, random_state=seed).fit_predict(
            space.onehot(values)
        )
    else:
        raise ValueError("method must be exact, agglomerative or kmeans")
    return labels, distance


def medoid_indices(labels: np.ndarray, distances: np.ndarray) -> list[int]:
    result = []
    for label in sorted(set(labels.tolist())):
        members = np.flatnonzero(labels == label)
        result.append(int(members[np.argmin(distances[np.ix_(members, members)].sum(axis=1))]))
    return result


def explain_clusters(
    train: np.ndarray,
    train_labels: np.ndarray,
    holdout: np.ndarray,
    holdout_labels: np.ndarray,
    names: list[str],
    seed: int,
) -> dict:
    tree = DecisionTreeClassifier(max_depth=3, min_samples_leaf=2, random_state=seed)
    tree.fit(train, train_labels)
    rules = []
    train_leaves, holdout_leaves = tree.apply(train), tree.apply(holdout)

    def visit(node: int, conditions: list[str]) -> None:
        feature = tree.tree_.feature[node]
        if feature >= 0:
            visit(tree.tree_.children_left[node], conditions + [f"NOT ({names[feature]})"])
            visit(tree.tree_.children_right[node], conditions + [names[feature]])
            return
        predicted = int(tree.classes_[np.argmax(tree.tree_.value[node][0])])
        train_mask, held_mask = train_leaves == node, holdout_leaves == node
        rules.append(
            {
                "if": conditions or ["TRUE"],
                "then_cluster": predicted,
                "train_support": int(train_mask.sum()),
                "train_precision": float(np.mean(train_labels[train_mask] == predicted)),
                "holdout_support": int(held_mask.sum()),
                "holdout_precision": float(np.mean(holdout_labels[held_mask] == predicted))
                if held_mask.any()
                else None,
            }
        )

    visit(0, [])
    return {
        "target": "cluster_id_only_not_validated_misconception",
        "train_fidelity": float(accuracy_score(train_labels, tree.predict(train))),
        "holdout_fidelity": float(accuracy_score(holdout_labels, tree.predict(holdout))),
        "holdout_majority_baseline_fidelity": float(
            np.mean(holdout_labels == Counter(train_labels.tolist()).most_common(1)[0][0])
        ),
        "rules": rules,
    }


def run_experiment(
    submissions: list[Submission],
    *,
    test_ids: list[str],
    method: str = "agglomerative",
    k: int = 2,
    seed: int = 42,
    test_fraction: float = 0.25,
    feature_mode: str = "combined",
    test_weight: float = 0.8,
) -> dict:
    """No code execution. A cluster is a review candidate, never a diagnosis.

    Holdout targets are nearest training medoids for every method, including KMeans.
    This deliberately evaluates an inexpensive frozen assignment policy, not a
    re-fitted holdout clustering or KMeans' nearest-centroid prediction.
    """
    if method not in ("exact", "agglomerative", "kmeans"):
        raise ValueError("Unknown clustering method")
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")
    if not 0 < test_fraction < 1:
        raise ValueError("test_fraction must be between 0 and 1")
    if feature_mode not in ("outcomes", "structural", "combined") or not 0 < test_weight <= 1:
        raise ValueError("Invalid feature mode or test weight")
    if method == "exact":
        feature_mode = "outcomes"
    if not test_ids or len(test_ids) != len(set(test_ids)):
        raise ValueError("Provide nonempty unique test IDs from the test manifest")
    if len(submissions) > 2000:
        raise ValueError("Prototype limit is 2000 rows per cohort (quadratic distances)")
    if len({row.cohort_key for row in submissions}) > 1:
        raise ValueError("Run each problem/language/suite cohort separately")
    if len({row.submission_id for row in submissions}) != len(submissions):
        raise ValueError("Duplicate submission IDs")
    for row in submissions:
        if set(row.outcomes) - set(test_ids):
            raise ValueError("Outcome test IDs are absent from the manifest")
        if not set(row.outcomes.values()) <= {
            "pass",
            "fail",
            "runtime_error",
            "timeout",
            "not_run",
        }:
            raise ValueError("Unsupported test outcome")
    routes = {row.submission_id: route_submission(row, test_ids) for row in submissions}
    rows = [row for row in submissions if routes[row.submission_id] == "eligible"]
    result = {
        "status": "abstained",
        "method": method,
        "feature_mode": feature_mode,
        "seed": seed,
        "config": {
            "k": k,
            "test_fraction": test_fraction,
            "test_weight": test_weight,
            "effective_feature_mode": feature_mode,
            "k_used": method != "exact",
        },
        "silhouette_metric": "weighted_hamming_common_comparison_not_kmeans_native_geometry",
        "routes": routes,
        "route_counts": dict(Counter(routes.values())),
        "n_eligible": len(rows),
        "identity": {
            "missing_student_ids": sum(row.student_id is None for row in submissions),
            "split_guarantee": (
                "known_student_and_exact_source_disjoint"
                if all(row.student_id is not None for row in submissions)
                else "exact_source_disjoint_only_student_independence_unverified"
            ),
        },
        "warnings": [
            "Clusters and surrogate rules are behavioral hypotheses requiring instructor validation.",
            "Exact source grouping does not detect renamed or otherwise near-duplicate code.",
            "AST presence indicators are syntactic evidence, not semantic fault detectors.",
        ],
    }
    if any(row.student_id is None for row in submissions):
        result["warnings"].append(
            "Student identity is missing: holdout is exploratory, not a student-disjoint benchmark."
        )
    if len(rows) < 4:
        return dict(result, reason="fewer_than_four_eligible_rows")
    # Preserve duplicate/student bridges even when a bridge row was routed out.
    all_groups = leakage_groups(submissions)
    groups = all_groups[[routes[row.submission_id] == "eligible" for row in submissions]]
    if len(set(groups.tolist())) < 2:
        return dict(result, reason="fewer_than_two_independent_groups")
    splitter = GroupShuffleSplit(n_splits=1, test_size=test_fraction, random_state=seed)
    train_i, held_i = next(splitter.split(rows, groups=groups))
    train_rows, held_rows = [rows[i] for i in train_i], [rows[i] for i in held_i]
    result["split"] = {
        "train_ids": [r.submission_id for r in train_rows],
        "holdout_ids": [r.submission_id for r in held_rows],
        "train_groups": len(set(groups[train_i].tolist())),
        "holdout_groups": len(set(groups[held_i].tolist())),
    }
    if len(train_rows) < 3:
        return dict(result, reason="fewer_than_three_training_rows")
    space = FeatureSpace.fit(train_rows, test_ids, test_weight, feature_mode)
    if not space.names:
        return dict(result, reason="no_varying_structural_features", features=[])
    train, held = space.transform(train_rows), space.transform(held_rows)
    active = space.weights > 0
    unique_count = len(np.unique(train[:, active].astype(str), axis=0))
    if unique_count < 2:
        return dict(result, reason="identical_training_features")
    if method != "exact" and (k >= len(train) or k > unique_count):
        return dict(result, reason="k_requires_more_training_rows_or_distinct_patterns")
    labels, distances = cluster_labels(train, space, method, k, seed)
    label_count = len(set(labels.tolist()))
    if label_count < 2:
        return dict(result, reason="single_cluster")
    medoids = medoid_indices(labels, distances)
    held_distances = weighted_hamming(held, train[medoids], space.weights)
    held_labels = np.asarray([labels[medoids[i]] for i in np.argmin(held_distances, axis=1)])
    result.update(
        {
            "status": "ok",
            "n_clusters": label_count,
            "features": [
                {"name": name, "weight": float(weight)}
                for name, weight in zip(space.names, space.weights)
            ],
            "oav": {
                r.submission_id: {name: str(value) for name, value in zip(space.names, values)}
                for r, values in zip(train_rows + held_rows, np.concatenate([train, held]))
            },
            "train_assignments": {
                r.submission_id: int(label) for r, label in zip(train_rows, labels)
            },
            "holdout_assignments": {
                r.submission_id: int(label) for r, label in zip(held_rows, held_labels)
            },
            "medoids": {str(int(labels[i])): train_rows[i].submission_id for i in medoids},
            "silhouette_train": float(silhouette_score(distances, labels, metric="precomputed"))
            if 1 < label_count < len(train)
            else None,
            "holdout_distance_to_medoid": {
                r.submission_id: float(d) for r, d in zip(held_rows, held_distances.min(axis=1))
            },
            "holdout_assignment_ties": int(
                np.sum(
                    np.sum(np.isclose(held_distances, held_distances.min(axis=1)[:, None]), axis=1)
                    > 1
                )
            ),
            "assignment_policy": "nearest_training_medoid_weighted_hamming; ties select lowest cluster id",
            "explanation": explain_clusters(
                space.onehot(train, False),
                labels,
                space.onehot(held, False),
                held_labels,
                space.onehot_names,
                seed,
            ),
        }
    )
    # Metric consistency check against the cheap outcome-only signature baseline.
    # The baseline always uses actual outcomes, even if this run has only structure.
    outcome_values = np.asarray(
        [[row.outcomes[test] for test in sorted(test_ids)] for row in train_rows]
    )
    _, exact = np.unique(outcome_values, axis=0, return_inverse=True)
    result["ari_vs_exact_signature_train"] = float(adjusted_rand_score(exact, labels))
    return result

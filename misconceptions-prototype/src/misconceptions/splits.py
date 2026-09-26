"""Corpus-wide, order-independent splits with student/source connected components."""

import hashlib
import json
from collections import Counter
from dataclasses import asdict

import numpy as np

PARTITIONS = ("train", "validation", "test")


def leakage_groups(rows):
    parents = list(range(len(rows)))

    def root(i):
        while parents[i] != i:
            parents[i] = parents[parents[i]]
            i = parents[i]
        return i

    seen = {}
    for i, row in enumerate(rows):
        keys = [("source", hashlib.sha256(row.source_code.encode("utf-8")).hexdigest())]
        if not row.source_code.strip():
            keys = []  # Absence of code is not evidence that two students copied a program.
        if row.student_id is not None:
            keys.append(("student", row.student_id))
        for key in keys:
            if key in seen:
                parents[root(i)] = root(seen[key])
            seen[key] = i
    return np.asarray([root(i) for i in range(len(rows))])


def corpus_digest(rows):
    content = [asdict(row) for row in sorted(rows, key=lambda row: row.submission_id)]
    return hashlib.sha256(json.dumps(content, sort_keys=True, ensure_ascii=False,
                                    separators=(",", ":")).encode("utf-8")).hexdigest()


def validate_assignments(rows, assignments):
    ids = [row.submission_id for row in rows]
    if len(set(ids)) != len(ids) or set(ids) != set(assignments):
        raise ValueError("Split IDs must match the dataset exactly and be unique")
    if not set(assignments.values()) <= set(PARTITIONS):
        raise ValueError("Unknown split partition")
    seen = {}
    for row, group in zip(rows, leakage_groups(rows)):
        partition = assignments[row.submission_id]
        if group in seen and seen[group] != partition:
            raise ValueError("Student/source connected component crosses split partitions")
        seen[group] = partition


def create_lock(rows, seed=42):
    if not rows:
        raise ValueError("Cannot split an empty corpus")
    groups = leakage_groups(rows)
    representatives = {}
    for row, group in zip(rows, groups):
        representatives[group] = min(representatives.get(group, row.submission_id), row.submission_id)
    group_partitions = {}
    for group, sid in representatives.items():
        value = int(hashlib.sha256(f"{seed}:{sid}".encode()).hexdigest(), 16) / 2**256
        group_partitions[group] = "train" if value < 0.7 else "validation" if value < 0.85 else "test"
    assignments = {row.submission_id: group_partitions[group] for row, group in zip(rows, groups)}
    validate_assignments(rows, assignments)
    return {
        "schema_version": 1, "seed": seed, "corpus_sha256": corpus_digest(rows),
        "policy": "sha256_component_min_id_70_15_15_v1",
        "independence": "student_and_exact_source" if all(r.student_id for r in rows)
        else "exact_source_only_student_identity_incomplete",
        "counts": dict(Counter(assignments.values())),
        "groups": dict(Counter(group_partitions.values())),
        "assignments": dict(sorted(assignments.items())),
    }


def validate_lock(rows, lock):
    if lock.get("schema_version") != 1 or lock.get("corpus_sha256") != corpus_digest(rows):
        raise ValueError("Split lock does not match the exact corpus")
    validate_assignments(rows, lock["assignments"])
    expected = create_lock(rows, lock["seed"])
    if lock != expected:
        raise ValueError("Split lock differs from its deterministic policy")

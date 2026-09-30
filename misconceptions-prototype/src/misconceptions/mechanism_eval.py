"""Cluster failing programs label-free, then score the partitions against mechanism labels.

Labels are read only by the scoring functions. Representations are fitted on the
training partition of the same problem and applied transductively to one cohort.
"""

from collections import Counter
from itertools import combinations

import numpy as np
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn.metrics import adjusted_mutual_info_score, adjusted_rand_score, silhouette_score

# Pre-registered block masses. Each representation's masses sum to one.
REPRESENTATIONS = {
    "outcomes": {"test": 1.0},
    "structural": {"ast": 1.0},
    "outcomes_stdout": {"test": 0.6, "stdout": 0.4},
    "combined_stdout": {"test": 0.48, "ast": 0.12, "stdout": 0.4},
    "deviation": {"test": 0.3, "dev": 0.4, "agg": 0.3},
    "evidence": {"test": 0.2, "dev": 0.3, "agg": 0.2, "code": 0.3},
    "code_cues": {"code": 1.0},
}
BLOCK_PREFIX = {"test": "test:", "ast": "ast:", "stdout": "stdout:", "dev": "dev:", "agg": "agg:",
                "code": "code:"}


def block_of(name):
    return next((block for block, prefix in BLOCK_PREFIX.items() if name.startswith(prefix)), None)


class CategoricalSpace:
    def __init__(self, names, categories, weights):
        self.names, self.categories, self.weights = names, categories, np.asarray(weights, float)

    @classmethod
    def fit(cls, train_rows, masses):
        names_by_block = {}
        for name in sorted({name for row in train_rows for name in row}):
            block = block_of(name)
            if block in masses and len({row.get(name, "__unknown__") for row in train_rows}) > 1:
                names_by_block.setdefault(block, []).append(name)
        present = {b: m for b, m in masses.items() if names_by_block.get(b)}
        total = sum(present.values())
        names, categories, weights = [], [], []
        for block, mass in present.items():
            for name in names_by_block[block]:
                names.append(name)
                categories.append(tuple(sorted({str(row.get(name, "__unknown__")) for row in train_rows}
                                               | {"__unknown__"})))
                weights.append(mass / total / len(names_by_block[block]))
        return cls(names, categories, weights)

    def transform(self, rows):
        values = np.empty((len(rows), len(self.names)), dtype=object)
        for i, row in enumerate(rows):
            for j, (name, categories) in enumerate(zip(self.names, self.categories)):
                value = str(row.get(name, "__unknown__"))
                values[i, j] = value if value in categories else "__unknown__"
        return values

    def onehot(self, values):
        blocks = [(values[:, j, None] == np.asarray(c)[None, :]).astype(float) * np.sqrt(w / 2)
                  for j, (c, w) in enumerate(zip(self.categories, self.weights))]
        return np.concatenate(blocks, axis=1) if blocks else np.zeros((len(values), 0))

    def distances(self, values):
        result = np.zeros((len(values), len(values)))
        for j, weight in enumerate(self.weights):
            result += weight * (values[:, j, None] != values[None, :, j])
        return result


def cluster(matrix, distances, method, k, seed):
    if k <= 1 or len(matrix) <= 1:
        return np.zeros(len(matrix), dtype=int)
    if method == "kmeans":
        return KMeans(n_clusters=k, n_init=10, random_state=seed).fit_predict(matrix)
    if method == "hac":
        return AgglomerativeClustering(n_clusters=k, metric="precomputed",
                                       linkage="average").fit_predict(distances)
    raise ValueError(method)


def distinct_patterns(matrix):
    return len(np.unique(np.round(matrix, 12), axis=0))


def choose_k_silhouette(matrix, distances, method, seed, k_max=10):
    """Label-free k: best silhouette on the representation's own distances."""
    limit = min(k_max, distinct_patterns(matrix), len(matrix) - 1)
    best = (None, 1)
    for k in range(2, limit + 1):
        labels = cluster(matrix, distances, method, k, seed)
        if 1 < len(set(labels.tolist())) < len(labels):
            score = silhouette_score(distances, labels, metric="precomputed")
            if best[0] is None or score > best[0]:
                best = (score, k)
    return best[1]


def pairwise_scores(predicted, gold):
    same_p = same_g = both = 0
    for i, j in combinations(range(len(gold)), 2):
        p, g = predicted[i] == predicted[j], gold[i] == gold[j]
        same_p += p
        same_g += g
        both += p and g
    precision = both / same_p if same_p else None
    recall = both / same_g if same_g else None
    f1 = 2 * precision * recall / (precision + recall) if precision and recall else 0.0
    return precision, recall, f1


def purity(predicted, gold):
    table = Counter(zip(predicted, gold))
    best = Counter()
    for (p, _), n in table.items():
        best[p] = max(best[p], n)
    return sum(best.values()) / len(gold)


def ceiling(values, gold):
    """Best accuracy of any function of the exact representation (bucket majority)."""
    buckets = Counter()
    per = {}
    for row, label in zip(map(tuple, values), gold):
        per.setdefault(row, Counter())[label] += 1
    for counts in per.values():
        buckets[None] += max(counts.values())
    return buckets[None] / len(gold)


def score(predicted, gold):
    precision, recall, f1 = pairwise_scores(list(predicted), list(gold))
    return {"ari": adjusted_rand_score(gold, predicted),
            "ami": adjusted_mutual_info_score(gold, predicted),
            "pair_precision": precision, "pair_recall": recall, "pair_f1": f1,
            "purity": purity(list(predicted), list(gold)), "n_clusters": len(set(predicted))}


def paired_summary(differences, seed=0, resamples=10000):
    values = np.asarray([d for d in differences if d is not None], dtype=float)
    if len(values) == 0:
        return {"n": 0}
    rng = np.random.default_rng(seed)
    means = rng.choice(values, size=(resamples, len(values)), replace=True).mean(axis=1)
    from scipy.stats import wilcoxon
    try:
        p = float(wilcoxon(values).pvalue) if np.any(values != 0) else 1.0
    except ValueError:
        p = None
    return {"n": len(values), "mean": float(values.mean()),
            "ci95": [float(np.quantile(means, 0.025)), float(np.quantile(means, 0.975))],
            "wins": int((values > 0).sum()), "losses": int((values < 0).sum()), "wilcoxon_p": p}

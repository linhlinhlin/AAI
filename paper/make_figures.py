"""Figures for the topic-5 manuscript from the registered test run (no hand-typed numbers).

Run with a Python that has matplotlib:  python paper/make_figures.py --lang en|vi
"""

import argparse
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULTS = ROOT / "research/runs/mechanism-v1.1-test/results.json"
ACCENT, NEUTRAL, INK, MUTED = "#2a78d6", "#7c7b76", "#0b0b0b", "#52514e"
PROPOSED = {"deviation", "evidence"}
ORDER = ["outcomes", "outcomes_stdout", "combined_stdout", "structural", "code_cues", "embedding",
         "deviation", "evidence"]
NAMES = {
    "en": {"outcomes": "Test outcomes (classic OAV)", "outcomes_stdout": "Outcomes + stdout",
           "combined_stdout": "Combined + stdout", "structural": "AST presence",
           "code_cues": "Code cues", "embedding": "Code embedding (Qwen3-0.6B)",
           "deviation": "Deviation OAV (ours)", "evidence": "Evidence OAV (ours)",
           "real": "Real repairs (full cohorts)", "injected": "Injected mutants (test cohorts)",
           "ari": "Adjusted Rand index vs. mechanism (K-means, oracle k)",
           "ceiling": "Identifiability ceiling", "null": "Random refinement of same granularity",
           "outcome_ceiling": "Test outcomes", "deviation_ceiling": "Deviation OAV"},
    "vi": {"outcomes": "Kết quả test (OAV kinh điển)", "outcomes_stdout": "Kết quả + stdout",
           "combined_stdout": "Kết hợp + stdout", "structural": "Cấu trúc AST",
           "code_cues": "Manh mối mã", "embedding": "Embedding mã (Qwen3-0.6B)",
           "deviation": "OAV độ lệch (đề xuất)", "evidence": "OAV bằng chứng (đề xuất)",
           "real": "Sửa lỗi thật (toàn cohort)", "injected": "Tiêm lỗi (cohort test)",
           "ari": "ARI so với cơ chế (K-means, k theo nhãn)",
           "ceiling": "Trần khả phân biệt", "null": "Phân hoạch ngẫu nhiên cùng độ mịn",
           "outcome_ceiling": "Kết quả test", "deviation_ceiling": "OAV độ lệch"},
}
SCOPE = {"real": "full", "injected": "partition"}


def cohort_values(report, benchmark, rep, key="kmeans_oracle", metric="ari"):
    scope = report["benchmarks"][benchmark]["scopes"][SCOPE[benchmark]]
    values = []
    for cohort in scope["cohorts"]:
        entry = cohort["reps"].get(rep)
        if entry and key in entry and entry[key].get(metric) is not None:
            values.append(entry[key][metric])
    return np.asarray(values)


def mean_ci(values, seed=0, resamples=10000):
    rng = np.random.default_rng(seed)
    means = rng.choice(values, size=(resamples, len(values)), replace=True).mean(axis=1)
    return values.mean(), np.quantile(means, 0.025), np.quantile(means, 0.975)


def decimal(value, lang):
    text = f"{value:.2f}"
    return text.replace(".", ",") if lang == "vi" else text


def style(ax, lang="en"):
    from matplotlib.ticker import FuncFormatter
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:.1f}".replace(".", ",")
                                               if lang == "vi" else f"{v:.1f}"))
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.spines["left"].set_color(MUTED)
    ax.spines["bottom"].set_color(MUTED)
    ax.tick_params(colors=MUTED, labelsize=8)
    ax.grid(axis="x", color="#e6e5e0", linewidth=0.6)
    ax.set_axisbelow(True)


def figure_ari(report, lang, out):
    names = NAMES[lang]
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.2), sharey=True)
    for ax, benchmark in zip(axes, ("real", "injected")):
        for row, rep in enumerate(ORDER):
            values = cohort_values(report, benchmark, rep)
            if not len(values):
                continue
            mean, low, high = mean_ci(values)
            color = ACCENT if rep in PROPOSED else NEUTRAL
            ax.plot([low, high], [row, row], color=color, linewidth=2, solid_capstyle="round")
            ax.plot(mean, row, "o", color=color, markersize=6)
            ax.annotate(decimal(mean, lang), (high, row), xytext=(4, 0), textcoords="offset points",
                        va="center", fontsize=7, color=MUTED)
        ax.axvline(0, color=MUTED, linewidth=0.8)
        ax.set_title(names[benchmark], fontsize=9, color=INK, loc="left")
        ax.set_yticks(range(len(ORDER)), [names[r] for r in ORDER])
        style(ax, lang)
    fig.supxlabel(names["ari"], fontsize=8, color=MUTED)
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)


def figure_ceiling(report, lang, out):
    names = NAMES[lang]
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.4), sharey=True)
    rows = [("outcome_ceiling", "outcomes", "ceiling"), ("null", "deviation", "null_ceiling"),
            ("deviation_ceiling", "deviation", "ceiling")]
    for ax, benchmark in zip(axes, ("real", "injected")):
        scope = report["benchmarks"][benchmark]["scopes"][SCOPE[benchmark]]
        for row, (label, rep, field) in enumerate(rows):
            values = np.asarray([c["reps"][rep][field] for c in scope["cohorts"]])
            mean, low, high = mean_ci(values)
            color = ACCENT if label == "deviation_ceiling" else NEUTRAL
            ax.plot([low, high], [row, row], color=color, linewidth=2, solid_capstyle="round")
            ax.plot(mean, row, "o", color=color, markersize=6)
            ax.annotate(decimal(mean, lang), (high, row), xytext=(4, 0), textcoords="offset points",
                        va="center", fontsize=7, color=MUTED)
        ax.set_yticks(range(len(rows)), [names[r[0]] for r in rows])
        ax.set_xlim(0.4, 1.02)
        ax.set_title(names[benchmark], fontsize=9, color=INK, loc="left")
        style(ax, lang)
    fig.supxlabel(names["ceiling"], fontsize=8, color=MUTED)
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lang", choices=("en", "vi"), default="en")
    args = parser.parse_args()
    report = json.loads(RESULTS.read_text(encoding="utf-8"))
    target = HERE / "figures"
    target.mkdir(exist_ok=True)
    plt.rcParams.update({"font.family": "DejaVu Sans", "pdf.fonttype": 42})
    figure_ari(report, args.lang, target / f"ari_{args.lang}.pdf")
    figure_ceiling(report, args.lang, target / f"ceiling_{args.lang}.pdf")
    print("figures written to", target)


if __name__ == "__main__":
    main()

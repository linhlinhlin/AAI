"""Summarize a registered mechanism evaluation: hypothesis verdicts, tables and tokens.

Reads results.json from run_mechanism_eval.py and applies the decision rules of
research/protocol-mechanism-v1.json (with amendments). Numbers are never typed by hand.
"""

import argparse
import json
from pathlib import Path

from misconceptions.research_io import write_json

REPS = ("outcomes", "outcomes_stdout", "combined_stdout", "structural", "code_cues", "deviation",
        "evidence", "embedding")
PRIMARY_SCOPE = {"real": "full", "injected": "partition"}  # Amendment A3 (condition checked below).


def holm(pvalues):
    order = sorted(range(len(pvalues)), key=lambda i: pvalues[i])
    adjusted, running = [None] * len(pvalues), 0.0
    for rank, index in enumerate(order):
        running = max(running, min(1.0, (len(pvalues) - rank) * pvalues[index]))
        adjusted[index] = running
    return adjusted


def verdict(summary, lower_bound_rule=True):
    if not summary or summary.get("n", 0) == 0:
        return "not_evaluable"
    low = summary["ci95"][0]
    return "supported" if low > 0 else "not_supported" if lower_bound_rule else "n/a"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = json.loads(args.results.read_text(encoding="utf-8"))
    out = {"partition": report["partition"], "benchmarks": {}, "hypotheses": {}}
    lines = [f"# Mechanism evaluation ({report['partition']} partition)", ""]
    pvalues, keys = [], []
    for benchmark, result in report["benchmarks"].items():
        scopes = result["scopes"]
        test_cohorts = len(scopes.get("partition", {}).get("cohorts", []))
        scope = PRIMARY_SCOPE[benchmark] if report["partition"] == "test" else "partition"
        if benchmark == "real" and report["partition"] == "test" and test_cohorts >= 10:
            scope = "partition"  # A3 applies only when the sealed partition is too small.
        summary = scopes.get(scope, {}).get("summary")
        entry = {"primary_scope": scope, "eligible_test_cohorts": test_cohorts,
                 "items_by_partition": result["items_by_partition"]}
        if summary:
            comparisons = summary["comparisons"]
            table = summary["table"]
            entry["ari_kmeans_oracle"] = {rep: table["kmeans_oracle"].get(rep, {}).get("ari")
                                          for rep in REPS}
            entry["ari_hac_oracle"] = {rep: table["hac_oracle"].get(rep, {}).get("ari") for rep in REPS}
            entry["ari_kmeans_silhouette"] = {rep: table["kmeans_silhouette"].get(rep, {}).get("ari")
                                              for rep in REPS}
            entry["exact_signature_ari"] = table.get("exact", {}).get("exact_signature", {}).get("ari")
            entry["ceilings"] = summary["ceilings"]
            entry["cohorts"] = table["kmeans_oracle"].get("outcomes", {}).get("cohorts")
            h1a = comparisons.get("H1a:ceiling(outcomes)")
            checks = {
                "H1a": (h1a, "supported" if h1a and h1a.get("n") and h1a["ci95"][1] < 0.95
                        else "not_supported"),
                "H1b": (comparisons.get("H1b:ceiling(deviation)-null"), None),
                "H2_kmeans": (comparisons.get("deviation-outcomes|kmeans_oracle|ari"), None),
                "H2_hac": (comparisons.get("deviation-outcomes|hac_oracle|ari"), None),
                "H3_kmeans": (comparisons.get("evidence-combined_stdout|kmeans_oracle|ari"), None),
                "H3_hac": (comparisons.get("evidence-combined_stdout|hac_oracle|ari"), None),
            }
            if benchmark == "injected":
                checks["H5"] = (comparisons.get("embedding:ari_source-ari_mechanism|kmeans_oracle"), None)
            entry["hypotheses"] = {}
            for name, (value, fixed) in checks.items():
                entry["hypotheses"][name] = {"summary": value,
                                             "verdict": fixed or verdict(value)}
                if value and value.get("wilcoxon_p") is not None and name != "H1a":
                    pvalues.append(value["wilcoxon_p"])
                    keys.append((benchmark, name))
        rules = result["rules"]
        entry["rules"] = {key: {k: v for k, v in value.items() if k in (
            "macro_f1", "coverage", "selective_accuracy", "accuracy_abstain_as_error", "n_rules",
            "bootstrap_macro_f1", "penalty", "n")} for key, value in rules.items()
            if isinstance(value, dict) and key != "seen_problems|H4_difference"}
        h4 = rules.get("seen_problems|H4_difference")
        entry["hypotheses_rules"] = {"H4": {"summary": h4, "verdict": (
            "supported" if h4 and h4["ci95"][0] > 0 else "not_supported")} if benchmark == "real" else None}
        out["benchmarks"][benchmark] = entry
    for (benchmark, name), adjusted in zip(keys, holm(pvalues)):
        out["benchmarks"][benchmark]["hypotheses"][name]["holm_p"] = adjusted
    for benchmark, entry in out["benchmarks"].items():
        header = ("| Representation | ARI K-means (oracle k) | ARI HAC (oracle k) "
                  "| ARI K-means (silhouette k) | Ceiling |")
        title = f"## {benchmark} (primary scope: {entry['primary_scope']}, cohorts: {entry.get('cohorts')})"
        lines += [title, "", header, "|---|---:|---:|---:|---:|"]
        for rep in REPS:
            def fmt(v):
                return "-" if v is None else f"{v:.3f}"
            lines.append(f"| {rep} | {fmt(entry.get('ari_kmeans_oracle', {}).get(rep))} | "
                         f"{fmt(entry.get('ari_hac_oracle', {}).get(rep))} | "
                         f"{fmt(entry.get('ari_kmeans_silhouette', {}).get(rep))} | "
                         f"{fmt(entry.get('ceilings', {}).get(rep))} |")
        lines += ["", f"Exact test signature ARI: {entry.get('exact_signature_ari')}", "",
                  "| Hypothesis | Mean | 95% CI | Wins/Losses | Holm p | Verdict |", "|---|---:|---|---|---:|---|"]
        for name, value in entry.get("hypotheses", {}).items():
            summary = value["summary"] or {}
            ci = summary.get("ci95")
            interval = "-" if not ci else "[{:.3f}, {:.3f}]".format(*ci)
            holm_p = "-" if value.get("holm_p") is None else "{:.4f}".format(value["holm_p"])
            lines.append(f"| {name} | {summary.get('mean', float('nan')):.3f} | {interval} | "
                         f"{summary.get('wins', '-')}/{summary.get('losses', '-')} | {holm_p} | "
                         f"{value['verdict']} |")
        if entry.get("hypotheses_rules") and entry["hypotheses_rules"]["H4"]:
            h4 = entry["hypotheses_rules"]["H4"]
            lines += ["", f"H4 (ILA-2 evidence minus outcome summary, macro-F1): {h4['summary']} -> {h4['verdict']}"]
        lines += ["", "| Rule model | Macro-F1 | Coverage | Selective accuracy | Rules |", "|---|---:|---:|---:|---:|"]
        for key, value in entry["rules"].items():
            if "macro_f1" in value:
                lines.append(f"| {key} | {value['macro_f1']:.3f} | {value.get('coverage', 1.0):.3f} | "
                             f"{value.get('selective_accuracy') or 0:.3f} | {value.get('n_rules', '-')} |")
        lines.append("")
    args.output.mkdir(parents=True, exist_ok=True)
    write_json(args.output / "summary.json", out)
    (args.output / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

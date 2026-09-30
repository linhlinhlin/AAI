"""Build the topic-5 manuscripts from committed research artifacts (no hand-typed numbers).

1. read the replay audit, reproducibility report, benchmark statistics, protocol and the
   registered test-run summary;
2. fill {{tokens}} in the template and sections (Vietnamese uses decimal commas);
3. compile with Tectonic and fail on undefined references, citations or leftover tokens.

Usage: python paper/build.py --lang en|vi [--tectonic PATH]
"""

import argparse
import datetime as dt
import hashlib
import json
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RUNS = ROOT / "research/runs"
DEFAULT_TECTONIC = ROOT.parents[1] / "BaiHong/tmp/tectonic/tectonic.exe"
NEWLINE = "\n"
ROW_END = " \\\\"
REP_ORDER = ("outcomes", "outcomes_stdout", "combined_stdout", "structural", "code_cues", "embedding",
             "deviation", "evidence")
REP_NAMES = {
    "en": {"outcomes": "Test outcomes (classic OAV)", "outcomes_stdout": "Outcomes + stdout",
           "combined_stdout": "Combined + stdout", "structural": "AST presence", "code_cues": "Code cues",
           "embedding": "Code embedding", "deviation": "Deviation OAV (ours)",
           "evidence": "Evidence OAV (ours)", "exact": "Exact test signature"},
    "vi": {"outcomes": "Kết quả test (OAV kinh điển)", "outcomes_stdout": "Kết quả + stdout",
           "combined_stdout": "Kết hợp + stdout", "structural": "Hiện diện AST", "code_cues": "Manh mối mã",
           "embedding": "Embedding mã", "deviation": "OAV độ lệch (đề xuất)",
           "evidence": "OAV bằng chứng (đề xuất)", "exact": "Chữ ký test trùng khớp"},
}
HYPOTHESES = ("H1a", "H1b", "H2_kmeans", "H2_hac", "H3_kmeans", "H3_hac", "H5")
VERDICT = {"en": {"supported": "supported", "not_supported": "not supported",
                  "not_evaluable": "not evaluable"},
           "vi": {"supported": "ủng hộ", "not_supported": "không ủng hộ",
                  "not_evaluable": "không đánh giá được"}}
TRACKS = {"en": {"seen_problems": "Seen assignments", "unseen_problems": "Unseen assignments"},
          "vi": {"seen_problems": "Bài đã thấy", "unseen_problems": "Bài mới"}}
ATTRS = {"en": {"evidence": "evidence", "outcome_summary": "outcome summary"},
         "vi": {"evidence": "bằng chứng", "outcome_summary": "tóm tắt kết quả"}}
MODELS = {"ila": "ILA", "ila2": "ILA-2", "cart": "CART"}


def load(path):
    return json.loads((RUNS / path).read_text(encoding="utf-8"))


def pct(value, digits=1):
    return f"{100 * value:.{digits}f}"


def number(value, digits=3, lang="en"):
    if value is None:
        return "--"
    text = f"{abs(value):.{digits}f}"
    if lang == "vi":
        text = text.replace(".", ",")
    return ("$-$" + text) if value < 0 and float(text.replace(",", ".")) != 0 else text


def ari_rows(summary, benchmark, lang):
    entry = summary["benchmarks"][benchmark]
    rows = []
    for rep in REP_ORDER:
        cells = [entry["ari_kmeans_oracle"].get(rep), entry["ari_hac_oracle"].get(rep),
                 entry["ari_kmeans_silhouette"].get(rep), entry["ceilings"].get(rep)]
        rows.append(REP_NAMES[lang][rep] + " & " + " & ".join(number(c, lang=lang) for c in cells) + ROW_END)
    rows.append(REP_NAMES[lang]["exact"] + " & " + number(entry.get("exact_signature_ari"), lang=lang)
                + " & -- & -- & --" + ROW_END)
    return NEWLINE.join(rows)


def hypothesis_rows(summary, lang):
    rows = []
    for name in HYPOTHESES:
        cells = []
        for benchmark in ("real", "injected"):
            value = summary["benchmarks"][benchmark].get("hypotheses", {}).get(name)
            if not value or not value.get("summary") or not value["summary"].get("n"):
                cells.append("-- & -- & --")
                continue
            s = value["summary"]
            separator = "; " if lang == "vi" else ", "
            interval = f"[{number(s['ci95'][0], lang=lang)}{separator}{number(s['ci95'][1], lang=lang)}]"
            cells.append(f"{number(s['mean'], lang=lang)} & {interval} & {VERDICT[lang][value['verdict']]}")
        rows.append(name.replace("_", " ") + " & " + " & ".join(cells) + ROW_END)
    return NEWLINE.join(rows)


def rule_rows(summary, benchmark, lang):
    rules = summary["benchmarks"][benchmark]["rules"]
    rows = []
    for track in ("seen_problems", "unseen_problems"):
        for attrs in ("evidence", "outcome_summary"):
            for model in ("ila", "ila2", "cart"):
                value = rules.get(f"{track}|{attrs}|{model}")
                if not value:
                    continue
                selective = value.get("selective_accuracy")
                if selective is None:
                    selective = value.get("accuracy_abstain_as_error")
                rows.append(f"{TRACKS[lang][track]} & {MODELS[model]} ({ATTRS[lang][attrs]}) & "
                            f"{number(value.get('macro_f1'), lang=lang)} & "
                            f"{number(value.get('coverage'), lang=lang)} & "
                            f"{number(selective, lang=lang)}" + ROW_END)
        value = rules.get(f"{track}|majority")
        if value:
            rows.append(f"{TRACKS[lang][track]} & {'Majority class' if lang == 'en' else 'Lớp đa số'} & "
                        f"{number(value.get('macro_f1'), lang=lang)} & {number(1.0, lang=lang)} & "
                        f"{number(value.get('accuracy_abstain_as_error'), lang=lang)}" + ROW_END)
    return NEWLINE.join(rows)


ATTRIBUTE_TEXT = {
    "en": {"code:output_calls=0": "the program has no output call",
           "code:input_calls=0": "the program has no input call",
           "agg:numbers=format_only": "printed numbers equal the oracle's but are written differently",
           "agg:prefix=truncated": "the output is a truncated prefix of the oracle",
           "agg:whitespace_only=yes": "the output differs from the oracle only in whitespace",
           "agg:text=extra_words": "the output contains words the oracle lacks",
           "agg:status=timeout": "the failing tests time out",
           "agg:newline_end=same": "the trailing newline is as expected",
           "agg:numbers=fewer": "fewer numbers than the oracle are printed"},
    "vi": {"code:output_calls=0": "chương trình không có lệnh in nào",
           "code:input_calls=0": "chương trình không có lệnh đọc dữ liệu",
           "agg:numbers=format_only": "các số in ra bằng đáp án nhưng viết khác cách",
           "agg:prefix=truncated": "output là phần đầu bị cụt của đáp án",
           "agg:whitespace_only=yes": "output chỉ khác đáp án ở khoảng trắng",
           "agg:text=extra_words": "output có chữ mà đáp án không có",
           "agg:status=timeout": "các test sai đều quá thời gian",
           "agg:newline_end=same": "ký tự xuống dòng cuối đúng như đáp án",
           "agg:numbers=fewer": "in ít số hơn đáp án"},
}
CATEGORY_TEXT = {
    "en": {"MISSING_STATEMENT": "missing statement", "OUTPUT_FORMAT": "output format",
           "OUTPUT_TEXT": "output text", "LOOP_BOUNDARY": "loop boundary", "COMPUTATION": "computation",
           "BRANCH_CONDITION": "branch condition", "INITIALIZATION": "initialisation",
           "CONTROL_FLOW": "control flow", "EXTRA_STATEMENT": "extra statement", "INPUT": "input",
           "STATEMENT_PLACEMENT": "statement placement", "NUMERIC_TYPE": "numeric type"},
    "vi": {"MISSING_STATEMENT": "thiếu bước xử lý", "OUTPUT_FORMAT": "đặc tả định dạng in",
           "OUTPUT_TEXT": "văn bản in ra", "LOOP_BOUNDARY": "biên vòng lặp", "COMPUTATION": "biểu thức tính",
           "BRANCH_CONDITION": "điều kiện rẽ nhánh", "INITIALIZATION": "khởi tạo",
           "CONTROL_FLOW": "luồng điều khiển", "EXTRA_STATEMENT": "thừa bước xử lý", "INPUT": "đọc dữ liệu",
           "STATEMENT_PLACEMENT": "vị trí câu lệnh", "NUMERIC_TYPE": "kiểu số"},
}


def condition_text(attribute, value, lang):
    key = f"{attribute}={value}"
    if key in ATTRIBUTE_TEXT[lang]:
        return ATTRIBUTE_TEXT[lang][key]
    escape = r"\_"
    return r"\texttt{" + attribute.replace("_", escape) + "} = " + value.replace("_", escape)


def top_rules(lang, limit=8):
    path = ROOT / "misconceptions-prototype/src/misconceptions/data/mechanism_rules.json"
    rules = json.loads(path.read_text(encoding="utf-8"))["rules"][:limit]
    rows = []
    for rule in rules:
        condition = (" and " if lang == "en" else " và ").join(
            condition_text(a, v, lang) for a, v in rule["if"].items())
        support = f"{rule['train_true_positives']}/{rule['train_true_positives'] + rule['train_false_positives']}"
        rows.append(f"{condition} & {CATEGORY_TEXT[lang][rule['then']]} & {support}" + ROW_END)
    return NEWLINE.join(rows)


def result_tokens(summary, categories, lang):
    out = {}
    for benchmark in ("real", "injected"):
        entry = summary["benchmarks"][benchmark]
        out[f"{benchmark}_cohorts"] = entry.get("cohorts")
        for rep in REP_ORDER:
            out[f"{benchmark}_ari_{rep}"] = number(entry["ari_kmeans_oracle"].get(rep), 2, lang)
            out[f"{benchmark}_arihac_{rep}"] = number(entry["ari_hac_oracle"].get(rep), 2, lang)
            out[f"{benchmark}_ceil_{rep}"] = number(entry["ceilings"].get(rep), 2, lang)
        out[f"{benchmark}_ari_exact"] = number(entry.get("exact_signature_ari"), 2, lang)
        for name, value in entry.get("hypotheses", {}).items():
            s = value.get("summary") or {}
            if not s.get("n"):
                continue
            key = f"{benchmark}_{name}"
            if name == "H1a":
                out[key + "_pct"] = number(100 * s["mean"], 1, lang)
            out[key + "_mean"] = number(s["mean"], 3 if name != "H1a" else 2, lang)
            out[key + "_lo"] = number(s["ci95"][0], 3 if name != "H1a" else 2, lang)
            out[key + "_hi"] = number(s["ci95"][1], 3 if name != "H1a" else 2, lang)
            out[key + "_wins"] = f"{s.get('wins')}/{s.get('n')}"
            if value.get("holm_p") is not None:
                out[key + "_p"] = number(value["holm_p"], 4, lang)
        for key, value in entry["rules"].items():
            flat = key.replace("|", "_")
            for metric in ("macro_f1", "coverage", "selective_accuracy", "accuracy_abstain_as_error",
                           "n_rules", "n"):
                if value.get(metric) is not None:
                    out[f"{benchmark}_{flat}_{metric}"] = (value[metric] if metric in ("n_rules", "n")
                                                            else number(value[metric], 2, lang))
        cats = categories["benchmarks"][benchmark]
        out[f"{benchmark}_same_signature_pairs"] = f"{cats['same_signature_pairs']:,}".replace(",", "." if lang == "vi" else ",")
        out[f"{benchmark}_collision_pairs"] = f"{cats['same_signature_different_mechanism_pairs']:,}".replace(",", "." if lang == "vi" else ",")
        out[f"{benchmark}_collision_pct"] = number(100 * cats["same_signature_different_mechanism_pairs"]
                                                   / cats["same_signature_pairs"], 1, lang)
        for rep, table in cats["recovered_share"].items():
            out[f"{benchmark}_catrec_{rep}"] = number(sum(table.values()) / len(table), 2, lang)
            for category, share in table.items():
                out[f"{benchmark}_rec_{rep}_{category.lower()}"] = number(share, 2, lang)
    for benchmark in ("real", "injected"):
        cats = categories["benchmarks"][benchmark]
        reps = ("exact_signature", "outcomes", "combined_stdout", "deviation", "evidence", "embedding")
        rows = []
        for category, n in cats["items_per_category"].items():
            cells = " & ".join(number(cats["recovered_share"][rep].get(category), 2, lang) for rep in reps)
            rows.append(f"{CATEGORY_TEXT[lang][category]} & {n} & {cells}" + ROW_END)
        out[f"table_categories_{benchmark}"] = NEWLINE.join(rows)
    h4 = summary["benchmarks"]["real"]["hypotheses_rules"]["H4"]["summary"]
    out.update({"h4_mean": number(h4["mean"], 3, lang), "h4_lo": number(h4["ci95"][0], 3, lang),
                "h4_hi": number(h4["ci95"][1], 3, lang), "table_top_rules": top_rules(lang)})
    return out


POLICY_NAMES = {"en": {"exact_exit0": "Exact output, exit status 0 (selected)",
                       "exact_any_exit": "Exact output, any exit status",
                       "trailing_ws_exit0": "Ignore trailing whitespace",
                       "tokens_exit0": "Whitespace-separated tokens"},
                "vi": {"exact_exit0": "Khớp chính xác, mã thoát 0 (được chọn)",
                       "exact_any_exit": "Khớp chính xác, mã thoát bất kỳ",
                       "trailing_ws_exit0": "Bỏ qua khoảng trắng cuối",
                       "tokens_exit0": "So theo token cách bởi khoảng trắng"}}


def audit_rows(lang):
    audit = load("replay-v2-20260930/oracle_audit.json")
    rows = []
    for name, policy in audit["policies"].items():
        cells = []
        for partition in ("train", "validation", "test"):
            counts = policy["agreement_by_partition"].get(partition, {})
            total = sum(counts.values())
            cells.append(number(100 * counts.get("agree", 0) / total, 2, lang) if total else "--")
        rows.append(POLICY_NAMES[lang][name] + " & " + " & ".join(cells) + ROW_END)
    return NEWLINE.join(rows)


def audit_tokens():
    """Agreement of single-category labels with the audit decisions over both samples."""
    agree = total = 0
    counts = {}
    for index, name in enumerate(("label-audit-20260930", "label-audit-v1.1-20260930"), 1):
        packet = load(f"{name}/audit_packet.json")
        decisions = load(f"{name}/audit_decisions.json")["decisions"]
        counts[f"audit{index}_cases"] = len(packet["cases"])
        counts[f"audit{index}_agree"] = sum(case["assigned_primary"] == decisions[case["case_id"]]["category"]
                                            for case in packet["cases"])
        excluded = [c for c in packet["cases"] if c["assigned_primary"] in ("MULTI", "OTHER", "NO_CHANGE")]
        counts[f"audit{index}_excluded"] = len(excluded)
        counts[f"audit{index}_excluded_wrong"] = sum(
            c["assigned_primary"] != decisions[c["case_id"]]["category"] for c in excluded)
        single = 0
        for case in packet["cases"]:
            if case["assigned_primary"] in ("MULTI", "OTHER", "NO_CHANGE"):
                continue
            single += 1
            total += 1
            agree += case["assigned_primary"] == decisions[case["case_id"]]["category"]
        counts[f"audit{index}_single"] = single
    z = 1.96
    p = agree / total
    low = (p + z * z / (2 * total) - z * (p * (1 - p) / total + z * z / (4 * total * total)) ** 0.5) \
        / (1 + z * z / total)
    return counts | {"audit_single_agree": f"{agree}/{total}", "audit_wilson_low": f"{low:.3f}"}


def tokens(lang):
    audit = load("replay-v2-20260930/oracle_audit.json")
    manifest = load("replay-v2-20260930/replay_manifest.json")
    repro = load("replay-reproducibility-20260930.json")
    stats = load("mechanism-bench-v1.1/stats.json")
    summary = load("mechanism-v1.1-test/summary.json")
    protocol = json.loads((ROOT / "research/protocol-mechanism-v1.json").read_text(encoding="utf-8"))
    policy = audit["policies"][audit["selected_policy"]]["agreement_by_partition"]
    agree = sum(c.get("agree", 0) for c in policy.values())
    cells = sum(sum(c.values()) for c in policy.values())
    compile_counts = audit["compile"]
    compile_agree = sum(v for k, v in compile_counts.items() if (
        "historical=compile_error" in k and "warning_free=False" in k) or (
        "historical=compiled_in_historical_run" in k and "warning_free=True" in k))
    compile_total = sum(compile_counts.values())
    stdout = audit["stdout_reproduction"]
    real, injected, corpus = stats["real"], stats["injected"], stats["corpus"]
    values = {
        "n_submissions": f"{corpus['submissions']:,}", "n_students": corpus["students"],
        "n_tests": corpus["tests"], "n_not_run_cells": f"{corpus['historical_not_run_cells']:,}",
        "cpu_limit": manifest["limits"]["run_cpu_seconds"], "wall_limit": manifest["limits"]["run_wall_seconds"],
        "gcc_version": manifest["compiler"].split()[-1],
        "audit_cells": f"{cells:,}", "audit_cells_pct": pct(agree / cells, 2),
        "audit_stdout_pct": pct(stdout["same"] / (stdout["same"] + stdout["different"])),
        "audit_compile_pct": pct(compile_agree / compile_total, 2),
        "repro_cells_pct": pct(repro["cell_agreement"], 2),
        "n_unstable": len(repro["outcome_differing_ids"]),
        "n_pairs": real["repair_events"], "n_real_gold": real["gold"],
        "ddmin_budget": stats["build"]["budget"], "max_sources": stats["build"]["max_sources"],
        "n_injected": f"{injected['mutants']:,}", "probes_total": f"{real['probes_total']:,}",
        "injected_candidates": f"{sum(injected['build_status'].values()):,}",
        "replay_minutes": round(manifest["elapsed_seconds"] / 60),
        "protocol_registered": protocol["registered_at_utc"].replace("T", " ").replace("Z", " UTC"),
        "real_test_cohorts": real["eligible_cohorts"]["test"],
        "relabel_changes": sum(v for k, v in stats["relabel"]["transitions"].items()
                               if k.split("->")[0] != k.split("->")[1]),
        **audit_tokens(),
        "ila_penalty": f"{load('mechanism-v1.1-test/run_manifest.json')['penalty']:.1f}",
    }
    if lang == "vi":
        values = {k: (v.replace(",", ".").replace(".", ",", 1) if isinstance(v, str)
                      and re.fullmatch(r"\d+\.\d+", v) else v.replace(",", ".") if isinstance(v, str)
                      and re.fullmatch(r"\d{1,3}(,\d{3})+", v) else v)
                  for k, v in values.items()}
    values.update(result_tokens(summary, load("mechanism-v1.1-test/categories.json"), lang))
    values["multi_share"] = number(100 * real["primary_all"].get("MULTI", 0)
                                   / sum(real["primary_all"].values()), 1, lang)
    small = sum(v for k, v in real["hunks_minimal"].items() if int(k) <= 2)
    values["real_small_repair_pct"] = number(100 * small / sum(real["hunks_minimal"].values()), 0, lang)
    values["real_ok"] = real["status"]["ok"]
    values["real_one_minimal"] = real["one_minimal"]
    status = injected["build_status"]
    values["injected_equivalent_pct"] = number(100 * status["equivalent_on_suite"] / sum(status.values()), 1, lang)
    decisions = [d for name in ("label-audit-20260930", "label-audit-v1.1-20260930")
                 for d in load(f"{name}/audit_decisions.json")["decisions"].values()]
    flow = [d for d in decisions if d["category"] == "CONTROL_FLOW"]
    values["audit_control_flow"] = len(flow)
    values["audit_control_flow_return"] = sum("return 0" in d.get("note", "") for d in flow)
    values["table_audit"] = audit_rows(lang)
    values.update({"table_ari_real": ari_rows(summary, "real", lang),
                   "table_ari_injected": ari_rows(summary, "injected", lang),
                   "table_hypotheses": hypothesis_rows(summary, lang),
                   "table_rules_real": rule_rows(summary, "real", lang),
                   "table_rules_injected": rule_rows(summary, "injected", lang)})
    extra = HERE / ("tokens_vi.json" if lang == "vi" else "tokens_en.json")
    if extra.exists():
        values.update(json.loads(extra.read_text(encoding="utf-8")))
    return values


def expand(text, folder):
    def include(match):
        return (folder / match.group(1)).read_text(encoding="utf-8")
    while re.search(r"^%%INCLUDE (\S+)$", text, flags=re.MULTILINE):
        text = re.sub(r"^%%INCLUDE (\S+)$", include, text, flags=re.MULTILINE)
    return text


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lang", choices=("en", "vi"), default="en")
    parser.add_argument("--tectonic", type=Path, default=DEFAULT_TECTONIC)
    args = parser.parse_args()
    folder = HERE if args.lang == "en" else HERE / "vi"
    template = (folder / "manuscript_template.tex").read_text(encoding="utf-8")
    text = expand(template, folder)
    values = tokens(args.lang)
    missing = sorted(set(re.findall(r"\{\{(\w+)\}\}", text)) - set(values))
    if missing:
        raise SystemExit(f"Unfilled tokens: {missing}")
    text = re.sub(r"\{\{(\w+)\}\}", lambda m: str(values[m.group(1)]), text)
    out = folder / "manuscript.tex"
    out.write_text(text, encoding="utf-8")
    if folder != HERE:
        (folder / "references.bib").write_text((HERE / "references.bib").read_text(encoding="utf-8"),
                                              encoding="utf-8")
        figures = folder / "figures"
        figures.mkdir(exist_ok=True)
        for figure in (HERE / "figures").glob("*_vi.pdf"):
            (figures / figure.name).write_bytes(figure.read_bytes())
    result = subprocess.run([str(args.tectonic), "--keep-logs", out.name], cwd=folder,
                            capture_output=True, text=True, encoding="utf-8", errors="replace")
    log_path = folder / "manuscript.log"
    log = log_path.read_text(encoding="utf-8", errors="replace") if log_path.exists() else ""
    issues = {"undefined_references": re.findall(r"Reference `([^']+)' .*undefined", log),
              "undefined_citations": re.findall(r"Citation `([^']+)' .*undefined", log),
              "missing_glyphs": re.findall(r"Missing character: There is no (.+?) in font", log)}
    pdf = folder / "manuscript.pdf"
    record = {"built": dt.datetime.now().isoformat(timespec="seconds"), "lang": args.lang,
              "exit": result.returncode, "issues": issues,
              "tex_sha256": hashlib.sha256(out.read_bytes()).hexdigest(),
              "pdf_sha256": hashlib.sha256(pdf.read_bytes()).hexdigest() if pdf.exists() else None,
              "tail": result.stderr[-1500:]}
    (folder / "build_record.json").write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n",
                                             encoding="utf-8")
    if result.returncode or any(issues.values()):
        raise SystemExit(json.dumps(record, indent=2, ensure_ascii=False))
    print(f"built {pdf}")


if __name__ == "__main__":
    main()

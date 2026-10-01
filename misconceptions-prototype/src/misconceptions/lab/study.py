"""Study summary for AAI Lab, computed from committed research artifacts only."""

import json
from pathlib import Path

import numpy as np

from ..mechanism_feedback import FEEDBACK
from .phrases import deviation_phrase

ROOT = Path(__file__).resolve().parents[4]
RUNS = ROOT / "research" / "runs"
RULES = Path(__file__).resolve().parents[1] / "data" / "mechanism_rules.json"
PAPERS = {"en": ROOT / "paper" / "manuscript.pdf", "vi": ROOT / "paper" / "vi" / "manuscript.pdf"}
REPRESENTATIONS = [
    ("outcomes", "Kết quả test (OAV của đề)"), ("outcomes_stdout", "Kết quả + stdout"),
    ("combined_stdout", "Kết hợp + stdout"), ("structural", "Cấu trúc AST"),
    ("code_cues", "Manh mối mã"), ("embedding", "Embedding mã"),
    ("deviation", "OAV độ lệch (đề xuất)"), ("evidence", "OAV bằng chứng (đề xuất)")]
HYPOTHESES = [
    ("H1a", "Chữ ký test giống nhau trộn lẫn nhiều cơ chế lỗi",
     "Trần tỷ lệ bài có thể xếp đúng chỉ từ kết quả test"),
    ("H1b", "Mô tả cách output lệch mang thêm thông tin về cơ chế",
     "Mức tăng trần so với chia ngẫu nhiên cùng độ mịn"),
    ("H2_kmeans", "Phân cụm theo độ lệch khớp cơ chế hơn phân cụm theo test",
     "Chênh lệch ARI, K-means"),
    ("H3_kmeans", "Thêm manh mối mã vượt baseline output sẵn có",
     "Chênh lệch ARI so với kết hợp + stdout"),
    ("H5", "Embedding mã gom theo chương trình gốc, không theo cơ chế",
     "ARI theo chương trình gốc trừ ARI theo cơ chế")]
SCOPE = {"real": "full", "injected": "partition"}


def vi(value, digits=2):
    return f"{value:.{digits}f}".replace(".", ",")


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def interval(values, seed=0, resamples=4000):
    values = np.asarray(values, dtype=float)
    rng = np.random.default_rng(seed)
    means = rng.choice(values, size=(resamples, len(values)), replace=True).mean(axis=1)
    return [float(values.mean()), float(np.quantile(means, 0.025)), float(np.quantile(means, 0.975))]


def ari_rows(results, benchmark):
    cohorts = results["benchmarks"][benchmark]["scopes"][SCOPE[benchmark]]["cohorts"]
    rows = []
    for key, name in REPRESENTATIONS:
        values = [c["reps"][key]["kmeans_oracle"]["ari"] for c in cohorts
                  if key in c["reps"] and "kmeans_oracle" in c["reps"][key]]
        if values:
            mean, low, high = interval(values)
            rows.append({"key": key, "name": name, "mean": mean, "low": low, "high": high,
                         "proposed": key in ("deviation", "evidence")})
    return {"rows": rows, "cohorts": len(cohorts)}


CONDITIONS = {
    ("code:output_calls", "0"): "chương trình không có lệnh in nào",
    ("code:input_calls", "0"): "chương trình không có lệnh đọc dữ liệu",
    ("code:loop_starts_nonzero", "1"): "có vòng lặp bắt đầu từ giá trị khác 0",
    ("code:modulo", "1"): "có phép chia lấy dư",
    ("code:init_zero", "1"): "có biến khởi tạo bằng 0",
    ("agg:newline_end", "same"): "xuống dòng ở cuối đúng như đáp án",
    ("agg:numbers", "none"): "không có số nào in sai",
    ("agg:fail_fraction", "some"): "trượt dưới một nửa số test",
    ("agg:fail_fraction", "most"): "trượt từ một nửa số test trở lên",
    ("agg:fail_fraction", "all"): "trượt mọi test",
}


def rule_text(rule):
    parts = []
    for attribute, value in rule["if"].items():
        phrase = CONDITIONS.get((attribute, value))
        if phrase is None and attribute == "code:output_calls":
            phrase = f"chương trình có {value} lệnh in"
        if phrase is None and attribute.startswith("agg:"):
            found = deviation_phrase(attribute[4:], value)
            phrase = found[0].lower() + found[1:] if found else None
        parts.append(phrase or f"{attribute} = {value}")
    return parts


def summary():
    stats = load(RUNS / "mechanism-bench-v1.1" / "stats.json")
    audit = load(RUNS / "replay-v2-20260930" / "oracle_audit.json")
    reproducibility = load(RUNS / "replay-reproducibility-20260930.json")
    test = load(RUNS / "mechanism-v1.1-test" / "summary.json")
    results = load(RUNS / "mechanism-v1.1-test" / "results.json")
    categories = load(RUNS / "mechanism-v1.1-test" / "categories.json")
    policy = audit["policies"][audit["selected_policy"]]["agreement_by_partition"]
    agree = sum(c.get("agree", 0) for c in policy.values())
    cells = sum(sum(c.values()) for c in policy.values())
    audits = [load(RUNS / name / "audit_decisions.json") for name in
              ("label-audit-20260930", "label-audit-v1.1-20260930")]
    packets = [load(RUNS / name / "audit_packet.json") for name in
               ("label-audit-20260930", "label-audit-v1.1-20260930")]
    single = [(c["assigned_primary"], a["decisions"][c["case_id"]]["category"])
              for p, a in zip(packets, audits) for c in p["cases"]
              if c["assigned_primary"] not in ("MULTI", "OTHER", "NO_CHANGE")]
    hypotheses = []
    for key, statement, measure in HYPOTHESES:
        entry = {"id": key.split("_")[0], "statement": statement, "measure": measure}
        for benchmark in ("real", "injected"):
            value = test["benchmarks"][benchmark].get("hypotheses", {}).get(key)
            if value and value["summary"] and value["summary"].get("n"):
                s = value["summary"]
                entry[benchmark] = {"mean": s["mean"], "low": s["ci95"][0], "high": s["ci95"][1],
                                    "supported": value["verdict"] == "supported"}
        hypotheses.append(entry)
    h4 = test["benchmarks"]["real"]["hypotheses_rules"]["H4"]["summary"]
    hypotheses.insert(4, {"id": "H4", "statement": "Luật ILA-2 trên bằng chứng dự đoán cơ chế tốt hơn luật chỉ dùng kết quả test",
                          "measure": "Chênh lệch macro-F1 trên sinh viên chưa thấy",
                          "real": {"mean": h4["mean"], "low": h4["ci95"][0], "high": h4["ci95"][1],
                                   "supported": h4["ci95"][0] > 0}})
    rules = load(RULES)
    real_rules = test["benchmarks"]["real"]["rules"]
    injected_rules = test["benchmarks"]["injected"]["rules"]
    return {
        "question": "Gom bài sai theo test bị trượt có gom đúng theo cơ chế lỗi không?",
        "answer": "Chưa đủ: bài cùng chữ ký test thường sai vì những lý do khác nhau. "
                  "Mô tả cách output lệch khôi phục được nhiều hơn, rõ nhất trên dữ liệu có kiểm soát.",
        "data": [
            {"value": stats["corpus"]["submissions"], "label": "bài C chạy lại trong môi trường cách ly",
             "detail": f"khớp {vi(100 * agree / cells)}% verdict của hệ thống chấm cũ; "
                       f"lần chạy lại thứ hai khớp {vi(100 * reproducibility['cell_agreement'])}%"},
            {"value": stats["real"]["gold"], "label": "nhãn cơ chế từ bản sửa của chính sinh viên",
             "detail": f"{stats['real']['repair_events']} lần sửa được thu gọn bằng delta debugging; "
                       f"audit {sum(a == b for a, b in single)}/{len(single)} nhãn khớp"},
            {"value": stats["injected"]["mutants"], "label": "bài tiêm đúng một lỗi biết trước",
             "detail": f"{len(stats['injected']['labels'])} loại cơ chế, từ "
                       f"{stats['injected']['sources']} bài đã đạt"}],
        "collisions": {b: 100 * categories["benchmarks"][b]["same_signature_different_mechanism_pairs"]
                       / categories["benchmarks"][b]["same_signature_pairs"] for b in ("real", "injected")},
        "hypotheses": hypotheses,
        "ari": {"real": ari_rows(results, "real"), "injected": ari_rows(results, "injected")},
        "rules": [{"if": rule_text(r), "then": FEEDBACK.get(r["then"], {}).get("name", r["then"]),
                   "support": r["train_true_positives"],
                   "matched": r["train_true_positives"] + r["train_false_positives"]}
                  for r in sorted(rules["rules"], key=lambda r: -r["train_true_positives"])],
        "rule_quality": {
            "real_seen": real_rules["seen_problems|evidence|ila2"]["macro_f1"],
            "injected_seen": injected_rules["seen_problems|evidence|ila2"]["macro_f1"],
            "injected_unseen": injected_rules["unseen_problems|evidence|ila2"]["macro_f1"],
            "injected_outcome_only": injected_rules["seen_problems|outcome_summary|ila2"]["macro_f1"]},
        "limits": [
            "Nhãn mô tả thay đổi trong chương trình, không phải niềm tin của sinh viên.",
            "Audit nhãn do AI thực hiện; cần hai người chấm độc lập trước khi nộp.",
            "Một khóa học, một chuẩn C90, chấm theo output khớp chính xác."],
        "papers": {lang: path.exists() for lang, path in PAPERS.items()}}

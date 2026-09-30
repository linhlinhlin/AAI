"""Figures for the topic-5 manuscript, built from committed artifacts (no hand-typed numbers).

Every figure is drawn at its printed width (the elsarticle preprint text width, 390 pt) with
6.5-8.5 pt Arial embedded as TrueType, and saved without cropping, so LaTeX never rescales
it. One indigo marks the proposed representations and grey the baselines; the palette was
checked for colour-vision deficiency, and every mark also carries a text label. Diagram
text is checked to fit its box before a file is written.

Run with a Python that has matplotlib:  python paper/make_figures.py --lang en|vi [--png]
"""

import argparse
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Rectangle
from matplotlib.ticker import FuncFormatter

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RUNS = ROOT / "research/runs"
WIDTH = 390 / 72.27  # elsarticle preprint \textwidth in inches
INK, INK2, INK3 = "#1F2430", "#5B6272", "#8A909C"
GRID, LINE, PANEL = "#E6E8EE", "#C9CED8", "#F4F5F8"
INDIGO, INDIGO_SOFT, INDIGO_INK = "#3F51B5", "#E8EAF6", "#2C3A8C"
ORANGE, TEAL = "#D98324", "#2E9E83"
FAIL, FAIL_SOFT, PASS_SOFT = "#C8453C", "#FBE9E7", "#E3F3EC"
SCOPE = {"real": "full", "injected": "partition"}
ORDER = ["outcomes", "outcomes_stdout", "combined_stdout", "structural", "code_cues", "embedding",
         "deviation", "evidence"]
PROPOSED = {"deviation", "evidence"}
CATEGORIES = ["OUTPUT_TEXT", "COMPUTATION", "MISSING_STATEMENT", "BRANCH_CONDITION", "LOOP_BOUNDARY",
              "OUTPUT_FORMAT", "CONTROL_FLOW", "EXTRA_STATEMENT", "INITIALIZATION", "INPUT",
              "STATEMENT_PLACEMENT", "NUMERIC_TYPE"]

TEXT = {
    "en": {
        "reps": {"outcomes": "Test outcomes (classic OAV)", "outcomes_stdout": "Outcomes + stdout",
                 "combined_stdout": "Combined + stdout", "structural": "AST presence",
                 "code_cues": "Code cues", "embedding": "Code embedding",
                 "deviation": "Deviation OAV (ours)", "evidence": "Evidence OAV (ours)"},
        "short": {"outcomes": "Test outcomes", "combined_stdout": "Combined + stdout",
                  "deviation": "Deviation OAV", "evidence": "Evidence OAV"},
        "cats": {"OUTPUT_TEXT": "Output text", "COMPUTATION": "Computation",
                 "MISSING_STATEMENT": "Missing statement", "BRANCH_CONDITION": "Branch condition",
                 "LOOP_BOUNDARY": "Loop boundary", "OUTPUT_FORMAT": "Output format",
                 "CONTROL_FLOW": "Control flow", "EXTRA_STATEMENT": "Extra statement",
                 "INITIALIZATION": "Initialisation", "INPUT": "Input",
                 "STATEMENT_PLACEMENT": "Statement placement", "NUMERIC_TYPE": "Numeric type"},
        "real": "Real student repairs", "injected": "Injected mutants",
        "real_scope": "21 full assignment cohorts", "injected_scope": "20 sealed test cohorts",
        "ari_axis": "Adjusted Rand index with the mechanism labels (K-means, oracle k)",
        "ceiling_axis": "Identifiability ceiling: largest share of items any function of the representation places correctly",
        "ceil_rows": ["Test-outcome OAV", "Random refinement", "Deviation OAV (ours)"],
        "fig1_task": "C-Pack-IPAs lab02-ex09: print a duration given in seconds as hh:mm:ss",
        "fig1_note": "Input 60, expected output 00:01:00\\n. {same} of the {total} failing submissions fail all four tests.",
        "fig1_head": [["Mechanism of the", "minimal repair"], ["Verified minimal repair", "− failing   + repaired"],
                      ["Tests", "1–4"], ["Printed", "(input 60)"], ["Deviation OAV", "(aggregated)"]],
        "fig1_same": "identical", "fig1_diff": "all different",
        "heat_axis": "Share of items whose K-means cluster has their mechanism as majority label",
        "rule_axis": "Macro-F1 on held-out students (bars: 95% bootstrap interval)",
        "rule_tracks": {"real|seen_problems": "Real repairs, seen tasks",
                        "injected|seen_problems": "Injected, seen tasks",
                        "injected|unseen_problems": "Injected, unseen tasks"},
        "rule_models": {"evidence|ila2": "ILA-2, evidence", "evidence|ila": "ILA, evidence",
                        "evidence|cart": "CART tree, evidence", "outcome_summary|ila2": "ILA-2, outcome summary",
                        "majority": "Majority class"},
    },
    "vi": {
        "reps": {"outcomes": "Kết quả test (OAV kinh điển)", "outcomes_stdout": "Kết quả + stdout",
                 "combined_stdout": "Kết hợp + stdout", "structural": "Hiện diện AST",
                 "code_cues": "Manh mối mã", "embedding": "Embedding mã",
                 "deviation": "OAV độ lệch (đề xuất)", "evidence": "OAV bằng chứng (đề xuất)"},
        "short": {"outcomes": "Kết quả test", "combined_stdout": "Kết hợp + stdout",
                  "deviation": "OAV độ lệch", "evidence": "OAV bằng chứng"},
        "cats": {"OUTPUT_TEXT": "Nội dung in ra", "COMPUTATION": "Biểu thức tính toán",
                 "MISSING_STATEMENT": "Thiếu câu lệnh", "BRANCH_CONDITION": "Điều kiện rẽ nhánh",
                 "LOOP_BOUNDARY": "Biên vòng lặp", "OUTPUT_FORMAT": "Định dạng in",
                 "CONTROL_FLOW": "Luồng điều khiển", "EXTRA_STATEMENT": "Thừa câu lệnh",
                 "INITIALIZATION": "Khởi tạo", "INPUT": "Đọc dữ liệu",
                 "STATEMENT_PLACEMENT": "Vị trí câu lệnh", "NUMERIC_TYPE": "Kiểu số"},
        "real": "Bản sửa thật của sinh viên", "injected": "Đột biến tiêm lỗi",
        "real_scope": "21 cohort đầy đủ theo bài", "injected_scope": "20 cohort test niêm phong",
        "ari_axis": "ARI giữa cụm và nhãn cơ chế (K-means, k theo nhãn)",
        "ceiling_axis": "Trần khả phân biệt: tỷ lệ bài lớn nhất mà mọi hàm của biểu diễn có thể xếp đúng",
        "ceil_rows": ["OAV kết quả test", "Chia ngẫu nhiên", "OAV độ lệch (đề xuất)"],
        "fig1_task": "C-Pack-IPAs lab02-ex09: in thời lượng (giây) dưới dạng hh:mm:ss",
        "fig1_note": "Input 60, đáp án 00:01:00\\n. {same}/{total} bài sai của bài tập này trượt cả bốn test.",
        "fig1_head": [["Loại của bản", "sửa tối thiểu"], ["Bản sửa tối thiểu đã kiểm chứng", "− bài sai   + bài đã sửa"],
                      ["Test", "1–4"], ["In ra", "(input 60)"], ["OAV độ lệch", "(tổng hợp)"]],
        "fig1_same": "giống hệt", "fig1_diff": "khác nhau",
        "heat_axis": "Tỷ lệ bài có cụm K-means mang đúng cơ chế của nó làm nhãn đa số",
        "rule_axis": "Macro-F1 trên sinh viên chưa thấy (thanh: khoảng bootstrap 95%)",
        "rule_tracks": {"real|seen_problems": "Sửa thật, bài đã thấy",
                        "injected|seen_problems": "Tiêm lỗi, bài đã thấy",
                        "injected|unseen_problems": "Tiêm lỗi, bài chưa thấy"},
        "rule_models": {"evidence|ila2": "ILA-2, bằng chứng", "evidence|ila": "ILA, bằng chứng",
                        "evidence|cart": "Cây CART, bằng chứng", "outcome_summary|ila2": "ILA-2, tóm tắt kết quả",
                        "majority": "Lớp đa số"},
    },
}


def load(path):
    return json.loads((RUNS / path).read_text(encoding="utf-8"))


def num(value, lang, digits=2):
    text = f"{value:.{digits}f}".replace("-", "−")
    return text.replace(".", ",") if lang == "vi" else text


def count(value, lang):
    text = f"{value:,}"
    return text.replace(",", ".") if lang == "vi" else text


def setup():
    plt.rcParams.update({
        "font.family": ["Arial", "DejaVu Sans"], "font.size": 7.5, "axes.titlesize": 8,
        "axes.labelsize": 7.6, "xtick.labelsize": 7.4, "ytick.labelsize": 7.8, "legend.fontsize": 7.4,
        "axes.spines.top": False, "axes.spines.right": False, "axes.linewidth": 0.6,
        "axes.edgecolor": INK3, "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK,
        "xtick.major.width": 0.6, "xtick.major.size": 2.5, "ytick.major.size": 0, "ytick.major.pad": 4,
        "text.color": INK, "pdf.fonttype": 42, "svg.fonttype": "none", "figure.dpi": 100,
    })


def mean_ci(values, seed=0, resamples=10000):
    values = np.asarray(values, dtype=float)
    rng = np.random.default_rng(seed)
    means = rng.choice(values, size=(resamples, len(values)), replace=True).mean(axis=1)
    return float(values.mean()), float(np.quantile(means, 0.025)), float(np.quantile(means, 0.975))


def cohorts(report, benchmark):
    return report["benchmarks"][benchmark]["scopes"][SCOPE[benchmark]]["cohorts"]


def save(fig, path, png=False):
    fig.savefig(path, facecolor="white")
    if png:
        fig.savefig(path.with_suffix(".png"), dpi=220, facecolor="white")
    plt.close(fig)


def fit_left(fig, ax, right=0.955, top=None, bottom=None, pad=0.08):
    """Set the left margin to the widest y tick label so the figure keeps its printed width."""
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    widest = max((t.get_window_extent(renderer).width for t in ax.get_yticklabels() if t.get_text()), default=0)
    left = (widest / fig.dpi + pad) / fig.get_figwidth()
    fig.subplots_adjust(left=left, right=right, **({"top": top} if top else {}), **({"bottom": bottom} if bottom else {}))
    return left


class Canvas:
    """A full-figure axis in inches (y grows downward) that checks text fits its box."""

    def __init__(self, height, width=WIDTH):
        self.width, self.height = width, height
        self.fig = plt.figure(figsize=(width, height))
        self.ax = self.fig.add_axes([0, 0, 1, 1])
        self.ax.set_xlim(0, width)
        self.ax.set_ylim(height, 0)
        self.ax.axis("off")
        self.fitted = []
        self.free = []

    def text(self, x, y, s, **kw):
        kw.setdefault("va", "top")
        kw.setdefault("ha", "left")
        kw.setdefault("fontsize", 7.2)
        kw.setdefault("color", INK)
        artist = self.ax.text(x, y, s, **kw)
        self.free.append(artist)
        return artist

    def box(self, x, y, w, h, face="white", edge=LINE, lw=0.8, radius=0.05):
        patch = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={radius}",
                               facecolor=face, edgecolor=edge, linewidth=lw)
        self.ax.add_patch(patch)
        return patch

    def boxed(self, x, y, w, h, lines, face="white", edge=LINE, title_color=INK, size=6.9, title_size=7.3,
              body_color=INK2):
        """A box with a bold first line; each line is checked to fit inside at export."""
        patch = self.box(x, y, w, h, face=face, edge=edge)
        step = size * 1.34 / 72
        top = y + h / 2 - (len(lines) - 1) * step / 2
        for i, line in enumerate(lines):
            artist = self.ax.text(x + w / 2, top + i * step, line, ha="center", va="center",
                                  fontsize=title_size if i == 0 else size, fontweight="bold" if i == 0 else "normal",
                                  color=title_color if i == 0 else body_color)
            self.fitted.append((artist, patch))
        return patch

    def arrow(self, x0, y0, x1, y1, color=INK3, lw=0.8):
        self.ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=6.5, color=color,
                                          linewidth=lw, shrinkA=0, shrinkB=0))

    def save(self, path, png=False):
        self.fig.canvas.draw()
        renderer = self.fig.canvas.get_renderer()
        frame = self.ax.get_window_extent(renderer)
        for artist, patch in self.fitted:
            outer, inner = patch.get_window_extent(renderer), artist.get_window_extent(renderer)
            assert outer.x0 + 2 <= inner.x0 and inner.x1 <= outer.x1 - 2, \
                f"{path.name}: text wider than its box: {artist.get_text()!r}"
            assert outer.y0 + 1 <= inner.y0 and inner.y1 <= outer.y1 - 1, \
                f"{path.name}: text taller than its box: {artist.get_text()!r}"
        for artist in self.free:
            inner = artist.get_window_extent(renderer)
            assert frame.x0 - 0.5 <= inner.x0 and inner.x1 <= frame.x1 + 0.5, \
                f"{path.name}: text leaves the figure: {artist.get_text()!r}"
        save(self.fig, path, png)


def wrap(text, limit):
    words, lines = text.split(), [""]
    for word in words:
        if lines[-1] and len(lines[-1]) + 1 + len(word) > limit:
            lines.append(word)
        else:
            lines[-1] = f"{lines[-1]} {word}".strip()
    return lines


# ---------------------------------------------------------------- Figure 1: motivating example

def short_code(line, limit=38):
    """Keep the format string of a long printf and elide its arguments."""
    if len(line) <= limit or not line.startswith("printf("):
        return line
    first = line.index('"')
    return line[:line.index('"', first + 1) + 1] + ", …);"


CHIPS = {"OUTPUT_TEXT": ["newline_end = missing", "whitespace_only = yes"],
         "OUTPUT_FORMAT": ["numbers = format_only"], "COMPUTATION": ["numbers = mixed"]}


def figure_example(lang, path, png):
    text = TEXT[lang]
    data = json.loads((HERE / "data" / "motivating_example.json").read_text(encoding="utf-8"))
    cols = [0.0, 1.06, 3.12, 3.72, 4.3]
    rows_h = [0.18 * 2 * max(len(i["removed"]), len(i["added"])) + 0.14 for i in data["items"]]
    top = 0.86
    height = top + sum(rows_h) + 0.24
    canvas = Canvas(height)
    canvas.text(0, 0.02, text["fig1_task"], fontsize=7.6, fontweight="bold")
    canvas.text(0, 0.21, text["fig1_note"].format(same=data["same_signature_failing"], total=data["cohort_failing"]),
                fontsize=7, color=INK2)
    for x, (first, second) in zip(cols, text["fig1_head"]):
        canvas.text(x, 0.48, first, fontsize=6.8, color=INK2, fontweight="bold")
        canvas.text(x, 0.62, second, fontsize=6.8, color=INK3)
    canvas.ax.plot([0, WIDTH], [top - 0.07, top - 0.07], color=LINE, linewidth=0.6)
    y = top
    for n, (item, h) in enumerate(zip(data["items"], rows_h)):
        mid = y + (h - 0.14) / 2
        name = wrap(text["cats"][item["label"]], 15)
        canvas.text(cols[0], y + 0.02, f"({'abc'[n]}) {name[0]}", fontsize=7.4, fontweight="bold")
        for extra, line in enumerate(name[1:], start=1):
            canvas.text(cols[0] + 0.2, y + 0.02 + extra * 0.14, line, fontsize=7.4, fontweight="bold")
        line_y = y
        for removed, added in zip(item["removed"], item["added"]):
            for sign, code, face, color in (("−", removed, FAIL_SOFT, FAIL), ("+", added, PASS_SOFT, TEAL)):
                canvas.ax.add_patch(Rectangle((cols[1], line_y), 1.98, 0.165, facecolor=face, edgecolor="none"))
                canvas.text(cols[1] + 0.05, line_y + 0.083, sign, va="center", fontsize=7, color=color, fontweight="bold")
                canvas.text(cols[1] + 0.17, line_y + 0.083, short_code(code), va="center", fontsize=6.4,
                            family="Consolas", color=INK)
                line_y += 0.18
        for k, outcome in enumerate(item["signature"]):
            x0 = cols[2] + k * 0.13
            canvas.ax.add_patch(Rectangle((x0, mid - 0.052), 0.104, 0.104, facecolor=FAIL if outcome != "pass" else TEAL,
                                          edgecolor="none"))
            canvas.ax.plot([x0 + 0.028, x0 + 0.076], [mid - 0.024, mid + 0.024], color="white", linewidth=0.9)
            canvas.ax.plot([x0 + 0.028, x0 + 0.076], [mid + 0.024, mid - 0.024], color="white", linewidth=0.9)
        canvas.text(cols[3], mid, item["printed"].replace("\n", "\\n"), va="center", fontsize=6.5, family="Consolas",
                    color=FAIL)
        chips = CHIPS[item["label"]]
        for m, chip in enumerate(chips):
            attribute, value = [part.strip() for part in chip.split("=")]
            assert item["deviation"][f"agg:{attribute}"] == value, chip  # chips repeat exported OAV values
            cy = mid - (len(chips) - 1) * 0.095 + m * 0.19
            patch = canvas.box(cols[4], cy - 0.075, 1.08, 0.15, face=INDIGO_SOFT, edge="none", radius=0.03)
            artist = canvas.ax.text(cols[4] + 0.06, cy, chip, va="center", fontsize=6.1, family="Consolas",
                                    color=INDIGO_INK)
            canvas.fitted.append((artist, patch))
        y += h
        canvas.ax.plot([0, WIDTH], [y - 0.06, y - 0.06], color=GRID, linewidth=0.6)
    canvas.text(cols[2], y + 0.0, text["fig1_same"], fontsize=6.9, color=INK2, fontweight="bold")
    canvas.text(cols[4], y + 0.0, text["fig1_diff"], fontsize=6.9, color=INDIGO, fontweight="bold")
    canvas.save(path, png)


# ---------------------------------------------------------------- Figure 2: overview

def figure_overview(lang, path, png, stats, audit_pct):
    en = lang == "en"
    real, inj, corpus = stats["real"], stats["injected"], stats["corpus"]
    c = lambda v: count(v, lang)
    canvas = Canvas(3.5)
    lanes = [("A", "Evaluation labels: built from executed evidence, never used as features" if en else
              "Nhãn đánh giá: dựng từ bằng chứng thực thi, không dùng làm đặc trưng", 0.0),
             ("B", "Representations of a failing program: available before any repair" if en else
              "Biểu diễn một bài sai: có sẵn trước mọi bản sửa", 1.5)]
    for letter, title, y in lanes:
        canvas.text(0, y, f"{letter}   {title}", fontsize=7.8, fontweight="bold")
    w, gap = 1.23, 0.1467
    xs = [i * (w + gap) for i in range(4)]
    row1 = ([["C-Pack-IPAs", f"{c(corpus['submissions'])} C90 programs", f"{corpus['students']} students, 25 tasks"],
             ["Isolated replay", f"{audit_pct}% agreement", "with the course grader"],
             ["Student's own repair", "delta debugging", f"{c(real['status']['ok'])} minimal diffs"],
             ["Classifier", "12 mechanisms", f"{c(real['gold'])} single labels"]] if en else
            [["C-Pack-IPAs", f"{c(corpus['submissions'])} bài C90", f"{corpus['students']} SV, 25 bài"],
             ["Chạy lại cách ly", f"khớp {audit_pct}%", "với hệ chấm của khóa"],
             ["Bản sửa của SV", "delta debugging", f"{c(real['status']['ok'])} diff tối thiểu"],
             ["Bộ phân loại", "12 cơ chế", f"{c(real['gold'])} nhãn đơn cơ chế"]])
    for x, lines in zip(xs, row1):
        canvas.boxed(x, 0.22, w, 0.56, lines)
    for i in range(3):
        canvas.arrow(xs[i] + w + 0.015, 0.5, xs[i + 1] - 0.015, 0.5)
    row1b = ([["Accepted programs", f"{c(inj['sources'])} warning-free"],
              ["Single-edit mutants", f"{c(inj['mutants'])} labels, {len(inj['labels'])} kinds"]] if en else
             [["Bài đã đạt", f"{c(inj['sources'])} bài sạch cảnh báo"],
              ["Đột biến một chỗ", f"{c(inj['mutants'])} nhãn, {len(inj['labels'])} loại"]])
    for x, lines in zip((xs[2], xs[3]), row1b):
        canvas.boxed(x, 0.9, w, 0.42, lines)
    canvas.arrow(xs[2] + w + 0.015, 1.11, xs[3] - 0.015, 1.11)
    canvas.ax.plot([xs[0] + w / 2, xs[0] + w / 2, xs[2] - 0.1], [0.8, 1.11, 1.11], color=INK3, linewidth=0.8)
    canvas.arrow(xs[2] - 0.1, 1.11, xs[2] - 0.015, 1.11)
    row2 = ([(["Outcome OAV", "pass / fail per test"], False), (["Deviation OAV (ours)", "how each output deviates"], True),
             (["Code cues", "18 static checks"], False), (["Code embedding", "Qwen3-Embedding-0.6B"], False)] if en else
            [(["OAV kết quả", "đạt / trượt từng test"], False), (["OAV độ lệch (đề xuất)", "output lệch thế nào"], True),
             (["Manh mối mã", "18 kiểm tra tĩnh"], False), (["Embedding mã", "Qwen3-Embedding-0.6B"], False)])
    for x, (lines, ours) in zip(xs, row2):
        canvas.boxed(x, 1.72, w, 0.44, lines, face=INDIGO_SOFT if ours else "white", edge=INDIGO if ours else LINE,
                     title_color=INDIGO_INK if ours else INK)
    row3 = ([["RQ1 Signatures", "identifiability ceiling"], ["RQ2 Clustering", "K-means, HAC: ARI"],
             ["RQ3 IF–THEN rules", "ILA, ILA-2 vs. CART"], ["RQ4 Embeddings", "origin or mechanism?"]] if en else
            [["RQ1 Chữ ký test", "trần khả phân biệt"], ["RQ2 Phân cụm", "K-means, HAC: ARI"],
             ["RQ3 Luật NẾU–THÌ", "ILA, ILA-2 so với CART"], ["RQ4 Embedding", "nguồn gốc hay cơ chế?"]])
    bus = 2.33
    for x in xs:
        canvas.ax.plot([x + w / 2, x + w / 2], [2.18, bus], color=INK3, linewidth=0.8)
    canvas.ax.plot([xs[0] + w / 2, xs[-1] + w / 2], [bus, bus], color=INK3, linewidth=0.8)
    for x, lines in zip(xs, row3):
        canvas.boxed(x, 2.5, w, 0.44, lines)
        canvas.arrow(x + w / 2, bus, x + w / 2, 2.48)
    canvas.box(0, 3.08, WIDTH, 0.4, face=PANEL, edge="none", radius=0.04)
    note = ("Instructor tool (AAI Lab, Fig. 8): groups with shared evidence, one ILA-2 rule per group, and a "
            "mechanism hypothesis only when a rule covers at least half of the group.") if en else \
           ("Công cụ cho giảng viên (AAI Lab, Hình 8): nhóm lỗi kèm bằng chứng chung, một luật ILA-2 mỗi nhóm, "
            "chỉ nêu giả thuyết cơ chế khi một luật khớp ít nhất nửa nhóm.")
    for k, line in enumerate(wrap(note, 118)):
        canvas.text(0.1, 3.16 + k * 0.13, line, fontsize=6.9, color=INK2)
    canvas.save(path, png)


# ---------------------------------------------------------------- Figure 3: benchmark flow

def figure_flow(lang, path, png, stats, build):
    en = lang == "en"
    real, inj, corpus = stats["real"], stats["injected"], stats["corpus"]
    c = lambda v: count(v, lang)
    parts, ip = real["gold_by_partition"], inj["by_partition"]
    status = build["summary"]["injected"]["status"]
    candidates = sum(status.values())
    multi, other = real["primary_all"]["MULTI"], real["primary_all"].get("OTHER", 0)
    compile_issues = status["compile_warning"] + status.get("compile_error", 0)
    bad = real["repair_events"] - real["status"]["ok"]
    left = [
        ([f"{c(corpus['submissions'])} programs replayed", "isolated runner", "oracles kept on the host"] if en else
         [f"Chạy lại {c(corpus['submissions'])} bài", "runner cách ly", "đáp án giữ ở host"], None),
        ([f"{c(real['repair_events'])} repair events", "failing submission →", "same student's next pass"] if en else
         [f"{c(real['repair_events'])} lần sửa", "bài sai → lần đạt", "kế tiếp của cùng SV"],
         [f"Excluded {bad}", f"{real['status'].get('endpoint_check_failed', 0)} endpoints failed",
          f"{real['status'].get('no_line_difference', 0)} identical pair"] if en else
         [f"Loại {bad}", f"{real['status'].get('endpoint_check_failed', 0)} không tái lập",
          f"{real['status'].get('no_line_difference', 0)} không khác dòng"]),
        ([f"{c(real['status']['ok'])} verified pairs", "delta debugging", f"{c(real['probes_total'])} program runs"] if en else
         [f"{c(real['status']['ok'])} cặp đã xác minh", "delta debugging", f"{c(real['probes_total'])} lần chạy"],
         [f"Excluded {multi + other}", f"{c(multi)} multi-category", f"{other} other category"] if en else
         [f"Loại {multi + other}", f"{c(multi)} nhiều loại", f"{other} loại khác"]),
        ([f"{c(real['gold'])} gold labels", "one mechanism each",
          f"{parts['train']} / {parts['validation']} / {parts['test']} train / val / test"] if en else
         [f"{c(real['gold'])} nhãn chuẩn, một cơ chế", f"{parts['train']} / {parts['validation']} / {parts['test']}",
          "huấn luyện / kiểm định / test"], None),
    ]
    right = [
        ([f"{c(inj['sources'])} accepted programs", "warning-free", "≤ 40 per task"] if en else
         [f"{c(inj['sources'])} bài đã đạt", "sạch cảnh báo", "≤ 40 bài mỗi bài tập"], None),
        ([f"{c(candidates)} candidate mutants", f"{len(inj['operators'])} operators", "one site per category"] if en else
         [f"{c(candidates)} đột biến ứng viên", f"{len(inj['operators'])} toán tử", "mỗi loại một vị trí"],
         [f"Excluded {c(candidates - status['kept'])}", f"{c(status['equivalent_on_suite'])} pass every test",
          f"{c(compile_issues)} compiler issues"] if en else
         [f"Loại {c(candidates - status['kept'])}", f"{c(status['equivalent_on_suite'])} đạt mọi test",
          f"{c(compile_issues)} lỗi biên dịch"]),
        ([f"{c(inj['mutants'])} gold labels", f"{len(inj['labels'])} mechanisms",
          f"{c(ip['train'])} / {ip['validation']} / {ip['test']} train / val / test"] if en else
         [f"{c(inj['mutants'])} nhãn chuẩn, {len(inj['labels'])} cơ chế",
          f"{c(ip['train'])} / {ip['validation']} / {ip['test']}", "huấn luyện / kiểm định / test"], None),
    ]
    main_w, ex_x, ex_w, step = 1.58, 1.7, 0.96, 0.8
    canvas = Canvas(0.24 + step * 3 + 0.52)
    for x0, title in ((0.0, "A   " + TEXT[lang]["real"]), (WIDTH / 2 + 0.03, "B   " + TEXT[lang]["injected"])):
        canvas.text(x0, 0.0, title, fontsize=7.8, fontweight="bold")
    for x0, steps in ((0.0, left), (WIDTH / 2 + 0.03, right)):
        y = 0.24
        for n, (lines, excluded) in enumerate(steps):
            last = n == len(steps) - 1
            canvas.boxed(x0, y, main_w, 0.5, lines, face=INDIGO_SOFT if last else "white", edge=INDIGO if last else LINE,
                         title_color=INDIGO_INK if last else INK)
            if not last:
                canvas.arrow(x0 + main_w / 2, y + 0.51, x0 + main_w / 2, y + step - 0.01)
                if excluded:
                    gap = y + 0.5 + (step - 0.5) / 2
                    canvas.boxed(x0 + ex_x - 0.08, gap - 0.23, ex_w - 0.04, 0.46, excluded, face=PANEL, edge="none",
                                 title_color=INK2, size=6.5, title_size=6.8)
                    canvas.ax.plot([x0 + main_w / 2, x0 + ex_x - 0.08], [gap, gap], color=INK3, linewidth=0.7)
            y += step
    canvas.save(path, png)


# ---------------------------------------------------------------- Figures 4, 5, 7: dot plots

def dot_row(ax, y, mean, low, high, color, lang, filled=True, bold=False):
    ax.plot([low, high], [y, y], color=color, linewidth=1.6, solid_capstyle="round", zorder=2)
    ax.plot(mean, y, "o", markersize=4.4, markerfacecolor=color if filled else "white", markeredgecolor=color,
            markeredgewidth=1.1, zorder=3)
    ax.annotate(num(mean, lang), (high, y), xytext=(3.5, 0), textcoords="offset points", va="center",
                fontsize=7.2, color=INK if bold else INK2, fontweight="bold" if bold else "normal",
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 0.6}, zorder=4)


def style_axis(ax, lang, zero=None, digits=1):
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: num(v, lang, digits)))
    ax.grid(axis="x", color=GRID, linewidth=0.6)
    ax.set_axisbelow(True)
    ax.spines["left"].set_visible(False)
    if zero is not None:
        ax.axvline(zero, color=INK3, linewidth=0.7, zorder=1)


def panel_title(ax, letter, title, fig_left, subtitle=None):
    x = -fig_left_offset(ax, fig_left)
    ax.text(x, 1.12 if subtitle else 1.04, f"{letter}   {title}", transform=ax.transAxes, ha="left",
            va="bottom", fontsize=8.3, fontweight="bold", color=INK)
    if subtitle:
        ax.text(x, 1.03, subtitle, transform=ax.transAxes, ha="left", va="bottom", fontsize=7.2, color=INK3)


def fig_left_offset(ax, fig_left):
    box = ax.get_position()
    return (box.x0 - fig_left) / box.width


def figure_ceiling(report, lang, path, png):
    text = TEXT[lang]
    fig, axes = plt.subplots(1, 2, figsize=(WIDTH, 1.55), sharey=True)
    rows = [("outcomes", "ceiling", INK3, True), ("deviation", "null_ceiling", INK3, False),
            ("deviation", "ceiling", INDIGO, True)]
    for ax, benchmark in zip(axes, ("real", "injected")):
        for y, (rep, field, color, filled) in enumerate(rows):
            mean, low, high = mean_ci([c["reps"][rep][field] for c in cohorts(report, benchmark)])
            dot_row(ax, y, mean, low, high, color, lang, filled=filled, bold=color == INDIGO)
        ax.set_xlim(0.4, 1.08)
        ax.set_xticks([0.4, 0.6, 0.8, 1.0])
        ax.set_ylim(len(rows) - 0.4, -0.6)
        ax.set_yticks(range(len(rows)), text["ceil_rows"])
        style_axis(ax, lang)
    axes[0].get_yticklabels()[-1].set_fontweight("bold")
    axes[0].get_yticklabels()[-1].set_color(INDIGO_INK)
    fit_left(fig, axes[0], top=0.82, bottom=0.26)
    fig.subplots_adjust(wspace=0.08)
    for ax, benchmark, letter in zip(axes, ("real", "injected"), "AB"):
        panel_title(ax, letter, text[benchmark], 0.0 if letter == "A" else ax.get_position().x0)
    fig.text(0.5, 0.02, text["ceiling_axis"], ha="center", fontsize=7.3, color=INK2)
    save(fig, path, png)


def figure_ari(report, lang, path, png):
    text = TEXT[lang]
    fig, axes = plt.subplots(1, 2, figsize=(WIDTH, 2.45), sharey=True)
    for ax, benchmark in zip(axes, ("real", "injected")):
        for y, rep in enumerate(ORDER):
            values = [c["reps"][rep]["kmeans_oracle"]["ari"] for c in cohorts(report, benchmark)
                      if rep in c["reps"] and "kmeans_oracle" in c["reps"][rep]]
            mean, low, high = mean_ci(values)
            dot_row(ax, y, mean, low, high, INDIGO if rep in PROPOSED else INK3, lang, bold=rep in PROPOSED)
        ax.set_yticks(range(len(ORDER)), [text["reps"][r] for r in ORDER])
        ax.set_xlim(-0.2, 0.66)
        ax.set_xticks([-0.2, 0, 0.2, 0.4, 0.6])
        ax.set_ylim(len(ORDER) - 0.4, -0.6)
        style_axis(ax, lang, zero=0)
    for tick, rep in zip(axes[0].get_yticklabels(), ORDER):
        if rep in PROPOSED:
            tick.set_fontweight("bold")
            tick.set_color(INDIGO_INK)
    fit_left(fig, axes[0], top=0.84, bottom=0.19)
    fig.subplots_adjust(wspace=0.08)
    for ax, benchmark, letter in zip(axes, ("real", "injected"), "AB"):
        panel_title(ax, letter, text[benchmark], 0.0 if letter == "A" else ax.get_position().x0,
                    subtitle=text[benchmark + "_scope"])
    fig.text(0.5, 0.02, text["ari_axis"], ha="center", fontsize=7.3, color=INK2)
    save(fig, path, png)


def figure_rules(report, lang, path, png):
    text = TEXT[lang]
    models = [("evidence|ila2", INDIGO, True), ("evidence|ila", INDIGO, False), ("evidence|cart", TEAL, True),
              ("outcome_summary|ila2", ORANGE, True), ("majority", INK3, False)]
    tracks = list(text["rule_tracks"])
    fig, axes = plt.subplots(1, len(tracks), figsize=(WIDTH, 1.7), sharey=True)
    for ax, track in zip(axes, tracks):
        benchmark, scope = track.split("|")
        rules = report["benchmarks"][benchmark]["rules"]
        for y, (model, color, filled) in enumerate(models):
            entry = rules[f"{scope}|{model}"]
            low, high = entry["bootstrap_macro_f1"]
            dot_row(ax, y, entry["macro_f1"], low, high, color, lang, filled=filled, bold=model == "evidence|ila2")
        ax.set_yticks(range(len(models)), [text["rule_models"][m[0]] for m in models])
        ax.set_xlim(0, 0.8)
        ax.set_xticks([0, 0.2, 0.4, 0.6])
        ax.set_ylim(len(models) - 0.4, -0.6)
        style_axis(ax, lang)
    fit_left(fig, axes[0], top=0.84, bottom=0.22)
    fig.subplots_adjust(wspace=0.16)
    for ax, track in zip(axes, tracks):
        ax.text(0, 1.05, text["rule_tracks"][track], transform=ax.transAxes, fontsize=7.7, fontweight="bold",
                va="bottom", color=INK)
    fig.text(0.5, 0.02, text["rule_axis"], ha="center", fontsize=7.3, color=INK2)
    save(fig, path, png)


# ---------------------------------------------------------------- Figure 6: per-category heatmap

def figure_categories(categories, lang, path, png):
    text = TEXT[lang]
    reps = ["outcomes", "combined_stdout", "deviation", "evidence"]
    cmap = LinearSegmentedColormap.from_list("indigo", ["#F3F4FA", "#B3BAE4", "#5A6AC6", "#27348B"])
    blocks = []
    for benchmark in ("real", "injected"):
        entry = categories["benchmarks"][benchmark]
        cats = sorted((c for c in CATEGORIES if c in entry["items_per_category"]),
                      key=lambda c: -entry["items_per_category"][c])
        blocks.append((benchmark, cats, entry))
    row = 0.185
    heights = [len(b[1]) for b in blocks]
    fig_h = row * sum(heights) + 1.24
    fig = plt.figure(figsize=(WIDTH, fig_h))
    label_w = 1.68 / WIDTH
    y_top = 1 - 0.34 / fig_h
    for (benchmark, cats, entry), letter in zip(blocks, "AB"):
        h = row * len(cats) / fig_h
        ax = fig.add_axes([label_w, y_top - h, 0.985 - label_w, h])
        matrix = np.array([[entry["recovered_share"][r].get(c, np.nan) for r in reps] for c in cats])
        ax.imshow(matrix, cmap=cmap, vmin=0, vmax=1, aspect="auto")
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                value = matrix[i, j]
                ax.text(j, i, num(value, lang), ha="center", va="center", fontsize=7.2,
                        color="white" if value >= 0.6 else INK)
        ax.set_yticks(range(len(cats)), [f"{text['cats'][c]} ({entry['items_per_category'][c]})" for c in cats])
        ax.set_xticks(range(len(reps)), [text["short"][r] for r in reps])
        ax.xaxis.tick_top()
        ax.tick_params(axis="x", length=0, pad=2, labelsize=7.4)
        ax.tick_params(axis="y", length=0, labelsize=7.4)
        for tick, rep in zip(ax.get_xticklabels(), reps):
            if rep in PROPOSED:
                tick.set_fontweight("bold")
                tick.set_color(INDIGO_INK)
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.set_xticks(np.arange(-0.5, len(reps)), minor=True)
        ax.set_yticks(np.arange(-0.5, len(cats)), minor=True)
        ax.grid(which="minor", color="white", linewidth=1.2)
        ax.tick_params(which="minor", length=0)
        fig.text(0.0, y_top + 0.2 / fig_h, f"{letter}   {text[benchmark]}", fontsize=8.3, fontweight="bold",
                 va="bottom")
        y_top -= h + 0.46 / fig_h
    fig.text(0.5, 0.012, text["heat_axis"], ha="center", va="bottom", fontsize=7.3, color=INK2)
    save(fig, path, png)


# ---------------------------------------------------------------- Figure 8: instructor tool

def figure_tool(lang, path, png):
    image = plt.imread(HERE / "data" / "aai_lab_class_view.png")
    marks = json.loads((HERE / "data" / "aai_lab_marks.json").read_text(encoding="utf-8"))
    height_px, width_px = image.shape[:2]
    legend = marks["legend"][lang]
    rows = (len(legend) + 1) // 2
    image_h = WIDTH * height_px / width_px
    legend_h = 0.16 * rows + 0.1
    fig = plt.figure(figsize=(WIDTH, image_h + legend_h))
    frac = image_h / (image_h + legend_h)
    ax = fig.add_axes([0, 1 - frac, 1, frac])
    ax.imshow(image, interpolation="lanczos")
    ax.set_xlim(0, width_px)
    ax.set_ylim(height_px, 0)
    ax.axis("off")
    ax.add_patch(Rectangle((0.5, 0.5), width_px - 1, height_px - 1, fill=False, edgecolor=LINE, linewidth=0.8))
    radius = width_px * 0.0118
    for n, (x, y) in enumerate(marks["points"], start=1):
        ax.add_patch(Circle((x, y), radius, facecolor=INDIGO, edgecolor="white", linewidth=0.8, zorder=5))
        ax.text(x, y, str(n), ha="center", va="center", fontsize=6.4, color="white", fontweight="bold", zorder=6)
    labels = []
    for n, item in enumerate(legend, start=1):
        col, line = (n - 1) % 2, (n - 1) // 2
        fy = (legend_h - 0.08 - line * 0.16) / fig.get_figheight()
        fig.text(col * 0.5, fy, str(n), fontsize=6.8, color=INDIGO, fontweight="bold", va="top")
        labels.append((col, fig.text(col * 0.5 + 0.022, fy, item, fontsize=6.8, color=INK2, va="top")))
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    for col, label in labels:  # each legend entry must stay inside its half of the width
        right = label.get_window_extent(renderer).x1 / fig.bbox.width
        assert right <= (0.49 if col == 0 else 1.0), f"{path.name}: legend too long: {label.get_text()!r}"
    save(fig, path, png)


# ---------------------------------------------------------------- Graphical abstract (13 x 5 cm)

def graphical_abstract(lang, path, png, summary, report, stats):
    en = lang == "en"
    real, inj = summary["benchmarks"]["real"], summary["benchmarks"]["injected"]
    canvas = Canvas(1.97, width=5.12)
    heads = (["Same failing tests,", "different errors"], ["Labels from students'", "own verified repairs"],
             ["What the test signature", "misses, output evidence finds"]) if en else \
        (["Cùng trượt test,", "khác lỗi"], ["Nhãn từ bản sửa", "đã kiểm chứng của SV"],
         ["Chữ ký test bỏ sót gì,", "bằng chứng output tìm lại"])
    xs = (0.06, 1.8, 3.38)
    for x, head in zip(xs, heads):
        canvas.text(x, 0.08, head[0], fontsize=8.2, fontweight="bold")
        canvas.text(x, 0.24, head[1], fontsize=8.2, fontweight="bold")
    names = ["Output text", "Output format", "Computation"] if en else ["Nội dung in ra", "Định dạng in", "Tính toán"]
    for k, name in enumerate(names):
        y = 0.6 + k * 0.42
        canvas.box(0.06, y, 1.5, 0.32, face=PANEL, edge="none", radius=0.04)
        for t in range(4):
            x0 = 0.14 + t * 0.14
            canvas.ax.add_patch(Rectangle((x0, y + 0.1), 0.11, 0.11, facecolor=FAIL, edgecolor="none"))
        canvas.text(0.76, y + 0.16, name, va="center", fontsize=7, color=INK2)
    canvas.text(1.8, 0.6, count(stats["real"]["gold"], lang), fontsize=14, fontweight="bold", color=INDIGO)
    canvas.text(1.8, 0.88, "delta-debugged student repairs" if en else "bản sửa SV qua delta debugging", fontsize=6.9, color=INK2)
    canvas.text(1.8, 1.16, count(stats["injected"]["mutants"], lang), fontsize=14, fontweight="bold", color=INDIGO)
    canvas.text(1.8, 1.44, "controlled single-edit mutants" if en else "đột biến một chỗ có kiểm soát", fontsize=6.9, color=INK2)
    h1a = real["hypotheses"]["H1a"]["summary"]["mean"]
    results = [(f"{100 * h1a:.0f}%", ["of real items, at most, can be", "placed from test outcomes"] if en else
                ["số bài thật, tối đa, xếp đúng", "được chỉ từ kết quả test"]),
               (f"{num(inj['ari_kmeans_oracle']['outcomes'], lang)} \u2192 {num(inj['ari_kmeans_oracle']['deviation'], lang)}",
                ["ARI from test outcomes to", "deviation OAV, controlled data"] if en else
                ["ARI từ kết quả test sang", "OAV độ lệch, dữ liệu kiểm soát"])]
    for k, (value, label) in enumerate(results):
        y = 0.6 + k * 0.66
        canvas.text(3.38, y, value, fontsize=13, fontweight="bold", color=INDIGO)
        for m, line in enumerate(label):
            canvas.text(3.38, y + 0.26 + m * 0.12, line, fontsize=6.8, color=INK2)
    canvas.arrow(1.6, 1.02, 1.74, 1.02)
    canvas.arrow(3.2, 1.02, 3.32, 1.02)
    canvas.save(path, png)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lang", choices=("en", "vi"), default="en")
    parser.add_argument("--png", action="store_true", help="also write PNG previews")
    parser.add_argument("--only", nargs="*", help="figure names to build")
    args = parser.parse_args()
    setup()
    report = load("mechanism-v1.1-test/results.json")
    summary = load("mechanism-v1.1-test/summary.json")
    categories = load("mechanism-v1.1-test/categories.json")
    stats = load("mechanism-bench-v1.1/stats.json")
    build = load("mechanism-bench-v1.1/build_manifest_v1.json")
    audit = load("replay-v2-20260930/oracle_audit.json")
    policy = audit["policies"][audit["selected_policy"]]["agreement_by_partition"]
    agree = sum(c.get("agree", 0) for c in policy.values())
    cells = sum(sum(c.values()) for c in policy.values())
    lang = args.lang
    audit_pct = num(100 * agree / cells, lang, 1)
    target = HERE / "figures"
    target.mkdir(exist_ok=True)
    jobs = {
        "fig1_example": lambda p: figure_example(lang, p, args.png),
        "fig2_overview": lambda p: figure_overview(lang, p, args.png, stats, audit_pct),
        "fig3_flow": lambda p: figure_flow(lang, p, args.png, stats, build),
        "fig4_ceiling": lambda p: figure_ceiling(report, lang, p, args.png),
        "fig5_ari": lambda p: figure_ari(report, lang, p, args.png),
        "fig6_categories": lambda p: figure_categories(categories, lang, p, args.png),
        "fig7_rules": lambda p: figure_rules(report, lang, p, args.png),
        "fig8_tool": lambda p: figure_tool(lang, p, args.png),
        "graphical_abstract": lambda p: graphical_abstract(lang, p, args.png, summary, report, stats),
    }
    for name, job in jobs.items():
        if args.only and name not in args.only:
            continue
        job(target / f"{name}_{lang}.pdf")
        print("wrote", name, lang)


if __name__ == "__main__":
    main()

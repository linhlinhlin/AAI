"""Screenshot of the AAI Lab class view for Fig. 8, with callout positions read from the page.

Needs a running AAI Lab on a fresh data directory (the shipped demo class), for example
  python -m misconceptions.lab --no-browser --port 8771 --data-dir ../.cache/lab-figure
Run from AAI/:  misconceptions-prototype/.venv/Scripts/python.exe paper/capture_tool.py
"""

import json
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
BASE = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8771/"
SCALE = 2
CLIP = {"x": 228, "y": 12, "width": 1196, "height": 990}
MARKS = [  # selector, anchor inside its box (fractions), legend EN, legend VI
    (".group-tab[aria-selected=true] .strip", (0.0, 0.5), "Test signature of each group (one cell per test)",
     "Chữ ký test của nhóm (mỗi ô một test)"),
    (".hypothesis-line .tag", (0.0, 0.5), "Hypothesis: rule source and members covered",
     "Giả thuyết: nguồn luật, số bài khớp"),
    (".teach .teach-card", (0.0, 0.2), "A question to ask and a re-teaching activity",
     "Câu hỏi kiểm tra và hoạt động dạy lại"),
    (".test-bars", (0.0, 0.1), "Per-test failures: group bar vs. other groups",
     "Tỷ lệ trượt: thanh của nhóm, vạch nhóm khác"),
    (".rule", (1.0, 0.3), "ILA-2 rule for the group, precision and coverage",
     "Luật ILA-2 của nhóm, độ chính xác và độ phủ"),
    (".verdict-control", (0.0, 0.5), "The instructor confirms or rejects the group",
     "Giảng viên xác nhận hoặc bác bỏ nhóm"),
    (".members", (0.0, 0.25), "Members, representative (medoid) first",
     "Các bài, bài tiêu biểu (medoid) đứng đầu"),
]


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1440, "height": 1010}, device_scale_factor=SCALE,
                                color_scheme="light")
        page.goto(BASE + "#/lop/max-array")
        page.wait_for_selector(".teach .teach-card")
        page.wait_for_timeout(400)
        points = []
        for selector, (fx, fy), _en, _vi in MARKS:
            box = page.locator(selector).first.bounding_box()
            assert box, selector
            x = box["x"] + fx * box["width"] + (17 if fx >= 1 else -17)  # sit in the margin
            y = box["y"] + fy * box["height"]
            points.append([round((x - CLIP["x"]) * SCALE, 1), round((y - CLIP["y"]) * SCALE, 1)])
        page.screenshot(path=str(HERE / "data" / "aai_lab_class_view.png"), clip=CLIP)
        browser.close()
    (HERE / "data" / "aai_lab_marks.json").write_text(json.dumps({
        "source": "AAI Lab class view, demo class, exercise max-array, group 1",
        "points": points,
        "legend": {"en": [m[2] for m in MARKS], "vi": [m[3] for m in MARKS]}}, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8")
    print("captured", len(points), "marks")


if __name__ == "__main__":
    main()

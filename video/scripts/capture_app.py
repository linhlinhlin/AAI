"""Screenshots of AAI Lab for the explainer (needs a fresh instance on port 8771).

Run from video/ with the prototype environment:
  ../misconceptions-prototype/.venv/Scripts/python.exe scripts/capture_app.py
"""

import json
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parents[1]
OUT = HERE / "public" / "img"
BASE = "http://127.0.0.1:8771/"
CLIP = {"x": 216, "y": 0, "width": 1224, "height": 1000}
TARGETS = {  # name -> selector whose box is reported for camera moves
    "strip": ".group-tab[aria-selected=true] .strip",
    "tabs": ".groups",
    "hypothesis": ".hypothesis-line",
    "teach": ".teach",
    "bars": ".test-bars",
    "rule": ".rule",
    "verdict": ".verdict-control",
    "members": ".members",
    "mixed": ".no-hypothesis",
    "title": ".panel-head h2",
}


def boxes(page):
    found = {}
    for name, selector in TARGETS.items():
        locator = page.locator(selector)
        if locator.count():
            box = locator.first.bounding_box()
            found[name] = [round(box["x"] - CLIP["x"]), round(box["y"] - CLIP["y"]), round(box["width"]),
                           round(box["height"])]
    return found


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    layout = {"clip": CLIP}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1440, "height": 1000}, device_scale_factor=2, color_scheme="light")
        page.goto(BASE + "#/lop/max-array")
        page.wait_for_selector(".teach .teach-card")
        page.wait_for_timeout(500)
        page.screenshot(path=str(OUT / "lab_max.png"), clip=CLIP)
        layout["lab_max"] = boxes(page)
        page.goto(BASE + "#/lop/sum-range")
        page.wait_for_selector("#group-tab-2")
        page.click("#group-tab-2")
        page.wait_for_selector(".no-hypothesis")
        page.wait_for_timeout(500)
        page.screenshot(path=str(OUT / "lab_mixed.png"), clip=CLIP)
        layout["lab_mixed"] = boxes(page)
        browser.close()
    (HERE / "src" / "app_layout.json").write_text(json.dumps(layout, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(layout))


if __name__ == "__main__":
    main()

"""Export the motivating example of Fig. 1 from the local replay cache to paper/data/.

Three failing submissions to C-Pack-IPAs lab02-ex09 share one test signature (every test
fails) but their verified minimal repairs fall into three mechanism categories. The
figure is built from the exported JSON, so it can be regenerated without the cache.

Run from AAI/:  misconceptions-prototype/.venv/Scripts/python.exe paper/export_example.py
"""

import difflib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "misconceptions-prototype" / "src"))
from misconceptions.deviation_features import deviation_oav
from misconceptions.lab.cpack_source import CPackSource

PROBLEM = "lab02-ex09"
# Chosen for illustration: in the all-fail signature of lab02-ex09 (one of the largest signatures
# that mixes mechanisms), the shortest program of each category whose minimal repair has one or
# two changed lines. The three categories deviate from the oracle in three different ways.
ITEMS = {
    "OUTPUT_TEXT": "cpack-year-5-lab02-ex09-stu_200-sub_001",
    "OUTPUT_FORMAT": "cpack-year-1-lab02-ex09-stu_022-sub_013",
    "COMPUTATION": "cpack-year-6-lab02-ex09-stu_207-sub_001",
}
OUT = Path(__file__).resolve().parent / "data" / "motivating_example.json"


def main():
    source = CPackSource(ROOT)
    cohort = source.load()[PROBLEM]
    repairs = {}
    for line in source.bench.read_text(encoding="utf-8").splitlines():
        row = json.loads(line)
        if row["item_id"] in ITEMS.values():
            repairs[row["item_id"]] = row
    tests = cohort["tests"]
    items = {item["id"]: item for item in cohort["items"]}
    same_signature = [i for i in cohort["items"] if all(v != "pass" for v in i["outcomes"].values())]
    exported = []
    for label, item_id in ITEMS.items():
        item, repair = items[item_id], repairs[item_id]
        assert repair["primary"] == label and repair["one_minimal"]
        diff = [d for d in difflib.unified_diff(item["code"].splitlines(), repair["patched_source"].splitlines(),
                                                lineterm="", n=0)
                if d[:1] in "+-" and d[:3] not in ("+++", "---")]
        first = tests[0]
        runs = {t["test_id"]: (item["outcomes"][t["test_id"]], item["outputs"].get(t["test_id"]) or "",
                               t["expected"]) for t in tests}
        values = deviation_oav(runs, {t["expected"] for t in tests})
        exported.append({
            "label": label, "item_id": item_id,
            "signature": [item["outcomes"][t["test_id"]] for t in tests],
            "removed": [d[1:].strip() for d in diff if d.startswith("-")],
            "added": [d[1:].strip() for d in diff if d.startswith("+")],
            "input": first["input"], "expected": first["expected"],
            "printed": item["outputs"].get(first["test_id"]) or "",
            "deviation": {k: v for k, v in values.items() if k.startswith("agg:")},
        })
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps({
        "problem": PROBLEM, "corpus": "C-Pack-IPAs (anonymised)", "n_tests": len(tests),
        "cohort_failing": len(cohort["items"]), "same_signature_failing": len(same_signature),
        "items": exported}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(OUT.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()

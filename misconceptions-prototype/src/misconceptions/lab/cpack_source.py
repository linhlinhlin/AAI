"""C-Pack-IPAs cohorts for AAI Lab, read from the local research cache when it exists.

Each student and year contributes its latest failing submission (the unit of the
repair-grounded benchmark). Outcomes and outputs come from the isolated replay; verified
mechanism labels, where a minimal repair exists, are attached for comparison only.
"""

import json
import threading
from collections import defaultdict
from pathlib import Path

from ..replay import POLICY_DEFAULT, outcomes_from_record

ROOT = Path(__file__).resolve().parents[4]
EXCLUDED = {"MULTI", "OTHER", "NO_CHANGE"}


class CPackSource:
    def __init__(self, root=ROOT):
        self.data = root / ".cache" / "cpack-v3"
        self.replay = root / ".cache" / "cpack-replay-v2"
        self.bench = root / ".cache" / "mechanism-bench-v1.1" / "real_repairs.jsonl"
        self.unstable_path = root / "research" / "runs" / "replay-reproducibility-20260930.json"
        self.lock = threading.Lock()
        self.cohorts = None

    def available(self):
        missing = [p for p in (self.data / "cohorts", self.replay / "cohorts") if not p.exists()]
        if missing:
            return {"available": False,
                    "reason": "Chưa có dữ liệu C-Pack đã chạy lại trên máy này.",
                    "steps": [
                        "python scripts/download_cpack.py --output ../.cache/cpack-raw",
                        "python scripts/prepare_cpack.py --raw ../.cache/cpack-raw --output ../.cache/cpack-v3",
                        ("python scripts/replay_cpack.py --data ../.cache/cpack-v3 "
                         "--split-lock ../research/splits/cpack-v3.json --output ../.cache/cpack-replay-v2")]}
        return {"available": True}

    def _labels(self):
        unstable = set()
        if self.unstable_path.exists():
            unstable = set(json.loads(self.unstable_path.read_text(encoding="utf-8"))["outcome_differing_ids"])
        labels = {}
        if self.bench.exists():
            for line in self.bench.read_text(encoding="utf-8").splitlines():
                repair = json.loads(line)
                if repair.get("status") == "ok" and repair.get("one_minimal") and \
                        repair["primary"] not in EXCLUDED and repair["item_id"] not in unstable:
                    labels[repair["item_id"]] = repair["primary"]
        return labels, unstable

    def load(self):
        with self.lock:
            if self.cohorts is not None:
                return self.cohorts
            labels, unstable = self._labels()
            cohorts = {}
            for folder in sorted((self.data / "cohorts").iterdir()):
                problem = folder.name
                replay_path = self.replay / "cohorts" / problem / "replay.jsonl"
                if not replay_path.exists():
                    continue
                manifest = json.loads((folder / "manifest.json").read_text(encoding="utf-8"))
                suite = json.loads((folder / "tests.json").read_text(encoding="utf-8"))
                tests = [{"test_id": tid, "name": f"Test {i}", "input": suite[tid]["input"],
                          "expected": suite[tid]["expected"]} for i, tid in enumerate(manifest["test_ids"], 1)]
                reviews = {json.loads(line)["submission_id"]: json.loads(line) for line in
                           (folder / "review.jsonl").read_text(encoding="utf-8").splitlines()}
                sources = {json.loads(line)["submission_id"]: json.loads(line) for line in
                           (folder / "submissions.jsonl").read_text(encoding="utf-8").splitlines()}
                records = {json.loads(line)["submission_id"]: json.loads(line) for line in
                           replay_path.read_text(encoding="utf-8").splitlines()}
                attempts = defaultdict(list)
                for sid, row in sources.items():
                    if sid in unstable:
                        continue
                    outcomes = outcomes_from_record(records.get(sid, {}), suite, **POLICY_DEFAULT)
                    if outcomes is None:
                        continue
                    review = reviews[sid]
                    attempts[(row["student_id"], review["year"])].append((review["attempt"], sid, outcomes))
                items, finished = [], 0
                for (student, year), history in attempts.items():
                    history.sort()
                    finished += all(v == "pass" for v in history[-1][2].values())
                    failing = [h for h in history if any(v != "pass" for v in h[2].values())]
                    if not failing:
                        continue
                    _, sid, outcomes = failing[-1]
                    stdout = {t["test_id"]: t["stdout"] for t in records[sid]["tests"]}
                    items.append({"id": sid, "author": f"{student.split(':')[-1]} · {year}",
                                  "code": sources[sid]["source_code"], "outcomes": outcomes,
                                  "outputs": stdout, "label": labels.get(sid)})
                lab, exercise = problem.split("-")
                cohorts[problem] = {
                    "id": problem, "title": f"Lab {int(lab[3:])} · Bài {int(exercise[2:])}",
                    "tests": tests, "items": sorted(items, key=lambda i: i["id"]),
                    "stats": {"students": len(attempts), "failing": len(items), "finished": finished,
                              "labelled": sum(1 for i in items if i["label"])}}
            self.cohorts = cohorts
            return cohorts

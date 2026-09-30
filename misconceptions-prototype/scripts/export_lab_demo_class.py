"""Export the authored demo classroom (already executed in Docker) for AAI Lab.

Reads a learning-app data directory created by prepare_learning_demo.py and
extend_learning_demo.py, keeps each submission's code and recorded per-test runs,
and gives authors neutral display names. No program is executed here.
"""

import argparse
import hashlib
import json
import sqlite3
from pathlib import Path

from misconceptions.learning_problems import BY_ID


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    database = sqlite3.connect(args.data_dir / "learning.sqlite3")
    rows = database.execute(
        "select a.id, u.username, a.problem_id, a.source, a.result, a.created "
        "from attempts a join users u on u.id = a.user_id "
        "where a.status = 'completed' order by a.created, a.id").fetchall()
    authors, submissions, images = {}, [], set()
    for attempt_id, username, problem_id, source, result, created in rows:
        result = json.loads(result)
        if result.get("verdict") not in ("accepted", "needs_work") or problem_id not in BY_ID:
            continue
        authors.setdefault(username, f"Học viên mẫu {len(authors) + 1:02d}")
        images.add(result["provenance"]["image_id"])
        submissions.append({
            "id": "demo-" + attempt_id[:12], "problem_id": problem_id, "author": authors[username],
            "code": source, "created": created,
            "result": {"verdict": result["verdict"], "passed": result["passed"], "total": result["total"],
                       "tests": [{"test_id": t["test_id"], "outcome": t["outcome"], "output": t["output"],
                                  "exit_code": t.get("exit_code"), "limit": t.get("limit")}
                                 for t in result["tests"]]}})
    payload = {
        "schema": "aai_lab_demo_class_v1",
        "description": "Lớp mẫu: code do nhóm tự viết, chấm thật trong Docker; không phải dữ liệu sinh viên.",
        "runner": {"images": sorted(images), "comparison": "whitespace_separated_tokens"},
        "submissions": submissions,
    }
    text = json.dumps(payload, ensure_ascii=False, indent=1) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8")
    print(f"{len(submissions)} submissions from {len(authors)} authors; "
          f"sha256 {hashlib.sha256(text.encode()).hexdigest()[:16]}")


if __name__ == "__main__":
    main()

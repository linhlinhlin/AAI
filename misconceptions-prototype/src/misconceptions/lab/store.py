"""Local SQLite store for AAI Lab: class submissions and instructor reviews (no accounts)."""

import json
import sqlite3
import threading
import time
import uuid
from contextlib import contextmanager
from pathlib import Path

DEMO_CLASS = Path(__file__).resolve().parents[1] / "data" / "demo_class.json"
REVIEW_STATUS = {"open", "confirmed", "rejected"}


class LabStore:
    def __init__(self, directory: Path, demo=DEMO_CLASS):
        directory.mkdir(parents=True, exist_ok=True)
        self.path = directory / "lab.sqlite3"
        self.lock = threading.Lock()
        with self.connect() as db:
            db.executescript("""
                create table if not exists submissions (
                    id text primary key, problem_id text not null, author text not null,
                    code text not null, result text not null, origin text not null,
                    created real not null);
                create table if not exists reviews (
                    scope text not null, group_key text not null, status text not null,
                    note text not null, updated real not null, primary key (scope, group_key));
                create table if not exists meta (key text primary key, value text not null);
            """)
            seeded = db.execute("select value from meta where key = 'demo_seeded'").fetchone()
            if not seeded and demo.exists():
                payload = json.loads(demo.read_text(encoding="utf-8"))
                db.executemany(
                    "insert or ignore into submissions values (?, ?, ?, ?, ?, 'demo', ?)",
                    [(s["id"], s["problem_id"], s["author"], s["code"], json.dumps(s["result"]),
                      s["created"]) for s in payload["submissions"]])
                db.execute("insert into meta values ('demo_seeded', ?)", (payload["schema"],))

    @contextmanager
    def connect(self):
        connection = sqlite3.connect(self.path, timeout=10)
        connection.row_factory = sqlite3.Row
        try:
            with connection:  # Commit on success, roll back on error.
                yield connection
        finally:
            connection.close()

    def submissions(self, problem_id=None):
        query = "select * from submissions" + (" where problem_id = ?" if problem_id else "") + \
            " order by created, id"
        with self.connect() as db:
            rows = db.execute(query, (problem_id,) if problem_id else ()).fetchall()
        return [dict(row) | {"result": json.loads(row["result"])} for row in rows]

    def latest_per_author(self, problem_id):
        """The class view uses each author's most recent submission for a problem."""
        latest = {}
        for row in self.submissions(problem_id):
            latest[row["author"]] = row
        return list(latest.values())

    def add(self, problem_id, author, code, result):
        key = "try-" + uuid.uuid4().hex[:12]
        with self.lock, self.connect() as db:
            db.execute("insert into submissions values (?, ?, ?, ?, ?, 'trial', ?)",
                       (key, problem_id, author, code, json.dumps(result), time.time()))
        return key

    def remove_trial(self, key):
        with self.lock, self.connect() as db:
            deleted = db.execute("delete from submissions where id = ? and origin = 'trial'", (key,)).rowcount
        if not deleted:
            raise ValueError("Chỉ xóa được bài thêm từ Chạy thử.")

    def reviews(self, scope):
        with self.connect() as db:
            rows = db.execute("select group_key, status, note, updated from reviews where scope = ?",
                              (scope,)).fetchall()
        return {row["group_key"]: dict(row) for row in rows}

    def save_review(self, scope, group_key, status, note):
        if status not in REVIEW_STATUS or not isinstance(note, str) or len(note) > 2000:
            raise ValueError("Đánh giá không hợp lệ.")
        if not isinstance(group_key, str) or not group_key or len(group_key) > 300:
            raise ValueError("Nhóm không hợp lệ.")
        with self.lock, self.connect() as db:
            db.execute("insert into reviews values (?, ?, ?, ?, ?) on conflict(scope, group_key) "
                       "do update set status = excluded.status, note = excluded.note, "
                       "updated = excluded.updated", (scope, group_key, status, note, time.time()))
        return {"status": status, "note": note}

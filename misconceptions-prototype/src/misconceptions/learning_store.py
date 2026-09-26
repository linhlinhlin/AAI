"""SQLite accounts, sessions and append-only submission/review history."""

import hashlib
import hmac
import json
import re
import secrets
import sqlite3
import time
import uuid
from contextlib import contextmanager

PASSWORD_ROUNDS = 600000


class Store:
    def __init__(self, path):
        path.parent.mkdir(parents=True, exist_ok=True)
        self.path = path
        with self.connect() as db:
            db.executescript('''
                PRAGMA journal_mode=WAL;
                CREATE TABLE IF NOT EXISTS users (
                    id TEXT PRIMARY KEY, username TEXT UNIQUE NOT NULL,
                    name TEXT NOT NULL, role TEXT NOT NULL, password TEXT NOT NULL,
                    created REAL NOT NULL);
                CREATE TABLE IF NOT EXISTS sessions (
                    token_hash TEXT PRIMARY KEY, user_id TEXT NOT NULL, expires REAL NOT NULL);
                CREATE TABLE IF NOT EXISTS attempts (
                    id TEXT PRIMARY KEY, user_id TEXT NOT NULL, problem_id TEXT NOT NULL,
                    suite_version TEXT NOT NULL, source TEXT NOT NULL, reflection TEXT NOT NULL,
                    status TEXT NOT NULL, progress TEXT NOT NULL, result TEXT,
                    created REAL NOT NULL, finished REAL);
                CREATE INDEX IF NOT EXISTS attempt_owner ON attempts(user_id, created);
                CREATE INDEX IF NOT EXISTS attempt_cohort ON attempts(user_id, problem_id, created);
                CREATE TABLE IF NOT EXISTS reports (
                    id TEXT PRIMARY KEY, teacher_id TEXT NOT NULL,
                    payload TEXT NOT NULL, created REAL NOT NULL);
                CREATE TABLE IF NOT EXISTS reviews (
                    id TEXT PRIMARY KEY, report_id TEXT NOT NULL, teacher_id TEXT NOT NULL,
                    payload TEXT NOT NULL, created REAL NOT NULL);
            ''')

    @contextmanager
    def connect(self):
        db = sqlite3.connect(self.path, timeout=10)
        db.row_factory = sqlite3.Row
        try:
            with db:
                yield db
        finally:
            db.close()

    @staticmethod
    def public(user):
        return {key: user[key] for key in ('id', 'username', 'name', 'role')}

    def has_teacher(self):
        with self.connect() as db:
            return bool(db.execute("SELECT 1 FROM users WHERE role='teacher'").fetchone())

    def register(self, username, name, password, role='student'):
        if not isinstance(username, str) or not re.fullmatch(r'[a-zA-Z0-9_]{3,32}', username):
            raise ValueError('Tên đăng nhập cần 3–32 chữ cái, số hoặc dấu gạch dưới.')
        if not isinstance(name, str) or not 1 <= len(name.strip()) <= 80:
            raise ValueError('Tên hiển thị cần từ 1 đến 80 ký tự.')
        if not isinstance(password, str) or not 10 <= len(password) <= 128:
            raise ValueError('Mật khẩu cần từ 10 đến 128 ký tự.')
        if role not in ('student', 'teacher'):
            raise ValueError('Vai trò không hợp lệ.')
        salt = secrets.token_hex(16)
        derived = hashlib.pbkdf2_hmac('sha256', password.encode(), bytes.fromhex(salt),
                                     PASSWORD_ROUNDS).hex()
        user = {'id': uuid.uuid4().hex, 'username': username.lower(), 'name': name.strip(),
                'role': role}
        try:
            with self.connect() as db:
                db.execute('BEGIN IMMEDIATE')
                if role == 'teacher' and db.execute(
                        "SELECT 1 FROM users WHERE role='teacher'").fetchone():
                    raise ValueError('Tài khoản giảng viên đã được thiết lập.')
                db.execute('INSERT INTO users VALUES(?,?,?,?,?,?)',
                           (*user.values(), f'{salt}:{derived}', time.time()))
        except sqlite3.IntegrityError as error:
            raise ValueError('Tên đăng nhập đã được sử dụng.') from error
        return user

    def login(self, username, password):
        if not isinstance(username, str) or not isinstance(password, str) or len(password) > 128:
            raise ValueError('Tên đăng nhập hoặc mật khẩu không đúng.')
        with self.connect() as db:
            user = db.execute('SELECT * FROM users WHERE username=?', (username.lower(),)).fetchone()
        salt, expected = user['password'].split(':') if user else ('00' * 16, '00' * 32)
        actual = hashlib.pbkdf2_hmac('sha256', password.encode(), bytes.fromhex(salt),
                                    PASSWORD_ROUNDS).hex()
        if not user or not hmac.compare_digest(actual, expected):
            raise ValueError('Tên đăng nhập hoặc mật khẩu không đúng.')
        return self.public(user)

    def session(self, user):
        token = secrets.token_urlsafe(32)
        with self.connect() as db:
            db.execute('DELETE FROM sessions WHERE expires < ?', (time.time(),))
            db.execute('INSERT INTO sessions VALUES(?,?,?)',
                       (hashlib.sha256(token.encode()).hexdigest(), user['id'], time.time() + 43200))
        return token

    def authenticate(self, token):
        with self.connect() as db:
            user = db.execute('''SELECT users.* FROM sessions JOIN users ON users.id=sessions.user_id
                WHERE token_hash=? AND expires>?''',
                              (hashlib.sha256(token.encode()).hexdigest(), time.time())).fetchone()
        return self.public(user) if user else None

    def logout(self, token):
        with self.connect() as db:
            db.execute('DELETE FROM sessions WHERE token_hash=?',
                       (hashlib.sha256(token.encode()).hexdigest(),))

    def recover(self):
        with self.connect() as db:
            db.execute("""UPDATE attempts SET status='system_error', progress=?, finished=?
                       WHERE status IN ('queued','running')""",
                       ('Phiên chạy bị gián đoạn khi khởi động lại. Hãy nộp lại.', time.time()))

    def create_attempt(self, user, problem, source, reflection):
        if not isinstance(source, str) or not source.strip() or len(source.encode()) > 65536:
            raise ValueError('Bài làm cần có nội dung và tối đa 64 KB.')
        if not isinstance(reflection, str) or len(reflection) > 2000:
            raise ValueError('Ghi chú tối đa 2.000 ký tự.')
        key, now = uuid.uuid4().hex, time.time()
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            if db.execute("SELECT 1 FROM attempts WHERE user_id=? AND status IN ('queued','running')",
                          (user['id'],)).fetchone():
                raise ValueError('Bạn có một bài đang chấm. Đợi kết quả trước khi nộp tiếp.')
            count = db.execute('SELECT count(*) FROM attempts WHERE user_id=? AND created>?',
                               (user['id'], now - 60)).fetchone()[0]
            queued = db.execute("SELECT count(*) FROM attempts WHERE status IN ('queued','running')").fetchone()[0]
            if count >= 6 or queued >= 32:
                raise ValueError('Có nhiều lượt chạy. Vui lòng thử lại sau một phút.')
            db.execute('INSERT INTO attempts VALUES(?,?,?,?,?,?,?,?,?,?,?)',
                       (key, user['id'], problem['id'], problem['suite_version'], source,
                        reflection, 'queued', 'Đang xếp hàng…', None, now, None))
        return key

    def update_attempt(self, key, status, progress, result=None):
        with self.connect() as db:
            db.execute('UPDATE attempts SET status=?,progress=?,result=?,finished=? WHERE id=?',
                       (status, progress, json.dumps(result, ensure_ascii=False) if result else None,
                        time.time() if status in ('completed', 'system_error') else None, key))

    @staticmethod
    def attempt_value(row, include_source=True):
        value = dict(row)
        value['result'] = json.loads(value['result']) if value['result'] else None
        if not include_source:
            value.pop('source', None)
        return value

    def attempt(self, key, user):
        with self.connect() as db:
            row = db.execute('SELECT * FROM attempts WHERE id=?', (key,)).fetchone()
        if not row or (row['user_id'] != user['id'] and user['role'] != 'teacher'):
            raise PermissionError('Không có quyền xem bài làm này.')
        return self.attempt_value(row)

    def history(self, user):
        with self.connect() as db:
            rows = db.execute('SELECT * FROM attempts WHERE user_id=? ORDER BY created DESC LIMIT 200',
                              (user['id'],)).fetchall()
        values = [self.attempt_value(row, False) for row in rows]
        for value in values:
            if value['result']:
                value['result'] = {k: value['result'][k] for k in ('verdict', 'passed', 'total')}
        return values

    def history_stats(self, user):
        with self.connect() as db:
            completed = db.execute("SELECT count(*) FROM attempts WHERE user_id=? AND status='completed'",
                                   (user['id'],)).fetchone()[0]
            attempted = db.execute('SELECT count(DISTINCT problem_id) FROM attempts WHERE user_id=?',
                                   (user['id'],)).fetchone()[0]
            solved = [r[0] for r in db.execute("""SELECT DISTINCT problem_id FROM attempts
                WHERE user_id=? AND json_extract(result,'$.verdict')='accepted'""", (user['id'],))]
        return {'completed': completed, 'attempted': attempted, 'solved': solved}

    def attempt_counts(self):
        with self.connect() as db:
            return dict(db.execute("""SELECT problem_id,count(*) FROM attempts
                WHERE status='completed' GROUP BY problem_id""").fetchall())

    def classroom(self):
        with self.connect() as db:
            students = [self.public(row) for row in db.execute(
                "SELECT * FROM users WHERE role='student' ORDER BY name")]
            rows = db.execute("""SELECT a.* FROM attempts a WHERE a.status='completed'
                AND NOT EXISTS (SELECT 1 FROM attempts b WHERE b.user_id=a.user_id
                    AND b.problem_id=a.problem_id AND b.status='completed'
                    AND (b.created>a.created OR (b.created=a.created AND b.id>a.id)))
                ORDER BY a.created DESC""").fetchall()
        return students, [self.attempt_value(row) for row in rows]

    def save_report(self, teacher, report):
        key = uuid.uuid4().hex
        with self.connect() as db:
            db.execute('INSERT INTO reports VALUES(?,?,?,?)',
                       (key, teacher['id'], json.dumps(report, ensure_ascii=False), time.time()))
        return key

    def report(self, key):
        with self.connect() as db:
            row = db.execute('SELECT payload FROM reports WHERE id=?', (key,)).fetchone()
            reviews = db.execute('SELECT * FROM reviews WHERE report_id=? ORDER BY created',
                                 (key,)).fetchall()
        if not row:
            raise ValueError('Báo cáo không tồn tại.')
        return json.loads(row['payload']), [dict(r) | {'payload': json.loads(r['payload'])} for r in reviews]

    def recent_reports(self):
        with self.connect() as db:
            return [dict(row) for row in db.execute("""SELECT reports.id,reports.created,
                json_extract(payload,'$.problem.title') AS title,
                (SELECT count(*) FROM reviews WHERE report_id=reports.id) AS reviews
                FROM reports ORDER BY created DESC LIMIT 25""")]

    def review(self, key, teacher, mappings):
        with self.connect() as db:
            db.execute('INSERT INTO reviews VALUES(?,?,?,?,?)',
                       (uuid.uuid4().hex, key, teacher['id'],
                        json.dumps(mappings, ensure_ascii=False), time.time()))

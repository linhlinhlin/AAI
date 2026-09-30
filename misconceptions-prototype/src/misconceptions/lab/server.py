"""AAI Lab: a local, single-user app for misconception clustering (topic 5).

Run with `python -m misconceptions.lab`. There are no accounts: the server listens on
127.0.0.1 only, accepts only local Host/Origin values and requires a custom header on
every write, so other web pages cannot drive it. Student code runs only in Docker.
"""

import argparse
import json
import secrets
import socket
import sys
import threading
import urllib.request
import webbrowser
from collections import OrderedDict
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from ..learning_problems import BY_ID, PROBLEMS
from ..learning_sandbox import DockerSandbox, SandboxUnavailable
from ..mechanism_feedback import FEEDBACK
from . import analysis, study
from .cpack_source import CPackSource
from .store import LabStore

WEB = Path(__file__).with_name("web")
ROOT = Path(__file__).resolve().parents[4]
ASSETS = {"/": ("index.html", "text/html"), "/app.css": ("app.css", "text/css"),
          "/app.js": ("app.js", "text/javascript")}
MAX_BODY = 131072
CATEGORY_NAMES = {key: value["name"] for key, value in FEEDBACK.items()}


class LabService:
    def __init__(self, data_dir, sandbox=None, cpack=None):
        self.store = LabStore(data_dir)
        self.sandbox = sandbox or DockerSandbox()
        self.cpack = cpack or CPackSource()
        self.run_lock = threading.Lock()
        self.runs = OrderedDict()  # Verified runs awaiting "add to class", newest last.

    def class_items(self, problem_id):
        problem = BY_ID[problem_id]
        rows = self.store.latest_per_author(problem_id)
        items, passed = [], 0
        for row in rows:
            tests = {t["test_id"]: t for t in row["result"]["tests"]}
            outcomes = {t["test_id"]: tests.get(t["test_id"], {}).get("outcome", "not_run")
                        for t in problem["tests"]}
            if all(value == "pass" for value in outcomes.values()):
                passed += 1
                continue
            items.append({"id": row["id"], "author": row["author"], "code": row["code"],
                          "outcomes": outcomes, "origin": row["origin"],
                          "outputs": {tid: test.get("output") for tid, test in tests.items()}})
        return problem, items, {"students": len(rows), "failing": len(items), "passed": passed}

    def cohort(self, source, problem_id):
        if source == "class":
            if problem_id not in BY_ID:
                raise ValueError("Bài tập không tồn tại.")
            problem, items, stats = self.class_items(problem_id)
            return problem["title"], problem["tests"], items, stats, problem_id
        if source == "cpack":
            cohorts = self.cpack.load()
            if problem_id not in cohorts:
                raise ValueError("Bài tập C-Pack không tồn tại.")
            cohort = cohorts[problem_id]
            return cohort["title"], cohort["tests"], cohort["items"], cohort["stats"], "cpack:" + problem_id
        raise ValueError("Nguồn dữ liệu không hợp lệ.")

    def problems(self, source):
        if source == "class":
            listing = []
            for problem in PROBLEMS:
                _, _, stats = self.class_items(problem["id"])
                listing.append({"id": problem["id"], "title": problem["title"],
                                "topic": problem["topic"], **stats})
            return {"source": "class", "available": True, "problems": listing}
        state = self.cpack.available()
        if not state["available"]:
            return {"source": "cpack", **state, "problems": []}
        return {"source": "cpack", "available": True,
                "problems": [{"id": c["id"], "title": c["title"], **c["stats"]}
                             for c in self.cpack.load().values()]}

    def analysis(self, source, problem_id, k):
        if k != "auto" and k not in {"2", "3", "4", "5", "6"}:
            raise ValueError("Số nhóm không hợp lệ.")
        title, tests, items, stats, key = self.cohort(source, problem_id)
        report = analysis.analyze(items, tests, key if source == "class" else "cpack", k)
        reviews = self.store.reviews(f"{source}:{problem_id}")
        for group in report["groups"]:
            group["review"] = reviews.get(group["key"], {"status": "open", "note": ""})
            if group["verified"]:
                group["verified"]["names"] = {code: CATEGORY_NAMES.get(code, code)
                                              for code in group["verified"]["counts"]}
        return {"source": source, "problem": {"id": problem_id, "title": title}, "stats": stats,
                "tests": [{"test_id": t["test_id"], "name": t.get("name")} for t in tests], **report}

    def submission(self, source, problem_id, submission_id):
        _, tests, items, _, key = self.cohort(source, problem_id)
        item = next((i for i in items if i["id"] == submission_id), None)
        if item is None:
            raise ValueError("Không tìm thấy bài nộp.")
        described = analysis.describe_submission(item, tests, key if source == "class" else "cpack")
        if described["label"]:
            described["label_name"] = CATEGORY_NAMES.get(described["label"], described["label"])
        return described

    def run(self, problem_id, code):
        if problem_id not in BY_ID:
            raise ValueError("Bài tập không tồn tại.")
        if not isinstance(code, str) or not code.strip() or len(code) > 65536:
            raise ValueError("Mã nguồn cần có nội dung và dưới 64 KB.")
        problem = BY_ID[problem_id]
        with self.run_lock:  # One compile/run at a time keeps the local machine responsive.
            result = self.sandbox.evaluate(code, problem["tests"])
        stored = {"verdict": result["verdict"], "passed": result["passed"], "total": result["total"],
                  "tests": [{"test_id": t["test_id"], "outcome": t["outcome"], "output": t["output"],
                             "exit_code": t.get("exit_code"), "limit": t.get("limit")}
                            for t in result["tests"]]}
        response = {"verdict": result["verdict"], "diagnostics": result.get("diagnostics", ""),
                    "passed": result["passed"], "total": result["total"]}
        if result["verdict"] != "compile_error":
            item = {"id": "trial", "author": None, "code": code,
                    "outcomes": {t["test_id"]: t["outcome"] for t in result["tests"]},
                    "outputs": {t["test_id"]: t["output"] for t in result["tests"]}}
            described = analysis.describe_submission(item, problem["tests"], problem_id)
            response.update(tests=described["tests"], hypothesis=described["hypothesis"])
            run_id = secrets.token_hex(12)
            self.runs[run_id] = (problem_id, code, stored)
            while len(self.runs) > 50:
                self.runs.popitem(last=False)
            response["run_id"] = run_id
        return response

    def add_to_class(self, run_id, author):
        if run_id not in self.runs:
            raise ValueError("Hãy chạy thử lại trước khi thêm vào lớp.")
        author = (author or "").strip()
        if not author or len(author) > 60:
            raise ValueError("Nhập tên hiển thị từ 1 đến 60 ký tự.")
        problem_id, code, result = self.runs.pop(run_id)
        return {"id": self.store.add(problem_id, author, code, result), "problem_id": problem_id}


def make_handler(service, port_holder):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *_args):
            pass  # Never log source code or notes.

        def send(self, status, body, mime="application/json; charset=utf-8"):
            data = body if isinstance(body, bytes) else json.dumps(
                body, ensure_ascii=False, allow_nan=False).encode()
            self.send_response(status)
            self.send_header("Content-Type", mime)
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("Referrer-Policy", "no-referrer")
            self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'self'; "
                             "style-src 'self'; img-src 'self' data:; frame-ancestors 'none'; "
                             "base-uri 'none'; form-action 'none'; object-src 'none'")
            self.end_headers()
            try:
                self.wfile.write(data)
            except (BrokenPipeError, ConnectionResetError):
                pass

        def boundary(self, write=False):
            port = port_holder["port"]
            hosts = {f"127.0.0.1:{port}", f"localhost:{port}"}
            if self.headers.get("Host") not in hosts:
                raise PermissionError("Chỉ mở app qua địa chỉ trên máy này.")
            origin = self.headers.get("Origin")
            if origin and origin not in {"http://" + host for host in hosts}:
                raise PermissionError("Nguồn yêu cầu không hợp lệ.")
            if write and (self.headers.get("X-AAI-Lab") != "1"
                          or not self.headers.get("Content-Type", "").startswith("application/json")):
                raise PermissionError("Yêu cầu ghi không hợp lệ.")

        def body(self):
            length = int(self.headers.get("Content-Length") or 0)
            if length <= 0 or length > MAX_BODY:
                raise ValueError("Nội dung gửi lên trống hoặc quá lớn.")
            return json.loads(self.rfile.read(length))

        def do_GET(self):
            try:
                self.boundary()
                url = urlparse(self.path)
                query = {k: v[0] for k, v in parse_qs(url.query).items()}
                if url.path in ASSETS:
                    name, mime = ASSETS[url.path]
                    return self.send(200, (WEB / name).read_bytes(), mime + "; charset=utf-8")
                if url.path in ("/paper/en.pdf", "/paper/vi.pdf"):
                    path = study.PAPERS[url.path[7:9]]
                    if not path.exists():
                        return self.send(404, {"error": "Chưa có bản PDF."})
                    return self.send(200, path.read_bytes(), "application/pdf")
                if url.path == "/api/state":
                    return self.send(200, {"runner": service.sandbox.health(),
                                           "cpack": service.cpack.available()})
                if url.path == "/api/problems":
                    return self.send(200, service.problems(query.get("source", "class")))
                if url.path == "/api/analysis":
                    return self.send(200, service.analysis(query.get("source", "class"),
                                                           query.get("problem", ""), query.get("k", "auto")))
                if url.path == "/api/submission":
                    return self.send(200, service.submission(query.get("source", "class"),
                                                             query.get("problem", ""), query.get("id", "")))
                if url.path == "/api/problem":
                    problem = BY_ID.get(query.get("id", ""))
                    if not problem:
                        raise ValueError("Bài tập không tồn tại.")
                    return self.send(200, {key: problem[key] for key in (
                        "id", "title", "topic", "description", "constraints", "starter", "hints")}
                        | {"examples": problem["tests"][:2], "n_tests": len(problem["tests"])})
                if url.path == "/api/study":
                    return self.send(200, study.summary())
                return self.send(404, {"error": "Không tìm thấy nội dung."})
            except PermissionError as error:
                self.send(403, {"error": str(error)})
            except (ValueError, TypeError, KeyError) as error:
                self.send(400, {"error": str(error)})

        def do_POST(self):
            try:
                self.boundary(write=True)
                url = urlparse(self.path)
                data = self.body()
                if url.path == "/api/run":
                    return self.send(200, service.run(data.get("problem"), data.get("code")))
                if url.path == "/api/class/add":
                    return self.send(200, service.add_to_class(data.get("run_id"), data.get("author")))
                if url.path == "/api/review":
                    source, problem = data.get("source"), data.get("problem")
                    if source not in ("class", "cpack") or not isinstance(problem, str):
                        raise ValueError("Phạm vi đánh giá không hợp lệ.")
                    return self.send(200, service.store.save_review(
                        f"{source}:{problem}", data.get("group"), data.get("status"), data.get("note", "")))
                return self.send(404, {"error": "Không tìm thấy nội dung."})
            except PermissionError as error:
                self.send(403, {"error": str(error)})
            except SandboxUnavailable as error:
                self.send(503, {"error": str(error)})
            except (ValueError, TypeError, KeyError, json.JSONDecodeError) as error:
                self.send(400, {"error": str(error)})

    return Handler


class LocalServer(ThreadingHTTPServer):
    """Owns its port: on Windows SO_REUSEADDR would let a second copy bind the same port."""

    allow_reuse_address = sys.platform != "win32"

    def server_bind(self):
        if sys.platform == "win32":
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_EXCLUSIVEADDRUSE, 1)
        super().server_bind()


def running_lab(url):
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    try:
        with opener.open(url + "api/state", timeout=2) as response:
            return "runner" in json.load(response)
    except (OSError, ValueError):
        return False


def serve(service, port=8770, open_browser=True):
    holder = {"port": port}
    try:
        server = LocalServer(("127.0.0.1", port), make_handler(service, holder))
    except OSError:
        url = f"http://127.0.0.1:{port}/"
        if not running_lab(url):
            raise SystemExit(f"Port {port} is used by another program. Run again with another port, "
                             f"for example: start_lab.ps1 -Port {port + 1}") from None
        print(f"AAI Lab is already running: {url}", flush=True)
        if open_browser:
            webbrowser.open(url)
        return
    holder["port"] = server.server_address[1]
    if service.cpack.available().get("available"):
        # Read the C-Pack cohorts in the background so the first visit does not wait.
        threading.Thread(target=service.cpack.load, daemon=True).start()
    url = f"http://127.0.0.1:{holder['port']}/"
    print(f"AAI Lab: {url}  (keep this window open; Ctrl+C stops the app)", flush=True)
    if open_browser:
        threading.Timer(0.6, webbrowser.open, args=(url,)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8770)
    parser.add_argument("--data-dir", type=Path, default=ROOT / ".cache" / "lab")
    parser.add_argument("--no-browser", action="store_true")
    args = parser.parse_args()
    serve(LabService(args.data_dir), args.port, not args.no_browser)


if __name__ == "__main__":
    main()

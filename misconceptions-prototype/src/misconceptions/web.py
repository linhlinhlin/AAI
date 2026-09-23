"""Loopback-only workbench. Existing research inputs are never overwritten."""

import argparse
import hashlib
import importlib.util
import json
import secrets
import subprocess
import sys
import threading
import uuid
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict
from datetime import UTC, datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, quote, urlparse

from .adapters import load_dataset
from .ai_labeling import attach_ai_proposals
from .annotation_intake import merge_round_one
from .cli import build_provenance
from .expert_validation import score_annotation_sources, validate_annotations
from .features import extract_oav, route_submission
from .llm_client import configuration
from .pipeline import run_experiment
from .teacher_dashboard import build_dashboard, validate_mapping
from .teaching_report import attach_teaching_report, load_evidence

ROOT = Path(__file__).resolve().parents[2]
STATIC = Path(__file__).with_name("web_assets")
MAX_BODY = 16 * 1024 * 1024


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    with path.open("x", encoding="utf-8") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2, allow_nan=False)


class Workbench:
    def __init__(self, root=ROOT, llm_config=None):
        self.root = root
        self.output = root / "results/web_runs"
        self.token = secrets.token_urlsafe(32)
        self.jobs = {}
        self.lock = threading.Lock()
        self.executor = ThreadPoolExecutor(max_workers=1)
        self.llm_config = configuration(root / ".env") if llm_config is None else llm_config

    def datasets(self):
        paths = sorted((self.root / "data/itsp/cohorts").glob("*/manifest.json"))
        paths += sorted((self.root / "data/teaching_examples").glob("*/manifest.json"))
        demo = self.root / "data/demo/manifest.json"
        if demo.exists():
            paths.insert(0, demo)
        paths += sorted(self.output.glob("*/dataset/manifest.json"))
        result = []
        for path in paths:
            manifest = read_json(path)
            submissions = path.with_name("submissions.jsonl")
            if not submissions.exists():
                continue
            result.append({
                "id": path.relative_to(self.root).as_posix(),
                "problem": manifest["problem_id"], "language": manifest["language"],
                "name": manifest["dataset_name"], "tests": len(manifest["test_ids"]),
                "count": sum(bool(line.strip()) for line in
                             submissions.read_text(encoding="utf-8").splitlines()),
                "suite": manifest["suite_version"],
            })
        return result

    def dataset(self, identifier):
        allowed = {d["id"] for d in self.datasets()}
        if identifier not in allowed:
            raise ValueError("Dataset không tồn tại. Hãy tải lại danh sách.")
        path = self.root / identifier
        manifest, rows = load_dataset(path, path.with_name("submissions.jsonl"))
        return path, manifest, rows

    def inspect(self, identifier):
        path, manifest, rows = self.dataset(identifier)
        logs = {}
        review = path.with_name("review.jsonl")
        if review.exists():
            logs = {r["submission_id"]: r for r in
                    map(json.loads, review.read_text(encoding="utf-8").splitlines())}
        return {"manifest": manifest, "rows": [
            asdict(row) | {"oav": extract_oav(row),
                           "route": route_submission(row, manifest["test_ids"]),
                           "logged_tests": logs.get(row.submission_id, {}).get("logged_tests", [])}
            for row in rows
        ]}

    def artifacts(self):
        result = []
        for directory in [self.root / "docs", self.root / "results"]:
            for path in directory.rglob("*"):
                if path.is_file() and path.suffix in {".md", ".json", ".zip", ".jsonl"}:
                    result.append({"id": path.relative_to(self.root).as_posix(),
                                   "size": path.stat().st_size})
        # Download templates without exposing arbitrary filesystem paths.
        for name in ["data/demo/manifest.json", "data/demo/submissions.jsonl"]:
            path = self.root / name
            if path.exists():
                result.append({"id": name, "size": path.stat().st_size})
        return sorted(result, key=lambda item: item["id"])

    def artifact(self, identifier):
        if identifier not in {r["id"] for r in self.artifacts()}:
            raise ValueError("File không nằm trong danh mục được phép tải.")
        path = (self.root / identifier).resolve()
        if not path.is_relative_to(self.root.resolve()):
            raise ValueError("Đường dẫn ngoài workspace.")
        return path

    def submit(self, request):
        if not isinstance(request, dict):
            raise TypeError("Yêu cầu phải là JSON object.")
        action = request.get("action")
        if action not in {"run", "compare", "upload", "annotation", "check", "mapping"}:
            raise ValueError("Chức năng không hợp lệ.")
        with self.lock:
            if any(j["status"] in {"queued", "running"} for j in self.jobs.values()):
                raise ValueError("Đang có tác vụ chạy. Vui lòng đợi hoàn tất.")
            key = uuid.uuid4().hex
            self.jobs[key] = {"id": key, "action": action, "status": "queued"}
        self.executor.submit(self._execute, key, request)
        return {"id": key}

    def _execute(self, key, request):
        folder = self.output / key
        folder.mkdir(parents=True)
        with self.lock:
            self.jobs[key]["status"] = "running"
        try:
            result = self.perform(request, folder)
            write_json(folder / "result.json", result)
            update = {"status": "complete", "result": result,
                      "download": (folder / "result.json").relative_to(self.root).as_posix()}
        except Exception as error:  # noqa: BLE001 — contain failures at the background job boundary
            # A failed request must not kill the local server or report a false success.
            update = {"status": "failed", "error": f"{type(error).__name__}: {error}"}
        with self.lock:
            self.jobs[key].update(update)
            snapshot = dict(self.jobs[key])
        write_json(folder / "job.json", snapshot | {"finished_at": datetime.now(UTC).isoformat()})

    def perform(self, request, folder):
        action = request["action"]
        if action == "mapping":
            source = self.artifact(request.get("source"))
            if not source.is_relative_to(self.output.resolve()) or source.name != "result.json":
                raise ValueError("Chọn kết quả chạy web để gắn nhãn.")
            original = read_json(source)
            arm = request.get("arm", "run")
            if original.get("kind") not in {"run", "compare"} or arm not in original["results"]:
                raise ValueError("Kết quả nguồn hoặc arm không hợp lệ.")
            report = original["results"][arm]
            mappings = request.get("mappings")
            validate_mapping(report, mappings, request.get("reviewer"))
            report["teacher"] = build_dashboard(report, mappings)
            return {"kind": "mapping", "dataset": original["dataset"], "source": request["source"],
                    "source_sha256": digest(source), "arm": arm, "reviewer": request["reviewer"],
                    "saved_at": datetime.now(UTC).isoformat(), "report": report,
                    "notice": "Nhãn nhóm do người dùng khai báo; không phải annotation chấm mù."}
        if action in {"run", "compare"}:
            path, manifest, rows = self.dataset(request.get("dataset"))
            config = request.get("config", {})
            if action == "compare" and config.get("method") == "exact":
                raise ValueError("Exact chỉ dùng outcomes; chọn agglomerative hoặc kmeans cho A/B/C.")
            modes = {"A": "outcomes", "B": "structural", "C": "combined"}
            if action == "run":
                modes = {"run": config.get("feature_mode", "combined")}
            results = {}
            for arm, mode in modes.items():
                report = run_experiment(
                    rows, test_ids=manifest["test_ids"], method=config.get("method", "kmeans"),
                    k=int(config.get("k", 3)), seed=int(config.get("seed", 42)),
                    test_fraction=float(config.get("test_fraction", 0.25)), feature_mode=mode,
                    test_weight=float(config.get("test_weight", 0.8)),
                )
                report["provenance"] = build_provenance(
                    manifest, path, path.with_name("submissions.jsonl")
                )
                attach_teaching_report(report, rows, path.with_name("review.jsonl"))
                report["population"] = {row.submission_id: row.student_id for row in rows}
                with self.lock:
                    if folder.name in self.jobs:
                        self.jobs[folder.name]["progress"] = "Đang chuẩn bị đề xuất tên lỗi cho các nhóm…"
                attach_ai_proposals(report, rows, manifest, path.with_name("review.jsonl"),
                                    self.root, config=self.llm_config)
                report["teacher"] = build_dashboard(report)
                results[arm] = report
            return {"kind": action, "dataset": request["dataset"], "results": results}
        if action == "upload":
            for key in ("manifest", "submissions"):
                if not isinstance(request.get(key), str):
                    raise TypeError(f"Thiếu nội dung {key}.")
            dataset = folder / "dataset"
            dataset.mkdir()
            for key, filename in [("manifest", "pending_manifest.json"),
                                  ("submissions", "submissions.jsonl")]:
                (dataset / filename).write_text(request[key], encoding="utf-8")
            manifest, rows = load_dataset(dataset / "pending_manifest.json",
                                          dataset / "submissions.jsonl")
            if request.get("evidence"):
                if not isinstance(request["evidence"], str):
                    raise TypeError("Evidence phải là nội dung JSONL.")
                (dataset / "review.jsonl").write_text(request["evidence"], encoding="utf-8")
                load_evidence(dataset / "review.jsonl", rows)
            # Publish only after both inputs have passed validation.
            (dataset / "pending_manifest.json").rename(dataset / "manifest.json")
            return {"kind": "upload", "dataset": (dataset / "manifest.json").relative_to(
                self.root).as_posix(), "count": len(rows), "problem": manifest["problem_id"]}
        if action == "annotation":
            return self.annotation(request, folder)
        return self.check(request.get("check"))

    def annotation(self, request, folder):
        mode = request.get("mode")
        if mode not in {"validate", "merge", "score"}:
            raise ValueError("Chọn validate, merge hoặc score.")
        inputs = request.get("files", [])
        if not isinstance(inputs, list) or not inputs or len(inputs) > 20:
            raise ValueError("Chọn từ 1 đến 20 file JSON annotation.")
        if mode != "validate" and request.get("coordinator_confirmed") is not True:
            raise ValueError("Người điều phối cần xác nhận nguồn và điều kiện review trước xử lý.")
        ap = self.root / "results/itsp/abc_review_assignments.json"
        assignments = read_json(ap)
        documents, provenance = [], []
        for i, item in enumerate(inputs):
            text = item["text"]
            p = folder / f"input_{i + 1}.json"
            p.write_text(text, encoding="utf-8")
            doc = json.loads(text.lstrip("\ufeff"))
            if doc.get("assignments_sha256") != digest(ap):
                raise ValueError(f"File {i + 1}: assignment hash không khớp 17 mẫu ITSP.")
            validate_annotations(doc, assignments)
            documents.append(doc)
            provenance.append({"original_name": str(item.get("name", "")), "sha256": digest(p),
                               "saved_input": p.relative_to(self.root).as_posix()})
        if mode == "merge":
            value = merge_round_one(documents, assignments)
            value["intake"]["sources"] = provenance
        elif mode == "score":
            if len(documents) != 1:
                raise ValueError("Chọn một file đã hợp nhất để tính metrics.")
            value = score_annotation_sources(documents[0], assignments)
        else:
            value = {"valid_files": len(documents), "message": "Schema và assignment hash hợp lệ."}
        write_json(folder / "annotation_output.json", value)
        return {"kind": "annotation", "mode": mode, "value": value, "sources": provenance,
                "output": (folder / "annotation_output.json").relative_to(self.root).as_posix(),
                "notice": "Kiểm tra cấu trúc không xác thực danh tính; không tự adjudicate."}

    def check(self, name):
        if name in {"tests", "lint"}:
            args = [sys.executable, "-m"] + (
                ["pytest", "-q"] if name == "tests" else ["ruff", "check", "."]
            )
            process = subprocess.run(args, cwd=self.root, capture_output=True, timeout=300,
                                     check=False)
            return {"kind": "check", "check": name, "passed": process.returncode == 0,
                    "exit_code": process.returncode,
                    "log": (process.stdout + process.stderr).decode("utf-8", errors="replace")}
        if name == "packet":
            spec = importlib.util.spec_from_file_location(
                "local_packet_audit", self.root / "scripts/audit_human_review_packet.py"
            )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return {"kind": "check", "check": name, "passed": True,
                    "audit": module.audit(self.root)}
        if name == "provenance":
            import re

            text = (self.root / "results/itsp/reviewer_sources.md").read_text(encoding="utf-8")
            entries = re.findall(r"\]\(<([^>]+)>\) \| `([a-f0-9]{64})`", text)
            if not entries:
                raise ValueError("Không tìm thấy mục hash trong manifest nguồn.")
            mismatches = [name for name, expected in entries
                          if not Path(name).is_file() or digest(Path(name)) != expected]
            return {"kind": "check", "check": name, "passed": not mismatches,
                    "checked": len(entries), "mismatches": mismatches}
        raise ValueError("Kiểm tra không hợp lệ.")


def make_handler(app):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *_args):
            pass

        def send(self, status, content, mime="application/json; charset=utf-8", attachment=None):
            payload = content if isinstance(content, bytes) else json.dumps(
                content, ensure_ascii=False, allow_nan=False
            ).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", mime)
            self.send_header("Content-Length", str(len(payload)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("Content-Security-Policy", "default-src 'self'; style-src 'self'; "
                             "script-src 'self'; img-src 'self' data:; frame-ancestors 'none'")
            if attachment:
                self.send_header("Content-Disposition", f"attachment; filename*=UTF-8''{quote(attachment)}")
            self.end_headers()
            self.wfile.write(payload)

        def local_request(self):
            port = self.server.server_address[1]
            return self.headers.get("Host") in {f"127.0.0.1:{port}", f"localhost:{port}"}

        def do_GET(self):
            if not self.local_request():
                return self.send(403, {"error": "Chỉ truy cập qua localhost."})
            parsed = urlparse(self.path)
            query = parse_qs(parsed.query)
            try:
                if parsed.path in {"/", "/app.js", "/teacher.js", "/style.css"}:
                    path = STATIC / ("index.html" if parsed.path == "/" else parsed.path[1:])
                    mime = {".html": "text/html", ".js": "text/javascript", ".css": "text/css"}
                    return self.send(200, path.read_bytes(), mime[path.suffix] + "; charset=utf-8")
                if parsed.path == "/api/bootstrap":
                    return self.send(200, {"token": app.token, "datasets": app.datasets(),
                                           "llm": {k: v for k, v in app.llm_config.items() if k != "key_name"},
                                           "artifacts": app.artifacts()})
                if parsed.path == "/api/dataset":
                    return self.send(200, app.inspect(query.get("id", [""])[0]))
                if parsed.path == "/api/job":
                    with app.lock:
                        job = dict(app.jobs[query.get("id", [""])[0]])
                    return self.send(200, job)
                if parsed.path == "/api/artifact":
                    path = app.artifact(query.get("id", [""])[0])
                    if query.get("download") == ["1"]:
                        return self.send(200, path.read_bytes(), "application/octet-stream",
                                         attachment=path.name)
                    if path.suffix == ".zip":
                        raise ValueError("Hãy tải ZIP về máy để xem.")
                    return self.send(200, {"text": path.read_text(encoding="utf-8-sig"),
                                           "sha256": digest(path)})
                return self.send(404, {"error": "Không tìm thấy trang."})
            except (ValueError, KeyError, OSError, TypeError) as error:
                self.send(400, {"error": str(error)})

        def do_POST(self):
            port = self.server.server_address[1]
            origin = self.headers.get("Origin")
            if (not self.local_request() or self.headers.get("X-Workbench-Token") != app.token
                    or (origin and origin not in {
                        f"http://localhost:{port}", f"http://127.0.0.1:{port}"})):
                return self.send(403, {"error": "Phiên không hợp lệ. Hãy tải lại trang."})
            if self.path != "/api/jobs":
                return self.send(404, {"error": "Không tìm thấy chức năng."})
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if not 0 < length <= MAX_BODY:
                    raise ValueError("Dữ liệu yêu cầu phải nhỏ hơn 16 MB.")
                request = json.loads(self.rfile.read(length))
                self.send(202, app.submit(request))
            except (ValueError, TypeError) as error:
                self.send(400, {"error": str(error)})

    return Handler


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    app = Workbench()
    server = ThreadingHTTPServer(("127.0.0.1", args.port), make_handler(app))
    print(f"Misconceptions Lab: http://127.0.0.1:{args.port} (Ctrl+C to stop)", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
        app.executor.shutdown(wait=False, cancel_futures=True)


if __name__ == "__main__":
    main()

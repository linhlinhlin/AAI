"""Exercise the web boundary without changing existing research artifacts."""

import json
import shutil
import threading
import time
from http.client import HTTPConnection
from http.server import ThreadingHTTPServer
from pathlib import Path

import pytest

from misconceptions.web import Workbench, make_handler

ROOT = Path(__file__).resolve().parents[1]
DEMO = "data/demo/manifest.json"


@pytest.fixture
def app(tmp_path):
    shutil.copytree(ROOT / "data/demo", tmp_path / "data/demo")
    workbench = Workbench(tmp_path, llm_config={"provider": "openai", "model": "", "configured": False})
    yield workbench
    workbench.executor.shutdown(wait=True)


def run_job(app, payload):
    key = app.submit(payload)["id"]
    deadline = time.monotonic() + 20
    while time.monotonic() < deadline:
        with app.lock:
            job = dict(app.jobs[key])
        if job["status"] in {"complete", "failed"}:
            return job
        time.sleep(0.02)
    pytest.fail("Web job timed out")


def test_run_compare_and_isolated_outputs(app):
    source = app.root / DEMO
    original = source.read_bytes()
    job = run_job(app, {"action": "compare", "dataset": DEMO, "config": {"k": 3}})
    assert job["status"] == "complete", job
    reports = job["result"]["results"]
    assert {r["feature_mode"] for r in reports.values()} == {"outcomes", "structural", "combined"}
    assert reports["A"]["split"] == reports["B"]["split"] == reports["C"]["split"]
    assert reports["C"]["status"] == "ok"
    assert job["download"].startswith("results/web_runs/")
    assert app.artifact(job["download"]).is_file()
    assert source.read_bytes() == original


def test_exact_cannot_silently_replace_abc(app):
    job = run_job(app, {"action": "compare", "dataset": DEMO, "config": {"method": "exact"}})
    assert job["status"] == "failed"
    assert "Exact" in job["error"]


def test_invalid_upload_does_not_break_catalog(app):
    before = app.datasets()
    job = run_job(app, {"action": "upload", "manifest": "{}", "submissions": "{}"})
    assert job["status"] == "failed"
    assert app.datasets() == before
    job = run_job(app, {"action": "upload", "manifest": "{}"})
    assert job["status"] == "failed"
    assert app.datasets() == before


def test_valid_upload_can_be_inspected_and_run(app):
    job = run_job(app, {"action": "upload", "manifest": (app.root / DEMO).read_text(),
                       "submissions": (app.root / "data/demo/submissions.jsonl").read_text()})
    assert job["status"] == "complete", job
    identifier = job["result"]["dataset"]
    rows = app.inspect(identifier)["rows"]
    assert len(rows) == 52
    assert rows[0]["oav"] and "route" in rows[0]
    assert run_job(app, {"action": "run", "dataset": identifier})["status"] == "complete"


def test_artifact_paths_are_allowlisted(app):
    for identifier in ["../secret.json", "src/misconceptions/web.py", str(ROOT / "README.md")]:
        with pytest.raises(ValueError):
            app.artifact(identifier)


def test_teacher_mapping_is_persisted_without_modifying_original_run(app):
    original = run_job(app, {"action": "run", "dataset": DEMO})
    assert original["result"]["results"]["run"]["method"] == "kmeans"
    source = app.artifact(original["download"])
    before = source.read_bytes()
    report = original["result"]["results"]["run"]
    cluster = str(next(iter(report["train_assignments"].values())))
    entry = {"cluster": cluster, "status": "confirmed", "category": "other_error",
             "label": "Synthetic test only", "rationale": "Test fixture",
             "follow_up": "Inspect synthetic examples"}
    saved = run_job(app, {"action": "mapping", "source": original["download"], "arm": "run",
                         "reviewer": "synthetic-test", "mappings": [entry]})
    assert saved["status"] == "complete", saved
    assert source.read_bytes() == before
    document = json.loads(app.artifact(saved["download"]).read_text(encoding="utf-8"))
    assert document["report"]["teacher"]["bars"][0]["label"] == "Synthetic test only"
    assert document["source_sha256"] and document["reviewer"] == "synthetic-test"


def test_blank_annotations_remain_unvalidated(app):
    destination = app.root / "results/itsp"
    destination.mkdir(parents=True)
    shutil.copyfile(ROOT / "results/itsp/abc_review_assignments.json",
                    destination / "abc_review_assignments.json")
    source = ROOT / "results/itsp/human_review/annotations.json"
    original = source.read_bytes()
    payload = {"action": "annotation", "mode": "score", "coordinator_confirmed": True,
               "files": [{"name": "annotations.json", "text": source.read_text(encoding="utf-8")} ]}
    job = run_job(app, payload)
    assert job["status"] == "complete", job
    assert job["result"]["value"]["status"] == "waiting_for_human_expert_annotation"
    assert source.read_bytes() == original
    payload["coordinator_confirmed"] = False
    assert run_job(app, payload)["status"] == "failed"


def test_http_serves_ui_and_rejects_foreign_requests(app):
    server = ThreadingHTTPServer(("127.0.0.1", 0), make_handler(app))
    worker = threading.Thread(target=server.serve_forever, daemon=True)
    worker.start()
    connection = HTTPConnection(*server.server_address, timeout=5)

    def request(method, path, body=None, headers=None):
        connection.request(method, path, body, headers or {})
        response = connection.getresponse()
        data = response.read()
        return response, data

    try:
        response, body = request("GET", "/")
        assert response.status == 200 and b"experiment-form" in body
        assert "frame-ancestors 'none'" in response.getheader("Content-Security-Policy")
        response, body = request("GET", "/api/bootstrap")
        assert json.loads(body)["token"] == app.token
        assert request("GET", "/api/bootstrap", headers={"Host": "untrusted.example"})[0].status == 403
        assert request("POST", "/api/jobs", "{}")[0].status == 403
        headers = {"X-Workbench-Token": app.token, "Origin": "https://untrusted.example"}
        assert request("POST", "/api/jobs", "{}", headers)[0].status == 403
        headers.pop("Origin")
        payload = json.dumps({"action": "run", "dataset": DEMO})
        response, body = request("POST", "/api/jobs", payload, headers)
        assert response.status == 202 and json.loads(body)["id"]
        assert request("GET", "/api/artifact?id=../secret.json")[0].status == 400
    finally:
        connection.close()
        server.shutdown()
        server.server_close()
        worker.join()

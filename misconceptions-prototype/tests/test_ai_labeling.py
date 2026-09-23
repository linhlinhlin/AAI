import io
import json
import urllib.error
from pathlib import Path

import pytest

from misconceptions.adapters import load_dataset
from misconceptions.ai_labeling import attach_ai_proposals, cluster_evidence, problem_description
from misconceptions.llm_client import configuration, request_label, validate_label
from misconceptions.pipeline import run_experiment
from misconceptions.teacher_dashboard import build_dashboard, validate_mapping

ROOT = Path(__file__).resolve().parents[1]
CONFIG = {"provider": "openai", "model": "test-model", "configured": True}


def test_env_file_loads_without_overriding_environment(tmp_path, monkeypatch):
    for name in ("OPENAI_API_KEY", "MISCONCEPTIONS_LLM_PROVIDER", "MISCONCEPTIONS_LLM_MODEL",
                 "PYTHON_DOTENV_DISABLED"):
        monkeypatch.delenv(name, raising=False)
    env_file = tmp_path / ".env"
    env_file.write_text('MISCONCEPTIONS_LLM_PROVIDER=openai\n'
                        'MISCONCEPTIONS_LLM_MODEL="file-model"\n'
                        'OPENAI_API_KEY="test-${literal}"\n', encoding="utf-8-sig")
    config = configuration(env_file)
    assert config["configured"] and config["model"] == "file-model"
    import os
    assert os.environ["OPENAI_API_KEY"] == "test-${literal}"
    assert "test-${literal}" not in json.dumps(config)
    monkeypatch.setenv("MISCONCEPTIONS_LLM_MODEL", "environment-model")
    assert configuration(env_file)["model"] == "environment-model"


def test_missing_env_file_remains_optional(tmp_path, monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("MISCONCEPTIONS_LLM_MODEL", raising=False)
    assert not configuration(tmp_path / "missing.env")["configured"]


def output():
    return {"misconception_name": "Cần kiểm tra điều kiện dừng", "misconception_type": "Lỗi vòng lặp",
            "reasoning": "Mẫu đại diện có biểu hiện cần đối chiếu với giới hạn vòng lặp.",
            "teaching_hint": "Hãy truy vết vòng lặp với đầu vào nhỏ nhất.",
            "category": "misconception", "evidence_samples": ["sample_1"]}


@pytest.fixture
def experiment():
    manifest, rows = load_dataset(ROOT / "data/demo/manifest.json", ROOT / "data/demo/submissions.jsonl")
    report = run_experiment(rows, test_ids=manifest["test_ids"], method="kmeans", k=3)
    report["population"] = {row.submission_id: row.student_id for row in rows}
    return manifest, rows, report


def test_evidence_is_bounded_and_does_not_send_identity_fields(experiment):
    _, rows, report = experiment
    cluster = next(iter(report["train_assignments"].values()))
    payload, bindings = cluster_evidence(report, rows, {}, "problem", cluster)
    assert 1 <= len(payload["samples"]) <= 4
    assert all(len(s["source"]) <= 3000 for s in payload["samples"])
    assert "student_id" not in json.dumps(payload) and "submission_id" not in json.dumps(payload)
    assert set(bindings) == {s["sample_id"] for s in payload["samples"]}


@pytest.mark.parametrize("change", [{"evidence_samples": ["invented"]}, {"category": "approved"},
                                    {"reasoning": "x " * 50}, {"misconception_type": "Other"},
                                    {"evidence_samples": []}])
def test_invalid_model_output_is_rejected(change):
    with pytest.raises(ValueError):
        validate_label(output() | change, {"samples": [{"sample_id": "sample_1"}]})


def test_llm_proposals_are_cached_and_remain_drafts(tmp_path, experiment):
    manifest, rows, report = experiment
    calls = []

    def fake(payload, config):
        calls.append(payload)
        return output(), {"test_tokens": 1}

    attach_ai_proposals(report, rows, manifest, tmp_path / "missing.jsonl", tmp_path, call=fake, config=CONFIG)
    assert calls and report["ai_labeling"]["calls"] == len(calls)
    first = report["ai_labeling"]["proposals"]
    assert all(p["source"] == "llm" for p in first)
    attach_ai_proposals(report, rows, manifest, tmp_path / "missing.jsonl", tmp_path, call=fake, config=CONFIG)
    assert len(calls) == len(first)
    assert all(p["source"] == "llm_cache" for p in report["ai_labeling"]["proposals"])
    d = build_dashboard(report)
    assert d["confirmed_submissions"] == 0 and all(m["status"] == "draft" for m in d["mappings"])
    assert sum(g["count"] for g in d["overview"]) + d["excluded_submissions"] == len(rows)


def test_missing_credentials_and_failed_llm_are_not_mislabeled_as_ai(tmp_path, experiment):
    manifest, rows, report = experiment
    calls = []

    def failing(*args):
        calls.append(1)
        raise ValueError("test failure with sensitive detail that must not be stored")

    attach_ai_proposals(report, rows, manifest, tmp_path / "missing", tmp_path,
                        call=failing, config=CONFIG | {"configured": False})
    assert not calls
    attach_ai_proposals(report, rows, manifest, tmp_path / "missing", tmp_path, call=failing, config=CONFIG)
    assert len(calls) == 1  # Stop repeated requests after the first failure.
    assert all(p["source"] == "local_rules" for p in report["ai_labeling"]["proposals"])
    assert "sensitive detail" not in json.dumps(report)


def test_ignore_preserves_population_and_can_be_reversed(tmp_path, experiment):
    manifest, rows, report = experiment
    attach_ai_proposals(report, rows, manifest, tmp_path / "missing", tmp_path,
                        config=CONFIG | {"configured": False})
    original = build_dashboard(report)
    entry = original["mappings"][0] | {"status": "ignored"}
    validate_mapping(report, [entry], "UI test")
    d = build_dashboard(report, [entry])
    assert d["ignored_submissions"] > 0 and d["total_submissions"] == len(rows)
    assert d["confirmed_submissions"] == 0
    assert build_dashboard(report, [entry | {"status": "draft"}])["ignored_submissions"] == 0


@pytest.mark.parametrize("provider", ["openai", "anthropic", "gemini"])
def test_provider_request_and_structured_response(monkeypatch, provider):
    monkeypatch.setenv("OPENAI_API_KEY", "test-secret")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-secret")
    monkeypatch.setenv("GEMINI_API_KEY", "test-secret")
    captured = []

    class Response:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

        def read(self, size):
            if provider == "gemini":
                return json.dumps({"candidates": [{"finishReason": "STOP", "content": {
                    "parts": [{"text": json.dumps(output())}]}}], "usageMetadata": {"totalTokenCount": 10}}).encode()
            value = ({"choices": [{"finish_reason": "stop", "message": {"content": json.dumps(output())}}]}
                     if provider == "openai" else {"stop_reason": "tool_use", "content": [
                         {"type": "tool_use", "name": "label_cluster", "input": output()}]})
            return json.dumps(value).encode()

    def fake(request, timeout):
        captured.append(json.loads(request.data))
        assert timeout == 40
        if provider == "gemini":
            assert request.full_url.startswith("https://generativelanguage.googleapis.com/v1beta/models/")
            assert "test-secret" not in request.full_url
            assert dict(request.header_items())["X-goog-api-key"] == "test-secret"
        return Response()

    monkeypatch.setattr("urllib.request.urlopen", fake)
    value, _ = request_label({"samples": []}, CONFIG | {"provider": provider})
    assert value == output()
    field = {"openai": "response_format", "anthropic": "tools", "gemini": "generationConfig"}[provider]
    assert field in captured[0]


def test_gemini_configuration_uses_its_own_key(monkeypatch):
    monkeypatch.setenv("MISCONCEPTIONS_LLM_PROVIDER", "gemini")
    monkeypatch.setenv("MISCONCEPTIONS_LLM_MODEL", "gemini-test")
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    monkeypatch.setenv("OPENAI_API_KEY", "wrong-provider-key")
    assert not configuration()["configured"]
    monkeypatch.setenv("GEMINI_API_KEY", "test-secret")
    assert configuration()["configured"]
    assert configuration()["key_name"] == "GEMINI_API_KEY"


def test_http_errors_do_not_expose_credentials(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-secret")

    def failure(*args, **kwargs):
        raise urllib.error.HTTPError("secret-url", 401, "test-secret", {}, None)

    monkeypatch.setattr("urllib.request.urlopen", failure)
    with pytest.raises(ValueError, match="HTTP 401") as caught:
        request_label({}, CONFIG)
    assert "test-secret" not in str(caught.value)


def test_configuration_never_returns_a_key(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-secret")
    monkeypatch.setenv("MISCONCEPTIONS_LLM_MODEL", "test-model")
    monkeypatch.setenv("MISCONCEPTIONS_LLM_PROVIDER", "openai")
    assert configuration()["configured"] is True
    assert "test-secret" not in json.dumps(configuration())


@pytest.mark.parametrize("code", ["insufficient_quota", "credit_balance_exhausted"])
def test_quota_error_is_actionable_without_raw_provider_content(monkeypatch, code):
    monkeypatch.setenv("OPENAI_API_KEY", "test-secret")

    def failure(*args, **kwargs):
        body = json.dumps({"error": {"code": code, "message": "test-secret"}})
        raise urllib.error.HTTPError("secret-url", 429, "test-secret", {}, io.BytesIO(body.encode()))

    monkeypatch.setattr("urllib.request.urlopen", failure)
    with pytest.raises(ValueError, match="insufficient_quota") as caught:
        request_label({}, CONFIG)
    assert "test-secret" not in str(caught.value)


def test_problem_description_excludes_solution_and_arbitrary_files(tmp_path):
    source = tmp_path / "data/raw/itsp/p/Main.c"
    source.parent.mkdir(parents=True)
    source.write_text("/* Describe a problem */\nint correct_solution(){}")
    assert problem_description({"problem_reference": str(source)}, tmp_path).strip() == "Describe a problem"
    assert "correct_solution" not in problem_description({"problem_reference": str(source)}, tmp_path)
    assert "Chưa có" in problem_description({"problem_reference": str(tmp_path / "secret")}, tmp_path)

"""Bounded cluster evidence -> cached LLM proposal -> human review, never auto-approval."""

import hashlib
import json
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

from .features import extract_oav
from .hardcoded_output import LABEL, hardcoded_output
from .llm_client import (
    SCHEMA,
    SYSTEM_PROMPT,
    LLMRequestError,
    configuration,
    request_label,
    validate_label,
)
from .teaching_report import load_evidence

PROMPT_VERSION = "raw-code-hardcoded-output-v3"


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def problem_description(manifest, root):
    if isinstance(manifest.get("specification"), str):
        return manifest["specification"][:4000]
    reference = manifest.get("problem_reference")
    if isinstance(reference, str):
        path = Path(reference).resolve()
        if path.is_relative_to((root / "data/raw/itsp").resolve()) and path.is_file():
            text = path.read_text(encoding="utf-8", errors="replace").lstrip()
            if text.startswith("/*") and "*/" in text:
                # Only the problem's leading comment; never the reference implementation.
                return text[2:text.index("*/")][:4000]
    return "Chưa có mô tả bài toán; không suy đoán yêu cầu ngoài evidence."


def cluster_evidence(report, rows, logs, description, cluster):
    assignments = report.get("train_assignments", {}) | report.get("holdout_assignments", {})
    members = [row for row in rows if assignments.get(row.submission_id) == cluster]
    oav = {r.submission_id: extract_oav(r) for r in members}
    medoid = report.get("medoids", {}).get(str(cluster))
    ordered = sorted(members, key=lambda r: (r.submission_id != medoid, r.submission_id))
    selected, signatures = [], set()
    for row in ordered:
        signature = tuple(sorted(oav[row.submission_id].items()))
        if signature not in signatures:
            selected.append(row)
            signatures.add(signature)
        if len(selected) == 4:
            break
    for row in ordered:
        if len(selected) == 4:
            break
        if row not in selected:
            selected.append(row)
    samples, bindings = [], {}
    for index, row in enumerate(selected, 1):
        alias = f"sample_{index}"
        bindings[alias] = row.submission_id
        tests = sorted(logs.get(row.submission_id, []),
                       key=lambda t: (row.outcomes.get(t["test_id"]) != "fail", t["test_id"]))[:4]
        samples.append({"sample_id": alias, "raw_code": row.source_code,
                        "raw_code_truncated": False,
                        "hardcoded_output_evidence": hardcoded_output(row.source_code, row.outcomes)
                        if row.language.lower() == "c" else [],
                        "oav": oav[row.submission_id], "logged_tests": [
                            {k: v[:240] for k, v in t.items()} for t in tests],
                        "test_strings_may_be_truncated": True,
                        "test_logs_total": len(logs.get(row.submission_id, []))})
    names = sorted({key for values in oav.values() for key in values})
    distribution = {key: dict(Counter(values.get(key, "__unknown__") for values in oav.values()))
                    for key in names}
    common = [key[5:] for key, values in distribution.items()
              if key.startswith("test:") and values.get("fail") == len(members)]
    return {"cluster_size": len(members), "problem": description,
            "language": members[0].language if members else "unknown",
            "feature_distributions": distribution, "common_failed_tests": common,
            "samples": samples, "sampling": "medoid then distinct OAV signatures; at most four",
            "scope": "not every member is inspected; mixed causes are possible"}, bindings


def local_proposal(report, cluster, count):
    assignments = report.get("train_assignments", {}) | report.get("holdout_assignments", {})
    # Re-evaluate saved snapshots too; legacy reports predate this rule and OAV field.
    rows = [row for row in report.get("submissions", [])
            if assignments.get(row["submission_id"]) == cluster]
    covered = sum(row.get("language", "").lower() == "c" and bool(hardcoded_output(
        row["source_code"], row["outcomes"])) for row in rows)
    if not rows:
        covered = max((s["by_cluster"].get(str(cluster), 0)
                       for s in report.get("teaching", {}).get("summaries", [])
                       if s.get("rule_id") == "C_HARDCODED_OUTPUT"), default=0)
    if covered:
        return {"misconception_name": LABEL if covered == count else f"Có dấu hiệu: {LABEL}",
                "misconception_type": None, "category": "other_error" if covered == count else "mixed",
                "reasoning": f"{covered}/{count} bài có lệnh in hằng/biến hằng, không phụ thuộc input, và trượt ít nhất hai test.",
                "teaching_hint": "Thử hai giá trị n khác nhau; tính tổng từ 1 đến n rồi in kết quả thay cho hằng số.",
                "evidence_samples": []}
    matches = [s for s in report.get("teaching", {}).get("summaries", [])
               if s["by_cluster"].get(str(cluster))]
    strongest = max(matches, key=lambda s: s["by_cluster"][str(cluster)], default=None)
    if strongest:
        covered = strongest["by_cluster"][str(cluster)]
        title = strongest.get("explanation", {}).get("title", strongest["then_vi"])
        full = len(matches) == 1 and covered == count
        return {"misconception_name": title if full else f"Có dấu hiệu: {title}",
                "misconception_type": None,
                "reasoning": f"Bộ luật xác định khớp {covered}/{count} bài; cần xem các bài còn lại trước khi kết luận chung.",
                "teaching_hint": "Đối chiếu code và test của từng bài trước khi chọn nội dung giảng lại.",
                "category": ("other_error" if strongest["category"] == "presentation_issue"
                             else "misconception") if full else "mixed", "evidence_samples": []}
    assignments = report.get("train_assignments", {}) | report.get("holdout_assignments", {})
    observed = [report.get("oav", {}).get(sid, {}) for sid, value in assignments.items() if value == cluster]
    common = sorted(set.intersection(*[
        {key[5:] for key, value in row.items() if key.startswith("test:") and value == "fail"}
        for row in observed])) if observed else []
    symptom = (f"{count} bài cùng trượt test: {', '.join(common[:3])}. " if common else
               f"Có {count} bài trong cụm. ")
    return {"misconception_name": "Chưa đủ bằng chứng để đặt tên lỗi",
            "misconception_type": None, "reasoning": symptom + "Chưa xác định được cơ chế chung; cần đối chiếu từng bài.",
            "teaching_hint": "Đối chiếu input/output của bài đại diện; yêu cầu học viên truy vết và giải thích một trường hợp biên.",
            "category": "unclear", "evidence_samples": []}


def interpretation(local, value):
    """AI wording is advisory; it cannot promote a category/type to validated gold."""
    if LABEL in local["misconception_name"]:
        # Do not allow vague or contradictory generated text to erase deterministic evidence.
        return local | {"teaching_hint": value["teaching_hint"]}
    return local | {k: value[k] for k in ("misconception_name", "reasoning",
                                        "teaching_hint", "evidence_samples")}


def attach_ai_proposals(report, rows, manifest, evidence_path, root, *, call=request_label, config=None):
    config = configuration() if config is None else config
    assignments = report.get("train_assignments", {}) | report.get("holdout_assignments", {})
    logs = load_evidence(evidence_path, rows)
    description = problem_description(manifest, root)
    proposals, stopped, calls = [], False, 0
    for cluster in sorted(set(assignments.values())):
        payload, bindings = cluster_evidence(report, rows, logs, description, cluster)
        local = local_proposal(report, cluster, payload["cluster_size"])
        payload["local_draft"] = local
        payload["assistant_role"] = "Suggest wording and follow-up questions only; never validate a misconception."
        cache_key = fingerprint({"provider": config["provider"], "model": config["model"],
                                 "prompt": SYSTEM_PROMPT, "schema": SCHEMA, "payload": payload})
        cache = root / "results/llm_cache" / f"{cache_key}.json"
        origin, reason, usage = "local_rules", "Chưa cấu hình API key và model LLM.", {}
        value, diagnostic = local, None
        if config["configured"] and not stopped and calls < 12:
            try:
                if cache.exists():
                    cached = json.loads(cache.read_text(encoding="utf-8"))
                    value = cached["output"]
                    usage = cached.get("usage", {})
                    validate_label(value, payload)
                    origin = "llm_cache"
                else:
                    calls += 1
                    value, usage = call(payload, config)
                    validate_label(value, payload)
                    cache.parent.mkdir(parents=True, exist_ok=True)
                    cache.write_text(json.dumps({"output": value, "usage": usage,
                                                "created_at": datetime.now(UTC).isoformat()},
                                               ensure_ascii=False), encoding="utf-8")
                    origin = "llm"
                value = interpretation(local, value)
                reason = "AI hỗ trợ diễn giải; giảng viên kiểm tra. Chưa xác thực misconception."
            except (ValueError, TypeError, KeyError, OSError) as error:
                # Fail closed, without exposing provider credentials or raw response errors.
                stopped = True
                value = local_proposal(report, cluster, payload["cluster_size"])
                reason = "LLM lỗi kết nối, quyền truy cập hoặc JSON/evidence không hợp lệ; dùng bộ luật cục bộ."
                if isinstance(error, LLMRequestError):
                    reason = f"{error} Đang dùng bộ luật cục bộ."
                    diagnostic = {"code": error.code, "retryable": error.retryable}
                else:
                    diagnostic = {"code": "invalid_response", "retryable": False}
        elif config["configured"]:
            reason = "Tạm dừng gọi LLM do lỗi trước đó hoặc giới hạn 12 lời gọi; dùng bộ luật cục bộ."
        proposals.append({"cluster": str(cluster), "status": "draft", "source": origin,
                          "provider": config["provider"] if origin.startswith("llm") else None,
                          "model": config["model"] if origin.startswith("llm") else None,
                          "prompt_version": PROMPT_VERSION, "request_sha256": cache_key,
                          "notice": reason, "output": value, "local_output": local,
                          "llm_error": diagnostic, "validation_status": "unvalidated_hypothesis", "usage": usage,
                          "sample_bindings": bindings, "input": payload})
    report["ai_labeling"] = {"configured": config["configured"], "provider": config["provider"],
                             "model": config["model"], "calls": calls, "proposals": proposals,
                             "created_at": datetime.now(UTC).isoformat()}
    # Labels on conditions are derived from actual evidence, not generated by the LLM.
    report["test_context"] = {}
    for tests in logs.values():
        for test in tests:
            report["test_context"].setdefault(test["test_id"], test["input"][:160])

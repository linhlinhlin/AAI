"""Offline, blinded human review form. Never generate or prefill gold labels."""

import json
from pathlib import Path

from .teacher_validation import forms


def render_editor(evidence, slot="reviewer_1"):
    if slot not in {"reviewer_1", "reviewer_2"}:
        raise ValueError("Choose reviewer_1 or reviewer_2")
    # Reject accidental cluster packets: reviewers must not see inferred labels/rules.
    allowed = {"case_id", "problem_id", "language", "source_code", "outcomes",
               "logged_tests", "problem_statement", "evidence_kind"}
    if not evidence.get("cases") or any(set(c) - allowed for c in evidence["cases"]):
        raise ValueError("Expected a blind teacher-validation evidence packet")
    if len({c["case_id"] for c in evidence["cases"]}) != len(evidence["cases"]):
        raise ValueError("Duplicate case IDs")
    form, _ = forms(evidence)
    # Only the cases enter the browser, never coordinator bindings or packet metadata.
    payload = json.dumps({"cases": evidence["cases"], "form": form, "slot": slot},
                         ensure_ascii=False).replace("<", "\\u003c").replace("&", "\\u0026")
    template = Path(__file__).with_name("web_assets") / "annotation_editor.html"
    return template.read_text(encoding="utf-8").replace("__PACKET_JSON__", payload)

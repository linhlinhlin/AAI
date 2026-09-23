"""Run-scoped human mapping. Labels never become independent evaluation ground truth."""

from collections import defaultdict


def oav_conditions(conditions):
    result = []
    for raw in conditions:
        negated = raw.startswith("NOT (") and raw.endswith(")")
        condition = raw[5:-1] if negated else raw
        if condition == "TRUE":
            result.append({"object": "Bài đang xét", "attribute": "Điều kiện bổ sung",
                           "operator": "=", "value": "Không có", "raw": raw})
            continue
        feature, separator, value = condition.rpartition("=")
        if not separator:
            raise ValueError("Unsupported rule condition")
        result.append({"object": "Bài đang xét", "attribute": feature,
                       "operator": "≠" if negated else "=", "value": value, "raw": raw})
    return result


def validate_mapping(report, entries, reviewer):
    if not isinstance(reviewer, str) or not reviewer.strip() or len(reviewer) > 120:
        raise ValueError("Nhập tên người phụ trách gắn nhãn (tối đa 120 ký tự).")
    clusters = {str(c) for c in (report.get("train_assignments", {})
                                | report.get("holdout_assignments", {})).values()}
    if not isinstance(entries, list):
        raise TypeError("Mapping phải là danh sách.")
    seen = set()
    for entry in entries:
        if not isinstance(entry, dict):
            raise TypeError("Nhãn nhóm phải là object.")
        cluster = entry.get("cluster")
        if cluster not in clusters or cluster in seen:
            raise ValueError("Nhóm không thuộc lượt chạy hoặc bị lặp.")
        seen.add(cluster)
        if entry.get("status") not in {"unreviewed", "draft", "confirmed", "ignored"}:
            raise ValueError("Trạng thái nhãn không hợp lệ.")
        if entry.get("category") not in {"misconception", "other_error", "mixed"}:
            raise ValueError("Loại nhãn không hợp lệ.")
        for field, limit in [("label", 200), ("rationale", 2000), ("follow_up", 2000)]:
            if not isinstance(entry.get(field), str) or len(entry[field]) > limit:
                raise ValueError(f"Trường {field} không hợp lệ.")
        if entry["status"] not in {"unreviewed", "ignored"} and not entry["label"].strip():
            raise ValueError("Nhãn nháp hoặc xác nhận cần có tên.")
        if entry["status"] == "confirmed" and (
            not entry["rationale"].strip() or not entry["follow_up"].strip()
        ):
            raise ValueError("Xác nhận cần căn cứ và bước giảng lại/kiểm tra tiếp theo.")


def build_dashboard(report, mappings=()):
    assignments = report.get("train_assignments", {}) | report.get("holdout_assignments", {})
    population = report.get("population", {sid: None for sid in report.get("routes", {})})
    proposals = {p["cluster"]: p for p in report.get("ai_labeling", {}).get("proposals", [])}
    mapped = {}
    for cluster, proposal in proposals.items():
        output = proposal["output"]
        mapped[cluster] = {"cluster": cluster, "status": "draft",
                           "category": "mixed" if output["category"] == "unclear" else output["category"],
                           "label": output["misconception_name"], "rationale": output["reasoning"],
                           "follow_up": output["teaching_hint"]}
    mapped.update({entry["cluster"]: entry for entry in mappings})
    groups = defaultdict(set)
    confirmed_ids = set()
    for sid, cluster in assignments.items():
        entry = mapped.get(str(cluster))
        if entry and entry["status"] == "confirmed":
            groups[(entry["category"], entry["label"])].add(sid)
            confirmed_ids.add(sid)
    identity_known = bool(population) and all(population.values())
    total = len(population)
    students = set(population.values()) if identity_known else set()
    bars = []
    for (category, name), ids in sorted(groups.items()):
        people = {population[sid] for sid in ids} if identity_known else set()
        bars.append({"label": name, "category": category, "submissions": len(ids),
                     "submission_percent": 100 * len(ids) / total if total else 0,
                     "students": len(people) if identity_known else None,
                     "student_percent": 100 * len(people) / len(students) if students else None})
    rules = []
    for rule in report.get("explanation", {}).get("rules", []):
        entry = mapped.get(str(rule["then_cluster"]))
        rules.append({"conditions": oav_conditions(rule["if"]),
                      "conclusion": "Nhóm đã bỏ qua — không dùng làm kết luận giảng dạy"
                      if entry and entry["status"] == "ignored"
                      else entry["label"] if entry and entry["status"] != "unreviewed"
                      else "Chưa xác định — cần giảng viên gắn nhãn",
                      "status": entry["status"] if entry else "unreviewed",
                      "category": entry["category"] if entry else None,
                      "cluster": rule["then_cluster"],
                      "follow_up": entry["follow_up"] if entry else "",
                      "technical": rule})
    overview = []
    for cluster in sorted(set(assignments.values())):
        entry = mapped.get(str(cluster))
        proposal = proposals.get(str(cluster))
        count = sum(c == cluster for c in assignments.values())
        overview.append({"cluster": str(cluster), "count": count, "percent": 100 * count / total if total else 0,
                         "label": entry["label"] if entry else "Cần xem bằng chứng để đặt tên lỗi",
                         "status": entry["status"] if entry else "unreviewed",
                         "source": proposal["source"] if proposal else "none"})
    return {"total_submissions": total, "total_students": len(students) if identity_known else None,
            "confirmed_submissions": len(confirmed_ids),
            "unmapped_submissions": total - len(confirmed_ids),
            "excluded_submissions": total - len(assignments), "bars": bars, "rules": rules,
            "denominator": "all_submissions_in_selected_dataset",
            "scope": "Cluster labels reviewed by the named operator; not individual diagnoses.",
            "mappings": list(mapped.values()), "overview": overview,
            "ignored_submissions": sum(entry["count"] for entry in overview
                                       if entry["status"] == "ignored")}

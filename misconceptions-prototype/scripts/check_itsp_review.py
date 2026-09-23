"""One-command checks for the frozen AI review; never perform human validation."""

import hashlib
import json
import subprocess
import sys
import zipfile
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVIEW = "data/itsp/ai_independent_review.json"
COMPARISON = "results/itsp/ai_independent_review_comparison.json"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def indexed(rows):
    result = {row["submission_id"]: row for row in rows}
    require(len(result) == len(rows), "Duplicate submission ID")
    return result


def check_review(document, archive):
    blank = json.loads(archive.read("human_review/annotations.json"))
    expected = indexed(blank["samples"])
    reviews = indexed(document["reviews"])
    require(len(reviews) == 17 and reviews.keys() == expected.keys(), "Sample coverage != 17")
    require(document["reviewer_kind"] == "AI", "Reviewer must remain AI")
    for key in ("eligible_for_expert_metrics", "eligible_for_human_agreement"):
        require(document[key] is False, f"AI eligibility changed: {key}")
    require(all(v is None for v in document["expert_metrics"].values()), "AI metrics not null")
    require(document["codebook_approved_by"] is None, "AI cannot approve codebook")
    require(document["codebook_version"] == blank["codebook"]["version"], "Codebook version")
    require(document["codebook_sha256"] == hashlib.sha256(
        archive.read("human_review/CODEBOOK.md")).hexdigest(), "Codebook hash")
    total = 0
    for sid, review in reviews.items():
        require(review["problem_id"] == expected[sid]["problem_id"], f"Problem ID: {sid}")
        require(review["reviewer_id"].startswith("ai:"), f"Non-AI identity: {sid}")
        require(review["status"] == "complete", f"Incomplete: {sid}")
        decision = review["misconception"]
        require(decision in ("Yes", "No", "Unclear"), f"Decision: {sid}")
        kind = review["misconception_type"]
        require(kind in blank["codebook"]["misconception_types"] if decision == "Yes"
                else kind is None, f"Type: {sid}")
        confidence = review["confidence"]
        require(type(confidence) is int and 1 <= confidence <= 5, f"Confidence: {sid}")
        for key in ("evidence", "alternative_explanation", "paired_correct_assessment",
                    "human_check"):
            require(isinstance(review[key], str) and review[key].strip(), f"{key}: {sid}")
        require(review["same_cause_as_cluster"] == {"A": None, "B": None, "C": None},
                f"Cluster label leaked into independent review: {sid}")
        prefix = f"human_review/{sid}/"
        files = review["evidence_files"]
        require(len(files) == 4 and {f["path"] for f in files} == {
            prefix + name for name in ("Main.c", "buggy.c", "paired_correct.c",
                                       "logged_tests.json")}, f"Evidence coverage: {sid}")
        for item in files:
            require(hashlib.sha256(archive.read(item["path"])).hexdigest() == item["sha256"],
                    f"Evidence hash: {item['path']}")
        logs = json.loads(archive.read(prefix + "logged_tests.json"))
        require(review["all_logged_tests_read"] == len(logs), f"Test count: {sid}")
        total += len(logs)
        require(review["logged_test_evidence"] and all(
            test in logs for test in review["logged_test_evidence"]), f"Quoted test changed: {sid}")
        lines = archive.read(prefix + "buggy.c").decode().splitlines()
        require(review["source_lines"] and all(
            type(n) is int and 1 <= n <= len(lines) for n in review["source_lines"]),
            f"Source lines: {sid}")
    require(total == 113, "Historical test coverage != 113")
    return dict(Counter(r["misconception"] for r in reviews.values()))


def check_human_pending(document, metrics):
    samples = indexed(document["samples"])
    require(len(samples) == 17, "Expert sample coverage")
    for sid, sample in samples.items():
        human = [r for r in sample["reviews"]
                 if not (r["reviewer_id"] or "").startswith("ai:")]
        require(len(human) == 1, f"Human slots changed: {sid}")
        for rating in human + [sample["adjudication"]]:
            require(rating["status"] == "pending" and all(rating[k] is None for k in (
                "reviewer_id", "misconception", "misconception_type", "confidence", "evidence"
            )), f"Human annotation no longer pending/null: {sid}")
        require(human[0]["same_cause_as_cluster"] == {"A": None, "B": None, "C": None},
                f"Human cluster values: {sid}")
    require(metrics["n_completed_records"] == metrics["n_adjudicated"] == 0,
            "Human counts no longer zero")
    require(metrics["cluster_purity"] is None and metrics["agreement"] is None,
            "Expert metrics no longer null")
    for item in metrics["purity_details"]:
        require(item["cluster_purity"] is None, "Per-arm purity not null")
    for item in metrics["ai_annotation"]:
        require(all(item[k] is None for k in ("cluster_purity", "raw_agreement", "cohen_kappa")),
                "AI counted as expert metrics")


def check_comparison(new, old, comparison):
    reviews, samples = indexed(new["reviews"]), indexed(old["samples"])
    rows = indexed(comparison["comparisons"])
    require(rows.keys() == reviews.keys() == samples.keys(), "Comparison coverage")
    require(comparison["expert_metrics_computed"] is False, "Comparison computed expert metrics")
    counts = Counter()
    for sid, row in rows.items():
        candidates = [r for r in samples[sid]["reviews"] if
                      (r["reviewer_id"] or "").startswith("ai:") and r["status"] == "complete"]
        require(len(candidates) == 1, f"Ambiguous old AI: {sid}")
        old_review, review = candidates[0], reviews[sid]
        keys = ("reviewer_id", "misconception", "misconception_type", "confidence")
        require(row["old_ai"] == {k: old_review[k] for k in keys}, f"Old comparison row: {sid}")
        require(row["new_ai"] == {k: review[k] for k in keys}, f"New comparison row: {sid}")
        diff = old_review["misconception"] != review["misconception"]
        raw = old_review["misconception_type"] != review["misconception_type"]
        mapped = comparison["provisional_type_mapping"].get(old_review["misconception_type"])
        both = old_review["misconception"] == review["misconception"] == "Yes"
        require(row["decision_disagreement"] is diff, f"Disagreement flag: {sid}")
        require(row["raw_type_difference"] is raw, f"Raw type flag: {sid}")
        require(row["old_type_mapped_to_draft"] == mapped, f"Type mapping: {sid}")
        require(row["confidence_difference"] == review["confidence"] - old_review["confidence"],
                f"Confidence difference: {sid}")
        priority = "P1" if diff else "P2" if (
            review["misconception"] == "Unclear" or sid in {
                "itsp-2812-270283_buggy", "itsp-2825-271203_buggy", "itsp-2833-271986_buggy",
                "itsp-2812-270285_buggy", "itsp-2812-270293_buggy"}) else "P3"
        require(row["priority"] == priority, f"Priority: {sid}")
        require(row["human_check"] == review["human_check"], f"Human question: {sid}")
        counts.update(n_samples=1, n_decision_disagreements=int(diff),
                      n_raw_type_differences=int(raw), n_both_yes_comparable=int(both),
                      n_broad_type_disagreements_after_provisional_mapping=int(
                          both and mapped != review["misconception_type"]))
    for key, value in counts.items():
        require(comparison[key] == value, f"Comparison total: {key}")
    order = [r["submission_id"] for r in sorted(
        rows.values(), key=lambda r: (r["priority"], r["submission_id"]))]
    require(comparison["human_priority_order"] == order, "Priority order")
    return [r for r in rows.values() if r["decision_disagreement"]]


def check_integrity(root):
    verification = read_json(root / "results/itsp/ai_independent_review_verification.json")
    baseline_path = root / "results/itsp/ai_review_integrity_baseline.json"
    require(sha(baseline_path) == verification["baseline_sha256"], "Baseline hash changed")
    baseline = read_json(baseline_path)
    require(len(baseline) == verification["protected_existing_files_checked"], "Baseline coverage")
    changed = [name for name, digest in baseline.items()
               if not (root / name).is_file() or sha(root / name) != digest]
    require(not changed, "Protected files changed/missing: " + ", ".join(changed))
    digest = sha(root / REVIEW)
    require(digest == verification["independent_review_sha256"] == (
        root / "data/itsp/ai_independent_review.sha256").read_text().split()[0],
        "Frozen independent review changed")
    comparison = read_json(root / COMPARISON)
    require(comparison["independent_review_sha256"] == digest, "Comparison review hash")
    require(comparison["existing_annotations_sha256"] == sha(
        root / "data/itsp/expert_annotations.json"), "Comparison old annotations hash")
    require(read_json(root / REVIEW)["packet_sha256"] == sha(
        root / "results/itsp/human_review_packet.zip"), "Packet hash")
    return len(baseline)


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    report = {"checked_at_utc": datetime.now(UTC).isoformat(), "checks": [],
              "human_validation": "PENDING — kiểm tra tự động không xác nhận misconception"}

    def run_check(name, function):
        try:
            detail = function()
            report["checks"].append({"name": name, "passed": True, "detail": detail})
            print(f"[PASS] {name}", flush=True)
        except (ValueError, KeyError, TypeError, OSError, zipfile.BadZipFile,
                subprocess.SubprocessError) as error:
            report["checks"].append({"name": name, "passed": False, "detail": str(error)})
            print(f"[FAIL] {name}: {error}", flush=True)

    run_check("Toàn vẹn 523 file gốc và AI snapshot", lambda: check_integrity(ROOT))

    def artifacts():
        new = read_json(ROOT / REVIEW)
        old = read_json(ROOT / "data/itsp/expert_annotations.json")
        with zipfile.ZipFile(ROOT / "results/itsp/human_review_packet.zip") as archive:
            counts = check_review(new, archive)
        check_human_pending(old, read_json(ROOT / "results/itsp/expert_validation_metrics.json"))
        differences = check_comparison(new, old, read_json(ROOT / COMPARISON))
        return {"decisions": counts, "disagreements": differences}

    run_check("17 hồ sơ, evidence, đối chiếu và human null", artifacts)

    def command(args):
        result = subprocess.run([sys.executable, *args], cwd=ROOT, capture_output=True,
                                text=True, encoding="utf-8", errors="replace", timeout=300, check=False)
        output = (result.stdout + result.stderr).strip()
        require(result.returncode == 0, f"Exit {result.returncode}: {output}")
        return output

    for name, args in (
        ("Schema expert (validate-only)", ["scripts/score_itsp_experts.py", "--validate-only"]),
        ("Toàn bộ tests", ["-m", "pytest", "-q"]),
        ("Lint", ["-m", "ruff", "check", "."]),
    ):
        run_check(name, lambda args=args: command(args))
    run_check("Toàn vẹn sau tests/lint", lambda: check_integrity(ROOT))
    report["passed"] = all(c["passed"] for c in report["checks"])
    output = ROOT / "results/itsp/ai_review_check_latest.json"
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("\nKIỂM TRA TỰ ĐỘNG: " + ("ĐẠT" if report["passed"] else "KHÔNG ĐẠT"))
    print("HUMAN VALIDATION: CHƯA THỰC HIỆN; AI không phải expert ground truth.")
    for check in report["checks"]:
        if check["passed"] and isinstance(check["detail"], dict):
            print("Kết quả AI:", check["detail"]["decisions"])
            print("Ưu tiên human (bất đồng AI):")
            for row in check["detail"]["disagreements"]:
                print(f"  {row['submission_id']}: {row['old_ai']['misconception']} -> "
                      f"{row['new_ai']['misconception']}; {row['human_check']}")
        elif check["passed"] and check["name"] in ("Toàn bộ tests", "Lint"):
            print(check["detail"])
    print(f"Báo cáo: {output}")
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())

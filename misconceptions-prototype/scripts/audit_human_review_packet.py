"""Audit the blind round-one ZIP against frozen evidence; never execute student code."""

import hashlib
import json
import re
import zipfile
from pathlib import Path, PurePosixPath

from misconceptions.expert_validation import validate_annotations


def audit(root):
    folder = root / "results/itsp/human_review"
    archive = root / "results/itsp/human_review_packet.zip"
    document = json.loads((folder / "annotations.json").read_text(encoding="utf-8"))
    assignment_path = root / "results/itsp/abc_review_assignments.json"
    assignments = json.loads(assignment_path.read_text(encoding="utf-8"))
    assert document["assignments_sha256"] == hashlib.sha256(assignment_path.read_bytes()).hexdigest()
    validate_annotations(document, assignments)
    assert len(document["samples"]) == 17
    assert document["codebook"]["approved_by"] is None
    assert document["codebook"]["label_policy"] is None
    expected = {"README.md", "CODEBOOK.md", "annotations.json", "evidence_manifest.json"}
    manifest = json.loads((folder / "evidence_manifest.json").read_text(encoding="utf-8"))
    expected_sources = set()
    for sample in document["samples"]:
        sid = sample["submission_id"]
        assert len(sample["reviews"]) == 1
        for rating in sample["reviews"] + [sample["adjudication"]]:
            assert rating["status"] == "pending"
            assert all(rating[k] is None for k in (
                "reviewer_id", "misconception", "misconception_type", "confidence", "evidence"
            ))
        assert sample["reviews"][0]["independent_blind_review"] is False
        assert all(v is None for v in sample["reviews"][0]["same_cause_as_cluster"].values())
        logs = root / f"data/itsp/cohorts/{sample['problem_id']}/review.jsonl"
        original = next(json.loads(line) for line in logs.read_text(encoding="utf-8").splitlines()
                        if json.loads(line)["submission_id"] == sid)
        keys = ("test_id", "verdict", "input", "expected", "output")
        tests = [{k: t[k] for k in keys} for t in original["logged_tests"]]
        packaged = json.loads((folder / sid / "logged_tests.json").read_text(encoding="utf-8"))
        assert tests == packaged
        assert len(tests) == (6 if sample["problem_id"] == "2833" else 7)
        sources = {
            "buggy.c": Path(original["raw_path"]),
            "paired_correct.c": Path(original["paired_correct_path"]),
            "Main.c": Path(original["raw_path"]).parent / "Main.c",
        }
        for name, source in sources.items():
            relative = f"{sid}/{name}"
            expected_sources.add(relative)
            assert (root / manifest[relative]["source"]).resolve() == source.resolve()
            assert (folder / relative).read_bytes() == source.read_bytes()
            assert hashlib.sha256(source.read_bytes()).hexdigest() == manifest[relative]["sha256"]
        expected.update(f"{sid}/{name}" for name in (*sources, "logged_tests.json"))
    assert set(manifest) == expected_sources
    assert {p.relative_to(folder).as_posix() for p in folder.rglob("*") if p.is_file()} == expected
    codebook = (folder / "CODEBOOK.md").read_text(encoding="utf-8")
    for sample in document["samples"]:
        assert sample["submission_id"] not in codebook
        assert sample["submission_id"].split("-")[-1].split("_")[0] not in codebook
    for kind in document["codebook"]["misconception_types"]:
        assert f"| {kind} |" in codebook
    for name in ("README.md", "CODEBOOK.md"):
        for target in re.findall(r"\]\(([^)]+)\)", (folder / name).read_text(encoding="utf-8")):
            assert target in expected, f"External or broken reviewer link: {target}"
    with zipfile.ZipFile(archive) as zipped:
        assert zipped.testzip() is None
        names = zipped.namelist()
        assert len(names) == len(set(names))
        assert set(names) == {f"human_review/{name}" for name in expected}
        for name in names:
            relative = PurePosixPath(name).relative_to("human_review").as_posix()
            assert zipped.read(name) == (folder / relative).read_bytes()
    return {
        "status": "ready_for_expert_codebook_confirmation_then_blind_round1",
        "n_samples": 17,
        "n_source_files_verified": len(expected_sources),
        "n_test_logs_verified": 17,
        "n_logged_tests": 113,
        "n_zip_files": len(expected),
        "zip_sha256": hashlib.sha256(archive.read_bytes()).hexdigest(),
        "assignments_sha256": document["assignments_sha256"],
        "checks": ["ZIP CRC and exact file allowlist", "blank human-only forms",
                   "51 source files match originals and manifest SHA-256",
                   "all historical test records match", "all reviewer Markdown links are offline",
                   "codebook definitions present, no sample-specific labels",
                   "no cluster assignments, AI reviews or reports packaged"],
        "human_completed": 0,
        "cluster_purity": None,
        "raw_agreement": None,
        "cohen_kappa": None,
        "sent_to_experts": False,
    }


if __name__ == "__main__":
    project = Path(__file__).resolve().parents[1]
    report = audit(project)
    output = project / "results/itsp/human_review_packet_audit.json"
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Verified {report['n_zip_files']} ZIP files; saved {output}")

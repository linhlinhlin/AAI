"""Dataset-independent records; evidence is not a misconception label."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Submission:
    submission_id: str
    student_id: str | None
    problem_id: str
    language: str
    source_code: str
    suite_version: str
    outcomes: dict[str, str]
    provenance: str

    @property
    def cohort_key(self) -> tuple[str, str, str]:
        return self.problem_id, self.language, self.suite_version

# AAI — project context

Research target: topic 5, **Misconceptions Clustering** from failed programming
submissions. The deliverable connects test evidence and code structure to OAV,
unsupervised clusters, IF–THEN rules and aggregate teaching feedback. We acquire
public data ourselves; there is no promised teacher dataset or live classroom.

The Python package is `misconceptions-prototype/`. Use its `.venv` interpreter.
From this repository root:

```text
python scripts/harness.py doctor
python scripts/harness.py check
python scripts/harness.py smoke
```

Use `docs/harness.md` for setup and command details, `docs/topic5-contract.md`
for acceptance criteria, and `research/STATE.md` for current evidence and the
next research decision. These are task-specific references, not a mandatory
reading list for every edit. The `aai-experiment` repository skill covers changes
to data, splits, representations, experiments and scientific claims.

## Research boundaries

- Historical test logs are observations, not fresh execution. A code error or
  cluster is not evidence of a student's belief. Human and AI annotations have
  separate status; absent validation metrics stay null.
- Fit representations and rules on training data. Keep student identities and
  duplicate-source components together across the whole corpus before creating
  per-problem cohorts. Never feed later correct submissions, repairs, labels,
  reviewer notes or source paths into clustering features.
- Preserve existing `results/itsp/` as historical evidence. New runs use new
  directories with input, code, configuration and environment fingerprints.
- Local tests use disposable fixtures and recorded public logs, with no paid
  APIs or execution of student programs. Run and repair affected checks within
  the requested work without repeated permission requests.

## Code Review Rules

Flag missing-as-pass coercion, shuffled submissions across shared students,
holdout-based feature selection, or fidelity/silhouette described as misconception
accuracy. ILA is supervised rule induction; clustering here is unsupervised.
In C, arguments (including pointers) are passed by value.

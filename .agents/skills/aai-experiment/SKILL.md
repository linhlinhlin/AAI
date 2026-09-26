---
name: aai-experiment
description: Design, run or review AAI clustering experiments, dataset adapters, split policies and evidence-backed research claims.
---

# AAI experiments

Use this workflow for scientific changes; ordinary UI or copy edits do not need it.

Select the relevant reference:

- Data ingestion or evaluation: `docs/topic5-contract.md` (repository root).
- Reproduction and commands: `docs/harness.md`.
- A new research decision or result: `research/STATE.md` and
  `research/protocol.json`.
- Related-work or novelty claims: `research/literature/bao_cao_nghien_cuu.md`
  and its source ledger; verify newer primary sources before updating the cutoff.

Define the claim and its falsifying comparison before running an experiment.
Use the locked split for every variant. Keep output-aware baselines alongside
pass/fail and structural baselines; representation collisions alone do not prove
different underlying mechanisms. Use training and validation for design choices;
the sealed test partition is for a frozen final protocol.

Run the relevant harness command, inspect its artifacts, and fix failures caused
by the change. Record measured results separately from hypotheses in STATE.md,
with the exact artifact path and remaining validation. A run is complete when
its inputs and implementation are fingerprinted, its split invariants pass,
and its reports connect OAV → cluster → IF–THEN rule → teaching evidence.
Publication claims additionally require independent mechanism annotations and
the evaluation specified in the protocol; software checks do not satisfy that gate.

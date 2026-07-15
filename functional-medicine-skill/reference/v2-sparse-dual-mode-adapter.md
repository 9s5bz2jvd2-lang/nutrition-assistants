# V2 Sparse Distillation Dual-Mode Adapter

## Purpose

This adapter connects the functional-medicine router to a completed `sparse-book-to-skill-distillation` v2 build. It defines two runtime modes without embedding any local trial path, fixed source count, fixed chunk count, or review-progress snapshot in the deployable package.

## One-Time Build Prerequisite

Before either automatic v2 mode may run, all canonical chunks must receive genuine semantic L0–L3 review and the build must emit mutually consistent artifacts:

- `expert-index.v2.json` — compact L0/L1 routing and safety index
- `registry.v2.json` — canonical chunk identities, stable order, paths, and provenance links
- `source-manifest.json` — source/chunk hashes and lineage

Template creation is not semantic review. Intake, chunking, hashing, or pending records alone do not make the runtime ready. If any required artifact is absent, stale, incomplete, or hash-inconsistent, fail closed.

## Mode A — Ordinary Sparse Query

1. Parse the question into intents, triggers, anti-triggers, and safety context.
2. Rank compact index entries.
3. Load only the selected exact original chunks plus any required safety companions.
4. Preserve claim-to-source provenance in the answer.
5. Do not traverse unrelated chapter bodies.

Ordinary-query cardinality and paths come from the built registry, never from a hard-coded inventory.

## Mode B — Formula / Supplement Design

Formula mode uses the two-pass contract in `reference/formula_full_scan_contract.md`.

### Phase A: targeted deep retrieval

Use purpose, symptoms, diagnoses, medications, contraindications, nutrients, and special populations to select candidate chunks. Deep-read the exact originals for every selected chunk.

### Phase B: 100% compact-index omission/safety sweep

Iterate every canonical registry chunk in stable registry order. Inspect its compact triggers, anti-triggers, safety red lines, uncertainty, and risk tags. Any relevant hit escalates to deep reading of the exact original chunk.

The coverage ledger must be generated dynamically from the built registry and source manifest, with exactly one entry per canonical chunk. A static prefilled file list is invalid.

### Formula finalization gates

Finalization is forbidden unless all are true:

- every Phase A selected chunk was deep-read;
- every registry chunk was swept exactly once in Phase B;
- every sweep hit was escalated and resolved;
- no entry is `pending`, `unreadable`, or `escalated_unresolved`;
- every chunk ID, path, and SHA-256 matches the registry/source manifest.

There is no justification bypass for unresolved items.

## Artifact and Package Boundary

The deployable candidate contains contracts and a blank ledger schema, not development-workspace state. Trial counts, local paths, progress snapshots, and review queues belong only in external audit artifacts such as the task `REPORT.md` and `MANIFEST.json`.

Runtime readiness must be recomputed from the actual build artifacts every time. The adapter never claims that compact-index sweeping is semantically equivalent to indiscriminate full-body loading; its safety depends on index quality, complete coverage, exact-source escalation, and resolved findings.

## Medical-Content Boundary

This adapter changes retrieval architecture only. It does not validate, update, endorse, or correct inherited medical claims. Separate evidence review and qualified clinical oversight remain required before any real-world use.

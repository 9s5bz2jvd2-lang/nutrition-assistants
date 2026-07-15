# Mode C automatic plan + evidence contract (v3)

## Normative precedence

This document resolves any earlier Mode B/C wording in this candidate that suggests missing intake, unresolved non-botanical context, unassessed regulation, or a failed query should suppress a draft. The reviewable draft and evidence gap record are mandatory. Fail-closed behavior applies only to finalization, efficacy promotion, and market/regulatory claims.

## Input invariant

Preserve supplied values. Do not make the person repeat known fields. For missing medication, pregnancy/lactation, allergy, treatment history, target market, product category, or other context, record `UNKNOWN` and create a specific reminder/human-review task.

## Per-component state machine

`INGESTED → DRAFT_CREATED → TRIAGE_RECORDED → IDENTITY_ALIGNED or BLOCKED_IDENTITY → T1/T2/T3/T4_ATTEMPTED → REMINDERS_ASSEMBLED → REVIEWABLE_OUTPUT → HUMAN_FINALIZATION_REQUIRED`.

- `DRAFT_CREATED` is mandatory on every non-crash invocation.
- A botanical needs common/local name + Latin species + plant part + preparation/extract + marker constituent + dose unit before its own specific evidence query. Incompleteness is `BLOCKED_IDENTITY`, not deletion.
- Every search attempt yields a ledger row, including zero results, access errors, and blocks.
- Tracks: T1 human; T2 animal/in-vivo; T3 TCM/material; T4 regulatory.
- Safety/mechanism/interactions are sidecar reminders, never evidence tracks or efficacy proof.
- A human recorded decision is required for `HRF`; HRF does not by itself mean publishing, clinical clearance, regulatory clearance, or product release.

## Fixed output

1. **Individualized plan draft** — multi-domain plan; each component/form, proposed phase/use, selection basis, alternatives.
2. **Reminders** — medication/use time, interaction/adverse-event red flags, unknown intake, monitoring and review timing, uncovered evidence/regulation, human actions.
3. **Evidence package** — T1/T2/T3/T4 matrices with sources, query/date/locator, result/limits, no cross-tier promotion.
4. **Auditable gaps** — identity log, search ledger, regulatory matrix, residual risk/unknown matrix.

## Claim boundaries

- Animal dose/result ≠ human dose/result.
- Tradition/classical/monograph identity ≠ clinical efficacy.
- Mechanism/safety ≠ efficacy or regulation.
- `not found` scoped to sources/query/date ≠ no evidence exists.
- Unknown/`not_assessed` regulation ≠ clearance, and blocks only market/clearance claims.

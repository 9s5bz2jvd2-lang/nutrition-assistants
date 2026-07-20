# Evidence Governance

> **Purpose.** Define how claims are supported, contradicted, appraised, and
> limited in this workflow. This is a stricter, claim-level companion to
> `evidence-and-uncertainty.md`.

---

## 1  Claim taxonomy

Every statement that could be read as factual, clinical, or mechanistic must be
classified into one of the following claim types before it is emitted.

| Claim type | Example | Required support |
|---|---|---|
| **Definitions / scope** | "This workflow is educational, not clinical." | Workflow documents themselves; no external source needed. |
| **General biological fact** | "Magnesium is a cofactor in many enzymatic reactions." | Source Ledger entry (e.g., NIH ODS fact sheet) with explicit claim fit. |
| **Study-type methodological fact** | "RCTs support causal inference in the tested population." | Verified methodology source or textbook-style epidemiology reference. |
| **Provisional hypothesis** | "Low magnesium intake has been observed alongside muscle cramps in some reports." | Evidence card with support, contradiction, alternatives, falsifiers, and evidence debt. |
| **Professional reasoning / question generation** | "A clinician might consider checking electrolytes." | Clearly labeled as `PROFESSIONAL-REASONING / GENERATION-ONLY`; not claim support. |
| **Textbook / framework claim** | "Functional medicine uses seven physiological imbalance domains." | Tagged `textbook-claim`; may be recorded as context but not as clinical evidence. |

---

## 2  Evidence tiers and what they can support

| Tier | What it can support | What it cannot support |
|---|---|---|
| **Guideline / position statement** | Broad consensus statements, screening recommendations, red-flag thresholds. | Mechanistic or population-specific claims outside the guideline scope. |
| **Systematic review / meta-analysis** | Pooled direction of evidence, remaining uncertainty, heterogeneity. | Individual patient prediction, causality in untested populations. |
| **Randomized controlled trial (RCT)** | Causal effect in the included population, primary outcome, harms reported in the trial. | Generalization to other ages, comorbidities, doses, or durations. |
| **Observational study** | Association, hypothesis generation, real-world prevalence. | Causation, intervention efficacy, individual diagnosis. |
| **Mechanistic / in-vitro / animal study** | Biological plausibility, candidate mechanisms. | Human clinical efficacy or safety. |
| **Case report / case series** | First signal, rare event, teaching illustration. | Efficacy, population-level inference, clinical recommendation. |
| **Expert opinion / textbook claim** | Description of a framework or clinical practice pattern. | Verified efficacy, safety, or guideline replacement. |

---

## 3  Verification statuses

Every external source cited in a claim must carry one of these statuses.

| Status | Meaning | Permitted use |
|---|---|---|
| `FULL_TEXT_VERIFIED` | The full text was read and the specific claim is supported by its content. | Substantive factual or clinical claim support. |
| `BIBLIOGRAPHIC_ONLY` | Only citation metadata (title, identifier, retraction status) was verified. | Bibliographic existence, publication context, retraction check; **not** substantive findings. |
| `UNVERIFIED_LEAD` | A reference was found but not independently checked. | Quarantined; may be listed as a lead for future verification, never as claim support. |

---

## 4  Required fields for every sourced claim

When a claim is retained in an evidence card or output, the following must be
recorded:

1. **Source Ledger ID** (e.g., `[S02]`).
2. **Verification status** (`FULL_TEXT_VERIFIED`, `BIBLIOGRAPHIC_ONLY`, `UNVERIFIED_LEAD`).
3. **Specific claim supported** — quote or paraphrase the exact claim in the source that maps to the output statement.
4. **Claim fit / limitation** — explain why the source is applicable and what limits that applicability.
5. **Population match** — does the study population resemble the synthetic scenario?
6. **Harms / adverse events** — what was reported or not reported?
7. **Contradictions / alternatives** — are there contrary findings or competing explanations?
8. **Falsifiers** — what evidence would reduce confidence in this claim?

If any of fields 1–4 are missing, the claim is removed or downgraded to a
`question-generation note`.

---

## 5  Prohibited claim forms

The following sentence forms must never appear in output as assertions:

- "X causes Y."
- "X treats Y."
- "X prevents Y."
- "You should take X mg of Y."
- "Your SNP means you need Z."
- "Your labs show you have condition W."
- "This supplement will resolve your symptoms."

Permitted alternatives:

- "X has been observed alongside Y in [population]."
- "A [study type] reported that X was associated with [outcome] under [conditions]."
- "The evidence for X as a treatment for Y is [status]; a clinician can discuss whether it is relevant."

---

## 6  Handling contradiction

| Situation | Action |
|---|---|
| Two sources disagree on the same question | Retain both; label the conflict; note population or design differences that may explain it. |
| A source is retracted or corrected | Remove any claim supported only by that source; record the retraction in the evidence verification record. |
| A textbook claim conflicts with a guideline | Prefer the guideline for clinical scope; record the textbook claim as `textbook-claim` with the conflict noted. |
| No source supports a plausible hypothesis | Label it `SPECULATIVE / GENERATION-ONLY`; do not emit as a sourced claim. |

---

## 7  Full-text versus bibliographic boundaries

- A bibliographic-only citation may establish that a study exists, its title,
  authors, journal, year, PMID/DOI, and retraction status.
- It may **not** establish effect size, statistical significance, clinical
  relevance, safety, or applicability.
- If only the abstract is read, treat it as `BIBLIOGRAPHIC_ONLY` unless the
  abstract itself contains the specific claim and the claim is limited to the
  abstract's content.

---

## 8  Transition rule

No output may be finalized until every retained factual or clinical claim has
passed the checks above and every `UNVERIFIED_LEAD` is quarantined.

---

## 9  Version

| Field | Value |
|---|---|
| Version | 0.2.0 |
| Date | 2026-07-17 |
| Provenance | Clean-room synthesis. |

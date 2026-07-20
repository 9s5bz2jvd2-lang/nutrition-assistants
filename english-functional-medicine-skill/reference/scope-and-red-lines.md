# Scope and Red Lines

> **Purpose.** Define the permitted modes, privacy gates, safety stops, and
> human-review boundary of this workflow.

---

## 1  Permitted Modes

This workflow serves qualified health professionals and advanced learners in
three bounded modes:

1. **General education** — no case data; evidence questions only.
2. **Synthetic training** — wholly fictional, non-PHI teaching cases.
3. **Individual diagnostic support** — a licensed healthcare professional or
   governed clinical team uses authorized, minimum-necessary, de-identified
   individual case information to prepare a diagnostic-support draft.

In individual mode, the workflow may:

- organize reported and documented case facts without inventing information;
- identify red flags, missing data, contradictions, and reliability limits;
- produce a problem representation and ranked differential-diagnosis support;
- show evidence for and against each candidate, case applicability,
  uncertainty, alternatives, and not-to-miss possibilities;
- list discriminating questions or evaluations for the licensed reviewer to
  consider, without issuing orders;
- require the reviewer to approve, revise, or reject the draft.

It does not release a final patient-facing diagnosis. It does not treat,
prescribe, dose, change medications, order tests, or execute care.

> **Six-Eye integration.** Six-Eye is used once for completeness after intake
> and triage. It remains `internal design / unvalidated`, not a diagnostic instrument.

---

## 2  Required User, Data, and Environment Conditions

Individual diagnostic-support mode may proceed only when all conditions hold:

- **Qualified reviewer:** the intended reviewer is a licensed healthcare
  professional or a governed clinical team operating within its competence.
- **Authorization:** the user attests to lawful authority to process the case
  for the stated professional purpose.
- **Minimum necessary:** only information needed for the diagnostic question is
  included.
- **De-identification:** direct identifiers are removed before entry.
- **Approved handling:** the user is responsible for an appropriately governed
  environment, access control, retention, and deletion. This Skill package
  is not itself a certified clinical data system.
- **Human sign-off:** no diagnostic-support draft is released as a clinical
  conclusion until the responsible licensed reviewer explicitly signs off.

Do not enter names, exact dates of birth, full addresses, phone numbers, email
addresses, medical-record numbers, account numbers, provider identifiers,
face images, or equivalent direct identifiers. Use a local pseudonymous case
key. Relative timelines are preferred when exact dates are unnecessary.

If direct identifiers or unnecessary PHI appear, stop, quarantine the draft,
remove the identifiers outside the workflow, and restart only with a safe
minimum-necessary de-identified input.

---

## 3  What This Workflow Is Not

| It is NOT | Boundary |
|---|---|
| An autonomous diagnostician | It drafts ranked differentials; a licensed reviewer owns the final diagnosis. |
| A direct-to-patient diagnosis service | Patient-facing self-diagnosis requests are redirected to qualified care. |
| An autonomous treatment planner or prescriber | It may produce class-gated food guidance or reviewer-facing supplement, medical-nutrition and TCM drafts under `formula-class-gates.md`; it does not independently prescribe, execute care, change medication, or release a high-risk draft without the required reviewer. |
| An ordering system | It may list discriminating information for clinician consideration, but issues no laboratory, imaging, referral, or medication orders. |
| An emergency service | Acute red flags stop routine reasoning immediately. |
| A validated clinical instrument | Six-Eye and the workflow itself have not been clinically validated. |
| A replacement for standard care | Guideline-recognized evaluation and the responsible clinician remain authoritative. |
| A certified PHI platform | Identified PHI is outside this Skill's ordinary file workflow. |
| A proprietary body-system taxonomy | It does not assign branded domain or matrix codes. |

---

## 4  Red-Flag Escalation — Immediate Exit Rules

The following are hard stops for routine diagnostic-support work:

- chest pain, pressure, or tightness;
- sudden facial drooping, arm weakness, or speech difficulty;
- severe or worsening shortness of breath;
- uncontrolled bleeding;
- loss of consciousness or unresponsiveness;
- sudden severe headache;
- signs of anaphylaxis;
- suicidal ideation or self-harm statements;
- suspected poisoning or overdose.

When a red flag is detected:

1. stop routine hypothesis and differential generation;
2. state that urgent in-person or emergency evaluation is required;
3. do not delay escalation by continuing the ordinary workflow;
4. record only a minimal fact-bound stop notice.

> Based on general emergency-triage sources in the Source Ledger [S01], [S07].

---

## 5  Mandatory Refusal or Escalation Domains

The workflow must refuse or escalate:

- consumer requests for a final diagnosis without qualified clinical review;
- any request to autonomously prescribe or execute treatment, start/stop/switch medication, order tests, or bypass the class-specific reviewer/release gate;
- emergency-management instructions beyond immediate escalation;
- supplement or food claims that promise to cure, treat, or prevent disease;
- deterministic genetic or SNP claims;
- diagnostic conclusions based only on mechanism, a single biomarker,
  proprietary testing, or a disputed functional-medicine label;
- work containing direct identifiers or unnecessary PHI;
- cases outside the stated professional's competence or authorization.

Specific laboratory results may be considered only in authorized individual
mode, with units, reference context, provenance, and uncertainty preserved.
A value is evidence, not a diagnosis by itself.

---

## 6  Mandatory Wording

Every individual output must include:

> **PROFESSIONAL DIAGNOSTIC-SUPPORT DISCLAIMER**
>
> This is a clinical decision-support draft for licensed-professional review.
> It is not medical advice to a patient and not a final diagnosis.

It must also state that the diagnostic-support draft itself authorizes no treatment, prescription, medication change, test order, or autonomous clinical action. Any separately requested formula/plan output must carry its own class-specific release state and required reviewer; an incomplete or unreviewed high-risk draft is not executable.

---

## 7  Evidence Standards

| Category | Rule |
|---|---|
| Government and guideline sources | Prefer current authoritative guidance for recognized diagnostic criteria and red flags. |
| Peer-reviewed literature | Verify identifier, retraction status, study design, population, claim fit, and limitations. |
| Bibliographic-only records | Establish citation existence only; do not support substantive findings. |
| Professional reasoning | May generate candidates, but cannot substitute for source support. |
| Diagnostic criteria | State version, population, threshold source, exclusions, and applicability. |
| Case fit | Record supporting facts, contradictions, missing data, and alternative explanations. |
| Contested functional labels | Mark disputed status and do not displace guideline-recognized differentials. |
| Quotations | No source passage longer than 25 consecutive words. |

---

## 8  Systems-Oriented Reasoning Principles

Use chronology, thematic grouping, Six-Eye completeness, evidence cards,
contradiction tracking, and falsifiers to widen rather than prematurely close
the differential. Keep case facts distinct from interpretation. Preserve
unknowns and dissent. Never turn a plausible mechanism into a diagnosis.

---

## 9  Version and Change Log

| Version | Date | Summary |
|---|---|---|
| 0.3.0 | 2026-07-18 | Added authorized de-identified individual diagnostic support with licensed-reviewer sign-off; retained no-treatment/prescribing/dosing and emergency boundaries. |
| 0.1.0 | 2026-07-17 | Initial synthetic educational scope. |

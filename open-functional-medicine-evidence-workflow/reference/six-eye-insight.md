# Six-Eye Insight (Six-Eye completeness prompt)

> **Origin**: Human-designed completeness prompt that Wang Runyuan identifies
> as her original work, restated here in a clean room as the
> "H0 (etiology exploration) + Six-Eye completeness prompt" step. Detailed
> provenance is retained in the maintainer's private records.

> **Label**: internal design / unvalidated completeness prompt. This is NOT a
> validated clinical tool, NOT a diagnostic method, NOT a treatment framework.

---

## 1  Purpose

Provide a structured, six-lens completeness check that identifies
**missing information and open questions** before any hypothesis work.
The lenses are designed to reduce blind spots by prompting for
dimensions that a purely biomedical review might overlook.

---

## 2  The Six Lenses

| # | Name | What to ask / observe | Type |
|---|---|---|---|
| 1 | **Body** (body) | Body/medical/nutrition observations and missing data. What physical findings are present? What medical or nutritional data is absent? | Observation gap |
| 2 | **Mind** (mind) | Emotional/cognitive/psychological context as questions, not labels. What mood, thought-pattern, or cognitive observations are present or missing? | Observation gap |
| 3 | **Behavior** (behavior) | Behavior/adherence/environmental-pattern questions. What daily behaviors, routines, or environmental patterns are reported or unreported? | Observation gap |
| 4 | **Relationship** (relationship) | Relationship/system/caregiving-context questions. What social supports, caregiving dynamics, or system-level factors are present or unknown? | Observation gap |
| 5 | **Time** (time) | Onset/course/sequence/timing questions. What is the temporal pattern? When did things begin, change, worsen? What sequence of events is documented or unclear? | Observation gap |
| 6 | **Cause** (cause) | Competing etiologic hypotheses, support, contradiction, alternatives, and falsification information — NEVER proof of causation. What competing explanations exist? What supports or contradicts each? What would rule each out? | Hypothesis scaffold |

---

## 3  Invocation Rules

| Rule | Detail |
|---|---|
| **When** | Once per case, after intake/triage, before hypothesis review |
| **Input** | Case facts only — not lane opinions, not new case facts, not diagnoses |
| **Output** | Missing-item/question list + at most one bounded H0 |
| **Fact vs hypothesis** | Each item distinguishes "observed fact" from "hypothesis" |
| **Unknown preserved** | `unknown / none of these` is always a valid response |
| **H0 bound** | At most one bounded, optional hypothesis (H0) per case |
| **H0 content** | Must include: supporting evidence, contradicting evidence, alternative hypotheses, falsification/differentiation information, evidence debt |
| **Label required** | Output is labeled internal design / unvalidated |
| **Failure/anchoring** | If anchoring risk or failure: status → `NO_DRAFT` or `ISSUE_EVIDENCE_ONLY`; empty/incomplete/failed output is permitted |

---

## 4  Safety Constraints

| Constraint | Detail |
|---|---|
| NOT a diagnostic tool | Must never be called a "deep diagnosis / rapid diagnostic tool" |
| No diagnosis/prescription | Does not diagnose, prescribe, or infer treatment |
| No causation claims | Cause lens explores competing hypotheses — never proves causation |
| Legacy framework excluded | The old functional-medicine framework is NOT included in this Skill and must not serve as default H0, causal chain, or clinical authority |
| Unvalidated label | Every output must carry: "internal design / unvalidated completeness prompt" |
| Human review required | Output is AI draft / pre-MDT workup only; adoption requires named human professional review |

---

## 5  Integration with This Workflow

| Where | How the six-eye connects |
|---|---|
| Intake | Structured intake collects facts; six-eye identifies what the intake missed |
| Evidence and uncertainty | Six-eye missing items feed into the contradiction register and evidence debt |
| Evidence cards | Cause lens directly informs the competing-hypotheses / falsifier fields |
| Output contract | Six-eye completeness status appears in the review summary |

---

## 6  What This Is NOT

- NOT a standalone diagnostic or triage tool
- NOT a validated instrument — no psychometric validation, no clinical trial
- NOT a proprietary branded framework
- NOT a replacement for clinical history-taking
- NOT causal proof of any relationship between observations

---

## 7  Version and Change Log

| Version | Date | Summary |
|---|---|---|
| 0.1.0 | 2026-07-17 | Initial clean-room restatement. |

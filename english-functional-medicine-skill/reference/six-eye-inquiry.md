# Six-Eye Inquiry (Six-Eye completeness prompt)

> **Origin.** Wang Runyuan asserts the Six-Eye lens as her human-original
> completeness prompt. This document is a clean-room restatement for educational use.
>
> **Label.** `internal design / unvalidated completeness prompt`. It is **NOT** a
> diagnostic tool, treatment framework, or validated clinical instrument.

---

## 1  Purpose

Run the Six-Eye lens once per synthetic teaching case, after intake/triage and
before hypothesis review, to identify **missing information and open questions**.
It reduces blind spots by asking for dimensions that a purely biomedical intake
might overlook.

---

## 2  The six lenses

| # | Lens | What to ask | What is missing? |
|---|---|---|---|
| 1 | Body | Physical and medical observations: symptoms, signs, functional capacity, reported lab values (as facts, not interpretations). | What physical data have not been reported? What body systems have not been described? |
| 2 | Mind | Emotional, cognitive, psychological, and meaning-related context. | What mood, thought patterns, beliefs, or cognitive symptoms are absent? |
| 3 | Behavior | Daily routines, habits, adherence, movement, sleep, substance use, screen time. | What behaviors or environmental patterns are unknown? |
| 4 | Relationship | Social support, caregiving, family dynamics, work culture, access to care, food access. | What relational or system-level factors are missing? |
| 5 | Time | Onset, course, sequence, duration, cyclical patterns, life-stage transitions. | When did things begin? What changed and in what order? What temporal clues are absent? |
| 6 | Cause | Competing explanations for the observations — support, contradiction, alternatives, and falsifiers. | What other hypotheses could explain the same facts? What would rule each out? |

---

## 3  Invocation rules

| Rule | Detail |
|---|---|
| **When** | Once per case, after triage, before hypothesis generation. |
| **Input** | Case facts only. No lane opinions, no new case facts, no diagnoses. |
| **Output** | Missing-item/question list plus at most one bounded H0. |
| **Fact vs. hypothesis** | Each item must distinguish "observed fact" from "hypothesis." |
| **Unknown preserved** | `unknown / none of these` is always a valid response. |
| **H0 bound** | At most one optional, bounded hypothesis per case. |
| **H0 content** | Must include: supporting evidence, contradicting evidence, alternative hypotheses, falsification/discrimination information, and evidence debt. |
| **Label** | Output must carry: `internal design / unvalidated completeness prompt`. |
| **Failure mode** | If anchoring or failure risk is high, output `NO_DRAFT` or `ISSUE_EVIDENCE_ONLY`. |

---

## 4  The optional bounded H0

A bounded H0 is a provisional working hypothesis, not a diagnosis. It must be
clearly separated from observed facts.

### Required H0 fields

1. **H0 statement** — one sentence, association language only.
2. **Supporting evidence** — observed facts and/or verified sources.
3. **Contradicting evidence** — facts or sources that argue against H0.
4. **Alternative hypotheses** — at least one competing explanation.
5. **Falsifier / discriminator** — what would rule H0 out or distinguish it from alternatives.
6. **Evidence debt** — what is missing that would change confidence.
7. **Status** — `done`, `incomplete`, `failed`, `NO_DRAFT`, or `ISSUE_EVIDENCE_ONLY`.

### Example H0 form (hypothetical, not clinical)

> **H0:** In this synthetic scenario, reported fatigue and low activity are
> associated with reported sleep disruption and high self-rated stress; a
> conventional medical evaluation for thyroid, anemia, and mood disorder has not
> yet been described.
>
> *This is a question organizer, not a diagnosis.*

---

## 5  Safety constraints

| Constraint | Detail |
|---|---|
| NOT a diagnostic tool | Must never be called a "deep diagnosis" or "rapid diagnostic tool." |
| No prescription | Does not recommend treatments, supplements, doses, or medication changes. |
| No causation claims | The Cause lens explores competing hypotheses; it never proves causation. |
| Legacy framework excluded | The old functional-medicine seven-imbalance framework is not used as the default H0 or clinical authority. |
| Unvalidated label | Every output must state: `internal design / unvalidated completeness prompt`. |
| Human review required | Output is an AI draft; adoption requires named human professional review. |

---

## 6  Integration with the workflow

| Stage | How Six-Eye connects |
|---|---|
| Intake | Structured intake collects facts; Six-Eye identifies what is missing. |
| Evidence cards | Missing items feed into evidence debt and contradiction register. |
| Cause lens | Directly informs the competing-hypotheses / falsifier fields. |
| Output | Six-Eye completeness status appears in the review summary. |

---

## 7  What this is NOT

- NOT a standalone diagnostic or triage tool.
- NOT a validated instrument — no psychometric validation, no clinical trial.
- NOT a proprietary branded framework.
- NOT a replacement for clinical history-taking.
- NOT causal proof of any relationship between observations.

---

## 8  Version and provenance

| Field | Value |
|---|---|
| Version | 0.2.0 |
| Date | 2026-07-17 |
| Origin | Wang Runyuan's asserted human-original Six-Eye lens |
| Provenance | Clean-room restatement; detailed provenance is retained in the maintainer's private records. |

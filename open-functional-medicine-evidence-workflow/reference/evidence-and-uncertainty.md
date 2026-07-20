# Evidence and Uncertainty

> **Purpose.** Define how observations are sorted, how provisional
> hypotheses are formed, how evidence is appraised by study type, and
> how uncertainty, contradiction, and evidence debt are tracked.

---

## 1  Observation Sorting (Step 1)

All information from the intake is sorted into two categories:

| Category | Description | Label |
|---|---|---|
| **Observed Facts** | Directly reported by the person or documented in their health history. Data points, not interpretations. | `FACT` |
| **Reported Context** | Environmental, social, occupational, or lifestyle details provided by the person. Contextual, not diagnostic. | `CONTEXT` |

### Rules

- No raw observation may be mislabeled as a conclusion or diagnosis.
- Laboratory values remain facts with units, reference context, timing, and provenance. In authorized individual mode, interpretation is written separately, sourced, and qualified by clinical context; a value alone cannot establish a diagnosis.
- Contradictions between reported or documented facts are flagged and remain visible unless a licensed reviewer resolves them with evidence.
- Each observation is organized by the factual content it contains,
  not by a body-system taxonomy. Organize by chronology, theme, or
  source — whatever best serves clarity.

---

## 2  Six-Eye Completeness Check (Step 2)

After sorting observations, run the Six-Eye completeness lens
(see `reference/six-eye-insight.md`) once to identify:

- **Missing information** across the six dimensions (Body, Mind, Behavior,
  Relationship, Time, Cause)
- **Outstanding questions** the intake did not answer
- **At most one bounded H0** (optional) with support, contradiction,
  alternatives, falsifiers, and evidence debt

Output: a missing-item list plus the optional H0. Label as
"internal design / unvalidated". See `six-eye-insight.md` §3 for complete rules.

---

## 3  Evidence Appraisal by Study Type (Step 3)

### 3.1  Contextual Evidence Classification

Evidence is classified by its study design and publication context.
There is no single universal ranking; applicability depends on the
specific claim, population, and question.

| Evidence Type | Context | Typical Strengths | Typical Limitations |
|---|---|---|---|
| **Guideline / Position Statement** | Expert panels convened by professional societies or government bodies | Broad consensus, systematic evidence review | May lag behind new findings; may reflect local practice norms |
| **Systematic Review** | Predefined protocol, comprehensive search, quality appraisal of included studies | Reduces selection bias; summarizes body of evidence | Quality depends on included studies; may mix heterogeneous populations |
| **Meta-Analysis** | Quantitative pooling of effect estimates from multiple studies | Increases statistical power; provides pooled effect estimate | Susceptible to publication bias, heterogeneity, ecological fallacy |
| **Randomized Controlled Trial (RCT)** | Random allocation, controlled comparison | Strongest for causal inference in the tested population | Narrow inclusion criteria; may not generalize; often short duration |
| **Observational Study** (cohort, case-control, cross-sectional) | No random allocation; measures associations | Reflects real-world populations; can study rare exposures/outcomes | Confounding, selection bias, reverse causation; association ≠ causation |
| **Mechanistic / In-Vitro / Animal Study** | Laboratory or preclinical | Generates hypotheses; explores biological plausibility | Cannot directly establish human clinical relevance; dose/context gaps |
| **Case Report / Case Series** | Individual or small-group clinical narratives | First signal of rare events; hypothesis-generating | No control group; no statistical inference; publication bias |

### 3.2  Applicability Assessment

For every evidence claim used in this workflow, document:

| Field | Description |
|---|---|
| **Population** | Who was studied? Age, sex, health status, setting. |
| **Intervention / Exposure** | What was tested or observed? |
| **Comparator** | What was the comparison group or condition? |
| **Outcome(s)** | What was measured? Primary and secondary. |
| **Effect Estimate** | Magnitude and direction (e.g., OR, RR, mean difference) with confidence interval if available. |
| **Applicability** | Does this study population and context match the person's situation? What limits generalizability? |
| **Limitations** | Design limitations, bias risks, confounding factors. |
| **Harms / Adverse Events** | What adverse effects were reported or not reported? |

### 3.3  Verification Requirements

| Requirement | Detail |
|---|---|
| **Title verification** | Confirm the cited title matches the actual publication. |
| **Identifier check** | Verify DOI or PMID exists and resolves to the cited work. |
| **Retraction/correction status** | Check whether the work has been retracted or corrected (e.g., via PubMed retraction notices). |
| **Publication context** | Note if the work is a preprint, conference abstract, or peer-reviewed article. |

> **Professional reasoning** (practitioner training/experience) may
> generate questions and hypotheses but **may NOT by itself support
> an external factual or clinical claim**. All such reasoning must
> be declared as `PROFESSIONAL-REASONING` and labeled `PROVISIONAL`.

---

## 4  Provisional Hypothesis Formation (Step 4)

### 4.1  What Counts as a Provisional Hypothesis

A provisional hypothesis is a **question-generating possible connection**
between two or more observations. It is:

- Always labeled: `PROVISIONAL — not a clinical conclusion`
- Generated from observed facts, sourced evidence, or explicitly declared
  professional reasoning; professional reasoning is a **generation cue**,
  not external factual or clinical support
- Never a diagnosis, disease prediction, or treatment suggestion

### 4.2  Hypothesis Generation / Support Status

| Status | Meaning | Label |
|---|---|---|
| **Sourced** | Supported by a source in the Ledger with a verified bibliographic identifier and explicit claim fit | `SOURCED` |
| **Professional-Reasoning Generated** | A practitioner proposed a question from training/experience; it has no independent evidentiary support until a source is verified | `PROFESSIONAL-REASONING / GENERATION-ONLY` |
| **Speculative** | Plausible question but no current supporting evidence found | `SPECULATIVE / GENERATION-ONLY` |

All statuses require the `PROVISIONAL` label. Only `SOURCED` may be
described as evidentially supported; generation-only items must remain in a
separate question-generation note and must not be emitted as Evidence Cards
or presented as external factual or clinical claims until an eligible source
is verified.

### 4.3  Rules

- A hypothesis must never use disease-causal language ("X causes Y").
  Use association language: "X has been observed alongside Y in some
  reported contexts."
- A hypothesis must never recommend a specific intervention or dosage.
- If two hypotheses contradict, both are retained with an explicit
  contradiction note.
- Each hypothesis must include:
  - Supporting evidence (observations and/or source entries)
  - Contradicting or contrary evidence (if any)
  - Alternative hypotheses
  - Information that would falsify or differentiate the hypothesis
  - Evidence debt: what is missing that would increase or decrease
    confidence

---

## 5  Relationship to Individual Differential Diagnosis

A provisional H0 or evidence question is not automatically a diagnosis. In authorized individual mode, the separate diagnostic-support synthesis may rank recognized candidate diagnoses only after:

1. adequate de-identified case context and provenance are present;
2. red-flag, authorization, and competence gates pass;
3. diagnostic criteria or authoritative evidence are identified;
4. support, contradiction, alternatives, not-to-miss conditions, applicability, and missing data are shown;
5. a licensed reviewer approves, revises, or rejects the draft.

Disputed functional labels may appear only in the contested-label register, never as established diagnoses. Treatment and dosing remain outside scope.

---

## 6  Source-Claim Verification Rule

Every external factual, medical, nutrition, safety, or clinical claim in
the output must be traceable to a Source Ledger entry via its source ID.

| Claim Type | Verification Rule |
|---|---|
| Specific nutrient role | Must have a Source Ledger entry (typically NIH ODS fact sheet) |
| Drug-supplement interaction | Must have a Source Ledger entry (typically NCCIH or MedlinePlus) |
| General health-systems factual claim | Must have a Source Ledger entry with explicit claim fit; professional reasoning alone is insufficient |
| Red-flag threshold | Must cite a verified government or professional triage source |
| Evidence-study-type classification | Must cite the study title/PMID/DOI or verified methodological source in the ledger |

If no source exists for an external factual or clinical claim, the claim
is removed. Professional reasoning may remain only as a clearly labeled
**question-generation note** that asserts no external fact, efficacy,
causation, diagnosis, or treatment implication.

---

## 6  Contradiction and Uncertainty Register (Step 5)

Maintain a running register of all unresolved tensions:

| Field | Description |
|---|---|
| `contradiction_id` | Sequential number |
| `observations` | The two or more conflicting items |
| `nature_of_conflict` | Brief description of why they conflict |
| `resolution_status` | `UNRESOLVED` / `RESOLVED` (with note) / `DEFERRED-TO-CLINICIAN` |

---

## 7  Evidence Verification Record

For each source used in a hypothesis or claim, record:

| Field | Description |
|---|---|
| `source_id` | Source Ledger ID (e.g., `[S01]`) |
| `verification_status` | One of: `FULL_TEXT_VERIFIED`, `BIBLIOGRAPHIC_ONLY`, `UNVERIFIED_LEAD` |
| `identifier` | PMID, DOI, or URL |
| `retraction_status` | `ACTIVE` / `RETRACTED` / `CORRECTED` / `UNKNOWN` |
| `population_match` | Does the study population match the case context? Brief note. |
| `applicable_limitations` | Key limitations affecting applicability to this case. |

### Verification Status Definitions

| Status | Meaning |
|---|---|
| `FULL_TEXT_VERIFIED` | The full text was reviewed and the claim is supported by the actual content. |
| `BIBLIOGRAPHIC_ONLY` | Only citation existence/metadata was checked. It may support title/identifier/publication-status metadata only and must not support a substantive factual or clinical finding. |
| `UNVERIFIED_LEAD` | A reference was found (e.g., cited in another work) but the original has not been independently checked. |

---

## 8  Transition to Output

Only after:
1. All observations are sorted and labeled, AND
2. Six-Eye completeness check is recorded, AND
3. Evidence claims are appraised by study type with verification record, AND
4. All provisional hypotheses carry required labels and falsifier fields, AND
5. The contradiction register is reviewed (unresolved items noted), AND
6. Every factual claim has a Source Ledger trace

may the workflow proceed to `output-contract.md`.

---

## 9  Template References

- Evidence card: `assets/evidence-card-template.md`
- Review output: `assets/review-output-template.md`

---

## 10  Version and Change Log

| Version | Date | Summary |
|---|---|---|
| 0.1.0 | 2026-07-17 | Initial clean-room creation — RCT governance layer, no domain taxonomy. |

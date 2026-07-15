# Personalized Selection Flow — Human-in-the-Loop Draft Route

> **Schema version:** `personalized-selection-v2.0`
> **Supersedes:** `personalized-selection-v1.0` (per HUMAN_REVIEW_POLICY + REMINDER_OUTPUT deltas)
> **Purpose:** Define the transparent, ordered route for generating a personalized formula draft AND its reminder package as co-products. ALL triage statuses produce a draft with visible gaps/reminders. Only automated finalization is gated.

---

## 1. Overview

The personalized selection flow operates for **every** personalized request. It always produces:
1. A professional working-plan draft (with assumptions, unknowns, exclusions, evidence tiers)
2. A structured reminder/checklist package (with source/trigger/severity/action-owner)

The flow does NOT halt based on triage status. Missing data, high-risk factors, evidence gaps, and regulatory gaps flow into the reminder package.

**Prerequisites:**
1. ✅ Intake contract fulfilled (per `reference/individualized_formula_intake_contract.md`)
2. ✅ Risk triage assigned (per `reference/risk_triage_contract.md` v2.0)
3. ✅ Consent to process health data = true

---

## 2. Ordered Selection Route (Seven Stages)

### Step 1: Intake Completeness & Triage Confirmation

```
VERIFY:
  - Intake fields present or explicitly marked unknown/missing
  - Triage status assigned (any draft-capable status)
  - Consent = true
IF missing fields:
  → Generate information_gap reminders for each
  → Apply safe assumptions where documented; mark as "assumed"
  → Proceed to Step 2 (do not halt)
IF red flags:
  → Generate safety_interaction reminders with severity=critical
  → Proceed to Step 2 (do not halt)
```

### Step 2: Identify Individual Constraints & Exclusions

Extract from the intake record. For each constraint, generate relevant reminders:

| Constraint Category | Source Fields | Action | Reminder Generated |
|--------------------|---------------|--------|-------------------|
| **Drug interactions** | `current_prescription_medications` | Cross-reference with Track 4 | safety_interaction per interaction signal |
| **Allergies/intolerances** | `allergies_intolerances` | Exclude matching ingredients | safety_interaction for each exclusion |
| **Life-stage** | `age_or_life_stage`, pregnancy/lactation | Apply special-population gates | safety_interaction with severity per risk |
| **Organ function** | `hepatic_status`, `renal_status` | Adjust/exclude | safety_interaction for dose adjustments |
| **Identity requirements** | `botanical_identity_requirements` | Pre-fill identity gate | information_gap for unresolved identities |
| **Preferences (soft)** | `diet_pattern`, practical preferences | Soft constraints | info-level reminder if not accommodated |
| **Cultural/TCM context** | `cultural_tcm_context` | Contextual input | No reminder (context only) |

**Critical rule:** Preferences CANNOT override identity, safety, or regulatory failures.

### Step 3: Select Generic Evidence-Supported Candidates

Using the existing two-pass corpus scan (Phase A + Phase B):
1. Identify relevant body systems from `intended_use_goal`, `symptoms`, `diagnoses`
2. Select highest-relevance expert nodes
3. Load and deeply read selected passages (Phase A)
4. Execute corpus-wide omission/safety sweep (Phase B)
5. Extract candidate nutrients/supplements with dose ranges, contraindications, synergies

**Evidence population caveat:** All evidence is population-level by default.

### Step 4: Execute Four Evidence Tracks + Regulatory Gate

For each candidate ingredient, execute all four evidence tracks per `reference/layer8_evidence_query.md` and regulatory assessment per `reference/regulatory_gate.md`.

For each evidence/regulatory finding, generate reminders:

| Finding | Reminder Category | Severity |
|---------|-------------------|----------|
| Animal-only evidence | evidence | important |
| Traditional-only evidence | evidence | important |
| Absent human evidence | evidence | critical if ingredient relies on it |
| Conflicting evidence | evidence | important |
| Drug interaction signal | safety_interaction | important/critical |
| Regulatory unknown for jurisdiction | regulatory_product | important |
| Regulatory prohibited | regulatory_product | critical |

### Step 5: Compare Against Person-Specific Constraints

Cross-reference generic candidates against individual constraints from Step 2:

| Check | Logic | Reminder Generated |
|-------|-------|-------------------|
| Drug-nutrient interaction | Track 4 signals vs. medications | safety_interaction per interaction |
| Allergy match | Identity vs. allergies | safety_interaction (exclusion) |
| Life-stage safety | Special-population rules | safety_interaction per flag |
| Organ function | Dose vs. hepatic/renal status | safety_interaction (adjustment) |
| Lab context | Informational only | info-level |
| Form preference | Soft match | info-level if not accommodated |

### Step 6: Produce Draft + Reminders Together (Co-Products)

Generate BOTH simultaneously using:
- `templates/personalized_formula_draft_template.md` (draft plan)
- `templates/reminder_package_template.md` (reminder package)

The draft includes:
1. Intake data provenance (user-reported/verified/unknown/assumed)
2. Triage status and reason
3. Individual constraints considered
4. Excluded ingredients with reasons and alternatives
5. Draft formula composition (phases: 强化期 → 维持期)
6. Evidence summary per ingredient (4 tracks, labeled by tier)
7. Regulatory coverage matrix
8. Assumptions applied (with explicit "assumed, not verified" markers)
9. **Reminder package section** (all 6 categories)
10. Professional-review checklist
11. Follow-up questions
12. Limitations and uncertainties
13. Human decision record section (for personalized selection step 5)

### Step 7: Await Human Review / Decision

```
Output triage status = one permitted v2 status selected at Step 2 (`draft_for_professional_review` for a standard no-risk draft)
Human decision = pending
Human decision recorded = false
Human reviewer sees: draft + reminders + checklist
Reviewer options: accept / modify / defer / specialist_referral
System records: human decision with timestamp and rationale
Auto-finalization blocked until human decision recorded
```

---

## 3. Population-Level Evidence Disclaimer

Every draft includes:

> **重要声明 / Important Notice:**
> 本个性化配方便方所引用的证据均为群体水平研究，不能证明对个体的具体疗效。本便方仅供专业人员审阅参考，不构成医疗处方或治疗保证。
>
> The evidence cited is population-level and does NOT prove specific efficacy for any individual. This draft is for professional review only and does NOT constitute a prescription or treatment guarantee.

---

## 4. Dose Derivation Prohibition

> **NEVER derive or recommend a human dose by scaling an animal study dose or traditional-use amount.**
> If only animal or traditional evidence is available → the ingredient is flagged with NO human dose recommendation.

---

## 5. Audit Trail

Every draft produces a privacy-minimized audit ledger entry recording: request ID, provenance, triage, constraints, exclusions, evidence tiers, regulatory summary, reminders generated, personalized selection stage, and timestamps. **No personal identifiers.**

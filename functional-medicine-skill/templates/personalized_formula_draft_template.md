# Template: Personalized Formula Draft — Professional Working Plan

> **Schema version:** `personalized-draft-template-v2.0`
> **Supersedes:** v1.0 (per HUMAN_REVIEW_POLICY + REMINDER_OUTPUT + PERSONALIZED_SELECTION deltas)
> **Usage:** Generated for EVERY personalized request regardless of triage status. The output is ALWAYS a professional working draft with assumptions, unknowns, and reminders. Auto-finalization is blocked until human decision recorded. Co-produced with `templates/reminder_package_template.md`.

---

## 0. Review Status Banner

```
┌──────────────────────────────────────────────────────────────────────┐
│ ⚠️  个性化配方/方案专业工作便方 — 人类在环审阅                          │
│ PERSONALIZED FORMULA PROFESSIONAL WORKING DRAFT — HUMAN-IN-THE-LOOP │
│                                                                       │
│ Triage Status: [IDNHI / DUSF / DMHR / DRG / DFPR / HRF]               │
│ Personalized Selection Stage: [1-7]                                                 │
│ This is NOT a prescription, diagnosis, or treatment guarantee.        │
│ Auto-finalization blocked. Human reviewer decision required.          │
│ Population-level evidence does NOT prove individual outcome.          │
└──────────────────────────────────────────────────────────────────────┘
```

### Complete v2 Triage Status Enumeration

| Abbreviation | Full Status Name | Description |
|---|---|---|
| IDNHI | `incomplete_draft_needs_human_input` | Missing or unresolvable required fields; draft generated with assumptions and information-gap reminders; human reviewer decides next step |
| DUSF | `draft_with_urgent_safety_flag` | Acute safety concern detected; draft generated with URGENT safety flag and emergency referral reminder; auto-finalization blocked |
| DMHR | `draft_with_mandatory_human_review` | High-risk identifier present (pregnancy, complex multimorbidity, drug interaction risk); draft generated with mandatory professional review required |
| DRG | `draft_with_regulatory_gap` | Regulatory assessment incomplete for one or more target jurisdictions; draft generated with regulatory gap reminders |
| DFPR | `draft_for_professional_review` | All required fields present, no high-risk identifiers; draft generated for standard professional review |
| HRF | `human_reviewed_finalization` | Human reviewer has documented a decision in §13 (accept/modify/defer/specialist_referral). **Requires an actual, documented human confirmation/decision record.** Does NOT convert a model draft into autonomous prescription, medical validation, legal clearance, or automatic release. |

> **Binding rule:** Every status generates a professional working draft and a co-produced reminder package. Only `human_reviewed_finalization` indicates that a human has reviewed and decided; it still does not constitute a medical prescription or regulatory clearance.

---

## 1. Intake Data Provenance

| Field | Value | Provenance | Assumption Applied? |
|-------|-------|-----------|-------------------|
| Request ID | | auto-generated | — |
| Intended Use / Goal | | required | |
| Target Markets | | required | |
| Product Category | | required | |
| Age / Life Stage | | required | |
| Sex | | conditional | |
| Pregnancy Status | | conditional | |
| Lactation Status | | conditional | |
| Symptoms | | user_reported | |
| Diagnoses | | user_reported / verified | |
| Clinical History | | user_reported | |
| Relevant Labs | | user_reported / verified | |
| Current Medications | | required / user_reported / verified | |
| OTC Drugs | | required | |
| Current Supplements | | required | |
| Allergies/Intolerances | | required | |
| Hepatic Status | | conditional | |
| Renal Status | | conditional | |
| Diet Pattern | | optional | |
| Preferences | | optional | |

**Provenance summary:** [X] verified, [Y] user_reported, [Z] unknown/missing, [W] assumed

---

## 2. Triage Status & Reason

| Field | Value |
|-------|-------|
| Triage Status | `IDNHI` / `DUSF` / `DMHR` / `DRG` / `DFPR` / `HRF` (human_reviewed_finalization) |
| Combined Statuses | (if multiple conditions apply) |
| Triage Reason | (specific identifiers) |
| Red Flags | (if any, with severity) |
| High-Risk Identifiers | (list) |
| Regulatory Gaps | (list uncovered jurisdictions) |
| Auto-Finalization | **Blocked** (human decision required) |

---

## 3. Individual Constraints Considered

| # | Constraint | Source | Action | Reminder Generated |
|---|-----------|--------|--------|-------------------|
| 1 | Drug interaction | medications | Excluded / Flagged / Adjusted | safety_interaction |
| 2 | Allergy/intolerance | allergies | Excluded | safety_interaction |
| 3 | Life-stage | age/pregnancy/lactation | Flagged / Adjusted | safety_interaction |
| 4 | Organ function | hepatic/renal | Adjusted / Excluded | safety_interaction |
| 5 | Lab context | labs | Informational | info |
| 6 | Identity | botanical_requirements | Resolved / Flagged | information_gap (if unresolved) |

---

## 4. Assumptions Applied

| # | Assumption | Field | Reason | Verification Needed |
|---|-----------|-------|--------|-------------------|
| | (e.g., "Target market: China assumed when not specified") | | | Yes — human_reviewer |

---

## 5. Excluded Ingredients

| # | Ingredient | Reason | Evidence Status | Alternative | Reminder |
|---|-----------|--------|----------------|------------|----------|
| | | | | | safety_interaction / evidence / regulatory_product |

---

## 6. Draft Formula Composition

### Phase 1: 强化期 (Intensive Phase)

| # | Ingredient | Scientific Name | Form | Dose | Frequency | Rationale | Evidence Tier | Constraints |
|---|-----------|----------------|------|------|-----------|-----------|---------------|-------------|
| 1 | | | | | | | Human RCT / Animal / TCM / Mechanistic | |

### Phase 2: 维持期 (Maintenance Phase)

| # | Ingredient | Scientific Name | Form | Dose | Frequency | Rationale | Evidence Tier | Constraints |
|---|-----------|----------------|------|------|-----------|-----------|---------------|-------------|
| 1 | | | | | | | | |

---

## 7. Per-Ingredient Evidence Summary

| Ingredient | Track 1: Human | Track 2: Animal | Track 3: TCM | Track 4: Mechanistic/Safety | Status | Reminder |
|-----------|---------------|----------------|-------------|---------------------------|--------|----------|
| | | | | | | |

---

## 8. Regulatory Coverage

| Ingredient | Jurisdiction | Status | Max Level | Limitations | Reminder |
|-----------|-------------|--------|-----------|-------------|----------|
| | | | | | regulatory_product (if gap) |

---

## 9. Reminder Package (Co-Product)

> See attached `templates/reminder_package_template.md` for full structured output.
>
> **Summary:** [N] total reminders — [X] critical, [Y] important, [Z] suggestions, [W] info
>
> Categories present: [use_followup / information_gap / safety_interaction / evidence / regulatory_product / human_review]
>
> These reminders are structured review items for the human-in-the-loop workbench. No external scheduled notifications have been sent or claimed.

---

## 10. Professional-Review Checklist

- [ ] Intake provenance reviewed (verified vs. user_reported vs. unknown vs. assumed)
- [ ] Triage status and reason understood
- [ ] All assumptions reviewed and accepted/modified
- [ ] Individual constraints reviewed
- [ ] Excluded ingredients and reasons reviewed
- [ ] Evidence tier labels checked (population-level ≠ individual proof)
- [ ] Animal/traditional/mechanistic NOT promoted to efficacy
- [ ] Regulatory coverage confirmed for target markets
- [ ] Reminder package reviewed (all categories, all severities)
- [ ] Information gaps acknowledged
- [ ] Safety flags addressed
- [ ] Professional clinical judgment applied

---

## 11. Follow-Up Questions

| # | Question | Related Field | Priority | Reminder ID |
|---|----------|---------------|----------|-------------|
| | | | High / Medium / Low | |

---

## 12. Limitations & Uncertainties

1. **Evidence is population-level.** Does not prove individual outcome.
2. **User-reported data is unverified** unless marked `verified`.
3. **Regulatory status is point-in-time.** May change.
4. **Evidence search is bounded.** Not all global literature covered.
5. **Not a medical prescription.** Requires qualified professional review.
6. **Assumptions applied where data was missing.** See §4.

---

## 13. Human Decision Record (Personalized Selection Step 5)

| Field | Value |
|-------|-------|
| Reviewer role | (pending) |
| Decision | (pending) accept / modify / defer / specialist_referral |
| Decision timestamp | (pending) |
| Rationale | (pending) |
| Changes made | (pending) |
| Reminders acknowledged | (pending) |
| Auto-finalization | **Blocked** until this section is completed by a human |

---

## 14. Attached Outputs (Required)

- [ ] Reminder Package (see `templates/reminder_package_template.md`)
- [ ] Four-Track Evidence Matrix
- [ ] Regulatory Coverage Matrix
- [ ] TCM Identity & Material Matrix (if applicable)
- [ ] Search Ledger
- [ ] Intake Audit Ledger
- [ ] Blocking/Residual-Risk Summary

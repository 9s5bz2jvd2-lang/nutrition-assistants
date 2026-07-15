# Risk Triage Contract — Human-in-the-Loop Professional Workbench

> **Schema version:** `risk-triage-v2.0`
> **Supersedes:** `risk-triage-v1.0` (per PARENT_DELTA_HUMAN_REVIEW_POLICY.md)
> **Purpose:** After intake data is collected, perform an explicit, machine-readable risk triage. Every personalized request is assigned a triage status. All statuses produce a professional working draft with visible gaps, reminders, and required human-review items. Automated finalization/release claims are gated; the human reviewer's ability to see an honest work-in-progress is NOT gated.

---


> **Mode C v3 precedence.** Required identity alignment remains strict for botanical-specific evidence, but it is an eligibility gate only. Missing intake, market, category, or identity creates `UNKNOWN`, `not_assessed`, or `BLOCKED_IDENTITY` rows; it preserves the draft and all independent work. Only finalization, efficacy promotion, and market claims are fail-closed. See `mode_c_automatic_contract.md`.


## 1. Interaction Model

The Skill is a **professional human-in-the-loop workbench**. Risk/uncertainty gates do NOT terminate the drafting workflow. They make uncertainty, red flags, missing data, contraindication/interaction questions, jurisdictional gaps, and required human decisions **visible, structured, and auditable**.

The human reviewer — not the model — decides whether to modify, defer, seek specialist input, or approve an output.

---

## 2. Triage Status Vocabulary (Draft-Capable)

| Status | Code | Meaning | Draft Behavior | Auto-Finalization |
|--------|------|---------|---------------|-------------------|
| `incomplete_draft_needs_human_input` | IDNHI | Required intake field missing/ambiguous | Draft generated with assumptions/unknowns section; targeted questions in reminders | Blocked |
| `draft_with_urgent_safety_flag` | DUSF | Emergency/red-flag/scope-exceeding presentation | Draft generated with URGENT safety flags and immediate referral guidance in reminders | Blocked |
| `draft_with_mandatory_human_review` | DMHR | High-risk context (pregnancy/pediatric/multimorbidity/drug interaction etc.) | Draft generated with mandatory review checklist and high-severity reminders | Blocked |
| `draft_with_regulatory_gap` | DRG | Market/category/regulatory coverage incomplete | Draft generated with regulatory gap matrix and open-jurisdiction reminders | Blocked |
| `draft_for_professional_review` | DFPR | All gates pass, intake complete, no high-risk flags | Clean draft with standard review checklist | Blocked |
| `human_reviewed_finalization` | HRF | Actual human reviewer has confirmed/modified the draft | Finalized version with human decision record | Allowed (requires human record) |

**Key principle:** Every status generates a draft + reminder package. Only `human_reviewed_finalization` permits automated release claims.

---

## 3. Triage Decision Tree

### Step 1: Intake Completeness Check

```
IF any required field is missing AND not marked unknown:
  → status = incomplete_draft_needs_human_input (IDNHI)
  → draft generated with: known fields populated, missing fields listed as "未提供/not provided"
  → reminders emit: information_gap reminders for each missing field
  → targeted questions included in draft
  → proceed to draft generation (do not halt)
```

### Step 2: Emergency / Red-Flag Screen

The following presentations trigger `draft_with_urgent_safety_flag`:

| Red Flag | Examples | Draft + Reminder Action |
|----------|---------|------------------------|
| Acute/emergency symptoms | Chest pain, severe bleeding, acute allergic reaction, suicidal ideation, stroke symptoms | DUSF draft with URGENT reminder: "Immediate emergency referral required. This draft is for review context only." |
| Scope-exceeding presentation | Request for diagnosis, request to replace emergency medication, active cancer treatment modification | DUSF draft with URGENT reminder: "Presentation exceeds functional medicine nutrition scope. Specialist referral required." |
| Request for autonomous prescription | Explicit request for a final prescription without professional review | DUSF draft with reminder: "Output is a professional working draft, not an issued prescription. Human reviewer finalization required." |

**The draft is still generated** — showing what the system can determine, with urgent flags and referral guidance.

### Step 3: High-Risk Context Identification

Any of the following conditions trigger `draft_with_mandatory_human_review`:

| Condition | Field Source | Reminder Generated |
|-----------|-------------|-------------------|
| Pregnancy or lactation | `pregnancy_status`, `lactation_status` | safety_interaction reminder: "Pregnancy/lactation — all ingredients require per-trimester safety review" |
| Pediatric (< 18 years) | `age_or_life_stage` | safety_interaction reminder: "Pediatric dosing — adult doses not directly applicable; weight/age adjustment required" |
| Older adult (≥ 65 years) | `age_or_life_stage` | safety_interaction reminder: "Older adult — renal clearance, polypharmacy risk assessment required" |
| Serious hepatic impairment | `hepatic_status` | safety_interaction reminder: "Hepatic impairment — metabolism-dependent dose adjustment may be needed" |
| Serious renal impairment | `renal_status` | safety_interaction reminder: "Renal impairment — renally-cleared ingredients require dose/exclusion review" |
| Cancer history or active malignancy | `high_risk_history` | safety_interaction reminder: "Cancer history — ingredient selection requires oncology-aware review" |
| Complex multimorbidity (≥ 3 chronic conditions) | `diagnoses`, `clinical_history` | human_review reminder: "Complex multimorbidity — multi-system interaction review required" |
| Prescription drug use with known interaction potential | `current_prescription_medications` | safety_interaction reminder per drug: "Potential [drug]–[ingredient] interaction — pharmacist/physician review required" |
| Uncertain allergy/intolerance profile | `allergies_intolerances` | information_gap reminder: "Allergy profile incomplete — confirm before use" |
| Organ transplant or immunosuppression | `high_risk_history` | safety_interaction reminder: "Immunosuppression — immune-modulating ingredients require specialist review" |
| Eating disorder history | `clinical_history` | safety_interaction reminder: "Eating disorder context — weight/food-related recommendations require specialist sensitivity review" |
| Substance use affecting metabolism | `substance_use` | safety_interaction reminder: "Substance use — hepatic load and interaction considerations" |

**The draft is still generated** with all high-risk factors visible and appropriate review reminders.

### Step 4: Regulatory / Coverage Assessment

```
IF target_markets contains jurisdiction not fully covered:
  → status = draft_with_regulatory_gap (DRG) (may be combined with DMHR/DUSF)
  → draft generated with regulatory gap matrix showing uncovered jurisdictions
  → reminders emit: regulatory_product reminders per gap

IF product_category = unknown_needs_classification:
  → draft generated with category ambiguity noted
  → reminders emit: regulatory_product reminder for category resolution

ALL drafts proceed to generation regardless of regulatory coverage.
```

### Step 5: Final Triage Assignment

```
The HIGHEST-SEVERITY status applies. Multiple conditions compound:
  DUSF > DMHR > DRG > IDNHI > DFPR

IF human reviewer has recorded a decision:
  → status = human_reviewed_finalization (HRF)
```

**No status blocks draft generation.** Only `human_reviewed_finalization` permits release claims.

---

## 4. Triage Output Record

```json
{
  "request_id": "...",
  "triage_timestamp": "ISO 8601",
  "triage_status": "IDNHI|DUSF|DMHR|DRG|DFPR|HRF",
  "combined_statuses": [],
  "intake_completeness": {
    "all_required_present": true,
    "missing_fields": [],
    "unknown_fields": []
  },
  "red_flag_screen": {
    "emergency_detected": false,
    "scope_exceeded": false,
    "flags": []
  },
  "high_risk_identifiers": [],
  "regulatory_coverage_check": {
    "all_markets_covered": true,
    "uncovered_markets": [],
    "category_resolved": true
  },
  "draft_generated": true,
  "reminder_count": 0,
  "reminder_categories_present": [],
  "auto_finalization_blocked": true,
  "blocking_reasons": [],
  "professional_review_checklist": []
}
```

---

## 5. Professional-Review Checklist (All Statuses)

Every draft output includes:

- [ ] Intake data provenance summary (user-reported vs. verified vs. unknown)
- [ ] Triage status and reason
- [ ] Individual constraints considered (medications, allergies, life stage, labs)
- [ ] Excluded ingredients and reasons
- [ ] Alternative ingredients considered
- [ ] Evidence tier labels on every ingredient
- [ ] Regulatory coverage status for declared markets
- [ ] Population-level evidence disclaimer acknowledged
- [ ] Follow-up questions and unresolved fields reviewed
- [ ] Reminder package reviewed (all categories)
- [ ] Recommendation to seek qualified professional review before use
- [ ] Limitations and residual uncertainties
- [ ] Human decision: accept / modify / defer / seek specialist

---

## 6. Fail-Closed Rules (Epistemic Boundaries Preserved)

1. **Never silently infer** missing history, market, category, medication, dose, or contraindication information. Make gaps visible in the draft and reminders.
2. **Never derive or recommend a human dose** by scaling an animal study or traditional-use amount.
3. **Never convert `user_reported` data to `verified`** without an actual verifiable source.
4. **Never skip triage** and proceed directly to formula generation.
5. **Never auto-finalize** — always output a draft with review status; only `human_reviewed_finalization` (with actual human decision record) permits release.
6. **Person-specific preference CANNOT override** an identity, safety, or regulatory failure.
7. **Animal/classical-TCM/mechanistic evidence CANNOT become human clinical proof.**
8. **RCT evidence CANNOT become regulatory authorization.**
9. **Uncertain/blocked sources CANNOT become affirmative clearance.**
10. **Automated finalization/release claims require a recorded human decision.**

---

## 7. Output Phrasing Guidance

Avoid generic "do not continue" wording. Prefer:
- "Draft generated for human review; required review items: …"
- "Evidence/regulatory status unresolved; no automatic finalization claim"
- "Reviewer decision required: [options]"
- "Assumptions applied: [list]. Unknowns: [list]. Verify before use."

# Individualized Formula Request — Intake Contract

> **Schema version:** `individualized-intake-v1.0`
> **Purpose:** Define the intake schema for a personalized formula/protocol draft request. This is an on-demand reference for the individualized formula-draft route. It separates required, optional, verified, user-reported, unknown, and not-applicable fields.

---

## 1. Product Boundary Statement

The individualized formula-draft route produces a **personalized formula/protocol draft for qualified professional review**. It is NOT:

- An autonomous diagnosis or treatment plan
- A prescription or medical order
- A guarantee of regulatory compliance
- A direct patient-facing clinical directive

The draft may tailor a candidate protocol to supplied person-specific information, but must:
- Distinguish user-reported data from verified clinical facts
- Ask for missing critical information rather than invent it
- Stop at a clarification, referral, or professional-review result when context is incomplete
- Never convert animal, mechanistic, classical-TCM, or regulatory-status information into human clinical efficacy/dose proof
- Retain all existing evidence, regulatory, identity, corpus sweep, and non-finalization gates

---

## 2. Field Provenance Vocabulary

Every field in the intake record carries a `provenance` tag:

| Provenance | Meaning |
|------------|---------|
| `required` | Must be provided or explicitly marked as unknown; missing → `incomplete_draft_needs_human_input` |
| `optional` | May be provided; missing does not block |
| `verified` | Data confirmed by an authoritative source (lab report, physician record); carries source reference |
| `user_reported` | Provided by the user without independent verification; used as context, not clinical fact |
| `unknown` | Field is acknowledged as not available; system must not invent a value |
| `not_applicable` | Explicitly excluded for this request (e.g., sex when irrelevant) |

**Privacy rule:** Do not require personally identifying data (name, ID, address). Do not retain sensitive data beyond the session/request scope.

---

## 3. Intake Field Schema

### 3.1 Request Context (Required)

| Field | Provenance | Type | Description | Fail-Closed Rule |
|-------|-----------|------|-------------|------------------|
| `request_id` | auto-generated | string | Session-scoped, non-personal identifier | Auto-filled |
| `intended_use_goal` | required | free-text | Health goal or condition the protocol targets | Missing → `incomplete_draft_needs_human_input` |
| `target_markets` | required | list[string] | Jurisdiction identifiers (CN, US, EU, etc.) | Missing/empty → `incomplete_draft_needs_human_input`; "global" unresolved → `incomplete_draft_needs_human_input` |
| `product_category` | required | enum | `conventional_food`, `dietary_supplement_health_product`, `medicine`, `unknown_needs_classification` | Missing/ambiguous → `incomplete_draft_needs_human_input` |
| `created_at` | auto-generated | ISO 8601 | Timestamp of request creation | Auto-filled |

### 3.2 Demographics & Life Stage (Required where applicable)

| Field | Provenance | Type | Description | Fail-Closed Rule |
|-------|-----------|------|-------------|------------------|
| `age_or_life_stage` | required | string | Age in years, or life stage (e.g., "postmenopausal", "adolescent") | Missing → `incomplete_draft_needs_human_input` |
| `sex` | conditional | enum: `male`, `female`, `other`, `not_applicable` | Required when sex-specific dosing, evidence, or safety applies | Relevant but missing → `incomplete_draft_needs_human_input` |
| `pregnancy_status` | conditional | enum: `not_pregnant`, `pregnant`, `planning_pregnancy`, `unknown` | Required for females of childbearing potential | If pregnant → `draft_with_mandatory_human_review` |
| `lactation_status` | conditional | enum: `not_lactating`, `lactating`, `unknown` | Required for postpartum individuals | If lactating → `draft_with_mandatory_human_review` |

### 3.3 Clinical History (User-Reported unless verified)

| Field | Provenance | Type | Description | Fail-Closed Rule |
|-------|-----------|------|-------------|------------------|
| `symptoms` | user_reported | list[free-text] | Current symptoms described by user | Treated as user-reported context; not clinical fact |
| `diagnoses` | user_reported (or verified if source provided) | list[string] | Known diagnoses; mark `verified` if physician record provided | User-reported → context only; `verified` → clinical reference |
| `clinical_history` | user_reported | free-text | Relevant medical history | Used for risk triage only |
| `relevant_labs` | user_reported (or verified if report provided) | list[object] | Lab name, value, unit, date, source | If no date or source → `user_reported`; used for context only |
| `high_risk_history` | user_reported | list[string] | Cancer history, organ transplant, autoimmune flares, etc. | If present → `draft_with_mandatory_human_review` |

### 3.4 Medications & Supplements (Required)

| Field | Provenance | Type | Description | Fail-Closed Rule |
|-------|-----------|------|-------------|------------------|
| `current_prescription_medications` | required | list[object] | Name, dose, frequency; mark `user_reported` or `verified` | Missing when interaction risk exists → `incomplete_draft_needs_human_input` |
| `otc_drugs` | required | list[string] | Current OTC medications | Missing when relevant → flag |
| `current_supplements` | required | list[string] | Current supplement regimen | Missing → flag; used for interaction check |
| `allergies_intolerances` | required | list[string] | Known food, drug, or supplement allergies/intolerances | Missing → `incomplete_draft_needs_human_input` if formula contains common allergens |
| `substance_use` | optional | free-text | Tobacco, alcohol, recreational substance use context | Used for hepatic/interaction triage |

### 3.5 Organ Function & Risk Factors (Conditional)

| Field | Provenance | Type | Description | Fail-Closed Rule |
|-------|-----------|------|-------------|------------------|
| `hepatic_status` | conditional | string | Hepatic function; required if formula affects hepatic metabolism | Significant impairment → `draft_with_mandatory_human_review` |
| `renal_status` | conditional | string | Renal function; required if formula includes renally-cleared ingredients | Significant impairment → `draft_with_mandatory_human_review` |
| `diabetes_status` | conditional | string | Diabetes type, HbA1c if available | Relevant for glucose-modulating ingredients |

### 3.6 Preferences & Context (Optional)

| Field | Provenance | Type | Description | Fail-Closed Rule |
|-------|-----------|------|-------------|------------------|
| `diet_pattern` | optional | string | Vegetarian, vegan, halal, kosher, etc. | Used for excipient/capsule/ingredient compatibility only |
| `practical_preferences` | optional | free-text | Pill size, frequency, taste, budget | Soft constraint only; cannot override safety/regulatory gate |
| `cultural_tcm_context` | optional | free-text | TCM constitution type, preferences, prior TCM treatment | Context only; not clinical evidence |
| `ingredient_form_preferences` | optional | list[string] | Preferred chemical forms (e.g., chelated minerals) | Soft constraint; identity gate still applies |
| `botanical_identity_requirements` | optional | list[object] | Specific species, cultivar, extract specifications if known | Used to pre-fill identity gate; ambiguity becomes BLOCKED_IDENTITY with draft preserved and a human-review/ledger row |

### 3.7 Consent & Privacy (Required)

| Field | Provenance | Type | Description | Fail-Closed Rule |
|-------|-----------|------|-------------|------------------|
| `consent_to_process_health_data` | required | boolean | User acknowledges health data processing for draft generation | If false or missing → cannot proceed |
| `data_retention_preference` | required | enum: `session_only`, `anonymized_summary` | User preference for data retention | Default to `session_only` if not specified |
| `personal_identifiers_excluded` | required (invariant) | boolean | Confirm no PII (name, ID, address) in request | Must always be `true` in the schema |

---

## 4. Intake Completeness Assessment

After collecting intake data, produce an **Intake Completeness Record**:

```
{
  "request_id": "...",
  "required_fields_present": true/false,
  "missing_required_fields": [],
  "unknown_fields": [],
  "user_reported_fields": [],
  "verified_fields": [],
  "conditional_fields_triggered": [],
  "privacy_compliant": true/false,
  "proceed_to_triage": true/false,
  "blocking_reasons": []
}
```

**Rules:**
- If any `required` field is missing and not marked `unknown` → `proceed_to_triage: false`, status = `incomplete_draft_needs_human_input`
- If `consent_to_process_health_data` is false → cannot proceed
- Unknown fields are acceptable if explicitly marked; they become risk triage inputs

---

## 5. Data Minimization Principles

1. **No PII required.** Name, national ID, address, phone, email are NEVER required.
2. **Session-scoped identifiers only.** Request IDs are non-personal, session-scoped.
3. **User-reported default.** All clinical data is `user_reported` unless a verifiable source is provided.
4. **No persistent storage.** Sensitive health data is not retained beyond the request unless the user explicitly opts for `anonymized_summary`.
5. **Audit without identity.** The audit ledger records field provenance and triage outcomes WITHOUT personal identifiers.

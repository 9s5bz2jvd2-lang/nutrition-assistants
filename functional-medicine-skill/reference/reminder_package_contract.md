# Reminder Package Contract — Co-Product of Every Personalized Draft

> **Schema version:** `reminder-package-v1.0`
> **Required by:** PARENT_DELTA_REMINDER_OUTPUT.md
> **Purpose:** Every personalized draft generates a structured reminder/checklist package as a mandatory co-product. Missing data, risk flags, evidence gaps, and regulatory gaps flow into reminders — they do NOT suppress the draft. Reminders are not external scheduled notifications; they are structured review items for the human-in-the-loop workbench.

---

## 1. Core Principle

**Plan and reminders are always co-products.** The human reviewer sees both the working draft and the structured reminders together. Warnings, missing data, risk flags, evidence gaps, or regulatory gaps do NOT blanket-suppress draft generation. They populate the reminder package so the reviewer can decide what to do.

Reminders are NOT:
- External scheduled notifications (no SMS/email/push claim)
- Medical facts or assertions
- Automated prescriptions or orders
- Autonomous clinical decisions

Reminders ARE:
- Structured review items with source/trigger/severity/action-owner
- Auditable evidence of what the system flagged
- Input for the human reviewer's decision process

---

## 2. Reminder Categories

### 2.1 Use / Follow-Up

Intended timing, pattern, or staged-review points from the human-approved plan template.

| Field | Type | Description |
|-------|------|-------------|
| `reminder_id` | string | Unique within this reminder package |
| `category` | `use_followup` | |
| `title` | string | Short description |
| `detail` | string | Full context |
| `source` | string | What generated this reminder (e.g., "staged plan template", "Phase 1→Phase 2 transition") |
| `trigger` | string | Condition or timing that activates this reminder |
| `status` | enum | `open`, `acknowledged`, `deferred`, `resolved_by_human` |
| `severity` | enum | `info`, `suggestion`, `important`, `critical` |
| `action_owner` | enum | `human_reviewer`, `specialist`, `patient_with_guidance` |
| `external_notification_claim` | `false` (always) | Explicit assertion that no external scheduled notification was sent |

### 2.2 Information Gaps

Missing medicines, allergies, target market/category, key labs/history, botanical identity/form/dose fields, or uncertain provenance.

| Field | Type | Description |
|-------|------|-------------|
| `reminder_id` | string | |
| `category` | `information_gap` | |
| `title` | string | e.g., "Current medications not provided" |
| `detail` | string | What is missing, why it matters, what assumption was used |
| `source` | string | Intake field that is missing/unknown |
| `trigger` | string | `intake_field_missing` or `intake_field_uncertain_provenance` |
| `status` | enum | `open`, `acknowledged`, `deferred`, `resolved_by_human` |
| `severity` | `info` if assumed safely, `important` if affects dosing/safety, `critical` if blocks safe use |
| `action_owner` | `human_reviewer` (must obtain from patient/case) |
| `assumed_value` | string or null | If the system applied a default assumption, state it here |
| `external_notification_claim` | `false` |

### 2.3 Safety & Interaction

Potential medicine/supplement interaction questions, allergies/intolerances, special-population/medical-risk flags, adverse-effect or urgent red-flag prompts.

| Field | Type | Description |
|-------|------|-------------|
| `reminder_id` | string | |
| `category` | `safety_interaction` | |
| `title` | string | e.g., "Warfarin–fish oil interaction question" |
| `detail` | string | Specific interaction/risk, evidence source, what is known vs. unknown |
| `source` | string | Track 4 signal / special-population rule / allergy match |
| `trigger` | string | `drug_interaction_signal`, `allergy_match`, `special_population_flag`, `urgent_red_flag` |
| `status` | enum | `open`, `acknowledged`, `deferred`, `resolved_by_human` |
| `severity` | `info` for theoretical, `important` for probable, `critical` for urgent/red-flag |
| `action_owner` | `human_reviewer`, `specialist` (e.g., oncologist for cancer, pharmacist for drug interaction) |
| `confirmed_known_issue` | boolean | `true` if evidence confirms the risk; `false` if "requires human check" |
| `external_notification_claim` | `false` |

### 2.4 Evidence

Evidence-tier limitations, animal/TCM-only records, absence/unreadability/retraction concerns, required source-review prompts.

| Field | Type | Description |
|-------|------|-------------|
| `reminder_id` | string | |
| `category` | `evidence` | |
| `title` | string | e.g., "Ingredient X: animal evidence only" |
| `detail` | string | Evidence status, what is missing, what was searched |
| `source` | string | Track number and search result |
| `trigger` | string | `animal_only`, `traditional_only`, `absent`, `conflicting`, `retraction_concern` |
| `status` | enum | `open`, `acknowledged`, `deferred`, `resolved_by_human` |
| `severity` | `info` for well-supported, `important` for weak/absent, `critical` if ingredient relies on it |
| `action_owner` | `human_reviewer` (decide whether to include/exclude ingredient) |
| `external_notification_claim` | `false` |

### 2.5 Regulatory / Product

Jurisdiction/category/form/claim/limit gaps, stale/uncertain sources, items requiring review before external/product use.

| Field | Type | Description |
|-------|------|-------------|
| `reminder_id` | string | |
| `category` | `regulatory_product` | |
| `title` | string | e.g., "Japan market regulatory status unknown" |
| `detail` | string | Specific gap, source registry coverage status, what is needed |
| `source` | string | Source registry entry |
| `trigger` | string | `uncovered_jurisdiction`, `unknown_status`, `category_ambiguous`, `stale_source` |
| `status` | enum | `open`, `acknowledged`, `deferred`, `resolved_by_human` |
| `severity` | `info` for informational, `important` for blocks marketing claim, `critical` for prohibited |
| `action_owner` | `human_reviewer` (may need regulatory specialist) |
| `external_notification_claim` | `false` |

### 2.6 Human Review & Monitoring

Reviewer-required decisions, suggested monitoring/follow-up questions, review cadence/status, and open decisions.

| Field | Type | Description |
|-------|------|-------------|
| `reminder_id` | string | |
| `category` | `human_review` | |
| `title` | string | e.g., "Reviewer decision: include Ingredient X despite animal-only evidence?" |
| `detail` | string | Decision context, options, rationale needed |
| `source` | string | Which gate/assessment generated this decision point |
| `trigger` | string | `ingredient_inclusion_decision`, `dose_adjustment_decision`, `market_readiness_decision`, `specialist_referral_needed` |
| `status` | enum | `open`, `acknowledged`, `deferred`, `resolved_by_human` |
| `severity` | `suggestion` for optional, `important` for recommended, `critical` for mandatory |
| `action_owner` | `human_reviewer` or `specialist` |
| `decision_options` | list[string] | e.g., ["include with caveat", "exclude", "defer to specialist"] |
| `external_notification_claim` | `false` |

---

## 3. Reminder Package Output

Every personalized draft includes a `## Reminder Package` section immediately after the draft formula and before the limitations. The section contains:

1. **Summary count** by category and severity
2. **All reminders** in structured table(s) grouped by category
3. **Explicit statement:** "These reminders are structured review items for the human-in-the-loop workbench. No external scheduled notifications have been sent or claimed."

---

## 4. Status Vocabulary for Reminders

| Status | Meaning |
|--------|---------|
| `open` | Not yet reviewed by human |
| `acknowledged` | Human has seen this reminder |
| `deferred` | Human has decided to address later |
| `resolved_by_human` | Human has made a decision and recorded it |

---

## 5. Severity Vocabulary

| Severity | Meaning | Draft Impact |
|----------|---------|-------------|
| `info` | Informational, no immediate action needed | No effect on draft |
| `suggestion` | Recommended review item | Draft proceeds; reviewer should consider |
| `important` | Significant safety/evidence/regulatory concern | Draft proceeds with explicit flag; reviewer must address |
| `critical` | Urgent or blocking concern | Draft proceeds with URGENT flag and referral guidance; reviewer must address before any use |

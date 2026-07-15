# Template: Reminder Package — Co-Product of Personalized Draft

> **Usage:** Generated alongside every personalized formula draft. Reminders are structured review items for the human-in-the-loop workbench. No external scheduled notifications are sent or claimed.

---

## Reminder Summary

| Category | Open | Critical | Important | Suggestion | Info |
|----------|------|----------|-----------|------------|------|
| Use/Follow-up | | | | | |
| Information Gaps | | | | | |
| Safety & Interaction | | | | | |
| Evidence | | | | | |
| Regulatory/Product | | | | | |
| Human Review | | | | | |
| **Total** | | | | | |

---

## 1. Use / Follow-Up Reminders

| ID | Title | Detail | Trigger | Severity | Owner | Status |
|----|-------|--------|---------|----------|-------|--------|
| | | | | | human_reviewer / specialist / patient_with_guidance | open |

---

## 2. Information Gap Reminders

| ID | Missing Field | Impact | Assumption Applied | Severity | Owner | Status |
|----|--------------|--------|-------------------|----------|-------|--------|
| | | | (null if none) | | human_reviewer | open |

---

## 3. Safety & Interaction Reminders

| ID | Title | Detail | Source | Trigger | Confirmed? | Severity | Owner | Status |
|----|-------|--------|--------|---------|------------|----------|-------|--------|
| | | | | drug_interaction / allergy / special_population / urgent_red_flag | yes / requires_human_check | | human_reviewer / specialist | open |

---

## 4. Evidence Reminders

| ID | Ingredient | Evidence Status | What Is Missing | Sources Searched | Severity | Owner | Status |
|----|-----------|----------------|-----------------|-----------------|----------|-------|--------|
| | | animal_only / traditional_only / absent / conflicting | | | | human_reviewer | open |

---

## 5. Regulatory / Product Reminders

| ID | Jurisdiction | Ingredient | Gap Description | Source Registry Status | Severity | Owner | Status |
|----|-------------|-----------|-----------------|----------------------|----------|-------|--------|
| | | | | uncovered / unknown / needs_review | | human_reviewer | open |

---

## 6. Human Review & Monitoring Reminders

| ID | Decision Needed | Context | Options | Severity | Owner | Status |
|----|----------------|---------|---------|----------|-------|--------|
| | | | [accept, modify, defer, specialist_referral] | | human_reviewer / specialist | open |

---

## 7. Explicit Assertions

- [ ] These reminders are structured review items for the human-in-the-loop workbench.
- [ ] No external scheduled notifications have been sent or claimed.
- [ ] Reminders disclose evidence/source/uncertainty and human action ownership.
- [ ] No reminder is represented as a medical fact, automated prescription, or external notification.
- [ ] All `open` reminders require human reviewer attention before any finalization.

---

## 8. Human Decision Record

| Field | Value |
|-------|-------|
| Reviewer role | |
| Decision timestamp | |
| Decision | accept / modify / defer / specialist_referral |
| Rationale | |
| Reminders acknowledged | |
| Reminders deferred | |
| Reminders resolved | |
| Changes made (if modify) | |

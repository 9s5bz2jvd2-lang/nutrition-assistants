# Regulatory Gate — Per-Ingredient, Per-Jurisdiction Assessment

> **Schema version:** `regulatory-gate-v1.0`
> **Purpose:** For every resolved ingredient in the formula, assess regulatory status in every declared target market/product category using ONLY authoritative sources from the source registry. Fail closed on missing, ambiguous, stale, or non-authoritative assessments.

---


> **Mode C v3 precedence.** Required identity alignment remains strict for botanical-specific evidence, but it is an eligibility gate only. Missing intake, market, category, or identity creates `UNKNOWN`, `not_assessed`, or `BLOCKED_IDENTITY` rows; it preserves the draft and all independent work. Only finalization, efficacy promotion, and market claims are fail-closed. See `mode_c_automatic_contract.md`.


## 1. Regulatory Assessment Principles

1. **Per-ingredient × per-jurisdiction × per-product-category.** Regulatory status is a three-dimensional assessment, not a single value.
2. **Authoritative sources only.** Only sources listed in `source_registry.md` Section 3 (Regulatory Source Families) can clear a regulatory gate. A web search snippet, blog post, or manufacturer website is NEVER authoritative.
3. **Independence from clinical evidence.** Regulatory clearance ≠ clinical efficacy proof. Clinical evidence ≠ market authorization. These are independent gates.
4. **fail closed on every gap.** If the authoritative source cannot be accessed, the document is not in the registry, or the assessment is ambiguous → status is `unknown`, not `cleared`.
5. **Date-stamped.** Every assessment includes the date the source was checked. Assessments may become stale if the source is updated.

---

## 2. Regulatory Assessment Table Schema

Each row in the regulatory coverage matrix represents one ingredient × one jurisdiction × one product category:

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `ingredient_id` | Yes | string | References ingredient identity tuple |
| `ingredient_name` | Yes | string | Common name |
| `jurisdiction` | Yes | string | Market code (e.g., `CN`, `US`, `EU`, `Codex`) |
| `product_category` | Yes | enum | `conventional_food`, `food_additive_ingredient`, `dietary_supplement_health_product`, `medicine`, `other` |
| `regulatory_authority` | Yes | string | Authority name from source registry |
| `source_id` | Yes | string | Source ID from source registry (e.g., `cn_samr`, `us_fda`, `eu_efsa`) |
| `source_url` | Yes | URL | Direct URL to the authority or document |
| `document_reference` | Yes | string | Specific document name, regulation number, monograph title |
| `document_version_date` | Yes | string | Version, edition, or effective date of the document |
| `status` | Yes | enum | `permitted`, `prohibited`, `conditional`, `unknown`, `not_assessed` |
| `max_level` | Conditional | string | Maximum permitted level/dose if the source provides it |
| `compositional_restrictions` | Conditional | string | Marker compound, purity, or compositional requirements |
| `label_claim_restrictions` | Conditional | string | Restrictions on claims, mandatory label statements |
| `identity_form_assessed` | Yes | string | The specific identity tuple being assessed (species, part, form, extract spec) |
| `applicability_limitations` | Yes | string | Scope limits of the assessment (e.g., "RNI is not additive authorization"; "GRAS self-determination is not FDA approval") |
| `checked_at` | Yes | ISO 8601 | Date the source was accessed |
| `assessor_notes` | Recommended | string | Any caveats, assumptions, or open questions |

---

## 3. Status Vocabulary

| Status | Meaning | Gate Effect |
|--------|---------|-------------|
| `permitted` | Authoritative source confirms the ingredient is permitted for the declared product category in this jurisdiction, for the specific identity/form | Passes regulatory gate for this ingredient × jurisdiction × category |
| `prohibited` | Authoritative source explicitly prohibits or does not authorize the ingredient for this category | Blocks formula for this market/category |
| `conditional` | Permitted with specific conditions (dose limits, label requirements, claim restrictions, etc.) | Passes only if all conditions are met and documented |
| `unknown` | No authoritative assessment could be located, OR the assessment is ambiguous | **Blocks regulatory clearance** for this ingredient × jurisdiction × category |
| `not_assessed` | Assessment has not yet been performed | **Blocks finalization** — every declared jurisdiction must have an assessment |

---

## 4. Common Applicability Limitations

These limitations must be stated explicitly where they apply:

| Limitation | Explanation |
|------------|-------------|
| RNI/AI ≠ additive authorization | A nutrient reference intake (RNI or AI) defines recommended dietary intake; it does NOT authorize the nutrient as a food additive or supplement ingredient at arbitrary levels |
| UL ≠ permitted maximum | A tolerable upper intake level (UL) is a safety threshold; it is NOT automatically the legal maximum for supplements or food fortification |
| GRAS self-determination ≠ FDA approval | Under DSHEA, manufacturers may self-determine GRAS status; FDA acknowledgment of a GRAS notification is NOT the same as FDA approval |
| Food rule ≠ medicine approval | A substance permitted as a food or food ingredient is NOT automatically approved as a medicine, and vice versa |
| Filing ≠ registration | In China, "filing" (备案) and "registration" (注册) are different regulatory pathways with different requirements |
| Old pharmacopoeia ≠ current standard | Previous editions of a pharmacopoeia are superseded; only the current edition is authoritative for regulatory purposes |
| Botanical claim "on hold" ≠ cleared | In the EU, many botanical health claims have "on hold" status under NHCR 1924/2006; this is NOT clearance |

---

## 5. Per-Jurisdiction Assessment Workflow

For each declared target market:

### Step 1: Identify the applicable regulatory authority and source
- Use `source_registry.md` to find the authoritative source for this jurisdiction + product category.
- If the jurisdiction or category is `uncovered` or `needs_jurisdiction_specific_review` → status = `unknown`.

### Step 2: Query the authoritative source
- Search for the specific ingredient (by identity tuple) in the context of the declared product category.
- Record: document reference, version/date, specific provisions.

### Step 3: Determine status
- `permitted`: Clear authorization found
- `conditional`: Permitted with conditions → document all conditions
- `prohibited`: Explicitly not authorized or banned
- `unknown`: Cannot determine from available authoritative sources

### Step 4: Record applicability limitations
- State explicitly what the source does and does NOT authorize.

### Step 5: Cross-check identity match
- Verify that the assessment applies to the exact identity tuple in the formula (species, part, form, extract specification).
- If the identity does not match → the assessment does NOT apply; status = `unknown` for this specific identity.

---

## 6. Global-Compliant Claim Rules

A formula may NOT claim to be "global-compliant," "market-ready," or "compliant with target market regulations" unless ALL of the following are true:

1. Every declared target market has a regulatory assessment for every ingredient.
2. Every assessment is `permitted` or `conditional` (with all conditions met).
3. No assessment is `unknown`, `not_assessed`, or `prohibited`.
4. Product category is resolved (not `unknown_needs_classification`).
5. All identity tuples are resolved.

**If any target market or ingredient assessment is missing, ambiguous, or prohibited:**
- Output the formula ONLY as a research/education candidate.
- Apply a BLOCKING status.
- State explicitly which markets/ingredients are unresolved.

---

## 7. Regulatory vs. Evidence Gate Independence

| Aspect | Evidence Gate | Regulatory Gate |
|--------|--------------|-----------------|
| Question | Does clinical evidence support this ingredient for this indication? | Is this ingredient authorized for this product category in this market? |
| Sources | PubMed, Cochrane, CNKI, etc. | FDA, SAMR, EFSA, etc. |
| Failure mode | "No evidence found" ≠ proof of safety or efficacy | "No authorization found" ≠ proof of illegality |
| Independence | Evidence exists regardless of regulatory status | Authorization exists regardless of clinical evidence |
| Both must pass | Yes — clinical evidence and regulatory clearance are independent, parallel gates |

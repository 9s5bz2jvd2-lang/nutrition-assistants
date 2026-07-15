# Formula Context & Identity Gate

> **Schema version:** `formula-context-gate-v1.0`
> **Purpose:** Before any evidence or regulatory search, the formula must have a fully resolved context and ingredient identity tuple. Missing or ambiguous fields fail closed.

---


> **Mode C v3 precedence.** Required identity alignment remains strict for botanical-specific evidence, but it is an eligibility gate only. Missing intake, market, category, or identity creates `UNKNOWN`, `not_assessed`, or `BLOCKED_IDENTITY` rows; it preserves the draft and all independent work. Only finalization, efficacy promotion, and market claims are fail-closed. See `mode_c_automatic_contract.md`.


## 1. Formula Context Record

Every formula must record the following BEFORE evidence or regulatory assessment begins:

| Field | Required | Values / Format | Fail-Closed Rule |
|-------|----------|-----------------|------------------|
| `formula_id` | Yes | Auto-generated or user-supplied identifier | Missing → abort |
| `formula_purpose` | Yes | Free-text: therapeutic goal, intended health outcome | Missing → abort |
| `intended_use` | Yes | Free-text: how the formula is to be used (e.g., oral supplement, topical, etc.) | Missing → abort |
| `product_category` | Yes | One of: `conventional_food`, `food_additive_ingredient`, `dietary_supplement_health_product`, `medicine`, `unknown_needs_classification` | Missing or ambiguous → abort; `unknown_needs_classification` blocks regulatory clearance |
| `target_markets` | Yes | List of jurisdiction identifiers (e.g., `CN`, `US`, `EU`, `Codex`, `JP`, etc.) | Empty → output ONLY as research/education candidate with BLOCKING status; no market-ready claim |
| `target_population` | Yes | Description of intended population including age, sex, physiological state | Missing → default to general adult population; flag as assumption |
| `contraindication_context` | Conditional | Current medications, known allergies, special conditions | If formula involves known interaction risks and this is missing → flag and require |
| `created_at` | Yes | ISO 8601 timestamp | Auto-filled |

---

## 2. Ingredient Identity Tuple

Every ingredient in the formula must have a resolved identity tuple BEFORE evidence or regulatory search:

| Field | Required | Format | Fail-Closed Rule |
|-------|----------|--------|------------------|
| `common_name` | Yes | Common name(s) in primary language(s) | Missing → abort |
| `local_names` | Recommended | Names in other relevant languages (e.g., Chinese name, regional name) | Missing → flag; do not abort if scientific name is resolved |
| `scientific_latin_name` | Yes (when applicable) | Binomial nomenclature (e.g., *Panax ginseng* C.A.Mey.) | Missing for botanical/TCM → abort for that ingredient |
| `plant_part` | Yes (for botanicals) | Specific plant part (e.g., root, leaf, rhizome, fruit) | Missing or ambiguous for botanical → fail closed for that ingredient |
| `processing_preparation` | Yes (when applicable) | Processing method (e.g., raw, extract, decoction, fermentation) | Missing when processing affects identity/potency → fail closed |
| `extract_ratio_or_marker` | Conditional | Extract ratio (e.g., 10:1) or marker compound + concentration (e.g., ≥5% ginsenosides) | Required for extracts; missing → fail closed for that ingredient |
| `chemical_form` | Yes (for nutrients) | Specific chemical form (e.g., magnesium glycinate vs. magnesium oxide vs. magnesium citrate) | Missing for nutrients with form-dependent bioavailability → flag |
| `dose_and_unit` | Yes | Numeric dose + unit (e.g., 500 mg, 2000 IU, 180 µg) | Missing → abort |
| `species_variety_cultivar` | Conditional | Subspecies, variety, or cultivar when identity depends on it | Required when species ambiguity exists; missing → fail closed |

---

## 3. Botanical/TCM Identity Ambiguity Rules

For botanical and TCM ingredients, additional fail-closed rules apply:

### 3.1 Species Ambiguity
- If the common name maps to multiple possible species (e.g., "人参" could be *Panax ginseng*, *Panax quinquefolius*, *Panax notoginseng*, etc.), the scientific name MUST be resolved.
- If unresolved → **fail closed for that ingredient**. Do not proceed to evidence or regulatory assessment.

### 3.2 Plant-Part Ambiguity
- If the plant part is not specified and different parts have different regulatory statuses or evidence bases (e.g., root vs. leaf vs. seed) → **fail closed for that ingredient**.

### 3.3 Extract Specification
- If the ingredient is an extract but the extraction solvent, ratio, or marker compound concentration is not specified and different specifications have different regulatory statuses → **fail closed for that ingredient**.

### 3.4 Species/Part Match to Pharmacopoeia
- For TCM ingredients, the identity tuple must be checked against the official pharmacopoeia monograph (e.g., CP 2020). If the pharmacopoeia specifies a particular species/part/processing and the ingredient does not match → **flag as non-compliant with pharmacopoeial standard**.

---

## 4. Identity Resolution Output

Once all ingredients have resolved identity tuples, produce:

1. **Ingredient Identity Table:** One row per ingredient with all tuple fields.
2. **Ambiguity Log:** Any ingredient with partial resolution, noted with the specific ambiguity and its impact on downstream assessment.
3. **Blocking List:** Any ingredient that failed closed, with the specific reason.

The formula proceeds to evidence and regulatory assessment ONLY for fully resolved ingredients. Blocked ingredients halt finalization unless explicitly excluded from the formula.

---

## 5. Example Identity Record

```json
{
  "common_name": "姜黄素",
  "local_names": ["Turmeric", "Curcumin", "Jiāng Huáng"],
  "scientific_latin_name": "Curcuma longa L.",
  "plant_part": "rhizome",
  "processing_preparation": "standardized extract",
  "extract_ratio_or_marker": "95% curcuminoids",
  "chemical_form": "curcumin (diferuloylmethane)",
  "dose_and_unit": "500 mg",
  "species_variety_cultivar": null,
  "identity_status": "resolved",
  "identity_ambiguities": []
}
```

---

## 6. Status Vocabulary

| Status | Meaning |
|--------|---------|
| `resolved` | All required fields are filled with verified values |
| `partially_resolved` | Some fields filled; ambiguity log entry exists |
| `blocked` | Critical field(s) missing; ingredient cannot proceed |
| `needs_classification` | Product category or market classification pending |

# Output contract

Output follows the invocation route and the user's actual request. A normal evidence question gets a direct answer; case artifacts are generated only for a case or explicit personalization.

## 1. Direct evidence answer

Required fields:

- question and any population qualifier;
- direct plain-language answer;
- practical food/action examples when supported;
- evidence lanes and exact verified sources;
- applicability, uncertainty and important cautions;
- when testing or professional care may be appropriate.

Do not claim the question proves an individual diagnosis/deficiency. Do not require a case intake unless personalization or safety needs it.

## 2. Evidence card or exploration report

Use `assets/evidence-card-template.md` or `assets/evidence-exploration-template.md`.

Preserve exact source identity, lane, verification state, population, intervention/exposure, comparator, outcome, form/range/duration, applicability, contradictions and evidence debt. Search snippets and bibliographic-only records are leads, not claim support.

## 3. Synthetic/hypothetical training analysis

Label synthetic status visibly. Never merge it with a real case or use it as efficacy evidence. Use the hypothetical-case and review templates.

## 4. Individual diagnostic-support draft

Mandatory guard: `PROFESSIONAL DIAGNOSTIC-SUPPORT DISCLAIMER`.

Title exactly:

`INDIVIDUAL DIAGNOSTIC SUPPORT DRAFT — NOT A FINAL DIAGNOSIS`

Include problem representation, material alternatives, support/contradiction, missing data, not-to-miss considerations, evidence trace, qualitative confidence rationale, discriminating questions/evaluations for clinician consideration, red-flag result and licensed-reviewer disposition.

It may not make a final diagnosis, order tests, change medication or execute care.

## 5. Functional-medicine matrix bundle

A successful generated bundle contains by default:

- `functional_medicine_matrix.json` — normalized allowlisted state with artifact and semantic-input identity;
- `functional_medicine_matrix.md` — complete text-equivalent worksheet (default human-facing deliverable);
- `functional_medicine_matrix_manifest.json` — exact input/file hashes and completion rule.

The optional `--include-svg` flag adds `functional_medicine_matrix.svg` — a standalone responsive vector worksheet (no spokes or causal edges). Use the SVG only when the user explicitly asks for a figure/image/SVG/matrix diagram; do not infer image consent from case/personalization alone.

The manifest is written last and lists only files actually emitted; a consumer must reject the bundle if any listed file hash differs or if a listed file is absent. Each item, system assignment and candidate relationship needs provenance and uncertainty. The central MES is not an eighth physiological system. Repeat the non-diagnostic boundary and visible AI/reviewer state in every human-facing artifact. Coverage means documentation completeness only. The bundle may not claim to be an official or proprietary branded diagnostic instrument.

## 6. Formula/plan outputs

All classes include:

- output class;
- release state;
- permitted/prohibited use;
- populated components or unpopulated scaffold;
- blockers/missing fields;
- claim-level evidence and range/dose state;
- contraindication/interaction/duplication review;
- monitoring, stopping and escalation logic derived from the specific source/risk;
- required reviewer competence and recorded human review.

### Food/lifestyle recipe

Allowed states:

- `ready_for_low_risk_use`
- `professional_review_recommended`
- `blocked_for_safety_or_missing_core_input`

Low-risk food quantities, recipes and preparation may be directly usable after allergy/restriction/context checks. Do not make cure/treatment promises.

### Supplement plan

Allowed states:

- `incomplete_scaffold_needs_core_input`
- `draft_for_qualified_professional_review`
- `draft_with_mandatory_specialist_review`
- `rejected_for_safety`
- `human_review_recorded`

A populated regimen is always a professional-review draft. Unknown medication or allergy status blocks regimen population. Unsupported range is `NOT_DERIVABLE`; never guess a safe default dose.

### Medical-nutrition plan

Allowed states:

- `incomplete_scaffold_needs_clinical_data`
- `draft_for_responsible_clinical_team`
- `rejected_or_escalated`
- `human_clinical_authorization_recorded`

Scope: appropriate condition-specific MNT, oral nutrition supplements and enteral formula planning. IV/parenteral composition or independent inpatient orders are excluded and must return escalation/required-data output only.

### TCM formula

Allowed states:

- `incomplete_scaffold_needs_syndrome_or_identity`
- `draft_for_licensed_tcm_practitioner_review`
- `draft_with_mandatory_cross_specialty_review`
- `rejected_for_safety`
- `human_practitioner_review_recorded`

A populated formula is always a licensed-practitioner review draft. Missing syndrome differentiation or complete herb identity blocks composition and dose.

## 7. Stop/escalation output

When red flags, authorization failure, unsafe environment or excluded scope is present, return:

- observable reason for stop;
- what was and was not assessed;
- immediate care/escalation direction appropriate to the signal;
- any safe records/artifacts preserved;
- explicit statement that no routine formula was generated.

Do not invent a diagnosis.

## 8. Model validation and fallback

Before merging generated content, apply `reference/model-io-and-output-validation.md`. If validation fails:

- merge nothing from the invalid response;
- preserve deterministic local map/report/scaffold;
- record the failed gate without exposing prompts/secrets;
- ask only for the missing input or required reviewer;
- do not regenerate repeatedly to force a pass.

## 9. Artifact transparency and privacy

Human-facing artifacts must remove credentials, private paths, prompts, tool traces, direct identifiers and test markers. They must preserve material AI-assistance disclosure, evidence provenance, release state and reviewer status.

## 10. Global invariants

- facts, interpretation, evidence, preference and professional judgment remain separate;
- cases/examples are not efficacy evidence;
- no medication start/stop/switch/dose action;
- no autonomous final diagnosis or care execution;
- no populated high-risk formula under incomplete/unreviewed gates;
- no longitudinal versioning or generic staged dialogue engine in this version;
- workflow/release status is not clinical approval.

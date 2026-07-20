# Four Formula Classes and Release Gates

Every invocation returns a useful status artifact. Missing essential safety data may produce an incomplete scaffold, but never guessed ingredients, ranges or doses.

## Common gates

Before a formula class is populated:

- stop on acute red flags;
- record authorization, audience and purpose;
- minimize/de-identify case data;
- preserve medications, supplements, allergies, life stage, relevant organ function and known conditions;
- keep facts, interpretation and unknowns separate;
- run interaction, duplication, contraindication and special-population checks appropriate to the class;
- attach claim-level evidence state and reviewer requirement;
- preserve blocked components and reasons;
- never replace prescribed care or imply clinical/regulatory finality.

## Class 1 — food recipe / lifestyle plan

May be directly usable by an ordinary person only when low risk.

Core inputs: goal, dietary pattern/restrictions, allergies/intolerances, relevant conditions, medications when food–drug interaction is material, and life-stage context.

Allowed: meal patterns, recipes, food choices, sleep/movement/stress/relationship suggestions, ordinary portions/frequency, monitoring questions and escalation signs.

Not allowed: disease-treatment/cure/prevention promises, disguised supplement dosing, ignored allergies, deterministic biomarker effects, or severe restriction without nutrition adequacy/reintroduction planning.

Release states:

- `ready_for_low_risk_use`
- `professional_review_recommended`
- `blocked_for_safety_or_missing_core_input`

## Class 2 — supplement plan

A populated plan is always a professional-review draft.

Required: medications, current supplements, allergies/excipients, relevant life stage, age, conditions, pregnancy/lactation when clinically relevant, renal/hepatic context when relevant, interaction/duplication/upper-limit review and human evidence for each proposed form/range.

If a safe human range cannot be supported, use `NOT_DERIVABLE`. Unknown medication or allergy status blocks population of the regimen but still permits an incomplete review scaffold.

Release states:

- `incomplete_scaffold_needs_core_input`
- `draft_for_qualified_professional_review`
- `draft_with_mandatory_specialist_review`
- `rejected_for_safety`
- `human_review_recorded`

The title “nutritionist” alone is not a universal authority. Record the competence and local scope required.

## Class 3 — medical nutrition

Current scope supports professional drafts for condition-specific MNT, oral nutrition supplements and enteral formula planning. Parenteral nutrition, IV nutrient protocols and independent inpatient orders are excluded; return escalation/required-data output only.

A populated draft requires responsible clinical-team context, indication or working diagnosis, route and setting, anthropometry/intake, relevant labs, contraindications, medication context, clinical source/guideline, calculation provenance, monitoring and reviewer authority.

Consider refeeding, fluid/electrolyte, glycemic, renal/hepatic and route/device risks when relevant. Missing core clinical data yields an incomplete scaffold, not a formula.

Release states:

- `incomplete_scaffold_needs_clinical_data`
- `draft_for_responsible_clinical_team`
- `rejected_or_escalated`
- `human_clinical_authorization_recorded`

## Class 4 — TCM formula

A populated formula is always a licensed-practitioner review draft.

Required: practitioner-provided or practitioner-reviewable syndrome differentiation, complete herb identity, medicinal part, processing/preparation, formula context, medications/supplements/allergies, relevant life stage and organ function, herb–drug/formula-level safety, and current jurisdiction/product-category context when relevant.

Evidence stays separate:

- classical/traditional record — historical rationale only;
- current official identity/quality standard;
- modern human clinical evidence;
- safety/interaction evidence;
- regulatory status.

If syndrome differentiation or herb identity is missing, return questions and an incomplete scaffold only. Do not use a vague constitutional approach to bypass the gate.

Release states:

- `incomplete_scaffold_needs_syndrome_or_identity`
- `draft_for_licensed_tcm_practitioner_review`
- `draft_with_mandatory_cross_specialty_review`
- `rejected_for_safety`
- `human_practitioner_review_recorded`

## Monitoring

No universal 4–8 or 8–12 week default. Timing, outcomes, stopping rules and escalation must come from the specific intervention, source, risk, clinical setting and responsible reviewer.

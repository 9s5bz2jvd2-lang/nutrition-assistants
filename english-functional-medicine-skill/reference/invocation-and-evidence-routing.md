# Invocation and evidence routing

This Skill has two invocation routes. Route by the user's actual input and request; do not force every question through case intake.

## Route A — direct knowledge/evidence question

Use this route when the user asks a general question without providing a case or requesting a personalized plan.

Examples:

- "What should I eat if I'm low on vitamin A?"
- "What is the evidence on dietary fiber and constipation?"
- "How should a given food and a given nutrient be combined?"

### Input

Required:

- the user's question;
- any population qualifier already supplied, such as adult, child or pregnancy.

Optional:

- desired answer depth;
- country/region when guideline or food availability matters;
- one safety fact needed to answer the exact question.

Do not require a case packet, matrix fields or a full intake.

### Procedure

1. Use the Skill's internal material as a concept map and query planner, not as proof that current evidence is still valid.
2. Retrieve and verify current authoritative guidance first when the question is practice-facing. Then retrieve relevant systematic reviews and RCTs; use observational studies for associations and animal/in-vitro evidence only as explicitly labeled mechanistic support.
3. Record exact source identity, year/version, population, intervention/exposure, comparator, outcome, applicability and limitation.
4. Answer the user's question directly in plain language. Distinguish guideline recommendation, human efficacy evidence, observational association, mechanistic support and unknown.
5. Give food examples, practical preparation or pairing advice and relevant cautions when supported.
6. Ask only the minimum safety clarification that can materially change the answer. A simple question must not be upgraded into a full case-analysis ritual.

### Escalate to Route B only when

- the user supplies personal symptoms, labs, diagnoses, medications, diet records or a case narrative and asks for analysis;
- the user asks for a personalized plan or formula;
- the answer would require a personalized supplement dose, medical-nutrition prescription or TCM formula;
- safety cannot be assessed without case-specific facts.

A general answer may explain when professional assessment or testing is appropriate. It must not pretend that a general question proves a deficiency or diagnosis.

## Route B — case analysis / personalized plan

Use this route only when the user supplies a case or explicitly requests analysis or a personalized plan.

### Input accepted

The user may provide messy natural language, chat excerpts, diet records, labs, symptoms, diagnoses, medications, supplements or professional notes. Do not require a webpage or a completed form.

Normalize internally into:

```json
{
  "intent": "case_analysis",
  "question": "what the user wants now",
  "requested_outputs": [
    "functional_medicine_matrix",
    "diagnostic_support_draft",
    "food_recipe",
    "supplement_plan",
    "medical_nutrition_plan",
    "tcm_formula"
  ],
  "source_records": [
    {
      "record_type": "free_text|diet|lab|medication|supplement|professional_note|other",
      "date": "known date or unknown",
      "content": "source content",
      "source": "user|clinician|laboratory|document|unknown",
      "certainty": "reported|verified|unknown"
    }
  ],
  "constraints": {
    "privacy_authorized": true,
    "deidentified": true,
    "intended_reviewer": "self|dietitian|physician|tcm_practitioner|team|unknown",
    "allergies": [],
    "medications": [],
    "pregnancy_or_lactation": "yes|no|unknown",
    "dietary_preferences": [],
    "budget_or_access": "free text"
  }
}
```

This is an internal normalization contract, not a form the user must fill.

### Procedure

1. Confirm authorization, minimum necessary use and de-identification for individual records.
2. Preserve source, date and uncertainty. Never convert a reported statement into a verified fact.
3. Run red-flag and scope checks before routine reasoning.
4. Determine sufficiency separately for each requested output; do not use one universal completeness threshold.
5. Produce every safe artifact that is currently possible. For unmet high-risk gates, produce a useful structured scaffold, exact missing-data list and reviewer route instead of guessed ingredients or doses.
6. Generate a functional medicine matrix only as a non-diagnostic organizing worksheet with per-item and per-link provenance; do not draw causal edges or spokes.
7. Apply the appropriate formula-class gate before populating a food recipe, supplement plan, medical-nutrition plan or TCM formula.
8. Keep facts, interpretation, evidence, user preference and professional judgment visibly separate.

## Output-specific sufficiency

| Requested output | Minimum sufficiency rule |
|---|---|
| functional medicine matrix | at least one source-grounded item; unmatched information stays `unclassified`; no fake finding is inserted; no causal edges or spokes; default deliverable is the Markdown text matrix; SVG is opt-in only |
| diagnostic-support draft | deidentified authorized case, problem representation, material alternatives, support/contradiction, red-flag result and professional reviewer route |
| food recipe | relevant allergies/intolerances, major medical restrictions and user food/access constraints; general food education may still be given when personalization is not safe |
| supplement plan | indication, current medications/supplements, allergy, pregnancy/lactation, organ-function considerations, product/ingredient identity, evidence and qualified reviewer gate |
| medical-nutrition plan | clinical indication, intake/anthropometry as applicable, GI/oral/enteral feasibility, relevant labs/risks and clinical nutrition reviewer; parenteral/IV planning is escalation only |
| TCM formula | explicit syndrome differentiation by an appropriate practitioner, complete materia-medica identity, contraindication/interaction review, evidence status and practitioner approval |

## Route invariants

- Direct evidence question → answer directly with fresh verified evidence.
- Case or explicit personalization → analyze the case.
- No generic staged conversation engine.
- No longitudinal history/version feature in this implementation.
- No case-shaped answer to a topic-only question.
- No general educational answer presented as individualized treatment.

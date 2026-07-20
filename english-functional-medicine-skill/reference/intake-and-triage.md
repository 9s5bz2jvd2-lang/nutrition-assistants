# Intake and triage

Intake applies only to Route B: an actual case or explicit personalized-plan request. A normal knowledge/evidence question uses Route A and must not be forced through this document.

## 1. Authorization and privacy gate

Internal mode marker: `AUTHORIZED_DEIDENTIFIED_INDIVIDUAL`.

Before processing individual material, establish:

- who supplied the material and for what purpose;
- whether the person is using their own information or has authority to provide it;
- whether minimum-necessary, de-identified processing is possible;
- intended audience: self, dietitian, physician, TCM practitioner or governed team;
- whether the current environment is appropriate for the material.

Do not copy direct identifiers into ordinary artifacts. If authorization or safe handling is unclear, stop and return a privacy/authorization clarification, not a case interpretation.

## 2. Accept messy input

The person may provide natural-language messages, diet logs, symptoms, labs, diagnoses, medications, supplements or professional notes. Do not require a webpage or full form.

Normalize each source record with:

- record type;
- date/period or `unknown`;
- source/author or `unknown`;
- content;
- verification state: `reported`, `document_verified` or `unknown`;
- uncertainty/contradiction notes.

Never convert user-reported text into a verified finding.

## 3. Requested output first

Record what the user actually wants:

- functional medicine matrix;
- individual diagnostic-support draft;
- food/lifestyle recipe;
- supplement plan;
- medical-nutrition plan;
- TCM formula.

One request may include several outputs. Sufficiency is assessed independently for each. Missing data for one high-risk output must not prevent a safe low-risk or organizational artifact.

## 4. Immediate red-flag stop

Before routine analysis, check whether the supplied information suggests urgent or potentially dangerous circumstances. The Skill does not diagnose emergencies. If urgent evaluation may be needed:

- stop routine formula generation;
- state the observable concern without inventing a diagnosis;
- direct the user to appropriate urgent/emergency care;
- do not let a recipe, supplement, MNT or TCM formula delay care.

Examples requiring conservative escalation include severe breathing difficulty, altered consciousness, severe chest pain, uncontrolled bleeding, severe dehydration, dangerous laboratory values, acute neurologic deficit, severe allergic reaction, rapidly deteriorating symptoms or explicit self-harm risk. This is not an exhaustive diagnostic list.

## 5. Core case domains

Collect only what is relevant to the requested output. Candidate domains include:

- age/life stage; pregnancy/lactation when relevant;
- goals and current concerns;
- symptom timing/course/severity and competing explanations;
- known diagnoses and major history;
- current medications, supplements and allergies/intolerances;
- diet pattern, intake and food access;
- anthropometry and weight change when relevant;
- labs/tests with units, reference range, date and source;
- GI/oral/swallowing/enteral context when relevant;
- renal/hepatic/cardiometabolic context when relevant;
- sleep, movement, stress and relationship context;
- clinician/dietitian/TCM assessment already available;
- user preferences, budget, cultural context and acceptable burden.

Unknown is valid. Do not fill it with a model guess.

## 6. Per-output sufficiency

### Functional medicine matrix

At least one source-grounded item is enough. Preserve unmatched material as `unclassified`. Never insert a fake example merely to make the worksheet non-empty.

### Diagnostic-support draft

Requires enough de-identified material for a problem representation, support/contradiction, material alternatives, missing data, not-to-miss considerations, evidence trace and reviewer route. Otherwise output an incomplete structured question set.

### Food/lifestyle recipe

Requires allergy/intolerance status, major medical restrictions and relevant preferences/access. Ordinary food education may still be possible when personalized planning is not.

### Supplement plan

A populated regimen requires the exact fields in `reference/formula-class-gates.md`, including current medication/supplement context, allergy/excipient issues, relevant life stage/organ function, identity, evidence, interactions/duplication and reviewer gate. Missing core fields yield an unpopulated scaffold.

### Medical-nutrition plan

A populated oral/MNT/enteral draft requires responsible clinical context, indication, route/setting, relevant intake/anthropometry/labs/risks, calculation provenance, monitoring and clinical reviewer. IV/parenteral planning is escalation only.

### TCM formula

A populated formula requires practitioner-provided or practitioner-reviewable syndrome differentiation, complete herb identity, contraindication/interaction review, evidence status and licensed-practitioner review. Missing syndrome or identity yields questions plus scaffold only.

## 7. Structured reasoning

After triage:

1. separate fact, interpretation, hypothesis, preference and professional judgment;
2. use Six-Eye inquiry to expose missing dimensions without treating it as a validated diagnostic instrument;
3. record supporting and contradicting material;
4. preserve unknowns and competing explanations;
5. use the functional medicine matrix only as an organizing/completeness worksheet;
6. retrieve evidence for each material claim/formula component;
7. apply the exact release gate before populating a plan.

## 8. No generic staged dialogue engine

Do not force gather → mirror → judge → return or any other fixed sequence. If the supplied case is sufficient, proceed. If it is not, ask only the smallest set of questions needed for the requested output. A missing high-risk gate returns a scaffold rather than endless questioning.

## 9. Output readiness

Every requested output ends in one of these outcomes:

- safe output produced under its class status;
- incomplete scaffold with exact missing fields;
- professional/specialist review required;
- rejected for safety;
- red-flag escalation/stop.

Never present a workflow status as clinical approval.

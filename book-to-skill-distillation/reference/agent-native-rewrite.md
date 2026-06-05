# agent-native-rewrite

Book distillation means rewriting a source into operational memory for agents. A book is linear: it teaches a human by sequence, exposition, examples, and repetition. A skill is callable: it should let an agent route a task, choose a procedure, request documents, inspect evidence, detect issues, draft findings, and know when to verify current law.

## Rewrite targets

Transform source material into these agent-native forms:

| Source pattern | Agent-native form |
|---|---|
| chapter narrative | routing table + task entry points |
| conceptual explanation | decision rule / checklist / caveat |
| long legal discussion | issue schema: facts → rule/current-law check → risk → remediation → evidence → report language |
| repeated examples | normalized finding patterns and red-flag leaves |
| document lists | DDQ / request list / evidence checklist |
| procedural prose | step-by-step workflow with stop/go gates |
| citations | statute map with freshness warning and verification procedure |
| case anecdotes | abstracted risk pattern, not copied fact pattern |

## What not to do

- Do not preserve the source order merely because the book is ordered that way.
- Do not copy long passages, even if OCR makes it easy.
- Do not treat old statutory citations as current without verification.
- Do not mix private extraction substrate with publishable skill content.
- Do not make one giant reference file when the agent needs progressive disclosure.

## Canonical per-topic rewrite recipe

For each chapter/topic:

1. Identify the task an agent would be doing when it loads the module.
2. Extract the topic’s operating procedure into: scope, documents, public searches, review tests, and report outputs.
3. Convert common issues into leaves using this schema:
   - Trigger / when to suspect
   - Facts to collect
   - Documents and public sources to verify
   - Legal/risk question to analyze
   - Risk severity and transaction impact
   - Remediation / condition precedent / disclosure / indemnity options
   - Draft finding pattern
   - Current-law verification notes
4. Add cross-links to adjacent modules; agents should traverse by issue relation, not by book page.
5. Include source uncertainty notes if OCR or page mapping is weak.

## Done definition

The result is agent-native when a future agent can load a small router, jump to the relevant module, run a checklist or prompt, produce a first-pass workpaper/finding, and know what external law or facts must be refreshed.

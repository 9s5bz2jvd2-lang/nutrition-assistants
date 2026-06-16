# Loop Architecture — The Dietary Guide Assistant as a Running Loop

## Architecture overview

```
┌─────────────────────────────────────────────────────────┐
│                 LOOP DIETARY GUIDE ASSISTANT              │
│                                                          │
│  ┌──────────┐    ┌──────────────┐    ┌──────────────┐  │
│  │Automation│───→│ Triage Skill │───→│  State File  │  │
│  │ (daily)  │    │  (classify)  │    │  (on disk)   │  │
│  └──────────┘    └──────┬───────┘    └──────────────┘  │
│                         │                                 │
│              ┌──────────┴──────────┐                     │
│              ▼                     ▼                     │
│     ┌──────────────┐     ┌──────────────┐               │
│     │    MAKER     │     │   CHECKER    │               │
│     │  (draft      │────→│  (verify     │               │
│     │   advice)    │     │   against     │               │
│     └──────────────┘     │   Guidelines │               │
│                          │   + safety)  │               │
│                          └──────┬───────┘               │
│                                 │                        │
│                    ┌────────────┴────────────┐          │
│                    ▼                         ▼          │
│           ┌──────────────┐         ┌──────────────┐    │
│           │  PUBLISH /   │         │  ESCALATE /  │    │
│           │  RESPOND     │         │  FLAG        │    │
│           └──────────────┘         └──────────────┘    │
│                                                          │
│  Skills: guidelines-content.md, dietary-pattern, etc.    │
│  Connectors: food-DB, evidence-source, nutrition-label   │
│  Worktrees: parallel claim verification                  │
└─────────────────────────────────────────────────────────┘
```

## The six primitives in dietary context

### 1. Automations — When the loop runs

| Automation type | Schedule | What it does |
|---|---|---|
| **Dietary triage** | Daily | Scan incoming questions/claims; classify into safe-answer / needs-verification / needs-human |
| **Compliance check** | Weekly | Review all advice given this week; check for safety boundary violations |
| **Guideline update scan** | Monthly | Check for new DGAC reports, DGA amendments, or relevant NASEM/ICCPUD publications |
| **State reconciliation** | After each session | Ensure state file is current; flag unresolved escalations |

### 2. Worktrees — When claims need parallel verification

```
Question batch arrives:
  ├── Claim A: "Coffee increases cancer risk" → Worktree 1 → Checker A
  ├── Claim B: "Children should drink whole milk" → Worktree 2 → Checker B
  └── Claim C: "Alcohol limit is 2 drinks/day for men" → Worktree 3 → Checker C
```

Each claim gets isolated verification. The state file tracks which worktrees are in progress.

### 3. Skills — What the agent knows (immutable dietary knowledge)

| Skill | Content | When loaded |
|---|---|---|
| `guidelines-content` | 5 Guidelines + life-stage rules | Always (shared core) |
| `dietary-pattern` | "Eat Healthy Your Way" 2,000-calorie table | Quantitative food-group questions |
| `alcohol-context` | Political timeline + 3 recommendations | Any alcohol question |
| `sustainable-diet` | 5 sustainable practices | Environment + health intersection |
| `glossary` | Key term definitions | Term lookup |

### 4. Connectors — What the agent can reach

| Connector | What it provides | When needed |
|---|---|---|
| Food composition DB | Nutrient values per food | Quantitative dietary analysis |
| Nutrition label API | Product-specific nutrient data | Product-specific questions |
| Evidence source lookup | DGAC report sections, CSPI publications | Evidence verification |

### 5. Sub-agents — Maker ≠ Checker

```
MAKER sub-agent:
  Input: question + relevant skills + food data
  Job: draft dietary advice based on Guidelines
  Output: draft response with guideline references

CHECKER sub-agent:
  Input: maker's draft + same skills + safety checklist
  Job: verify against Guidelines + safety gates
  Output: PASS (with notes) / REVISE (with specific issues) / ESCALATE (with reason)
```

### 6. State — What the loop remembers

```markdown
# State File: dietary-loop-state.md

## Session: 2026-06-16
- Questions triaged: 12
- Safe answers: 8
- Needed verification: 3
- Escalated to human: 1
- Safety flags: 0
- Unresolved escalations: 1 (alcohol limit for medication-interaction patient)

## Weekly compliance:
- All advice checked against Guidelines: YES
- Special population checks performed: YES
- Official vs. uncompromised clarified (where alcohol): YES
- Human review of flagged items: PENDING

## Open items:
- [ ] Follow up on escalated alcohol question
- [ ] Verify claim about potassium supplementation in elderly
```

---

## The complete daily loop cycle

```
1. AUTOMATION fires (daily schedule)
2. Load SKILLS (guidelines-content, dietary-pattern, etc.)
3. Read STATE file (pick up from yesterday)
4. For each new question/claim:
   a. TRIAGE: classify (safe / verify / escalate)
   b. If safe → MAKER drafts answer → CHECKER confirms → respond
   c. If verify → MAKER drafts → CHECKER verifies with evidence → respond with source labels
   d. If escalate → log to state file, flag for human
5. After all questions: update STATE
6. If /goal condition met (all questions resolved) → stop
7. If unresolved items → they carry forward to tomorrow's run
```

## Scaling rules

| Scale | Pattern | Watch for |
|---|---|---|
| 1 question | Single maker-checker cycle | Over-engineering: don't loop a one-off question |
| 5–10 questions/day | Daily triage + state file | Stale skills: update when guidelines change |
| 50+ questions/day | Parallel worktrees + batch triage | Orchestration tax: human review bandwidth |
| Unattended overnight | Full loop + `/goal` + verification gate | Cognitive surrender: did a human check the flagged items? |

---

## Tool-agnostic design

The loop architecture maps onto any agent runtime:

| Primitive | Codex | Claude Code | Any runtime |
|---|---|---|---|
| Automation | Automations tab | `/loop` or cron | Any scheduler |
| Worktree | Built-in | `--worktree` | Git worktree |
| Skills | `SKILL.md` | `SKILL.md` | Any skill format |
| Connectors | MCP | MCP | Any API connector |
| Sub-agents | `.codex/agents/` | `.claude/agents/` | Any multi-agent setup |
| State | Markdown or Linear | Markdown or Linear | Any persistent store |

# Loop Design Pattern — A Concrete Example and Generic Checklist

## 1. The Morning Triage Loop (from the article)

This is the canonical example of a complete loop in action:

```
Every morning:
  1. Automation runs on the repo
  2. Prompt calls a triage skill
  3. Skill reads yesterday's CI failures + open issues + recent commits
  4. Findings written into a markdown file or Linear board (STATE)
  5. For each finding worth doing:
     a. Thread opens an isolated WORKTREE
     b. Sub-agent drafts the fix (MAKER)
     c. Second sub-agent reviews against project SKILLS + existing tests (CHECKER)
  6. CONNECTOR opens the PR and updates the ticket
  7. Unhandleable items land in triage inbox for the developer
  8. STATE file remembers: tried, passed, still open
  9. Tomorrow's run picks up where today stopped
```

> You designed it one time. You did not prompt any of those steps. That's Steinberger's whole point made real.

---

## 2. Generic Loop Design Checklist

Use this checklist when designing any autonomous coding-agent loop:

### Boundary
- [ ] Source repo identified and accessible
- [ ] Legal/privacy boundary confirmed (what the loop can read/write)
- [ ] Task scope defined (triage? bug-fix? feature? migration?)
- [ ] Human escalation path defined (what the loop cannot handle)

### Automations
- [ ] Cadence set (daily? per-commit? on-demand?)
- [ ] Automation prompt calls a skill (not a wall of instructions)
- [ ] `/goal` condition defined for run-until-done tasks
- [ ] `/loop` cadence defined for recurring tasks
- [ ] Separate model checks the stop condition

### Worktrees
- [ ] Each parallel task gets its own worktree
- [ ] Max parallel count ≤ human review bandwidth
- [ ] Merge strategy defined

### Skills
- [ ] Project conventions written into `SKILL.md`
- [ ] Build steps, test commands, "we don't do X because Y" captured
- [ ] Skill descriptions are precise (not clever) for implicit matching
- [ ] Intent debt filled: no gaps the agent will guess at

### Connectors / Plugins
- [ ] Issue tracker connected
- [ ] CI/CD status accessible
- [ ] PR creation automated (not manual)
- [ ] Notification channel reachable if needed
- [ ] Connectors packaged as plugin for team reuse

### Sub-agents
- [ ] Maker and checker are different agents
- [ ] Verifier has different instructions from implementer
- [ ] Verifier may use stronger model / higher reasoning effort
- [ ] Explorer agent is read-only and fast
- [ ] Token budget allocated for sub-agent overhead

### State
- [ ] State file format defined (markdown? board?)
- [ ] State records: tried, passed, open, next steps
- [ ] State is on disk, not in conversation context
- [ ] Next run reads state to pick up where previous stopped

### Dangers (MUST check)
- [ ] Verification gate present (loop doesn't ship without confirmation)
- [ ] Comprehension debt addressed (someone reads what the loop made)
- [ ] Cognitive surrender guard (human maintains independent judgment)
- [ ] Token cost budgeted (especially for sub-agents)
- [ ] "Done" is verified, not just claimed

---

## 3. Loop Architecture Decision Tree

```
Is the task recurring?
├── YES → Use /loop with a cadence
│         └── Does it need to run until a condition is true?
│             ├── YES → Use /goal instead of /loop
│             └── NO → /loop is correct
└── NO → Is the task multi-step?
    ├── YES → Can steps run in parallel?
    │         ├── YES → Use worktrees + sub-agents
    │         └── NO → Sequential in one thread, state file tracks progress
    └── NO → Single prompt is fine. No loop needed.
```

---

## 4. Scaling Rules

| Scale | Pattern | Watch for |
|---|---|---|
| 1 agent, 1 task | Simple automation + state file | Over-engineering: don't add a loop for a one-shot task |
| 1 agent, recurring | `/loop` + skill + state | Stale skills: update when conventions change |
| 2 agents (make + check) | Worktree + sub-agents + state | Maker-checker alignment: do they agree on the spec? |
| N agents, parallel | N worktrees + skills + connectors + shared state | **Orchestration tax**: your review bandwidth is the ceiling |
| Unattended overnight | Full loop + `/goal` + verification gate | **Cognitive surrender**: did you read what it shipped? |

---

## 5. Tool-Agnostic Observation

> A year ago, if you wanted a loop, you wrote a pile of bash and maintained it forever. Now the pieces ship inside the products.

Steinberger's list maps almost exactly onto the Codex app, and then almost the same onto Claude Code. Once you notice the shape is the same, you stop arguing about which tool — you just design a loop that still works no matter which one you happen to be sitting in.

**Implication:** Design your loop in terms of the six primitives (automations, worktrees, skills, connectors, sub-agents, state), not in terms of a specific vendor's CLI flags. The vendor is the implementation; the primitives are the architecture.

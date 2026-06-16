# CACHE.md — loop-engineering cache layout

## 1. Stable prefix (200–800 tokens, rarely changes)

- Skill name + one-line purpose: "Design autonomous coding-agent loops, not interactive prompting."
- Shared core rules: design not prompt, maker ≠ checker, state on disk, skills compound, loops change work.
- Red lines: no unattended loop without verification, no skipping reading output, no cognitive surrender.
- Key quotations table (source-anchored, 5 entries).
- Router table (situation → read next).

## 2. Variable suffix (changes per task)

- Current loop-design task description
- Selected primitives for this task
- Vendor-specific configuration (Codex / Claude Code / other)
- Current draft of the loop
- Human preferences and constraints

## 3. On-demand reference

- Full primitives comparison table (Codex vs. Claude Code)
- Concrete loop-design-pattern walkthrough
- Detailed danger analysis with mitigation strategies
- Eval case details

## 4. Budget

| Content | Default budget | When to upgrade |
|---|---:|---|
| Shared core (SKILL.md) | 200–800 tokens | Almost never |
| Primitives reference | 800–3000 tokens | Designing a new loop |
| Loop design pattern | 800–2000 tokens | Moving to concrete implementation |
| Dangers reference | 400–1200 tokens | Any unattended loop |
| Eval cases | 200–600 tokens | Validating a loop design |

## 5. Gotchas

1. **Loop ≠ prompt replacement for simple tasks** — A single prompt is fine for simple work. Loop engineering adds value when work is recurring, multi-step, or needs parallel verification.
2. **Worktree count ceiling = human review bandwidth** — The orchestration tax means your review capacity, not the tool, determines how many parallel branches you can sustain.
3. **Token cost warning** — Sub-agents burn more tokens (each does its own model + tool work). Spend them where a second opinion is worth paying for.
4. **"Done" is a claim, not a proof** — The maker-checker split makes "done" meaningful, but it does not eliminate the need for human confirmation.
5. **Comfortable posture = dangerous posture** — When the loop runs itself, it is very tempting to stop having an opinion. Designing the loop is the cure when done with judgement, and the accelerant when done to avoid thinking.

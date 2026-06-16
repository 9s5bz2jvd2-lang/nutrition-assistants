# Loop Primitives — The Six Pieces (Plus One)

A loop needs six things. The first five do the work; the sixth remembers what happened.

---

## 1. Automations — Discovery + Triage on a Schedule

**Job:** Find the work, sort it, and surface it without human intervention.

### What it does
- Runs on a cadence (daily, hourly, per-commit)
- Reads CI failures, open issues, recent commits, etc.
- Writes findings into a triage inbox or state file
- Decides which findings are worth acting on

### `/loop` vs. `/goal`
| Primitive | Behavior | Use when |
|---|---|---|
| `/loop` | Re-runs on a fixed cadence | Ongoing monitoring (e.g., daily triage) |
| `/goal` | Keeps going until a condition is true | One-shot completion (e.g., "all tests pass and lint is clean") |

**Critical detail:** In `/goal`, a *separate small model* checks whether the loop is done after every turn — the agent that wrote the code is not the one grading it. This is the maker-checker split applied to the stop condition itself.

### Tool comparison

| Feature | Codex | Claude Code |
|---|---|---|
| Schedule | Automations tab: pick project, prompt, cadence, environment | Cron, hooks, GitHub Actions |
| Run-until-done | `/goal` with pause/resume/clear | `/goal` |
| Recurring | Automations with cadence | `/loop` |
| Inbox | Results land in Triage inbox | Results land in state file or board |

### Design checklist
- [ ] Cadence defined (daily? per-commit? on-demand?)
- [ ] Prompt calls a skill, not a wall of instructions
- [ ] Findings written to a persistent state file
- [ ] Unhandleable items escalate to human triage inbox

---

## 2. Worktrees — Isolate Parallel Features

**Job:** Let two agents work on the same repo at the same time without stepping on each other.

### What it does
- A git worktree is a separate working directory on its own branch sharing the same repo history
- Each agent/thread gets its own checkout
- Prevents mechanical file conflicts

### Tool comparison

| Feature | Codex | Claude Code |
|---|---|---|
| Built-in worktree | Per thread | `--worktree` flag |
| Sub-agent isolation | — | `isolation: worktree` on sub-agent |
| Cleanup | Automatic | Automatic |

### Orchestration tax
> Worktrees take away the mechanical collision but **you are still the ceiling** — your review bandwidth decides how many you can actually run, not the tool.

### Design checklist
- [ ] Each parallel task has its own worktree
- [ ] Review bandwidth estimated before launching parallel branches
- [ ] Merge strategy defined before agents start

---

## 3. Skills — Codify Project Knowledge

**Job:** Write down project conventions once so the agent reads them every run instead of you re-explaining.

### What it does
- A folder with a `SKILL.md` holding instructions and metadata
- Optional scripts, references, and assets
- The agent loads the skill instead of you pasting context

### Skills vs. Intent Debt
> An agent starts every session cold and fills any hole in your intent with a confident guess. A skill is that intent written down on the outside — the conventions, the build steps, the "we don't do it like this because of that one incident" — written one time where the agent reads it every run.

**Without skills:** the loop re-derives your whole project from zero every cycle.
**With skills:** knowledge compounds.

### Skills vs. Plugins
| Concept | Role |
|---|---|
| Skill | The authoring format (`SKILL.md` + folder) |
| Plugin | How you distribute it (bundled skills + connectors for teammate install) |

### Design checklist
- [ ] Skills written for every recurring convention
- [ ] Skill descriptions are tight and boring (not clever) — they must match the right tasks
- [ ] Build steps, exceptions, and "why not" rationales captured

---

## 4. Plugins & Connectors — Connect Your Tools

**Job:** Let the loop see beyond the filesystem.

### What it does
- Connectors (built on MCP) let the agent: read issue trackers, query databases, hit APIs, send messages
- Plugins bundle connectors + skills for one-click install
- Both Codex and Claude Code speak MCP — a connector written for one usually works in the other

### The key distinction
> This is the difference between an agent that says "here is the fix" and a loop that opens the PR, links the Linear ticket, and pings the channel once CI is green — by itself.

### Design checklist
- [ ] Issue tracker connected (Linear, GitHub Issues, etc.)
- [ ] CI/CD status accessible
- [ ] Communication channels reachable (Slack, etc.) if auto-notification needed
- [ ] Connectors shared via plugin, not manually configured

---

## 5. Sub-agents — Ideate and Verify

**Job:** Keep the maker away from the checker.

### What it does
- Spawns separate agents for different tasks
- The most useful structural split: **one writes, one reviews**
- The model that wrote the code is too nice grading its own homework

### Typical splits
| Role | Job | Model effort |
|---|---|---|
| Explorer | Read codebase, find relevant files | Fast, read-only |
| Implementer | Write the fix | Normal |
| Verifier | Review against spec + project skills + tests | Strong model, high reasoning effort |

### Tool comparison

| Feature | Codex | Claude Code |
|---|---|---|
| Definition format | `.codex/agents/` TOML files | `.claude/agents/` files |
| Per-agent model | Yes (TOML: `model`, `reasoning_effort`) | Yes |
| Per-agent instructions | Yes | Yes |
| Agent teams | — | Teams that pass work between them |
| Spawning | When asked | Sub-agents and agent teams |

### Token cost warning
> Sub-agents burn more tokens since each does its own model and tool work. Spend them where a second opinion is worth paying for.

### Design checklist
- [ ] Maker and checker are different agents
- [ ] Verifier uses different instructions (and sometimes a different model) from implementer
- [ ] `/goal` stop condition checked by a separate model
- [ ] Token budget allocated for sub-agent overhead

---

## 6. State — Track What's Done (The Sixth Piece)

**Job:** Remember progress across runs.

### What it does
- A markdown file, or a Linear board — anything that lives outside the conversation
- Holds: what's done, what's in progress, what's still open
- The spine of the whole loop

### Core principle
> **The agent forgets, the repo doesn't.**

The model forgets everything between runs, so the memory has to be on disk and not in the context.

### Tool comparison

| Feature | Codex | Claude Code |
|---|---|---|
| State format | Markdown or Linear via connector | Markdown (`AGENTS.md`, progress files) or Linear via MCP |
| Persistence | On disk, outside conversation | On disk, outside conversation |

### Design checklist
- [ ] State file defined before the loop starts
- [ ] State includes: tried, passed, open, next steps
- [ ] Tomorrow's run picks up where today stopped
- [ ] State is not in conversation context — it's on disk

---

## Full Comparison Table

| Primitive | Job in the Loop | Codex App | Claude Code |
|---|---|---|---|
| **Automations** | discovery + triage on a schedule | Automations tab; `/goal` for run-until-done | Cron, `/loop`, `/goal`, hooks, GitHub Actions |
| **Worktrees** | isolate parallel features | Built-in worktree per thread | `git worktree`, `--worktree`, `isolation: worktree` |
| **Skills** | codify project knowledge | Agent Skills (`SKILL.md`), `$name` or implicit | Agent Skills (`SKILL.md`) |
| **Plugins / connectors** | connect your tools | Connectors (MCP) + plugins | MCP servers + plugins |
| **Sub-agents** | ideate and verify | `.codex/agents/` TOML | `.claude/agents/`, agent teams |
| **State** | track what's done | Markdown or Linear via connector | Markdown (`AGENTS.md`) or Linear via MCP |

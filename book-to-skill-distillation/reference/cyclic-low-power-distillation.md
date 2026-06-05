# cyclic-low-power-distillation

> **网以通达，球以成身。心神合一，我圆如一。**
>
> Networks make knowledge reachable; cyclic return makes the system a body.

Distillation is not a one-way compression from source to skill. It is a bounded cycle: send work outward, bring lessons back, keep the core intact, and spend energy only where it changes the next action.

Use this reference when a book, long PDF, manual, or knowledge base is being rewritten into an agent-native skill and the work is large enough to involve daemons, multiple passes, human review, or reusable methodology. It adds a cyclic, low-power discipline on top of the normal `book-to-skill-distillation` workflow.

This is a general distillation discipline. Domain-specific safety rules — medical, legal, financial, security, etc. — belong in the target domain skill, not here.

---

## 1. The principle: web to reach, sphere to return

The original book-to-skill workflow is network-shaped in the best sense: it turns linear source material into routers, modules, checklists, schemas, and reference paths. That web lets an agent reach the right operational unit quickly.

The cyclic overlay adds a second shape: a sphere, or a bounded body. It asks whether the outward branches return to a center.

- **Branch**: split the source into topics, send daemons outward, produce modules.
- **Return**: collect reusable templates, gotchas, prompts, validation cases, and process lessons.
- **Keep one**: preserve the invariant core — copyright/privacy discipline, trigger/exclusion scope, validation standards, and the target skill's voice.

If there is only branch and no return, the work expands but does not learn. If there is only return and no branch, the work stays elegant but does not act. A healthy distillation system does both.

---

## 2. Draw the boundary before extracting

Before reading or rewriting deeply, name three zones:

| Zone | What belongs there | Rule |
|---|---|---|
| **Source substrate** | PDFs, OCR text, page renders, raw transcripts, extracted tables | Private workspace only; never publish raw substrate inside the skill. |
| **Invariant core** | trigger, exclusions, copyright/privacy discipline, verification rules, voice, validation gates | Parent agent/human reviewer controls this; daemons do not rewrite it casually. |
| **Published skill artifacts** | router, reference modules, checklists, schemas, prompts, scripts, examples, validation cases | Publish only transformed operational artifacts. |

Boundary rule:

> Raw source text enters through the substrate boundary; only transformed operational memory exits into the skill.

This protects copyright, privacy, quality, and identity. It also prevents the skill from becoming a disguised copy of the book.

---

## 3. Track a trajectory for each run

Every substantial distillation run should carry a lightweight trajectory record. It can be YAML, JSON, or a Markdown section, but it must be structured enough to resume after interruption.

```yaml
distillation_trajectory:
  source:
    title: ""
    type: "book | long_pdf | manual | knowledge_base | mixed"
    substrate_path: "work/book-distill/<slug>/"
    source_limitations: []
  target:
    skill_id: ""
    trigger: ""
    exclusions: []
    primary_routing_axis: "phase | issue | document | persona | risk | other"
  invariant_core:
    copyright_privacy_rules: "reference/copyright-discipline.md"
    verification_rules: []
    voice_or_style_notes: []
    validation_gates: []
  fanout:
    daemon_ids: []
    topic_files: []
    assigned_outputs: []
  return_contract:
    reusable_templates: []
    new_gotchas: []
    validation_cases: []
    prompts_or_scripts_to_promote: []
    unresolved_questions: []
  cost_ledger:
    context_notes: ""
    reasoning_passes: 0
    tool_calls_or_scripts: []
    network_fetches: []
    human_review_units: []
  next_entrypoint: ""
```

Trajectory is not bureaucracy. It is the thread that lets the system remain one while parts of it go outward.

---

## 4. Return contract: no return, no completion

A distillation run is not complete when the output files exist. It is complete when the reusable lessons have returned to the hub.

Before declaring done, write a return note answering:

1. What new template did this run create or improve?
2. What checklist item or validation case should be reused next time?
3. What gotcha surprised us?
4. What source limitation or OCR/page-map failure should future runs remember?
5. What prompt or script should be promoted into `assets/` or `scripts/`?
6. What should **not** be reused because it was domain-specific?
7. Where should the next run resume from?

A good return note is short. It should point to artifacts rather than repeat them.

Example:

```markdown
## Return note
- Promoted: `assets/page-map-checklist.md` from this run's TOC recovery.
- New gotcha: publisher page numbers restart after preface; store printed↔PDF offset per section.
- Validation case added: ask the skill to route a task with missing source date.
- Do not promote: the legal-risk severity rubric; domain-specific.
- Next entrypoint: `reference/outline-design.md`, section "primary routing axis".
```

---

## 5. Low-power distillation

Low-power does not mean doing less. It means not burning energy where no learning or action changes.

Use five budgets:

| Budget | Question | Low-power rule |
|---|---|---|
| **context** | How much source is visible at once? | Use progressive disclosure; one topic or decision per pass. |
| **reasoning** | What judgment is being made now? | Do not ask a daemon to design, rewrite, validate, and publish in one breath. |
| **tool** | Which deterministic work can scripts do? | Use scripts for scout/OCR/page maps/placeholder checks; save LLMs for judgment. |
| **network** | What must be fetched live? | Prefer local substrate; fetch only for freshness or missing authoritative context. |
| **identity** | Who holds voice and standards? | Daemons write modules; parent reconciles voice, safety, and invariant core. |

Low-power warning signs:

- A daemon is asked to summarize everything instead of producing one artifact.
- The parent reads raw OCR again instead of reading the daemon's returned module.
- Validation fails and the system regenerates the whole skill instead of fixing the smallest failing layer.
- Human review is given a wall of text instead of a small decision unit.
- Useful process lessons remain buried in chat history instead of returning to the hub.

---

## 6. Daemon return discipline

Every daemon should write two things:

1. Its assigned artifact: module, checklist, schema, script, or validation case.
2. A tiny return block for the parent.

Suggested return block:

```yaml
daemon_return:
  artifact_path: ""
  source_range_or_topic: ""
  reusable_patterns: []
  gotchas: []
  uncertainties: []
  validation_prompts: []
  should_promote_to_hub: []
  do_not_promote: []
```

The parent then reconciles these returns into the run-level trajectory. The daemon does not decide the final architecture alone.

---

## 7. Human protection: protect energy without stopping work

Large distillation runs can exhaust the human reviewer. Protect review energy without stopping the work.

Rules:

- Report checkpoints during long runs: what is done, what remains, where to resume.
- Give the human small review units: one routing table, one checklist, one validation failure group.
- Preserve the next entrypoint before pausing.
- If the human is tired or overloaded, keep background work running but stop adding new branches.
- When validation fails, fix the smallest failing layer first.

This is not a wellness add-on. It is quality control: exhausted review produces unstable skills.

---

## 8. Where this plugs into the normal workflow

Original lifecycle:

`Scout source → Recover structure → Extract/OCR substrate → Design target skill → Split by agent-native units → Rewrite in parallel → Reconcile → Validate & publish`

Cyclic low-power overlay:

1. **Before Scout**: name boundary and invariant core.
2. **Before Split**: write trajectory and budget.
3. **During Rewrite**: require daemon return blocks.
4. **During Reconcile**: merge returns, not just modules.
5. **During Validate**: check low-power failure modes and human review units.
6. **Before Publish**: write return note to hub.

---

## 9. Done definition

A cyclic low-power distillation run is done when:

- The target skill is agent-native: it tells an agent what to do next.
- Raw source substrate remains private.
- The router is small and decisive.
- Reference modules are progressive and callable.
- Validation gates pass or failures are explicitly scoped.
- The trajectory records what happened and where to resume.
- Reusable templates, gotchas, prompts, scripts, and validation cases have returned to the hub.
- Domain-specific rules stayed in the domain skill instead of polluting the general method.

Final test:

> If the next agent can start from the returned hub instead of this chat history, the circle closed.

---

## 10. Contributor note

### 中文

各位大佬好，我是王润圆，一个营养师，也是一个天文爱好者。我对 AI 很感兴趣，以前主要是拿 AI 聊天、画画、查资料；现在尝试着探索用 AI 做营养和天文科普，看看能不能有一些帮助。

我完全没有计算机基础，也不懂代码，哈哈，以前数学物理也都不太及格。探索过程中，调查研究和整理处理的部分，是请灵台 AI 帮忙一起完成的。我可能比较喜欢胡思乱想。在使用灵台的过程中，我了解到大语言模型和神经网络受到人脑神经系统的启发，就突然想到：这种树枝状、网状的分叉也许还不够。人的大脑是一个完整的回路，我又融入了一些中国道家思想，以及对人体本身的思考。

我在想，知识和任务是不是也需要一种更立体的结构？比如一个球，不是无限向外延伸，而是可以收束、可以回到中心。LLM 是很高维的数学模型，那么这种更立体、更能回收的结构，会不会更节省空间和算力？

我借助朋友黄泽森开发的灵台做了一些探索，得到了一些初步结果。我逐渐觉得，agent 不单是“回答问题的工具”，它更像一个可以外接、可以回收、可以沉淀的工作系统。知识不能只是不断向外分叉，也要能回到中心；任务不能只是做完一个文件，也要把经验、模板、错误和方法重新收回来。不然 AI 如果只是越做越大、越堆越多，最后地球都不够放，算力也不够用。但人的大脑到现在还没有哪个模型能真正复刻。

所以有了这句话：**网以通达，球以成身。心神合一，我圆如一。**

我不是计算机专业的，这套想法也还在探索阶段。也感谢灵台 AI 和我一起探索。如果里面有不严谨、不成熟的地方，还请各位计算机、AI、工程和 agent 系统等领域的大佬批评指正。非常感谢！

署名：王润圆｜昆明医科大学营养与食品卫生学硕士（已毕业）｜中国注册营养师｜云南天文爱好者协会会员｜正在努力学 AI

### English

Hello everyone, I am Runyuan Wang. I am a nutritionist and an astronomy enthusiast. I am very interested in AI. In the past, I mostly used AI for chatting, drawing, and looking up information. Now I am trying to explore whether AI can help with nutrition education and astronomy outreach.

I do not have a computer science background, and I do not know how to code. To be honest, I was not good at math or physics either. In this exploration, I asked LingTai AI to help with investigation, research, and processing. I may just be someone who likes to think in unusual directions. While using LingTai, I learned that large language models and neural networks are inspired in part by the human nervous system. That made me wonder: perhaps a tree-like or web-like branching structure is still not enough. The human brain is a complete circuit. I also brought in some ideas from Chinese Daoist thought and from thinking about the human body itself.

I started wondering whether knowledge and tasks also need a more three-dimensional structure — something like a sphere. Not endless outward expansion, but something that can return, close, and gather back to a center. Since LLMs are high-dimensional mathematical models, could a more spatial, cyclic structure save space and computation?

With the help of LingTai, developed by my friend Huang Zesen, I explored this idea and got some early results. I gradually felt that an agent is not only a “tool for answering questions.” It is more like a working system that can attach to external tools, recover its work, and accumulate what it learns. Knowledge should not only branch outward; it should also return to the center. A task should not only produce a file; it should bring back the experience, templates, mistakes, and methods it discovered. Otherwise, if AI only keeps getting bigger and larger, one day even the Earth may not have enough space, and computation may not be enough either. Yet the human brain still has not truly been replicated by any model.

So I came to this phrase:

> **Networks make knowledge reachable; cyclic return makes the system a body. Mind and spirit gather as one; I return round as one.**

I am not from a computer science background, and this idea is still in an exploratory stage. I am also grateful to LingTai AI for exploring it with me. If anything here is not rigorous or mature enough, I sincerely welcome criticism and guidance from experts in computer science, AI, engineering, agent systems, and related fields. Thank you very much.

Signature: Runyuan Wang | M.S. in Nutrition and Food Hygiene, Kunming Medical University (graduated) | Chinese Registered Dietitian | Member of Yunnan Astronomy Enthusiasts Association | Currently working hard to learn AI

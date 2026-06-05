# 🍬 Glucose Revolution Skill

English version translated from the existing Chinese README.

> Your personal glucose-control buddy, making blood-glucose management easier and more fun.

## Introduction

Hi! I am your **glucose-control assistant** 👋

This skill is designed for common problems such as getting very sleepy after meals, struggling to lose weight despite eating less, recurring skin breakouts, or becoming irritable when hungry. Based on the scientific methods from *Glucose Revolution*, it uses a **relaxed and humorous** conversational style to help with glucose management without starvation or misery.

> 💡 **Core idea**: glucose control is not ascetic practice; it is eating smartly and feeling better.

## Core Features

### Conversational interaction

Talk as if chatting with a friend:

- **Self-assessment** — quick questions to see whether glucose swings may be affecting you.
- **Symptom consultation** — describe a problem and receive analysis plus practical suggestions.
- **Scenario guidance** — meals out, convenience stores, takeout, and other real-life situations.
- **Follow-up feedback** — report what happened after trying a method and adjust together.
- **Long-term tracking** — supports long conversations for habit formation.

### Knowledge depth

- **80 TKPs** — a complete glucose-control teaching knowledge system.
- **Three-level teaching** — beginner, advanced, and expert levels matched to the user.
- **10 practical tricks** — from food order to post-meal movement.
- **Three causal chains** — understand the principles so glucose control is less confusing.

## Quick Start

```bash
# One-click install
curl -fsSL https://raw.githubusercontent.com/yourusername/glucose-revolution-skill/main/quick-install.sh | bash

# Manual copy
cp -r glucose-revolution-skill ~/.workbuddy/skills/custom/  # WorkBuddy
cp -r glucose-revolution-skill ~/.lingtai/custom/          # LingTai TUI
```

After installation, start a conversation directly. More examples are in `EXAMPLES.md`.

## Capability List

### Symptom-to-strategy quick reference

| Concern | Response |
|---------|----------|
| Sleepy right after meals | Food order + vinegar before meals + walking after meals |
| Difficulty losing weight | Insulin mechanism + stable breakfast + stop grazing |
| Skin issues | Reduce sugary drinks + food order + Omega-3 |
| Hangry episodes | Stable breakfast + savory snack alternatives |
| Brain fog | Food order + avoid glucose roller coasters |

### Scenario guidance

- **Social meals** — vegetables first, eat before drinking, choose dry wine.
- **Convenience stores** — tea eggs, vegetable salad, grilled chicken legs, oden.
- **Cravings for sweets** — eat desserts after a meal and buffer with protein first.
- **Breakfast design** — eggs, avocado, and a small amount of whole grain instead of porridge plus buns.

### 10 glucose-control tricks

1. Correct food order: vegetables first, then meat, rice last.
2. Add a green starter before meals.
3. Stop focusing only on calories.
4. Stabilize breakfast with higher protein and fewer refined carbs.
5. Treat all sugars as sugar; do not be fooled by “healthy sugar.”
6. Eat dessert after a meal rather than as a snack.
7. Drink vinegar before meals when appropriate.
8. Move after meals.
9. Choose savory snacks instead of sweet ones.
10. “Dress” carbohydrates with protein.

## File Structure

```text
glucose-revolution-skill/
├── skill.yaml
├── system_prompt.md
├── README.md
├── QUICK_REFERENCE.md
├── CONVERSATION_GUIDE.md
├── EXAMPLES.md
├── METHODOLOGY.md
├── install.sh
└── install.bat
```

## Documentation

| Document | Purpose |
|----------|---------|
| `QUICK_REFERENCE.md` | Five-minute onboarding, daily demo, symptom-strategy quick reference |
| `EXAMPLES.md` | Ten complete conversation examples |
| `CONVERSATION_GUIDE.md` | Conversation-flow design and interaction patterns |
| `METHODOLOGY.md` | TKP-to-Skill conversion methodology |

## Knowledge Source

- **Book**: *Glucose Revolution*
- **Author**: Jessie Inchauspé
- **TKPs**: 80 teaching knowledge points
- **Methodology**: Teaching Meta-Methodology, adapted from `impersonate-meta`

## Tone

Friendly, casual, humorous, and practical rather than lecture-like.

## License

MIT

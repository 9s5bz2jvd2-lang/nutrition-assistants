[中文](README.md)

# Nutrition Assistants

> **An open-source nutrition education and AI-assisted nutrition workflow project maintained by a nutrition professional.**

🌱 I am new to AI and hope to use it to spread nutrition knowledge and help more people. Feedback is welcome.

This is not a generic nutrition repository. It is a complete open-source AI project that brings together **distillation methodology, food-therapy assistant resources, a nutritionist application assistant, public education web projects, and AI-assisted workflows**. The goal is to connect: **evidence sources → skill distillation → AI applications → public-health communication → multi-agent workflow research**.

## Project focus

- **Evidence-informed nutrition education**: structure nutrition knowledge from authoritative food-therapy guides, public-health materials, nutrition history, and professional nutrition frameworks.
- **Public health communication**: translate professional nutrition knowledge into clear, warm, non-alarmist web and education materials for the public.
- **AI-assisted nutrition guidance**: help nutrition professionals organize diet records, identify follow-up questions, draft communication wording, and prepare review material.
- **Future multi-agent nutrition assessment systems**: explore multi-agent workflows for source collection, evidence extraction, nutrition review, writing, media production, and evaluation.
- **Open-source community value**: publish methodology, knowledge structures, skills, workflows, and examples for learning, review, reuse, and responsible improvement.

## Why OpenAI API credits would meaningfully accelerate this project

OpenAI API credits would directly support:

1. **Evidence extraction and cross-checking** from guidelines, papers, textbooks, and public-health materials before review by a nutrition professional.
2. **Iteration of nutrition assistants and workflows**, including food-therapy skills, the nutritionist diet-evaluation assistant, public-education production workflows, and multi-agent collaboration prototypes.
3. **Public-health communication**, including bilingual explainers, FAQs, web copy, poster copy, and education-material drafts.
4. **Safety and boundary evaluation**, checking for fabricated citations, exaggerated claims, medical-scope overreach, and missing referral-to-care warnings.
5. **Open-source documentation**, including bilingual READMEs, examples, evaluation sets, methodology notes, and reusable templates.

In short, credits would accelerate the loop from **evidence base → AI workflow → safety evaluation → public-health communication → future multi-agent nutrition assessment systems**.

## Five project components

```text
nutrition-assistants/
├── Distillation Methodology
├── Food-therapy Assistants
├── Nutritionist Application Skill
├── Public Education Web Projects
└── Workflows & Multi-Agent Research
```

### 1. Distillation Methodology

| Project | Description | Entry |
|---------|-------------|-------|
| Nutrition Skill Methodology | Methodology for distilling nutrition / food-therapy guide materials into reusable AI skills. | [`nutrition-skill-methodology/`](nutrition-skill-methodology/) |
| Book-to-Skill Distillation | General method for turning long books, PDFs, and source packs into agent-native skills. | [`book-to-skill-distillation/`](book-to-skill-distillation/) |

### 2. Food-therapy Assistants

Backbone arrangement:

```text
├── Diabetes Guide
├── CKD Guide
├── Hypertension Guide
├── Nutritionist Assistant Skill
└── Multi-Agent Research (In Progress)
```

| Project | Description | Status | Entry |
|---------|-------------|--------|-------|
| Diabetes Guide | Adult diabetes food-therapy assistant. | ✅ Available | [`diabetes-food-guide-skill/`](diabetes-food-guide-skill/) |
| CKD Guide | Adult chronic kidney disease food-therapy assistant. | ✅ Available | [`ckd-food-guide-skill/`](ckd-food-guide-skill/) |
| Hypertension Guide | Adult hypertension food-therapy assistant. | ✅ Available | [`hypertension-food-guide/`](hypertension-food-guide/) |
| Gout Dietary Guide | Hyperuricemia & gout food-therapy assistant. | ✅ Available | [`gout-dietary-guide/`](gout-dietary-guide/) |
| Hyperlipidemia Food Guide | Hyperlipidemia food-therapy assistant. | ✅ Available | [`hyperlipidemia-food-guide/`](hyperlipidemia-food-guide/) |
| Obesity Food Guide | Adult obesity food-therapy assistant. | ✅ Available | [`obesity-food-guide/`](obesity-food-guide/) |
| Child Obesity Food Guide Skill | Childhood & adolescent obesity food-therapy assistant. | ✅ Available | [`child-obesity-food-guide-skill/`](child-obesity-food-guide-skill/) |
| Childhood Obesity Agent | Complete system-prompt agent for childhood obesity food-therapy education. | ✅ Available | [`childhood-obesity-agent/`](childhood-obesity-agent/) |
| Osteoporosis Food Guide Skill | Osteoporosis food-therapy assistant. | ✅ Available | [`osteoporosis-food-guide-skill/`](osteoporosis-food-guide-skill/) |
| Sarcopenia Food Guide Skill | Sarcopenia food-therapy assistant. | ✅ Available | [`sarcopenia-food-guide-skill/`](sarcopenia-food-guide-skill/) |
| Stroke Food Guide Skill | Stroke food-therapy assistant. | ✅ Available | [`stroke-food-guide-skill/`](stroke-food-guide-skill/) |
| Stunting Dietary Guide | Childhood stunting food-therapy assistant. | ✅ Available | [`stunting-dietary-guide/`](stunting-dietary-guide/) |
| Glucose Revolution Skill | Glucose-management teaching skill. | ✅ Available | [`glucose-revolution-skill/`](glucose-revolution-skill/) |
| Nutrition Taibai Growth | Playful child-growth nutrition education assistant. | ✅ Available | [`nutrition-taibai-growth/`](nutrition-taibai-growth/) |
| Nutrition History Anti-Hallucination | Anti-hallucination workflow for nutrition-history research. | ✅ Available | [`nutrition-history-anti-hallucination-skill/`](nutrition-history-anti-hallucination-skill/) |

### 3. Nutritionist Application Skill

| Project | Description | Entry |
|---------|-------------|-------|
| Nutritionist Assistant Skill | Professional-support workflow for structuring three-day diet records, estimating trends, drafting follow-up questions, preparing internal review material, and generating client-friendly communication wording. | [`yuanjiang-nutritionist-diet-evaluation-assistant-skill/`](yuanjiang-nutritionist-diet-evaluation-assistant-skill/) |

### 4. Public Education Web Projects

| Project | Description | Entry |
|---------|-------------|-------|
| Shiwu Guanxing / 食物观星 | Public communication web project linking nutrition education, lifestyle health, and stargazing. | [`shiwu-guanxing/`](shiwu-guanxing/) |

### 5. Workflows & Multi-Agent Research

| Project | Description | Status | Entry |
|---------|-------------|--------|-------|
| Yuanjiang Nutrition Production Line Skill | Nutrition public-communication workflow: evidence gate, multi-agent collaboration, copy/media production, and review loop. | ✅ Available | [`yuanjiang-nutrition-production-line-skill/`](yuanjiang-nutrition-production-line-skill/) |
| Multi-Agent Research | Research direction for multi-agent nutrition literature, evidence, review, and public-communication workflows. | 🚧 In Progress | [`multi-agent-research/`](multi-agent-research/) |

## Safety & boundaries

- This repository supports **nutrition education, public-health communication, and professional workflow assistance**;
- Medical and nutrition claims should trace back to real guidelines, textbooks, papers, or authoritative public materials;
- It does not fabricate guideline names, papers, years, institutional documents, or pseudo-citations;
- It does **not** replace physicians, registered dietitians/nutritionists, clinical diagnosis, treatment, or individualized medical nutrition therapy;
- For specific disease, medication, pregnancy, child, older-adult, kidney disease, diabetes, or other clinical contexts, users should consult qualified medical professionals or registered nutrition professionals.

---

*Maintainer: Wang Runyuan (9s5bz2jvd2-lang).*  
*This project is open-source and welcomes careful review, educational reuse, and responsible improvement.*

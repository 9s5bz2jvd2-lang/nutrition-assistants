[English](README.en.md)

# Nutrition Assistants｜圆酱营养助手合集

> 🌱 初学 AI，希望用 AI 传播营养学知识，帮助更多的人。如有不足请多多指点。

这是一个**营养知识库 + AI 应用项目**合集（Nutrition knowledge base + AI application projects）。这里既沉淀基于权威指南的营养/食养/膳食评价**知识**，也包含把这些知识做成可用工具的 **AI 应用**——食养科普对话 Skill、营养师工作辅助 Skill，以及在研的多 Agent 研究方向。

## 📂 仓库定位与排列

```
nutrition-assistants/
├── Diabetes Guide                    糖尿病食养助手
├── CKD Guide                         慢性肾脏病食养助手
├── Hypertension Guide                高血压食养助手
├── Nutritionist Assistant Skill      营养师膳食评价助手 Skill
└── Multi-Agent Research (In Progress) 多智能体研究（进行中）
```

上面这条排列是合集的主线：前三项是**知识库型**食养助手（把国家卫健委发布的食养指南蒸馏为结构化知识与科普对话能力），第四项是面向营养师的**专业工作流 Skill**，第五项是仍在探索阶段的**多 Agent 研究**方向。

| 项目 | 说明 | 状态 | 入口 |
|------|------|------|------|
| **Diabetes Guide** | 基于《成人糖尿病食养指南（2023年版）》的 AI 科普对话 Skill，含 KPK 知识点、地区/季节食谱与中医证型指导。 | ✅ 可用 | [`diabetes-food-guide-skill/`](diabetes-food-guide-skill/) |
| **CKD Guide** | 基于《成人慢性肾脏病食养指南（2024年版）》的 AI 科普对话 Skill，含分期饮食指导与中医辨证食养方。 | ✅ 可用 | [`ckd-food-guide-skill/`](ckd-food-guide-skill/) |
| **Hypertension Guide** | 基于《成人高血压食养指南（2023年版）》的 AI 科普对话 Skill。 | ✅ 可用 | [`hypertension-food-guide/`](hypertension-food-guide/) |
| **Nutritionist Assistant Skill** | 营养师膳食评价助手：帮助营养专业人员整理三日膳食记录、估算能量与宏量营养素趋势（带置信标签）、拟定随访问题、准备内部判断材料并生成面向客户的沟通话术。面向专业评估辅助，不替代诊断、临床判断或个体化治疗处方。 | ✅ 可用 | [`yuanjiang-nutritionist-diet-evaluation-assistant-skill/`](yuanjiang-nutritionist-diet-evaluation-assistant-skill/) |
| **Multi-Agent Research** | 在研方向：用多 Agent 协作搭建营养学文献 / 证据 / 科普生产线。目前为占位说明，不预先声称已完成能力。 | 🚧 In Progress | [`multi-agent-research/`](multi-agent-research/) |

## 📚 合集中的其他食养助手

除上述主线外，仓库还收录了一批基于国家卫健委食养指南的 AI 科普对话 Skill，持续完善中：

- [`gout-dietary-guide/`](gout-dietary-guide/) — 高尿酸血症与痛风食养助手
- [`hyperlipidemia-food-guide/`](hyperlipidemia-food-guide/) — 高脂血症食养助手
- [`obesity-food-guide/`](obesity-food-guide/) — 成人肥胖食养助手
- [`child-obesity-food-guide-skill/`](child-obesity-food-guide-skill/) — 儿童青少年肥胖食养助手
- [`osteoporosis-food-guide-skill/`](osteoporosis-food-guide-skill/) — 骨质疏松食养助手
- [`sarcopenia-food-guide-skill/`](sarcopenia-food-guide-skill/) — 肌少症食养助手
- [`stroke-food-guide-skill/`](stroke-food-guide-skill/) — 脑卒中食养助手
- [`stunting-dietary-guide/`](stunting-dietary-guide/) — 生长迟缓食养助手

## 🛡️ 安全与边界

- 本合集内容面向 **教育科普（for education）与专业辅助（professional support）**；
- 以**循证（evidence-based）**、源于权威食养指南为原则；
- **不构成医疗诊断或治疗**（not medical diagnosis），不替代医生或营养师的临床判断与个体化处方；
- 具体健康问题请咨询专业医疗机构或注册营养师。

---

*Maintainer: Wang Runyuan (9s5bz2jvd2-lang).*

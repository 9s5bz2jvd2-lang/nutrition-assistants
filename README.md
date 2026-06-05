[English](README.en.md)

# Nutrition Assistants｜圆酱营养助手合集

> **An open-source nutrition education and AI-assisted nutrition workflow project maintained by a nutrition professional.**  
> **由营养专业人员维护的开源营养教育与 AI 辅助营养工作流项目。**

🌱 初学 AI，希望用 AI 传播营养学知识，帮助更多的人。如有不足请多多指点。

## 维护者 / Nutrition professional maintainer

**王润圆**：昆明医科大学营养与食品卫生学硕士（已毕业），中国注册营养师。项目中使用的作者头像为本人真实头像。

本仓库不是泛泛的“营养资料仓库”。它是一个完整的 AI 开源项目：把**蒸馏方法论、食养助手资料、营养师应用助手、科普网页、工作流**放在同一个开源集合中，形成“证据资料 → Skill 蒸馏 → AI 应用 → 公共健康传播 → 多 Agent 工作流”的闭环。

## 项目定位

- **Evidence-informed nutrition education（基于证据的营养教育）**：把国家卫健委食养指南、营养学资料、历史文献与专业判断框架整理成可复用知识。
- **Public health communication（公共健康传播）**：把专业营养内容转化为普通人能理解、温和、不制造焦虑的科普网页与内容。
- **AI-assisted nutrition guidance（AI 辅助营养指导）**：帮助营养专业人员整理饮食记录、发现追问线索、生成沟通话术与内部判断材料。
- **Future multi-agent nutrition assessment systems（未来多 Agent 营养评估系统）**：探索资料获取、证据提取、营养审稿、文案生成、媒体产出、评测回流等多 Agent 协作。
- **Open-source community value（开源社区价值）**：开放方法论、资料结构、Skill、工作流与示例，方便学习、复核、复用和改进。

## 为什么 OpenAI API credits 能实质性加速本项目

OpenAI API credits 将直接用于：

1. **证据整理与交叉核验**：从指南、论文、教材和公开资料中提取结构化知识，再由营养专业人员复核。
2. **营养助手与工作流迭代**：测试食养助手、营养师膳食评价助手、科普生产线与多 Agent 协作流程。
3. **公共健康传播**：生成中英双语科普、FAQ、网页文案、海报文案和教育材料初稿。
4. **安全与边界评测**：检查伪引用、夸大疗效、越过医疗边界、缺少就医提示等风险。
5. **开源文档维护**：维护 bilingual README、示例、评测集、方法论文档和可复用模板。

这些 credits 不是简单“调用模型”，而是帮助项目更快形成：**证据库 → AI 工作流 → 安全评测 → 公共健康传播 → 多 Agent 营养评估系统**。

## 五个组成部分

```text
nutrition-assistants/
├── Distillation Methodology        蒸馏方法论
├── Food-therapy Assistants         食养助手（资料 / Skills）
├── Nutritionist Application Skill  营养师应用助手
├── Public Education Web Projects   科普网页
└── Workflows & Multi-Agent Research 工作流与多 Agent 研究
```

### 1. Distillation Methodology｜蒸馏方法论

| 项目 | 说明 | 入口 |
|------|------|------|
| Nutrition Skill Methodology | 食养指南蒸馏方法论：把营养/食养指南资料转成可复用 AI Skill。 | [`nutrition-skill-methodology/`](nutrition-skill-methodology/) |
| Book-to-Skill Distillation | 把长书、PDF、资料包蒸馏成 agent-native Skill 的通用方法论。 | [`book-to-skill-distillation/`](book-to-skill-distillation/) |

### 2. Food-therapy Assistants｜食养助手（资料 / Skills）

主线排列：

```text
├── Diabetes Guide
├── CKD Guide
├── Hypertension Guide
├── Nutritionist Assistant Skill
└── Multi-Agent Research (In Progress)
```

| 项目 | 说明 | 状态 | 入口 |
|------|------|------|------|
| Diabetes Guide | 成人糖尿病食养助手。 | ✅ 可用 | [`diabetes-food-guide-skill/`](diabetes-food-guide-skill/) |
| CKD Guide | 成人慢性肾脏病食养助手。 | ✅ 可用 | [`ckd-food-guide-skill/`](ckd-food-guide-skill/) |
| Hypertension Guide | 成人高血压食养助手。 | ✅ 可用 | [`hypertension-food-guide/`](hypertension-food-guide/) |
| Gout Dietary Guide | 高尿酸血症与痛风食养助手。 | ✅ 可用 | [`gout-dietary-guide/`](gout-dietary-guide/) |
| Hyperlipidemia Food Guide | 高脂血症食养助手。 | ✅ 可用 | [`hyperlipidemia-food-guide/`](hyperlipidemia-food-guide/) |
| Obesity Food Guide | 成人肥胖食养助手。 | ✅ 可用 | [`obesity-food-guide/`](obesity-food-guide/) |
| Child Obesity Food Guide Skill | 儿童青少年肥胖食养助手。 | ✅ 可用 | [`child-obesity-food-guide-skill/`](child-obesity-food-guide-skill/) |
| Childhood Obesity Agent | 儿童青少年肥胖食养完整 System Prompt Agent。 | ✅ 可用 | [`childhood-obesity-agent/`](childhood-obesity-agent/) |
| Osteoporosis Food Guide Skill | 骨质疏松症食养助手。 | ✅ 可用 | [`osteoporosis-food-guide-skill/`](osteoporosis-food-guide-skill/) |
| Sarcopenia Food Guide Skill | 肌少症食养助手。 | ✅ 可用 | [`sarcopenia-food-guide-skill/`](sarcopenia-food-guide-skill/) |
| Stroke Food Guide Skill | 脑卒中食养助手。 | ✅ 可用 | [`stroke-food-guide-skill/`](stroke-food-guide-skill/) |
| Stunting Dietary Guide | 儿童青少年生长迟缓食养助手。 | ✅ 可用 | [`stunting-dietary-guide/`](stunting-dietary-guide/) |
| Glucose Revolution Skill | 血糖管理教学 Skill。 | ✅ 可用 | [`glucose-revolution-skill/`](glucose-revolution-skill/) |
| Nutrition Taibai Growth | 趣味儿童长高食养科普助手。 | ✅ 可用 | [`nutrition-taibai-growth/`](nutrition-taibai-growth/) |
| Nutrition History Anti-Hallucination | 营养学历史文献调研防幻觉流程。 | ✅ 可用 | [`nutrition-history-anti-hallucination-skill/`](nutrition-history-anti-hallucination-skill/) |

### 3. Nutritionist Application Skill｜营养师应用助手

| 项目 | 说明 | 入口 |
|------|------|------|
| Nutritionist Assistant Skill | 三日膳食记录整理、能量和宏量营养素趋势粗估、追问清单、内部判断材料与客户沟通话术。 | [`yuanjiang-nutritionist-diet-evaluation-assistant-skill/`](yuanjiang-nutritionist-diet-evaluation-assistant-skill/) |

### 4. Public Education Web Projects｜科普网页

| 项目 | 说明 | 入口 |
|------|------|------|
| 食物观星 / Shiwu Guanxing | 营养科普、生活方式健康与星空探索的公共传播网页项目。 | [`shiwu-guanxing/`](shiwu-guanxing/) |

### 5. Workflows & Multi-Agent Research｜工作流与多 Agent 研究

| 项目 | 说明 | 状态 | 入口 |
|------|------|------|------|
| Yuanjiang Nutrition Production Line Skill | 圆酱营养科普生产线 workflow：证据门、分身协作、文案/媒体产出与审稿回流。 | ✅ 可用 | [`yuanjiang-nutrition-production-line-skill/`](yuanjiang-nutrition-production-line-skill/) |
| Multi-Agent Research | 多 Agent 营养文献、证据、审稿、科普生产线研究方向。 | 🚧 In Progress | [`multi-agent-research/`](multi-agent-research/) |

## 安全与边界

- 本仓库内容面向 **营养教育、公共健康传播与专业工作辅助**；
- 医学/营养建议应尽量回到真实指南、教材、论文或公开权威资料；
- 不编造指南、论文、年份、机构文件或伪引用；
- 不替代医生、注册营养师或其他医疗专业人员的临床诊断、治疗方案或个体化处方；
- 涉及疾病、用药、妊娠、儿童、老年、肾病、糖尿病等具体情况时，应鼓励咨询专业医疗机构或注册营养师。

---

*Maintainer: Wang Runyuan (9s5bz2jvd2-lang).*  
*This project is open-source and welcomes careful review, educational reuse, and responsible improvement.*

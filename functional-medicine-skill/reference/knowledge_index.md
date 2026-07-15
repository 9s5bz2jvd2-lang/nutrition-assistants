# Full Knowledge Index — Functional Medicine Skill (Candidate)

This index maps every topic and layer in the original SKILL.md to the exact
on-demand file path in the candidate package. All content is verbatim from the
source at commit 0733166df8520c4b08a950f8fb18ac44d6c7b754.

## Reference Layers (extracted from authored SKILL.md sections)

| Layer | Content | Path |
|-------|---------|------|
| 1 | Quick Reference (定义/六原则/七大失衡/Go-to-it/干预五层面/核心概念速查) | reference/layer1_quick_reference.md |
| 2 | Seven Imbalances Deep Knowledge (消化/免疫/解毒/激素/氧化/循环/结构) | reference/layer2_imbalances.md |
| 3 | Genomics & Nutrients (SNP/表观遗传/HCY/维生素D/营养素补充剂) | reference/layer3_genomics_nutrients.md |
| 4 | Formula Design (配方设计核心流程/营养素选择/基因多态性调整/协同原则/处方格式模板) | reference/layer4_formula_design.md |
| 5 | Cases Library (10个病例精要/跨病例核心规律/高频营养素TOP10) | reference/layer5_cases.md |
| 6 | Special Populations (儿童4-A病/抗衰老/慢性疲劳综合征/居家解毒方案) | reference/layer6_special_populations.md |
| Safety | Safety Red Lines & Limitations (安全红线/局限性) | reference/safety_red_lines.md |
| 8 | Evidence Query Workflow (循证医学动态查询/配方迭代/各国使用标准) | reference/layer8_evidence_query.md |
| Nav | Tree Navigation & Progressive Disclosure Rules | reference/routing_tree_navigation.md |

## Primary Textbook: 功能医学概论 (曾强, 17 chapters, 514 pages)

| Topic | Chapter | Path |
|-------|---------|------|
| 功能医学概论 | 第一章 | knowledge/ch01_overview.txt |
| 消化吸收与肠道菌群失衡 | 第二章 | knowledge/ch02_digestion.txt |
| 免疫失衡与炎症 | 第三章 | knowledge/ch03_immune.txt |
| 解毒与生物转化失衡 | 第四章 | knowledge/ch04_detox.txt |
| 激素与神经递质失衡 | 第五章 | knowledge/ch05_hormone.txt |
| 氧化还原失衡与线粒体损伤 | 第六章 | knowledge/ch06_oxidative.txt |
| 循环运输失衡 | 第七章 | knowledge/ch07_circulation.txt |
| 结构性失衡 | 第八章 | knowledge/ch08_structural.txt |
| 诊疗路径与稳态 | 第九章 | knowledge/ch09_homeostasis.txt |
| 基因组学与矩阵 | 第十章 | knowledge/ch10_genomics.txt |
| 营养素详解 | 第十一章 | knowledge/ch11_nutrition.txt |
| 抗衰老功能医学 | 第十二章 | knowledge/ch12_antiaging.txt |
| 慢性代谢性疾病 | 第十三章 | knowledge/ch13_metabolic.txt |
| 女性性激素失衡 | 第十四章 | knowledge/ch14_female.txt |
| 儿童4-A病 | 第十五章 | knowledge/ch15_children4A.txt |
| 其他慢性病 | 第十六章 | knowledge/ch16_other.txt |
| 病例分享 | 第十七章 | knowledge/ch17_cases.txt |

## Secondary Textbook: 功能医学【营养达人荟萃版】 (厉昀, 16 chapters, 571 pages)

| Topic | Chapter | Path |
|-------|---------|------|
| 功能医学起源 | 第一章 | knowledge/fm2_ch01_origin.txt |
| 功能医学定义 | 第二章 | knowledge/fm2_ch02_definition.txt |
| 七大失衡 | 第三章 | knowledge/fm2_ch03_imbalance.txt |
| 诊断方法 | 第四章 | knowledge/fm2_ch04_diagnosis.txt |
| 中医结合 | 第五章 | knowledge/fm2_ch05_tcm.txt |
| 食物不耐受 | 第六章 | knowledge/fm2_ch06_food.txt |
| 检测指标 | 第七章 | knowledge/fm2_ch07_indicators.txt |
| 消化系统 | 第八章 | knowledge/fm2_ch08_digestive.txt |
| 胰岛素抵抗 | 第九章 | knowledge/fm2_ch09_insulin.txt |
| 心血管 | 第十章 | knowledge/fm2_ch10_cardiovascular.txt |
| 甲状腺 | 第十一章 | knowledge/fm2_ch11_thyroid.txt |
| 自身免疫 | 第十二章 | knowledge/fm2_ch12_autoimmune.txt |
| 女性健康 | 第十三章 | knowledge/fm2_ch13_female.txt |
| 生活方式 | 第十四章 | knowledge/fm2_ch14_lifestyle.txt |
| 功能医学检测 | 第十五章 | knowledge/fm2_ch15_testing.txt |
| 营养素补充剂 | 第十六章 | knowledge/fm2_ch16_supplements.txt |

## Distilled Knowledge Summaries

| Topic | Path |
|-------|------|
| 基础理论蒸馏 | knowledge/distilled_01_fundamentals.md |
| 消化系统蒸馏 | knowledge/distilled_02_digestive.md |
| 免疫解毒蒸馏 | knowledge/distilled_03_immune_detox.md |
| 激素代谢蒸馏 | knowledge/distilled_04_hormone_metabolic.md |
| 氧化循环蒸馏 | knowledge/distilled_05_oxidative_circulatory.md |
| 基因营养蒸馏 | knowledge/distilled_06_genomics_nutrition.md |
| 病例特殊人群蒸馏 | knowledge/distilled_07_cases_special.md |

## Layer-to-Knowledge Routing

| Layer | When to load | Primary knowledge files |
|-------|-------------|------------------------|
| 1 (Quick Reference) | Always on (compact root covers this) | — |
| 2 (Imbalances) | 深入某个失衡系统 | ch02~ch08, distilled_02~05, fm2_ch03, fm2_ch06~10 |
| 3 (Genomics/Nutrients) | 基因多态性或营养素详解 | ch10, ch11, distilled_06, fm2_ch07, fm2_ch16 |
| 4 (Formula Design) | 设计补剂配方 | ch11, fm2_ch16, distilled_06 |
| 5 (Cases) | 参考病例 | ch17, distilled_07 |
| 6 (Special Populations) | 特殊人群调整 | ch14, ch15, ch12, distilled_07, fm2_ch13 |
| 7 (Full Knowledge) | 需要原文级深度引用 | 按主题定位对应章节 |
| 8 (Evidence Query) | 配方生成后强制执行RCT查询 | — (uses web search) |

## Formula Full-Corpus Traversal Guide

**When mode=formula_design is triggered, ALL files below must be visited. Coverage must reach 100% before formula finalization.**

### Stage 1: Structured Reference Layers (7 files)
| # | File | Extract |
|---|------|---------|
| 1 | reference/layer1_quick_reference.md | Core concepts, 6 principles, 7 imbalances |
| 2 | reference/layer2_imbalances.md | System-specific nutrient recommendations |
| 3 | reference/layer3_genomics_nutrients.md | SNP adjustments, vitamin D, HCY |
| 4 | reference/layer4_formula_design.md | Formula workflow, nutrient selection tables |
| 5 | reference/layer5_cases.md | Cross-case patterns, TOP10 nutrients |
| 6 | reference/layer6_special_populations.md | Pediatric, anti-aging, CFS adjustments |
| 7 | reference/safety_red_lines.md | Non-negotiable safety constraints |

### Stage 2: Primary Textbook (17 chapters)
| # | File | Topic | Key formula extract |
|---|------|-------|---------------------|
| 1 | knowledge/ch01_overview.txt | 概论 | Theory framework |
| 2 | knowledge/ch02_digestion.txt | 消化 | 5R protocol nutrients |
| 3 | knowledge/ch03_immune.txt | 免疫 | Anti-inflammatory nutrients |
| 4 | knowledge/ch04_detox.txt | 解毒 | Phase I/II support |
| 5 | knowledge/ch05_hormone.txt | 激素 | HPA/thyroid/sex hormone support |
| 6 | knowledge/ch06_oxidative.txt | 氧化还原 | Mitochondrial nutrients |
| 7 | knowledge/ch07_circulation.txt | 循环 | Cardiovascular support |
| 8 | knowledge/ch08_structural.txt | 结构 | Musculoskeletal support |
| 9 | knowledge/ch09_homeostasis.txt | 稳态 | Clinical tools, matrix |
| 10 | knowledge/ch10_genomics.txt | 基因组 | SNP-specific adjustments |
| 11 | knowledge/ch11_nutrition.txt | 营养素 | Complete nutrient reference |
| 12 | knowledge/ch12_antiaging.txt | 抗衰老 | Longevity nutrients |
| 13 | knowledge/ch13_metabolic.txt | 代谢 | Metabolic syndrome support |
| 14 | knowledge/ch14_female.txt | 女性 | Female hormone balancing |
| 15 | knowledge/ch15_children4A.txt | 儿童 | 4-A pediatric protocols |
| 16 | knowledge/ch16_other.txt | 其他 | Other chronic diseases |
| 17 | knowledge/ch17_cases.txt | 病例 | 10 complete case formulas |

### Stage 3: Secondary Textbook (16 chapters)
| # | File | Topic |
|---|------|-------|
| 1 | knowledge/fm2_ch01_origin.txt | 起源 |
| 2 | knowledge/fm2_ch02_definition.txt | 定义 |
| 3 | knowledge/fm2_ch03_imbalance.txt | 失衡 |
| 4 | knowledge/fm2_ch04_diagnosis.txt | 诊断 |
| 5 | knowledge/fm2_ch05_tcm.txt | 中医 |
| 6 | knowledge/fm2_ch06_food.txt | 食物 |
| 7 | knowledge/fm2_ch07_indicators.txt | 指标 |
| 8 | knowledge/fm2_ch08_digestive.txt | 消化 |
| 9 | knowledge/fm2_ch09_insulin.txt | 胰岛素 |
| 10 | knowledge/fm2_ch10_cardiovascular.txt | 心血管 |
| 11 | knowledge/fm2_ch11_thyroid.txt | 甲状腺 |
| 12 | knowledge/fm2_ch12_autoimmune.txt | 自身免疫 |
| 13 | knowledge/fm2_ch13_female.txt | 女性 |
| 14 | knowledge/fm2_ch14_lifestyle.txt | 生活方式 |
| 15 | knowledge/fm2_ch15_testing.txt | 检测 |
| 16 | knowledge/fm2_ch16_supplements.txt | 补充剂（1.17 MB，最大文件） |

### Stage 4: Distilled Summaries (7 files)
| # | File | Topic |
|---|------|-------|
| 1 | knowledge/distilled_01_fundamentals.md | 基础理论 |
| 2 | knowledge/distilled_02_digestive.md | 消化 |
| 3 | knowledge/distilled_03_immune_detox.md | 免疫解毒 |
| 4 | knowledge/distilled_04_hormone_metabolic.md | 激素代谢 |
| 5 | knowledge/distilled_05_oxidative_circulatory.md | 氧化循环 |
| 6 | knowledge/distilled_06_genomics_nutrition.md | 基因营养 |
| 7 | knowledge/distilled_07_cases_special.md | 病例特殊人群 |

### Stage 5: Evidence & Assets (2 files)
| # | File | Purpose |
|---|------|---------|
| 1 | reference/layer8_evidence_query.md | RCT query workflow |
| 2 | assets/eval-cases.md | Validation test cases |

**This is a human-authored routing inventory, not formula-mode coverage proof. Formula coverage cardinality must be generated from the completed v2 registry; schema: `reference/formula_coverage_ledger_template.json`.**

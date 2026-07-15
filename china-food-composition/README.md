# 中国食物成分参考 Skill / China Food Composition Reference Skill

## 中文

### 用途

本目录是一个面向代理和人的中文食物成分参考 Skill，基于《中国食物成分表（标准版）》第 6 版的 OCR 文本蒸馏而成。它用于查询和解释食物分类、食物编码、GI、营养素定义、单位、分析方法及相关特别成分的参考信息，支持营养资料整理、教育内容制作和专业复核辅助。

它不是完整的食物成分数据库：一般营养成分、氨基酸、脂肪酸、碘、嘌呤/DHA/EPA 及植物化学物的主体数值表在当前仓库中因 OCR 质量问题标为待补充。

### 适用对象与使用方式

适用于营养师、研究/内容团队、需要可追溯参考的代理，以及希望查阅编码或术语的人。代理或人工应先按问题定位文件，再核对原文上下文、单位、可食部（EP）、代表值和特殊符号；需要实际数值时，只使用仓库中明确存在且可读的条目，并注明这是参考数据。查询食物营养成分、GI、食物编码或营养素定义时，可将本目录作为 `china-food-composition` Skill 的本地知识源调用。

### 文件导航

| 文件 | 内容 |
|---|---|
| [`SKILL.md`](SKILL.md) | Skill 元数据、适用查询、渐进式披露、当前限制与免责声明 |
| [`cheatsheet.md`](cheatsheet.md) | GI 分类、单位、编码和换算的快速参考 |
| [`methodology.md`](methodology.md) | 数据来源、表达规范、EP、代表值、编码规则和出版简史 |
| [`glossary.md`](glossary.md) | 食物成分、营养素、INFOODS Tagname 等术语 |
| [`data/food-classification.md`](data/food-classification.md) | 食物分类、亚类与 6 位编码体系 |
| [`data/gi-table.md`](data/gi-table.md) | 259 个食物的 GI 参考表 |
| [`data/nutrient-definitions.md`](data/nutrient-definitions.md) | 营养素定义、单位、Tagname、分析/计算方法和精确度字段 |
| [`data/special-tables.md`](data/special-tables.md) | 碘、维生素、植物化学物、GI、嘌呤及 DHA/EPA 特别表的元数据与方法说明 |
| [`../README.md`](../README.md) | 仓库中文入口 |
| [`../README.en.md`](../README.en.md) | 仓库英文入口 |

### 证据、准确性与边界

- 内容来源和版本信息以 [`SKILL.md`](SKILL.md) 及 [`methodology.md`](methodology.md) 的现有说明为准；其中包含对《中国食物成分表（标准版）》第 6 版（2018）的引用信息。
- OCR 蒸馏可能引入识别错误；食物品种、产地、季节、加工方式和可食部会造成实际差异。仓库内容不能替代原始出版物、实验室测定或专业复核。
- 本目录是参考资料和导航，不诊断疾病、不处方、不提供个体化治疗方案。糖尿病、肾病、痛风等合并基础疾病的营养方案须由医生或注册营养师指导。
- 相关出版物由其原出版者和权利人负责。本仓库只提供有限的结构化摘录、方法说明和参考索引；不暗示替代权威出版表，也不主张重新发布完整的受版权保护表格。需要权威数值时请查阅合法获得的原始出版物。

### 创建者

仓库现有 `SKILL.md` 将创建者列为王润圆（中国注册营养师，昆明医科大学营养与食品卫生学硕士）；本 README 仅据此作出该信用说明。

## English

### Purpose

This directory is a Chinese food-composition reference Skill for agents and people. It is distilled from OCR text of the *China Food Composition Tables (Standard Edition), 6th edition*. It supports lookups and explanations of food classification, food codes, GI, nutrient definitions, units, analytical methods, and metadata for selected special-composition tables, for nutrition-reference organization, educational content, and professional review support.

It is not a complete food-composition database. The repository explicitly marks the main tables for general nutrients, amino acids, fatty acids, iodine, purines/DHA/EPA, and phytochemicals as incomplete because of OCR quality.

### Intended users and use

The intended users are nutrition professionals, research/content teams, agents needing reviewable references, and people looking up codes or terminology. First locate the relevant file, then verify context, units, edible portion (EP), representative-value rules, and symbols. Use only readable entries actually present in the repository when quoting values, and label them as reference data. For questions about food composition, GI, food codes, or nutrient definitions, use this directory as the local `china-food-composition` Skill source.

### File navigation

| File | Contents |
|---|---|
| [`SKILL.md`](SKILL.md) | Skill metadata, intended queries, progressive disclosure, limitations, and disclaimer |
| [`cheatsheet.md`](cheatsheet.md) | Quick reference for GI categories, units, codes, and conversions |
| [`methodology.md`](methodology.md) | Data sources, expression rules, EP, representative values, codes, and publication history |
| [`glossary.md`](glossary.md) | Terms for food composition, nutrients, and INFOODS Tagnames |
| [`data/food-classification.md`](data/food-classification.md) | Food classes, subclasses, and six-digit coding system |
| [`data/gi-table.md`](data/gi-table.md) | GI reference table for 259 foods |
| [`data/nutrient-definitions.md`](data/nutrient-definitions.md) | Nutrient definitions, units, Tagnames, analytical/calculation methods, and precision fields |
| [`data/special-tables.md`](data/special-tables.md) | Metadata and method notes for iodine, vitamins, phytochemicals, GI, purines, and DHA/EPA tables |
| [`../README.md`](../README.md) | Repository Chinese entry point |
| [`../README.en.md`](../README.en.md) | Repository English entry point |

### Evidence, accuracy, and boundaries

- Source and edition claims are limited to the existing statements in [`SKILL.md`](SKILL.md) and [`methodology.md`](methodology.md), including their cited 2018 6th-edition publication information.
- OCR distillation can introduce recognition errors. Real composition varies with food variety, origin, season, processing, and edible portion. Repository notes do not replace the published source, laboratory measurement, or professional review.
- This is reference material and navigation, not diagnosis, prescribing, or individualized treatment. Nutrition plans for people with diabetes, kidney disease, gout, or other conditions require a physician or registered dietitian.
- The cited publication remains subject to its publisher’s and rights holders’ terms. This repository provides limited structured excerpts, methodological notes, and reference indexing; it does not replace the authoritative published tables or claim to republish complete copyrighted tables. Consult a lawfully obtained original publication for authoritative values.

### Creator credit

The existing `SKILL.md` identifies Wang Runyuan (registered dietitian; M.S. in Nutrition and Food Hygiene, Kunming Medical University) as the creator. This credit is stated here only on that repository-supported basis.

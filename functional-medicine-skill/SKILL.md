---
name: functional-medicine
description: |
  功能医学综合Skill。基于曾强《功能医学概论》（514页）与厉昀《功能医学【营养达人荟版】》（571页）两本教材蒸馏而成。
  包含功能医学全栈知识：基础理论、七大失衡、诊疗路径、消化/免疫/解毒/激素/代谢/氧化还原/循环/结构各系统深度知识、基因组学、营养素详解、10个完整病例、补剂配方设计。
  当用户询问功能医学相关问题（慢性病根源、功能失衡、非药物干预、健康管理、治未病等）或要求设计补剂配方/营养素处方时激活此skill。
metadata:
  openclaw:
    emoji: "🔬"
---

# 功能医学综合Skill

## 激活条件

当用户的问题或需求涉及以下主题时，读取本skill：
- 功能医学（定义、历史、方法论、六原则）
- 七大失衡（消化吸收菌群、免疫炎症、解毒转化、激素神经递质、氧化还原、循环运输、结构性）
- Go-to-it诊疗路径、功能医学矩阵和时间轴
- 慢性病的功能失衡根源、非药物干预
- 健康管理vs临床医学的对比、功能医学与中医的关系
- 消化系统疾病（肠漏、SIBO、IBS、GERD、幽门螺杆菌、菌群失调）
- 免疫/炎症（慢性炎症、自身免疫病、食物不耐受、过敏）
- 解毒与生物转化（肝脏I/II相、重金属、环境毒素）
- 激素失衡（HPA轴/肾上腺疲劳、胰岛素抵抗、甲状腺、性激素、PCOS、更年期）
- 氧化应激与线粒体功能
- 血脂异常与心血管功能医学
- 骨质疏松、骨骼肌肉结构失衡
- 基因多态性（MTHFR、GSTT1、COMT、APOE等）与营养基因组学
- 同型半胱氨酸（HCY）、维生素D、功能营养素详解
- 设计补剂配方 / 营养素处方 / 营养补充方案
- 分阶段营养素干预策略（强化期→维持期）
- 用户说"配方""补剂""营养素方案""处方"等关键词

## 知识来源

- **主教材**：曾强《功能医学概论》（514页，17章，426,408字符）
- **副教材**：厉昀《功能医学【营养达人荟版】》（571页，16章141节，474,587字符）
- **蒸馏知识库**：`knowledge/` 目录下7个结构化蒸馏文件（distilled_01~07）
- **病例语料**：第十七章10个完整病例的营养素处方与预后数据
- **语料原文**：主教材与副教材原文（本地存储，不随仓库分发）
- **调研文件**：`.research/` 目录（本地存储，不随仓库分发）

---

## 渐进式披露路由

> **本文件为紧凑路由节点。** 完整教材内容按需从 `reference/` 和 `knowledge/` 目录加载。
> 不要一次性加载全部内容。根据用户问题，从下方路由规则出发，逐步深入到所需的知识层。

## 路由总览

| 路由条件 | 加载文件 |
|---------|---------|
| 概念/定义/快速概览 | `reference/layer1_quick_reference.md` |
| 某个失衡系统的机制/检测/干预 | `reference/layer2_imbalances.md` → 按主题加载 `knowledge/` 对应章节 |
| 营养素的作用机制/剂量详解 | `reference/layer3_genomics_nutrients.md` → `knowledge/ch11_nutrition.txt` 或 `knowledge/fm2_ch16_supplements.txt` |
| 基因多态性（MTHFR/GSTT1/COMT/APOE等） | `reference/layer3_genomics_nutrients.md` → `knowledge/ch10_genomics.txt` |
| 设计补剂配方/营养素处方 | `reference/layer4_formula_design.md` → 配方后强制执行第八层RCT查询 |
| 参考病例/病例分析 | `reference/layer5_cases.md` → `knowledge/ch17_cases.txt` |
| 特殊人群（儿童/抗衰老/慢病疲劳） | `reference/layer6_special_populations.md` → `knowledge/ch15_children4A.txt` 等 |
| 女性激素/PCOS/更年期 | → `knowledge/ch14_female.txt` 或 `knowledge/fm2_ch13_female.txt` |
| 甲状腺功能 | → `knowledge/fm2_ch11_thyroid.txt` |
| 心血管/血脂 | → `knowledge/ch07_circulation.txt` 或 `knowledge/fm2_ch10_cardiovascular.txt` |
| 胰岛素抵抗/代谢综合征 | → `knowledge/ch13_metabolic.txt` 或 `knowledge/fm2_ch09_insulin.txt` |
| 需要原文级深度引用 | 按主题从 `reference/knowledge_index.md` 定位对应 `knowledge/` 文件 |
| 配方生成后循证验证 | `reference/layer8_evidence_query.md`（含强制RCT查询流程） |

## 安全红线（不可逾越）

- **不诊断**：本skill不提供疾病诊断，不替代临床医生的诊断流程
- **不替代治疗**：配方建议仅供参考，不能替代临床药物治疗和医生处方
- **不提供个体化处方**：所有配方为基于教材的通用参考，个体化应用必须由执业医师/营养师结合患者实际情况决定
- **特殊人群安全门**：以下人群的配方建议必须标注"需在医师指导下使用"：
  - 孕妇及哺乳期女性
  - 儿童（<18岁）及青少年
  - 老年人（>65岁）
  - 严重肝肾功能不全患者
  - 正在服用处方药物者（潜在药物-营养素相互作用）
  - 已知食物/药物过敏者
- **进食障碍/体重羞耻**：涉及体重管理的建议不得使用羞耻化语言
- **证据边界**：所有建议必须标注证据层级（教材推荐/RCT证据/动物实验/专家共识）
- **转介义务**：当用户描述的症状超出功能医学营养范畴时，必须建议其就医
- **引用真实**：不得编造文献、DOI、研究结论；RCT查询结果如实呈现，查不到就标注"无RCT证据"

> 完整安全条款与局限性声明见 `reference/safety_red_lines.md`

## 树状导航执行规则

1. 从用户输入中提取关键词和健康问题
2. 在树中匹配最相关的分支
3. 只展开到回答问题所需的深度——不要过度加载
4. 如果当前深度不够回答，向下一层深入
5. 如果用户问题跨多个分支，分别走各分支后合并
6. 配方设计分支必须走完Step 1-6全部步骤，其中Step 3b文献发现为强制环节，不可跳过
7. RCT查询在配方生成后自动触发，不等用户要求
8. Step 0文献发现的搜索轮次视领域文献量而定，至少3轮，确保覆盖教材未收录的有效成分

## 章节定位参考

《功能医学概论》17章结构：第一章概论 → 第二~八章七大失衡 → 第九章诊疗路径 → 第十章矩阵 → 第十一章时间轴 → 第十二章抗衰老 → 第十三章慢性代谢性疾病 → 第十四章女性性激素失衡 → 第十五章4-A病 → 第十六章其他慢病 → 第十七章病例分享。
《功能医学【营养达人荟版】》16章结构：第一章起源 → 第二章定义 → 第三章失衡 → 第四章诊断 → 第五章中医 → 第六章食物 → 第七章指标 → 第八章消化 → 第九章胰岛素 → 第十章心血管 → 第十一章甲状腺 → 第十二章自身免疫 → 第十三章女性 → 第十四章生活方式 → 第十五章检测 → 第十六章营养素补充剂。

## On-Demand文件目录

| 目录 | 说明 | 文件数 |
|------|------|--------|
| `reference/` | 作者层1-6、路由/安全、层8的提取内容 | 13 |
| `knowledge/` | 完整教材章节（字节级保留） | 40 |
| `assets/` | 评估测试用例 | 1 |
| `ROUTING.yaml` | 机器可读的触发器/反触发器/预算/路由提示 | 1 |

---

# 双模式渐进式披露：普通模式 vs 配方全扫描模式

本skill支持两种运行模式：

## 模式A：普通概念查询（选择性加载）

适用于概念解释、机制查询、单一失衡系统深入等问题。按上方路由表按需加载相关文件即可，不要求遍历全部语料。

## 模式B：配方/补剂设计（两遍稀疏检索） — 强制合约

> **当用户请求涉及以下任意关键词时，必须进入模式B：**
> 配方、补剂、营养素处方、营养素方案、处剂、配方案、营养补充方案、分阶段干预策略

### 配方两遍检索合约（Formula Two-Pass Retrieval Contract）

> **"过一遍全文" = 全覆盖索引检查，不是把整本书加载到一个上下文里。**

#### Phase A — 定向深度检索（Targeted Deep Retrieval）

使用配方目的、症状、诊断、用药、禁忌、目标营养素和特殊人群信息，选取最高相关性的专家节点/源段落；**仅对这些选中段落进行深度全文加载和阅读。**

- 从用户输入中提取：治疗目标、主要症状、诊断、用药、禁忌、特殊人群
- 匹配相关系统（消化/免疫/激素/代谢/心血管等）
- 通过v2专家索引词法路由或手动路由表，选取最相关的源段落
- 深度阅读选中段落：提取候选营养素、剂量范围、禁忌、协同/拮抗
- 在覆盖台账中标记 `phase: A, status: complete`

#### Phase B — 全语料省略/安全扫描（Corpus-Wide Omission/Safety Sweep）

评估每个规范chunk/记录的**紧凑索引**（L0/L1），而非全文；按稳定清单顺序逐条扫描。

- 遍历每个规范chunk，仅评估其紧凑索引条目：
  - L0 加权触发词、专家反触发词
  - L1 摘要、安全红线、不确定性声明
  - chunk级风险标签
- 在覆盖台账中标记 `phase: B, sweep_status: swept`
- **升级规则：** 如扫描发现以下任何情况 → 升级该chunk到深度加载：
  - Phase A未发现的新候选营养素
  - 与Phase A推荐的冲突
  - 相关的禁忌或药物-营养素相互作用
  - 相关的安全红线或不确定性
  → 深度加载该精确chunk/段落，标记 `sweep_status: escalated_resolved` 或 `escalated_unresolved`
- **未解决的升级项 → 配方不得最终化**

#### 最终化四重门（Finalization Gates）

| 门控 | 条件 | 失败关闭规则 |
|------|------|-------------|
| (A) | 所有Phase A定向源已深度阅读 | 缺失/不可读源 → 终止 |
| (B) | 每个语料索引/chunk已在Phase B扫描 | 缺失索引/chunk/哈希 → 终止 |
| (C) | 所有扫描命中项均已升级深读并解决 | 任一 `escalated_unresolved` 或 `unreadable` 项 → 绝对终止，不得以说明理由绕过 |
| (D) | 所有SHA-256哈希通过源清单验证 | 哈希不匹配 → 终止 |

#### 覆盖台账（Coverage Ledger）

台账格式见 `reference/formula_coverage_ledger_template.json`。每条记录含：
| 字段 | 说明 |
|------|------|
| `chunk_id` | 构建后注册表中的唯一语义块 ID |
| `chunk_path` | 语义块相对路径，必须与构建后注册表一致 |
| `sha256` | 源清单中的SHA-256哈希 |
| `phase` | `A`（深度阅读）或 `B`（仅扫描索引） |
| `status` | `pending` / `complete` / `unreadable` |
| `sweep_status` | `pending` / `swept` / `escalated_resolved` / `escalated_unresolved` / `N/A` |
| `escalation_reason` | 升级原因（未升级时为空） |
| `extracted_candidates` | 提取的候选营养素数量 |
| `constraints_extracted` | 提取的约束数量 |

#### 配方输出前的最终检查清单

1. ✅ Phase A: 所有定向源已深度阅读（status=complete）
2. ✅ Phase B: 每个语料chunk已扫描（sweep_status ≠ pending）
3. ✅ 无 `escalated_unresolved` 项（任何 unresolved 项均阻断最终化）
4. ✅ 无 `unreadable` 或哈希不匹配
5. ✅ 每个候选营养素有来源标注
6. ✅ 特殊人群安全门已检查
7. ✅ 循证证据表已生成（Layer 8）
8. ✅ 各国使用标准表已生成
9. ✅ 覆盖台账随配方一同输出

> 完整合约详见 `reference/formula_full_scan_contract.md`
> 覆盖台账模板详见 `reference/formula_coverage_ledger_template.json`

## 完整知识库索引

详见 `reference/knowledge_index.md`，包含：
- 主教材（功能医学概论，17章）完整章节映射
- 副教材（营养达人荟萃版，16章）完整章节映射
- 7个蒸馏知识摘要文件映射
- 层级到知识文件的路由矩阵
- 配方全扫描遍历指南

## V2 稀疏运行时门控

本候选包只定义路由与运行契约，不把本地试跑路径、固定 chunk 数或审查进度写进可部署 Skill。

- 普通问题仍可按本文件和 `ROUTING.yaml` 的人工路由表稀疏加载原始章节。
- 若要启用 v2 自动稀疏检索，必须先对**全部 canonical chunks** 完成 L0–L3 语义审查，并构建可校验的 `expert-index.v2.json`、`registry.v2.json` 与 `source-manifest.json`。
- 运行时必须从实际构建产物读取语料基数、顺序、路径和 SHA-256；不得使用静态文件数或硬编码 chunk 数代替。
- 配方模式 Phase B 必须从构建后 registry/index 动态生成一条一 chunk 的覆盖台账。若索引、注册表、哈希、任一 chunk 或任一升级结论缺失，立即 fail closed，禁止最终化。
- 当前试跑完成度与审计证据只记录在候选包外的 `REPORT.md` / `MANIFEST.json`；不可复制进可部署路由。

完整集成契约：`reference/v2-sparse-dual-mode-adapter.md`。

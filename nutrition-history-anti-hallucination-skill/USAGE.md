# 使用说明

## 1. 安装到 custom skill 目录

将本仓库中的 `SKILL.md` 复制到代理环境的 custom skill 目录：

```bash
mkdir -p .library/custom/nutrition-history-anti-hallucination
cp SKILL.md .library/custom/nutrition-history-anti-hallucination/SKILL.md
```

如果你的系统以仓库形式加载 skill，也可以直接引用本仓库内容。

## 2. 何时触发

当用户要求进行以下任务时，应优先使用本流程：

- 营养学史、食疗史、饮食医学史调研；
- 古籍作者、年代、版本、校注、辑佚、OCR 差异核验；
- “完整爬取原文”“逐字蒸馏”“历史文献学对比”“避免幻觉”；
- 东西方营养史、dietetics/regimen 与现代 nutrition science 的比较；
- 生成营养学史报告、文献矩阵、时间线、阶段报告。

## 3. 推荐提示词

```text
请使用 nutrition-history-anti-hallucination 流程处理本次营养学历史文献调研：
1. 先为每个来源建立 source record；
2. 标注 full_text_status 和 source_level；
3. 搜索片段只进入线索表，不进入结论；
4. 对取得的完整原文进行逐字/逐段蒸馏；
5. 用历史文献学方法检查题名、作者、年代、版本与证据边界；
6. 最终报告中区分古代食疗经验与现代营养学证据。
```

## 4. Source record 模板

```yaml
source_id:
title:
author_or_attribution:
period:
source_type:
full_text_status: full_text_obtained | partial_text | metadata_only | search_snippet_only | blocked
source_level: A | B | C | D
path_or_url:
version_or_edition:
page_or_volume_refs:
structure_recovered: yes | partial | no
can_enter_argument: yes | limited | no
notes:
```

## 5. 证据状态判定

- `full_text_obtained`：可进入逐字/逐段蒸馏，但仍需标注版本来源。
- `partial_text`：只能分析已取得部分，不得外推整书。
- `metadata_only`：只用于目录、版本线索、待核问题。
- `search_snippet_only`：只进入线索表，不进入正文结论。
- `blocked`：记录阻碍，不凭印象补写。

## 6. 逐字蒸馏模板

```markdown
### [source_id] [卷/章/条目]

- 原文位置：卷/章/页/段/URL anchors
- 原文摘录：尽量短引，必要时保留完整段落路径
- 白话释义：只解释原文说了什么
- 术语表：关键字、异体字、可能误读
- 食物—身体模型：性味/脏腑/体液/能量/营养素/代谢/群体风险等
- 学科关系：医学/本草/药学/养生/食品卫生/化学/生理/公共卫生/政策
- Supports：此段能支持什么
- Does not support：此段不能支持什么
- Evidence boundary：证据等级、版本问题、待核项
- Return-to-hub：它如何回答“营养学与其他学科的区别”
```

## 7. 写作边界

禁止写法：

- “古代已经有现代营养学。”
- “某古方有效。”（除非另有现代临床证据并经核验）
- “搜索结果显示，所以事实是……”
- “某书是第一部……”但没有原页和学术史来源。
- 把传统食治、本草、调摄直接等同于现代 nutrition science。

推荐写法：

- “该材料说明饮食很早进入医学/养生/本草知识体系。”
- “这属于传统食治/本草/调摄体系，不等同于现代营养学。”
- “目前仅为搜索片段线索，待原页核验。”
- “此处可支持历史思想史判断，不能支持现代疗效判断。”

## 8. 建议产出文件

```text
exports/营养学调研/营养学调研_sources_catalog_batchX_主题_日期.md
exports/营养学调研/营养学调研_distillation_notes_batchX_主题_日期.md
exports/营养学调研/营养学调研_timeline_update_batchX_主题_日期.md
exports/营养学调研/营养学调研_open_questions_batchX_主题_日期.md
exports/营养学调研/营养学调研_阶段报告_vN_日期.md
```

## 9. 免责声明

本流程服务于历史文献与学术写作防幻觉，不是医学建议。不要把古代食疗条文当作现代疗效证据；涉及疾病、治疗和个体健康决策时，应依据现代医学与营养学证据，并咨询合格专业人员。
# 营养学历史文献调研防幻觉 Skill

[English version](README.en.md)

这是一个面向 **营养学史、食疗史、饮食医学史与东西方营养史大工程** 的防幻觉工作流 skill。它的核心目标不是节省 token，而是把“搜索片段、模型常识、百科概括、古籍经验、现代营养证据”严格分层，避免在历史文献调研中把线索误写成结论。

本仓库由本地 custom skill `.library/custom/nutrition-history-anti-hallucination/` 整理而来，可作为独立小仓库公开发布和复用。

## 适用场景

当任务涉及以下内容时，建议启用本 skill：

- 梳理营养学史、食疗史、东西方饮食医学史；
- 查证古籍作者、年代、版本、辑佚、异名与 OCR 问题；
- 对比《食疗本草》《千金方》《饮膳正要》《本草纲目》《黄帝内经》等传统文献；
- 对比西方 dietetics、regimen、vitamins、RDA/DRI、公共卫生营养等历史线索；
- 做完整原文爬取、逐字/逐段蒸馏、历史文献学对比；
- 构建“历史时间 × 东西方”的文献矩阵、时间线、阶段报告。

## 核心原则

1. **原文状态先行**  
   每个来源必须先建立 source record，并标注 `full_text_status`。没有完整原文或权威原页时，只能进入线索表，不能进入强结论。

2. **搜索片段不能当证据**  
   `search_snippet_only` 只能作为待核线索。不能用搜索结果摘要、模型印象或二手转述直接写结论。

3. **逐字蒸馏而非摘几句**  
   对取得的完整原文，应按卷、章、页、段或 URL anchor 回到原文位置，记录原文摘录、白话释义、术语表、可支持/不可支持的判断与证据边界。

4. **历史文献学检查**  
   对古籍和旧文献必须检查题名、作者归属、成书/刊刻/整理年代、版本来源、异体字/OCR 风险、“第一/最早”等范围限定。

5. **古代食疗不是现代疗效证据**  
   古代食疗、本草、养生、调摄材料只能作为历史思想、经验体系或知识制度的证据。除非另有现代临床与营养证据核验，不能把古代条文当作现代疗效证明。

6. **东西方比较不可强行合并**  
   dietetics、regimen、食治、本草、现代 nutrition science 属于不同历史语境和知识系统。比较时应说明差异，而不是直接等同。

## 不是医学建议

本 skill 仅用于历史文献调研、证据分层与写作防幻觉流程，不提供医学建议、诊断、治疗方案或个体化营养处方。任何涉及疾病、治疗、补充剂、药食同源或临床效果的表述，都必须另行依据现代医学与营养学证据核验。

## 仓库文件

- `SKILL.md`：原始 skill 定义与完整流程。
- `USAGE.md`：安装、触发、产出格式与使用示例。
- `CONTRIBUTOR_NOTE.md`：公开维护与贡献注意事项。
- `README.md`：项目说明。

## 快速使用

将 `SKILL.md` 放入支持 custom skill 的代理环境中，例如：

```text
.library/custom/nutrition-history-anti-hallucination/SKILL.md
```

然后在营养学史或食疗史调研任务中明确要求使用该 skill，例如：

```text
请使用 nutrition-history-anti-hallucination 流程，先建立 source record，区分 full_text_obtained / partial_text / search_snippet_only，再进行逐字蒸馏和历史文献学对比。
```

## 典型产出

建议每批至少产出：

- sources catalog：来源目录与 full_text_status；
- distillation notes：逐字/逐段蒸馏记录；
- timeline update：历史时间线更新；
- open questions：待核问题与证据缺口；
- stage report：阶段报告。

## 许可

当前整理未附加专门许可证。公开发布前如需明确开源许可证，建议仓库所有者补充 `LICENSE` 文件。

<!-- Maintainer update: Runyuan Wang (9s5bz2jvd2-lang). -->

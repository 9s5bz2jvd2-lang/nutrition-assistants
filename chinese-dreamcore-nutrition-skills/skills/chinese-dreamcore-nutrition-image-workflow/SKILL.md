---
name: chinese-dreamcore-nutrition-image-workflow
description: |
  把“中式梦核 + 营养科普 + 可爱温柔”风格沉淀为可调用的图片生产 skill：用户给主题后，必须产出图片文件，或明确写出缺失的真实出图后端。
  触发时机：用户说“调用这个 skill 生成图/产图/做一张中式梦核营养图片”，或想生成一张中式梦核风、可爱优先、无字底图 + 后期中文排版的营养科普图片；已持有或愿意先写主题证据卡；只做静态图，不做视频。
  不要触发：用户没证据卡也不愿建、要实拍/二次元/营销海报/医学处方图、要视频、要模型直接生成中文正文、要新增/核验营养事实。
version: 1.0.0
tags: [image-generation, workflow, chinese-dreamcore, nutrition, cute, poster]
last_changed_at: 2026-07-09T08:00:00Z
---

# 中式梦核营养图片生成工作流

## 0. 可调用生产契约（调用本 skill 必须先看）

本 skill 不是只写方案。用户说“调用这个 skill 生成图”时，执行者必须进入生产模式，并给出一个明确结果：

```text
成功：产出图片文件 + 复查记录
受阻：写出 BLOCKED.md，说明缺哪个真实出图后端/素材/证据，不得假装已生成
原型：若无真实图像模型但用户接受原型，可产出 local prototype，并明确标注“原型，不是真实图像模型结果”
```

### 0.1 输出文件夹

每次调用先建一个主题文件夹，例如：

```text
work/chinese_dreamcore_nutrition_runs/<topic_id>_<YYYYMMDD>/
```

至少落地：`evidence_card.yaml`、`prompt_used.md`、`review_note.md`，以及以下二者之一：

- 真实出图后端可用：`base_images/*.png`、`selected_base.png`、`final.png`。
- 真实出图后端不可用但用户接受原型：`selected_base_prototype.png` 或 `final_prototype.svg/png`，并在 `review_note.md` 写明“原型”。

### 0.2 出图后端路由

按顺序判断：

1. 用户明确指定的图像生成工具/账号/模型是否可用；若指定，必须按指定执行，不得替换。
2. 当前 LingTai 是否有可用图像生成 MCP、CLI、网页工具或本地模型；有则用它生成 9 张无字底图。
3. 若无真实图像生成后端，但只需闭环原型，可运行 `scripts/render_local_prototype.py` 生成无字 PNG 原型图。
4. 若用户要求“真实模型生成图”，而后端缺失，则停止并写 `BLOCKED.md`：缺什么、需要谁配置、可先做什么原型。

### 0.3 本地原型脚本

无真实出图后端时，可用：

```bash
python3 .library/custom/chinese-dreamcore-nutrition-image-workflow/scripts/render_local_prototype.py \
  --topic-id apple_nutrition \
  --title 一只苹果的温柔营养 \
  --outdir work/chinese_dreamcore_nutrition_runs/apple_nutrition_<YYYYMMDD>/
```

它只生成“中式梦核营养”无字底图原型，用来跑通闭环；不得把它说成真实图像模型产物。

## 1. 定位与触发

### 1.1 何时使用

- 要生产一张**中式梦核 · 营养科普 · 可爱温柔**的静态图片。
- 已有主题证据卡，或愿意先按本 skill 模板建立证据卡。
- 目标是**无字底图 + 后期中文排版**，最终导出 `final.png`。
- 接受“先 9 张候选、硬淘汰、Cute Gate、选 1 张”的流水线。

### 1.2 何时不要触发

- 没有证据卡且用户拒绝建立。
- 需要视频、实拍、二次元、营销海报、药品/疗效图。
- 要求模型直接生成中文正文或新增营养结论。
- 需要核验营养事实：本 skill 只排版，不生成/不核验营养内容。

### 1.3 一句话流程

```text
主题证据卡 → prompt 模块 → 9 张无字底图 → 硬淘汰 → Cute Gate → 中文排版 → 复查 → final.png
```

---

## 2. 中式梦核营养硬门

每张图必须同时通过三层，否则退回。

| 层级 | 必须 | 禁止 |
|---|---|---|
| **中式梦核** | 旧家宅、月洞门、花窗、竹帘、白瓷、粗陶、木桌、宣纸光、月白雾感 | 阴森、废弃、鬼片、无限走廊、玄学/宗教/风水/仙侠堆叠 |
| **营养科普** | 画面服务营养主题，食物是日常普通食物 | 食物画成药、疗效/减肥承诺、假文献、恐吓式健康海报 |
| **可爱温柔** | 圆润、软、小份量、亲近、第一眼可爱 | 廉价卡通、二次元少女、玩具广告、幼稚表情 |

任一不成立：直接退回当前层。

---

## 3. 输入：主题证据卡

开始生成前必须落一张卡，模板见 `assets/evidence-card-template.yaml`。

关键字段：

```yaml
topic_id: <主题唯一标识>
中文主题: <如：早餐蛋白质怎么吃更稳>
目标人群: <普通成年人 / 家庭科普>
一句主信息: <已核/待核的一句话，如：早餐搭配优质蛋白有助于增加饱腹感>
证据状态: 已核 / 待核 / 仅科普常识
可说内容: <列表>
不可说内容: <列表>
允许画面元素: <列表>
禁止画面元素: <列表>
```

证据状态规则：

- `已核`：可进入正式排版，但表达仍须保守。
- `待核`：只能做内部草稿，图上写占位或打草稿水印，不可公开发布。
- `仅科普常识`：可说大白话，不写具体文献名。

> 本 skill 不负责核验营养事实。遇到具体营养内容，先走证据卡、权威来源或调用营养相关 skill。

---

## 4. Prompt 模块库

prompt 不写成灵感散文，拆成模块。模板见 `assets/prompt-modules.yaml`。

```yaml
subject_cute: 决定可爱主体
  examples:
    - round small bowl with gentle warm steam
    - tiny ceramic spoon resting beside a soft cloth
    - plump white porcelain cup with a shy little handle

chinese_daily_scene: 决定中式日常空间
  examples:
    - moon gate window in an old quiet courtyard
    - bamboo curtain, warm wooden table, white porcelain
    - paper-cut shadow on a cream wall

dreamy_layer: 决定梦幻感
  examples:
    - soft moon-white light
    - thin mist like rice paper texture
    - floating dust motes, gentle glow, quiet morning air

composition: 为后期中文排版留白
  examples:
    - main subject in lower right, clean empty space in upper left
    - centered object with wide blank margin on top

quality: 控制画质
  examples:
    - soft watercolor texture
    - gentle semi-realistic illustration
    - high detail but not photorealistic advertising

negative: 禁止跑偏
  examples:
    - no text, no letters, no logo, no watermark
    - no horror, no abandoned hallway, no infinite corridor
    - no anime girl, no chibi character, no childish toy style
    - no hospital, no medicine, no before-after body comparison
    - no luxury marketing poster, no cheap commercial ad
```

英文底图 prompt 模板：

```text
Create a vertical 4:5 nutrition education poster background with NO text.

Cute-first visual priority:
A soft, round, approachable [subject_cute], looking gentle and friendly without becoming cartoonish.

Chinese everyday dream setting:
Place it in [chinese_daily_scene], with [dreamy_layer].

Composition:
[composition]. Leave clean negative space for later Chinese typography.

Color and texture:
warm cream, moon white, pale apricot, soft jade green; low saturation, no neon, no harsh contrast. [quality].

Nutrition boundary:
Use only ordinary everyday food props. Do not imply medical treatment, weight-loss promise, or specific nutrition advice.

Strict negative prompt:
[negative]. Absolutely no readable text, no fake labels, no fake references, no logo, no watermark.
```

> 图像模型只负责无字底图，中文正文一律后期叠加，不让模型直接写中文。

---

## 5. 生成 9 张无字底图

最小批次：

```yaml
scenes: 3
variations_per_scene: 3
总图数: 9
尺寸: 4:5 或 3:4
文字: 禁止
```

建议从三个首选场景开始：

1. 月洞门旁的小桌与温热普通食物。
2. 竹帘窗下的白瓷杯、小碗、柔软蒸汽。
3. 旧家宅暖光里的圆润餐具与留白墙面。

每个场景 3 张变体，共 9 张。全部无字、无 logo、无水印。

---

## 6. 硬淘汰

出现以下任一，直接淘汰，不进入 Cute Gate：

1. 有文字、伪文字、乱码、logo、水印。
2. 有药品、针管、医院诊断感。
3. 有减肥羞辱、身材对比、恐吓符号。
4. 有阴森走廊、废弃空间、鬼片感。
5. 中式元素变成玄学、宗教、风水、仙侠。
6. 可爱变成幼稚玩具、廉价卡通、二次元少女。
7. 食物过于具体，暗示未经核验的营养建议。
8. 没有给中文标题和正文留白。

---

## 7. Cute Gate 评分

硬淘汰后评分。权重与门槛：

| 项目 | 权重 | 门槛 |
|---|---:|---|
| Cute 可爱 | 40% | ≥ 4/5 |
| Dreamy 梦感 | 25% | 柔光、薄雾、安静，不阴森 |
| Chinese 中式 | 20% | 日常中式母题，不堆符号 |
| Readable 可排版 | 15% | 适合中文标题/正文叠加 |

通过条件：

```yaml
Cute: >= 4/5
Total: >= 3.5/5
Hard veto: false
```

**150px 缩略图测试**：缩到手机缩略图大小，仍能一眼看出“软、圆、亲近”，主体不糊，留白够，中式元素可辨认。不过就不排版。

---

## 8. Prompt 返工规则

按失败维度修：

| 问题 | 加 | 删 |
|---|---|---|
| 不够可爱 | rounder shapes, softer edges, smaller scale, gently plump ceramic forms | cinematic, dramatic, mysterious, surreal horror, liminal |
| 不够中式 | moon gate window, bamboo curtain, white porcelain, warm wooden table, paper-cut shadow | generic asian, temple, dragon, lantern overload, fantasy palace |
| 梦感太阴森 | warm light, clean home atmosphere, safe cozy courtyard, morning glow | empty corridor, abandoned, dark, foggy horror, uncanny |
| 不适合排字 | large clean blank space in upper left, simple background, no clutter, poster layout safe area | busy details, full-frame pattern, dense decoration |

返工后回到第 5 步重新生成 9 张，不要只修一张。

---

## 9. 中文排版

### 9.1 原则

- 中文正文后期叠加，不让图像模型直接生成。
- 工具任选：Figma / Canva / Python Pillow / ReportLab。

### 9.2 文字层级

```yaml
标题: 8-14 个字
副标题: 可选，一句话
正文: 2-3 条，每条不超过 18 字
来源角标: 内容参考：WHO / 中国居民膳食指南等公开资料整理
免责声明: 如需个体化建议，请咨询医生或营养师
```

### 9.3 文案红线

禁止：

- “必须”“一定”“治愈”“逆转”。
- “月瘦 XX 斤”。
- “排毒”“清除毒素”。
- 编造文献名和专家共识。
- 把普通食物画成药。

推荐：

- “可以试着……”
- “更稳妥的做法是……”
- “对多数人来说……”
- “如果你有慢病或特殊情况，请先咨询专业人员。”

---

## 10. 最终复查

按六门复查，全部通过才导出 `final.png`：

### 10.1 画面复查

- 可爱是否第一眼成立？
- 梦感是否温柔，不阴森？
- 中式是否日常，不堆符号？
- 食物是否普通，不偷渡营养处方？

### 10.2 文字复查

- 有没有假文献？
- 有没有绝对化表达？
- 有没有恐吓或羞辱？
- 有没有把待核内容写成事实？

### 10.3 排版复查

- 手机缩略图是否可读？
- 标题是否遮挡主体？
- 正文是否太密？
- 留白是否舒服？

### 10.4 安全复查

- 无本地路径、无 `.lingtai` 内部 ID、无 token/key/secret。
- 无未授权 IP / logo / 明星脸。

---

## 11. 停止条件

满足任一即停止，不继续往下走：

1. 9 张里没有 Cute ≥ 4 的图 → 不排版，先改 prompt。
2. 营养证据未核 → 只做内部草稿，不公开。
3. 中文排版遮挡或不可读 → 返回 layout。
4. 用户要求修改方向超出本 skill 范围（视频、疗效图、营销海报）。

---

## 12. 失败层修复

失败时只修失败层，不整条推倒：

| 失败层 | 修复动作 |
|---|---|
| 证据卡 | 回权威来源或营养 skill 重新核验，不硬画 |
| prompt | 按第 8 节返工，改模块词 |
| 底图生成 | 重跑 9 张，不纠结单张 |
| 硬淘汰 | 检查 negative prompt 是否足够严格 |
| Cute Gate | 先修“可爱”维度，可爱不够总分为零 |
| 中文排版 | 改字体/位置/留白，不重新生成图 |
| 复查失败 | 按失败门类返回对应层 |

---

## 13. 交付物清单

每个主题交付一个文件夹：

```text
/<topic_id>/
  evidence_card.yaml
  prompt_used.md
  base_images/
    scene01_v01.png
    scene01_v02.png
  cute_gate_scorecard.md
  selected_base.png
  layout_source.fig / .psd / .py
  final.png
  final_mobile_preview.png
  review_note.md
```

`review_note.md` 必写：

1. 这张图想表达什么。
2. 哪些营养文字已核，哪些待核。
3. 为什么选这张底图。
4. Cute Gate 得分。
5. 是否可公开发布。

---

## 14. 验收门

发布前必须全部勾选：

- [ ] 硬门三层成立：中式梦核 + 营养科普 + 可爱温柔。
- [ ] 证据卡存在，营养文字来源清楚。
- [ ] 9 张底图无字、无 logo、无水印。
- [ ] 选中底图 Cute ≥ 4，总分 ≥ 3.5，无 hard veto。
- [ ] 中文排版手机缩略图可读。
- [ ] 文案无绝对化、无疗效承诺、无假文献。
- [ ] 无本地路径、无内部 ID、无 token/secret。
- [ ] `review_note.md` 已填写。

---

## 15. 边界与免责声明

- 本 skill **只负责图片生产流程**，不生成、不核验营养事实。
- 所有营养内容必须来自用户提供的证据卡、权威来源或营养相关 skill。
- 禁止编造指南、论文、年份、机构。
- 待核内容只能做内部草稿，不可公开发布。
- 不替代医生或注册营养师建议。

---

## 16. 示例：苹果主题（仅示例，非唯一主题）

以下是一个可替换的主题示例，用于说明 prompt 怎么用。实际使用时把 `[subject_cute]` 替换成当前主题食物。

```text
Cute-first subject:
A round fresh apple with natural red and pale yellow skin, placed gently on a small white porcelain plate. The apple should feel soft, friendly, and ordinary, not magical.

Chinese dreamcore nutrition setting:
An old Chinese home interior with a moon gate window in the background, soft moon-white morning light, warm wooden table, faint rice-paper texture, clean air, quiet and safe.

Composition:
Place the apple and plate in the lower right. Leave large clean blank space in the upper left for later Chinese title and short text.
```

中文排版示例（如证据卡允许）：

```text
标题：一只苹果的温柔营养
正文1：完整鲜果，比果汁更稳妥
正文2：洗净带皮吃，保留更多纤维口感
正文3：它是好水果，不是神奇药方
角标：内容参考公开营养资料整理
```

> 不要把“苹果”当作本 skill 唯一主题。任何普通日常食物/膳食主题都可以按同样流程处理。

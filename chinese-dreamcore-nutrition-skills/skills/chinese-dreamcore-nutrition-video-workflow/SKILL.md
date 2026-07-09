---
name: chinese-dreamcore-nutrition-video-workflow
description: |
  把“中式梦核 + 营养科普 + 可爱温柔”风格沉淀为可调用的短视频生产 skill：用户给主题和合格底图后，必须产出视频文件，或明确写出缺失的视频合成/图生视频后端。
  触发时机：用户说“调用这个 skill 生成视频/把这张图做成中式梦核营养短视频”，或想基于已通过 Cute Gate 的中式梦核营养底图生成 15-45 秒竖屏短视频；已持有或愿意先建立主题证据卡、脚本、分镜；接受先 15 秒/5 镜头 MVP。
  不要触发：用户没有合格底图、没有证据卡、一上来就要 60 秒以上长视频/复杂图生视频/数字人口播/营销爆款、要新增/核验营养事实。
version: 1.0.0
tags: [video-generation, workflow, chinese-dreamcore, nutrition, cute, short-video]
last_changed_at: 2026-07-09T08:00:00Z
---

# 中式梦核营养视频生成工作流

## 0. 可调用生产契约（调用本 skill 必须先看）

本 skill 不是只写脚本/分镜。用户说“调用这个 skill 生成视频”时，执行者必须进入生产模式，并给出一个明确结果：

```text
成功：产出 final_1080x1920.mp4 或 preview_720p.mp4 + 复查记录
受阻：写出 BLOCKED.md，说明缺哪个底图/视频合成工具/图生视频后端，不得假装已生成
MVP：若无图生视频模型但有 ffmpeg/剪辑工具，可用合格静图做轻微平移/缩放 slideshow 原型，并标注“原型”
```

### 0.1 输出文件夹

每次调用先建一个主题文件夹，例如：

```text
work/chinese_dreamcore_nutrition_video_runs/<video_topic_id>_<YYYYMMDD>/
```

至少落地：`evidence_card.yaml`、`script.md`、`storyboard.md`、`storyboard.json`、`review_note.md`，以及以下之一：

- 视频合成后端可用：`final_1080x1920.mp4` 和 `preview_720p.mp4`。
- 只有静图轻动效可用：`preview_slideshow_prototype.mp4`，并标注“原型”。
- 后端缺失：`BLOCKED.md`，写清下一步需要配置什么。

### 0.2 后端路由

按顺序判断：

1. 是否已有通过图片 skill/Cute Gate 的底图；没有则先回图片 skill，不直接做视频。
2. 用户明确指定的视频工具/模型是否可用；若指定，必须按指定执行，不得替换。
3. 当前环境是否有 ffmpeg、Remotion、FFCreatorLite、剪映/CapCut、Kling/MiniMax/Seedance/本地图生视频工具；有则选最小可控方案。
4. 若没有任何可执行后端，停止并写 `BLOCKED.md`；不要只交一份“视频方案”冒充视频产物。

## 1. 定位与触发

### 1.1 何时使用

- 要生产一支**中式梦核 · 营养科普 · 可爱温柔**的竖屏短视频。
- 已按图片 skill 生成并通过 Cute Gate 的**无字底图**。
- 已有主题证据卡、短视频脚本、分镜表。
- 愿意先跑 **15 秒 / 5 镜头 MVP**，不一上来就复杂视频模型。

### 1.2 何时不要触发

- 没有合格底图或证据卡。
- 一上来要求 60 秒以上长视频、数字人口播、复杂图生视频、营销爆款剪辑。
- 需要新增或核验营养事实：本 skill 只负责视频生产，不生成/不核验营养内容。
- 目标不是中式梦核可爱温柔风。

### 1.3 一句话流程

```text
主题证据卡 → 脚本/分镜 → 基于图片 skill 的 approved base images → 轻动效/图生视频微动效 → 中文字幕/配音/BGM → 合成 → 复查 → final.mp4
```

---

## 2. 中式梦核营养硬门

每支视频必须同时通过三层，否则退回。

| 层级 | 必须 | 禁止 |
|---|---|---|
| **中式梦核** | 旧家宅、月洞门、花窗、竹帘、白瓷、粗陶、木桌、宣纸光、月白雾感 | 阴森、废弃、鬼片、无限走廊、玄学/宗教/风水/仙侠堆叠 |
| **营养科普** | 每句字幕/旁白回到证据卡；画面只辅助理解，不新增结论 | 疗效/减肥承诺、假文献、绝对化表达、把待核内容写成事实 |
| **可爱温柔** | 镜头节奏慢、软、亲近；动效只轻轻活起来 | 强刺激、爆款、数字人口播、营销剪辑、恐怖或廉价动效 |

---

## 3. 输入：三张卡

### 3.1 主题证据卡

同图片 skill。必须包含：

```yaml
topic_id: <主题唯一标识>
中文主题: <一句话主题>
证据状态: 已核 / 待核 / 仅科普常识
一句主信息: <已核/待核>
可说内容: <列表>
不可说内容: <列表>
```

> 本 skill 不负责核验营养事实。字幕/旁白每句话必须能回到证据卡。

### 3.2 视觉风格卡

```yaml
style_name: 可爱优先中式梦感
cute_priority: 最高
visual_keywords:
  - round soft objects
  - warm ordinary food
  - moon-white light
  - bamboo curtain
  - white porcelain
  - soft steam
negative_keywords:
  - horror
  - abandoned corridor
  - anime girl
  - cheap ad
  - hospital warning poster
  - fake text
```

### 3.3 视频规格卡

```yaml
format: vertical_short_video
ratio: 9:16
resolution: 1080x1920
duration: 15-45s
scene_count: 5-7
caption: Chinese, added in post-production
voiceover: optional
bgm: soft, low volume, non-distracting
publish_status: internal draft until reviewed
```

---

## 4. 脚本与分镜

### 4.1 最小脚本长度（15 秒 MVP）

```yaml
shots: 4-5
voiceover_chars: 80-120 中文字
title_chars: 8-14 中文字
key_points: 2 条
```

### 4.2 脚本结构

```text
开头：一个温柔问题，不制造焦虑。
承接：一句已核或待核主信息。
展开：2-3 条可执行但保守的小提示。
收束：提醒个体情况不同，需要专业复核。
```

### 4.3 分镜表

每镜一张卡，模板见 `assets/storyboard-template.yaml`：

```yaml
shot_id: S01
duration: 3s
画面目的: 建立温柔早晨氛围
底图需求: 月洞窗、白瓷小碗、柔软蒸汽、上方留白
运动方式: 慢推近 / 轻微平移 / 蒸汽微动
屏幕文字: <来自证据卡的短句>
旁白: <可选，与字幕一致>
Cute Gate: 待评分
evidence状态: 只做氛围 / 来自证据卡第 X 条
```

---

## 5. 推荐 5 镜头最小结构

| 镜头 | 时长 | 目的 | 画面 | 屏幕文字 |
|---|---|---|---|---|
| S01 | 3s | 开场 | 月白窗光下小木桌，圆润白瓷碗，柔软蒸汽，大片留白 | <主题问题> |
| S02 | 3s | 情绪承接 | 竹帘轻动，普通温热食物在小碗里 | 不用吃得很复杂 |
| S03 | 3s | 科普信息 1 | 小碗、杯子、盘子呈圆润组合 | <证据卡第 1 条> |
| S04 | 3s | 科普信息 2 | 柔光照在普通餐具上 | <证据卡第 2 条> |
| S05 | 3s | 收束 | 窗边暖光，画面更安静 | 个体情况不同，可问专业人员 |

每镜字幕/旁白都必须能回到证据卡。

---

## 6. 画面生成：每个镜头先生成底图

### 6.1 每镜 3 张候选

```yaml
shots: 5
images_per_shot: 3
总底图: 15
```

每张底图都必须过图片 skill 的硬淘汰和 Cute Gate（Cute ≥ 4，总分 ≥ 3.5）。

### 6.2 底图 prompt 模板

```text
Create a vertical 9:16 no-text illustration background for a warm nutrition education short video.

Scene purpose: [shot purpose]
Cute-first subject: [round soft object / ordinary warm food / gentle ceramic bowl]
Chinese everyday dream setting: [moon gate window / bamboo curtain / wooden table / rice paper light]
Motion-ready composition: leave clean space for Chinese subtitles, keep main subject stable, avoid clutter.
Mood: cute, soft, safe, warm, dreamy but not eerie.

Strict negative:
no text, no logo, no watermark, no horror, no abandoned corridor, no hospital, no medicine, no weight-loss ad, no anime girl, no fake food label, no fake reference.
```

---

## 7. 动效策略

先用轻动效，不急着上复杂图生视频。

### 7.1 第一优先：后期镜头运动（MVP 推荐）

- 慢推近
- 慢平移
- 轻微缩放
- 柔光浮动
- 蒸汽透明层缓慢上升
- 纸纹/尘光轻微移动

优点：稳定、可控、不变形、不乱生成。

### 7.2 第二优先：图生视频微动效

只用于 3-5 秒小段。可用 CogVideo / HunyuanVideo / MiniMax / Kling / Seedance 等。

图生视频 prompt：

```text
Animate this image subtly. Keep all objects stable and cute. Only add gentle steam movement, soft light breathing, tiny floating dust motes. Do not change the food, do not add text, do not add people, do not add new objects, do not make it cinematic or horror.
```

淘汰条件：食物变形、出现文字、场景变阴森、主体乱跳、增加人物/药物/广告元素。

### 7.3 不建议

- 大幅镜头穿梭
- 复杂人物表演
- 数字人口播
- 快节奏营销剪辑
- 抖音爆款式强钩子

---

## 8. 字幕与配音

### 8.1 字幕

- 每屏最多 1 个标题 + 1 行短句。
- 每行不超过 14-18 个中文字。
- 字体圆润、清楚，不花哨。
- 字幕安全区：底部不要贴边，上下留 8-10%。
- 字幕和画面主体不能抢。

### 8.2 配音

- 温柔、慢一点。
- 不像广告推销。
- 不夸张喊口号。
- 和字幕内容一致。
- 不新增字幕里没有的营养结论。

### 8.3 BGM

- 音量低。
- 无强鼓点。
- 无恐怖氛围。
- 无版权风险。
- 不压过人声。

---

## 9. 合成

### 9.1 最小可运行方案

```text
无字底图 PNG
+ 中文字幕 PNG/文字层
+ 轻微缩放/平移
+ 可选配音 WAV
+ 可选 BGM
→ ffmpeg / CapCut / 剪映 / Remotion / FFCreatorLite 合成
```

### 9.2 程序化方案

```yaml
engine: Remotion 或 FFCreatorLite
input:
  - storyboard.json
  - base_images/
  - captions.json
  - voice.wav
  - bgm.mp3
output:
  - final_1080x1920.mp4
  - preview_720p.mp4
```

### 9.3 storyboard.json 片段示例

```json
{
  "video_id": "breakfast_protein_001_v01",
  "ratio": "9:16",
  "resolution": "1080x1920",
  "duration": 15,
  "shots": [
    {
      "id": "S01",
      "duration": 3,
      "image": "base_images/S01_selected.png",
      "motion": "slow_zoom_in",
      "caption": "早餐怎么吃更稳？",
      "voice_text": "早上不用吃得很复杂。",
      "caption_position": "upper_left",
      "cute_gate_score": 4.4
    }
  ]
}
```

---

## 10. 最终复查

### 10.1 内容复查

- 每一句营养话术是否来自证据卡？
- 有没有绝对化、恐吓、营销表达？
- 有没有 fake reference？
- 有没有把待核内容做成正式结论？

### 10.2 视觉复查

- 第一眼是否可爱？
- 梦感是否安全温柔？
- 中式元素是否日常？
- 字幕是否清楚？
- 画面是否过暗、过雾、过乱？

### 10.3 动效复查

- 食物有没有变形？
- 画面有没有突然出现新物体？
- 动效是否晕、快、廉价？
- 节奏是否太像广告？

### 10.4 声音复查

- 人声是否清楚？
- BGM 是否压人声？
- 语气是否温柔？
- 有没有诱导性营销感？

### 10.5 安全复查

- 无本地路径、无 `.lingtai` 内部 ID、无 token/key/secret。
- 无未授权商标/IP/明星脸。
- 无自动发布行为。

---

## 11. 停止条件

满足任一即停止：

1. 任一镜头底图 Cute < 4 或总分 < 3.5 → 回图片 skill 改 prompt，不做视频。
2. 脚本/字幕里有任何一句话无法回到证据卡 → 回证据卡，不改画面掩盖。
3. 图生视频微动效导致变形/阴森/新增物体 → 退回静图平移。
4. 配音/BGM 破坏温柔感 → 换素材或取消。
5. 用户要求扩到 60 秒以上、加数字人、加营销剪辑 → 说明超出本 skill 范围。

---

## 12. 失败层修复

| 失败层 | 修复动作 |
|---|---|
| 证据卡/话术 | 回证据卡或营养 skill，不硬编 |
| 底图 | 回图片 skill 改 prompt 重跑 |
| 动效 | 先用后期镜头运动；图生视频失败就退回静图平移 |
| 字幕 | 改排版，不重新生成图 |
| 配音/BGM | 换素材或取消 |
| 合成 | 检查 ffmpeg/Remotion 参数，不牺牲可爱风格 |
| 复查失败 | 按失败门类返回对应层 |

---

## 13. 交付物清单

```text
/<video_topic_id>/
  evidence_card.yaml
  script.md
  storyboard.md
  storyboard.json
  prompts/
    S01_prompt.md
    S02_prompt.md
  base_images/
    S01_v01.png
    S01_selected.png
  motion_tests/
    S01_motion_test.mp4
  captions.json
  voice.wav
  bgm_license_note.md
  render_source/
    remotion_project/ 或 ffcreator_project/
  final_1080x1920.mp4
  preview_720p.mp4
  review_note.md
```

`review_note.md` 必写：

1. 主题和目标人群。
2. 证据状态。
3. 使用了哪些镜头。
4. 哪些图过了 Cute Gate。
5. 字幕/配音是否与证据卡一致。
6. 是否可公开发布。

---

## 14. 验收门

发布前必须全部勾选：

- [ ] 硬门三层成立：中式梦核 + 营养科普 + 可爱温柔。
- [ ] 所有镜头底图来自图片 skill 并通过 Cute Gate。
- [ ] 每句字幕/旁白都能回到证据卡。
- [ ] 动效不阴森、不廉价、食物不变形。
- [ ] 字幕手机可读，不贴边，不遮挡主体。
- [ ] 配音/BGM 温柔、不压人声、不营销。
- [ ] 无本地路径、无内部 ID、无 token/secret。
- [ ] `review_note.md` 已填写。

---

## 15. 边界与免责声明

- 本 skill **只负责视频生产流程**，不生成、不核验营养事实。
- 所有营养话术必须来自证据卡、权威来源或营养相关 skill。
- 禁止编造指南、论文、年份、机构。
- 待核内容只能做内部草稿，不可公开发布。
- 不自动发布，必须人工复查。
- 不替代医生或注册营养师建议。

---

## 16. 示例：15 秒苹果主题分镜（仅示例）

假设证据卡是“苹果的营养”，可设计如下 5 镜：

| 镜头 | 时长 | 画面 | 字幕/旁白 | 说明 |
|---|---|---|---|---|
| S01 | 3s | 月洞门下白瓷盘里的苹果 | 苹果，不只是甜 | 建立主题 |
| S02 | 3s | 竹帘窗光落在苹果切片上 | 完整鲜果，比果汁更稳妥 | 来自证据卡 |
| S03 | 3s | 苹果与淡青布巾，留白 | 洗净带皮吃，保留更多纤维口感 | 谨慎表达 |
| S04 | 3s | 木桌上苹果与小杯 | 它是好水果，不是神奇药方 | 防夸大 |
| S05 | 3s | 旧家宅暖光收束 | 个体情况不同，可问专业人员 | 安全收口 |

动效只用：慢推近、轻平移、柔光微动。不使用强图生视频，不让苹果变形。

> 不要把“苹果”当作本 skill 唯一主题。任何普通日常食物/膳食主题都可以按同样流程处理。

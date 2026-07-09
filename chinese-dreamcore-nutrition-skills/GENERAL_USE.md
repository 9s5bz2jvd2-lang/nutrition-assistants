# 通用使用说明｜General Use Guide

这份说明把本目录从“某个灵台内部工作流”改成更通用的可复用包：别人可以在 LingTai、其他 agent 系统，或普通人工流程中使用。

This guide makes the package portable beyond one private LingTai setup. Other users can reuse it inside LingTai, in another agent framework, or as a manual production workflow.

## 1. 谁能用｜Who can use it

### 中文

三类人都能用：

1. **LingTai 用户**：把 `skills/` 下的两个 skill 目录放进自己的 custom skill 目录，刷新后调用。
2. **其他 Agent/工作流用户**：把 `SKILL.md` 当作执行协议，把 `assets/*.yaml` 当作输入模板，把 `scripts/` 当作可选本地工具。
3. **人工团队**：不用任何 agent，也可以按证据卡、prompt、Cute Gate、后期排版、复查表逐步执行。

### English

Three groups can use it:

1. **LingTai users**: copy the two folders under `skills/` into their own custom-skill directory and refresh.
2. **Other agent/workflow users**: treat `SKILL.md` as an execution protocol, `assets/*.yaml` as input templates, and `scripts/` as optional local tools.
3. **Human teams**: use the evidence card, prompts, Cute Gate, post-layout, and review steps manually without an agent runtime.

## 2. 安装到 LingTai｜Install in LingTai

### 中文

把这两个目录复制到目标灵台的 custom skills 区：

```text
skills/chinese-dreamcore-nutrition-image-workflow/
skills/chinese-dreamcore-nutrition-video-workflow/
```

刷新技能目录后即可调用。不要把 `trial_runs/` 当作必须安装内容；它只是示例试跑。

### English

Copy these two folders into the target LingTai custom-skills area:

```text
skills/chinese-dreamcore-nutrition-image-workflow/
skills/chinese-dreamcore-nutrition-video-workflow/
```

Refresh the skill catalog afterward. `trial_runs/` is an example run, not required installation content.

## 3. 非 LingTai 用法｜Use without LingTai

### 中文

如果你没有 LingTai，也可以这样用：

1. 选择一个主题，例如“苹果的营养”或“早餐里的全谷物”。
2. 复制 `assets/evidence-card-template.yaml`，填入主题、已核事实、安全表达、禁止表达。
3. 按 image skill 写 9 条英文无字底图 prompt。
4. 用你自己的图像工具生成 9 张 4:5 无字底图。
5. 按 Cute Gate 打分淘汰。
6. 用 Canva/Figma/Pillow/设计工具后期加中文正文。
7. 如果做视频，再按 video skill 写 15 秒/5 镜头分镜并合成。

### English

If you do not use LingTai:

1. Choose a topic, such as apple nutrition or whole grains at breakfast.
2. Copy `assets/evidence-card-template.yaml` and fill in the topic, verified facts, safe claims, and forbidden claims.
3. Follow the image skill to write nine English no-text base-image prompts.
4. Generate nine 4:5 no-text base images with your own image tool.
5. Score and filter them with Cute Gate.
6. Add Chinese text in post-layout with Canva, Figma, Pillow, or another design tool.
7. For video, follow the video skill to create a 15-second / 5-shot storyboard and render it.

## 4. 后端接口要求｜Backend contract

### 中文

真实生成不是靠本目录“凭空变出来”。你需要接入自己的后端。最低要求：

图像后端：

```text
input: English prompt + output directory + aspect ratio 4:5 + no-text requirement
output: one or more PNG files, preferably 1080x1350 or similar vertical format
must: no Chinese body text, no watermark/logo, no horror/uncanny/eye-gaze drift
```

视频后端：

```text
input: approved base images + storyboard + duration + motion/caption/voice/BGM instructions
output: mp4 preview or final render
must: preserve evidence-card facts; do not invent nutrition claims in visuals, captions, or voiceover
```

如果没有后端，必须写 `BLOCKED.md` 或产出明确标注的本地原型，不得假装已经生成真实模型图/视频。

### English

This folder does not magically provide a model backend. You must connect your own backend.

Image backend minimum contract:

```text
input: English prompt + output directory + 4:5 aspect ratio + no-text requirement
output: one or more PNG files, preferably 1080x1350 or a similar vertical format
must: no Chinese body text, no watermark/logo, no horror/uncanny/eye-gaze drift
```

Video backend minimum contract:

```text
input: approved base images + storyboard + duration + motion/caption/voice/BGM instructions
output: mp4 preview or final render
must: preserve evidence-card facts; do not invent nutrition claims in visuals, captions, or voiceover
```

If no backend exists, write `BLOCKED.md` or produce a clearly labeled local prototype. Do not pretend that a prototype is a real model-generated image or video.

## 5. 如何替换主题｜How to change the topic

### 中文

不要把苹果写死。换主题时只换这四处：

1. `topic_id` 和标题。
2. 证据卡里的已核营养事实。
3. 食物主体和道具。
4. 中文排版文案。

不变的是：中式梦核、可爱优先、营养证据门、无字底图、Cute Gate、后期中文排版、最终复查。

### English

Do not hard-code apples. When changing the topic, replace only these parts:

1. `topic_id` and title.
2. Verified nutrition facts in the evidence card.
3. Main food subject and props.
4. Chinese layout copy.

Keep the fixed workflow: Chinese dreamcore, cute-first visual gate, evidence card, no-text base image, Cute Gate, Chinese post-layout, and final review.

## 6. 最小试跑｜Minimal trial

### 中文

若没有真实图像后端，可以先跑本地原型脚本验证闭环：

```bash
python3 skills/chinese-dreamcore-nutrition-image-workflow/scripts/render_local_prototype.py \
  --topic-id apple_nutrition \
  --title '一只苹果的温柔营养' \
  --outdir trial_runs/local_trial_apple
```

这只说明“流程能落地为文件”，不说明模型图质量。

### English

If no real image backend is available, use the local prototype renderer only to validate the loop:

```bash
python3 skills/chinese-dreamcore-nutrition-image-workflow/scripts/render_local_prototype.py \
  --topic-id apple_nutrition \
  --title 'A gentle nutrition note for one apple' \
  --outdir trial_runs/local_trial_apple
```

This only proves that the workflow can produce a file. It does not prove real image-model quality.

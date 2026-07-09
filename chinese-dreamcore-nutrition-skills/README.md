# 中式梦核营养图片/视频 Skills｜Chinese Dreamcore Nutrition Image & Video Skills

## 中文说明

这组目录收纳两套可调用的 LingTai custom skills，用于把「中式梦核 + 营养科普 + 可爱温柔」做成可执行的内容生产流程。

它不是普通审美说明书，而是生产契约：当用户调用图片或视频 skill 时，执行者必须产出文件，或清楚写明缺少哪个真实后端，不能用“方案”冒充成品。

### 包含内容

- `skills/chinese-dreamcore-nutrition-image-workflow/`
  - 给定营养主题后，走证据卡、无字底图 prompt、硬淘汰、Cute Gate、后期中文排版与最终复查。
  - 若真实图像生成后端缺失，可用本地 fallback 生成原型 PNG；但必须标注“原型，不是真实图像模型结果”。

- `skills/chinese-dreamcore-nutrition-video-workflow/`
  - 基于已通过 Cute Gate 的底图，生成 15–45 秒竖屏短视频 workflow。
  - 若视频合成或图生视频后端缺失，必须写 `BLOCKED.md`，不得只交“视频方案”冒充视频产物。

- `trial_runs/gpt_skill_trial_apple_20260709/`
  - GPT 分神实际调用图片 skill 的苹果主题试跑。
  - 因当时没有真实图像生成后端，产物 `selected_base_prototype.png` 是本地 fallback 原型，不是真实图像模型图。

- `reports/`
  - Kimi 初稿报告与主身复查记录。

### 安全边界

1. 营养事实必须回到证据卡；不可编造指南、论文、年份、机构文件或疗效承诺。
2. 视觉模型不得生成中文正文；中文排版应后期叠加。
3. 本地原型可用于闭环验证，但不得冒充真实 AI 图像生成结果。
4. 若缺少真实图像/视频后端，必须明确阻塞。

### 下一步

若要产出真正模型图，需要配置可调用的图像生成后端，例如 image-generation MCP、本地 ComfyUI/SDXL/Flux 工作流，或稳定可用的外部 CLI/API。后端需要支持英文 prompt、4:5 无字 PNG、批量候选图生成，并允许后续 Cute Gate 评分与中文排版。

## English explanation

This folder contains two callable LingTai custom skills for producing cute-first Chinese dreamcore nutrition media.

They are not merely style notes. They define a production contract: when the image or video skill is invoked, the executor must either produce concrete files or explicitly state which real backend is missing. A written plan must not be presented as a finished image or video.

### What is included

- `skills/chinese-dreamcore-nutrition-image-workflow/`
  - Given a nutrition topic, the skill guides an evidence card, no-text base-image prompts, hard veto checks, Cute Gate scoring, Chinese post-layout, and final review.
  - If no real image-generation backend is available, it may generate a local fallback prototype PNG, but it must be labeled as a prototype, not a real image-model result.

- `skills/chinese-dreamcore-nutrition-video-workflow/`
  - Builds a 15–45 second vertical short-video workflow from base images that already passed Cute Gate.
  - If video synthesis or image-to-video tooling is missing, it must write `BLOCKED.md`; a video plan must not be treated as a video product.

- `trial_runs/gpt_skill_trial_apple_20260709/`
  - A GPT sub-agent trial that actually invoked the image skill with an apple-nutrition topic.
  - Because no real image-generation backend was available during the trial, `selected_base_prototype.png` is a local fallback prototype, not a real image-model output.

- `reports/`
  - Kimi's authoring report and the main-agent review note.

### Safety boundaries

1. Nutrition claims must trace back to the evidence card. Do not invent guidelines, papers, years, institutions, or therapeutic promises.
2. Image/video models should not generate Chinese body text directly; Chinese text should be added in post-layout.
3. Local prototypes are allowed for workflow validation, but must never be passed off as real AI-generated images.
4. If the required image/video backend is missing, state the blocker clearly.

### Next step for real generation

To produce real model-generated images, configure a callable image-generation backend such as an image-generation MCP, local ComfyUI/SDXL/Flux workflow, or a stable external CLI/API. The backend should support English prompts, 4:5 no-text PNGs, batch candidate generation, and downstream Cute Gate scoring plus Chinese layout.

## 通用化入口｜General portability

- 通用使用说明 / General use guide: [`GENERAL_USE.md`](GENERAL_USE.md)
- 后端接口契约 / Backend contract: [`docs/backend-contract.md`](docs/backend-contract.md)

# GPT skill trial report — 苹果的营养

## 结果

已按 `chinese-dreamcore-nutrition-image-workflow` 的“可调用生产契约”完成一次可检查试跑，输出目录：

`work/chinese_dreamcore_nutrition_runs/gpt_skill_trial_apple_20260709/`

实际产物：

- `evidence_card.yaml`
- `prompt_used.md`
- `review_note.md`
- `selected_base_prototype.png`
- `render_manifest.json`
- `GPT_SKILL_TRIAL_REPORT.md`

## 是否真实模型图

不是。`selected_base_prototype.png` 是 **原型，不是真实图像模型结果**。

## 使用的后端/原型

- 未发现本次 daemon 可用的真实图像生成 MCP、CLI、网页工具或本地模型后端。
- 按 skill 和父任务约束，运行本地 fallback：
  `scripts/render_local_prototype.py`
- 该脚本用本地程序化绘制生成无字 PNG，用于闭环验证，不可冒充图像模型生成图。

## QA / 验证

- 已用 bash 验证必需文件存在，且 PNG 非空/可识别。
- 已用 vision 做简短 QA：图像可爱温柔；有竹帘、圆形窗/中式日常空间感；有后期营养科普排版留白；未见恐怖、眼睛凝视、伪文字/乱码、logo/watermark；整体明显是原型图而非真实模型精修图。

## 阻塞

真实出图阻塞：缺少可调用的真实图像生成后端。因此没有生成 9 张真实无字候选底图，也没有产出 `selected_base.png` / `final.png`。

营养发布阻塞：本次证据卡只按保守科普常识写成，未做外部营养事实核验；不建议公开发布。

## 下一步要真实生成需配置

1. 配置一个真实图像生成后端，例如可调用的 image-generation MCP、稳定可用的本地图像模型/ComfyUI/SDXL/Flux 工作流，或明确的外部 CLI/API。
2. 后端需支持按英文 prompt 生成无字 4:5 PNG，并能一次生成或批量生成 9 张候选底图。
3. 生成后按 skill 执行硬淘汰、Cute Gate、选中 `selected_base.png`，再用后期工具/Pillow/Figma/Canva 叠加中文排版生成 `final.png`。
4. 若要公开发布，先用权威来源或营养相关 skill 核验 `evidence_card.yaml` 中的营养表述。

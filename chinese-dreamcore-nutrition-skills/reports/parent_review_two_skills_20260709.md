# 中式梦核营养图片/视频双 Skill 主身复查记录

时间：2026-07-09

## 结论

两个 custom skill 已由 Kimi 分神初稿完成，主身按师父最新要求“调用 skill 就可以生成图/产物”补了生产契约，不再只是 workflow 说明书。

当前状态：可刷新进入技能目录。

## Skill 文件

图片 skill：
- `.library/custom/chinese-dreamcore-nutrition-image-workflow/SKILL.md`
- `assets/evidence-card-template.yaml`
- `assets/prompt-modules.yaml`
- `scripts/render_local_prototype.py`

视频 skill：
- `.library/custom/chinese-dreamcore-nutrition-video-workflow/SKILL.md`
- `assets/storyboard-template.yaml`

Kimi 报告：
- `work/chinese_dreamcore_nutrition_workflow_20260709/kimi_two_skills_authoring_report_20260709.md`

## 主身补改

师父补充要求：不是只把 workflow 写成文档，而是“我调用这个 skill 就可以生成图”。

因此主身补了：

1. 图片 skill 的“可调用生产契约”。
   - 调用时必须产出图片文件，或写清缺失的真实出图后端。
   - 若真实图像生成后端可用：生成 9 张无字底图、Cute Gate、排版，产出 `final.png`。
   - 若无真实图像后端但可先跑闭环：运行本地原型脚本，产出 `selected_base_prototype.png`，并明确标注“原型，不是真实图像模型结果”。
   - 若用户要求真实模型图但无后端：写 `BLOCKED.md`，不得假装已生成。

2. 视频 skill 的“可调用生产契约”。
   - 调用时必须产出 `final_1080x1920.mp4` / `preview_720p.mp4`，或写清缺失的视频合成/图生视频后端。
   - 若只有 ffmpeg/剪辑工具，可做轻动效 slideshow 原型，并明确标注“原型”。
   - 若无可执行后端，写 `BLOCKED.md`，不得只交“视频方案”冒充视频产物。

3. 图片 skill 增加本地兜底脚本：
   - `scripts/render_local_prototype.py`
   - 纯 Python 标准库，无外部依赖。
   - 用于无真实出图后端时生成一张中式梦核营养无字 PNG 原型图。

## 验证结果

官方 validator：PASS。

```text
image skill: ALL CHECKS PASSED
video skill: ALL CHECKS PASSED
```

行数：

```text
image SKILL.md: 445 lines
video SKILL.md: 478 lines
```

validator 有 NOTE：建议 `<300` 行时可拆 references；但两者均 `<500` 行，且当前内容主要是执行流程，暂不拆，避免调用时还要多跳一层。

安全扫描：PASS。

```text
safety_scan_hits=false
```

扫描未见：本机绝对路径、内部运行目录、分神运行号、Bearer/sk-/api_key/password 等泄漏形态。

本地原型脚本 smoke test：PASS。

```text
work/chinese_dreamcore_nutrition_runs/smoke_test_20260709/selected_base_prototype.png
bytes: 36758
```

## 边界

这两个 skill 能把调用转成生产动作，但 skill 本身不凭空增加外部图像/视频模型能力。

若真实图像生成后端已配置，它会走真实生成。
若没有，它会：

1. 对图片：可先产出本地 PNG 原型，明确标注原型。
2. 对视频：若有 ffmpeg/剪辑后端，可产出轻动效原型；若没有，写 `BLOCKED.md`。

不得把原型冒充真实 AI 生成图/视频。

## 下一步

1. `system.refresh` 让两个 custom skill 进入当前技能目录。
2. 用 `skills.info` 确认目录健康。
3. 向师父用微信报告：已做成可调用生产 skill；真实后端缺失时不冒充，会落 `BLOCKED.md` 或本地原型。

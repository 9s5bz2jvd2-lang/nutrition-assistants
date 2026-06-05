# 把「圆酱营养科普生产线」交给另一个灵台

## 方式 A：复制目录

把整个目录复制到目标灵台的 custom skill 目录：

```text
.library/custom/yuanjiang-nutrition-production-line/
```

目标灵台刷新后即可在 skill catalog 里看到：

```text
圆酱营养科普生产线
```

## 方式 B：发送 zip

把 `yuanjiang-nutrition-production-line-skill.zip` 解压到目标灵台：

```bash
unzip yuanjiang-nutrition-production-line-skill.zip -d <target-agent>/.library/custom/
```

确认解压后结构为：

```text
<target-agent>/.library/custom/yuanjiang-nutrition-production-line/SKILL.md
<target-agent>/.library/custom/yuanjiang-nutrition-production-line/assets/production-templates.md
<target-agent>/.library/custom/yuanjiang-nutrition-production-line/assets/role-briefs.md
<target-agent>/.library/custom/yuanjiang-nutrition-production-line/assets/handoff.md
<target-agent>/.library/custom/yuanjiang-nutrition-production-line/README.md
```

## 目标灵台使用前检查

1. 是否有图片/视频/音频生成工具？有则可以直接产出媒体文件；无则输出 prompt/分镜/口播稿。
2. 是否能访问用户提供资料或网页？不能则先向用户要资料。
3. 是否有微信/Telegram/邮件等人类沟通渠道？按原渠道回复。
4. 是否已经读本 skill 的 `SKILL.md`？不要只读 README。
5. 是否明确“不编造、不越证据、不跳医学红线”？

## 最小启动口令

可以对目标灵台说：

> 请读取并使用 custom skill「圆酱营养科普生产线」。以后我给你营养/食品安全/标准/论文资料时，先做证据拆解卡，再按需要调用分身生成正文、海报、图片、视频、音频和素材包；有媒体生成工具就直接生成文件，没有工具就输出 prompt/分镜/口播稿。所有强结论必须可追溯，不要编造论文/指南/年份/数据。

## 注意

本 skill 是流程，不是事实库。具体疾病/指南事实仍要查对应资料或疾病食养 skill。

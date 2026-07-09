# 中式梦核营养图片/视频双 Skill 编写报告

**编写时间**：2026-07-09
**编写者**：Kimi 分神（LingTai daemon）
**任务**：把既有图片/视频 workflow 沉淀为两个 LingTai custom skill，并验证。

---

## 1. 创建的文件

### 1.1 图片 Skill

- `.library/custom/chinese-dreamcore-nutrition-image-workflow/SKILL.md`
- `.library/custom/chinese-dreamcore-nutrition-image-workflow/assets/evidence-card-template.yaml`
- `.library/custom/chinese-dreamcore-nutrition-image-workflow/assets/prompt-modules.yaml`

### 1.2 视频 Skill

- `.library/custom/chinese-dreamcore-nutrition-video-workflow/SKILL.md`
- `.library/custom/chinese-dreamcore-nutrition-video-workflow/assets/storyboard-template.yaml`

### 1.3 本报告

- `work/chinese_dreamcore_nutrition_workflow_20260709/kimi_two_skills_authoring_report_20260709.md`

---

## 2. 验证结果

### 2.1 结构验证

使用官方脚本验证：

```bash
python3 .library/intrinsic/capabilities/skills/scripts/validate.py .library/custom/chinese-dreamcore-nutrition-image-workflow --require-last-changed-at
python3 .library/intrinsic/capabilities/skills/scripts/validate.py .library/custom/chinese-dreamcore-nutrition-video-workflow --require-last-changed-at
```

结果：**两个 skill 均 PASS。**

- Frontmatter：包含 `name`、`description`、`version`、`tags`、`last_changed_at`。
- Directory structure：所有在 `SKILL.md` 中提到的 `assets/...` 文件均已创建，无 broken reference。

脚本给出 NOTE：两个 SKILL.md 都超过 300 行（分别为 400 行、445 行），建议考虑移到 `references/`。由于任务要求“尽量控制 SKILL.md 不超过 500 行”，当前仍在 500 行以内，且内容主要是可执行流程步骤，因此保留在 SKILL.md 中，未做过度拆分。

### 2.2 Quick self-test

| 检查项 | 结果 |
|---|---|
| frontmatter 字段齐全 | PASS（name/description/version/tags/last_changed_at） |
| 路径存在 | PASS（两个 skill 文件夹及 assets 均已创建） |
| 无 [UPPERCASE] placeholder | PASS |
| 无 `.lingtai`/绝对本机路径泄漏 | PASS（只在“安全复查”清单里以否定形式出现 `.lingtai`，非泄漏） |
| 无 token/secret 字样 | PASS（只在验收清单里以否定形式出现） |
| 没有把苹果硬编码成唯一主题 | PASS（ explicitly 标注“仅示例，非唯一主题”，且说明任何普通日常食物均可） |

---

## 3. 主要设计取舍

### 3.1 内容组织

- **用中文写主体，术语保留英文**：流程、门、检查表、示例都用中文；prompt 模块、negative prompt、技术工具名保留英文，便于直接喂给图像/视频模型。
- **可执行流程而非概念散文**：每节都是“做什么、按什么顺序、通过标准、失败怎么办”，避免口号。
- **硬门前置**：把“中式梦核 + 营养科普 + 可爱温柔”作为第一层共同标准，图片/视频 skill 分别继承。

### 3.2 与原材料的关系

- 图片 skill 覆盖了原材料 `image_generation_workflow_v0.1_20260709.md` 的完整流水线：证据卡 → prompt 模块 → 9 张无字底图 → 硬淘汰 → Cute Gate → 中文排版 → 复查 → final.png。
- 视频 skill 覆盖了原材料 `video_generation_workflow_v0.1_20260709.md` 的完整流水线，并明确基于图片 skill 的 approved base images。
- 苹果主题示例只作为“示例”出现在第 16 节，且明确标注“非唯一主题”，没有把苹果写死。

### 3.3 营养事实边界

- 两个 skill 都明确：**不负责生成/核验营养事实**。
- 所有营养话术必须来自主题证据卡、权威来源或营养相关 skill。
- 禁止编造指南、论文、年份、机构；禁止疗效/减肥承诺；待核内容只能做内部草稿。

### 3.4 MVP 优先

- 视频 skill 强调先 **15 秒 / 5 镜头 MVP**，轻动效优先，图生视频微动效次之，不一开始就用复杂视频模型。
- 图片 skill 强调先 **9 张无字底图 + Cute Gate**， cute 不到 4 分不排版。

### 3.5 交付与验收

- 两个 skill 都给出了：停止条件、失败层修复表、交付物清单、验收门（checkbox）。
- 图片 skill 验收门 8 项，视频 skill 验收门 8 项。

### 3.6 assets 设计

只建了最必要的模板文件：

- 图片：证据卡模板 + prompt 模块库。
- 视频：分镜表模板。

没有过度拆分，避免给主身增加维护负担。

---

## 4. 主身需要复查的点

1. **营养事实表述**：skill 中所有营养示例（如“早餐蛋白质”“苹果”）是否保守、是否来自已核来源，需要主身逐句确认。
2. **苹果示例的边界**：虽然已明确标注“仅示例，非唯一主题”，但主身应确认是否接受把苹果示例留在 skill 中，还是移到外部 references/。
3. **SKILL.md 长度**：当前 400/445 行， validator 建议 <300 行。主身可决定是否把第 16 节示例或部分模块表拆到 `references/`。
4. **触发词与 description**：description 已尽量 trigger-friendly，主身可在实际使用时测试是否被正确触发。
5. **不刷新 agent**：按任务要求，本次没有执行 system.refresh；主身复查后自行决定是否刷新。
6. **不发布到 GitHub**：所有文件仅存放在 `.library/custom/` 和 `work/` 下，未做 git 提交或 push。

---

## 5. 结论

两个 LingTai custom skill 已按任务要求完成创建与验证，验证结果 PASS，self-test 通过，未触碰安全/凭证/外部发布红线，等待主身复查。

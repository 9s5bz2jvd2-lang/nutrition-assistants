# 圆酱的营养师膳食评价助手skill

[English README](README.en.md)


**中文署名：王润圆 + 灵台AI 制作**  
**English attribution: Created by Runyuan Wang + LingTai AI**

## 作者 / Author

**王润圆**  
昆明医科大学营养与食品卫生学硕士（已毕业）；中国注册营养师；天文爱好者；科普临时工。

**Runyuan Wang**  
M.Sc. in Nutrition and Food Hygiene, Kunming Medical University; Chinese Registered Dietitian; astronomy enthusiast; popular-science contributor.

**联合制作 / Co-created with:** 灵台AI（LingTai AI）

正在学习使用 AI 科普营养，求各位大佬指点，求星星。  
I am learning to use AI for nutrition science communication. Feedback, suggestions, and GitHub stars are very welcome.

> 面向营养师/营养团队的三日膳食记录评价助手：把客户零散的饮食打卡、聊天记录、表格或语音转文字整理为可复盘、可沟通、可作图的专业分析材料。

## 这个 skill 能输出什么

1. 客户三日饮食结构化表
2. 记录完整度与追问清单
3. 每日饮食模式分析
4. 热量与三大宏量营养素趋势粗估
5. DRIs 2023 差距评估（资料足够且参考值已核验时）
6. B-limited 食物成分查表：当有“食物 + 可食部克数”时，可计算能量、蛋白质、脂肪、碳水、膳食纤维、维A、B1、B2、烟酸、维E、钠、钙、铁、维C、胆固醇
7. 主要饮食问题与风险分级
8. 营养师内部分析总结
9. 可执行干预建议
10. 可转述给客户的话术
11. 趋势图数据与作图建议
12. 可视化 brief（用于长图、PPT、客户报告等）

## 定位

本项目默认使用者是**营养师、临床营养师、健康管理师或营养团队成员**。客户/来访者是分析对象，不是默认操作者。

- 内部层：给营养师看的结构化表、置信度、证据边界、DRIs 差距、风险分级、追问清单、干预优先级。
- 客户层：由营养师筛选后可转述给客户的温和话术、趋势图图注和 1–3 个小行动。
- 禁止口径：不要把输出写成普通人自助诊断、自助治疗或自助极端减重方案；不要绕过营养师直接给客户下医学/临床结论。

## 文件结构

- `SKILL.md`：skill 主体说明。
- `assets/analysis-template.md`：营养师版输出模板。
- `assets/user-context-template.md`：客户画像与个性化约束模板。
- `assets/trend-chart-data-template.csv`：趋势图数据表模板。
- `assets/visual-brief-template.md`：可视化 brief 模板。
- `assets/dri2023-*.csv`：DRIs 2023 相关模板/草案数据。
- `assets/food-composition-data/`：B-limited 食物成分查表数据与来源清单。
- `reference/food-composition-data/`：食物成分表原文对照、全网交叉验证、查表换算规则。
- `reference/`：计算设计、来源分层、外部参考融合记录。

## 重要说明

- 当前内置 DRIs 成人核心值为 `verified_draft` 草案，来自公开资料抽取后整理，仍需人工二次校对；不可当作最终权威全集。
- DRIs 2023 是“参考摄入量”对照，不是食物营养成分数据库；当前已额外接入一份 B-limited 食物成分表数据，但该数据经交叉验证高度推断为 1991 版《中国食物成分表》子集/简表抄录，非 2018 标准版第 6 版、非现行官方完整数据库。

- 当前 B-limited 食物成分数据可用于 demo / 营养师内部粗估：能计算能量、蛋白质、脂肪、碳水、膳食纤维、维A、B1、B2、烟酸、维E、钠、钙、铁、维C、胆固醇。
- 当前 B-limited 食物成分数据不覆盖钾、磷、镁、锌、硒、铜、锰、碘、氟等多数常量/微量元素；如需完整计算，应接入合规的《中国食物成分表 标准版 第6版》等来源。
- 低置信度饮食记录不应被包装成精确营养计算。
- 本 skill 不替代营养师专业判断、临床诊断或个体化治疗处方。

## 隐私与数据边界

- 请勿把客户姓名、手机号、住址、身份证号、完整病历号等可识别个人信息直接放入公开样例或公开 issue。
- 分享案例、截图或报告前，应先做脱敏处理。
- 涉及儿童、孕产妇、老年人、慢病、用药、术后、肿瘤治疗、进食障碍等情况时，应由专业人员复核，不应仅依赖 AI 输出。

## License

MIT

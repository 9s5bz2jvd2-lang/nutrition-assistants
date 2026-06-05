# 中国食物成分表 PDF 数据接入说明（2026-05-28）

本目录记录圆酱提供的腾讯文档 PDF《中国食物成分表》提取与接入边界。

## 结论先行

- PDF 来源：`https://docs.qq.com/pdf/DRkJFSkhPbnJIeHdk`，完整下载 2,062,728 bytes，共 96 页。
- 原文对照：Section A（pages 1–23 + 24–46）已抽取为 1,284 条食物主表记录；左右半表按行号对齐，抽样截图对照通过。
- 全网交叉验证：通过大黄米/大麦等数值、条目数、旧版类别码体系等线索，**高度推断这份 PDF 是 1991 版《中国食物成分表》的子集/简表抄录**，不是 2018 标准版第 6 版，也不是现行官方完整电子数据库。
- 使用定位：可作为 **B-limited 查表计算 / demo 数据源**，但不得用于对外宣称“最新版”“官方完整”“临床唯一依据”。

## 已接入数据文件

主用文件（保持原有路径，供 skill 3B 调用）：

- `assets/food-composition-data/china_food_composition_pdf_section_a_validated_20260528.csv`
- `assets/food-composition-data/china_food_composition_pdf_section_a_validated_20260528.jsonl`

辅助规范化文件（Claude Code 分神生成，便于后续程序化查表/模糊匹配）：

- `assets/food-composition-data/cn_food_composition_1991_v0.csv`
- `assets/food-composition-data/cn_food_composition_1991_v0.jsonl`
- `assets/food-composition-data/source_manifest.json`
- `assets/food-composition-data/category_code_map_1991_draft.csv`
- `assets/food-composition-data/standard_weight_table.csv`（PDF 附带标准体重表；与食物成分主表不是同一用途）

## 能计算的字段

每 100g 可食部：能量、水分、蛋白质、脂肪、膳食纤维、碳水化合物、维生素A、维生素B1、维生素B2、烟酸、维生素E、钠、钙、铁、维生素C、胆固醇。

## 不能声称完整覆盖的字段

本 PDF 不含或未可靠覆盖：钾、磷、镁、锌、硒、铜、锰、碘、氟等多数常量/微量元素，也不含完整维生素谱。需要《中国食物成分表 标准版 第6版》等更完整、合规来源后再升级。

## 使用边界

- 必须标注数据版本：**推断为 1991 版子集/简表抄录，来源为腾讯文档分享 PDF，非官方电子版，非 2018 第6版。**
- 可用于 B-limited 查表计算，不可宣称为最新版官方完整数据库。
- 输出必须带数据来源、版本推断、字段缺口和置信度。
- 类别码（如 11/21/31）属于旧版编码体系的草案映射，见 `category_code_map_1991_draft.csv`，待圆酱对照完整表确认；不要把旧类别码直接与 2015/2018 新编码体系混合。
- 不同版本食物成分表不得混算；若未来接入第6版，应作为独立数据源替换或显式选择。

详见：

- `validation_report.md`：原文截图/抽样对照与抽取质量。
- `web_crosscheck.md`：全网交叉验证与版本推断。
- `lookup-and-calculation.md`：一餐查表与换算规则。

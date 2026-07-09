# Prompt used — apple nutrition skill trial

## Run mode

- Skill: `chinese-dreamcore-nutrition-image-workflow`
- Topic: 苹果的营养 / apple_nutrition
- Output folder: `work/chinese_dreamcore_nutrition_runs/gpt_skill_trial_apple_20260709/`
- Backend route: no real image-generation MCP / CLI / local model was registered or identified in this daemon run; per skill contract and parent instruction, used local fallback prototype renderer.
- Result type: **原型，不是真实图像模型结果**.
- Generated PNG: `selected_base_prototype.png`

## Local fallback command actually run

```bash
python3 .library/custom/chinese-dreamcore-nutrition-image-workflow/scripts/render_local_prototype.py \
  --topic-id apple_nutrition \
  --title '一只苹果的温柔营养' \
  --outdir work/chinese_dreamcore_nutrition_runs/gpt_skill_trial_apple_20260709
```

## Intended no-text base-image prompt if a real backend is later configured

Create a vertical 4:5 nutrition education poster background with NO text.

Cute-first visual priority:
A round fresh apple with natural red and pale yellow skin, placed gently on a small white porcelain plate. The apple should feel soft, friendly, and ordinary, not magical.

Chinese everyday dream setting:
An old Chinese home interior with a moon gate window in the background, bamboo curtain, warm wooden table, white porcelain, soft moon-white morning light, faint rice-paper texture, clean air, quiet and safe.

Composition:
Place the apple and plate in the lower right. Leave large clean blank space in the upper left for later Chinese title and short nutrition notes.

Color and texture:
warm cream, moon white, pale apricot, soft jade green; low saturation, no neon, no harsh contrast. Soft watercolor texture, gentle semi-realistic illustration, high detail but not photorealistic advertising.

Nutrition boundary:
Use only ordinary everyday food props. Do not imply medical treatment, weight-loss promise, detox effect, disease prevention, or specific nutrition advice.

Strict negative prompt:
no text, no letters, no logo, no watermark, no fake labels, no fake references, no horror, no abandoned hallway, no infinite corridor, no eyes staring at viewer, no hospital, no medicine, no syringe, no pills, no before-after body comparison, no anime girl, no chibi character, no childish toy advertisement, no religious / feng-shui / fantasy symbols, no luxury marketing poster, no cheap commercial ad.

## Production notes

The local renderer does not use this prompt as a generative-model prompt; it procedurally draws a soft no-text apple poster prototype so the workflow can produce a tangible file. A real image backend should generate 9 candidates, then Cute Gate should select one before typography.

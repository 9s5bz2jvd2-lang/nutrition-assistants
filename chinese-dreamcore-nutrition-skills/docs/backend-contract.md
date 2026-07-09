# Backend Contract｜图像/视频后端契约

## Image backend

A real image backend should accept:

```json
{
  "topic_id": "apple_nutrition",
  "prompt": "English no-text image prompt...",
  "aspect_ratio": "4:5",
  "output_dir": "...",
  "count": 9,
  "no_text": true
}
```

It should return PNG files and a manifest such as:

```json
{
  "backend": "your-backend-name",
  "outputs": ["base_01.png", "base_02.png"],
  "notes": "No Chinese text was generated."
}
```

Minimum quality gate:

- no Chinese body text inside model output
- no watermark or logo
- no horror, uncanny eye-gaze, medical fear, or cheap advertising style
- enough blank space for later Chinese layout
- the food subject remains recognizable

## Video backend

A real video backend should accept:

```json
{
  "topic_id": "apple_nutrition_video",
  "base_images": ["selected_base.png"],
  "storyboard": "storyboard.json",
  "duration_seconds": 15,
  "output_dir": "..."
}
```

It should return MP4 previews/finals and a manifest.

Minimum quality gate:

- no new nutrition facts invented by motion, caption, voice, or generated text
- no horror/liminal drift
- captions and voiceover match the evidence card
- output path and render settings are recorded

## Missing backend behavior

If no backend is available, the executor must write `BLOCKED.md` or produce an explicitly labeled local prototype. Never present a prototype as a real model output.

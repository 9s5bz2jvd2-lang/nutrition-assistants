# Chinese Dreamcore Nutrition Image & Video Skills

This folder contains two callable LingTai custom skills for producing cute-first Chinese dreamcore nutrition media.

They define a production contract: when invoked, the executor must either produce concrete files or explicitly state which real backend is missing. A written plan must not be presented as a finished image or video.

## Contents

- `skills/chinese-dreamcore-nutrition-image-workflow/` — image production skill: evidence card, no-text prompts, hard veto checks, Cute Gate scoring, Chinese post-layout, final review, and fallback prototype handling.
- `skills/chinese-dreamcore-nutrition-video-workflow/` — short-video production skill: storyboard, light motion/video backend routing, captions/voice/BGM, render checks, and `BLOCKED.md` behavior when no backend is available.
- `trial_runs/gpt_skill_trial_apple_20260709/` — a GPT sub-agent apple-nutrition trial. The PNG is a local fallback prototype, not a real image-model output.
- `reports/` — authoring and review notes.

## Safety boundaries

1. Nutrition claims must trace back to an evidence card.
2. Do not invent guidelines, papers, years, institutions, or therapeutic promises.
3. Do not let image/video models generate Chinese body text directly; add Chinese text during post-layout.
4. Local prototypes may validate the workflow, but must not be presented as real AI-generated images.
5. If image/video backends are missing, write the blocker clearly instead of pretending the media product exists.

## Real generation requirement

A real production run needs a callable image/video backend: for example, an image-generation MCP, a local ComfyUI/SDXL/Flux workflow, or a stable external CLI/API. The backend should support English prompts, 4:5 no-text PNG output, batch candidate generation, and downstream Cute Gate scoring plus Chinese layout.

## General portability

- General use guide: [`GENERAL_USE.md`](GENERAL_USE.md)
- Backend contract: [`docs/backend-contract.md`](docs/backend-contract.md)

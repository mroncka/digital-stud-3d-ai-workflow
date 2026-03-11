# 3D + AI Character Workflow

> Replication of the [BankruptKyun workflow](https://www.reddit.com/r/StableDiffusion/comments/1puszuc/) — merging 3D model poses with AI image/video generation for anime-style hyperrealistic character output.

## Overview

This workflow bridges **traditional 3D modeling** with **AI image/video generation** to produce high-quality, consistent character outputs. The key insight: instead of wrestling with prompts for pose/anatomy, you feed 3D renders directly as reference — the AI "skins" your model with realism.

**Stack:**
- **3D Posing:** Blender / DAZ Studio / Poser / Web3D tools
- **Image Generation:** ComfyUI + Qwen + Flux
- **LoRA Training:** Custom anime-style + character-specific LoRAs
- **Video Generation:** ComfyUI + Wan2.2 (experimental)
- **Video Enhancement:** FlashVSR (4x upscale), GIMM-VFI (motion interpolation)
- **Rendering:** Cloud GPU (VastAI / RunPod)

## Pipeline

```
3D Model → [STAGE 1] Pose & Render → [STAGE 2] Image Generation
         → [STAGE 3] Face Refinement → [STAGE 4] Video Generation
         → [STAGE 5] Video Assembly
```

### Stage 1: Pose & Render
- Tool: Blender / DAZ Studio / Web3D posing sites
- Output: Neutral-background render (pose reference)
- Keep background neutral/clean; export depth maps for precision

### Stage 2: Image Generation
- Tool: ComfyUI + Qwen + Flux
- 3D render as pose reference (replaces ControlNet in many cases)
- Run 20–100+ iterations, cherry-pick best results

### Stage 3: Face & Detail Refinement
- Tool: ComfyUI inpainting / face restoration nodes
- Regenerate face and clothing regions independently
- Most iteration-heavy step

### Stage 4: Video Generation (Experimental)
- Tool: ComfyUI + Wan2.2
- Expect 10–50 failed renders per usable ~6s clip
- Light2x LoRA reduces steps needed

### Stage 5: Video Assembly
- Stitch 6s clips; hide cuts cinematically
- Enhancement: FlashVSR 4x → GIMM-VFI motion interpolation

## Key Principles

1. **3D model = pose skeleton.** AI skins it. Clean geometry + neutral background.
2. **Quality > Quantity.** 50–100 iterations for one good frame is normal.
3. **LoRA is your style fingerprint.** Train on your own renders.
4. **Video is hard.** 6-second clips stitched well > 30-second garbage.
5. **Budget:** ~$50–$200/month cloud GPU. Local only worth it if 24GB+ VRAM.

## Hardware

- **Minimum viable:** RTX 3060 12GB (image gen fine; video gen slow)
- **Sweet spot:** RTX 3090 24GB (runs Wan2.2 fully)
- **Original creator's setup:** Titan X Maxwell → all video done on cloud

## Resources

- [BankruptKyun original post](https://www.reddit.com/r/StableDiffusion/comments/1puszuc/)
- [Workflow clarification post](https://www.reddit.com/r/StableDiffusion/comments/1pwlt52/)
- [AI is in Wonderland (YouTube)](https://www.youtube.com/@ai_is_in_wonderland) — primary tutorial inspiration
- [3D + AI skin example (YouTube)](https://youtu.be/67t-AWeY9ys) — 90% of the workflow
- [Wan2.2 animate from 3D model](https://www.reddit.com/r/comfyui/comments/1ojbuyt/)
- [PoseMyArt](https://posemy.art/app/) — web-based 3D posing

## Folder Structure

```
├── README.md
├── comfyui/
│   ├── workflows/README.md     # Workflow node chain specs
│   └── custom_nodes.md         # Required custom nodes list
├── lora/README.md              # LoRA training guide + Kohya config
├── 3d/
│   ├── daz_workflow.md         # DAZ Studio posing workflow
│   ├── blender_workflow.md     # Blender posing + depth export
│   └── web_posing_tools.md     # Free web-based posing alternatives
├── video/assembly_guide.md     # Clip stitching + cut-hiding techniques
└── cloud/gpu_rental_guide.md   # VastAI / RunPod setup + cost breakdown
```

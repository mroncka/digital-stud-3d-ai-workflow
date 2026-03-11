# Image & Video Generation SOTA

> Auto-updated every 30 minutes by the digital-stud research pipeline.
> Last updated: 2026-03-11 21:30 (Prague / CET) | Run #1

---

## 🏆 Image Generation SOTA — March 2026

### Top Models by Category

| Category | Model | API Access | Cost | Notes |
|----------|-------|------------|------|-------|
| **Overall SOTA** | Nano Banana 2 (Gemini 3.1 Flash Image) | Gemini API | ~$0.03/img | #1 Chatbot Arena at 1280 Elo, character consistency, text rendering |
| **Photorealism** | Flux 2 Flex | fal.ai, Replicate | ~$0.03/img | Gold standard for skin, lighting, anatomy |
| **Photorealism (fast)** | Flux 2 Klein (9B) | fal.ai, Replicate | ~$0.02/img | Faster, native editing, inpainting |
| **Open Source / NSFW** | Flux Dev / Flux 2 Schnell | Local + Replicate | $0.025/img | Best open-weight for adult content |
| **Anime/Illustrative** | Illustrious XL / NoobAI XL | Local (CivitAI) | Free (local) | NoobAI Chenkin RF = latest, best contrast |
| **Anime + LoRA ecosystem** | Pony Diffusion V6 XL | Local (CivitAI) | Free (local) | Massive LoRA ecosystem, tag-based control |
| **Ultra-cheap + open** | Z Image Turbo (Qwen) | HF Inference, fal.ai | ~$0.004/img | 6B params, Apache 2.0, 16GB VRAM, 3s gen |
| **Logos / Design** | Recraft V4 | fal.ai, Recraft API | ~$0.075/img | #1 HF benchmark for vectors/logos, SVG export |
| **Text in image** | Seedream 5.0 Lite (ByteDance) | fal.ai | TBC | Best Chinese/multilingual text rendering |

### Flux 2 Family — Full Breakdown

- **Flux 2 Flex** — Full-featured photorealism, LoRA support, image editing. ~$0.03/image.
- **Flux 2 Klein (9B)** — Smaller/faster variant, native inpainting, editing. ~$0.02/image.
- **Flux Kontext** — Advanced context-aware image editing. ~$0.04/image.
- **Flux 2 Schnell** — Open-source, fast previews (4 steps), free to run locally.
- All available on: fal.ai, Replicate, Microsoft Azure AI Foundry.

### Free / Zero-Cost Image Gen Options

1. **HuggingFace ZeroGPU Spaces** (H200, ~25 min/day free GPU)
   - Flux Dev, Z Image Turbo, NoobAI, Illustrious all have active ZeroGPU Spaces
   - Best for testing; not for production volume
2. **Google AI Studio** — Nano Banana 2 free tier (rate-limited)
3. **Replicate free trial credits** — enough for testing Flux/SDXL variants
4. **fal.ai signup credits** — includes Flux, Seedream, video models
5. **Local ComfyUI** — Flux Schnell/Dev on RTX 3090 (24GB) runs well

### Noteworthy New Entrants (2025–2026)

- **GLM-Image** (Jan 2026, Zhipu AI) — First open-source industrial-grade autoregressive (non-diffusion) image model
- **Seedream 5.0 Lite** (Feb 2026, ByteDance) — "Deeper thinking" architecture, superior multilingual text, in-image translation
- **Z Image Turbo** (Nov 2025, Alibaba Qwen) — S3-DiT architecture, 6B params, 10-20x cheaper than DALL-E 3, Apache 2.0
- **FireRed-Image-Edit 1.1** — New open-source SOTA for image editing, beats Qwen edit
- **Recraft V4** — Now in ComfyUI via custom node

---

## 🎬 Video Generation SOTA — March 2026

### Top Models by Category

| Category | Model | Params | VRAM | API/Local | Notes |
|----------|-------|--------|------|-----------|-------|
| **Open Source Best** | Wan2.2 TI2V-5B | 5B | 24GB (RTX 4090) | Local + Replicate | MoE architecture, 720P/24fps, Apache 2.0 |
| **Open Source Heavy** | HunyuanVideo (original) | 13B | 60-80GB | Local (A100) | Beats Runway Gen-3, Luma 1.6 |
| **Open Source Lightweight** | HunyuanVideo 1.5 | 8.3B | 14GB | Local + fal.ai | SSTA attention, 1.87x faster, 1080p upscale |
| **Commercial Best Quality** | Kling 2.5 / 3.0 | — | API only | Kling API, fal.ai | Best character consistency, multi-angle |
| **Budget Commercial** | Kling 2.1 | — | API only | Kling API | ~$0.14/clip, solid quality |
| **Open Mid-tier** | CogVideoX-1.5 | 5B | 12-16GB | Local + HF | 1360×768, LoRA support, DDIM Inverse editing |
| **Free via Colab** | CogVideoX 5B | 5B | T4 (Colab) | Google Colab | 6s clips, 720×480, 8fps |
| **Real-time / distilled** | CAUSVID / NVIDIA FastGen | — | — | Local research | 4-step causal generator (CVPR 2025) |
| **Long-form realtime** | Helios (Wan-based) | 14B | H100 | Research | 19.5 FPS on H100, minute-scale videos |
| **Speech-driven** | Wan2.2-S2V | — | — | Local | Audio-driven character animation |

### Wan2.2 — Priority Model for This Workflow

- **Architecture**: World's first open-source MoE video generation model
- **TI2V-5B variant**: Unified text+image input → video, 720P/24fps, runs on RTX 4090
- **Key extensions**:
  - `Wan2.2-Animate`: Character animation from reference image + motion video
  - `Wan2.2-S2V`: Speech-to-video with audio-driven generation
  - `FLF2V`: First/Last Frame interpolation workflow
- **ComfyUI**: Official native workflow available at [docs.comfy.org](https://docs.comfy.org/tutorials/video/wan/wan2_2)
- **License**: Apache 2.0 (commercial use OK)

### HunyuanVideo 1.5 — Best Lightweight Open Option

- 8.3B params, 14GB VRAM (vs 60-80GB for full HunyuanVideo)
- SSTA (Selective & Sliding Tile Attention): 1.87x speedup vs FlashAttention-3
- Super-resolution to 1080p built in
- CFG-distilled models for additional 2x speedup
- Available: fal.ai, local (Linux; WSL2 on Windows)

### CAUSVID / Distillation Speedups

- CVPR 2025: Distills 50-step bidirectional diffusion → 4-step causal generator
- NVIDIA FastGen: Open-source library unifying distillation techniques
- `Diagonal Distillation` (arxiv 2603.09488): New streaming autoregressive approach (March 2026)
- Result: Real-time or near-real-time video generation becoming feasible

### Video API Pricing (Feb/March 2026)

| Provider | Model | Price/sec | Free Tier |
|----------|-------|-----------|----------|
| Replicate | Wan 2.2 A14B (optimized) | ~$0.05/sec | Small credits |
| Replicate | Wan 2.6 / Grok | ~$0.05/sec | Small credits |
| fal.ai | HunyuanVideo 1.5 | TBC | Signup credits |
| fal.ai | Kling 2.1 | ~$0.14/5s clip | Signup credits |
| RunwayML | Gen-3 Alpha | ~$0.75/sec | 125 free credits |
| WaveSpeedAI | 700+ models unified API | Varies | Free trial |

### Best img2vid Workflow (Community Consensus, Feb-March 2026)

1. **Wan2.2 TI2V-5B in ComfyUI** — Best overall control, official template available
2. **LTX-2 I2V** — Better lip sync, audio integration, faster than Wan
3. **HunyuanVideo 1.5** — Best open quality if you have 14GB+ VRAM
4. **Kling 2.1 API** — Best commercial option if local GPU unavailable

---

## 🧠 LoRA Training SOTA — March 2026

| Method | Tool | Notes |
|--------|------|-------|
| **Best overall** | AI-Toolkit (ostris) | Simplest Flux LoRA, great defaults |
| **Full control** | Kohya SS (sd-scripts, Flux branch) | network_dim 32, bf16, most flexible |
| **Face/identity retention** | X-Flux finetuning | Best for character identity |
| **Hosted fast** | fal.ai Flux LoRA Fast Training | ~$2-5 per LoRA, no GPU needed |
| **Hosted (Replicate)** | Replicate Fine-tune Flux | One-line API call |
| **Video LoRA** | finetrainers (CogVideoX factory) | CogVideoX and Mochi video LoRA |

---

## ⚡ Free GPU Options — March 2026

| Option | GPU | Cost | Best For |
|--------|-----|------|----------|
| **VastAI** | RTX 3090 (24GB) | ~$0.45/hr | ComfyUI workflows, no content policy |
| **RunPod** | Various | ~$0.50-2/hr | Persistent volumes, ComfyUI templates |
| **HF ZeroGPU** | H200 | Free (25 min/day) | Testing models, not production |
| **Google Colab** | T4 (free) / A100 (Pro) | Free / $10/mo | LoRA training, CogVideoX inference |
| **E2B** | Sandboxed | Usage-based | Code execution, API testing |

---

## 🔧 ComfyUI Ecosystem — Notable Nodes/Updates (March 2026)

- **ComfyUI Native Wan2.2 support** — Official workflow templates in ComfyUI menu
- **Recraft V4 ComfyUI node** — [blog.comfy.org](https://blog.comfy.org/p/recraft-v4-now-available-in-comfyui)
- **IP-Adapter** — Still the standard for style/face transfer; updated for Flux
- **ComfyUI-Manager** — Essential for node/model management
- **ControlNet** — Flux ControlNet nodes available (pose, depth, canny)
- **Wan2.2-Animate node** — Animate reference image with motion video input
- **FLF2V (First/Last Frame to Video)** — Interpolation between two keyframe images

---

## 🔌 Key APIs Summary

| Platform | Speciality | Free Tier | URL |
|----------|-----------|-----------|-----|
| fal.ai | Fastest inference, 1000+ models | Signup credits | https://fal.ai |
| Replicate | Largest open-source library | Small trial credits | https://replicate.com |
| Together AI | Open model hosting | $5 signup credit | https://together.ai |
| HF Inference API | Community models, serverless | Free (rate-limited) | https://huggingface.co |
| WaveSpeedAI | 700+ models unified API | Free trial | https://wavespeed.ai |
| Gemini API | Nano Banana 2 image gen | Free tier | https://ai.google.dev |

---

*Next update: 30 minutes. This file is machine-generated by the digital-stud SOTA pipeline.*

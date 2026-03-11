# Image & Video Generation SOTA

> Auto-updated every 30 minutes by the digital-stud research pipeline.
> Last updated: 2026-03-12 00:03 (Prague / CET) | Run #6

---

## 🖼️ Image Generation SOTA — March 2026

### Top Models by Category

| Category | Model | API Access | Cost | Notes |
|----------|-------|------------|------|-------|
| **Overall SOTA** | Nano Banana 2 (Gemini 3.1 Flash Image) | Gemini API, Google AI Studio | ~$0.03/img | #1 Chatbot Arena 1280 Elo; **4K native output**; real-time web grounding; reliable text rendering; character consistency up to 5 chars |
| **Photorealism** | Flux 2 Flex | fal.ai, Replicate | ~$0.03/img | Gold standard for skin, lighting, anatomy |
| **Photorealism (fast)** | Flux 2 Klein (9B) | fal.ai, Replicate | ~$0.02/img | Faster, native editing, inpainting; **Klein consistency LoRA released March 2026** |
| **Open Source / NSFW** | Flux Dev / Flux 2 Schnell | Local + Replicate | $0.025/img | Best open-weight; Schnell free via HF/SiliconFlow/Firework AI |
| **Anime/Illustrative** | Illustrious XL / NoobAI XL | Local (CivitAI) | Free (local) | NoobAI Chenkin RF = latest, best contrast |
| **Anime + LoRA ecosystem** | Pony Diffusion V6 XL | Local (CivitAI) | Free (local) | Massive LoRA ecosystem, tag-based control |
| **Ultra-cheap + open** | Z Image Turbo (Qwen) | HF Inference, fal.ai | ~$0.004/img | 6B params, Apache 2.0, 16GB VRAM, 3s gen |
| **Logos / Design** | Recraft V4 | fal.ai, Recraft API | ~$0.075/img | #1 HF benchmark for vectors/logos, SVG export; ComfyUI node available |
| **Text in image** | Seedream 5.0 Lite (ByteDance) | fal.ai | TBC | Best Chinese/multilingual text rendering |
| **Budget API** | GPT Image 1 Mini | OpenAI API | ~$0.005/img | Cheapest frontier option |

### Nano Banana 2 — March 2026 Highlights

- **4K native output** (512px to 4K) — 4K is now standard, not premium
- **Real-time web grounding** via Google Search — current products/locations without stale data
- **Reliable text rendering** — readable text without manual Photoshop overlays
- **Ultra-wide aspect ratios** (4:1, 1:4, 8:1) for banners and cinematic formats
- Available free in Google AI Studio (rate-limited); also in Comfy Cloud free tier

### Flux 2 Family — Full Breakdown

- **Flux 2 Flex** — Full photorealism, LoRA support, image editing. ~$0.03/image.
- **Flux 2 Klein (9B)** — Faster variant, native inpainting, editing. ~$0.02/image. Klein consistency LoRA now available.
- **Flux Kontext** — Context-aware image editing. ~$0.04/image.
- **Flux 2 Schnell** — Open-source, 4-step, free via HF/SiliconFlow/Firework AI APIs.
- NVFP4 quantized models for Klein (4B and 9B): **2.5x faster, 60% lower VRAM** on RTX 50 Series.

### Free / Zero-Cost Image Gen Options

1. **HuggingFace ZeroGPU Spaces** (H200, ~25 min/day free GPU) — Flux Dev, Z Image Turbo, NoobAI, Illustrious
2. **Google AI Studio** — Nano Banana 2 free tier (rate-limited)
3. **Comfy Cloud free tier** (March 3, 2026) — 400 monthly credits, no credit card; 900+ models, 350+ templates
4. **SiliconFlow / Firework AI / HF Inference** — Flux Schnell free API
5. **Local ComfyUI** — Flux Schnell/Dev on RTX 3090 (24GB)

### Noteworthy New Entrants (2025–2026)

- **GLM-Image** (Jan 2026, Zhipu AI) — First open-source autoregressive (non-diffusion) image model
- **Seedream 5.0 Lite** (Feb 2026, ByteDance) — Superior multilingual text, in-image translation
- **Z Image Turbo** (Nov 2025, Alibaba Qwen) — S3-DiT, Apache 2.0, 10-20x cheaper than DALL-E 3
- **FireRed-Image-Edit 1.1** — Open-source SOTA for image editing, beats Qwen edit
- **Recraft V4** — Now in ComfyUI via custom node
- **Grok Imagine** (Mar 2026, xAI) — Four-agent architecture, 10s 720p video gen also available

---

## 🎬 Video Generation SOTA — March 2026

### Top Models by Category

| Category | Model | Params | VRAM | API/Local | Notes |
|----------|-------|--------|------|-----------|-------|
| **Open Source Best** | Wan2.2 TI2V-5B | 5B | 24GB (RTX 4090) | Local + Replicate | MoE, 720P/24fps, Apache 2.0 |
| **Open Source Heavy** | HunyuanVideo (original) | 13B | 60-80GB | Local (A100) | Beats Runway Gen-3, Luma 1.6 |
| **Open Source Lightweight** | HunyuanVideo 1.5 | 8.3B | 14GB | Local + fal.ai | SSTA attention, 1.87x faster, 1080p upscale |
| **Audio-Video (new)** | LTX-2.3 | — | — | Local (ComfyUI native) | 9:16 portrait, audio-video, better motion, NVFP4 support |
| **Commercial Best** | Kling 2.5 / 3.0 | — | API only | Kling API, fal.ai | Best character consistency, multi-angle |
| **Kling Motion Control** | Kling 3.0 MC | — | API only | ComfyUI native | **Motion Control 3.0 nodes live in ComfyUI (Mar 2026)** |
| **Budget Commercial** | Kling 2.1 | — | API only | Kling API | ~$0.14/clip |
| **Open Mid-tier** | CogVideoX-1.5 | 5B | 12-16GB | Local + HF | 1360×768, LoRA support, DDIM Inverse editing |
| **Free via Colab** | CogVideoX 5B | 5B | T4 (Colab) | Google Colab | 6s clips, 720×480, 8fps |
| **Real-time / distilled** | CAUSVID / NVIDIA FastGen | — | — | Local research | 4-step causal (CVPR 2025); Diagonal Distillation (arxiv 2603.09488) |
| **Long-form realtime** | Helios (Wan-based) | 14B | H100 | Research | 19.5 FPS on H100, minute-scale |
| **Speech-driven** | Wan2.2-S2V | — | — | Local | Audio-driven character animation |

### LTX-2.3 — New Addition (March 2026, Day-0 ComfyUI)

- **9:16 vertical portrait support** — ideal for social media
- Enhanced image-to-video with better motion consistency
- Cleaner audio, reduced noise, improved dialogue/music
- Better text rendering and prompt understanding
- New latent space & VAE for sharper textures
- **NVFP4 + FP8** quantized models: 1.7x faster, 40% VRAM reduction on RTX GPUs
- **IAMCCS nodes** enable 1080p on low-VRAM (4080-class) GPUs
- Official templates in ComfyUI menu

### Wan2.2 — Priority Model for This Workflow

- MoE architecture, TI2V-5B: unified text+image → video, 720P/24fps, RTX 4090
- **Memory optimization update (March 2026)**: improved efficiency; LoRAs from Wan2.1 still compatible
- Extensions: `Wan2.2-Animate`, `Wan2.2-S2V`, `FLF2V`
- [docs.comfy.org](https://docs.comfy.org/tutorials/video/wan/wan2_2) | Apache 2.0

### HunyuanVideo 1.5 — Best Lightweight Open Option

- 8.3B params, 14GB VRAM; SSTA (1.87x speedup); CFG-distilled (2x additional speedup); 1080p built-in

### Video API Pricing (March 2026)

| Provider | Model | Price/sec | Free Tier |
|----------|-------|-----------|-----------|
| Replicate | Wan 2.2 A14B | ~$0.05/sec | Small credits |
| fal.ai | HunyuanVideo 1.5 | TBC | Signup credits |
| fal.ai | Kling 2.1 | ~$0.14/5s clip | Signup credits |
| RunwayML | Gen-3 Alpha | ~$0.75/sec | 125 free credits |
| WaveSpeedAI | 700+ models | Varies | Free trial |

---

## 🧪 LoRA Training SOTA — March 2026

### Training Tools Comparison

| Tool | Best For | Notes |
|------|----------|-------|
| **Kohya SS / musubi-tuner** | Full control, all models | SD1.x, SDXL, SD3, Flux, HunyuanImage-2.1; LoRA/LoHa/LoKr |
| **AI-Toolkit (ostris)** | Flux LoRA, video LoRA | Simple config files, ZIT video LoRA; 80% defaults just work |
| **OneTrainer (Nerogar)** | Character/face LoRAs | Growing adoption; less overfitting than AI-Toolkit for characters |
| **SimpleTuner** | SDXL + Flux, attention masking | Experimental stability features, comprehensive docs |
| **fal.ai hosted** | Fast / no GPU | ~$2-5 per LoRA, API-based |
| **Replicate hosted** | Simple one-shot | One-line API call |
| **WaveSpeedAI** | Cloud training | Upload dataset, train FLUX/SDXL LoRA on cloud GPUs |

> **Klein consistency LoRA** (March 2026): New official consistency LoRA for Flux 2 Klein — improves character consistency across generations without full character LoRA training.

> **Community note:** OneTrainer gaining ground over AI-Toolkit for character LoRAs (significantly less overfitting). musubi-tuner preferred for newer Flux variants.

### Video LoRA — Updated March 2026

- **Video2LoRA** (arxiv 2603.08210): per-reference-video LoRA for semantic-controlled video gen
- **finetrainers** (CogVideoX factory): CogVideoX + Mochi video LoRA training
- **Flimmer** (**NEW March 2026**): Dedicated video LoRA toolkit for diffusion transformers — cleaner API than AI-Toolkit ZIT, supports Wan2.2 + HunyuanVideo; growing community adoption
- **AI-Toolkit ZIT**: Still viable for video LoRA; Flimmer emerging as preferred alternative

### Optimal Hyperparameters — Flux Dev Character LoRA

```
learning_rate: 1e-4 (range 3e-5 to 1e-4)
lora_rank: 128 (optimal); 32-64 (resource-constrained)
network_alpha: same as rank (1:1) or half
conv_dim: 8-16
steps: ~30,000
batch_size: 2-3 (16GB VRAM)
optimizer: Prodigy or Prodigy_adv (preferred); AdamW8bit (fallback)
mixed_precision: bf16
```

### Optimal Hyperparameters — SDXL Character LoRA

```
unet_lr: 5e-5
text_encoder_lr: 1e-5
lora_rank: 32
network_alpha: 16
conv_dim: 8
epochs: 15-25
noise_offset: 0.035-0.1
mixed_precision: fp16 or bf16
```

### Dataset Preparation Best Practices

- **Size**: 30-50 images for SDXL; 20-80 for Flux
- **Variety**: Front, 3/4, profile, expressions; full body + torso + face closeup
- **Resolution**: 768×768 min; 1024×1024 preferred
- **Captions**: LoraTag for auto-captioning (FLUX/SDXL/SD3); trigger word = rare 3-5 char + class (e.g. `zkw woman`)

### LyCORIS / Alternative Architectures

| Method | File Size | Use Case |
|--------|-----------|----------|
| **LoRA** | ~33-66MB | Standard; fast convergence |
| **LoKr** | ~few MB | Extremely compact; faster convergence; growing community interest |
| **LoHa** | Medium | Hadamard product; different parameter distribution |
| **GLoRA / GLoKR** | Varies | Generalized; more flexible parameter targeting |

---

## 📍 Pose Estimation SOTA — March 2026

### Model Comparison

| Model | Type | Keypoints | Speed | Best For |
|-------|------|-----------|-------|----------|
| **YOLO26-Pose** | Single-stage, NMS-free | 17 (COCO) + custom | 30+ FPS | Real-time multi-person, custom keypoints, **43% faster CPU than YOLO11-N** |
| **RTMPose** | Two-stage | 17-133 | 30+ FPS | Production speed/accuracy balance |
| **DWPose** | Two-stage whole-body | 133 (body+hand+face) | Medium | **Best for ComfyUI ControlNet** |
| **ViTPose / ViTPose++** | ViT-based | 17-133 | Slower | Research; highest mAP |
| **Sapiens2** | Foundation (0.4-5B) | 308 body + face | Slow | SOTA whole-body, 1K-4K, multi-task; ICLR 2026 |
| **MediaPipe Holistic** | Lightweight | 33+21/hand+468 face | 30+ FPS mobile | Mobile/browser |
| **SDPose-OOD** | Robust | 17+ | Medium | ComfyUI; robust out-of-distribution |

> **YOLO26-Pose key upgrade (Jan 2026)**: NMS-free end-to-end inference, non-human keypoint support for custom schemas, ProgLoss + STAL for small/occluded targets. mAP 57.2% (nano) to 71.6% (XL).

### New: HTP Framework — 3D Video Pose Efficiency (2026)

- **Hierarchical Temporal Pruning** for diffusion-based 3D pose estimation
- **38.5% training MACs reduction, 56.8% inference MACs reduction, 81.1% speed improvement**
- Three-stage pruning: TCEP (temporal correlation) → SFT MHSA (sparse attention) → MGPTP (semantic token pruning)
- Preserves temporal consistency across video sequences
- SOTA on Human3.6M and MPI-INF-3DHP

### Yedp Action Director v9.2 — Major Update (March 2026)

- **FBX/GLB/BVH file loading** from Mixamo and other animation sources
- Accurate ControlNet conditioning image export from 3D animations
- Up to 8K resolution animation input
- Direct integration with video generation pipelines
- **Key for this workflow**: load DAZ/Blender animations → precise pose-guided video gen in ComfyUI

### DWPose — Best for This Workflow (ComfyUI)

- 133 whole-body keypoints; standard ControlNet preprocessor
- Node: `comfyui_controlnet_aux`; model: `DWPose-dw-ll-ucoco-384.pth`
- Significantly outperforms OpenPose for hand/face accuracy

### ComfyUI Pose Nodes Ecosystem

| Node / Tool | What It Does |
|-------------|-------------|
| `comfyui_controlnet_aux` | DWPose, OpenPose, MediaPipe preprocessors |
| `Yedp Action Director v9.2` | FBX/GLB/BVH → ControlNet conditioning (NEW) |
| `ComfyUI Open Pose Editor` | Visual skeleton editor |
| `ComfyUI-SCAIL-Pose` | Advanced pose processing |
| `ComfyUI-SDPose-OOD` | Robust OOD pose estimation |
| `Ubisoft CHORD` | Character pose reference + image editing |
| `Pose Studio Node` | One image → infinite pose variations |
| `Save Pose Keypoints Node` | Export keypoints for reuse (updated in `comfyui_controlnet_aux`) |

### Pose-to-Image Workflow (This Project)

```
DAZ/Blender 3D render → DWPose extraction → ControlNet (pose) → Flux Dev + LoRA
                    OR
DAZ/Blender animation (FBX) → Yedp Action Director v9.2 → ControlNet → Wan2.2 video
                    OR
PoseMyArt web tool → DWPose extraction → ControlNet → Flux Dev
                    OR
Reference photo → DWPose extraction → ControlNet → Flux Dev + LoRA
```

### Free APIs / Inference for Pose Estimation

- **HuggingFace Spaces**: DWPose, MediaPipe Holistic, RTMPose — active ZeroGPU Spaces
- **HF Inference API**: RTMPose, ViTPose — serverless (rate-limited free)
- **Roboflow**: YOLO11-pose hosted (free tier)
- **MediaPipe**: Client-side JS SDK — zero server cost
- **MMPose**: 40+ SOTA models, PyPI installable

---

## 🔧 ComfyUI Ecosystem — Notable Nodes/Updates (March 2026)

### 🔥 Major: App Mode, App Builder & ComfyHub (March 10, 2026)

- **App Mode**: One-click transform any workflow into a clean non-technical UI (node graph hidden)
- **App Builder**: Configure which inputs/outputs to expose; rename/reorder without touching nodes
- **Shareable App URLs**: Distribute complete workflows as single URLs; run in-browser via Comfy Cloud
- **ComfyHub**: Public marketplace for sharing apps and workflows (preview launched March 10)
- **Impact**: Non-technical collaborators can now use complex ComfyUI pipelines directly

### 🔥 Major: NVIDIA RTX Acceleration at GDC 2026 (March 10)

- **RTX Video Super Resolution node**: Real-time 4K upscaling on RTX GPUs, 30x faster than alternatives — available now in Manage Extensions
- **NVFP4 model support**: Flux 2 Klein (4B + 9B) + LTX-2.3 in NVFP4 format — 2.5x faster, 60% lower VRAM on RTX 50 Series
- **FP8 support**: 1.7x faster, 40% VRAM reduction (any RTX GPU)
- 40% overall RTX performance improvement since Sept 2025

### Other Notable Updates

- **LTX-2.3 Day-0 native support** — audio-video, 9:16, sharper textures; IAMCCS nodes for 1080p on low-VRAM
- **Yedp Action Director v9.2** — FBX/GLB/BVH → ControlNet conditioning; full 3D scene control
- **Hunyuan 3D advanced features** — 3D Parts Decomposition, UV Unwrapping, Smart Topology via Partner Nodes
- **SageAttention 2++** — Advanced attention optimization (requires CUDA Toolkit + MSVC)
- **Comfy Cloud free tier** (March 3) — 400 monthly credits, no credit card, 900+ models
- **ComfyUI-Manager integrated** into core ComfyUI (no separate install)
- **Wan2.2 native support** — Official templates in ComfyUI menu; memory optimization update
- **IP-Adapter** — Updated for Flux
- **ControlNet Flux nodes** — pose, depth, canny
- **CHORD (Ubisoft, open-sourced)** — Character pose reference + image editing
- **Kling 3.0 Motion Control** — Available now as ComfyUI partner nodes
- **Qwen Image ControlNet + LoRA** — DiffSynth ControlNet Union support; EasyCache for KV-cache efficiency
- **Dynamic VRAM** — New memory optimization enabled by default (replaces manual --lowvram flags)

---

## ⚡ Free GPU Options — March 2026

| Option | GPU | Cost | Best For |
|--------|-----|------|----------|
| **VastAI** | RTX 3090 (24GB) | ~$0.45/hr | ComfyUI workflows, no content policy |
| **RunPod** | Various | ~$0.50-2/hr | Persistent volumes, ComfyUI templates |
| **HF ZeroGPU** | H200 | Free (25 min/day) | Testing models |
| **Google Colab** | T4 (free) / A100 (Pro) | Free / $10/mo | LoRA training, CogVideoX inference |
| **Comfy Cloud** | Cloud GPU | 400 free credits/mo | 900+ models, no install |
| **E2B** | Sandboxed | Usage-based | Code execution, API testing |

---

## 🔑 Key APIs Summary

| Platform | Specialty | Free Tier | URL |
|----------|-----------|-----------|-----|
| fal.ai | Fastest inference, 1000+ models | Signup credits | https://fal.ai |
| Replicate | Largest open-source library | Small trial credits | https://replicate.com |
| Together AI | Open model hosting | $5 signup credit | https://together.ai |
| HF Inference API | Community models, serverless | Free (rate-limited) | https://huggingface.co |
| WaveSpeedAI | 700+ models unified API | Free trial | https://wavespeed.ai |
| Gemini API | Nano Banana 2 image gen | Free tier | https://ai.google.dev |
| SiliconFlow | Flux Schnell + open models | Free tier | https://siliconflow.cn |

---

*Next update: 30 minutes. This file is machine-generated by the digital-stud SOTA pipeline.*

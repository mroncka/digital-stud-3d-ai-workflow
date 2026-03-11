# Image & Video Generation SOTA

> Auto-updated every 30 minutes by the digital-stud research pipeline.
> Last updated: 2026-03-11 21:37 (Prague / CET) | Run #1 + manual expand

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
2. **Google AI Studio** — Nano Banana 2 free tier (rate-limited)
3. **Replicate free trial credits**
4. **fal.ai signup credits** — includes Flux, Seedream, video models
5. **Local ComfyUI** — Flux Schnell/Dev on RTX 3090 (24GB)

### Noteworthy New Entrants (2025–2026)

- **GLM-Image** (Jan 2026, Zhipu AI) — First open-source autoregressive (non-diffusion) image model
- **Seedream 5.0 Lite** (Feb 2026, ByteDance) — Superior multilingual text, in-image translation
- **Z Image Turbo** (Nov 2025, Alibaba Qwen) — S3-DiT, Apache 2.0, 10-20x cheaper than DALL-E 3
- **FireRed-Image-Edit 1.1** — New open-source SOTA for image editing
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
- **Key extensions**: `Wan2.2-Animate` (character animation), `Wan2.2-S2V` (speech-to-video), `FLF2V` (first/last frame)
- **ComfyUI**: Official native workflow at [docs.comfy.org](https://docs.comfy.org/tutorials/video/wan/wan2_2)
- **License**: Apache 2.0

### HunyuanVideo 1.5 — Best Lightweight Open Option

- 8.3B params, 14GB VRAM; SSTA attention (1.87x speedup); CFG-distilled for 2x additional speedup
- Available: fal.ai, local (Linux/WSL2)

### CAUSVID / Distillation Speedups

- CVPR 2025: 50-step bidirectional → 4-step causal generator
- NVIDIA FastGen: open-source distillation library
- `Diagonal Distillation` (arxiv 2603.09488, March 2026): streaming autoregressive approach

### Video API Pricing (March 2026)

| Provider | Model | Price/sec | Free Tier |
|----------|-------|-----------|----------|
| Replicate | Wan 2.2 A14B | ~$0.05/sec | Small credits |
| fal.ai | HunyuanVideo 1.5 | TBC | Signup credits |
| fal.ai | Kling 2.1 | ~$0.14/5s clip | Signup credits |
| RunwayML | Gen-3 Alpha | ~$0.75/sec | 125 free credits |
| WaveSpeedAI | 700+ models unified | Varies | Free trial |

---

## 🧠 LoRA Training SOTA — March 2026

### Training Tools Comparison

| Tool | Best For | Notes |
|------|----------|-------|
| **Kohya SS / musubi-tuner** | Full control, all models | SD1.x, SDXL, SD3, Flux, HunyuanImage-2.1; LoRA/LoHa/LoKr; most flexible |
| **AI-Toolkit (ostris)** | Flux LoRA, video LoRA | Simple config files, ZIT video LoRA support; 80% of the time defaults just work |
| **OneTrainer (Nerogar)** | Character/face LoRAs | Growing adoption; better cross-model stability; steeper curve but more control |
| **SimpleTuner** | SDXL + Flux, attention masking | Experimental stability features, comprehensive docs |
| **fal.ai hosted** | Fast / no GPU | ~$2-5 per LoRA, API-based |
| **Replicate hosted** | Simple one-shot | One-line API call |
| **WaveSpeedAI** | Cloud training | Upload dataset, train FLUX/SDXL LoRA on cloud GPUs |

> **Community note (March 2026):** Many users switching AI-Toolkit → OneTrainer for character LoRAs, reporting significantly less overfitting. musubi-tuner (Kohya fork) is preferred for newer Flux variants when Kohya GUI lacks updates.

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
network_alpha: 16 (half of rank)
conv_dim: 8
epochs: 15-25
noise_offset: 0.035-0.1
mixed_precision: fp16 or bf16
```

### Dataset Preparation Best Practices

- **Size**: 30-50 images for SDXL; 20-80 for Flux
- **Variety**: Front, 3/4, profile, looking up/down, expressions; full body + torso + face closeup
- **Resolution**: 768×768 minimum; 1024×1024 preferred
- **Backgrounds**: Non-distracting variety (solid colors or simple environments)
- **Captions**: Use LoraTag for auto-captioning (FLUX/SDXL/SD3 compatible); trigger word = rare 3-5 char + class (e.g. `zkw woman`)
- **Quality**: Dataset quality matters more for newer models (ZIB / Z Image); facial consistency issues usually from prompt sensitivity, not training params

### LyCORIS / Alternative Architectures

| Method | File Size | Use Case |
|--------|-----------|----------|
| **LoRA** | ~33-66MB | Standard; fast convergence |
| **LoKr** | ~few MB | Extremely compact; faster convergence than LoRA |
| **LoHa** | Medium | Hadamard product; different parameter distribution |
| **GLoRA / GLoKR** | Varies | Generalized; more flexible parameter targeting |

> LoKr is getting significant community interest (March 2026) for very small file sizes with competitive quality vs LoRA.

### Video LoRA (Emerging)

- **Video2LoRA** (arxiv 2603.08210, March 2026): per-reference-video LoRA for semantic-controlled video generation
- **finetrainers** (CogVideoX factory): CogVideoX + Mochi video LoRA training
- **Flimmer**: Video LoRA training toolkit for diffusion transformer models (new, March 2026)
- **AI-Toolkit ZIT**: Preferred for video LoRA currently

---

## 📍 Pose Estimation SOTA — March 2026

### Model Comparison

| Model | Type | Keypoints | Speed | Accuracy | Best For |
|-------|------|-----------|-------|----------|----------|
| **YOLO26-Pose** | Single-stage | 17 (COCO) + custom | 30+ FPS | High | Real-time multi-person, custom keypoints |
| **RTMPose** | Two-stage | 17-133 | 30+ FPS | High | Production: speed + accuracy balance |
| **DWPose** | Two-stage whole-body | 133 (body+hand+face) | Medium | Very High | **Best for ComfyUI ControlNet** |
| **ViTPose / ViTPose++** | ViT-based | 17-133 | Slower | SOTA mAP | Research; highest accuracy |
| **Sapiens2** | Foundation (0.4-5B) | 308 body + face | Slow | SOTA | Whole-body, 1K-4K resolution, multi-task |
| **MediaPipe Holistic** | Lightweight | 33 body + 21/hand + 468 face | 30+ FPS mobile | Medium | Mobile/browser, real-time |
| **SDPose-OOD** | Robust | 17+ | Medium | High OOD | ComfyUI node; robust out-of-distribution |

### YOLO26-Pose (March 2026 SOTA for Speed)

- Removes NMS entirely → true end-to-end detection
- MuSGD optimizer + Residual Log-Likelihood Estimation
- Supports non-human custom keypoints (machinery, sports, infrastructure)
- Improved occlusion handling for small/partially hidden bodies
- Available sizes: nano, small, medium, large, xlarge

### Sapiens2 (Research SOTA)

- 1 billion high-quality human image training set
- Sizes: 0.4B – 5B params; native 1K resolution, 4K hierarchical variant
- +4 mAP over Sapiens1 on pose; +24.3 mIoU on body-part segmentation
- Multi-task: pose + segmentation + normal estimation + depth from one model
- Best when maximum accuracy > speed (research / high-quality reference generation)

### DWPose — Best for This Workflow (ComfyUI)

- 133 whole-body keypoints: 17 body + 6 feet + 68 face + 21 hands ×2
- **Standard pose preprocessor for ControlNet in ComfyUI**
- Works with: `comfyui_controlnet_aux` node pack
- Outperforms OpenPose for hand/face accuracy significantly
- Models: `DWPose-dw-ll-ucoco-384.pth` (recommended)

### ComfyUI Pose Nodes Ecosystem

| Node / Tool | What It Does |
|-------------|---------------|
| `comfyui_controlnet_aux` | DWPose, OpenPose, MediaPipe preprocessors |
| `ComfyUI Open Pose Editor` | Visual pose editor (drag skeleton joints manually) |
| `ComfyUI-SCAIL-Pose` | Advanced pose processing for AI artists |
| `ComfyUI-SDPose-OOD` | Robust pose estimation (out-of-distribution bodies) |
| `ComfyUI_Lam Open Pose Editor Plus` | Manipulate + edit existing poses from images |
| `Ubisoft CHORD` | Open-sourced character pose reference + image editing |
| `Pose Studio Node` | One image → infinite pose variations (video pipeline compatible) |

### Pose-to-Image Workflow (This Project)

```
3D render (DAZ/Blender) → DWPose extraction → ControlNet (pose) → Flux Dev + LoRA
                        OR
Web posing tool (PoseMyArt) → screenshot → DWPose extraction → ControlNet → Flux Dev
                        OR
Reference photo → DWPose extraction → ControlNet → Flux Dev + LoRA
```

### Free APIs / Inference for Pose Estimation

- **HuggingFace Spaces**: DWPose, MediaPipe Holistic, RTMPose all have active ZeroGPU Spaces
- **HF Inference API**: RTMPose, ViTPose available serverless (rate-limited free tier)
- **Roboflow**: YOLO11-pose hosted inference (free tier)
- **MediaPipe**: Runs client-side in browser (JS SDK) — zero server cost
- **MMPose**: Open-source toolbox with 40+ SOTA models, PyPI installable

---

## 🔧 ComfyUI Ecosystem — Notable Nodes/Updates (March 2026)

- **ComfyUI Native Wan2.2 support** — Official workflow templates in ComfyUI menu
- **ComfyUI-Manager now integrated** into core ComfyUI (no separate install needed)
- **Preprocessor template workflows** — official templates for DWPose, depth, canny (blog.comfy.org)
- **Recraft V4 ComfyUI node** — [blog.comfy.org](https://blog.comfy.org/p/recraft-v4-now-available-in-comfyui)
- **IP-Adapter** — Updated for Flux; still the standard for face/style transfer
- **ControlNet Flux nodes** — pose, depth, canny available
- **Wan2.2-Animate node** — Animate reference image with motion video input
- **FLF2V (First/Last Frame to Video)** — Interpolation between two keyframe images
- **CHORD (Ubisoft, open-sourced)** — Character pose reference + image editing model

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

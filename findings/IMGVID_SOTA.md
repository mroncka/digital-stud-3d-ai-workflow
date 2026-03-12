# Image & Video Generation SOTA

> Auto-updated every 30 minutes by the digital-stud research pipeline.
> Last updated: 2026-03-12 03:30 (Prague / CET) | Run #13

---

## 🖼️ Image Generation SOTA — March 2026

### Top Models by Category

| Category | Model | API Access | Cost | Notes |
|----------|-------|------------|------|-------|
| **Overall SOTA** | Nano Banana 2 (Gemini 3.1 Flash Image) | Gemini API, Google AI Studio | ~$0.03/img | #1 Chatbot Arena 1280 Elo; **4K native output**; real-time web grounding; reliable text rendering; character consistency up to 5 chars |
| **Premium reasoning** | Gemini 3 Pro Image ("Nano Banana Pro") | Gemini API, Google AI Studio | $0.134/img (1K-2K), $0.24/img (4K) | **50% Batch API discount**; advanced reasoning; character consistency; 4K res; top LMArena |
| **Photorealism** | Flux 2 Flex | fal.ai, Replicate | ~$0.03/img | Gold standard for skin, lighting, anatomy |
| **Photorealism (fast)** | Flux 2 Klein (9B) | fal.ai, Replicate | ~$0.02/img | Faster variant, native inpainting, editing. **Klein consistency LoRA released March 2026** |
| **Open Source / NSFW** | Flux Dev / Flux 2 Schnell | Local + Replicate | $0.025/img | Best open-weight; Schnell free via HF/SiliconFlow/Firework AI |
| **FLUX.2 Pro** | FLUX.2 Pro (Black Forest Labs) | fal.ai, Replicate, BFL API | $0.025–0.07/img | **1265 Elo — matches GPT Image 1.5**; superior cost-to-quality; sub-second generation |
| **Google budget** | Imagen 4 Fast | Google AI Studio, Vertex AI | $0.02/img | Best budget Google option; thumbnails/previews; **50% Batch API discount** |
| **Anime/Illustrative** | Illustrious XL / NoobAI XL | Local (CivitAI) | Free (local) | NoobAI Chenkin RF = latest, best contrast |
| **Anime + LoRA ecosystem** | Pony Diffusion V6 XL | Local (CivitAI) | Free (local) | Massive LoRA ecosystem, tag-based control |
| **Ultra-cheap + open** | Z Image Turbo (Qwen) | HF Inference, fal.ai | ~$0.004/img | 6B params, Apache 2.0, 16GB VRAM, 3s gen |
| **Logos / Design** | Recraft V4 | fal.ai, Recraft API | ~$0.075/img | #1 HF benchmark for vectors/logos, SVG export; ComfyUI node available |
| **Text in image** | Seedream 5.0 Lite (ByteDance) | fal.ai | TBC | Best Chinese/multilingual text rendering |
| **Budget API** | GPT Image 1 Mini | OpenAI API | ~$0.005/img | Cheapest frontier option; added to Batch API (50% discount = $0.0025) |
| **Logos + 10s video** | Grok Imagining (xAI, Mar 2026) | Grok API | TBC | Four-agent architecture; 10s 720p video gen also available |
| **Budget competitor** | MiniMax Image-01 | MiniMax API, fal.ai | ~$0.01/img | Superior prompt adherence from Hailuo lineage; Feb 2026 release |
| **Open-source text render** | GLM-Image (Z.ai / Zhipu AI) | HF, API | ~$0.015/img | 16B, hybrid autoregressive+diffusion; best text rendering 0.9116 CVTG-2k; Apache 2.0 |
| **Free via Microsoft** | MAI-Image-1 (Microsoft) | Bing/Copilot | Free (limited) | First MS in-house model; top-10 LMArena; integrated in M365 AI |

### Image API Pricing Comparison (March 2026)

| Model | Provider | Cost/Image | Best For |
|-------|----------|-----------|----------|
| Stability AI SDXL | Stability AI | ~$0.003 | Ultra-budget |
| GPT Image 1 Mini (Low) | OpenAI | $0.005 ($0.0025 batch) | Budget |
| Z Image Turbo | HF/fal.ai | ~$0.004 | Open ultra-cheap |
| Imagen 4 Fast | Google | $0.02 ($0.01 batch) | Budget production |
| FLUX.2 Klein 4B | BFL | $0.014 | Low-cost quality |
| MiniMax Image-01 | MiniMax/fal.ai | $0.01 | Budget cinematic |
| FLUX.2 Pro | BFL | $0.025–0.07 | Standard quality value |
| Flux 2 Flex | fal.ai/Replicate | ~$0.03 | Photorealism |
| GPT Image 1.5 (Medium) | OpenAI | $0.034 | Market leader quality |
| Imagen 4 Ultra | Google | $0.06 | Premium quality |
| Gemini 3 Pro (1K-2K) | Google | $0.134 ($0.067 batch) | Premium reasoning |
| Gemini 3 Pro (4K) | Google | $0.24 ($0.12 batch) | Ultra-premium |

### Nano Banana 2 — March 2026 Highlights

- **4K native output** (512px to 4K) — 4K is now standard, not premium
- **Real-time web grounding** via Google Search — current products/locations without stale data
- **Reliable text rendering** — readable text without manual Photoshop overlays
- **Ultra-wide aspect ratios** (4:1, 1:4, 8:1) for banners and cinematic formats
- Available free in Google AI Studio (rate-limited); also in Comfy Cloud free tier
- **Free tier**: 100 images/day (Nano Banana) / 3/day (Pro) via Gemini App; 500 RPD via Gemini API free tier

### Flux 2 Family — Full Breakdown

- **Flux 2 Flex** — Full photorealism, LoRA support, image editing. ~$0.03/image.
- **Flux 2 Klein (9B)** — Faster variant, native inpainting, editing. ~$0.02/image. Klein consistency LoRA now available.
- **Flux 2 Pro** — **1265 Elo, matches GPT Image 1.5; $0.025–0.07/img; sub-second generation.** Best cost-to-quality among frontier models.
- **Flux Kontex** — Context-aware image editing. ~$0.04/image.
- **Flux 2 Schnell** — Open-source, 4-step, free via HF/SiliconFlow/Firework AI APIs.
- NVFP4 quantized models for Klein (4B and 9B): **2.5× faster, 60% lower VRAM** on RTX 50 Series.

### Free / Zero-Cost Image Gen Options

1. **HuggingFace ZeroGPU Spaces** (H200, ~25 min/day free GPU) — Flux Dev, Z Image Turbo, NoobAI, Illustrious
2. **Google AI Studio** — Nano Banana 2 free tier (rate-limited); Veo 3.1 video free tier
3. **Comfy Cloud free tier** (out of beta, March 2026) — 400 monthly credits, no credit card; NVIDIA Blackwell RTX 6000 Pro (96GB VRAM); 900+ models, 350+ templates
4. **SiliconFlow / Firework AI / HF Inference** — Flux Schnell free API
5. **Local ComfyUI** — Flux Schnell/Dev on RTX 3090 (24GB)
6. **Gemini App** — 100 Nano Banana 2 images/day, 3 Pro images/day (free accounts)
7. **Google Batch API** — 50% discount on Gemini 3 Pro, Imagen 4; ideal for bulk non-urgent gen

### Noteworthy New Entrants (2025–2026)

- **GLM-Image** (Jan 2026, Zhipu AI) — First open-source autoregressive (non-diffusion) image model; Apache 2.0; industrial text rendering; best CVTG-2k score
- **Seedream 5.0 Lite** (Feb 2026, ByteDance) — Superior multilingual text, in-image translation
- **Z Image Turbo** (Nov 2025, Alibaba Qwen) — S3-DiT, Apache 2.0, 10–20× cheaper than DALL-E 3
- **FireRed-Image-Edit 1.1** — Open-source SOTA for image editing, beats Qwen edit
- **Recraft V4** — Now in ComfyUI via custom node
- **Grok Imagining** (Mar 2026, xAI) — Four-agent architecture, 10s 720p video gen also available
- **MiniMax Image-01** (Feb 2026) — $0.01/img, extremely competitive
- **MAI-Image-1** (Microsoft) — First in-house Microsoft image model; free via Bing
- **FLUX Image to Video** ⭐ NEW March 2026 — BFL releasing Flux-native image-to-video capability
- **FLUX.2 Pro** ⭐ NEW — 1265 Elo at $0.025–0.07/img; best cost-per-quality frontier model
- **Gemini 3 Pro Image** ⭐ — $0.134/img; 50% batch discount; advanced reasoning + 4K res

---

## 🎬 Video Generation SOTA — March 2026

### Top Models by Category

| Category | Model | Params | VRAM | API/Local | Notes |
|----------|-------|--------|------|-----------|-------|
| **Open Source Best** | Wan2.2 TI2V-5B | 5B | 24GB (RTX 4090) | Local + Replicate | MoE, 720P/24fps, Apache 2.0 |
| **Open Source Heavy** | HunyuanVideo (original) | 13B | 60–80GB | Local (A100) | Beats Runway Gen-3, Luma 1.6 |
| **Open Source Lightweight** | HunyuanVideo 1.5 | 8.3B | 14GB | Local + fal.ai | SSTA attention, 1.87× faster, 1080p upscale |
| **Audio-Video (open)** | LTX-2.3 | — | — | Local (ComfyUI native) | **Native 4K@50fps, 20-sec clips, synchronized audio**; 9:16 portrait; NVFP4 support; NVFP4+FP8 = 3× faster on cloud-class GPUs |
| **Commercial Best** | Kling 3.0 Pro | — | API only | Kling API, fal.ai | Motion Control, multi-shot, best character consistency |
| **Kling Motion Control** | Kling 3.0 MC | — | API only | ComfyUI native | **Motion Control 3.0 nodes live in ComfyUI (Mar 2026)** |
| **Extended clips (Kling)** | Kling 2.6 | — | API only | Kling API | **Up to 2-min videos at 1080p/30fps; simultaneous audio-visual gen; DiT+3D VAE** |
| **Budget Commercial** | Kling 2.1 | — | API only | Kling API | ~$0.14/clip |
| **Open Mid-tier** | CogVideoX-1.5 | 5B | 12–16GB | Local + HF | 1360×768, LoRA support, DDIM Inverse editing |
| **Free via Colab** | CogVideoX 5B | 5B | T4 (Colab) | Google Colab | 6s clips, 720×480, 8fps |
| **Real-time / distilled** | CAUSVID / Diagonal Distillation | — | — | Local research | 4-step causal (CVPR 2025); Diagonal Distillation (arxiv 2603.09488) |
| **Long-form realtime** | Helios (Wan-based) | 14B | H100 | Research | 19.5 FPS on H100, minute-scale |
| **Speech-driven** | Wan2.2-S2V | — | — | Local | Audio-driven character animation |
| **Highest res commercial** | Veo 3.1 (Google) | — | API only | Gemini API, Vertex AI | **4K + native audio, $0.20–$0.60/sec**; free rate-limited tier via AI Studio |
| **Longest clips** | Sora 2 Pro (OpenAI) | — | API only | OpenAI + fal.ai | Up to 25s clips, native audio, $0.30–$0.50/sec |
| **Quad-modal input** | Seedance 2.0 (ByteDance) | — | API only | Dreamina platform | Text+image+video+audio in single pass; 2K cinema; 8+ language lip-sync |
| **Open-source research** | Wan 2.6 | — | 24GB+ | HF, Alibaba Cloud | **Released Dec 2025; 15s 1080p multi-shot + audio; Video Roleplay** |
| **Open-Sora 2.0** | Open-Sora 2.0 | — | — | Research/HF | arxiv 2503.09642; commercial-level quality at lower training cost |
| **Cinematic human** | SkyReels V1 | — | — | HF | HunyuanVideo fine-tune; 33 expressions, 400+ movements; 12s/24fps |
| **Minute-scale** | Helios | 14B | H100 | Research | 1452 frames (~60s at 24fps); Apache 2.0 |
| **Flux I2V NEW** | FLUX Image to Video | — | — | API (BFL) | **March 2026 release; Flux-native image-to-video** |

### LTX-2.3 — Updated March 2026 (Major)

- **Native 4K at 50fps**, up to 20-second clips — significant leap over LTX-2.x
- **Synchronized native audio generation** (video + sound jointly) — first open-source model with this
- **9:16 vertical portrait support** — ideal for social media
- Enhanced image-to-video with better motion consistency
- New latent space & VAE for sharper textures
- **NVFP4 + FP8** quantized models: 1.7× faster, 40% VRAM reduction on RTX GPUs; **3× faster on Blackwell RTX 6000 Pro** (cloud)
- **IAMCCS nodes** enable 1080p on low-VRAM (4080-class) GPUs
- Official templates in ComfyUI menu; Comfy Cloud support
- Apache 2.0 license, free for sub-$10M ARR; licensed training data (Getty/Shutterstock)

### Kling 2.6 — NEW Entry (March 2026)

- **Up to 2-minute videos at 1080p/30fps** — longest open-commercial clips available
- **Simultaneous audio-visual generation** — major architecture innovation
- DiT architecture with 3D VAE
- **Free tier**: ~6 videos/day, watermarked, renews daily
- 10M+ videos generated globally
- Motion Control 3.0 in ComfyUI (native partner nodes, March 9, 2026)

### Wan2.2 — Priority Model for This Workflow

- MoE architecture, TI2V-5B: unified text+image → video, 720P/24fps, RTX 4090
- **Memory optimization update (March 2026)**: improved efficiency; LoRAs from Wan2.1 still compatible
- Extensions: `Wan2.2-Animate`, `Wan2.2-S2V`, `FLF2V`
- [docs.comfy.org](https://docs.comfy.org/tutorials/video/wan/wan2_2) | Apache 2.0

### Wan 2.6 — December 2025 Release (NEW)

- 15-second 1080p multi-shot with audio
- **Video Roleplay**: cast characters from reference videos into new scenes
- Open-source weights on HuggingFace (Apache 2.0)
- GGUF quantized variants for consumer GPUs
- Pricing via fal.ai: ~$0.10/second for 720p

### FLUX Image to Video — March 2026 NEW

- Black Forest Labs releasing Flux-native image-to-video capability
- Leverages Flux's superior visual quality for consistent I2V generation
- API expected via fal.ai/Replicate; self-host weights TBC
- Strong character/style consistency — directly complements Flux LoRA pipeline

### HunyuanVideo 1.5 — Best Lightweight Open Option

- 8.3B params, 14GB VRAM; SSTA (1.87× speedup); CFG-distilled (2× additional speedup); 1080p built-in

### Video API Pricing (March 2026)

| Provider | Model | Price/sec | Free Tier |
|----------|-------|-----------|----------|
| Replicate | Wan 2.2 A14B | ~$0.05/sec | Small credits |
| fal.ai | HunyuanVideo 1.5 | TBC | Signup credits |
| fal.ai | Kling 2.1 | ~$0.14/5s clip | Signup credits |
| fal.ai | Kling 2.6 | ~$0.14/clip+ | Signup credits |
| fal.ai | Wan 2.6 | ~$0.10/sec 720p | Signup credits |
| RunwayML | Gen-4.5 | ~$0.75/sec | 125 free credits |
| fal.ai | Veo 3.1 | $0.20–$0.60/sec | — |
| fal.ai | Sora 2 Pro | $0.30–$0.50/sec | — |
| WaveSpeedAI | 700+ models | Varies | Free trial |
| Google AI Studio | Veo 3.1 | Free (rate-limited) | Best free option |

---

## 🧶 LoRA Training SOTA — March 2026

### Training Tools Comparison

| Tool | Best For | Notes |
|------|---------|-------|
| **Kohya SS v0.9.1+ / musubi-tuner** | Full control, all models | SD1.x, SDXL, SD3, Flux, HunyuanImage-2.1; LoRA/LoHa/LoKr; **fused backward pass: SDXL 24GB → 10GB VRAM** |
| **AI-Toolkit (ostris)** | Flux LoRA, video LoRA | Simple config files, ZIT video LoRA; 80% defaults just work |
| **OneTrainer (Nerogar)** | Character/face LoRAs | **Growing adoption; significantly less overfitting than AI-Toolkit for characters; supports FLUX text-encoder training** |
| **SimpleTuner** | SDXL + Flux, attention masking | Experimental stability features, comprehensive docs |
| **fal.ai hosted** | Fast / no GPU | ~$2–5 per LoRA, API-based |
| **Replicate hosted** | Simple one-shot | One-line API call |
| **WaveSpeedAI** | Cloud training | Upload dataset, train FLUX/SDXL LoRA on cloud GPUs |

> **Klein consistency LoRA** (March 2026): New official consistency LoRA for Flux 2 Klein — improves character consistency across generations without full character LoRA training.

> **Community note:** OneTrainer gaining ground over AI-Toolkit for character LoRAs (significantly less overfitting). musubi-tuner preferred for newer Flux variants. OneTrainer uniquely supports FLUX text-encoder training unlike Kohya-ss.

### Key Training Advances (March 2026)

- **LoRA+ (16× ratio baseline)**: Apply differential LR to LoRA-A and LoRA-B matrices — **~30% faster convergence**, better detail capture. Now the universal baseline in Kohya-ss v0.9.1+
- **Fused backward pass** (Kohya-ss v0.9.1+): SDXL training VRAM **24GB → 10GB** with bf16 — enables consumer-GPU training for previously cloud-only workloads
- **T-LoRA** (arxiv 2507.05964, **NEW**): Timestep-Dependent Low-Rank Adaptation — two key innovations: (1) dynamic rank-constrained updates per diffusion timestep, (2) dynamic fine-tuning strategy. **Single-image character customization without overfitting**; drop-in for standard LoRA pipelines

### Video LoRA — Updated March 2026

- **Video2LoRA** (arxiv 2603.08210): per-reference-video LoRA for semantic-controlled video gen
- **finetrainers** (CogVideoX factory): CogVideoX + Mochi video LoRA training
- **Flimmer** (**NEW March 2026**, by Alvdansen Labs): Dedicated video LoRA toolkit for DiT transformers
  - Full pipeline: scene detection → frame normalization → CLIP-based triage → VAE pre-encoding → phased training
  - **Phased training**: multi-stage runs with unique LR per phase — curriculum learning + MoE expert specialization for Wan2.2 dual-expert architecture
  - **Block swapping**: ~0.67GB saved per block; MoE training optimized
  - **Memory**: optimizer dispatch with CPU offload + Adam-mini; 24GB/48GB VRAM templates for T2V and I2V
  - Wan2.2 I2V VRAM: approaching 24–40GB (from ~60GB unoptimized)
  - Supports Wan2.2 + HunyuanVideo; cleaner API than AI-Toolkit ZIT
- **AI-Toolkit ZIT**: Still viable for video LoRA; Flimmer emerging as preferred alternative
- **T-LoRA**: Single-image concept customization without overfitting — key for character LoRA from minimal training data; drop-in for standard LoRA pipelines (arxiv 2507.05964)

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
lora_plus_ratio: 16 (universal baseline, ~30% faster convergence)
```

### Flux Dev Character LoRA — Small Dataset Config

```
# Optimal for 20-30 images (face/identity)
learning_rate: 4e-4 (faces: higher LR OK)
lora_rank: 16
steps: 2000
save_interval: 250
best_checkpoint: ~step 1250
batch_size: 2, cosine LR scheduler
resolution: 1024x1024
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
# Kohya v0.9.1+: fused backward pass = 24GB -> 10GB VRAM
```

### Dataset Preparation Best Practices

- **Size**: 30–50 images for SDXL; 20–80 for Flux; as few as 1 image with T-LoRA
- **Variety**: Front, 3/4, profile, expressions; full body + torso + face closeup
- **Resolution**: 768×768 min; 1024×1024 preferred; up to 2048 for high-quality face LoRA
- **Captions**: LoraTagger for auto-captioning (FLUX/SDXL/SD3); trigger word = rare 3–5 char + class (e.g., `zkw woman`)
- **Character dataset standard**: 40–60 images with multiple poses, angles, and lighting variations

### LyCORIS / Alternative Architectures

| Method | File Size | Use Case |
|--------|----------|----------|
| **LoRA** | ~33–66MB | Standard; fast convergence |
| **LoKr** | ~few MB | Extremely compact; faster convergence; growing community interest |
| **LoHa** | Medium | Hadamard product; different parameter distribution |
| **GLoRA / GLoKR** | Varies | Generalized; more flexible parameter targeting |

---

## 🏃 Pose Estimation SOTA — March 2026

### Model Comparison

| Model | Type | Keypoints | Accuracy | Speed | Best For |
|-------|------|-----------|----------|-------|----------|
| **YOLO26-Pose** | Single-stage, NMS-free | 17 (COCO) + custom | mAP 57.2% (nano) to 71.6% (XL) | 30+ FPS | Real-time multi-person; **43% faster CPU than YOLO11-N**; MuSGD optimizer |
| **RTMPose** | Two-stage, SimCC head | 17–133 | COCO-AP competitive | 30+ FPS | Production speed/accuracy balance |
| **DWPose** | Two-stage whole-body | 133 (body+hand+face) | Whole AP 0.631 (DWPose-l) | Medium | **Best for ComfyUI ControlNet** |
| **ViTPose / ViTPose++** | ViT-based | 17–133 | Highest mAP | Slower | Research; multi-dataset training |
| **HEViTPose** | Hybrid ViT (CGSR-MHA) | 17–133 | **90.7% MPII / 72.6% COCO** | Medium | **NEW 2026 SOTA efficiency model**; superior perf-per-param vs HRNet |
| **Sapiens2** | Foundation (0.4–5B) | 308 body + face | SOTA whole-body | Slow | SOTA whole-body, 1K–4K, multi-task; ICLR 2026 |
| **MediaPipe Holistic** | Lightweight | 33+21/hand+468 face | — | 30+ FPS mobile | Mobile/browser |
| **SDPose-OOD** | Robust (SD U-Net) | 133 | Parity with Sapiens-1B/2B | Medium | ComfyUI native (Mar 8, 2026); superior OOD generalization |

> **YOLO26-Pose key upgrade (Jan 2026)**: NMS-free end-to-end inference, non-human keypoint support for custom schemas, ProgLoss + STAL for small/occluded targets. MuSGD optimizer from LLM training.

> **HEViTPose (2026)**: CGSR-MHA (cascaded group spatial reduction multi-head self-attention) for efficiency. 90.7% MPII / 72.6% COCO with significantly lower compute than comparable accuracy models.

> **SDPose-OOD** (ComfyUI native since Mar 8, 2026): Built on SD U-Net; superior OOD generalization; 133 wholebody keypoints; parity with Sapiens-1B/2B at 1/5 training schedule.

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

## 🛠️ ComfyUI Ecosystem — Notable Nodes/Updates (March 2026)

### 🆕 Major: App Mode, App Builder & ComfyHub (March 10, 2026)

- **App Mode**: One-click transform any workflow into a clean non-technical UI (node graph hidden)
- **App Builder**: Configure which inputs/outputs to expose; rename/reorder without touching nodes
- **Shareable App URLs**: Distribute complete workflows as single URLs; run in-browser via Comfy Cloud
- **ComfyHub**: Public marketplace for sharing apps and workflows at comfy.org/workflows (preview March 10)
- **Impact**: Non-technical collaborators can now use complex ComfyUI pipelines directly

### 🆕 Major: Comfy Cloud Out of Beta (March 2026)

- **Powered by NVIDIA Blackwell RTX 6000 Pro** (96GB VRAM, 180GB system RAM)
- **Pay-per-use GPU billing**: Only charged during active execution; config/tweaking is free
- **~90% of local custom nodes** available cloud-side, zero configuration
- Custom LoRA uploads from HuggingFace and CivitAI; community LoRA library
- Model access: Wan2.2, LTX-2.3, HunyuanVideo (open) + Sora, Veo, Nano Banana 2, Kling 3.0, Grok (closed)
- Free tier: 400 credits/month, no credit card required

### 🆕 Major: AMD ROCm 7.1.1 Native Integration

- **One-click ComfyUI installer** for AMD hardware (.exe / portable / git)
- **5.4× performance improvement** over ROCm 6.4
- Supports AMD Ryzen AI Max+ systems and Radeon AI Pro workstation GPUs
- Eliminates configuration friction for AMD users

### 🆕 Major: NVIDIA RTX Acceleration at GDC 2026 (March 10)

- **RTX Video Super Resolution node**: Real-time 4K upscaling on RTX GPUs, 30× faster than alternatives — available now in Manage Extensions
- **NVFP4 model support**: Flux 2 Klein (4B + 9B) + LTX-2.3 in NVFP4 format — 2.5× faster, 60% lower VRAM on RTX 50 Series
- **FP8 support**: 1.7× faster, 40% VRAM reduction (any RTX GPU)
- 40% overall RTX performance improvement since Sept 2025

### 🆕 Major: Node Replacement API

- **Official migration paths** for custom node devs: deprecated nodes auto-upgrade to new versions
- **Prevents workflow breakage** on node updates/renames
- Full REST API for retrieving registered replacements; enables input/output remapping
- Major pain point for complex workflow portability now solved

### 🆕 Major: ElevenLabs Partner Nodes (March 9, 2026)

- **Text-to-Speech**, **Voice Cloning**, **Audio Transcription**, **Voice Isolation**, **Multi-Speaker Dialogue**, **Sound Design**
- Enables full multimodal pipelines: Prompt → Image → Video → Voiceover — all inside ComfyUI

### v0.16.1 Changelog (March 5, 2026)

- **Kling 3.0 Motion Control** enabled — ComfyUI native partner nodes
- **LTXAV 2.3 Model Support** — Lightricks audio-video model day-0
- **WAN 2.6/WAN Video Models** — I2V and video processing variants
- **Kandinsky 5.0** — T2V, I2V, T2I variants
- **Veo 3.1 & Veo3 First-Last-Frame Node** — extended video options
- **ResolutionSelector Node** — aspect ratio presets
- **CURVE Type Support** — advanced parameter control
- **BBox Widget** — precise bounding box selection
- **GLSL Shader Node** — PyOpenGL-based visual effects
- **SplitImageToTileList / ImageMergeTileList** — tiled processing
- **Dynamic VRAM** — new memory optimization enabled by default
- **NanoBanana2 API** — IMAGE+TEXT support
- **Recraft V4 Nodes** — new creative workflow nodes

### Other Notable Updates

- **LTX-2.3 Day-0 native support** — audio-video, 9:16, sharper textures; IAMCCS nodes for 1080p on low-VRAM; Comfy Cloud RTX 6000 Pro = 3× faster
- **Yedp Action Director v9.2** — FBX/GLB/BVH → ControlNet conditioning; full 3D scene control
- **HunyuanImage-2.1 advanced features** — 3D Parts Decomposition, UV Unwrapping, Smart Topology via Partner Nodes
- **SageAttention 2++** — Advanced attention optimization (requires CUDA Toolkit + MSVC)
- **ComfyUI-Manager integrated** into core ComfyUI (no separate install)
- **Wan2.2 native support** — Official templates in ComfyUI menu; memory optimization update
- **IP-Adapter** — Updated for Flux
- **ControlNet Flux nodes** — pose, depth, canny
- **CHORD (Ubisoft, open-sourced)** — Character pose reference + image editing
- **Kling 3.0 Motion Control** — Available now as ComfyUI partner nodes
- **Qwen Image ControlNet + LoRA** — DiffSynth ControlNet Union support; EasyCache for KV-cache efficiency
- **ComfyUI Cluster** — 200+ models with auto-selection; workflow packs system
- **3D Animation FBX custom node** — FBX → conditioning image export for video gen
- **FLUX Image to Video** — Flux-native I2V, March 2026 release
- **Flimmer** (**NEW**) — Dedicated video LoRA toolkit for DiT models (Wan2.2, HunyuanVideo); phased training with MoE specialization

---

## ☁️ Free GPU Options — March 2026

| Option | GPU | Cost | Best For |
|--------|-----|------|---------|
| **VastAI** | RTX 3090 (24GB) | ~$0.45/hr | ComfyUI workflows, no content policy |
| **RunPod** | Various | ~$0.50–2/hr | Persistent volumes, ComfyUI templates |
| **HF ZeroGPU** | H200 | Free (25 min/day) | Testing models |
| **Google Colab** | T4 (free) / A100 (Pro) | Free / $10/mo | LoRA training, CogVideoX inference |
| **Comfy Cloud** | Blackwell RTX 6000 Pro (96GB) | 400 free credits/mo | 900+ models, no install; pay-per-use |
| **E2B** | Sandboxed | Usage-based | Code execution, API testing |

---

## 🔑 Key APIs Summary

| Platform | Specialty | Free Tier | URL |
|---------|-----------|-----------|-----|
| fal.ai | Fastest inference, 1000+ models | Signup credits | https://fal.ai |
| Replicate | Largest open-source library | Small trial credits | https://replicate.com |
| Together AI | Open model hosting | $5 signup credit | https://together.ai |
| HF Inference API | Community models, serverless | Free (rate-limited) | https://huggingface.co |
| WaveSpeedAI | 700+ models unified API | Free trial | https://wavespeed.ai |
| Gemini API | Nano Banana 2 / Gemini 3 Pro image gen | Free tier | https://ai.google.dev |
| SiliconFlow | Flux Schnell + open models | Free tier | https://siliconflow.cn |
| BFL (Black Forest Labs) | Flux 2 series, Flux I2V | — | https://api.bfl.ai |
| Google AI Studio | Veo 3.1 video + Gemini 3 Pro image (best free) | Rate-limited daily | https://aistudio.google.com |
| Kling AI | Kling 2.6/3.0 video | ~6 videos/day | https://app.klingai.com |
| OpenAI | GPT Image 1.5, Sora 2 Pro | ~$5 trial | https://platform.openai.com |

---

*Next update: 30 minutes. This file is machine-generated by the digital-stud SOTA pipeline.*

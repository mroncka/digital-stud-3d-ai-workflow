# Image & Video Generation SOTA

### 🆕 Qwen-Image-Edit-2511 Camera-Pose LoRA (March 2026)

- LoRA providing **96 precise camera poses** for exact viewpoint control with Qwen-Image-Edit-2511
- Bridges Qwen-2511's built-in viewpoint capability with discrete, reproducible camera angles
- Use case: lock character to a scene → cycle through 96 predefined camera positions
- Civitai / Instagram: @czmilo tutorial video
- Digital-Stud relevance: multi-angle character shot generation from a single edited reference

### 🆕 Dark Beast DBKlein9b V2.0 (Civitai, March 3, 2026)

- Style fine-tune model for **FLUX.2 Klein 9B** with LoRA adapter injection support
- Compatible with any Klein 9B or Qwen Edit base/fine-tune models via LoRA parameter injection
- Rank-256 format available; directly applicable to Klein 9B + Qwen Edit base models
- Civitai: civitai.com/models/2242173
- Digital-Stud relevance: high-quality Klein 9B style LoRA as reference architecture for custom character fine-tunes

### 🆕 FLUX.2 Klein 4B Custom ControlNet Training (OzzyGT Tutorial, March 2026)

- Workflow: train a **custom control generator + ControlNet** for FLUX.2 Klein 4B using an edit model
- Enables domain-specific control (custom pose, depth, edge) beyond stock ControlNet weights
- Tutorial: x.com/OzzyGT | ComfyUI node: custom training via Diffusers fine-tune pipeline
- Digital-Stud relevance: create pose-specific ControlNets tailored to character animation style

### 🆕 LTX-2.3 ComfyUI Cinematic-Prompt Node (Community, March 2026)

- Auto-infers shot types, camera moves, and audio descriptors from a simple scene prompt
- Free, fully local, uncensored — runs on top of LTX-2.3 in ComfyUI
- Reddit r/StableDiffusion: 217 upvotes; 63 comments confirming quality
- GitHub: check ComfyUI Manager registry for "LTX cinematic" node
- Digital-Stud relevance: simplifies professional video prompting for character animation shots

> Auto-updated every 30 minutes by the digital-stud research pipeline.
> Last updated: 2026-03-12 11:30 (Prague / CET) | Run #29

---

## 🖼️ Image Generation SOTA — March 2026

### 🆕 Luma Uni-1 — Location Accuracy Leader (March 2026)

- Outperforms Nano Banana 2 on **real-world location / scene accuracy** (Marina Bay, landmarks, specific venues)
- Slightly slower than NB2; weaker multi-subject consistency
- Use case: architectural / travel / location-specific renders where NB2 drifts on geography

### Top Models by Category

| Category | Model | API Access | Cost | Notes |
|----------|-------|------------|------|-------|
| **Overall SOTA** | Nano Banana 2 (Gemini 3.1 Flash Image) | Gemini API, Google AI Studio | ~$0.03/img | #1 Chatbot Arena 1280 Elo; **4K native output**; real-time web grounding; reliable text rendering; character consistency up to 5 chars |
| **Premium reasoning** | Gemini 3 Pro Image ("Nano Banana Pro") | Gemini API, Google AI Studio | $0.134/img (1K-2K), $0.24/img (4K) | **50% Batch API discount**; advanced reasoning; character consistency; 4K res; top LMArena |
| **Photorealism** | Flux 2 Flex | fal.ai, Replicate | ~$0.03/img | Gold standard for skin, lighting, anatomy |
| **Photorealism (fast)** | Flux 2 Klein (9B) | fal.ai, Replicate | ~$0.02/img | Faster variant, native inpainting, editing. **Klein consistency LoRA released March 2026** |
| **Open Source / NSFW** | Flux Dev / Flux 2 Schnell | Local + Replicate | $0.025/img | Best open-weight; Schnell free via HF/SiliconFlow/Firework AI |
| **FLUX.2 Pro v1.1** | FLUX.2 Pro v1.1 (Black Forest Labs) | fal.ai, Replicate, BFL API | $0.055/img | **1265 Elo — LM Arena**; v1.1 refinement over v1.0; sub-second generation |
| **FLUX.2 Pro v1.0** | FLUX.2 Pro (Black Forest Labs) | fal.ai, Replicate, BFL API | $0.025–0.07/img | **1258 Elo**; best cost-per-quality baseline; sub-second generation |
| **Google budget** | Imagen 4 Fast | Google AI Studio, Vertex AI | $0.02/img | Best budget Google option; thumbnails/previews; **50% Batch API discount** |
| **Anime/Illustrative** | Illustrious XL / NoobAI XL | Local (CivitAI) | Free (local) | NoobAI Chenkin RF = latest, best contrast |
| **Anime + LoRA ecosystem** | Pony Diffusion V6 XL | Local (CivitAI) | Free (local) | Massive LoRA ecosystem, tag-based control |
| **Ultra-cheap + open** | Z Image Turbo (Qwen) | HF Inference, fal.ai | ~$0.004/img | 6B params, Apache 2.0, 16GB VRAM, 3s gen |
| **Logos / Design** | Recraft V4 | fal.ai, Recraft API | ~$0.075/img | #1 HF benchmark for vectors/logos, SVG export; ComfyUI node available |
| **Text in image** | Seedream 5.0 Lite (ByteDance) | fal.ai | TBC | Best Chinese/multilingual text rendering |
| **Budget API** | GPT Image 1 Mini | OpenAI API | ~$0.005/img | Cheapest frontier option; Batch API = $0.0025/img |
| **Logos + 10s video** | Grok Imagining (xAI, Mar 2026) | Grok API | ~$0.02/img | Four-agent architecture; 10s 720p video gen also available |
| **Budget competitor** | MiniMax Image-01 | MiniMax API, fal.ai | ~$0.01/img | Superior prompt adherence from Hailuo lineage; Feb 2026 release |
| **Open-source text render** | GLM-Image (Z.ai / Zhipu AI) | HF, API | ~$0.015/img | 16B, hybrid autoregressive+diffusion; best text rendering 0.9116 CVTG-2k; Apache 2.0 |
| **Free via Microsoft** | MAI-Image-1 (Microsoft) | Bing/Copilot | Free (limited) | First MS in-house model; top-10 LMArena; integrated in M365 AI |

### LM Arena Image Rankings (March 2026)

| Rank | Model | Elo | Cost/Img |
|------|-------|-----|----------|
| 1 | GPT Image 1.5 (OpenAI) — ~95% text-in-image accuracy | 1,284 | $0.034–0.20 |
| 2 | Nano Banana 2 (Gemini 3.1 Flash Image) | 1,280 | ~$0.03 |
| 3 | Gemini 3 Pro Image | 1,268 | $0.134 (std) |
| 4 | FLUX.2 Pro v1.1 | 1,265 | $0.055 |
| 5 | FLUX.2 Pro v1.0 | 1,258 | $0.025–0.07 |
| 6 | Flux 2 Dev (open) | 1,245 | Free (self-host) |
| 7 | Stable Diffusion 3.5 Large (open) | 1,198 | Free (self-host) |

### Image API Pricing Comparison (March 2026)

| Model | Provider | Cost/Image | Best For |
|-------|----------|-----------|----------|
| Stability AI SDXL | Stability AI | ~$0.003 | Ultra-budget |
| GPT Image 1 Mini (Low) | OpenAI | $0.005 ($0.0025 batch) | Budget |
| Z Image Turbo | HF/fal.ai | ~$0.004 | Open ultra-cheap |
| Grok Imagine | xAI | ~$0.02 | Budget fast |
| Imagen 4 Fast | Google | $0.02 ($0.01 batch) | Budget production |
| FLUX.2 Klein 4B | BFL | $0.014 | Low-cost quality |
| MiniMax Image-01 | MiniMax/fal.ai | $0.01 | Budget cinematic |
| FLUX.2 Pro v1.0 | BFL | $0.025–0.07 | Standard quality value |
| Flux 2 Flex | fal.ai/Replicate | ~$0.03 | Photorealism |
| FLUX.2 Pro v1.1 | BFL | $0.055 | Highest quality BFL |
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
- **Free tier**: 100 images/day (Nano Banana) / 3/day (Pro) via Gemini App; **up to 1,500 images/day via Gemini Flash API free tier** (web UI); 500 RPD via standard Gemini API free tier

### 🆕 FLUX.2 Klein Consistency LoRA (Community, March 2026)

- Fixes **pixel drift / content shifting** in img2img operations with Klein 9B
- Locks composition and character identity during iterative in/outpainting passes
- ComfyUI AIO workflow: Edit, Inpaint, Place, Replace, Remove using Klein + this LoRA
- Find on: CivitAI search "Flux Klein Consistency" | r/StableDiffusion confirmed quality
- Digital-Stud relevance: enables reliable character editing loops without identity degradation

### Flux 2 Family — Full Breakdown

- **Flux 2 Flex** — Full photorealism, LoRA support, image editing. ~$0.03/image.
- **Flux 2 Klein (9B)** — Faster variant, native inpainting, editing. ~$0.02/image. Klein consistency LoRA now available.
- **Flux 2 Pro v1.0** — **1258 Elo; $0.025–0.07/img; sub-second generation.** Best cost-per-quality baseline.
- **Flux 2 Pro v1.1** — **1265 Elo; $0.055/img; refinement over v1.0** with improved detail consistency.
- **Flux Kontex** — Context-aware image editing. ~$0.04/image.
- **Flux 2 Schnell** — Open-source, 4-step, free via HF/SiliconFlow/Firework AI APIs.
- NVFP4 quantized models for Klein (4B and 9B): **2.5× faster, 60% lower VRAM** on RTX 50 Series.

### Free / Zero-Cost Image Gen Options

1. **HuggingFace ZeroGPU Spaces** (H200, ~25 min/day free GPU) — Flux Dev, Z Image Turbo, NoobAI, Illustrious
2. **Google AI Studio** — Nano Banana 2 free tier (rate-limited); Veo 3.1 video free tier
3. **Gemini Flash API free tier** — **up to 1,500 images/day** (most generous free API for production use)
4. **Comfy Cloud free tier** (out of beta, March 2026) — 400 monthly credits, no credit card; NVIDIA Blackwell RTX 6000 Pro (96GB VRAM); 900+ models, 350+ templates
5. **SiliconFlow / Firework AI / HF Inference** — Flux Schnell free API
6. **Local ComfyUI** — Flux Schnell/Dev on RTX 3090 (24GB)
7. **Gemini App** — 100 Nano Banana 2 images/day, 3 Pro images/day (free accounts)
8. **Google Batch API** — 50% discount on Gemini 3 Pro, Imagen 4; ideal for bulk non-urgent gen

### Noteworthy New Entrants (2025–2026)

- **GLM-Image** (Jan 2026, Zhipu AI) — First open-source autoregressive (non-diffusion) image model; Apache 2.0; industrial text rendering; best CVTG-2k score
- **Seedream 5.0 Lite** (Feb 2026, ByteDance) — Superior multilingual text, in-image translation
- **GLM-Image** (Jan 14 2026, Zhipu AI) — 16B params; **90.5% text rendering accuracy**; open-source autoregressive model; **Apache 2.0**; best CVTG-2k score; strong open-source alternative to proprietary text-in-image leaders
- **Z Image Turbo** (Nov 2025, Alibaba Qwen) — S3-DiT, Apache 2.0, 10–20× cheaper than DALL-E 3
- **MiniMax Image-01** (Feb 2026) — **$0.01/image** cinematic quality; among cheapest quality-per-dollar API options
- **FireRed-Image-Edit 1.1** — Open-source SOTA for image editing, beats Qwen edit
- **Stable Diffusion 4 Ultra** (Stability AI, March 6 2026)
  - Major open-source release: improved text rendering, correct anatomy/hands, cinema-grade lighting
  - 4th in image leaderboard (~1130 Elo); **best open-weight option** for fine-tuning and local deployment
  - Open-weight; community fine-tuning community rapidly adopting as Flux.2 alternative base

- **FLUX.2 Klein 9B** (ModelsLab, March 11 2026)
  - Distilled 9B model variant with improved image-to-image consistency
  - Available via ModelsLab API; good for rapid iteration / real-time editing workflows
  - Digital-Stud relevance: fast I2I for character variant generation without full inference cost

### 🆕 REDEdit-Bench — Bilingual Image Editing Benchmark (March 9, 2026)

- Released by FireRed team: **1,673 bilingual** (Chinese/English) editing pairs across **15 categories**
- More realistic/diverse than HIVE, EditBench, EmuEdit
- March 2026 leaderboard: FireRed-Image-Edit-1.1 (4.56) > Qwen-Image-Edit-2511 (4.51) > FLUX.2 Dev (4.35)
- GitHub: github.com/FireRedTeam/FireRed-Image-Edit
- Digital-Stud relevance: authoritative benchmark for evaluating instruction-following edits on character/product images

### 🆕 LongCat-Image-Edit-Turbo (Meituan, Early March 2026)

- Distilled 8-step inference: ~**10× speedup** over base LongCat-Image-Edit
- Strong instruction-following; best-in-class bilingual (Chinese/English) in-image text rendering
- Multi-turn editing: non-edited regions preserved well across iterative passes
- HuggingFace: meituan-longcat/LongCat-Image-Edit | vLLM-Omni supported
- Digital-Stud relevance: fast multi-turn editing for iterative character + scene refinement without full regeneration

### 🆕 TDM-R1 — RL for Few-Step Diffusion with Non-Differentiable Rewards (arXiv 2603.07700)

- Novel RL paradigm: decoupled into surrogate reward learning + generator optimization
- Non-differentiable reward types supported: **human preference, object count, OCR correctness**
- Key results: GenEval 61% → **92%** (surpasses 80-NFE base at 63% and GPT-4o at 84%); only **4 NFEs**
- Scales to 6B Z-Image model; CUHK-Shenzhen + Xiaohongshu (hi-Lab)
- Digital-Stud relevance: reward-guided sampling for character accuracy and prompt adherence without retraining

### 🆕 Step1X-Edit-v1p2 — Reasoning Image Editor (March 2026)

- Introduces **explicit reasoning + reflection** before finalising edits
- Better compound instruction parsing; significantly stronger non-edit region preservation vs v1p1
- Benchmark: top-tier on GEdit-O and ImgEdit-O metrics
- Digital-Stud relevance: high-accuracy multi-sub-task character editing (change outfit + lighting + expression simultaneously)

- **FLUX.2 Dev 8-step Turbo LoRA — Speed Benchmarks** (ComfyUI, March 2026)
  - PyTorch SDP + xFormers: ~560s at 1.6MP (1280×1280)
  - Sage Attention variant: ~537s (29s savings); scales better on large batches
  - Full 25-step non-Turbo: ~23 min (PyTorch) / ~21 min (Sage) — Turbo LoRA saves ~60% time

- **FLUX.2 Ecosystem Stats** (March 2026)
  - **50,000+ LoRAs** now on HuggingFace; FLUX.2 is base for ~90% of all community fine-tunes
  - Hundreds of style variants: anime, pixel art, portrait photography, product rendering
  - API leaderboard: FLUX.2 Pro v1.1 at 1265 Elo (#2 overall); FLUX.2 Max at 1206 Elo (#5)

- **OmniGen2 / Wallaroo** — Multi-modal generation + editing
  - Pending HF release: "will release models, training code, datasets, data" per official communications
  - State-of-the-art among open-source models for consistency in generation+editing
  - Wallaroo (arXiv 2603.04980): Simple baseline for unifying understanding + generation + editing

- **OmniEdit** (arXiv 2603.09084, March 2026)
  - Training-free framework for **lip synchronization + audio-visual editing** in videos
  - Reformulates lipsync as a cross-modal attention task; no per-video fine-tuning needed
  - Digital-Stud relevance: Add talking-head dialogue to generated character videos post hoc
  - GitHub: pending public release; paper available

- **Canva Magic Layers** (March 12 2026)
  - Turns any flat AI-generated image into a fully editable layered design
  - Generative remix/refine without re-generating from scratch
  - **Digital-Stud relevance**: Post-processing step for character sheets and product renders

- **Chroma1-Radiance** (lodestones, HF) — Open-weight image model updated Feb 22 2026; 144+ HF likes; community-developed SOTA-tier open image model
- **Unsloth LTX-2.3 Dynamic GGUF** — All GGUF quantization variants (Q4_K_M, Q5_K_S, Q8, etc.) released; dynamic variants with important layers upcasted; Colab T4 workflow included; run I2V on 15GB VRAM
- **FLUX.2 Klein Enhancer node pack** (ComfyUI) — Lock poses, Flux 2 Klein-specific consistency controls; 360° panorama LoRA companion; inpainting via `flux klein` mask-fill workflow; best inpaint ControlNet: Qwen Image (crop&stitch)
- **Modular Diffusers** (HuggingFace, March 5 2026) — Composable building blocks for diffusion pipelines; mix-and-match ControlNet/VAE/scheduler blocks; FLUX.2-klein-4B example workflow provided
- **Seedream 4.5** (ByteDance) — New image generation model available on OpenRouter (March 2026); Elo ~1,147 with strong typography support; commercial-friendly API
- **AIMomentz** — New open platform for human-preference AI image evaluation with tamper-proof audit trail (launched March 11, 2026)
- **FLUX-1.1-pro on Microsoft Foundry** — FLUX-1.1-pro now available via Microsoft Foundry (updated March 10, 2026); broadens enterprise access
- **HuggingFace W11 paper: CoCo** — "Code as CoT for Text-to-Image Preview and Rare Concept Generation" — uses code-style chain-of-thought for rare concept generation; featured on HF daily papers week 11
- **Flux.1 Fill + Flux Klein masked inpaint** — Community-confirmed (Reddit March 2026) best inpainting combo: `flux1 fill onereward` for quality + Klein masked inpaint node for targeted region work
- **Recraft V4** — Now in ComfyUI via custom node
- **Grok Imagining** (Mar 2026, xAI) — Four-agent architecture, 10s 720p video gen also available; ~$0.02/img
- **MiniMax Image-01** (Feb 2026) — $0.01/img, extremely competitive
- **MAI-Image-1** (Microsoft) — First in-house Microsoft image model; free via Bing
- - **FLUX Kontext** (BFL, March 2026) — Subject consistency across scene transformations; Flux-native approach to character/object consistency without IP-Adapter overhead
- **DeepSeek V4** (imminent, Apache 2.0) — 1T total / 37B active params (MoE); native image + video gen competing with DALL-E 3 / Midjourney; Engram Memory (1M token retrieval); consumer-friendly quantization (1× RTX 5090 INT4, 2× RTX 4090 INT8); V4 Lite appeared March 9 — full release imminent; expected to pressure proprietary image API pricing significantly
- **FLUX Image to Video** ⭐ NEW March 2026 — BFL releasing Flux-native image-to-video capability; transforms photos to cinematic video; competitive API pricing via fal.ai/Replicate
- **FLUX.2 Pro v1.1** ⭐ NEW — 1265 Elo at $0.055/img; refined over v1.0
- **Gemini 3 Pro Image** ⭐ — $0.134/img; 50% batch discount; advanced reasoning + 4K res

---

### 🆕 ImageCritic — Fine-Grained Inconsistency Detector for AI Images (March 5, 2026)

- kombitz.com/2026/03/05/imagecritic-improves-ai-image-editing-accuracy/
- AI system that detects and automatically corrects fine-grained visual inconsistencies (e.g. extra fingers, mismatched lighting, text errors)
- Integrates into AI-assisted editing loops as a post-generation quality gate
- Digital-Stud relevance: automated QC layer on top of face refinement or LoRA-generated character outputs

### 🆕 Adobe Photoshop AI Assistant (March 10, 2026)

- Integrated AI assistant for Photoshop, connecting to external generation APIs
- Supports: **Runway Gen-4.5**, **Black Forest Labs FLUX**, and other partner models via API call-out
- Goal: keep creative work inside Photoshop with AI generation as an inline tool
- Source: TechCrunch, March 10, 2026
- Digital-Stud relevance: FLUX integration means Photoshop can serve as a ComfyUI-adjacent front-end for professional retouching

## 🎬 Video Generation SOTA — March 2026

### 🆕 MSVBench — First Multi-Shot Video Generation Benchmark (arXiv 2602.23969)

- Hierarchical scripts + reference images tailored for **multi-shot narrative video** evaluation
- Evaluates: shot-to-shot consistency, character identity persistence, scene continuity
- Addresses gap in existing benchmarks (EvalCrafter, T2V-CompBench) which test single-shot only
- Digital-Stud relevance: framework for evaluating character animation sequences across multiple shots

### 🆕 Luma Uni-1 — Location Accuracy Leader (March 2026)

- Outperforms Nano Banana 2 on **real-world location / scene accuracy** (Marina Bay, landmarks, specific venues)
- Slightly slower than NB2; weaker multi-subject consistency
- Use case: architectural / travel / location-specific renders where NB2 drifts on geography

### Top Models by Category

| Category | Model | Params | VRAM | API/Local | Notes |
|----------|-------|--------|------|-----------|-------|
| **Open Source Best** | Wan2.2 TI2V-5B | 5B | 24GB (RTX 4090) | Local + Replicate | MoE, 720P/24fps, Apache 2.0; **37.1% adoption among open-source enthusiasts** |
| **Open Source Heavy** | HunyuanVideo (original) | 13B | 60–80GB | Local (A100) | Beats Runway Gen-3, Luma 1.6; Text Alignment 61.8% vs Runway 47.7% |
| **Open Source Lightweight** | HunyuanVideo 1.5 | 8.3B | **14GB** | Local + fal.ai | **SSTA (Selective & Sliding Tile Attention): 1.87× faster than FlashAttention-3**; 1080p upscale; dual-stream hybrid arch; bilingual |
| **Audio-Video (open)** | LTX-2.3 | — | — | Local (ComfyUI native) | **Native 4K@50fps, 20-sec clips, synchronized audio**; 9:16 portrait; NVFP4 support |
| **Commercial 4K flagship** | Kling 3.0 Pro | — | API only | Kling API, fal.ai | **ELO 1243** (LMArena Mar 2026); 15s clips, native 4K/60fps, AI Director mode (up to 6 camera cuts/gen), native audio in 5+ languages |
| **Kling Omni** | Kling 3.0 Omni Pro | — | API only | Kling API | **ELO 1236**; combined model variant |
| **Kling Motion Control** | Kling 3.0 MC | — | API only | ComfyUI native | **Motion Control 3.0 nodes live in ComfyUI (Mar 2026)**; body movement + facial expression + camera transfer |
| **O3 Standard** | Kling Video O3 Standard | — | API only | WaveSpeedAI, Kling API | Part of Kuaishou O3 family (Feb 2026); standardized consistent quality |
| **Extended clips** | Kling 2.6 | — | API only | Kling API | **Up to 2-min videos at 1080p/30fps; simultaneous audio-visual gen; DiT+3D VAE** |
| **Budget Commercial** | Kling 2.1 | — | API only | Kling API | ~$0.14/clip |
| **Open Mid-tier** | CogVideoX-1.5 | 5B | 12–16GB | Local + HF | 1360×768, LoRA support, DDIM Inverse editing |
| **Free via Colab** | CogVideoX 5B | 5B | T4 (Colab) | Google Colab | 6s clips, 720×480, 8fps |
| **Real-time / distilled** | CAUSVID / Diagonal Distillation | — | — | Local research | 4-step causal (CVPR 2025); Diagonal Distillation (arxiv 2603.09488) |
| **Long-form realtime** | Helios (Wan-based) | 14B | H100 | Research (Wan2.1) | 19.5 FPS on H100, minute-scale; 1452 frames (~60s at 24fps); Apache 2.0; **based on Wan2.1 foundation** |
| **Speech-driven** | Wan2.2-S2V | — | — | Local | Audio-driven character animation |
| **Highest res commercial** | Veo 3.1 (Google) | — | API only | Gemini API, Vertex AI | **4K + native audio, $0.20–$0.60/sec; 20% better audio quality vs Veo 3**; leads for dialogue-heavy cinematic content; ELO ~1150 |
| **Veo 3.1 Fast** | Veo 3.1 Fast (Google) | — | API only | Google AI Studio | 4–8s videos at 720p/1080p in 45–60 seconds; reference image for character consistency |
| **Longest clips** | Sora 2 Pro (OpenAI) | — | API only | OpenAI + fal.ai | **ELO 1199**; up to 2-min clips; multi-shot storytelling; $0.30–$0.50/sec |
| **Quad-modal input** | Seedance 2.0 (ByteDance) | — | API only | Dreamina platform | **"DeepSeek moment for AI video"**; text+image+video+audio in single pass; 2K cinema; 8+ language lip-sync |
> **Seedance 2.0 API note** (March 2026): Currently API-only via Dreamina/Jimeng platforms. Broader API access planned Q3 2026. Dual-branch DiT architecture; 6-shot multi-cut in single generation pass.
> **Confirmed pricing** (March 10, 2026): ¥28/M tokens (~$3.90) for video editing with video input; ¥46/M tokens (~$6.40) for pure text-to-video generation. A 15-second video ≈ 308,880 tokens → ~$0.14/sec. Supports 10–20 requests/min batch processing. Sub-second latency (<2s for 15-sec HD clip).

| **Open-source research** | Wan 2.6 | — | API only | **Commercial only** | **⚠️ Dec 2025 release; weights NOT open-source** — commercial API via Alibaba Cloud only; 15s 1080p multi-shot + audio; community asking for open weights |
| **Open-Sora 2.0** | Open-Sora 2.0 | — | — | Research/HF | **$200K training cost; Video DC-AE 4×32×32 compression; 5.2× training throughput vs HunyuanVideo VAE; 10×+ inference speedup**; arxiv 2503.09642 |
| **Cinematic human** | SkyReels V1 | — | — | HF | HunyuanVideo fine-tune; 33 expressions, 400+ movements; 12s/24fps |
| **Flux I2V NEW** | FLUX Image to Video | — | — | API (BFL) | **March 2026 release; Flux-native image-to-video** |
| **Deprecated** | Sora 1 (OpenAI) | — | — | — | **⚠️ Deprecated March 13, 2026 in US** — migrate to Sora 2 |

### LMArena Video ELO Rankings (March 2026)

| Rank | Model | ELO |
|------|-------|-----|
| 1 | Kling 3.0 Pro | 1,243 |
| 2 | Kling 3.0 Omni Pro | 1,236 |
| 3 | Sora 2 Pro | 1,199 |
| 4 | Veo 3.1 | ~1,150 |
| — | Wan2.2 / Open-source | ~1,080–1,100 |

> Gap between Kling 3.0 Pro (1243) and Sora 2 Pro (1199) = 44 ELO points — substantial lead.

### 🆕 HunyuanVideo Foley — Audio-Aligned Video (if-ai ComfyUI Node, March 8 2026)

- `ComfyUI_HunyuanVideoFoley` (if-ai) on production ComfyUI registry since March 8 2026
- Generates **sound effects + ambient audio synchronized to video motion** using HunyuanVideo
- Input: video frames / motion; output: matching audio track
- Digital-Stud relevance: adds audio to AI character video without a separate audio pipeline

### HunyuanVideo-1.5 — Efficiency Breakdown

- **8.3B parameters** vs 13B original — 36% smaller, same quality tier
- **SSTA (Selective & Sliding Tile Attention)**: 1.87× speedup vs FlashAttention-3 specifically
- **14GB VRAM minimum** (down from 60–80GB for original HunyuanVideo)
- **3D causal VAE**: 16× spatial + 4× temporal compression
- **Dual-stream → single-stream hybrid**: better text-video fusion
- **Acceleration options**: CFG distilled (2× faster), sparse attention (1.5–2×), SageAttention
- **⚠️ WaveSpeedAI API cap**: Currently capped at 480p despite model's 1080p capability — check other providers
- Available: HuggingFace, GitHub (Tencent-Hunyuan/HunyuanVideo-1.5), Apache 2.0

### LTX-2.3 — Updated March 2026 (Major)

> **Run 22 update (2026-03-12 08:03):**
> - Architecture: **AVTransformer3DModel** — unified audio-video DiT; generates synchronized audio + video in a single model pass; 22B params
> - Official ComfyUI I+A2V workflow updated **March 9, 2026** (Image + Audio to Video); lip-sync support; LoRA-based mode ~242s, MelBandRoformer mode ~326s on RTX 4090
> - **RTX 5090 I2V benchmark vs Wan2.2 14B (GGUF Q4, 32GB VRAM)**: LTX-2.3 22B = **22s** vs Wan2.2 = **125s** → **5.7× faster** generation; trade-off: Wan2.2 better camera stability and hand quality
> - **LTX-2.3 FLF2V (First-Last-Frame) Status**
  - **No official template yet** (March 2026); Lightricks provides only T2V + I2V official workflows
  - **Recommended**: Kijai's FLF2V workflow (HuggingFace Discussions) — pre-built, community-tested
  - Key parameters: first frame strength 0.8–1.0, last frame strength 0.6–0.9 for natural motion
  - TTP Toolset FirstLastFrame also available but needs tweaking for 2.3
- **LTX-2.3 Audio-Video Sync Parameters** (community best practices)
  - Modality guidance: **7**, CFG: **3** → best synchronized audio-video output
  - Avoid full-body human shots for audio lipsync; use close headshot/upper body
  - Image injection: full-size OR 50% latent downscale → 2x upscale pass (style tradeoff)
  - FP8 + GGUF variants from Kijai for VRAM reduction (T4/15GB Colab confirmed working)
- **IC-LoRA with ControlNet union** (depth + human pose + edges): Available in `ComfyUI-LTXVideo` official repo — critical for pose-conditioned character video generation in Digital-Stud workflows
- IC-LoRA motion tracking node also available
- ⚠️ Standard KSampler nodes cause `split_with_sizes` error — must use official `ComfyUI-LTXVideo` node set (21-node AV pipeline)
> - ⚠️ **SageAttention3 gives ~0% speedup on GGUF models** — GGUF dequant (4-bit→bf16) dominates; sageattn3 only effective on non-quantized Wan2.2 (~13% gain)



- **Native 4K at 50fps**, up to 20-second clips
- **Synchronized native audio generation** (video + sound jointly) — first open-source model with this
- **9:16 vertical portrait support**
- **NVFP4 + FP8** quantized: 1.7× faster, 40% VRAM reduction; **3× faster on Blackwell RTX 6000 Pro**
- **IAMCCS nodes** enable 1080p on low-VRAM (4080-class) GPUs
- Apache 2.0, free for sub-$10M ARR
- **⚠️ Community note**: LTX Desktop reportedly outperforms ComfyUI out-of-box for LTX-2.3 — custom node configuration matters for parity


### 🆕 Runway Characters — Real-Time Avatar API (March 9, 2026)

- Generates fully **conversational AI avatars** from a single static reference image
- Real-time video agent API; enterprise integration; bundled with Adobe Firefly
- Use case: product demo characters, AI tutors, branded digital humans
- Digital-Stud relevance: character activation for client-facing assets without full vid gen pipeline

### Kling 3.0 Pro — Commercial 4K Flagship (February 2026)

- **ELO 1243** — top-ranked commercial video model (LMArena, March 2026)
- **15-second clips at native 4K/60fps** — highest resolution commercial output available
- **AI Director mode**: Multi-shot editing with up to **6 camera cuts** in a single generation
- **Native audio co-generation**: Dialogue, music, SFX in 5+ languages, synchronized
- **Motion Control 3.0**: Body movement, facial expression, and camera dynamics transfer from reference video
- Motion Control 3.0 nodes live in ComfyUI (March 9, 2026)

### Wan 2.6 — Status Clarification

- **⚠️ Commercial-only**: Wan 2.6 released Dec 2025 as commercial product; **weights not open-sourced**
- Available via Alibaba Cloud commercial API only
- Community actively requesting open-source release (Reddit thread active)
- **Use Wan 2.2 for open-source workflows** — still best open-weight option

### 🆕 HunyuanVideo — RL Post-Training Code Open-Sourced (Tencent, March 2026)

- **HunyuanVideo RL post-training code** released for community fine-tuning and real-time training (GitHub: `Tencent-Hunyuan/HunyuanVideo`)
- Enables custom model adaptation without full retraining; complements HY-WU on-the-fly LoRA approach
- **HunyuanVideo-Avatar**: MM-DiT-based model for audio-driven talking/singing video; multi-character dialogue, emotion-controllable; 480p/720p up to 120s via WaveSpeedAI ($0.15/5s)

### 🆕 Wan2.6 — Coming Soon (Alibaba, March 2026)

- **API-first positioning**: Alibaba announced *Wan2.6 Masterclass: Learn to call HTTP APIs and generate stunning videos* on **March 24, 2026** — suggests API-centric design vs Wan2.2's local-first approach
- Specific feature improvements vs Wan2.2 not yet publicly detailed; expect resolution/speed improvements based on version cadence
- Per-second pricing structure hinted (720P ~¥0.6/sec based on `wan-2-6-i2v` listings)
- **Digital-Stud action**: Update `wan22_img2vid.json` workflow to Wan2.6 API endpoint when weights release

### 🆕 SkyReels V4 — Joint Audio-Video Generation (Late Feb / Early Mar 2026)

- Major architectural shift from V2 (infinite-length) to **joint audio-video generation** (max 15s currently)
- **Native audio as first-class feature**: beat-sync, voice-guided pacing, automatic audio-visual balance
- Video quality improvements: better edge detail, color hold, motion consistency up to **1080p**
- SkyReels V2 remains better for: content >15s, ComfyUI ecosystem, hardware flexibility
- API: WaveSpeedAI wavespeed.ai/blog/posts/skyreels-v4-vs-v2/
- Digital-Stud note: V4 useful for short cinematic clips with synced audio; V2 for long-form animation

### 🆕 Seedance 2.0 — Reference Cluster & Character Consistency (Feb 2026)

- **Reference Cluster System**: up to **12 multimodal inputs** (9 images + 3 videos); @-tag syntax for identity/motion binding
- **Golden Ratio Method**: 70% identity ref + 30% motion ref weighting → prevents character drift across shots
- Consistency script workflow enables >30-second sequences with same character
- Digital-Stud verdict: currently best for multi-shot consistent character video; API: Replicate, fal.ai, ByteDance API

### 🆕 Seedance 2.0 — Commercial API Pricing Disclosed

- ByteDance disclosed commercial API pricing via LinkedIn (Asteris AI, March 2026)
- **No public REST API yet** — expected Q3 2026; current access via Jimeng/Doubao (China) or dreamina.capcut.com (global, free daily credits)
- Jimeng subscription: $9/month = 1800 credits + 60 daily free; Seedance 1.5 available now at ~10s/60 credits
- **Generation latency**: 2-10 hours on Jimeng (server queue) — not production-ready for high-frequency workflows

### 🆕 MatAnyone — Video Matting Without Green Screen

- AI system separating people/objects from video with fine hair and motion blur support
- No green screen required; highly precise matting for compositing
- **Digital-Stud relevance**: Post-processing node for cleanly isolating AI-generated characters for compositing into scenes

### 🆕 HY 3D 3.0 — Advanced Features in ComfyUI (March 10, 2026)

- Tencent HunyuanVideo 3D (HY 3D 3.0) Advanced Features now available via ComfyUI Partner Nodes
- Enables 3D asset generation tightly coupled with HunyuanVideo pipelines
- **Digital-Stud relevance**: 3D mesh output from video frames; potential integration with Blender workflow

### WanGP GGUF Quantization Guide (March 2026 Community Best Practices)

- **Wan2.2 I2V 14B Q6 GGUF**: Best quality/speed tradeoff; recommended as default for RTX 3090/4090 users
- **16GB VRAM** (RTX 4080, 5070 Ti): Use I2V 14B Q6; T2V works with int8
- **Wan2.2 T2V + LightX2V LoRA**: Working combo for motion effects; some artifact risk when stacking LoRAs
- **Warning**: Multiple LoRAs stacked on Wan2.2 → visual artifacts; use single LoRA per generation pass

### WanGP API — Headless Backend Service Mode (v10.987+)

- New **internal API** exposed for using WanGP as a backend video generation service
- **LTX Desktop WanGP**: reference app built on WanGP API; reduces VRAM floor from 32GB
- Enables batch/headless generation without GUI; scriptable via Python
- Digital-Stud relevance: pipeline-level video batch generation for automated character content

### 🆕 WanGP v10.987 (March 10, 2026)

- **Qwen3.5 VL Abliterated Prompt Enhancer**: 4B/9B + GGUF Q4/Int8 variants; uncensored prompt enhancement
- **GGUF CUDA Kernels**: 15% speed boost on diffusion video models; 3× faster LLM performance
- **LTX-2.3 improvements**: End-frame-only generation (reverse sequence), new GGUF checkpoints, reduced VAE banding
- **Export audio**: New MP4 AAC192-320 (lossy) and ALAC (lossless) format support
- **SVI PRO2 End Frames**: Sliding window extended sequence generation

### 🆕 WanGP v10.984 (mid-March 2026)

- **Index TTS 2 with emotion**: fear, sadness, disgust, happy, anger support
- **Multi-speaker dialogue mode** with voice cloning
- Incremental audio quality improvements between v10.981 and v10.987

### 🆕 WanGP v10.981 (March 7, 2026)

- Updated "GPU Poor" inference toolkit: LTX-2.3 day-0 support added
- New features: **Flux 2 outpainting**, **Qwen Image outpainting**, Lanpaint for Flux 2
- vLLM + int8 quantization for LM: fast + low VRAM (10GB RAM + some VRAM)
- Supports: Wan 2.1/2.2, Qwen Image, HunyuanVideo, LTX Video, Flux
- GitHub: `deepbeepmeep/Wan2GP` — recommended for low-VRAM local setups

### 🆕 WAN VACE Clip Joiner — Smooth AI Video Transitions (CivitAI, March 2026)

- ComfyUI workflow: creates seamless transitions between video clips using **Wan VACE** (Wan 2.2 Fun VACE or Wan 2.1 VACE)
- Input: any two video clips → Output: smooth in-between transition via VACE conditioning
- Compatible with: Wan-based outputs, LTX-2.3, HunyuanVideo, and any external video source
- CivitAI model ID: 2024299 | Available in ComfyUI Manager
- Digital-Stud relevance: bridges separate character animation clips into seamless sequences

### Wan2.2 — Priority Model for This Workflow

- MoE architecture, TI2V-5B: unified text+image → video, 720P/24fps, RTX 4090
- **Memory optimization (March 2026)**: improved efficiency; Wan2.1 LoRAs still compatible
- Extensions: `Wan2.2-Animate`, `Wan2.2-S2V`, `FLF2V`, **`Wan2.2-speech-to-video`** (lip-synced video from image + audio; distinct from S2V)
- [docs.comfy.org](https://docs.comfy.org/tutorials/video/wan/wan2_2) | Apache 2.0
- **⚠️ Performance note (March 2026)**: Community reports 33%+ increase in generation time after recent ComfyUI updates (same workflow, same settings) — check ComfyUI version before assuming hardware issue
- **WanGP** (github.com/deepbeepmeep/Wan2GP): GPU-poor fast inference tool; supports Wan2.1/2.2, HunyuanVideo, LTX, Flux; Q4_K quantized Wan2.2 14B runs on 8–10GB VRAM; **Quantization formats: int8, fp8, gguf, NV FP4, Nunchaku** (auto-downloads model for your specific GPU architecture)

### 🆕 Research Finding: Wan 2.1 1.3B vs 2.2 5B for Source Preservation (March 2026)

- arXiv 2511.01266v5 finding: **Wan 2.1 (1.3B) empirically outperforms Wan 2.2 (5B)** in preserving source structures during I2V
- Particularly relevant for user-interactive motion-controlled generation
- Practical impact: for character animation where source pose/appearance must be preserved, prefer Wan 2.1 1.3B
- For pure cinematic quality / prompt following without strict source fidelity: Wan 2.2 5B remains superior

### Open-Sora 2.0 — Cost Breakthrough

- Trained for only **$200,000** (5–10× cheaper than comparable models)
- Video DC-AE: **4×32×32 compression ratio**
- **5.2× improvement** in training throughput; **10×+ inference speedup**
- Performance gap with OpenAI Sora reduced from 4.52% → 0.69%
- Apache 2.0; arxiv 2503.09642

### Video API Pricing (March 2026)

| Provider | Model | Price/sec | Free Tier |
|----------|-------|-----------|----------|
| Replicate | Wan 2.2 A14B | ~$0.05/sec | Small credits |
| fal.ai | HunyuanVideo 1.5 | TBC | Signup credits |
| WaveSpeedAI | HunyuanVideo 1.5 | TBC | ⚠️ Capped at 480p currently |
| fal.ai | Kling 2.1 | ~$0.14/5s clip | Signup credits |
| fal.ai | Kling 2.6 | ~$0.14/clip+ | Signup credits |
| RunwayML | Gen-4.5 | ~$0.75/sec | 125 free credits |
| fal.ai | Veo 3.1 | $0.20–$0.60/sec | — |
| fal.ai | Sora 2 Pro | $0.30–$0.50/sec | — |
| WaveSpeedAI | 700+ models | Varies | Free trial |
| Google AI Studio | Veo 3.1 | Free (rate-limited) | Best free option |
| Google AI Studio | Veo 3.1 Fast | Free (rate-limited) | 45-60s per clip |

---

## 🧵 LoRA Training SOTA — March 2026

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

> **Community consensus (March 2026)**: OneTrainer increasingly preferred over AI-Toolkit for character LoRAs due to significantly less overfitting. musubi-tuner preferred for newer Flux variants.

> **Best practice (LoRA + ControlNet + IP-Adapter combo)**: New community documentation published March 2026 confirming three-way combo as production standard for pose + style + identity control simultaneously.

> **ComfyUI inpainting standard (March 2026)**: `comfyui-impact-pack` SEGS Detailer confirmed as production standard for targeted face/body inpainting within existing workflows. PersephoneFlux + DoomFlux combo emerging for layered character workflows.

> **Reflective Flow Sampling Enhancement** (arxiv 2603.06165, March 2026): New technique for flow-matching models (Flux). Improves sampling quality by incorporating reflective guidance — potentially applicable to ComfyUI custom samplers.

### 🆕 RF-Sampling — Training-Free Flow Model Inference Enhancement (arXiv 2603.06165)

- Drop-in **training-free sampler enhancement** for flow matching models (FLUX.2, LTX-2.3, Wan)
- Reflective flow sampling improves sample diversity + quality at inference time
- No re-training required; plug in as alternate scheduler/sampler in ComfyUI
- Digital-Stud relevance: free quality boost for all FLUX.2 and LTX pipelines

### Key Training Advances (March 2026)

- **LoRA+ (16× ratio baseline)**: Apply differential LR to LoRA-A and LoRA-B matrices — **~30% faster convergence**, better detail capture. Now the universal baseline in Kohya-ss v0.9.1+
- **Fused backward pass** (Kohya-ss v0.9.1+): SDXL training VRAM **24GB → 10GB** with bf16
- **T-LoRA** (arxiv 2507.05964): Timestep-Dependent Low-Rank Adaptation — dynamic rank-constrained updates per diffusion timestep + dynamic fine-tuning strategy. **Single-image character customization without overfitting**; drop-in for standard LoRA pipelines

### Dataset Preparation — Auto-Captioning Best Options (March 2026)

- **JoyCaption 2** (recommended): Best open-source BLIP/VLM-based captioner; detailed scene + style + character descriptions; runs locally
- **CogVLM**: Strong for detailed image captioning; slower than JoyCaption 2 but higher descriptive quality
- **Molmo** (Allen AI): Fast, good for batch captioning; less detailed on clothing/style attributes
- Recommendation for character LoRA: JoyCaption 2 → manual review of 20% samples → Kohya/AI-Toolkit training

### WD-Tagger v4 — Updated CLIP Tagger (March 2026)

- New v4 model weights: improved anime/style/character tagging accuracy
- Supports Danbooru, E621, Derpibooru tag sets
- Best for: style LoRA, anime character LoRA, NSFW-aware tag filtering
- Available in ComfyUI via WD14Tagger node (update node + weights)

### 🆕 NVIDIA Nemotron 3 Super 120B (March 11 2026)

- Open-weight hybrid MoE Mamba-Transformer; beats GPT-OSS and Qwen3.5 on throughput
- **5× higher throughput** vs equivalent dense models for agentic AI systems
- Supports overnight LoRA/QLoRA fine-tuning; open weights + datasets + recipes
- Digital-Stud relevance: potential fast LLM backend for prompt enhancement / captioning pipelines

### 🆕 LTX-2.3 LoRA Training — Status (March 2026)

- **Not yet officially supported**: No training scripts from Lightricks for LTX-2.3 as of March 12 2026
- Community experiments ongoing; Flimmer (DiT-native) may be the first viable path
- **Expected**: Community training configs within 2-4 weeks based on LTX-2.2 precedent
- **Digital-Stud action**: Monitor Lightricks repo + Flimmer releases; ready to generate training config when available

### 🆕 Face LoRA vs Face Swap — Recommendation (2026)

- **Face LoRA preferred** for identity-consistent character generation: better lighting/environment adaptation
- **Face swap (IPAdapter)**: Better for style/lighting injection over existing video; not identity-consistent across frames
- **IPAdapter + LoRA combo**: Apply LoRA for identity → IPAdapter for style reference → best of both
- For video: Face LoRA in Wan2.2/HunyuanVideo produces most temporally consistent identity

### 🆕 FLUX.2 LoRA on Consumer GPU — Recommended Config (March 2026)

- **network_dim**: 16–32 (32 for detailed character; 16 for style)
- **Optimizer**: Prodigy (auto-LR) or AdaFactor (stable); avoid Adam for VRAM-constrained setups
- **Steps**: 2000–4000 for character; 1000–2000 for style
- **VRAM**: 24GB target (RTX 4090/3090); <24GB → use gradient checkpointing + bf16
- **AI-Toolkit**: Recommended over Kohya for FLUX.2 LoRA; cleaner FLUX-native architecture

### Video LoRA — Updated March 2026

- **Video2LoRA** (arxiv 2603.08210): per-reference-video LoRA for semantic-controlled video gen
- **finetrainers** (CogVideoX factory): CogVideoX + Mochi video LoRA training
- **Flimmer** (**NEW March 2026**, Alvdansen Labs): Dedicated video LoRA toolkit for DiT transformers
  - Phased training with curriculum learning + MoE expert specialization for Wan2.2 dual-expert arch
  - Block swapping: ~0.67GB saved per block; Adam-mini optimizer + CPU offload
  - Wan2.2 I2V VRAM: approaching 24–40GB (from ~60GB unoptimized)
  - Supports Wan2.2 + HunyuanVideo; cleaner API than AI-Toolkit ZIT
- **AI-Toolkit ZIT**: Still viable; Flimmer emerging as preferred alternative
- **T-LoRA**: Single-image concept customization without overfitting (arxiv 2507.05964)

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

### LyCORIS / Alternative Architectures

| Method | File Size | Use Case |
|--------|----------|----------|
| **LoRA** | ~33–66MB | Standard; fast convergence |
| **LoKr** | ~few MB | Extremely compact; faster convergence; growing community interest |
| **LoHa** | Medium | Hadamard product; different parameter distribution |
| **GLoRA / GLoKR** | Varies | Generalized; more flexible parameter targeting |

---

### 📊 MLPerf Inference v6.0 — Video Generation Benchmark (March 10, 2026)

**First industry-standard benchmark for text-to-video generation:**
- **Reference model**: Wan2.2-T2V-A14B-Diffusers (BF16)
- **Framework**: VBench with 6 metrics: Subject Consistency, Background Consistency, Motion Smoothness, Dynamic Degree, Appearance Style, Scene Quality
- **Target**: 720p×1280p @ 16fps (81 frames), 100 samples
- **Reference accuracy**: 70.48 VBench score (minimum threshold 69.77 = 99%)
- **Scenario**: SingleStream (not Server — videos take minutes per generation)
- **Significance**: Wan2.2 is now the industry reference model for video generation perf benchmarking

---

## 🏃 Pose Estimation SOTA — March 2026

### 🆕 PoseRWGCN — Attention-Free RWKV-GCN Real-Time 3D Pose (Mar 9 2026)

- First use of **RWKV linear-time temporal modeling** for 3D human pose estimation
- Dual-stream: RWKV temporal + GCN spatial — avoids quadratic transformer cost
- Causal mode = real-time inference; bidirectional mode = offline video analysis
- Benchmarked on Human3.6M + MPI-INF-3DHP; outperforms attention baselines in efficiency
- Open access: Complex & Intelligent Systems, DOI 10.1007/s40747-026-02239-x

### 🆕 TAR-ViTPose — Temporal Aggregate-and-Restore for Video (arXiv 2603.05929, Mar 2026)

- Extends ViTPose with **multi-frame aggregation** for video-level pose consistency
- **+2.3 mAP gain** over single-frame ViTPose on COCO benchmark
- Aggregate-and-restore: collects temporal context then reconstructs per-frame accuracy
- Practical use: character pose tracking in video with reduced jitter vs per-frame inference

### 🆕 tttLRM — Test-Time Training for 3D Gaussian Splat Reconstruction (CVPR 2026)

- **Adobe + UPenn** researchers — open-source: github.com/cwchenwang/tttLRM
- Input: set of photos → Output: high-quality **3D Gaussian Splats** with iterative refinement
- Test-time training: model adapts to each new scene at inference → better per-object accuracy
- Handles long-context multi-image sets (autoregressive 3D reconstruction)
- Digital-Stud relevance: consumer photo → production-grade 3D asset pipeline; bridges character photography to 3D rigging

### 🆕 SuperHead — Animatable 3D Head Avatars from Low-Quality Input (CMU, March 10 2026)

- Framework: transforms **smartphone/webcam footage** into high-fidelity animatable 3D head avatars
- Multi-view supervision with sparse upscaled 2D face renders + depth maps for geometric accuracy
- Supports: GaussianAvatar + SplattingAvatar representations
- Benchmarked on NeRSemble + INSTA datasets; strong realism improvement over baselines
- CMU XR Technology Center: cmu.edu/xrtc/news/2026/march/superhead.html
- Digital-Stud relevance: single webcam session → animatable 3D character head for rigging or video generation

### Model Comparison

| Model | Type | Keypoints | Accuracy | Speed | Best For |

### 📄 New Research: Controllable Complex Human Motion (arxiv 2603.08028, March 12 2026)

- **Text-to-motion-to-video pipeline**: Text prompt → motion sequence → video generation
- **Dataset**: 90/10 train/test split on complex human motion sequences
- **Integration**: Complements DWPose/RTMPose extraction in ComfyUI ControlNet workflows
- **Relevance**: Enables more nuanced character motion control beyond static pose matching

|-------|------|-----------|----------|-------|----------|
| **YOLO26-Pose** | Single-stage, NMS-free | 17 (COCO) + custom | mAP 57.2% (nano) to 71.6% (XL) | 30+ FPS; **43% faster CPU than YOLO11-N** | Real-time multi-person; custom keypoints; MuSGD optimizer |
| **ER-Pose** | Keypoint-driven single-stage (arxiv 2603) | 17+ custom | +3.2 AP (no pretrain) / **+7.4 AP (with pretrain)** vs YOLO-Pose | Fast | Removes bounding-box supervision entirely; keypoint-driven dynamic sample assignment aligned with OKS; smooth OKS loss function; fewer params than YOLO-Pose |
| **RTMPose-m** | Two-stage, SimCC head | 17–133 | **75.8% AP on COCO** @ 90+ FPS (Intel i7) | 30+ FPS | Production speed/accuracy balance; 430+ FPS on GTX 1660 Ti |
| **DWPose-l** | Two-stage whole-body distillation | 133 (body+hand+face) | Whole AP 66.5% (COCO-WholeBody) | Medium | **Best for ComfyUI ControlNet** |
| **ViTPose / ViTPose++** | ViT-based | 17–133 | Highest mAP | Slower | Research; multi-dataset training |
| **PoseSynViT** | Lightweight ViT (CVPR 2025W) | 17–133 | **84.3 AP on MS COCO** (largest model) | Medium | Scales 10M–1B params; knowledge token for cross-scale transfer |
| **DETRPose** | DETR end-to-end transformer | 17–133 | Competitive/superior to CNN alternatives | Real-time | **5–10× faster training** than CNN; no NMS; pose denoising (positive + negative queries); arxiv 2506.13027 |
| **HEViTPose** | Hybrid ViT (CGSR-MHA) | 17–133 | **90.7% MPII / 72.6% COCO** | Medium | NEW 2026 SOTA efficiency; superior perf-per-param vs HRNet |
| **Sapiens2** | Foundation (0.4–5B) | 308 body + face | SOTA whole-body | Slow | SOTA whole-body, 1K–4K, multi-task; ICLR 2026 |
| **MediaPipe Holistic** | Lightweight | 33+21/hand+468 face | — | 30+ FPS mobile | Mobile/browser; zero server cost (client-side JS SDK) |
| **SDPose-OOD** | Robust (SD U-Net) | 133 | Parity with Sapiens-1B/2B at 1/5 training | Medium | ComfyUI native (Mar 8, 2026); superior OOD generalization |
| **RF-DETR** | DINOv2 transformer (ICLR 2026) | — | SOTA real-time detection + segmentation | Real-time | Roboflow; object detection + instance seg; **useful as detection backbone before pose** |

> **YOLO26-Pose key facts**: NMS-free end-to-end inference; non-human keypoint support for custom schemas; ProgLoss + STAL for small/occluded targets; MuSGD optimizer from LLM training (5-10× faster training). ⚠️ YOLO26 not yet supported in C++ inference examples (Ultralytics v8.4.21) — Python only.

> **DETRPose** (arxiv 2506.13027, June 2025): First real-time DETR-style multi-person pose estimation. Pose denoising: generates both positive and negative query samples for faster convergence. 5–10× faster training than CNN alternatives. Outperforms YOLO11-X and YOLOv8-X on COCO and CrowdPose with fewer parameters.

> **RF-DETR** (Roboflow, ICLR 2026): DINOv2-based real-time transformer for object detection + instance segmentation. Useful as backbone for person detection stage before pose estimation pipeline.

### New: HTP Framework — 3D Video Pose Efficiency (2026)

- **Hierarchical Temporal Pruning** for diffusion-based 3D pose estimation
- **38.5% training MACs reduction, 56.8% inference MACs reduction, 81.1% speed improvement**
- Three-stage: TCEP → SFT MHSA → MGPTP
- SOTA on Human3.6M and MPI-INF-3DHP

### StableGen — Blender 3D Generation & Texturing Plugin (Updated March 5, 2026)

- AI-powered 3D generation and texturing directly inside Blender via ComfyUI backend
- Supports ControlNet-guided texture baking and mesh-aware generation
- GitHub: https://github.com/sakalond/StableGen
- **Digital-Stud relevance**: Direct Blender→ComfyUI bridge for character texturing workflows

### Yedp Action Director v9.2 — Major Update (March 2026)

- **FBX/GLB/BVH file loading** from Mixamo and other animation sources
- Accurate ControlNet conditioning image export from 3D animations; up to 8K resolution input
- **Key for this workflow**: load DAZ/Blender animations → precise pose-guided video gen in ComfyUI
- Build 155 - SubBuild 2026.3.3

### DWPose — Best for This Workflow (ComfyUI)

- 133 whole-body keypoints; standard ControlNet preprocessor
- Node: `comfyui_controlnet_aux`; model: `DWPose-dw-ll-ucoco-384.pth`
- Significantly outperforms OpenPose for hand/face accuracy
- Whole AP task breakdown: Body 72.2%, Foot 70.4%, Face 88.7%, Hand 62.1%
- ⚠️ Known issue: DWPose Estimator node re-downloads model on each reopen in some setups — use OpenPose node as fallback if needed

### Any-Pose Portrait Editing Workflow (NEW March 2026)

```
3D character rig (DAZ/Blender) → pose → Qwen Image Edit → face fix → Flux 2 Klein 4K upscale
```
- New official ComfyUI template; any-pose from 3D → portrait with identity preservation
- Combines Z_Image pose extraction + Qwen Edit + Flux 2 Klein upscaling

### 🆕 Bumblebee — Long-Sequence Motion Generation (Seoul, March 2026)

- Korean AI startup; developed a generative model for **long-sequence character motion**
- Targets film/TV production; content deals for global market in progress
- Differentiator: temporal coherence across long sequences vs single-shot video models
- Digital-Stud relevance: could bridge gap between pose-guided single clips and full scene choreography

### 🆕 Any-Pose Portrait Editing Workflow (Confirmed Details)

- **Two-stage cascaded framework** (arXiv 2603.08028): Stage 1 — autoregressive text-to-skeleton model generates 2D pose sequence from text; Stage 2 — pose-conditioned video diffusion
- **"Text-to-Skeleton Cascade"** approach addresses training data scarcity for human motion generation
- **Digital-Stud relevance**: Type in motion description → get pose sequence → feed to Wan/LTX → character video

### 🆕 Depth Anything 3 (DA3) — ICLR 2026, Human-Like Spatial Perception

- Presented at **ICLR 2026** (previously noted as March 2026 release)
- Goal: recovering complete visual space from any viewpoints ("human-like" spatial perception)
- Succeeds Depth Anything V2; improved multi-view consistency and edge sharpness
- Companion work: **DepthLM** — metric depth from Vision Language Models (ICLR 2026)
  - Achieves **pixel-level metric depth** without architectural changes to VLMs
  - Enables metric depth estimation from any VLM (Gemini, GPT-4V, etc.) as a plug-in
- ComfyUI: available as DepthAnything3 custom node (check registry); DA2 nodes accept DA3 weights
- Digital-Stud: better depth conditioning for ControlNet poses + 3D scene reconstruction



- Unifies monocular + multi-view geometric constraints; production-deployed in ROS2, video plugins
- **Recommendation**: use V3 for depth-conditioned ControlNet maps; use Depth Pro for metric accuracy
- Available: HuggingFace `depth-anything/Depth-Anything-V3-*`; included in Depth Scanner 2 AE plugin
- Outperforms Depth Anything V2 on consistency; Depth Pro still sharper for absolute metric tasks

### 🆕 CyanPuppets — 1B-Param Blender/UE5 AI Motion Capture (March 2026)

- Converts camera footage / uploaded video → real-time 3D motion data (Blender + Unreal Engine)
- 1B-parameter model; MetaHuman interface compatible; no mocap suit required
- Digital-Stud pipeline fit: generate portrait image → refine with LoRA → CyanPuppets for 3D motion → video

### 🆕 SIMSPINE — 3D Spine Motion from Ordinary Video (March 2026)

- Extracts vertebral-level 3D spine motion from standard video (monocular, no sensors)
- Novel granularity beyond full-body pose (DWPose/OpenPose miss spinal detail)
- Research code available; paper: arXiv / Instagram @DVnK9m-Gl1I

### 🆕 KDMR — Kinodynamic Motion Retargeting (arXiv 2603.09956, March 10 2026)

- Humanoid locomotion retargeting via multi-contact whole-body trajectory optimisation
- Enforces rigid-body dynamics + contact complementarity constraints vs kinematic-only (GMR) baselines
- Auto heel-toe contact detection; integrates GRF measurements; outperforms GMR
- **Pipeline open-sourced upon publication** — watch arXiv 2603.09956
- Digital-Stud relevance: physics-accurate character motion retargeting from video/mocap sources

### 🆕 Alibaba-PAI FLUX.2-dev-Fun-Controlnet-Union (Updated Feb/Mar 2026)

- HuggingFace: `alibaba-pai/FLUX.2-dev-Fun-Controlnet-Union`
- Control types: **Canny, HED, Depth (Midas), Pose (OpenPose), MLSD, Scribble, Gray**
- Two versions: standard + **`Union-2602.safetensors`** (improved Scribble/Gray + CFG distillation post-training)
- **Recommended scale**: controlnet_conditioning_scale 0.65–0.80
- Supports inpainting mode + multi-condition control in one model
- Klein variant: **FLUX.2 Klein ControlNet** (Pose + Depth + LineArt) — dedicated ComfyUI workflow available (YouTube: Flux 2 Klein Control Net ComfyUI)

### ControlNet-Union FLUX — Pose Conditioning Quality Guide

- **OpenPose**: Still widely recommended for ComfyUI FLUX workflows; fast, well-tested
- **DWPose**: Higher quality keypoint extraction, more accurate joint positions; slower
- Recommendation: Use DWPose for hero shots / final renders; OpenPose for rapid iteration
- **ControlNet-Union**: Combines depth + pose + edges in single pass; supported in FLUX.2 ComfyUI ecosystem

### 🆕 NLF_pose — Blender Rig for Wan SCAIL-Pose Workflows

- Bone-based rigging system in Blender compatible with Wan video generation and SCAIL-pose ComfyUI nodes
- Full pipeline: rig in Blender → export pose → SCAIL-pose node → Wan2.2 video
- Covered in Alex Villabón VFX+AI newsletter #027 (March 2026), alongside Flux.2 Klein 360° panorama LoRA and Wan2.2 4× frame interpolation
- **Digital-Stud relevance**: Core bridge between 3D (Blender) and AI video (Wan/SCAIL)

### 🆕 HuMo — Human-Object Interaction Video Generation (arXiv 2603.09883)

- Multi-subject video generation conditioned on reference object + human images + text prompt
- Generates Human-Object Interaction (HOI) videos with precise, directable interactions
- **Digital-Stud relevance**: Character-prop interaction generation without manual animation setup

### ComfyUI Pose Nodes Ecosystem

| Node / Tool | What It Does |
|-------------|-------------|
| `comfyui_controlnet_aux` | DWPose, OpenPose, MediaPipe preprocessors |
| `Yedp Action Director v9.2` | FBX/GLB/BVH → ControlNet conditioning (NEW) |
| `ComfyUI Open Pose Editor` | Visual skeleton editor |
| `ComfyUI-SCAIL-Pose` | Advanced pose processing |
- **Z-Image Turbo — Face Detailer for ComfyUI** (nextdiffusion.ai, March 2026)
  - Auto-detects faces in generated images → builds mask → enhances face detail in 8 steps
  - Requires only 3 model files; works with FLUX.2 Dev and SD4
  - Tutorial: nextdiffusion.ai/tutorials/how-to-use-z-image-turbo-as-a-face-detailer-in-comfyui

- **SCAIL ComfyUI Tutorial** (nextdiffusion.ai, March 2026) — End-to-end guide: install, pose injection, Wan2.2 character animation workflow; covers 3D-consistent motion from pose sequence
| `ComfyUI-SDPose-OOD` | Robust OOD pose estimation |
| `Ubisoft CHORD` | Character pose reference + image editing |
| `Pose Studio Node` | One image → infinite pose variations |
| `Save Pose Keypoints Node` | Export keypoints for reuse |

---

## 🛠️ ComfyUI Ecosystem — Notable Nodes/Updates (March 2026)

### 🆕 ComfyUI v0.16.1 (March 5, 2026) — New Nodes & Features

- **ResolutionSelector** node with aspect ratio presets; **CURVE** type for parameter control; **BBox** widget for precise region selection
- **3-band EQ** audio node; **GLSL shader** node (PyOpenGL); **ElevenLabs API** text-to-speech nodes
- **Model support**: LTXAV 2.3, LongCat-Image (native), ACE-Step 1.5, **SDPose-OOD** pose models
- **Wan2.2 Animate** (v0.16 changelog): Native ComfyUI support for Wan2.2 Animate model — enables character replacement and motion transfer directly in ComfyUI workflow nodes
- **Veo3 video generation** node (audio-visual synthesis); **Moonvalley V2V** (video-to-video); **Rodin3D Gen-2** (image-to-3D API)
- **Dynamic VRAM now default** — massive RAM reduction on NVIDIA hardware (Windows + Linux)
- **Sage Attention (KJ-Nodes)**: `Patch Sage Attention` node from ComfyUI-KJ-Nodes confirmed as best attention mode for video generation & high-res workflows (March 2026); lower VRAM than Flash Attention, better than xFormers for long sequences
- **⚠️ OOM regression**: v0.16.3/0.16.4 reports CUDA OOM errors on some setups (GitHub #12823) — check version before upgrading
- **Comfy Cloud out of beta**: 90% of local custom nodes accessible; Workflow API deployment (production APIs from workflows) coming soon

### 🔄 Community Workflow Patterns (March 2026)

- **Flux2 Klein face-swap + LoRA chain**: Expression-preserving face swap via Klein base + LoRA refinement; `ComfyUI-KJ-Nodes` Patch Sage Attention + Klein LoRA = production face-swap standard
### 🆕 Announced: LTX 3.0 (Next-Generation, via LTX Studio)

- **LTX 3.0**: Next-gen long-form, high-fidelity video model announced via LTX Studio
- Focus: Extended duration, higher fidelity, production-ready video generation
- Status: Announced — release timeline TBD; successor to LTX-2.3

- **LTX 2.3 native portrait support**: Up to 1080×1920 resolution for mobile-first/vertical content; rebuilt VAE with improved latent space for sharper textures; larger text connector for better multi-subject prompt understanding; reduced "Ken Burns" freezing effect in I2V mode
- **LTX 2.3 quality tip**: Shorter clips (<10 seconds) measurably improve visual quality — confirmed by community testing (r/comfyui, Facebook ComfyUI group, March 2026)
- **Multi-model routing pattern**: NB Pro for volume ($0.039), NB2 for premium ($0.067/1K), GPT Image 1.5 for text-critical; production teams adopting dynamic model selection
- **Qwen/FireRed Image Edit workflows**: Multi-reference editing + restoration chains; `qwen_2511_restore` has compatibility issues after recent ComfyUI updates (black image bug)

### 🆕 Major: Hunyuan 3D Advanced Features in ComfyUI (March 2026)

- **3D Parts Decomposition**: Split 3D assets into editable, modular components directly in ComfyUI via Partner Nodes
- **UV Unwrapping**: Automatic UV layout generation for easier texturing pipelines
- **Smart Topology**: Convert dense geometry into cleaner, production-ready meshes
- **Workflow integration**: Ready-to-run workflows available on Comfy Cloud — useful for Digital-Stud character asset prep

### ComfyUI Desktop v0.8.x Release Cadence (March 2026)

- **v0.8.18** (Mar 7): bundles core 0.16.4; fixes compiled-bad-node regression
- **v0.8.16** (Mar 6): core 0.16.3; audio encoder stability
- **v0.8.15** (Mar 5): general stability pass
- Cadence: ~2 releases/week — always update before LTX-2.3 / Wan2.2 workflows
- To use core 0.16.4 in Desktop 0.8.16: update internal component separately (GitHub issue #12828)

### 🆕 NVIDIA NVFP4 / FP8 — ComfyUI Native Quantization (GDC 2026)

- **FLUX.2 Klein 4B & 9B NVFP4 weights**: available now (NVIDIA RTX AI Garage)
- **LTX-2.3 NVFP4**: coming soon
- **Speed/VRAM gains (RTX 5090)**:
  - NVFP4: **2.5× faster, 60% lower VRAM**
  - FP8: **1.7× faster, 40% lower VRAM**
- WanGP addition: NVFP4 for LTX-2 & FLUX.2; +30% speed on RTX 50xx w/ PyTorch 2.9.1 / CUDA 13
- Load directly from HuggingFace via ComfyUI Template Browser
- Digital-Stud relevance: run FLUX.2 Klein 9B on 8GB VRAM cards with NVFP4

### 🆕 Major: App Mode, App Builder & ComfyHub (March 10, 2026)
- **ComfyUI v0.16.1 / v0.16.2** — LTX-2.3 native support; Desktop v0.8.15 bump; resolves `split_with_sizes` prompt error
- **Template Library**: One-click model download per workflow; accessible via gear icon in ComfyUI interface

- **App Mode**: One-click transform any workflow into a clean non-technical UI
- **App Builder**: Configure which inputs/outputs to expose; rename/reorder without touching nodes
- **Shareable App URLs**: Distribute complete workflows as single URLs; run in-browser via Comfy Cloud
- **ComfyHub**: Public marketplace at comfy.org/workflows (preview March 10)

### 🆕 Major: Subgraph Feature

- Package **complex node combinations into single reusable subgraph nodes**
- Enables sharing of composable pipeline components
- Subgraph Blueprints installable via `comfyui-workflow-templates` PyPI package

### 🆕 Major: ComfyUI MCP Server

- **MCP server** (io-ateliertech/comfyui-mcp): Comprehensive workflow automation and management via Model Context Protocol
- Enables programmatic ComfyUI control from any MCP-compatible client (Claude Desktop, etc.)
- Supports workflow execution, image generation, model management remotely

### 🆕 Major: Comfy Cloud Out of Beta (March 2026)

- **Powered by NVIDIA Blackwell RTX 6000 Pro** (96GB VRAM, 180GB system RAM)
- Pay-per-use billing; ~90% of local custom nodes available cloud-side
- Free tier: 400 credits/month, no credit card
- **LTX-2.3 on Blackwell**: 3× faster than comparable cloud GPUs

### 🆕 Major: AMD ROCm 7.1.1 Native Integration

- One-click ComfyUI installer for AMD hardware
- **5.4× performance improvement** over ROCm 6.4
- AMD Radeon RX 9000 Series GPUs fully supported

### OpenClaw 2026.3.2 — ComfyUI Manager Update

- New release of OpenClaw (ComfyUI Manager fork) adds node versioning support — addresses the long-standing "workflow breaks after update" problem (r/comfyui discussion, March 2026)
- Enables pinning specific node versions per workflow, improving reproducibility



### 🆕 Paper: HHMotion — Motion Turing Test (arXiv 2603.06181)

- Dataset: 1,000 video clips from 11 humanoid robot models + 10 human subjects; all converted to SMPL-X
- Introduces human-likeness evaluation (0–5 scale, 15 action categories, 500+ annotation hours)
- Key finding: Humanoid robot motions still distinguishable from human — dynamic actions (boxing, jumping, running) are hardest to fake
- **Digital-Stud relevance**: Benchmark for evaluating realism of pose-driven character animations


### 🆕 Paper: FootMR — 3D Foot Motion Refinement (arXiv 2603.09681)

- Refines foot motion estimated by existing human recovery models via 2D foot keypoint lifting
- Generalizes to extreme foot poses; SOTA on MOYO, RICH, and MOOF benchmarks
- Improves ankle/foot precision in markerless monocular motion capture
- **Digital-Stud relevance**: Higher-fidelity whole-body animation including feet for character workflows

### 🆕 Paper: ConfCtrl — Camera Control for Video Diffusion (arXiv 2603.09819)

- Enables **precise camera trajectory control** in video diffusion models via Confidence-Aware Interpolation
- Predict-Update (Kalman-inspired) architecture for handling uncertainty in 3D geometric priors
- Jointly encodes projected point clouds + camera poses for novel view synthesis
- Complements DWPose-driven character workflows by adding camera motion on top of pose control

### 🆕 New Node: ComfyUI-Qwen3-TTS (March 9, 2026)

- Text-to-speech node available via ComfyUI Easy Install (released March 9)
- Includes automatic SoX installation; enables direct audio generation in ComfyUI video/animation workflows

### 🆕 New Node: ComfyUI-AudioX (March 10-11, 2026)

- Generate sound effects and background music directly from video input inside ComfyUI
- Powered by HKUSTAudio/AudioX model (similar to MMAudio family)
- Requires ≥16GB VRAM; GitHub: `jinxishe/ComfyUI-AudioX`
- **Digital-Stud relevance**: Audio-video synchronized generation for character animation outputs


### 🆕 Trainer: Ktiseos Nyx Trainer (Alpha, March 2026)

- Web-based LoRA training interface built on Kohya SS; Next.js + FastAPI stack
- 132+ configurable parameters; supports SDXL, SD1.5, Flux, SD3/SD3.5, Lumina
- LoRA variants: Standard, LoCon, LoHa, LoKr, DoRA
- Drag-and-drop dataset prep with auto-tagging (WD14); real-time browser logging; HuggingFace upload
- Runs on VastAI / RunPod; minimum 12GB VRAM (24GB for SDXL)
- **Digital-Stud relevance**: Accessible alternative to local Kohya install for cloud-based LoRA training

### 🆕 Trainer: SECourses Musubi Tuner v27.6 (March 8, 2026)

- Updated LoRA training app with improved quantizer; adds **FLUX 2 Dev** support
- Minimum 18GB VRAM with torch compile optimization
- GUI-based workflow for local FLUX LoRA training without CLI

### 🆕 New Node: nLoRA × nPrompt Batch Trainer (March 2026)

- ComfyUI node enabling `n` LoRA models × `n` prompts batch generation for trainer workflows
- Useful for rapid LoRA quality evaluation across multiple checkpoints without manual swapping
- Available via ComfyUI Node Manager

### ⚠️ Known Issue: SeedVR2 Node Crash (ComfyUI Portable)

- SeedVR2 nodes cause Windows fatal exception (`access violation`) in ComfyUI Portable
- Workaround: Use full Python installation; avoid Portable until fix is released

### 🛠️ ComfyUI–Houdini Bridge (March 2026)

- Integration tool by Rafael Drelich & Anatolii I. connecting ComfyUI and Houdini
- Enables terrain generation and procedural 3D scene creation with AI assistance
- **Digital-Stud relevance**: Procedural 3D + AI texturing pipeline potential

### 🆕 Major: NVIDIA RTX Acceleration (GDC 2026, March 10)

- **RTX Video Super Resolution node**: Real-time 4K upscaling, 30× faster than alternatives
- **NVFP4**: Flux 2 Klein (4B+9B) + LTX-2.3 — 2.5× faster, 60% lower VRAM on RTX 50 Series
- **FP8**: 1.7× faster, 40% VRAM reduction (any RTX GPU)

### 🆕 Major: Node Replacement API

- Official migration paths for deprecated/renamed nodes — prevents workflow breakage
- Full REST API for retrieving registered replacements; input/output remapping

### 🆕 Major: ElevenLabs Partner Nodes (March 9, 2026)

- TTS, Voice Cloning, Audio Transcription, Voice Isolation, Multi-Speaker Dialogue, Sound Design
- Full multimodal pipeline: Prompt → Image → Video → Voiceover — all inside ComfyUI

### Version History (March 2026)

| Version | Date | Key Additions |
|---------|------|---------------|
| v0.16.4 | Mar 7, 2026 | Bug fixes, stability; latest stable release |
| v0.16.1 | Mar 5, 2026 | Kling 3.0 Motion Control, LTXAV 2.3, WAN 2.6, Kandinsky 5.0, Veo 3.1 nodes, Dynamic VRAM default |
| v0.16.0 | Mar 5, 2026 | ResolutionSelector, CURVE type, LongCat-Image, SDPose-OOD, SCAIL WAN, Z-image support |

### Other Notable Nodes/Updates

- **LTX-2.3 native support** — day-0; IAMCCS nodes for 1080p on low-VRAM GPUs; ⚠️ LTX Desktop may outperform ComfyUI out-of-box — proper workflow config needed
- **Yedp Action Director v9.2** — FBX/GLB/BVH → ControlNet conditioning (Build 2026.3.3)
- **comfyui-rmbg v2.9.4** — ⭐ Split into three focused modules: Basic Character, Skin Details, Style and Pose
- **HunyuanImage-2.1** — 3D Parts Decomposition, UV Unwrapping, Smart Topology via Partner Nodes
- **SageAttention 2++** — Advanced attention optimization (requires CUDA Toolkit + MSVC)
- **ComfyUI-Manager integrated** into core ComfyUI (no separate install)
- **Wan2.2 native support** — official templates; memory optimization update
- **IP-Adapter** — Updated for Flux
- **ControlNet Flux nodes** — pose, depth, canny
- **CHORD (Ubisoft, open-sourced)** — Character pose reference + image editing
- **Kling 3.0 Motion Control** — ComfyUI partner nodes
- **Qwen Image ControlNet + LoRA** — DiffSynth support; EasyCache KV-cache efficiency
- **FLUX Image to Video** — Flux-native I2V, March 2026
- **Flimmer** — Dedicated video LoRA toolkit for DiT models (Wan2.2, HunyuanVideo)

### Official Workflow Templates (March 2026)

Available at comfy.org/workflows:
- Z-Image-Turbo Text to Image
- Wan 2.2 14B Image to Video
- Nano Banana Pro / Nano Banana 2 Image Edit
- Grok: Image Edit / Grok: Text to Image / Grok: Video generation
- Qwen Image Edit (2509, 2511, 2512 variants)
- Any-Pose Portrait Editing (3D char → Qwen Edit → Flux Klein 4K) ⭐ NEW
- LTX-2.3 audio-video workflows
- Kling 3.0 Motion Control workflows

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

## 💰 Nano Banana 2 Pricing Details (Verified March 2026)

| Resolution | Official Price | 3rd-Party (APIYI) |
|------------|---------------|-------------------|
| 512px | $0.045/img | $0.018/img |
| 1K (1024×1024) | $0.067/img (+72% vs NB Pro) | $0.025/img |
| 2K | $0.101/img | ~$0.037/img |
| 4K | $0.151/img | ~$0.054/img |

- Official API input tokens: $0.50/M (up from $0.30 for NB Pro)
- Fal.ai promotional discounts up to 55% OFF (March 2026)
- Adobe Firefly now bundles **25+ AI models** including NB2, GPT Image 1.5, FLUX.2 — commercial indemnification on all

---

## 🔑 Key APIs Summary

| Platform | Specialty | Free Tier | URL |
|---------|-----------|-----------|-----|
| fal.ai | Fastest inference, 1000+ models | Signup credits | https://fal.ai |
| Replicate | Largest open-source library | Small trial credits | https://replicate.com |
| Together AI | Open model hosting | $5 signup credit | https://together.ai |
| HF Inference API | Community models, serverless | Free (rate-limited) | https://huggingface.co |
| WaveSpeedAI | 700+ models unified API | Free trial | https://wavespeed.ai |
| Gemini API | Nano Banana 2 / Gemini 3 Pro image gen | Free tier; **1,500 img/day via Flash** | https://ai.google.dev |
| SiliconFlow | Flux Schnell + open models | Free tier | https://siliconflow.cn |
| BFL (Black Forest Labs) | Flux 2 series (v1.0 + v1.1), Flux I2V | — | https://api.bfl.ai |
| Adobe Photoshop | Flux.2 Pro + Runway Gen-4.5 integration (March 10 AI Assistant launch) | — | https://adobe.com/photoshop |
| Google AI Studio | Veo 3.1 / 3.1 Fast video + image | Rate-limited daily | https://aistudio.google.com |
| Kling AI | Kling 2.6/3.0/O3 video | ~6 videos/day | https://app.klingai.com |
| OpenAI | GPT Image 1.5, Sora 2 Pro | ~$5 trial | https://platform.openai.com |

---

*Next update: 30 minutes. This file is machine-generated by the digital-stud SOTA pipeline.*


> **Sora integration note (March 11, 2026)**: OpenAI announced plans to embed Sora video generator directly into ChatGPT, per The Information report.


### 🆕 Research: Brown University Multi-Robot Motion Generation (March 2026)

- New AI model from Brown University generates motion for diverse robot types (humanoids, quadrupeds, animated figures) from simple text/motion inputs
- **Relevance**: potential downstream synergy with pose-driven character animation pipelines



### 🆕 Research: Meta-LoRA — Domain-Aware Face Identity Personalization (March 2026)

- Three-layer structured LoRA for face identity: **Meta-Down** (identity-agnostic domain priors) → **Mid/Up** (identity-specific fine-tuning)
- Meta-trained across multiple identities to establish shared facial feature manifold
- Single-image fine-tuning sufficient; achieves **~95% identity retention**
- Benchmark dataset: **Meta-PHD** — diverse identities with varied poses, lighting, backgrounds
- Tested on FLUX.1-dev; outperforms standard LoRA on face similarity metrics
- **Digital-Stud relevance**: Directly applicable to character face consistency in Flux-based pipelines

### 🆕 Reference: FLUX.2 LoRA Training Complete Guide (March 2026)

- By Kevin Gabeci (built serverless LoRA training infra at Apatero)
- Key insight: Flux training fundamentally differs from SD due to architecture changes; optimal settings validated over hundreds of runs
- Practical tiers: Google Colab T4 (free, slow), Vast.ai/RunPod ~$1/hr (dev), FP16 reduces VRAM floor
- **HunyuanVideo LoRA speed**: 400 steps / 100 epochs = **1h37min** — ~50% faster than LTX LoRA (requires 4,000 steps)
- Multi-LoRA compositing in ComfyUI: stack character + style LoRAs for txt2vid and v2v workflows

### 🆕 Research: HY-WU — On-the-Fly LoRA for HunyuanVideo (Tencent, March 2026)

- **HY-WU** (Hunyuan Weight Update): Scalable framework for on-the-fly conditional generation of low-rank (LoRA) updates
- Synthesizes instance-conditioned adapter weights without retraining the base model
- GitHub: `Tencent-Hunyuan/HY-WU`
- **Digital-Stud relevance**: Real-time identity/character adaptation for HunyuanVideo without full LoRA training cycle


---

## 🆕 arXiv Papers — March 11-12, 2026

### V2M-Zero — Zero-Pair Video-to-Music Generation (arXiv 2603.11042)

- Generates music that **temporally aligns with video events** without paired training data
- Addresses key limitation of text-to-music models lacking fine-grained temporal control
- **Digital-Stud relevance**: Post-processing step to add synchronized music to AI video outputs

### COMIC — Agentic Sketch Comedy Generation (arXiv 2603.11048)

- Fully automated pipeline producing short comedic videos (SNL-style sketch comedy)
- Uses LLM agents for scripting + video diffusion for scene generation
- Demonstrates multi-shot narrative video generation from pure text intent

### DiT4DiT — Coupled Video + Action Diffusion Transformer (arXiv 2603.10448)

- Couples a **video DiT** with an **action DiT** in end-to-end joint training (Vision-Language-Action framework)
- Bridges video generation and robot/character action modeling
- **Digital-Stud relevance**: Foundation for future pose-conditioned character action video generation


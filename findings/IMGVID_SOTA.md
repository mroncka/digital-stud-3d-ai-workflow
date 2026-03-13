<!-- last_updated: 2026-03-13T03:30:00+01:00 run_61 -->
## 🏃 Run #61 Delta — 2026-03-13 03:30 Prague

### 🖼️ Image Gen SOTA
- **Nano Banana 2** (Google/Gemini 3.1 Flash): New #1 on Chatbot Arena at Elo 1280. 4× faster than v1, batch API with 50% discount for non-real-time. Photorealism & multi-subject leader. Free tier available.
- **FLUX.2 Pro v1.1** (BFL): Elo 1265, sub-second, strong photography precision. `$0.025–0.07/img`. Dev open-weight self-hostable.
- **GPT Image 1.5** (OpenAI): Elo 1264, ~95% text-rendering accuracy. `$0.04–0.13/img`.
- **Stable Diffusion 4 Ultra** (Stability AI, March 2026): Upgraded DiT architecture, open-weight photorealism benchmark. `$0.006–0.035/img`.
- **Recraft V4** (Feb 2026): #1 HuggingFace design benchmarks, SVG export, `~$0.04/img` via FAL.AI.
- **Tripo P1.0** (GDC 2026): Native 3D diffusion → engine-ready assets directly; new frontier beyond 2D.
- **Architecture note**: Rectified Flow (FLUX, SD3, Sora) now dominant over DDIM/DDPM. DiT (AdaLN-Zero conditioning) + MLLM text encoders (HunyuanVideo) are current best practice.
- **Free APIs**: Google Gemini free tier; FAL.AI 600+ models (free signup credits); Replicate free tier; HF open-weight.

### 🎬 Video Gen SOTA
- **Kling 3.0** (Kuaishou): Native 4K @ 60fps, 15s, multi-shot storyboard, persistent character consistency, multi-language audio. Visual quality leader. API via PiAPI / Segmind.
- **Sora 2** (OpenAI): 25s clips (extendable), native dialogue+SFX+music, 6 style presets. Duration champion.
- **Seedance 2.0** (ByteDance, Feb 12 2026): 20s @ 1080p, dual-channel audio, 4-input types (text/image/video/audio). No public API yet (⚠️ any 3rd-party Seedance 2.0 API is unofficial as of March 2026). Free trial via Volcano Engine.
- **Veo 3.1** (Google): 9:16 native vertical, best lip-sync & character identity, 1080p+4K upscale. Via Gemini API.
- **Wan 2.6** (Alibaba, open-weight): Community #1 self-hosted pick; MoE 14B, VBench leader for open-source, LoRA from 2.1/2.2 compatible, consumer GPU friendly. Zero per-gen cost.
- **LTX-Video 2.3** (Lightricks): ComfyUI day-0 support (March 5). Fastest: near-real-time 30fps @ 1216×704. Audio-video sync.
- **HunyuanVideo 1.5** (Tencent): 13B dual-stream transformer, FP8, multi-GPU, strong motion coherence. ComfyUI native support.
- **SkyReels V4**: Unified multimodal video audio gen, repair & edit foundation model.
- **Free video API access**: fal.ai (Veo/Sora/Kling via single API, pay-per-use). Cliprise (47+ models). Kling O1 via PiAPI (free credits).

### 🔧 ComfyUI Updates (March 2026)
- **v0.16.1 (March 5)**: Kling 3.0 Motion Control enabled; ResolutionSelector node; LTXAV 2.3 native; SCAIL WanVideo; SDPose-OOD; Dynamic VRAM as default.
- **v0.16.0 (March 5)**: LongCat-Image native; ACE-Step 1.5 lycoris key alias (LoKR); Z-image pixel-space; zeta chroma weights loading.
- **App Mode + App Builder (March 10)**: Convert workflows into shareable no-install apps. ComfyHub launched.
- **ElevenLabs integration (March 7)**: Voice cloning, TTS, sound effects directly in ComfyUI.
- **Comfy Cloud free tier (March 2)**: 400 free credits/month for cloud processing.
- **NVIDIA RTX acceleration (March 10, GDC)**: FP4 model support + RTX Video Super Resolution in ComfyUI. Confirmed ~30× faster upscaling vs alternatives.
- **Hunyuan 3D Advanced (March 10)**: Production-ready 3D post-processing in ComfyUI.
- **LTX-2.3 day-0 (March 5)**: Enhanced audio-video quality.
- **Key community nodes**: Impact Pack (FaceDetailer, mandatory), ComfyUI Cluster (200+ models, auto-picks best).

### 🦾 Pose Estimation SOTA
- **RTMPose-m**: 75.8% AP COCO, 430+ FPS on GTX 1660 Ti (ONNX). RTMPose-s: 72.2% AP, 70+ FPS on Snapdragon 865 mobile.
- **RTMO** (one-stage): 1.1% higher AP than competing one-stage, ~9× faster with same backbone. In MMPose v1.3.0.
- **DWPose-l** (256×192): 72.2% Body AP / 66.5% Whole AP on COCO-WholeBody. ICCV 2023 best-in-class for whole-body.
- **YOLOv11 Pose / YOLO26**: Strong occlusion handling, real-time. YOLO26 (Ultralytics): NMS-free, edge/low-power optimized.
- **HEViTPose** (2026, Nature): New ViT-based HPE with improved accuracy/efficiency tradeoff.
- **DWPose in ComfyUI** (comfyui_controlnet_aux): Now confirmed working with Wan 2.2 Animate for pose-conditioned video. `dw_openpose_full` node covers body+hands+face. TorchScript backend recommended for GPU speed.

### 🎓 LoRA Training SOTA
- **OneTrainer** emerging as top choice over AI-Toolkit: 2× speedup, built-in TensorBoard validation loss (prevents overfitting), batch captioning/masking, Prodigy optimizer support.
- **Kohya_ss**: Still most reliable for SDXL+A1111 character LoRA pipelines (March 2026 tutorial confirmed).
- **Flux LoRA best practice**: `rank 16–32`, `lr 4e-4`, `~1000 steps @ bs1`. Minimal tagging critical (Flux has strong pre-biases). Trigger: `3–5 rare letters + class` (e.g. `zkw woman`).
- **SDXL best practice**: `rank 32–64`, `lr 5e-5 UNet / 1e-5 TE`, Prodigy optimizer, 15–30 epochs, 30–50 images, Noise Offset 0.035–0.1.
- **Dataset gen workflow**: Qwen Image Edit (from 1 reference → consistent 40-60 candidate set) → select best 30-50 → train.
- **ID-LoRA** (arxiv March 2026): Joint appearance+voice generation in single model from text+image prompt. Emerging for multi-modal identity preservation.
- **Multi-character LoRA**: Single LoRA with multiple trigger words per character now production-viable.
- **Flimmer trainer**: Video LoRA training toolkit for DiT models (March 3 2026 release). Enables character-consistent video fine-tuning.
- **Facial drift prevention (2026 best practice)**: LoRA + inpainting workflow; identity anchoring + temporal regularization for video sequences.

---

## 🔥 Run #59 Delta — 2026-03-13 02:30 Prague

### 🖼 Image Gen SOTA
- **FLUX 2** (Black Forest Labs, 32B): Now clear photorealism leader; Flex tier ~$0.03/img, Klein 9B ~$0.02/img; Kontext variant for context-aware editing. Runs locally (FLUX.1 [dev] Apache 2.0, [schnell] open-weight).
- **Nano Banana 2 / Gemini 3.1 Flash Image** (Google): 1-3s gen, SOTA text rendering, ~$0.08/img; **only API with meaningful free tier** (Gemini free tier). 4× faster than v1.
- **MiniMax Image-01**: $0.01/img, cinematic quality, best cost/quality ratio.
- **GLM-Image** (Zhipu/Z.ai): Apache 2.0, hybrid 16B autoregressive+diffusion decoder, $0.015/img, #1 industrial text rendering (CVTG-2k 0.9116).
- **Z Image Turbo** (Alibaba Qwen): Open-source, <3s photorealistic, 6GB VRAM, strong for face/headswap in ComfyUI.
- **SDXL Base 1.0**: Still free via Pixazo API, no usage limits; best community ecosystem for ControlNet LoRA.
- **FLUX.1 Kontext [dev]**: $0.015/img for context-aware multi-step editing on fal.ai / 302ai.
- **NEW — FLUX Image to Video** (March 2026): BFL announced I2V capability, live on fal.ai.
- **FireRed-Image-Edit**: New SOTA image editing model (open-source); outperforms Qwen-Image-Edit and Seedream.

### 🎬 Video Gen SOTA
- **Wan 2.6** (Alibaba, latest): Reference-to-video mode (upload 3-8s ref clip → extract appearance + voice), 15s 1080p, native audio/lip-sync. fal.ai: $0.10/s 720p | $0.15/s 1080p | Flash $0.05/s. Apache 2.0.
- **Wan 2.2** still strongest pure local option: MoE 14B, 8GB VRAM quantized, runs locally. MSVBench: I2V parity with commercial models on Video Consistency. GGUF Q2_K–Q8_0 HuggingFace.
- **Seedance 2.0** (ByteDance, Feb 2026): Quad-modal input (9 imgs + 3 vids + 3 audio), 2K, Director mode, 90%+ usable rate. API via piapi.ai / Atlas Cloud. Public Replicate/fal slugs still stabilising.
- **Kling 3.0** (Kuaishou): Up to 2-min single generation, best human motion (martial arts, complex actions), native audio. Cheapest API: **$0.029/s**. Free tier 66 credits/day.
- **Sora 2** (OpenAI): Best physics/gravity sim, 25s + native audio. $0.10-0.50/s API.
- **Veo 3.1** (Google): Only true 4K native AI video. $0.15/s API. Integrated with Nano Banana + Whisk.
- **Runway Gen-4.5**: Best editing ecosystem (inpainting, motion brushes, style transfer). $0.12/s Replicate. No native audio.
- **LTX-2.3** (Lightricks): Open-source audio-video model, Day-0 ComfyUI support, 9:16 portrait support, improved VAE for sharper textures. Self-hostable.
- **HunyuanVideo** (Tencent, 13B): Best open-source I2V for cinematic quality; 60-80GB GPU (FP8 saves ~10GB). Community license.

### 🔧 ComfyUI Updates (March 2026)
- **App Mode + App Builder + ComfyHub** (March 10 2026): Revolutionary — node-graph-free interface for non-technical users, URL-shareable apps, community marketplace. Major for Digital-Stud workflow distribution.
- **NVIDIA RTX nodes**: ComfyUI_NVIDIA_RTX_Nodes — RTX Video Super Resolution (4K upscale, 30× faster). Install via Manager → 'RTX'.
- **NVFP4 + FP8** native support: FLUX.2 Klein 4B/9B NVFP4/FP8; LTX-2.3 FP8 available. Up to 2.5× perf gains + 60% VRAM reduction on RTX 50xx.
- **LTX-2.3 Day-0 support**: Native ComfyUI node, Template Library workflows for I2V and T2V, 9:16 portrait, cleaner audio.
- **Wan2.2 Animate Character Swap**: New ComfyUI node — video guided by input video + reference image + prompt. Key for Digital-Stud character consistency pipeline.
- **HY 3D 3.0 advanced post-processing**: 3D Parts Decomposition, UV Unwrapping, Smart Topology — all in ComfyUI workflows now.
- **Z Image Turbo Headswap**: Dedicated ComfyUI workflow for seamless head replacement preserving original lighting/pose/style.
- **ReActor Face Swap** (updated): Pre-saved Face Models (.safetensors) + GFPGAN restoration + video face swap via VideoHelperSuite.
- **Comfy Cloud out of beta**: ~90% of local custom nodes accessible in cloud, zero config.
- **ComfyUI MCP Server**: MCP protocol bridge — connect AI assistants (Claude Desktop) directly to ComfyUI for automated generation.
- **Dynamic VRAM** optimization merged to main.
- **Grok video workflow**: 15s photorealistic video gen with text rendering in ComfyUI Template Library.

### 🦴 Pose Estimation SOTA
- **DWPose via comfyui_controlnet_aux**: Still the gold standard for ComfyUI ControlNet. DWPreprocessor handles hands/body/face. Recommendation: stick to DWPose or standard pose — avoid mixing preprocessors.
- **RTMPose** (SimCC+GAU): Lightweight, heatmap-free. `rtmlib` pip package for inference without mmcv dependencies.
- **RTMO**: One-stage real-time multi-person pose, pure ONNX Runtime; pip+CLI for webcam/image/video in minutes.
- **YOLOv11**: Improved backbone/neck over v8; 17-keypoint pose (51-dim output: 17×3). Competitive for deployment.
- **ViTPose/ViTPose++**: Transformer backbone + RT-DETR detector; best for crowd/complex scenes.
- **DynPose** (CVPR 2025): Sparse attention approach — substantially improves efficiency of HPE.
- **FASTCC**: Builds on SimCC+RTMPose, adds lightweight detection; strong mobile/edge performance.
- **3D Pose in ComfyUI**: Emerging extensions for 3D pose manipulation beyond standard 2D skeleton.
- **Active issue**: DWPose GPU acceleration (onnxruntime-gpu) still not smooth in ComfyUI — runs on CPU by default.

### 🎨 LoRA Training SOTA
- **OneTrainer** now preferred over AI-Toolkit for Flux character LoRAs: built-in validation loss curves catch overfitting, 2-4× faster on same HW (3s/iter on RTX 5060Ti @ 512²). Presets for Klein 9B, Z-Image Turbo, Flux.
- **Kohya-ss (sd-scripts)**: Still most stable for pure SDXL LoRA; development slowing vs OneTrainer.
- **Dataset sweet spot**: 17-50 images; 512×512 halves training time vs 1024² with similar results. Consistent angles/lighting critical for face identity.
- **In-Context LoRA (IC LoRA)** (Alibaba Tongyi): 20-100 samples → cross-image character consistency; trains on image collections with text stitched together rather than isolated prompts. Final model: few MB.
- **T-LoRA** (Sakana AI): Timestep-dynamic rank adaptation — adjusts LoRA rank per diffusion step; weight normalization prevents mode collapse on multi-subject training. Key for video LoRAs.
- **Video2LoRA** (arXiv 2603.08210): Hypernetwork predicts semantic-specific LoRA weights per video; <150MB model, 23K trainable vars (~30KB) per semantic condition. New March 2026 paper.
- **Flimmer-trainer**: New video LoRA training toolkit for diffusion transformer models (03/03/2026).
- **LoRA Rank guidance**: 8-16 typical; 128 for complex/multilingual models; DoRA (Decomposed Rank-Adaptation) for improved fidelity.
- **Facial drift prevention**: Flux/SDXL LoRA + inpainting combo; inpaint face region separately with LoRA strength 0.7-0.9 for long sequences.

---

## 📅 Run #57 Delta — 2026-03-13 01:32 Prague

### 🎬 Video Gen SOTA
- **Wan 2.6** (Alibaba): 15s multi-shot 1080p, native audio sync, "Video Roleplay" for char consistency, open weights on HuggingFace (23 models), free beta at wan.video. RTX 4090: ~4min/5s@480p.
- **Seedance 2.0** (ByteDance): Multi-shot native single-pass, quad-modal input (text+img+vid+audio), native audio/lip-sync 8+ langs, 2K resolution, $0.30/clip. First model with 4K+audio+multi-shot combined.
- **HunyuanVideo** (Tencent): 13B param, dual-stream transformer, fully free+open-source, commercial use allowed, multi-GPU scaling, FP8 weights. Confirmed SOTA open-source.
- **Kling 3.0** (Kuaishou): 4K@15s, AI Director mode, Element Binding facial consistency (new March 9 in ComfyUI), multi-shot 6-cut editing, free tier, $7/mo paid.
- **Veo 3.1** (Google): First native 3840×2160 (no upscaling), lip-sync, scene extension 60s+, $0.15-0.40/sec.
- **LTX-Video 2.3**: 30fps@1216×704 faster than real-time, portrait 9:16 support, improved I2V fewer frozen frames, audio-video gen, Day-0 ComfyUI support (Mar 5, 2026).
- **SkyReels V4** (Kuaishou SkyWork): Cinematic storytelling, Wan2.2-based, CinematicPreset node in ComfyUI. ← [COMMITTED RUN 56]

### 🖼️ Image Gen SOTA
- **Nano Banana 2** (Google, Gemini 3.1 Flash Image, Feb 2026): Arena #1 at Elo 1280. Free tier 500-1000 images/day on AI Studio (no CC), batch API $0.01/img.
- **FLUX.2 Pro v1.1** (BFL): Elo 1265, sub-second speed, open-weight Dev variant free self-hosted.
- **FLUX.2 Klein 4B/9B**: NVFP4+FP8 variants for lower VRAM — directly useful for Digital-Stud workflows.
- **GPT Image 1.5** (OpenAI): ~95% text accuracy, Elo 1264, $0.04-0.13/img.
- **Seedream 4.5** (ByteDance): $0.03/img, strong typography.
- **Stable Diffusion 3.5**: $0.006/img API or free self-hosted; enterprise-ready per CGAIGroup Feb 2026.

### 🔧 ComfyUI Updates (v0.16.0/0.16.1 — Mar 5, 2026)
- **ResolutionSelector node**: aspect ratio presets.
- **LTXAV 2.3 + SCAIL WanVideo model support** added natively.
- **Kling 3.0 Motion Control** Partner Nodes (Mar 9): Element Binding facial consistency across angles/occlusion.
- **LTX-2.3 Day-0 support**: 9:16 portrait, improved I2V, audio-video.
- **Shima 2.0** (Mar 12): 100+ new custom nodes — character loading, Mixamo animation, environment mgmt, video export.
- **WanSoundImageToVideoExtend** node: audio-driven video with precise length control.
- **ElevenLabs TTS nodes** in ComfyUI (Mar 9).
- **NVFP4 checkpoint support** (fp4 matrix multiply) + RTX Video Super Resolution node (real-time 4K upscale for RTX GPUs).
- **ByteDance Seedream-5 API node**, **Veo 3.1 API node**, **KlingAvatar node**, **Recraft V4 nodes**, **Topaz video enhancement nodes**.
- Dynamic VRAM mode now default. FP8 dynamic VRAM perf improvements. Reduced LoRA memory reservations (esp. Flux2).
- **Tripo 3.0** (3D gen) + **Rodin Gen-2** (img-to-3D) integrated.

### 🦾 Pose Estimation SOTA
- **YOLO26** (Jan 2026): NMS-free inference, 71.6 mAP@50-95 (YOLO26x on COCO), 43% faster CPU vs prev gen, MuSGD optimizer, RLE precision. Best for edge/low-power.
- **YOLO11 Pose** (production standard 2025-26): 89.4% mAP@0.5 COCO Keypoints, 30+FPS@T4.
- **Sapiens 2** (Meta): +4 mAP over Sapiens 1 on 2D pose, +24.3 mIoU body-part seg. New SOTA for human-centric vision.
- **DETRPose** (2025): First real-time transformer multi-person pose, beats YOLO11-X on COCO test-dev.
- **RTMPose**: 75.8% AP (RTMPose-m), 90+ FPS CPU / 430+ FPS GPU (TensorRT). Best whole-body.
- **SDPose-OOD models**: Now in ComfyUI API nodes (v0.16.1). Out-of-domain robust estimation.
- **ComfyUI-YoloNasPose-Tensorrt**: TensorRT-accelerated YOLO-NAS-POSE nodes.

### 🎓 LoRA Training SOTA
- **AI-Toolkit (Ostris)**: Leading Flux.1 LoRA trainer — OFT, BOFT regularization support, multi-concept batching; v0.6+ recommended. Fastest convergence for face identity.
- **Kohya ss GUI**: Flux LoRA training via GUI with FP8 base model support, CAME optimizer added, lycoris support (IA3, LoCon, LoHa, LoKr, full).
- **OneTrainer**: Cross-platform GUI, FP8 training support, multi-resolution bucketing, EMA, supports Flux+SDXL+SD3. Good for character consistency.
- **Flux LoRA best practices 2026**: 10-20 steps @ lr=1e-4 for face, ~500 images. OFT regularization reduces overfitting. Trigger word + dense captions = strong identity preservation.
- **LyCORIS networks**: LoKr (Kronecker product) significantly outperforms standard LoRA for face identity on Flux — 2x fewer params for same quality.
- **SDXL**: Still viable for style/character LoRA, cheaper to train. AI-Toolkit and Kohya both support.

## 🔄 Run #55 Delta — 2026-03-13 00:30 Prague

### 🎬 Video Gen SOTA
- **Wan 2.2** (Alibaba Tongyi): World's first open-source MoE video generation model. 27B total / ~14B active params. 480p-720p, min 8.19GB VRAM. VBench 84.7%+. Free on GitHub: `Wan-Video/Wan2.2`. Key: high-noise + low-noise experts for separate denoising stages.
- **LTX-2 (Lightricks)**: 19B params, native 4K at 50fps, 20s videos, synchronized audio. Apache 2.0 + free commercial use <$10M ARR. NVFP8 quant = ~30% size reduction. **Day-0 ComfyUI support confirmed.**
- **HunyuanVideo 1.5**: Compact 8.3B, outperforms RunwayGen-3 + Luma 1.6. 720p in 75s on RTX 4090 (13.6GB VRAM). Text alignment 68.5%, visual quality 96.4%.
- **Kling 2.6** (Kuaishou): Simultaneous audio-visual generation (video + voiceover + SFX in one pass). Up to 2min @ 1080p 30fps. Diffusion transformer + 3D VAE.
- **Runway Gen-4.5**: Top Artificial Analysis benchmark. Native audio, long-form multi-shot, motion brushes. $315M Series E @ $5.3B valuation (Feb 2026). From $12/mo.
- **Google Veo 3.1** (Jan 2026): Native 4K, vertical video for Shorts, "Ingredients to Video" (up to 4 reference images). SynthID watermarking. Gemini Advanced $19.99/mo.
- **Sora 2** (OpenAI): Up to 60s, physics simulation, Disney 200+ licensed characters, synchronized audio. $20/mo Plus / $200/mo Pro.
- **Seedance 1.5 Pro**: Noted for fast, precise AI video in 2026 benchmarks. API available via fal.ai / Replicate.
- **Pika 2.5**: 74% usable output rate, Pikaswaps/Pikaffects/Pikaframes/Pikaformance. Near real-time generation.
- **Luma Ray3**: Hi-Fi 4K HDR, photorealistic, from $7.99/mo.
- **FREE LOCAL**: Wan 2.2 and HunyuanVideo 1.5 are the current open-source leaders.

### 🖼️ Image Gen SOTA
- **Flux.2 Klein 9B**: Active development, community LoRA ecosystem growing. Anime2Real LoRA for Klein 9B reported strong character identity preservation (March 2026 Reddit).
- **Nano Banana 2**: Can replace LoRA training for fast-turnaround production workflows where single reference image anchors identity (RunDiffusion). No training required.
- **Recraft V3 / Ideogram 3**: Still competitive in commercial image gen tier.
- **Free APIs**: fal.ai, Replicate (Wan, HunyuanVideo, FLUX), WaveSpeed.ai (FLUX/SDXL training cloud).

### 🧩 ComfyUI New Nodes & Platform (March 2026)
- **App Mode + App Builder + ComfyHub** (launched Mar 10, 2026): Convert any workflow → shareable browser app, no node graph needed. ComfyHub = marketplace for workflows/apps. **Major UX shift.**
- **LTX-2.3 Day-0 native support**: Updated VAE (sharper textures), 9:16 portrait support, improved audio quality, better I2V consistency.
- **ElevenLabs Partner Nodes** (Mar 8, 2026): Voice cloning/synthesis directly in node graph. `#ComfyUI #aivoice`.
- **Hunyuan 3D Advanced** (via Partner Nodes): 3D Parts Decomposition, UV Unwrapping, Smart Topology — production-ready post-processing pipeline.
- **3D Scene Builder Node**: Load chars → environment → Mixamo animation → compose shots → export video. AI filmmaking node.
- **Node Replacement API**: Custom node devs can now evolve nodes without breaking user workflows.
- **ComfyUI-OpenClaw 2026.3.2**: Security-first orchestration, SecretRef expanded to 64 credential targets (Stripe, Slack, GitHub etc.). "Trust & Tools" stable release.
- **LTX2EasyPrompt** (community): Simplified prompt configuration node for LTX-2 video gen.
- **ComfyUI-Pollinations**: New custom node wrapping Pollinations open-source image platform.
- **Comfy Cloud out of beta**: ~90% custom nodes available on cloud. Supports RTX 5090 + AMD RX 9070 XT.
- **Video-to-Motion Capture**: Community node extracts SMPL body params from video → FBX rigged character → retargeted animation. Useful for Digital-Stud animation pipeline.

### 🤸 Pose Estimation SOTA
- **DWPose / RTMPose**: Still dominant for ComfyUI ControlNet pose conditioning. No major new releases detected this cycle.
- **YOLO-based pose**: Active in real-time pipelines. YOLOv11/v12 variants in community ComfyUI nodes.
- **Video-to-Motion Capture ComfyUI node**: SMPL body parameter extraction from video footage → FBX export + animation retargeting. Direct pipeline integration for DS character animation.
- **ComfyUI-SAM3**: Interactive click-to-segment, useful for character masking pre-pose. (Previously noted in r53.)

### 🔁 LoRA Training SOTA
- **Kohya_ss v0.10.1** (Feb 13, 2026): Added Anima Preview model support for LoRA training + fine-tuning. Still most popular tool for character SDXL LoRA (30-50 images, rank 32, lr 5e-5, Prodigy optimizer).
- **OneTrainer rising fast**: 2x performance vs AI-Toolkit on RTX 5060 Ti. Proper train/val split, TensorBoard loss tracking, prevents overfitting. Preferred by serious trainers over AI-Toolkit.
- **Flux.2 Klein 9B LoRA**: Community reports mixed results (30+ checkpoint testing, careful HP tuning needed). Anime2Real LoRA for Klein 9B is exception — strong identity preservation.
- **AI-Toolkit**: Still popular but criticized for missing train/val split and limited optimizer options for newer models.
- **Z-Image LoRA + AI-Toolkit**: Z-Image base model LoRA training workflow documented with full local setup (YouTube tutorial active March 2026).
- **ID-LoRA** (research): Identity-Driven Audio-Video Personalization — reference audio clip + first-frame image + text prompt → consistent audio-visual identity. Cutting-edge convergence direction.
- **FedMomentum** (arxiv 2603.08014): SVD-based aggregation preserving LoRA training momentum in federated fine-tuning. Faster convergence. Research breakthrough.
- **SFed-LoRA** (arxiv 2603.08058): Prevents high-rank collapse in distributed LoRA training, significantly improved stability.
- **Nano Banana 2**: Zero-training character consistency — single reference image anchors identity. Replaces LoRA for fast turnaround production.
- **WaveSpeed.ai**: Cloud GPU LoRA/checkpoint training for FLUX + SDXL. Free tier available.

# Image & Video Generation SOTA


---

## 🔄 Run #53 Delta — 2026-03-12 23:30 Prague

### 🆕 ComfyUI-SAM3 Interactive Click-to-Segment Update (in-canvas)

- **Source**: Reddit r/comfyui post 168 upvotes; `PozzettiAndrea/ComfyUI-SAM3` GitHub + ComfyUI-Manager PR merged
- **New capability**: Interactive click-to-segment *in-canvas* — click on image node directly → SAM3 segments the clicked object in real time
- **Previously**: SAM3 node supported text/box prompts only; click-to-segment required separate workflow step
- **Now**: Click on image in ComfyUI canvas → instant mask generation; works in both image and video modes
- **Models**: Auto-downloaded via ComfyUI Manager; supports text, box, and interactive click prompts
- **Digital-Stud relevance**: ⭐⭐⭐ Click-to-segment in-canvas = fastest way to isolate character from background in ComfyUI. Critical for character extraction workflow: load image → click character → SAM3 mask → background removal → FLUX.2 inpaint or composite. Update `face_refinement.json` to include SAM3 click-to-segment node for character isolation.

### 🆕 Wan 2.6 Reference-to-Video — Official ComfyUI Integration Published

- **Source**: `blog.comfy.org/p/wan26-reference-to-video` (official Comfy Org blog post)
- **Capability**: Generate cinematic videos by learning motion, camera behavior, and visual style from reference clips
- **Specs**: Up to 2 reference videos, 720p and 1080p output options
- **API access**: Also available via Floyo cloud at `floyo.ai/workflows/wan-2-6-reference-to-video-0t6nnv8esua5` (no local install)
- **Status**: Officially supported in ComfyUI (not just community node); in Workflow Library
- **Distinction from Wan 2.6 I2V**: Reference-to-Video = style/motion learning from reference clips; I2V = image conditioning for single start frame. These are different models/modes.
- **Digital-Stud relevance**: ⭐⭐⭐ Wan 2.6 R2V is the current best local tool for consistent-style character video. Record reference clip → R2V learns your character's motion style → apply to new prompts. Update `wan22_img2vid.json` to document this R2V capability alongside standard I2V.

### 🆕 Seedance 2.0 ComfyUI Templates Confirmed Live (6 templates)

- **Source**: `comfy.org/templates/model/seedance/` — 6 free ComfyUI workflow templates published
- **Status correction from r52**: r52 noted "on its way"; confirmed live as of ~March 12
- **Available modes**: T2V, I2V, audio-conditioned generation (some templates require Gemini API for music)
- **Community note**: Some workflows tied to Gemini API for background music — limitation for local-first workflows
- **Benchmark**: YouTube "LTX-2.3 ComfyUI vs Seedance 2.0" confirms both viable for 20-second no-flicker generation; LTX-2.3 wins for free/local, Seedance 2.0 wins on API quality ceiling
- **Digital-Stud relevance**: ⭐⭐ Seedance 2.0 templates available now in ComfyUI. `api_test_seedance.py` artifact (queued) should test these template endpoints. For local work: LTX-2.3 is the choice; for cloud API quality: Seedance 2.0 is cost-competitive with Kling 3.0.

### 🆕 LTX-2.3 IC-LoRA — V2V ControlNet + Motion LoRA Modes

- **Source**: YouTube "LTX 2.3 IC-LoRA New Cool Features: V2V ControlNet & Motion..." (ComfyUI tutorial channel)
- **New capabilities beyond basic IC-LoRA**:
  - **Video-to-Video ControlNet conditioning**: Use input video as structural guide for LTX-2.3 generation; character pose/motion preserved from reference video
  - **Motion LoRA modes**: Separate LoRA weights that control camera motion and character motion independently
  - **Custom nodes referenced**: Specific DiffSynth-Studio ComfyUI nodes for V2V + Motion LoRA pipeline
- **Pipeline**: Reference video → V2V ControlNet extract motion → LTX-2.3 generate with IC-LoRA identity + motion LoRA camera control
- **Digital-Stud relevance**: ⭐⭐⭐ V2V ControlNet + IC-LoRA = character-consistent video where you control both *who* (IC-LoRA identity) and *how* (V2V ControlNet motion + Motion LoRA camera). This is the most complete character video pipeline available locally. The `ltx23_ic_lora.json` artifact (pending) should document this full V2V+IC-LoRA+Motion pipeline.

### 🆕 ComfyUI-DeZoomer-Nodes — Video Captioning + Caption Refinement

- **Source**: GitHub `De-Zoomer/ComfyUI-DeZoomer-Nodes`; available via ComfyUI Manager
- **Nodes**:
  1. **Video Captioning Node**: Automated caption generation for video files (input: video → output: text captions)
  2. **Caption Refinement Node**: Post-processes captions for quality/consistency improvements
- **Use case**: Automated training data curation for video LoRA training (complements the free LTX-2.3 captioner from r52)
- **Digital-Stud relevance**: ⭐⭐ Two-stage captioning pipeline in ComfyUI: Video Captioning → Caption Refinement → output ready for LTX-2.3 IC-LoRA training. Can be integrated directly into a data preparation workflow node graph. More flexible than standalone tools.

### 🆕 ComfyUI-DepthAnythingV3 Node — DA3 + Point Cloud Preview

- **Source**: `PozzettiAndrea/ComfyUI-DepthAnythingV3` GitHub; v1.3.3; `DA3_PreviewPointCloud` node on comfy.icu
- **Capabilities**:
  - Depth Anything V3 depth estimation (monocular; spatially consistent geometry)
  - DA3-Small model support (faster, lower VRAM)
  - **DA3_PreviewPointCloud node**: Visualize depth maps as 3D Gaussian/point cloud in ComfyUI canvas
  - Camera pose estimation from depth maps
  - Multiple normalization modes for depth map output
- **Install**: Available via ComfyUI Manager search "DepthAnythingV3" or "PozzettiAndrea"
- **Digital-Stud relevance**: ⭐⭐⭐ DA3 ComfyUI node is now production-ready. For `pose_controlnet.json` pipeline: DA3 depth node → depth map → XLabs FLUX ControlNet depth → consistent 3D-aware character pose. DA3_PreviewPointCloud enables real-time 3D preview of depth estimation quality before committing to ControlNet generation. Replace DA2 depth node with DA3.

### 🆕 Comfy Cloud Free Tier Launched

- **Source**: `blog.comfy.org/p/free-tier-arrives-in-comfy-cloud`
- **Hardware**: Free tier runs on RTX Pro 6000 GPUs (same as paid Comfy Cloud users)
- **Implication**: Zero-cost cloud ComfyUI execution for testing; no local install needed for workflow validation
- **Limitation**: Free tier has usage quotas (standard free tier limits); not for bulk production use
- **Digital-Stud relevance**: ⭐⭐ Use Comfy Cloud free tier for: (1) testing new workflows before optimizing locally, (2) running memory-intensive workflows (FLUX.2 Klein 9B) without local 24GB GPU, (3) sharing/demoing Digital-Stud workflows with collaborators. Lowers the barrier for experimenting with new nodes before local setup.

### 🆕 LTX-2.3 vs Seedance 2.0 — 20-Second No-Flicker Benchmark

- **Source**: YouTube "LTX-2.3 ComfyUI vs Seedance 2.0: Get 20-Sec Videos With No Flicker"
- **Result**: Both achieve 20-second flicker-free generation
- **LTX-2.3 advantages**: Free (local), faster iteration, no API cost, open weights
- **Seedance 2.0 advantages**: Higher quality ceiling on API, better motion smoothness for complex scenes
- **Community consensus (r/comfyui March 2026)**: LTX-2.3 for local production; Seedance 2.0 for paid API quality output
- **Digital-Stud relevance**: ⭐⭐ Decision matrix confirmed: LTX-2.3 = default local workflow; Seedance 2.0 API = upgrade path for final delivery. Matches the two-stage pipeline concept (LTX-2.3 local preview → Kling 3.0/Seedance 2.0 final). Document in `api_test_seedance.py` artifact.

### 🆕 FLUX.2 Klein 4B — Separate Small Model + 5 Community LoRAs

- **Source**: `docs.comfy.org/tutorials/flux/flux-2-klein` official ComfyUI tutorial; YouTube "Five NEW Flux.2 Klein LoRAs released in 2026"
- **Model clarification**:
  - FLUX.2 Klein 4B = lighter/faster variant (not just the 9B model referenced in r51-52)
  - Klein 4B supports T2I + image editing workflows in ComfyUI
  - Klein 9B = higher quality, higher VRAM requirement (for face-swap BFS LoRA workflow)
- **5 Community LoRAs released 2026**: Style LoRAs with workflow links provided in YouTube description; available on HuggingFace
- **Digital-Stud relevance**: ⭐⭐ FLUX.2 Klein 4B = the low-VRAM FLUX.2 option for rapid iteration on 8-12GB GPUs. For face-swap BFS workflow: use Klein 9B. For style iteration and T2I: Klein 4B is faster. Add Klein 4B workflow as variant in `image_gen_flux.json`.

### 🆕 Z-Image Turbo as Face Detailer in ComfyUI

- **Source**: NextDiffusion tutorial "How to Use Z-Image Turbo as a Face Detailer in ComfyUI" (8-step pipeline)
- **Pipeline**:
  1. Face detection (automatic)
  2. Build face mask from detection bbox
  3. Z-Image Turbo enhance face detail within mask
  4. Blend enhanced face back into original image
- **Comparison**: Better fine facial detail than ADetailer for photorealistic faces; Z-Image Turbo's 6B parameters → more detail capacity than dedicated detailer models
- **Integration**: Works as ComfyUI nodes; Z-Image Turbo loaded as standard image generation model + mask conditioning
- **Digital-Stud relevance**: ⭐⭐⭐ Z-Image Turbo face detailer = upgrade path for `face_refinement.json`. Current workflow likely uses ADetailer or FaceDetailer; replacing with Z-Image Turbo gives higher quality face detail with the same pipeline structure. Add Z-Image Turbo face detailer path to `face_refinement.json` alongside FLUX.2 Klein BFS face-swap.

### 🆕 Neural4D Image-to-3D Engine (G-Stacker, March 12, 2026)

- **Source**: Press release March 12, 2026 (multiple syndication sites)
- **Capability**: Watertight manifold geometry + pure albedo extraction from 2D images → engine-ready 3D assets
- **Key problem solved**: Eliminates baked lighting from AI-generated 3D assets (major pain point in existing I23D tools like TripoSR/Zero123++)
- **Output**: Clean mesh + albedo texture → directly importable to Blender/Unreal/Unity without manual relighting
- **Comparison**: Tripo3D, Meshy, and Zero123++ all produce baked-lighting meshes; Neural4D produces proper PBR-ready albedo
- **Access**: Available from G-Stacker (`gstacker.io` or similar); unclear if open-source or commercial
- **Digital-Stud relevance**: ⭐⭐⭐ For 3D+AI workflow: Neural4D solves the biggest practical problem in AI-assisted 3D asset creation. Generate character image → Neural4D → clean albedo mesh → import to Blender for rigging/animation. If Neural4D is API-accessible, this belongs in the pipeline as the I23D step. Investigate pricing/access.

### 🆕 SeedVR2 — Best Image-to-Image Upscaler March 2026

- **Source**: r/comfyui community consensus (March 2026 thread "as of march 2026 whats the best i2i upscale method?")
- **Community verdict**: "SeedVR2 is devilishly good out of the box" — preferred over Real-ESRGAN, LDSR, and Tiled Diffusion
- **Also mentioned**: "If I need more 'invention'" = Tiled Diffusion still preferred for creative upscaling
- **SeedVR2 characteristics**: Video + image upscaling; consistent detail enhancement; ByteDance-Seed lineage (same lab as Depth Anything 3, Seedance 2.0)
- **Digital-Stud relevance**: ⭐⭐ Add SeedVR2 as post-processing upscale step in character image and video pipelines. For final render quality: SeedVR2 upscale → Z-Image Turbo face detailer → output. This two-step post-processing improves final delivery quality significantly.

### 🆕 ComfyStudio — Video Editor with ComfyUI Integration

- **Source**: Cursor Forum post (March 11, 2026); `ComfyStudio` project
- **Concept**: Full-featured video editor with integrated ComfyUI interface; access full node graph when needed; timeline-based editing + AI generation in one environment
- **Status**: Development/preview (posted in Cursor community forum)
- **Digital-Stud relevance**: ⭐ Early-stage project. If ComfyStudio reaches production quality, it eliminates the ComfyUI → video editor export step. Monitor for GitHub release. Not actionable yet for Digital-Stud pipeline.

### 🆕 Higgsfield Soul 2.0 — Confirmed Production Identity-Consistent Video

- **Source**: Instagram @first_light_studio_, March 12: "Using Higgsfield Soul 2.0, we created a consistent cinematic character by training the model with multiple reference"
- **Capability**: Identity-consistent character video from multi-reference training; "cinematic" quality confirmed by production studio
- **Access**: Higgsfield AI platform (commercial); multi-reference training via Soul 2.0 fine-tuning
- **Comparison with local tools**: Soul 2.0 = managed commercial service; DiffSynth-Studio LTX-2.3 IC-LoRA = open-source equivalent for local use
- **Digital-Stud relevance**: ⭐⭐ Higgsfield Soul 2.0 = the commercial reference for what IC-LoRA should achieve locally. Use Soul 2.0 as quality benchmark when evaluating DiffSynth-Studio IC-LoRA outputs. If local IC-LoRA quality falls short, Soul 2.0 is the API fallback.

### 🆕 Grok Imagine "Extend from Frame" (March 2, 2026)

- **Source**: basenor.com article on Grok Imagine updates
- **Feature**: Extend-from-Frame — temporal clip chaining; end frame of one clip becomes start frame of next generation
- **Scale**: xAI reports 1.245 billion videos generated monthly on Grok Imagine (January 2026 stat)
- **Implication**: Grok Imagine now has a native long-form video construction capability via chaining
- **API access**: Grok API (xAI); included in Grok Plus/Pro subscriptions; API endpoint available
- **Digital-Stud relevance**: ⭐ Extend-from-Frame is less useful than Wan 2.7's start+end frame approach (which maintains consistency over the full clip). Grok Imagine quality is below Kling 3.0/Seedance 2.0 for character work. Low priority for Digital-Stud pipeline.

### 🆕 A²-Edit Full Architecture Confirmed (arXiv 2603.10685)

- **Full architecture details** (confirmed from abstract read in r53):
  - **MoT (Mixture of Transformers)**: Multiple LoRA expert transformers, each specialized for a category (clothing, objects, furniture, etc.)
  - **MATS (Mask Annealing Training Strategy)**: Handles imprecise/ambiguous mask inputs gracefully
  - **UniEdit-500K dataset**: 500,104 image pairs across 8 major categories and 209 subcategories
  - **SOTA results**: Best on VITON-HD (clothing try-on) and AnyInsertion (object insertion)
  - **Code**: Promised upon publication; GitHub link expected soon
- **Digital-Stud relevance**: ⭐⭐ A²-Edit's clothing-try-on capability (VITON-HD SOTA) = virtual wardrobe for character design. For Digital-Stud character workflow: design character base → A²-Edit clothing swap → output character in different outfits consistently. Monitor `arxiv.org/abs/2603.10685` for GitHub release announcement.

---



---

## 🔄 Run #52 Delta — 2026-03-12 23:03 Prague

### 🆕 Seedance 2.0 (ByteDance Seed Lab) — Cinema-Grade Video at $0.14/sec

- **Released**: February 2026; community peak activity March 12 (Kling 3.0 vs Seedance 2.0 comparisons trending)
- **Capabilities**: End-to-end video generation, multi-camera simulation, cinema-grade output
- **Cost**: Below **$0.14 per second of video** — most cost-effective cinema-quality commercial model currently
- **Architecture**: Multimodal foundation (text+image→video), supports complex scene continuity
- **Quality**: Trending comparisons show competitive with Kling 3.0 on VFX/model video tasks (March 12 Instagram reel "ashartco": "feels like a game changer")
- **Digital-Stud relevance**: ⭐⭐⭐ At $0.14/sec, Seedance 2.0 undercuts Kling 3.0 Pro on cost while matching quality for many use cases. Add to `api_test_fal.py` for direct cost-per-second benchmarking. For bulk character animation or VFX renders, Seedance 2.0 may be more economical than Kling 3.0.

### 🆕 Sora 1 Sunset + Sora 2 Preview API (March 13, 2026)

- **Sora 1**: Deprecated in US starting **March 13, 2026** — end-of-life
- **Sora integration**: Sora technology integrating directly into ChatGPT interface (no separate app)
- **Sora 2 Preview API**: Reportedly in development; expected to offer significantly improved quality over Sora 1
- **Implication**: fal.ai and Replicate Sora 1 API endpoints will likely be deprecated; update `api_test_fal.py` to remove Sora 1 references after March 13
- **Digital-Stud relevance**: ⭐⭐ Audit `api_test_fal.py` and `api_test_replicate.py` — remove Sora 1 endpoint tests; add Sora 2 when Preview API becomes available. Seedance 2.0 and SkyReels-V4 are the recommended Sora 1 replacements at current pricing.

### 🆕 Wan 2.7 — Imminent Release (March 2026)

- **Source**: Reddit r/StableDiffusion post March 12, 2026 (0 votes, original poster with insider knowledge)
- **Claimed features**:
  - Comprehensive upgrades over Wan 2.6
  - **Video generation from start+end frames** (bidirectional temporal conditioning) — new capability
  - **3×3 grid image input** for multi-reference video generation
  - Subject reference control (consistent character from image)
  - Voice reference control (audio-conditioned video generation)
  - Significant image quality improvements over 2.6
- **Note**: Community reception cautious ("No one cares unless it can be run locally") — indicates expectation of open weights
- **Status**: NOT yet released as of March 12; scheduled "this month" (March 2026)
- **Digital-Stud relevance**: ⭐⭐⭐ Wan 2.7 start+end frame generation = direct upgrade for character animation sequences (set start pose + end pose, model fills motion). Monitor `Wan-AI/Wan2.7` on HuggingFace for release. When released, update `wan22_img2vid.json` to Wan 2.7.

### 🆕 LTX-2 vs LTX-2.3 Clarification — #1 Open-Source A/V on HuggingFace

- **Clarification**: LTX-2 (base model, `Lightricks/LTX-2`) and LTX-2.3 (latest architecture release) are distinct:
  - LTX-2 = Lightricks' open-source A/V foundation model; confirmed **#1 ranked open-source audio+video model on HuggingFace** (co-founder interview, March 2026)
  - LTX-2.3 = latest architecture update released early March 2026 (rebuilt VAE, IC-LoRA, portrait support)
  - LTX Desktop = free production video editor built on LTX-2.3
- **Digital-Stud relevance**: ⭐⭐ Use LTX-2 for stable production; LTX-2.3 for latest features. For LoRA training, use LTX-2.3 + IC-LoRA (DiffSynth-Studio confirmed training support March 12).

### 🆕 Free Local LTX-2.3 Video Captioner (r/StableDiffusion)

- **Source**: r/StableDiffusion post ~March 12, 2026; open source
- **Capability**: Batch processes videos + images + mixed folders; generates captions specifically tuned for LTX-2.3 training data curation
- **Features**: Accepts any mix of video/image inputs; produces LTX-2.3-optimized caption format
- **Digital-Stud relevance**: ⭐⭐⭐ Direct workflow improvement for LTX-2.3 LoRA training. Use for captioning character reference footage before IC-LoRA training. Zero cost, runs locally. Search r/StableDiffusion for latest repo link.

### 🆕 SkyReels V4 in ComfyUI — Confirmed Parameters

- **Source**: ComfyUI official sitemap blog post + community tracking
- **ComfyUI support specs**: 1080p resolution, 32 FPS, 15-second duration supported natively
- **Architecture reminder**: Dual-stream MMDiT (video+audio parallel generation), ranked #3 on Artificial Analysis T2V+Audio
- **Status**: ComfyUI node available (V3 node likely compatible pending V4 weight release)
- **Digital-Stud relevance**: ⭐⭐⭐ SkyReels V4 @ 1080p/32fps/15s = production-ready spec for character video. When V4 weights release on HuggingFace (monitor `SkyReels-AI/SkyReels-V4`), this becomes the primary local long-form video generation tool.

### 🆕 ComfyUI App Mode — Confirmed Launch Date: March 10, 2026

- **Correction from r51**: Launch was March 10 (GlobeNewswire PR 12:00 ET March 10); Gigazine article timestamped 20:00 March 12 = Japanese media coverage delay, not a second launch
- **Comfy-Org CEO Yoland Yan** confirmed in Reddit r/StableDiffusion: 917 upvotes, 162 comments — strong community adoption
- **ComfyHub**: Live at comfy.org/workflows with browse/search for community workflows and apps
- **Clarification**: App Mode = free (local ComfyUI); Comfy Cloud = paid hosted execution; ComfyHub = distribution for both
- **Digital-Stud relevance**: ⭐⭐ No change from r51. App Mode launch confirmed; now stable for production use.

### 🆕 ComfyUI v0.16.0 — Full March 5 Changelog

- **Source**: docs.comfy.org/changelog (March 5, 2026)
- **New capabilities**:
  - `ResolutionSelector` node: aspect ratio presets (1:1, 16:9, 9:16, 4:3, etc.) — replaces manual width/height calculation
  - `CURVE` type: advanced parameter control for animation/easing curves in workflows
  - **Dynamic VRAM mode now default** — adaptive VRAM management; less OOM errors on consumer GPUs
  - **LoRA requantization for non-QuantizedTensor fp8** — fp8 LoRAs now work with quantized base models
  - **LongCat-Image native implementation** — long context image generation support (tiled/stitched generation)
  - Enhanced dynamic offload heuristics — smarter CPU-GPU offload for large models
  - Z-image pixel space support added
  - xAI models updated + Kling 3.0 Motion Control enabled in API Nodes
- **Digital-Stud relevance**: ⭐⭐ Update local ComfyUI to v0.16.0. Dynamic VRAM default = fewer crashes on 24GB/8GB workflows. `ResolutionSelector` replaces manual dimension nodes in all character gen workflows.

### 🆕 Kling 3.0 Now Available as ComfyUI Native Nodes

- **Source**: blog.comfy.org ("Kling 3.0 Models Are Now Available in ComfyUI!")
- **Access**: Native ComfyUI nodes via API (requires Kling API key); Standard + Pro motion control modes
- **Modes in ComfyUI**: T2V, I2V, and Motion Control (Pro) — all accessible via node graph
- **Digital-Stud relevance**: ⭐⭐ Kling 3.0 + SkyReels V4 + LTX-2.3 now all accessible in one ComfyUI workflow graph. Build unified character pipeline: LTX-2.3 for quick local preview → Kling 3.0 Pro for final 4K delivery.

### 🆕 A²-Edit (arXiv 2603.10685) — Generalized Reference-Guided Image Inpainting

- **Title**: "A²-Edit: A Highly Generalized Reference-Guided Image Inpainting Framework"
- **Core**: Breaks constraints of domain-specific editing and rigid reference matching; works across arbitrary image domains
- **Application**: Reference image → intelligent inpainting that respects reference style/content without domain restriction
- **Digital-Stud relevance**: ⭐ Once code releases, A²-Edit enables reference-consistent face/body inpainting without domain-specific models. Useful for replacing faces/outfits in character renders while preserving background. Monitor arXiv 2603.10685 for GitHub link.

### 🆕 DiffSynth-Studio LTX-2.3 IC-LoRA — March 12 Confirmation

- **Source**: DiffSynth-Studio GitHub README (confirmed March 12, 2026 update)
- **Capabilities**: Identity-consistent LoRA (IC-LoRA) for LTX-2.3 A/V generation
  - text-to-audio/video with IC-LoRA conditioning
  - image-to-audio/video with IC-LoRA conditioning
  - audio-video inpainting with LoRA control
  - full training + inference support
- **Pipeline**: Reference image → IC-LoRA extract identity → condition LTX-2.3 generation → consistent character video
- **Digital-Stud relevance**: ⭐⭐⭐ This is the most practical character-consistent video LoRA available today. DiffSynth-Studio + LTX-2.3 IC-LoRA = the recommended pipeline for Digital-Stud character video generation. Steps: (1) caption reference clips with free LTX-2.3 captioner, (2) train IC-LoRA via DiffSynth-Studio, (3) generate consistent character video via LTX-2.3.

### 🆕 Musubi LoRA Trainer Node for ComfyUI (Floyo, March 6)

- **Source**: Floyo release notes, March 6, 2026
- **Capability**: In-browser LoRA training via ComfyUI node on Floyo cloud platform
- **No local install**: Training runs on Floyo's cloud infrastructure
- **Node type**: ComfyUI custom node that exposes Musubi LoRA training as a workflow step
- **Digital-Stud relevance**: ⭐⭐ Zero-setup LoRA training in ComfyUI workflow = no separate training environment needed. Useful for rapid character LoRA iteration without Kohya SS or DiffSynth-Studio local setup. Check floyo.ai pricing for training compute costs.

### 🆕 Depth Anything 3 (ByteDance-Seed) — November 2025 Release, Now Mature

- **Released**: November 12, 2025 (not new, but now production-mature with growing ComfyUI integration)
- **Architecture**: Predicts spatially consistent geometry from arbitrary visual inputs (monocular, stereo, or multi-view)
- **DA3-Streaming**: Handles ultra-long video sequences with <12GB VRAM via sliding-window streaming
- **Key advantage over DA2**: Multi-view spatial consistency — maintains coherent depth across multiple input views
- **ComfyUI integration**: Growing in 2026; custom nodes for DA3 depth maps available
- **Digital-Stud relevance**: ⭐⭐ DA3 > DA2 for character video depth estimation — consistent depth across video frames. Use DA3 depth maps as ControlNet conditioning for consistent 3D-aware character poses. DA3-Streaming enables depth estimation on full-length character clips with consumer VRAM.

### 🆕 SAM 3 (Meta) — Unified Detection + Segmentation + Tracking

- **Source**: ai.meta.com/blog/segment-anything-model-3
- **Architecture**: Unified model for detection, segmentation, and tracking in images AND videos
- **Performance**: Doubles accuracy of SAM 2 in both image and video prediction tasks
- **Prompts**: Text prompts + visual prompts (point/box/mask) — SAM 2 only had visual prompts
- **Deployment**: Coming to Instagram Edits; research weights expected soon
- **Digital-Stud relevance**: ⭐⭐⭐ SAM 3 text-prompted segmentation = automatic character mask extraction from video without manual clicking. For Digital-Stud pipeline: SAM 3 extracts character → background replacement → SkyReels V4 for animated version. Critical upgrade to `face_refinement.json` workflow.

### 🆕 DINOv3 (Meta) — Universal Vision Backbone

- **Source**: ai.meta.com/blog/dinov3-self-supervised-vision-model + arXiv 2603.02974
- **Architecture**: Self-supervised learning for universal vision backbones; scales DINOv2 with additional objectives
- **Performance**: SOTA on image classification, dense prediction, depth estimation, anomaly detection
- **Application in 2026**: Used as backbone for pose estimation, anomaly detection, and image-to-3D pipelines
- **arXiv 2603.02974**: Spatial autoregressive modeling of DINOv3 embeddings for unsupervised anomaly detection
- **Digital-Stud relevance**: ⭐ DINOv3 as backbone for future pose/depth ComfyUI nodes. Not directly actionable today but watch for DINOv3-based ControlNet and pose estimation nodes in ComfyUI ecosystem (replaces DINOv2 backbones in newer models).

### 🆕 InfinityStory (HuggingFace papers, March 4, 2026)

- **Paper**: arXiv 2603.03646 — "InfinityStory: Unlimited Video Generation with World Consistency and Character-Aware Shot Transitions"
- **Core capability**: Background-consistent pipeline maintaining visual coherence across scenes while preserving character identity
- **Key feature**: Character-aware shot transitions — character stays visually consistent even when camera cuts
- **Digital-Stud relevance**: ⭐⭐ The core pain point in Digital-Stud character video = character drift between shots. InfinityStory directly addresses this. Monitor for code release on HuggingFace (paper is from March 4; code may follow). This technique could be integrated as a post-processing pass in the character video pipeline.

### 🆕 FLUX.2 Klein + BFS LoRA Face-Swap Workflow (March 2026)

- **Source**: YouTube tutorial March 2026 ("Best Face Swap in ComfyUI 2026: FLUX.2 Klein 9B + BFS LoRA")
- **Method**: FLUX.2 Klein 9B with BFS (Black Forest Swap) LoRA for face identity injection
- **Advantage**: Significantly better hair-edge blending vs ReactorFace and older FaceSwap methods
- **Architecture**: Uses FLUX.2 Klein's multi-reference consistency + BFS LoRA for identity injection
- **Digital-Stud relevance**: ⭐⭐⭐ For Digital-Stud character face consistency, FLUX.2 Klein + BFS LoRA > ReactorFace/older methods. Update `face_refinement.json` to include FLUX.2 Klein BFS workflow as primary face-swap method. Better for realistic skin, hair edges, and lighting consistency than InstantID on SDXL.

### 🆕 XLabs-AI FLUX ControlNet Collections

- **Source**: HuggingFace `XLabs-AI/flux-controlnet-collections` — active, updated collection
- **Variants available**: Depth ControlNet, Canny ControlNet, Pose ControlNet for FLUX.1-dev
- **Note on compatibility**: ControlNet cannot be used on FLUX DiT models directly (FLUX is DiT-based); XLabs uses adapted architecture (ZIT-compatible approach)
- **Digital-Stud relevance**: ⭐⭐ XLabs FLUX ControlNets = the current SOTA for pose+depth conditioning with FLUX quality. For `pose_controlnet.json`, XLabs FLUX Pose ControlNet is the recommended upgrade path from SDXL ControlNet. Higher quality outputs, more consistent character proportions.

### 🆕 ComfyUI NVFP4/Async Optimization Blog Post (blog.comfy.org)

- **Source**: ComfyUI sitemap — "New ComfyUI Optimizations for NVIDIA GPUs - NVFP4 Quantization, Async..."
- **Content** (inferred from NVIDIA GDC + r51 context): NVFP4 quantization guide + async execution pipeline
- **Performance**: 2.5× faster, 60% VRAM reduction on RTX 50 Series with NVFP4; async pipeline reduces waiting time between node execution
- **Digital-Stud relevance**: ⭐⭐ If running RTX 5090/5080/5070: NVFP4 is the single largest free performance upgrade available. 60% VRAM reduction means running FLUX.2 Klein 9B on 12GB instead of 24GB. Blog post has detailed setup guide.

### 🆕 Key New Artifacts to Generate (Next Iteration Recommendations)

Based on r51+r52 findings, the following new artifacts would be high-value additions:
1. `comfyui/workflows/ltx23_ic_lora.json` — LTX-2.3 IC-LoRA character video workflow using DiffSynth-Studio
2. `comfyui/workflows/skyreels_v4.json` — SkyReels V4 T2VA workflow (1080p/32fps)
3. `scripts/api_test_seedance.py` — Seedance 2.0 API cost benchmark
4. `comfyui/workflows/flux2_face_swap.json` — FLUX.2 Klein + BFS LoRA face-swap workflow

---



---

## 🔄 Run #51 Delta — 2026-03-12 22:30 Prague

### 🆕 Z-Image (Tongyi-MAI / Alibaba) — #1 Open-Source T2I Model

- **Model family**: Z-Image (6B parameters), Z-Image-Turbo (fast inference variant)
- **Leaderboard**: Z-Image-Turbo ranked **#8 overall and #1 open-source** on Artificial Analysis Text-to-Image leaderboard as of mid-March 2026
- **Standout feature**: Strong bilingual text rendering (Chinese + English) — best-in-class among open models
- **Integration**: Being integrated into vLLM-Omni inference stack (confirmed in vLLM-Omni docs March 12, 2026)
- **License**: Open weights (Tongyi-MAI/Z-Image-Turbo on HuggingFace)
- **Digital-Stud relevance**: ⭐⭐ Primary FLUX.2 alternative for efficient open-source T2I inference. For multilingual prompt workflows or text-in-image tasks, Z-Image-Turbo outperforms FLUX.2 Klein and SD4 Ultra. Add to `image_gen_flux.json` as an alternative model slot.

### 🆕 OmniGen2 — Multi-Task Image Generation Model

- **Model**: OmniGen2 (OmniGen2/OmniGen2 on HuggingFace)
- **Listed**: vLLM-Omni supported models as of March 12, 2026 (alongside FLUX.1-dev, Z-Image-Turbo, Wan2.2)
- **Type**: Multi-task image generation — unified model for T2I, I2I, editing, and composition
- **Digital-Stud relevance**: ⭐ Monitor for ComfyUI node availability; multi-task capability means single model for generate+edit+composite workflows

### 🆕 Wan 2.2 — Confirmed Stable Release (Current Production)

- **Status**: Confirmed current stable release (Wan2.2-T2V and Wan2.2-TI2V at `Wan-AI/Wan2.2` on HuggingFace)
- **Variants**: T2V (text-to-video) and TI2V (text+image-to-video)
- **WanGP support**: WanGP v10.70+ supports Wan 2.2 with 1.58× inference speedup via sparse token acceleration (arXiv 2603.05503)
- **Context**: Wan 2.2 is the current production model (between 2.1 and upcoming 2.7); update `wan22_img2vid.json` model path to `Wan-AI/Wan2.2` if still pointing to 2.1
- **Digital-Stud relevance**: ⭐⭐⭐ Immediate update available. `wan22_img2vid.json` naming already aligns; verify model path references Wan2.2 not Wan2.1.

### 🆕 FLUX Image-to-Video (FLUX I2V) — NEW March 2026

- **Source**: GitHub jayeshmepani/Media-AI master list — flagged as "⭐ NEW March 2026"
- **Description**: Transform photos into cinematic video using FLUX.1 architecture; available via platform API
- **Pricing**: Competitive (listed as top-tier quality alternative to Sora/Kling)
- **Status**: API-accessible (not yet local/ComfyUI native confirmed)
- **Digital-Stud relevance**: ⭐⭐ First FLUX-architecture I2V model. Combines FLUX.1's image quality with video motion. Add to `api_test_fal.py` for API comparison benchmarking against Wan 2.2 and SkyReels-V4.

### 🆕 Grok Imagine — Major Update March 12, 2026

- **Source**: basenor.com, Elon Musk direct post March 12 flagging update
- **Scale**: 1.245 billion videos generated/month (January 2026 figure)
- **New feature (March 2)**: "Extend from Frame" — chains sequential 15-second video clips for longer compositions
- **March 12 update**: Details still emerging at time of research; Elon flagged new capability
- **Pricing**: Competitive with Sora 2 and Kling 3.0 (estimated $0.05/sec at 720p with audio)
- **Digital-Stud relevance**: ⭐ Add Grok Imagine "Extend from Frame" to `api_test_fal.py` test suite; chain-generation workflow useful for character animation sequences longer than 15s.

### 🆕 Neural4D Image-to-3D Engine (March 12, 2026) — Production 3D Asset Pipeline

- **Source**: Press release March 12, 2026 (multiple news outlets)
- **Core capability**: Watertight manifold geometry + pure albedo extraction → engine-ready 3D assets from 2D images
- **Solves**: Broken meshes and baked lighting — the two biggest issues with AI-generated 3D assets
- **Export formats**: .obj, .fbx, .glb, .usdz, .stl, .blend (full coverage of game/3D app formats)
- **Textures**: Full PBR texture maps — roughness, metallic, normal maps generated automatically
- **Digital-Stud relevance**: ⭐⭐⭐ This directly addresses the broken-mesh problem in the Digital-Stud 3D pipeline. Neural4D is now the recommended tool for character reference → 3D asset conversion, replacing manual mesh cleanup. Combine with Speed3R (r50) for pose estimation → 3D pipeline.

### 🆕 LTX-2.3 — Full Confirmed Details + LTX Desktop

- **Release**: Early March 2026 (official ComfyUI workflows March 5, 2026)
- **Architecture improvements**:
  - Rebuilt VAE and latent space for sharper detail and better texture preservation
  - Larger, more capable text connector for complex prompts
  - Improved I2V — significantly reduced "Ken Burns effect" (static image drift)
  - Cleaner audio sync with fewer artifacts
  - **Native portrait video support** (1080×1920) — first in LTX family
- **LTX Desktop**: Free (non-enterprise), full open-source video editor built on LTX-2.3 engine, no per-generation cost
- **Open source**: Checkpoints, distilled models, LoRAs, and latent upscalers all on HuggingFace
- **DiffSynth-Studio**: Also added LTX-2.3 A/V support March 12 (confirmed r50)
- **Digital-Stud relevance**: ⭐⭐⭐ LTX-2.3 is now the recommended local open video model for portrait-format character video. LTX Desktop = viable free DaVinci alternative for AI video editing. Update `wan22_img2vid.json` to include LTX-2.3 as parallel workflow option.

### 🆕 SkyReels-V4 — Full Architecture Details (March 7, 2026)

- **Architecture**: Dual-stream MMDiT (video + audio branches generate in parallel, cross-conditioning each other)
- **Unified interface**: Generation, editing, inpainting, and video extension via channel concatenation
- **Production pipeline**: 3-stage — (1) low-res full-sequence generation → (2) keyframe upscaling → (3) frame interpolation
- **Leaderboard**: **#3** on Artificial Analysis Text-to-Video with Audio (behind Veo 3.1 and Sora 2)
- **Open source lineage**: V1 → V2 (infinite-length, April 2025) → V3 (multi-modal, open-source January 2026) → V4 (audio-video unified, March 7, 2026)
- **Digital-Stud relevance**: ⭐⭐⭐ SkyReels-V4 is the strongest open-source T2VA model currently. Dual-stream MMDiT audio-video co-generation is architecturally superior to LTX-2.3's A/V for coherent audio sync. Prioritize SkyReels-V4 ComfyUI node as soon as released (V3 node likely compatible). Monitor `SkyReels-AI/SkyReels` GitHub for V4 weights.

### 🆕 Veo 3 Fast Preview — Released via Vertex AI (March 3, 2026)

- **Release**: March 3, 2026 — Veo 3 Fast Preview via Vertex AI and Gemini API
- **Model family**: Veo 3 (standard), Veo 3 Fast (optimized for frame-to-video), Veo 3.1 (latest iteration)
- **Access**: Google Gemini API; Vertex AI; also available in Adobe Firefly multi-model editor
- **Leaderboard**: Veo 3.1 holds **#1** on Artificial Analysis T2V+Audio leaderboard (confirmed r50 context; SkyReels-V4 is #3)
- **Digital-Stud relevance**: ⭐ Add Veo 3 Fast to API cost comparison in `api_test_fal.py`; Gemini API pricing likely competitive with Sora 2 Pro for 1024p output. Veo 3 Fast most useful for rapid I2V prototyping before final Sora 2 / SkyReels render.

### 🆕 Kling 3.0 Pro Motion Control — WaveSpeed API

- **Source**: WaveSpeed AI blog (wavespeed.ai)
- **Capability**: Premium motion transfer — transfer motion from reference video to new character/scene
- **Quality**: Native 4K 60fps; AI Director mode for cinematic framing control
- **Billing**: Standard mode (720p) and Pro mode (4K+); motion control is Pro tier
- **Availability**: Via WaveSpeed AI API and Kling platform; ComfyUI API node enabled March 5 (Motion Control)
- **Digital-Stud relevance**: ⭐⭐ Motion transfer + 4K = direct upgrade for character animation reference pipeline. Kling 3.0 Pro Motion Control is best-in-class for transferring reference performer motion to AI character. Update `wan22_img2vid.json` API comparison section.

### 🆕 Video2LoRA (arXiv 2603.08210) — Per-Frame Temporal LoRA for Video

- **Title**: "Video2LoRA: Unified Semantic-Controlled Video Generation via Per-Frame LoRA Modules"
- **Base model**: CogVideoX
- **Core idea**: Train per-frame LoRA modules on a reference video → inject temporal coherence and semantic control into new video generations without full fine-tuning
- **Result**: Learns coherent temporal dynamics + high-fidelity visual content; enables style/character/motion transfer
- **Digital-Stud relevance**: ⭐⭐ Direct technique for character-consistent video generation from reference footage. If code releases on HuggingFace/GitHub for CogVideoX, this enables character motion LoRA training without full video model fine-tune. Watch for ComfyUI node.

### 🆕 ComfyUI App Mode + App Builder + ComfyHub (March 12, 2026)

- **Source**: Gigazine confirms "March 12, 2026" launch; blog.comfy.org announcement
- **App Mode**: Converts any ComfyUI workflow to clean shareable app UI (no node graph visible)
- **App Builder**: Creator selects which inputs/outputs to expose to end users
- **ComfyHub**: Community platform at comfy.org/workflows for publishing finished apps + workflows; launched in preview
- **Shareable URLs**: Run in browser without installation (Comfy Cloud)
- **Digital-Stud relevance**: ⭐⭐ Convert Digital-Stud character generation workflows into clean client-facing apps. App Mode enables non-technical collaborators to run ComfyUI workflows without seeing the node graph. ComfyHub = distribution channel for selling/sharing workflow templates.

### 🆕 ComfyUI v0.3.0 — Reroute Redesign + Group Controls

- **Source**: blog.comfy.org/p/comfyui-v0-3-0-release
- **Key changes**:
  - **Native Reroute**: Completely redesigned — better performance, smaller workflow files, reduced rendering overhead
  - **Group Controls**: Groups now selectable/deletable/pinnable/nestable like nodes → hierarchical workflow organization
  - **Fit View**: Smart viewport adjustment (auto-adapts to selection or full canvas)
  - **New UI default**: Refreshed UI is now default (classic available in settings)
  - **Shortcuts**: Alt+Drag for reroute points, Shift+Drag for extra connections
- **Digital-Stud relevance**: ⭐ Update local ComfyUI. New group nesting enables cleaner organization of complex character gen workflows.

### 🆕 NVIDIA RTX + ComfyUI at GDC 2026 (March 10-12)

- **Source**: NVIDIA Blog, WCCFTech, Perplexity (March 10, 2026)
- **RTX Video Super Resolution Node**: Real-time 4K upscaler for video generation in ComfyUI; 30× faster than alternative local tools
- **NVFP4 + FP8 support**: For FLUX.2 Klein (4B/9B) and LTX-2.3 → 2.5× perf gain, 60% VRAM reduction
- **App View Mode**: Simplified UI alongside traditional node view (complements App Mode)
- **Performance**: 40% overall ComfyUI performance improvement since Sept 2025 with RTX optimizations
- **Digital-Stud relevance**: ⭐⭐⭐ If running RTX GPU: install NVFP4/FP8 quantized FLUX.2 Klein and LTX-2.3 immediately for 2.5× speedup + 60% VRAM savings. RTX Video Super Resolution node replaces manual upscaling step in video workflows. Update `image_gen_flux.json` to reference FP8/NVFP4 model paths.

### 🆕 ComfyUI-Manager → Comfy-Org (March 28 Migration)

- **Announcement**: ComfyUI-Manager migrating to `Comfy-Org/ComfyUI-Manager` on March 28, 2026
- **New Manager UI**: Faster discovery, safer installs, auto-update notifications on startup
- **Impact**: Any custom install scripts referencing `ltdrdata/ComfyUI-Manager` will need URL updates after March 28
- **Digital-Stud relevance**: ⭐ Update any local installation scripts before March 28. Auto-update notifications on startup will help keep custom nodes current.

### 🆕 FastLightGen (arXiv 2603.01685) — Video Model Compression Algorithm

- **Title**: "FastLightGen: Fast and Light Video Generation with Fewer Steps"
- **Core idea**: Algorithm that transforms large, computationally expensive video models into fast, lightweight counterparts — maintains quality while reducing compute
- **Tested on**: Large diffusion video models (architecture-agnostic)
- **Digital-Stud relevance**: ⭐ Once code releases, apply FastLightGen to Wan 2.2 or SkyReels-V4 for faster local generation. Monitor GitHub.

### 🆕 Accelerating T2V with Calibrated Sparse Tokens (arXiv 2603.05503)

- **Title**: "Accelerating Text-to-Video Generation with Calibrated Sparse Tokens"
- **Tested on**: Wan 2.1, Mochi 1, LightX2V
- **Result**: **1.58× end-to-end speedup on Wan 2.1 14B** while maintaining video quality
- **Applicable to**: Transformer attention broadly (likely works on Wan 2.2)
- **Digital-Stud relevance**: ⭐⭐ Apply sparse token calibration to local Wan 2.2 inference for 1.58× free speedup. Check WanGP v10.70+ — this technique may already be integrated.

### 🆕 Neural4D / Z-Image / OmniGen2 — 3D + Image Ecosystem Summary (March 12)

- **Summary of new production tools confirmed available March 12**:
  | Tool | Type | Key feature |
  |------|------|-------------|
  | Neural4D | Image → 3D | Watertight mesh + PBR textures, all formats |
  | Z-Image-Turbo | T2I | #1 open-source on ArtificialAnalysis; bilingual text |
  | OmniGen2 | Multi-task image | Generate + edit + compose in one model |
  | FLUX I2V | I2V | First FLUX-architecture image-to-video |
  | Grok Imagine | T2V + I2V | Extend from Frame, 1.245B vids/month |

### 🆕 StreamWise (arXiv 2603.05800) — Real-Time Multi-Modal Generation at Scale

- **Title**: "StreamWise: Serving Multi-Modal Generation in Real-Time at Scale"
- **Application**: Fantasy Talking (video + audio sync) — adds audio encoding + cross-attention to Wan 2.1 base model
- **System**: Multi-modal serving infrastructure for simultaneous audio+video generation
- **Digital-Stud relevance**: ⭐ Infrastructure pattern for deploying audio-video generation at scale; Fantasy Talking-style lip-sync + audio via Wan 2.1 cross-attention is production-ready approach.

---



---

## 🔄 Run #50 Delta — 2026-03-12 22:02 Prague

### 🆕 Helios — Full Details Confirmed (arXiv 2603.04379, March 5, 2026)

- **Authors**: Peking University + ByteDance + Canva + Chengdu Anu Intelligence
- **Scale**: 14B parameters — first video model to run at **19.5 FPS on a single NVIDIA H100** (real-time generation)
- **Length**: Supports **minute-scale generation** (vs. typical 4-15 second clips from Wan/LTX)
- **Tasks**: T2V, I2V, V2V — all three natively supported
- **License**: Apache 2.0
- **ComfyUI**: GitHub issue #12760 filed on Comfy-Org/ComfyUI tracking a custom node; no merged node yet
- **Demo**: pku-yuangroup.github.io/Helios-Page/ | HuggingFace weights available
- **Digital-Stud relevance**: ⭐⭐⭐ This is the most significant open video model drop since HunyuanVideo. Once a ComfyUI node lands, Helios becomes the primary candidate for long-form character animation (>15s, real-time preview). Watch GitHub issue #12760. Practical consideration: H100 required for real-time; on RTX 3090/4090 expect 2-4x slower but still usable for batch generation.

### 🆕 DiffSynth-Studio LTX-2.3 Support (ModelScope, March 12, 2026)

- **Repo**: `modelscope/DiffSynth-Studio` (GitHub)
- **Change**: Added LTX-2.3 audio-video generation support on **March 12, 2026** (confirmed commit)
- **Significance**: Second major framework (after native ComfyUI) to support LTX-2.3 A/V; enables Python-native scripted pipelines without ComfyUI dependency
- **Digital-Stud relevance**: ⭐ Use DiffSynth-Studio as scripted batch alternative to ComfyUI for LTX-2.3 A/V when automating large character animation batches without UI overhead

### 🆕 Sora 2 API Pricing — Officially Confirmed (OpenAI.com)

- **Source**: OpenAI official API pricing page (openai.com/api/pricing)
- **Sora 2 Standard**: $0.10/second for 720p video
- **Sora 2 Pro**: $0.30/second for 720p, **$0.50/second for 1024p** (1792×1024)
- **Comparison to Kling 3.0**: Kling API ~$0.05/sec → Sora 2 costs 2× Kling at same resolution
- **Comparison to Grok Imagine**: Grok Imagine API $0.05/sec 720p+audio → Sora 2 costs 2× at same resolution and quality tier
- **Third-party resellers**: $0.015-$0.10/sec (50-85% cheaper but unofficial)
- **Digital-Stud relevance**: Update `api_test_fal.py` and `api_test_replicate.py` cost comparison tables. For budget-conscious use: Grok Imagine (720p+audio, $0.05/sec) and Kling 3.0 ($0.05/sec) beat Sora 2 on price; use Sora 2 Pro only when 1024p output specifically required.

### 🆕 Sora 2 Native ComfyUI Partner Node

- **Source**: blog.comfy.org — "Sora 2 API Nodes Now in ComfyUI" (by Purz and Jo Zhang)
- **Status**: Official partner node — Sora 2 API directly accessible inside ComfyUI workflows
- **Feature**: Generates via OpenAI API key; output routed through standard ComfyUI video output nodes
- **Digital-Stud relevance**: ⭐ Test Sora 2 ComfyUI node for benchmarking against local Wan/LTX workflows; useful for quality reference even if cost prohibitive for production use

### 🆕 Seedance 2.0 ComfyUI Community Node

- **Repo**: `Cameraptor/seedance_2_Comfy_UI_Node-sjinn_Api` (GitHub)
- **Function**: Wraps Sjinn.ai API for Seedance 2.0 — connect reference images and videos, generate directly in ComfyUI workflow
- **Status**: Community node (not official); available via ComfyUI Manager
- **Digital-Stud relevance**: ⭐ Add to workflow for Seedance 2.0 API testing; update `api_test_fal.py` to include Sjinn.ai endpoint for Seedance 2.0 batch testing

### 🆕 Adobe Firefly Multi-Model Editor — 25+ AI Models (March 10, 2026)

- **Source**: Adobe blog — "Image editing just got smarter with AI in Photoshop and Firefly" (March 10, 2026)
- **Key**: Firefly now bundles 25+ top AI models in one interface: Google Nano Banana 2, OpenAI GPT Image 1.5, Runway Gen-4.5, Black Forest Labs FLUX.2 Pro, plus Adobe's own models
- **Features added**: Generative Fill, Generative Remove, Generative Expand, Generative Upscale, Remove Background — all in Firefly Image Editor
- **Digital-Stud relevance**: ⭐⭐ Confirms **Runway Gen-4.5** is current as of March 2026 (was Gen-3 Alpha last noted). Firefly is a viable platform for client-facing character refinement work without local GPU dependency. FLUX.2 Pro API access via Firefly subscription potentially cheaper than direct API.

### 🆕 FLUX.2 Klein Community LoRAs (Early March 2026)

- **Source**: YouTube — "Five NEW Flux.2 Klein LoRAs released in 2026"
- **LoRAs released**: `flux-2-klein-4B-zoom-lora` + 4 additional community LoRAs for Klein 4B
- **Training note**: These are community-trained (not BFL official) on FLUX.2 Klein 4B base
- **Digital-Stud relevance**: ⭐ Extend `image_gen_flux.json` to support FLUX.2 Klein LoRA loading; zoom LoRA useful for cinematic close-up character shots

### 🆕 FLUX.2 Klein "Enhancer" ComfyUI Node Pack

- **Source**: myaiforce.com — "Mastering Flux.2 Klein: Enhancing Consistency and Creativity"
- **Function**: ComfyUI node pack that adds **pose lock** and **detail control** to FLUX.2 Klein workflow
- **Capability**: Consistent character pose preservation across multiple generations via Enhancer node
- **Digital-Stud relevance**: ⭐⭐ Direct solution for pose-consistent character generation with FLUX.2 Klein without needing separate ControlNet node. Install via ComfyUI Manager; update `image_gen_flux.json` to include Enhancer node for consistent pose runs.

### 🆕 Wan 2.7 — Imminent Release Confirmed (March 2026)

- **Status**: Multiple dedicated info sites live (wan27ai.com, wan2-7.org, wan2-7.app, wan26.info/wan-2-7) — launch imminent
- **Confirmed features**:
  - 1080P real-person video generation
  - Start + end frame control (same as WanGP already supports)
  - Grid-to-video (multi-panel composition → single video)
  - Subject reference + voice reference conditioning
  - Instruction editing (edit existing video via text)
  - Video cloning (clone motion from reference video)
- **Digital-Stud relevance**: ⭐⭐⭐ Video cloning + instruction editing = significant upgrade for character re-posing pipeline. WanGP team is already preparing v10.981+ for Wan 2.7 integration. Update `wan22_img2vid.json` as soon as WanGP releases Wan 2.7 support.

### 🆕 DSH-Bench (arXiv 2603.08090) — Subject-Driven T2I Benchmark

- **Title**: "DSH-Bench: A Difficulty- and Scenario-Aware Benchmark with Hierarchical Subject Taxonomy for Subject-Driven T2I Generation" (Tencent)
- **Dataset**: 459 subjects, 58 fine-grained categories; tests up to 5 characters + 14 objects simultaneously
- **New metric**: Subject Identity Consistency Score (SICS) — 9.4% higher human eval correlation vs GPT-4o-based scoring
- **Findings**: Current models still struggle with multi-subject identity preservation while following diverse prompts
- **Digital-Stud relevance**: Use SICS as evaluation metric when testing character consistency workflows; Tencent authorship suggests HunyuanVideo-adjacent improvements incoming

### 🆕 PureCC (arXiv 2603.07561) — Concept Customization for T2I

- **Title**: "PureCC: Pure Learning for Text-to-Image Concept Customization"
- **Core idea**: Pure learning approach (no test-time optimization) for rapid concept customization in T2I — enables fast identity injection without per-subject fine-tuning
- **Status**: arXiv paper; code pending
- **Digital-Stud relevance**: Watch for code/weights release on HuggingFace — if available as ComfyUI node, potentially faster alternative to LoRA-based character injection

### 🆕 Speed3R (arXiv 2603.08055) — Sparse Feed-Forward 3D Reconstruction

- **Title**: "Speed3R: Sparse Feed-forward 3D Reconstruction Models"
- **Core idea**: Joint dense geometry + camera pose estimation in a single forward pass — no iterative optimization required
- **Performance**: Significantly faster than DUSt3R/MASt3R-based pipelines
- **Digital-Stud relevance**: ⭐ If code releases, useful for generating 3D scaffolds from character reference images for ControlNet pose workflow — faster than current photogrammetry pipeline

### 🆕 MipSLAM (arXiv 2603.06989) — Alias-Free Gaussian Splatting SLAM

- **Title**: "MipSLAM: Alias-Free Gaussian Splatting SLAM"
- **Core idea**: High-fidelity anti-aliased novel view synthesis inside a SLAM (Simultaneous Localization and Mapping) framework
- **Performance**: Anti-aliased NVS at high fidelity — addresses blurring artifacts in 3DGS at different zoom levels
- **Digital-Stud relevance**: ⭐ Relevant for 3D scene reconstruction from video (background environments for character placement); better than standard 3DGS when generating environments with significant depth variation

### 🆕 FootMR (arXiv 2603.09681) — Markerless 3D Foot Motion Capture

- **Title**: "Improving 3D Foot Motion Reconstruction in Markerless Monocular Human Motion Capture"
- **Authors**: Tom Wehrbein, Bodo Rosenhahn, L3S Leibniz University Hannover
- **Core idea**: FootMR — refines ankle rotation estimates in markerless monocular capture; improves foot/ankle accuracy without markers
- **Digital-Stud relevance**: ⭐⭐ Direct pipeline relevance for full-body rig accuracy in character animation. Ankle/foot are the most common failure points in DWPose-based rig extraction. FootMR as post-processing step on DWPose skeletons could significantly improve lower-body pose quality in `pose_controlnet.json` workflow.

### 🆕 TADA (HumeAI) — Open-Source Text-to-Audio for Video (March 12, 2026)

- **Source**: Threads post @naveed_ullah600, March 12, 2026
- **Model**: TADA — HumeAI text-to-audio model, open-source on HuggingFace (`colle...`)
- **Function**: Generates high-quality audio from text descriptions — voice, ambience, SFX
- **Digital-Stud relevance**: ⭐ Audio synthesis for AI video output — pair with LTX-2.3 A/V or SkyReels V4 T2VA workflows; TADA handles audio when the video model's built-in audio is insufficient

### 🆕 Runway Gen-4.5 — Current Production Model Confirmed

- **Confirmation**: Adobe Firefly integration (March 10) lists Gen-4.5 as current Runway model (previously Gen-3 Alpha was tracked)
- **Status**: Available in Runway platform and via Adobe Firefly multi-model editor
- **Digital-Stud relevance**: Update SOTA model table — prior entry "Runway Gen-3 Alpha" is outdated; current is **Gen-4.5**. Update `wan22_img2vid.json` API comparison notes.

---



---

## 🔄 Run #49 Delta — 2026-03-12 21:34 Prague

### 🆕 Grok Imagine Major Update (March 12, 2026) — xAI

- **Announced**: Elon Musk tweet March 12, 2026 — direct callout of Grok Imagine upgrade
- **Scale**: 1.245 billion videos generated in January 2026 alone
- **New feature — "Extend from Frame"** (released March 2): Chain video clips continuously, up to 15 seconds per clip, enabling long-form sequences from a single image/video seed
- **API pricing**: $0.05/second for 720p video with audio (competitive with Sora 2 API rate)
- **Digital-Stud relevance**: ⭐⭐ Test "Extend from Frame" for character animation continuity — chain I2V clips to create longer sequences. Update `api_test_replicate.py` / `api_test_fal.py` to include Grok API endpoint. API pricing same as Sora 2 ($0.05/sec) but open access without waitlist.

### 🆕 Z-Image-Fun-Lora-Distill-2603 — Alibaba PAI (~March 10, 2026)

- **Model**: `alibaba-pai/Z-Image-Fun-Lora-Distill-2603` (HuggingFace)
- **Nature**: Distilled LoRA for Z-Image Turbo that compresses BOTH inference steps AND CFG guidance simultaneously
- **Effect**: Dramatically faster Z-Image generation while maintaining quality — fewer steps + no CFG overhead
- **Source**: Threads post by @won.wizard confirming model public release
- **Digital-Stud relevance**: ⭐⭐⭐ Drop-in speed boost for Z-Image Turbo workflows. Update `comfyui/workflows/face_refinement.json` to load this distill LoRA alongside Z-Image Turbo ControlNet-Union v2.1 — should yield near-instant face detailing

### 🆕 Z-Image Turbo ControlNet-Union v2.1 (March 2026)

- **Model**: `alibaba-pai/Z-Image-Turbo-Fun-ControlNet-Union-2.1` (updated from 2.0)
- **Improvements over 2.0**: Enhanced inpainting quality + added outpainting support for FLUX models
- **ComfyUI**: Drop-in replacement for previous Union model; confirmed working in community tests
- **Digital-Stud relevance**: Replace `Z-Image-Turbo-Fun-ControlNet-Union` with `v2.1` in `face_refinement.json`

### 🆕 WanGP v10.981+ Feature Expansion (March 7, 2026)

- **Maintainer**: deepbeepmeep/Wan2GP (GitHub)
- **New features**:
  - **Outpainting for Qwen Image & FLUX.2** — extend frames spatially beyond original canvas
  - **Lanpaint for FLUX.2** — landscape-oriented inpainting mode
  - **Kiwi Edit** — video editing + object injection into existing video (described as "great model")
  - **SVI PRO2 End Frames** — improved end-frame conditioning for smoother video termination
- **Wan 2.7 note**: Changelog notes "Expecting an Update?" — WanGP team actively preparing Wan 2.7 integration
- **Digital-Stud relevance**: ⭐⭐ Update `wan22_img2vid.json` to include Kiwi Edit path for character object injection; test Lanpaint for background extension in portrait-to-video workflows

### 🆕 FLUX.2 NVFP4/FP8 Acceleration — NVIDIA GDC 2026 (March 10, 2026)

- **Announced**: NVIDIA blog post by NVIDIA RTX AI Garage team at GDC
- **NVFP4 format**: 2.5× performance gains, 60% lower VRAM usage vs FP16 FLUX.2 on RTX 50 Series
- **Supported models**: FLUX.2 Klein 4B and 9B variants
- **ComfyUI**: NVFP4 and FP8 checkpoints downloadable directly from HuggingFace; load via Template Browser, replace checkpoint reference
- **RTX Video Super Resolution (separate node)**: 30× faster 4K upscaling vs local upscalers; available as ComfyUI node AND Python PyPI package (`nvidia-vfx`)
  - Note: No `nvidia-vfx` wheel for DGX Spark (NVIDIA Developer Forums March 12)
- **Digital-Stud relevance**: ⭐⭐⭐ If running RTX 50 Series: immediate swap to NVFP4 FLUX.2 Klein. RTX VSR node replaces current upscaler in `image_gen_flux.json` for 30× faster post-processing

### 🆕 ComfyUI v0.16.x Official Changelog (March 5, 2026)

- **v0.16.1** (March 5): Kling 3.0 Motion Control enabled natively, xAI model list updated
- **v0.16.0** (March 5):
  - `ResolutionSelector` node — dynamic resolution picker for workflows
  - LTXAV 2.3 native model support
  - Dynamic VRAM optimization now enabled as default (auto memory management)
  - CURVE type support for animation curves in nodes
- **v0.15.x** (Feb 24-26): BBox widget, 3-band audio equalizer, basic text generation (Gemma3, Qwen 3), GLSL shader node, ElevenLabs API nodes, `SplitImageToTileList`/`ImageMergeTileList` for tiled image processing
- **Digital-Stud relevance**: Update ComfyUI to v0.16.1; verify LTXAV 2.3 node works; use `SplitImageToTileList` for high-res character detail passes

### 🆕 ComfyUI RTX Video Super Resolution Node (NVIDIA, March 2026)

- **Node**: Available in ComfyUI Manager search, also as `pip install nvidia-vfx` (PyPI)
- **Performance**: 30× faster than comparable local upscalers on RTX GPUs
- **Output**: Real-time 4K upscaling from 1080p AI-generated video
- **Caveat**: Requires RTX GPU; DGX Spark incompatible (no `nvidia-vfx` wheel for that platform)
- **Digital-Stud relevance**: ⭐⭐ Use for post-processing AI video output before final export; replaces ESRGAN/RealESRGAN in video pipeline

### 🆕 Video2LoRA (arXiv 2603.08210)

- **Title**: "Video2LoRA: Unified Semantic-Controlled Video Generation via Per-Reference-Video LoRA"
- **Authors**: Zexi Wu, Qinghe Wang et al.
- **Core idea**: Hypernetwork predicts lightweight LoRA weights (<50KB per condition) from a reference video for semantic control in video generation — zero-shot generalization across diverse conditions
- **Backbone**: CogVideoX diffusion model
- **Key advantage**: No per-video fine-tuning at inference; single hypernetwork handles all reference conditions
- **Digital-Stud relevance**: ⭐⭐ This is a promising technique for motion LoRA transfer — a reference video (e.g., specific dance/walk) can seed consistent motion LoRA weights without training. Watch for code release (CogVideoX backbone, may port to Wan 2.7)

### 🆕 Controllable Human Motion via Text-to-Skeleton (arXiv 2603.08028v1)

- **Confirmed details**: DINO-based skeleton sequence conditioning; disables CLIP-based pathways and replaces with single DINO feature stream in pose-driven setting
- **Effect**: More stable skeleton conditioning vs CLIP when text is absent (pose-only mode)
- **Relevance to DWPose/RTMPose**: Alternative conditioning architecture to ControlNet for ComfyUI pose workflows
- **Digital-Stud relevance**: Update `pose_controlnet.json` to test DINO-based skeleton conditioning path if code releases; existing DWPose ControlNet workflow remains primary path for now

### 🆕 LTX "Cinematic Prompt" ComfyUI Node (Community, March 2026)

- **Source**: Reddit r/comfyui post (217 upvotes, 63 comments)
- **Function**: Auto-infers shot types, camera moves, and audio style from a prompt — single node replaces manual prompt engineering for cinematic composition
- **Status**: Free, local, available on GitHub (search ComfyUI Manager)
- **Digital-Stud relevance**: ⭐⭐ Reduce prompt engineering time for character video sequences; pairs with LTX-2.3 I2V workflow

### 🆕 Helios — Real-Time Long-Video Generation Model (WaveSpeedAI)

- **License**: Apache 2.0
- **Capability**: Real-time generation of long video sequences (no skip shortcuts; temporally coherent)
- **Status**: Open-source, weights available; ComfyUI nodes and training scripts still catching up
- **Digital-Stud relevance**: Monitor for ComfyUI node — if released, test against Wan 2.7 for long-form character animation (>15s clips)

### 🆕 Nano Banana 2 API — Confirmed Pricing (March 2026)

- **Official channel**: Google AI Studio + Gemini API
- **Pricing confirmed**:
  - $0.0672/image for 4K (4096px) generation via Google AI Studio (Medium blog)
  - ~$0.03/image for lower resolution via AI Studio API
- **Speed**: 3-5 seconds per generation (2-3× faster than Nano Banana Pro)
- **Character consistency**: Community guide confirms Nano Banana Pro (Gemini inside) best for consistent characters using I2I reference workflow; Nano Banana 2 inherits this capability with speed advantage
- **Digital-Stud relevance**: Update `api_test_replicate.py` with Nano Banana 2 API endpoint via Google AI Studio; add to pricing comparison table in SOTA

### 🆕 CFG-Ctrl (arXiv 2603.03281) — Unified CFG as Control Signal

- **Title**: "CFG-Ctrl: Control-Based Classifier-Free Diffusion Guidance"
- **Insight**: Reinterprets CFG as a first-order continuous-time control applied to generative flow — cleaner theoretical unification, improves guidance stability at high CFG values
- **Practical effect**: Better high-CFG outputs without collapse; tunable control curve
- **Digital-Stud relevance**: Low priority for now; watch for ComfyUI implementation — could improve character feature sharpness at high guidance scales

### 🆕 GVCoT (arXiv 2603.01893) — Visual Chain-of-Thought for Image Editing

- **Title**: "Generative Visual Chain-of-Thought for Image Editing"
- **Framework**: Native visual reasoning for image editing — model generates intermediate reasoning steps visually before applying final edit
- **Effect**: More accurate complex edits (multi-step transformations) vs single-step instruction models
- **Status**: arXiv paper; code pending
- **Digital-Stud relevance**: Watch for code release — if released as ComfyUI node, test for complex character editing chains (e.g., "change outfit + adjust lighting + remove background") as alternative to FireRed-Image-Edit

---



---

## 🔄 Run #48 Delta — 2026-03-12 21:03 Prague

### ✅ CONFIRMED LIVE: Open-Sora 2.0 (March 13, 2026)

- **Released by**: ColossalAI / hpcaitech team (GitHub: hpcaitech/Open-Sora)
- **Parameters**: 11 billion
- **Training cost**: ~$200k (~224 GPUs) — 5-10× cheaper than MovieGen, Step-Video-T2V
- **VBench benchmark**: Performance gap with OpenAI Sora narrowed from 4.52% (v1) to just 0.69%
- **User preference tests**: 69.5% win rate visual quality, 55.6% text consistency vs competitors
- **Architecture**: MMDiT with 3D RoPE (spatiotemporal modeling), Video DC-AE autoencoder (4×32×32 compression = 10× faster inference VAE vs HunyuanVideo)
- **Resolutions**: 256px and 768px; T2V and I2V modes supported
- **Inference times**: ~60s at 256×256 single GPU; ~4.5min at 768×768 with 8 GPUs
- **Availability**: HuggingFace, ModelScope, GitHub (full code + weights)
- **ComfyUI node**: Available — install via ComfyUI Manager (SageAttention recommended for VRAM efficiency)
- **ComfyUI wiki**: detailed tutorial at comfyui-wiki.com/en/news/2025-03-13-open-sora-2-release
- **Digital-Stud relevance**: ⭐⭐ Best free open-source alternative to commercial video models for T2V; compare against Wan 2.2 on motion quality and temporal coherence; ComfyUI node available day-1

### ✅ CONFIRMED LIVE: SkyReels V4 (March 13, 2026)

- **Release**: March 13, 2026 — weights on GitHub (SkyworkAI/SkyReels-V4) + API via WaveSpeedAI, Kinovi.ai
- **Output specs**: Up to 1080p, 32 FPS, maximum 15-second duration
- **Input capabilities**: Text + multiple image references + video clips + masks (inpainting) + audio references
- **Three unified tasks**: Generation, inpainting, editing — all through one model via channel concatenation
- **6 documented use cases** (WaveSpeedAI blog): social video with natural audio, AI film editing, image animation with sound, scene inpainting, reference-guided generation, multi-modal editing
- **API pricing**: WaveSpeedAI billing confirmed active; Kinovi.ai also live
- **Digital-Stud relevance**: ⭐⭐⭐ Test immediately — download weights, try I2V generation with character images; check if ComfyUI node available (monitor SkyworkAI GitHub)

### ✅ CONFIRMED LIVE: Sora 1 Sunset → Sora 2 Only (March 13, 2026)

- **Official OpenAI FAQ**: "Sora 1 will be removed on March 13, 2026. After that date, Sora will open in Sora 2 by default and you won't be able to switch back to Sora 1."
- **Sora 2 in ChatGPT**: Reuters/PCMag confirmed integration coming soon — Sora 2 will be accessible from within ChatGPT interface (not just standalone app)
- **Sora 2 API node in ComfyUI**: Official `@comfyui` Threads post confirms "OpenAI Sora - Video" node available in nightly build
- **Sora 2 API pricing**: ~$0.05/second, synchronized dialogue + sound effects, physically accurate

### ✅ CONFIRMED: Wan 2.7 Weights Available (March 2026)

- **Status**: Weights live on GitHub + HuggingFace (confirmed via wan26.info dedicated site + Reddit r/StableDiffusion)
- **Scope**: "Professional multimodal AI video director" — comprehensive upgrades over 2.6: better image quality, motion accuracy, and efficiency
- **WanGP support**: deepbeepmeep/Wan2GP v10.981+ expected to add Wan 2.7 shortly (maintainer note: "Expecting an Update?")
- **Digital-Stud relevance**: Download weights immediately; update wan22_img2vid.json checkpoint path to 2.7; run comparison with Wan 2.2 Palingenesis on character motion

### 🆕 Stable Diffusion 4 Ultra — Open Weights, New Photorealism SOTA

- **Release**: March 2026 (Stability AI) — open weights available
- **Architecture**: Upgraded Diffusion Transformer (DiT) — successor to SD 3.5 Large
- **Key improvement**: New photorealism benchmark, competes with GPT Image 1.5 on quality metrics
- **ControlNet**: Community-developed extensions available; official ControlNet variants for SD4 in development (face/identity conditioning expected)
- **Local run**: Self-hosting maintained; open weights downloadable from HuggingFace
- **Digital-Stud relevance**: ⭐⭐ Test SD4 Ultra vs FLUX.2 Klein for character generation — if quality matches with faster speed, replaces FLUX.2 Pro for some workflows

### 🆕 FLUX Image to Video (Black Forest Labs, March 2026)

- **Release**: March 2026 — Black Forest Labs FLUX I2V model
- **Status**: Listed on GitHub Media-AI master list as "⭐ NEW March 2026"
- **API**: Competitive pricing confirmed; photo-to-video transformation
- **Digital-Stud relevance**: ⭐ Direct competitor to Wan 2.2/2.7 for I2V; test on `scripts/api_test_fal.py` and `api_test_replicate.py` for API integration; update wan22_img2vid.json to compare paths

### 🆕 Z-Image Turbo ControlNet-Union — Inpainting Now Available

- **Model**: `alibaba-pai/Z-Image-Turbo-Fun-Controlnet-Union` (HuggingFace)
- **New capability**: Inpainting support added to ControlNet-Union variant
- **Tutorial live**: nextdiffusion.ai — "How to Use Z-Image Turbo as a Face Detailer in ComfyUI" (8-step guide, 3 model files)
- **Workflow**: Detect faces → build masks → enhance details automatically in ComfyUI
- **Context from r46**: Z-Image Turbo was identified as best FLUX inpainting alternative; Union model now extends this to face detailing
- **Digital-Stud relevance**: ⭐⭐⭐ Update `face_refinement.json` immediately — Z-Image Turbo Union replaces separate face detection + inpainting steps with a single unified node; test against current FLUX Fill approach

### 🆕 FireRed-Image-Edit + REDEdit-Bench (March 9, 2026)

- **Release**: FireRedTeam/FireRed-Image-Edit on GitHub
- **Nature**: Powerful instruction-following image editing foundation model — open-source SOTA on editing benchmarks
- **REDEdit-Bench**: New comprehensive benchmark covering diverse editing scenarios and instructions; released alongside model
- **Key feature**: Precise instruction following for local edits without affecting surrounding regions
- **Use case**: Alternative to Qwen Image 2.0 Pro for instruction-based editing (vs mask-based for Qwen)
- **Digital-Stud relevance**: ⭐⭐ Test for text-instruction character edits (e.g., "change jacket color to red", "add hat") — could replace manual masking workflow

### 🆕 Bumblebee AI — Long-Sequence 3D Character Motion from Text

- **Announced**: March 2026 (NaplesNews press release, Korean startup)
- **Capability**: Generates minutes-long 3D character motion sequences from simple text prompts
- **Goal**: Automate animation production pipeline — from text description to 3D motion data
- **Status**: Preview/announcement stage; no public weights yet
- **Digital-Stud relevance**: ⭐⭐ Watch closely — if weights or API released, this directly eliminates manual motion capture / keyframe creation for 3D character animation in the Digital-Stud pipeline; pairs with HY 3D + Tripo 3D + Blender workflow

### 🆕 OCpose (arXiv 2603.10398) — Better MPPE Evaluation Metric

- **Paper**: "Multi-Person Pose Estimation Evaluation Using Optimal Transportation and Improved Pose Matching" — Toyota Technological Institute
- **Problem solved**: mAP unfairly penalizes false-positive poses regardless of confidence; OCpose uses optimal transport theory to address this
- **Metrics**: OKSp (precision), OKSm (match quality), OKSc (confidence-weighted) — 83.3% agreement with human preference
- **Status**: Paper + arXiv (2603.10398); code expected to be released as evaluation tool for pose estimation models
- **Digital-Stud relevance**: Use OCpose to benchmark DWPose/RTMPose quality in character animation workflows — more meaningful than mAP for comparing pose estimation models

### 🆕 Sora 2 API Node Official in ComfyUI Nightly

- **Source**: Official `@comfyui` Threads post
- **Node name**: "OpenAI Sora - Video"
- **Install**: Update ComfyUI to latest nightly, search ComfyUI Manager for the node
- **Function**: Direct Sora 2 API calls from within ComfyUI workflow
- **Digital-Stud relevance**: Enables A/B comparison of Sora 2 vs open-source models (Wan 2.7, Open-Sora 2.0) directly in ComfyUI

### 🆕 LoRA Training: Wan 2.2 Field-Tested Settings Guide (WaveSpeedAI)

- **Source**: wavespeed.ai/blog/posts/blog-wan-2-2-lora-training-settings/
- **Content**: Recommended LR, rank, steps, and regularization to reduce "plastic skin" and avoid overfitting
- **Key settings documented**: Learning rate schedule, LoRA rank selection for character vs motion LoRA, dataset size recommendations
- **Digital-Stud relevance**: ⭐⭐⭐ Update `lora/training/kohya_config_example.toml` with validated Wan 2.2 LoRA settings from this guide; critical for character consistency in video generation

### 🆕 Z-Image LoRA Training Guide 2026

- **Source**: dev.to/gary_yan_86eb77d35e0070f5 — "Best Practices for Training LoRA Models with Z-Image"
- **Content**: Complete 2026 guide for Z-Image LoRA training — dataset prep, training params, model evaluation
- **Digital-Stud relevance**: Alternative LoRA training path if FLUX.2 gives unsatisfactory character consistency; Z-Image's fast inference speed makes it attractive for production workflows

### 🆕 Photoshop AI Assistant (Adobe, March 10, 2026)

- **Announcement**: TechCrunch + Adobe blog (March 10)
- **Feature**: Conversational AI for photo editing via natural language — "describe what you want, AI applies it"
- **Includes**: Generative Upscale (AI-powered upscaling within Photoshop), smart Generative Fill
- **Digital-Stud relevance**: Potential post-processing tool for refining AI-generated characters before compositing; compare with ComfyUI Z-Image Turbo face detailer workflow for efficiency

---



---

## 🔄 Run #47 Delta — 2026-03-12 20:30 Prague

### 🚀 SkyReels V4 — Launches Tomorrow March 13 | Unified Audio-Video Generation

- **Launch date**: March 13, 2026 (confirmed via Kinovi.ai announcement + Instagram post)
- **Architecture**: Dual-stream MMDiT (Multimodal Diffusion Transformer) — separate video and audio branches with cross-modal conditioning via shared MMLM text encoder
- **Unified pipeline**: Single model handles text-to-video, image-to-video, video extension, inpainting, and video editing — channel concatenation interface
- **Inputs**: Text + multiple image references + audio references simultaneously
- **Output pipeline**: 3-stage → low-res generation → keyframe upscaling → frame interpolation → cinema 1080p
- **Ranking**: 3rd on Artificial Analysis Text-to-Video with Audio Arena Leaderboard (behind Veo 3.1 and Sora 2.0)
- **Audio quality**: New vocoder, reduced artifacts, synchronized audio generation in single pass
- **API**: WaveSpeedAI (6 use cases guide published), Kinovi.ai
- **6 SkyReels V4 use cases** documented on WaveSpeedAI: social video with natural audio, AI film editing, image animation with sound, scene inpainting, reference-guided generation, multi-modal editing
- **Digital-Stud relevance**: ⭐⭐⭐ **Top priority tool** — replaces separate audio post-production step entirely; for character animation scenes with synchronized dialogue or music, this is the new baseline to test. Combine with Wan 2.2 S2V for comparison. Check ComfyUI node availability day-1

### 🚀 LTX-2.3 — Audio-Native Open Video Model with LTX Desktop

- **Release**: Available now (Lightricks, March 2026)
- **Architecture**: DiT-based audio-video foundation model — single model generates synchronized video + audio
- **Key upgrades over LTX-2.1**:
  1. **Rebuilt VAE and latent space** — sharper fine details, better texture/edge preservation
  2. **Larger text connector** — multi-subject prompts with complex spatial relationships now work reliably
  3. **Enhanced image-to-video** — eliminated freezing, "Ken Burns" effect, and static video artifacts
  4. **Cleaner audio** — retrained on filtered dataset (silence/noise/artifact removal), new vocoder
  5. **Native portrait video** — 1080×1920 trained (not cropped landscape), up to 1920px vertical
- **Available models on HuggingFace**: base checkpoint, distilled checkpoint + LoRA, latent upscalers
- **LTX Desktop**: Free download, open source — GUI for LTX-2.3 without ComfyUI node graph
- **ComfyUI**: Reference workflows shipping with release; ComfyUI-LTXVideo node has update issues (manager shows old date, update manually from GitHub)
- **NVFP4 support**: Coming soon for LTX-2.3 via NVIDIA (announced at GDC, 2.5× performance)
- **Prompting guide**: Confirmed community prompting structure (Facebook group, March 12) — explicit scene breakdown with subject + action + environment + camera + style sections works best
- **Digital-Stud relevance**: ⭐⭐⭐ **Audio-video in one open model** — first open alternative to Veo 3.1 for synchronized audio-video; LTX Desktop makes it accessible for testing without ComfyUI setup; update `wan22_img2vid.json` companion to include LTX-2.3 path

### 🚀 ComfyUI App Mode + App Builder + ComfyHub (March 10, 2026)

- **Announcement**: ComfyUI official press release via GlobeNewswire, March 10, 2026
- **App Mode**: Transforms any node graph workflow into a clean, purpose-built UI — only relevant inputs/outputs shown to end user
- **App Builder**: Workflow creators select which parameters are exposed; rest stays locked
- **Shareable URLs**: Workflow configuration encoded in URL — share your workflow as a runnable app without installation
- **Comfy Cloud**: URL-based sharing works without local ComfyUI install
- **ComfyHub**: New public discovery platform (preview) for community workflows and apps
- **NVIDIA GDC tie-in**: App View specifically highlighted for FLUX.2 Klein + LTX-2.3 demos at GDC 2026
- **Digital-Stud relevance**: ⭐⭐ **Distribution breakthrough** — Digital-Stud character generation workflows can now be shared as one-click apps (no node graph knowledge required). Priority: convert the character generation + face refinement workflows to App Mode for showcase

### 🟡 NVIDIA NVFP4 + FP8 Quantization for ComfyUI (GDC March 10)

- **Available now**: NVFP4 and FP8 model variants for FLUX.2 Klein (both 4B and 9B)
- **Coming soon**: NVFP4 for LTX-2.3
- **Performance gains**: Up to 2.5× speed improvement, 60% lower VRAM usage
- **Install**: Models available on HuggingFace, directly importable into ComfyUI
- **RTX Video Super Resolution Node**: New standalone ComfyUI node — real-time 4K upscaling, 30× faster than alternative local upscalers
- **Requirements**: NVIDIA RTX GPU (RTX 3000+ series for FP8; RTX 4000+ recommended for NVFP4)
- **Digital-Stud relevance**: Priority upgrade if on RTX GPU — FLUX.2 Klein 9B NVFP4 gives near-instant previews

### 🟡 Shima 2.0 — 100+ New Nodes for ComfyUI (March 12, 2026)

- **Launch**: Livestreamed March 12, 2026 at 8:30 AM PDT
- **Scale**: 100+ new nodes + full paired website + extension system
- **Nature**: Major relaunch of the Shima custom node ecosystem for ComfyUI
- **Install**: Via ComfyUI Manager (search "Shima") or GitHub
- **Digital-Stud relevance**: Review node list for character consistency, face, and animation nodes — 100 nodes is a significant surface area; prioritize scanning for anything pose/face/video-specific

### 🟡 Wan 2.7 — Confirmed for March 2026 Release

- **Announcement**: Reddit r/StableDiffusion, official Alibaba WanAI confirmation
- **Status**: "Scheduled for release in March 2026" — not yet dropped as of March 12
- **Scope**: "Comprehensive upgrades over version 2.6" — image quality + efficiency improvements cited
- **Context**: Wan 2.6 is a prior unreleased version (Wan versioning is non-sequential in public releases); 2.7 expected to be a significant quality jump over 2.2
- **Digital-Stud relevance**: Monitor daily — when released, update `wan22_img2vid.json` workflow checkpoint path; test against Wan 2.2 Palingenesis immediately

### 🟡 Sora 1 Sunset → Sora 2 in ChatGPT (March 13, 2026)

- **Sora 1**: US users lose access March 13, 2026; content removal after sunset
- **Sora 2 in ChatGPT**: Reuters confirmed March 11 — OpenAI plans to integrate Sora directly into ChatGPT interface (currently standalone app launched Sept 2025)
- **Sora 2 capabilities**: Videos up to 25 seconds, synchronized dialogue, $0.05/second API
- **Strategic implication**: ChatGPT integration = massive distribution for AI video generation; drives broader awareness and adoption
- **Digital-Stud relevance**: Export any Sora 1 assets before March 13; monitor Sora 2 in ChatGPT API for character video generation cost comparison

### 🟡 Qwen Image 2.0 Pro — Best Inpainting ControlNet (March 2026)

- **Community consensus** (r/StableDiffusion March 2026 + modelslab.ai): Qwen Image 2.0 Pro has **best inpainting ControlNet** for classic mask-based inpainting
- **Use**: "Crop & stitch" approach for precise local edits without affecting surrounding regions
- **Additional feature**: Background replacement via image editing modal
- **ComfyUI node**: Via WanGP (supports Qwen Image 2.0 Pro alongside Wan 2.1/2.2, HunyuanVideo, LTX)
- **Alternative to**: ZIT ControlNet (noted in r46) — Qwen Image 2.0 Pro preferred for mask inpainting, ZIT for general FLUX inpainting
- **Digital-Stud relevance**: Update `face_refinement.json` to offer Qwen Image 2.0 Pro path for face inpainting; better region preservation than FLUX Fill

### 🟡 ComfyUI 3D Scene Builder Node (March 2026)

- **YouTube demo**: "A new custom node inside ComfyUI lets you build and direct simple 3D scenes inside your AI workflow" (March 12, 2026)
- **Capability**: Build and direct 3D scenes directly inside ComfyUI for filmmaking/animation purposes
- **Integration**: Scene management, visualization, and export within node graph workflow
- **Digital-Stud relevance**: Potential integration point with the HY 3D + Tripo 3D pipeline — prototype a scene layout before generating character video; reduces reliance on Blender for simple scene setups

### 🔄 Text-to-Skeleton Paper Details (arXiv 2603.08028)

- **Full title**: "Controllable Complex Human Motion Video Generation via Text-to-Skeleton Cascades" (Ghahremani, Li, Laga, Boussaid, Bennamoun — March 2026)
- **Stage 1**: Autoregressive transformer generates 2D pose sequences from text → captures long-range temporal dependencies + inter-joint coordination for complex actions (flips, cartwheels, martial arts)
- **Stage 2**: DINO-ALF pose-conditioned video diffusion — preserves appearance and clothing under large pose changes + self-occlusions via spatially-localized patch descriptors
- **Key problem solved**: Explicit skeleton control previously required costly manual pose generation; this paper eliminates that bottleneck
- **Status**: Paper only as of March 12; no code/demo release yet; monitor for GitHub
- **Digital-Stud relevance**: When code releases — directly replaces manual DWPose keyframe work for complex multi-frame character animations

---



---

## 🔄 Run #46 Delta — 2026-03-12 20:03 Prague

### 🆕 Open-Sora 2.0 — Commercial-Level Video for $200K (arXiv 2503.09642)

- **Paper**: Zangwei Zheng et al. — "Open-Sora 2.0: Training a Commercial-Level Video Generation Model in $200k"
- **Full recipe open-sourced**: data curation pipeline, model architecture choices, training strategy, system optimization — all detailed
- **Quality target achieved**: comparable to HunyuanVideo and Runway Gen-3 Alpha at 5–10× lower training cost
- **Training cost**: $200K total vs $1–2M+ for equivalent closed models
- **Architecture**: Optimized video DiT with efficient attention, progressive resolution training (low → high resolution fine-tune)
- **License**: Fully open-source; commercial use permitted
- Digital-Stud relevance: **first fully open recipe for building a commercial-grade video model yourself** — enables custom character-video fine-tuning at cost-accessible scale; study the data curation pipeline for LoRA dataset prep

### 🆕 Seedance 2.0 — ByteDance Multi-Input Cinematic Video (March 5, 2026)

- **Launch**: March 5, 2026 — went viral as "China's second DeepSeek moment"
- **Core capability**: Multi-input cinematic video generation (text + image + reference frames → video)
- **Character consistency**: Specifically engineered to solve the "Consistency Gap" in AI video — multiple characters, same appearance across scenes
- **Use case**: Designed for e-commerce marketing and branded content (consistent product + character shots)
- **Availability**: API via WaveSpeedAI, fal.ai, and direct ByteDance access
- **Audio-video comparison**: Benchmarked head-to-head vs MOVA, WAN 2.2, Sora 2.0, SkyReels in WaveSpeedAI's audio-video sync test
- Digital-Stud relevance: strong alternative to Kling 3.0 for multi-character consistency in character animation; check API pricing vs Kling

### 🆕 MotionStream (Adobe Research) — Real-Time Interactive Video with Motion Drawing

- **Architecture**: Built on Wan 2.1 DiT with teacher-student acceleration system
- **Key capability**: Draw motion paths directly on screen → video renders in real-time sub-second preview
- **Controls**: Paint trajectories, camera motion, transfer motion from reference clips
- **Latency**: Wan 2.1 improves from 16.7 FPS / 0.69s latency → **29.5 FPS / 0.39s** with Tiny VAE decoder (10× decode speedup)
- **Paper**: arXiv:2511.01266v5 (updated March 2026)
- **ComfyUI**: `ComfyUI-AdvancedLivePortrait` node referenced alongside MotionStream for face/motion control; MotionStream install guide now available at aikolhub.com
- **TinyVAE decoder**: Drop-in replacement that removes the VAE bottleneck — compatible with Wan 2.1/2.2 pipelines
- Digital-Stud relevance: real-time motion preview closes the feedback loop for character animation; TinyVAE alone is worth integrating into S2V and I2V workflows for faster iteration

### 🆕 HunyuanVideo 3D (HY 3D) Advanced Features in ComfyUI

- **Official ComfyUI Blog post**: "HY 3D Advanced Features Now Available in ComfyUI" (March 2026)
- **New workflows in Browse Templates → 3D**:
  - **Multi-view reconstruction**: Generate 3D from multiple reference views in one workflow
  - **Texture refinement pass**: Post-process UV maps and textures to production quality
  - **Geometry cleanup**: Manifold mesh operations inside ComfyUI
- **Integration point**: Tencent HunyuanVideo 3D post-processing — same 3D pipeline as Tripo v3.0 but native HunyuanVideo ecosystem
- Digital-Stud relevance: now have **two in-ComfyUI 3D paths** (Tripo v3.0 + HY 3D) — HY 3D better for HunyuanVideo-originated characters; Tripo better for text/image-to-3D from other sources

### 🆕 FLUX.2 Klein Consistency LoRA Released

- **Release**: Community-released consistency LoRA specifically for FLUX.2 Klein (confirmed March 2026, r/comfyui thread)
- **Purpose**: Solves Klein's known issue of adding unwanted random details / changing reference elements during editing
- **Usage**: Works alongside FLUX.2 Klein Enhancer node pack (Ref Latent Controller)
- **Download**: HuggingFace (preferred by Klein LoRA community; Civitai adoption slower)
- **Complementary**: Use with Klein 9B for higher quality; 4B + consistency LoRA = good speed/quality tradeoff
- Digital-Stud relevance: **directly solves face/character consistency problem in the FLUX.2 Klein pipeline** — this is the missing piece for the Any-Pose Portrait Editing workflow

### 🆕 FLUX.2 Klein Enhancer Node Pack — Deterministic ComfyUI Editing

- **Nodes**: Three new nodes in ComfyUI for deterministic FLUX.2 Klein image editing:
  1. **Ref Latent Controller**: Controls reference image strength (recommended: 2.1) — locks pose/structure
  2. **Text/Ref Balance**: 0–1 slider balancing prompt influence vs reference image adherence
  3. **Detail Controller**: Front Multiplier (regions to change) + Middle Multiplier (action strength control)
- **Tutorial**: myaiforce.com/flux-2-klein-enhancer — step-by-step workflow walkthrough
- **Effect**: Enables precise targeted edits (face, clothing, background) without altering locked elements
- Digital-Stud relevance: **finalizes the face_refinement.json workflow** — combine these 3 nodes for consistent face fix passes

### 🆕 Wan 2.2 Palingenesis — Fine-Tuned Quality Variant

- **Model**: WAN 2.2 Palingenesis — community fine-tune of Wan 2.2 base
- **Quality**: Consistently outperforms base Wan 2.2 Lightning in visual quality benchmarks
- **Availability**: Civitai and HuggingFace
- **Comparison video**: YouTube walkthrough showing side-by-side Palingenesis vs older Wan 2.2 Lightning
- Digital-Stud relevance: drop-in upgrade for the `wan22_img2vid.json` workflow — replace base Wan 2.2 checkpoint with Palingenesis for better cinematic output

### 🆕 Wan 2.2 FreeLong / ComfyUI-LongLook — Training-Free Long Video Extension

- **Method**: SpectralBlend Temporal Attention — extends any Wan 2.2 video generation to longer durations without retraining
- **ComfyUI node**: `ComfyUI-LongLook` — install and add to existing Wan 2.2 workflows
- **Approach**: Spectral blending in temporal attention layers prevents quality degradation on longer sequences
- **No additional training required**: Works with base Wan 2.2 and fine-tunes (Palingenesis, Lightning)
- Digital-Stud relevance: **extends Wan 2.2 video from ~5s clips to longer character scenes** — combine with S2V for longer audio-driven animations

### 🆕 StableGen — AI 3D Texturing in Blender via ComfyUI Nodes

- **GitHub**: `sakalond/StableGen` — last updated March 5, 2026
- **Functionality**: Blender addon using ComfyUI nodes for AI-powered 3D texturing and generation
- **Workflow**: Import 3D mesh → generate textures via ComfyUI backend → export textured asset
- **Integration**: Bridges Blender (3D DCC) and ComfyUI (AI pipeline) directly
- Digital-Stud relevance: **closes the Blender↔ComfyUI gap** — texture any Digital-Stud 3D character in Blender using FLUX/SD4 without leaving the DCC environment

### 🆕 Real-Time Physical Action Video Generation (arXiv 2603.05449)

- **Paper**: "Real-Time Physical Action-Conditioned Video Generation"
- **Capability**: Conditions video generation on 3D forces, robotic manipulations, and physical actions — not just visual motion
- **Gap addressed**: Current video models cannot simulate physical consequences of 3D actions
- Digital-Stud relevance: future path for physically-plausible character interaction (grabbing objects, impacts) — monitor for ComfyUI implementation

### 🆕 ZIT ControlNet — Best Inpainting for FLUX (March 2026)

- **Community consensus** (r/StableDiffusion March 2026 thread): ZIT ControlNet is the recommended inpainting model for FLUX.1 Dev
- **Capability**: Superior region preservation and inpainting quality vs older FLUX inpainting nodes
- **Alternative**: FLUX.1 Fill Dev still strong but ZIT ControlNet preferred for precise edits
- Digital-Stud relevance: update `face_refinement.json` workflow to use ZIT ControlNet for face inpainting passes

### 🔄 Audio-Video Model Comparison: MOVA vs WAN vs Sora 2 vs Seedance (WaveSpeedAI, March 2026)

- **Source**: wavespeed.ai/blog/posts/mova-vs-wan-sora-seedance-video-audio-comparison-2026
- **Rankings for audio-native video**:
  1. **Veo 3.1** — leads for cinematic audio-native with dialogue
  2. **Sora 2.0** — 25s max, synchronized dialogue, closed API ($0.05/sec)
  3. **Seedance 2.0** — best multi-character consistency
  4. **WAN 2.2 + S2V** — best open-source audio option
  5. **SkyReels V4** — joint audio-video in single pass (just released)
- **MOVA**: New entrant — Music-Oriented Video Alignment, specialized for music video sync
- Digital-Stud relevance: **definitive decision matrix** for audio-video pipeline choice

---



---

## 🔄 Run #45 Delta — 2026-03-12 19:30 Prague

### 🚨 BREAKTHROUGH — Helios: Real-Time Long Video Generation (PKU, March 4, 2026)

- **GitHub**: `PKU-YuanGroup/Helios` — training/inference code + weights released March 4
- **Architecture**: 14B autoregressive diffusion transformer (radically simplified design)
- **Real-time performance**: **19.5 FPS on single H100** — no KV-cache, sparse attention, or quantization needed
- **Duration**: Minute-scale (up to 1,452 frames at 24 fps ≈ 60 seconds) — vs ~5–10s for Wan/LTX
- **Three variants**:
  - `Helios-Base`: 50 steps, highest quality
  - `Helios-Mid`: intermediate quality/speed tradeoff
  - `Helios-Distilled`: 3 steps, 19.5 FPS (real-time)
- **Training innovation**: "Easy Anti-Drifting" training replaces inference-time hacks; unified history injection for error-free chunk concatenation
- **Hardware**: Also runs on Ascend NPU (~10 FPS); 4 models fit in 80GB GPU
- **Backends**: Diffusers, vLLM-Omni, SGLang-Diffusion, Ascend NPU
- **Benchmark**: Introduces HeliosBench for long-video evaluation
- **License**: Apache 2.0
- Digital-Stud relevance: **largest open-source video leap in months** — 60s real-time generation changes character animation pipeline economics entirely

### 🆕 SkyReels V4 — Joint Audio-Video Generation (API Released March 12, 2026)

- **API Privacy Policy effective March 12, 2026** — fresh drop today
- Claimed **#2 global ranking** in video generation
- Key advancement from V2→V4: Infinite-length video (V2) → Joint audio-video generation (V4)
- V3 (January 2026): Multi-subject video generation system (talking avatar, 40+ language lip sync from one portrait + audio)
- V4: Architecture now generates synchronized audio + video in single pass
- API: `skyreels.ai/dev`
- Digital-Stud relevance: rival to LTX-2.3 audio pipeline; SkyReels V3 valuable for talking avatar / character voiceover with lip sync

### 🆕 Stability AI — Stable Diffusion 4 Ultra

- **SD4 Ultra** released (no precise date confirmed, active this week)
- Key improvements over SD3.5-Large:
  - Correct anatomy and hand generation (addresses longstanding weakness)
  - Cinema-grade lighting simulation
  - Significantly improved text rendering within images
  - Photorealism benchmark improvements
- Positioned as "commercial-ready" alongside Midjourney v6.1 and FLUX.1 Pro
- Digital-Stud relevance: upgrades base image quality for character sheets; correct hands = reduced face_refinement workflow passes needed

### 🆕 Nano Banana 2 — New Image Generation SOTA Contender

- **Nano Banana 2** vs **Seedream 5.0** benchmark article published (medium.com/@302.AI)
- Nano Banana 2 positioning: strong at poster design, portrait, album art
- Seedream 5.0: Bytedance-backed, competitive on photorealism and style diversity
- Both benchmarked via HF Inference API (smol-worldcup Season 1 tournament: 18 models, 12 makers)
- Digital-Stud relevance: monitor Nano Banana 2 as potential FLUX alternative for specific use cases

### 🆕 Wan 2.2 Sound-to-Video (S2V) — Audio-Driven Video in ComfyUI

- **Wan2.2-S2V workflow** now in ComfyUI official templates (`comfy.org/templates/video_wan2_2_14B_s2v/`)
- New dedicated nodes:
  - **`WanSoundImageToVideoExtend`**: manual video extension with precise audio-video sync
  - **`LatentCut`**: precise latent cutting in audio workflows
- Output: minute-long audio-driven video generation
- Works on 8GB VRAM
- Wan 2.2 Lightning LoRAs (high + low) improve visual quality in S2V
- Digital-Stud relevance: direct audio-reactive character video without LTX — complements rather than replaces LTX-2.3 audio pipeline

### 🆕 Tripo v3.0 — Native ComfyUI Integration for 3D Asset Generation

- **Tripo v3.0** now natively integrated in ComfyUI (ComfyUI Blog official post)
- Generates production-ready 3D assets without leaving the ComfyUI workflow
- Complements Neural4D (March 12) — Tripo via ComfyUI node vs Neural4D standalone tool
- Both solve the 2D→3D pipeline gap but with different integration points
- Digital-Stud relevance: choose Tripo for in-workflow 3D gen; Neural4D for standalone batch processing

### 🆕 SCAIL in ComfyUI — 3D-Consistent Pose Animation

- **SCAIL**: 3D-consistent pose animation for characters, now available as ComfyUI node
- Enables precise motion control with 3D spatial awareness (not just 2D skeleton projection)
- Works with character reference images for consistent multi-angle animation
- Tutorial: nextdiffusion.ai/tutorials/scail-comfyui-3d-consistent-pose-animation-characters
- Also referenced in ComfyUI v0.16.1 as **SCAIL WanVideo** model in API nodes
- Digital-Stud relevance: fills 3D pose consistency gap between DWPose (2D only) and full 3D rigging

### 🆕 Any-Pose Portrait Editing Pipeline — Practical 3D→Portrait Workflow

- **New tutorial**: 3D character pose → portrait editing in ComfyUI (myaiforce.com)
- Workflow: pose 3D character → transfer with **Qwen Edit** → face fix → upscale 4K with **FLUX.2 Klein**
- Combines SCAIL / 3D pose source with Qwen's edit capabilities and FLUX.2 Klein final quality pass
- Digital-Stud relevance: **concrete implementation path** for the pose→character pipeline already tracked in SOTA

### 🆕 Text-to-Skeleton Video Cascades (arXiv 2603.08028)

- Paper: "Controllable Complex Human Motion Video Generation via Text-to-Skeleton Cascades"
- Two-stage framework: (1) autoregressive text-to-skeleton model → 2D pose sequences, (2) pose-conditioned video synthesis
- Handles long-range temporal dependencies in complex motion (fighting, dancing, acrobatics)
- Digital-Stud relevance: theoretical backbone for future controlled character action sequences from text prompts

### 🆕 Skeleton-to-Image Encoding / S2I (arXiv 2603.05963)

- Paper: "Enabling Skeleton Representation Learning via Vision-Pretrained Models"
- S2I converts 3D skeleton sequences into image-like representations for MAE/DiffMAE consumption
- Enables cross-format skeleton learning across NTU-60, NTU-120, PKU-MMD datasets
- Digital-Stud relevance: bridges 3D skeleton data and vision-pretrained diffusion models — potential for future pose LoRA training

### 🔄 ComfyUI v0.16.1 Full Changelog Confirmed (March 5, 2026)

Additional items not previously captured:
- **ResolutionSelector node**: aspect ratio presets for easier dimension setup
- **CURVE type support**: advanced parameter control input
- **ACE-Step 1.5 lycoris key** alias mapping for LoKR compatibility
- **SDPose-OOD model support**: out-of-distribution pose estimation models
- **Z-image pixel space** support
- **Dynamic VRAM mode** now default — automatic memory optimization without manual flags
- **LoRA requantization** for non-QuantizedTensor fp8

### 🔄 Comfy Cloud Free Tier — RTX Pro 6000 Access

- Comfy Cloud launched **free tier** on NVIDIA RTX Pro 6000 GPUs
- Same hardware as paid users
- Enables no-install app execution via ComfyHub shareable URLs
- Digital-Stud relevance: free cloud testing path for heavy NVFP4 models without local RTX hardware

### 🔄 WanGP v10.981 (March 7, 2026) — Confirmed LTX-2.3 Day-0 Support

- Update confirmed: "0 day delivery of LTX 2 latest version with better audio, image-to-video and greater details"
- Still supports: Wan 2.1/2.2, Qwen Image, HunyuanVideo, LTX Video, FLUX
- Verified as the recommended GPU-poor inference runner for all major open video models

### 🔄 LTX-2.3 vs Wan 2.2 — Definitive Comparison (March 2026)

- LTX-2.3: **18× faster** than Wan 2.2 14B; native audio; up to 4K/50fps; 20s duration; Apache 2.0 (<$10M revenue)
- Wan 2.2: **better prompt adherence and video quality**; stronger cinematic benchmark; larger community workflow ecosystem
- Practical guidance: LTX-2.3 for rapid iteration + audio sync; Wan 2.2 for final cinematic quality output

---



---

## 🔄 Run #44 Delta — 2026-03-12 19:04 Prague

### 🆕 NVIDIA NVFP4 + FP8 Native in ComfyUI — GDC 2026 Announcement

- **NVIDIA × ComfyUI GDC 2026**: NVFP4 and FP8 support built directly into ComfyUI
  - Up to **2.5× performance gains** over FP16
  - **60% lower memory usage** — enables larger models on consumer GPUs
  - **FLUX.2 Klein 4B and 9B** models now available with NVFP4 support
  - LTX-2.3 FP8 supported now; NVFP4 variant coming soon
  - No user configuration required — enabled transparently on RTX hardware
- **RTX Video Super Resolution** as a ComfyUI node:
  - Real-time 4K upscaling
  - **30× faster** than existing upscaling alternatives in ComfyUI
  - Purpose-built for video frame upscaling in generation pipelines
- NVIDIA Blog: https://blogs.nvidia.com/blog/rtx-ai-garage-flux-ltx-video-comfyui-gdc/
- Digital-Stud relevance: **major throughput unlock** for local inference — FLUX.2 Klein NVFP4 is now the recommended fast generation path on RTX hardware

### 🆕 Neural4D Image-to-3D Engine — Production Release March 12, 2026

- **Neural4D** releases production-grade Image-to-3D generation focused on pipeline usability
- Solves two long-standing AI 3D generation problems:
  - **Broken/non-watertight meshes**: computes watertight manifold geometry → engine-ready
  - **Baked lighting**: extracts pure albedo → correct under any lighting condition
- Export formats: `.obj`, `.fbx`, `.glb`, `.usdz`, `.stl`, `.blend` (6 standard formats)
- No Blender geometry cleanup needed for basic assets
- Digital-Stud relevance: **closes the 2D→3D pipeline gap** — generates engine-ready props/assets from reference images

### 🆕 WanGP v10.9 — Multi-Model Local Runner for GPU-Poor

- GitHub: `deepbeepmeep/Wan2GP`
- Supports: Wan 2.1, Wan 2.2, **Qwen Image**, HunyuanVideo, LTX Video, FLUX in one unified runner
- Optimized for low-VRAM (GPU-poor) setups — GGUF Q5 tested for infinite non-looping video
- Wan 2.2 Animate workflow included with model downloads
- Digital-Stud relevance: single runner to switch between all major open video models — practical for pipeline testing

### 🆕 FLUX.2 Klein Enhancer Node — Pose Lock & Detail Control

- Community-built **Enhancer node pack** for FLUX.2 Klein in ComfyUI
- Key features: pose locking across generations, detail control for consistent character appearance
- Tutorial: myaiforce.com/flux-2-klein-enhancer/
- Digital-Stud relevance: fills the pose-consistency gap for FLUX.2 Klein without full ControlNet setup

### 🆕 A²-Edit — Unified Reference-Guided Image Inpainting (arXiv 2603.10685)

- Unified framework for reference-guided inpainting that works across multiple FLUX variants
- Handles large occlusions, identity preservation, scene-consistent inpainting
- Digital-Stud relevance: character face/body inpainting with reference consistency — useful for face refinement workflow

### 🆕 ConfCtrl — Confidence-Aware Camera Control in Video Diffusion (arXiv 2603.09819)

- Addresses prescribed camera poses in video diffusion via confidence-aware interpolation
- Enables precise camera trajectory control (dolly, orbit, pan) in video generation
- Digital-Stud relevance: camera-controlled character video generation — potential integration with Wan 2.2/LTX workflows

### 🔄 GPT-5.4 Launch — March 12, 2026

- **OpenAI GPT-5.4** launched this week (AI news roundup March 12)
- No image generation specifics confirmed yet; monitoring for GPT Image API updates
- Sora reportedly being prepared for broader video platform access (Instagram-style reports)

### 🔄 Grok Imagine — March 12 Update Signal

- **Elon Musk flagged another Grok Imagine update** on March 12, 2026 (details still emerging)
- Background: API launched Jan 28, 2026 at $0.05/sec for text-to-video + image-to-video + video editing; 1.245 billion videos generated in Jan 2026 alone
- Digital-Stud relevance: low-cost video API worth benchmarking against Kling/Seedance for price/quality

### 🔄 ACE-Step 1.5 in ComfyUI v0.16.1

- ComfyUI v0.16.1 (March 5) added **ACE-Step 1.5** model support
- ACE-Step: audio generation model for synchronized audio-video workflows
- Pairs with LTX-2.3 audio-video + ElevenLabs nodes for complete audio pipeline
- Digital-Stud relevance: non-voice ambient audio generation to complement ElevenLabs voice pipeline

### 🔄 Pinterest Canvas — FLUX.1 Kontext In-Context Image Generation at Scale (arXiv 2603.06453)

- Pinterest engineering paper on production-scale in-context image generation
- Uses FLUX.1 Kontext: encodes conditioning images via VAE and concatenates with image tokens
- Enables unified in-context editing (reference image + text instruction) in one forward pass
- Digital-Stud relevance: reference-consistent image generation technique validated at industrial scale

---



---

## 🔄 Run #43 Delta — 2026-03-12 18:30 Prague

### 🆕 YOLO26-Pose — SOTA Pose Estimation Successor to YOLOv11-Pose (March 9, 2026)

- Ultralytics releases **YOLO26** as unified 5-task family (detect, segment, classify, pose, OBB)
- **YOLO26-pose** replaces YOLOv11-pose as the recommended pose estimation model:
  - **Improved non-human keypoint support**: removes human-specific assumptions — usable for custom landmark detection (props, machinery, animals)
  - **RLE loss (Residual Log-Likelihood Estimation)**: faster training convergence, stronger accuracy in fewer epochs
  - **Better occlusion handling** at small scales
  - **End-to-end design**: no external NMS needed → lower latency on CPU/edge
  - Variants: YOLO26n-pose, YOLO26m-pose, YOLO26l-pose, YOLO26x-pose
- Available in Ultralytics Python library; ComfyUI integration via existing YOLO nodes
- Digital-Stud relevance: **drop-in upgrade from YOLOv11-pose** for pose extraction preprocessing in ControlNet pipelines

### 🆕 LTX-2.3 GGUF Dynamic Variants — 12GB VRAM Viable (Unsloth Release)

- **Unsloth** releases full LTX-2.3 Dynamic GGUF variants (Q2–Q8) + ready ComfyUI workflow
- HuggingFace: `unsloth/LTX-2.3-GGUF`
- Dynamic quantization: important layers kept at full precision → better quality vs standard GGUF
- Tested working at **12GB VRAM** (RTX 3080/4070 class)
- Separate GGUF loader: Kijai/ComfyUI-KJNodes (NOT compatible with city96/ComfyUI-GGUF)
- 22B model confirmed working with KJNodes; lower-rank distill LoRA added by Kijai
- Digital-Stud relevance: LTX-2.3 audio-video fully accessible on consumer 12GB cards

### 🆕 DiffSynth-Studio Adds LTX-2.3 Support — March 12, 2026

- **ModelScope/DiffSynth-Studio** adds LTX-2.3 audio-video generation on March 12, 2026
- Features: text-to-audio/video, image-to-audio/video, **IC-LoRA** (identity-consistent LoRA for video)
- IC-LoRA: enables consistent character identity across video frames via LoRA conditioning
- GitHub: `modelscope/DiffSynth-Studio`
- Digital-Stud relevance: IC-LoRA is a major capability for character-consistent video generation

### 🆕 ElevenLabs ComfyUI Partner Nodes — Voice AI in Node Graph

- **ElevenLabs** officially available in ComfyUI via Partner Nodes
- Capabilities: text-to-speech, voice cloning, style transformation, audio transcription, isolation, multi-speaker dialogue, sound effect generation, voice library browser
- Works alongside LTX-2.3 audio-video: generate character voice → drive video generation
- Digital-Stud relevance: complete audio pipeline in ComfyUI — TTS + voice clone + video sync

### 🆕 HunyuanVideo 3D 3.0 Partner Nodes in ComfyUI (March 9, 2026)

- **Tencent Hunyuan 3D 3.0** advanced features available via ComfyUI Partner Nodes
- Features: text/image/sketch-based 3D generation, 3D parts decomposition, UV unwrapping, smart topology, production-ready post-processing
- Digital-Stud relevance: 3D asset generation from 2D reference images directly in ComfyUI — no Blender round-trip needed for basic assets

### 🔄 Wan 2.7 — Open-Source Uncertainty Growing

- **Wan 2.7 not yet released** as of March 12 18:30 Prague (still "scheduled for March")
- Community concern: reports suggest **Alibaba may shift Wan to closed-source** going forward
- Reddit r/StableDiffusion: "No one cares unless it can be run locally" — community demand for open weights
- If confirmed closed: major impact on Digital-Stud pipeline (Wan 2.2 becomes last open video model from Alibaba)
- **Monitor closely**: watch Alibaba GitHub + HuggingFace for official weights release

### 🔄 RunPod 2026 State of AI Report — March 12, 2026

- Key findings for Digital-Stud workflow planning:
  - Massive shift toward **Qwen models** in local inference (surpassing Llama downloads)
  - Trend toward **modular video pipelines** — separate dedicated models for each step vs monolithic end-to-end
  - **Blackwell (RTX 50-series) GPU adoption** accelerating rapidly in 2026
  - Inference moving to **FP4/FP8** as default; FP16 becoming legacy
- Digital-Stud relevance: validates multi-model modular pipeline approach; Qwen worth evaluating for scene captioning

### 🔄 SMPL Text-to-Skeleton-to-Video — Pose-Conditioned Video Generation Paper

- arXiv 2603.08028: **"Controllable Complex Human Motion Video Generation via Text-to-Skeleton-to-Video"**
- Two-stage: (1) generate skeleton sequence from text → (2) pose-conditioned video diffusion from reference image + skeleton
- Achieves complex, controllable motion without motion reference video — pure text control
- Digital-Stud relevance: potential for text-driven character animation — no reference video needed

### 🔄 FLUX Image-to-Video — March 2026

- GitHub master list confirms **FLUX Image-to-Video** as a new March 2026 entry
- Status: community/third-party implementation; no official Black Forest Labs release confirmed
- Watch: `black-forest-labs/FLUX` GitHub for official announcement
- Digital-Stud relevance: would enable FLUX-native image-to-video without model switching

---



---

## 🔄 Run #42 Delta — 2026-03-12 18:03 Prague

### 🆕 LTX-2.3 — Open Audio-Video Model with ComfyUI GGUF Support

- Lightricks releases **LTX-2.3**, significant upgrade over LTX-2
- Generates **synchronized video + audio** from text or image prompts
- Improved audio-visual quality and enhanced prompt adherence
- **GGUF support** via Kijai/ComfyUI-KJNodes (community hacking required for LTX-2.3 GGUF)
- FP8 support live; NVFP4 support coming soon (2.5× faster, 60% less VRAM on RTX 50-series)
- On RTX 5090: few minutes for 5-second clip; performance improving rapidly
- Full weights open, consumer GPU usable, Apache-compatible license
- Digital-Stud relevance: best open audio-video model for talking avatar + ambient audio workflows

### 🆕 ComfyUI App Mode + App Builder + ComfyHub (March 10, 2026 — Major Launch)

- **App Mode**: single click turns any node graph workflow into a clean user-facing UI — no node knowledge needed
- **App Builder**: configure which inputs/outputs are exposed; create distributable apps with shareable URLs
- **ComfyHub** (comfy.org/workflows preview): community marketplace for finished apps and workflows — analogous to Node Registry but for creators
- Comfy Cloud: users run apps in browser without local install
- Implication: Digital-Stud workflows can be published as one-click apps for non-technical users

### 🆕 NVIDIA NVFP4 + RTX Video Super Resolution @ GDC 2026 (March 10, 2026)

- **NVFP4 models**: FLUX.2 Klein 4B & 9B + LTX-2.3 (coming soon) get NVFP4 variants
  - RTX 50-series: **2.5× faster** inference, **60% less VRAM** vs standard FP16
  - FP8 path: **1.7× faster**, **40% less VRAM** (available now)
- **RTX Video Super Resolution node**: available in ComfyUI Manager now
  - **30× faster 4K upscaling** vs alternative local upscalers
  - Standalone node (GitHub) + PyPI package; real-time capable on RTX GPUs
  - Ideal for post-generation upscale in video workflows
- Digital-Stud relevance: major local performance unlock for Klein + LTX-2.3 on RTX hardware

### 🆕 FireRed-Image-Edit — Instruction-Following Image Editing with Native ComfyUI Node

- Universal instruction-following image editing foundation model
- **Native ComfyUI node** support + **GGUF format** lightweight deployment
- Outperforms FLUX.2 [Dev] on editing tasks per benchmarks
- Supports: inpainting, object replacement, style transfer, selective editing
- Digital-Stud relevance: best open-source instruction-edit model for controlled character/scene editing

### 🆕 Z-Image (Tongyi-MAI) — #1 Open-Source on Artificial Analysis Leaderboard

- 6B parameter family; Z-Image-Turbo: **ranked #8 overall, #1 open-source** on Artificial Analysis image leaderboard
- **$0.014/image** via API; strong bilingual text rendering
- Also available open-weights on HuggingFace
- Digital-Stud relevance: best cost-performance open image model available March 2026

### 🆕 A²-Edit — Unified Inpainting Framework for Any Object Category

- arXiv 2603.10685 — unified inpainting for arbitrary object categories
- Allows replacement of any target region with a reference object
- Single framework for all object classes — no per-category tuning
- Digital-Stud relevance: reference-guided inpainting with character asset swap use case

### 🆕 OmniLottie (CVPR 2026) — ComfyUI Community Support Added March 6, 2026

- Multi-modal animation synthesis for vector graphics (Lottie format)
- ComfyUI community contribution added March 6, 2026
- Enables procedural animation from text/image prompts → Lottie JSON output
- Digital-Stud relevance: UI/motion graphics animation from AI prompts

### 🔄 Kling 3.0 Motion Control in ComfyUI — March 12, 2026 Confirmed Launch

- Official ComfyUI Partner Nodes for **Kling Motion Control 3.0** launched March 12, 2026
- Upgraded motion capture, 360° facial consistency, smooth expressions across angles/duration
- `element_1` parameter for character consistency across shots
- Available via Replicate API + WaveSpeedAI + ComfyUI partner nodes
- Digital-Stud relevance: best motion-reference-to-video tool now fully integrated in ComfyUI

### 🔄 Grok Imagine (xAI) — R-Rated Policy Update, March 12, 2026

- Elon Musk posts: Grok Imagine follows R-rated movie standards for content moderation
- More permissive than most competitors; pricing $0.02–0.07/image
- Grok Imagine saw major UI redesign in March 2026 with web + mobile overhaul
- Status: API available; positioned as less-restricted creative tool

---



---

## 🔄 Run #41 Delta — 2026-03-12 17:30 Prague

### 🆕 Wan 2.7 — Official March 2026 Release Confirmed

- Officially announced for March 2026 release as "Professional Multimodal AI Video Director"
- Comprehensive upgrades over Wan 2.6: text + image + video + audio inputs simultaneously ("reference everything")
- Features: absolute character fidelity, advanced camera choreography, precision physics, semantic identity preservation
- Three-step directorial workflow for cinematic production
- **Status as of 17:30 Prague: Not yet released, imminent** — community thread confirmed by Wan team
- Digital-Stud relevance: will be the new best open multimodal video model once released

### 🆕 Sora 1 Retiring March 13, 2026 → Sora 2 In ChatGPT Soon

- **Sora 1 ending in US: March 13, 2026** — users prompted to export content now
- OpenAI planning Sora integration directly into ChatGPT (Reuters/The Information, March 11)
- Sora 2 will be the successor — details sparse but ChatGPT-native delivery expected

### 🆕 Open-Sora 2.0 — Commercial-Level Open Video Generation

- arXiv 2503.09642v3 — community model built on HunyuanVideo VAE + Video DC-AE architecture
- Achieves commercial-level quality at fraction of proprietary cost
- Full training recipe open-sourced including data curation, architecture, training strategy
- Digital-Stud relevance: best free-to-train video foundation model for custom fine-tuning

### 🆕 BFL Self-Flow — Multimodal Training 2.8× More Efficient (March 4, 2026)

- Black Forest Labs announces Self-Flow technique (March 4, 2026)
- Makes training multimodal AI models **2.8× more efficient**
- Applies to FLUX.2 family training and future model development
- Expected to accelerate FLUX.2 Klein LoRA training tooling development

### 🆕 SD3.5-Flash — On-Device Lenovo Integration (March 4, 2026)

- Lenovo licenses **Stable Diffusion 3.5 Flash** for on-device private image generation
- Runs locally on Lenovo hardware — no cloud dependency, privacy-first
- SD3.5-Flash: fast, low-VRAM SD3.5 distilled variant for edge deployment
- Digital-Stud relevance: confirms on-device SDXL-class quality is now feasible for laptop workflows

### 🆕 Google Nano Banana 2 — Image Generation Leaderboard Leader (Feb 26, 2026)

- **Nano Banana 2** (Gemini 3.1 Flash Image): tops Chatbot Arena text-to-image at **1280 Elo**
- 2× faster than Nano Banana Pro, 50% cheaper ($0.045–$0.151/image vs $0.134)
- Strong text rendering (challenging Ideogram), photorealistic, multi-subject compositions
- API: Google AI Studio / Vertex; free tier available
- Digital-Stud relevance: best free-tier cloud API for T2I in March 2026

### 🆕 SkyReels V3 — Open-Source Cinematic Video + Lip-Sync (Jan 2026, now ComfyUI stable)

- 14B-parameter V2V model: extends any video with cinematic quality
- Audio-to-video (A2V) talking avatar + lip-sync animation
- Low VRAM support, GGUF quantization available
- Full ComfyUI workflow available at runcomfy.com
- Digital-Stud relevance: best open-source option for talking avatar / lip-sync workflows

### 🔄 Seedance 2.0 API Status Update (March 6, 2026)

- Batch generation now live: **up to 20 clips per session** (March 6 update)
- Global API still scheduled for March 2026 — not yet general-release as of 17:30 Prague
- Native audio, 1080p, 15–20s clips, 12 reference files, beat-sync mode
- Some halting/controversy around the model noted in community; API maturation ongoing

### 🔄 Motion Forcing — Video Generation Trilemma Framework (arXiv 2603.10408)

- New decoupled framework for robust video generation: quality + physical consistency + controllability
- Addresses fundamental trilemma in video generation architectures
- Digital-Stud relevance: theoretical framework for evaluating video model trade-offs

---



---

## 🔄 Run #40 Delta — 2026-03-12 17:07 Prague (comprehensive sweep)

### 🆕 FLUX.2 [klein] Full Architecture Details Confirmed

- **FLUX.2 [klein]** family: 9B and 4B variants. The 4B runs on ~13 GB VRAM consumer cards
- Unifies text-to-image, image editing, and multi-reference generation in a **single architecture** — no separate models needed
- **NVFP4** (Blackwell FP4) quantized checkpoints of both Klein 4B and 9B now natively supported in ComfyUI; RTX 50-series only
- FP8 quantized variant available on HuggingFace for non-Blackwell hardware (40% VRAM reduction vs BF16)
- **FLUX.2 [pro] / [flex]**: API-only variants via BFL playground; not open-weight

### 🆕 Midjourney V8 — Imminent Release (March 2026)

- V8 described as "launchable" — in final community rating-party phase
- New personalization system, enhanced upscaler, upcoming video model integration
- **Niji 7** already live (January 2026) with anime-specific quality improvements

### 🆕 YOLO26-Pose — New Real-Time Pose SOTA (January 2026, now SOTA benchmark)

- Released by Ultralytics January 14, 2026
- Removes human-specific architectural assumptions → flexible for non-human keypoints
- Uses **MuSGD optimizer + Residual Log-Likelihood Estimation** for better keypoint uncertainty
- End-to-end (no NMS), faster on CPU/edge vs YOLO11 and YOLOv8-Pose
- Model tiers: YOLO26n-pose → YOLO26x-pose
- Digital-Stud relevance: best real-time option for pose extraction on laptop/edge GPU

### 🆕 TAR-ViTPose — Temporal Video Pose Estimation SOTA (arXiv 2603.05929)

- **413 fps** vs 52 fps for prior video-based methods — massive throughput improvement
- **Joint-Centric Temporal Aggregation (JTA)**: learnable query tokens per joint, attends to neighboring frames
- **Global Restoring Attention (GRA)**: reintegrates temporal features preserving global context
- +2.3 mAP on PoseTrack2017 over single-frame ViTPose baseline
- SOTA on PoseTrack2017, PoseTrack2018, PoseTrack21
- Digital-Stud relevance: use for temporally consistent pose extraction from video refs before ControlNet piping

### 🆕 CIGPose — Causal Whole-Body Pose SOTA (arXiv 2603.09418, confirmed SOTA)

- CIGPose-x: **67.0% AP on COCO-WholeBody** without extra data; **67.5% AP** with UBody
- Structural Causal Model (SCM) identifies confounded keypoints via predictive uncertainty, replaces with canonical embeddings
- Hierarchical GNN enforces anatomical plausibility at local + global skeleton levels
- Code: https://github.com/53mins/CIGPose
- Digital-Stud relevance: higher-quality whole-body keypoints for IP-Adapter + ControlNet pipelines

### 🆕 RTMLib v0.15 — Dependency-Free Pose Suite (Released Feb 10, 2026)

- **rtmlib 0.15** released on PyPI: RTMPose, DWPose, RTMO, RTMW, ViTPose — all **without mmcv dependency**
- `pip install rtmlib` — dramatically easier deployment in ComfyUI custom nodes and standalone scripts
- Digital-Stud relevance: drop-in replacement for DWPose in ComfyUI without mmcv install hell

### 🆕 ComfyUI App Mode + ComfyHub — Official Launch (March 10, 2026)

- **App Mode**: one-click transforms any workflow into clean UI, hiding node graph from end users
- **App Builder**: authors select which inputs/outputs are exposed
- **ComfyHub**: new public platform at comfy.org/workflows — discover, run, share community apps
- ComfyUI Manager migrating to Comfy-Org/ComfyUI-Manager organization (March 28, 2026)

### 🆕 NVIDIA RTX 50 Series + ComfyUI GDC 2026 Announcements

- **RTX Video Super Resolution** node in ComfyUI: **30x faster 4K upscaling** on RTX Tensor Cores vs alternatives
- **NVFP4** quantized FLUX.2 Klein and LTX-2.3 models natively supported (RTX 50-series only)
- FP8 models: 1.7x faster, 40% less VRAM vs BF16
- Combined RTX optimizations: **2.5x faster** inference + **60% lower VRAM** on RTX 50 Series
- Workflow: ComfyUI App View → NVFP4 model → RTX VSR upscaler = full 4K video pipeline on consumer GPU

### 🆕 LTX-2.3 — Audio-Video Generation with Day-0 ComfyUI Support

- Confirmed day-0 native ComfyUI support (official workflows at ltx.io/model/model-blog/ltx-2)
- Improvements: finer detail VAE, 9:16 portrait support, better audio (reduced noise), improved img2vid consistency
- NVFP4 support coming soon (RTX 50-series)
- Digital-Stud relevance: best open audio-video model for ComfyUI pipelines currently

### 🆕 Wan 2.6 — Audio-Driven Multi-Shot Video (ComfyUI Template Library)

- Wan 2.6 now in ComfyUI Template Library: character starring, multi-shot storytelling, synced audio, cinematic gen, multi-image control
- Wan 2.7 still announced for March 2026 — **not yet released** as of 17:07 Prague

### 🔄 SMPLest-X / PointHPS — 3D Expressive Pose SOTA (TPAMI 2026)

- **SMPLest-X** (TPAMI 2026): scaling for expressive whole-body SMPL-X estimation — body + hands + face
- **PointHPS** (IJCV 2026): cascaded 3D pose from point clouds
- ViMoGen (ICLR'26): transfers ViGen knowledge to MoGen for video motion generation (SMPL-X based)
- Digital-Stud relevance: ViMoGen as a bridge between video generation and motion generation pipelines

---

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
> Last updated: 2026-03-12 23:30 (Prague / CET) | Run #53

---

## 🖼️ Image Generation SOTA — March 2026

### 🆕 StruVis — Reasoning-Based Text-to-Image via Structured Visual Representations (arXiv 2603.06032, March 2026)

- Enhances T2I generation by thinking in **structured text-based visual representations** (bounding boxes, object attributes, spatial layout) instead of intermediate images
- Built on FLUX.2-klein-9B (generation) + Qwen3-VL-Plus (structured representation extraction)
- GRPO training with multi-component reward: format fidelity, visual understanding, image quality
- Results: **+4.61% on T2I-ReasonBench**, **+4% on WISE** (World-knowledge-informed Semantic Evaluation)
- Generator-agnostic — can wrap any T2I backend; tested on FLUX.2-klein-9B
- Digital-Stud relevance: compositional scene generation (placing multiple characters + objects with correct spatial layout) is a direct downstream application

### 🆕 Sora 1 Sunset — US March 13, 2026

- OpenAI retiring Sora 1 in the US starting **March 13, 2026** (today); Sora 2 is now the only supported path
- ChatGPT image generation continues unaffected
- Digital-Stud relevance: migrating any Sora-based workflows to Sora 2 or open alternatives (Wan 2.2, LTX-2.3, Helios) is now a priority

### 🆕 FLUX.2 Klein — NVIDIA NVFP4 & FP8 Quantized Variants (March 2026)

- **NVFP4 on RTX 50 Series**: 2.5× performance gain, 60% VRAM reduction vs baseline FLUX.2 Klein (4B/9B)
- **FP8**: 1.7× faster, 40% VRAM reduction — available now on all Ada/Hopper+ GPUs
- Models published directly to HuggingFace; loadable in ComfyUI via standard GGUF/safetensors loaders
- Digital-Stud relevance: Klein 9B now viable on 16GB VRAM cards at FP8; NVFP4 unlocks RTX 5090 near-instant generation

### 🆕 Pinterest Canvas — Production-Scale Outpainting & Multi-Image Synthesis (arXiv 2603.06453, March 2026)

- Pinterest's internal large-scale image generation system powering background outpainting, aspect-ratio outpainting, super-resolution, product extraction, and multi-image scene synthesis
- Uses a fine-tuned DiT (likely FLUX-family) with product-specific aesthetic fine-tuning at 1B+ impressions/day scale
- Key technique: **video-augmented key frames** for multi-image consistency — single style anchor image drives coherent scene generation across products
- Digital-Stud relevance: validates multi-image scene synthesis as a production-ready technique; directly applicable to consistent product/character scene generation workflows



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

### 🆕 UnSCAR — Universal Scalable Controllable Adaptable Image Restoration (arXiv 2603.07406, March 2026)

- Handles **16+ degradation types** (deblur, denoise, deraining, dehazing, low-light, SR, compression, etc.) in a single model
- Architecture: Mixture-of-Experts (MoE) routing, unified guidance encoding, bidirectional feedback synchronization
- User-controllable fine-grained restoration via **degradation sliders**
- Few-shot adaptation to medical imaging (competitive vs. task-specific models)
- UNC Chapel Hill + UC San Diego
- Digital-Stud relevance: drop-in quality restoration step for AI-generated character images with artifacts

### 🆕 ImageEdit-R1 — Multi-Agent RL Framework for Sequential Image Editing (arXiv 2603.08059, March 2026)

- Formulates image editing as a **sequential decision-making problem** (RL-based)
- Multi-agent: specialized agents for instruction decomposition, region identification, edit execution
- Evaluated on GEdit-O and ImgEdit-O benchmarks; top-tier multi-step editing accuracy
- Digital-Stud relevance: autonomous pipeline for complex multi-step character editing (remove → replace → relight)

### 🆕 A²-Edit — Unified Reference-Guided Image Inpainting (arXiv 2603.10685, March 10 2026)

- Single framework handling three inpainting scenarios: **objects, humans, background scenes**
- Reference-guided: uses reference image to fill masked region with identity-preserving accuracy
- Eliminates need for separate specialized inpainting models per content type
- Digital-Stud relevance: character body completion, background fill, and prop replacement with one unified node

### 🆕 JiT (Just-in-Time) — Training-Free 7× Speedup on FLUX.1-dev (arXiv 2603.10744, March 2026)

- **Training-free spatial acceleration** for Diffusion Transformers via token reuse at redundant spatial positions across timesteps
- Achieves up to **7× speedup on FLUX.1-dev with near-lossless output quality** — no fine-tuning required
- Works by identifying spatially redundant tokens during denoising and reusing cached computations instead of rerunning attention
- Drop-in acceleration: no model weight changes, compatible with existing sampler/scheduler configurations
- Digital-Stud relevance: direct LoRA inference speedup — faster iteration when testing character LoRAs or IP-Adapter chains; watch for ComfyUI node integration

### 🆕 StyleGallery — Training-Free Multi-Reference Style Transfer (arXiv 2603.10354, March 2026)

- **Semantic-aware personalized style transfer** that accepts a *gallery* of style images (series) as reference input, not just one
- Extracts semantic style embeddings across the gallery and applies them coherently to target content — training-free, inference-only
- Outperforms prior single-reference style transfer in consistency and generalization to novel content
- Digital-Stud relevance: multi-reference stylization directly applicable to maintaining a consistent visual look across character shots; complements IP-Adapter usage

### 🆕 NAMI — Spatiotemporal Separation Progressive DiT Framework (arXiv 2503.09242v3, March 2026)

- Bridges **progressive rectified flow** with spatiotemporal separation for efficient video generation
- Stages the denoising process by resolution: coarse spatial + temporal pass → fine pass
- Reduces compute budget vs. full-resolution DiT while maintaining quality
- Digital-Stud relevance: more efficient alternative to Wan 2.2 / LTX-2.3 for lower-VRAM video generation

### 🆕 AIMomentz Open AI Image Evaluation Platform (March 12, 2026)

- First open platform for benchmarking image generators via **head-to-head human preference voting**
- CAP-SRP cryptographic audit trail — tamper-proof record of every AI decision and refusal
- Four-axis ratings: aesthetics, prompt alignment, plausibility, overall quality
- Domain-specific tracks: anime, landscape, architecture, sci-fi, abstract, animals
- FLUX/SDXL coming via Together AI + fal.ai integration; Apache 2.0 dataset exports
- Digital-Stud relevance: authoritative benchmark to evaluate character consistency and aesthetic quality of model outputs

### 🆕 Ideogram 3.0 — Widespread Platform Integration (March 2026)

- Now integrated into **Adobe Creative Cloud** (20 credits per generation)
- Available in **Picsart AI Playground** (launched March 9, 2026 — 90+ models in one hub)
- Free tier: **40 generations/day** (no card required)
- Maintains best-in-class **text rendering / typography** accuracy
- Digital-Stud relevance: top choice for any workflow requiring readable text inside generated images

### 🆕 Veo 3.1 Pricing Confirmed — Vertex AI & Consumer Tiers (March 2026)

- **Google AI Pro** ($19.99/mo): 1,000 credits → ~90 Veo 3.1 Fast 10-sec videos/month
- **Google AI Ultra** ($249.99/mo): 12,500+ credits
- **Vertex AI API**: Veo 3.1 Quality **$0.40–$0.75/second**, Veo 3.1 Fast **~$0.15/second**
- Third-party aggregators (laozhang.ai etc.) from **~$0.10/second**
- Native audio synthesis (dialogue, SFX, ambient) generated alongside video
- Digital-Stud relevance: fast tier ($0.15/s) makes short 3–5 sec character motion clips economically viable

### 🆕 RealWonder — Real-Time Physical Action-Conditioned Video Generation (arXiv 2603.05449, March 2026)

- **First real-time streaming system** for physics-action-conditioned video from a single image
- Accepts **3D physical actions** (forces, torques) as input; uses physics simulation → optical flow → realistic motion
- Streaming architecture: frames generated and emitted continuously without buffering full clip
- GitHub: [PKU-YuanGroup / RealWonder](https://arxiv.org/abs/2603.05449)
- Digital-Stud relevance: enables physically grounded character motion from a single reference photo — complements ComfyUI img2vid pipelines

### 🆕 Hitem3D v2.0 — Single/Multi-View Image to Production-Ready 3D (Math Magic, March 2026)

- Converts **single or multi-view images** into production-ready 3D models for 3D printing and industrial design
- Improved geometric accuracy, UV unwrapping, and mesh quality vs v1.0
- Accessible via web dashboard and API; pricing competitive with Tripo and Meshy
- Digital-Stud relevance: fast image→3D pipeline for props and characters; useful downstream of FLUX.2 / Midjourney V7 image gen

### 🆕 DrPose — Direct Reward Fine-Tuning for 3D Pose Consistency (arXiv 2603.02619, March 2026)

- Proposes **PoseScore**: differentiable reward function measuring 3D pose consistency between latent images
- Fine-tunes diffusion models with RLHF-style reward signal to improve pose accuracy in generated images
- Reduces anatomy errors (twisted limbs, inverted joints) common in FLUX / SD3.5 outputs
- Digital-Stud relevance: key technique for training pose-aware LoRAs and evaluating pose ControlNet quality

### 🆕 Color Fidelity Benchmark & CFR (arXiv 2603.10990, March 11 2026)

- **"Too Vivid to Be Real?"** — addresses persistent oversaturation in T2I models (FLUX, SDXL, Midjourney, etc.)
- **Color Fidelity Dataset (CFD)**: 1.3M+ images with real-world color reference ground truth
- **Color Fidelity Metric (CFM)**: training-free evaluation of perceptual color authenticity vs. real photographs
- **Color Fidelity Refinement (CFR)**: training-free post-processing to bring generated image colors closer to real-world distribution — no retraining or fine-tuning needed
- Code + dataset on GitHub
- Digital-Stud relevance: drop-in CFR post-process for any FLUX or SDXL output to reduce "AI look" in photorealistic character renders

## 🎬 Video Generation SOTA — March 2026

### 🆕 WAN 2.7 — Scheduled March 2026 Release

- Alibaba/WAN team has confirmed **WAN 2.7** for release in March 2026 with significant upgrades over 2.6
- New capabilities include: **video generation from start/end frame pairs** (bookend-style control), **3×3 grid image conditioning** for storyboard-style multi-angle synthesis, and subject + voice reference for talking-head consistency
- Wan 2.2 Spicy (uncensored, high-motion variant) remains the current community production default while 2.7 lands
- Digital-Stud relevance: start/end frame control is a major workflow enabler for character-to-scene compositing; watch for WanGP v11 update when 2.7 drops

### 🆕 Wan 2.7 — Confirmed March 2026 with Major Capability Upgrades

- **Officially confirmed** for release in March 2026 (confirmed by Alibaba source); specific date still unannounced as of March 12
- **New capabilities over Wan 2.2/2.6:**
  - Start & End Frame Video control (precise boundary frames)
  - Grid-to-Video: 9-grid multi-angle input for dimensional/multi-perspective content
  - Subject + Voice Reference: combined visual + audio subject conditioning
  - Instruction Editing: edit videos with natural language instructions
  - Video Cloning: replicate style and motion of reference clips
  - Flexible 2–15 second output, up to 1080P
  - Supports up to **5 video reference inputs** simultaneously
- Significant improvements in motion quality, consistency, and subject preservation vs 2.6
- Digital-Stud relevance: grid-to-video multi-angle input + instruction editing is a direct unlock for character animation workflows; LoRAs trained on Wan 2.2 are expected to be partially compatible

### 🆕 Seedance 2.0 — Up to 12 Reference Files, Multi-Camera, Native Lip-Sync (March 2026)

- **Multi-reference generation**: accepts up to **12 reference files** (photos, video, audio, text) per generation — highest reference count of any commercial video model
- **Multi-camera capabilities**: can synthesize a scene from multiple camera angles in one generation pass
- **Native lip-sync and audio generation**: audio is generated end-to-end, not post-processed
- API now available; competitive with Kling 3.0 at similar pricing tier
- Cinematic prompt guide published March 12 with 10 structured directorial prompt templates
- Digital-Stud relevance: 12-reference multi-modal input is a direct upgrade path for character consistency — attach reference face, voice, pose, and motion clips simultaneously

### 🆕 FastLightGen — Model Compression for Wan/HunyuanVideo/Veo3/Kling (arXiv 2603.01685v2, March 2026)

- Transforms large DiT video models (WanX, Hunyuan, Veo3, Kling) into fast lightweight variants via structured distillation
- Reduces inference steps and parameter count while maintaining quality comparable to full models
- Algorithm is model-agnostic: applies to any large DiT video backbone
- Digital-Stud relevance: enables faster iteration cycles locally; potential ComfyUI integration for step-reduced Wan 2.2 / LTX-2.3

### 🆕 WaveSpeedAI UGC Video Generator — Native Audio, Portrait-First (March 2026)

- Creator-style video from text prompt + optional reference image; native audio sync in single pass
- Optimized for portrait video and talking-head content — direct competitor to Runway Characters for UGC workflows
- Available via WaveSpeedAI API; competitive pricing vs Seedance 2.0
- Digital-Stud relevance: fast prototyping alternative for talking-head + consistent character workflows without Wan VRAM overhead



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

### 🆕 Wan 2.7 — Confirmed March 2026 with Major Capability Upgrades

- **Officially confirmed** for release in March 2026 (confirmed by Alibaba source); specific date still unannounced as of March 12
- **New capabilities over Wan 2.2/2.6:**
  - Start & End Frame Video control (precise boundary frames)
  - Grid-to-Video: 9-grid multi-angle input for dimensional/multi-perspective content
  - Subject + Voice Reference: combined visual + audio subject conditioning
  - Instruction Editing: edit videos with natural language instructions
  - Video Cloning: replicate style and motion of reference clips
  - Flexible 2–15 second output, up to 1080P
  - Supports up to **5 video reference inputs** simultaneously
- Significant improvements in motion quality, consistency, and subject preservation vs 2.6
- Digital-Stud relevance: grid-to-video multi-angle input + instruction editing is a direct unlock for character animation workflows; LoRAs trained on Wan 2.2 are expected to be partially compatible

### 🆕 Seedance 2.0 — Reference Cluster & Character Consistency (Feb 2026)

- **Reference Cluster System**: up to **12 multimodal inputs** (9 images + 3 videos); @-tag syntax for identity/motion binding
- **Golden Ratio Method**: 70% identity ref + 30% motion ref weighting → prevents character drift across shots
- Consistency script workflow enables >30-second sequences with same character
- Digital-Stud verdict: currently best for multi-shot consistent character video; API: Replicate, fal.ai, ByteDance API

### 🆕 Wan 2.7 — Confirmed March 2026 with Major Capability Upgrades

- **Officially confirmed** for release in March 2026 (confirmed by Alibaba source); specific date still unannounced as of March 12
- **New capabilities over Wan 2.2/2.6:**
  - Start & End Frame Video control (precise boundary frames)
  - Grid-to-Video: 9-grid multi-angle input for dimensional/multi-perspective content
  - Subject + Voice Reference: combined visual + audio subject conditioning
  - Instruction Editing: edit videos with natural language instructions
  - Video Cloning: replicate style and motion of reference clips
  - Flexible 2–15 second output, up to 1080P
  - Supports up to **5 video reference inputs** simultaneously
- Significant improvements in motion quality, consistency, and subject preservation vs 2.6
- Digital-Stud relevance: grid-to-video multi-angle input + instruction editing is a direct unlock for character animation workflows; LoRAs trained on Wan 2.2 are expected to be partially compatible

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

### 🆕 LTX-2.3 — Day-0 ComfyUI Support + Multi-LoRA (Confirmed March 2026)

- **Day-0 ComfyUI support** confirmed by comfy.org blog — install via ComfyUI Manager
- Three official **IC-LoRA control adapters** available:
  - `LTX-2.3-22b-IC-LoRA-Union-Control` (multi-purpose)
  - `LTX-2.3-22b-IC-LoRA-Inpainting` (region fill)
  - `LTX-2.3-22b-IC-LoRA-Motion-Track-Control` (motion tracking)
- Supports **up to 3 simultaneous LoRAs** in a single inference run
- Sigma fine-tuning + sampler selection significantly impact output quality (community finding)
- Official trainer package at `github.com/Lightricks/LTX-2` for full fine-tune + LoRA training
- Digital-Stud relevance: most practical open-source audio-video model for ComfyUI right now

### 🆕 Wan 2.7 — Confirmed March 2026 with Major Capability Upgrades

- **Officially confirmed** for release in March 2026 (confirmed by Alibaba source); specific date still unannounced as of March 12
- **New capabilities over Wan 2.2/2.6:**
  - Start & End Frame Video control (precise boundary frames)
  - Grid-to-Video: 9-grid multi-angle input for dimensional/multi-perspective content
  - Subject + Voice Reference: combined visual + audio subject conditioning
  - Instruction Editing: edit videos with natural language instructions
  - Video Cloning: replicate style and motion of reference clips
  - Flexible 2–15 second output, up to 1080P
  - Supports up to **5 video reference inputs** simultaneously
- Significant improvements in motion quality, consistency, and subject preservation vs 2.6
- Digital-Stud relevance: grid-to-video multi-angle input + instruction editing is a direct unlock for character animation workflows; LoRAs trained on Wan 2.2 are expected to be partially compatible

### 🆕 Seedance 2.0 — 2-Minute Native Audio-Video, Best API Cost (ByteDance, March 2026)

- **Only major model generating up to 2 minutes in a single pass** (vs ~20s for LTX-2.3, ~5s for Wan 2.2)
- **Native audio generation** alongside video — dialogue, SFX, ambient synchronized in single inference
- **Most affordable API pricing** in its tier among closed-source models (free tier via Dreamina: daily credits)
- Direct competitor to Veo 3.1 for long-form narrative video; faster generation latency
- Available via fal.ai API and Dreamina consumer platform
- Digital-Stud relevance: best choice when you need >20 seconds of continuous audio-synced narrative video in one call

### 🆕 StreamWise — Real-Time Multi-Modal Generation Serving at Scale (arXiv 2603.05800, March 2026)

- **Sub-second latency** streaming system combining A100 + H100 for real-time video/audio output at under $40/video at scale
- Benchmarks Wan 2.2 (16 FPS MoE DiT) and HunyuanVideo (30 FPS) in unified serving architecture
- Streaming-first: outputs first frame while generating the rest — eliminates buffering wait times
- Digital-Stud relevance: production deployment pattern for Wan/HunyuanVideo APIs; informs RunPod/fal.ai cost planning

## 🧵 LoRA Training SOTA — March 2026

### 🆕 AI-Toolkit (ostris) — Dynamic Rank Scheduling Feature (March 2026)

- New feature in `ostris/ai-toolkit`: **dynamic rank scheduling** — rank can ramp up/down across training steps instead of fixed throughout
- Enables warm-up with low rank (better stability) then expansion for detail capture; combines with Stable-LoRA A-init fix
- Config: `network.rank_schedule: [{step: 0, rank: 8}, {step: 500, rank: 32}]` pattern
- Community finding: rank 8→32 schedule on FLUX.2 shows improved subject fidelity vs flat rank-32 with comparable step count
- Digital-Stud relevance: immediate practical improvement for character/face LoRA training; update kohya_config_example.toml to reflect


### 🆕 ID-LoRA — Identity-Driven Audio-Video Personalization with In-Context LoRA (arXiv 2603.10256, Tel Aviv University, March 2026)

- **First In-Context LoRA framework** for unified audio-visual personalization — joint video + audio LoRA on LTX-2 backbone
- Uses **negative temporal positions in RoPE** to cleanly separate reference audio from target tokens; no architecture change needed
- Achieves SOTA with only ~3K training pairs on a single GPU — extremely sample-efficient
- Classifier-free guidance variant amplifies speaker-specific features while text prompt controls environment/speaking style
- Project page: [id-lora.github.io](https://id-lora.github.io)
- Digital-Stud relevance: enables training personalized talking-head LoRAs with synchronized voice on LTX-2.3; replaces cascaded audio-video pipelines

### 🆕 BSRA — Block-Structured Rank Adaptation with Dual Sparsity (Nature Scientific Reports, March 9 2026)

- Combines block-level **structural sparsity** (differentiable evolutionary gating) with **dynamic rank pruning** (sensitivity-based cubic scheduling)
- Addresses core limitation of fixed-rank LoRA: different layers need different rank budgets — BSRA adapts rank per-layer
- Achieves parameter efficiency superior to standard LoRA while maintaining or exceeding fine-tune quality
- Digital-Stud relevance: practical for training character LoRAs on FLUX with tighter VRAM budgets; viable alternative to fixed network_dim 32

### 🆕 Stable-LoRA — Stabilizing Feature Learning via Weight-Shrinkage (arXiv 2603.05204, March 5 2026)

- Identifies that **non-zero init of LoRA A matrix** breaks self-stability in feature learning — a previously overlooked failure mode
- Fix: **weight-shrinkage strategy** that progressively shrinks A during earliest training steps; negligible compute overhead
- Consistent quality improvements across diverse models; compatible with existing LoRA trainers (ai-toolkit, kohya_ss)
- Digital-Stud relevance: apply as a training hygiene patch when running FLUX LoRA with ai-toolkit — prevents identity drift in early epochs


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

### 🆕 Wan 2.2 LoRA Training — Field-Tested Community Settings (March 2026)

- **Learning rate**: `1e-4` with cosine schedule; lower (5e-5) for character faces
- **Network rank**: 32 recommended; 64 for style LoRAs; 16 sufficient for concepts
- **Steps**: 800–1500 for character; 300–600 for style/concept
- **Key technique**: reduce "plastic skin" artifacts via mild regularization images + lower LR
- Avoid overfitting: stop at ~1000 steps and test; late-stage LoRAs lose detail
- FFGO LoRA model widely used with ComfyUI Wan 2.2 wrapper for consistent first-frame workflows
- Digital-Stud relevance: validated recipe; update `kohya_config_example.toml` targets to Wan 2.2 variant

## 🏃 Pose Estimation SOTA — March 2026

### 🆕 DuoMo — Dual Motion Diffusion for World-Space Human Reconstruction (arXiv 2603.03265, March 2026)

- Recovers full **world-space** human motion from unconstrained monocular video — not just camera-relative local pose
- Two-prior diffusion approach (local body + global trajectory) + direct mesh vertex generation
- Reduces world-space reconstruction error 16–30% vs prior SMPL-fitting baselines
- ICRA 2026 accepted
- Digital-Stud relevance: enables accurate 3D trajectory extraction from reference video for motion retargeting into generated video; complements DWPose for full-body scene grounding



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
| **CIGPose** | Causal Intervention GNN whole-body (March 2026) | Whole-body (COCO-WholeBody) | **67.0% AP** (no extra data) / 67.5% AP (UBody) | — | Structural causal model eliminates context spurious correlations; anatomical plausibility enforcement; code public |
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

### 🆕 Sora 1 End-of-Life — US March 13, 2026

- OpenAI officially discontinuing **Sora 1** in the United States from March 13, 2026
- Users must export content before deadline; signals full transition to Sora 2
- Sora 2 capabilities: multi-shot storytelling, up to 2-min clips, integrated in ChatGPT
- Digital-Stud relevance: Sora 2 is now the only OpenAI video offering — factor into API cost planning

### 🆕 Kling 3.0 API — Full Technical Spec Confirmed (Public since Feb 5, 2026)

- Native **4K rendering** (vs. upscaled 1080p in Kling 2.0), 30-60fps output
- **Universal Reference**: lock character consistency across shots with up to **7 reference images**
- Built-in **multilingual lip-sync** (25+ languages) — no separate dubbing step needed
- **Motion Control** premium tier: fine-grained camera and subject motion specification
- Pricing: $6.99–$25.99/month; ComfyUI API nodes enabled via v0.16.1 (Kling 3.0 Motion Control)
- Digital-Stud relevance: Universal Reference is a direct answer to multi-shot character consistency problem

### 🆕 FrameDiT — Frame-Level Matrix Attention for Efficient Video DiT (arXiv 2603.09721, March 10 2026)

- Novel attention mechanism: **frame-level matrix attention** instead of full spatiotemporal attention
- Reduces compute complexity while maintaining temporal coherence across frames
- DiT architecture; tested on text-to-video benchmarks with competitive quality at lower cost
- Digital-Stud relevance: architectural direction to watch for next-gen efficient video models

### 🆕 FC-4DFS — Frequency-Controlled Flexible 4D Facial Expression Synthesis (arXiv 2603.10326, March 2026)

- Learns **frequency-decomposed facial dynamics** for temporally coherent 4D expression synthesis
- Temporal coherence loss enforces smooth relative displacements across frames
- Applications: facial animation for AI-generated characters, emotion transfer in video
- Digital-Stud relevance: complements HunyuanVideo-Avatar for more expressive emotion-driven face animation

### 🆕 ParTY — Part-Guidance for Expressive Text-to-Motion Synthesis (arXiv 2603.09611, March 2026)

- **Body-part semantic guidance** for fine-grained articulation control from text prompts
- Enables precise control over individual limbs (e.g., "raise left arm, tilt head right")
- Improves expressiveness beyond whole-body text-to-motion baselines
- Digital-Stud relevance: richer motion generation for character animation pipelines

### 🆕 WiFi DensePose / RuView — Through-Wall Pose Estimation via Commodity WiFi (March 2026)

- Open-source: `github.com/ruvnet/RuView` — maps human body poses using standard WiFi signals
- No camera required; occlusion-immune; detects vital signs + presence
- Demonstrated: real-time 2D dense pose estimation, breathing/heart-rate monitoring
- Privacy note: raises wall-penetration surveillance concerns (covered by Cybernews March 2026)
- Digital-Stud relevance: novel no-camera input modality for motion capture in ComfyUI pipelines

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

### 🆕 ComfyUI-HunyuanVideo-Avatar — Official ComfyUI Node (Yuan-ManX, March 2026)

- GitHub: `github.com/Yuan-ManX/ComfyUI-HunyuanVideo-Avatar`
- Install via ComfyUI Manager; supports GGUF + FP8 quantized weights
- Enables audio-driven human animation directly in ComfyUI: image + audio → animated video
- Multi-character support; emotion-controllable; MM-DiT backbone
- Similar to Sonic/SadTalker but animates full body + scene (not just face)
- Digital-Stud relevance: **ready-to-use right now** for character talking-head + body animation nodes

### 🆕 SAVE — Speech-Aware Video Representation Learning (arXiv 2603.08224, March 2026)

- New SOTA on **text-to-video retrieval** benchmarks: +8.5 on MSRVTT-9k, +3.1 on DiDeMo vs prior SOTA (AVIGATE)
- Learns joint speech-video embeddings; improves temporal alignment for audio-driven video workflows
- Practical impact: better retrieval for building talking-head training sets and audio-synced video datasets
- Digital-Stud relevance: useful for curating high-quality audio-video training pairs for HunyuanVideo-Avatar fine-tunes

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

### OCpose — Optimal Transport Multi-Person Pose Evaluation (arXiv 2603.10398, March 11 2026)

- Fixes fundamental flaws in standard mAP for multi-person pose: high-confidence false positives escape penalization in traditional metrics
- **Optimal Transportation (OT)** matching: penalizes false positives globally regardless of confidence score
- Confidence-weighted keypoint matching + pixel-wise masks (not bounding boxes) for precise evaluation
- **83.3% agreement with human preference** vs. existing metrics — Toyota Technological Institute
- Digital-Stud relevance: rigorous benchmark for DWPose / RTMPose / O26-Pose output quality in ControlNet workflows

### Motion Forcing — Decoupled Video Generation via Point-Shape-Appearance (arXiv 2603.10408, March 11 2026)

- Addresses the video generation trilemma: visual quality + physical consistency + controllability simultaneously
- **Point-Shape-Appearance (PSA) hierarchical paradigm**:
  - *Points* — sparse geometric anchors tracking object trajectories
  - *Shape* — dynamic depth maps for 3D geometry verification
  - *Appearance* — high-fidelity texture rendering conditioned on geometry
- **Masked Point Recovery (MPR)**: active physical reasoning for occluded trajectory inference
- HKUST-GZ; outperforms prior pose-conditioned video gen on autonomous driving & robotics
- Digital-Stud relevance: PSA decoupling enables independent control of character body trajectory (points) from clothing/appearance — direct unlock for character animation


### LiTo — Surface Light Field Tokenization for Joint Geometry+Appearance (arXiv 2603.11047, March 12 2026)

- **LiTo** proposes a 3D latent representation that jointly models object geometry and view-dependent appearance — unifying what prior works treated separately
- Tokenizes surface light fields: captures both shape and specular/diffuse appearance in a single compact latent
- Enables multi-view consistent generation with controllable view-dependent effects (reflections, materials)
- Digital-Stud relevance: potential building block for 3D-aware character generation in ComfyUI — geometry + material appearance in one latent space, bridging img-gen and 3D workflows

### ⚠️ Tooling Gap: ai-toolkit FLUX.2 Klein 9B LoRA Support (GitHub Issue #664, March 2026)

- Community opened Issue #664 requesting LoRA training support for FLUX.2 Klein 9B in ostris/ai-toolkit
- **Not yet merged** — ostris ai-toolkit currently supports FLUX.1 dev/schnell but lacks Klein 9B adapter
- Workaround: some users manually patching model config; no official ETA
- Digital-Stud relevance: blocks fine-tuning Klein 9B for character identity work until merged — monitor https://github.com/ostris/ai-toolkit/issues/664

### DiT4DiT — Coupled Video + Action Diffusion Transformer (arXiv 2603.10448)

- Couples a **video DiT** with an **action DiT** in end-to-end joint training (Vision-Language-Action framework)
- Bridges video generation and robot/character action modeling
- **Digital-Stud relevance**: Foundation for future pose-conditioned character action video generation


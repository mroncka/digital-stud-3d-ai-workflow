# Cloud GPU Guide

## Providers

### VastAI — Cheapest
- RTX 3090: $0.40-0.60/hr | A100: $1.20-1.80/hr
- Community hosts — variable reliability
- Best for: cost-sensitive work

### RunPod — Most Reliable
- Similar pricing, slightly higher
- One-click ComfyUI template
- Best for: reliability + fast setup

## GPU Selection

| GPU | VRAM | Best For | Cost/hr |
|-----|------|----------|---------|
| RTX 3080 | 10GB | Image gen only | ~$0.25 |
| RTX 3090 | 24GB | Image + video | ~$0.50 |
| RTX 4090 | 24GB | Image + video (faster) | ~$0.75 |
| A100 40GB | 40GB | Fast video + training | ~$1.50 |
| A100 80GB | 80GB | LoRA training | ~$2.50 |

## Monthly Cost Estimates

```
Light (mostly images): $20-50
Regular (images + video): $50-100
Heavy (video-focused): $100-200+
```

## Cost Tips

1. Batch everything — start, render all, terminate
2. Spot/interruptible instances: 30-50% cheaper
3. Persistent volume for models (save reinstall time)
4. Light2x LoRA for Wan — fewer steps needed
5. Low-res seed candidates first, upscale only winners

## RunPod Setup (Easiest)

1. RunPod → Pods → Deploy → search "ComfyUI"
2. Select template + GPU → Deploy
3. Open pod URL → ComfyUI ready
4. Mount persistent volume for models

## VastAI Setup (Cheaper)

```bash
git clone https://github.com/comfyanonymous/ComfyUI
cd ComfyUI && pip install -r requirements.txt
cd custom_nodes
git clone https://github.com/ltdrdata/ComfyUI-Manager
# Download models to models/ subfolders
python main.py --listen 0.0.0.0 --port 8188
```

Mount a persistent volume (~50GB) at /workspace to avoid re-downloading models each session.

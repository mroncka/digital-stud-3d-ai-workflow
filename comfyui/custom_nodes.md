# Required Custom Nodes for ComfyUI

## Nodes

| Node | Repo | Purpose |
|------|------|---------|
| ComfyUI-Manager | ltdrdata/ComfyUI-Manager | Node management |
| ComfyUI_IPAdapter_plus | cubiq/ComfyUI_IPAdapter_plus | Image reference conditioning |
| ComfyUI-WanVideoWrapper | kijai/ComfyUI-WanVideoWrapper | Wan2.2 video generation |
| ComfyUI-VideoHelperSuite | Kosinkadink/ComfyUI-VideoHelperSuite | Video output/combine |
| ComfyUI_InstantID | cubiq/ComfyUI_InstantID | Face consistency |
| ComfyUI-Impact-Pack | ltdrdata/ComfyUI-Impact-Pack | Face detection/masking |
| was-node-suite-comfyui | WASasquatch/was-node-suite-comfyui | Utility nodes |

## Models

### Checkpoints
- `flux1-dev.safetensors` — primary image model
- `Wan2.2_I2V_480p.safetensors` or 720p variant

### VAE
- `ae.safetensors` (Flux VAE)

### LoRAs
- `anime_style_base.safetensors` — train from style references
- `character_custom.safetensors` — train from 3D renders (see /lora/)

### CLIP (for Flux)
- `clip_l.safetensors`
- `t5xxl_fp8_e4m3fn.safetensors`

## Install

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/ltdrdata/ComfyUI-Manager
# Restart ComfyUI, then use Manager for remaining nodes
```

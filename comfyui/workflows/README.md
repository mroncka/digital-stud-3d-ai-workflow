# ComfyUI Workflows

Three core workflows for the 3D+AI pipeline.

## image_gen_base.json — Base Image Generation (Qwen + Flux)

**Node chain:**
1. Load 3D render as image
2. Qwen VLM node — analyze pose from render (replaces manual ControlNet)
3. Flux checkpoint loader (flux1-dev)
4. LoRA stack: anime-style LoRA + character LoRA
5. KSampler (steps: 20-30, CFG: 3.5-5.0)
6. VAE decode → output

**Settings:** 768x1024 or 1024x1024 | Flux dev | euler sampler | run 20+ seeds

## face_refinement.json — Face/Hair Inpainting

**Node chain:**
1. Load best image from base workflow
2. Mask face region (manual or SAM node)
3. Inpaint with face-specific LoRA (weight 0.8-1.0)
4. IP-Adapter with cosplay/game character ref
5. Blend back at strength 0.6-0.75

**Tips:** Run 20-50x. Hair needs a separate mask pass from face.

## video_wan.json — Wan2.2 Video (img2vid)

**Node chain:**
1. Load best still image
2. Wan2.2 I2V checkpoint loader
3. Video conditioning (start frame + optional end frame)
4. Light2x LoRA (optional — fewer steps, minimal quality loss)
5. KSampler video (steps: 20, ~81 frames = 3-4s @ 24fps)
6. Video combine → MP4

**Tips:** 6 seconds (~144 frames) is the stable limit on 24GB VRAM. Use img2vid not txt2vid.

## See custom_nodes.md for required nodes and models.

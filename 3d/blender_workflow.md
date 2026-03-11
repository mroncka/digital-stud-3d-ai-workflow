# Blender Posing + Depth Export

## Advantages Over DAZ

- Free and open source
- More precise pose control
- Mixamo animation import for video reference frames
- Native OpenPose export

## Addons

- **Rigify** (built-in) — auto-rig
- **MPFB2** — free human figure generator
- **BlenderKit** (built-in) — free asset library

## Render Settings

```python
import bpy
scene = bpy.context.scene
scene.render.engine = 'CYCLES'
scene.render.resolution_x = 1024
scene.render.resolution_y = 1024
scene.render.film_transparent = True  # clean background
```

## Depth Map Export

```
Compositing → Use Nodes → Enable
Add: Render Layers → Map Range (0-10) → File Output (EXR)
```

## Mixamo Pipeline (for Video Gen reference frames)

1. Export mesh as FBX
2. Upload to mixamo.com (free Adobe account)
3. Auto-rig → select animation
4. Download FBX @ 30fps
5. Import to Blender → render key frames
6. Use as start/end frames for Wan I2V

## OpenPose Export

```
Install: ZusakiHideki/blender-openpose
File → Export → OpenPose JSON
ComfyUI: ControlNet Loader → openpose_full
```

## Free Figures

- MPFB2 (full morphs, free)
- Ready Player Me (glTF import, free)
- Mixamo characters (free with Adobe account)

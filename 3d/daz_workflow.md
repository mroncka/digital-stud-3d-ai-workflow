# DAZ Studio Posing Workflow

## Why DAZ

- Free Genesis figures with good anatomy
- Built-in pose library, no rigging needed
- Clean neutral-background renders

## Render Settings for AI Reference

```
Engine: NVIDIA Iray (or 3Delight for speed)
Resolution: 1024x1024 minimum (1536x1536 ideal)
Quality: Medium — just need clean pose data
Background: White/gray flat plane
Lighting: 3-point neutral (no colored gels)
```

## Angles to Render (8 per pose)

1. Front (0 deg)
2. 3/4 front left (45 deg)
3. 3/4 front right (-45 deg)
4. Side left (90 deg)
5. Side right (-90 deg)
6. 3/4 back left (135 deg)
7. Upper body close-up
8. Face close-up

## Depth Map Export

`Render Settings → Render Elements → Add Element → Depth`

Export depth maps alongside RGB for ControlNet precision mode.

## Workflow

1. Load figure → apply/adjust pose
2. Fine-tune clothing with dForce physics
3. Batch render 8 angles: `Render → Batch Render`
4. Export to `training_data/[character]/img/[repeat]_[trigger]/`
5. Write `.txt` caption files

**Time:** 30-60 min setup, 10-20 min to render 8 angles.

## Free Resources

- [Daz3D Free Models](https://www.daz3d.com/free-3d-models)
- [Renderosity Free Section](https://www.renderosity.com/marketplace/free)
- [ShareCG](https://www.sharecg.com/)

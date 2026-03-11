# Video Assembly Guide

## The Core Challenge

AI video tops out at ~6 seconds per stable clip. **The quality of stitching separates professional output from slop.**

## Per-Clip Budget

| Scene | Iterations | Cloud Cost |
|-------|-----------|------------|
| Simple (head turn) | 10-20 | $2-5 |
| Medium (walk cycle) | 20-50 | $5-15 |
| Complex (action) | 50-100+ | $15-30+ |

## Cut-Hiding Techniques

1. **Motion-at-Cut** — start/end on moving frames, not static holds
2. **Match Cut** — end clip A on a pose, start clip B on the same pose
3. **Smash Cut** — fast motion hides abrupt transitions
4. **Audio-Driven** — cut on beat
5. **L-Cut / J-Cut** — audio leads/trails the video transition

## Enhancement Pipeline

### Quick (drafts)
```
Wan output → editor → export
```

### Quality (release)
```
Wan output → GIMM-VFI (2x frames: 24→48fps) → FlashVSR 4x → color grade → export
```

### Maximum (~1700s render on 5090 for 81-frame clip)
```
Wan 720p (81 frames) → GIMM-VFI (162 frames) → FlashVSR 4x (~5K) → DaVinci grade → 4K export
```

## Color Grading (DaVinci Resolve, free)

1. Skin tone correction — HSL, target skin hue range
2. Contrast + clarity — AI video is soft, moderate boost
3. Vignette — hides edge artifacts, draws focus
4. Anime grade — desaturate backgrounds, boost character saturation

## Export

```
Codec: H.264 or H.265
1080p: 8-12 Mbps | 4K: 20-40 Mbps
24fps | Rec.709
```

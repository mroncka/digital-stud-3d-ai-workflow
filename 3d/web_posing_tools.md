# Free Web-Based 3D Posing Tools

No install, no rigging — for fast pose drafting.

## Tools

| Tool | Platform | Best For |
|------|----------|----------|
| [PoseMyArt](https://posemy.art/app/) | Web | Quick drafts, good articulation |
| [Design Doll](https://terawell.net/en/) | Windows | Anime proportions |
| [Magic Poser](https://magicposer.com/) | Web/Mobile | Multi-figure scenes |
| [JustSketchMe](https://app.justsketch.me/) | Web | Simple single-figure poses |

## Workflow

1. Pose in web tool → screenshot/export PNG
2. ComfyUI: load as image reference
3. Qwen VLM describes pose → feed into generation
4. Or: use as ControlNet input (openpose extractor node)

**From BankruptKyun:** "Web 3D tools cut down the rigging headache by a huge margin for drafting."

## Pose Extraction from Existing Images

No 3D model needed — extract from any photo:

```
ComfyUI:
1. Load reference image
2. ControlNet Preprocessor → DWPose or OpenPose extractor
3. Outputs skeleton image
4. Use as ControlNet conditioning + apply LoRAs
```

Skeleton data is not copyrightable — safe to extract from any image.

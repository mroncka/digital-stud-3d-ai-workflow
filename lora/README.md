# LoRA Training Guide

The core of BankruptKyun's consistency trick: train on YOUR 3D renders.

## Strategy: Two LoRAs in tandem

1. **Style LoRA** — anime aesthetic + skin rendering style (train once, reuse)
2. **Character LoRA** — specific character identity, face, outfit (per character)

The character LoRA keeps the "soul" of your 3D model when AI applies realism.

## Dataset Requirements

| Parameter | Recommendation |
|-----------|---------------|
| Total images | 30-100 |
| Background | Pure neutral (white/gray/black) |
| Lighting | Even, neutral — no colored gels |
| Angles | 8+: front, 3/4 L/R, side L/R, back 3/4 L/R |
| Expressions | 3-5 for face retention |
| Resolution | 1024x1024 preferred |

**Rules:** No accessories in base renders. Consistent lighting across dataset. No flip augmentation (ruins asymmetric characters).

## Caption Format

Each image needs a `.txt` file:
```
character_name, 1girl, solo, front view, neutral expression, white background, simple background
```

Minimal captions. Over-captioning dilutes the trigger word.

## Dataset Folder Structure

```
training_data/
└── character_name/
    └── img/
        └── 25_character_name/   # repeat count
            ├── front_01.png
            ├── front_01.txt
            └── ...
```

## Kohya Config (Flux LoRA)

```toml
[model_arguments]
pretrained_model_name_or_path = "path/to/flux1-dev.safetensors"

[dataset_arguments]
train_data_dir = "./training_data/character_name"
resolution = "1024,1024"
batch_size = 1
flip_aug = false

[training_arguments]
output_name = "character_name_v1"
max_train_epochs = 20
learning_rate = 1e-4
unet_lr = 1e-4
text_encoder_lr = 5e-5
lr_scheduler = "cosine_with_restarts"

[network_arguments]
network_module = "networks.lora"
network_dim = 32
network_alpha = 16

[optimizer_arguments]
optimizer_type = "AdamW8bit"
mixed_precision = "bf16"
```

**Cloud training:** A100 80GB on RunPod, ~$2-8 per run. 30-60 min for 20 epochs on 50 images.

## Inference Weights

- Style LoRA: 0.6-0.8
- Character LoRA: 0.7-1.0
- Test at 0.5, 0.7, 0.9 — sweet spot varies

## Skin Texture Injection (IP-Adapter)

Feed high-res skin reference at IP-Adapter weight 0.3-0.5 in "style only" mode.
Free sources: Polyhaven, AmbientCG, Unsplash/Pexels portraits.

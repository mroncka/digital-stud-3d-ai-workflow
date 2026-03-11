#!/usr/bin/env python3
"""
Replicate API Test Script — digital-stud-3d-ai-workflow
Tests: Flux Dev (image gen) + Wan2.2 TI2V-5B (img2vid)

Setup:
    pip install replicate pillow requests
    export REPLICATE_API_TOKEN=r8_...

Usage:
    python scripts/api_test_replicate.py
    python scripts/api_test_replicate.py --model flux --prompt "a photo of a woman"
    python scripts/api_test_replicate.py --model wan22 --image path/to/image.jpg
"""

import argparse
import os
import sys
import time
from pathlib import Path

try:
    import replicate
except ImportError:
    sys.exit("[ERROR] replicate not installed. Run: pip install replicate")

try:
    import requests
except ImportError:
    sys.exit("[ERROR] requests not installed. Run: pip install requests")

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

FLUX_DEV_MODEL   = "black-forest-labs/flux-dev"
FLUX_SCHNELL_MODEL = "black-forest-labs/flux-schnell"
WAN22_MODEL      = "wavespeed-ai/wan-2.2-t2v-480p"  # fallback t2v; swap for TI2V when available
WAN22_I2V_MODEL  = "wan-ai/wan2.2-i2v-480p"         # img2vid

DEFAULT_FLUX_PROMPT = (
    "professional portrait photo of a woman, soft natural light, "
    "sharp focus, photorealistic, 8k resolution"
)
DEFAULT_WAN_PROMPT = (
    "cinematic camera pan, soft bokeh, subtle motion, professional video"
)

OUTPUT_DIR = Path("output/replicate_test")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def check_token() -> str:
    token = os.environ.get("REPLICATE_API_TOKEN", "")
    if not token:
        sys.exit(
            "[ERROR] REPLICATE_API_TOKEN not set.\n"
            "Export it: export REPLICATE_API_TOKEN=r8_..."
        )
    print(f"[OK] Token found: {token[:6]}...{token[-4:]}")
    return token


def save_output(url: str, filename: str) -> Path:
    """Download a URL and save to OUTPUT_DIR."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    dest = OUTPUT_DIR / filename
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    dest.write_bytes(resp.content)
    print(f"[SAVED] {dest} ({len(resp.content) / 1024:.1f} KB)")
    return dest


def print_cost_estimate(model: str, elapsed: float) -> None:
    """Very rough cost estimates based on March 2026 Replicate pricing."""
    estimates = {
        "flux-dev":     "~$0.025–0.03 / image",
        "flux-schnell": "~$0.003 / image (4-step)",
        "wan22":        "~$0.05 / sec of video",
    }
    label = (
        "flux-dev" if "flux-dev" in model
        else "flux-schnell" if "flux-schnell" in model
        else "wan22"
    )
    print(f"[COST EST] {estimates.get(label, 'unknown')}  |  elapsed: {elapsed:.1f}s")


# ---------------------------------------------------------------------------
# Flux Dev — image generation
# ---------------------------------------------------------------------------

def test_flux(
    prompt: str = DEFAULT_FLUX_PROMPT,
    model: str = FLUX_DEV_MODEL,
    width: int = 1024,
    height: int = 1024,
    num_inference_steps: int = 28,
    guidance_scale: float = 3.5,
    num_outputs: int = 1,
) -> list[Path]:
    print(f"\n{'='*60}")
    print(f"[FLUX] Model : {model}")
    print(f"[FLUX] Prompt: {prompt[:80]}..." if len(prompt) > 80 else f"[FLUX] Prompt: {prompt}")
    print(f"[FLUX] Size  : {width}x{height} | steps: {num_inference_steps} | cfg: {guidance_scale}")

    t0 = time.time()
    output = replicate.run(
        model,
        input={
            "prompt": prompt,
            "width": width,
            "height": height,
            "num_inference_steps": num_inference_steps,
            "guidance_scale": guidance_scale,
            "num_outputs": num_outputs,
            "output_format": "webp",
            "output_quality": 90,
        },
    )
    elapsed = time.time() - t0

    urls = list(output) if not isinstance(output, str) else [output]
    print(f"[FLUX] Done in {elapsed:.1f}s — {len(urls)} image(s)")
    print_cost_estimate(model, elapsed)

    saved = []
    for i, url in enumerate(urls):
        fname = f"flux_{int(time.time())}_{i}.webp"
        saved.append(save_output(str(url), fname))
    return saved


# ---------------------------------------------------------------------------
# Wan2.2 — image-to-video generation
# ---------------------------------------------------------------------------

def test_wan22_img2vid(
    image_path: str | None = None,
    prompt: str = DEFAULT_WAN_PROMPT,
    num_frames: int = 81,        # ~3.4s @ 24fps
    fps: int = 24,
    resolution: str = "480p",
) -> Path | None:
    print(f"\n{'='*60}")
    print(f"[WAN2.2 I2V] Model : {WAN22_I2V_MODEL}")
    print(f"[WAN2.2 I2V] Prompt: {prompt[:80]}")

    input_params: dict = {
        "prompt": prompt,
        "num_frames": num_frames,
        "fps": fps,
        "resolution": resolution,
        "guidance_scale": 5.0,
    }

    # Attach image if provided
    if image_path:
        img_file = Path(image_path)
        if not img_file.exists():
            print(f"[WARN] Image not found: {image_path} — running text-to-video fallback")
            model = WAN22_MODEL
        else:
            print(f"[WAN2.2 I2V] Image: {image_path}")
            input_params["image"] = open(img_file, "rb")  # noqa: SIM115
            model = WAN22_I2V_MODEL
    else:
        print("[WAN2.2] No image provided — text-to-video mode")
        model = WAN22_MODEL

    t0 = time.time()
    try:
        output = replicate.run(model, input=input_params)
    except replicate.exceptions.ReplicateError as exc:
        print(f"[ERROR] Replicate API error: {exc}")
        return None
    elapsed = time.time() - t0

    url = str(output) if isinstance(output, str) else str(list(output)[0])
    print(f"[WAN2.2] Done in {elapsed:.1f}s")
    print_cost_estimate(model, elapsed)

    fname = f"wan22_{int(time.time())}.mp4"
    return save_output(url, fname)


# ---------------------------------------------------------------------------
# Flux Schnell — fast/cheap sanity check
# ---------------------------------------------------------------------------

def test_flux_schnell(prompt: str = DEFAULT_FLUX_PROMPT) -> list[Path]:
    return test_flux(
        prompt=prompt,
        model=FLUX_SCHNELL_MODEL,
        num_inference_steps=4,
        guidance_scale=0.0,  # Schnell is guidance-distilled
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Replicate API test — Flux Dev + Wan2.2 img2vid"
    )
    parser.add_argument(
        "--model",
        choices=["flux", "flux-schnell", "wan22", "all"],
        default="all",
        help="Which model to test (default: all)",
    )
    parser.add_argument(
        "--prompt",
        default=DEFAULT_FLUX_PROMPT,
        help="Text prompt for image generation",
    )
    parser.add_argument(
        "--image",
        default=None,
        help="Path to source image for Wan2.2 img2vid",
    )
    parser.add_argument(
        "--width",  type=int, default=1024, help="Image width (Flux)"
    )
    parser.add_argument(
        "--height", type=int, default=1024, help="Image height (Flux)"
    )
    args = parser.parse_args()

    check_token()
    results: list[str] = []

    if args.model in ("flux", "all"):
        paths = test_flux(prompt=args.prompt, width=args.width, height=args.height)
        results += [str(p) for p in paths]

    if args.model in ("flux-schnell", "all"):
        paths = test_flux_schnell(prompt=args.prompt)
        results += [str(p) for p in paths]

    if args.model in ("wan22", "all"):
        path = test_wan22_img2vid(image_path=args.image, prompt=args.prompt)
        if path:
            results.append(str(path))

    print(f"\n{'='*60}")
    print(f"[DONE] {len(results)} output(s) saved to {OUTPUT_DIR}/")
    for r in results:
        print(f"  {r}")


if __name__ == "__main__":
    main()

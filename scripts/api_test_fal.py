#!/usr/bin/env python3
"""
scripts/api_test_fal.py

Digital-Stud fal.ai API test script.
Tests: Flux 2 Flex (image), HunyuanVideo 1.5 (video), Wan2.2 TI2V-5B (img2vid), Kling 2.1 (video).

Usage:
    pip install fal-client Pillow requests
    export FAL_KEY="your_fal_api_key"
    python scripts/api_test_fal.py [--test all|image|video|wan|kling] [--output-dir ./test_outputs]

Fal.ai key: https://fal.ai/dashboard/keys
All prices approximate as of March 2026.
"""

import argparse
import base64
import json
import os
import sys
import time
from pathlib import Path
from datetime import datetime

try:
    import fal_client
except ImportError:
    sys.exit("[ERROR] fal-client not installed. Run: pip install fal-client")

try:
    import requests
except ImportError:
    sys.exit("[ERROR] requests not installed. Run: pip install requests")


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

DEFAULT_OUTPUT_DIR = Path("./test_outputs")

# Model endpoints (fal.ai slugs, March 2026)
MODELS = {
    "image": {
        "flux2_flex":  "fal-ai/flux-pro/v1.1-ultra",          # Flux 2 Flex / 1.1 Ultra
        "flux_schnell": "fal-ai/flux/schnell",                 # Flux Schnell (fast/free tier)
        "flux_dev":    "fal-ai/flux/dev",                      # Flux Dev
    },
    "video": {
        "hunyuan_15":  "fal-ai/hunyuan-video",                 # HunyuanVideo 1.5
        "wan22":       "fal-ai/wan-i2v",                       # Wan2.2 TI2V img2vid
        "kling_21":    "fal-ai/kling-video/v1.6/standard/image-to-video",  # Kling 2.1
    },
}

# Test prompts
IMAGE_PROMPT = (
    "portrait of a young woman, cinematic lighting, photorealistic, "
    "soft rim light, shallow depth of field, 4k"
)
VIDEO_PROMPT = (
    "slow dolly-in, cinematic, stable camera, "
    "soft bokeh background, natural motion"
)

# Minimal test image (1x1 white PNG) encoded as data-URI for img2vid tests
_TINY_PNG_B64 = (
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8"
    "z8BQDwADhQGAWjR9awAAAABJRU5ErkJggg=="
)
TEST_IMAGE_DATA_URI = f"data:image/png;base64,{_TINY_PNG_B64}"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def check_api_key() -> str:
    key = os.environ.get("FAL_KEY", "")
    if not key:
        sys.exit(
            "[ERROR] FAL_KEY environment variable not set.\n"
            "Get your key at https://fal.ai/dashboard/keys\n"
            "Then: export FAL_KEY=your_key"
        )
    return key


def save_result(output_dir: Path, name: str, data: dict) -> Path:
    """Persist raw JSON result and, if image/video URL present, download the file."""
    output_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")

    # Save raw JSON
    json_path = output_dir / f"{name}_{ts}.json"
    with open(json_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"  [saved] {json_path}")

    # Download media if URL present
    url = None
    if "images" in data and data["images"]:
        url = data["images"][0].get("url")
        ext = "png"
    elif "video" in data:
        vid = data["video"]
        url = vid.get("url") if isinstance(vid, dict) else vid
        ext = "mp4"

    if url:
        media_path = output_dir / f"{name}_{ts}.{ext}"
        try:
            r = requests.get(url, timeout=120)
            r.raise_for_status()
            media_path.write_bytes(r.content)
            print(f"  [saved] {media_path} ({len(r.content) // 1024} KB)")
        except Exception as e:
            print(f"  [warn] Could not download media: {e}")

    return json_path


def run_with_timer(label: str, fn):
    """Run fn(), print elapsed time and return result."""
    print(f"\n{'='*60}")
    print(f"TEST: {label}")
    print(f"{'='*60}")
    t0 = time.time()
    try:
        result = fn()
        elapsed = time.time() - t0
        print(f"  [ok] completed in {elapsed:.1f}s")
        return result, elapsed, None
    except Exception as e:
        elapsed = time.time() - t0
        print(f"  [error] {e} (after {elapsed:.1f}s)")
        return None, elapsed, str(e)


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_image_flux2_flex(output_dir: Path) -> dict:
    """Flux 2 Flex / 1.1 Ultra — photorealism SOTA (~$0.03/img)."""
    print(f"  model : {MODELS['image']['flux2_flex']}")
    print(f"  prompt: {IMAGE_PROMPT[:80]}...")

    result = fal_client.run(
        MODELS["image"]["flux2_flex"],
        arguments={
            "prompt": IMAGE_PROMPT,
            "num_images": 1,
            "image_size": "portrait_4_3",
            "output_format": "png",
            "safety_tolerance": "2",
        },
    )
    save_result(output_dir, "flux2_flex", result)
    url = result.get("images", [{}])[0].get("url", "N/A")
    print(f"  image : {url}")
    return result


def test_image_flux_schnell(output_dir: Path) -> dict:
    """Flux Schnell — fast, free-tier friendly (4 steps)."""
    print(f"  model : {MODELS['image']['flux_schnell']}")
    print(f"  prompt: {IMAGE_PROMPT[:80]}...")

    result = fal_client.run(
        MODELS["image"]["flux_schnell"],
        arguments={
            "prompt": IMAGE_PROMPT,
            "num_images": 1,
            "image_size": "landscape_16_9",
            "num_inference_steps": 4,
            "output_format": "png",
        },
    )
    save_result(output_dir, "flux_schnell", result)
    url = result.get("images", [{}])[0].get("url", "N/A")
    print(f"  image : {url}")
    return result


def test_video_hunyuan_15(output_dir: Path) -> dict:
    """
    HunyuanVideo 1.5 — best lightweight open-source video (14GB VRAM).
    Text-to-video, 1080p capable.
    Estimated cost: ~$0.05-0.10 / 5s clip.
    """
    print(f"  model : {MODELS['video']['hunyuan_15']}")
    print(f"  prompt: {VIDEO_PROMPT[:80]}...")

    result = fal_client.run(
        MODELS["video"]["hunyuan_15"],
        arguments={
            "prompt": IMAGE_PROMPT + ". " + VIDEO_PROMPT,
            "video_size": "landscape_16_9",
            "num_frames": 45,            # ~3s at 15fps
            "num_inference_steps": 30,
            "guidance_scale": 6.0,
            "flow_shift": 7.0,
        },
    )
    save_result(output_dir, "hunyuan_15", result)
    vid = result.get("video", {})
    url = vid.get("url") if isinstance(vid, dict) else vid
    print(f"  video : {url}")
    return result


def test_video_wan22(output_dir: Path) -> dict:
    """
    Wan2.2 TI2V-5B image-to-video — priority model for this workflow.
    MoE architecture, 720p/24fps, Apache 2.0.
    Estimated cost: ~$0.05/sec on Replicate; fal pricing TBC.
    NOTE: Uses a minimal test image; replace TEST_IMAGE_DATA_URI with a real image URI
          for production use.
    """
    print(f"  model : {MODELS['video']['wan22']}")
    print(f"  prompt: {VIDEO_PROMPT[:80]}...")
    print(f"  image : [test data-URI — replace with real image for production]")

    result = fal_client.run(
        MODELS["video"]["wan22"],
        arguments={
            "prompt": VIDEO_PROMPT,
            "image_url": TEST_IMAGE_DATA_URI,
            "num_frames": 81,            # ~3.4s at 24fps
            "frames_per_second": 24,
            "resolution": "720p",
            "num_inference_steps": 30,
            "guidance_scale": 5.0,
        },
    )
    save_result(output_dir, "wan22_i2v", result)
    vid = result.get("video", {})
    url = vid.get("url") if isinstance(vid, dict) else vid
    print(f"  video : {url}")
    return result


def test_video_kling_21(output_dir: Path) -> dict:
    """
    Kling 2.1 image-to-video — best budget commercial option (~$0.14/5s clip).
    Great character consistency.
    """
    print(f"  model : {MODELS['video']['kling_21']}")
    print(f"  prompt: {VIDEO_PROMPT[:80]}...")
    print(f"  image : [test data-URI — replace with real image for production]")

    result = fal_client.run(
        MODELS["video"]["kling_21"],
        arguments={
            "prompt": VIDEO_PROMPT,
            "image_url": TEST_IMAGE_DATA_URI,
            "duration": "5",
            "aspect_ratio": "16:9",
        },
    )
    save_result(output_dir, "kling_21", result)
    vid = result.get("video", {})
    url = vid.get("url") if isinstance(vid, dict) else vid
    print(f"  video : {url}")
    return result


# ---------------------------------------------------------------------------
# Queue / async variant (for long-running video jobs)
# ---------------------------------------------------------------------------

def test_video_wan22_async(output_dir: Path) -> dict:
    """
    Wan2.2 via fal_client queue (recommended for video — avoids HTTP timeout).
    Polls until complete; logs progress events.
    """
    print(f"  model : {MODELS['video']['wan22']} [async queue]")

    def on_queue_update(update):
        if hasattr(update, "logs") and update.logs:
            for log in update.logs:
                print(f"    [queue] {log.get('message', '')}")

    result = fal_client.subscribe(
        MODELS["video"]["wan22"],
        arguments={
            "prompt": VIDEO_PROMPT,
            "image_url": TEST_IMAGE_DATA_URI,
            "num_frames": 81,
            "frames_per_second": 24,
            "resolution": "720p",
            "num_inference_steps": 30,
            "guidance_scale": 5.0,
        },
        with_logs=True,
        on_queue_update=on_queue_update,
    )
    save_result(output_dir, "wan22_i2v_async", result)
    vid = result.get("video", {})
    url = vid.get("url") if isinstance(vid, dict) else vid
    print(f"  video : {url}")
    return result


# ---------------------------------------------------------------------------
# Summary report
# ---------------------------------------------------------------------------

def print_summary(results: list):
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    passed = sum(1 for _, _, err in results if err is None)
    failed = len(results) - passed
    print(f"  passed: {passed}/{len(results)}")
    if failed:
        print(f"  failed: {failed}")
    print()
    for label, elapsed, err in results:
        status = "OK" if err is None else "FAIL"
        print(f"  [{status:4s}] {label:<35} {elapsed:>6.1f}s{f'  -> {err[:60]}' if err else ''}")
    print()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Digital-Stud fal.ai API test suite"
    )
    parser.add_argument(
        "--test",
        choices=["all", "image", "video", "wan", "kling", "hunyuan", "schnell"],
        default="all",
        help="Which test(s) to run (default: all)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Directory for outputs (default: {DEFAULT_OUTPUT_DIR})",
    )
    parser.add_argument(
        "--async-video",
        action="store_true",
        help="Use async queue for Wan2.2 (recommended for production)",
    )
    args = parser.parse_args()

    check_api_key()
    out = args.output_dir

    print(f"Digital-Stud fal.ai API Test Suite")
    print(f"Output dir : {out.resolve()}")
    print(f"Tests      : {args.test}")
    print(f"Timestamp  : {datetime.utcnow().isoformat()}Z")

    all_results = []

    run_image   = args.test in ("all", "image")
    run_schnell = args.test in ("all", "image", "schnell")
    run_video   = args.test in ("all", "video")
    run_wan     = args.test in ("all", "video", "wan")
    run_kling   = args.test in ("all", "video", "kling")
    run_hunyuan = args.test in ("all", "video", "hunyuan")

    if run_image:
        r, t, e = run_with_timer("Flux 2 Flex (image)", lambda: test_image_flux2_flex(out))
        all_results.append(("Flux 2 Flex", t, e))

    if run_schnell:
        r, t, e = run_with_timer("Flux Schnell (image, fast)", lambda: test_image_flux_schnell(out))
        all_results.append(("Flux Schnell", t, e))

    if run_hunyuan:
        r, t, e = run_with_timer("HunyuanVideo 1.5 (t2v)", lambda: test_video_hunyuan_15(out))
        all_results.append(("HunyuanVideo 1.5", t, e))

    if run_wan:
        if args.async_video:
            r, t, e = run_with_timer("Wan2.2 I2V async", lambda: test_video_wan22_async(out))
            all_results.append(("Wan2.2 I2V (async)", t, e))
        else:
            r, t, e = run_with_timer("Wan2.2 I2V", lambda: test_video_wan22(out))
            all_results.append(("Wan2.2 I2V", t, e))

    if run_kling:
        r, t, e = run_with_timer("Kling 2.1 I2V", lambda: test_video_kling_21(out))
        all_results.append(("Kling 2.1 I2V", t, e))

    print_summary(all_results)

    # Exit non-zero if any test failed
    if any(e for _, _, e in all_results):
        sys.exit(1)


if __name__ == "__main__":
    main()

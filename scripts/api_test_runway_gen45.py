#!/usr/bin/env python3
"""
api_test_runway_gen45.py
Digital-Stud 3D+AI Workflow — Runway Gen-4.5 API test & integration helper
Generated: 2026-03-15 (run 169)

Runway Gen-4.5 (released Dec 1 2025)
  - #1 Artificial Analysis Video Benchmark (1247 Elo, Jan 2026)
  - Adobe Firefly integration
  - 5s / 10s clips, 720p / 1080p, 16:9 / 9:16 / 1:1
  - Text-to-video (T2V) and image-to-video (I2V)
  - Motion intensity control, camera motion presets
  - Official SDK: pip install runwayml>=3.0.0
  - Docs: https://docs.dev.runwayml.com/

Usage:
  export RUNWAYML_API_SECRET=your_key_here
  python api_test_runway_gen45.py --mode t2v --prompt "cinematic close-up..."
  python api_test_runway_gen45.py --mode i2v --image_path hero.png --prompt "slow zoom out"
  python api_test_runway_gen45.py --mode test   # dry-run connectivity check
"""

import os
import sys
import time
import json
import base64
import argparse
from pathlib import Path

# -- SDK import ----------------------------------------------------------------
try:
    import runwayml
    from runwayml import RunwayML
except ImportError:
    print("runwayml SDK not installed. Run: pip install runwayml>=3.0.0")
    sys.exit(1)

# -- Config --------------------------------------------------------------------
API_KEY   = os.environ.get("RUNWAYML_API_SECRET", "")
MODEL_T2V = "gen4_turbo"          # Gen-4.5 text-to-video (turbo = fast)
MODEL_I2V = "gen4_turbo"          # Gen-4.5 image-to-video (same model ID)
POLL_INTERVAL = 5                  # seconds between status polls
MAX_WAIT  = 600                    # 10 min hard timeout

# Default generation params (digital-stud character workflow optimised)
DEFAULTS = {
    "ratio":        "1280:720",    # 16:9 landscape -- change to "720:1280" for 9:16 portrait
    "duration":     5,             # 5 or 10
}

OUTPUT_DIR = Path("output/runway_gen45")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def get_client() -> RunwayML:
    if not API_KEY:
        raise EnvironmentError(
            "RUNWAYML_API_SECRET not set. Export it or pass via env."
        )
    return RunwayML(api_key=API_KEY)


def image_to_data_uri(image_path: str) -> str:
    """Read local image file and encode as base64 data URI."""
    p = Path(image_path)
    if not p.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")
    suffix = p.suffix.lower().lstrip(".")
    mime = {
        "jpg": "image/jpeg", "jpeg": "image/jpeg",
        "png": "image/png", "webp": "image/webp",
    }.get(suffix, "image/png")
    b64 = base64.b64encode(p.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{b64}"


def poll_task(client: RunwayML, task_id: str, label: str = "") -> dict:
    """Poll a task until completion or failure. Returns final task object."""
    print(f"  Polling task {task_id}{f' ({label})' if label else ''} ...")
    deadline = time.time() + MAX_WAIT
    while time.time() < deadline:
        task = client.tasks.retrieve(task_id)
        status = task.status
        progress = getattr(task, "progress", None)
        prog_str = f" {int(progress*100)}%" if progress is not None else ""
        print(f"    status={status}{prog_str}")
        if status == "SUCCEEDED":
            return task
        if status in ("FAILED", "CANCELLED", "THROTTLED"):
            err = getattr(task, "failure", None) or getattr(task, "failureCode", status)
            raise RuntimeError(f"Task {task_id} {status}: {err}")
        time.sleep(POLL_INTERVAL)
    raise TimeoutError(f"Task {task_id} did not complete within {MAX_WAIT}s")


def run_t2v(client: RunwayML, prompt: str, ratio: str, duration: int) -> str:
    """Text-to-video generation. Returns output video URL."""
    print(f"\n[T2V] Gen-4.5 | {ratio} | {duration}s")
    print(f"  prompt: {prompt[:120]}")
    task = client.image_to_video.create(
        model=MODEL_T2V,
        prompt_text=prompt,
        ratio=ratio,
        duration=duration,
    )
    result = poll_task(client, task.id, label="t2v")
    url = result.output[0] if result.output else None
    if not url:
        raise RuntimeError("No output URL in succeeded task")
    print(f"  OK Output URL: {url}")
    return url


def run_i2v(client: RunwayML, prompt: str, image_path: str, ratio: str, duration: int) -> str:
    """Image-to-video generation. Returns output video URL."""
    print(f"\n[I2V] Gen-4.5 | {ratio} | {duration}s")
    print(f"  image: {image_path}")
    print(f"  prompt: {prompt[:120]}")

    prompt_image = image_to_data_uri(image_path)

    task = client.image_to_video.create(
        model=MODEL_I2V,
        prompt_image=prompt_image,
        prompt_text=prompt,
        ratio=ratio,
        duration=duration,
    )
    result = poll_task(client, task.id, label="i2v")
    url = result.output[0] if result.output else None
    if not url:
        raise RuntimeError("No output URL in succeeded task")
    print(f"  OK Output URL: {url}")
    return url


def download_video(url: str, filename: str) -> Path:
    """Download video from Runway CDN to local output dir."""
    import urllib.request
    out_path = OUTPUT_DIR / filename
    print(f"  Downloading -> {out_path} ...")
    urllib.request.urlretrieve(url, out_path)
    size_mb = out_path.stat().st_size / 1024 / 1024
    print(f"  Saved: {out_path} ({size_mb:.1f} MB)")
    return out_path


def run_connectivity_test(client: RunwayML):
    """Lightweight connectivity / auth check -- no generation credits used."""
    print("\n[TEST] Connectivity check (organisation info) ...")
    try:
        org = client.organizations.retrieve()
        print(f"  OK Connected -- org: {org.name if hasattr(org, 'name') else org}")
    except Exception as e:
        print(f"  FAIL Connection failed: {e}")
        sys.exit(1)


# -- Digital-Stud character video presets --------------------------------------
PRESETS = {
    "char_intro": {
        "mode": "i2v",
        "prompt": (
            "cinematic slow push-in, character walks forward with confident stride, "
            "studio lighting with soft rim light, shallow depth of field, "
            "locked horizon, professional color grade"
        ),
        "duration": 5,
        "ratio": "720:1280",      # portrait for social
    },
    "bg_reveal": {
        "mode": "t2v",
        "prompt": (
            "aerial crane shot revealing a futuristic city at golden hour, "
            "dramatic volumetric light rays, photorealistic, cinematic 4K"
        ),
        "duration": 10,
        "ratio": "1280:720",
    },
    "product_orbit": {
        "mode": "i2v",
        "prompt": (
            "smooth 360 orbit around subject, even studio lighting, "
            "clean white background, professional product video style"
        ),
        "duration": 5,
        "ratio": "1:1",
    },
}


def run_preset(client: RunwayML, preset_name: str, image_path: str = None) -> str:
    p = PRESETS.get(preset_name)
    if not p:
        raise ValueError(f"Unknown preset '{preset_name}'. Available: {list(PRESETS)}")
    mode     = p["mode"]
    prompt   = p["prompt"]
    ratio    = p.get("ratio", DEFAULTS["ratio"])
    duration = p.get("duration", DEFAULTS["duration"])

    if mode == "t2v":
        url = run_t2v(client, prompt, ratio, duration)
    else:
        if not image_path:
            raise ValueError(f"Preset '{preset_name}' requires --image_path")
        url = run_i2v(client, prompt, image_path, ratio, duration)

    ts  = time.strftime("%Y%m%d_%H%M%S")
    out = download_video(url, f"{preset_name}_{ts}.mp4")
    return str(out)


# -- CLI -----------------------------------------------------------------------
def parse_args():
    p = argparse.ArgumentParser(
        description="Runway Gen-4.5 API test -- digital-stud workflow"
    )
    p.add_argument("--mode", choices=["t2v", "i2v", "preset", "test"],
                   default="test", help="Operation mode")
    p.add_argument("--prompt", default="", help="Text prompt (t2v / i2v)")
    p.add_argument("--image_path", default="", help="Source image for I2V")
    p.add_argument("--ratio", default=DEFAULTS["ratio"],
                   help="Aspect ratio, e.g. 1280:720 / 720:1280 / 1:1")
    p.add_argument("--duration", type=int, default=DEFAULTS["duration"],
                   choices=[5, 10], help="Clip duration in seconds")
    p.add_argument("--preset", default="char_intro",
                   help=f"Named preset: {list(PRESETS)}")
    p.add_argument("--download", action="store_true",
                   help="Download output video locally after generation")
    return p.parse_args()


def main():
    args = parse_args()
    client = get_client()

    if args.mode == "test":
        run_connectivity_test(client)
        print("\nOK Runway Gen-4.5 API connectivity OK")
        print(f"   SDK version : {runwayml.__version__}")
        print(f"   Model T2V   : {MODEL_T2V}")
        print(f"   Model I2V   : {MODEL_I2V}")
        print(f"   Output dir  : {OUTPUT_DIR.resolve()}")
        print("\nAvailable presets:")
        for name, cfg in PRESETS.items():
            print(f"  {name:18s}  mode={cfg['mode']}  {cfg['ratio']}  {cfg['duration']}s")
        print("\nQuick start:")
        print("  # I2V from a render:")
        print("  python api_test_runway_gen45.py \\")
        print("      --mode i2v \\")
        print("      --image_path renders/hero_frame.png \\")
        print('      --prompt "slow push-in, character smiles" \\')
        print("      --ratio 720:1280 --duration 5 --download")
        print()
        print("  # T2V background:")
        print("  python api_test_runway_gen45.py \\")
        print("      --mode t2v \\")
        print('      --prompt "cinematic aerial city, golden hour" \\')
        print("      --ratio 1280:720 --duration 10 --download")
        print()
        print("  # Named preset (i2v):")
        print("  python api_test_runway_gen45.py \\")
        print("      --mode preset --preset char_intro \\")
        print("      --image_path renders/hero_frame.png --download")
        return

    if args.mode == "preset":
        out = run_preset(client, args.preset, args.image_path or None)
        print(f"\nOK Preset '{args.preset}' complete -> {out}")
        return

    if args.mode == "t2v":
        if not args.prompt:
            print("ERROR: --prompt required for t2v mode"); sys.exit(1)
        url = run_t2v(client, args.prompt, args.ratio, args.duration)
        if args.download:
            ts = time.strftime("%Y%m%d_%H%M%S")
            download_video(url, f"t2v_{ts}.mp4")
        else:
            print(f"\n  Video URL: {url}")
        return

    if args.mode == "i2v":
        if not args.prompt:
            print("ERROR: --prompt required for i2v mode"); sys.exit(1)
        if not args.image_path:
            print("ERROR: --image_path required for i2v mode"); sys.exit(1)
        url = run_i2v(client, args.prompt, args.image_path, args.ratio, args.duration)
        if args.download:
            ts = time.strftime("%Y%m%d_%H%M%S")
            download_video(url, f"i2v_{ts}.mp4")
        else:
            print(f"\n  Video URL: {url}")
        return


if __name__ == "__main__":
    main()


# -- Integration notes ---------------------------------------------------------
# Runway Gen-4.5 in the digital-stud pipeline:
#
#   Blender render (PNG)
#     ->  api_test_runway_gen45.py --mode i2v --preset char_intro
#          ->  5s portrait video (720:1280) for social
#               ->  kling_3.0 extend to 15s (api_test_fal.py preset=kling_extend)
#                    ->  LTX-2.3 audio sync + upscale (ComfyUI ltx23_flf2v.json)
#
# Pricing (Jan 2026):
#   Gen-4.5 standard: $0.05 / credit
#   5s  clip = 50 credits  approx $2.50
#   10s clip = 100 credits approx $5.00
#   Run test mode first -- no credits consumed.
#
# Rate limits: 3 concurrent tasks (standard tier)
# Adobe Firefly integration: use Firefly API image_gen -> pass as prompt_image
#
# Key refs:
#   https://docs.dev.runwayml.com/
#   https://www.artificialanalysis.ai/text-to-video  (Elo leaderboard)
#   https://runwayml.com/research/introducing-runway-gen-4.5

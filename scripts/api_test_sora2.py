#!/usr/bin/env python3
"""
api_test_sora2.py — Digital-Stud 3D+AI Workflow
OpenAI Sora 2 / Sora 2 Pro API integration test
Models: sora-2  |  sora-2-pro
API docs: https://platform.openai.com/docs/api-reference/video
Context: run 171 | 2026-03-15 | mroncka/digital-stud-3d-ai-workflow

Capabilities (Sora 2 / Sora 2 Pro):
  - Text-to-video (T2V) and image-to-video (I2V)
  - Resolution: up to 1920x1080 (sora-2-pro: native 4K via upscale)
  - Duration: 5–20 s (sora-2), 5–60 s (sora-2-pro)
  - FPS: 24 fps
  - Storyboard / multi-shot: sora-2-pro only (up to 6 shots)
  - Audio-visual sync: sora-2-pro only (ambient audio generation)
  - Aspect ratios: 16:9, 9:16, 1:1, 4:3, 3:4, 21:9
  - Style presets: photorealistic, cinematic, anime, 3d_render, claymation
  - Pricing (March 2026):
      sora-2:      $0.06 / video-second  (720p)
                   $0.10 / video-second  (1080p)
      sora-2-pro:  $0.18 / video-second  (1080p)
                   $0.30 / video-second  (4K/upscaled)
  - Free trial: $5 credit on new API accounts (~83 s of sora-2 720p)

Digital-Stud use cases:
  - 3D character turntable animation → sora-2 I2V (5 s, 1080p)
  - Cinematic B-roll for portfolio → sora-2-pro T2V (10-20 s, 16:9)
  - Stylised product loops (10 s, 1:1) → sora-2 (cinematic preset)
  - Blender render + Sora 2 Pro relighting → I2V with style preset
"""

import os
import time
import json
import base64
import argparse
from pathlib import Path
from openai import OpenAI

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
API_KEY = os.environ.get("OPENAI_API_KEY", "")
if not API_KEY:
    raise EnvironmentError(
        "OPENAI_API_KEY not set. "
        "Export it before running: export OPENAI_API_KEY=sk-..."
    )

client = OpenAI(api_key=API_KEY)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
MODEL_STANDARD = "sora-2"
MODEL_PRO       = "sora-2-pro"

# Aspect ratio → (width, height) for 1080p
RES_MAP = {
    "16:9": (1920, 1080),
    "9:16": (1080, 1920),
    "1:1":  (1080, 1080),
    "4:3":  (1440, 1080),
    "3:4":  (1080, 1440),
    "21:9": (2560, 1080),
}

STYLE_PRESETS = [
    "photorealistic",
    "cinematic",
    "anime",
    "3d_render",
    "claymation",
]

# ---------------------------------------------------------------------------
# Helper: poll job until done
# ---------------------------------------------------------------------------
def poll_video_job(
    job_id: str,
    poll_interval: float = 5.0,
    timeout: float = 600.0,
    verbose: bool = True,
) -> dict:
    """Poll an async Sora 2 video generation job until complete or timeout."""
    elapsed = 0.0
    while elapsed < timeout:
        job = client.video.jobs.retrieve(job_id)
        status = job.status  # pending | processing | succeeded | failed
        if verbose:
            print(f"  [{elapsed:5.0f}s] job={job_id[:12]}… status={status}")
        if status == "succeeded":
            return {"status": "succeeded", "job": job}
        if status == "failed":
            err = getattr(job, "error", {}) or {}
            return {"status": "failed", "error": err}
        time.sleep(poll_interval)
        elapsed += poll_interval
    return {"status": "timeout", "job_id": job_id}


# ---------------------------------------------------------------------------
# Helper: download + save video
# ---------------------------------------------------------------------------
def save_video(job, out_path: Path) -> Path:
    """Download video bytes from a succeeded job and write to out_path."""
    # Sora 2 API returns video_url (signed, 1 h TTL) or inline base64
    video_url = getattr(job, "video_url", None)
    b64_data   = getattr(job, "video_b64", None)

    if video_url:
        import urllib.request
        out_path.parent.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(video_url, out_path)
    elif b64_data:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_bytes(base64.b64decode(b64_data))
    else:
        raise ValueError("No video_url or video_b64 in succeeded job response")

    print(f"  Saved → {out_path} ({out_path.stat().st_size / 1024:.1f} KB)")
    return out_path


# ---------------------------------------------------------------------------
# Test 1 — Text-to-Video (T2V), sora-2, 5 s, 16:9, cinematic
# ---------------------------------------------------------------------------
def test_t2v_standard(
    prompt: str = (
        "A 3D rendered character walks through a neon-lit Tokyo alley at night. "
        "Camera follows at shoulder height, cinematic depth of field, rain on "
        "reflective pavement, 24fps film grain."
    ),
    duration: int = 5,
    aspect: str = "16:9",
    style: str = "cinematic",
    resolution: str = "1080p",
    out_dir: str = "./output/sora2_test",
    dry_run: bool = False,
) -> dict:
    """Run a T2V test with sora-2 (standard tier)."""
    print("\n── Test 1: T2V sora-2 (standard) ──")
    print(f"  prompt   : {prompt[:80]}…")
    print(f"  duration : {duration}s | aspect: {aspect} | style: {style} | res: {resolution}")

    if dry_run:
        print("  [DRY RUN] skipping API call")
        return {"dry_run": True}

    w, h = RES_MAP.get(aspect, (1920, 1080))
    # Scale to 720p if resolution flag is 720p
    if resolution == "720p":
        w, h = w * 720 // 1080, 720

    job = client.video.generate(
        model=MODEL_STANDARD,
        prompt=prompt,
        duration=duration,
        width=w,
        height=h,
        style=style,
        fps=24,
    )
    print(f"  Job created: {job.id}")
    result = poll_video_job(job.id)

    if result["status"] == "succeeded":
        out_path = Path(out_dir) / f"sora2_t2v_{aspect.replace(':','x')}_{duration}s.mp4"
        save_video(result["job"], out_path)
        return {"status": "ok", "output": str(out_path), "job_id": job.id}
    else:
        print(f"  FAILED: {result}")
        return {"status": "error", "detail": result}


# ---------------------------------------------------------------------------
# Test 2 — Image-to-Video (I2V), sora-2, 5 s, 1:1, 3d_render
#           Typical use: Blender character render → animated loop
# ---------------------------------------------------------------------------
def test_i2v_standard(
    image_path: str = "./assets/character_turntable_frame.png",
    prompt: str = (
        "The 3D character slowly rotates 360 degrees on a neutral studio background. "
        "Soft rim lighting, 24fps, seamless loop."
    ),
    duration: int = 5,
    aspect: str = "1:1",
    style: str = "3d_render",
    out_dir: str = "./output/sora2_test",
    dry_run: bool = False,
) -> dict:
    """Run an I2V test with sora-2 using a reference image."""
    print("\n── Test 2: I2V sora-2 (standard) ──")
    img = Path(image_path)
    if not img.exists():
        print(f"  [SKIP] image not found: {image_path}")
        return {"status": "skipped", "reason": f"image not found: {image_path}"}

    print(f"  image    : {image_path}")
    print(f"  prompt   : {prompt[:80]}…")
    print(f"  duration : {duration}s | aspect: {aspect} | style: {style}")

    if dry_run:
        print("  [DRY RUN] skipping API call")
        return {"dry_run": True}

    w, h = RES_MAP.get(aspect, (1080, 1080))

    with open(image_path, "rb") as f:
        job = client.video.generate(
            model=MODEL_STANDARD,
            prompt=prompt,
            image=f,  # reference image (first frame)
            duration=duration,
            width=w,
            height=h,
            style=style,
            fps=24,
        )

    print(f"  Job created: {job.id}")
    result = poll_video_job(job.id)

    if result["status"] == "succeeded":
        out_path = Path(out_dir) / f"sora2_i2v_{aspect.replace(':','x')}_{duration}s.mp4"
        save_video(result["job"], out_path)
        return {"status": "ok", "output": str(out_path), "job_id": job.id}
    else:
        print(f"  FAILED: {result}")
        return {"status": "error", "detail": result}


# ---------------------------------------------------------------------------
# Test 3 — T2V Pro, 20 s, storyboard, cinematic, 16:9 — sora-2-pro
#           Cinematic B-roll for portfolio use
# ---------------------------------------------------------------------------
def test_t2v_pro(
    shots: list[str] | None = None,
    duration: int = 20,
    aspect: str = "16:9",
    style: str = "cinematic",
    out_dir: str = "./output/sora2_test",
    dry_run: bool = False,
) -> dict:
    """Run a multi-shot T2V test with sora-2-pro (storyboard mode)."""
    if shots is None:
        shots = [
            "Extreme wide: a futuristic Czech city skyline at golden hour, Stodůlky district, "
            "glass towers reflecting sunset, slow cinematic push-in.",
            "Mid shot: a fashion-forward character walks down a cobblestone street, "
            "practical LED signage in Czech, motion blur on background crowd.",
            "Close-up: hands typing on a holographic keyboard, cyan light glow, "
            "bokeh background of city lights, 24fps.",
        ]

    print("\n── Test 3: T2V sora-2-pro (multi-shot storyboard) ──")
    print(f"  shots    : {len(shots)}")
    print(f"  duration : {duration}s total | aspect: {aspect} | style: {style}")

    if dry_run:
        print("  [DRY RUN] skipping API call")
        return {"dry_run": True}

    w, h = RES_MAP.get(aspect, (1920, 1080))

    job = client.video.generate(
        model=MODEL_PRO,
        storyboard=shots,   # multi-shot: list of prompt strings per shot
        duration=duration,
        width=w,
        height=h,
        style=style,
        fps=24,
        generate_audio=True,  # ambient audio synthesis (sora-2-pro only)
    )

    print(f"  Job created: {job.id}")
    result = poll_video_job(job.id, poll_interval=10.0, timeout=900.0)

    if result["status"] == "succeeded":
        out_path = Path(out_dir) / f"sora2pro_storyboard_{len(shots)}shots_{duration}s.mp4"
        save_video(result["job"], out_path)
        return {"status": "ok", "output": str(out_path), "job_id": job.id}
    else:
        print(f"  FAILED: {result}")
        return {"status": "error", "detail": result}


# ---------------------------------------------------------------------------
# Test 4 — List models + capabilities introspection
# ---------------------------------------------------------------------------
def test_list_models() -> dict:
    """Retrieve and display Sora model capabilities from the API."""
    print("\n── Test 4: List Sora video models ──")
    try:
        models = client.models.list()
        sora_models = [m for m in models.data if "sora" in m.id.lower()]
        print(f"  Found {len(sora_models)} Sora model(s):")
        for m in sora_models:
            print(f"    {m.id:30s}  created={m.created}")
        return {"status": "ok", "models": [m.id for m in sora_models]}
    except Exception as exc:
        print(f"  ERROR: {exc}")
        return {"status": "error", "detail": str(exc)}


# ---------------------------------------------------------------------------
# Test 5 — Cost estimator (no API call)
# ---------------------------------------------------------------------------
PRICING = {
    "sora-2": {
        "720p":  0.06,
        "1080p": 0.10,
    },
    "sora-2-pro": {
        "1080p": 0.18,
        "4k":    0.30,
    },
}

def estimate_cost(
    model: str = "sora-2",
    resolution: str = "1080p",
    duration: int = 10,
    count: int = 1,
) -> dict:
    """Estimate generation cost for a batch of videos."""
    tier = PRICING.get(model, {})
    rate = tier.get(resolution)
    if rate is None:
        return {"status": "error", "detail": f"Unknown model/resolution: {model} {resolution}"}
    total = rate * duration * count
    print(f"  {count}x {model} {resolution} {duration}s → ${total:.4f} "
          f"(${rate}/s × {duration}s × {count} videos)")
    return {"model": model, "resolution": resolution, "duration": duration,
            "count": count, "rate_per_second": rate, "total_usd": round(total, 4)}


# ---------------------------------------------------------------------------
# CLI entrypoint
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Sora 2 API integration tests for Digital-Stud 3D+AI workflow"
    )
    parser.add_argument("--dry-run",    action="store_true",  help="Skip actual API calls")
    parser.add_argument("--test",       type=int, default=0,   help="Run specific test (1-5, 0=all)")
    parser.add_argument("--model",      default=MODEL_STANDARD, choices=[MODEL_STANDARD, MODEL_PRO])
    parser.add_argument("--duration",   type=int, default=5)
    parser.add_argument("--aspect",     default="16:9",         choices=list(RES_MAP.keys()))
    parser.add_argument("--style",      default="cinematic",    choices=STYLE_PRESETS)
    parser.add_argument("--resolution", default="1080p",        choices=["720p", "1080p", "4k"])
    parser.add_argument("--image",      default="./assets/character_turntable_frame.png")
    parser.add_argument("--out-dir",    default="./output/sora2_test")
    parser.add_argument("--count",      type=int, default=1,   help="Batch count for cost estimate")
    args = parser.parse_args()

    results = {}

    if args.test in (0, 4):
        results["test4_list_models"] = test_list_models()

    if args.test in (0, 5):
        print("\n── Test 5: Cost estimator ──")
        results["cost_sora2_5s_720p"]        = estimate_cost("sora-2",     "720p",  5,  1)
        results["cost_sora2_10s_1080p"]      = estimate_cost("sora-2",     "1080p", 10, 1)
        results["cost_sora2pro_20s_1080p"]   = estimate_cost("sora-2-pro", "1080p", 20, 1)
        results["cost_sora2pro_20s_4k"]      = estimate_cost("sora-2-pro", "4k",    20, 1)
        results["cost_batch_10x_sora2_5s"]   = estimate_cost("sora-2",     "720p",  5,  args.count)

    if args.test in (0, 1):
        results["test1_t2v_standard"] = test_t2v_standard(
            duration=args.duration,
            aspect=args.aspect,
            style=args.style,
            resolution=args.resolution,
            out_dir=args.out_dir,
            dry_run=args.dry_run,
        )

    if args.test in (0, 2):
        results["test2_i2v_standard"] = test_i2v_standard(
            image_path=args.image,
            duration=args.duration,
            aspect=args.aspect,
            style=args.style,
            out_dir=args.out_dir,
            dry_run=args.dry_run,
        )

    if args.test in (0, 3):
        results["test3_t2v_pro"] = test_t2v_pro(
            duration=args.duration,
            aspect=args.aspect,
            style=args.style,
            out_dir=args.out_dir,
            dry_run=args.dry_run,
        )

    print("\n── Summary ──")
    print(json.dumps(results, indent=2, default=str))
    return results


if __name__ == "__main__":
    main()


# ---------------------------------------------------------------------------
# Quick usage reference
# ---------------------------------------------------------------------------
# Dry run (no API cost):
#   python api_test_sora2.py --dry-run
#
# Cost estimate only:
#   python api_test_sora2.py --test 5 --count 10
#
# List available Sora models:
#   python api_test_sora2.py --test 4
#
# Single T2V test (720p, 5s, cheap):
#   python api_test_sora2.py --test 1 --duration 5 --resolution 720p --dry-run
#
# I2V from Blender render:
#   python api_test_sora2.py --test 2 --image ./render/character_01.png --aspect 1:1
#
# Pro multi-shot portfolio B-roll (20s):
#   python api_test_sora2.py --test 3 --model sora-2-pro --duration 20
#
# Requirements:
#   pip install openai>=1.30.0
#   export OPENAI_API_KEY=sk-...

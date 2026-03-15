#!/usr/bin/env python3
"""
api_test_veo31.py
=================
Digital-Stud production test harness for Google Veo 3.1 (and veo-3.1-fast)
via the Gemini Developer API (google-genai SDK).

Models confirmed:
  - veo-3.1          : released Oct 2025, significantly updated Jan 13 2026
  - veo-3.1-fast     : lower latency, same API surface
  - veo-3.0          : older baseline (kept for A/B comparison)

API reference:
  https://ai.google.dev/api/generate-content#v1beta.models.generateVideo
  https://ai.google.dev/gemini-api/docs/video

Cloudflare Workers AI note (from run 166):
  CF Workers AI does NOT yet expose Veo 3.1 (it's Google-exclusive via Gemini API).
  Use Gemini API key path only.

Usage:
  export GEMINI_API_KEY="your-key-here"
  python api_test_veo31.py                   # text-to-video (default)
  python api_test_veo31.py --mode i2v        # image-to-video
  python api_test_veo31.py --model veo-3.1-fast --prompt "product shot"
  python api_test_veo31.py --help
"""

import os, sys, time, argparse, pathlib
from typing import Optional

# ── Optional: rich progress if available ────────────────────────────────────
try:
    from rich.console import Console
    from rich.progress import Progress, SpinnerColumn, TextColumn
    RICH = True
    console = Console()
except ImportError:
    RICH = False
    class _Console:
        def print(self, *a, **kw): print(*a)
        def log(self, *a, **kw): print(*a)
    console = _Console()

# ── Defaults ────────────────────────────────────────────────────────────────

DEFAULT_MODEL   = "veo-3.1"
DEFAULT_PROMPT  = (
    "A premium skincare bottle sits on a white marble surface. "
    "Soft natural window light rakes across the product. "
    "Ultra-shallow depth of field. Cinematic. 4K."
)
DEFAULT_DURATION = 8          # seconds (Veo 3.1 supports 5–30s)
DEFAULT_ASPECT   = "16:9"     # or "9:16" (portrait)
DEFAULT_FPS      = 24
DEFAULT_OUTDIR   = "./output"

POLL_INTERVAL = 5             # seconds between status checks
MAX_WAIT      = 600           # 10-minute timeout

SUPPORTED_MODELS = ["veo-3.1", "veo-3.1-fast", "veo-3.0"]

# ── CLI ─────────────────────────────────────────────────────────────────────

def parse_args():
    p = argparse.ArgumentParser(
        description="Veo 3.1 API test — Digital-Stud pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--model",    default=DEFAULT_MODEL,  choices=SUPPORTED_MODELS)
    p.add_argument("--prompt",   default=DEFAULT_PROMPT)
    p.add_argument("--mode",     default="t2v", choices=["t2v", "i2v"],
                   help="t2v = text-to-video, i2v = image-to-video")
    p.add_argument("--image",    default=None,
                   help="Path to reference image (required for --mode i2v)")
    p.add_argument("--duration", type=int,   default=DEFAULT_DURATION,
                   help="Video length in seconds (5–30)")
    p.add_argument("--aspect",   default=DEFAULT_ASPECT, choices=["16:9", "9:16"])
    p.add_argument("--fps",      type=int,   default=DEFAULT_FPS,
                   help="Frames per second (24 or 30)")
    p.add_argument("--outdir",   default=DEFAULT_OUTDIR)
    p.add_argument("--dry-run",  action="store_true",
                   help="Print request payload without calling API")
    return p.parse_args()


# ── Helpers ─────────────────────────────────────────────────────────────────

def get_api_key() -> str:
    key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not key:
        console.print("[red]ERROR:[/red] GEMINI_API_KEY not set." if RICH else
                      "ERROR: GEMINI_API_KEY not set.")
        sys.exit(1)
    return key


def load_image_b64(path: str) -> str:
    """Read image file and return base64-encoded string."""
    data = pathlib.Path(path).read_bytes()
    return base64.b64encode(data).decode("utf-8")


def detect_mime(path: str) -> str:
    ext = pathlib.Path(path).suffix.lower()
    return {".jpg": "image/jpeg", ".jpeg": "image/jpeg",
            ".png": "image/png",  ".webp": "image/webp"}.get(ext, "image/jpeg")


# ── Core API calls ───────────────────────────────────────────────────────────

BASE_URL = "https://generativelanguage.googleapis.com/v1beta"


def submit_generation(api_key: str, model: str, payload: dict) -> str:
    """Submit a video generation job. Returns operation name."""
    url = f"{BASE_URL}/models/{model}:predictLongRunning"
    headers = {"Content-Type": "application/json", "x-goog-api-key": api_key}
    r = requests.post(url, json=payload, headers=headers, timeout=30)
    r.raise_for_status()
    data = r.json()
    op_name = data.get("name")
    if not op_name:
        raise RuntimeError(f"No operation name in response: {data}")
    console.print(f"  Operation: {op_name}")
    return op_name


def poll_operation(api_key: str, op_name: str) -> dict:
    """Poll until done. Returns the completed operation dict."""
    url = f"{BASE_URL}/{op_name}"
    headers = {"x-goog-api-key": api_key}
    elapsed = 0
    while elapsed < MAX_WAIT:
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()
        op = r.json()
        if op.get("done"):
            return op
        elapsed += POLL_INTERVAL
        console.log(f"  Waiting… {elapsed}s elapsed")
        time.sleep(POLL_INTERVAL)
    raise TimeoutError(f"Generation exceeded {MAX_WAIT}s timeout.")


def download_video(api_key: str, video_uri: str, outpath: pathlib.Path) -> None:
    """Download generated video bytes to outpath."""
    headers = {"x-goog-api-key": api_key}
    r = requests.get(video_uri, headers=headers, stream=True, timeout=60)
    r.raise_for_status()
    outpath.parent.mkdir(parents=True, exist_ok=True)
    with open(outpath, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
    console.print(f"  Saved → {outpath}  ({outpath.stat().st_size / 1024:.1f} KB)")


# ── Build request payload ───────────────────────────────────────────────────

def build_payload_t2v(args) -> dict:
    return {
        "instances": [{
            "prompt": args.prompt
        }],
        "parameters": {
            "durationSeconds":  args.duration,
            "aspectRatio":      args.aspect,
            "fps":              args.fps,
            "personGeneration": "dont_allow",   # safe default for product shots
            "enhance_prompt":   True,            # Veo 3.1 prompt enhancement
            "number_of_videos": 1,
            "output_gcs_uri":   None,            # inline response (no GCS bucket needed)
        }
    }


def build_payload_i2v(args) -> dict:
    if not args.image:
        console.print("ERROR: --image is required for i2v mode." if not RICH else
                      "[red]ERROR:[/red] --image is required for --mode i2v")
        sys.exit(1)
    image_b64 = load_image_b64(args.image)
    mime      = detect_mime(args.image)
    return {
        "instances": [{
            "prompt": args.prompt,
            "image":  {"bytesBase64Encoded": image_b64, "mimeType": mime}
        }],
        "parameters": {
            "durationSeconds":  args.duration,
            "aspectRatio":      args.aspect,
            "fps":              args.fps,
            "personGeneration": "dont_allow",
            "number_of_videos": 1,
        }
    }


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    args = parse_args()
    api_key = get_api_key()

    # Build payload
    payload = build_payload_i2v(args) if args.mode == "i2v" else build_payload_t2v(args)

    console.print(f"\n{'='*60}")
    console.print(f"  Veo 3.1 API Test — Digital-Stud Pipeline")
    console.print(f"{'='*60}")
    console.print(f"  Model   : {args.model}")
    console.print(f"  Mode    : {args.mode.upper()}")
    console.print(f"  Prompt  : {args.prompt[:80]}{'…' if len(args.prompt) > 80 else ''}")
    console.print(f"  Duration: {args.duration}s  Aspect: {args.aspect}  FPS: {args.fps}")
    console.print(f"{'='*60}\n")

    if args.dry_run:
        console.print("DRY RUN — payload:")
        console.print(json.dumps(payload, indent=2, default=str))
        return

    # Submit
    console.print("Submitting generation request…")
    t0 = time.time()
    op_name = submit_generation(api_key, args.model, payload)

    # Poll
    console.print("Polling for completion…")
    op = poll_operation(api_key, op_name)

    # Handle error
    if "error" in op:
        err = op["error"]
        console.print(f"[red]Generation failed:[/red] {err.get('message', err)}" if RICH
                      else f"Generation failed: {err.get('message', err)}")
        sys.exit(1)

    # Extract video URI(s)
    response  = op.get("response", {})
    videos    = response.get("videos", [response.get("video", {})])
    elapsed   = time.time() - t0

    console.print(f"\n✅ Done in {elapsed:.1f}s — {len(videos)} video(s) generated")

    # Download
    outdir = pathlib.Path(args.outdir)
    for idx, vid in enumerate(videos):
        uri = vid.get("uri") or vid.get("gcsUri") or vid.get("bytesBase64Encoded")
        if not uri:
            console.print(f"  WARNING: No URI in video[{idx}]: {vid.keys()}")
            continue
        ts_str = time.strftime("%Y%m%d_%H%M%S")
        fname  = f"veo31_{args.mode}_{ts_str}_{idx}.mp4"
        outpath = outdir / fname

        if uri.startswith("http"):
            download_video(api_key, uri, outpath)
        elif uri.startswith("gs://"):
            # GCS path — requires gcloud auth, not handled here
            console.print(f"  GCS output (download manually): {uri}")
            console.print(f"  Command: gsutil cp {uri} {outpath}")
        else:
            # Inline base64
            outpath.parent.mkdir(parents=True, exist_ok=True)
            outpath.write_bytes(base64.b64decode(uri))
            console.print(f"  Saved (inline b64) → {outpath}  ({outpath.stat().st_size / 1024:.1f} KB)")

    # Summary JSON
    summary = {
        "run_at":       time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "model":        args.model,
        "mode":         args.mode,
        "prompt":       args.prompt,
        "duration_s":   args.duration,
        "aspect":       args.aspect,
        "fps":          args.fps,
        "elapsed_s":    round(elapsed, 1),
        "operation":    op_name,
        "videos_count": len(videos),
    }
    summary_path = outdir / f"veo31_summary_{time.strftime('%Y%m%d_%H%M%S')}.json"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(summary, indent=2))
    console.print(f"  Summary → {summary_path}")


if __name__ == "__main__":
    main()


# ── Quick sanity-check (no API call) ─────────────────────────────────────────
# python api_test_veo31.py --dry-run
#
# Expected payload preview:
#   {
#     "instances": [{"prompt": "A premium skincare bottle ..."}],
#     "parameters": {
#       "durationSeconds": 8, "aspectRatio": "16:9", "fps": 24,
#       "personGeneration": "dont_allow", "enhance_prompt": true,
#       "number_of_videos": 1, "output_gcs_uri": null
#     }
#   }
#
# Cost reference (Veo 3.1, Jan 2026):
#   veo-3.1      : ~$0.035 / second of video
#   veo-3.1-fast : ~$0.012 / second of video
#   8s clip      : $0.28 (standard) / $0.10 (fast)
#
# Free tier: Google AI Studio — 10 video generations/day (limited resolution)
# Paid tier: requires billing enabled on GCP project

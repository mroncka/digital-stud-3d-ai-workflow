"""
api_test_seedance.py
─────────────────────────────────────────────────────────────────────────────
Digital-Stud 3D+AI Workflow — Seedance 2.0 API test script
Generated: 2026-03-13  run #58

Seedance 2.0 (ByteDance) — March 2026 SOTA video model
  • Multi-shot single-pass generation
  • Quad-modal input: text + image + video + audio
  • Native lip-sync in 8+ languages
  • 2K cinema resolution
  • API access via: Replicate, fal.ai, ByteDance API (beta)

This script tests image-to-video generation via Replicate and fal.ai,
and optionally the ByteDance direct API if a key is available.
─────────────────────────────────────────────────────────────────────────────
"""

import os, sys, time, json, base64, urllib.request, urllib.error
from pathlib import Path
from typing import Optional

REPLICATE_API_TOKEN      = os.environ.get("REPLICATE_API_TOKEN", "")
FAL_API_KEY              = os.environ.get("FAL_KEY", "")
BYTEDANCE_API_KEY        = os.environ.get("BYTEDANCE_SEEDANCE_API_KEY", "")
REPLICATE_SEEDANCE_MODEL = "bytedance/seedance-2-0"
FAL_SEEDANCE_ENDPOINT    = "fal-ai/seedance-2-0"
TEST_IMAGE_URL  = "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=512"
TEST_PROMPT     = "A young woman with dark hair walks confidently forward, cinematic lighting, 4K, photorealistic, smooth motion"
TEST_DURATION   = 5
TEST_RESOLUTION = "1280x720"
OUTPUT_DIR = Path("output/seedance_tests")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def _post_json(url, payload, headers):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={**headers, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP {e.code}: {e.read().decode('utf-8','replace')}") from e

def _get_json(url, headers):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))

def _download(url, dest):
    urllib.request.urlretrieve(url, dest)
    print(f"  ↓ Saved: {dest}")

def test_replicate_seedance(image_url, prompt):
    if not REPLICATE_API_TOKEN:
        print("[Replicate] REPLICATE_API_TOKEN not set — skipping"); return None
    print("\n[Replicate] Submitting Seedance 2.0 prediction...")
    headers = {"Authorization": f"Bearer {REPLICATE_API_TOKEN}"}
    image_input = image_url if image_url.startswith("http") else f"data:image/jpeg;base64,{base64.b64encode(Path(image_url).read_bytes()).decode()}"
    payload = {"version": REPLICATE_SEEDANCE_MODEL, "input": {"image": image_input, "prompt": prompt, "duration": TEST_DURATION, "resolution": TEST_RESOLUTION, "seed": 42}}
    result = _post_json("https://api.replicate.com/v1/predictions", payload, headers)
    pred_id = result.get("id"); pred_url = result.get("urls", {}).get("get")
    print(f"  Prediction ID: {pred_id}")
    status = result.get("status", "starting"); timeout = 300; elapsed = 0
    while status not in ("succeeded", "failed", "canceled") and elapsed < timeout:
        time.sleep(5); elapsed += 5
        result = _get_json(pred_url, headers); status = result.get("status")
        print(f"  [{elapsed:3d}s] status={status}")
    if status == "succeeded":
        output = result.get("output"); video_url = output[0] if isinstance(output, list) else output
        print(f"  ✓ Done! Video URL: {video_url}")
        dest = OUTPUT_DIR / f"seedance_replicate_{int(time.time())}.mp4"; _download(video_url, dest); return str(dest)
    print(f"  ✗ Failed: {result.get('error') or status}"); return None

def test_fal_seedance(image_url, prompt):
    if not FAL_API_KEY:
        print("[fal.ai] FAL_KEY not set — skipping"); return None
    print("\n[fal.ai] Submitting Seedance 2.0 via queue...")
    headers = {"Authorization": f"Key {FAL_API_KEY}"}
    queue_url = f"https://queue.fal.run/{FAL_SEEDANCE_ENDPOINT}"
    payload = {"image_url": image_url, "prompt": prompt, "duration": TEST_DURATION, "resolution": TEST_RESOLUTION, "seed": 42}
    result = _post_json(queue_url, payload, headers)
    request_id = result.get("request_id")
    status_url = f"https://queue.fal.run/{FAL_SEEDANCE_ENDPOINT}/requests/{request_id}/status"
    result_url = f"https://queue.fal.run/{FAL_SEEDANCE_ENDPOINT}/requests/{request_id}"
    print(f"  Request ID: {request_id}")
    status = "IN_QUEUE"; timeout = 300; elapsed = 0
    while status not in ("COMPLETED", "FAILED") and elapsed < timeout:
        time.sleep(6); elapsed += 6
        status = _get_json(status_url, headers).get("status", "UNKNOWN")
        print(f"  [{elapsed:3d}s] status={status}")
    if status == "COMPLETED":
        r = _get_json(result_url, headers)
        video_url = (r.get("video") or {}).get("url") or r.get("video_url")
        print(f"  ✓ Done! Video URL: {video_url}")
        dest = OUTPUT_DIR / f"seedance_fal_{int(time.time())}.mp4"; _download(video_url, dest); return str(dest)
    print(f"  ✗ Failed or timed out"); return None

def test_bytedance_seedance(image_url, prompt):
    if not BYTEDANCE_API_KEY:
        print("[ByteDance] BYTEDANCE_SEEDANCE_API_KEY not set — skipping"); return None
    print("\n[ByteDance] Submitting via direct API...")
    headers = {"Authorization": f"Bearer {BYTEDANCE_API_KEY}"}
    try:
        result = _post_json("https://api.bytedance.com/v1/seedance/video/generate", {"model": "seedance-2-0-i2v-480p", "image": image_url, "prompt": prompt, "duration": TEST_DURATION, "seed": 42}, headers)
    except RuntimeError as e:
        print(f"  ✗ Submit error: {e}"); return None
    task_id = result.get("task_id") or result.get("id"); print(f"  Task ID: {task_id}")
    poll_url = f"https://api.bytedance.com/v1/seedance/video/tasks/{task_id}"
    status = "PENDING"; timeout = 300; elapsed = 0
    while status not in ("SUCCEEDED", "FAILED") and elapsed < timeout:
        time.sleep(8); elapsed += 8; tr = _get_json(poll_url, headers); status = (tr.get("status") or "UNKNOWN").upper()
        print(f"  [{elapsed:3d}s] status={status}")
    if status == "SUCCEEDED":
        video_url = tr.get("output", {}).get("video_url") or tr.get("video_url")
        print(f"  ✓ Done! Video URL: {video_url}")
        dest = OUTPUT_DIR / f"seedance_bytedance_{int(time.time())}.mp4"; _download(video_url, dest); return str(dest)
    print("  ✗ Failed or timed out"); return None

def test_fal_seedance_t2v(prompt):
    if not FAL_API_KEY:
        print("[fal.ai T2V] FAL_KEY not set — skipping"); return None
    print("\n[fal.ai T2V] Submitting Seedance 2.0 multi-shot T2V...")
    headers = {"Authorization": f"Key {FAL_API_KEY}"}
    t2v_ep = "fal-ai/seedance-2-0-t2v"
    multi_prompt = "SHOT 1: Close-up of a woman's face in golden hour light. SHOT 2: She turns and walks through a forest path, bokeh background. SHOT 3: Wide shot, she looks into the distance at sunset. Cinematic, photorealistic, smooth cuts."
    try:
        result = _post_json(f"https://queue.fal.run/{t2v_ep}", {"prompt": multi_prompt, "duration": 10, "resolution": "1280x720", "num_shots": 3, "seed": 42}, headers)
    except RuntimeError as e:
        print(f"  ✗ Submit error: {e}"); return None
    request_id = result.get("request_id")
    status_url = f"https://queue.fal.run/{t2v_ep}/requests/{request_id}/status"
    result_url = f"https://queue.fal.run/{t2v_ep}/requests/{request_id}"
    status = "IN_QUEUE"; timeout = 360; elapsed = 0
    while status not in ("COMPLETED", "FAILED") and elapsed < timeout:
        time.sleep(8); elapsed += 8
        status = _get_json(status_url, headers).get("status", "UNKNOWN")
        print(f"  [{elapsed:3d}s] status={status}")
    if status == "COMPLETED":
        r = _get_json(result_url, headers)
        video_url = (r.get("video") or {}).get("url") or r.get("video_url")
        print(f"  ✓ Done! Video URL: {video_url}")
        dest = OUTPUT_DIR / f"seedance_t2v_{int(time.time())}.mp4"; _download(video_url, dest); return str(dest)
    print(f"  ✗ T2V test failed (status={status})"); return None

def main():
    print("=" * 70); print("Digital-Stud — Seedance 2.0 API Test Suite"); print("=" * 70)
    results = {}
    results["replicate_i2v"]    = test_replicate_seedance(TEST_IMAGE_URL, TEST_PROMPT) or "SKIPPED/FAILED"
    results["fal_i2v"]          = test_fal_seedance(TEST_IMAGE_URL, TEST_PROMPT) or "SKIPPED/FAILED"
    results["bytedance_direct"] = test_bytedance_seedance(TEST_IMAGE_URL, TEST_PROMPT) or "SKIPPED/FAILED"
    results["fal_t2v_multishot"]= test_fal_seedance_t2v(TEST_PROMPT) or "SKIPPED/FAILED"
    print("\n" + "=" * 70); print("RESULTS SUMMARY"); print("=" * 70)
    for k, v in results.items():
        print(f"  {'✓' if 'SKIPPED/FAILED' not in v else '–'} {k}: {v}")
    Path(OUTPUT_DIR / "test_results.json").write_text(json.dumps(results, indent=2))
    print("\nNotes: Replicate ~$0.30/clip, fal.ai queue API, ByteDance beta direct, multi-shot T2V via SHOT 1/2/3 prompts.")

if __name__ == "__main__":
    main()

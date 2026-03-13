"""
api_test_actionmesh.py
======================
Digital-Stud 3D+AI Workflow — ActionMesh API test script
Run #102 artifact — 2026-03-14

ActionMesh is a video-to-3D character rigging + motion retargeting service.
It takes a source video (with a person moving), extracts SMPL-X body pose,
and outputs a rigged/animated 3D character (GLB, FBX, or BVH).

Endpoints tested here:
  1. POST /v1/jobs         — submit a video-to-3D job
  2. GET  /v1/jobs/{id}    — poll job status
  3. GET  /v1/jobs/{id}/result — download result GLB/BVH

Usage:
  pip install requests python-dotenv
  export ACTIONMESH_API_KEY=your_key_here
  python api_test_actionmesh.py --video path/to/input.mp4 [--output_dir ./output]

References:
  https://actionmesh.io/docs/api
  ComfyUI-mesh2motion integration: github.com/jtydhr88/ComfyUI-mesh2motion
  arXiv Ani3DHuman: 2602.19089 (kinematics + video diffusion for photorealistic animation)
"""

import argparse
import os
import sys
import time
import json
import requests
from pathlib import Path

BASE_URL = "https://api.actionmesh.io"
DEFAULT_POLL_INTERVAL = 5
DEFAULT_TIMEOUT = 300

def get_api_key():
    key = os.environ.get("ACTIONMESH_API_KEY", "")
    if not key:
        env_path = Path(".env")
        if env_path.exists():
            for line in env_path.read_text().splitlines():
                if line.startswith("ACTIONMESH_API_KEY="):
                    key = line.split("=", 1)[1].strip().strip('"\'\"')
                    break
    if not key:
        print("[ERROR] ACTIONMESH_API_KEY not found.")
        sys.exit(1)
    return key

def submit_job(api_key, video_path, output_format="glb"):
    url = f"{BASE_URL}/v1/jobs"
    headers = {"Authorization": f"Bearer {api_key}"}
    with open(video_path, "rb") as f:
        files = {"video": (Path(video_path).name, f, "video/mp4")}
        data = {"output_format": output_format, "pose_format": "smplx",
                "retarget": "true", "fps": "30"}
        resp = requests.post(url, headers=headers, files=files, data=data, timeout=60)
    resp.raise_for_status()
    job = resp.json()
    print(f"[OK] Job submitted: id={job.get('id')}  status={job.get('status')}")
    return job

def poll_job(api_key, job_id, poll_interval=DEFAULT_POLL_INTERVAL, timeout=DEFAULT_TIMEOUT):
    url = f"{BASE_URL}/v1/jobs/{job_id}"
    headers = {"Authorization": f"Bearer {api_key}"}
    elapsed = 0
    while elapsed < timeout:
        resp = requests.get(url, headers=headers, timeout=30)
        resp.raise_for_status()
        job = resp.json()
        status = job.get("status", "unknown")
        progress = job.get("progress", 0)
        print(f"  [{elapsed:>4}s] status={status}  progress={progress}%")
        if status == "completed":
            return job
        if status == "failed":
            print(f"[FAIL] {job.get('error', 'no details')}")
            return job
        time.sleep(poll_interval)
        elapsed += poll_interval
    return {"id": job_id, "status": "timeout"}

def download_result(api_key, job_id, output_dir):
    url = f"{BASE_URL}/v1/jobs/{job_id}/result"
    headers = {"Authorization": f"Bearer {api_key}"}
    resp = requests.get(url, headers=headers, timeout=60)
    resp.raise_for_status()
    result = resp.json()
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    saved = []
    for file_info in result.get("files", []):
        fname = file_info.get("name", f"{job_id}_output")
        furl  = file_info.get("url", "")
        if not furl:
            continue
        fdata = requests.get(furl, timeout=120)
        fdata.raise_for_status()
        fpath = output_path / fname
        fpath.write_bytes(fdata.content)
        saved.append(str(fpath))
        print(f"  [DL] {fname}  ({len(fdata.content)//1024}KB)")
    meta_path = output_path / f"{job_id}_meta.json"
    meta_path.write_text(json.dumps(result, indent=2))
    saved.append(str(meta_path))
    return saved

def smoke_test(api_key):
    print("\n-- Smoke Test --")
    try:
        resp = requests.get(f"{BASE_URL}/v1/health", timeout=10)
        print(f"[OK] Health: {resp.status_code}")
    except Exception as e:
        print(f"[WARN] Health: {e}")
    try:
        resp = requests.get(f"{BASE_URL}/v1/jobs",
                            headers={"Authorization": f"Bearer {api_key}"},
                            params={"limit": 5}, timeout=15)
        if resp.status_code == 401:
            print("[FAIL] Auth failed")
            return False
        resp.raise_for_status()
        jobs = resp.json().get("jobs", [])
        print(f"[OK] Auth OK — {len(jobs)} recent job(s)")
        return True
    except Exception as e:
        print(f"[FAIL] {e}")
        return False

def main():
    p = argparse.ArgumentParser(description="ActionMesh API test")
    p.add_argument("--video", default=None)
    p.add_argument("--output_dir", default="./output/actionmesh")
    p.add_argument("--format", default="glb", choices=["glb","fbx","bvh"])
    p.add_argument("--smoke_only", action="store_true")
    p.add_argument("--job_id", default=None)
    args = p.parse_args()

    api_key = get_api_key()
    if not smoke_test(api_key):
        sys.exit(1)
    if args.smoke_only:
        return
    if args.job_id:
        job = poll_job(api_key, args.job_id)
        if job.get("status") == "completed":
            download_result(api_key, args.job_id, args.output_dir)
        return
    if not args.video:
        print("No --video supplied. Smoke test complete.")
        return
    if not Path(args.video).exists():
        print(f"[ERROR] Video not found: {args.video}")
        sys.exit(1)
    job = submit_job(api_key, args.video, output_format=args.format)
    job_id = job.get("id")
    if not job_id:
        sys.exit(1)
    job = poll_job(api_key, job_id)
    if job.get("status") == "completed":
        saved = download_result(api_key, job_id, args.output_dir)
        print(f"[OK] {len(saved)} file(s) saved to {args.output_dir}")

if __name__ == "__main__":
    main()

# ComfyUI-mesh2motion integration notes:
# Workflow: [Video] -> ComfyUI-mesh2motion ActionMesh node -> GLB -> Load3D -> StableGen -> FLUX.2 v2v
# Related: scripts/api_test_replicate.py, api_test_fal.py, api_test_seedance.py
# arXiv: Ani3DHuman (2602.19089), Hoi3DGen (2603.12126), NBAvatar (2603.12063)

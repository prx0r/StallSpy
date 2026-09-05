#!/usr/bin/env python3
"""
Full Content Automation — connects daily actions → video rendering → R2 backup.

Usage:
  python3 auto_content.py --day 1                # generate daily content
  python3 auto_content.py --day 1 --render       # also render video
  python3 auto_content.py --day 1 --backup       # also backup to R2
  python3 auto_content.py --day 1 --full         # all of the above
"""

import boto3
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# ── Paths ───────────────────────────────────────────────────────────────

REPO = "/root/StallSpy"
LOG_DIR = os.path.join(REPO, "logs")
PLATINUM_DIR = os.path.join(REPO, "tool/r2_imports/platinum")
R2_IMPORTS = os.path.join(REPO, "tool/r2_imports")

# ── R2 Config ───────────────────────────────────────────────────────────

R2_ENDPOINT = "https://954612afb5a97bb15dddcdc70176813d.r2.cloudflarestorage.com"
R2_ACCESS_KEY = "2a8d61c9ed22f5899b8507435a794f5d"
R2_SECRET_KEY = "e673672255567cc054e43479fcee0030862fe998e3bc8d1c447b91503c5c729d"
R2_BUCKET = "blog-video-assets"

def get_r2():
    return boto3.client(
        "s3",
        endpoint_url=R2_ENDPOINT,
        aws_access_key_id=R2_ACCESS_KEY,
        aws_secret_access_key=R2_SECRET_KEY,
        region_name="auto",
    )


# ── Content Generation (from daily_content.py) ─────────────────────────

def generate_content(day_number, date_str=None, notes=""):
    """Run the daily content engine."""
    if not date_str:
        date_str = datetime.now().strftime("%Y-%m-%d")
    
    # Import and run the existing engine
    sys.path.insert(0, os.path.join(REPO, "tool"))
    from daily_content import get_git_log, get_etsy_store_metrics, get_today_expenses
    from daily_content import generate_full_log, generate_video_script, generate_tldr
    
    commits = get_git_log(date_str)
    metrics = get_etsy_store_metrics()
    expenses = get_today_expenses(date_str)
    
    os.makedirs(LOG_DIR, exist_ok=True)
    
    # Generate all three formats
    full_log = generate_full_log(commits, metrics, expenses, day_number, notes)
    video_script = generate_video_script(commits, metrics, expenses, day_number)
    tldr = generate_tldr(commits, metrics, expenses, day_number)
    
    prefix = os.path.join(LOG_DIR, date_str)
    
    with open(f"{prefix}_full.md", "w") as f:
        f.write(full_log)
    with open(f"{prefix}_video.md", "w") as f:
        f.write(video_script)
    with open(f"{prefix}_tldr.md", "w") as f:
        f.write(tldr)
    
    # Save machine-readable ledger
    ledger_entry = {
        "date": date_str,
        "day_number": day_number,
        "timestamp": datetime.now().isoformat(),
        "commits": commits,
        "expenses": expenses,
        "etsy_metrics": metrics,
        "expense_total": sum(e.get("amount", 0) for e in expenses),
    }
    with open(os.path.join(REPO, "ledger.jsonl"), "a") as f:
        f.write(json.dumps(ledger_entry) + "\n")
    
    return full_log, video_script, tldr, ledger_entry


# ── Video Rendering ─────────────────────────────────────────────────────

def find_renderers():
    """Find available platinum renderers."""
    renderers = []
    for f in sorted(os.listdir(PLATINUM_DIR)):
        if f.endswith(".py"):
            path = os.path.join(PLATINUM_DIR, f)
            with open(path) as fh:
                content = fh.read()
            
            # Extract title from docstring
            title_match = re.search(r'"""(.*?)"""', content, re.DOTALL)
            title = ""
            if title_match:
                first_line = title_match.group(1).strip().split("\n")[0]
                title = first_line
            
            # Count functions (complexity indicator)
            funcs = len(re.findall(r'^def ', content, re.MULTILINE))
            
            renderers.append({
                "file": f,
                "path": path,
                "title": title,
                "functions": funcs,
                "size_kb": os.path.getsize(path) // 1024,
            })
    
    return renderers


def render_video(renderer_path, output_dir=None, scene=None, fps=10, width=1280, height=720):
    """Render a platinum video."""
    if not output_dir:
        output_dir = os.path.join(REPO, "output", datetime.now().strftime("%Y-%m-%d_%H%M%S"))
    
    os.makedirs(output_dir, exist_ok=True)
    
    cmd = [
        sys.executable, renderer_path,
        "--fps", str(fps),
        "--width", str(width),
        "--height", str(height),
    ]
    
    if scene is not None:
        cmd.extend(["--scene", str(scene)])
    
    print(f"Rendering: {os.path.basename(renderer_path)}")
    print(f"Output: {output_dir}")
    
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=600, cwd=output_dir)
    
    if result.returncode == 0:
        # Find the output video
        for f in os.listdir(output_dir):
            if f.endswith(".mp4"):
                video_path = os.path.join(output_dir, f)
                size_mb = os.path.getsize(video_path) / (1024 * 1024)
                print(f"  Output: {video_path} ({size_mb:.1f} MB)")
                return video_path
    
    print(f"  Error: {result.stderr[:500]}")
    return None


# ── R2 Backup ───────────────────────────────────────────────────────────

def backup_to_r2(local_path, r2_key):
    """Upload a file to R2."""
    client = get_r2()
    client.upload_file(local_path, R2_BUCKET, r2_key)
    size = os.path.getsize(local_path)
    print(f"  Backed up: {r2_key} ({size} bytes)")
    return r2_key


def backup_day(day_number, date_str=None):
    """Backup all daily content to R2."""
    if not date_str:
        date_str = datetime.now().strftime("%Y-%m-%d")
    
    prefix = f"experiments/£0to1M/day-{day_number:04d}/{date_str}"
    backed_up = []
    
    # Backup logs
    for suffix in ["_full.md", "_video.md", "_tldr.md"]:
        local = os.path.join(LOG_DIR, f"{date_str}{suffix}")
        if os.path.exists(local):
            r2_key = f"{prefix}/{os.path.basename(local)}"
            backup_to_r2(local, r2_key)
            backed_up.append(r2_key)
    
    # Backup ledger entry
    ledger = os.path.join(REPO, "ledger.jsonl")
    if os.path.exists(ledger):
        # Get last line
        with open(ledger) as f:
            lines = f.readlines()
            if lines:
                entry_path = os.path.join(LOG_DIR, f"{date_str}_ledger.json")
                with open(entry_path, "w") as ef:
                    ef.write(lines[-1])
                r2_key = f"{prefix}/ledger.json"
                backup_to_r2(entry_path, r2_key)
                backed_up.append(r2_key)
    
    return backed_up


# ── Main ────────────────────────────────────────────────────────────────

def run(day_number, render=False, backup=False, full=False):
    """Run the full automation pipeline."""
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    print(f"\n{'='*60}")
    print(f"Day {day_number} — {date_str}")
    print(f"{'='*60}\n")
    
    # Step 1: Generate content
    print("Step 1: Generating daily content...")
    full_log, video_script, tldr, ledger = generate_content(day_number, date_str)
    print(f"  Full log: {len(full_log)} chars")
    print(f"  Video script: {len(video_script)} chars")
    print(f"  TL;DR: {len(tldr)} chars")
    
    # Step 2: Render video (if requested)
    if render or full:
        print("\nStep 2: Rendering video...")
        renderers = find_renderers()
        print(f"  Found {len(renderers)} platinum renderers")
        
        # Pick a renderer based on day number (cycle through them)
        renderer = renderers[day_number % len(renderers)]
        print(f"  Selected: {renderer['title'][:60]}")
        
        video_path = render_video(
            renderer["path"],
            output_dir=os.path.join(REPO, "output", f"day-{day_number:04d}"),
            fps=10,
        )
        if video_path:
            ledger["video_path"] = video_path
    
    # Step 3: Backup to R2 (if requested)
    if backup or full:
        print("\nStep 3: Backing up to R2...")
        backed_up = backup_day(day_number, date_str)
        ledger["r2_backups"] = backed_up
    
    # Step 4: Summary
    print(f"\n{'='*60}")
    print(f"Done. Day {day_number} complete.")
    print(f"  Content: {LOG_DIR}/{date_str}_*.md")
    if render or full:
        print(f"  Video: output/day-{day_number:04d}/")
    if backup or full:
        print(f"  R2: experiments/£0to1M/day-{day_number:04d}/")
    print(f"{'='*60}\n")
    
    return ledger


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Full Content Automation")
    parser.add_argument("--day", type=int, required=True, help="Day number")
    parser.add_argument("--render", action="store_true", help="Render video")
    parser.add_argument("--backup", action="store_true", help="Backup to R2")
    parser.add_argument("--full", action="store_true", help="All of the above")
    parser.add_argument("--list-renderers", action="store_true", help="List available renderers")
    
    args = parser.parse_args()
    
    if args.list_renderers:
        renderers = find_renderers()
        print(f"Available platinum renderers ({len(renderers)}):")
        for i, r in enumerate(renderers):
            print(f"  {i:2d}. {r['title'][:60]:60s} ({r['functions']} funcs, {r['size_kb']}KB)")
        sys.exit(0)
    
    run(args.day, render=args.render, backup=args.backup, full=args.full)

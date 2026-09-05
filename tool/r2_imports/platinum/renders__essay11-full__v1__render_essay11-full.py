#!/usr/bin/env python3
"""Auto-generated render script for essay11-full. Uses visual_templates dispatch."""
import sys, os, subprocess, json
sys.path.insert(0, '/root/projects/blog/scripts/renderer')
sys.path.insert(0, '/root/projects/blog/visual-library')
from visual_templates import render_shot, MOTIF_TEMPLATE as _MT

FPS = 6
OUT = r"/root/projects/blog/content/publishing/renders/essay11-full/v1"

with open(f"{OUT}/storyboard.json") as f:
    SHOTS = json.load(f)

def render_all():
    for i, s in enumerate(SHOTS):
        sid = f"s{i+1:03d}"
        dur = s["duration"]
        motif = s.get("visual_mode", "stone_eye")
        sd = os.path.join(OUT, "scenes", sid)
        os.makedirs(sd, exist_ok=True)
        frames = int(dur * FPS)
        for fi in range(frames):
            t_val = fi / FPS
            u_val = fi / frames if frames > 1 else 1
            im = render_shot(motif, t_val, u_val, i)
            im.save(os.path.join(sd, f"frame_{fi:05d}.png"))
        
        mp4 = os.path.join(OUT, "scenes", f"{sid}.mp4")
        subprocess.run(["ffmpeg", "-y", "-framerate", str(FPS), "-i",
            f"{sd}/frame_%05d.png", "-c:v", "libx264", "-pix_fmt", "yuv420p",
            "-preset", "ultrafast", "-crf", "28", "-t", str(dur), mp4],
            capture_output=True)
        if i % 10 == 0: print(f"  [{i+1}/{len(SHOTS)}] {sid}")
    
    with open(os.path.join(OUT, "concat.txt"), "w") as f:
        for s in SHOTS:
            sid = f"s{SHOTS.index(s)+1:03d}"
            f.write(f"file '{os.path.join(OUT, 'scenes', sid)}.mp4'\n")
    
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i",
        os.path.join(OUT, "concat.txt"), "-c", "copy",
        os.path.join(OUT, "draft.mp4")], capture_output=True)

if __name__ == "__main__":
    render_all()
    print("Done.")

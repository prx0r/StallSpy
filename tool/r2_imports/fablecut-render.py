#!/usr/bin/env python3
"""FableCut VPS Renderer — download from R2, render with ffmpeg."""
import json, subprocess, sys, os, tarfile, tempfile
import boto3

R2_ENDPOINT = "https://954612afb5a97bb15dddcdc70176813d.r2.cloudflarestorage.com"
R2_KEY = "2a8d61c9ed22f5899b8507435a794f5d"
R2_SECRET = "e673672255567cc054e43479fcee0030862fe998e3bc8d1c447b91503c5c729d"
R2_BUCKET = "fablecut-projects"


def download_bundle(key, dest_dir):
    s3 = boto3.client("s3", endpoint_url=R2_ENDPOINT,
                       aws_access_key_id=R2_KEY, aws_secret_access_key=R2_SECRET,
                       region_name="auto")
    tar_path = os.path.join(dest_dir, "bundle.tar.gz")
    s3.download_file(R2_BUCKET, key, tar_path)
    with tarfile.open(tar_path) as tf:
        tf.extractall(dest_dir)
    print(f"Downloaded and extracted: {key}")


def render(project_dir, output_path):
    with open(os.path.join(project_dir, "project.json")) as f:
        proj = json.load(f)

    media_map = {m["id"]: m for m in proj["media"]}
    clips = proj.get("clips", [])

    video_clips = [c for c in clips if c["kind"] == "video"]
    audio_clips = [c for c in clips if c["kind"] == "audio"]

    if not video_clips:
        print("No video clips found"); sys.exit(1)

    inputs = []
    filter_parts = []
    v_labels = []

    for i, vc in enumerate(video_clips):
        media = media_map[vc["mediaId"]]
        src = os.path.join(project_dir, media["src"].lstrip("/"))
        inputs += ["-ss", str(vc.get("in", 0)), "-t", str(vc["duration"]), "-i", src]
        filter_parts.append(
            f"[{i}:v]scale=1920:1080:force_original_aspect_ratio=decrease,"
            f"pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1[v{i}]"
        )
        v_labels.append(f"[v{i}]")

    if len(video_clips) == 1:
        vfilter = f"[v0]null[outv]"
    else:
        vfilter = "".join(v_labels) + f"concat=n={len(video_clips)}:v=1:a=0[outv]"

    afilter = None
    if audio_clips:
        a_idx = len(video_clips)
        a_labels = []
        for i, ac in enumerate(audio_clips):
            media = media_map[ac["mediaId"]]
            src = os.path.join(project_dir, media["src"].lstrip("/"))
            inputs += ["-ss", str(ac.get("in", 0)), "-t", str(ac["duration"]), "-i", src]
            # Each audio input gets its own index; aresample normalizes
            filter_parts.append(f"[{a_idx + i}:a]aresample=44100[a{i}]")
            a_labels.append(f"[a{i}]")

        if len(audio_clips) == 1:
            afilter = f"[a0]anull[outa]"
        else:
            # Use adelay to position each clip on the timeline, then amix
            delay_parts = []
            for i, ac in enumerate(audio_clips):
                delay_ms = int(ac.get("start", 0) * 1000)
                delay_parts.append(f"[a{i}]adelay={delay_ms}|{delay_ms}[d{i}]")
            delay_filter = ";".join(delay_parts)
            mix_input = "".join(f"[d{i}]" for i in range(len(audio_clips)))
            afilter = delay_filter + ";" + mix_input + f"amix=inputs={len(audio_clips)}:duration=longest:dropout_transition=0[outa]"

    cmd = ["ffmpeg", "-y"] + inputs
    all_filters = filter_parts + [vfilter]
    if afilter:
        all_filters.append(afilter)
    cmd += ["-filter_complex", ";".join(all_filters)]
    cmd += ["-map", "[outv]"]
    if audio_clips:
        cmd += ["-map", "[outa]"]
    cmd += ["-c:v", "libx264", "-preset", "fast", "-crf", "18",
            "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart",
            "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709",
            output_path]

    print(f"Rendering {len(video_clips)} video(s), {len(audio_clips)} audio(s)...")
    print(f"Command: {' '.join(cmd[:8])}...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"FFMPEG STDERR:\n{result.stderr[-2000:]}")
        sys.exit(1)
    print(f"Done: {output_path} ({os.path.getsize(output_path) // 1024}KB)")


if __name__ == "__main__":
    bundle_key = sys.argv[1] if len(sys.argv) > 1 else "clip1-1920-kaoh39.tar.gz"
    output = sys.argv[2] if len(sys.argv) > 2 else "rendered.mp4"

    with tempfile.TemporaryDirectory() as tmpdir:
        download_bundle(bundle_key, tmpdir)
        render(tmpdir, os.path.abspath(output))

"""Generate narration WAVs for each scene and mux into MP4."""
import os, json, asyncio, subprocess

OUT = "/root/projects/blog/content/publishing/renders/daimon-threshold/v1"

# Narration text per scene — key phrases from the essay
NARRATION = {
    "dt01": "There is something with you right now that has always been with you. Before you were born, it was watching.",
    "dt02": "The daimon is a function — the operational interface between the divine and the human. Three orders: mortals, daimons, and gods.",
    "dt03": "This being was assigned to you at the moment of your birth. A companion who has known you from the very first breath.",
    "dt04": "What kind of being is it, exactly? It stands at the threshold — neither divine nor human, but the place where they meet.",
    "dt05": "The daimon provides an escort for creation, guiding souls across the boundary between worlds.",
}

async def gen():
    import edge_tts
    for sid, text in NARRATION.items():
        wav_path = f"{OUT}/{sid}.wav"
        if not os.path.exists(wav_path):
            await edge_tts.Communicate(text, "en-US-AriaNeural").save(wav_path)
            print(f"  {sid}: {len(text.split())} words")

asyncio.run(gen())

# Mux audio into each scene's MP4
for sid, text in NARRATION.items():
    wav = f"{OUT}/{sid}.wav"
    mp4_in = f"{OUT}/scenes/{sid}.mp4"
    mp4_out = f"{OUT}/scenes/{sid}_audio.mp4"
    if os.path.exists(wav) and os.path.exists(mp4_in):
        subprocess.run(['ffmpeg','-y','-i',mp4_in,'-i',wav,
            '-c:v','copy','-c:a','aac','-map','0:v:0','-map','1:a:0','-shortest',
            mp4_out], capture_output=True)
        print(f"  Muxed {sid}")

# Re-assemble with audio
with open(f"{OUT}/c_audio.txt","w") as f:
    for sid in NARRATION:
        f.write(f"file '{OUT}/scenes/{sid}_audio.mp4'\n")

subprocess.run(['ffmpeg','-y','-f','concat','-safe','0','-i',f"{OUT}/c_audio.txt",
    '-c','copy',f"{OUT}/daimon_threshold_audio.mp4"], capture_output=True)

sz = os.path.getsize(f"{OUT}/daimon_threshold_audio.mp4")
print(f"Final with audio: {sz/1024:.0f} KB")

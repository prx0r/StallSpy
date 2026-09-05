"""Daimon Threshold Pack — 5 scenes, each with a unique concrete visual."""
import sys, os, json, math, subprocess
sys.path.insert(0, '/root/projects/blog/scripts/renderer')
from renderer import *
FPS = 10
OUT = "/root/projects/blog/content/publishing/renders/daimon-threshold/v1"

with open(f"{OUT}/scene_manifest.json") as f:
    MANIFEST = json.load(f)

VOID = (13,17,23); GOLD = (212,165,116); CRIMSON = (141,44,57)
LAPIS = (42,70,110); UMBER = (60,47,38); IVORY = (246,242,232)
PALE = (200,195,185)

# ── SCENE 1: The Threshold Door ─────────────────────────────
def scene_threshold_door(t, u, idx):
    """A vertical aperture opens between dark below and luminous above."""
    im = canvas(VOID); d = ImageDraw.Draw(im)
    cx, cy = 640, 360
    # Upper realm (luminous, cool)
    for y in range(0, cy, 4):
        brightness = int(20 * (1 - y/cy))
        d.line([(0,y),(1280,y)], fill=(brightness,brightness,brightness+10))
    # Lower realm (dark, warm)
    d.rectangle([(0,cy),(1280,720)], fill=UMBER)
    # The aperture — a vertical door shape
    ap_w = 40 + 160 * u
    ap_h = 80 + 240 * u
    d.rectangle([(cx-ap_w/2, cy-ap_h/2), (cx+ap_w/2, cy+ap_h/2)], 
                outline=rgba(GOLD, 0.6 + 0.3 * math.sin(t*0.5)), width=3)
    # Light bleeding through the door
    for yy in range(int(cy-ap_h/2), int(cy+ap_h/2), 2):
        bleed = 0.3 * (1 - abs(yy-cy)/(ap_h/2))
        dot(d, cx, yy, 2, GOLD, bleed)
    return im

# ── SCENE 2: The Three Orders ──────────────────────────────
def scene_three_orders(t, u, idx):
    """Three horizontal bands: mortal, daimonic, divine."""
    im = canvas(VOID); d = ImageDraw.Draw(im)
    # Divine (top) — cool blue, expansive
    d.rectangle([(0,0),(1280,200)], fill=(5,10,30))
    for i in range(20):
        dot(d, 640+300*math.sin(t*0.1+i*0.3), 80+60*math.sin(t*0.15+i), 2, LAPIS, 0.15)
    # Daimonic (middle) — warm gold, bridging
    d.rectangle([(0,200),(1280,520)], fill=(10,8,5))
    # The threshold band
    for x in range(0, 1280, 4):
        yy = 360 + 30 * math.sin(x*0.02 + t*0.5)
        dot(d, x, yy, 2, GOLD, 0.3 + 0.2 * math.sin(t + x*0.01))
    # A luminous figure in the daimonic band
    dot(d, 640, 360, 20 + 5 * math.sin(t*0.3), PALE, 0.4)
    # Mortal (bottom) — warm earth
    d.rectangle([(0,520),(1280,720)], fill=(25,20,15))
    for i in range(10):
        dot(d, 300+i*70, 620+30*math.sin(t*0.2+i), 3, UMBER, 0.5)
    # Separator lines
    d.line([(0,200),(1280,200)], fill=rgba(GOLD, 0.3), width=1)
    d.line([(0,520),(1280,520)], fill=rgba(GOLD, 0.2), width=1)
    return im

# ── SCENE 3: The Daimon Presence ────────────────────────────
def scene_daimon_presence(t, u, idx):
    """A luminous figure-shape at the threshold, facing both directions."""
    im = canvas(VOID); d = ImageDraw.Draw(im)
    cx, cy = 640, 360
    # The figure — an upright oval with a suggestion of shoulders
    figure_width = 30 + 5 * math.sin(t*0.3)
    figure_height = 80 + 10 * math.sin(t*0.4)
    pulse = 1 + 0.03 * math.sin(t*0.8)
    # Body
    d.ellipse([(cx-figure_width*pulse, cy-figure_height*pulse), 
               (cx+figure_width*pulse, cy+figure_height*pulse)], 
              outline=rgba(PALE, 0.5 + 0.2 * math.sin(t*0.5)), width=2)
    d.ellipse([(cx-15, cy-40), (cx+15, cy-10)], fill=rgba(PALE, 0.3))
    # Radiating presence lines
    for i in range(12):
        ang = i*0.524 + t*0.1
        r = 50 + 30 * math.sin(t*0.3 + i)
        x = cx + r * math.cos(ang)
        y = cy + r * math.sin(ang) * 0.6
        d.line([(cx, cy), (x, y)], fill=rgba(GOLD, 0.1 + 0.1 * math.sin(t*0.5 + i)), width=1)
    return im

# ── SCENE 4: The Interface Glow ────────────────────────────
def scene_interface_glow(t, u, idx):
    """A warm gold glow at the contact point between human and daimon."""
    im = canvas(VOID); d = ImageDraw.Draw(im)
    cx, cy = 640, 360
    # Two approaching presences — one from below (human), one from above (daimon)
    human_y = 500 - 140 * u
    daimon_y = 220 + 140 * u
    # Human (smaller, warmer)
    dot(d, cx-40, human_y, 8 + 3 * math.sin(t*0.6), UMBER, 0.7)
    # Daimon (larger, luminous)
    dot(d, cx+40, daimon_y, 15 + 5 * math.sin(t*0.4), PALE, 0.5)
    # Interface glow — appears when they get close
    dist = abs(human_y - daimon_y)
    if dist < 200:
        glow = smoothstep(200, 50, dist) * 0.6
        for rr in range(20, 100, 10):
            ring(d, cx, (human_y + daimon_y)/2, rr * (1 - u * 0.3), 
                 GOLD, glow * (1 - rr/100), 1)
        dot(d, cx, (human_y + daimon_y)/2, 5, GOLD, glow)
    return im

# ── SCENE 5: The Escort Crossing ───────────────────────────
def scene_escort_crossing(t, u, idx):
    """A small point of light ascends through the threshold, escorted."""
    im = canvas(VOID); d = ImageDraw.Draw(im)
    cx, cy = 640, 360
    # The threshold door (from scene 1, simplified)
    d.rectangle([(cx-80, cy-120), (cx+80, cy+120)], outline=rgba(GOLD, 0.3), width=2)
    # The soul — a small point ascending
    soul_y = 550 - 400 * u
    dot(d, cx, soul_y, 5 + 2 * math.sin(t*2), GOLD, 0.9)
    # The escort — a larger presence beside the soul
    escort_x = cx + 40 + 10 * math.sin(t*0.5)
    escort_y = soul_y - 30
    d.ellipse([(escort_x-12, escort_y-20), (escort_x+12, escort_y+20)], 
              outline=rgba(PALE, 0.4), width=2)
    # Trace of the path
    if u > 0.1:
        for i in range(10):
            yy = 550 - 400 * (u * i/10)
            dot(d, cx + 5 * math.sin(yy*0.05), yy, 2, GOLD, 0.1)
    # Upper realm glow as they near it
    if u > 0.7:
        a = smoothstep(0.7, 0.9, u) * 0.2
        d.rectangle([(cx-120, cy-140), (cx+120, cy-120)], fill=rgba(LAPIS, a))
    return im

FUNCTIONS = {
    "threshold_door": scene_threshold_door,
    "three_orders": scene_three_orders,
    "daimon_presence": scene_daimon_presence,
    "interface_glow": scene_interface_glow,
    "escort_crossing": scene_escort_crossing,
}

# ── RENDER ──────────────────────────────────────────────────
def render():
    scenes = MANIFEST["scenes"]
    print(f"Rendering {len(scenes)} scenes at {FPS}fps:")
    for s in scenes:
        sid = s["id"]
        dur = s["duration_seconds"]
        mode = s["mode"]
        fn = FUNCTIONS.get(mode)
        if not fn:
            print(f"  SKIP {sid}: no function for {mode}")
            continue
        sd = os.path.join(OUT, "scenes", sid)
        os.makedirs(sd, exist_ok=True)
        frames = int(dur * FPS)
        for fi in range(frames):
            fn(fi/FPS, fi/frames if frames>0 else 1, 0).save(
                os.path.join(sd, f"frame_{fi:05d}.png"))
        print(f"  {sid}: {frames} frames = {dur}s [{mode}]")
    
    # Assemble
    print("\nAssembling...")
    with open(os.path.join(OUT, "c.txt"), "w") as f:
        for s in scenes:
            sid = s["id"]
            mp4 = os.path.join(OUT, "scenes", f"{sid}.mp4")
            sd = os.path.join(OUT, "scenes", sid)
            subprocess.run(['ffmpeg','-y','-framerate',str(FPS),'-i',
                f'{sd}/frame_%05d.png','-c:v','libx264','-pix_fmt','yuv420p',
                '-preset','ultrafast','-crf','28','-t',str(s["duration_seconds"]),mp4],
                capture_output=True)
            f.write(f"file '{mp4}'\n")
    
    subprocess.run(['ffmpeg','-y','-f','concat','-safe','0','-i',
        os.path.join(OUT,'c.txt'),'-c','copy',
        os.path.join(OUT,'daimon_threshold_animation.mp4')], capture_output=True)
    
    sz = os.path.getsize(os.path.join(OUT,'daimon_threshold_animation.mp4'))
    total = sum(s["duration_seconds"] for s in scenes)
    print(f"Final: {sz/1024:.0f} KB, {total:.0f}s ({total/60:.1f} min)")

if __name__ == "__main__":
    render()
    print("Done.")

from PIL import Image, ImageDraw
import math

PARCHMENT=(245,242,238); INK=(40,40,42); GOLD=(180,150,60)
CRIMSON=(160,55,55); LAPIS=(55,75,120); SILVER=(180,188,195)
DARK=(50,52,55); WHITE=(250,248,244); VOID=(26,29,35)

def border(d):
    for i in range(4): d.rectangle([i,i,1279-i,719-i], outline=(215,210,205), width=1)

def scene_s001(ctx, t, u):
    im = Image.new("RGB", (1280, 720), VOID)
    d = ImageDraw.Draw(im)
    cx, cy = 640, 360
    r = 15 + 30 * u
    for i in range(5):
        glow = int(60 - i * 10)
        d.ellipse([cx-r*(1+i*.3), cy-r*(1+i*.3), cx+r*(1+i*.3), cy+r*(1+i*.3)], outline=(GOLD[0],GOLD[1],GOLD[2],glow), width=1)
    d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=GOLD)
    return im

def scene_s002(ctx, t, u):
    im = Image.new("RGB", (1280, 720), VOID)
    d = ImageDraw.Draw(im)
    cx, cy = 640, 360
    n = int(8 + 16 * u)
    for i in range(n):
        a = (i / n) * 6.283 + t * 0.3
        L = 80 + 60 * u * (0.5 + 0.5 * math.sin(i * 1.3))
        d.line([(cx + 50 * math.cos(a), cy + 50 * math.sin(a)),
                (cx + (50 + L) * math.cos(a), cy + (50 + L) * math.sin(a))], fill=GOLD, width=2)
    d.ellipse([cx-30, cy-30, cx+30, cy+30], fill=WHITE)
    return im

def scene_s003(ctx, t, u):
    im = Image.new("RGB", (1280, 720), PARCHMENT)
    d = ImageDraw.Draw(im)
    cx, cy = 640, 360
    d.line([(100,cy), (1180,cy)], fill=INK, width=2)
    r = 40 + 20 * math.sin(t * 2)
    d.ellipse([cx-r, cy-150-r, cx+r, cy-150+r], outline=SILVER, width=2)
    border(d)
    return im

def scene_s004(ctx, t, u):
    im = Image.new("RGB", (1280, 720), PARCHMENT)
    d = ImageDraw.Draw(im)
    cx, cy = 640, 360
    d.ellipse([cx-200, cy-120, cx+200, cy+120], fill=LAPIS)
    pts = [(cx-180, cy-20)]
    for i in range(1, 12):
        x = cx - 180 + i * 32
        y = cy + 40 * math.sin(x * 0.03 + u * 2)
        pts.append((x, y))
    for i in range(len(pts)-1):
        d.line([pts[i], pts[i+1]], fill=GOLD, width=4)
    border(d)
    return im

def scene_s005(ctx, t, u):
    im = Image.new("RGB", (1280, 720), PARCHMENT)
    d = ImageDraw.Draw(im)
    for i in range(20):
        x = 300 + i * 35
        y = 320 + 60 * math.sin(x * 0.03 + u * 3)
        d.line([(x-3, y-3), (x+3, y+3)], fill=CRIMSON, width=1+int(u*3))
    border(d)
    return im

def scene_s006(ctx, t, u):
    im = Image.new("RGB", (1280, 720), PARCHMENT)
    d = ImageDraw.Draw(im)
    cx, cy = 640, 400
    d.rectangle([cx-120, cy-80, cx+120, cy+80], outline=INK, width=3)
    d.rectangle([cx-100, cy-60, cx+100, cy+60], outline=SILVER, width=1)
    fill_h = int(60 * u)
    d.rectangle([cx-78, cy+38-fill_h, cx+78, cy+38], fill=GOLD)
    border(d)
    return im

def scene_s007(ctx, t, u):
    im = Image.new("RGB", (1280, 720), VOID)
    d = ImageDraw.Draw(im)
    cx, cy = 640, 360
    sep = 300 - 280 * u
    for side in [-1, 1]:
        x = cx + side * sep // 2
        r = 20 + 15 * (1 - u)
        d.ellipse([x-r, cy-r, x+r, cy+r], fill=GOLD)
    if u > 0.5:
        m = (u - 0.5) * 2
        d.ellipse([cx-60*m, cy-60*m, cx+60*m, cy+60*m], outline=GOLD, width=2)
    return im

def scene_s008(ctx, t, u):
    im = Image.new("RGB", (1280, 720), VOID)
    d = ImageDraw.Draw(im)
    cx, cy = 640, 360
    r = 80 + 60 * u
    d.arc([cx-r, cy-r, cx+r, cy+r], 0, 360*u, fill=GOLD, width=3)
    if u > 0.9:
        d.ellipse([cx-8, cy-8, cx+8, cy+8], fill=WHITE)
    if u > 0.5:
        ri = 30 * (u - 0.5) * 2
        d.ellipse([cx-ri, cy-ri, cx+ri, cy+ri], outline=GOLD, width=1)
    return im

def scene_s009(ctx, t, u):
    im = Image.new("RGB", (1280, 720), PARCHMENT)
    d = ImageDraw.Draw(im)
    cx, cy = 640, 360
    d.ellipse([cx-200, cy-100, cx+200, cy+100], outline=SILVER, width=3)
    d.ellipse([cx-150, cy-75, cx+150, cy+75], outline=GOLD, width=2)
    if u > 0.3:
        alpha = (u-0.3)/0.7
        d.ellipse([cx-100*alpha, cy-50*alpha, cx+100*alpha, cy+50*alpha], fill=GOLD)
    border(d)
    return im

def scene_s010(ctx, t, u):
    im = Image.new("RGB", (1280, 720), VOID)
    d = ImageDraw.Draw(im)
    cx, cy = 640, 360
    for i in range(8):
        a = i * 0.785 + t * 0.2
        r = 50 + 200 * u
        x = cx + r * math.cos(a)
        y = cy + r * math.sin(a)
        d.line([(cx, cy), (x, y)], fill=GOLD, width=2)
    d.ellipse([cx-40*u, cy-40*u, cx+40*u, cy+40*u], fill=WHITE)
    return im

SCENE_FUNCTIONS = [scene_s001, scene_s002, scene_s003, scene_s004, scene_s005,
                   scene_s006, scene_s007, scene_s008, scene_s009, scene_s010]

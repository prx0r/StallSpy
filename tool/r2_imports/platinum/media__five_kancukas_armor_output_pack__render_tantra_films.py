from __future__ import annotations

import argparse
import json
import math
import os
import textwrap
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 720
FPS = 2

DEV_FONT = "/usr/share/fonts/truetype/noto/NotoSansDevanagari-Regular.ttf"
LAT_FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
LAT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

FONT = {
    "dev_xl": ImageFont.truetype(DEV_FONT, 78),
    "dev_l": ImageFont.truetype(DEV_FONT, 50),
    "dev_m": ImageFont.truetype(DEV_FONT, 32),
    "xl": ImageFont.truetype(LAT_BOLD, 55),
    "l": ImageFont.truetype(LAT_BOLD, 38),
    "m": ImageFont.truetype(LAT_FONT, 28),
    "s": ImageFont.truetype(LAT_FONT, 22),
    "xs": ImageFont.truetype(LAT_FONT, 17),
    "bold_s": ImageFont.truetype(LAT_BOLD, 22),
}

INK = (236, 231, 219)
MUTED = (145, 141, 132)
GOLD = (211, 178, 105)
CRIMSON = (136, 45, 58)
DARK = (12, 12, 15)
DARK_2 = (23, 22, 25)
WHITE = (248, 246, 240)
BLACK = (18, 18, 20)


def clamp(x: float, a: float = 0.0, b: float = 1.0) -> float:
    return max(a, min(b, x))


def smoothstep(a: float, b: float, x: float) -> float:
    if b == a:
        return 1.0 if x >= b else 0.0
    y = clamp((x - a) / (b - a))
    return y * y * (3.0 - 2.0 * y)


def lerp(a: float, b: float, u: float) -> float:
    return a + (b - a) * u


def rgba(c: tuple[int, int, int], a: float = 1.0) -> tuple[int, int, int, int]:
    return (c[0], c[1], c[2], int(255 * clamp(a)))


def canvas(bg: tuple[int, int, int] = DARK) -> Image.Image:
    return Image.new("RGBA", (W, H), (*bg, 255))


def text_size(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0], box[3] - box[1]


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    paragraphs = text.split("\n")
    lines: list[str] = []
    for p in paragraphs:
        words = p.split()
        if not words:
            lines.append("")
            continue
        cur = words[0]
        for word in words[1:]:
            test = cur + " " + word
            if text_size(draw, test, font)[0] <= max_width:
                cur = test
            else:
                lines.append(cur)
                cur = word
        lines.append(cur)
    return lines


def draw_centered(
    draw: ImageDraw.ImageDraw,
    text: str,
    y: float,
    font: ImageFont.FreeTypeFont,
    color: tuple[int, int, int] = INK,
    alpha: float = 1.0,
    max_width: int | None = None,
    line_gap: int = 8,
) -> float:
    lines = [text] if max_width is None else wrap_text(draw, text, font, max_width)
    yy = y
    for line in lines:
        w, h = text_size(draw, line, font)
        draw.text(((W - w) / 2, yy), line, font=font, fill=rgba(color, alpha))
        yy += h + line_gap
    return yy


def draw_left(
    draw: ImageDraw.ImageDraw,
    text: str,
    x: float,
    y: float,
    font: ImageFont.FreeTypeFont,
    color: tuple[int, int, int] = INK,
    alpha: float = 1.0,
    max_width: int | None = None,
    line_gap: int = 8,
) -> float:
    lines = [text] if max_width is None else wrap_text(draw, text, font, max_width)
    yy = y
    for line in lines:
        _, h = text_size(draw, line, font)
        draw.text((x, yy), line, font=font, fill=rgba(color, alpha))
        yy += h + line_gap
    return yy


def draw_dot(draw: ImageDraw.ImageDraw, x: float, y: float, r: float, color=GOLD, alpha=1.0) -> None:
    draw.ellipse((x - r, y - r, x + r, y + r), fill=rgba(color, alpha))


def draw_ring(draw: ImageDraw.ImageDraw, x: float, y: float, r: float, color=GOLD, alpha=1.0, width=2) -> None:
    draw.ellipse((x - r, y - r, x + r, y + r), outline=rgba(color, alpha), width=width)


def draw_arrow(draw: ImageDraw.ImageDraw, p1: tuple[float, float], p2: tuple[float, float], color=GOLD, alpha=1.0, width=2) -> None:
    x1, y1 = p1
    x2, y2 = p2
    draw.line((x1, y1, x2, y2), fill=rgba(color, alpha), width=width)
    ang = math.atan2(y2 - y1, x2 - x1)
    size = 10
    a1 = ang + math.pi * 0.82
    a2 = ang - math.pi * 0.82
    draw.polygon(
        [(x2, y2), (x2 + size * math.cos(a1), y2 + size * math.sin(a1)), (x2 + size * math.cos(a2), y2 + size * math.sin(a2))],
        fill=rgba(color, alpha),
    )


def scene_label(draw: ImageDraw.ImageDraw, index: int, title: str, alpha: float = 0.85) -> None:
    draw.text((42, 28), f"{index:02d}", font=FONT["xs"], fill=rgba(MUTED, alpha))
    draw.text((83, 27), title.upper(), font=FONT["xs"], fill=rgba(MUTED, alpha))


def vignette(im: Image.Image, strength: float = 0.25) -> Image.Image:
    # Disabled in the fast draft renderer; retained as an API hook.
    return im


def draw_silhouette(draw: ImageDraw.ImageDraw, cx: float, cy: float, scale: float, alpha: float = 1.0, color=INK) -> None:
    head_r = 28 * scale
    draw.ellipse((cx - head_r, cy - 120 * scale - head_r, cx + head_r, cy - 120 * scale + head_r), outline=rgba(color, alpha), width=max(1, int(3 * scale)))
    draw.rounded_rectangle((cx - 58 * scale, cy - 90 * scale, cx + 58 * scale, cy + 105 * scale), radius=int(28 * scale), outline=rgba(color, alpha), width=max(1, int(3 * scale)))
    draw.line((cx - 55 * scale, cy - 20 * scale, cx - 110 * scale, cy + 70 * scale), fill=rgba(color, alpha), width=max(1, int(3 * scale)))
    draw.line((cx + 55 * scale, cy - 20 * scale, cx + 110 * scale, cy + 70 * scale), fill=rgba(color, alpha), width=max(1, int(3 * scale)))
    draw.line((cx - 25 * scale, cy + 105 * scale, cx - 55 * scale, cy + 210 * scale), fill=rgba(color, alpha), width=max(1, int(3 * scale)))
    draw.line((cx + 25 * scale, cy + 105 * scale, cx + 55 * scale, cy + 210 * scale), fill=rgba(color, alpha), width=max(1, int(3 * scale)))


def draw_flower(draw: ImageDraw.ImageDraw, cx: float, cy: float, r: float, petals: int, color=GOLD, alpha=1.0, rotation: float = 0.0) -> None:
    pts = []
    for i in range(petals * 2):
        a = rotation + i * math.pi / petals
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    draw.line(pts + [pts[0]], fill=rgba(color, alpha), width=2)
    draw_dot(draw, cx, cy, 4, color, alpha)


def draw_tattva_grid(draw: ImageDraw.ImageDraw, reveal: float, highlight_group: int | None = None, add_labels: bool = True) -> None:
    # 36 nodes in six horizontal bands: 5 pure, 6 maya/coverings, purusha/prakriti, inner organ, senses/actions/subtle, gross elements.
    bands = [5, 6, 2, 3, 10, 10]
    names = ["pure", "māyā + kañcukas", "puruṣa / prakṛti", "inner organ", "senses + subtle", "gross + action"]
    y_positions = [110, 205, 300, 390, 495, 600]
    index = 0
    for band_idx, (count, y) in enumerate(zip(bands, y_positions)):
        x0, x1 = 190, 1090
        spacing = (x1 - x0) / max(1, count - 1)
        for j in range(count):
            node_u = smoothstep(index / 36, (index + 2) / 36, reveal)
            x = (x0 + x1) / 2 if count == 1 else x0 + spacing * j
            r = 7 if band_idx < 2 else 5
            c = GOLD if band_idx < 2 else INK
            a = node_u * (1.0 if highlight_group is None or highlight_group == band_idx else 0.25)
            draw_dot(draw, x, y, r, c, a)
            if j > 0:
                prev_x = x0 + spacing * (j - 1)
                draw.line((prev_x + r, y, x - r, y), fill=rgba(c, a * 0.35), width=1)
            if band_idx > 0 and j == count // 2:
                prev_count = bands[band_idx - 1]
                prev_spacing = (x1 - x0) / max(1, prev_count - 1)
                prev_x = (x0 + x1) / 2 if prev_count == 1 else x0 + prev_spacing * (prev_count // 2)
                draw.line((prev_x, y_positions[band_idx - 1] + 10, x, y - 10), fill=rgba(MUTED, a * 0.3), width=1)
            index += 1
        if add_labels:
            draw.text((45, y - 10), names[band_idx], font=FONT["xs"], fill=rgba(MUTED, 0.8))


@dataclass
class Scene:
    title: str
    duration: float
    fn: Callable[[float, float, int], Image.Image]
    note: str


class Film:
    def __init__(self, title: str, scenes: list[Scene], output: Path):
        self.title = title
        self.scenes = scenes
        self.output = output

    @property
    def duration(self) -> float:
        return sum(s.duration for s in self.scenes)

    def manifest(self) -> dict:
        t = 0.0
        rows = []
        for i, scene in enumerate(self.scenes, 1):
            rows.append({"index": i, "title": scene.title, "start": round(t, 3), "end": round(t + scene.duration, 3), "duration": scene.duration, "note": scene.note})
            t += scene.duration
        return {"title": self.title, "resolution": [W, H], "fps": FPS, "duration_seconds": self.duration, "scenes": rows}

    def render(self) -> None:
        self.output.parent.mkdir(parents=True, exist_ok=True)
        temp = self.output.with_suffix(".temp.mp4")
        writer = cv2.VideoWriter(str(temp), cv2.VideoWriter_fourcc(*"mp4v"), FPS, (W, H))
        if not writer.isOpened():
            raise RuntimeError(f"Could not open VideoWriter for {temp}")
        try:
            for scene_idx, scene in enumerate(self.scenes, 1):
                frames = max(1, int(scene.duration * FPS))
                for frame_idx in range(frames):
                    t = frame_idx / FPS
                    u = frame_idx / max(1, frames - 1)
                    im = scene.fn(t, u, scene_idx).convert("RGB")
                    arr = np.array(im)[:, :, ::-1]
                    writer.write(arr)
                print(f"Rendered {scene_idx:02d}/{len(self.scenes)}: {scene.title}", flush=True)
        finally:
            writer.release()
        # Transcode to browser-friendly H.264, with fast start. Fall back to mp4v if libx264 is unavailable.
        cmd = f"ffmpeg -y -loglevel error -i '{temp}' -c:v libx264 -pix_fmt yuv420p -preset veryfast -crf 21 -movflags +faststart '{self.output}'"
        rc = os.system(cmd)
        if rc != 0:
            temp.replace(self.output)
        else:
            temp.unlink(missing_ok=True)


# ----------------------------- 36 TATTVAS FILM -----------------------------

def tattva_01(t: float, u: float, idx: int) -> Image.Image:
    im = canvas(DARK)
    d = ImageDraw.Draw(im)
    scene_label(d, idx, "The unobservable point")
    cx, cy = W / 2, H / 2 + 10
    for i in range(6):
        r = 52 + i * 52 + 7 * math.sin(t * 0.45 + i)
        draw_ring(d, cx, cy, r, INK, smoothstep(0.05 + i * 0.035, 0.5 + i * 0.04, u) * (0.19 - i * 0.018), 1)
    draw_dot(d, cx, cy, 6 + 1.2 * math.sin(t * 0.8), GOLD, 1)
    a = smoothstep(0.08, 0.22, u)
    draw_centered(d, "THE ARCHITECTURE OF EXPERIENCE", 92, FONT["m"], INK, a)
    draw_centered(d, "३६ तत्त्वानि", 145, FONT["dev_l"], GOLD, smoothstep(0.18, 0.34, u))
    phrase = "Everything can be observed—except the point from which observation happens."
    draw_centered(d, phrase, 580, FONT["s"], INK, smoothstep(0.48, 0.68, u), 980)
    return vignette(im, 0.28)


def tattva_02(t: float, u: float, idx: int) -> Image.Image:
    im = canvas(WHITE)
    d = ImageDraw.Draw(im)
    scene_label(d, idx, "24 versus 36")
    a24 = smoothstep(0.05, 0.24, u)
    a36 = smoothstep(0.42, 0.62, u)
    d.text((235, 180), "24", font=FONT["xl"], fill=rgba(BLACK, a24))
    d.text((860, 180), "36", font=FONT["xl"], fill=rgba(CRIMSON, a36))
    d.text((195, 265), "SĀṄKHYA", font=FONT["m"], fill=rgba(MUTED, a24))
    d.text((845, 265), "TRIKA", font=FONT["m"], fill=rgba(MUTED, a36))
    for n in range(24):
        col = n % 6
        row = n // 6
        draw_dot(d, 170 + col * 55, 360 + row * 50, 4, BLACK, a24 * smoothstep(n / 28, (n + 4) / 28, u))
    for n in range(36):
        col = n % 6
        row = n // 6
        color = CRIMSON if n < 12 else BLACK
        draw_dot(d, 810 + col * 55, 335 + row * 43, 4, color, a36 * smoothstep(0.44 + n / 110, 0.52 + n / 110, u))
    draw_centered(d, "The 36 tattvas are the entrance point into Kashmir Śaivism.", 620, FONT["s"], BLACK, smoothstep(0.67, 0.82, u), 980)
    return im


def tattva_03(t: float, u: float, idx: int) -> Image.Image:
    im = canvas(DARK)
    d = ImageDraw.Draw(im)
    scene_label(d, idx, "Puruṣa, prakṛti, and the guṇas")
    draw_dot(d, 390, 170, 16, GOLD, smoothstep(0.05, 0.18, u))
    draw_centered(d, "puruṣa", 210, FONT["m"], GOLD, smoothstep(0.06, 0.2, u))
    draw_ring(d, 890, 170, 42 + 3 * math.sin(t * 0.5), CRIMSON, smoothstep(0.15, 0.28, u), 3)
    d.text((835, 216), "prakṛti", font=FONT["m"], fill=rgba(CRIMSON, smoothstep(0.15, 0.28, u)))
    streams = [("sattva", GOLD, -120), ("rajas", CRIMSON, 0), ("tamas", MUTED, 120)]
    for i, (name, color, dx) in enumerate(streams):
        a = smoothstep(0.28 + i * 0.12, 0.43 + i * 0.12, u)
        x = 640 + dx
        draw_arrow(d, (890, 230), (x, 460), color, a, 3)
        draw_ring(d, x, 515, 42 + 3 * math.sin(t * 0.7 + i), color, a, 2)
        w, _ = text_size(d, name, FONT["s"])
        d.text((x - w / 2, 570), name, font=FONT["s"], fill=rgba(color, a))
    draw_centered(d, "equilibrium   ·   motion   ·   structure", 630, FONT["xs"], INK, smoothstep(0.67, 0.83, u))
    return vignette(im, 0.22)


def tattva_04(t: float, u: float, idx: int) -> Image.Image:
    im = canvas(WHITE)
    d = ImageDraw.Draw(im)
    scene_label(d, idx, "The inner organ")
    cx, cy = W / 2, 360
    levels = [("buddhi", 210, GOLD), ("ahaṁkāra", 145, CRIMSON), ("manas", 80, BLACK)]
    for i, (name, r, color) in enumerate(levels):
        a = smoothstep(0.07 + i * 0.17, 0.25 + i * 0.17, u)
        draw_ring(d, cx, cy, r + 3 * math.sin(t * 0.4 + i), color, a, 3)
        d.text((cx + r + 28, cy - 13), name, font=FONT["m"], fill=rgba(color, a))
    draw_dot(d, cx, cy, 6, BLACK, smoothstep(0.52, 0.7, u))
    draw_centered(d, "antaḥkaraṇa", 100, FONT["m"], BLACK, smoothstep(0.05, 0.22, u))
    draw_centered(d, "discernment → self-reference → sensory processing", 626, FONT["s"], BLACK, smoothstep(0.68, 0.84, u), 980)
    return im


def tattva_05(t: float, u: float, idx: int) -> Image.Image:
    im = canvas(DARK)
    d = ImageDraw.Draw(im)
    scene_label(d, idx, "The 24-tattva base")
    reveal = smoothstep(0.03, 0.84, u)
    # Show only lower 24 with a clipped architecture.
    group_counts = [2, 3, 10, 9]
    group_names = ["puruṣa / prakṛti", "inner organ", "senses + actions", "subtle + gross elements"]
    ys = [170, 290, 420, 570]
    node_index = 0
    for gi, (count, y) in enumerate(zip(group_counts, ys)):
        x0, x1 = 220, 1060
        sp = (x1 - x0) / max(1, count - 1)
        for j in range(count):
            a = smoothstep(node_index / 28, (node_index + 3) / 28, reveal)
            x = (x0 + x1) / 2 if count == 1 else x0 + j * sp
            draw_dot(d, x, y, 6, GOLD if gi == 0 else INK, a)
            if j:
                d.line((x - sp + 8, y, x - 8, y), fill=rgba(MUTED, a * 0.45), width=1)
            node_index += 1
        d.text((45, y - 12), group_names[gi], font=FONT["xs"], fill=rgba(MUTED, 0.85))
    draw_centered(d, "A complete map of manifestation—yet consciousness itself remains unexplained.", 650, FONT["s"], INK, smoothstep(0.72, 0.88, u), 1050)
    return vignette(im, 0.2)


def tattva_06(t: float, u: float, idx: int) -> Image.Image:
    im = canvas(WHITE)
    d = ImageDraw.Draw(im)
    scene_label(d, idx, "The five pure tattvas")
    names = [("शिव", "Śiva"), ("शक्ति", "Śakti"), ("सदाशिव", "Sadāśiva"), ("ईश्वर", "Īśvara"), ("शुद्धविद्या", "Śuddhavidyā")]
    cx = W / 2
    for i, (dev, lat) in enumerate(names):
        y = 115 + i * 104
        a = smoothstep(0.06 + i * 0.13, 0.2 + i * 0.13, u)
        r = 7 + i * 2
        draw_dot(d, cx, y, r, GOLD if i < 2 else CRIMSON, a)
        if i:
            d.line((cx, y - 104 + 10, cx, y - 10), fill=rgba(MUTED, a * 0.55), width=2)
        d.text((cx + 36, y - 20), dev, font=FONT["dev_m"], fill=rgba(BLACK, a))
        d.text((cx + 190, y - 11), lat, font=FONT["s"], fill=rgba(MUTED, a))
    draw_left(d, "I", 260, 190, FONT["xl"], GOLD, smoothstep(0.18, 0.35, u))
    draw_left(d, "THIS", 930, 400, FONT["l"], CRIMSON, smoothstep(0.48, 0.66, u))
    draw_centered(d, "subject and object arise inside one field", 655, FONT["s"], BLACK, smoothstep(0.7, 0.86, u))
    return im


def tattva_07(t: float, u: float, idx: int) -> Image.Image:
    im = canvas(DARK)
    d = ImageDraw.Draw(im)
    scene_label(d, idx, "Māyā and the five kañcukas")
    cx, cy = W / 2, 375
    draw_silhouette(d, cx, cy, 0.9, 0.95, INK)
    names = ["kalā", "vidyā", "rāga", "kāla", "niyati"]
    for i, name in enumerate(names):
        a = smoothstep(0.12 + i * 0.12, 0.28 + i * 0.12, u)
        r = 116 + i * 45
        draw_ring(d, cx, cy, r - 6 * smoothstep(0.1, 0.9, u), CRIMSON if i in (2, 3) else GOLD, a * 0.74, 3)
        ang = -1.7 + i * 0.82
        x = cx + (r + 34) * math.cos(ang)
        y = cy + (r + 34) * math.sin(ang)
        w, _ = text_size(d, name, FONT["bold_s"])
        d.text((x - w / 2, y - 11), name, font=FONT["bold_s"], fill=rgba(INK, a))
    draw_centered(d, "The infinite becomes a bounded person.", 635, FONT["m"], INK, smoothstep(0.72, 0.88, u))
    return vignette(im, 0.25)


def tattva_08(t: float, u: float, idx: int) -> Image.Image:
    im = canvas(WHITE)
    d = ImageDraw.Draw(im)
    scene_label(d, idx, "Seven perceivers")
    names = ["śakala", "pralayākala", "vijñānākala", "mantra", "mantreśa", "sadāśiva", "Śiva"]
    for i, name in enumerate(names):
        a = smoothstep(0.05 + i * 0.095, 0.17 + i * 0.095, u)
        x = 125 + i * 172
        color = CRIMSON if i < 3 else GOLD
        draw_flower(d, x, 330, 44, 6, color, a, rotation=t * 0.1 + i * 0.3)
        w, _ = text_size(d, name, FONT["xs"])
        d.text((x - w / 2, 405), name, font=FONT["xs"], fill=rgba(BLACK, a))
        d.text((x - 4, 480), str(i + 1), font=FONT["xs"], fill=rgba(MUTED, a))
    draw_centered(d, "One reality. Seven modes of recognition.", 120, FONT["m"], BLACK, smoothstep(0.04, 0.2, u))
    draw_centered(d, "The universe becomes increasingly transparent to itself.", 585, FONT["s"], BLACK, smoothstep(0.72, 0.86, u), 1000)
    return im


def tattva_09(t: float, u: float, idx: int) -> Image.Image:
    im = canvas(DARK)
    d = ImageDraw.Draw(im)
    scene_label(d, idx, "Separate or recognize")
    split = lerp(200, 0, smoothstep(0.52, 0.84, u))
    d.line((W / 2, 120, W / 2, 600), fill=rgba(MUTED, 1 - smoothstep(0.5, 0.84, u)), width=2)
    draw_ring(d, W / 2 - split, 360, 125, GOLD, 0.85, 3)
    draw_ring(d, W / 2 + split, 360, 125, CRIMSON, 0.85, 3)
    if u < 0.52:
        d.text((180, 160), "puruṣa", font=FONT["l"], fill=rgba(GOLD, smoothstep(0.04, 0.22, u)))
        d.text((910, 160), "prakṛti", font=FONT["l"], fill=rgba(CRIMSON, smoothstep(0.04, 0.22, u)))
        draw_centered(d, "Sāṅkhya: separate", 620, FONT["s"], INK, smoothstep(0.25, 0.42, u))
    else:
        draw_dot(d, W / 2, 360, 9 + 2 * math.sin(t), INK, smoothstep(0.55, 0.72, u))
        draw_centered(d, "Trika: recognize", 620, FONT["m"], INK, smoothstep(0.55, 0.75, u))
    return vignette(im, 0.25)


def tattva_10(t: float, u: float, idx: int) -> Image.Image:
    im = canvas(WHITE)
    d = ImageDraw.Draw(im)
    scene_label(d, idx, "Why thirty-six?")
    draw_tattva_grid(d, smoothstep(0.02, 0.72, u), None, True)
    if u > 0.62:
        # close system into a circle
        a = smoothstep(0.62, 0.88, u)
        draw_ring(d, W / 2, 355, 310, CRIMSON, a * 0.5, 2)
        draw_ring(d, W / 2, 355, 340, GOLD, a * 0.55, 2)
        draw_centered(d, "The system accounts for the world, the knower, forgetting, and return.", 655, FONT["s"], BLACK, a, 1050)
    return im


def tattva_11(t: float, u: float, idx: int) -> Image.Image:
    im = canvas(DARK)
    d = ImageDraw.Draw(im)
    scene_label(d, idx, "The self-sealed system")
    cx, cy = W / 2, 360
    # Knot made of three looping paths.
    knot_alpha = 1.0 - smoothstep(0.52, 0.86, u)
    for phase, color in [(0.0, CRIMSON), (2.1, GOLD), (4.2, MUTED)]:
        pts = []
        for i in range(280):
            a = i / 279 * math.pi * 4
            r = 130 + 35 * math.sin(3 * a + phase)
            pts.append((cx + r * math.cos(a), cy + 0.62 * r * math.sin(a)))
        d.line(pts, fill=rgba(color, knot_alpha * 0.85), width=3)
    thread = smoothstep(0.18, 0.85, u)
    d.line((180, cy, lerp(180, 1100, thread), cy), fill=rgba(GOLD, 0.95), width=4)
    if u > 0.62:
        a = smoothstep(0.62, 0.9, u)
        for i in range(7):
            draw_ring(d, cx, cy, 45 + i * 46 + 4 * math.sin(t + i), GOLD, a * (0.42 - i * 0.045), 2)
    draw_centered(d, "Release is not acquiring something new.", 90, FONT["m"], INK, smoothstep(0.08, 0.24, u))
    draw_centered(d, "It is the relaxation of a contraction.", 625, FONT["s"], INK, smoothstep(0.72, 0.88, u))
    return vignette(im, 0.22)


def tattva_12(t: float, u: float, idx: int) -> Image.Image:
    bg_mix = smoothstep(0.7, 1.0, u)
    bg = tuple(int(lerp(DARK[i], WHITE[i], bg_mix)) for i in range(3))
    im = canvas(bg)
    d = ImageDraw.Draw(im)
    scene_label(d, idx, "Iti Śivam", 1 - bg_mix * 0.7)
    # cave aperture / manuscript lines
    a_cave = 1 - smoothstep(0.45, 0.82, u)
    d.arc((120, 60, 1160, 990), start=180, end=360, fill=rgba(INK, a_cave * 0.65), width=5)
    for i in range(6):
        y = 470 + i * 22
        d.line((340, y, 940, y), fill=rgba(MUTED, a_cave * (0.5 - i * 0.04)), width=2)
    cx, cy = W / 2, 340
    r = lerp(7, 920, smoothstep(0.44, 0.95, u))
    draw_dot(d, cx, cy, r, WHITE, smoothstep(0.38, 0.96, u))
    if u < 0.65:
        draw_centered(d, "The architecture of experience", 135, FONT["l"], INK, smoothstep(0.04, 0.24, u))
        draw_centered(d, "is the architecture of your own awareness.", 590, FONT["s"], INK, smoothstep(0.28, 0.5, u), 980)
    if u > 0.74:
        draw_centered(d, "इति शिवम्", 300, FONT["dev_xl"], BLACK, smoothstep(0.78, 0.95, u))
    return im


TATTVA_SCENES = [
    Scene("The unobservable point", 45, tattva_01, "Hook: bindu, observation, title."),
    Scene("24 versus 36", 45, tattva_02, "Compare Sāṅkhya and Trika counts."),
    Scene("Puruṣa, prakṛti, and the guṇas", 50, tattva_03, "Dual foundation and three guṇas."),
    Scene("The inner organ", 45, tattva_04, "Buddhi, ahaṁkāra, manas as nested functions."),
    Scene("The 24-tattva base", 55, tattva_05, "Lower architecture assembles."),
    Scene("The five pure tattvas", 50, tattva_06, "Śiva through Śuddhavidyā."),
    Scene("Māyā and the five kañcukas", 50, tattva_07, "Contraction rings around bounded figure."),
    Scene("Seven perceivers", 45, tattva_08, "One form shown through seven modes."),
    Scene("Separate or recognize", 50, tattva_09, "Dual separation resolves into recognition."),
    Scene("Why thirty-six?", 50, tattva_10, "Full map becomes self-sealed."),
    Scene("The self-sealed system", 45, tattva_11, "Māyā knot relaxes along a golden thread."),
    Scene("Iti Śivam", 50, tattva_12, "Return to source; expand into white."),
]


# ----------------------------- FIVE KAÑCUKAS FILM -----------------------------

def armor_title(t: float, u: float, idx: int) -> Image.Image:
    im = canvas(DARK)
    d = ImageDraw.Draw(im)
    scene_label(d, idx, "You're wearing armor")
    draw_silhouette(d, W / 2, 370, 1.0, smoothstep(0.06, 0.24, u), INK)
    # five plates descend around silhouette
    plates = [(-150, -95, 150, -40), (-150, -20, 150, 30), (-150, 55, 150, 110), (-100, 130, -15, 220), (15, 130, 100, 220)]
    for i, (x1, y1, x2, y2) in enumerate(plates):
        a = smoothstep(0.22 + i * 0.09, 0.34 + i * 0.09, u)
        drop = (1 - a) * 110
        d.rounded_rectangle((W / 2 + x1, 370 + y1 - drop, W / 2 + x2, 370 + y2 - drop), radius=14, outline=rgba(GOLD if i % 2 == 0 else CRIMSON, a), width=3)
    draw_centered(d, "YOU'RE WEARING ARMOR", 95, FONT["xl"], INK, smoothstep(0.05, 0.2, u))
    draw_centered(d, "five mechanisms between infinity and the person you take yourself to be", 625, FONT["s"], MUTED, smoothstep(0.72, 0.9, u), 1040)
    return vignette(im, 0.28)


def armor_five(t: float, u: float, idx: int) -> Image.Image:
    im = canvas(WHITE)
    d = ImageDraw.Draw(im)
    scene_label(d, idx, "Five mechanisms")
    names = [("कलā", "kalā", "limited agency"), ("विद्या", "vidyā", "limited knowledge"), ("राग", "rāga", "craving"), ("काल", "kāla", "time"), ("नियति", "niyati", "necessity")]
    for i, (dev, lat, gloss) in enumerate(names):
        y = 135 + i * 104
        a = smoothstep(0.05 + i * 0.13, 0.18 + i * 0.13, u)
        d.rounded_rectangle((165, y - 32, 1115, y + 38), radius=22, outline=rgba(CRIMSON if i in (2, 3) else GOLD, a), width=2)
        d.text((205, y - 24), dev, font=FONT["dev_m"], fill=rgba(BLACK, a))
        d.text((410, y - 16), lat, font=FONT["bold_s"], fill=rgba(BLACK, a))
        d.text((670, y - 16), gloss, font=FONT["s"], fill=rgba(MUTED, a))
    return im


def armor_knot(t: float, u: float, idx: int) -> Image.Image:
    im = canvas(DARK)
    d = ImageDraw.Draw(im)
    scene_label(d, idx, "Māyāgranthi")
    cx, cy = W / 2, 360
    for phase, color in [(0.0, CRIMSON), (2.0, GOLD), (4.1, MUTED)]:
        pts = []
        for i in range(300):
            a = i / 299 * math.pi * 5
            r = 120 + 42 * math.sin(2.5 * a + phase)
            pts.append((cx + r * math.cos(a), cy + 0.66 * r * math.sin(a)))
        d.line(pts, fill=rgba(color, 0.78), width=3)
    draw_centered(d, "मायाग्रन्थि", 100, FONT["dev_l"], GOLD, smoothstep(0.05, 0.2, u))
    draw_centered(d, "A knot pulls tighter the more you wrestle it.", 610, FONT["m"], INK, smoothstep(0.65, 0.82, u))
    return vignette(im, 0.25)


def armor_quote(t: float, u: float, idx: int) -> Image.Image:
    im = canvas(WHITE)
    d = ImageDraw.Draw(im)
    scene_label(d, idx, "The five obscuring coverings")
    quote = "The five obscuring coverings are limited agency, limited noetic subjectivity, craving, temporal differentiation, and necessity."
    draw_centered(d, "“", 70, FONT["xl"], GOLD, smoothstep(0.04, 0.18, u))
    draw_centered(d, quote, 205, FONT["l"], BLACK, smoothstep(0.12, 0.36, u), 1000, 15)
    d.line((300, 555, 980, 555), fill=rgba(CRIMSON, smoothstep(0.48, 0.7, u)), width=2)
    draw_centered(d, "Mālinīvijayavārttika tradition — paraphrased from the supplied text", 585, FONT["xs"], MUTED, smoothstep(0.55, 0.74, u), 970)
    return im


def kancuka_card(title_dev: str, title_lat: str, gloss: str, metaphor: str, mechanism: str, color: tuple[int, int, int]):
    def _fn(t: float, u: float, idx: int) -> Image.Image:
        im = canvas(DARK)
        d = ImageDraw.Draw(im)
        scene_label(d, idx, title_lat)
        draw_centered(d, title_dev, 85, FONT["dev_xl"], color, smoothstep(0.05, 0.2, u))
        draw_centered(d, title_lat.upper(), 190, FONT["l"], INK, smoothstep(0.1, 0.25, u))
        draw_centered(d, gloss, 250, FONT["m"], MUTED, smoothstep(0.2, 0.36, u))
        # mechanism glyph
        cx, cy = W / 2, 425
        if mechanism == "agency":
            for i in range(5):
                a = smoothstep(0.28 + i * 0.06, 0.42 + i * 0.06, u)
                length = 55 + i * 42
                d.line((cx - length, cy, cx + length, cy), fill=rgba(color, a), width=3)
                d.line((cx + length, cy, cx + length - 14, cy - 9), fill=rgba(color, a), width=3)
                d.line((cx + length, cy, cx + length - 14, cy + 9), fill=rgba(color, a), width=3)
        elif mechanism == "knowledge":
            draw_ring(d, cx, cy, 110, color, smoothstep(0.3, 0.5, u), 3)
            d.arc((cx - 190, cy - 80, cx + 190, cy + 80), start=200, end=340, fill=rgba(color, smoothstep(0.38, 0.56, u)), width=4)
            draw_dot(d, cx, cy, 8, color, smoothstep(0.45, 0.62, u))
        elif mechanism == "craving":
            for i in range(6):
                a = smoothstep(0.28 + i * 0.055, 0.42 + i * 0.055, u)
                r = 165 - i * 24
                d.arc((cx - r, cy - r, cx + r, cy + r), start=210, end=330, fill=rgba(color, a), width=3)
            draw_dot(d, cx, cy + 40, 8, INK, smoothstep(0.6, 0.75, u))
        elif mechanism == "time":
            draw_ring(d, cx, cy, 125, color, smoothstep(0.3, 0.48, u), 3)
            for i in range(12):
                a = i / 12 * math.tau
                x1, y1 = cx + 105 * math.cos(a), cy + 105 * math.sin(a)
                x2, y2 = cx + 122 * math.cos(a), cy + 122 * math.sin(a)
                d.line((x1, y1, x2, y2), fill=rgba(color, smoothstep(0.36, 0.53, u)), width=2)
            ang = -math.pi / 2 + t * 0.23
            d.line((cx, cy, cx + 85 * math.cos(ang), cy + 85 * math.sin(ang)), fill=rgba(color, 0.95), width=4)
        elif mechanism == "necessity":
            for i in range(5):
                a = smoothstep(0.28 + i * 0.07, 0.42 + i * 0.07, u)
                x = cx - 160 + i * 80
                draw_ring(d, x, cy, 38, color, a, 3)
                if i:
                    d.line((x - 80 + 38, cy, x - 38, cy), fill=rgba(color, a), width=3)
        draw_centered(d, metaphor, 620, FONT["s"], INK, smoothstep(0.68, 0.86, u), 1050)
        return vignette(im, 0.2)
    return _fn


def armor_mirror(t: float, u: float, idx: int) -> Image.Image:
    im = canvas(WHITE)
    d = ImageDraw.Draw(im)
    scene_label(d, idx, "Vidyā as mirror")
    cx, cy = W / 2, 365
    # eye / mirror
    d.arc((cx - 250, cy - 110, cx + 250, cy + 110), start=195, end=345, fill=rgba(BLACK, smoothstep(0.05, 0.24, u)), width=4)
    d.arc((cx - 250, cy - 110, cx + 250, cy + 110), start=15, end=165, fill=rgba(BLACK, smoothstep(0.05, 0.24, u)), width=4)
    draw_ring(d, cx, cy, 70, CRIMSON, smoothstep(0.2, 0.4, u), 3)
    draw_dot(d, cx, cy, 8, BLACK, smoothstep(0.28, 0.48, u))
    # reflection axis
    d.line((cx, 130, cx, 600), fill=rgba(GOLD, smoothstep(0.42, 0.62, u)), width=2)
    draw_centered(d, "An eye cannot see itself without a mirror.", 100, FONT["m"], BLACK, smoothstep(0.05, 0.2, u))
    draw_centered(d, "Vidyā is the capacity to watch your own watching.", 610, FONT["s"], BLACK, smoothstep(0.67, 0.84, u), 980)
    return im


def armor_timestamp(t: float, u: float, idx: int) -> Image.Image:
    im = canvas(DARK)
    d = ImageDraw.Draw(im)
    scene_label(d, idx, "The cage of just now")
    # repeated timestamps become bars
    for i in range(12):
        a = smoothstep(0.04 + i * 0.045, 0.14 + i * 0.045, u)
        x = 90 + i * 95
        d.line((x, 140, x, 585), fill=rgba(CRIMSON if i % 3 == 0 else MUTED, a * 0.72), width=2)
        d.text((x - 26, 600), f"{i:02d}", font=FONT["xs"], fill=rgba(MUTED, a))
    draw_silhouette(d, W / 2, 360, 0.75, smoothstep(0.2, 0.4, u), INK)
    draw_centered(d, "The words “just now” are a cage.", 85, FONT["l"], INK, smoothstep(0.06, 0.22, u))
    return vignette(im, 0.25)


def armor_fist(t: float, u: float, idx: int) -> Image.Image:
    im = canvas(WHITE)
    d = ImageDraw.Draw(im)
    scene_label(d, idx, "Contraction carries life")
    cx, cy = W / 2, 370
    # five closing arcs like fingers
    for i in range(5):
        a = smoothstep(0.08 + i * 0.08, 0.22 + i * 0.08, u)
        r = 170 - i * 22
        start = lerp(205, 245, a)
        end = lerp(335, 295, a)
        d.arc((cx - r, cy - r, cx + r, cy + r), start=start, end=end, fill=rgba(CRIMSON if i < 2 else GOLD, a), width=5)
    for i in range(8):
        draw_ring(d, cx, cy, 30 + i * 27 + 3 * math.sin(t + i), GOLD, smoothstep(0.45, 0.75, u) * (0.34 - i * 0.032), 2)
    draw_centered(d, "The fist that closes also brings blood to the palm.", 90, FONT["m"], BLACK, smoothstep(0.05, 0.2, u), 980)
    draw_centered(d, "Even limitation is a form of energy.", 620, FONT["s"], BLACK, smoothstep(0.68, 0.84, u))
    return im


def armor_hunger(t: float, u: float, idx: int) -> Image.Image:
    im = canvas(DARK)
    d = ImageDraw.Draw(im)
    scene_label(d, idx, "Rāga")
    cx, cy = W / 2, 370
    # grasping hands as converging lines
    for side in (-1, 1):
        for i in range(5):
            a = smoothstep(0.08 + i * 0.07, 0.22 + i * 0.07, u)
            start_x = cx + side * 520
            start_y = 240 + i * 62
            end_x = cx + side * (130 + i * 8)
            end_y = cy - 65 + i * 32
            d.line((start_x, start_y, end_x, end_y), fill=rgba(CRIMSON, a), width=3)
    draw_dot(d, cx, cy, 7, GOLD, smoothstep(0.34, 0.52, u))
    draw_centered(d, "Hunger is how the contracted self feels its own shape.", 90, FONT["m"], INK, smoothstep(0.05, 0.22, u), 1000)
    draw_centered(d, "by grasping · wanting · not-yet", 620, FONT["s"], MUTED, smoothstep(0.68, 0.86, u))
    return vignette(im, 0.24)


def armor_states(t: float, u: float, idx: int) -> Image.Image:
    im = canvas(WHITE)
    d = ImageDraw.Draw(im)
    scene_label(d, idx, "States and perceivers")
    states = ["waking", "dreaming", "deep sleep", "the Fourth", "beyond"]
    for i, state in enumerate(states):
        a = smoothstep(0.05 + i * 0.13, 0.19 + i * 0.13, u)
        x = 150 + i * 245
        r = 32 + i * 13
        draw_ring(d, x, 350, r, CRIMSON if i < 3 else GOLD, a, 3)
        draw_dot(d, x, 350, 4, BLACK, a)
        w, _ = text_size(d, state, FONT["xs"])
        d.text((x - w / 2, 440), state, font=FONT["xs"], fill=rgba(BLACK, a))
    draw_centered(d, "The restraints reconfigure as consciousness moves through its own states.", 585, FONT["s"], BLACK, smoothstep(0.7, 0.86, u), 1040)
    return im


def armor_night(t: float, u: float, idx: int) -> Image.Image:
    im = canvas(DARK)
    d = ImageDraw.Draw(im)
    scene_label(d, idx, "Māyā as night")
    # sun moves behind a dark disc, stars appear
    sun_x, sun_y = 640, 330
    draw_dot(d, sun_x, sun_y, 96, GOLD, smoothstep(0.05, 0.2, u))
    cover = smoothstep(0.2, 0.62, u)
    draw_dot(d, lerp(920, sun_x + 6, cover), sun_y, 105, DARK_2, 1)
    rng = np.random.default_rng(7)
    for i in range(80):
        x = float(rng.integers(60, W - 60))
        y = float(rng.integers(80, H - 80))
        draw_dot(d, x, y, float(rng.uniform(0.6, 1.8)), INK, smoothstep(0.45, 0.8, u) * float(rng.uniform(0.25, 0.8)))
    draw_centered(d, "Night: the sun's own turning away from itself.", 90, FONT["m"], INK, smoothstep(0.05, 0.22, u))
    draw_centered(d, "The same turning makes stars visible.", 620, FONT["s"], INK, smoothstep(0.66, 0.83, u))
    return vignette(im, 0.3)


def armor_signature(t: float, u: float, idx: int) -> Image.Image:
    im = canvas(WHITE)
    d = ImageDraw.Draw(im)
    scene_label(d, idx, "No two souls wear the same armor")
    rng = np.random.default_rng(11)
    for j in range(5):
        cx = 150 + j * 245
        cy = 360
        draw_silhouette(d, cx, cy, 0.36, smoothstep(0.05 + j * 0.08, 0.2 + j * 0.08, u), BLACK)
        for i in range(5):
            a = smoothstep(0.22 + j * 0.06 + i * 0.025, 0.38 + j * 0.06 + i * 0.025, u)
            r = 48 + i * 13 + float(rng.integers(-7, 8))
            draw_ring(d, cx, cy, r, CRIMSON if (i + j) % 2 else GOLD, a * 0.72, 2)
    draw_centered(d, "Your limits are your signature.", 90, FONT["l"], BLACK, smoothstep(0.05, 0.22, u))
    draw_centered(d, "Each configuration produces a different world of joy and suffering.", 620, FONT["s"], BLACK, smoothstep(0.7, 0.86, u), 1040)
    return im


def armor_time_slice(t: float, u: float, idx: int) -> Image.Image:
    im = canvas(DARK)
    d = ImageDraw.Draw(im)
    scene_label(d, idx, "Time as a gesture")
    # eternal line, sliced progressively
    y = 350
    d.line((100, y, 1180, y), fill=rgba(GOLD, smoothstep(0.04, 0.2, u)), width=5)
    for i in range(17):
        a = smoothstep(0.2 + i * 0.025, 0.3 + i * 0.025, u)
        x = 135 + i * 63
        d.line((x, y - 95, x, y + 95), fill=rgba(CRIMSON, a * 0.82), width=2)
    draw_centered(d, "Time is a slicing of the eternal into manageable pieces.", 90, FONT["m"], INK, smoothstep(0.05, 0.22, u), 1000)
    draw_centered(d, "The clock ticks because awareness permits it.", 620, FONT["s"], INK, smoothstep(0.69, 0.85, u))
    return vignette(im, 0.22)


def armor_garment(t: float, u: float, idx: int) -> Image.Image:
    im = canvas(WHITE)
    d = ImageDraw.Draw(im)
    scene_label(d, idx, "Karma woven into form")
    # weave lattice then silhouette emerges
    for i in range(19):
        a = smoothstep(0.03 + i * 0.02, 0.12 + i * 0.02, u)
        x = 130 + i * 57
        d.line((x, 105, x, 615), fill=rgba(GOLD if i % 2 else MUTED, a * 0.45), width=2)
    for j in range(10):
        a = smoothstep(0.2 + j * 0.025, 0.3 + j * 0.025, u)
        y = 130 + j * 52
        d.line((95, y, 1185, y), fill=rgba(CRIMSON if j % 3 == 0 else MUTED, a * 0.42), width=2)
    draw_silhouette(d, W / 2, 360, 0.86, smoothstep(0.45, 0.68, u), BLACK)
    draw_centered(d, "The body: a garment woven from the same thread as the armor.", 620, FONT["s"], BLACK, smoothstep(0.68, 0.84, u), 1050)
    return im


def armor_release(t: float, u: float, idx: int) -> Image.Image:
    bg_mix = smoothstep(0.75, 1.0, u)
    bg = tuple(int(lerp(DARK[i], WHITE[i], bg_mix)) for i in range(3))
    im = canvas(bg)
    d = ImageDraw.Draw(im)
    scene_label(d, idx, "The coverings cut both ways", 1 - bg_mix * 0.65)
    cx, cy = W / 2, 370
    draw_silhouette(d, cx, cy, 0.88, 1 - smoothstep(0.62, 0.92, u), INK)
    for i in range(5):
        a = 1 - smoothstep(0.18 + i * 0.08, 0.58 + i * 0.08, u)
        draw_ring(d, cx, cy, 130 + i * 47 + 6 * math.sin(t * 0.6 + i), CRIMSON if i in (2, 3) else GOLD, a * 0.75, 3)
    for i in range(9):
        a = smoothstep(0.42, 0.86, u) * (0.42 - i * 0.038)
        draw_ring(d, cx, cy, 42 + i * 48, GOLD, a, 2)
    if u < 0.58:
        draw_centered(d, "They hide the infinite.", 100, FONT["l"], INK, smoothstep(0.05, 0.22, u))
    if u > 0.46:
        draw_centered(d, "They also make the finite livable, beautiful, and temporary.", 600, FONT["s"], INK if bg_mix < 0.6 else BLACK, smoothstep(0.5, 0.72, u), 1050)
    if u > 0.79:
        draw_centered(d, "UNARMORED · UNBOUND · ALWAYS", 320, FONT["l"], BLACK, smoothstep(0.82, 0.97, u))
    return im


ARMOR_SCENES = [
    Scene("You're wearing armor", 30, armor_title, "Five plates descend around a bounded figure."),
    Scene("Five mechanisms", 40, armor_five, "Introduce kalā, vidyā, rāga, kāla, niyati."),
    Scene("Māyāgranthi", 35, armor_knot, "Māyā as knot; struggling tightens it."),
    Scene("The five obscuring coverings", 30, armor_quote, "Quote card from supplied text."),
    Scene("Kalā", 30, kancuka_card("कला", "kalā", "limited agency", "You can only lift so much. Beneath it: the power to lift anything.", "agency", GOLD), "Limited agency."),
    Scene("Vidyā", 30, kancuka_card("विद्या", "vidyā", "limited knowledge", "You see a sliver. Beneath it: the capacity to see through.", "knowledge", GOLD), "Limited knowledge."),
    Scene("Rāga", 30, kancuka_card("राग", "rāga", "craving", "You reach for what you lack. Beneath it: fullness.", "craving", CRIMSON), "Craving."),
    Scene("Kāla", 30, kancuka_card("काल", "kāla", "time", "You move from A to B. Beneath it: the present that never moves.", "time", CRIMSON), "Time."),
    Scene("Niyati", 30, kancuka_card("नियति", "niyati", "necessity", "You reap what you sow. Beneath it: freedom.", "necessity", GOLD), "Necessity."),
    Scene("Vidyā as mirror", 40, armor_mirror, "The intellect requires a mirror for self-observation."),
    Scene("The cage of just now", 35, armor_timestamp, "Temporal stamping as cage."),
    Scene("Contraction carries life", 35, armor_fist, "The fist and the pulse within contraction."),
    Scene("Rāga as hunger", 35, armor_hunger, "Grasping reveals the contracted self's contour."),
    Scene("States and perceivers", 35, armor_states, "Waking, dream, sleep, fourth, beyond."),
    Scene("Māyā as night", 40, armor_night, "Obscuration makes stars visible."),
    Scene("Unique armor", 35, armor_signature, "No two souls wear the same configuration."),
    Scene("Time as a gesture", 35, armor_time_slice, "Consciousness slices eternity into moments."),
    Scene("Karma woven into form", 40, armor_garment, "Body and instruments woven with coverings."),
    Scene("Unarmored", 45, armor_release, "Armor dissolves into an expanding field."),
]


def build_film(kind: str, out_dir: Path) -> Film:
    if kind == "tattvas":
        return Film("The 36 Tattvas — The Architecture of Experience", TATTVA_SCENES, out_dir / "36_tattvas_minimal_animation.mp4")
    if kind == "armor":
        return Film("You're Wearing Armor — The Five Kañcukas", ARMOR_SCENES, out_dir / "five_kancukas_armor_animation.mp4")
    raise ValueError(kind)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("kind", choices=["tattvas", "armor", "both"])
    parser.add_argument("--out-dir", default="/mnt/data/tantra_animation_packs")
    args = parser.parse_args()
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    kinds = ["tattvas", "armor"] if args.kind == "both" else [args.kind]
    for kind in kinds:
        film = build_film(kind, out_dir)
        manifest_path = out_dir / f"{kind}_scene_manifest.json"
        manifest_path.write_text(json.dumps(film.manifest(), ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Rendering {film.title}: {film.duration:.1f}s", flush=True)
        film.render()
        print(f"Saved {film.output}", flush=True)


if __name__ == "__main__":
    main()

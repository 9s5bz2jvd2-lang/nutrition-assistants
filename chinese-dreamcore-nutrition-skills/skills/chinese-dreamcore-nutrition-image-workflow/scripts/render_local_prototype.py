#!/usr/bin/env python3
"""Render a no-text Chinese-dreamcore nutrition prototype PNG with only stdlib.

This is a fallback prototype renderer, not a true image-generation model.
It creates a soft 4:5 base image so the workflow can produce a tangible file
when no external image backend is configured.
"""
from __future__ import annotations
import argparse, json, math, struct, time, zlib
from pathlib import Path

W, H = 1080, 1350

def clamp(x):
    return max(0, min(255, int(x)))

def blend(buf, x, y, color, a=1.0):
    if x < 0 or y < 0 or x >= W or y >= H:
        return
    i = (y * W + x) * 3
    r, g, b = color
    ia = 1.0 - a
    buf[i] = clamp(buf[i] * ia + r * a)
    buf[i+1] = clamp(buf[i+1] * ia + g * a)
    buf[i+2] = clamp(buf[i+2] * ia + b * a)

def fill_rect(buf, x0, y0, x1, y1, color, a=1.0):
    for y in range(max(0, y0), min(H, y1)):
        for x in range(max(0, x0), min(W, x1)):
            blend(buf, x, y, color, a)

def fill_ellipse(buf, cx, cy, rx, ry, color, a=1.0):
    x0, x1 = int(cx-rx), int(cx+rx)
    y0, y1 = int(cy-ry), int(cy+ry)
    for y in range(max(0, y0), min(H, y1+1)):
        yy = ((y-cy)/ry)**2
        if yy > 1: continue
        span = int(rx * math.sqrt(1-yy))
        for x in range(max(0, cx-span), min(W, cx+span+1)):
            blend(buf, x, y, color, a)

def stroke_ellipse(buf, cx, cy, rx, ry, color, width=6, a=1.0):
    for t in range(0, 3600):
        ang = t * math.pi / 1800
        x = int(cx + rx * math.cos(ang))
        y = int(cy + ry * math.sin(ang))
        for dy in range(-width//2, width//2+1):
            for dx in range(-width//2, width//2+1):
                if dx*dx + dy*dy <= (width//2+1)**2:
                    blend(buf, x+dx, y+dy, color, a)

def line(buf, x0, y0, x1, y1, color, width=2, a=1.0):
    steps = max(abs(x1-x0), abs(y1-y0), 1)
    for s in range(steps+1):
        x = int(x0 + (x1-x0)*s/steps)
        y = int(y0 + (y1-y0)*s/steps)
        for dy in range(-width//2, width//2+1):
            for dx in range(-width//2, width//2+1):
                blend(buf, x+dx, y+dy, color, a)

def save_png(path, buf):
    raw = bytearray()
    for y in range(H):
        raw.append(0)
        raw.extend(buf[y*W*3:(y+1)*W*3])
    def chunk(tag, data):
        import binascii
        return struct.pack('>I', len(data)) + tag + data + struct.pack('>I', binascii.crc32(tag + data) & 0xffffffff)
    png = b'\x89PNG\r\n\x1a\n'
    png += chunk(b'IHDR', struct.pack('>IIBBBBB', W, H, 8, 2, 0, 0, 0))
    png += chunk(b'IDAT', zlib.compress(bytes(raw), 9))
    png += chunk(b'IEND', b'')
    Path(path).write_bytes(png)

def render(outdir: Path, topic_id: str, title: str):
    buf = bytearray(W * H * 3)
    # warm paper gradient
    for y in range(H):
        for x in range(W):
            t = y / H
            i = (y*W+x)*3
            buf[i] = clamp(250 - 18*t)
            buf[i+1] = clamp(239 - 12*t)
            buf[i+2] = clamp(218 - 6*t)
    # soft jade shadow and moon gate
    fill_ellipse(buf, 540, 500, 420, 420, (236, 245, 231), 0.45)
    stroke_ellipse(buf, 540, 500, 420, 420, (189, 166, 125), 7, 0.38)
    fill_rect(buf, 0, 955, W, H, (179, 137, 91), 0.28)
    fill_rect(buf, 0, 1000, W, H, (142, 102, 69), 0.15)
    # bamboo curtain left and paper-cut shadows
    for x in range(80, 255, 22):
        line(buf, x, 80, x+18, 880, (122, 143, 105), 3, 0.23)
    for y in range(130, 820, 95):
        line(buf, 70, y, 285, y+18, (122, 143, 105), 2, 0.16)
    # porcelain plate and cute food object
    fill_ellipse(buf, 680, 930, 260, 92, (255, 252, 241), 0.95)
    stroke_ellipse(buf, 680, 930, 260, 92, (202, 190, 170), 5, 0.35)
    fill_ellipse(buf, 680, 805, 150, 145, (205, 75, 55), 0.94)
    fill_ellipse(buf, 730, 775, 70, 62, (242, 171, 107), 0.32)
    fill_ellipse(buf, 640, 780, 58, 48, (255, 221, 153), 0.20)
    line(buf, 680, 660, 708, 715, (87, 70, 46), 8, 0.75)
    fill_ellipse(buf, 735, 692, 58, 25, (108, 145, 91), 0.78)
    # steam / dream motes
    for k, sx in enumerate([525, 600, 760, 835]):
        for p in range(80):
            y = 650 - p*5
            x = int(sx + math.sin(p/10 + k) * 18)
            blend(buf, x, y, (255, 255, 255), 0.18)
            blend(buf, x+1, y, (255, 255, 255), 0.12)
    for k in range(55):
        x = (97*k*k + 233) % W
        y = (131*k + 211) % 880 + 60
        fill_ellipse(buf, x, y, 3 + (k % 5), 3 + (k % 5), (255, 255, 245), 0.18)
    # safe blank area glow for later Chinese typography
    fill_rect(buf, 340, 115, 980, 360, (255, 250, 236), 0.35)
    outdir.mkdir(parents=True, exist_ok=True)
    png = outdir / 'selected_base_prototype.png'
    save_png(png, buf)
    (outdir / 'prompt_used.md').write_text(f"# Local prototype prompt\n\nTopic: {topic_id}\nTitle: {title}\n\nMode: local no-model prototype renderer. This is not a true image-generation-model output.\n", encoding='utf-8')
    (outdir / 'review_note.md').write_text(f"# Review note\n\n- topic_id: {topic_id}\n- title: {title}\n- output: {png.name}\n- status: local prototype only; not a true image-generation-model result.\n- next: replace with 9 real no-text base images when a real image backend is configured, then run Cute Gate.\n", encoding='utf-8')
    (outdir / 'render_manifest.json').write_text(json.dumps({"topic_id": topic_id, "title": title, "output": str(png), "mode": "local_prototype", "generated_at": time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}, ensure_ascii=False, indent=2), encoding='utf-8')
    print(png)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--topic-id', required=True)
    ap.add_argument('--title', required=True)
    ap.add_argument('--outdir', required=True)
    args = ap.parse_args()
    render(Path(args.outdir), args.topic_id, args.title)

if __name__ == '__main__':
    main()

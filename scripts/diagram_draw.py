# -*- coding: utf-8 -*-
"""학습 일지용 도식. 참고 스택프레임 그림이랑 같은 톤."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

BG = (255, 255, 255)
HEADER = (92, 92, 92)
HEADER_TEXT = (255, 255, 255)
LINE = (214, 214, 214)
BORDER = (186, 186, 186)
TEXT = (28, 28, 28)
MUTED = (90, 90, 90)
CELL = (252, 252, 252)
ACCENT = (245, 245, 245)
BOX_FILL = (255, 255, 255)
ARROW = (92, 92, 92)

FONT_BD = Path(r"C:\Windows\Fonts\malgunbd.ttf")
FONT_RG = Path(r"C:\Windows\Fonts\malgun.ttf")


def font(size: int, bold: bool = True) -> ImageFont.FreeTypeFont:
    path = FONT_BD if bold and FONT_BD.exists() else FONT_RG
    return ImageFont.truetype(str(path), size)


def measure(draw: ImageDraw.ImageDraw, text: str, f: ImageFont.FreeTypeFont) -> tuple[int, int]:
    b = draw.textbbox((0, 0), text, font=f)
    return b[2] - b[0], b[3] - b[1]


def wrap(draw: ImageDraw.ImageDraw, text: str, f: ImageFont.FreeTypeFont, max_w: int) -> list[str]:
    text = text.strip()
    if measure(draw, text, f)[0] <= max_w:
        return [text]
    # prefer splitting on space / slash / comma
    for sep in [" / ", " -> ", " → ", ", ", " "]:
        if sep in text:
            parts = text.split(sep)
            lines, cur = [], ""
            for i, p in enumerate(parts):
                piece = p if not cur else cur + sep + p
                if measure(draw, piece, f)[0] <= max_w:
                    cur = piece
                else:
                    if cur:
                        lines.append(cur)
                    cur = p
            if cur:
                lines.append(cur)
            return lines or [text]
    lines, cur = [], ""
    for ch in text:
        trial = cur + ch
        if measure(draw, trial, f)[0] <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = ch
    if cur:
        lines.append(cur)
    return lines or [text]


def draw_center(draw: ImageDraw.ImageDraw, xy_box, text: str, f, fill=TEXT):
    x0, y0, x1, y1 = xy_box
    lines = wrap(draw, text, f, max(20, x1 - x0 - 24))
    lh = measure(draw, "가", f)[1] + 8
    total = lh * len(lines) - 8
    y = y0 + (y1 - y0 - total) / 2
    for line in lines:
        w, h = measure(draw, line, f)
        draw.text(((x0 + x1 - w) / 2, y), line, font=f, fill=fill)
        y += lh


def header(draw: ImageDraw.ImageDraw, w: int, title: str, h: int = 62) -> int:
    draw.rectangle([0, 0, w, h], fill=HEADER)
    f = font(28, True)
    tw, th = measure(draw, title, f)
    draw.text(((w - tw) / 2, (h - th) / 2 - 2), title, font=f, fill=HEADER_TEXT)
    return h


def frame(draw: ImageDraw.ImageDraw, w: int, h: int):
    draw.rectangle([0, 0, w - 1, h - 1], outline=BORDER, width=2)


def save(img: Image.Image, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, "PNG")


def stack(title: str, rows: list[str], width: int = 900) -> Image.Image:
    row_h = 86 if len(rows) <= 6 else 72
    hh = 62
    h = hh + row_h * len(rows)
    img = Image.new("RGB", (width, h), BG)
    d = ImageDraw.Draw(img)
    header(d, width, title, hh)
    f = font(26, True)
    for i, row in enumerate(rows):
        y0 = hh + i * row_h
        y1 = y0 + row_h
        d.rectangle([0, y0, width, y1], fill=CELL if i % 2 == 0 else BG)
        d.line([(0, y0), (width, y0)], fill=LINE, width=1)
        draw_center(d, (0, y0, width, y1), row, f)
    frame(d, width, h)
    return img


def hflow(title: str, steps: list[str], width: int = 1100) -> Image.Image:
    hh = 62
    n = len(steps)
    pad = 28
    gap = 36
    box_w = (width - pad * 2 - gap * (n - 1)) // n
    box_h = 120
    h = hh + 40 + box_h + 28
    img = Image.new("RGB", (width, h), BG)
    d = ImageDraw.Draw(img)
    header(d, width, title, hh)
    f = font(22, True)
    y0 = hh + 36
    for i, step in enumerate(steps):
        x0 = pad + i * (box_w + gap)
        x1 = x0 + box_w
        d.rounded_rectangle([x0, y0, x1, y0 + box_h], radius=10, fill=ACCENT, outline=BORDER, width=2)
        draw_center(d, (x0, y0, x1, y0 + box_h), step, f)
        if i < n - 1:
            ax0 = x1 + 6
            ax1 = x1 + gap - 6
            mid = y0 + box_h / 2
            d.line([(ax0, mid), (ax1 - 8, mid)], fill=ARROW, width=4)
            d.polygon([(ax1, mid), (ax1 - 14, mid - 8), (ax1 - 14, mid + 8)], fill=ARROW)
    frame(d, width, h)
    return img


def vflow(title: str, steps: list[str], width: int = 900) -> Image.Image:
    hh = 62
    box_h = 70
    gap = 28
    pad = 40
    h = hh + 24 + len(steps) * box_h + (len(steps) - 1) * gap + 24
    img = Image.new("RGB", (width, h), BG)
    d = ImageDraw.Draw(img)
    header(d, width, title, hh)
    f = font(24, True)
    y = hh + 24
    for i, step in enumerate(steps):
        d.rounded_rectangle([pad, y, width - pad, y + box_h], radius=8, fill=ACCENT, outline=BORDER, width=2)
        draw_center(d, (pad, y, width - pad, y + box_h), step, f)
        if i < len(steps) - 1:
            mx = width / 2
            y1 = y + box_h
            d.line([(mx, y1 + 2), (mx, y1 + gap - 10)], fill=ARROW, width=4)
            d.polygon([(mx, y1 + gap - 2), (mx - 8, y1 + gap - 16), (mx + 8, y1 + gap - 16)], fill=ARROW)
        y += box_h + gap
    frame(d, width, h)
    return img


def two_col(title: str, left: tuple[str, list[str]], right: tuple[str, list[str]], width: int = 1100) -> Image.Image:
    hh = 62
    col_h_title = 48
    rows = max(len(left[1]), len(right[1]), 1)
    row_h = 56
    body = col_h_title + rows * row_h + 24
    h = hh + 20 + body + 16
    img = Image.new("RGB", (width, h), BG)
    d = ImageDraw.Draw(img)
    header(d, width, title, hh)
    mid = width // 2
    pad = 24
    y0 = hh + 20
    cols = [(pad, mid - 12, left), (mid + 12, width - pad, right)]
    ft = font(22, True)
    fi = font(20, True)
    for x0, x1, (name, items) in cols:
        d.rounded_rectangle([x0, y0, x1, y0 + body], radius=8, outline=BORDER, width=2)
        d.rectangle([x0, y0, x1, y0 + col_h_title], fill=HEADER)
        draw_center(d, (x0, y0, x1, y0 + col_h_title), name, ft, HEADER_TEXT)
        for i, item in enumerate(items):
            iy0 = y0 + col_h_title + i * row_h
            if i % 2 == 0:
                d.rectangle([x0 + 1, iy0, x1 - 1, iy0 + row_h], fill=CELL)
            draw_center(d, (x0, iy0, x1, iy0 + row_h), item, fi)
    frame(d, width, h)
    return img


def three_col(title: str, cols: list[tuple[str, list[str]]], width: int = 1200) -> Image.Image:
    hh = 62
    col_h_title = 48
    rows = max(len(c[1]) for c in cols)
    row_h = 52
    body = col_h_title + rows * row_h + 16
    h = hh + 20 + body + 16
    img = Image.new("RGB", (width, h), BG)
    d = ImageDraw.Draw(img)
    header(d, width, title, hh)
    pad = 20
    gap = 16
    col_w = (width - pad * 2 - gap * (len(cols) - 1)) // len(cols)
    y0 = hh + 20
    ft = font(20, True)
    fi = font(18, True)
    for i, (name, items) in enumerate(cols):
        x0 = pad + i * (col_w + gap)
        x1 = x0 + col_w
        d.rounded_rectangle([x0, y0, x1, y0 + body], radius=8, outline=BORDER, width=2)
        d.rectangle([x0, y0, x1, y0 + col_h_title], fill=HEADER)
        draw_center(d, (x0, y0, x1, y0 + col_h_title), name, ft, HEADER_TEXT)
        for j, item in enumerate(items):
            iy0 = y0 + col_h_title + j * row_h
            draw_center(d, (x0, iy0, x1, iy0 + row_h), item, fi)
    frame(d, width, h)
    return img


def memory_map(title: str, bands: list[str], width: int = 900) -> Image.Image:
    hh = 62
    top_h = 36
    bot_h = 36
    row_h = 58
    h = hh + top_h + row_h * len(bands) + bot_h
    img = Image.new("RGB", (width, h), BG)
    d = ImageDraw.Draw(img)
    header(d, width, title, hh)
    f_s = font(18, True)
    f = font(22, True)
    d.text((16, hh + 8), "High Address", font=f_s, fill=MUTED)
    y = hh + top_h
    for i, band in enumerate(bands):
        fill = (236, 236, 236) if i == 0 else (CELL if i % 2 else BG)
        d.rectangle([0, y, width, y + row_h], fill=fill)
        d.line([(0, y), (width, y)], fill=LINE, width=1)
        draw_center(d, (0, y, width, y + row_h), band, f)
        y += row_h
    d.text((16, h - bot_h + 8), "Low Address", font=f_s, fill=MUTED)
    frame(d, width, h)
    return img


def linked(title: str, labels: list[str], kind: str = "single", width: int = 1100) -> Image.Image:
    hh = 62
    h = 280
    img = Image.new("RGB", (width, h), BG)
    d = ImageDraw.Draw(img)
    header(d, width, title, hh)
    n = len(labels)
    box_w, box_h = 160, 88
    gap = (width - 80 - n * box_w) / max(n, 1)
    y = hh + 80
    f = font(22, True)
    xs = []
    for i, lab in enumerate(labels):
        x = 40 + i * (box_w + gap)
        xs.append(x)
        d.rounded_rectangle([x, y, x + box_w, y + box_h], radius=8, fill=ACCENT, outline=BORDER, width=2)
        if kind != "plain":
            d.line([(x + box_w * 0.68, y), (x + box_w * 0.68, y + box_h)], fill=LINE, width=2)
            draw_center(d, (x, y, x + box_w * 0.68, y + box_h), lab, f)
        else:
            draw_center(d, (x, y, x + box_w, y + box_h), lab, f)
        if i < n - 1:
            ax0 = x + box_w + 4
            ax1 = x + box_w + gap - 8
            mid = y + box_h * (0.35 if kind == "double" else 0.5)
            d.line([(ax0, mid), (ax1, mid)], fill=ARROW, width=3)
            d.polygon([(ax1 + 8, mid), (ax1 - 6, mid - 7), (ax1 - 6, mid + 7)], fill=ARROW)
            if kind == "double":
                mid2 = y + box_h * 0.65
                d.line([(ax1, mid2), (ax0, mid2)], fill=ARROW, width=3)
                d.polygon([(ax0 - 8, mid2), (ax0 + 6, mid2 - 7), (ax0 + 6, mid2 + 7)], fill=ARROW)
    if kind == "circular" and n >= 2:
        y_arc = y - 28
        d.line([(xs[0] + box_w / 2, y), (xs[0] + box_w / 2, y_arc), (xs[-1] + box_w / 2, y_arc), (xs[-1] + box_w / 2, y)], fill=ARROW, width=3)
        f2 = font(18, True)
        draw_center(d, (0, hh + 8, width, hh + 50), "원형: 끝이 다시 처음으로", f2, MUTED)
    frame(d, width, h)
    return img


def vtable(title: str = "VTable") -> Image.Image:
    w, hh = 1100, 62
    h = 420
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img)
    header(d, w, title, hh)
    f = font(20, True)
    ft = font(22, True)
    # object
    d.rounded_rectangle([60, 140, 280, 320], radius=8, outline=BORDER, width=2)
    d.rectangle([60, 140, 280, 188], fill=HEADER)
    draw_center(d, (60, 140, 280, 188), "객체", ft, HEADER_TEXT)
    draw_center(d, (60, 188, 280, 250), "vptr", f)
    d.line([(60, 250), (280, 250)], fill=LINE, width=1)
    draw_center(d, (60, 250, 280, 320), "멤버 데이터", f)
    # arrow
    d.line([(280, 219), (420, 219)], fill=ARROW, width=4)
    d.polygon([(436, 219), (420, 211), (420, 227)], fill=ARROW)
    # table
    rows = ["[0] foo()", "[1] bar()", "[2] render()"]
    d.rounded_rectangle([436, 120, 1040, 360], radius=8, outline=BORDER, width=2)
    d.rectangle([436, 120, 1040, 168], fill=HEADER)
    draw_center(d, (436, 120, 1040, 168), "가상함수 테이블 (함수 포인터 배열)", ft, HEADER_TEXT)
    rh = (360 - 168) / len(rows)
    for i, r in enumerate(rows):
        y0 = 168 + i * rh
        draw_center(d, (436, y0, 1040, y0 + rh), r, f)
        if i:
            d.line([(436, y0), (1040, y0)], fill=LINE, width=1)
    frame(d, w, h)
    return img


def formula(title: str, lines: list[str], width: int = 900) -> Image.Image:
    hh = 62
    row_h = 80
    h = hh + row_h * len(lines)
    img = Image.new("RGB", (width, h), BG)
    d = ImageDraw.Draw(img)
    header(d, width, title, hh)
    f = font(28, True)
    for i, line in enumerate(lines):
        y0 = hh + i * row_h
        d.rectangle([0, y0, width, y0 + row_h], fill=CELL if i % 2 == 0 else BG)
        d.line([(0, y0), (width, y0)], fill=LINE, width=1)
        draw_center(d, (0, y0, width, y0 + row_h), line, f)
    frame(d, width, h)
    return img


def layers(title: str, rows: list[str], width: int = 900) -> Image.Image:
    return stack(title, rows, width)


def grid_cells(title: str, cells: list[list[str]], width: int = 900) -> Image.Image:
    hh = 62
    rows, cols = len(cells), len(cells[0])
    cell = 90
    pad = 40
    h = hh + pad + rows * cell + pad
    img = Image.new("RGB", (width, h), BG)
    d = ImageDraw.Draw(img)
    header(d, width, title, hh)
    f = font(18, True)
    gw = cols * cell
    x0 = (width - gw) / 2
    y0 = hh + pad
    for r in range(rows):
        for c in range(cols):
            x = x0 + c * cell
            y = y0 + r * cell
            d.rectangle([x, y, x + cell, y + cell], outline=BORDER, width=2, fill=CELL)
            draw_center(d, (x, y, x + cell, y + cell), cells[r][c], f)
    frame(d, width, h)
    return img


def bezier_img(title: str = "3차 베지어") -> Image.Image:
    w, hh, h = 1000, 62, 420
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img)
    header(d, w, title, hh)
    pts = [(120, 340), (280, 120), (720, 120), (880, 340)]
    # curve
    prev = None
    for i in range(0, 81):
        t = i / 80
        u = 1 - t
        x = u**3 * pts[0][0] + 3 * u**2 * t * pts[1][0] + 3 * u * t**2 * pts[2][0] + t**3 * pts[3][0]
        y = u**3 * pts[0][1] + 3 * u**2 * t * pts[1][1] + 3 * u * t**2 * pts[2][1] + t**3 * pts[3][1]
        if prev:
            d.line([prev, (x, y)], fill=HEADER, width=4)
        prev = (x, y)
    d.line([pts[0], pts[1]], fill=LINE, width=2)
    d.line([pts[2], pts[3]], fill=LINE, width=2)
    d.line([pts[1], pts[2]], fill=LINE, width=2)
    names = ["P0", "P1", "P2", "P3"]
    f = font(20, True)
    for p, n in zip(pts, names):
        d.ellipse([p[0] - 8, p[1] - 8, p[0] + 8, p[1] + 8], fill=HEADER)
        d.text((p[0] - 12, p[1] + 12), n, font=f, fill=TEXT)
    frame(d, w, h)
    return img


def aabb_obb(title: str = "AABB / OBB") -> Image.Image:
    w, hh, h = 1100, 62, 420
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img)
    header(d, w, title, hh)
    ft = font(22, True)
    d.text((160, 90), "AABB", font=ft, fill=TEXT)
    d.text((740, 90), "OBB", font=ft, fill=TEXT)
    # AABB
    d.rectangle([80, 140, 420, 340], outline=HEADER, width=4)
    d.polygon([(160, 210), (300, 170), (360, 280), (200, 310)], outline=BORDER, width=3)
    # OBB rotated rect
    obb = [(640, 200), (900, 140), (980, 280), (720, 340)]
    d.polygon(obb, outline=HEADER, width=4)
    d.polygon([(700, 230), (860, 190), (910, 290), (750, 320)], outline=BORDER, width=3)
    f2 = font(18, True)
    draw_center(d, (80, 350, 420, 400), "축에 평행한 상자", f2, MUTED)
    draw_center(d, (640, 350, 1000, 400), "물체 방향에 맞춘 상자", f2, MUTED)
    frame(d, w, h)
    return img


def rays(title: str = "Raytracing") -> Image.Image:
    w, hh, h = 1100, 62, 460
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img)
    header(d, w, title, hh)
    f = font(20, True)
    # eye
    d.ellipse([70, 220, 140, 290], outline=HEADER, width=3)
    draw_center(d, (40, 300, 170, 340), "눈/카메라", f)
    # primary
    d.line([(140, 255), (420, 210)], fill=HEADER, width=3)
    d.polygon([(432, 206), (416, 200), (418, 222)], fill=HEADER)
    d.ellipse([410, 170, 520, 280], outline=BORDER, width=3)
    draw_center(d, (410, 290, 520, 330), "물체", f)
    # secondary
    d.line([(520, 210), (760, 140)], fill=ARROW, width=3)
    d.line([(520, 230), (780, 300)], fill=ARROW, width=3)
    d.line([(500, 250), (640, 380)], fill=LINE, width=3)
    draw_center(d, (700, 100, 1060, 150), "2차: 반사/굴절/그림자", f)
    draw_center(d, (200, 150, 400, 190), "1차: 레이캐스트", f)
    d.ellipse([860, 90, 920, 150], outline=HEADER, width=2)
    draw_center(d, (840, 155, 1040, 195), "광원", f)
    frame(d, w, h)
    return img


def normalize_vec(title: str = "Normalize") -> Image.Image:
    w, hh, h = 1000, 62, 380
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img)
    header(d, w, title, hh)
    f = font(20, True)
    # long vector
    d.line([(80, 240), (420, 140)], fill=HEADER, width=5)
    d.polygon([(432, 134), (412, 128), (418, 152)], fill=HEADER)
    draw_center(d, (80, 260, 420, 310), "원래 벡터 (길이 != 1)", f)
    d.line([(560, 240), (720, 180)], fill=HEADER, width=5)
    d.polygon([(732, 176), (712, 170), (718, 194)], fill=HEADER)
    draw_center(d, (520, 260, 900, 310), "정규화 (길이 1, 방향 유지)", f)
    d.line([(500, 100), (500, 340)], fill=LINE, width=2)
    frame(d, w, h)
    return img


def buffers(title: str, front: str, back: str) -> Image.Image:
    return two_col(title, ("Front", [front, "화면 출력"]), ("Back", [back, "그리는 중"]))


def render(kind: str, title: str, data) -> Image.Image:
    if kind == "stack":
        return stack(title, data)
    if kind == "hflow":
        return hflow(title, data)
    if kind == "vflow":
        return vflow(title, data)
    if kind == "two":
        return two_col(title, data[0], data[1])
    if kind == "three":
        return three_col(title, data)
    if kind == "memory":
        return memory_map(title, data)
    if kind == "linked":
        return linked(title, data[0], data[1] if len(data) > 1 else "single")
    if kind == "vtable":
        return vtable(title)
    if kind == "formula":
        return formula(title, data)
    if kind == "grid":
        return grid_cells(title, data)
    if kind == "bezier":
        return bezier_img(title)
    if kind == "aabb":
        return aabb_obb(title)
    if kind == "rays":
        return rays(title)
    if kind == "norm":
        return normalize_vec(title)
    raise ValueError(kind)

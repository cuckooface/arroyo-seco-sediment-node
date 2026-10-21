#!/usr/bin/env python3
"""Build the 8.5 x 11 landscape position sheets.

    python3 position/build.py            -> position/ASSN_Position_Sheets.pdf

Sheet 1 is the pile-up, sheet 2 the index (position + all references),
sheets 3 onward one reference per page: image, information, relevance, project.
Layout and text live in config.py. Images are read from position/images/<ID>.jpg;
a missing image is drawn as a labeled gray placeholder at the correct size.
"""
import hashlib
import os
import sys

from PIL import Image, ImageEnhance, ImageOps
from reportlab.lib.colors import Color, black, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import config as C  # noqa: E402

IN = 72.0
PW, PH = C.SHEET_W * IN, C.SHEET_H * IN
IMG_DIR = os.path.join(HERE, "images")
CACHE = os.path.join(HERE, ".cache")
OUT = os.path.join(HERE, "ASSN_Position_Sheets.pdf")
REFS = {r["id"]: r for r in C.REFERENCES}

REG, BOLD = "Helvetica", "Helvetica-Bold"   # one family, two weights
INK = Color(0.08, 0.08, 0.08)
GREY = Color(0.45, 0.45, 0.45)
RULE = Color(0.80, 0.80, 0.80)


# ---------- images ----------

def find_image(rid):
    for ext in (".jpg", ".jpeg", ".png", ".tif", ".tiff", ".JPG", ".PNG"):
        p = os.path.join(IMG_DIR, rid + ext)
        if os.path.exists(p):
            return p
    return None


def prepared(rid, aspect, w_in, focus=(0.5, 0.5), muted=0.0):
    """Crop the source to `aspect` (cover fit), resample to w_in at DPI, return a cached path."""
    src = find_image(rid)
    if not src:
        return None
    key = f"{src}{os.path.getmtime(src)}{aspect:.4f}{w_in:.3f}{focus}{muted}{C.DPI}"
    out = os.path.join(CACHE, hashlib.md5(key.encode()).hexdigest() + ".jpg")
    if os.path.exists(out):
        return out
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    sw, sh = im.size
    if sw / sh > aspect:                        # too wide: trim the sides
        cw, ch = int(sh * aspect), sh
    else:                                       # too tall: trim top and bottom
        cw, ch = sw, int(sw / aspect)
    x0 = int((sw - cw) * focus[0])
    y0 = int((sh - ch) * focus[1])
    im = im.crop((x0, y0, x0 + cw, y0 + ch))
    tw = int(round(w_in * C.DPI))
    th = int(round(tw / aspect))
    if tw < cw:                                 # never upsample; print at native size
        im = im.resize((tw, th), Image.LANCZOS)
    if muted:
        im = ImageEnhance.Contrast(im).enhance(1 - 0.5 * muted)
        im = Image.blend(im, Image.new("RGB", im.size, (255, 255, 255)), muted * 0.6)
    os.makedirs(CACHE, exist_ok=True)
    im.save(out, quality=92, dpi=(C.DPI, C.DPI))
    return out


def draw_image(c, rid, x, y, w, h, focus=(0.5, 0.5), muted=0.0, label=True):
    """Image or placeholder with its lower-left corner at (x, y) in points."""
    path = prepared(rid, w / h, w / IN, focus, muted)
    if path:
        c.drawImage(path, x, y, w, h)
        return
    g = 0.86 + 0.08 * muted
    c.setFillColor(Color(g, g, g))
    c.rect(x, y, w, h, stroke=0, fill=1)
    c.setStrokeColor(Color(g - 0.12, g - 0.12, g - 0.12))
    c.setLineWidth(0.4)
    c.line(x, y, x + w, y + h)
    c.line(x, y + h, x + w, y)
    if not label:
        return
    r = REFS[rid]
    size = max(7, min(22, w / 6))
    c.setFillColor(Color(0.35, 0.35, 0.35))
    c.setFont(BOLD, size)
    c.drawCentredString(x + w / 2, y + h / 2 + size * 0.2, rid)
    small = max(4.5, min(7, w / 22))
    c.setFont(REG, small)
    for i, line in enumerate(wrap(f"{r['title']}. {r['image']}", REG, small, w - 12)[:4]):
        c.drawCentredString(x + w / 2, y + h / 2 - size * 0.55 - i * small * 1.25, line)
    c.setFont(BOLD, small)
    c.drawCentredString(x + w / 2, y + 6, f"images/{rid}.jpg")


def wrap(text, font, size, width):
    from reportlab.pdfbase.pdfmetrics import stringWidth
    lines, cur = [], ""
    for word in text.split():
        t = f"{cur} {word}".strip()
        if stringWidth(t, font, size) <= width or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


# ---------- type ----------

def style(size, font=REG, lead=1.3, color=INK):
    return ParagraphStyle("s", fontName=font, fontSize=size, leading=size * lead, textColor=color)


def para(c, text, x, top, width, st):
    """Draw a paragraph with its top at `top`; return the y below it."""
    p = Paragraph(text, st)
    _, h = p.wrapOn(c, width, PH)
    p.drawOn(c, x, top - h)
    return top - h


def label(c, text, x, y, size=6.5, color=GREY):
    t = c.beginText(x, y)
    t.setFont(BOLD, size)
    t.setCharSpace(size * 0.12)
    t.setFillColor(color)
    t.textLine(text.upper())
    t.setCharSpace(0)                           # Tc persists in the page state otherwise
    c.drawText(t)


def tag(c, text, x, y, size=6.5):
    """Group tag: black box, white tracked caps. (x, y) is the box's lower-left."""
    from reportlab.pdfbase.pdfmetrics import stringWidth
    w = stringWidth(text.upper(), BOLD, size) + len(text) * size * 0.12 + 8
    c.setFillColor(INK)
    c.rect(x, y, w, size + 6, stroke=0, fill=1)
    label(c, text, x + 4, y + 4, size, white)
    return w


def footer(c, n, total, left):
    label(c, left, 0.5 * IN, 0.32 * IN, 6)
    s = f"{n:02d} / {total:02d}"
    label(c, s, PW - 0.5 * IN - len(s) * 4.4, 0.32 * IN, 6)


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def ref_title(r):
    return f"{r['title']}, {r['author']}" + (f", {r['year']}" if r["year"] else "")


# ---------- sheets ----------

def sheet_pileup(c):
    c.setFillColor(white)
    c.rect(0, 0, PW, PH, stroke=0, fill=1)
    for item in C.PILEUP:
        r = REFS[item["id"]]
        w = item["w"] * IN
        h = w / r["aspect"]
        c.saveState()
        c.translate(item["x"] * IN, PH - item["y"] * IN)
        c.rotate(item.get("rot", 0))
        if item.get("border", True):
            b = 2.5                                     # white border, pt
            c.setFillColor(Color(0, 0, 0, alpha=0.18))  # thin drop shadow
            c.rect(-w / 2 - b + 1.6, -h / 2 - b - 1.6, w + 2 * b, h + 2 * b, stroke=0, fill=1)
            c.setFillColor(white)
            c.rect(-w / 2 - b, -h / 2 - b, w + 2 * b, h + 2 * b, stroke=0, fill=1)
        draw_image(c, item["id"], -w / 2, -h / 2, w, h, r["focus"], item.get("muted", 0))
        c.restoreState()
    if C.QUOTE:
        qx, qy = C.QUOTE_POS
        c.setFillColor(INK)
        c.setFont(REG, 10)
        c.drawString(qx * IN, PH - qy * IN, C.QUOTE)


def sheet_index(c, n, total):
    x0, top = 0.5 * IN, PH - 0.55 * IN
    colw = 3.05 * IN
    label(c, "Position", x0, top)
    y = para(c, esc(C.POSITION), x0, top - 7, colw, style(9.5, BOLD, 1.32))
    label(c, "Material", x0, y - 16)
    y = para(c, esc(C.MATERIAL), x0, y - 23, colw, style(8.5))
    c.setStrokeColor(RULE)
    c.setLineWidth(0.5)
    c.line(x0, y - 12, x0 + colw, y - 12)
    label(c, "Thom Mayne", x0, y - 26)
    y = para(c, esc(C.MAYNE_PROMPT), x0, y - 33, colw, style(9.5, BOLD))
    for head, body in C.MAYNE:
        label(c, head, x0, y - 14, 6, INK)
        y = para(c, esc(body), x0, y - 20, colw, style(8))

    # grid of references, 4 x 3
    gx, gw, gap = 3.95 * IN, PW - 0.5 * IN - 3.95 * IN, 0.2 * IN
    cw = (gw - 3 * gap) / 4
    rh = (PH - 1.05 * IN) / 3
    th = cw / 1.5
    for i, r in enumerate(C.REFERENCES):
        col, row = i % 4, i // 4
        x = gx + col * (cw + gap)
        ty = PH - 0.55 * IN - row * rh
        draw_image(c, r["id"], x, ty - th, cw, th, r["focus"], label=False)
        yy = ty - th - 13
        c.setFillColor(INK)
        c.setFont(BOLD, 9)
        c.drawString(x, yy, r["id"])
        label(c, r["group"], x + 30, yy + 0.5, 5.5)
        yy = para(c, esc(ref_title(r)), x, yy - 4, cw, style(7, BOLD, 1.25))
        para(c, esc(r["caption"]), x, yy - 3, cw, style(6.8, REG, 1.3, Color(0.25, 0.25, 0.25)))
    footer(c, n, total, "Reference index")


def sheet_reference(c, r, n, total):
    # image: left field, fitted to its frame aspect, top aligned
    fx, ftop, fw, fh = 0.5 * IN, PH - 0.5 * IN, 6.2 * IN, PH - 1.0 * IN
    w = min(fw, fh * r["aspect"])
    h = w / r["aspect"]
    draw_image(c, r["id"], fx, ftop - h, w, h, r["focus"])

    x, colw = 7.05 * IN, PW - 0.5 * IN - 7.05 * IN
    top = PH - 0.5 * IN
    c.setFillColor(INK)
    c.setFont(BOLD, 30)
    c.drawString(x, top - 26, r["id"])
    tag(c, r["group"], x, top - 48)

    y = top - 72
    label(c, "Information", x, y)
    y = para(c, esc(r["title"]), x, y - 7, colw, style(14, BOLD, 1.18))
    y = para(c, esc(r["author"] + (f", {r['year']}" if r["year"] else "")), x, y - 3, colw,
             style(10))
    y -= 4
    for line in r["info"]:
        c.setFillColor(GREY)
        c.circle(x + 2, y - 6.6, 1.1, stroke=0, fill=1)
        y = para(c, esc(line), x + 8, y - 4, colw - 8, style(8, REG, 1.3, Color(0.25, 0.25, 0.25)))
    c.setStrokeColor(RULE)
    c.setLineWidth(0.5)
    c.line(x, y - 12, x + colw, y - 12)

    y -= 26
    label(c, "Relevance", x, y)
    y = para(c, esc(r["caption"]), x, y - 7, colw, style(11.5, BOLD, 1.28))
    c.line(x, y - 12, x + colw, y - 12)

    y -= 26
    label(c, "Project", x, y)
    para(c, esc(r["project"]), x, y - 7, colw, style(9, REG, 1.38))
    footer(c, n, total, f"{r['id']}  {r['title']}")


def main():
    total = 2 + len(C.REFERENCES)
    c = canvas.Canvas(OUT, pagesize=(PW, PH))
    c.setTitle("Position sheets: contemporary landscape")
    c.setAuthor("Brandon Avalos")
    sheet_pileup(c)
    c.showPage()
    sheet_index(c, 2, total)
    c.showPage()
    for i, r in enumerate(C.REFERENCES):
        sheet_reference(c, r, 3 + i, total)
        c.showPage()
    c.save()
    missing = [r["id"] for r in C.REFERENCES if not find_image(r["id"])]
    print(f"wrote {os.path.relpath(OUT)} ({total} sheets)")
    if missing:
        print("placeholders for:", " ".join(missing))


if __name__ == "__main__":
    main()

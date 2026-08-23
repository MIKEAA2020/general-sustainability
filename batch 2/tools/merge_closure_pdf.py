#!/usr/bin/env python3
"""Portable version: merge cover + body into the final consolidated PDF.

Paths resolved relative to this script's location (tools/).
Cover fallback order: _build/cover.pdf (freshly rendered), then
assets/cover.pdf (shipped prebuilt) — so the rebuild works even without
node/playwright.

Preserves link annotations and PDF outlines via PdfWriter.append().
"""
import os
from pypdf import PdfReader, PdfWriter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BUILD = os.path.join(ROOT, "_build")
OUT = os.path.join(ROOT, "GENERAL_THEORY_CLOSURE_REVIEW.pdf")

A4_W, A4_H = 595.28, 841.89  # A4 in points


def main():
    cover_src = os.path.join(BUILD, "cover.pdf")
    if not os.path.exists(cover_src):
        cover_src = os.path.join(ROOT, "assets", "cover.pdf")
        print(f"note: no freshly rendered cover; using shipped {cover_src}")
    body_src = os.path.join(BUILD, "body.pdf")
    for p in (cover_src, body_src):
        if not os.path.exists(p):
            raise SystemExit(f"missing required input: {p}")

    writer = PdfWriter()
    writer.append(cover_src)
    writer.append(body_src)

    # normalize cover page to exact A4 (html2poster output is 595.9x842.9 pt)
    cover = writer.pages[0]
    w, h = float(cover.mediabox.width), float(cover.mediabox.height)
    if abs(w - A4_W) > 0.5 or abs(h - A4_H) > 0.5:
        cover.scale_to(A4_W, A4_H)

    writer.add_metadata({
        "/Title": "Mathematical Closure Review - General Theory of Sustainability (Docket T1-T9)",
        "/Author": "Z.ai",
        "/Subject": "External mathematical review of the general-theory closure packet: TCS-1.0 schema audit, theorem dependency graph, result records R01-R09, boundary theorem, research plan",
        "/Creator": "Z.ai",
    })
    with open(OUT, "wb") as f:
        writer.write(f)

    r = PdfReader(OUT)
    sizes = {(round(float(p.mediabox.width), 1), round(float(p.mediabox.height), 1)) for p in r.pages}
    n_links = 0
    for pg in r.pages[:3]:
        annots = pg.get("/Annots")
        if annots:
            n_links += len(annots)
    print(f"Final PDF: {OUT}")
    print(f"  pages: {len(r.pages)}, sizes: {sizes}, outline entries: {len(r.outline) if r.outline else 0}, TOC-page link annots: {n_links}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""PDF, linkage and workbook QA; visual confirmation is a separate explicit step."""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from pathlib import Path

import pymupdf
from PIL import Image, ImageDraw
from build_F16 import ROOT, CACHE, expand, require

DECL = "Arena.ai Agent Mode was used to assist with computational methods and literature review."


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pdf(kind: str) -> dict:
    path = ROOT / f"integrated_F16_A01_{kind}.pdf"
    document = pymupdf.open(path)
    texts, bad, links, fonts, sheets = [], [], [], set(), []
    for index, page in enumerate(document):
        texts.append(page.get_text())
        links.extend(link.get("uri", "") for link in page.get_links())
        fonts.update(font[0] for font in page.get_fonts(full=True))
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                for span in line["spans"]:
                    x0, y0, x1, y1 = span["bbox"]
                    if min(x0, y0) < -0.5 or x1 > page.rect.width + 0.5 or y1 > page.rect.height + 0.5:
                        bad.append({"page": index + 1, "text": span["text"], "bbox": span["bbox"]})
    checks = []
    for xref in fonts:
        ok = bool(document.extract_font(xref)[3])
        method = "font program"
        if not ok:
            obj = document.xref_object(xref)
            match = re.search(r"/CharProcs\s+(\d+)\s+0\s+R", obj)
            if "/Subtype /Type3" in obj and match:
                refs = re.findall(r"(\d+)\s+0\s+R", document.xref_object(int(match[1])))
                ok = bool(refs) and all(bool(document.xref_stream(int(ref))) for ref in refs)
                method = "Type3 embedded CharProcs"
        checks.append({"xref": xref, "embedded": ok, "method": method})
    require(not bad, "PDF clipping " + kind)
    require(all(row["embedded"] for row in checks), "Unembedded font " + kind)
    normalized = " ".join(" ".join(texts).split())
    require(any("orcid.org/0000-0002-0019-1842" in link for link in links), "ORCID link")
    require(all(len(text) > 400 for text in texts), "Unexpected near-blank page")
    if kind == "main":
        require(DECL in normalized, "AI declaration")
        for value in ["17.639", "38.918", "104", "296", "634", "183", "68", "3.303", "17.293", "136.251", "148,732", "3.783", "137,372", "133,564,800", "31.10", "32.14", "250.6"]:
            require(value in normalized, "Key result missing " + value)
    layout = CACHE / "layout"
    layout.mkdir(parents=True, exist_ok=True)
    for start in range(0, len(document), 6):
        tiles = []
        for index in range(start, min(start + 6, len(document))):
            pixmap = document[index].get_pixmap(matrix=pymupdf.Matrix(1.2, 1.2))
            image = Image.frombytes("RGB", (pixmap.width, pixmap.height), pixmap.samples)
            image.thumbnail((650, 920))
            tile = Image.new("RGB", (680, 960), "#dedede")
            tile.paste(image, ((680 - image.width) // 2, 30))
            ImageDraw.Draw(tile).text((12, 8), f"{kind} | Page {index + 1}", fill="black")
            tiles.append(tile)
        canvas = Image.new("RGB", (1360, 960 * ((len(tiles) + 1) // 2)), "#dedede")
        for tile_index, image in enumerate(tiles):
            canvas.paste(image, (680 * (tile_index % 2), 960 * (tile_index // 2)))
        name = f"{kind}_{start + 1:02}_{min(start + 6, len(document)):02}.jpg"
        canvas.save(layout / name, quality=92)
        sheets.append(name)
    report = {
        "file": path.name, "sha256": sha(path), "pages": len(document),
        "page_text_characters": [len(text) for text in texts],
        "text_outside_page_bounds": bad, "all_fonts_embedded": True,
        "font_checks": sorted(checks, key=lambda row: row["xref"]),
        "ORCID_hyperlink": True, "AI_declaration": DECL in normalized,
        "contact_sheets": sheets,
    }
    document.close()
    return report


def run(visual: bool = False) -> None:
    main = (ROOT / "integrated_F16_A01_main.tex").read_text()
    full = expand(ROOT / "integrated_F16_A01_main.tex")
    si = expand(ROOT / "integrated_F16_A01_SI.tex")
    require(full.count("\\begin{figure}") == 7 and full.count("\\begin{table}") == 2, "Main figure/table allocation")
    results = main.split("\\section{Results}")[1].split("\\section{Discussion}")[0]
    require(results.count("\\subsection{") == 5, "Five result sections")
    require("\\section{Discussion}" not in si and "Primary national AGB target and remaining evidence requirements" not in si, "Standalone discussion/work plan remains in SI")
    abstract = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", main, re.S)[1]
    keywords = re.search(r"\\textbf\{Keywords:\}([^\n]+)", main)[1].split(";")
    require(len(abstract.split()) <= 250 and len(keywords) == 7, "Abstract or keyword count")
    linkage = json.loads((ROOT / "metadata/SI_linkage_F16.json").read_text())
    require(linkage["every_SI_figure_and_table_cited_in_main"] and len(linkage["labels"]) == 30, "SI linkage")
    report = {
        "main": pdf("main"), "SI": pdf("SI"),
        "main_figures": 7, "main_tables": 2, "main_result_sections": 5,
        "SI_figures": 2, "SI_tables": 28, "all_SI_items_explicitly_cited": True,
        "abstract_whitespace_words": len(abstract.split()), "keywords": 7,
        "visual_review_completed": visual,
    }
    report["visual_review_pages"] = {kind: list(range(1, report[kind]["pages"] + 1)) for kind in ("main", "SI")} if visual else {}
    report["workbook"] = json.loads((ROOT / "metadata/workbook_QA_F16.json").read_text())
    require(report["workbook"]["sha256"] == sha(ROOT / report["workbook"]["file"]), "Stale workbook QA")
    (ROOT / "metadata/deliverable_QA_F16.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({key: value for key, value in report.items() if key not in ("main", "SI")} | {"main_pages": report["main"]["pages"], "SI_pages": report["SI"]["pages"]}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--confirm-visual-review", action="store_true")
    run(parser.parse_args().confirm_visual_review)

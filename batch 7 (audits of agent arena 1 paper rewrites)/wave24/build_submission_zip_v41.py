#!/usr/bin/env python3
"""Wave-24 / Task 102, part 5: build the main-manuscript submission zip
for the Theoretical Ecology portal --- submission_zips/
paper4_delay_dynamics_v41_TE.zip.

Owner directive (this round, directive 1): "for main manuscript, journal
portal wants LaTeX with figures and tables compressed into a .zip format
that will compile into a PDF for peer review."

Design (the P1 v28 main-zip precedent, plus the Task-101 figure-path
lesson applied):
  latex/paper4_delay_dynamics_v41.tex    the main file (article class,
                                         standard packages only --- no
                                         custom .cls/.sty needed)
  latex/paper4_delay_dynamics_v41.pdf    the compiled PDF (45 pp, one
                                         figure) for review
  latex/figs_p4/fig2_five_regime_topology_v2.png
                                        the figure at the DIRECT relative
                                        path the tex asks for first
  figs_p4/fig2_five_regime_topology_v2.png
                                        the same PNG (byte-identical,
                                        sha256 a4bbddc6...) at the
                                        graphicspath {{../}} resolution
  README.txt                            compile instructions for the
                                        portal/editor

The tables are inline tabular/longtable environments in the tex (the
manuscript has no external table files), and the references are inline
(no BibTeX run needed) --- verified below, so the zip carries every
non-standard file the compile needs.

Verification (all fail-loud):
  1. the shipped tex/pdf are the three-byte-identical-build artifacts;
     the tex needs no \\input/\\include/\\bibliography (self-contained
     apart from the one PNG);
  2. the zip is built deterministically (sorted names, fixed timestamp,
     deflate) and is idempotent (rebuild -> identical sha256);
  3. SCENARIO A (in place): extract, tectonic-compile
     latex/paper4_delay_dynamics_v41.tex --- error-free, 45 pages,
     text layer byte-identical to the shipped PDF, Figure 1 page
     pixel-identical;
  4. SCENARIO B (flat): copy the tex to the archive root and compile
     there --- error-free, 45 pages, same text layer (the direct-path
     figs_p4/ copy resolves; exactly the Task-101 failure scenario,
     now covered);
  5. the exact entry list (6 entries) and the figure's byte-identity
     across both in-zip copies and the repository file.
"""
from __future__ import annotations

import hashlib
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PR = ROOT / "arena agent 1/paper rewrites"
LATEX = PR / "latex"
ZIP = PR / "submission_zips/paper4_delay_dynamics_v41_TE.zip"

TEX = LATEX / "paper4_delay_dynamics_v41.tex"
PDF = LATEX / "paper4_delay_dynamics_v41.pdf"
FIG_LATEX = LATEX / "figs_p4/fig2_five_regime_topology_v2.png"
FIG_PARENT = PR / "figs_p4/fig2_five_regime_topology_v2.png"

TEX_MD5 = "9690145302dd5ffe790a5cee799de0b7"
PDF_MD5 = "9a63b3d62eb6be1eb3f217a362941b2f"
FIG_SHA256 = (
    "a4bbddc6221476a9adbc0562ca5dc0a4e0ca0517572567f5420b379a4be6e058"
)

README_TXT = """Submission package - paper4_delay_dynamics_v41
===============================================

Journal: Theoretical Ecology (LaTeX source package for peer review)

Contents
--------
latex/paper4_delay_dynamics_v41.tex
    The main LaTeX source file. Standard article class, standard
    packages only (no custom .cls or .sty required). The reference
    list is part of the source, so no BibTeX run is needed; tables are
    inline environments; there is exactly one figure file.

latex/paper4_delay_dynamics_v41.pdf
    The compiled PDF (45 pages, one figure), as built from this source.

latex/figs_p4/fig2_five_regime_topology_v2.png
figs_p4/fig2_five_regime_topology_v2.png
    Figure 1, placed at both resolution paths (beside the source and
    at the archive root). The source compiles with the directory
    structure as shipped, or with the .tex moved to the archive root.

README.txt
    This note.

How to compile
--------------
The main file is latex/paper4_delay_dynamics_v41.tex. Any standard
LaTeX engine works (tectonic, pdflatex, or xelatex; two passes
recommended for cross-references). The compile is fully
self-contained: no bibliography run, no external table files, and the
single figure is included in this archive at the path the source asks
for. All journal-article references carry DOIs.
"""

ENTRIES = [
    "README.txt",
    "figs_p4/fig2_five_regime_topology_v2.png",
    "latex/figs_p4/fig2_five_regime_topology_v2.png",
    "latex/paper4_delay_dynamics_v41.pdf",
    "latex/paper4_delay_dynamics_v41.tex",
]


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def md5(p: Path) -> str:
    return hashlib.md5(p.read_bytes()).hexdigest()


def tectonic_compile(texfile: Path, cwd: Path) -> tuple[int, str, Path]:
    rc = subprocess.run(
        ["tectonic", "--keep-logs", str(texfile)],
        cwd=str(cwd), capture_output=True, text=True,
    )
    runlog = rc.stdout + rc.stderr
    logfile = cwd / (texfile.stem + ".log")
    logtext = logfile.read_text(errors="replace") if logfile.exists() else ""
    return rc.returncode, runlog + logtext, logfile


def pages_from_log(logtext: str) -> int:
    for line in logtext.splitlines():
        if line.startswith("Output written on"):
            return int(re.search(r"\((\d+) pages", line).group(1))
    return -1


def text_layer(pdf: Path) -> list[str]:
    import fitz
    doc = fitz.open(pdf)
    out = [doc[i].get_text() for i in range(doc.page_count)]
    doc.close()
    return out


def figure_page_pixels(pdf: Path, page_idx: int) -> bytes:
    import fitz
    doc = fitz.open(pdf)
    pix = doc[page_idx].get_pixmap(dpi=100)
    data = pix.samples
    doc.close()
    return data


def main() -> int:
    # ---------- 1. pre-state ---------------------------------------------------
    assert md5(TEX) == TEX_MD5, "the shipped tex is not the build artifact"
    assert md5(PDF) == PDF_MD5, "the shipped pdf is not the build artifact"
    tex = TEX.read_text(encoding="utf-8")
    for cmd in ("\\input{", "\\include{", "\\bibliography{",
                "\\bibliographystyle{"):
        assert cmd not in tex, f"the tex is not self-contained: {cmd}"
    n_figs = len(re.findall(r"\\includegraphics", tex))
    assert n_figs == 1, f"expected exactly 1 figure, found {n_figs}"
    assert sha256(FIG_LATEX) == FIG_SHA256, "latex/figs_p4 png drifted"
    assert sha256(FIG_PARENT) == FIG_SHA256, "parent figs_p4 png drifted"
    print("  pre-state: the shipped tex/pdf are the byte-identical-build "
          "artifacts; the tex is self-contained (no \\input/\\include/"
          "\\bibliography; 1 figure); both figs_p4 copies sha256-matched")

    # ---------- 2. build the zip deterministically ----------------------------
    ZIP.parent.mkdir(exist_ok=True)
    payload = {
        "README.txt": README_TXT.encode("utf-8"),
        "figs_p4/fig2_five_regime_topology_v2.png": FIG_PARENT.read_bytes(),
        "latex/figs_p4/fig2_five_regime_topology_v2.png":
            FIG_LATEX.read_bytes(),
        "latex/paper4_delay_dynamics_v41.pdf": PDF.read_bytes(),
        "latex/paper4_delay_dynamics_v41.tex": TEX.read_bytes(),
    }
    with tempfile.TemporaryDirectory() as td:
        out = Path(td) / "paper4_delay_dynamics_v41_TE.zip"
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
            for name in ENTRIES:
                zi = zipfile.ZipInfo(
                    name, date_time=(2026, 9, 19, 12, 0, 0))
                zi.compress_type = zipfile.ZIP_DEFLATED
                zi.external_attr = 0o644 << 16
                zf.writestr(zi, payload[name])
        new_bytes = out.read_bytes()
    if ZIP.exists():
        prev = sha256(ZIP)
        if prev == hashlib.sha256(new_bytes).hexdigest():
            print("  the zip is already at the target state (idempotent)")
        else:
            print(f"  NOTE: replacing the existing zip (old sha256 {prev})")
    ZIP.write_bytes(new_bytes)
    zip_sha = sha256(ZIP)
    print(f"  zip built: {ZIP.name} ({len(new_bytes) // 1024} KB, 5 "
          f"entries, sha256 {zip_sha})")

    # ---------- 3. verify the zip structure ------------------------------------
    with zipfile.ZipFile(ZIP) as zf:
        names = zf.namelist()
        assert names == ENTRIES, f"entry list drifted: {names}"
        assert zf.read(
            "latex/paper4_delay_dynamics_v41.tex") == TEX.read_bytes()
        assert zf.read(
            "latex/paper4_delay_dynamics_v41.pdf") == PDF.read_bytes()
        fig_a = zf.read("figs_p4/fig2_five_regime_topology_v2.png")
        fig_b = zf.read(
            "latex/figs_p4/fig2_five_regime_topology_v2.png")
        assert fig_a == fig_b == FIG_LATEX.read_bytes(), (
            "the in-zip figure copies are not byte-identical to the "
            "repository figure"
        )
        assert zf.read("README.txt").decode("utf-8") == README_TXT
    print("  zip structure: exact entry list; tex/pdf/figure bytes "
          "identical to the repository artifacts")

    # ---------- 4. SCENARIO A: compile in place --------------------------------
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        with zipfile.ZipFile(ZIP) as zf:
            zf.extractall(tdp)
        rc, logtext, _ = tectonic_compile(
            tdp / "latex/paper4_delay_dynamics_v41.tex", tdp / "latex")
        assert rc == 0, f"SCENARIO A tectonic failed:\n{logtext[-2000:]}"
        errs = [l for l in logtext.splitlines() if l.startswith("! ")]
        assert not errs, f"SCENARIO A TeX errors: {errs[:5]}"
        assert "Missing character" not in logtext, "missing glyphs"
        pages = pages_from_log(logtext)
        assert pages == 45, f"SCENARIO A pages: {pages}"
        built = tdp / "latex/paper4_delay_dynamics_v41.pdf"
        assert built.exists() and built.stat().st_size > 10_000
        tl_a, tl_ship = text_layer(built), text_layer(PDF)
        assert tl_a == tl_ship, (
            "SCENARIO A text layer differs from the shipped PDF"
        )
        # Figure 1 sits on pdf page 27 (index 26) in the shipped build
        fig_page = next(i for i, t in enumerate(tl_ship)
                        if "Figure 1:" in t)
        pix_a = figure_page_pixels(built, fig_page)
        pix_ship = figure_page_pixels(PDF, fig_page)
        assert pix_a == pix_ship, (
            f"SCENARIO A figure page {fig_page + 1} pixels differ"
        )
        byte_identical = built.read_bytes() == PDF.read_bytes()
        print(f"  SCENARIO A (in place): tectonic clean, {pages} pages, "
              f"text layer byte-identical to the shipped PDF, Figure 1 "
              f"page {fig_page + 1} pixel-identical"
              + ("; PDF bytes identical too" if byte_identical else
                 "; PDF bytes differ (build metadata only - text and "
                 "pixels verified identical)"))

    # ---------- 5. SCENARIO B: the flat compile (Task-101's lesson) ------------
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        with zipfile.ZipFile(ZIP) as zf:
            zf.extractall(tdp)
        shutil.copy2(tdp / "latex/paper4_delay_dynamics_v41.tex",
                     tdp / "paper4_delay_dynamics_v41.tex")
        rc, logtext, _ = tectonic_compile(
            tdp / "paper4_delay_dynamics_v41.tex", tdp)
        assert rc == 0, f"SCENARIO B tectonic failed:\n{logtext[-2000:]}"
        errs = [l for l in logtext.splitlines() if l.startswith("! ")]
        assert not errs, f"SCENARIO B TeX errors: {errs[:5]}"
        pages = pages_from_log(logtext)
        assert pages == 45, f"SCENARIO B pages: {pages}"
        built = tdp / "paper4_delay_dynamics_v41.pdf"
        tl_b = text_layer(built)
        assert tl_b == tl_ship, (
            "SCENARIO B text layer differs from the shipped PDF"
        )
        pix_b = figure_page_pixels(built, fig_page)
        assert pix_b == pix_ship, (
            f"SCENARIO B figure page {fig_page + 1} pixels differ"
        )
        print(f"  SCENARIO B (tex moved to the archive root - exactly "
              f"the Task-101 failure scenario): tectonic clean, {pages} "
              f"pages, text layer and Figure 1 page identical")

    # ---------- 6. idempotence ---------------------------------------------------
    with tempfile.TemporaryDirectory() as td:
        out = Path(td) / "rebuild.zip"
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
            for name in ENTRIES:
                zi = zipfile.ZipInfo(
                    name, date_time=(2026, 9, 19, 12, 0, 0))
                zi.compress_type = zipfile.ZIP_DEFLATED
                zi.external_attr = 0o644 << 16
                zf.writestr(zi, payload[name])
        assert out.read_bytes() == ZIP.read_bytes(), (
            "the zip build is not byte-reproducible"
        )
    print("  idempotence: rebuild -> byte-identical zip")

    print(f"\nbuild_submission_zip_v41: ALL CHECKS PASS "
          f"(sha256 {zip_sha})")
    return 0


if __name__ == "__main__":
    sys.exit(main())

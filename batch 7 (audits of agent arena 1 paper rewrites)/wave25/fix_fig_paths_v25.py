#!/usr/bin/env python3
"""wave25 / fix_fig_paths_v25.py — the systemic figure-path fix for ALL papers (Task 103).

Owner directive (this round): "if there's something wrong with the figures, fix it."
Task 101 fixed the P4 instance (latex/figs_p4/) and flagged the systemic class
(31 of 45 distinct figure paths relying on the parent-level ../ fallback); this
script applies the same additive remedy to every remaining family:

  - copy figs_e1, figs_e2, figs_e3, figs_e4, figs_p5 (complete folders,
    byte-identical) from "paper rewrites/" into "paper rewrites/latex/";
  - copy the 4 older-P1 referenced files into the existing latex/figs_p1/;
  - NO tex/md/pdf is touched (graphicx tries the direct relative path first,
    so the in-folder copies resolve with zero source changes; the {{../}}
    graphicspath entries remain valid for the repo-structure scenario).

Fail-loud and idempotent: every copy is sha256-verified against the source;
re-running on a fixed tree must be a no-op that still passes all gates.
"""
import hashlib
import re
import shutil
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[2] / "arena agent 1" / "paper rewrites"
LATEX = BASE / "latex"

# The 30 plain ../-fallback distinct paths (Task 101's count minus the P4 one it fixed)
# split by remedy: complete-folder copies vs older-P1 file additions.
FOLDER_COPIES = ["figs_e1", "figs_e2", "figs_e3", "figs_e4", "figs_p5"]
P1_ADDITIONS = [
    "fig1_witness_v22.png",
    "fig1_witness_v25.png",
    "fig1_witness_v26.png",
    "fig2_weight_intervals_v31.png",
]
# Files already present in latex/figs_p1 whose parent copies must be byte-identical.
P1_PREEXISTING = [
    "fig1_witness_v38.png",
    "fig2_weight_intervals_v35.png",
    "fig3_path_view_v31.png",
]

FIG_RE = re.compile(r"\\includegraphics(?:\[[^\]\n]*\])?\{([^{}\n]+)\}")
GP_RE = re.compile(r"\\graphicspath\s*(\{(?:\{[^{}]*\})+\})")


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def audit() -> dict:
    """Classify every distinct figure path referenced by the latex/ texs."""
    direct, fallback, explicit = set(), set(), set()
    texs = sorted(LATEX.glob("*.tex"))
    assert texs, "no tex files found — wrong base dir?"
    for t in texs:
        txt = t.read_text(encoding="utf-8", errors="replace")
        for m in FIG_RE.finditer(txt):
            p = m.group(1).strip()
            if p.startswith("../"):
                explicit.add(p)
            elif (LATEX / p).exists():
                direct.add(p)
            else:
                fallback.add(p)
    return {"direct": direct, "fallback": fallback, "explicit": explicit, "n_tex": len(texs)}


def main() -> int:
    print("== wave25 fix_fig_paths_v25.py ==")
    pre = audit()
    print(f"pre-fix audit over {pre['n_tex']} texs:")
    print(f"  distinct paths: {len(pre['direct'] | pre['fallback'] | pre['explicit'])}")
    print(f"  direct in latex/        : {len(pre['direct'])}")
    print(f"  ../-fallback (plain)    : {len(pre['fallback'])}")
    print(f"  explicit ../-prefixed   : {len(pre['explicit'])}  {sorted(pre['explicit'])}")

    copied = []
    for folder in FOLDER_COPIES:
        src, dst = BASE / folder, LATEX / folder
        assert src.is_dir(), f"source folder missing: {src}"
        dst.mkdir(exist_ok=True)
        for f in sorted(src.iterdir()):
            if not f.is_file():
                continue
            d = dst / f.name
            if d.exists():
                assert sha256(d) == sha256(f), f"pre-existing file differs from parent: {d}"
                continue
            shutil.copyfile(f, d)
            assert sha256(d) == sha256(f), f"copy failed verification: {d}"
            copied.append(f"{folder}/{f.name}")
        print(f"  folder {folder}: {len(list(dst.iterdir()))} files in latex/{folder} (all sha256-verified)")

    p1 = LATEX / "figs_p1"
    for name in P1_ADDITIONS:
        src, d = BASE / "figs_p1" / name, p1 / name
        assert src.is_file(), f"source file missing: {src}"
        if d.exists():
            assert sha256(d) == sha256(src), f"pre-existing file differs from parent: {d}"
            continue
        shutil.copyfile(src, d)
        assert sha256(d) == sha256(src), f"copy failed verification: {d}"
        copied.append(f"figs_p1/{name}")
    for name in P1_PREEXISTING:
        a, b = p1 / name, BASE / "figs_p1" / name
        assert a.is_file() and b.is_file(), f"expected pre-existing pair missing: {name}"
        assert sha256(a) == sha256(b), f"latex/figs_p1/{name} differs from parent copy"
    print(f"  figs_p1: +{len([c for c in copied if c.startswith('figs_p1/')])} older referenced files; "
          f"{len(P1_PREEXISTING)} pre-existing pairs confirmed byte-identical to parent")

    post = audit()
    print("post-fix audit:")
    print(f"  direct in latex/        : {len(post['direct'])}")
    print(f"  ../-fallback (plain)    : {len(post['fallback'])}  {sorted(post['fallback'])}")
    print(f"  explicit ../-prefixed   : {len(post['explicit'])}  {sorted(post['explicit'])}")

    # GATES
    assert not post["fallback"], f"plain ../-fallback paths remain: {sorted(post['fallback'])}"
    assert post["explicit"] == {
        "../figs_p5/fig_cod_v39.png",
        "../figs_p5/fig_rho_scan_v39.png",
        "../figs_p5/fig_screen_v39.png",
    }, f"unexpected explicit-parent set: {sorted(post['explicit'])}"
    # every current-version tex must now be self-contained
    for t in sorted(LATEX.glob("*.tex")):
        txt = t.read_text(encoding="utf-8", errors="replace")
        for m in FIG_RE.finditer(txt):
            p = m.group(1).strip()
            if p.startswith("../"):
                continue  # the documented residual (superseded P5 v39/v40/v41)
            assert (LATEX / p).exists(), f"{t.name}: still missing {p}"

    # no frozen artifact touched: tex/md/pdf in latex/ unchanged by this script
    print(f"new files copied this run: {len(copied)}")
    for c in copied:
        print(f"    + latex/{c}")
    print("ALL FIG-PATH GATES PASS "
          f"(plain ../-fallback: 30 -> 0; residual: 3 explicit ../-prefixed paths in the "
          "superseded paper5 v39/v40/v41_NatSustain texs, owner-gated tex edit)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

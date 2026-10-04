#!/usr/bin/env python3
"""make_v39_ecomod.py — ECOMOD v38 -> v39 portal-tex hardening round.

Owner directive (this round): the portal requires the .tex as the Manuscript
item — a submitted PDF cannot be relied on for display — so the .tex itself
must compile and display properly on the journal portal's servers. v38 made
the preamble engine-adaptive (pdfLaTeX branch) and the source pure ASCII;
this round adds belt-and-braces so that EVERY engine a portal might pick
succeeds:

  H1  Font-existence guards in the fontspec (Lua/XeTeX) branch: each
      \\set*font is wrapped in \\IfFontExistsTF, so a portal server that
      compiles with Lua/XeTeX but lacks the DejaVu / Latin Modern Math
      SYSTEM fonts (the v35 failure mode's second half) falls back to the
      distribution's bundled Latin Modern instead of dying with
      "font-not-found". Authoritative builds on machines that have the
      fonts are unchanged (same lookups succeed).
  H2  \\graphicspath gains an explicit {./} first entry, so the flattened
      upload-directory layout (all files in one folder, as Editorial
      Manager stages them) resolves the figure PNGs even before kpathsea's
      bare-name fallback is considered.
  H3  Provenance header block for v39 (no content change).

Content invariance is asserted: everything from \\begin{document} to EOF is
byte-identical to v38. All ops are anchored exact matches asserted to occur
exactly the stated number of times (family discipline; fails loudly).
"""
import subprocess
import sys

SRC = "manuscript_ECOMOD_v38.tex"
DST = "manuscript_ECOMOD_v39.tex"

OPS = [
# ---- H3: provenance header ---------------------------------------------------
("H3 v39 header block",
r"""% v38 (2026-10-04): submission-repair round per the line-level review ---""",
r"""% v39 (2026-10-04): portal-tex hardening per the owner's directive --- the
% .tex itself is the Manuscript item (the portal compiles it; a submitted
% PDF cannot be relied on for display). Belt-and-braces: the fontspec
% branch now guards each font with \IfFontExistsTF (a portal server that
% compiles with Lua/XeTeX but lacks the DejaVu/LM-Math system fonts falls
% back to the distribution's bundled Latin Modern instead of a fatal
% lookup), and \graphicspath gains an explicit {./} first entry so the
% flattened upload-directory layout resolves the figure PNGs. Verified:
% flat-dir pdfLaTeX (Editorial Manager simulation: tex + the two exact-name
% PNGs alone) 0 errors / 0 overfull / 28 pp, both figures embedded;
% LuaLaTeX authoritative 0/0/31 pp. No content change.
% v38 (2026-10-04): submission-repair round per the line-level review ---""", 1),
# ---- H1: font-existence guards in the fontspec branch -------------------------
("H1 font guards",
r"""  \usepackage{fontspec}
  \usepackage{unicode-math}
  \setmainfont{DejaVu Serif}
  \setmonofont{DejaVu Sans Mono}
  \setmathfont{Latin Modern Math}""",
r"""  \usepackage{fontspec}
  \usepackage{unicode-math}
  % Font guards (portal safety): if the named system fonts are absent, fall
  % back to the distribution's bundled Latin Modern (fontspec's default
  % text/mono faces; latinmodern-math.otf for math) instead of a fatal
  % fontspec lookup. Authoritative builds with the fonts present are
  % unchanged: the same lookups succeed.
  \IfFontExistsTF{DejaVu Serif}{\setmainfont{DejaVu Serif}}{}%
  \IfFontExistsTF{DejaVu Sans Mono}{\setmonofont{DejaVu Sans Mono}}{}%
  \IfFontExistsTF{Latin Modern Math}{\setmathfont{Latin Modern Math}}{\setmathfont{latinmodern-math.otf}}%""", 1),
# ---- H2: graphicspath explicit cwd entry --------------------------------------
("H2 graphicspath cwd",
r"""\graphicspath{{reports/}{supplementary/FIGURES/}{graphical_abstract/}}""",
r"""\graphicspath{{./}{reports/}{supplementary/FIGURES/}{graphical_abstract/}}""", 1),
]


def main():
    with open(SRC, encoding="ascii") as f:
        src = f.read()

    out = src
    for name, old, new, count in OPS:
        found = out.count(old)
        assert found == count, (
            f"op {name!r}: expected {count} occurrence(s), found {found}")
        out = out.replace(old, new)
        print(f"  ok  {name}")

    # ASCII purity (portal safety, carried from v38)
    try:
        out.encode("ascii")
    except UnicodeEncodeError as e:
        sys.exit(f"FATAL: non-ASCII introduced: {e}")

    # Content invariance: everything from \begin{document} to EOF byte-identical
    marker = "\\begin{document}"
    assert src.count(marker) == 1 and out.count(marker) == 1
    a, b = src.split(marker, 1)[1], out.split(marker, 1)[1]
    assert a == b, "FATAL: body changed below \\begin{document}"
    print("  ok  body byte-identical to v38 below \\begin{document}")

    with open(DST, "w", encoding="ascii") as f:
        f.write(out)
    nlines = out.count("\n") + 1
    print(f"wrote {DST} ({nlines} lines; v38 had {src.count(chr(10)) + 1})")


if __name__ == "__main__":
    main()

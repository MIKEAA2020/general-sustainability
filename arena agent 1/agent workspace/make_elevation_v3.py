#!/usr/bin/env python3
"""Create campaign_e2_elevation_v3.py: the elevation campaign on the v3
(source-year) basis, with the portability bug fixed.

campaign_srcyear.py computes e_min / e_q05 / e_q10 from the SOURCE-YEAR
residuals and already uses e_q05 / e_min for the finite-duration floors, but
hardcodes the registered (hybrid) values in five display/derived places:

    line 251  constructive_raw = gK - 114.85          ->  gK - abs(e_q10)
    line 267  bool(460.0 > gmax), bool(318.8 > gmax)  ->  abs(e_min), abs(e_q05)
    line 396  max(0.0, gK_star - 114.85)              ->  abs(e_q10)
    line 453  figure floors (-114.85, -318.8, -460.0) ->  (e_q10, e_q05, e_min)
    line 563  axhline(318.8 / 460.0)                  ->  abs(e_q05) / abs(e_min)

Also fixes a portability bug: REPO is hardcoded to /home/user/git_repo, which
does not exist here, so the module cannot even be imported.
"""
import ast
from pathlib import Path

SRC = Path("/home/user/repo/wave_e_cod/src/campaign_srcyear.py")
DST = Path("/home/user/repo/wave_e_cod/src/campaign_e2_elevation_v3.py")

t = SRC.read_text(encoding="utf-8")

EDITS = [
    # ---- portability ------------------------------------------------------
    ('REPO = Path("/home/user/git_repo")',
     'REPO = Path(__file__).resolve().parents[2]'),
    ('OUT = HERE / "results_srcyear"',
     'OUT = HERE / "results_srcyear_v3"'),
    ('FIG = HERE / "figures"',
     'FIG = HERE / "figures_v3"'),

    # ---- docstring --------------------------------------------------------
    ("     -114.85), BAU q10 T=1/T=inf kernel intervals, vacuity status;",
     "     -80.87 under v3), BAU q10 T=1/T=inf kernel intervals, vacuity status;"),

    # ---- derived quantities ----------------------------------------------
    ("        constructive_raw = gK - 114.85",
     "        constructive_raw = gK - abs(e_q10)"),
    ('"worst_vacuous": bool(460.0 > gmax), "q05_vacuous": bool(318.8 > gmax),',
     '"worst_vacuous": bool(abs(e_min) > gmax), '
     '"q05_vacuous": bool(abs(e_q05) > gmax),'),
    ('"constructive": max(0.0, gK_star - 114.85),',
     '"constructive": max(0.0, gK_star - abs(e_q10)),'),

    # ---- pass the source-year floors into the figure layer ---------------
    ("    make_figures(r0, K0, K_STAR, e_q10, res_by_year, kdf, cdf, ssb, years, allee_fit)",
     "    make_figures(r0, K0, K_STAR, e_q10, e_q05, e_min, res_by_year, kdf, "
     "cdf, ssb, years, allee_fit)"),
    ("def make_figures(r0, K0, K_STAR, e_q10, res_by_year, kdf, cdf, ssb, years, allee_fit):",
     "def make_figures(r0, K0, K_STAR, e_q10, e_q05, e_min, res_by_year, kdf, "
     "cdf, ssb, years, allee_fit):"),

    # ---- figure 1 floors --------------------------------------------------
    # handled below by line index: the label strings contain $ and the
    # vacuous-classes text carries escaped backslashes, so exact-matching
    # them through this file's own escaping is fragile.

    # ---- figure 6 floor lines --------------------------------------------
    ('    a1.axhline(318.8, color="0.7", ls="--", lw=1)\n'
     '    a1.axhline(460.0, color="0.5", ls="--", lw=1)\n'
     '    a1.text(1850, 335, "q05 floor 318.8", fontsize=7.5)\n'
     '    a1.text(1850, 475, "worst floor 460.0", fontsize=7.5)',
     '    a1.axhline(abs(e_q05), color="0.7", ls="--", lw=1)\n'
     '    a1.axhline(abs(e_min), color="0.5", ls="--", lw=1)\n'
     '    a1.text(1850, abs(e_q05) + 16, f"q05 floor {abs(e_q05):.1f}", fontsize=7.5)\n'
     '    a1.text(1850, abs(e_min) + 16, f"worst floor {abs(e_min):.1f}", fontsize=7.5)'),
]

missing = []
for old, new in EDITS:
    if old not in t:
        missing.append(old[:70])
    else:
        t = t.replace(old, new, 1)

if missing:
    raise SystemExit("NOT FOUND:\n  " + "\n  ".join(missing))

# ---- line-index edits: figure 1 floor labels + vacuous band ---------------
lines = t.split("\n")


def repl(idx, new, expect):
    """1-based line number -> replace, asserting the old content."""
    assert expect in lines[idx - 1], f"line {idx} did not match: {lines[idx-1]!r}"
    lines[idx - 1] = new


def find(pred, start=0):
    for i in range(start, len(lines)):
        if pred(lines[i]):
            return i
    raise SystemExit("anchor not found")


# splice the two-line floor tuple into a three-line one
i_for = find(lambda L: "for y, lab in" in L)
assert "-114.85" in lines[i_for] and "-318.8" in lines[i_for], lines[i_for]
assert "worst floor" in lines[i_for + 1], lines[i_for + 1]
lines[i_for:i_for + 2] = [
    '    for y, lab in ((e_q10, f"q10 floor {e_q10:.1f}"),',
    '                   (e_q05, f"q05 floor {e_q05:.1f}"),',
    '                   (e_min, f"worst floor {e_min:.1f}")):',
]

# the vacuous band and its label are keyed to the old worst-floor magnitude
i_fb = find(lambda L: "fill_between(S, -460" in L)
lines[i_fb] = ('    ax.fill_between(S, e_min - 60, e_min - 120, '
               'color="0.9", alpha=0.6)')
i_tx = find(lambda L: "vacuous classes" in L)
lines[i_tx] = ('    ax.text(1300, e_min - 96, '
               '"vacuous classes: $|e| > g_{max}$", fontsize=8)')
t = "\n".join(lines)

# no registered/hybrid floor constants may survive
for bad in ("114.85", "318.8", "460.0", "-114.9"):
    if bad in t:
        print(f"  WARNING: '{bad}' still present")

ast.parse(t)
DST.write_text(t, encoding="utf-8")
print("wrote", DST)
print("  portability fixed, floors now derived from the source-year residuals")

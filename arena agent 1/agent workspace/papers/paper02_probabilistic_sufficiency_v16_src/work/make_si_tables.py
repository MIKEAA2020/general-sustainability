#!/usr/bin/env python3
"""Generate the SI tables for paper02 v16 from p02_core (exact)."""
import os, sys
from fractions import Fraction as Q
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import p02_core as C

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "si_parts")
os.makedirs(OUT, exist_ok=True)

def frac(q):
    q = Q(q)
    if q.denominator == 1:
        return f"${q.numerator}$"
    return f"$\\tfrac{{{q.numerator}}}{{{q.denominator}}}$"

# ---- S1: certified grid table (hold class, symmetric prior)
lines = []
lines.append("\\begin{tabular}{@{}l cccc c cccc c cccc@{}}")
lines.append("\\toprule")
lines.append(" & \\multicolumn{4}{c}{$\\Tobs=1$} & & \\multicolumn{4}{c}{$\\Tobs=2$} & & \\multicolumn{4}{c}{$\\Tobs=3$}\\\\")
lines.append("\\cmidrule{2-5}\\cmidrule{7-10}\\cmidrule{12-15}")
lines.append("$z_0$ & $k{=}1$ & $k{=}2$ & $k{=}3$ & $k{=}4$ & & $k{=}1$ & $k{=}2$ & $k{=}3$ & $k{=}4$ & & $k{=}1$ & $k{=}2$ & $k{=}3$ & $k{=}4$\\\\")
lines.append("\\midrule")
unit = half = 0
for z0 in C.GRID:
    row = [f"{float(z0):.1f}"]
    for T in C.TOBS:
        cells = []
        for k in C.HORIZONS:
            ell = C.effective_window(k, T)
            v = C.bf_hold(z0, Q(1, 2), ell)
            assert v == C.closed_hold(z0, Q(1, 2), ell)
            unit += (v == 1); half += (v == Q(1, 2))
            cells.append(frac(v))
        row.append(" & ".join(cells))
    lines.append(row[0] + " & " + " & & ".join(row[1:]) + "\\\\")
lines.append("\\bottomrule")
lines.append("\\end{tabular}")
open(os.path.join(OUT, "tab_grid.tex"), "w").write("\n".join(lines) + "\n")
assert (unit, half) == (36, 156), (unit, half)

# ---- S2: asymmetric audit table
w = Q(3, 10); z0 = Q(3, 2)
lines = ["\\begin{tabular}{@{}l c c l@{}}", "\\toprule",
         "Segment $(u_0,u_1)$ & positions after step 1 ($\\theta=+1$, $\\theta=-1$) & surviving mass & lost branch\\\\", "\\midrule"]
for seq in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
    zp = z0 + seq[0]; zm = z0 - seq[0]
    sp = C.survives_branch(z0, 1, list(seq)); sm = C.survives_branch(z0, -1, list(seq))
    mass = (w if sp else 0) + ((1 - w) if sm else 0)
    lost = "$\\theta=-1$ (mass $\\tfrac{7}{10}$)" if not sm else "$\\theta=+1$ (mass $\\tfrac{3}{10}$)"
    lines.append(f"$({seq[0]:+d},{seq[1]:+d})$ & ${zp}$, ${zm}$ & {frac(mass)} & {lost}, at step 1\\\\")
lines += ["\\bottomrule", "\\end{tabular}"]
open(os.path.join(OUT, "tab_asym.tex"), "w").write("\n".join(lines) + "\n")

# ---- S4: deadline table
lines = ["\\begin{tabular}{@{}c c c l c c@{}}", "\\toprule",
         "$\\Tl$ & pinned threshold & $|K|$ & kernel $K$ on the grid & probe-free threshold & $|K|$ (probe-free)\\\\", "\\midrule"]
for TL in range(5):
    K = C.threshold_on_grid(lambda z: C.pinned_probe_viable(z, TL), C.GRID)
    Kf = C.threshold_on_grid(lambda z: C.probe_free_viable(z, TL), C.GRID)
    thr = C.pinned_threshold(TL)
    assert all((z >= thr) == (z in K) for z in C.GRID)
    assert all((z >= 1 + Q(TL, 10)) == (z in Kf) for z in C.GRID)
    ks = "$\\{" + ", ".join(f"{float(z):.1f}" for z in K) + "\\}$"
    lines.append(f"{TL} & ${float(thr):.1f}$ & {len(K)} & {ks} & ${float(1 + Q(TL, 10)):.1f}$ & {len(Kf)}\\\\")
lines += ["\\bottomrule", "\\end{tabular}"]
open(os.path.join(OUT, "tab_deadline.tex"), "w").write("\n".join(lines) + "\n")

# ---- S5: majority table
lines = ["\\begin{tabular}{@{}c c c c@{}}", "\\toprule",
         "$n$ & exact $p_{\\mathrm{wrong}}(n)$ & decimal & bound $(3/5)^n$\\\\", "\\midrule"]
for n in (1, 3, 5, 7, 9, 11):
    p = C.majority_wrong(n, Q(1, 10)); b = Q(3, 5) ** n
    assert p <= b
    lines.append(f"{n} & {frac(p)} & {float(p):.6g} & {float(b):.4g}\\\\")
lines += ["\\bottomrule", "\\end{tabular}"]
open(os.path.join(OUT, "tab_majority.tex"), "w").write("\n".join(lines) + "\n")
print("SI tables written")

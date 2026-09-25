#!/usr/bin/env python3
"""
Applied regime viability v1 — verification.

Regenerates every fraction, inequality, power, ratio, and temporal claim of
applied_regime_viability_v1.tex in exact integer and rational arithmetic,
standard library only, directly from the provenance-locked CSV files of the
calibration record (wave-e-cod). No floating point anywhere.
"""
import os
import csv
import sys
from fractions import Fraction as Q

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "paperE1_calibration_data_v1_wave_e_cod")
PASS = []


def check(name, ok, detail=""):
    PASS.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + (f" ({detail})" if detail else ""))


def rows(fname):
    with open(os.path.join(DATA, fname), newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


ncam = {int(r["year"]): r for r in rows("ncam_2016_table_a2.csv")}
xte = {int(r["year"]): r for r in rows("xtencam_table17_ssb.csv")}
land = {int(r["year"]): r for r in rows("dfo_2025_table1_landings.csv")}
cap = {int(r["year"]): r for r in rows("capelin_acoustic_observed.csv")}


def ssb(y):
    return Q(ncam[y]["ssb_kt"])


# (1) the certified windows
good_years = list(range(1983, 1990))
good_mult = [(ssb(y + 1) / ssb(y), y) for y in good_years[:-1]]
rho_g, rho_g_y = min(good_mult)
bad = (ssb(1992) / ssb(1991), ssb(1993) / ssb(1992))
ok = (rho_g == Q(41800, 45147) and rho_g_y == 1985
      and bad[0] == Q(38195, 73451) and bad[1] == Q(2021, 7639)
      and rho_g < 1 and all(b < 1 for b in bad))
check("certified windows: good-window worst multiplier 41800/45147 at 1986; "
      "bad-window multipliers 38195/73451 and 2021/7639; all < 1", ok)

# (2) the moratorium obstruction: removals collapse, decline continues
ok = (Q(land[1992]["catch_kt"]) == Q(40956, 1000)
      and Q(land[1993]["catch_kt"]) == Q(11392, 1000)
      and bad[1] == Q(2021, 7639) and bad[1] < 1)
check("moratorium obstruction: removals 40956 -> 11392 t while the net "
      "multiplier is 2021/7639 < 1 (witness, not counterfactual)", ok)

# (3) breach-time certificates
lim = Q(276)
ok = (bad[1] <= Q(27600, 73451)
      and (2021 * 73451 < 7639 * 27600)          # integer cross-multiplication
      and ssb(1993) < lim
      and Q(xte[1993]["ssb_over_blim"]) == Q(29, 100)
      and ssb(1991) < Q(8846, 10))
check("breach certificates: 2021/7639 <= 27600/73451 (cross-mult exact); "
      "101.05 < 276 in 1993 with the xteNCAM ratio 0.29; the 1991 reading "
      "734.51 already below the LRP 884.6", ok)

# (4) the reference decade: LRP = decade mean; marginality
seven = [ssb(y) for y in range(1983, 1990)]
mean7 = sum(seven) / 7
lrp = Q(8846, 10)
ratios = [s / lrp for s in seven]
ok = (mean7 == Q(88458, 100) and abs(lrp - mean7) == Q(1, 50)
      and min(ratios) == Q(4180, 4423) and max(ratios) == Q(94075, 88460)
      and max(ratios) - 1 < Q(64, 1000) and 1 - min(ratios) < Q(64, 1000))
check("reference decade: mean 884.58 exactly, LRP its 1/50-rounding; "
      "decade ratios within [84108/88460, 94075/88460] (within +-6.4%)", ok)

# (5) the sixteen-year worst-case breach bound from the 1989 reading
z89 = ssb(1989)
target = lim / z89
rho16 = rho_g ** 16
rho15 = rho_g ** 15
ok = (rho16 <= target and target < rho15)
check("worst-case good-window breach from 921.66 kt: rho^16 <= 276/921.66 "
      "< rho^15 (exact integer powers) -- sixteen-year bound", ok)

# (6) the capelin alarm leads the mortality crossing
c90, c91 = Q(cap[1990]["acoustic_kt"]), Q(cap[1991]["acoustic_kt"])
m90 = Q(ncam[1990]["M_age5_14"])
m91 = Q(ncam[1991]["M_age5_14"])
ok = (cap[1990]["observed"] == "1" and cap[1991]["observed"] == "1"
      and c90 == Q(5783) and c91 == Q(138)
      and m90 == Q(403, 1000) and m91 == Q(1002, 1000)
      and m90 < 1 < m91)
check("probe datum: capelin 5783 -> 138 kt (observed rows) in 1991, one "
      "step before the M diagnostic crosses 1 (0.403 -> 1.002)", ok)

# (7) xteNCAM confirmation rows cited in the text's data section
ok = (Q(xte[1992]["ssb_kt"]) == Q(352) and Q(xte[1993]["ssb_kt"]) == Q(79)
      and Q(xte[2024]["ssb_kt"]) == Q(342))
check("xteNCAM independent readings present (1992: 352; 1993: 79; "
      "2024: 342) consistent with the lock's checkpoints", ok)

# ---------------- text needles, structure, hygiene -----------------
tex = open(os.path.join(HERE, "applied_regime_viability_v1.tex"),
           encoding="utf-8").read()
tnorm = " ".join(tex.split())
NEEDLES = [
    "closes that limitation",
    "41800}{45147}",
    "2021}{7639}",
    "38195}{73451}",
    "11{,}392",
    "40{,}956",
    "the fishery effectively closed",
    "witnessed obstruction in the dynamics, not the catch level",
    "27600}{73451}",
    "101.05 < 276",
    "0.29",
    "734.51 < 884.6",
    "884.58",
    "4180}{4423}",
    "94075}{88460}",
    "16} \\le \\tfrac{27600}{92166}",
    "138}{5783}",
    "0.403", "1.002",
    "one-year lead", "the probe datum",
    "review-timing reading of the",
    "three-year review cycle",
    "diagnostics only",
    "not a forecast",
    "exact integer and rational",
    "September 26, 2026",
]
missing = [n for n in NEEDLES if " ".join(n.split()) not in tnorm]
check(f"all {len(NEEDLES)} headline needles present in the tex", not missing,
      f"(missing: {missing})" if missing else "")

check("declarations and code pointer",
      "\\subsection*{Funding}" in tex
      and "The author reviewed and edited outputs and takes responsibility "
          "for the final work." in tnorm
      and tnorm.count("applied\\_regime\\_viability\\_v1\\_verification.py") == 1
      or tnorm.count("applied_regime_viability_v1_verification.py") == 1)

labels = [l for l in ("intro", "data", "windows", "breach", "marginal",
                      "probe", "scope", "methods", "conclusion")
          if f"\\label{{{l}}}" not in tex]
check("section labels intact", not labels, f"{labels}")

raw = open(os.path.join(HERE, "applied_regime_viability_v1.tex"), "rb").read()
check("source hygiene", all(b >= 32 or b == 10 for b in raw))

n_pass = sum(1 for _, ok in PASS if ok)
print(f"\nverification: {n_pass}/{len(PASS)} checks pass")
sys.exit(0 if n_pass == len(PASS) else 1)

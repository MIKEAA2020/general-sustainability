#!/usr/bin/env python3
"""Consequences of adopting each convention, computed with the committed machinery.

A (source-year, srcyear runner) : fit and residuals both use C_j      -> COHERENT
H (hybrid, committed v2)        : fit uses C_j, residuals use C_{j+1} -> INCOHERENT
B (destination, self-consistent): fit and residuals both use C_{j+1}  -> COHERENT
"""
import numpy as np
import sys

sys.path.insert(0, "/home/user/repo/wave_e_cod/src")
import run_intervention_v2 as b  # noqa: E402
from run_ladder import load, surplus  # noqa: E402

years, ssb, c_reg, c_ann, idx, lrp = load()
TRAIN_END = 2007
pols = b.make_policies()
KS = b.K_STAR


def resid(r, K, shift):
    out = {}
    for j in range(len(years) - 1):
        pred = ssb[j] + surplus(ssb[j], r, K) - c_ann[j + shift]
        out[int(years[j + 1])] = float(ssb[j + 1] - pred)
    tr = np.array([out[y] for y in sorted(out) if y <= TRAIN_END])
    return tr


def block(r, K, shift):
    tr = resid(r, K, shift)
    return {"worst": float(tr.min()),
            "q05": float(np.percentile(tr, 5)),
            "q10": float(np.percentile(tr, 10)),
            "sd": float(tr.std(ddof=1))}


VARIANTS = [
    ("A  source-year (coherent)", 0.2368694, 5000.0, 0),
    ("H  hybrid (committed v2)", 0.2368694, 5000.0, 1),
    ("B  destination (coherent)", 0.2084, 5000.0, 1),
]

fit = b.fit_surplus()

print("=" * 78)
print("1. DISTURBANCE CLASSES AND VACUITY   (g_max = rK/4, same r,K for A and H)")
print("=" * 78)
print(f"{'variant':28s} {'SD':>8s} {'worst':>9s} {'q05':>9s} {'q10':>9s} {'g_max':>8s}")
print("-" * 78)
for lab, r, K, sh in VARIANTS:
    bl = block(r, K, sh)
    gm = r * K / 4
    print(f"{lab:28s} {bl['sd']:8.2f} {bl['worst']:9.2f} {bl['q05']:9.2f} "
          f"{bl['q10']:9.2f} {gm:8.2f}")

print()
print(f"{'variant':28s} {'worst':>12s} {'q05':>12s} {'q10':>12s}   #vacuous")
print("-" * 78)
for lab, r, K, sh in VARIANTS:
    bl = block(r, K, sh)
    gm = r * K / 4
    st = {k: ("VACUOUS" if abs(bl[k]) > gm else "informative")
          for k in ("worst", "q05", "q10")}
    nv = sum(1 for v in st.values() if v == "VACUOUS")
    print(f"{lab:28s} {st['worst']:>12s} {st['q05']:>12s} {st['q10']:>12s}   {nv} of 3")

print()
print("=" * 78)
print("2. BAU KERNEL LOWER BOUNDARY AT T = inf   (kt; empty = no viable state)")
print("=" * 78)
print(f"{'variant':28s} {'worst':>10s} {'q05':>10s} {'q10':>10s}")
print("-" * 78)
for lab, r, K, sh in VARIANTS:
    bl = block(r, K, sh)
    row = []
    for k in ("worst", "q05", "q10"):
        kk = b.kernel_inf_stable(pols["BAU"], fit, bl[k], KS)
        bd = b.boundary(kk)
        row.append("empty" if bd is None else f"{float(bd):.1f}")
    print(f"{lab:28s} {row[0]:>10s} {row[1]:>10s} {row[2]:>10s}")

print()
print("=" * 78)
print("3. WHAT THE COMMITTED ARTIFACT ACTUALLY CONTAINS")
print("=" * 78)
import json  # noqa: E402
d = json.load(open("/home/user/fam/e2/results/intervention_results_v2.json"))
print("  intervention_results_v2.json  UC block:")
for k, v in d["UC"].items():
    print(f"     {k:8s} = {v}")
blA = block(0.2368694, 5000.0, 0)
blH = block(0.2368694, 5000.0, 1)
KEYMAP = {"UC_min": "worst", "UC_q05": "q05", "UC_q10": "q10"}
print()
for nm, bl in (("A (source-year)", blA), ("H (hybrid)", blH)):
    ok = all(abs(d["UC"][k] - bl[KEYMAP[k]]) < 0.01 for k in d["UC"])
    print(f"  match to {nm:18s}: {ok}")
print("  fit residual SD in artifact: %.4f  (A=%.4f  H=%.4f)"
      % (d["fit"]["train_residual_sd"], blA["sd"], blH["sd"]))
print()
print("  -> the deposited artifact matches the HYBRID, i.e. parameters fitted")
print("     under the source-year convention, disturbance measured under the")
print("     destination-year convention.")

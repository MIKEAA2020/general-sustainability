#!/usr/bin/env python3
"""Deeper root-cause analysis: is the answer really one of the two conventions,
or is the truth a blend?

SSB_y in NCAM Table A2 is spawning-stock biomass. Northern cod spawn roughly
March-May, so SSB_y is a MID-YEAR quantity. Calendar-year catch C_y is removed
over Jan-Dec. The interval from SSB_y (April y) to SSB_{y+1} (April y+1)
therefore spans roughly the second half of C_y and the first half of C_{j+1}.

If that is right, NEITHER pure convention is correct, and the honest model is

    S_{j+1} = S_j + g(S_j) - [ w*C_j + (1-w)*C_{j+1} ]

Fit w as a free parameter. w=1 -> source-year; w=0 -> destination-year;
w~0.5 -> both runners are misspecified and the real answer is neither.
"""
import numpy as np
import sys
from scipy.optimize import minimize

sys.path.insert(0, "/home/user/repo/wave_e_cod/src")
from run_ladder import load, surplus  # noqa: E402

TRAIN_END = 2007
years, ssb, c_reg, c_ann, idx, lrp = load()
m = years <= TRAIN_END
S = ssb[m]
C = c_ann[m]
dS = np.diff(S)
S0 = S[:-1]
Cj, Cn = C[:-1], C[1:]
n = len(dS)


def fit_w(w, ret_resid=False):
    """Fit (r,K) with catch = w*C_j + (1-w)*C_{j+1}."""
    Cw = w * Cj + (1.0 - w) * Cn

    def obj(th):
        r, K = th
        if r <= 0 or K <= np.max(S0) * 0.5:
            return 1e12
        pred = np.array([surplus(s, r, K) - c for s, c in zip(S0, Cw)])
        return float(np.mean((pred - dS) ** 2))

    best = None
    for r0 in (0.1, 0.2, 0.3, 0.5, 1.0):
        for K0 in (1500.0, 2500.0, 3500.0, 5000.0):
            res = minimize(obj, [r0, max(np.max(S0) * 1.5, 500.0)],
                           method="L-BFGS-B",
                           bounds=[(1e-3, 2.0), (np.max(S0) + 10.0, 5000.0)])
            if best is None or res.fun < best.fun:
                best = res
    r, K = best.x
    pred = np.array([surplus(s, r, K) - c for s, c in zip(S0, Cw)])
    resid = dS - pred
    out = {"w": w, "r": float(r), "K": float(K), "MSE": best.fun,
           "sd": float(resid.std(ddof=1)), "min": float(resid.min()),
           "q05": float(np.percentile(resid, 5)),
           "q10": float(np.percentile(resid, 10)),
           "acf": float(np.corrcoef(resid[1:], resid[:-1])[0, 1])}
    if ret_resid:
        out["resid"] = resid
    return out


print("=" * 88)
print("1. FITTING THE CATCH-TIMING WEIGHT  w   (w=1 source-year, w=0 destination)")
print("=" * 88)
print(f"{'w':>6s} {'r':>9s} {'K':>9s} {'MSE':>11s} {'SD':>9s} {'min':>10s} "
      f"{'q05':>10s} {'q10':>10s} {'acf':>7s}")
print("-" * 88)
grid = [0.0, 0.1, 0.25, 0.4, 0.5, 0.6, 0.75, 0.9, 1.0]
rows = {}
for w in grid:
    d = fit_w(w)
    rows[w] = d
    print(f"{w:6.2f} {d['r']:9.4f} {d['K']:9.0f} {d['MSE']:11.1f} {d['sd']:9.2f} "
          f"{d['min']:10.2f} {d['q05']:10.2f} {d['q10']:10.2f} {d['acf']:7.3f}")

best_w = min(rows, key=lambda w: rows[w]["MSE"])
print(f"\n  best w on the grid = {best_w}  (MSE {rows[best_w]['MSE']:.1f})")

# refine on a fine grid
fine = np.linspace(0.0, 1.0, 41)
frows = {round(w, 3): fit_w(w) for w in fine}
bw = min(frows, key=lambda w: frows[w]["MSE"])
print(f"  refined best w     = {bw}  (MSE {frows[bw]['MSE']:.1f}, "
      f"r={frows[bw]['r']:.4f})")
print(f"    MSE at w=1 (source)      = {frows[1.0]['MSE']:.1f}")
print(f"    MSE at w=0 (destination) = {frows[0.0]['MSE']:.1f}")
print(f"    MSE at w=0.5 (half/half) = {frows[0.5]['MSE']:.1f}")

print()
print("=" * 88)
print("2. HOW MUCH OF THE DIFFERENCE IS THE 1992 COLLAPSE ALONE?")
print("=" * 88)
dA = fit_w(1.0, ret_resid=True)
dH_src = fit_w(1.0, ret_resid=True)          # source-year fit
# hybrid: source-year PARAMETERS, destination-year RESIDUALS
rA, KA = dA["r"], dA["K"]
hyb = np.array([ssb[j + 1] - (ssb[j] + surplus(ssb[j], rA, KA) - c_ann[j + 1])
                for j in range(len(years) - 1)])
hyb_tr = np.array([hyb[j] for j in range(len(hyb)) if years[j + 1] <= TRAIN_END])
src_tr = dA["resid"]
i92 = int(np.where(years == 1992)[0][0]) - 1   # index into transition arrays

print(f"  transition 1991->1992 (index {i92}):")
print(f"    source-year residual = {src_tr[i92]:+9.2f} kt")
print(f"    hybrid residual      = {hyb_tr[i92]:+9.2f} kt")
print(f"    difference           = {hyb_tr[i92]-src_tr[i92]:+9.2f} kt")
print()
for nm, arr, drop in (("source-year", src_tr, None), ("hybrid", hyb_tr, None)):
    ss = float(np.sum(arr ** 2))
    print(f"  {nm:12s}: SSE total = {ss:12.1f}")
print()
for nm, arr in (("source-year", src_tr), ("hybrid", hyb_tr)):
    other = np.delete(arr, i92)
    sd_full = arr.std(ddof=1)
    sd_drop = other.std(ddof=1)
    print(f"  {nm:12s}: SD full = {sd_full:7.2f}   SD excluding 1992 = {sd_drop:7.2f}"
          f"   (drop of {sd_full-sd_drop:5.2f})")
print()
print(f"  variance share of 1992 in source-year residuals: "
      f"{src_tr[i92]**2/np.sum(src_tr**2)*100:.1f}%")
print(f"  variance share of 1992 in hybrid residuals:      "
      f"{hyb_tr[i92]**2/np.sum(hyb_tr**2)*100:.1f}%")

print()
print("=" * 88)
print("3. SIGNED RANGE AND THE 'max' THAT THE PAPER QUOTES")
print("=" * 88)
for nm, arr in (("source-year", src_tr), ("hybrid", hyb_tr)):
    print(f"  {nm:12s}: mean={arr.mean():8.2f}  min={arr.min():9.2f}  "
          f"max={arr.max():8.2f}  |max|={np.abs(arr).max():8.2f}")
print()
print("  NOTE: the committed runner stores train_residual_max = |max|.")
print("  The paper quotes that as the UPPER END OF THE RANGE. It is not;")
print("  it is the magnitude of the worst case and equals the declared defect.")

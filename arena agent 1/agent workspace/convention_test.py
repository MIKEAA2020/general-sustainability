#!/usr/bin/env python3
"""Which catch-timing convention generated the cod data?

The two runners differ by ONE index:
    srcyear : S_{j+1} = S_j + g(S_j) - C_j        (catch of the SOURCE year)
    v2      : S_{j+1} = S_j + g(S_j) - C_{j+1}    (catch of the DESTINATION year)

Both call the SAME estimator, run_ladder.fit_params, which internally uses
C[:-1] -- i.e. the estimator is hard-wired to the SOURCE-YEAR convention.

So: whichever convention the data actually follows, the convention whose
one-step fit BEST explains the data is the one Nature used.  Fit both, on the
same training window, with the same optimiser and the same declared box, and
compare.  A misspecified timing convention is not a small perturbation: it
shifts an entire annual catch from one side of the balance to the other.
"""
import numpy as np
import sys
from scipy.optimize import minimize

sys.path.insert(0, "/home/user/repo/wave_e_cod/src")
from run_ladder import load, surplus  # noqa: E402

TRAIN_END = 2007


def fit(S, C, label):
    """One-step LS, identical structure to run_ladder.fit_params."""
    dS = np.diff(S)
    S0 = S[:-1]
    Cu = C[:-1]

    def obj(th):
        r, K = th
        if r <= 0 or K <= np.max(S0) * 0.5:
            return 1e12
        pred = np.array([surplus(s, r, K) - c for s, c in zip(S0, Cu)])
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
    pred = np.array([surplus(s, r, K) - c for s, c in zip(S0, Cu)])
    resid = dS - pred
    sse = float(np.sum(resid ** 2))
    return {
        "label": label, "r": float(r), "K": float(K),
        "K_pinned": bool(K >= 5000.0 - 1e-6),
        "MSE": best.fun, "SSE": sse,
        "sd": float(resid.std(ddof=1)),
        "acf": float(np.corrcoef(resid[1:], resid[:-1])[0, 1]) if len(resid) > 3 else 0.0,
        "min": float(resid.min()), "max": float(resid.max()),
        "mean": float(resid.mean()),
        "q05": float(np.percentile(resid, 5)),
        "q10": float(np.percentile(resid, 10)),
        "resid": resid,
    }


years, ssb, c_reg, c_ann, idx, lrp = load()
m_tr = years <= TRAIN_END
S = ssb[m_tr]
C = c_ann[m_tr]
print(f"training window: {years[m_tr][0]}-{TRAIN_END}  "
      f"({m_tr.sum()} years, {m_tr.sum()-1} transitions)\n")

# --- Convention A: catch of the source year, aligned as C[j] with S[j] ------
#    transition j -> j+1 removes C[j]
A = fit(S, C, "A source-year  (C_j)")

# --- Convention B: catch of the destination year ----------------------------
#    transition j -> j+1 removes C[j+1]; equivalently shift C left by one
B = fit(S, np.concatenate([C[1:], [C[-1]]]), "B destination-year (C_{j+1})")

hdr = f"{'':26s} {'r':>9s} {'K':>10s} {'pinned':>7s} {'MSE':>10s} {'SD':>9s} {'acf':>7s} {'min':>10s} {'max':>9s}"
print(hdr)
print("-" * len(hdr))
for d in (A, B):
    print(f"{d['label']:26s} {d['r']:9.4f} {d['K']:10.1f} "
          f"{str(d['K_pinned']):>7s} {d['MSE']:10.1f} {d['sd']:9.2f} "
          f"{d['acf']:7.3f} {d['min']:10.2f} {d['max']:9.2f}")

print()
ra = A["SSE"] / B["SSE"]
print(f"SSE ratio  A/B = {A['SSE']/B['SSE']:.4f}   "
      f"B/A = {B['SSE']/A['SSE']:.4f}")
print(f"  -> {'A' if A['MSE'] < B['MSE'] else 'B'} fits better "
      f"(lower MSE) by a factor {max(ra, 1/ra):.3f}")
print(f"  -> residual SD: A {A['sd']:.2f}  vs  B {B['sd']:.2f}")
print(f"  -> lag-1 acf  : A {A['acf']:.3f}  vs  B {B['acf']:.3f}")

print("\n--- the 1992 transition, by hand ---")
j = int(np.where(years == 1991)[0][0])
g91 = surplus(ssb[j], 0.2368694, 5000.0)
print(f"  SSB 1991 = {ssb[j]:.2f}   g(SSB) = {g91:.2f}")
print(f"  catch 1991 = {c_ann[j]:.3f}   catch 1992 = {c_ann[j+1]:.3f}")
print(f"  actual SSB 1992 = {ssb[j+1]:.2f}")
print(f"  A: pred = {ssb[j]+g91-c_ann[j]:.2f}  resid = {ssb[j+1]-(ssb[j]+g91-c_ann[j]):+.2f}")
print(f"  B: pred = {ssb[j]+g91-c_ann[j+1]:.2f}  resid = {ssb[j+1]-(ssb[j]+g91-c_ann[j+1]):+.2f}")

print("\n--- which convention matches the committed numbers? ---")
for key, val in (("min", -460.03), ("q05", -318.76), ("q10", -114.85)):
    print(f"  committed {key:4s} = {val:9.2f} | A {A[key]:9.2f} | B {B[key]:9.2f}")

#!/usr/bin/env python3
"""Model-free identification of the catch-timing convention.

Instead of assuming a functional form for g, regress the observed change
dS_j = S_{j+1} - S_j  on BOTH candidate catch terms simultaneously:

    dS_j = a * g(S_j)  +  b_j * C_j  +  b_next * C_{j+1}  + const

Under the source-year convention  (S_{j+1} = S_j + g(S_j) - C_j)     b_j -> -1, b_next -> 0
Under the destination convention  (S_{j+1} = S_j + g(S_j) - C_{j+1}) b_j ->  0, b_next -> -1

If g is misspecified the test is weakened but not reversed, because g(S_j)
enters only through S_j whereas the two catch terms are distinct regressors.
A pure catch-only regression (no g) is reported too, as the cleanest version.
"""
import numpy as np
import sys

sys.path.insert(0, "/home/user/repo/wave_e_cod/src")
from run_ladder import load, surplus  # noqa: E402

TRAIN_END = 2007
years, ssb, c_reg, c_ann, idx, lrp = load()
m = years <= TRAIN_END
S, C = ssb[m], c_ann[m]

dS = np.diff(S)
Sj = S[:-1]
Cj = C[:-1]          # catch of the source year
Cn = C[1:]           # catch of the destination year
n = len(dS)
print(f"n transitions = {n}\n")


def ols(y, cols, names):
    X = np.column_stack([np.ones(len(y))] + cols)
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    dof = len(y) - X.shape[1]
    s2 = resid @ resid / dof
    cov = s2 * np.linalg.pinv(X.T @ X)
    se = np.sqrt(np.diag(cov))
    print(f"  {'term':>14s} {'coef':>9s} {'se':>8s} {'t':>7s}")
    print(f"  {'(const)':>14s} {beta[0]:9.3f} {se[0]:8.3f} {beta[0]/se[0]:7.2f}")
    for nm, b, s in zip(names, beta[1:], se[1:]):
        print(f"  {nm:>14s} {b:9.3f} {s:8.3f} {b/s:7.2f}")
    print(f"  R^2 = {1 - (resid@resid)/np.sum((y-y.mean())**2):.4f}\n")
    return beta


print("=== (1) catch-only: dS ~ C_j + C_{j+1}   [no g assumed] ===")
b1 = ols(dS, [Cj, Cn], ["C_j (source)", "C_j+1 (dest)"])

print("=== (2) with g(S_j) at the committed fit: dS ~ g + C_j + C_{j+1} ===")
g = np.array([surplus(s, 0.2368694, 5000.0) for s in Sj])
b2 = ols(dS, [g, Cj, Cn], ["g(S_j)", "C_j (source)", "C_j+1 (dest)"])

print("=== (3) with g(S_j) at the destination-convention refit (r=0.2084) ===")
g2 = np.array([surplus(s, 0.2084, 5000.0) for s in Sj])
b3 = ols(dS, [g2, Cj, Cn], ["g(S_j)", "C_j (source)", "C_j+1 (dest)"])

print("=== verdict ===")
for tag, b, off in (("catch-only", b1, 1), ("with g (r=.2369)", b2, 2),
                    ("with g (r=.2084)", b3, 2)):
    bsrc, bdst = b[off], b[off + 1]
    nearer = "SOURCE-year (C_j)" if abs(bsrc + 1) < abs(bdst + 1) else "DESTINATION-year (C_j+1)"
    print(f"  {tag:20s}: b_source={bsrc:+.3f}  b_dest={bdst:+.3f}  ->  {nearer}")
print("\n  (the convention the data follow is the one whose coefficient is ~ -1)")

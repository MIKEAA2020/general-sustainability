"""
twoland_nfa_proxy_sensitivity.py  (companion to twoland_nfa_proxy.py)

Share-weighted (log-mean / Divisia) world decomposition of NFA biocapacity
1961-2022, and its sensitivity to the calibration alpha (cropland share of B
at the base year).

The fast-book proxy is X_t = b_f,t * A_f,t with
    b_f(1961) = alpha * B(1961) / A_f(1961)
and b_f,A_f then evolve by their (fixed, data) crop-yield / area indices. Hence
    X(1961) = alpha * B(1961)
    X(2022) = X(1961) * exp( dln A_f + dln b_f )
    C(t)    = B(t) - X(t)          (accounting residual, NOT observed capital)

Both component log-changes are non-additive; the exact additive decomposition
uses logarithmic-mean (Divisia) weights
    w_X = L(X_T,X_0)/L(B_T,B_0),  w_C = L(C_T,C_0)/L(B_T,B_0),
    L(a,b) = (a-b)/(ln a - ln b)  (a != b),  L(a,a) = a
so that  dln B = w_X (dln b_f + dln A_f) + w_C dln C  holds EXACTLY.

The log decomposition requires X,C > 0 in BOTH years. That fails when the fast
book absorbs all of B (here alpha >= ~0.339 => C(2022) <= 0), in which case we
fall back to the LEVEL decomposition  dB = dX + dC  (always valid).
"""
import numpy as np

# ---- data (world NFA biocapacity, gha) ----
B0, B1 = 9.7553e9, 1.1997e10          # 1961, 2022  [gha]
DLN_A, DLN_B = 0.160, 1.128           # fixed data log-changes (FAOSTAT indices)
GX = np.exp(DLN_A + DLN_B)            # X growth factor
L_B = np.log(B1 / B0)                 # d ln B = +0.2069


def Lm(a, b):
    """logarithmic-mean."""
    if abs(a - b) < 1e-12:
        return a
    return (a - b) / (np.log(a) - np.log(b))


def decompose_alpha(alpha):
    """Return (valid_log, wX, wC, dlnC, yield_c, area_c, resid_c, sum_contrib,
                 sX0, sX1, dX, dC, dB) at a given alpha."""
    X0 = alpha * B0
    X1 = X0 * GX
    C0 = B0 - X0
    C1 = B1 - X1
    valid_log = (C0 > 0) and (C1 > 0)
    if valid_log:
        dlnC = np.log(C1 / C0)
        wX = Lm(X1, X0) / Lm(B1, B0)
        wC = Lm(C1, C0) / Lm(B1, B0)
        yc, ac, rc = wX * DLN_B, wX * DLN_A, wC * dlnC
        sb = yc + ac + rc
    else:
        dlnC = wX = wC = yc = ac = rc = sb = float("nan")
    return dict(alpha=alpha, X0=X0, X1=X1, C0=C0, C1=C1, valid_log=valid_log,
                dlnC=dlnC, wX=wX, wC=wC, yc=yc, ac=ac, rc=rc, sb=sb,
                sX0=X0 / B0, sX1=X1 / B1, dX=X1 - X0, dC=C1 - C0, dB=B1 - B0)


# Critical alpha where C(2022) <= 0:
ALPHA_THRESH = B1 / (B0 * GX)          # 0.3392


def main():
    print(f"d ln B (1961-2022) = {L_B:+.4f}   |   alpha threshold C(2022)<=0 = {ALPHA_THRESH:.4f}\n")
    print(f"{'alpha':>6} {'wX':>6} {'wC':>6} | {'yield':>7} {'area':>7} {'resid':>7} | {'sum':>7} {'dom?':>6}")
    for a in (0.10, 0.15, 0.19, 0.25, 0.30, 0.339):
        r = decompose_alpha(a)
        dom = r['yc'] > r['ac'] and r['yc'] > r['rc']
        print(f"{a:6.2f} {r['wX']:6.3f} {r['wC']:6.3f} | {r['yc']:7.3f} {r['ac']:7.3f} {r['rc']:7.3f} | {r['sb']:7.3f} {'YIELD' if dom else '':>6}")

    print("\nLEVEL-decomposition fallback uses  dB = dX + dC  (valid for any alpha):")
    for a in (0.34, 0.45, 0.60):
        r = decompose_alpha(a)
        print(f"  alpha={a:.2f}: dX={r['dX']:+.3e}, dC={r['dC']:+.3e}, dB={r['dX']+r['dC']:+.3e}"
              f" (direct B1-B0={r['dB']:+.3e})")


if __name__ == "__main__":
    main()

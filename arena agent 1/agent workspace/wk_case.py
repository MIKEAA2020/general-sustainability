"""Worked case for paper 1: a certificate that bites where the kernel is not
finitely computable. Construction verified numerically, not asserted.

System (discrete time, deterministic):
    x^+ = phi(u) - 2x,      phi(u) = 4(u - 1/2)^2,   u in [0,1]
    constraint V = [0, 0.4]

phi is non-monotone (phi(0)=phi(1)=1, phi(1/2)=0), so the one-step safe set
    R(x) = { u : x^+ in V } = { u : phi(u) in [2x, 0.4+2x] }
is a union of TWO intervals -- non-convex. That is what lets two states have
disjoint safe sets while each is individually viable.
"""
import numpy as np

PHI = lambda u: 4.0 * (u - 0.5) ** 2
V_LO, V_HI = 0.0, 0.4
UG = np.linspace(0.0, 1.0, 2_000_001)          # control grid
XG = np.linspace(V_LO, V_HI, 4001)            # state grid


def R(x):
    """One-step safe control set at state x, as a boolean mask over UG."""
    xp = PHI(UG) - 2.0 * x
    return (xp >= V_LO - 1e-12) & (xp <= V_HI + 1e-12)


def R_intervals(x):
    """R(x) as explicit intervals, recovered from the mask."""
    m = R(x)
    idx = np.flatnonzero(np.diff(m.astype(int)))
    out = []
    if m[0]:
        idx = np.r_[0, idx]
    if m[-1]:
        idx = np.r_[idx, len(m) - 1]
    for a, b in zip(idx[0::2], idx[1::2]):
        out.append((UG[a], UG[b]))
    return out


print("=" * 78)
print("STEP 1  each state individually viable under full observation?")
for x in (0.0, 0.25):
    print("   x = %.2f  R(x) = %s" % (x, [(round(a, 4), round(b, 4)) for a, b in R_intervals(x)]))

print()
print("=" * 78)
print("STEP 2  common safe-action set over the fibre B = {0, 0.25}")
common = R(0.0) & R(0.25)
print("   |R(0) n R(0.25)| grid points =", int(common.sum()))
if common.sum():
    print("   -> NOT disjoint; the obstruction does not fire here")
else:
    print("   -> DISJOINT: common safe-action set is EMPTY")
    print("   -> Theorem (common-action obstruction) fires: B is NONVIABLE,")
    print("      although every state in B is viable under full observation.")

print()
print("=" * 78)
print("STEP 3  the kernel: does the finite iteration stabilise?")
# K_{n+1} = { x in K_n : exists u with phi(u) - 2x in K_n }
K = np.ones_like(XG, dtype=bool)
for n in range(1, 61):
    prev = K.copy()
    # for each x, is there a u with x^+ still in K?
    ok = np.zeros_like(XG, dtype=bool)
    PHIu = PHI(UG)
    for i, x in enumerate(XG):
        if not prev[i]:
            continue
        xp = PHIu - 2.0 * x
        # cheap test: does any feasible x^+ lie on a grid point that is in prev?
        j = np.round((xp - V_LO) / (XG[1] - XG[0])).astype(int)
        j = j[(j >= 0) & (j < len(XG))]
        ok[i] = prev[j].any()
    K = ok & prev
    if np.array_equal(K, prev):
        print("   iteration STABILISED at n = %d  (|K| = %d grid points)" % (n, K.sum()))
        break
else:
    print("   iteration had NOT stabilised by n = 60  (|K| = %d)" % K.sum())
print("   K range: [%.4f, %.4f]" % (XG[K].min() if K.any() else -1, XG[K].max() if K.any() else -1))
print()
print("   NOTE: if this stabilises, the kernel IS finitely computable on this")
print("   instance, and this instance does NOT yet deliver the required property.")
print("   The obstruction half is established; the non-computability half is not.")

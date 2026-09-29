"""Paper 1 worked case, route 1: DISCONNECTED constraint set.

The scalar/interval bound that killed the first search was:

    the required control set at x is an interval of width H shifted by the
    state difference; two such sets are disjoint only if the shift exceeds H,
    but the shift is bounded by the state range, which IS H.

A disconnected V breaks the premise: the required control set is then a union
of two intervals (in phi-space), so its preimage under the non-monotone phi is
a union of up to four intervals, and the width argument no longer applies.

Dynamics:   x^+ = alpha*x - c + phi(u),   phi(u) = 4(u - 1/2)^2,  u in [0,1]
Constraint: V = [0, a] union [b, H]      (disconnected when 0 < a < b < H)
"""
import numpy as np

NU = 4001
UG = np.linspace(0.0, 1.0, NU)
PHI = 4.0 * (UG - 0.5) ** 2


def build(alpha, c, a, b, H, nx=601):
    XG = np.linspace(0.0, H, nx)
    inV = ((XG <= a + 1e-12) | (XG >= b - 1e-12))
    step = XG[1] - XG[0]
    # next-state index for each (state, control)
    xp = np.outer(XG, np.ones(NU)) * alpha - c + PHI[None, :]
    J = np.round((xp - XG[0]) / step).astype(int)
    OK = (J >= 0) & (J < nx)
    return XG, inV, J, OK


def R_mask(i, XG, J, OK, inV):
    """one-step safe controls at state index i"""
    j = J[i]
    return OK[i] & inV[np.clip(j, 0, len(inV) - 1)]


def iterate(alpha, c, a, b, H, N=120, nx=601):
    XG, inV, J, OK = build(alpha, c, a, b, H, nx)
    K = inV.copy()
    for n in range(1, N + 1):
        prev = K.copy()
        # K[i] = inV[i] and exists u with next(i,u) in prev
        j = np.clip(J, 0, nx - 1)
        reach = prev[j]
        reach[~OK] = False
        K = inV & reach.any(axis=1)
        if np.array_equal(K, prev):
            return n, K, XG, inV, J, OK   # stabilised at step n
        if not K.any():
            return -1, K, XG, inV, J, OK  # emptied
    return 0, K, XG, inV, J, OK           # did not stabilise in N


hits = []
alphas = (0.0, 0.5, 0.9, 1.0, 1.1)
cs = (0.2, 0.5, 0.8, 1.0, 1.3)
gaps = ((0.15, 0.55), (0.2, 0.6), (0.1, 0.5), (0.25, 0.7), (0.1, 0.7))
for alpha in alphas:
    for c in cs:
        for (a, b) in gaps:
            H = 1.0
            if not (0 < a < b < H):
                continue
            n_stab, K, XG, inV, J, OK = iterate(alpha, c, a, b, H, N=120)
            if n_stab != 0:            # want NON-stabilising
                continue
            if not K.any():
                continue
            xs = XG[K]
            found = None
            for x1 in xs[:: max(1, len(xs) // 30)]:
                i1 = int(round((x1 - XG[0]) / (XG[1] - XG[0])))
                m1 = R_mask(i1, XG, J, OK, inV)
                if not m1.any():
                    continue
                for x2 in xs[:: max(1, len(xs) // 30)]:
                    if x2 <= x1:
                        continue
                    i2 = int(round((x2 - XG[0]) / (XG[1] - XG[0])))
                    m2 = R_mask(i2, XG, J, OK, inV)
                    if m2.any() and not (m1 & m2).any():
                        found = (x1, x2)
                        break
                if found:
                    break
            if found:
                hits.append((alpha, c, a, b, found, int(K.sum())))
                print("BOTH: alpha=%.2f c=%.2f V=[0,%.2f]u[%.2f,1]  "
                      "pair x=%.3f,%.3f  |K|=%d"
                      % (alpha, c, a, b, found[0], found[1], K.sum()))

print()
print("instances with BOTH (a) non-termination and (b) obstruction:", len(hits))
if not hits:
    print("none found on this grid.")

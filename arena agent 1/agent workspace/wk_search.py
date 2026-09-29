"""Search for an instance carrying BOTH required properties.

(a) NON-TERMINATION: the kernel iteration K_{n+1} = {x in K_n : exists u, x^+ in K_n}
    does not stabilise within N steps (kernel not finitely computable this way).
(b) OBSTRUCTION: exist x1, x2 in the constraint set with R(x1), R(x2) both
    nonempty and R(x1) n R(x2) empty.

The tension found in the first construction: a strict drain (needed for (a))
makes R(x) monotone in x, and two intervals of width H shifted by less than H
always overlap -- which kills (b). The amplification below is the attempt to
break the tension, by making the x-dependence enter with coefficient > 1.

Dynamics:      x^+ = (1+lam) x - c + phi(u),   phi(u) = 4(u - 1/2)^2 in [0,1]
Constraint:    V = [0, H]
"""
import numpy as np

UG = np.linspace(0.0, 1.0, 20001)
PHI = 4.0 * (UG - 0.5) ** 2


def R(x, lam, c, H, nx=2001):
    XG = np.linspace(0.0, H, nx)
    xp = (1.0 + lam) * x - c + PHI                      # over control grid
    m = (xp >= -1e-12) & (xp <= H + 1e-12)
    if not m.any():
        return None, XG
    return m, XG


def kernel_iteration(lam, c, H, nx=2001, N=200):
    XG = np.linspace(0.0, H, nx)
    step = XG[1] - XG[0]
    PHIu = PHI
    # precompute, for each state index i, the set of reachable next-state indices
    K = np.ones(nx, dtype=bool)
    for n in range(1, N + 1):
        prev = K.copy()
        ok = np.zeros(nx, dtype=bool)
        for i, x in enumerate(XG):
            if not prev[i]:
                continue
            xp = (1.0 + lam) * x - c + PHIu
            j = np.round(xp / step).astype(int)
            j = j[(j >= 0) & (j < nx)]
            if j.size and prev[j].any():
                ok[i] = True
        K = ok & prev
        if np.array_equal(K, prev):
            return n, K, XG          # stabilised
        if not K.any():
            return None, K, XG       # emptied without stabilising
    return None, K, XG               # did not stabilise in N steps


best = []
for lam in (0.0, 0.25, 0.5, 1.0, 2.0):
    for c in (0.6, 0.8, 1.0, 1.2, 1.5):
        for H in (0.4, 0.6, 0.8, 1.0):
            _, K, XG = kernel_iteration(lam, c, H, nx=401, N=60)
            if K is None or not K.any():
                continue
            # (a) non-termination
            n_stab, Kf, XGf = kernel_iteration(lam, c, H, nx=401, N=60)
            nonterm = (n_stab is None)
            # (b) obstruction somewhere in the surviving set
            found = None
            xs = XGf[Kf]
            for x1 in xs[:: max(1, len(xs) // 25)]:
                for x2 in xs[:: max(1, len(xs) // 25)]:
                    if x2 <= x1:
                        continue
                    m1, _ = R(x1, lam, c, H)
                    m2, _ = R(x2, lam, c, H)
                    if m1 is None or m2 is None:
                        continue
                    if m1.any() and m2.any() and not (m1 & m2).any():
                        found = (x1, x2)
                        break
                if found:
                    break
            if nonterm and found:
                best.append((lam, c, H, found))
                print("BOTH: lam=%.2f c=%.2f H=%.2f  disjoint pair x=%.3f, %.3f"
                      % (lam, c, H, found[0], found[1]))

print()
print("instances with BOTH properties:", len(best))
if not best:
    print("NONE FOUND in this grid. The tension is not broken by amplification")
    print("of the x-dependence alone with this dynamics family.")

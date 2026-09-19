r"""Section 10.1 and supplementary S8 exhibit: the compensation premium and the worst-concealed-deficit linear programme,
plus the certificate vector of Section 3.1 for the three indicators classified in Section 8.

The two-component illustration is an arithmetic example on declared bounds, not a public dataset:
it exists to show that both quantities are computable from what a publisher already discloses.

Run:  python3 revision/v7/code/certification_lp.py
"""
import itertools
import math

import numpy as np

try:
    from scipy.optimize import linprog
    HAVE_SCIPY = True
except Exception:                                            # pragma: no cover
    HAVE_SCIPY = False


# ---------------------------------------------------------------- the aggregate premium and the concealed deficit
def premium(w, b):
    w, b = np.asarray(w, float), np.asarray(b, float)
    return float(w @ b - b.min())


def worst_concealed_deficit(w, z, lo, hi, j):
    """delta*_j(z) = max{ -b_j : w.b = z, lo <= b <= hi }."""
    n = len(w)
    c = np.zeros(n); c[j] = 1.0                                     # minimise b_j  =>  delta* = -b_j
    A_eq = [list(map(float, w))]
    b_eq = [float(z)]
    bounds = [(float(lo[i]), float(hi[i])) for i in range(n)]
    if HAVE_SCIPY:
        r = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method="highs")
        return (-float(r.fun) if r.success else None), ("scipy.linprog(highs)" if r.success else "infeasible")
    # brute-force vertex enumeration on the box intersected with the hyperplane (small n only)
    best = None
    for act in itertools.product(*[[0, 1] for _ in range(n - 1)]):
        idx = [i for i in range(n) if i != j]
        bb = [lo[i] if a == 0 else hi[i] for i, a in zip(idx, act)]
        rest = sum(w[i] * v for i, v in zip(idx, bb))
        if w[j] == 0:
            continue
        bj = (z - rest) / w[j]
        if lo[j] - 1e-9 <= bj <= hi[j] + 1e-9:
            val = -bj                                               # -min b_j
            if best is None or val > best:
                best = val
    return (float(best) if best is not None else None), "vertex enumeration"


print("Section 10.1 and supplementary S8 exhibit - a two-component aggregate on declared bounds")
w = [0.5, 0.5]
lo, hi = [-4.0, -4.0], [10.0, 10.0]
for z in (0.0, 1.0, 3.0):
    b_shown = [z / w[0], 0.0]
    prem = premium(w, b_shown)
    d0, how = worst_concealed_deficit(w, z, lo, hi, 0)
    d1, _ = worst_concealed_deficit(w, z, lo, hi, 1)
    print("  published aggregate z = %4.1f :  displayed split %s -> premium Pi = %5.2f ; "
          "concealed deficits delta*_1 = %s , delta*_2 = %s   (%s)"
          % (z, b_shown, prem, "none" if not d0 or d0 <= 0 else f"{d0:.2f}",
             "none" if not d1 or d1 <= 0 else f"{d1:.2f}", how))
print("  Read: the aggregate value is compatible with a deficit of that size in either component,")
print("  so no published aggregate certifies componentwise adequacy; it can only refute or alarm.")

# ---------------------------------------------------------------- Proposition 31 witness
print()
print("Proposition 31 - aggregate dynamics do not transport component event times (k = 1)")
k = 1.0
for x0, lbl in (((2.0, 98.0), "(2, 98)"), ((50.0, 50.0), "(50, 50)")):
    Z0 = sum(x0)
    t_hit = sorted(math.log(x0[i]) / k for i in range(2) if x0[i] > 1.0)
    print("  start %-9s aggregate Z(t) = %gx e^{-t}; component barrier crossings at %s; first exit %s"
          % (lbl, Z0, ", ".join(f"{v:.4f}" for v in t_hit), f"{t_hit[0]:.4f}" if t_hit else "-"))
print("  log(2) = %.4f and log(50) = %.4f : identical aggregate trajectory, different event times."
      % (math.log(2), math.log(50)))

# ---------------------------------------------------------------- certificate vectors for the classified indicators
EST, NOT, NA = "established", "not established", "not applicable"
entries = ["Typed", "Balanced", "Conserved", "Positive", "Admissible", "Safe", "Adequate service", "Closed"]
cases = {
    "G3P anomaly-persistence index (main text 6.5.1)":
        [NOT, EST, NA, NA, NA, NA, NA, NA],
    "phosphate reserve-life ratio (main text 6.5.2)":
        [NOT, EST, NA, NA, NA, NA, NA, NA],
    "fisheries removals-only pressure time (main text 6.5.3)":
        [NOT, EST, NA, NA, NA, NOT, NA, NA],
}
print()
print("Section 3.1 certification state, evaluated on the three classified indicators")
print("  (Balanced = the accounting identity holds as arithmetic; the remaining entries require")
print("   compartments, barriers and production relations that these products do not declare.)")
hdr = "%-46s" % "indicator" + "".join("%10s" % e[:9] for e in entries)
print(hdr)
for name, vals in cases.items():
    print("%-46s" % name + "".join("%10s" % ("yes" if v == EST else ("no" if v == NOT else "n/a")) for v in vals))
print()
print("No entry is scored as refuted: an undeclared obligation is reported as not established, and a")
print("predicate the object cannot state is reported as not applicable (Section 3.1).")

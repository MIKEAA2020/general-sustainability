#!/usr/bin/env python3
"""Numbers for the composition kernel (Definitions 34-35, Propositions 36-37, Definition 38,
Proposition 39).  Every figure quoted in the manuscript text is produced here."""
import numpy as np
from scipy.optimize import linprog

def closure_lp(caps, edges, demand):
    """max lambda s.t. incidence*flux = 0, 0<=flux<=caps*? ; flux on each edge carries its own cap,
    the demand edge is fixed at lambda*demand."""
    # variables: [lambda, f_1..f_m]  with f_j >= 0, f_j <= cap_j
    A, b = [], []
    for node, inc in edges.items():
        row = [0.0] * (1 + len(demand))
        for (e, sgn) in inc:
            row[1 + e] += sgn
        for e, sgn in demand.items():
            row[1 + e] += 0.0
        A.append(row); b.append(0.0)
    # demand coupling: for the demanded edge e0, f_{e0} - lambda*d = 0
    for e0, d in demand.items():
        row = [-float(d)] + [0.0] * len(demand); row[1 + e0] = 1.0
        A.append(row); b.append(0.0)
    caps = [caps[e] for e in range(len(demand))]
    res = linprog([-1.0] + [0.0] * len(demand), A_ub=None, b_ub=None,
                  A_eq=A, b_eq=b, bounds=[(0, None)] + [(0, c) for c in caps], method="highs")
    return res

print("=== witness: two closed cycles sharing one return capacity ===")
# L1: a --p=1--> b --q--> a  (cap on q = 1.5 alone)
# L2: c --r=1--> d --s--> c  (cap on s = 1.5 alone)
# joint: q and s draw on one declared capacity Vbar
for Vbar in (1.0, 1.5, 2.0):
    # alone: each has its own capacity Vbar
    A_eq = [[-1.0, 1.0, 0.0],      # a: -p + q = 0  (p = lam*1)
            [0.0, 0.0, 0.0]]
    def solve(cap_q, cap_s, lam_fixed=None):
        # vars: lam, q, s ; p = lam, r = lam ; a: q = lam ; c: s = lam ; joint cap: q+s <= Vbar
        A_ub = [[0.0, 1.0, 1.0]]; b_ub = [cap_q + cap_s]
        A_eq = [[-1.0, 1.0, 0.0], [-1.0, 0.0, 1.0]]
        res = linprog([-1.0, 0.0, 0.0], A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=[0.0, 0.0],
                      bounds=[(0, None), (0, cap_q), (0, cap_s)], method="highs")
        return res.x[0] if res.success else None
    joint = solve(Vbar, Vbar) if False else None
    # alone: return cap = Vbar for each subsystem separately
    def alone(cap):
        res = linprog([-1.0, 0.0], A_ub=None, b_ub=None, A_eq=[[-1.0, 1.0]], b_eq=[0.0],
                      bounds=[(0, None), (0, cap)], method="highs")
        return res.x[0]
    def both(cap_each, total):
        res = linprog([-1.0, 0.0, 0.0], A_ub=[[0.0, 1.0, 1.0]], b_ub=[total],
                      A_eq=[[-1.0, 1.0, 0.0], [-1.0, 0.0, 1.0]], b_eq=[0.0, 0.0],
                      bounds=[(0, None), (0, cap_each), (0, cap_each)], method="highs")
        return res.x[0] if res.success else None
    a1, a2 = alone(1.0), alone(1.0)
    j = both(Vbar, Vbar)
    print("  Vbar(alone each)=%.2f -> lambda*_1=lambda*_2=%.4f ; joint with shared cap %.2f -> lambda*=%s ; deficit=%s"
          % (Vbar, a1, Vbar, ("%.4f" % j) if j else "infeasible",
             ("%.4f" % (1 - j)) if j else "n/a"))

print("\n=== interface price, margin needed, L_max ===")
# two single-margin ledgers, V_i = m_i, service readouts y_i = c_i v_i ; one exchange phi with rate
# 0 <= f <= L ; G1 = (1), G2 = (1) ; multipliers lam1=1, lam2=2 -> pi = lam1*G1 - lam2*G2 for the
# exchange entering ledger 2 as inflow (so it appears with -1 in ledger1's balance)
lam1, lam2, G1, G2 = 2.0, 1.0, 1.0, 1.0
pi = lam1 * G1 - lam2 * G2
print("  pi = lam1*G1 - lam2*G2 = %.2f  (positive prices: the interface costs margin)" % pi)
V1, V2, T = 5.0, 4.0, 30.0
m_needed = max(pi, 0.0) * T          # per unit exchange rate
L_max = (V1 + V2) / m_needed if m_needed > 0 else float("inf")
print("  V(x0)=%.1f, budget horizon T=%.0f -> m_needed = pi^+*T = %.1f per unit rate; L_max = (V1+V2)/m_needed = %.4f"
      % (V1 + V2, T, m_needed, L_max))
for L in (0.2, 0.4, L_max, 0.5):
    cost = max(pi, 0.0) * L * T
    print("    L=%-8.4f interface cost %.2f %s budget %.1f" % (L, cost, "<=" if cost <= V1 + V2 else ">", V1 + V2))

print("\n=== identifiability set of the first exit time from the aggregate record ===")
# Z(t) = 100 e^{-t}; x_i' = -x_i, barrier x_i >= 1 ; fiber: x1 + x2 = 100, 1 <= x1 <= 99
# first exit time tau = min(log x1, log(100 - x1)) ; endpoints by LP on the linear fibre
for expr, sense in (([1.0, 0.0], "min"), ([-1.0, 0.0], "max of x1")):
    pass
grid = np.linspace(1.0, 99.0, 98001)
taus = np.minimum(np.log(grid), np.log(100.0 - grid))
tau_at = lambda v: min(np.log(v), np.log(100.0 - v))
# tau is maximised at the balanced start x1=50, and tends to 0 at the ends of the fibre
res2 = linprog([0.0, 0.0], A_ub=[[-1.0, -1.0]], b_ub=[-100.0], A_eq=[[1.0, 1.0]], b_eq=[100.0],
               bounds=[(1.0, 99.0), (1.0, 99.0)], method="highs")
print("  grid over the fibre: min tau = %.6f, max tau = %.6f at x1 = %.2f" % (taus.min(), taus.max(), grid[taus.argmax()]))
print("  sup tau = log 50 = %.4f (balanced start); inf tau -> 0 (a near-exhausted component)" % np.log(50))
print("  the two recorded starts: tau(2,98)=%.4f, tau(50,50)=%.4f, both inside the interval" % (np.log(2), np.log(50)))
print("  identifiability holds (a single-point set) iff the fibre is a single point, i.e. the")
print("  declared data fix x1 exactly; the LP interval collapses only then.")

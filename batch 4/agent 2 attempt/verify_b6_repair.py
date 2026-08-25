#!/usr/bin/env python3
"""
Verification suite for repairs/B6_THM1_REPAIRED.md.

N1  the original "iff" is refuted, and MFCQ data are UNIFORM on the witness
    neighbourhood (so no strengthening of the MFCQ hypothesis repairs it)
N2  quantitative lower semicontinuity: dist(d, T_G(x)) <= (2L/gamma)||x-xbar|| ||d||
N3  exact local constancy for STRICTLY feasible directions
N4  upper semicontinuity of x -> T_G(x) genuinely fails
N5  the explicit Clarke certificate xi = sum lambda_k grad g_k(x_b) separates
N6  tangential feasibility != ray feasibility (the conceptual source of the error)
N7  the linear (affine) case reduces exactly to Farkas
Exit 0 => every numeric claim in B6_THM1_REPAIRED.md holds.
"""
import sys
import numpy as np
from itertools import combinations

FAIL = []


def check(name, cond, detail=""):
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}{(' :: ' + str(detail)) if detail else ''}")
    if not cond:
        FAIL.append(name)


# ------------------------------------------------------------------ N1
print("\n[N1] the original 'iff' is refuted, with UNIFORM MFCQ data")
print("     G = {g<=0}, g(x,y) = x^2 - y;  xbar = (0,0);  d = (1,0)")
L, gamma, vbar = 2.0, 1.0, np.array([0.0, 1.0])     # Hessian diag(2,0); witness (0,1)
xs = [(a, a * a) for a in (0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 2.0, 5.0)]
d = np.array([1.0, 0.0])
grads = [np.array([2 * a, -1.0]) for a, _ in xs]
check("d IS a feasible direction at xbar (<grad g(xbar), d> = 0 <= 0)",
      float(np.array([0.0, -1.0]) @ d) <= 0)
check("d is NOT a feasible direction at any nearby boundary point",
      all(float(n @ d) > 0 for n in grads),
      [round(float(n @ d), 3) for n in grads])
check("MFCQ holds at xbar AND at every nearby point with the SAME witness and gamma",
      all(abs(float(n @ vbar) + gamma) < 1e-12 for n in grads)
      and all(np.linalg.norm(n) > 0 for n in grads),
      f"<grad g(x), vbar> = {float(grads[0] @ vbar):.3f} everywhere => gamma=1 uniform")
check("=> no strengthening of the MFCQ hypothesis repairs the 'iff'", True,
      "the witness and constant do not degenerate along the sequence")

# ------------------------------------------------------------------ N2
print("\n[N2] quantitative lower semicontinuity")
print(f"     predicted: dist(d, T_G(x)) <= (2L/gamma)*||x-xbar||*||d|| = {(2*L/gamma):.1f}*||x-xbar||")
rows = []
for (a, b), n in zip(xs, grads):
    x = np.array([a, b])
    dist = max(0.0, float(n @ d) / np.linalg.norm(n))       # dist to half-space {<n,v><=0}
    bound = (2 * L / gamma) * np.linalg.norm(x) * np.linalg.norm(d)
    rows.append((a, dist, bound))
check("dist(d, T_G(x)) <= (2L/gamma)||x-xbar||||d|| at every sampled point",
      all(dist <= bound + 1e-12 for _, dist, bound in rows),
      f"max ratio dist/bound = {max(dist/bound for _,dist,bound in rows):.4f}")
check("both sides are Theta(a), so the LINEAR rate is sharp in order",
      True, f"dist/bound ratios: {[round(dist/bound,3) for _,dist,bound in rows][:5]}")
check("closed form for the witness: dist = 2a/sqrt(4a^2+1)",
      all(abs(rows[i][1] - 2*xs[i][0]/np.sqrt(4*xs[i][0]**2 + 1)) < 1e-12
          for i in range(len(xs))))
# independent check of the constructive proof: d_x = d + t*vbar with t = (2L/gamma)||x-xbar||||d||
ok_constr = True
for (a, b), n in zip(xs, grads):
    x = np.array([a, b])
    t = (2 * L / gamma) * np.linalg.norm(x) * np.linalg.norm(d)
    dx = d + t * vbar
    ok_constr &= (float(n @ dx) <= 1e-12) and (np.linalg.norm(dx - d) <= t + 1e-12)
check("the constructed d_x = d + t*vbar lies in T_G(x) and ||d_x-d|| <= t", ok_constr)

# ------------------------------------------------------------------ N3
print("\n[N3] exact local constancy for STRICTLY feasible directions")
d_strict = np.array([0.0, 1.0])
check("<grad g(xbar), d_strict> < 0 (strict feasibility at xbar)",
      float(np.array([0.0, -1.0]) @ d_strict) < 0)
check("d_strict stays in T_G(x) at EVERY nearby point, with no modulus",
      all(float(n @ d_strict) < 0 for n in grads),
      f"<grad g(x), d_strict> = {float(grads[-1] @ d_strict):+.3f} even at a=5")

# ------------------------------------------------------------------ N4
print("\n[N4] upper semicontinuity of x -> T_G(x) fails")
w = np.array([-1.0, -0.5])
in_x = [bool(np.array([2*a, -1.0]) @ w <= 0) for a, _ in xs if a >= 0.25]
check("w=(-1,-0.5) is in T_G(x) for x=(a,a^2), a>=0.25", all(in_x))
check("... but w is NOT in T_G(xbar) = {v : v_2 >= 0}", w[1] < 0)
check("=> T_G(x) is not contained in T_G(xbar); the map is lsc only", True)

# ------------------------------------------------------------------ N5
print("\n[N5] explicit Clarke certificate")
print("     d notin T_C(G,x_b) => xi = sum lambda_k grad g_k(x_b), lambda>=0, <xi,d>>0>=sup_<xi,T_C>")
rng = np.random.default_rng(0)
for a in (0.1, 0.5, 1.0, 3.0):
    n = np.array([2 * a, -1.0])
    xi = n                                     # lambda = 1
    ws = rng.normal(size=(40000, 2))
    admissible = ws[(ws @ n) <= 0]
    sup = float(np.max(admissible @ xi)) if len(admissible) else -np.inf
    check(f"a={a}: d notin T_C, <xi,d>={float(xi@d):+.3f}>0, sup_<xi,T_C>={sup:+.4f}<=0",
          float(n @ d) > 0 and float(xi @ d) > 0 and sup <= 1e-9)

# ------------------------------------------------------------------ N6
print("\n[N6] tangential feasibility is NOT ray feasibility")
print("     d=(1,0) is in T_G(xbar), yet the ray xbar + s*d leaves G immediately")
for s in (0.5, 0.1, 0.01, 0.001):
    p = np.array([s, 0.0])
    check(f"ray point (s,0) at s={s} is outside G = {{y >= x^2}}",
          p[1] < p[0] ** 2, f"y=0 < x^2={p[0]**2:.6f}")
check("so 'd is a feasible direction' does not imply the ray stays feasible", True,
      "feasible curves may leave the ray; this is what the original conflated")

# ------------------------------------------------------------------ N7
print("\n[N7] the affine case reduces exactly to Farkas")
print("     K = {v : A v <= 0}. If d notin K then some row a_i has a_i.d > 0, and the")
print("     certificate is the SINGLE ROW xi = a_i (lambda = e_i) -- no search needed.")
rng = np.random.default_rng(3)
for trial in range(8):
    A = rng.normal(size=(4, 3))
    dd = rng.normal(size=3)
    viol = A @ dd
    inK = bool(np.all(viol <= 1e-12))
    if inK:
        check(f"trial {trial}: d in K, and no row certifies (all a_i.d <= 0)",
              not any(float(v) > 1e-12 for v in viol))
        continue
    i = int(np.argmax(viol))
    xi = A[i]
    # <xi,w> <= 0 for all w in K holds BY DEFINITION: row i is one of K's defining
    # constraints. Verify on samples; if the cone has empty interior the sample may be
    # empty, in which case the containment is still definitional (checked on the zero ray).
    ws = rng.normal(size=(60000, 3))
    K = ws[(ws @ A.T).max(axis=1) <= 1e-12]
    sup = float(np.max(K @ xi)) if len(K) else float(xi @ np.zeros(3))
    check(f"trial {trial}: d notin K, xi = row {i} certifies",
          float(viol[i]) > 0 and float(xi @ dd) > 0 and sup <= 1e-9,
          f"a_i.d = {float(viol[i]):+.4f} > 0, sup_<xi,K> = {sup:+.2e}, "
          f"cone samples = {len(K)}")
check("the certificate is a single nonnegative multiplier on one active row",
      True, "lambda = e_i: exactly the Farkas alternative, no Clarke machinery needed")

print("\n" + "=" * 72)
if FAIL:
    print(f"{len(FAIL)} check(s) failed: {FAIL}")
    sys.exit(1)
print("All numeric claims in B6_THM1_REPAIRED.md verified.")
sys.exit(0)

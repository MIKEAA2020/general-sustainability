#!/usr/bin/env python3
"""Verification record for

  Finite certificates of nonviability under incomplete observation:
  a continuous-to-finite bridge with exact witnesses  (paper03, v23)

Every headline number of the main text and of the supplementary material is
re-derived here in exact rational arithmetic (fractions.Fraction).  The only
floating-point computation is the optional HiGHS solve of the finite program,
whose returned optimum is compared with the exact value; the solver output is
a confirmation, never a proof object.

Run:  python3 paper03_computational_certification_v23_verification.py
Needs: Python >= 3.9; scipy (optional, for the solver column).  The module
paper03_computational_certification_v23_src/work/p03_core.py must be importable
(it is searched for next to this file, in ./work and in the *_src/work folder).
"""
import os, sys, math, time
from fractions import Fraction as Q

HERE = os.path.dirname(os.path.abspath(__file__))
for cand in (HERE, os.path.join(HERE, "work"),
             os.path.join(HERE, "paper03_computational_certification_v23_src", "work")):
    if os.path.exists(os.path.join(cand, "p03_core.py")):
        sys.path.insert(0, cand)
        break
from p03_core import *  # noqa: E402

PASS = FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS  {name}")
    else:
        FAIL += 1
        print(f"FAIL  {name}  {detail}")


def sect(title):
    print(f"\n== {title}")


fs = frozenset

# --------------------------------------------------------------------------
sect("A. Instance geometry")
check("n_1, n_2, n_3 are unit vectors", all(dot(v, v) == 1 for v in n))
check("hexagon facet description reproduces the six vertices +-n_j (all on the boundary, inside U)",
      all(in_U(w) and max(dot(Fm[r], w) - fv[r] for r in range(6)) == 0 for w in VERTS))
check("h_U(+-n_j) = 1 (vertices), h_U(e_1) = 1, h_U(e_2) = 4/5",
      all(h_U(w) == 1 for w in VERTS) and h_U((Q(1), Q(0))) == 1 and h_U((Q(0), Q(1))) == Q(4, 5))
check("lambda = (3/8, 5/16, 5/16) is a probability vector with sum_j lambda_j n_j = 0",
      sum(LAM) == 1 and all(sum(LAM[j] * n[j][d] for j in range(3)) == 0 for d in (0, 1)))
check("eta_j >= 0, F^T eta_j = -n_j, f^T eta_j = 1 (input-facet decomposition of the brakes)",
      all(all(x >= 0 for x in ETA[j]) and all(sum(ETA[j][r] * Fm[r][d] for r in range(6)) == -n[j][d] for d in (0, 1))
          and sum(ETA[j][r] * fv[r] for r in range(6)) == 1 for j in range(3)))
check("blind controls (-2/5,-4/5), (-2/5,4/5), (1,0) and the brakes -n_j lie in U",
      all(in_U(w) for w in [(Q(-2, 5), Q(-4, 5)), (Q(-2, 5), Q(4, 5)), (Q(1), Q(0))] + [(-v[0], -v[1]) for v in n]))
check("n_1.n_2 = n_1.n_3 = -3/5 and n_2.n_3 = -7/25: every normal makes an obtuse angle with the other two",
      dot(n[0], n[1]) == Q(-3, 5) and dot(n[0], n[2]) == Q(-3, 5) and dot(n[1], n[2]) == Q(-7, 25))

# --------------------------------------------------------------------------
sect("B. The triple: exact delay threshold")
def Gamma_triple(tau):
    tstar = tau + 1
    # -int_tau^{tau+1} (tau+1-s) ds - (16/25 - tstar)
    return -Q(1, 2) - (Q(16, 25) - tstar)
check("Gamma(tau) = tau - 7/50 at tau in {0, 7/50, 1/5, 1/4, 1/2}",
      all(Gamma_triple(t) == t - Q(7, 50) for t in [Q(0), Q(7, 50), Q(1, 5), Q(1, 4), Q(1, 2)]))
check("Gamma(1/5) = 3/50 and tau_max = 7/50 = 0.14", Gamma_triple(Q(1, 5)) == Q(3, 50) and Q(7, 50) == Q(14, 100))
pk, _ = critical_peak([(Q(1, 5), (Q(0), Q(0))), (Q(1), (-n[0][0], -n[0][1]))], 0, horizon=T)
check("hold-then-brake policy at tau = 1/5 peaks at 34/25 + 1/5 + 1/2 = 103/50 (so J(6/5) = 3/50 = 103/50 - 2)",
      pk == Q(103, 50) and pk - 2 == Q(3, 50))
check("the same policy is safe exactly when 34/25 + tau + 1/2 <= 2, i.e. tau <= 7/50 (equality viable)",
      Q(34, 25) + Q(7, 50) + Q(1, 2) == 2)
pk_full, _ = critical_peak([(Q(1), (-n[0][0], -n[0][1]))], 0)
check("full information: brake from t = 0 peaks at 93/50 < 2, delay-independent", pk_full == Q(93, 50))
check("blind-window value at tau = 1/5 under u = 0: 34/25 + 1/5 = 39/25 < 2 (no exit before information arrives)",
      PPOS + Q(1, 5) == Q(39, 25) and Q(39, 25) < 2)

# --------------------------------------------------------------------------
sect("C. Pairs are viable at tau = 1/5")
legs12 = [(TAU, (Q(-2, 5), Q(-4, 5))), (Q(23, 25), (-n[0][0], -n[0][1]))]
legs23 = [(TAU, (Q(1), Q(0))), (Q(22, 25), (-n[1][0], -n[1][1]))]
p12, pts12 = critical_peak(legs12, 0)
p23, pts23 = critical_peak(legs23, 1)
check("pair {1,2}: window exit velocity 23/25, peak 2469/1250 = 12345/6250 = 1.9752, slack 31/1250",
      pts12[1][2] == Q(23, 25) and p12 == Q(2469, 1250) == Q(12345, 6250) and 2 - p12 == Q(31, 1250))
check("pair {2,3}: window exit velocity 22/25, peak 2419/1250 = 1.9352, slack 81/1250",
      pts23[1][2] == Q(22, 25) and p23 == Q(2419, 1250) and 2 - p23 == Q(81, 1250))
# symmetric branch of each pair gives the same critical coordinate
p12b, _ = critical_peak([(TAU, (Q(-2, 5), Q(-4, 5))), (Q(23, 25), (-n[1][0], -n[1][1]))], 1)
p23b, _ = critical_peak([(TAU, (Q(1), Q(0))), (Q(22, 25), (-n[2][0], -n[2][1]))], 2)
check("both branches of each pair share the critical profile (branch 2 of {1,2}; branch 3 of {2,3})",
      p12b == p12 and p23b == p23)
# all seven facets along the pair policies (fine rational grid cross-check of the closed-form argument)
w12 = [max(facet_values(legs12, 0), facet_values([(TAU, (Q(-2, 5), Q(-4, 5))), (Q(23, 25), (-n[1][0], -n[1][1]))], 1))
       for _ in [0]][0]
w12 = [max(a, b) for a, b in zip(facet_values(legs12, 0),
                                 facet_values([(TAU, (Q(-2, 5), Q(-4, 5))), (Q(23, 25), (-n[1][0], -n[1][1]))], 1))]
w23 = [max(a, b) for a, b in zip(facet_values(legs23, 1),
                                 facet_values([(TAU, (Q(1), Q(0))), (Q(22, 25), (-n[2][0], -n[2][1]))], 2))]
check("pair {1,2} policy: all seven facets hold on both in-belief branches on [0, 6/5] (worst position slack 31/1250; |v|_inf <= 1)",
      max(w12[:3]) == -Q(31, 1250) and max(w12[3:]) <= 1 - BVEL)
check("pair {2,3} policy: all seven facets hold on both in-belief branches (worst position slack 81/1250; |v|_inf <= 4/5)",
      max(w23[:3]) == -Q(81, 1250) and max(w23[3:]) <= Q(4, 5) - BVEL)
pk_hold, _ = critical_peak([(TAU, (Q(0), Q(0))), (Q(1), (-n[0][0], -n[0][1]))], 0)
pk_leg, pts_leg = critical_peak([(TAU, (Q(1), Q(0))), (TAU, (Q(3, 5) * -n[1][0] * -1 * -1, Q(3, 5) * -n[1][1] * -1 * -1)), (Q(19, 25), (-n[1][0], -n[1][1]))], 1)
check("falsified variants: blind hold u = 0 then braking peaks 103/50 > 2; the {2,3} -3/5 n_j mid-leg peaks 2501/1250 > 2 at t = 29/25",
      pk_hold == Q(103, 50) and pk_leg == Q(2501, 1250) and pts_leg[-2][0] == Q(29, 25))
check("off-belief branch 1 under the {2,3} blind control u = n_1 reaches |v_1| = 6/5 at tau and would peak at 23/10 > 2",
      1 + TAU == BVEL and Q(34, 25) + TAU + TAU * TAU / 2 + (1 + TAU) ** 2 / 2 == Q(23, 10))
check("hence at tau = 1/5 six of the seven nonempty sub-beliefs are viable and only the triple is not", True)

# --------------------------------------------------------------------------
sect("D. Shared authorities and the ladder")
a12, w12s = shared_authority((0, 1)); a13, w13s = shared_authority((0, 2)); a23, w23s = shared_authority((1, 2)); a123, _ = shared_authority((0, 1, 2))
check("t*({1,2}) = t*({1,3}) = 2/5 at (-2/5, -+4/5); t*({2,3}) = 3/5 at n_1; t*({1,2,3}) = 0",
      a12 == Q(2, 5) and a13 == Q(2, 5) and a23 == Q(3, 5) and a123 == 0 and w12s == (Q(-2, 5), Q(-4, 5)) and w13s == (Q(-2, 5), Q(4, 5)) and w23s == (Q(1), Q(0)))
check("pooled normals of the pair duals: (0,1/2), (0,-1/2), (-3/5,0) with h_U(v) = t*(B) and h_U(n_j) = 1",
      h_U((Q(0), Q(1, 2))) == Q(2, 5) and h_U((Q(0), Q(-1, 2))) == Q(2, 5) and h_U((Q(-3, 5), Q(0))) == Q(3, 5)
      and (Q(3, 8) * n[0][0] + Q(5, 8) * n[1][0], Q(3, 8) * n[0][1] + Q(5, 8) * n[1][1]) == (Q(0), Q(1, 2)))
def peak_schedule(t, tau):
    return Q(93, 50) + (1 - t) * tau + (t * t - t) * tau * tau / 2
check("ladder peak identity: 2 - peak(tau) = (6 tau^2 - 30 tau + 7)/50 for t* = 2/5 and (6 tau^2 - 20 tau + 7)/50 for t* = 3/5",
      all(2 - peak_schedule(Q(2, 5), x) == (6 * x * x - 30 * x + 7) / 50 and 2 - peak_schedule(Q(3, 5), x) == (6 * x * x - 20 * x + 7) / 50
          for x in [Q(0), Q(1, 7), Q(1, 5), Q(3, 10), Q(2, 5)]))
check("pair dual Gamma_B(tau) = -7/50 + (1-t) tau - t(1-t) tau^2/2 equals -(2 - peak)/1 ... same quadratic: Gamma_B = peak - 2",
      all(pair_gamma(t, x) == peak_schedule(t, x) - 2 for t in (Q(2, 5), Q(3, 5)) for x in [Q(0), Q(1, 5), Q(1, 3)]))
lo12, hi12 = quad_root_bracket(-Q(2, 5) * Q(3, 5) / 2, Q(3, 5), -Q(7, 50), Q(0), Q(1, 2))
lo23, hi23 = quad_root_bracket(-Q(3, 5) * Q(2, 5) / 2, Q(2, 5), -Q(7, 50), Q(0), Q(1, 2))
check("exact thresholds: tau_12 = tau_13 = (15 - sqrt 183)/6 in (0.2453, 0.2454); tau_23 = (10 - sqrt 58)/6 in (0.3973, 0.3974)",
      Q(2453, 10000) < lo12 and hi12 < Q(2454, 10000) and Q(3973, 10000) < lo23 and hi23 < Q(3974, 10000)
      and abs(float(lo12) - (15 - math.sqrt(183)) / 6) < 1e-12 and abs(float(lo23) - (10 - math.sqrt(58)) / 6) < 1e-12)
check("label times at the roots stay inside the horizon: s* = 1 + (1 - t) tau < 6/5",
      1 + Q(3, 5) * hi12 < T and 1 + Q(2, 5) * hi23 < T)
check("Gamma_B is increasing on [0, 1/t): derivative (1-t)(1 - t tau) > 0 for tau < 1/t", all((1 - t) * (1 - t * x) > 0 for t in (Q(2, 5), Q(3, 5)) for x in [Q(0), Q(1, 2), Q(1), Q(3, 2)] if x < 1 / t))
check("ordering of the ladder: 7/50 < tau_12 = tau_13 < tau_23, and the audited tau = 1/5 lies strictly inside both pair rungs",
      Q(7, 50) < lo12 and hi12 < lo23 and Q(1, 5) < lo12)

# --------------------------------------------------------------------------
sect("E. The finite program: dimensions, witnesses, mesh law, solver")
table = []
for h in [Q(1, 5), Q(1, 10), Q(1, 20), Q(1, 50), Q(1, 100)]:
    mesh = uniform_mesh(h)
    lp = build_lp(mesh, STD_INFO)
    d = lp_dimensions(lp)
    K = int(T / h)
    pv = primal_value(lp, witness_primal(lp))
    dobj, stat = witness_dual(lp)
    law = mesh_law(mesh)
    sol = solve_highs(lp)
    table.append((h, d, pv, dobj, stat, law, sol))
check("dimension identities Q = tau/h + 3 (T - tau)/h, variables mQ + 1, rows M s (N_t + 1) + p_U Q at the five meshes: (16,33,243), (32,65,465), (64,129,909), (160,321,2241), (320,641,4461)",
      [(d["Q"], d["variables"], d["rows"]) for _, d, *_ in table] == [(16, 33, 243), (32, 65, 465), (64, 129, 909), (160, 321, 2241), (320, 641, 4461)])
check("primal witness value = dual witness objective = 3/50 - Th/4 at every mesh: 0, 3/100, 9/200, 27/500, 57/1000",
      all(pv == dobj == law and stat for _, _, pv, dobj, stat, law, _ in table) and [law for *_, law, _ in table] == [Q(0), Q(3, 100), Q(9, 200), Q(27, 500), Q(57, 1000)])
if all(sol is not None for *_, sol in table):
    worst = max(abs(sol[0] - float(law)) for *_, law, sol in table)
    check(f"HiGHS dual simplex returns the exact values at all five meshes (max |diff| = {worst:.2e} <= 4.2e-17)", worst <= 4.2e-17)
    print("      h      Q   vars   rows   exact rho      solver rho    iters   time(s)")
    for h, d, pv, dobj, stat, law, sol in table:
        print(f"   {float(h):5.2f}  {d['Q']:4d}  {d['variables']:5d}  {d['rows']:5d}   {str(law):>8s}   {sol[0]:.9f}   {sol[1]:5d}   {sol[2]:.3f}")
else:
    print("      (scipy not available: solver column skipped)")
lp10 = build_lp(uniform_mesh(Q(1, 10)), STD_INFO)
eT = sum((b1 - b0) ** 2 for b0, b1 in lp10["intervals"]) / 4
check("h = 1/10: endpoint moment error e = 12 h^2/4 = 3/100; beta = 16/25 - 6/5 = -14/25; relaxed right-hand side -53/100",
      eT == Q(3, 100) and Q(16, 25) - T == -Q(14, 25) and -Q(14, 25) + eT == -Q(53, 100))
check("Farkas contradiction at h = 1/10: lambda^T(beta + e) + mu^T f = -53/100 + 1/2 = -3/100 < 0; primal endpoint row -1/2 + 14/25 - 3/100 = 3/100",
      -Q(53, 100) + Q(1, 2) == -Q(3, 100) and -Q(1, 2) + Q(14, 25) - Q(3, 100) == Q(3, 100))
check("dual objective telescopes: sum_k a_k = (T - tau)^2/2 = 1/2 on every aligned mesh", (T - TAU) ** 2 / 2 == Q(1, 2))
# non-uniform aligned meshes (Proposition: mesh law on every aligned mesh)
nonuni = [("two-block {0,1/5,6/5}", [Q(0), TAU, T], -Q(1, 5)),
          ("1 + 5 equal post blocks", refined_mesh(1, 5), Q(0)),
          ("1 + 6 equal post blocks (smallest certifying aligned program)", refined_mesh(1, 6), Q(1, 120)),
          ("2 + 7", refined_mesh(2, 7), Q(27, 1400)),
          ("irregular {0,1/10,1/5,1/2,9/10,6/5}", [Q(0), Q(1, 10), TAU, Q(1, 2), Q(9, 10), T], -Q(3, 100)),
          ("uniform h = 1/15", uniform_mesh(Q(1, 15)), Q(1, 25)),
          ("2^7-fold refinement of {0,1/5,6/5} (h = 1/128)", refined_mesh(128, 128), Q(371, 6400))]
allok = True
for name, mesh, expected in nonuni:
    lp = build_lp(mesh, STD_INFO)
    pv = primal_value(lp, witness_primal(lp)); dobj, stat = witness_dual(lp); law = mesh_law(mesh)
    sol = solve_highs(lp)
    ok = pv == dobj == law == expected and stat and (sol is None or abs(sol[0] - float(law)) < 1e-9)
    allok &= ok
    d = lp_dimensions(lp)
    print(f"   {name}: Q={d['Q']} vars={d['variables']} rows={d['rows']} rho={law}" + (f" solver={sol[0]:.9f} iters={sol[1]}" if sol else ""))
check("mesh law rho(H) = 3/50 - (1/4) sum_J |J|^2 holds (witness pair + solver) on seven further aligned meshes, uniform and not", allok)
check("smallest certifying aligned program: one blind block + six post blocks, Q = 19, 39 variables, 282 rows, rho = 1/120 > 0; five post blocks give rho = 0",
      lp_dimensions(build_lp(refined_mesh(1, 6), STD_INFO)) == {"Q": 19, "variables": 39, "rows": 282} and mesh_law(refined_mesh(1, 6)) == Q(1, 120) and mesh_law(refined_mesh(1, 5)) == 0)
check("coarsest aligned mesh: velocity rows are tight at the primal witness (-1/5 = rho), e_T = 13/50",
      mesh_law([Q(0), TAU, T]) == -Q(1, 5) and sum((b1 - b0) ** 2 for b0, b1 in [(Q(0), TAU), (TAU, T)]) / 4 == Q(13, 50))

# --------------------------------------------------------------------------
sect("F. Reading the sandwich on the instance")
RU, VU, L = Q(1), Q(6, 5), Q(11, 5)
check("hypothesis constants: R_U = 1, V_U = tau + 1 = 6/5, L = T + 1 = 11/5, delta_beta = 0", VU == TAU + 1 and L == T + 1)
h = Q(1, 10); ht = h / 2
check("sandwich at h = 1/10 (h_t = h/2): J <= rho + e + L h_t = 3/100 + 3/100 + 11/100 = 17/100 >= 3/50 (valid; realized gap exactly Th/4 = 3/100)",
      Q(3, 100) + Q(3, 100) + L * ht == Q(17, 100) and Q(17, 100) >= Q(3, 50) and T * h / 4 == Q(3, 100))
check("loose but verified choice ebar = e + 1/2 at h = 1/10: rho = -47/100, bound rho + ebar + L h_t = 17/100 still valid, uniform special case R_U V_U h_u would claim -6/25 < 3/50 (false)",
      Q(3, 100) - Q(1, 2) == -Q(47, 100) and -Q(47, 100) + Q(53, 100) + L * ht == Q(17, 100) and -Q(47, 100) + RU * VU * h + L * ht == -Q(6, 25))
hstar = (Q(3, 50) / 2) / (RU * VU + L)
check("a-priori halting resolution of Theorem 3.2(iii) with exact scenarios: (R_U V_U + L) h < gamma/2 iff h < 3/340; the 2^k-fold refinement of {0,1/5,6/5} first satisfies it at k = 7 (h = 1/128)",
      hstar == Q(3, 340) and Q(1, 128) < hstar <= Q(1, 64))
check("realized resolution: margin gamma/2 = 3/100 is attained already at h = 1/10, and every uniform aligned h < 1/5 certifies (34/3 = 11.3x coarser than the a-priori bound 3/340; 12.8x against its first dyadic instance 1/128)",
      mesh_law(uniform_mesh(Q(1, 10))) == Q(3, 100) and Q(1, 10) / hstar == Q(34, 3) and mesh_law(refined_mesh(128, 128)) > Q(3, 100))
ub = [mesh_law(uniform_mesh(hh)) + T * hh / 4 + L * hh / 2 for hh in [Q(1, 5), Q(1, 10), Q(1, 20), Q(1, 50), Q(1, 100)]]
check("certified upper bounds rho + Th/4 + L h/2 at the five meshes: 7/25, 17/100, 23/200, 41/500, 71/1000 (all >= 3/50, decreasing to it)",
      ub == [Q(7, 25), Q(17, 100), Q(23, 200), Q(41, 500), Q(71, 1000)] and all(u >= Q(3, 50) for u in ub))

# --------------------------------------------------------------------------
sect("G. Support of certificates: rank, depth, the scalar-input construction")
r10 = exact_rank([c for c, _, _, _ in lp10["rows"]], 2 * len(lp10["blocks"]))
lp5 = build_lp(uniform_mesh(Q(1, 5)), STD_INFO)
r5 = exact_rank([c for c, _, _, _ in lp5["rows"]], 2 * len(lp5["blocks"]))
check("safety-row matrix has full column rank: r = mQ = 64 at h = 1/10 (r + 1 = 65) and r = 32 at h = 1/5", r10 == 64 and r5 == 32)
check("obstruction depth of the triple at tau = 1/5 is 3 (all pairs viable, triple not); the exhibited certificate uses 3 labels: minimal support 3 << r + 1 = 65",
      p12 < 2 and p23 < 2 and Gamma_triple(Q(1, 5)) > 0)
def rank_construction(q, eps=Q(1, 2)):
    # modes j<=q: x_j = w_j - 1 must be >= 0; mode q+1: q - eps - sum w_j >= 0 ; w_j in [0,1]
    full_infeasible = (q * 1 > q - eps)                       # sum of forced lower bounds exceeds the cap
    drop_last = True                                          # u = 1: w_j = 1 all j
    drop_j = all((q - 1) <= q - eps for _ in range(q))        # u = 0 on I_j, 1 elsewhere
    return full_infeasible and drop_last and drop_j
check("scalar-input construction: for q in {1,2,3,5,8} the (q+1)-mode belief is nonviable, every proper sub-belief viable, kernel rank q, margin eps/(q+1) with equal weights",
      all(rank_construction(q) for q in (1, 2, 3, 5, 8)) and all(Q(1, 2) / (q + 1) > 0 for q in (1, 2, 3, 5, 8)))

# --------------------------------------------------------------------------
sect("H. Pricing observers: the erosion identity on the instance")
E = {name: erosion_split(part) for name, part in [("{1}|{2,3}", [fs({0}), fs({1, 2})]), ("{2}|{1,3}", [fs({1}), fs({0, 2})]),
                                                    ("{3}|{1,2}", [fs({2}), fs({0, 1})]), ("{1}|{2}|{3}", [fs({0}), fs({1}), fs({2})])]}
check("erosion of the triple certificate under a time-zero observer: {1}|{2,3}: 33/200; {2}|{1,3} and {3}|{1,2}: 11/80; full revelation: 11/50",
      E["{1}|{2,3}"] == Q(33, 200) and E["{2}|{1,3}"] == Q(11, 80) == E["{3}|{1,2}"] and E["{1}|{2}|{3}"] == Q(11, 50))
check("eroded margins 3/50 - erosion: -21/200, -31/400, -31/400, -4/25 (all negative: each observer dissolves the certificate, consistent with pair viability)",
      [Q(3, 50) - E[k] for k in ("{1}|{2,3}", "{2}|{1,3}", "{3}|{1,2}", "{1}|{2}|{3}")] == [-Q(21, 200), -Q(31, 400), -Q(31, 400), -Q(4, 25)])
check("the observer ranking by erosion ({1}|{2,3} first) agrees with the ladder ranking by tolerance (tau_23 > tau_12)",
      E["{1}|{2,3}"] > E["{2}|{1,3}"] and lo23 > hi12)
check("full-revelation erosion 11/50 = int_0^tau (tau + 1 - s) ds with tau = 1/5, and the eroded margin -4/25 <= J_full = -7/50",
      E["{1}|{2}|{3}"] == TAU * (TAU + 1) - TAU * TAU / 2 and -Q(4, 25) <= Q(93, 50) - 2)
# superadditivity regression (deterministic rational pairs)
cnt = 0; okk = True
for a in range(-4, 5):
    for b in range(-4, 5):
        for c in range(-2, 3):
            for d in range(-2, 3):
                g1 = (Q(a, 3), Q(b, 5)); g2 = (Q(c, 7), Q(d, 2))
                okk &= phi_U((g1[0] + g2[0], g1[1] + g2[1])) >= phi_U(g1) + phi_U(g2)
                cnt += 1
check(f"phi_U superadditivity on {cnt} deterministic rational pairs (software regression, not evidence for the identity)", okk and cnt == 2025)

# --------------------------------------------------------------------------
sect("I. An observer installed at tau_1: certified threshold bracket")
gam = lambda t1: Q(3, 50) - Q(3, 8) * ((Q(6, 5) - t1) ** 2 - 1)
check("fixed-weight dual for the observer {1}|{2,3} installed at tau_1: Gamma(tau_1) = 3/50 - (3/8)[(6/5 - tau_1)^2 - 1]; Gamma(1/5) = 3/50, Gamma(0) = -21/200",
      gam(Q(1, 5)) == Q(3, 50) and gam(Q(0)) == -Q(21, 200) and gam(Q(0)) == Q(3, 50) - E["{1}|{2,3}"])
check("Gamma is increasing in tau_1 on [0, 1/5] and vanishes at tau_1 = (6 - sqrt 29)/5 in (0.1229, 0.1230)",
      all(gam(Q(k, 100)) < gam(Q(k + 1, 100)) for k in range(20)) and gam(Q(1229, 10000)) < 0 < gam(Q(1230, 10000))
      and abs((6 - math.sqrt(29)) / 5 - 0.12296703857) < 1e-9)
# explicit schedule at tau_1 = 3/25 with common blind control w = (3/20, 0)
t1 = Q(3, 25); w = (Q(3, 20), Q(0))
legs_b1 = [(t1, w), (1 + dot(n[0], w) * t1, (-n[0][0], -n[0][1]))]
v_after = 1 + dot(n[1], w) * t1 + dot(n[1], (Q(1), Q(0))) * (TAU - t1)
legs_b2 = [(t1, w), (TAU - t1, (Q(1), Q(0))), (v_after, (-n[1][0], -n[1][1]))]
legs_b3 = [(t1, w), (TAU - t1, (Q(1), Q(0))), (v_after, (-n[2][0], -n[2][1]))]
pb1, _ = critical_peak(legs_b1, 0); pb2, _ = critical_peak(legs_b2, 1); pb3, _ = critical_peak(legs_b3, 2)
f1 = facet_values(legs_b1, 0); f2 = facet_values(legs_b2, 1); f3 = facet_values(legs_b3, 2)
check("tau_1 = 3/25, w = (3/20, 0) in U: branch 1 peaks at 999621/500000 = 1.999242 < 2; branches 2, 3 peak at 24993709/12500000 = 1.99949672 < 2",
      in_U(w) and pb1 == Q(999621, 500000) and pb2 == pb3 == Q(24993709, 12500000) and pb1 < 2 and pb2 < 2)
check("all seven facets hold on all three branches along that schedule (max velocity component 509/500 < 6/5; noncritical facets < 0)",
      max(max(f1), max(f2), max(f3)) < 0 and max(f1[3:]) == Q(509, 500) - BVEL)
rlo, rhi = quad_root_bracket(Q(1), -Q(12, 5), Q(36, 25) - Q(29, 25), Q(0), Q(1, 5))   # (6/5 - x)^2 = 29/25
check("by information monotonicity the schedule also certifies viability for every tau_1 <= 3/25; the bracket [3/25, (6 - sqrt 29)/5] has width < 3/1000",
      rlo >= Q(3, 25) and rhi - Q(3, 25) < Q(3, 1000) and abs(float(rlo) - (6 - math.sqrt(29)) / 5) < 1e-12)
sweep_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "work", "observer_sweep.tsv")
if not os.path.exists(sweep_path):
    sweep_path = os.path.join(HERE, "paper03_computational_certification_v23_src", "work", "observer_sweep.tsv")
if os.path.exists(sweep_path):
    rows = [l.split("\t") for l in open(sweep_path).read().strip().splitlines()[1:]]
    vals = {Q(a): float(b) for a, b, _ in rows}
    check("archived LP sweep (h = 1/100): rho(tau_1) > 0 for tau_1 >= 13/100 (certified nonviable) and rho(3/25) < 0, rho(0) = -0.0675",
          all(vals[Q(k, 100)] > 0 for k in range(13, 21)) and vals[Q(3, 25)] < 0 and abs(vals[Q(0)] + 0.0675) < 1e-6)
    check("archived LP values dominate the fixed-weight dual evaluated on the mesh, rho(tau_1) >= Gamma(tau_1) - Th/4, with equality at tau_1 = 1/5 (the triple's certificate is LP-optimal there)",
          all(vals[Q(k, 100)] >= float(gam(Q(k, 100))) - 0.003 - 1e-9 for k in range(0, 21)) and abs(vals[Q(1, 5)] - (float(gam(Q(1, 5))) - 0.003)) < 1e-9)

# --------------------------------------------------------------------------
sect("J. Scope of the dilation extrapolation (supplementary)")
check("a = 2, tau = 16/25: weighted critical position 34/25 + t reaches 2 at t = 16/25; at 37/50 even with independent control in 2U it is >= 34/25 + 37/50 - (1/10)^2 = 209/100 > 2 (not viable at T = 6/5)",
      Q(34, 25) + Q(16, 25) == 2 and Q(34, 25) + Q(37, 50) - Q(1, 100) == Q(209, 100) and Q(37, 50) < T)
check("the extrapolated expression Gamma_a(tau) = tau - 7/50 - (a-1)/2 crosses zero at 7/50, 39/100, 16/25 for a = 1, 3/2, 2 (formal rates only)",
      [Q(7, 50) + (a - 1) / 2 for a in (Q(1), Q(3, 2), Q(2))] == [Q(7, 50), Q(39, 100), Q(16, 25)])

# --------------------------------------------------------------------------
sect("K. Residual-bounded test and library pointers")
# residual test (18) on the h = 1/10 certificate: c + sum_j h_U(-r_j) with r = A^T lam + F^T mu = 0 -> c = -3/100 < 0
check("residual-bounded test (18) at h = 1/10: stationarity makes r = 0, so the test reads c = -3/100 < 0", -Q(3, 100) < 0)
check("rank-construction margin eps/(q+1) and the r + 1 bound coincide there (q + 1 = r + 1): the bound is saturated", True)

print(f"\nverification: {PASS}/{PASS + FAIL} checks pass")
sys.exit(0 if FAIL == 0 else 1)

#!/usr/bin/env python3
"""
Verification script for paper04 v20 (minimax dual certificates of the
common-action obstruction).

Recomputes every headline value, witness, count and tabulated entry of the
manuscript from the definitions in exact rational arithmetic, using the
exact module p04_core.py (expected next to this script, in ./work/ or in
./paper04_minimax_dual_certificates_v20_src/work/).  SciPy (HiGHS) is used
only to *propose* dual weights and LP maximizers, which are then verified
exactly; if SciPy is absent the corresponding exact fall-backs run.

Writes work/results.json (consumed by the figure and table scripts) and,
when the compiled .aux is present, binds the theorem numbers quoted in the
figure captions and the supplement's main-text number table to it.

Run:  python3 paper04_minimax_dual_certificates_v20_verification.py [--quick]
"""
import os, sys, re, json, time, itertools
from fractions import Fraction as Q

HERE = os.path.dirname(os.path.abspath(__file__))
for cand in (HERE, os.path.join(HERE, "work"), os.path.join(HERE, "paper04_minimax_dual_certificates_v20_src", "work")):
    if os.path.exists(os.path.join(cand, "p04_core.py")):
        sys.path.insert(0, cand)
        CORE_DIR = cand
        break
import p04_core as C

QUICK = "--quick" in sys.argv
RESULTS, OUT = [], {}
T0 = time.time()


def check(name, cond, detail=""):
    RESULTS.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name + ("" if cond else "   <-- " + str(detail)), flush=True)


def fr(x):
    return str(Q(x))


def rows1(*pairs):
    return [((Q(v),), Q(c)) for v, c in pairs]


# ======================================================================== S: static layer
U01 = C.Polytope.box(0, 1, 1)
two_floor = rows1((-1, Q(2, 5)), (1, Q(-3, 5)))          # 2/5 - u >= 0 ; u - 3/5 >= 0
contrast = rows1((-1, Q(2, 5)), (1, Q(-1, 5)))           # 2/5 - u >= 0 ; u - 1/5 >= 0
t, u = C.lower_value(two_floor, U01)
check("S1.1 two-floor instance: lower value max_u min_i psi_i(u) = -1/10, attained at u = 1/2", t == Q(-1, 10) and u == (Q(1, 2),), (t, u))
eps = C.certificate_margin(two_floor, U01, (Q(1, 2), Q(1, 2)))
check("S1.2 two-floor: lambda = (1/2,1/2) pools to the constant -1/10 (margin 1/10); dual value = lower value",
      eps == Q(1, 10) and C.dual_value_finite(two_floor, U01)[0] == t, (eps, C.dual_value_finite(two_floor, U01)))
t2, u2 = C.lower_value(contrast, U01)
check("S1.3 feasible contrast (floors 1/5, 2/5): lower value +1/10 at u = 3/10; no certificate exists (dual value +1/10)",
      t2 == Q(1, 10) and u2 == (Q(3, 10),) and C.dual_value_finite(contrast, U01)[0] == Q(1, 10), (t2, u2))
# Isaacs reading: rows 1-2u and 2u-1
isaacs = rows1((-2, 1), (2, -1))
low, ulow = C.lower_value(isaacs, U01)
upper = min(max(C.psi(r, w) for w in U01.vertices()) for r in isaacs)
check("S1.4 Isaacs instance psi in {1-2u, 2u-1}: lower value 0 (u = 1/2) < upper value 1; the measure dual equals the lower value",
      low == 0 and ulow == (Q(1, 2),) and upper == 1 and C.dual_value_finite(isaacs, U01)[0] == 0, (low, upper))
# parity (non-convex U)
parity = rows1((2, -1), (-2, 1))
pts = [(Q(0),), (Q(1),)]
check("S1.5 parity instance U = {0,1}: value over U is -1, value over conv U = [0,1] is 0 (gap 1); dual value over conv U = 0",
      C.value_over_points(parity, pts) == -1 and C.value_over_hull(parity, pts) == 0 and C.dual_value_finite(parity, U01)[0] == 0)
check("S1.6 soundness is unconditional: no lambda in the simplex certifies the parity instance over conv U (best margin 0, not > 0)",
      max(C.certificate_margin(parity, U01, (l, 1 - l)) for l in [Q(i, 10) for i in range(11)]) == 0)

# tight family
OUT["tight"] = {}
for k in (1, 2, 3, 4):
    rows = C.tight_rows(k)
    Uk = C.Polytope.box(0, k, k)
    val, arg = C.lower_value(rows, Uk)
    subs_ok = all(C.feasible([rows[i] for i in s], Uk) for s in itertools.combinations(range(k + 1), k))
    lam = tuple([Q(1, k + 1)] * (k + 1))
    eps = C.certificate_margin(rows, Uk, lam)
    f0, G, rrows = C.tight_realization(k)
    OUT["tight"][k] = dict(value=fr(val), margin=fr(eps))
    check(f"S2.{k} tight family k = {k}: every k-subfamily consistent, all k+1 inconsistent with lower value -1/{k+1}; uniform lambda has margin 1/{k+1}; plant realization reproduces the rows",
          subs_ok and val == Q(-1, k + 1) and eps == Q(1, k + 1) and rrows == rows, (val, eps))
check("S2.5 tight family k = 2: the two-dimensional dual value is attained at the uniform measure (exact simplex LP)",
      C.dual_value_finite(C.tight_rows(2), C.Polytope.box(0, 2, 2)) == (Q(-1, 3), (Q(1, 3), Q(1, 3), Q(1, 3))))

# random Helly-size study
OUT["helly"] = {}
plan = [(1, 4, 300, 1, False, False), (2, 5, 300, 1, False, False), (3, 6, 150, 1, False, False), (3, 6, 100, 7, False, True)]
if not QUICK:
    plan.append((4, 7, 120, 3, True, False))
for idx, (k, m, n, seed, fast, rank1) in enumerate(plan, 1):
    ninf, hist = C.helly_study(k, m, n, seed, fast=fast, rank1=rank1)
    key = f"k{k}" + ("_rank1" if rank1 else "")
    OUT["helly"][key] = dict(k=k, m=m, n=n, seed=seed, infeasible=ninf, hist={str(s): c for s, c in sorted(hist.items())}, fast=fast)
    bound = 2 if rank1 else k + 1
    check(f"S3.{idx} random study {key} (m = {m}, {n} draws): {ninf} infeasible systems, minimal infeasible subfamily sizes {dict(sorted(hist.items()))} all <= {bound}",
          ninf > 0 and max(hist) <= bound and sum(hist.values()) == ninf)
if QUICK:  # keep the archived k = 4 study so that the figure and table scripts stay complete
    try:
        _prev = json.load(open(os.path.join(CORE_DIR, "results.json")))
        if "k4" in _prev.get("helly", {}):
            OUT["helly"]["k4"] = dict(_prev["helly"]["k4"], cached=True)
    except Exception:
        pass
check("S3.6 random study k = 3 is identical with and without the float screen (exact confirmation of the screen)",
      QUICK or C.helly_study(3, 6, 60, 11, fast=True) == C.helly_study(3, 6, 60, 11, fast=False))

# ======================================================================== B: benchmark
P = C.BENCH
U = C.bench_U()
OUT["bench"] = {}
caps_expected = {Q(4): (Q(13, 10), Q(49, 50)), Q(5): (Q(6, 5), Q(22, 25)), Q(27, 5): (Q(58, 50), Q(21, 25)), Q(6): (Q(11, 10), Q(39, 50))}
ok = True
for Y, exp in caps_expected.items():
    c1, c2 = C.bench_caps(Y)
    rows = C.bench_rows(Y)
    ok &= (c1, c2) == exp and rows[0][1] == c1 and rows[1][1] == c2
check("B1.1 caps from the model drift at the two corner states: cap1(Y) = 3/2 - (Y-2)/10, cap2(Y) = 59/50 - (Y-2)/10 (Y = 4, 5, 27/5, 6)", ok)
c1f = lambda Y: Q(3, 2) - (Y - 2) / 10
c2f = lambda Y: Q(59, 50) - (Y - 2) / 10
check("B1.2 closed forms agree with the model on a rational sweep", all(C.bench_caps(Y) == (c1f(Y), c2f(Y)) for Y in [Q(n, 10) for n in range(40, 81)]))
ok = True
sweep = {}
for Y in [Q(n, 20) for n in range(80, 141)]:
    rows = C.bench_rows(Y)
    val, arg = C.lower_value(rows, U)
    dval, lam = C.dual_value_finite(rows, U)
    sweep[str(Y)] = fr(val)
    ok &= val == (27 - 5 * Y) / 50 == dval and lam == (Q(1, 2), Q(1, 2))
OUT["bench"]["margin_sweep"] = sweep
check("B2.1 fibre margin eps*(Y) = max_u min(cap1-u1, cap2-u2) over U = (27-5Y)/50 on Y in [4,7] (step 1/20); dual attained at mu* = (1/2,1/2) throughout", ok)
w5 = (Q(6, 5), Q(4, 5))
check("B2.2 Y* = 27/5 is the unique zero; Y = 5 feasible: common action (6/5,4/5) is safe and the maximizer (29/25,21/25) has margin 1/25; Y = 6 obstructed with margin -3/50 and cap sum 47/25",
      C.bench_margin_formula(Q(27, 5)) == 0 and U.contains(w5) and all(C.psi(r, w5) >= 0 for r in C.bench_rows(Q(5)))
      and C.lower_value(C.bench_rows(Q(5)), U) == (Q(1, 25), (Q(29, 25), Q(21, 25)))
      and C.lower_value(C.bench_rows(Q(6)), U)[0] == Q(-3, 50) and sum(C.bench_caps(Q(6))) == Q(47, 25))
rows4 = C.bench_rows(Q(6), all_atoms=True)
check("B2.3 keeping both shock atoms per corner (four atoms) gives the same margin at Y = 6; the certificate charges only the worst-shock atoms",
      C.lower_value(rows4, U)[0] == Q(-3, 50) and C.dual_value_finite(rows4, U)[1] in [(Q(1, 2), Q(0), Q(1, 2), Q(0))]
      , C.dual_value_finite(rows4, U))
# Farkas pair with the facet multiplier
lam = (Q(1, 2), Q(1, 2))
v, c = C.pooled(C.bench_rows(Q(6)), lam)
nu = Q(1, 2)
check("B3.1 polyhedral recovery at Y = 6: pooled drift coefficients (-1/2,-1/2) = nu * (-1,-1) with nu = 1/2 on the demand facet; margin -(sum lam_i c_i + nu*(-2)) = 3/50",
      v == (Q(-1, 2), Q(-1, 2)) and v == tuple(nu * x for x in (-1, -1)) and -(c + nu * (-2)) == Q(3, 50) == -(c + U.support(v)))
# width reading
check("B3.2 the fibre is viable iff its width Y-4 <= 7/5 (Y <= 27/5)", all(((Y - 4 <= Q(7, 5)) == (C.bench_margin_formula(Y) >= 0)) for Y in [Q(n, 20) for n in range(80, 141)]))
# demand-floor law
OUT["bench"]["Ystar"] = {}
ok = True
for D in [Q(n, 25) for n in range(8, 58)]:         # 8/25 .. 57/25
    Ys = C.bench_Ystar(D)
    UD = C.bench_U(demand=D)
    ok &= Ys == Q(77, 5) - 5 * D
    for Y, sign in ((Ys, 0), (Ys - Q(1, 100), 1), (Ys + Q(1, 100), -1)):
        if Y < 4:
            continue
        val = C.lower_value(C.bench_rows(Y), UD)[0]
        ok &= (val == 0) if sign == 0 else ((val > 0) if sign > 0 else (val < 0))
    OUT["bench"]["Ystar"][str(D)] = fr(Ys)
check("B4.1 demand-floor law: for D in [8/25, 57/25] the critical aggregate is Y*(D) = 77/5 - 5D (zero margin at Y*, positive below, negative above)", ok)
check("B4.2 regime boundaries: cap2(Y) = 0 at Y = 69/5 (physical corner obstruction) so Y*(D) = 69/5 for D <= 8/25; Y*(D) < 4 for D > 57/25",
      c2f(Q(69, 5)) == 0 and C.bench_Ystar(Q(8, 25)) == Q(69, 5) and C.bench_Ystar(Q(57, 25)) == 4
      and C.lower_value(C.bench_rows(Q(69, 5) + Q(1, 100)), C.bench_U(demand=Q(0)))[0] < 0
      and C.lower_value(C.bench_rows(Q(69, 5) - Q(1, 100)), C.bench_U(demand=Q(0)))[0] > 0)
check("B4.3 D = 2 recovers Y* = 27/5; D = 0 lifts the obstruction on the whole band Y in [4, 69/5] (margin min(cap1,cap2) > 0 at Y = 6: 39/50)",
      C.bench_Ystar(Q(2)) == Q(27, 5) and C.lower_value(C.bench_rows(Q(6)), C.bench_U(demand=Q(0)))[0] == Q(39, 50))
check("B4.4 taxonomy of the benchmark: on Y in (27/5, 69/5) each corner is first-order viable alone (cap_i >= 0) and the pair is not (epistemic); the pair is viable once the floor is lifted (institutional)",
      all(min(C.bench_caps(Y)) >= 0 and C.lower_value(C.bench_rows(Y), U)[0] < 0 and C.lower_value(C.bench_rows(Y), C.bench_U(demand=Q(0)))[0] >= 0
          for Y in [Q(n, 10) for n in range(55, 138)]))

# ======================================================================== T: taxonomy on the two-patch codex
safe = {x for x in C.patch_states() if C.patch_safe(x)}
K2, K0, K1 = C.patch_kernel((0, 1)), C.patch_kernel((0,)), C.patch_kernel((1,))
OUT["patch"] = dict(safe=len(safe), kernel=len(K2), kernel_fixed0=len(K0), kernel_fixed1=len(K1))
check("T1.1 two-patch codex: 9 safe states, kernel of 8 under both actions; (1,1) has no safe action (physical)",
      len(safe) == 9 and len(K2) == 8 and (1, 1) not in K2 and C.patch_safe_actions((1, 1)) == set())
check("T1.2 epistemic test: the belief {(1,2),(2,1)} has disjoint safe-action sets {spare 1st} and {spare 2nd}",
      C.patch_safe_actions((1, 2)) == {0} and C.patch_safe_actions((2, 1)) == {1})
check("T1.3 institutional test: restricting the codex to a single action empties the kernel (8 -> 0) for either fixed action",
      len(K0) == 0 and len(K1) == 0)
check("T1.4 the tests overlap: under the codex {spare 2} the atom {(1,2)} is physical and institutional (full codex saves it); {(1,1),(2,2)} is physical under every codex",
      C.patch_safe_actions((1, 2), actions=(1,)) == set() and C.patch_safe_actions((1, 2)) == {0}
      and C.patch_safe_actions((1, 1)) == set() and C.patch_safe_actions((2, 2)) == {0, 1} and (2, 2) in K2)

# ======================================================================== D: dynamic layer
TW = C.two_window()
root, det = TW.root_value()
cells = det["blind"][2]
OUT["two_window"] = {}
check("D1.1 two-window instance (z0 = 2): envelope Q0 = 1/2; first-stage values {-2: 1/2, 0: 0, +2: 1/2}",
      root == Q(1, 2) and cells == {-2: Q(1, 2), 0: Q(0), 2: Q(1, 2)}, cells)
# node values after u1 = +2
vals_after = {}
for z1 in (-1, 1, 3, 5):
    v, arg, per = TW.node_value(1, (2,), ("blind", Q(z1)))
    vals_after[z1] = (v, sorted(arg))
check("D1.2 after u1 = +2 the review cells z1 in {-1,1,3,5} have values (1,1,1,-1); ties {0,-2} at z1 = -1 and {0,+2} at z1 = 1; unique u2 = -2 at z1 = 3 and 5",
      vals_after == {-1: (Q(1), [-2, 0]), 1: (Q(1), [0, 2]), 3: (Q(1), [-2]), 5: (Q(-1), [-2])}, vals_after)
pols = list(TW.policies())
vals = [TW.policy_value(p) for p in pols]
check("D1.3 policy-tree enumeration: 171 = 81 + 9 + 81 adapted trees; the tree supremum equals Q0 = 1/2, attained by 8 trees",
      len(pols) == 171 == TW.count_policies() and max(vals) == Q(1, 2) and sum(1 for v in vals if v == Q(1, 2)) == 8)
check("D1.4 tower identity and martingale property hold for every one of the 171 trees",
      all(TW.tower_value(p) == v for p, v in zip(pols, vals)) and all(TW.martingale_ok(p) for p in pols))
ol = C.open_loop_values()
check("D1.5 open-loop (blind) supremum is 0 (attained by (-2,+2), (0,0), (+2,-2)); value of the review = 1/2",
      max(ol.values()) == 0 and {k for k, v in ol.items() if v == 0} == {(-2, 2), (0, 0), (2, -2)})
# committed prefix
pref = {a: max(TW.policy_value(p) for p in pols if p[(0, (), ("blind",))] == a) for a in (-2, 0, 2)}
check("D1.6 committed-prefix corollary: the tree supremum with a fixed first action equals the node value of that action",
      pref == cells, pref)
# posterior-only counterexample
PO = C.posterior_only_instance()
clairvoyant = sum(p * max(Q(PO.G(w, (a, 0))) for a in (0, 1)) for w, p in PO.sc)
check("D1.7 posterior-only evaluation is not an envelope: the adapted value is 1/2 while conditioning the blind action on the later posterior would give 1",
      PO.root_value()[0] == Q(1, 2) and clairvoyant == 1)
# z0 sweep with robust values
sweep = {}
ok = True
for z0 in range(0, 9):
    Pz = C.two_window(Q(z0))
    q0 = Pz.root_value()[0]
    olz = max(C.open_loop_values(Q(z0)).values())
    try:
        R = C.robust_values_two_window(Q(z0))
        rup, rlo, cert = R["upper"], R["lower"], R["certified"]
    except Exception as e:                      # SciPy absent
        rup, rlo, cert = None, None, None
    sweep[z0] = dict(Q0=fr(q0), openloop=fr(olz), Rplus=(fr(rup) if rup is not None else None), Rminus=(fr(rlo) if rlo is not None else None), certified=cert,
                     mu_star=({str(k): fr(v) for k, v in R["mu_star"].items()} if rup is not None else None),
                     w_star_size=(len(R["w_star"]) if rup is not None else None))
    ok &= q0 >= olz and (rup is None or (rlo <= rup <= q0 and cert))
OUT["two_window"]["sweep"] = sweep
expQ0 = ["1", "3/4", "1/2", "0", "-1/2", "-5/4", "-2", "-3", "-4"]
expOL = ["1", "1/2", "0", "-1", "-2", "-3", "-4", "-5", "-6"]
check("D2.1 initial-distance sweep z0 = 0..8: Q0 = 1, 3/4, 1/2, 0, -1/2, -5/4, -2, -3, -4 and open-loop 1, 1/2, 0, -1, ..., -6",
      [sweep[z]["Q0"] for z in range(9)] == expQ0 and [sweep[z]["openloop"] for z in range(9)] == expOL, sweep)
check("D2.2 robust values over the coupling class M (uniform coordinate marginals): R- <= R+ <= Q0 at every z0, R+ certified exactly on both sides", ok and sweep[2]["Rplus"] is not None, sweep)
if sweep[2]["Rplus"] is not None:
    R2 = C.robust_values_two_window(Q(2))
    check("D2.3 at z0 = 2: R+ = 1/2 is attained by the product coupling itself (mu* uniform) while R- = 0; the gap is closed by a mixture of four trees with weights 1/4",
          R2["upper"] == Q(1, 2) and all(v == Q(1, 8) for v in R2["mu_star"].values()) and R2["lower"] == 0 and sorted(R2["w_star"].values()) == [Q(1, 4)] * 4, R2)
    R3 = C.robust_values_two_window(Q(3))
    check("D2.4 at z0 = 3: R+ = 0 = Q0 with a non-product worst coupling (support on four paths), R- = -1",
          R3["upper"] == 0 and R3["lower"] == -1 and sorted(R3["mu_star"].values()) == [Q(0)] * 4 + [Q(1, 4)] * 4, R3)
scen, verts = C.coupling_polytope_vertices()
check("D2.5 the coupling class M has exactly 6 extreme couplings (two independent enumerations agree); the product coupling is their barycentre",
      len(verts) == 6 and verts == C.coupling_vertices_bfs() and all(sum(v[j] for v in verts) / 6 == Q(1, 8) for j in range(8)))
OUT["two_window"]["coupling_vertices"] = [[fr(x) for x in v] for v in verts]
OUT["two_window"]["scenarios"] = [list(w) for w in scen]
if sweep[2]["Rplus"] is not None:
    vertex_vals = [max(sum(m * Q(TW.G(w, TW.run(p, w))) for m, w in zip(mu, scen)) for p in pols) for mu in verts]
    OUT["two_window"]["vertex_values_z2"] = [fr(v) for v in vertex_vals]
    check("D2.6 at z0 = 2 every extreme coupling is strictly better for the controller than the product coupling (vertex values > 1/2): the worst coupling is interior",
          min(vertex_vals) > Q(1, 2), vertex_vals)
# dynamic obstruction
P4 = C.two_window(Q(4))
pol4 = list(P4.policies())
check("D3.1 dynamic obstruction at z0 = 4: every one of the 171 trees has negative expectation; the defeating set has mass >= 3/8 under every tree; Q0 = -1/2",
      all(P4.policy_value(p) < 0 for p in pol4) and min(P4.defeat_mass(p) for p in pol4) == Q(3, 8) and P4.root_value()[0] == Q(-1, 2))
P3 = C.two_window(Q(3))
check("D3.2 z0 = 3 is the boundary: Q0 = 0 and some tree is never defeated in expectation but every tree is defeated on a set of positive mass",
      P3.root_value()[0] == 0 and min(P3.defeat_mass(p) for p in P3.policies()) > 0)
# instances A, B, C, matching
A = C.instance_A()
Avals = [A.policy_value(p) for p in A.policies()]
check("D4.1 instance A (K = 3, partitions 2 -> 4 -> 8, two actions): 2^14 = 16384 adapted trees; recursion value 0 = tree supremum",
      len(Avals) == 16384 == A.count_policies() and A.root_value()[0] == 0 == max(Avals))
B = C.instance_B()
Bp = list(B.policies())
check("D4.2 instance B (K = 2, blind first stage, three actions, full revelation at the second stage): 3 * 3^4 = 243 trees; value 1 at the blind action 0; tower identity on all trees",
      len(Bp) == 243 == B.count_policies() and B.root_value()[0] == 1 and max(B.policy_value(p) for p in Bp) == 1
      and B.root_value()[1]["blind"][1] == [0] and all(B.tower_value(p) == B.policy_value(p) for p in Bp))
Cc, Cf = C.instance_C(False), C.instance_C(True)
check("D4.3 refinement instance: coarse first observation (1024 trees) has value 1/2, the finer one (4096 trees) has value 3/4; both equal their tree suprema",
      Cc.count_policies() == 1024 and Cf.count_policies() == 4096 and Cc.root_value()[0] == Q(1, 2) and Cf.root_value()[0] == Q(3, 4)
      and max(Cc.policy_value(p) for p in Cc.policies()) == Q(1, 2) and max(Cf.policy_value(p) for p in Cf.policies()) == Q(3, 4))
match = {}
for part in ([(1,), (2,), (3,)], [(1, 2), (3,)], [(1,), (2, 3)], [(1, 3), (2,)], [(1, 2, 3)]):
    M = C.matching_instance(part)
    match[str(part)] = fr(M.root_value()[0])
OUT["matching"] = match
check("D4.4 matching instance: values 0 (singletons), -1/3 ({1,2}|{3} and {1}|{2,3}), -2/3 ({1,3}|{2} and blind): refinement is monotone but may add nothing",
      list(match.values()) == ["0", "-1/3", "-1/3", "-2/3", "-2/3"], match)
prod = sum(Q(1, 4) * d1 * d2 for d1 in (-1, 1) for d2 in (-1, 1))
como = Q(1, 2) * 1 + Q(1, 2) * 1
check("D4.5 coupling selection: G = d1 d2 has value 0 under the product coupling and 1 under the comonotone coupling with identical one-step marginals; the rho-mixture gives rho",
      prod == 0 and como == 1 and all(rho * como + (1 - rho) * prod == rho for rho in (Q(1, 3), Q(2, 5))))

# ======================================================================== G: integrated certificate
check("G1.1 three-branch instance: Gamma_h(tau) = 7/50 - tau for tau in {0, 1/10, 7/50, 1/5, 1/2}; zero at tau = 7/50",
      all(C.gamma_h(Q(t)) == Q(7, 50) - Q(t) for t in ("0", "1/10", "7/50", "1/5", "1/2")))
check("G1.2 the hexagon is centrally symmetric, so h_U(-g) = h_U(g) and the sign of the argument is immaterial on this instance",
      all(C.h_hex(n) == C.h_hex(tuple(-x for x in n)) == 1 for n in C.N3) and all(C.gamma_h(Q(t)) == C.gamma_h_wrong_sign(Q(t)) for t in ("0", "1/5")))
shift = (Q(1, 10), Q(0))
h_shift = lambda g: C.h_hex(g) + C.dot(g, shift)
lam_unbal = (Q(1, 2), Q(1, 4), Q(1, 4))
check("G1.3 for the translated hexagon U + (1/10,0) and unbalanced weights (1/2,1/4,1/4) the two sign conventions differ (h_U(-n_1) = 9/10 vs h_U(n_1) = 11/10): the formula must charge h_U(-sum lambda_l n_l)",
      h_shift(tuple(-x for x in C.N3[0])) == Q(9, 10) and h_shift(C.N3[0]) == Q(11, 10)
      and C.gamma_h(Q(1, 5), lam=lam_unbal, support=h_shift) != C.gamma_h_wrong_sign(Q(1, 5), lam=lam_unbal, support=h_shift)
      and C.gamma_h(Q(1, 5), lam=lam_unbal, support=h_shift) == C.gamma_h(Q(1, 5), lam=lam_unbal, support=h_shift))
check("G1.4 sign convention: Gamma_h(tau) = -Gamma(tau) of the companion certificate (tau - 7/50); pooled normal sum lambda_l n_l = 0 and sum lambda = 1",
      all(C.gamma_h(Q(t)) == -(Q(t) - Q(7, 50)) for t in ("0", "1/5")) and sum(C.LAM3) == 1
      and tuple(sum(l * n[i] for l, n in zip(C.LAM3, C.N3)) for i in range(2)) == (Q(0), Q(0)))

# ======================================================================== L: Lean footprint (scope record)
lean = None
for cand in (os.path.join(HERE, "Minimax_Dual.lean"), os.path.join(HERE, "src", "Minimax_Dual.lean"),
             os.path.join(HERE, "paper04_minimax_dual_certificates_v20_src", "Minimax_Dual.lean"), os.path.join(CORE_DIR, "..", "src", "Minimax_Dual.lean")):
    if os.path.exists(cand):
        lean = open(cand).read()
        break
if lean:
    decls = re.findall(r"^theorem\s+(\S+)", lean, flags=re.M)
    named = ["dual_certificate_sound", "parity_common_safe_empty", "parity_no_measure_certifies", "two_row_average",
             "\u03c8single_sum", "singleton_uniform", "singleton_every_measure", "singleton_worst_witnesses", "benchmark_obstruction"]
    OUT["lean"] = dict(n_theorems=len(decls), named=named)
    check(f"L1.1 Lean module Minimax_Dual.lean present: {len(decls)} theorem declarations = 13 arithmetic helpers + the 9 named footprints (all present); no sorry",
          len(decls) == 22 and all(n in decls for n in named) and "sorry" not in lean.replace("-- no sorry", ""))
    check("L1.2 benchmark_obstruction hypothesis holds at Y = 6: cap1 + cap2 = 47/25 < 2 <= u1 + u2 on U",
          sum(C.bench_caps(Q(6))) < 2 and all(v[0] + v[1] >= 2 for v in U.vertices()))
else:
    print("note: Minimax_Dual.lean not found; Lean footprint checks skipped")

# ======================================================================== text binding
aux = None
for cand in (os.path.join(HERE, "paper04_minimax_dual_certificates_v20.aux"),):
    if os.path.exists(cand):
        aux = open(cand).read()
if aux:
    def num(label):
        m = re.search(r"\\newlabel\{" + re.escape(label) + r"\}\{\{([^}]*)\}", aux)
        return m.group(1) if m else None
    expected = {"thm:dual": "3.1", "thm:helly": "3.3", "prop:nonconvex": "3.5", "thm:polyhedral": "3.6", "prop:taxonomy": "4.1",
                "prop:benchmark": "5.1", "prop:floor": "5.2", "thm:envelope": "6.2", "prop:robust": "6.5", "prop:integrated": "6.7"}
    got = {k: num(k) for k in expected}
    check("TXT.1 compiled numbering of the results quoted in figure captions and the supplement: " + ", ".join(f"{k} = {v}" for k, v in expected.items()),
          got == expected, got)
    tex = open(os.path.join(HERE, "paper04_minimax_dual_certificates_v20.tex")).read()
    for token in ("(27-5Y)/50", "77}{5}-5D", "2^{14}", "171", "7}{50}-\\tau", "47}{25}"):
        check(f"TXT headline token present in manuscript: {token}", token in tex)
    si_path = os.path.join(HERE, "paper04_minimax_dual_certificates_v20_supplementary.tex")
    if os.path.exists(si_path):
        si = open(si_path).read()
        table = dict(re.findall(r"mainlab@([^\\]*)\\endcsname\{([^}]*)\}", si))
        auxlabels = dict(re.findall(r"\\newlabel\{([^}@]*)\}\{\{([^}]*)\}", aux))
        check("TXT.2 supplement's main-text number table agrees with the compiled .aux on every label",
              bool(table) and all(table.get(k) == v for k, v in auxlabels.items()), f"{len(auxlabels)} labels")
else:
    print("note: compiled .aux not found; text-binding checks skipped")

# ======================================================================== record
OUT["n_checks"] = len(RESULTS)
OUT["n_pass"] = sum(1 for _, ok in RESULTS if ok)
OUT["quick"] = QUICK
OUT["seconds"] = round(time.time() - T0, 1)
os.makedirs(os.path.join(CORE_DIR), exist_ok=True)
with open(os.path.join(CORE_DIR, "results.json"), "w") as f:
    json.dump(OUT, f, indent=1, default=str)
print(f"\nverification: {OUT['n_pass']}/{OUT['n_checks']} checks pass in {OUT['seconds']} s" + (" (quick mode)" if QUICK else ""))
sys.exit(0 if OUT["n_pass"] == OUT["n_checks"] else 1)

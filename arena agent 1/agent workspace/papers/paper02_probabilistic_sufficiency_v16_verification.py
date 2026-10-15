#!/usr/bin/env python3
"""
Verification script for paper02 v16 (belief-state safety values).

Recomputes every headline value, witness, threshold, count and tabulated
entry of the manuscript from the definitions, in exact rational arithmetic
(standard library only, deterministic), using the exact module p02_core.py
(expected next to this script or in ./work/).  Finally binds the result
numbers quoted in the figure captions / titles to the compiled .aux file
when it is present.

Run:  python3 paper02_probabilistic_sufficiency_v16_verification.py
"""
import os, sys, random, re
from fractions import Fraction as Q
from itertools import product

HERE = os.path.dirname(os.path.abspath(__file__))
for cand in (HERE, os.path.join(HERE, "work"), os.path.join(HERE, "paper02_probabilistic_sufficiency_v16_src", "work")):
    if os.path.exists(os.path.join(cand, "p02_core.py")):
        sys.path.insert(0, cand)
        break
import p02_core as C

RESULTS = []
def check(name, cond, detail=""):
    RESULTS.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name + ("" if cond else "   <-- " + str(detail)))

GRID = C.GRID
half = Q(1, 2)

# ---------------------------------------------------------------- Section 2/3: generic model
M = C.two_floor()
G = M.alpha_sets(5)
check("S2.1 two-floor: Gamma_1 = {(1,0),(0,1)}", G[1] == {(Q(1), Q(0)), (Q(0), Q(1))}, G[1])
check("S2.2 two-floor: V_k(1/2,1/2) = 1/2 for k=1..5",
      all(M.value(G[k], {0: half, 1: half}) == half for k in range(1, 6)))
check("S2.3 two-floor: V_k(b) = max(b0,b1) on 11 beliefs, k=1..5",
      all(M.value(G[k], {0: Q(i, 10), 1: 1 - Q(i, 10)}) == max(Q(i, 10), 1 - Q(i, 10))
          for i in range(11) for k in range(1, 6)))
# chance-constrained certificate on the two-floor instance
delta = min(sum(half * (1 - sum(M.T[(x, a)].values(), Q(0))) for x in M.S) for a in M.A)
check("S4.1 two-floor: chance certificate delta = 1/2 = exact deficit", delta == half == 1 - M.value(G[3], {0: half, 1: half}))

# feedback family: value of observation bound attained
ok = True
for n in (2, 3, 4):
    Mn, P = C.feedback_family(n)
    Gn = Mn.alpha_sets(2)
    for trial in range(3):
        rnd = random.Random(100 + n + trial)
        ws = [Q(rnd.randint(1, 9)) for _ in range(n)]; tot = sum(ws)
        b = {p: w / tot for p, w in zip(P, ws)}
        vseq = Mn.value(Gn[2], b); vol = Mn.openloop_value(b, 2)[0]
        ok &= (vseq == 1 and vol == max(b.values()) and vseq - vol == 1 - max(b.values()))
check("S3.1 family F_n (n=2,3,4): V_seq_2 = 1, V_ol_2 = max b, gap = 1 - max b", ok)
M2, P2 = C.feedback_family(2)
check("S3.2 F_2: blind value 1/2 at uniform prior (strict feedback/blind separation)",
      M2.openloop_value({P2[0]: half, P2[1]: half}, 2)[0] == half)

# antichain: witnesses are 0/1 indicators and form an antichain (two-floor, F_n)
def is_antichain(vecs):
    vecs = list(vecs)
    return all(not (v != w and all(a <= b for a, b in zip(v, w))) for v in vecs for w in vecs)
check("S3.3 witnesses are {0,1}-vectors forming an antichain (two-floor k<=5, F_3 k<=2)",
      all(all(x in (0, 1) for v in G[k] for x in v) and is_antichain(G[k]) for k in range(1, 6))
      and all(all(x in (0, 1) for v in C.feedback_family(3)[0].alpha_sets(2)[k] for x in v) for k in range(3)))
# Sperner attained at k=1: n=4, actions = all 2-subsets
n = 4
states = list(range(n)); subsets = [s for s in product((0, 1), repeat=n) if sum(s) == n // 2]
T = {}; g = {}
for si, s in enumerate(subsets):
    for x in states:
        T[(x, si)] = {x: Q(1)} if s[x] else {}
        if s[x]:
            g[(x, si, x)] = {"y": Q(1)}
Msp = C.SafetyPOMDP(states, list(range(len(subsets))), ["y"], T, g)
from math import comb
check("S3.4 Sperner bound attained: n=4, |Gamma_1| = C(4,2) = 6", len(Msp.alpha_sets(1)[1]) == comb(4, 2) == 6)

# ---------------------------------------------------------------- Section 5: delayed instance
# closed forms vs brute force: structured sweep + random battery
sweep = [(Q(n, 4), Q(m, 10), ell) for n in range(0, 21) for m in range(0, 11) for ell in range(1, 7)]
bad = [(z, w, l) for z, w, l in sweep if C.bf_hold(z, w, l) != C.closed_hold(z, w, l) or C.bf_openloop(z, w, l) != C.closed_openloop(z, w, l)]
check(f"S5.1 closed forms (hold, open-loop) = brute force on structured sweep of {len(sweep)} triples", not bad, bad[:3])
rnd = random.Random(2026)
bad = 0
for _ in range(500):
    z = Q(rnd.randint(0, 60), 10); w = Q(rnd.randint(0, 20), 20); l = rnd.randint(1, 6)
    bad += (C.bf_hold(z, w, l) != C.closed_hold(z, w, l)) or (C.bf_openloop(z, w, l) != C.closed_openloop(z, w, l))
check("S5.2 closed forms = brute force on seeded random battery of 500 cases", bad == 0, bad)
# sequential value by the generic alpha-vector backup on the finite reachable model (single
# non-exit observation inside the window) must equal the open-loop closed form
def delayed_model(z0, ell):
    states = [(z0 + j, th) for j in range(-ell, ell + 1) for th in (-1, 1) if z0 + j >= 1]
    T, g = {}, {}
    for (z, th) in states:
        for u in (1, -1):
            z2 = z + th * u
            T[((z, th), u)] = {(z2, th): Q(1)} if (z2, th) in states else {}
            if (z2, th) in states:
                g[((z, th), u, (z2, th))] = {"y": Q(1)}
    return C.SafetyPOMDP(states, [1, -1], ["y"], T, g)
ok = True
for z0 in GRID:
    for ell in (1, 2, 3):
        Md = delayed_model(z0, ell)
        Gd = Md.alpha_sets(ell)
        for w in (half, Q(3, 10)):
            b = {(z0, 1): w, (z0, -1): 1 - w}
            ok &= Md.value(Gd[ell], b) == C.closed_openloop(z0, w, ell)
check("S5.3 sequential value by the generic alpha-vector backup = open-loop closed form (grid, l<=3, two priors)", ok)
check("S5.4 observed value = 1[z0>=1]", all(C.closed_observed(z) == (1 if z >= 1 else 0) for z in [Q(n, 10) for n in range(0, 40)]))
# lattice and gaps
ok = True
for z in [Q(n, 10) for n in range(10, 50)]:
    for w in [Q(m, 10) for m in range(11)]:
        for l in (1, 2, 3, 4):
            vh, vo, vs = C.closed_hold(z, w, l), C.closed_openloop(z, w, l), C.closed_observed(z)
            ok &= vh <= vo <= vs
            ok &= (vo - vh) == (min(w, 1 - w) if 2 <= z < 1 + l else 0)
            ok &= (vs - vo) == (min(w, 1 - w) if 1 <= z < 2 else 0)
check("S5.5 class lattice and both gaps (Theorem 5.2) on z0 in [1,5), w in tenths, l<=4", ok)
# census
types, distinct, unit, hv = C.census()
check("S5.6 census: 36 unit / 156 half values on 192 combinations", (unit, hv) == (36, 156), (unit, hv))
check("S5.7 witnesses: 384 vectors, types (1,1):72, (1,0):156, (0,1):156; 348 distinct",
      sum(types.values()) == 384 and types[(Q(1), Q(1))] == 72 and types[(Q(1), Q(0))] == 156 and types[(Q(0), Q(1))] == 156 and distinct == 348,
      (types, distinct))
viable, common, timing = C.cell_classes()
check("S5.8 partition: 6 viable / 30 common-action / 12 timing cells", (len(viable), len(common), len(timing)) == (6, 30, 12))
diff = C.class_difference(GRID)
check("S5.9 class-difference set on the grid: 36 combinations = timing cells x k in {2,3,4}",
      len(diff) == 36 and set(diff) == {(z, T, k) for (z, T) in timing for k in (2, 3, 4)})
ext = [Q(n, 10) for n in range(10, 41)]
check("S5.10 class-difference set = {2 <= z0 < 1+min(k,T)} on the extended grid to z0=4.0",
      set(C.class_difference(ext)) == set(C.region_difference(ext)))
check("S5.11 off-grid example (3.5, T=3, k=2): both classes attain one", C.bf_hold(Q(7, 2), half, 2) == C.bf_openloop(Q(7, 2), half, 2) == 1)
# jump loci
ok = True
for T in (1, 2, 3):
    for k in (1, 2, 3, 4):
        l = min(k, T)
        vals = [(z, C.closed_hold(z, half, l)) for z in [Q(n, 20) for n in range(0, 120)]]
        jumps = [vals[i][0] for i in range(1, len(vals)) if vals[i][1] != vals[i - 1][1]]
        ok &= jumps == [Q(1), Q(1 + l)]
check("S5.12 jump loci of the hold value: exactly z0=1 and z0=1+min(k,T)", ok)
# deficit profile
ok = True
for (z, T) in common + timing:
    for k in (1, 2, 3, 4):
        d = 1 - C.closed_hold(z, half, min(k, T))
        expect = half if (k > T or k > z - 1) else 0
        ok &= d == expect
check("S5.13 deficit profile on the 42 nonviable cells (0 before falling-branch exit, 1/2 after)", ok)
check("S5.14 timing cells: deficit 0 at k=1 and 1/2 at k>=2; common cells: 1/2 at all k",
      all(1 - C.closed_hold(z, half, 1) == 0 and all(1 - C.closed_hold(z, half, min(k, T)) == half for k in (2, 3, 4)) for z, T in timing)
      and all(1 - C.closed_hold(z, half, min(k, T)) == half for z, T in common for k in (1, 2, 3, 4)))
# asymmetric audit
masses = {seq: (Q(3, 10) if C.survives_branch(Q(3, 2), 1, list(seq)) else 0) + (Q(7, 10) if C.survives_branch(Q(3, 2), -1, list(seq)) else 0)
          for seq in product((1, -1), repeat=2)}
check("S4.2 asymmetric audit at (3/2,2), w=3/10: masses {3/10,3/10,7/10,7/10}, value 7/10, deficit 3/10 = min mass",
      sorted(masses.values()) == [Q(3, 10), Q(3, 10), Q(7, 10), Q(7, 10)] and max(masses.values()) == Q(7, 10))
# stabilization to horizon 40
check("S3.5 stabilization: hold value frozen for k>=T_obs, open-loop from k=1, to horizon 40 on the grid",
      all(C.closed_hold(z, half, min(k, T)) == C.closed_hold(z, half, T) for z in GRID for T in (1, 2, 3) for k in range(T, 41))
      and all(C.bf_openloop(z, half, l) == C.bf_openloop(z, half, 1) for z in GRID for l in range(1, 9)))
check("S3.6 survivable families nested: V_l non-increasing in l (brute force, grid, l<=6)",
      all(C.bf_openloop(z, w, l + 1) <= C.bf_openloop(z, w, l) and C.bf_hold(z, w, l + 1) <= C.bf_hold(z, w, l)
          for z in GRID for w in (Q(3, 10), half) for l in range(1, 6)))

# ---------------------------------------------------------------- Section 6: deadlines
check("S6.1 theta observed: all 16 grid states viable", all(C.theta_observed_viable(z) for z in GRID))
check("S6.2 free probe: viable iff z0 >= 21/10 (5 grid states)",
      [z for z in GRID if C.pinned_probe_viable(z, 0)] == [z for z in GRID if z >= Q(21, 10)] and sum(z >= Q(21, 10) for z in GRID) == 5)
fine = [Q(n, 20) for n in range(20, 80)]
check("S6.3 pinned-probe identity 21/10 + T/10 on a 1/20 grid, T=0..6",
      all((z >= C.pinned_threshold(T)) == C.pinned_probe_viable(z, T) for z in fine for T in range(7)))
check("S6.4 kernel sizes 5,4,3,2,1 (pinned) and 16,15,14,13,12 (probe-free)",
      [sum(C.pinned_probe_viable(z, T) for z in GRID) for T in range(5)] == [5, 4, 3, 2, 1]
      and [sum(C.probe_free_viable(z, T) for z in GRID) for T in range(5)] == [16, 15, 14, 13, 12])
check("S6.5 probe-free threshold 1 + T/10 on a 1/20 grid", all((z >= 1 + Q(T, 10)) == C.probe_free_viable(z, T) for z in fine for T in range(7)))
# general law: instance A and B aligned, misaligned example
dhA = lambda th: Q(-1, 10); dpA = lambda th: Q(-1, 10) + th; dlA = lambda th: Q(9, 10)
dhB = lambda th: Q(-3, 20); dpB = lambda th: Q(-3, 20) + Q(9, 10) * th; dlB = lambda th: Q(-3, 20) + Q(9, 10)
dhM = lambda th: Q(-1, 2) + Q(1, 2) * th; dpM = lambda th: Q(-1, 2) - Q(1, 2) * th; dlM = lambda th: Q(1)
ok = True
for T in range(7):
    ok &= C.general_threshold(T, dhA, dpA, (-1, 1)) == Q(21, 10) + Q(T, 10)
    ok &= C.general_threshold(T, dhB, dpB, (-1, 1)) == Q(41, 20) + Q(3 * T, 20)
    ok &= all((z >= Q(41, 20) + Q(3 * T, 20)) == C.schedule_viable(z, T, dhB, dpB, dlB, (-1, 1)) for z in fine)
    ok &= all((z >= C.general_threshold(T, dhM, dpM, (-1, 1))) == C.schedule_viable(z, T, dhM, dpM, dlM, (-1, 1)) for z in fine)
check("S6.6 general schedule law: thresholds 21/10+T/10 (A), 41/20+3T/20 (B), exact on misaligned instance, T=0..6", ok)
check("S6.7 misaligned instance at T=1: exact threshold 2, additive value 3",
      C.general_threshold(1, dhM, dpM, (-1, 1)) == 2 and 1 + 1 * 1 + 1 == 3 and C.schedule_viable(Q(2), 1, dhM, dpM, dlM, (-1, 1)))
check("S6.8 delayed instance as schedule: 1 + T_obs threshold for the hold class at k > T_obs",
      all((z >= 1 + T) == (C.closed_hold(z, half, T) == 1) for z in fine for T in (1, 2, 3)))

# ---------------------------------------------------------------- Section 7: stochastic layer
ok = True
for i in range(0, 21):
    b1 = Q(i, 20); b2 = 1 - b1
    for eps in (Q(1, 20), Q(1, 10), Q(1, 4)):
        d = C.sensor_deficits(b1, b2, eps)
        ok &= min(d.values()) == min(eps, b1, b2)
        ok &= d["own"] == eps and d["always1"] == b2 and d["always2"] == b1 and d["opposite"] == 1 - eps
check("S7.1 sensor instance: Delta_1 = min{eps, b1, b2} over all four maps, prior sweep", ok)
check("S7.2 sensor at (1/2,1/2), eps=1/20: deficit 1/20 < min mass 1/2",
      min(C.sensor_deficits(half, half, Q(1, 20)).values()) == Q(1, 20) < half)
check("S7.3 sensor at (99/100,1/100): optimal deficit 1/100 (constant map), below eps",
      min(C.sensor_deficits(Q(99, 100), Q(1, 100), Q(1, 20)).values()) == Q(1, 100))
ok = True
for z in [Q(n, 10) for n in range(8, 60)]:
    for tp in range(4):
        for k in range(tp, tp + 7):
            for eps in (Q(1, 10), Q(1, 20), Q(1, 4)):
                ok &= C.noisy_probe_value_formula(z, tp, k, eps) == C.noisy_probe_value_bf(z, tp, k, eps)
check("S7.4 noisy-probe closed form = enumeration over (theta, reading)", ok)
ok = True
levels = set()
for z in [Q(n, 10) for n in range(8, 60)]:
    for tp in range(4):
        for k in range(tp + 2, tp + 9):
            v3 = C.majority3_value_formula(z, tp, k, Q(1, 10)); ok &= v3 == C.majority3_value_bf(z, tp, k, Q(1, 10))
            levels.add(C.noisy_probe_value_formula(z, tp, k, Q(1, 10)))
check("S7.5 majority-of-three closed form = enumeration over 8 reading patterns", ok)
check("S7.6 single-probe values take exactly the levels {0, 9/10, 1} at eps=1/10", levels == {Q(0), Q(9, 10), Q(1)}, levels)
check("S7.7 p_3 = eps^2(3-2eps) = 7/250 at eps=1/10", C.majority_wrong(3, Q(1, 10)) == Q(7, 250) == Q(1, 100) * (3 - Q(2, 10)))
exact = {1: Q(1, 10), 3: Q(7, 250), 5: Q(107, 12500), 7: Q(341, 125000), 9: Q(22273, 25000000)}
check("S7.8 exact wrong-majority probabilities n=1,3,5,7,9 and bound (3/5)^n",
      all(C.majority_wrong(n, Q(1, 10)) == v and v <= Q(3, 5) ** n for n, v in exact.items()))
check("S7.9 bound (4eps(1-eps))^(n/2) holds for eps in {1/10,1/5,3/10,2/5}, odd n<=15 (squared form)",
      all(C.majority_wrong(n, e) ** 2 <= (4 * e * (1 - e)) ** n for e in (Q(1, 10), Q(1, 5), Q(3, 10), Q(2, 5)) for n in range(1, 16, 2)))
# deficit on the middle band equals the post-reading minimal mass eps
check("S7.10 noisy probe: deficit = eps exactly on the middle band",
      all((1 - C.noisy_probe_value_formula(z, 0, 2, Q(1, 10)) == Q(1, 10)) == (1 <= z < 1 + Q(11, 10) * 2) for z in [Q(n, 10) for n in range(8, 60)]))

# ---------------------------------------------------------------- Section 8: contamination
Cm = C.contamination_example()
check("S8.1 contamination example: V_2^{1/2} = 1/16, endpoints 1/4 and 0, affine mix 1/8",
      Cm.value_rho({"s": Q(1)}, 2, half) == Q(1, 16) and Cm.value_rho({"s": Q(1)}, 2, Q(0)) == Q(1, 4)
      and Cm.value_rho({"s": Q(1)}, 2, Q(1)) == 0 and half * Q(1, 4) == Q(1, 8))
check("S8.2 contamination example: V_k^rho = ((1-rho)/2)^k for k<=4, rho in quarters",
      all(Cm.value_rho({"s": Q(1)}, k, r) == ((1 - r) / 2) ** k for k in range(5) for r in (Q(0), Q(1, 4), half, Q(3, 4), Q(1))))
# one-stage identity vs vertex enumeration
ok = True
rnd = random.Random(7)
for _ in range(200):
    m = rnd.randint(2, 5)
    p = [Q(rnd.randint(0, 5)) for _ in range(m)]; s = sum(p) or Q(1); p = [x / s for x in p]
    v = [Q(rnd.randint(0, 10), 10) for _ in range(m)]
    for r in (Q(0), Q(1, 3), half, Q(1)):
        lhs = min((1 - r) * sum(pi * vi for pi, vi in zip(p, v)) + r * v[j] for j in range(m))
        ok &= lhs == (1 - r) * sum(pi * vi for pi, vi in zip(p, v)) + r * min(v)
check("S8.3 one-stage contamination identity = vertex enumeration (200 random cases)", ok)
# prior contamination closed form
ok = True
for z in [Q(n, 10) for n in range(5, 45)]:
    for w in [Q(m, 10) for m in range(11)]:
        for l in (1, 2, 3):
            for r in (Q(0), Q(1, 4), half, Q(3, 4), Q(1)):
                vals = []
                for u in (1, -1):
                    sp = C.survives_branch(z, 1, [u] * l); sm = C.survives_branch(z, -1, [u] * l)
                    vals.append(min(((1 - r) * w + r * rr) * int(sp) + ((1 - r) * (1 - w) + r * (1 - rr)) * int(sm) for rr in (Q(0), Q(1))))
                v = max(vals)
                expect = Q(0) if z < 1 else (Q(1) if z >= 1 + l else (1 - r) * max(w, 1 - w))
                ok &= v == expect
check("S8.4 prior-contamination closed form on the delayed hold class (vertex enumeration)", ok)
check("S8.5 two-floor value is convex, not concave: midpoint 1/2 < average of vertex values 1",
      M.value(G[1], {0: half, 1: half}) == half and M.value(G[1], {0: Q(1)}) == 1 and M.value(G[1], {1: Q(1)}) == 1)

# ---------------------------------------------------------------- SI: two-patch instance
Bx = frozenset({(1, 2), (2, 1)})
Bh = frozenset({(x, g) for x in Bx for g in (1, 2)})
agg = lambda xe: xe[0][0] + xe[0][1]; full = lambda xe: xe
check("SI4.1 two-patch: hidden g + aggregate observation nonviable; (x,g) observed viable; each fixed g viable under full observation",
      (not C.patch_viable(Bh, agg, 12)) and (not C.patch_viable(Bh, agg, 10)) and C.patch_viable(Bh, full, 12) and C.patch_viable(Bh, full, 10)
      and all(C.patch_viable(frozenset({(x, g) for x in Bx}), full, 12) for g in (1, 2)))

# ---------------------------------------------------------------- text binding: figure captions vs .aux numbering
aux = None
for cand in (os.path.join(HERE, "paper02_probabilistic_sufficiency_v16.aux"),):
    if os.path.exists(cand):
        aux = open(cand).read()
if aux:
    def num(label):
        m = re.search(r"\\newlabel\{" + re.escape(label) + r"\}\{\{([^}]*)\}", aux)
        return m.group(1) if m else None
    check("TXT.1 compiled numbering: thm:closed = 5.1 (quoted in Figure 2 title)", num("thm:closed") == "5.1", num("thm:closed"))
    check("TXT.2 compiled numbering: prop:deadline = 6.1 (quoted in Figure 3 title)", num("prop:deadline") == "6.1", num("prop:deadline"))
    check("TXT.3 compiled numbering: prop:noisyprobe = 7.2 and prop:probecount = 7.3 (Figure 4 titles)",
          num("prop:noisyprobe") == "7.2" and num("prop:probecount") == "7.3", (num("prop:noisyprobe"), num("prop:probecount")))
    check("TXT.4 compiled numbering: thm:support = 3.1, thm:antichain = 3.3, thm:lattice = 5.2, cor:timing = 5.3, thm:additive = 6.2",
          (num("thm:support"), num("thm:antichain"), num("thm:lattice"), num("cor:timing"), num("thm:additive")) == ("3.1", "3.3", "5.2", "5.3", "6.2"))
    tex = open(os.path.join(HERE, "paper02_probabilistic_sufficiency_v16.tex")).read()
    for token in ("36/156", "348", "384", "\\tfr{21}{10}+\\tfr{\\Tl}{10}", "\\tfr7{250}", "\\tfr1{16}", "\\tfr{41}{20}+\\tfr{3T}{20}", "\\tfr{22273}{25000000}"):
        check(f"TXT headline token present in manuscript: {token}", token in tex)
    si_path = os.path.join(HERE, "paper02_probabilistic_sufficiency_v16_supplementary.tex")
    if os.path.exists(si_path):
        si = open(si_path).read()
        table = dict(re.findall(r"mainlab@([^\\]*)\\endcsname\{([^}]*)\}", si))
        auxlabels = dict(re.findall(r"\\newlabel\{([^}@]*)\}\{\{([^}]*)\}", aux))
        check("TXT.5 supplement's main-text number table agrees with the compiled .aux on every label",
              bool(table) and all(table.get(k) == v for k, v in auxlabels.items()),
              f"{len(auxlabels)} labels")
else:
    print("note: compiled .aux not found; text-binding checks skipped")

n_pass = sum(1 for _, ok in RESULTS if ok)
print(f"\nverification: {n_pass}/{len(RESULTS)} checks pass")
sys.exit(0 if n_pass == len(RESULTS) else 1)

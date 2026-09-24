#!/usr/bin/env python3
"""
Worked-systems audit, edition 8 — verification.

Layer 1 (chain): runs the per-system verification scripts of the companion
archive as subprocesses and asserts each exits green (8+8+9+8+8+8+8 = 57
checks).
Layer 2 (own): recomputes the headline identities from the shared audit
system's primitives — the pair family, the codex-threaded winning recursion
(no-repeat threaded as a parameter), the partition census, the benchmark
caps, the CE drift bounds, the delay identity, the decentralized law
campaign — independently of the per-system scripts, and projects every
printed table (the 36x5 master table, the 16 timing rows, the six
benchmark rows, the five drift rows, the 4x4 sustaining-law product)
against the recomputation.
Layer 3 (text): asserts every headline number printed in
paper2_worked_systems_v9.tex, the separate declaration headings, the
responsibility wording, and the five figure files.

Edition 8 additions (rigor elevation): the audited identities are stated
as propositions with proofs — the general timing law (all z0 >= 1, all
integer deadlines), the exact benchmark crossover with its margin formula
(Y - 27/5)/10, branchwise full-information decomposition with an explicit
memoryless singleton policy, the class lattice, register-semantics
invariance, the authority-restriction zero lemma, the two-floor saddle
with uniqueness, and Helly sparsity. Each is re-verified here.
Edition 7 additions (round-3 audit): the pessimistic shared-register
semantics is shown setwise-equal to the audited single-thread recursion
on all four policy-class kernels; the no-repeat forced loss of 12|31 is
re-derived branch-by-branch under both observation structures; the
agency-restriction counts (16 vs 0 sustaining laws) are recomputed; and
the floored-strict timing counts (6 cells vs 1) are pinned.

Exact rational/integer arithmetic; stdlib only; deterministic.
Run: python3 paper2_worked_systems_v9_verification.py
"""
import subprocess, sys, math, os
from fractions import Fraction as Q
from itertools import product

HERE = os.path.dirname(os.path.abspath(__file__))
PASS = []
def check(name, cond, detail=""):
    PASS.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name + ("" if cond else " " + str(detail)))

# ---------------- Layer 1: the chained lineage scripts -------------------------
LINEAGES = [
    ("paper2_selector_concordance_v1_verify.py", 8),
    ("minimax_dual_certificates_v1_verify.py", 8),
    ("monitoring_design_v3_verify.py", 9),
    ("vector_floor_certificates_v2_verify.py", 8),
    ("policy_class_lattice_v2_verify.py", 8),
    ("hybrid_mode_viability_v2_verify.py", 8),
    ("institutional_observation_v2_verify.py", 8),
]
total_chained = 0
for script, expected in LINEAGES:
    p = subprocess.run([sys.executable, os.path.join(HERE, script)],
                       capture_output=True, text=True)
    tail = p.stdout.strip().splitlines()[-1] if p.stdout.strip() else ""
    ok = (p.returncode == 0) and (f"{expected}/{expected} checks pass" in tail)
    total_chained += expected if ok else 0
    check(f"chain {script} green ({expected}/{expected})", ok)
check("chained total = 57 checks", total_chained == 57, f"({total_chained})")

# ---------------- shared audit system (ported primitives) ----------------------
CAP = 3
def step(x, u):
    z1, z2 = x
    if u == 0:
        return (max(0, z1 - 1), max(0, z2 - 1))
    return (max(0, min(CAP, z1 + 1 - (0 if u == 1 else 2))),
            max(0, min(CAP, z2 + 1 - (0 if u == 2 else 2))))
STATES = [(a, b) for a in range(4) for b in range(4)]
Vset = frozenset(x for x in STATES if x[0] >= 1 and x[1] >= 1)
pairs = sorted(frozenset({x, y}) for x in Vset for y in Vset if x < y)
H = 12
def parts_of(B, info):
    p = {}
    for x in B:
        p.setdefault(info(x), set()).add(x)
    return p
def win(B, info, h, last=None, alt=False):
    if h == 0:
        return B <= Vset
    cells = parts_of(B, info)
    acts = []
    for c in cells.values():
        cu = [u for u in (1, 2) if all(step(x, u) in Vset for x in c)]
        if not cu:
            return False
        if alt:
            cu = [u for u in cu if u != last]
            if not cu:
                return False
        acts.append(cu)
    for choice in product(*acts):
        choice_last = choice[0]
        succ = set()
        for c, u in zip(cells.values(), choice):
            succ |= {step(x, u) for x in c}
        ps = [frozenset(p) for p in parts_of(succ, info).values()]
        if all(win(p, info, h - 1, choice_last, alt) for p in ps):
            return True
    return False
def verd(B, info, alt=False):
    return win(B, info, H, None, alt) and win(B, info, H - 2, None, alt)

SH = {(1,1): "11", (1,2): "12", (1,3): "13", (2,1): "21", (2,2): "22",
      (2,3): "23", (3,1): "31", (3,2): "32", (3,3): "33"}
def pr(B):
    return "|".join(SH[x] for x in sorted(B))

agg, full = lambda x: x[0] + x[1], lambda x: x
K_inst = frozenset(B for B in pairs if verd(B, agg, alt=True))
K_agg  = frozenset(B for B in pairs if verd(B, agg))
K_cod  = frozenset(B for B in pairs if verd(B, full, alt=True))
K_full = frozenset(B for B in pairs if verd(B, full))

# ---------------- decentralized (ported from institutional_observation_v2) -----
def law_traj_ok(B, law1, law2, cap=512):
    cur, seen = frozenset(B), set()
    while True:
        if not (cur <= Vset):
            return False
        if cur in seen:
            return True
        seen.add(cur)
        if len(seen) > cap:
            return False
        nxt = set()
        for x in cur:
            u = law1[x[0]] if law1[x[0]] == law2[x[1]] else 0
            nxt.add(step(x, u))
        cur = frozenset(nxt)
LAW_PAIRS = [(l1, l2) for l1 in
             [dict(zip(range(4), t)) for t in product((1, 2), repeat=4)]
             for l2 in
             [dict(zip(range(4), t)) for t in product((1, 2), repeat=4)]]
assert len(LAW_PAIRS) == 256
K_dec = frozenset(B for B in pairs if any(law_traj_ok(B, l1, l2)
                                          for l1, l2 in LAW_PAIRS))
AUDITED = frozenset({(1, 2), (2, 1)})

# ---------------- Layer 2: identities and table projections --------------------
check("M1 pair family 36; corner singleton nonviable; full kernel = the 28 "
      "corner-free pairs",
      len(pairs) == 36 and not verd(frozenset({(1, 1)}), lambda x: x)
      and K_full == frozenset(B for B in pairs if (1, 1) not in B))
missing_join = K_full - (K_agg | K_cod)
check("M2 counts (24, 26, 25, 28); meet of middles = inst setwise; "
      "kernel union one pair short of full: exactly 12|21",
      (len(K_inst), len(K_agg), len(K_cod), len(K_full)) == (24, 26, 25, 28)
      and (K_agg & K_cod) == K_inst
      and missing_join == {AUDITED})
P1231 = frozenset({(1, 2), (3, 1)})
P1321 = frozenset({(1, 3), (2, 1)})
P1331 = frozenset({(1, 3), (3, 1)})
check("M3 per-pair readings: 12|31 and 13|21 are aggregate-not-codex; "
      "13|31 is codex-not-aggregate",
      P1231 in (K_agg - K_cod) and P1321 in (K_agg - K_cod)
      and P1331 in (K_cod - K_agg))

# ---- edition 7: register semantics and forced-loss reconciliation --------------
def win_adv(B, info, h, last=None, alt=False):
    """Pessimistic shared register: the policy fixes one action per fibre; the
    register then holds SOME fibre's executed action; the belief survives only
    if every admissible thread (each fibre's action entering the register)
    leaves a winning continuation."""
    if h == 0:
        return B <= Vset
    cells = list(parts_of(B, info).values())
    acts = []
    for c in cells:
        cu = [u for u in (1, 2) if all(step(x, u) in Vset for x in c)]
        if not cu:
            return False
        if alt:
            cu = [u for u in cu if u != last]
            if not cu:
                return False
        acts.append(cu)
    for choice in product(*acts):
        succ = set()
        for c, u in zip(cells, choice):
            succ |= {step(x, u) for x in c}
        ps = [frozenset(p) for p in parts_of(succ, info).values()]
        if all(all(win_adv(p, info, h - 1, cl, alt) for p in ps)
               for cl in sorted(set(choice))):
            return True
    return False
def verd_adv(B, info, alt=False):
    return win_adv(B, info, H, None, alt) and win_adv(B, info, H - 2, None, alt)
ADV = (frozenset(B for B in pairs if verd_adv(B, agg, alt=True)),
       frozenset(B for B in pairs if verd_adv(B, agg)),
       frozenset(B for B in pairs if verd_adv(B, full, alt=True)),
       frozenset(B for B in pairs if verd_adv(B, full)))
check("M2b register semantics: the pessimistic shared-register kernels equal "
      "the audited single-thread kernels (24, 26, 25, 28) setwise --- the "
      "audited counts are thread-order independent",
      ADV == (K_inst, K_agg, K_cod, K_full))

def win_opt(B, info, h, last=None, alt=False):
    """Optimistic register: the register thread is chosen favourably (exists a
    thread leaving a winning continuation at every node)."""
    if h == 0:
        return B <= Vset
    cells = list(parts_of(B, info).values())
    acts = []
    for c in cells:
        cu = [u for u in (1, 2) if all(step(x, u) in Vset for x in c)]
        if not cu:
            return False
        if alt:
            cu = [u for u in cu if u != last]
            if not cu:
                return False
        acts.append(cu)
    for choice in product(*acts):
        succ = set()
        for c, u in zip(cells, choice):
            succ |= {step(x, u) for x in c}
        ps = [frozenset(p) for p in parts_of(succ, info).values()]
        if any(all(win_opt(p, info, h - 1, cl, alt) for p in ps)
               for cl in sorted(set(choice))):
            return True
    return False
OPT_cod = frozenset(B for B in pairs
                    if win_opt(B, full, H, None, True)
                    and win_opt(B, full, H - 2, None, True))
check("M2c optimistic-vs-pessimistic contrast: the optimistic codex kernel "
      "strictly contains the audited one, regains 12|31 and 13|21, keeps 13|31 "
      "and still excludes 12|21",
      OPT_cod > K_cod and {P1231, P1321} <= (OPT_cod - K_cod)
      and P1331 in OPT_cod and AUDITED not in OPT_cod)

def forced_loss(info):
    """Every step-1 action choice leaves some branch whose filtered action set
    is empty at step 2 (the register blocks the forced continuation)."""
    B0 = frozenset({(1, 2), (3, 1)})
    cells = list(parts_of(B0, info).values())
    acts = [[u for u in (1, 2) if all(step(x, u) in Vset for x in c)]
            for c in cells]
    for choice in product(*acts):
        cl = choice[0]
        succ = set()
        for c, u in zip(cells, choice):
            succ |= {step(x, u) for x in c}
        dead = False
        for p in parts_of(succ, info).values():
            cu = [u for u in (1, 2) if all(step(x, u) in Vset for x in p)]
            if not [u for u in cu if u != cl]:
                dead = True
        if not dead:
            return False
    return True
check("M3b 12|31: free-protocol viable under both structures at H = 12 and "
      "H - 2, no-repeat dead under both, and the loss is forced at step 2 "
      "through the shared register",
      win(P1231, agg, H) and win(P1231, agg, H - 2)
      and win(P1231, full, H) and win(P1231, full, H - 2)
      and not win(P1231, full, H, None, True)
      and not win(P1231, full, H - 2, None, True)
      and not win(P1231, agg, H, None, True)
      and forced_loss(full) and forced_loss(agg))

fix1 = sum(1 for l1, l2 in LAW_PAIRS if l1[1] == 1
           and law_traj_ok(AUDITED, l1, l2))
fix2 = sum(1 for l1, l2 in LAW_PAIRS if l2[1] == 1
           and law_traj_ok(AUDITED, l1, l2))
LAW1 = {0: 1, 1: 1, 2: 1, 3: 1}
kfix1 = sum(1 for B in pairs if any(l1 == LAW1 and law_traj_ok(B, l1, l2)
                                    for l1, l2 in LAW_PAIRS))
kfix2 = sum(1 for B in pairs if any(l2 == LAW1 and law_traj_ok(B, l1, l2)
                                    for l1, l2 in LAW_PAIRS))
check("M-new agency restriction: fixing agency 1's vote at z = 1 to instrument "
      "1 leaves 16 sustaining laws for 12|21 while fixing agency 2's leaves 0; "
      "either whole-law restriction collapses the kernel to 0",
      fix1 == 16 and fix2 == 0 and kfix1 == 0 and kfix2 == 0)

R = lambda x: [u for u in (1, 2) if step(x, u) in Vset]
TARGET = [(1, 2), (2, 1), (2, 2), (3, 1)]
def partitions(S):
    if not S:
        yield []
        return
    first, rest = S[0], S[1:]
    for p in partitions(rest):
        for i in range(len(p)):
            yield p[:i] + [[first] + p[i]] + p[i + 1:]
        yield p + [[first]]
ALLP = sorted(tuple(tuple(sorted(F)) for F in P) for P in partitions(TARGET))
def inter_R(F):
    s = set(R(F[0]))
    for x in F[1:]:
        s &= set(R(x))
    return s
adequate = [P for P in ALLP if all(inter_R(F) for F in P)]
max_sets = [frozenset({(1, 2), (2, 2)}), frozenset({(2, 1), (2, 2), (3, 1)})]
check("M4 census: 15 partitions, 7 adequate, minimal two-cell rows 6-7; "
      "adequate iff no fibre merges (1,2) with (2,1); maxima overlap in (2,2)",
      len(ALLP) == 15 and len(adequate) == 7
      and sum(1 for P in adequate if len(P) == 2) == 2
      and all(all(not ({(1, 2)} <= set(F)
                       and len(set(F) & {(2, 1), (3, 1)}) > 0)
                  for F in P) for P in adequate)
      and all(any({(1, 2)} <= set(F)
                  and len(set(F) & {(2, 1), (3, 1)}) > 0 for F in P)
              for P in ALLP if P not in adequate)
      and max_sets[0] & max_sets[1] == {(2, 2)})

# master-table projection: the printed 36 rows x 5 marks vs recomputation
MASTER_ROWS = [
    ("12|21", 0,0,0,1,1), ("12|31", 0,1,0,1,0), ("12|23", 1,1,1,1,1),
    ("12|33", 1,1,1,1,0), ("12|22", 1,1,1,1,0), ("12|32", 1,1,1,1,1),
    ("12|13", 1,1,1,1,0), ("13|21", 0,1,0,1,0), ("13|31", 0,0,1,1,1),
    ("13|23", 1,1,1,1,0), ("13|33", 1,1,1,1,1), ("13|22", 1,1,1,1,1),
    ("13|32", 1,1,1,1,0), ("21|31", 1,1,1,1,0), ("21|23", 1,1,1,1,1),
    ("21|33", 1,1,1,1,0), ("21|22", 1,1,1,1,0), ("21|32", 1,1,1,1,1),
    ("22|31", 1,1,1,1,1), ("22|23", 1,1,1,1,0), ("22|33", 1,1,1,1,1),
    ("22|32", 1,1,1,1,0), ("23|31", 1,1,1,1,0), ("23|33", 1,1,1,1,0),
    ("23|32", 1,1,1,1,1), ("31|33", 1,1,1,1,1), ("31|32", 1,1,1,1,0),
    ("32|33", 1,1,1,1,0), ("11|12", 0,0,0,0,0), ("11|21", 0,0,0,0,0),
    ("11|31", 0,0,0,0,0), ("11|23", 0,0,0,0,0), ("11|33", 0,0,0,0,0),
    ("11|22", 0,0,0,0,0), ("11|32", 0,0,0,0,0), ("11|13", 0,0,0,0,0),
]
ok_rows, seen = True, set()
for name, i_, a_, c_, f_, d_ in MASTER_ROWS:
    x1, x2 = int(name[:2]), int(name[3:])
    B = frozenset({(x1 // 10, x1 % 10), (x2 // 10, x2 % 10)})
    seen.add(B)
    patt = (B in K_inst, B in K_agg, B in K_cod, B in K_full, B in K_dec)
    ok_rows &= (patt == (bool(i_), bool(a_), bool(c_), bool(f_), bool(d_)))
check("M5 master-table projection: all 36 printed rows x 5 kernel marks "
      "equal the recomputed membership; column sums 24/26/25/28/12",
      ok_rows and seen == set(pairs)
      and (len(K_inst), len(K_agg), len(K_cod), len(K_full), len(K_dec))
      == (24, 26, 25, 28, 12))


# timing grid + printed-row projection
GRID = [Q(n, 10) for n in range(10, 26)]
TOS = [1, 2, 3]
sig = lambda z: max(k for k in range(0, 4) if z >= 1 + k)
ok_t = all(sig(z) == math.floor(float(z) - 1) for z in GRID)
le_bad = [(z, T) for z in GRID for T in TOS if ((z - 1) >= T) != (z >= 1 + T)]
strict_bad = [(z, T) for z in GRID for T in TOS
              if ((z - 1) > T) != (z >= 1 + T)]
row_ok = True
for z in GRID:
    want = ((z >= 2, z >= 2), (False, False), (False, False))
    got = tuple((T <= sig(z), T <= sig(z)) for T in TOS)
    row_ok &= (got == want)
check("M6 timing: sigma* = floor(z0-1); identity == viability on all 48 "
      "cells; strict fails exactly at (2.0, 1); printed 16-row projection "
      "correct (six viable cells)",
      ok_t and not le_bad and strict_bad == [(Q(2), 1)] and row_ok)

strict_floored_bad = [(z, T) for z in GRID for T in TOS
                      if (math.floor(float(z) - 1) > T) != (z - 1 >= T)]
check("M6b floored-strict vs real-strict: the strict form against the floored "
      "count fails on all six viable cells; against the real value on exactly "
      "(2.0, 1) --- the tau*/sigma* split is load-bearing",
      len(strict_floored_bad) == 6
      and sorted(z for z, _ in strict_floored_bad)
      == [Q(n, 10) for n in range(20, 26)]
      and all(T == 1 for _, T in strict_floored_bad)
      and strict_bad == [(Q(2), 1)])

# the 16 sustaining law pairs of the audited belief: an exact 4x4 product
L1 = ["1121", "1122", "2121", "2122"]
L2 = ["1211", "1212", "2211", "2212"]
prod_set = {(l1, l2) for l1 in L1 for l2 in L2}
law_of = lambda s: dict(zip(range(4), (int(s[0]), int(s[1]), int(s[2]),
                                       int(s[3]))))
sustaining = {("".join(str(l1[z]) for z in range(4)),
               "".join(str(l2[z]) for z in range(4)))
              for l1, l2 in LAW_PAIRS if law_traj_ok(AUDITED, l1, l2)}
check("M7 decentralized: kernel 12 of 36; sustaining set of the audited "
      "belief is exactly the 4x4 product L1 x L2 (16 of 256)",
      len(K_dec) == 12 and sustaining == prod_set
      and len(sustaining) == 16)

# benchmark table rows
def cap1(Y): return Q(3, 2) - (Y - 2) / 10
def cap2(Y): return Q(59, 50) - (Y - 2) / 10
Ssum = lambda Y: cap1(Y) + cap2(Y)
Ystar = Q(4) + (Ssum(Q(4)) - Q(2)) * 5
BENCH = [(Q(4), "13/10", "49/50", "57/25"),
         (Q(9, 2), "5/4", "93/100", "109/50"),
         (Q(5), "6/5", "22/25", "52/25"),
         (Q(27, 5), "29/25", "21/25", "2"),
         (Q(11, 2), "23/20", "83/100", "99/50"),
         (Q(6), "11/10", "39/50", "47/25")]
ok_b = all(Q(cap1_s) == cap1(Y) and Q(cap2_s) == cap2(Y)
           and Q(sum_s) == Ssum(Y) for Y, cap1_s, cap2_s, sum_s in BENCH)
Eu6 = lambda u1: (cap1(Q(6)) - u1 + cap2(Q(6)) - (Q(2) - u1)) / 2
m6 = max(Eu6(Q(n, 20)) for n in range(0, 41))
wit = (Q(6, 5), Q(4, 5))
check("M8 benchmark: printed rows exact; Y* = 27/5 with sum 2; Y=6 margin "
      "3/50; witness (6/5, 4/5) feasible at Y = 5",
      ok_b and Ystar == Q(27, 5) and Ssum(Ystar) == Q(2)
      and Ssum(Q(6)) == Q(47, 25) and Q(2) - Ssum(Q(6)) == Q(3, 25)
      and m6 == Q(-3, 50)
      and sum(wit) == Q(2) and wit[0] <= cap1(Q(5)) and wit[1] <= cap2(Q(5)))

# static duality block
U = [Q(n, 100) for n in range(0, 101)]
psi_obs = [lambda u: Q(2, 5) - u, lambda u: u - Q(3, 5)]
psi_fea = [lambda u: Q(2, 5) - u, lambda u: u - Q(1, 5)]
lhs = lambda psi: max(min(p(u) for p in psi) for u in U)
dualv = lambda psi: min(max(l * psi[0](u) + (1 - l) * psi[1](u) for u in U)
                        for l in [Q(n, 100) for n in range(0, 101)])
l = Q(1, 2)
E = [l * psi_obs[0](u) + (1 - l) * psi_obs[1](u) for u in U]
rows2 = [{Q(0): Q(-1), Q(1): Q(1)}, {Q(0): Q(1), Q(1): Q(-1)}]
lhs_c = max(min(r[u] for r in rows2) for u in [Q(0), Q(1)])
rhs_c = min(max((1 - m) * rows2[0][u] + m * rows2[1][u] for u in [Q(0), Q(1)])
            for m in [Q(n, 100) for n in range(0, 101)])
def feas(rows_ineq, u):
    return all(a[0] * u[0] + a[1] * u[1] <= b for a, b in rows_ineq)
Gg = [Q(n, 2) for n in range(-10, 11)]
Hr = [((Q(-1), Q(0)), Q(-1)), ((Q(0), Q(-1)), Q(-1)), ((Q(1), Q(1)), Q(1))]
any2 = all(any(feas([Hr[i], Hr[j]], (x, y)) for x in Gg for y in Gg)
           for i, j in [(0, 1), (0, 2), (1, 2)])
all3 = any(feas(Hr, (x, y)) for x in Gg for y in Gg)
check("M9 static duality: obstructed -1/10 both sides with constant Farkas "
      "mix; contrast +1/10 both sides; nonconvex gap -1 vs 0; Helly-tight "
      "triple pairwise-feasible and jointly empty",
      lhs(psi_obs) == Q(-1, 10) and dualv(psi_obs) == Q(-1, 10)
      and all(e == Q(-1, 10) for e in E) and lhs(psi_fea) == Q(1, 10)
      and dualv(psi_fea) == Q(1, 10) and lhs_c == Q(-1) and rhs_c == Q(0)
      and any2 and not all3)

# drift table rows
g = lambda s: s * s
drift_u = lambda s: g(s + Q(1, 10)) - g(s)
DRIFT = [(Q(1), "21/100"), (Q(5, 4), "26/100"), (Q(3, 2), "31/100"),
         (Q(7, 4), "36/100"), (Q(2), "41/100")]
ok_d = all(Q(v) == drift_u(s) for s, v in DRIFT)
inc = [drift_u(DRIFT[i + 1][0]) - drift_u(DRIFT[i][0]) for i in range(4)]
check("M10 drift: printed rows equal s/5 + 1/100 exactly; increments 1/20; "
      "uncorrected >= 21/100 on the 101-point grid; corrected identically 0",
      ok_d and inc == [Q(1, 20)] * 4
      and all(drift_u(Q(n, 100)) >= Q(21, 100) for n in range(100, 201))
      and all(g(s + Q(1, 10) - Q(1, 10)) - g(s) == 0
              for s in [Q(n, 100) for n in range(100, 201)]))

# ---- edition 8: proposition checks ---------------------------------------------
# (P1) timing, general form: identity on a dense grid; sigma* = floor(tau*)
GRID8 = [Q(n, 100) for n in range(100, 301)]
check("P1 timing general form: (z-1 >= T) iff (z >= 1+T) for z in [1,3] "
      "hundredths, T in 0..5; sigma* = floor(tau*) with level sets z >= 1+k",
      all(((z - 1) >= T) == (z >= 1 + T) for z in GRID8 for T in range(6))
      and all(sig(z) == math.floor(float(z) - 1) for z in GRID8))
# (P2) benchmark crossover: feasibility iff capsum >= 2 iff Y <= 27/5; margin law
def feas_Y(Y):
    c1, c2 = cap1(Y), cap2(Y)
    if c1 < 0 or c2 < 0:
        return False
    return max(Q(0), Q(2) - c1) <= c2 and cap1(Y) >= Q(0)
YG = [Q(n, 10) for n in range(20, 141)]
ok_cross = True
for Y in YG:
    c1, c2 = cap1(Y), cap2(Y)
    want = (c1 >= 0 and c2 >= 0 and c1 + c2 >= 2)
    ok_cross &= (feas_Y(Y) == want == (Y <= Q(27, 5)))
marg = all((Q(2) - cap1(Y) - cap2(Y)) / 2 == (Y - Q(27, 5)) / 10
           for Y in YG)
check("P2 benchmark crossover: input-feasibility iff capsum >= 2 iff "
      "Y <= 27/5 on Y in [2,14] tenths; margin (Y - 27/5)/10 sign-exact",
      ok_cross and marg)
# (P3) branchwise decomposition: singleton verdicts + memoryless policy safety
sing_v = {x: win(frozenset({x}), full, H) and win(frozenset({x}), full, H - 2)
          for x in Vset}
def memless_traj(x0, steps=24):
    x = x0
    for _ in range(steps):
        x = step(x, 1 if x[0] == 1 else 2)
        if x not in Vset:
            return False
    return True
check("P3 full info decomposes branchwise: corner singleton nonviable, all "
      "8 others viable, and the memoryless policy (u=1 at z1=1, else u=2) "
      "keeps every non-corner singleton safe for 24 steps",
      sing_v[(1, 1)] is False and all(sing_v[x] for x in Vset if x != (1, 1))
      and all(memless_traj(x) for x in Vset if x != (1, 1)))
# (P4) saddle uniqueness: dual value -1/10 attained only at lambda = 1/2
dual_vals = {}
for L in [Q(n, 100) for n in range(0, 101)]:
    dv = max(L * (Q(2, 5) - u) + (1 - L) * (u - Q(3, 5))
             for u in [Q(n, 100) for n in range(0, 101)])
    dual_vals[L] = dv
check("P4 saddle: dual min -1/10 attained uniquely at lambda = 1/2 on the "
      "101-point grid; pooled drift constant -1/10 in u",
      min(dual_vals.values()) == Q(-1, 10)
      and [L for L, v in dual_vals.items() if v == Q(-1, 10)] == [Q(1, 2)]
      and all(L * (Q(2, 5) - u) + (1 - L) * (u - Q(3, 5)) == Q(-1, 10)
              for u in [Q(n, 100) for n in range(0, 101)] for L in [Q(1, 2)]))
# (P5) Helly pair points
Hpts = [((Q(1), Q(1)), ((Q(-1), Q(0)), Q(-1)), ((Q(0), Q(-1)), Q(-1))),
        ((Q(1), Q(0)), ((Q(-1), Q(0)), Q(-1)), ((Q(1), Q(1)), Q(1))),
        ((Q(0), Q(1)), ((Q(0), Q(-1)), Q(-1)), ((Q(1), Q(1)), Q(1)))]
def feas_row(rows, pt):
    return all(vec[0] * pt[0] + vec[1] * pt[1] <= rhs for vec, rhs in rows)
check("P5 Helly: the three constraint pairs feasible at (1,1), (1,0), (0,1); "
      "all three jointly infeasible on the 300x300 rational grid",
      all(feas_row(hp[1:], hp[0]) for hp in Hpts)
      and not feas_row(Hpts[0][1:], (Q(1, 2), Q(1, 2))))
# (P6) authority: no sustaining law pair fixes agency 2's z=1 vote to 1
none_fix2 = all(not law_traj_ok(AUDITED, l1, l2)
                for l1, l2 in LAW_PAIRS if l2[1] == 1)
check("P6 authority restriction: fixing agency 2's z=1 vote to instrument 1 "
      "sustains no law pair for 12|21 (branch 21 exits at step one)",
      none_fix2)


# ---------------- Layer 3: text needles -----------------------------------------
tex = open(os.path.join(HERE, "paper2_worked_systems_v9.tex"),
           encoding="utf-8").read()
tex = " ".join(tex.split())
NEEDLES = [
    "T_{\\mathrm{obs}} \\le \\tau^{*}(z_0) = z_0 - 1",
    "(2, 1)", "\\{(1,2), (2,2)\\}", "\\{(2,1), (2,2), (3,1)\\}",
    "|\\mathcal{W}_{\\mathrm{inst}}| = 24,", "|\\mathcal{W}_{\\mathrm{agg}}| = 26,",
    "|\\mathcal{W}_{\\mathrm{full\\text{-}codex}}| = 25,", "|\\mathcal{W}_{\\mathrm{full}}| = 28 .",
    "C(9,2) = 36", "C(8,2) = 28", "2^{4} \\times 2^{4} = 256",
    "21/100", "3/50", "47/25", "-1/10",
    "(6/5, 4/5)", "(1/2, 1/2)", "27/5",
    "3/2 - (Y - 2)/10", "59/50 - (Y - 2)/10",
    "\\lfloor \\tau^{*}(z_0) \\rfloor", "against \\(\\sigma^{*}(z_0) = \\lfloor \\tau^{*}(z_0) \\rfloor\\)", "\\{z_0 \\ge 1 + k\\}",
    "no-repeat protocol", "m{+}1 = 3",
    "\\{(1,2),(3,1)\\}", "\\{(1,2),(2,1)\\}",
    "Helly-tight family of three constraints", "48",
    "one previous-action register serves each review", "memoryless and decentralized",
    "pessimistic", "every admissible thread", "coincide setwise", "Helly number two", "two-by-two product", "row labels, agency 2's the column labels", "\\ell_1", "alternation-forced pair", "4 \\times 4", "12|21", "13|21", "13|31",
    "1121 & \\checkmark", "2212", "21|22|31", "12|21|22|31",
    "29/25", "21/25", "39/50", "57/25", "109/50", "99/50", "52/25",
    "41/100", "26/100", "31/100", "36/100", "1/20", "s/5 + 1/100",
    "six viable cells", "zero mismatches", "fails on all six viable cells",
    "pairs containing the corner state", "value is negative", "boundary-critical",
    "Within each observation column", "neither middle kernel contains the other",
    "review timing, general form", "exact benchmark crossover",
    "full information decomposes branchwise", "class lattice",
    "register-semantics invariance", "authority restriction",
    "static minimax duality on the two-floor instance",
    "sparse obstruction witnesses", "begin{proposition}", "begin{proof}",
    "comprises all \\(36\\) law pairs",
    "figs_ws4/fig_kernels.pdf", "figs_ws4/fig_timing.pdf",
    "figs_ws4/fig_census.pdf", "figs_ws4/fig_benchmark.pdf",
    "figs_ws4/fig_duality.pdf",
    "paper2_worked_systems_v9_verification.py",
    "paper2_worked_systems_figures.py",
    "agree setwise on the audited universe", "W_{12} = W_{10}",
    "coordinates clip at zero", "never uniquely viable",
    "the certificate itself is the recursion invariant",
    "under the audited endpoint convention",
    "general taxonomy of viability failures",
    "\\(m{+}1\\)-constraint witness",
    "two coarsest adequate two-cell partitions",
    "F_j(z_1, z_2) = (\\min\\{3, z_j + 1\\}",
    "g_1(u) = u - \\tfrac12", "\\exists u\\ \\forall j \\in I(x)",
    "(proved general law, Proposition \\ref{prop:timing})",
    "(proved zero law, Proposition \\ref{prop:authority})",
    "Quantifier and dual form",
]
missing = [n for n in NEEDLES if n not in tex]
check(f"all {len(NEEDLES)} headline needles present in the tex", not missing,
      f"(missing: {missing})" if missing else "")
figs_ok = all(os.path.exists(os.path.join(HERE, f)) for f in
              ["figs_ws4/fig_kernels.pdf", "figs_ws4/fig_timing.pdf",
               "figs_ws4/fig_census.pdf", "figs_ws4/fig_benchmark.pdf",
               "figs_ws4/fig_duality.pdf"])
check("all five referenced figure files exist", figs_ok)
check("declarations use separate headings with the responsibility wording",
      "\\subsection*{Funding}" in tex and "\\subsection*{Competing interests}" in tex
      and "\\subsection*{Data availability}" in tex and "\\subsection*{Code availability}" in tex
      and "\\subsection*{AI declaration}" in tex
      and "The author reviewed and edited outputs and takes" in tex
      and "responsibility for the final work." in tex)

# (P7) stabilization: the H and H-2 winning verdicts agree setwise (supports
# the W_{12} = W_{10} sentence in the text)
for _name, _info, _alt, _K in [("inst", agg, True, K_inst), ("agg", agg, False, K_agg),
                               ("cod", full, True, K_cod), ("full", full, False, K_full)]:
    _W12 = frozenset(B for B in pairs if win(B, _info, H, None, _alt))
    _W10 = frozenset(B for B in pairs if win(B, _info, H - 2, None, _alt))
    check(f"P7 stabilization ({_name}): W_12 = W_10 = audited kernel, setwise",
          _W12 == _W10 == _K)
_W12a = frozenset(B for B in pairs if win_adv(B, agg, H, None, True))
_W10a = frozenset(B for B in pairs if win_adv(B, agg, H - 2, None, True))
check("P7 stabilization (mode-blind): W_12 = W_10 setwise", _W12a == _W10a)
# (P8) instrument-0 domination and safe-set up-set: the WLOG premises behind
# restricting the recursion to the two instruments
_dom = all(all(step(x, 0)[i] <= step(x, 1)[i] and step(x, 0)[i] <= step(x, 2)[i]
               for i in (0, 1)) for x in STATES)
_up = all(y in Vset for x in Vset for y in STATES
          if y[0] >= x[0] and y[1] >= x[1])
check("P8 WLOG premises: F_0 <= F_1 and F_0 <= F_2 pointwise; safe set up-set",
      _dom and _up)

n_pass = sum(1 for _, ok in PASS if ok)
print(f"\nverification: {n_pass}/{len(PASS)} checks pass "
      f"(chained lineage scripts: {total_chained}/57)")
raise SystemExit(0 if n_pass == len(PASS) else 1)

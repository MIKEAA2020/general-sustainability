#!/usr/bin/env python3
"""
Worked-systems audit, edition 5 — verification.

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
paper2_worked_systems_v5.tex, the separate declaration headings, the
responsibility wording, and the five figure files.

Exact rational/integer arithmetic; stdlib only; deterministic.
Run: python3 paper2_worked_systems_v4_verification.py
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

# ---------------- Layer 3: text needles -----------------------------------------
tex = open(os.path.join(HERE, "paper2_worked_systems_v5.tex"),
           encoding="utf-8").read()
tex = " ".join(tex.split())
NEEDLES = [
    "T_{\\mathrm{obs}} \\le \\sigma^{*}(z_0) = z_0 - 1",
    "(2, 1)", "\\{(1,2), (2,2)\\}", "\\{(2,1), (2,2), (3,1)\\}",
    "|\\mathcal{W}_{\\mathrm{inst}}| = 24,", "|\\mathcal{W}_{\\mathrm{agg}}| = 26,",
    "|\\mathcal{W}_{\\mathrm{full\\text{-}codex}}| = 25,", "|\\mathcal{W}_{\\mathrm{full}}| = 28 .",
    "C(9,2) = 36", "C(8,2) = 28", "2^{4} \\times 2^{4} = 256",
    "21/100", "3/50", "47/25", "-1/10",
    "(6/5, 4/5)", "(1/2, 1/2)", "27/5",
    "3/2 - (Y - 2)/10", "59/50 - (Y - 2)/10", "\\Delta x_1(Y) = Y - 4",
    "\\lfloor z_0 - 1 \\rfloor", "\\{z_0 \\ge 1 + k\\}",
    "no-repeat protocol", "m{+}1 = 3",
    "\\{(1,2),(3,1)\\}", "\\{(1,2),(2,1)\\}",
    "Helly-tight triple", "48",
    "alternation-forced pair", "single previous-action register", "4 \\times 4", "12|21", "13|21", "13|31",
    "1121 & \\checkmark", "2212", "21|22|31", "12|21|22|31",
    "29/25", "21/25", "39/50", "57/25", "109/50", "99/50", "52/25",
    "41/100", "26/100", "31/100", "36/100", "1/20", "s/5 + 1/100",
    "six viable cells", "zero mismatches",
    "figs_ws4/fig_kernels.pdf", "figs_ws4/fig_timing.pdf",
    "figs_ws4/fig_census.pdf", "figs_ws4/fig_benchmark.pdf",
    "figs_ws4/fig_duality.pdf",
    "paper2_worked_systems_v5_verification.py",
    "paper2_worked_systems_figures.py",
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

n_pass = sum(1 for _, ok in PASS if ok)
print(f"\nverification: {n_pass}/{len(PASS)} checks pass "
      f"(chained lineage scripts: {total_chained}/57)")
raise SystemExit(0 if n_pass == len(PASS) else 1)

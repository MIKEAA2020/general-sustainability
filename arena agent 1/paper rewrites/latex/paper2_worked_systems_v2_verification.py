#!/usr/bin/env python3
"""
Worked-systems audit, edition 2 — verification.

Layer 1 (chain): runs the per-system verification scripts of the companion
archive as subprocesses and asserts each exits green (8+8+9+8+8+8+8 = 57
checks).
Layer 2 (own): recomputes the headline identities from the shared audit
system's primitives — the pair family, the codex-threaded winning recursion
(no-repeat threaded as a parameter), the partition census, the benchmark
caps, the CE drift bounds, and the delay identity — independently of the
per-system scripts.
Layer 3 (text): asserts every headline number printed in
paper2_worked_systems_v2.tex.

Exact rational/integer arithmetic; stdlib only; deterministic.
Run: python3 paper2_worked_systems_v2_verification.py
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
pairs = [frozenset({x, y}) for x in Vset for y in Vset if x < y]
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

# ---------------- Layer 2a: the headline identities, recomputed ------------------
corner = not verd(frozenset({(1, 1)}), lambda x: x)
agg, full = lambda x: x[0] + x[1], lambda x: x
v_inst = [verd(B, agg, alt=True) for B in pairs]
v_part = [verd(B, agg) for B in pairs]
v_falt = [verd(B, full, alt=True) for B in pairs]
v_full = [verd(B, full) for B in pairs]
inst_set = frozenset(B for B, a in zip(pairs, v_inst) if a)
part_set = frozenset(B for B, a in zip(pairs, v_part) if a)
falt_set = frozenset(B for B, a in zip(pairs, v_falt) if a)
full_set = frozenset(B for B, a in zip(pairs, v_full) if a)
check("M1 pair family 36; corner singleton nonviable; top kernel = 28 pairs avoiding the corner",
      len(pairs) == 36 and corner
      and full_set == frozenset(B for B in pairs if (1, 1) not in B))
check("M2 four-cell counts (24, 26, 25, 28) with meet of middles = institutional setwise",
      (sum(v_inst), sum(v_part), sum(v_falt), sum(v_full)) == (24, 26, 25, 28)
      and (part_set & falt_set) == inst_set)

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
ALLP = [tuple(tuple(sorted(F)) for F in P) for P in partitions(TARGET)]
def inter_R(F):
    s = set(R(F[0]))
    for x in F[1:]:
        s &= set(R(x))
    return s
adm = [P for P in ALLP if all(inter_R(F) for F in P)]
max_sets = [frozenset({(1, 2), (2, 2)}), frozenset({(2, 1), (2, 2), (3, 1)})]
check("M3 15 partitions, 7 admissible; maximal common-action sets overlap in (2,2)",
      len(ALLP) == 15 and len(adm) == 7
      and max_sets[0] & max_sets[1] == {(2, 2)})

def cap1(Y): return Q(3, 2) - (Y - 2) / 10
def cap2(Y): return Q(59, 50) - (Y - 2) / 10
Ssum = lambda Y: cap1(Y) + cap2(Y)
Ystar = Q(4) + (Ssum(Q(4)) - Q(2)) * 5
lam = Q(1, 2)
Eu = lambda u: lam * (cap1(Q(6)) - u[0]) + (1 - lam) * (cap2(Q(6)) - u[1])
m6 = max(Eu((Q(n, 10), Q(2) - Q(n, 10))) for n in range(0, 21))
check("M4 benchmark: Y* = 27/5 with cap sum 2; Y=6 sum 47/25; dual margin 3/50",
      Ystar == Q(27, 5) and Ssum(Ystar) == Q(2)
      and Ssum(Q(6)) == Q(47, 25) and m6 == Q(-3, 50))

g = lambda s: s * s
drift_u = lambda s: g(s + Q(1, 10)) - g(s)
drift_c = lambda s: g(s + Q(1, 10) - Q(1, 10)) - g(s)
check("M5 CE convention: uncorrected drift >= 21/100 on [1,2]; corrected identically zero",
      all(drift_u(Q(n, 100)) >= Q(21, 100) for n in range(100, 201))
      and all(drift_c(Q(n, 100)) == 0 for n in range(100, 201)))

GRID = [Q(n, 10) for n in range(10, 26)]
le_bad = [(z, T) for z in GRID for T in (1, 2, 3)
          if ((z - 1) >= T) != (z >= 1 + T)]
strict_bad = [(z, T) for z in GRID for T in (1, 2, 3)
              if ((z - 1) > T) != (z >= 1 + T)]
c7 = all(math.floor(float(z) - 1) == max(k for k in range(0, 4) if z >= 1 + k)
         for z in GRID)
check("M6 delay identity on 48 cells (zero mismatches); strict fails exactly at (2,1); sigma* = floor(z0-1)",
      not le_bad and strict_bad == [(Q(2), 1)] and c7)

# ---------------- Layer 3: text needles -----------------------------------------
tex = open(os.path.join(HERE, "paper2_worked_systems_v2.tex"), encoding="utf-8").read()
tex = " ".join(tex.split())
NEEDLES = [
    "T_{\\mathrm{obs}} \\le \\sigma^{*}(z_0) = z_0 - 1",
    "(2, 1)", "\\{(1,2), (2,2)\\}", "\\{(2,1), (2,2), (3,1)\\}",
    "= 24,", "= 26,", "= 25,", "= 28 .",
    "C(9,2) = 36", "C(8,2) = 28", "2^{4} \\times 2^{4} = 256",
    "21/100", "3/50", "47/25", "-1/10",
    "(6/5, 4/5)", "(1/2, 1/2)", "27/5",
    "3/2 - (Y - 2)/10", "59/50 - (Y - 2)/10", "\\Delta x_1(Y) = Y - 4",
    "\\lfloor z_0 - 1 \\rfloor", "\\{z_0 \\ge 1 + k\\}",
    "no-repeat protocol", "m{+}1 = 3",
    "\\{(1,2),(3,1)\\}", "\\{(1,2),(2,1)\\}",
    "Helly-tight triple", "17" if False else "48",
]
missing = [n for n in NEEDLES if n not in tex]
check(f"all {len(NEEDLES)} headline needles present in the tex", not missing,
      f"(missing: {missing})" if missing else "")
check("declarations carry the AI line and the master script name",
      "GLM (Z.ai), Qwen (Alibaba Cloud) and DeepSeek AI" in tex
      and "paper2_worked_systems_v2_verification.py" in tex)

n_pass = sum(1 for _, ok in PASS if ok)
print(f"\nverification: {n_pass}/{len(PASS)} checks pass "
      f"(chained lineage scripts: {total_chained}/57)")
raise SystemExit(0 if n_pass == len(PASS) else 1)

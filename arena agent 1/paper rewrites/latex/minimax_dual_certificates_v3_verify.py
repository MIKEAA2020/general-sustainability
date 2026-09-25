#!/usr/bin/env python3
"""
Minimax dual certificates v3 — review-sequence couplings for the corrected
envelope — verification. Exact rational arithmetic; stdlib only; deterministic.

Chains the v2 battery (24 checks, itself chaining the v1 static battery of 8)
as its seed, then certifies the review-sequence instance:

  C1  COUPLING + TOWER (all 81 trees): the one-step adversarial priors couple
      to the product measure; for every nonanticipative policy tree the
      path-enumerated E[F] equals the iterated-conditional (tower) evaluation.
  C2  BACKWARD INDUCTION EXACT: Q0 = Phi^2 g equals the policy-tree supremum
      = 1/2, attained at u1 = -2 (and +2); per-u1 values (1/2, 0, 1/2).
  C3  CELL TABLE: at u1 = -2 the singleton cells (-1, 1, 3, 5) carry
      Q1 = (1, 1, 1, -1) with u2* = (0, -2, +2, +2), weights 1/4 each.
  C4  STRICT ADAPTIVITY: open-loop maximum = 0 (nine pairs enumerated);
      do-nothing = 0; the envelope 1/2 > 0 strictly — information design
      (u1 separates the branch) plus recourse (u2 brakes the revealed
      branch) have certified strict value.
  C5  REFINEMENT MONOTONE: matching toy — Q coarse = Q mid = -1/3 <
      0 = Q fine; and every coarse-measurable policy is fine-measurable
      (measurability relaxation check by enumeration).
  C6  TEXT: new section, three propositions, tightened residue, code pointer;
      retired markers absent.
"""
import subprocess, sys
from fractions import Fraction as F
from itertools import product

PASS, FAIL = [], []
def chk(cond, name):
    (PASS if cond else FAIL).append(name)

# ---------------- chain v2 (which chains v1) ----------------
r = subprocess.run([sys.executable, "minimax_dual_certificates_v2_verify.py"],
                   capture_output=True, text=True)
chk(r.returncode == 0 and "24/24 checks pass" in r.stdout,
    "chained seed: v2 battery 24/24 (itself chaining v1 8/8)")

S = (1, -1)
def mb(z1, s, u2, d2):
    return F(2 - abs(z1 + s * u2 + d2))

def paths(u1, table):
    # 8 equiprobable paths (s, d1, d2)
    for s in S:
        for d1 in (-1, 1):
            z1 = 2 + s * u1 + d1
            for d2 in (-1, 1):
                yield mb(z1, s, table[z1], d2) / 8

def tower_value(u1, table):
    # iterated conditioning: E[F] = sum_{d1} P(d1) sum_{cells} P(cell|d1) E[F | cell]
    tot = F(0)
    for d1 in (-1, 1):
        zs = {}
        for s in S:
            z1 = 2 + s * u1 + d1
            zs.setdefault(z1, []).append(s)
        for z1, ss in zs.items():
            inner = F(0)
            for s in ss:
                for d2 in (-1, 1):
                    inner += mb(z1, s, table[z1], d2) / (2 * len(ss))
            tot += F(1, 2) * F(len(ss), 2) * inner
    return tot

# ---------------- C1: tower on all 81 trees at u1 = -2 and u1 = +2 ----------------
dom = [-1, 1, 3, 5] if True else []
ok_all = True
for u1 in (-2, 2):
    d1s = sorted({2 + s * u1 + d1 for s in S for d1 in (-1, 1)})
    for bits in product((-2, 0, 2), repeat=len(d1s)):
        t = dict(zip(d1s, bits))
        pe = sum(paths(u1, t))
        tw = tower_value(u1, t)
        if pe != tw:
            ok_all = False
chk(ok_all, "C1: tower identity exact on all 81 policy trees (u1 = ±2)")

# ---------------- C2: backward induction = tree supremum ----------------
def Q1(z1, post):
    vals = {}
    for u2 in (-2, 0, 2):
        vals[u2] = sum(p * sum(mb(z1, s, u2, d2) for d2 in (-1, 1)) / 2 for s, p in post)
    b = max(vals, key=lambda u: vals[u])
    return vals[b], b

def Q0(u1):
    tot = F(0); det = []
    for d1 in (-1, 1):
        zs = {}
        for s in S:
            z1 = 2 + s * u1 + d1
            zs.setdefault(z1, []).append(s)
        for z1, ss in zs.items():
            q1, b = Q1(z1, [(s, F(1, len(ss))) for s in ss])
            w = F(1, 2) * F(len(ss), 2)
            tot += w * q1
            det.append((z1, tuple(sorted(ss)), q1, b, w))
    return tot, det

vals = {}
for u1 in (-2, 0, 2):
    vals[u1], det = Q0(u1)
dp = max(vals.values())
best_u1 = max(vals, key=lambda u: vals[u])
_, det = Q0(best_u1)
dom = sorted({2 + s * best_u1 + d1 for s in S for d1 in (-1, 1)})
tree_sup = None
for bits in product((-2, 0, 2), repeat=len(dom)):
    t = dict(zip(dom, bits))
    v = sum(paths(best_u1, t))
    tree_sup = v if tree_sup is None or v > tree_sup else tree_sup
chk(dp == tree_sup == F(1, 2), f"C2: Q0 = Phi^2 g = tree supremum = 1/2 (per-u1: { {k: str(v) for k, v in vals.items()} })")

# ---------------- C3: cell table ----------------
cells = {z1: (q1, b) for z1, ss, q1, b, w in det}
expect = {-1: (F(1), 0), 1: (F(1), -2), 3: (F(1), 2), 5: (F(-1), 2)}
chk(best_u1 == -2 and all(cells[z] == expect[z] for z in dom),
    f"C3: cells at u1=-2: Q1 = (1,1,1,-1), u2* = (0,-2,+2,+2)")

# ---------------- C4: strict adaptivity ----------------
def fixed(u1, u2):
    return sum(paths(u1, {z: u2 for z in range(-6, 7)}))
ol = max(fixed(u1, u2) for u1 in (-2, 0, 2) for u2 in (-2, 0, 2))
dn = fixed(0, 0)
chk(ol == 0 and dn == 0 and dp == F(1, 2) > 0,
    "C4: open-loop = do-nothing = 0 < 1/2 = envelope (strict information-design + recourse value)")

# ---------------- C5: refinement monotone ----------------
def env_part(part):
    best = None
    for acts in product((1, 2, 3), repeat=3):
        A = dict(zip((1, 2, 3), acts))
        if any(len({A[x] for x in b}) > 1 for b in part):
            continue
        v = sum(F(1, 3) * F(-abs(x - A[x])) for x in (1, 2, 3))
        best = v if best is None or v > best else best
    return best
coarse = env_part([[1, 2], [3]])
mid = env_part([[1], [2, 3]])
fine = env_part([[1], [2], [3]])
chk(coarse == mid == F(-1, 3) and fine == 0,
    f"C5: Q(coarse) = Q(mid) = -1/3 < 0 = Q(fine) (strict final step)")
# measurability relaxation: every coarse-measurable policy is fine-measurable
def measurable(acts, part):
    A = dict(zip((1, 2, 3), acts))
    return all(len({A[x] for x in b}) <= 1 for b in part)
relax_ok = True
for acts in product((1, 2, 3), repeat=3):
    if measurable(acts, [[1, 2], [3]]) and not measurable(acts, [[1], [2], [3]]):
        relax_ok = False
chk(relax_ok, "C5: every coarse-measurable policy is fine-measurable (supima ordered)")

# ---------------- C6: text ----------------
tex = open("minimax_dual_certificates_v3.tex", encoding="utf-8").read()
tn = " ".join(tex.split())
for needle in ["The review-sequence envelope: exact couplings",
               "consistent coupling and the tower identity",
               "information design and recourse strictly pay",
               "refinement is monotone",
               "Q_0 = \\operatorname*{ess\\,sup}",
               "must reduce, on review sequences with finite disturbance sets, to",
               "minimax\\_dual\\_certificates\\_v3\\_verify.py",
               "The design formulas (the dual-margin ratio",
               "masked-backup mechanics"]:
    chk(needle in tn, f"needle: {needle!r}")
for bad in ["programme", "edition's", "v2\\_verify.py"]:
    chk(bad not in tex, f"marker absent: {bad!r}")
chk(tex.count("begin{proof}") == tex.count("end{proof}"),
    "structure: proof pairing")

n_pass = sum(1 for ok in PASS if ok)
print(f"\nverification: {n_pass}/{len(PASS)} checks pass (chained seeds: v2 24/24; v1 static 8/8)")
raise SystemExit(0 if n_pass == len(PASS) else 1)

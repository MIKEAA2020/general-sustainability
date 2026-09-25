#!/usr/bin/env python3
"""
Exact belief-state computation at scale — edition 1 verification.

Re-derives every claim of paper2_exact_belief_computation_v1.tex in exact
rational arithmetic (standard library only): the finite-horizon blind value
table by definition-level trajectory enumeration (k = 1, 2, 3, 6; twelve
levels); the maximal jointly survivable parameter sets by two- and
three-periodic policy search with 60-step certificates (antichain filtering);
the averaging obstruction (every control's drifts sum to -1/5 per step over
the four cells; no 3-periodic policy keeps all four cells alive from z = 2.1);
the observation ladder (one theta1 probe: value 1 for z >= 1.1, 1/2 at the
edge; fully observed 1 everywhere); exact point-based evaluation (alpha-set
evaluation at seven probed rational beliefs equals per-belief trajectory
enumeration; the k = 6 alpha-set deduplicates 15,625 sequences); and the
compression census (48 stored maximal sets in place of 180 raw subset
evaluations).
"""
import os
import re
import sys
import random
from fractions import Fraction as Q
from itertools import product

HERE = os.path.dirname(os.path.abspath(__file__))
PASS = []


def check(name, ok, detail=""):
    PASS.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + (f" ({detail})" if detail else ""))


ZL = [Q(i, 10) for i in range(10, 22)]
THS = list(product((1, -1), (1, -1)))
ACTS = [(1, 1), (-1, -1), (1, -1), (-1, 1), (0, 0)]
W = Q(1, 4)


def drift(u, th):
    return Q(-1, 10) + Q(1, 5) * (u[0] * th[0] + u[1] * th[1])


def survives(seq, th, z, k):
    zz = z
    if zz < 1:
        return False
    for t in range(k):
        zz += drift(seq[t % len(seq)], th)
        if zz < 1:
            return False
    return True


# (1) finite-horizon blind table by definition-level enumeration
def V_blind(z, k):
    best = Q(0)
    for seq in product(ACTS, repeat=k):
        tot = Q(0)
        for th in THS:
            if survives(seq, th, z, k):
                tot += W
        best = max(best, tot)
    return best


tab = {}
for z in ZL:
    for k in (1, 2, 3, 6):
        tab[(z, k)] = V_blind(z, k)
v6_ok = (tab[(Q(10, 10), 6)] == Q(1, 4)
         and all(tab[(z, 6)] == Q(1, 2) for z in ZL if Q(11, 10) <= z <= Q(15, 10))
         and all(tab[(z, 6)] == Q(1) for z in ZL if z >= Q(16, 10)))
mono = all(tab[(z, k1)] >= tab[(z, k2)] for z in ZL
           for k1, k2 in ((1, 2), (2, 3), (3, 6)))
check("finite-horizon table exact (definition enumeration): V_6 = 1/4 at "
      "1.0, 1/2 on 1.1..1.5, 1 on 1.6..2.1; monotone nonincreasing in k",
      v6_ok and mono,
      f"V6: " + ",".join(str(tab[(z, 6)]) for z in ZL))

# (2) maximal jointly survivable sets (2- and 3-periodic policies, 60-step)
SEQS = [s for p in (1, 2, 3) for s in product(ACTS, repeat=p)]


def maxsets(z):
    S = set()
    for seq in SEQS:
        kept = frozenset(th for th in THS if survives(seq, th, z, 60))
        if kept:
            S.add(kept)
    return {s for s in S if not any(s < t for t in S)}


NAMES = {(1, 1): "++", (-1, -1): "--", (1, -1): "+-", (-1, 1): "-+"}
M = {z: maxsets(z) for z in ZL}
singles = (len(M[Q(10, 10)]) == 4
           and all(len(s) == 1 for s in M[Q(10, 10)]))
COORD = {frozenset({(1, 1), (1, -1)}), frozenset({(1, 1), (-1, 1)}),
         frozenset({(-1, -1), (1, -1)}), frozenset({(-1, -1), (-1, 1)})}
pairs = all(M[z] == COORD for z in ZL if z >= Q(11, 10))
lim_ok = all(max(sum(W for _ in s) for s in M[z])
             == (Q(1, 4) if z == Q(10, 10) else Q(1, 2)) for z in ZL)
check("maximal survivable sets: four singletons at 1.0; exactly the four "
      "coordinate pairs at every z >= 1.1 (antichain); kernel limits 1/4 "
      "and 1/2 by band", singles and pairs and lim_ok)

# (3) averaging obstruction + quadruple impossibility
sums_ok = all(sum(drift(u, th) for th in THS) == Q(-2, 5) for u in ACTS)
none4 = not any(all(survives(s, th, Q(21, 10), 60) for th in THS)
                for s in SEQS)
check("averaging obstruction: every control's drifts sum to -2/5 per step "
      "over the four cells; no 3-periodic policy keeps all four cells alive "
      "from z0 = 2.1 (60-step certificates)", sums_ok and none4)

# (4) observation ladder: post-probe the controller maximizes expected
# survival over the two-cell posterior support (one probe of theta1)
def V_probe1(z, k):
    tot = Q(0)
    for t1 in (1, -1):
        best = Q(0)
        for seq in product(ACTS, repeat=min(k, 6)):
            a = 1 if survives(seq, (t1, 1), z, k) else 0
            b = 1 if survives(seq, (t1, -1), z, k) else 0
            best = max(best, Q(a + b, 2))
        tot += Q(1, 2) * best
    return tot


p6 = {z: V_probe1(z, 6) for z in ZL}
ladder = (p6[Q(10, 10)] == Q(1, 2)
          and all(p6[z] == Q(1) for z in ZL if z >= Q(11, 10)))
# post-probe support survivability from 1.1 (indefinite, periodic search)
pair_ok = any(survives(s, (1, 1), Q(11, 10), 60)
              and survives(s, (1, -1), Q(11, 10), 60) for s in SEQS)
check("observation ladder: one theta1 probe reaches 1 for every "
      "z >= 1.1 and 1/2 at the edge (one cell of the pair kept alive); "
      "the post-probe coordinate pair is jointly survivable from 1.1",
      ladder and pair_ok)

# (5) exact point-based evaluation at probed beliefs
rnd = random.Random(12)
beliefs = []
while len(beliefs) < 7:
    a, b, c = (rnd.randint(0, 10), rnd.randint(0, 10), rnd.randint(0, 10))
    d = 10 - a - b - c
    if d > 0:
        beliefs.append((Q(a, 10), Q(b, 10), Q(c, 10), Q(d, 10)))
# alpha-set at horizon k: deduplicated indicator vectors over the cells
def alpha_set(k, z):
    raw = 0
    vecs = set()
    for seq in product(ACTS, repeat=k):
        raw += 1
        vecs.add(tuple(1 if survives(seq, th, z, k) else 0
                       for th in THS))
    return raw, vecs


raw6, vecs6 = alpha_set(6, Q(21, 10))
ok_pb = True
raws = {}
for z in (Q(11, 10), Q(16, 10), Q(21, 10)):
    for k in (1, 3, 6):
        raw, vs = alpha_set(k, z)
        raws[(z, k)] = raw
        for bl in beliefs:
            v_alpha = max(sum(bi * vi for bi, vi in zip(bl, v)) for v in vs)
            v_bf = max(
                sum(bi * (1 if survives(seq, th, z, k) else 0)
                    for bi, th in zip(bl, THS))
                for seq in product(ACTS, repeat=min(k, 6)))
            ok_pb &= (v_alpha == v_bf)
check("exact point-based evaluation: alpha-set values at 7 probed rational "
      "beliefs x 3 levels x 3 horizons equal per-belief trajectory "
      f"enumeration; k = 6 alpha-set deduplicates {raw6} sequences to "
      f"{len(vecs6)} witness vectors", ok_pb and all(r == 5 ** k for (z2, k), r in raws.items())
      and len(vecs6) <= 16, f"D={len(vecs6)}")

# (6) compression census
raw = sum(2 ** 4 - 1 for _ in ZL)
comp = sum(len(M[z]) for z in ZL)
check("compression census: 48 stored maximal sets in place of 180 raw "
      "subset evaluations", raw == 180 and comp == 48, f"{raw}->{comp}")

# ---------------- text needles, structure, hygiene -----------------
tex = open(os.path.join(HERE, "paper2_exact_belief_computation_v1.tex"),
           encoding="utf-8").read()
tnorm = " ".join(tex.split())
NEEDLES = [
    "Exact Belief-State Computation at Scale",
    "48 augmented states 12 stock levels against the floor",
    "five controls", "no floating point anywhere",
    "with two compression disciplines",
    "48 stored sets in place of 180 raw subset evaluations across the",
    "the four coordinate pairs", "nothing larger, ever",
    "Every control's drifts over the four parameter cells sum to",
    "-2/5 per step",
    "keeps all four parameter cells safe indefinitely",
    "certifies at 60 steps",
    "the indefinite-horizon kernel at the uniform belief is 1/2 for",
    "every z_0 >= 1.1 and 1/4 at the edge",
    "one well-chosen probe exhausts the value of observation",
    "the second parameter is worth nothing once the first",
    "V_6 b_0 = 1/4", "1/2 on 1.1 through 1.5",
    "seven probed rational beliefs",
    "definition-level trajectory enumeration",
    "48 stored sets, 180 raw by counting",
    "the antichain representation", "September 26, 2026",
]
import re as _re
def _n(s):
    z = _re.sub(r"\\tfrac\{(\d+)\}\{(\d+)\}", r"\1/\2", s)
    z = _re.sub(r"\\tfrac(\d)(\d)", r"\1/\2", z)
    z = z.replace("\\(", " ").replace("\\)", " ")
    z = z.replace("\\[", " ").replace("\\]", " ")
    z = z.replace("\\ge", " >= ").replace("\\le", " <= ")
    z = z.replace("\\times", " x ")
    z = _re.sub(r"\\[a-zA-Z]+", " ", z)
    for ch in "()[]{}":
        z = z.replace(ch, " ")
    z = z.replace("_ ", "_")
    return " ".join(z.split())
missing = [n for n in NEEDLES if _n(n) not in _n(tnorm)]
check(f"all {len(NEEDLES)} headline needles present in the tex", not missing,
      f"(missing: {missing})" if missing else "")

check("declarations use separate headings with the responsibility wording",
      "\\subsection*{Funding}" in tex and "\\subsection*{AI declaration}" in tex
      and "The author reviewed and edited outputs and takes responsibility "
          "for the final work." in tnorm)

check("code pointer: the verification script named exactly once",
      tnorm.count("paper2_exact_belief_computation_v1_verification.py") == 1)

labels = re.findall(r"\\label\{([^}]+)\}", tex)
refs = set(re.findall(r"\\ref\{([^}]+)\}", tex))
dupl = [l for l in set(labels) if labels.count(l) > 1]
check("label/ref integrity", not dupl and refs <= set(labels),
      f"dupl={dupl} undef={sorted(refs - set(labels))}"
      if (dupl or refs - set(labels)) else "")

raw_tex = open(os.path.join(HERE, "paper2_exact_belief_computation_v1.tex"),
               "rb").read()
hyg = (all(b >= 32 or b == 10 for b in raw_tex)
       and re.search(r"(?![\\a-zA-Z])ef\{", raw_tex.decode()) is None
       and re.search(r"(?![\\a-zA-Z])exttt\{", raw_tex.decode()) is None)
check("source hygiene", bool(hyg))

n_pass = sum(1 for _, ok in PASS if ok)
print(f"\nverification: {n_pass}/{len(PASS)} checks pass")
sys.exit(0 if n_pass == len(PASS) else 1)

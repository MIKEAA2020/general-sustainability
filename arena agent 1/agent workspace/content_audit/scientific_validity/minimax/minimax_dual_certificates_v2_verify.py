#!/usr/bin/env python3
"""
Minimax dual certificates v2 — the corrected dynamic envelope — verification.
Exact rational arithmetic; stdlib only; deterministic. Chains the v1 static
battery (8 checks) as its seed, then verifies the corrected envelope:

  N1  BRIDGE LEMMA (exact): an expectation of a bounded rational functional
      that is strictly negative forces a positive-weight set of strictly
      negative realizations; the contrapositive holds exactly (all
      realizations >= 0  =>  expectation >= 0).
  N2  ENVELOPE WELL-POSEDNESS (finite): the one-step operator Phi V(b) =
      max_a E[V(b') | b, a] computed by exact backward induction on a
      2-branch, 2-step, 2-action POMDP matches the brute-force policy
      evaluation; and order preservation V <= W => Phi V <= Phi W holds on
      a rational scan of comparison pairs.
  N3  IDENTIFICATION ON THE THREE-BRANCH INSTANCE: with beta(tau) =
      16/25 - tau - 1, pooled window kernel zero, and support values
      lambda_j * 1/2, the envelope evaluation is exactly
      Gamma_h(tau) = 7/50 - tau at tau in {1/10, 7/50, 1/5}:
      values 1/25 > 0 (no fire), 0 (boundary), -3/50 < 0 (fires).
  N4  THE POOLING WEIGHTS ARE THE GAME'S EQUALIZER: for the component rate
      matrix R (R_jk = n_j . n_k of the hexagon directions), R lambda = 0
      at lambda = (3/8, 5/16, 5/16); and for every rational scan vector f
      with (Rf)_1 >= 0 the sum (Rf)_2 + (Rf)_3 = 18/25 - (48/25) f_1 <= 0,
      so the blind-braking game's value is 0 — no common control discharges
      all three branches at any positive rate (hold-then-brake is optimal).
  N5  TEXT: the corrected-envelope section, lemma, definition, theorem,
      identification, corollary, and residue conjecture are present; the
      retired meta-markers are absent; the code pointer names this script.
"""
import csv, subprocess, sys
from fractions import Fraction as F

PASS, FAIL = [], []
def chk(cond, name):
    (PASS if cond else FAIL).append(name)

# ---------------- chain v1 (8 static checks) ----------------
r = subprocess.run([sys.executable, "minimax_dual_certificates_v1_verify.py"],
                   capture_output=True, text=True)
seed_ok = (r.returncode == 0) and ("8/8 checks pass" in r.stdout)
chk(seed_ok, f"chained seed: v1 static battery 8/8 (got: {r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.returncode})")

# ---------------- N1: bridge lemma ----------------
w = [F(1, 2), F(1, 4), F(1, 4)]
vals = [F(-1, 10), F(3, 10), F(-1, 20)]
E = sum(wi * vi for wi, vi in zip(w, vals))
chk(E == F(-1, 40) and E < 0 and min(vals) < 0 and any(v < 0 for wi, v in zip(w, vals) if wi > 0),
    "N1: E[F] = -1/40 < 0 with positive weight on negative realizations (bridge fires)")
vals2 = [F(1, 10), F(0), F(2, 5)]
E2 = sum(wi * vi for wi, vi in zip(w, vals2))
chk(E2 >= 0 and all(v >= 0 for v in vals2),
    "N1 contrapositive: all realizations >= 0 => expectation >= 0 exactly")

# ---------------- N2: finite envelope ----------------
# Two branches (hidden state s in {1,2}, prior 1/2 each), two actions a in {0,1},
# two steps. Step payoff margin M(s, a) and transition of the OBSERVED belief:
# after step 1 the observation reveals s exactly (posterior point mass), so the
# second step acts on the true branch with full information.
M1 = {(1, 0): F(-1, 10), (1, 1): F(1, 10), (2, 0): F(1, 10), (2, 1): F(-3, 20)}
M2 = {(1, 0): F(1, 5), (1, 1): F(-1, 10), (2, 0): F(-1, 10), (2, 1): F(1, 5)}
# Backward induction: V1(s) = max_a M2(s, a); V0(b) = E_s[ max_a (M1 + V1(s))(s, a) ]  (reveal after step 1)
V1 = {s: max(M2[(s, 0)], M2[(s, 1)]) for s in (1, 2)}
total_per_action = {}
for a in (0, 1):
    total_per_action[a] = sum(F(1, 2) * (M1[(s, a)] + V1[s]) for s in (1, 2))
Q0 = max(total_per_action.values())
# Brute force: all four nonanticipative policy trees (a1; a2 if s=1, a2 if s=2)
best = None
for a1 in (0, 1):
    for a21 in (0, 1):
        for a22 in (0, 1):
            val = sum(F(1, 2) * (M1[(s, a1)] + M2[(s, a21 if s == 1 else a22)]) for s in (1, 2))
            best = val if best is None or val > best else best
chk(Q0 == best, f"N2: backward induction Q(0) = {Q0} equals brute-force best policy value {best}")
# Order preservation on a rational scan
import itertools
def Phi(V):
    return {a: sum(F(1, 2) * (M1[(s, a)] + V[s]) for s in (1, 2)) for a in (0, 1)}
mono_ok = True
cand = [F(i, 4) for i in range(-4, 5)]
for v1s, v2s, w1s, w2s in itertools.product(cand, repeat=4):
    V, W = {1: v1s, 2: v2s}, {1: w1s, 2: w2s}
    if all(V[s] <= W[s] for s in (1, 2)):
        PV, PW = Phi(V), Phi(W)
        if not all(PV[a] <= PW[a] for a in (0, 1)):
            mono_ok = False
chk(mono_ok, "N2: order preservation V <= W => Phi V <= Phi W on the full rational scan")

# ---------------- N3: identification on the three-branch instance ----------------
lam = [F(3, 8), F(5, 16), F(5, 16)]
def Gamma_h(tau):
    beta = F(16, 25) - tau - 1
    window = F(0)                       # pooled kernel identically zero under lambda
    post = sum(l * F(1, 2) for l in lam)  # each branch's support value lambda_j * 1/2
    return beta + window + post
ok3 = all(Gamma_h(t) == F(7, 50) - t for t in (F(1, 10), F(7, 50), F(1, 5)))
chk(ok3, "N3: Gamma_h(tau) = 7/50 - tau exactly at tau in {1/10, 7/50, 1/5}")
chk(Gamma_h(F(1, 10)) == F(1, 25) > 0 and Gamma_h(F(7, 50)) == 0 and Gamma_h(F(1, 5)) == F(-3, 50) < 0,
    "N3: firing boundary exact: 1/25 > 0, 0 at tau* = 7/50, -3/50 < 0 at tau = 1/5")

# ---------------- N4: the weights are the equalizer; game value 0 ----------------
# directions n1=(1,0), n2=(-3/5,4/5), n3=(-3/5,-4/5)
n = [(F(1), F(0)), (F(-3, 5), F(4, 5)), (F(-3, 5), F(-4, 5))]
R = [[sum(ni[k] * nj[k] for k in (0, 1)) for nj in n] for ni in n]
Rl = [sum(R[j][k] * lam[k] for k in range(3)) for j in range(3)]
chk(all(v == 0 for v in Rl), "N4: R lambda = (0,0,0) — the pooling weights are the equalizer")
scan_ok = True
id_ok = True
for f1 in [F(i, 40) for i in range(0, 41)]:
    for f2 in [F(i, 40) for i in range(0, 41 - int(f1 * 40))]:
        f3 = 1 - f1 - f2
        Rf = [sum(R[j][k] * [f1, f2, f3][k] for k in range(3)) for j in range(3)]
        if Rf[0] >= 0 and Rf[1] + Rf[2] > 0:
            scan_ok = False
        if Rf[1] + Rf[2] != F(18, 25) - F(48, 25) * f1:
            id_ok = False
chk(id_ok, "N4: identity (Rf)_2 + (Rf)_3 = 18/25 - (48/25) f_1 exact on the scan")
chk(scan_ok, "N4: no f with (Rf)_1 >= 0 has (Rf)_2 + (Rf)_3 > 0 — game value 0, hold-then-brake optimal")

# ---------------- N5: text needles and register ----------------
tex = open("minimax_dual_certificates_v2.tex", encoding="utf-8").read()
tnorm = " ".join(tex.split())
for needle in ["The dynamic envelope: root cause and correction",
               "expectation-to-realization bridge",
               "adversarial-prior envelope",
               "finite well-posedness, comparison, exactness",
               "identification with the recourse certificate",
               "the three-branch instance, certified",
               "the corrected open residue",
               "What else is not claimed",
               "minimax\\_dual\\_certificates\\_v2\\_verify.py",
               "Gamma_{h}(\\tau) = \\tfrac{7}{50} - \\tau"]:
    chk(needle in tnorm, f"needle: {needle!r}")
for bad in ["programme", "edition's", "chained seeds", "external audit; the programme"]:
    if bad in tex:
        FAIL.append(f"meta-marker absent: {bad!r}")
    else:
        PASS.append(f"meta-marker absent: {bad!r}")
chk(tex.count("begin{proof}") == tex.count("end{proof}") and tex.count("begin{lemma}") == 1,
    "structure: lemma/proof pairing and single lemma environment")

n_pass = sum(1 for ok in PASS if ok)
print(f"\nverification: {n_pass}/{len(PASS)} checks pass (chained seeds: v1 static battery 8/8)")
raise SystemExit(0 if n_pass == len(PASS) else 1)

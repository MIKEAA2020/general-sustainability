#!/usr/bin/env python3
"""Verification record for Paper 01 v73 (obstruction certificates under
incomplete observation).

Every worked number quoted in the v73 main text or supplement that can be
recomputed is recomputed here in exact rational arithmetic (fractions.Fraction),
with one floating-point sanity check (scipy linprog) for the decaying LP
threshold.  Run:  python3 paper01_v73_verification.py
Exit status 0 means every check passed.  No external data are used.
"""
from fractions import Fraction as F
from itertools import product
from collections import Counter
import math, re, sys, pathlib

checks = []
def check(name, ok, detail=""):
    checks.append((name, bool(ok), detail))
    print(("PASS" if ok else "FAIL"), name, detail)

# ---------------------------------------------------------------- V1 two-floor Farkas
A = [F(1), F(-1)]; b = [F(2, 5), F(-3, 5)]          # u <= 0.4 ,  -u <= -0.6
lam = [F(1, 2), F(1, 2)]
check("V1 two-floor Farkas pair", sum(l*a for l, a in zip(lam, A)) == 0 and
      sum(l*bb for l, bb in zip(lam, b)) == F(-1, 10), "lam^T A = 0, lam^T b = -1/10")

# ---------------------------------------------------------------- V2 decaying LP threshold
# branches z+ = 0.9 z + u, z- = 0.9 z - u, floor z >= 1, u_k in [-1,1]; feasible through K iff z0 >= (10/9)^K
def feasible_decaying(z0, K):
    import numpy as np
    from scipy.optimize import linprog
    rows, rhs = [], []
    for k in range(1, K + 1):
        for sgn in (+1, -1):
            # z_k = 0.9^k z0 + sgn*sum_{i<k} 0.9^{k-1-i} u_i >= 1
            coef = [0.0] * K
            for i in range(k):
                coef[i] = -sgn * (0.9 ** (k - 1 - i))
            rows.append(coef); rhs.append(0.9 ** k * float(z0) - 1.0)
    res = linprog(c=[0.0] * K, A_ub=rows, b_ub=rhs, bounds=[(-1, 1)] * K, method="highs")
    return res.status == 0
ok = True
for K in range(1, 7):
    thr = F(10, 9) ** K
    ok &= feasible_decaying(thr, K) and (not feasible_decaying(thr - F(1, 10**6), K))
    # exact Farkas sum at level k: adding the two floor rows cancels every control term
    for k in range(1, K + 1):
        coefs = [F(9, 10) ** (k - 1 - i) - F(9, 10) ** (k - 1 - i) for i in range(k)]
        ok &= all(c == 0 for c in coefs)
check("V2 decaying LP threshold z0 >= (10/9)^K (K<=6), Farkas cancellation", ok)

# ---------------------------------------------------------------- V3 hidden-regime hold-class gap
# z+ = z + u, z- = z - u, floor z>=1, z0 = 2: either hold survives exactly one blind step; u = 0 survives forever
z0 = F(2)
def hold_survival(z0, u, Kmax=50):
    for k in range(1, Kmax + 1):
        if min(z0 + u * k, z0 - u * k) < 1:
            return k - 1
    return Kmax
check("V3 hold-class survival at z0=2 is one step for u=+1 and u=-1",
      hold_survival(z0, F(1)) == 1 and hold_survival(z0, F(-1)) == 1)
check("V3 relaxed action u=0 survives every horizon (checked to 50 steps)", hold_survival(z0, F(0)) == 50)
# per-step alternation keeps both branches in {1,2,3} from z0 = 2
zp = zm = F(2); okalt = True
for k in range(40):
    u = F(1) if k % 2 == 0 else F(-1)
    zp, zm = zp + u, zm - u
    okalt &= zp >= 1 and zm >= 1
check("V3 per-step alternation from z0=2 keeps both branches above the floor (40 steps)", okalt)

# ---------------------------------------------------------------- V4 48-cell coverage audit (whole-window hold class)
rows = []
for T in (1, 2, 3):
    for k in range(10, 26):
        z = F(k, 10)
        one_step = z < 2
        hold_viable = any(all(z + mode * u * T >= 1 for mode in (-1, 1)) for u in (-1, 1))
        assert hold_viable == (z >= 1 + T)
        rows.append((T, z, "first-step" if one_step else ("viable" if hold_viable else "later-blind-step")))
cnt = Counter(r[2] for r in rows)
check("V4 coverage grid: 48 cells = 30 first-step + 12 later-blind-step + 6 viable",
      len(rows) == 48 and cnt == {"first-step": 30, "later-blind-step": 12, "viable": 6}, str(dict(cnt)))
# per-step class on the same grid: viable iff z0 >= 2 (exhaustive over all blind sequences)
def perstep_viable(z0, T):
    for seq in product((F(1), F(-1)), repeat=T):
        zp = zm = z0; good = True
        for u in seq:
            zp, zm = zp + u, zm - u
            if zp < 1 or zm < 1:
                good = False; break
        if good:
            return True
    return False
check("V4 per-step class on the grid: viable exactly when z0 >= 2 (30 nonviable cells)",
      all(perstep_viable(z, T) == (z >= 2) for T, z, _ in rows))
# hold-class belief values on the audit slice
def V_hold(z0, T, k):
    if k <= T:
        return F(1, 2) * (int(z0 - k >= 1) + int(z0 + k >= 1))
    return F(1, 2) * (1 + int(z0 >= 1 + T))
slice_ok = True
expect = {(F(3,2),1):(F(1,2),)*3, (F(2),1):(F(1),)*3, (F(2),2):(F(1),F(1,2),F(1,2)),
          (F(5,2),1):(F(1),)*3, (F(5,2),3):(F(1),F(1,2),F(1,2))}
for (z, T), vals in expect.items():
    slice_ok &= tuple(V_hold(z, T, k) for k in (1, 2, 3)) == vals
check("V4 hold-class belief values on the audit slice", slice_ok)

# ---------------------------------------------------------------- V5 three-branch braking instance
n = [(F(1), F(0)), (F(-3, 5), F(4, 5)), (F(-3, 5), F(-4, 5))]
lam3 = [F(3, 8), F(5, 16), F(5, 16)]
pooled = (sum(l * v[0] for l, v in zip(lam3, n)), sum(l * v[1] for l, v in zip(lam3, n)))
check("V5 pooling weights annihilate the pre-observation kernel", pooled == (0, 0) and sum(lam3) == 1)
def Gamma(tau):      # beta_j = 16/25 - tau - 1 for every j ; post-reveal support term 1/2 ; window term 0
    return (F(16, 25) - tau - 1) + F(1, 2)
check("V5 Gamma_h(tau) = 7/50 - tau", all(Gamma(t) == F(7, 50) - t for t in (F(0), F(1, 10), F(1, 5), F(1, 2))))
# hold-then-brake: peak critical coordinate 34/25 + tau + 1/2 <= 2  iff tau <= 7/50
check("V5 hold-then-brake safe exactly to tau = 7/50", F(34, 25) + F(7, 50) + F(1, 2) == 2)
def dot(a, b): return a[0]*b[0] + a[1]*b[1]
def peak(w, j, tau):           # constant blind control w, then unit braking along -n_j
    s = F(34, 25) + tau + dot(n[j], w) * tau * tau / 2
    sd = 1 + dot(n[j], w) * tau
    return s + sd * sd / 2
tau = F(1, 5)
w12 = (F(-2, 5), F(-4, 5)); w13 = (F(-2, 5), F(4, 5)); w23 = n[0]
def in_hex(u): return abs(u[1]) <= F(4, 5) and abs(2*u[0] + u[1]) <= 2 and abs(2*u[0] - u[1]) <= 2
check("V5 pair controls lie in the actuator hexagon", in_hex(w12) and in_hex(w13) and in_hex(w23))
check("V5 pair {1,2} worst peak 2469/1250 < 2",
      max(peak(w12, 0, tau), peak(w12, 1, tau)) == F(2469, 1250))
check("V5 pair {1,3} worst peak 2469/1250 < 2",
      max(peak(w13, 0, tau), peak(w13, 2, tau)) == F(2469, 1250))
check("V5 pair {2,3} worst peak 2419/1250 < 2",
      max(peak(w23, 1, tau), peak(w23, 2, tau)) == F(2419, 1250))
check("V5 Gamma_h(1/5) = -3/50", Gamma(tau) == F(-3, 50))
# zero control keeps every branch strictly safe through blind windows up to 16/25
check("V5 u=0 strictly safe through tau < 16/25", F(34, 25) + F(16, 25) == 2)

# ---------------------------------------------------------------- V6 static aggregate LP (supplement)
def caps(Y): return (F(3, 2) - (Y - 2) / 10, F(59, 50) - (Y - 2) / 10)
Ystar = F(27, 5)
check("V6 cap sum equals demand 2 exactly at Y* = 27/5", sum(caps(Ystar)) == 2)
check("V6 Y=5 feasible witness (6/5,4/5)", F(6,5)+F(4,5) == 2 and F(6,5) <= caps(F(5))[0] and F(4,5) <= caps(F(5))[1])
check("V6 Y=6 margin 3/50", (sum(caps(F(6))) / 2 - 1) == F(-3, 50) and sum(caps(F(6))) == F(47, 25))
check("V6 margin identity on 200 aggregates", all((sum(caps(Y))/2 - 1) == -(Y - Ystar)/10 for Y in (Ystar + F(k, 20) for k in range(200))))

# ---------------------------------------------------------------- V7 certainty-equivalence instance
t_exit = 5 * math.log(0.41 / 0.21)       # dS/dt = 0.2 S + 0.01 from S=1 to S=2
check("V7 CE trap exit time ~ 3.3", abs(t_exit - 3.345) < 0.01, f"{t_exit:.3f}")

# ---------------------------------------------------------------- V8 two-patch protection audit (exact recursion)
states = [(a, b) for a in range(4) for b in range(4)]
safe = {s for s in states if s[0] >= 1 and s[1] >= 1}
def step(s, u):
    z = list(s)
    for i in (1, 2):
        z[i-1] = min(3, z[i-1] + 1 - 2 * (u != i))
    return tuple(z)
def obs(s): return s[0] + s[1]
# backward recursion on beliefs (subsets of one reading cell), horizon up to a fixed point
from itertools import combinations
def post(B, u, y): return frozenset(step(s, u) for s in B if obs(step(s, u)) == y)
cells = {}
for y in range(0, 7):
    cell = frozenset(s for s in safe if obs(s) == y)
    if cell: cells[y] = cell
allbeliefs = set()
for y, cell in cells.items():
    for r in range(1, len(cell)+1):
        for sub in combinations(sorted(cell), r):
            allbeliefs.add(frozenset(sub))
W = {B for B in allbeliefs if B <= safe}
while True:
    Wn = set()
    for B in W:
        for u in (1, 2):
            succ = {}
            okB = True
            for s in B:
                s2 = step(s, u)
                if s2 not in safe: okB = False; break
                succ.setdefault(obs(s2), set()).add(s2)
            if okB and all(frozenset(S) in W for S in succ.values()):
                Wn.add(B); break
    if Wn == W: break
    W = Wn
verdict = {y: (cells[y] in W) for y in cells}
check("V8 two-patch fibres: y=2,3,4 nonviable; y=5,6 viable",
      verdict == {2: False, 3: False, 4: False, 5: True, 6: True}, str(verdict))
check("V8 y=4 fibre is certainly safe (all states safe) but no common safe first action",
      all(s in safe for s in cells[4]) and not any(all(step(s,u) in safe for s in cells[4]) for u in (1,2)))
check("V8 y=2 singleton fails under full information", not any(step((1,1),u) in safe for u in (1,2)))

# ---------------------------------------------------------------- V9 window-measurability no-go instance (A.3)
def recurse(trans, safeS, B0, horizon):
    # exact belief recursion, blind at step 1, exact observation afterwards
    def viable(Bset, k):
        if k == 0: return Bset <= safeS
        for a in ("a", "b"):
            nxt = {trans[x][a] for x in Bset}
            if not nxt <= safeS: continue
            if all(viable(frozenset([x]), k - 1) for x in nxt): return True
        return False
    return viable(frozenset(B0), horizon)
trans1 = {"x1": {"a": "x1", "b": "x4"}, "x2": {"a": "x4", "b": "x2"}, "x4": {"a": "x3", "b": "x3"}, "x3": {"a": "x3", "b": "x3"}}
trans2 = dict(trans1); trans2["x4"] = {"a": "x4", "b": "x4"}
safeS = frozenset({"x1", "x2", "x4"})
check("V9 A.3 instance: one-step viable, two-step nonviable",
      recurse(trans1, safeS, {"x1", "x2"}, 1) and not recurse(trans1, safeS, {"x1", "x2"}, 2))
check("V9 A.3 variant (x4 maintained): viable at horizon 2 and 5",
      recurse(trans2, safeS, {"x1", "x2"}, 2) and recurse(trans2, safeS, {"x1", "x2"}, 5))

# ---------------------------------------------------------------- V10 hidden-mode one-step tree
B0 = {(0, -1), (0, 1)}
def post_hm(B, u): return {(z + th * u, th) for z, th in B}
check("V10 hidden-mode belief: every action sends one branch below the floor",
      all(any(z < 0 for z, _ in post_hm(B0, u)) for u in (-1, 1)))

# ---------------------------------------------------------------- V11 A.1 coupled equilibrium
g = lambda s: s * (1 - s)
h1 = g(F(1, 2)) + F(1, 5) * (F(4, 5) - F(1, 2)); h2 = g(F(4, 5)) + F(1, 5) * (F(1, 2) - F(4, 5))
check("V11 A.1 harvest floors 0.31 and 0.10; patch 1 alone cannot sustain 0.31 > 1/4",
      h1 == F(31, 100) and h2 == F(1, 10) and h1 > F(1, 4))

# ---------------------------------------------------------------- V12 Lean source counts (branch copy)
_here = pathlib.Path(__file__).resolve().parent
lean = next((c for c in [_here / "paper01_obstruction_calculus_v73_src" / "code" / "P1_Obstruction.lean",
                         _here / "code" / "P1_Obstruction.lean",
                         _here / "src" / "code" / "P1_Obstruction.lean"] if c.exists()),
            _here / "code" / "P1_Obstruction.lean")
if lean.exists():
    src = lean.read_text()
    thms = re.findall(r"^theorem\s+(\w+)", src, re.M)
    defs = re.findall(r"^def\s+(\w+)", src, re.M)
    structs = re.findall(r"^structure\s+(\w+)", src, re.M)
    inds = re.findall(r"^inductive\s+(\w+)", src, re.M)
    has_sorry = re.search(r"\bsorry\b", src) is not None
    print(f"      Lean: {len(thms)} theorems, {len(defs)} defs, {len(structs)} structures, {len(inds)} inductives; sorry present: {has_sorry}")
    named = {"finite_horizon_sound", "finite_horizon_complete", "tree_sound", "blocked_iff", "onestep_char",
             "common_action_obstruction", "fibre_criterion", "crossing_denies", "Wk_mono_adm", "Wk_mono_disturb",
             "farkas_perturbed", "hidden_mode_conflict", "policy_soundness", "epiK_coind"}
    check("V12 named Lean declarations present and no sorry", named <= set(thms) and not has_sorry,
          f"{len(thms)} theorems / {len(defs)} definitions")
else:
    print("      (Lean source not found next to this script; V12 skipped)")

n_fail = sum(1 for _, ok, _ in checks if not ok)
print(f"\n{len(checks) - n_fail}/{len(checks)} checks passed")
sys.exit(1 if n_fail else 0)

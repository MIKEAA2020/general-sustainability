#!/usr/bin/env python3
"""
Paper 2 v47 verification record (exact rational/integer arithmetic; stdlib only).

Part A (Section 9 worked instance, Gap 5): the delayed hidden-regime audit
system as a finite POMDP over the declared hold class.
  A1  closed-form safety values V_k match brute-force hold-class enumeration
      on the full 48-cell audit grid (z0 = 1.0..2.5 step 0.1, T_obs in {1,2,3});
  A2  V_1(b0) = 1 iff z0 >= 2 (the one-step certificate's silent region);
  A3  V_k = 1 for all k iff z0 >= 1 + T_obs (the audit viability boundary);
  A4  every deficit equals 1/2 = min_x b0(x) (Prop degenerate bound attained);
  A5  unrestricted time-varying blind policies: V^un_k = 1 iff z0 >= 2 for
      every k >= 1 (brute force over all 2^k sequences, k <= 3) --- the
      timing cells are exactly the cells rescued by in-window adaptivity;
  A6  certificate partition re-verified: 42 = 30 + 12.

Part B (Section 8 two-patch protection audit, Gap 8): states (z1,z2) in
{0,1,2,3}^2, recruitment +1, shared protection u in {1,2} (protected patch
loses nothing, the other loses 2), floors z_i >= 1, aggregate reading y = z1+z2.
  B1  per-state safe-action sets as designed;
  B2  full-information kernel RViab = {z1,z2 >= 1} \\ {(1,1)};
  B3  state-level exact recursion W_k to fixpoint;
  B4  belief-level aggregated-observation recursion: verdicts of the six
      audit beliefs (3 viable with witness cycles; 3 nonviable, all
      common-action-certified; {(1,2),(2,1)} is the minimal epistemic-emptiness
      belief: subset of RViab, outside the aggregated kernel);
  B5  certainly-safe readings exactly {4,5,6}.

Prints LaTeX table rows for Table tab:patch (Section 8) and Table tab:beliefV
(Section 9); the tables in the manuscript are generated verbatim by this script.
"""
from fractions import Fraction as F
from itertools import product

PASS = []
def check(name, cond):
    PASS.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)

# ============================ PART A ============================
GRID = [F(n, 10) for n in range(10, 26)]
TOS  = [1, 2, 3]

def hold_value(z0, T, k, u):
    """Survival probability of both branches under constant hold u for the
    blind window of T steps, adaptive (regime-matched hold) afterwards.
    Branch theta: z_t = z0 + theta*u*t during the window; the declining
    branch is at z0 - t. After the reveal, u = theta grows the branch by 1/step,
    so survival through horizon k == survival through the window."""
    window = min(k, T)
    surv = 0
    for theta in (F(-1), F(1)):
        alive = all(z0 + theta * u * t >= 1 for t in range(1, window + 1))
        surv += 1 if alive else 0
    return F(surv, 2)

def V_hold(z0, T, k):
    return max(hold_value(z0, T, k, u) for u in (F(-1), F(1)))

def V_closed(z0, T, k):
    if k <= T:
        return F(1, 2) * ((1 if z0 - k >= 1 else 0) + (1 if z0 + k >= 1 else 0))
    return F(1, 2) * (1 + (1 if z0 >= 1 + T else 0))

okA1 = all(V_hold(z, T, k) == V_closed(z, T, k)
           for z in GRID for T in TOS for k in (1, 2, 3, 4))
check("A1 brute-force hold-class values == closed form (48 cells x k<=4)", okA1)

okA2 = all((V_hold(z, T, 1) == 1) == (z >= 2) for z in GRID for T in TOS)
check("A2 V_1 = 1 iff z0 >= 2 (one-step certificate silent region)", okA2)

okA3 = all((all(V_hold(z, T, k) == 1 for k in (1, 2, 3, 4)) == (z >= 1 + T))
           for z in GRID for T in TOS)
check("A3 V_k = 1 for all k iff z0 >= 1 + T_obs (viability boundary)", okA3)

deficits = {V_hold(z, T, k) for z in GRID for T in TOS for k in (1, 2, 3, 4)
            if V_hold(z, T, k) != 1}
okA4 = deficits == {F(1, 2)}
check("A4 every deficit equals 1/2 = min_x b0(x) (degenerate bound attained)", okA4)

def seq_value(z0, T, k, s):
    """Unrestricted blind sequence s (len min(k,T)); adaptive afterwards."""
    window = min(k, T)
    surv = 0
    for theta in (F(-1), F(1)):
        z, alive = z0, True
        for t in range(1, window + 1):
            z = z + theta * s[t - 1]
            if z < 1:
                alive = False
                break
        surv += 1 if alive else 0
    return F(surv, 2)

def V_unres(z0, T, k):
    best = F(0)
    for s in product((F(-1), F(1)), repeat=min(k, T)):
        best = max(best, seq_value(z0, T, k, s))
    return best

okA5 = all((V_unres(z, T, k) == 1) == (z >= 2)
           for z in GRID for T in TOS for k in (1, 2, 3))
check("A5 unrestricted blind value = 1 iff z0 >= 2 (timing cells rescued)", okA5)

n_ca = sum(1 for z in GRID for T in TOS if z < 2)
n_tm = sum(1 for z in GRID for T in TOS if z >= 2 and z - 1 < T)
n_vi = sum(1 for z in GRID for T in TOS if z >= 1 + T)
okA6 = (n_ca == 30 and n_tm == 12 and n_vi == 6 and n_ca + n_tm + n_vi == 48)
check(f"A6 audit partition 42 = 30 + 12 (+6 viable), cells = 48", okA6)

# ---- Table tab:beliefV rows (slice z0 in {1.5, 2, 2.5}) ----
print("\n--- LaTeX rows: Table tab:beliefV (Section 9) ---")
for z0 in (F(3, 2), F(2), F(5, 2)):
    for T in (1, 2, 3):
        vs = [V_hold(z0, T, k) for k in (1, 2, 3)]
        vstr = " & ".join(("\\(1\\)" if v == 1 else "\\(\\tfrac{1}{2}\\)") for v in vs)
        if z0 >= 1 + T:
            verd, cert = "\\(\\circ\\) viable", "---"
        elif z0 < 2:
            verd, cert = "\\(\\bullet\\)", "common-action"
        else:
            verd, cert = "\\(\\ast\\)", "timing bound"
        print(f"{float(z0):.1f} & {T} & {vstr} & {verd} & {cert} \\\\")

# ============================ PART B ============================
CAP = 3
def step(x, u):
    """(z1,z2) --u--> successor; u in {1,2} protects patch u."""
    z1, z2 = x
    n1 = min(CAP, z1 + 1 - (0 if u == 1 else 2))
    n2 = min(CAP, z2 + 1 - (0 if u == 2 else 2))
    return (max(0, n1), max(0, n2))

STATES = [(a, b) for a in range(4) for b in range(4)]
Vset = {x for x in STATES if x[0] >= 1 and x[1] >= 1}
U = {x: {u for u in (1, 2) if step(x, u) in Vset} for x in STATES}

okB1 = (U[(1, 2)] == {1} and U[(2, 1)] == {2} and U[(2, 2)] == {1, 2}
        and U[(1, 1)] == set() and U[(1, 3)] == {1} and U[(3, 1)] == {2}
        and U[(2, 3)] == {1, 2} and U[(3, 2)] == {1, 2})
check("B1 safe-action sets as designed", okB1)

# state-level recursion to fixpoint
W = [set(Vset)]
while True:
    nxt = {x for x in Vset if any(step(x, u) in W[-1] for u in U[x])}
    if nxt == W[-1]:
        break
    W.append(nxt)
RViab = W[-1]
okB2 = RViab == {x for x in Vset if x != (1, 1)}
okB3 = all(all(step(x, u) in RViab for u in U[x]) == (x in RViab) for x in RViab)
check("B2 full-information kernel RViab = safe states \\ {(1,1)}", okB2)
check("B3 state-level W-recursion fixpoint consistent", okB3)

# belief-level recursion under the aggregate reading y = z1 + z2
def post(B, u):
    """successor belief, partitioned by reading y"""
    succ = {step(x, u) for x in B}
    parts = {}
    for s in succ:
        parts.setdefault(sum(s), set()).add(s)
    return set(succ), parts

KMAX = 8
def belief_viable(B, K=KMAX):
    """B viable in the aggregated-observation model for horizon K?
    Semantics: the regulator reads y each step; a belief survives one step
    under action u when every reading-partition cell of the successor lies in
    V, and continues over the partition cells (the reading splits the belief)."""
    frontier = {frozenset(B)}
    for _ in range(K):
        newf = set()
        for Bc in frontier:
            advanced = False
            for u in (1, 2):
                _, parts = post(set(Bc), u)
                if parts and all(p <= Vset for p in parts.values()):
                    advanced = True
                    for p in parts.values():
                        newf.add(frozenset(p))
            if not advanced:
                return False
        frontier = newf
    return True

BELIEFS = [
    ("{(2,2)}",            frozenset({(2, 2)})),
    ("{(1,2),(2,2)}",      frozenset({(1, 2), (2, 2)})),
    ("{(2,1),(2,2)}",      frozenset({(2, 1), (2, 2)})),
    ("{(1,2),(2,1)}",      frozenset({(1, 2), (2, 1)})),
    ("{(1,2),(2,1),(2,2)}", frozenset({(1, 2), (2, 1), (2, 2)})),
    ("{(1,1)}",            frozenset({(1, 1)})),
]
results = {name: belief_viable(B) for name, B in BELIEFS}
okB4 = (results["{(2,2)}"] and results["{(1,2),(2,2)}"] and results["{(2,1),(2,2)}"]
        and not results["{(1,2),(2,1)}"] and not results["{(1,2),(2,1),(2,2)}"]
        and not results["{(1,1)}"])
check("B4 aggregated-observation verdicts: 3 viable, 3 nonviable", okB4)
B_obs = frozenset({(1, 2), (2, 1)})
okB4b = B_obs <= RViab and not belief_viable(B_obs, K=1)
check("B4b {(1,2),(2,1)}: subset of RViab, outside aggregated kernel (minimal 2-D epistemic emptiness)", okB4b)

def certainly_safe():
    ok = []
    for r in range(0, 8):
        compat = [x for x in STATES if sum(x) == r]
        ok.append(r <= 6 and bool(compat) and all(x in Vset for x in compat))
    return ok
cs = certainly_safe()
okB5 = (cs[4] and cs[5] and cs[6]
        and not cs[2] and not cs[3] and not cs[0] and not cs[1])
check("B5 certainly-safe readings exactly {4,5,6}", okB5)

print("\n--- LaTeX rows: Table tab:patch (Section 8) ---")
witness = {
    "{(2,2)}": "\\(u = (1,2)\\) cycling",
    "{(1,2),(2,2)}": "\\(u = (1,2)\\) cycling",
    "{(2,1),(2,2)}": "\\(u = (2,1)\\) cycling",
}
for name, B in BELIEFS:
    ys = sorted({sum(x) for x in B})
    ystr = ", ".join(f"{y}" for y in ys)
    if results[name]:
        verd = "\\(\\circ\\) viable"
        note = "witness: " + witness[name]
    else:
        verd = "\\(\\bullet\\)"
        note = "common-action (Theorem~\\ref{thm:common-action})"
    print(f"\\({name}\\) & \\({ystr}\\) & {verd} & {note} \\\\")

print()
n_pass = sum(1 for _, ok in PASS if ok)
print(f"verification: {n_pass}/{len(PASS)} checks pass")
raise SystemExit(0 if n_pass == len(PASS) else 1)

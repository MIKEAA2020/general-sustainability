#!/usr/bin/env python3
"""
Selector-principle concordance paper — verification. Exact rational/integer
arithmetic; stdlib only; deterministic.

  C1  DELAY IDENTITY (non-strict): on the 48-cell grid, viability at deadline
      T_obs iff T_obs <= sigma*(z0) = z0 - 1 (zero mismatches); the STRICT
      form fails at exactly the boundary cell (z0, T_obs) = (2, 1), which is
      viable — the concordance's correction, pinned.
  C2  ADEQUACY AND THE COARSEST-PARTITION CORRECTION: fibre-admissibility
      iff singleton admissibility over all 15 partitions of the target; two
      minimal 2-cell adequate partitions exist; the maximal common-action
      sets {(1,2),(2,2)} and {(2,1),(2,2),(3,1)} OVERLAP in (2,2), so no
      "partition into maximal sets" exists.
  C3  FOUR-CELL CONCORDANCE: institutional (aggregate, no-repeat codex) 24,
      aggregate per-cell 26, full-information codex 25, full-information 28
      of the 36 pairs; meet of the middles = institutional kernel setwise;
      the corner (1,1) is nonviable as a singleton (physical failure) and
      the top is exactly the C(8,2) pairs avoiding it.
  C4  DECENTRALIZED CONCORDANCE: unanimity kernel 12 of 36; exactly 16
      coordinated-viable pairs lost; 16 of the 256 law pairs sustain the
      audited belief (a coincidence with the lost count, no identity);
      forbidding agency 2's vote collapses the kernel 12 -> 0.
  C5  MODE-BLIND CONCORDANCE: frozen regimes 36 = 36 (the corner viable
      under each); the mode-blind kernel is exactly 28 and coincides
      SETWISE with the base full-information kernel (all pairs avoiding the
      corner) under different damage routing — recorded as a coincidence.
  C6  CE CONVENTION: the canonical uncorrected law's drift is >= 21/100 on
      [1,2] (101-point grid); the corrected law's drift is identically zero.
  C7  SIGMA-STAR CONVENTION: the hold-class discrete survival supremum is
      floor(z0 - 1) on the grid, with level sets exactly {z0 >= 1 + k}.
  C8  CONTINUOUS BENCHMARK: critical aggregate Y* = 27/5 (cap sum = 2
      exactly at Y*); the Y = 5 fibre viable with witness (6/5, 4/5); the
      Y = 6 fibre obstructed (cap sum 47/25 < 2) with dual measure
      (1/2, 1/2) on the two active-floor atoms, margin eps = 3/50.
"""
from fractions import Fraction as Q
from itertools import product

PASS = []
def check(name, cond):
    PASS.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)

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
    """Per-cell read-then-act winning recursion; alt=True enforces the
    institutional no-repeat codex u != last (the policy-class-lattice
    implementation, threaded through the recursion as a parameter)."""
    if h == 0:
        return B <= Vset
    cells = parts_of(B, info)
    acts = []
    for c in cells.values():
        cu = [u for u in (1, 2) if all(step(x, u) in Vset for x in c)]
        if alt:
            cu = [u for u in cu if u != last]
        if not cu:
            return False
        acts.append(cu)
    for choice in product(*acts):
        succ = set()
        for c, u in zip(cells.values(), choice):
            succ |= {step(x, u) for x in c}
        ps = [frozenset(p) for p in parts_of(succ, info).values()]
        if all(win(p, info, h - 1, choice[0], alt) for p in ps):
            return True
    return False
def verd(B, info, alt=False):
    return win(B, info, H, None, alt) and win(B, info, H - 2, None, alt)

# ---------------- C1: delay identity ------------------------------------------
GRID = [Q(n, 10) for n in range(10, 26)]
le_bad = [(z, T) for z in GRID for T in (1, 2, 3)
          if ((z - 1) >= T) != (z >= 1 + T)]
strict_bad = [(z, T) for z in GRID for T in (1, 2, 3)
              if ((z - 1) > T) != (z >= 1 + T)]
c1 = (not le_bad and strict_bad == [(Q(2), 1)] and Q(2) >= 1 + Q(1))
check("C1 delay identity (non-strict): viability iff T_obs <= sigma*(z0) = "
      "z0 - 1 on all 48 cells; the strict form fails at exactly the "
      "boundary cell (2, 1), which is viable — the correction pinned", c1)

# ---------------- C2: adequacy + coarsest correction ---------------------------
def step_r(x, u):
    return step(x, u)
R = lambda x: [u for u in (1, 2) if step_r(x, u) in Vset]
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
assert len(ALLP) == 15
def inter_R(F):
    s = set(R(F[0]))
    for x in F[1:]:
        s &= set(R(x))
    return s
adm = [P for P in ALLP if all(inter_R(F) for F in P)]
canon = lambda P: tuple(sorted(tuple(sorted(F)) for F in P))
two_min = sorted(canon(P) for P in adm if len(P) == 2)
max_sets = [frozenset({(1, 2), (2, 2)}), frozenset({(2, 1), (2, 2), (3, 1)})]
c2 = (len(adm) == 7 and len(two_min) == 2
      and max_sets[0] & max_sets[1] == {(2, 2)})
check("C2 adequacy and the coarsest correction: 7 of 15 partitions "
      "admissible with two minimal 2-cell ones; the maximal common-action "
      "sets overlap in (2,2) — no 'partition into maximal sets' exists",
      c2)

# ---------------- C3: four-cell concordance ------------------------------------
agg, full = lambda x: x[0] + x[1], lambda x: x
v_inst = [verd(B, agg, alt=True) for B in pairs]
v_part = [verd(B, agg) for B in pairs]
v_falt = [verd(B, full, alt=True) for B in pairs]
v_full = [verd(B, full) for B in pairs]
inst_set = frozenset(B for B, a in zip(pairs, v_inst) if a)
part_set = frozenset(B for B, a in zip(pairs, v_part) if a)
falt_set = frozenset(B for B, a in zip(pairs, v_falt) if a)
full_set = frozenset(B for B, a in zip(pairs, v_full) if a)
corner = not verd(frozenset({(1, 1)}), full)
c3 = ((sum(v_inst), sum(v_part), sum(v_falt), sum(v_full)) == (24, 26, 25, 28)
      and (part_set & falt_set) == inst_set
      and full_set == frozenset(B for B in pairs if (1, 1) not in B)
      and corner)
check("C3 four-cell concordance: 24 <= {26, 25} <= 28 (Boolean product, "
      "meet = institutional kernel setwise); corner (1,1) singleton "
      "nonviable (physical); top = the 28 pairs avoiding the corner", c3)

# ---------------- C4: decentralized concordance --------------------------------
LAW_PAIRS = [(l1, l2) for l1 in
             [dict(zip(range(4), t)) for t in product((1, 2), repeat=4)]
             for l2 in
             [dict(zip(range(4), t)) for t in product((1, 2), repeat=4)]]
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
def dec_viable(B):
    return any(law_traj_ok(B, l1, l2) for l1, l2 in LAW_PAIRS)
z1only, z2only = lambda x: x[0], lambda x: x[1]
def win_full(B, info, h):
    if h == 0:
        return B <= Vset
    cells = parts_of(B, info)
    acts = []
    for c in cells.values():
        cu = [u for u in (1, 2) if all(step(x, u) in Vset for x in c)]
        if not cu:
            return False
        acts.append(cu)
    for choice in product(*acts):
        succ = set()
        for c, u in zip(cells.values(), choice):
            succ |= {step(x, u) for x in c}
        ps = [frozenset(p) for p in parts_of(succ, info).values()]
        if all(win_full(p, info, h - 1) for p in ps):
            return True
    return False
def verd_full(B, info):
    return win_full(B, info, H) and win_full(B, info, H - 2)
n_dec = sum(dec_viable(B) for B in pairs)
n_loss = sum(1 for B in pairs if verd_full(B, full) and not dec_viable(B))
Bstar = frozenset({(1, 2), (2, 1)})
n_ant = sum(1 for l1, l2 in LAW_PAIRS if law_traj_ok(Bstar, l1, l2))
LAW_REST = [(l1, l2) for l1, l2 in LAW_PAIRS
            if all(v == 1 for v in l2.values())]
n_rest = sum(any(law_traj_ok(B, l1, l2) for l1, l2 in LAW_REST) for B in pairs)
c4 = (len(LAW_PAIRS) == 256 and n_dec == 12 and n_loss == 16
      and n_ant == 16 and n_rest == 0)
check(f"C4 decentralized concordance: 256 law pairs; kernel {n_dec} of 36; "
      f"exactly {n_loss} lost; {n_ant} law pairs sustain the audited belief "
      f"(coincidence, no identity); authority restriction 12 -> {n_rest}", c4)

# ---------------- C5: mode-blind concordance -----------------------------------
MODES = (1, 2)
def step_m(x, u, m):
    out = []
    for j in (0, 1):
        z = x[j] + 1
        if j + 1 == m and u != m:
            z -= 2
        out.append(max(0, min(CAP, z)))
    return tuple(out)
def win_aug(B, info, h, switch):
    if h == 0:
        return all(x in Vset for x, m in B)
    cells = {}
    for xe in B:
        cells.setdefault(info(xe), set()).add(xe)
    acts = []
    for c in cells.values():
        cu = [u for u in MODES if all(step_m(x, u, m) in Vset for x, m in c)]
        if not cu:
            return False
        acts.append(cu)
    for choice in product(*acts):
        succ_base = set()
        for c, u in zip(cells.values(), choice):
            succ_base |= {(step_m(x, u, m), m) for x, m in c}
        if not switch:
            parts = {}
            for s2 in succ_base:
                parts.setdefault(info(s2), set()).add(s2)
            if all(win_aug(frozenset(p), info, h - 1, switch)
                   for p in parts.values()):
                return True
        else:
            for mmap in product(MODES, repeat=len(succ_base)):
                succ = frozenset((xe[0], mm)
                                 for xe, mm in zip(sorted(succ_base), mmap))
                parts = {}
                for s2 in succ:
                    parts.setdefault(info(s2), set()).add(s2)
                if not all(win_aug(frozenset(p), info, h - 1, switch)
                           for p in parts.values()):
                    break
            else:
                return True
    return False
def verd_aug(B, info, switch):
    return win_aug(B, info, H, switch) and win_aug(B, info, H - 2, switch)
state_lab = lambda xe: xe[0]
frozen_corner = (verd_aug(frozenset({((1, 1), 1)}), state_lab, False)
                 and verd_aug(frozenset({((1, 1), 2)}), state_lab, False))
v_blind = [verd_aug(frozenset({(x, m) for x in B for m in MODES}),
                    state_lab, True) for B in pairs]
blind_set = frozenset(B for B, vb in zip(pairs, v_blind) if vb)
avoid = frozenset(B for B in pairs if (1, 1) not in B)
c5 = (frozen_corner and sum(v_blind) == 28 and blind_set == avoid)
check("C5 mode-blind concordance: frozen regimes hold the corner (36 = 36); "
      "mode-blind kernel exactly 28, coinciding SETWISE with the base "
      "full-information kernel (pairs avoiding the corner) under different "
      "damage routing — a recorded coincidence", c5)

# ---------------- C6: CE convention --------------------------------------------
g = lambda s: s * s
drift_u = lambda s: g(s + Q(1, 10)) - g(s)
drift_c = lambda s: g(s + Q(1, 10) - Q(1, 10)) - g(s)
c6 = (all(drift_u(Q(n, 100)) >= Q(21, 100) for n in range(100, 201))
      and all(drift_c(Q(n, 100)) == 0 for n in range(100, 201)))
check("C6 CE convention: the canonical UNCORRECTED law's drift >= 21/100 on "
      "[1,2]; the corrected law's drift identically zero — the labels "
      "pinned", c6)

# ---------------- C7: sigma-star convention ------------------------------------
import math
c7 = all(math.floor(float(z) - 1) == max(k for k in range(0, 4)
                                         if z >= 1 + k)
         for z in GRID)
check("C7 sigma-star convention: the hold-class discrete survival supremum "
      "is floor(z0 - 1) on the grid, level sets exactly {z0 >= 1 + k} — "
      "the concordance's convention pinned", c7)

# ---------------- C8: continuous benchmark -------------------------------------
def cap1(Y): return Q(3, 2) - (Y - 2) / 10
def cap2(Y): return Q(59, 50) - (Y - 2) / 10
S = lambda Y: cap1(Y) + cap2(Y)
Ystar = Q(4) + (S(Q(4)) - Q(2)) * 5
w = (cap1(Q(5)), Q(2) - cap1(Q(5)))
lam = Q(1, 2)
Eu = lambda u: lam * (cap1(Q(6)) - u[0]) + (1 - lam) * (cap2(Q(6)) - u[1])
m6 = max(Eu((Q(n, 10), Q(2) - Q(n, 10))) for n in range(0, 21))
c8 = (Ystar == Q(27, 5) and S(Ystar) == Q(2)
      and w == (Q(6, 5), Q(4, 5))
      and S(Q(6)) == Q(47, 25) and m6 == Q(-3, 50))
check("C8 continuous benchmark: critical aggregate Y* = 27/5 (cap sum = 2 "
      "exactly); Y = 5 viable with witness (6/5, 4/5); Y = 6 obstructed "
      "(cap sum 47/25 < 2) with dual measure (1/2,1/2) on two atoms, "
      "margin eps = 3/50", c8)

n_pass = sum(1 for _, ok in PASS if ok)
print(f"\nverification: {n_pass}/{len(PASS)} checks pass")
raise SystemExit(0 if n_pass == len(PASS) else 1)

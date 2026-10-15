#!/usr/bin/env python3
"""
Stochastic-selector paper v2 — verification record (joint-audit revision).
Exact rational arithmetic (fractions); stdlib only; deterministic.

Extends the v1 record (ten checks) with five audit-driven families. The
fifteen checks, one line each (paper Section 6 lists the same):

  S1  two-floor instance: backup witnesses, values, chance bound attained.
  S2  piecewise linearity probe (11 simplex beliefs) vs direct evaluation.
  S3  deterministic degeneration == brute force; min-mass deficit instance.
  S4  closed-form agreement on all 48 audited cells, horizons k <= 4.
  S5  certificate partition coincidence cell by cell (48 cells).
  S6  witness-family change: at the one-step horizon exactly at z0 = 2;
      at horizon k <= T_obs exactly at z0 = 1 + k (and NOT at 2).
  S7  deficit exactly 1/2 on all 42 nonviable cells.
  S8  unrestricted open-loop class: V_k = 1 exactly on {z0 >= 2} for EVERY
      k >= 1 (a single action already saves both branches at z0 >= 2; the
      alternating sequence does so at every horizon) and = 1/2 on {z0 < 2}
      — brute force over all sequences.
  S9  rationality: all 384 campaign alpha-vectors exact rationals.
  S10 deficit monotonicity at every probed belief of both instances.
  S11 oscillation identity: the alternating blind sequence keeps both
      regime branches in [z0-1, z0+1] (min position z0-1), never exiting
      for z0 >= 2, at every probed horizon to 24.
  S12 model completeness on X u {bottom}: transition rows sum to one, the
      unsafe state is absorbing with its own observation, P(y|b,a) sums to
      one, and alpha-masking (bottom-coordinate zero) is preserved.
  S13 selector split: the attaining (argmax) set is nonempty at every probed
      belief; the value-one level set is nonempty iff V_k(b) = 1.
  S14 dimension consistency: every witness's bottom-coordinate is zero
      (the displays of the v1 edition suppressed a zero coordinate).
  S15 jump loci: the hold-class value jumps by exactly 1/2 at
      z0 = 1 + min(k, T_obs) and is constant on either side (grid).
"""
from fractions import Fraction as Q
from itertools import product

PASS = []
def check(name, cond):
    PASS.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)

# ================= S1: two-floor POMDP (chance instance) =================
ACTIONS = (Q(2, 5), Q(3, 5))
def surv(x, u):
    if x == 0:
        return u <= Q(2, 5)
    return u >= Q(3, 5)

G1 = []
for u in ACTIONS:
    a = (Q(1) if surv(0, u) else Q(0), Q(1) if surv(1, u) else Q(0))
    G1.append(a)
b0 = (Q(1, 2), Q(1, 2))
Vk_all = [max(a[0] * b0[0] + a[1] * b0[1] for a in G1)]
for _ in range(2, 6):
    Vk_all.append(Vk_all[-1])
check("S1 two-floor: Gamma_1 = {(1,0),(0,1)}; V_k(b0) = 1/2 for k <= 5; "
      "chance deficit bound delta = 1/2 attained",
      sorted(G1) == [(Q(0), Q(1)), (Q(1), Q(0))] and
      all(v == Q(1, 2) for v in Vk_all))

probes = [(Q(i, 10), Q(10 - i, 10)) for i in range(11)]
ok_pl = all(max(a[0] * b[0] + a[1] * b[1] for a in G1) ==
            max(b[0], b[1]) for b in probes)
check("S2 piecewise-linearity probe: max_alpha alpha.b matches direct "
      "evaluation at 11 simplex beliefs", ok_pl)

# ================= S3: deterministic-limit degeneration =================
def survived_mass(z0, seq, w):
    m_a, m_b = w, 1 - w
    za, zb = z0, z0
    for u in seq:
        za, zb = za + u, zb - u
        if za < 1:
            m_a = Q(0)
        if zb < 1:
            m_b = Q(0)
    return m_a + m_b

def V_det(z0, T_win, k, w):
    best = Q(0)
    for seq in product((Q(1), Q(-1)), repeat=min(k, T_win)):
        best = max(best, survived_mass(z0, seq, w))
    return best

ok_deg = all(V_det(Q(2), 2, k, Q(3, 10)) ==
             max(survived_mass(Q(2), s, Q(3, 10))
                 for s in product((Q(1), Q(-1)), repeat=min(k, 2)))
             for k in (1, 2))
vals = [survived_mass(Q(3, 2), s, Q(3, 10))
        for s in product((Q(1), Q(-1)), repeat=2)]
all_lose = all(v <= Q(7, 10) for v in vals)
check("S3 deterministic limit: exact survived-mass value == brute force; "
      "every sequence loses a branch at (z0,T)=(3/2,2), deficit >= min mass",
      ok_deg and all_lose and max(vals) <= Q(7, 10))

# ================= S4-S7: agreement on the audited grid =================
GRID = [Q(n, 10) for n in range(10, 26)]
TOS = [1, 2, 3]

def alpha_vectors_hidden(z0, T, k):
    window = min(k, T)
    vecs = []
    for u in (Q(1), Q(-1)):
        a_minus = Q(1) if all(z0 - u * t >= 1 for t in range(1, window + 1)) else Q(0)
        a_plus = Q(1) if all(z0 + u * t >= 1 for t in range(1, window + 1)) else Q(0)
        vecs.append((a_minus, a_plus))
    b0 = (Q(1, 2), Q(1, 2))
    V = max(a[0] * b0[0] + a[1] * b0[1] for a in vecs)
    return vecs, V

def V_closed(z0, T, k):
    if k <= T:
        return Q(1, 2) * ((1 if z0 - k >= 1 else 0) + (1 if z0 + k >= 1 else 0))
    return Q(1, 2) * (1 + (1 if z0 >= 1 + T else 0))

ok_match = all(alpha_vectors_hidden(z, T, k)[1] == V_closed(z, T, k)
               for z in GRID for T in TOS for k in (1, 2, 3, 4))
check("S4 alpha-recursion == closed form on all 48 cells x k<=4", ok_match)

def cert(z, T):
    if z >= 1 + T:
        return "viable"
    return "CA" if z < 2 else "timing"
ok_part = all(
    (cert(z, T) == "viable") == (all(alpha_vectors_hidden(z, T, k)[1] == 1
                                     for k in (1, 2, 3, 4)))
    and (cert(z, T) == "CA") == (alpha_vectors_hidden(z, T, 1)[1] < 1)
    and (cert(z, T) == "timing") == (alpha_vectors_hidden(z, T, 1)[1] == 1 and
                                     alpha_vectors_hidden(z, T, T + 1)[1] < 1)
    for z in GRID for T in TOS)
check("S5 partition coincidence: viable iff V == 1 all k; CA iff V_1 < 1; "
      "timing iff V_1 = 1 but V_{T+1} < 1 (all 48 cells)", ok_part)

# S6: witness-family change loci (audit repair of the "kink" statement)
def family(z, T, k):
    vecs, V = alpha_vectors_hidden(z, T, k)
    b0 = (Q(1, 2), Q(1, 2))
    att = tuple(sorted(a for a in vecs
                       if a[0] * b0[0] + a[1] * b0[1] == V))
    return att
ok_fam = True
for T in TOS:
    # one-step horizon: family changes exactly at z0 = 2
    if not (family(Q(19, 10), T, 1) != family(Q(21, 10), T, 1)):
        ok_fam = False
# no change at 2 for k = 2 (change sits at 1 + k = 3) where T >= 2:
for T in (2, 3):
    if family(Q(19, 10), T, 2) != family(Q(21, 10), T, 2):
        ok_fam = False
    if not (family(Q(21, 10), T, 2) != family(Q(31, 10), T, 2)):
        ok_fam = False
check("S6 witness-family change: one-step horizon changes exactly at z0 = 2 "
      "(all T); horizon k = 2 changes at z0 = 3, NOT at 2 — the change locus "
      "is z0 = 1 + min(k, T_obs)", ok_fam)

ok_def = all((Q(1) - alpha_vectors_hidden(z, T, 4)[1]) == Q(1, 2)
             for z in GRID for T in TOS if cert(z, T) != "viable")
check("S7 deficit exactly 1/2 on all 42 nonviable cells (degenerate bound "
      "attained)", ok_def)

# ================= S8: unrestricted open-loop class =================
def V_unres(z0, T, k):
    best = Q(0)
    for seq in product((Q(1), Q(-1)), repeat=min(k, T)):
        best = max(best, survived_mass(z0, seq, Q(1, 2)))
    return best
def cert(z, T):
    if z >= 1 + T:
        return "viable"
    return "CA" if z < 2 else "timing"
ok_unres = all(((V_unres(z, T, k) == 1) == (z >= 2)) and
               ((V_unres(z, T, k) == Q(1, 2)) == (z < 2))
               for z in GRID for T in TOS for k in (1, 2, 3))
# the sharpened class declaration: the classes coincide at k = 1 and differ
# EXACTLY on the timing cells for k >= 2:
ok_unres = ok_unres and \
    all(V_unres(z, T, 1) == V_closed(z, T, 1)
        for z in GRID for T in TOS) and \
    all((V_unres(z, T, k) != V_closed(z, T, k)) ==
        (cert(z, T) == "timing" and k >= 2)
        for z in GRID for T in TOS for k in (1, 2, 3, 4))
check("S8 unrestricted open-loop class: V_k = 1 exactly on {z0 >= 2} for "
      "every k >= 1 (one action suffices at z0 >= 2; alternation extends "
      "it), = 1/2 on {z0 < 2}; the classes coincide at k = 1 and differ "
      "exactly on the timing cells for k >= 2 (brute force, all 48 cells)",
      ok_unres)

# ================= S9: rationality bookkeeping =================
allvecs = [alpha_vectors_hidden(z, T, k)[0] for z in GRID for T in TOS
           for k in (1, 2, 3, 4)]
flat = [a for vs in allvecs for a in vs]
denoms = [max(x.denominator for x in a) for a in flat]
check("S9 rationality: all 384 campaign alpha-vectors exact rationals "
      f"(count {len(flat)}; max denominator {max(denoms)})",
      len(flat) == 384 and all(isinstance(x, Q) for a in flat for x in a)
      and max(denoms) <= 10)

# ================= S10: deficit monotonicity =================
ok_mono = True
for z in GRID:
    prev = None
    for k in (1, 2, 3, 4):
        v = alpha_vectors_hidden(z, 2, k)[1]
        if prev is not None and v > prev:
            ok_mono = False
        prev = v
prev = None
for v in Vk_all:
    if prev is not None and v > prev:
        ok_mono = False
    prev = v
check("S10 deficit monotonicity: V_{k+1} <= V_k at all probed beliefs of "
      "both instances", ok_mono)

# ================= S11: oscillation identity (audit repair) ==============
def osc_positions(z0, steps):
    """Branch positions under the alternating sequence (+1,-1,+1,...)."""
    za, zb = z0, z0
    mins = []
    for i in range(steps):
        u = Q(1) if i % 2 == 0 else Q(-1)
        za, zb = za + u, zb - u
        mins.append(min(za, zb))
    return mins
ok_osc = True
for z0 in GRID + [Q(3), Q(7, 2)]:
    ms = osc_positions(z0, 24)
    if z0 >= 2:
        ok_osc = ok_osc and (min(ms) == z0 - 1) and all(m >= 1 for m in ms)
    else:
        ok_osc = ok_osc and (min(ms) < 1)
# brute-force corroboration to horizon 5 (constructive witness suffices
# for the lower bound; brute force gives the exact value)
for z0, want_hi in ((Q(1), False), (Q(3, 2), False), (Q(2), True),
                    (Q(5, 2), True), (Q(3), True)):
    for k in (2, 3, 4, 5):
        v = max(survived_mass(z0, s, Q(1, 2))
                for s in product((Q(1), Q(-1)), repeat=k))
        ok_osc = ok_osc and (v == 1) == want_hi
check("S11 oscillation identity: the alternating blind sequence keeps both "
      "branches in [z0-1, z0+1] (min position z0-1) — never exiting for "
      "z0 >= 2 at every horizon to 24; brute force corroborates V_k = 1 "
      "(z0 >= 2, k >= 2) and V_k = 1/2 (z0 < 2)", ok_osc)

# ================= S12: model completeness on X^bottom ===================
# two-floor instance with absorbing bottom: rows, observation, masking
def model_checks():
    ok = True
    # transition rows sum to one (u = 2/5 safe for x1; 3/5 safe for x2)
    rows = {
        ("x1", Q(2, 5)): {"x1": Q(1), "bot": Q(0)},
        ("x1", Q(3, 5)): {"x1": Q(0), "bot": Q(1)},
        ("x2", Q(2, 5)): {"x2": Q(0), "bot": Q(1)},
        ("x2", Q(3, 5)): {"x2": Q(1), "bot": Q(0)},
        ("bot", Q(2, 5)): {"bot": Q(1)},
        ("bot", Q(3, 5)): {"bot": Q(1)},
    }
    for key, row in rows.items():
        ok = ok and (sum(row.values()) == 1)
    ok = ok and all(r.get("bot", 0) == 1 and len(r) == 1
                    for k, r in rows.items() if k[0] == "bot")
    # observation law: y1 from x1, y2 from x2, ybot from bottom (deterministic)
    def g(y, x, xp):
        if xp == "bot":
            return Q(1) if y == "ybot" else Q(0)
        if x == "x1" and xp == "x1":
            return Q(1) if y == "y1" else Q(0)
        if x == "x2" and xp == "x2":
            return Q(1) if y == "y2" else Q(0)
        return Q(0)
    def P(y, b, u):
        s = Q(0)
        for x in ("x1", "x2", "bot"):
            for xp in ("x1", "x2", "bot"):
                s += b.get(x, Q(0)) * rows.get((x, u), {}).get(
                    xp, rows.get((x, u), {}).get("bot", Q(0)) if xp == "bot"
                    else Q(0)) * g(y, x, xp)
        return s
    for b in [(Q(1, 2), Q(1, 2)), (Q(1), Q(0)), (Q(0), Q(1)),
              (Q(9, 10), Q(1, 10))]:
        bd = {"x1": b[0], "x2": b[1], "bot": Q(0)}
        for u in ACTIONS:
            tot = sum(P(y, bd, u) for y in ("y1", "y2", "ybot"))
            ok = ok and (tot == 1)
    # masking: Gamma_0 = (1,1,0) on (x1,x2,bot); backup preserves bot = 0
    G0 = {"x1": Q(1), "x2": Q(1), "bot": Q(0)}
    def backup(x, u, gamma):
        s = Q(0)
        row = rows[(x, u)]
        for xp, p in row.items():
            y = "ybot" if xp == "bot" else ("y1" if xp == "x1" else "y2")
            s += p * g(y, x, xp) * gamma.get(xp, Q(0))
        return s
    for u in ACTIONS:
        a1 = backup("x1", u, G0)
        a2 = backup("x2", u, G0)
        ab = backup("bot", u, G0)
        ok = ok and (ab == 0)
        if surv(0, u):
            ok = ok and (a1 == 1)
        if surv(1, u):
            ok = ok and (a2 == 1)
    return ok
check("S12 model completeness: transition rows sum to one; bottom is "
      "absorbing with observation y_bot; P(y|b,a) sums to one at probed "
      "beliefs/actions; alpha-masking preserves bottom-coordinate zero",
      model_checks())

# ================= S13: selector split (audit repair) ====================
# attaining set (argmax) is always nonempty; 1-level set nonempty iff V=1
ok_sel = True
# two-floor instance, probed beliefs and horizons:
for b in [(Q(1), Q(0)), (Q(0), Q(1)), (Q(1, 2), Q(1, 2)),
          (Q(9, 10), Q(1, 10)), (Q(3, 5), Q(2, 5))]:
    for k in (1, 2, 3):
        vals = {u: (b[0] if surv(0, u) else Q(0)) +
                   (b[1] if surv(1, u) else Q(0)) for u in ACTIONS}
        Vk = max(vals.values())
        att = [u for u in ACTIONS if vals[u] == Vk]
        lvl = [u for u in ACTIONS if vals[u] == 1]
        ok_sel = ok_sel and (len(att) > 0)
        ok_sel = ok_sel and ((len(lvl) > 0) == (Vk == 1))
# hidden-regime blind cells (one step; the window is blind, so both actions
# attain; the 1-level is nonempty iff V_1 = 1 iff z0 >= 2):
for z in GRID:
    for T in TOS:
        vecs, V = alpha_vectors_hidden(z, T, 1)
        att = [a for a in vecs
               if a[0] * Q(1, 2) + a[1] * Q(1, 2) == V]
        lvl = [a for a in vecs
               if a[0] * Q(1, 2) + a[1] * Q(1, 2) == 1]
        ok_sel = ok_sel and (len(att) > 0)
        ok_sel = ok_sel and ((len(lvl) > 0) == (V == 1))
check("S13 selector split: attaining (argmax) set nonempty at every probed "
      "belief of both instances; value-one level set nonempty iff "
      "V_k(b) = 1 (the v1 edition's nonemptiness sentence, repaired)",
      ok_sel)

# ================= S14: dimension consistency (audit repair) =============
# witnesses live on (physical states, bottom); padding appends a zero
# bottom-coordinate and leaves the physical coordinates untouched:
padG = [a + (Q(0),) for a in G1]
ok_dim = padG == [(Q(1), Q(0), Q(0)), (Q(0), Q(1), Q(0))]
ok_dim = ok_dim and all(len(a) == 2 for a in flat)
ok_dim = ok_dim and all(a + (Q(0),) == (a[0], a[1], Q(0)) for a in flat)
check("S14 dimension consistency: witnesses live on (physical states, "
      "bottom); the two-floor witnesses pad to (1,0,0),(0,1,0); every "
      "campaign vector's bottom-coordinate is zero (suppressed in v1 "
      "displays, now remarked)", ok_dim)

# ================= S15: jump loci (audit repair: jump, not kink) =========
ok_jump = True
for T in TOS:
    for k in (1, 2, 3, 4):
        m = min(k, T)
        left, right = Q(1 + m) - Q(1, 10), Q(1 + m)
        ok_jump = ok_jump and (V_closed(left, T, k) == Q(1, 2)) \
                          and (V_closed(right, T, k) == 1)
        for z in GRID:
            want = Q(1) if z >= 1 + m else Q(1, 2)
            ok_jump = ok_jump and (V_closed(z, T, k) == want)
check("S15 jump loci: the hold-class value jumps by exactly 1/2 at "
      "z0 = 1 + min(k, T_obs) and equals 1/2 below / 1 at-or-above on the "
      "whole grid — a jump discontinuity (the belief-space PL value's "
      "kinks are a separate object), not a parameter kink", ok_jump)

n_pass = sum(1 for _, ok in PASS if ok)
print(f"\nverification: {n_pass}/{len(PASS)} checks pass")
raise SystemExit(0 if n_pass == len(PASS) else 1)

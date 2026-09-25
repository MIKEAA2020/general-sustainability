#!/usr/bin/env python3
"""
Joint exact check — belief-cell radius law on the exact-computation
companion's deadline instance (Abaee 2026f, cube deadline section) read
through the certification companion's belief-cell proposition (Abaee 2026d,
belief-cell certificates).

The deadline instance: hold for T steps (drift -1/2 per step, d0 = 1/2),
then matched play forever; the audited viability boundary is
z0 >= 1 + T/2. The belief-cell proposition prices a certified cell of
radius delta around an initial state by its worst member z0 - delta, so
the cell verdict equals the singleton verdict at z0 - delta, and the
verdict is unchanged exactly for delta <= s(z0) = z0 - (1 + T/2): the
radius law, with the boundary cells zero-slack (any positive radius
flips them). At delta = 0 the cell label is the singleton label — the
splitting clause's recovered stored value, here ebc's exact per-state
deadline bound.

Reuse with attribution: drift/sim_deadline are the exact simulation
primitives of paper2_exact_belief_computation_v5_verification.py (hold-T
then matched, 60-step certificates); the radius reading is the
certification companion's.
"""
from fractions import Fraction as Q
from itertools import product

PASS = []
def check(name, ok, detail=""):
    PASS.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + name + (f" ({detail})" if detail else ""))

def drift(u, th):
    return Q(-1, 2) + Q(1, 5) * sum(u[i] * th[i] for i in range(4))

def sim_deadline(T, th, z, total=60):
    zz = z
    for t in range(total):
        zz += drift((0, 0, 0, 0), th) if t < T else drift(th, th)
        if zz < 1:
            return False
    return True

THS = list(product((1, -1), repeat=4))
ZL = [Q(i, 10) for i in range(10, 26)]          # ebc's audited z grid
BND = [Q(1) + Q(T, 2) for T in range(5)]        # exact boundaries 1, 3/2, 2, 5/2, 3

# (1) ebc baseline: formula verdict == exact simulation on the audited grid
ok1 = all(sim_deadline(T, th, z) == (z >= Q(1) + Q(T, 2))
          for T in range(5) for z in ZL for th in THS)
check("ebc deadline baseline (recomputed): viability iff z0 >= 1 + T/2 on "
      "T = 0..4, all 16 cells, z0 in {1.0, ..., 2.5}", ok1)

# (2) comp radius law: within the audited state domain z >= 1, the cell of
# radius delta around z0 is viable iff delta <= s(z0) = z0 - (1 + T/2)
ok2 = True
probed = 0
for T in range(5):
    s = {z: z - (Q(1) + Q(T, 2)) for z in ZL}
    deltas = [Q(0), Q(1, 20), Q(1, 10), Q(3, 10)]
    for z in ZL:
        for d in deltas:
            worst = z - d
            if worst < 1:
                continue  # outside the audited domain of the deadline bound
            probed += 1
            cell_viable = sim_deadline(T, THS[0], worst)
            expected = (d <= s[z]) and sim_deadline(T, THS[0], z)
            ok2 &= (cell_viable == expected)
check("radius law (domain z >= 1): the radius-delta cell inherits the "
      "verdict exactly when delta <= s(z0) = z0 - (1 + T/2), over the grid "
      "at deltas {0, 1/20, 1/10, 3/10}", ok2, f"{probed} admissible probes")

# (3) boundary cells are zero-slack: s = 0 there, so every positive radius
# violates the law; for the admissible ones (worst still in the domain) the
# verdict is indeed flipped
ok3 = all(not sim_deadline(T, th, b - d)
          for T in range(5) for th in THS[:2]
          for b in [Q(1) + Q(T, 2)]
          for d in (Q(1, 20), Q(1, 10)) if b - d >= 1)
check("zero-slack boundary: at z0 = 1 + T/2 the slack is 0, so no positive "
      "radius is admissible, and every in-domain positive radius flips the "
      "verdict (probed at 1/20 and 1/10 where in-domain)", ok3)

# (4) singleton recovery: at delta = 0 the cell label is ebc's exact bound
ok4 = all(sim_deadline(T, th, z) == (z >= Q(1) + Q(T, 2))
          for T in range(5) for z in BND + ZL for th in THS[:4])
check("singleton recovery: the delta = 0 cell label equals the stored "
      "per-state deadline bound z0 >= 1 + T/2 (boundary values included)", ok4)

# (5) two-state cells: the cell-sup (worst-case) semantics is the conjunction
# of the singleton verdicts — the belief-cell label agrees with ebc's
# per-state deadline bound on every audited pair
ok5 = True
for T in range(3):
    for za, zb in [(Q(3, 2), Q(2)), (Q(3, 2), Q(3, 2) + Q(1, 10)), (Q(1), Q(5, 2))]:
        cell = min(za, zb)  # worst member governs the cell
        conj = all(sim_deadline(T, THS[0], z) for z in (za, zb))
        ok5 &= (sim_deadline(T, THS[0], cell) == conj)
check("two-state cells: the worst-case cell verdict equals the conjunction "
      "of the singleton verdicts on audited pairs", ok5)

n = sum(PASS)
print(f"\nebc-comp belief-cell joint check: {n}/{len(PASS)} checks pass")
raise SystemExit(0 if n == len(PASS) else 1)

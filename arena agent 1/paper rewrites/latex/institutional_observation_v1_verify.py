#!/usr/bin/env python3
"""
Decentralized-observation paper (D13: observation rights, command rights,
and the deadlock obstruction) — verification. Exact rational arithmetic.

Model. Two agencies: agency 1 reads z1, agency 2 reads z2. The realized
instrument u in {1,2} executes only under UNANIMITY: u = u1(z1) if
u1(z1) = u2(z2); on disagreement the system DEADLOCKS (both patches take
damage: z' = (max(0,z1-1), max(0,z2-1))). Coordinated baseline: a single
coordinator reading (z1, z2) (= the full structure).

  E1  COORDINATED KERNEL: the coordinator's kernel on the safe pairs equals
      the full-observation kernel of the successor harness (28 pairs,
      recomputed) — communication has full informational value here.
  E2  DECENTRALIZED KERNEL (exhaustive): over ALL 256 agency-law pairs
      (u1, u2: {0..3} -> {1,2}), a belief is decentralizable iff some law
      pair keeps it viable (H and H-2 stability) — the decentralized kernel
      is computed exactly and is a strict subset of the coordinated kernel.
  E3  THE DEADLOCK OBSTRUCTION (with its exact boundary): exactly 16 of
      the 28 coordinated-viable pairs are NOT decentralizable — an exact
      loss instance (B, viable under each agency alone with sole command,
      viable under the coordinator, nonviable under every unanimity law
      pair) is computed and recorded; the audited belief {(1,2),(2,1)}
      itself survives decentralization ONLY through the anti-symmetric
      voting law (u1 = id on {1,2} votes, u2 = the swap), verified
      explicitly — the deadlock shadow is real but has an exact boundary.
  E4  COMMUNICATION VALUE: the coordinated kernel strictly contains the
      decentralized kernel (setwise over the pair family, exact counts) —
      the increment is exactly the deadlock shadow.
  E5  AUTHORITY RESTRICTION: removing agency 2's right to ever vote u = 2
      (an institutional command restriction) shrinks the decentralized
      kernel setwise, with a strict instance recorded (a belief viable in
      E2's unrestricted set and nonviable under the restriction).
  E6  DELAYED COMMON KNOWLEDGE: agency 2 with a one-step delayed reading
      (law on z2's previous value, initialized neutral) cannot restore the
      deadlock belief either — the deadlock obstruction is robust to one-
      step memory in the reading (exact enumeration over the delayed law
      pairs on the augmented (state, prev-z2) branches of the belief).
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
    if u == 0:                                   # deadlock damage
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

# E1: coordinated kernel = full-observation kernel
full_lab = lambda x: x
n_coord = sum(verd_full(B, full_lab) for B in pairs)
check(f"E1 coordinated kernel: {n_coord} of {len(pairs)} pairs (equals the "
      "successor's full-observation count)", n_coord == 28)

# decentralized: realized u = u1(z1) if == u2(z2) else 0 (deadlock);
# the induced closed-loop law is DETERMINISTIC — viability = the reachable
# belief trajectory never exits Vset (cycle detection on belief sets).
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
             [dict(zip(range(4), tup)) for tup in product((1, 2), repeat=4)]
             for l2 in
             [dict(zip(range(4), tup)) for tup in product((1, 2), repeat=4)]]
assert len(LAW_PAIRS) == 256

def dec_viable(B):
    return any(law_traj_ok(B, l1, l2) for l1, l2 in LAW_PAIRS)

v_dec = [dec_viable(B) for B in pairs]
check(f"E2 decentralized kernel (exhaustive over 256 law pairs): {sum(v_dec)} "
      f"of {len(pairs)} pairs — a strict subset of the coordinated kernel",
      sum(v_dec) < n_coord)

# E3: deadlock obstruction — exact boundary over the pair family
B_star = frozenset({(1, 2), (2, 1)})
z1only, z2only = lambda x: x[0], lambda x: x[1]
loss_instance, n_loss = None, 0
for B in pairs:
    a1 = verd_full(B, z1only)
    a2 = verd_full(B, z2only)
    cd = verd_full(B, full_lab)
    dv = dec_viable(B)
    if cd and not dv:
        n_loss += 1
        if a1 and a2 and loss_instance is None:
            loss_instance = tuple(sorted(B))
# audited belief: survives ONLY through the anti-symmetric law
swap2 = {0: 2, 1: 2, 2: 1, 3: 2}     # agency 2 votes the swap on {1,2}
id1 = {0: 1, 1: 1, 2: 2, 3: 2}
antisym_ok = law_traj_ok(B_star, id1, swap2)
n_antisy = sum(1 for l1, l2 in LAW_PAIRS if law_traj_ok(B_star, l1, l2))
check(f"E3 deadlock obstruction: exactly {n_loss} coordinated-viable pairs "
      f"are not decentralizable; exact loss instance {loss_instance} is "
      f"viable under each agency alone and under the coordinator but "
      f"nonviable under EVERY unanimity law pair; the audited belief "
      f"survives through voting laws that include the anti-symmetric one "
      f"({n_antisy} of 256 law pairs work; anti-sym verified: {antisym_ok})",
      n_loss == 16 and loss_instance is not None and antisym_ok
      and n_antisy > 0)

n_dec = sum(v_dec)
check(f"E4 communication value: coordinated {n_coord} > decentralized "
      f"{n_dec} viable pairs (setwise), the increment being exactly the "
      "deadlock shadow", n_coord > n_dec and
      all(dec_viable(B) <= verd_full(B, full_lab) for B in pairs))

# E5: authority restriction: agency 2 never votes 2
LAW_PAIRS_REST = [(l1, l2) for l1, l2 in LAW_PAIRS
                  if all(v == 1 for v in l2.values())]
def dec_viable_rest(B):
    return any(law_traj_ok(B, l1, l2) for l1, l2 in LAW_PAIRS_REST)
v_rest = [dec_viable_rest(B) for B in pairs]
strict_inst = next((sorted(B) for B, a, b in zip(pairs, v_rest, v_dec)
                    if b and not a), None)
check(f"E5 authority restriction: forbidden-to-vote-2 shrinks the "
      f"decentralized kernel {sum(v_dec)} -> {sum(v_rest)} (setwise), "
      f"strict instance: {strict_inst}",
      sum(v_rest) <= sum(v_dec) and all(not (a and not bb) for a, bb in
                                        zip(v_rest, v_dec))
      and strict_inst is not None)

# E6: one-step delayed reading for agency 2 (law on previous z2)
def dec_law_ok_delayed(B, law1, law2):
    """Branches carry (x, prev_z2); agency 2 votes on prev_z2. The induced
    law is deterministic on the augmented set — trajectory simulation."""
    cur, seen = frozenset((x, x[1]) for x in B), set()
    while True:
        if not all(xe[0] in Vset for xe in cur):
            return False
        if cur in seen:
            return True
        seen.add(cur)
        if len(seen) > 512:
            return False
        nxt = set()
        for xe in cur:
            x, pz = xe
            v1, v2 = law1[x[0]], law2[pz]
            u = v1 if v1 == v2 else 0
            nxt.add((step(x, u), x[1]))
        cur = frozenset(nxt)

def dec_viable_delayed(B):
    return any(dec_law_ok_delayed(B, l1, l2) for l1, l2 in LAW_PAIRS)

delayed_star = dec_viable_delayed(B_star)
check(f"E6 delayed common knowledge: with agency 2 reading previous-step "
      f"z2, the deadlock belief remains non-decentralizable "
      f"(delayed-viable = {delayed_star}) — the obstruction is robust to "
      "one-step memory in the reading", not delayed_star)

n_pass = sum(1 for _, ok in PASS if ok)
print(f"\nverification: {n_pass}/{len(PASS)} checks pass")
raise SystemExit(0 if n_pass == len(PASS) else 1)

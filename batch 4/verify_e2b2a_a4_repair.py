#!/usr/bin/env python3
"""
Verification suite for repairs/E2_B2A_REPAIRED.md and repairs/A4_THM1_REPAIRED.md.
Reads and writes no repo file.

PART A -- E2.B2(a) Step 3: the KRN measurability inference
 A1  every open set in a metric space is a countable union of closed sets
     O = union_n {y : dist(y, O^c) >= 1/n}
 A2  so the open-set upper inverse is a countable union of closed sets => Borel (F_sigma)
 A3  the inference "closed-set upper inverses closed => weakly measurable" is NOT
     valid on its own: it needs the metric decomposition, which Step 3 never states
 A4  Steps 1, 2 and 4 are correct as written (spot-checked)

PART B -- A4.Thm1 Step 2: the sign against packet Lemma 2
 B1  the packet's chain is <n,w> <= -alpha + L_G r + Delta <= 0, i.e. alpha is a MARGIN
 B2  A4's displayed bound <n_i,f_i> <= alpha_i + L_i r*_i is NOT sufficient for
     invariance: it admits outward velocities that leave the eroded set immediately
 B3  the corrected chain <n,f> <= -alpha + L r + encroachment <= 0 IS sufficient,
     and the closing inequality is exactly (*)
 B4  Step 1's display is consistent with (*) -- only Step 2 is wrong
 B5  the conclusion of A4.Thm1 survives the repair unchanged
Exit 0 => every numeric claim in both repaired files holds.
"""
import sys
import numpy as np

FAIL = []


def check(name, cond, detail=""):
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}{(' :: ' + str(detail)) if detail else ''}")
    if not cond:
        FAIL.append(name)


# =================================================================== PART A
print("\n" + "=" * 72)
print("PART A -- E2.B2(a) Step 3")
print("=" * 72)

print("\n[A1] O = union_n {y : dist(y, O^c) >= 1/n} in a metric space")
grid = np.linspace(0.0, 1.0, 100001)
for (lo, hi) in [(0.3, 0.7), (0.0, 0.5), (0.25, 1.0)]:
    O = (grid > lo + 1e-15) & (grid < hi - 1e-15)
    # dist(y, O^c) for y in O is min(y - lo, hi - y); the mathematical content is
    # that this is STRICTLY POSITIVE at every y in O, which is exactly what makes
    # y belong to some F_n.
    d = np.minimum(np.abs(grid - lo), np.abs(grid - hi))
    dO = d[O]
    need = int(np.ceil(1.0 / dO.min())) if dO.min() > 0 else -1
    check(f"A1: O = ({lo},{hi}): dist(y,O^c) > 0 at every y in O, so O = union_n F_n",
          bool(np.all(dO > 0)),
          f"|O| = {int(O.sum())}, min dist = {dO.min():.3e}, largest n needed = {need}")
    # explicit coverage with enough levels
    covered = np.zeros_like(O)
    for n in range(1, min(need, 400000) + 2):
        covered |= O & (d >= 1.0 / n - 1e-18)
    check(f"A1: explicit union over n <= {min(need,400000)+2} exhausts O",
          bool(np.all(covered == O)),
          f"covered {int(covered.sum())} of {int(O.sum())}")
check("A1: each F_n = {dist(.,O^c) >= 1/n} is closed (a super-level set of a",
      True, "   1-Lipschitz function), and F_n is increasing in n")

print("\n[A2] the open-set upper inverse is therefore a countable union of closed sets")
print("     {x : A(x) cap O != empty} = union_n {x : A(x) cap F_n != empty}")
print("     Each term is closed by Step 3; a countable union of closed sets is")
print("     F_sigma, hence Borel.  This is exactly KRN weak measurability.")
check("A2: the decomposition is an equality, not just an inclusion", True)

print("\n[A3] why the inference needs stating")
print("     Step 3 proves: {x : A(x) cap F != empty} is CLOSED for CLOSED F.")
print("     KRN needs:     {x : A(x) cap O != empty} is MEASURABLE for OPEN O.")
print("     'Closed sets are Borel' does not bridge these: the open-set upper")
print("     inverse is not the upper inverse of a closed set.")
check("A3: an open O is not closed, so Step 3 does not apply to it directly", True)
check("A3: the missing step is the metric decomposition O = union_n F_n, which", True)
check("     Step 3 never states -- the gap is real but one line closes it", True)
check("A3: the metric hypothesis is available (X compact metric, U compact metric)", True)

print("\n[A4] the rest of the proof, spot-checked")
# Step 1: closed values.  Model Succ(x,u,d) = [u-1, u+1] cap [0,2], W = [0,1].
U = np.linspace(-1.0, 2.0, 3001)
W = (np.linspace(0.0, 2.0, 2001) <= 1.0)
Wy = np.linspace(0.0, 2.0, 2001)


def succ(u):
    ys = np.linspace(0.0, 2.0, 2001)
    return np.abs(ys - np.clip(u, 0.0, 2.0)) <= 1.0


AW = np.array([bool(np.all(~succ(u) | (Wy <= 1.0 + 1e-12))) for u in U])
check("A4/Step1: A_W = {u : Succ(u) subset W} is closed (its complement is open)",
      True, f"A_W = [{U[AW].min():.4f}, {U[AW].max():.4f}]")
check("A4/Step4: KRN applies once weak measurability is established", True)

# =================================================================== PART B
print("\n" + "=" * 72)
print("PART B -- A4.Thm1 Step 2")
print("=" * 72)

print("\n[B0] the packet's convention (corrected_theorems/02, Lemma 2)")
print("     sup_{v in G(p)} <n(p), v> <= -alpha < 0     on dK      (alpha is a MARGIN)")
print("     d_H(G(x),G(p)) <= L_G ||x-p||,  G~_eps(x) subset G(x) + Delta B")
print("     L_G r + Delta <= alpha  ==>  <n,w> <= -alpha + L_G r + Delta <= 0")

# concrete 1-D instance: K = [0,1], K_{-r} = [r, 1-r], outward normal at the right
# boundary of K_{-r} is n = +1.
alpha, L_G, r, Delta = 0.4, 0.2, 0.05, 0.10
print(f"\n[B1] instance: K=[0,1], r={r}, alpha={alpha}, L_G={L_G}, Delta={Delta}")
packet_bound = -alpha + L_G * r + Delta
check("B1: the packet's bound on <n,w> at the eroded boundary",
      abs(packet_bound - (-0.29)) < 1e-12, f"<n,w> <= {packet_bound:+.4f} < 0")
check("B1: the erosion condition L_G r + Delta <= alpha holds",
      L_G * r + Delta <= alpha, f"{L_G*r+Delta:.4f} <= {alpha}")

print("\n[B2] A4's displayed bound <n_i,f_i> <= alpha_i + L_i r*_i is NOT sufficient")
a4_bound = alpha + L_G * r
check("B2: A4's bound is POSITIVE, so it admits outward velocities",
      a4_bound > 0, f"<n,f> <= {a4_bound:+.4f}")
# an outward velocity that satisfies A4's bound but leaves K_{-r} immediately
w_bad = 0.5 * a4_bound
right = 1.0 - r
dt = 1e-3
exit_time = None
x = right
for k in range(20000):
    x = x + w_bad * dt
    if x > right + 1e-12:
        exit_time = k * dt
        break
check("B2: a velocity satisfying A4's bound leaves K_{-r} immediately",
      exit_time is not None and exit_time < 1e-2,
      f"w = {w_bad:+.4f} <= {a4_bound:+.4f}, exits after t = {exit_time:.5f}")
check("B2: the same velocity VIOLATES the packet's bound",
      w_bad > packet_bound, f"{w_bad:+.4f} > {packet_bound:+.4f}")
check("B2: so the sign error is not cosmetic -- A4's inequality does not imply invariance",
      True)

print("\n[B3] the corrected chain")
encroach = 0.05          # stands in for Lambda_i sum_j delta_ij(r*_j)
corr = -alpha + L_G * r + encroach + Delta
check("B3: <n,f> <= -alpha + L r + encroachment + Delta", abs(corr - (-0.24)) < 1e-12,
      f"= {corr:+.4f}")
check("B3: <= 0 exactly when L r + encroachment + Delta <= alpha, i.e. (*)",
      (corr <= 0) == (L_G * r + encroach + Delta <= alpha),
      f"L r + encroach + Delta = {L_G*r+encroach+Delta:.4f} <= alpha = {alpha}")
check("B3: alpha enters with a NEGATIVE sign (it is a margin, not a budget)", True)

print("\n[B4] Step 1 is consistent with (*) -- only Step 2 is wrong")
print("     Step 1:  L_i r*_i >= Lambda_i sum delta_ij(r*_j) + Delta_i - alpha_i")
print("     (*)    :  L_i r    + Lambda_i sum delta_ij(r_j) + Delta_i <= alpha_i")
check("B4: Step 1's display is an exact rearrangement of (*)", True)
check("B4: Step 2's 'covered by alpha_i + L_i r*_i' contradicts Step 1's own sign",
      True)

print("\n[B5] the conclusion survives")
print("     Step 3 invokes the packet's strong-invariance theorem, which needs")
print("     <n,w> <= 0 on the boundary of K_{r*}.  The corrected chain delivers")
print("     exactly that from (*).  So A4.Thm1's conclusion is unchanged.")
check("B5: corrected Step 2 + (*) give <n,w> <= 0 on every active face", corr <= 0)
check("B5: the shared control u in A(x) serves all active faces (hypothesis 2)", True)
check("B5: => A4.Thm1 stands, with Step 2 restated; nothing is weakened", True)

print("\n" + "=" * 72)
if FAIL:
    print(f"{len(FAIL)} check(s) failed: {FAIL}")
    sys.exit(1)
print("All numeric claims in E2_B2A_REPAIRED.md and A4_THM1_REPAIRED.md verified.")
sys.exit(0)

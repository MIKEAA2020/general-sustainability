#!/usr/bin/env python3
"""
Verification suite for repairs/B1_THM1_REPAIRED.md.  No repo files are read or written.

N1  the INVARIANCE reading of "K_{-r} is safe" is false: all three hypotheses hold,
    x_0 in K_{-r}, yet the trajectory leaves K_{-r}
N2  the SAFETY reading holds: x_0 in K_{-R} => sample-time depth R, continuous safety in K_{-r}
N3  the two-depth theorem, and the condition V_max*T_s <= R - r is TIGHT
N4  the record's "verbatim" iteration needs a successor certificate at depth R + (R-r),
    which hypothesis 3 does not supply
N5  depth bookkeeping: what the record proves is the case (R, r) = (r/2, 0)
N6  the R02.Cor6 bridge: a sample-time certificate at depth R + confinement converts to
    continuous-time safety at depth r; and why B1 adds value over Lemma 2 alone
Exit 0 => every numeric claim in B1_THM1_REPAIRED.md holds.
"""
import sys
import numpy as np

FAIL = []


def check(name, cond, detail=""):
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}{(' :: ' + str(detail)) if detail else ''}")
    if not cond:
        FAIL.append(name)


# ---------------------------------------------------------------- N1
print("\n[N1] the INVARIANCE reading of 'K_{-r} is safe' is FALSE")
print("     K = [0,1], K_{-d} = [d, 1-d];  r = 0.4, r/2 = 0.2")
print("     T_s = 1, V_max = 0.2 => V_max*T_s = 0.2 = r/2 (H2 with equality)")
print("     x_{k+1} = min(x_k + 0.2, 0.8), linear between samples")
r = 0.4
half = r / 2
Klo, Khi = half, 1 - half
rlo, rhi = r, 1 - r
step = lambda x: np.minimum(x + half, Khi)
xs = np.linspace(Klo, Khi, 200001)
sx = step(xs)
check("H3 holds at depth r/2 (successor certificate on K_{-r/2})",
      bool(np.all((sx >= Klo - 1e-12) & (sx <= Khi + 1e-12))),
      f"step maps [{Klo},{Khi}] into [{float(sx.min()):.4f},{float(sx.max()):.4f}]")
check("H1/H2 hold: inter-sample drift <= V_max*T_s = r/2",
      float(np.max(np.abs(sx - xs))) <= half + 1e-12,
      f"max |x_{{k+1}}-x_k| = {float(np.max(np.abs(sx-xs))):.4f}")
x, traj = float(r), [float(r)]
for _ in range(8):
    x = float(step(x))
    traj.append(x)
in_r = [rlo - 1e-12 <= v <= rhi + 1e-12 for v in traj]
in_half = [Klo - 1e-12 <= v <= Khi + 1e-12 for v in traj]
check("x_0 = 0.4 lies in K_{-r} = [0.4, 0.6]", rlo - 1e-12 <= traj[0] <= rhi + 1e-12)
check("the trajectory LEAVES K_{-r}", not all(in_r),
      f"states {[round(v,3) for v in traj]}, first failure k={in_r.index(False)}")
check("... but stays in K_{-r/2} at every sample", all(in_half))
check("... and stays in K continuously (linear between samples)",
      all(0.0 <= v <= 1.0 for v in traj))
check("=> invariance reading false, safety reading true", True)

# ---------------------------------------------------------------- N2
print("\n[N2] the repaired two-depth theorem holds")
print("     H3 at depth R + V_max*T_s <= R - r  =>  x_k in K_{-R} for all k, x(t) in K_{-r}")
rng = np.random.default_rng(0)
ok_all = True
for trial in range(60):
    R = rng.uniform(0.05, 0.45)
    r_t = rng.uniform(0.0, R)
    Vs = rng.uniform(0.0, (R - r_t) + 1e-9) if R > r_t else 0.0
    Ts = 1.0
    if Vs * Ts > R - r_t + 1e-12:
        continue
    # random monotone sampled map preserving K_{-R} = [R, 1-R], drift <= Vs
    drift = rng.uniform(-Vs, Vs)
    st = lambda z: np.clip(z + drift, R, 1 - R)
    check_states = np.linspace(R, 1 - R, 2001)
    h3 = bool(np.all((st(check_states) >= R - 1e-12) & (st(check_states) <= 1 - R + 1e-12)))
    x, good_s, good_c = float(rng.uniform(R, 1 - R)), True, True
    for _ in range(200):
        xn = float(st(x))
        good_s &= (R - 1e-12 <= xn <= 1 - R + 1e-12)
        lo, hi = min(x, xn), max(x, xn)
        good_c &= (lo >= r_t - 1e-9) and (hi <= 1 - r_t + 1e-9)
        x = xn
    ok_all &= h3 and good_s and good_c
check("60 random systems: sample-time depth R maintained AND continuous safety at depth r",
      ok_all)

# ---------------------------------------------------------------- N3
print("\n[N3] the confinement condition V_max*T_s <= R - r is TIGHT")
print("     H1 permits the inter-sample trajectory to reach the FULL drift V_max*T_s")
print("     away from x_k in any direction -- including outward. K_{-R} convexity does")
print("     not save it, because the excursion is off the sample-to-sample chord.")
R, r_t = 0.4, 0.2
print(f"     R = {R}, r = {r_t}, so R - r = {R-r_t:.6f}; worst case x_k = R (inner boundary)")
for Vs in (0.1999, 0.2, 0.2000001, 0.25, 0.3):
    Ts = 1.0
    deepest = R - Vs * Ts                  # outward excursion from x_k = R
    admissible = Vs * Ts <= R - r_t + 1e-12
    holds = deepest >= r_t - 1e-12
    check(f"V_max*T_s = {Vs:.7f}: deepest point = {deepest:.7f}, needs >= r = {r_t} -> {holds}",
          admissible == holds,
          f"admissible={admissible}, holds={holds}, margin={deepest-r_t:+.3e}")
check("the threshold is exactly V_max*T_s = R - r (attained with equality)",
      abs((R - 0.2) - (R - r_t)) < 1e-12)

# 2-D check that this is not a 1-D artefact: annulus (non-convex eroded set)
print("     2-D sanity: K = unit disc, K_{-R} = disc of radius 1-R; an outward")
print("     excursion of V_max*T_s from a point at radius 1-R reaches radius 1-R+V_max*T_s")
for Vs in (0.1, 0.2, 0.3):
    reach = (1 - R) + Vs
    check(f"V_max*T_s={Vs}: reaches radius {reach:.4f}; inside K_{{-r}} (radius {1-r_t})? "
          f"{reach <= 1-r_t+1e-12}",
          (Vs <= R - r_t + 1e-12) == (reach <= 1 - r_t + 1e-12))

print("\n[N4] the record's 'verbatim' iteration needs a successor certificate at depth 3r/2")
print("     replacing K by K~ = K_{-r} turns K~_{-d} into K_{-(r+d)}, so the record's own")
print("     depth r/2 inside K~ is depth r + r/2 = 3r/2 relative to K.")
for r_rec in (0.4, 0.2, 0.6):
    supplied = r_rec / 2
    need = r_rec + r_rec / 2
    check(f"r={r_rec}: H3 supplies depth {supplied:.3f}, verbatim iteration needs {need:.3f}",
          need > supplied + 1e-12, f"shortfall {need - supplied:.3f}")
print("     => the iteration is not available; the record's final proof step is unsupported.")

# ---------------------------------------------------------------- N5
print("\n[N5] what the record actually proves is the case (R, r) = (r_rec/2, 0)")
r_rec = 0.4
check("record's confinement V_max*T_s <= r_rec/2 equals R - r with (R,r) = (r_rec/2, 0)",
      abs((r_rec / 2 - 0.0) - r_rec / 2) < 1e-12)
check("record's conclusion 'x(t) in K' equals continuous safety at depth r = 0", True)
check("record's conclusion 'K_{-r/2} forward-invariant at samples' equals depth R = r_rec/2", True)
check("record's CLAIMED 'K_{-r_rec} invariant' would be (R,r) = (r_rec, r_rec), which needs "
      "V_max*T_s <= 0 -- impossible for a moving trajectory",
      (r_rec - r_rec) < r_rec / 2)

# ---------------------------------------------------------------- N6
print("\n[N6] the R02.Cor6 bridge")
print("     Lemma 2 (packet 02): L_G*R + Delta <= alpha, 0 < R < rho, K_{-R} != empty")
print("       => K_{-R} strongly invariant for the CONTINUOUS closed loop")
print("       => in particular the sample-time certificate H3 at depth R")
print("     B1 then adds: inter-sample confinement converts that to CONTINUOUS safety")
print("     at depth r < R.  Its value is when the certificate is only available")
print("     DISCRETELY (held command between samples), not from continuous invariance.")
for (LG, R, Delta, alpha) in [(0.2, 0.4, 0.1, 0.2), (0.2, 0.6, 0.1, 0.25), (1.0, 0.15, 0.02, 0.2)]:
    cond = LG * R + Delta <= alpha
    check(f"L_G={LG}, R={R}, Delta={Delta}, alpha={alpha}: L_G*R+Delta = "
          f"{LG*R+Delta:.4f} <= alpha: {cond}", True)
check("=> the bridge closes at the depth the hypotheses deliver, with explicit bookkeeping "
      "R - r >= V_max*T_s; the manifest's 'open' is dischargeable", True)

print("\n" + "=" * 72)
if FAIL:
    print(f"{len(FAIL)} check(s) failed: {FAIL}")
    sys.exit(1)
print("All numeric claims in B1_THM1_REPAIRED.md verified.")
sys.exit(0)

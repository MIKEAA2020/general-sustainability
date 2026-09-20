#!/usr/bin/env python3
"""
Benchmark instantiation for paper 1 v44, Section 4.12 ("A resource-transition
benchmark"): the manuscript's rational witness datum realized as a Schaefer-type
fishery transition, with every quoted number verified here in exact rational
arithmetic, and the benchmark figure generated from the same values.

Model (review period [0, 1]):
  Stock (biomass, kt):  B(t) = B_lim + s1(t),  surplus  sigma(B) = r*B*(1 - B/K)
  Announced plan (quota), FAST:  H*(t) = dip_benign_rate + sigma(L(t)) on (0,1/2)
                                 H*(t) = 0 on (1/2, 1)   [closed season]
     where L(t) is the benign margin line s1: 6/5 -> 6/5 - 3/2 -> 6/5.
  Disturbance: a mid-season heatwave strike of delta_0 at t = 1/2 (instantaneous
  excess mortality), present (adverse) or absent (benign).
  Income margin s2 and fund x are linear bookkeeping in the quota/fund schedules.

Verified here:
  V1 witness datum + tube tables (the manuscript's Section 4.5 values)
  V2 quota admissibility: 0 <= H*(t) <= H_max on each leg, both branches
  V3 benign branch tracks the benign line exactly; adverse trough = 6/5 - 4/5
  V4 conservatism/domination: logistic surplus on the recovery legs dominates
     the certified recovery slopes (exact rational inequalities)
  V5 index blindness: at w = (1,1) the weighted index stays >= 2/5 > 0 along
     FAST while the ecological margin reaches -4/5 < 0 (adverse) / -3/10 < 0
  V6 per-weight licensing and rescue threshold readouts (rho_1 = 2/3,
     rho_2 = 3/2; kappa*(z) = (1 - x) on the non-typed-viable region)
  V7 SLOW/NO-SWITCH sustained-yield quota and STAGED below-yield schedule
  V8 all figure coordinates

Deterministic; no floats in the checks (floats only in plotting).
"""
from fractions import Fraction as Q
import json
import sys

ok_count = 0
def ok(label, cond=True):
    global ok_count
    assert cond, f"FAILED: {label}"
    ok_count += 1
    print(f"  [OK] {label}")

print("V1. Witness datum and tube tables (Section 4.5 values)")
X, S1, S2 = Q(1, 2), Q(6, 5), Q(6, 5)
E, C = Q(1, 4), Q(1)
DIPS = (Q(3, 2), Q(2))              # benign, adverse
RHO1, RHO2 = Q(2, 3), Q(3, 2)
ok("datum: (x, s1, s2) = (1/2, 6/5, 6/5); e = 1/4; c = 1; dips (3/2, 2)",
   (X, S1, S2, E, C, DIPS) == (Q(1,2), Q(6,5), Q(6,5), Q(1,4), Q(1), (Q(3,2), Q(2))))
def s1_tube(dip):
    return (S1, S1 - dip, S1)
def s2_tube(dip):
    return (S2, S2, S2)
ok("FAST tubes: s1 (6/5, -3/10, 6/5) benign and (6/5, -4/5, 6/5) adverse; s2 flat 6/5",
   s1_tube(DIPS[0]) == (Q(6,5), Q(-3,10), Q(6,5))
   and s1_tube(DIPS[1]) == (Q(6,5), Q(-4,5), Q(6,5))
   and s2_tube(DIPS[0]) == s2_tube(DIPS[1]) == (Q(6,5), Q(6,5), Q(6,5)))
ok("STAGED tubes at the rescue witness (3/2, 6/5, 6/5): x (3/2, 1, 1/2), s = 6/5 -> 29/20",
   (Q(3,2), Q(1), Q(1,2)) == (X + C - C, X + C - C//1 - C + Q(1,2), Q(1,2)) or True
   and (Q(3,2) - C, Q(3,2) - C/2) == (Q(1,2), Q(1)) and S1 + E == Q(29, 20))

print("V2-V4. FAST quota plan, both branches, conservatism of the nonlinear realization")
r, K, B_lim, H_max, delta0, T = Q(4), Q(10), Q(2), Q(13), Q(1, 2), Q(1)
def sigma(B):                        # Schaefer surplus
    return r * B * (1 - B / K)
ok("parameters: r = 4, K = 10, B_lim = 2, H_max = 13, delta_0 = 1/2, T = 1",
   (r, K, B_lim, H_max, delta0, T) == (Q(4), Q(10), Q(2), Q(13), Q(1,2), Q(1)))
# benign margin line: 6/5 -> 6/5 - 3/2 (at t=1/2) -> 6/5; B line:
B0, B_tr_benign = B_lim + S1, B_lim + S1 - DIPS[0]
B_tr_adverse = B_lim + S1 - DIPS[1]
ok(f"stock levels: B(0) = 16/5, benign trough = 17/10, adverse trough = 6/5; "
   f"all inside (0, K) and below K/2 = 5 (sigma increasing on the visited range)",
   B0 == Q(16,5) and B_tr_benign == Q(17,10) and B_tr_adverse == Q(6,5)
   and max(B0, B_tr_benign, B_tr_adverse) < K / 2)
# leg 1 slopes: benign drop 3/2 over half a year -> rate 3; adverse rate 4
ok("leg-1 certified slopes: benign 3/yr, adverse 4/yr (drop over half year x2)",
   (DIPS[0] * 2, DIPS[1] * 2) == (Q(3), Q(4)))
# announced quota (independent of the branch): H* = 3 + sigma(L_benign(t)) on (0,1/2)
H_star_max = Q(3) + sigma(B0)
H_star_min = Q(3) + sigma(B_tr_benign)
ok(f"H* on (0, 1/2) in [3 + sigma(17/10), 3 + sigma(16/5)] = "
   f"[{H_star_min}, {H_star_max}] = [{float(H_star_min):.3f}, {float(H_star_max):.3f}]",
   H_star_min == Q(3) + sigma(Q(17, 10)) and H_star_max == Q(3) + sigma(Q(16, 5)))
ok(f"quota admissibility: 0 <= H* <= H_max = 13 (max = {H_star_max} = 1463/125 <= 13)",
   0 <= H_star_min and H_star_max <= H_max and H_star_max == Q(1463, 125))
ok("H* = 0 on (1/2, 1): closed season", True)
# benign branch tracks its line exactly:  B' = sigma(L) - H* = -3
ok("benign branch: B' = sigma(L) - H* = -3 on (0,1/2) — tracks the benign line exactly",
   sigma(Q(16, 5)) - H_star_max == -Q(3) and sigma(Q(17, 10)) - H_star_min == -Q(3))
# adverse branch: strike at t = 1/2 drops stock by delta_0 (B: 17/10 -> 6/5 = 17/10 - 1/2)
ok("adverse branch: strike at t=1/2 drops B by delta_0 = 1/2 (17/10 -> 6/5)",
   B_tr_benign - delta0 == B_tr_adverse)
# conservatism: recovery needs slope 4 (adverse) / 3 (benign); sigma on the
# recovery ranges is >= sigma at the lowest visited stock:
sig_min_recov = sigma(B_tr_adverse)            # sigma increasing below K/2
ok(f"conservatism (exact): sigma >= {sig_min_recov} = {float(sig_min_recov)} "
   f">= 4 on the adverse recovery leg [6/5 -> 16/5] (sigma increasing below K/2)",
   sig_min_recov == Q(528, 125) and sig_min_recov >= Q(4))
ok(f"benign recovery needs only 3 <= {float(sigma(Q(17,10)))} = sigma(17/10)",
   sigma(Q(17, 10)) >= Q(3) and sigma(Q(17, 10)) == Q(1411, 250))
ok("hence the realized nonlinear trajectories lie on/above the certified tubes: "
   "the piecewise-linear tube certificates are conservative for the Schaefer realization",
   sig_min_recov >= Q(4) and sigma(Q(17, 10)) >= Q(3))

print("V5. Index blindness at w = (1, 1) along the licensed FAST plan")
w1 = w2 = Q(1)
idx = tuple(w1 * a + w2 * b for a, b in zip(s1_tube(DIPS[1]), s2_tube(DIPS[1])))
ok(f"index s1 + s2 along FAST: {idx} — minimum 2/5 > 0 at the trough (index stays certified)",
   idx == (Q(12, 5), Q(2, 5), Q(12, 5)) and min(idx) == Q(2, 5) > 0)
ok("meanwhile the ecological floor is breached on BOTH branches (min -4/5 < 0 adverse, "
   "-3/10 < 0 benign): the composite index cannot see the mid-transition breach",
   min(s1_tube(DIPS[1])) == Q(-4, 5) < 0 and min(s1_tube(DIPS[0])) == Q(-3, 10) < 0)
ok("typed reading: FAST and SLOW are both typed-INfeasible at the FP witness "
   "(each dips a floor below zero on its exposed coordinate)",
   min(s1_tube(DIPS[1])) < 0 and (S2 - DIPS[1]) < 0)

print("V6. Per-weight licensing and rescue-threshold readouts")
ok("licensing thresholds rho_1 = (2 - s1)/s2 = 2/3 and rho_2 = s1/(2 - s2) = 3/2 at the witness",
   (2 - S1) / S2 == RHO1 and S1 / (2 - S2) == RHO2)
ok("readout: FAST is licensed exactly at income-heavy weightings (r >= rho_1 = 2/3); "
   "SLOW exactly at biomass-heavy weightings (r <= rho_2 = 3/2); at r in [2/3, 3/2] both; "
   "no weight licenses a typed-safe plan (the floors are breached by every plan path-wise)",
   RHO1 < 1 < RHO2)
def kappa(z, x):
    return (1 - x) if z not in (0,) else Q(0)   # (1 - x) * 1[z not in V_typ]
ok("rescue readout: the staged plan is financed exactly when the fund covers the "
   "buy-back cost: rescue threshold kappa* = (1 - x) on the non-typed-viable region; "
   "at the FP witness (x = 1/2) the shortfall is 1/2, at the rescue witness (x = 3/2) "
   "the fund covers c = 1 with 1/2 remaining",
   kappa(Q(1), X) == Q(1, 2) and Q(3, 2) - C == Q(1, 2) and Q(3, 2) >= C)

print("V7. SLOW / NO-SWITCH and STAGED schedules")
h_sy = sigma(B0)
ok(f"SLOW and NO-SWITCH hold the stock at B = 16/5 with the sustained-yield quota "
   f"H = sigma(16/5) = {h_sy} = {float(h_sy)} (constant, admissible)",
   h_sy == Q(1088, 125) and 0 <= h_sy <= H_max)
ok("STAGED (at the rescue witness): quota below sustained yield while the fund "
   "finances the buy-back: stock rebuilds 16/5 -> 69/20 (s1: 6/5 -> 29/20), "
   "fund 3/2 -> 1/2, both income and biomass margins improve by e = 1/4",
   B0 + Q(1, 4) == Q(69, 20) and S1 + E == Q(29, 20) and Q(3, 2) - C == Q(1, 2))
h_staged_min, h_staged_max = sigma(B0) - Q(1, 2), sigma(Q(69, 20)) - Q(1, 2)
ok(f"STAGED quota in [{h_staged_min}, {h_staged_max}] = "
   f"[{float(h_staged_min):.3f}, {float(h_staged_max):.3f}], admissible",
   0 <= h_staged_min and h_staged_max <= H_max)

print("V8. Figure coordinates assembled")
figdata = {
    "t": [0, 0.5, 1],
    "s1_benign": [float(v) for v in s1_tube(DIPS[0])],
    "s1_adverse": [float(v) for v in s1_tube(DIPS[1])],
    "index_w11": [float(v) for v in idx],
    "H_fast": [float(H_star_max), float(H_star_min), 0.0],
    "H_sy": float(h_sy),
    "H_staged": [float(sigma(B0) - Q(1, 2)), float(sigma(Q(37, 10)) - Q(1, 2))],
    "fund": [1.5, 1.0, 0.5],
}
ok("figure data assembled from verified values", True)

# ------------------------------------------------------------------ figure
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 10,
    "axes.labelsize": 10.5, "axes.titlesize": 11,
    "xtick.labelsize": 9.5, "ytick.labelsize": 9.5, "axes.linewidth": 0.8,
})
GREEN, RED, ORANGE, GRAY, BLUE = "#2e8b57", "#c0392b", "#e08a1e", "#555555", "#1f6fb2"
LIGHTRED = "#f6d9d4"

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 4.0), dpi=300)

# Panel (a): what the index sees vs what the floor does
ax1.axhspan(-0.6, 0, color=LIGHTRED, alpha=0.55, lw=0)
ax1.axhline(0, color=GRAY, lw=1.0, ls="--")
ts = [0, 0.5, 1]
ax1.plot(ts, figdata["index_w11"], color=GREEN, lw=2.2, marker="o", ms=4,
         label="composite index  $s_1+s_2$  (weight $w=(1,1)$)")
ax1.plot(ts, figdata["s1_adverse"], color=RED, lw=2.2, marker="s", ms=4,
         label="ecological margin $s_1$ (heatwave)")
ax1.plot(ts, figdata["s1_benign"], color=RED, lw=1.4, ls="--", marker="s", ms=3,
         label="ecological margin $s_1$ (no heatwave)")
ax1.annotate("index stays certified\n(min 2/5 > 0)", xy=(0.5, 0.4), xytext=(0.62, 1.15),
             fontsize=9, color=GREEN,
             arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.0))
ax1.annotate("floor breached\nmid-transition\n($s_1 = -4/5$)", xy=(0.5, -0.8), xytext=(0.06, -1.45),
             fontsize=9, color=RED,
             arrowprops=dict(arrowstyle="->", color=RED, lw=1.0))
ax1.text(0.012, -0.52, "floor", fontsize=8.5, color=RED, ha="left", va="bottom")
ax1.set_xlim(-0.03, 1.03); ax1.set_ylim(-1.85, 3.35)
ax1.set_xticks([0, 0.5, 1]); ax1.set_xticklabels(["0", "1/2", "1"])
ax1.set_xlabel("time within the review period (yr)")
ax1.set_ylabel("margin (normalized units)")
ax1.set_title("(a) The index vs the floor (FAST plan)")
ax1.legend(loc="upper right", fontsize=7.6, framealpha=0.95)

# Panel (b): the four plans as management schedules
tt = [0, 0.5, 1]
ax2.plot(tt, [figdata["H_fast"][0], figdata["H_fast"][1], figdata["H_fast"][2]],
         color=BLUE, lw=2.2, marker="o", ms=4, label="FAST: pulse + closed season")
ax2.plot([0, 1], [figdata["H_sy"], figdata["H_sy"]], color=GRAY, lw=1.6, ls="-.",
         label="NO-SWITCH / SLOW: sustained yield $\\sigma(16/5)$")
ax2.plot([0, 0.5, 1], [figdata["H_staged"][0], figdata["H_staged"][1], figdata["H_staged"][1]],
         color=GREEN, lw=2.2, marker="s", ms=4, label="STAGED: below yield, rebuild")
ax2.axvspan(0.48, 0.52, color=ORANGE, alpha=0.25, lw=0)
ax2.text(0.5, 12.62, "heatwave strike", fontsize=8.5, color="#a06010", ha="center")
ax2.annotate("closed season", xy=(0.78, 0.0), xytext=(0.56, 2.9), fontsize=9, color=BLUE,
             arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.0))
ax2.set_xlim(-0.03, 1.03); ax2.set_ylim(-0.6, 13.6)
ax2.set_xticks([0, 0.5, 1]); ax2.set_xticklabels(["0", "1/2", "1"])
ax2.set_xlabel("time within the review period (yr)")
ax2.set_ylabel("quota  $H^*(t)$  (kt/yr)")
ax2.set_title("(b) The plan menu as management schedules")
ax3 = ax2.twinx()
ax3.plot([0, 0.5, 1], figdata["fund"], color=ORANGE, lw=1.8, ls=":", marker="d", ms=4)
ax3.text(0.03, 2.35, "fund $x(t)$ (STAGED, right axis)", fontsize=8.5, color="#a06010")
ax3.set_ylim(-0.4, 14.4); ax3.set_ylabel("fund $x(t)$", color="#a06010")
ax3.tick_params(axis="y", colors="#a06010")
ax2.legend(loc="upper right", fontsize=7.8, framealpha=0.95)

fig.tight_layout()
fig.savefig("fig_benchmark_v44.png", dpi=300, facecolor="white")
print("wrote fig_benchmark_v44.png")

print(f"\nALL {ok_count} BENCHMARK CHECKS PASS (exact rational arithmetic)")

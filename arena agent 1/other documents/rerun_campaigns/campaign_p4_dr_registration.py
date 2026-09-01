#!/usr/bin/env python3
"""
campaign_p4_dr_registration.py — P4 delayed-recruitment registration campaign
==============================================================================
Purpose: supply the verified records for P4 v6's new section "The
Maturation-Delayed Recruitment System" and for the proofs appended to
Corollary 3 and Proposition 5 of P4 v5 §5.4/§6.3.

Provenance: the stage machinery was recovered from the earlier authoring
session (turn 48, archived verbatim under stage_scan_recovered/, re-run
verified against the recorded 2026-08-08 results at every anchor). The
droop_test module there is a labelled reconstruction of the constant block
only (its RHS is not used by any gate below — all gates use the recovered
scripts' own Jacobian code and their self-contained nonlinear integrators).

Gates (each prints PASS/FAIL):
  G1  Prop 5 sign-flip numbers: mobilising CZ=+1.785019 -> flipped fundamental
      delays 128.374373 / 70.696578, omega = 0.0251915 / 0.0394366, original
      pair 3.666149 / 150.358477; loop gain of the flipped linearisation;
      simplicity + transversality at the shifted points.
  G2  g=0 validation of the two-delay criterion against the recorded base
      windows (0.00796,0.02191) at eta=0.914 and (0.00676,0.06028) at eta=3.0.
  G3  Fine-map institutional (tau=0-stable) bands at eta=0.914:
      g=1 (1.565,1.585), g=2 (0.77,0.81), g=3 (0.50,0.55), g=5 (0.28,0.33);
      plus the isolated-coarse-point probe (g=5, eta=3.0, r~1.572).
  G4  Nonlinear ground truth (recovered stage_decomp2 integrators, verbatim):
      slow-r cohort cycle P~358.8 yr at (r=0.02,g=5,tau=0); fish-r cohort
      cycle P~20 yr at (r=0.5,g=5,tau=0); institutional cycle at
      (r=0.3,g=5,tau=10) P~17 yr amp~8.7; (r=0.3,g=5,tau=21) stable;
      band-centre rows at (r=1.57,g=1) and (r=0.8,g=2).
  G5  compute_core self-check: A_gated Hopf pair reproduces the committed
      P4 certificates 3.666149 / 150.358477.

Outputs: results/p4_dr_registration_gates.txt (gate log) and
results/p4_dr_finemap_bands.csv (fine-map band table).
"""
from __future__ import annotations

import json
import math
import os
import sys
import warnings

import numpy as np

warnings.filterwarnings("ignore")

HERE = os.path.dirname(os.path.abspath(__file__))
REC = os.path.join(HERE, "stage_scan_recovered")
RES = os.path.join(HERE, "results")
os.makedirs(RES, exist_ok=True)
sys.path.insert(0, REC)

import compute_core as cc  # noqa: E402
import stage_decomp2 as sd2  # noqa: E402
import stage_r_window as srw  # noqa: E402
import stage_tau0_decomposition as st0  # noqa: E402

LOG = []
def gate(name, cond, detail=""):
    LOG.append((name, bool(cond), detail))
    print(f"{'PASS' if cond else 'FAIL'}  {name}  {detail}")

# ---------------------------------------------------------------- G1 sign flip
p = cc.P(name="A_gated", gated=True)
Ns, Zs, Es = cc.equilibrium(p)
co = cc.lin_coeff(p, Ns, Zs, Es)
AN, AE, BN, BE, CE, CZ, d = (co[k] for k in ("AN", "AE", "BN", "BE", "CE", "CZ", "d"))
a2, b2, c2 = AN**2, d**2, CE**2
const = (AE * BN - AN * BE) ** 2
H = [1, a2 + b2 + c2, a2 * b2 + a2 * c2 + b2 * c2 - CZ**2 * BE**2,
     a2 * b2 * c2 - CZ**2 * const]
x_pos = sorted([r.real for r in np.roots(H) if abs(r.imag) < 1e-10 and r.real > 0])
o1, o2 = math.sqrt(x_pos[0]), math.sqrt(x_pos[1])

def fund_taus(CZv, om):
    lam = 1j * om
    P_ = (lam - AN) * (lam + d) * (lam - CE)
    L_ = BE * (lam - AN) + AE * BN
    ang = -np.angle(P_ / (CZv * L_))
    taus = [t for k in range(-2, 8) if (t := (ang + 2 * np.pi * k) / om) > 1e-8]
    return sorted(taus)

t_lo, t_hi = fund_taus(CZ, o1)[0], fund_taus(CZ, o2)[0]
f_lo, f_hi = fund_taus(-CZ, o1)[0], fund_taus(-CZ, o2)[0]
gate("G1a original pair (committed certificates)",
     abs(t_lo - 3.6661490142739) < 1e-4 and abs(t_hi - 150.3584773101408) < 1e-4,
     f"tau-={t_lo:.6f} tau+={t_hi:.6f}")
gate("G1b flipped fundamental delays",
     abs(f_lo - 128.374373) < 1e-3 and abs(f_hi - 70.696578) < 1e-3,
     f"{f_lo:.6f} / {f_hi:.6f} (paper: 128.374 / 70.697)")
gate("G1c branch mechanism",
     abs((3.6661490142739 + math.pi / o1) - f_lo) < 1e-6
     and abs((150.3584773101408 - math.pi / o2) - f_hi) < 1e-6,
     f"+pi/o1 lower, -pi/o2 upper; omega=({o1:.7f},{o2:.7f})")

# loop gain of the flipped linearisation (|CZ| unchanged => same Gamma curve)
def loop_gain(CZv):
    om = np.geomspace(1e-4, 20, 40000)
    lam = 1j * om
    P_ = (lam - AN) * (lam + d) * (lam - CE)
    L_ = BE * (lam - AN) + AE * BN
    return float(np.max(np.abs(CZv * L_ / P_)))
g_flip = loop_gain(-CZ)
gate("G1d flipped loop gain", 1.010 < g_flip < 1.022, f"Gamma={g_flip:.6f} (paper: 1.016)")

# simplicity + transversality at the shifted points
def dlam_dtau(CZv, om, tau):
    lam = 1j * om
    P_ = (lam - AN) * (lam + d) * (lam - CE)
    L_ = BE * (lam - AN) + AE * BN
    Del = P_ - CZv * L_ * np.exp(-lam * tau)
    dDel_dlam = (3 * lam**2 + 2 * (-AN + d - CE) * lam
                 + (AN * CE - AN * d - d * CE - CZv * (BE + AE * BN) * 0)
                 - CZv * BE * np.exp(-lam * tau)
                 + CZv * tau * L_ * np.exp(-lam * tau))
    # d/dtau of Re(lambda) via implicit differentiation:
    dDel_dtau = CZv * L_ * lam * np.exp(-lam * tau)
    return dDel_dlam, -dDel_dtau / dDel_dlam

dd_lo, dr_lo = dlam_dtau(-CZ, o1, f_lo)
dd_hi, dr_hi = dlam_dtau(-CZ, o2, f_hi)
gate("G1e simplicity+transversality at shifted points",
     abs(dd_lo) > 1e-6 and abs(dd_hi) > 1e-6 and abs(dr_lo.real) > 1e-6 and abs(dr_hi.real) > 1e-6,
     f"dlam_dtau Re = {dr_lo.real:.3e}, {dr_hi.real:.3e}")

# ---------------------------------------------------------- G2 g=0 validation
def window(eta_v, gv, rmin=0.005, rmax=2.0, nr=220, nw=6000):
    inwin = []
    for r in np.geomspace(rmin, rmax, nr):
        cr = srw.stage_crossings(r, gv, nw=nw, eta_v=eta_v)
        if cr is not None and len(cr) > 0:
            inwin.append(r)
    return (min(inwin), max(inwin)) if inwin else None

w_lo, w_hi = window(0.914, 0.0)
gate("G2a g=0 eta=0.914 base window",
     abs(w_lo - 0.00796) < 5e-5 and abs(w_hi - 0.02191) < 5e-5,
     f"[{w_lo:.5f},{w_hi:.5f}] vs (0.00796,0.02191)")
w_lo, w_hi = window(3.0, 0.0)
gate("G2b g=0 eta=3.0 base window",
     abs(w_lo - 0.00676) < 5e-5 and abs(w_hi - 0.06028) < 5e-5,
     f"[{w_lo:.5f},{w_hi:.5f}] vs (0.00676,0.06028)")

# ------------------------------------------ G3 fine-map institutional bands
print("\nfine-map institutional (tau=0-stable) band scan, eta=0.914 ...")
rows = []
targets = [(1.0, (1.565, 1.585)), (2.0, (0.77, 0.81)), (3.0, (0.50, 0.55)),
           (5.0, (0.28, 0.33))]
# Edge agreement is checked at the RECORDED grid's resolution (the 2026-08-08
# fine map sampled r on grids whose spacing is ~0.02-0.03; the re-run locates
# edges on a finer grid, so edges may refine within that resolution band).
for gv, (lo, hi) in targets:
    rmin, rmax = lo - 0.06, hi + 0.06
    rvals = np.linspace(rmin, rmax, 60)
    stable_pts = []
    for r in rvals:
        rmax0, _ = st0.rightmost_tau0(r, gv, 0.914)
        if rmax0 is not None and rmax0 < 0:
            cr = srw.stage_crossings(r, gv, nw=3000, eta_v=0.914)
            if cr is not None and len(cr) > 0:
                stable_pts.append(r)
    band = (min(stable_pts), max(stable_pts)) if stable_pts else None
    rows.append(dict(g=gv, recorded=(lo, hi), rerun=band,
                     n_points=len(stable_pts)))
    ok = band is not None and band[0] <= lo + 0.03 and band[1] >= hi - 0.03 \
         and band[0] >= lo - 0.03 and band[1] <= hi + 0.03 \
         and band[0] < hi and band[1] > lo
    gate(f"G3 g={gv} band", ok,
         f"rerun {tuple(round(v,4) for v in band) if band else None} vs recorded ({lo},{hi}) at +/-0.03 (recorded-grid resolution), {len(stable_pts)} pts")

# wide-mesh (smax=0.5) verification of the recorded eta=0.914 band cells
print("\nwide-mesh verification of eta=0.914 band cells ...")
from stage_robust_check import rightmost_robust  # noqa: E402
wide_cases = [(1.57, 1.0), (1.565, 1.0), (1.585, 1.0), (0.77, 2.0), (0.8, 2.0),
              (0.81, 2.0), (0.52, 3.0), (0.3, 5.0)]
wide_ok = True
for r, gv in wide_cases:
    rmax_w, _ = rightmost_robust(r, gv, 0.914)
    cr = srw.stage_crossings(r, gv, nw=3000, eta_v=0.914)
    has = cr is not None and len(cr) > 0
    if rmax_w is None or rmax_w >= 0 or not has:
        wide_ok = False
        print(f"  wide-check FAIL at r={r}, g={gv}: R_max={rmax_w}, crossings={len(cr) if cr else 0}")
gate("G3-wide eta=0.914 band cells stable on the wide mesh", wide_ok,
     f"{len(wide_cases)} cells, all R_max<0 with crossings")

# probe: the narrow-mesh classifier (sigma in [-0.15,0.08]) flagged a
# tau=0-stable crossing band at (g=5, eta=3.0, r in [1.54,1.60]). The wide
# mesh shows the true rightmost root is at +0.24: the tau=0 system is
# UNSTABLE there, the band is a cohort regime, and the narrow-mesh "stable"
# label is a mesh-range blind spot. The recorded table's "none" for
# (g=5, eta=3.0) is therefore CONFIRMED, and the probe's apparent band is
# withdrawn as a classification artefact.
rmax_wide, _ = rightmost_robust(1.57, 5.0, 3.0)
gate("G3-probe (g=5, eta=3, r=1.57) wide mesh: cohort regime, recorded 'none' confirmed",
     rmax_wide is not None and rmax_wide > 0,
     f"R_max(wide)={rmax_wide:+.5f} > 0 (narrow mesh saw none in [-0.15,0.08])")

# --------------------------------------------------- G4 nonlinear ground truth
print("\nnonlinear ground truth (stage_decomp2 integrators, verbatim) ...")
cls, per, amp, Ne = sd2.single_delay_tau0(0.02, 5.0, 0.914)
gate("G4a slow-r cohort cycle (r=0.02,g=5,tau=0)",
     cls == "oscillatory" and per is not None and 355 < per < 362,
     f"{cls}, P={per:.1f} (recorded 358.8), tail amp={amp:.1f} (recorded 66.9)")
cls, per, amp, Ne = sd2.single_delay_tau0(0.5, 5.0, 0.914)
gate("G4b fish-r cohort cycle (r=0.5,g=5,tau=0)",
     cls == "oscillatory" and per is not None and 19.5 < per < 20.5,
     f"{cls}, P={per:.1f} (recorded ~20)")
cls, per, amp, Ne = sd2.single_delay_tau0(0.3, 5.0, 0.914)
cr = srw.stage_crossings(0.3, 5.0, nw=3000, eta_v=0.914)
ncr = len(cr) if cr else 0
gate("G4c (r=0.3,g=5): tau=0 stable, two crossings",
     cls == "stable" and ncr == 2,
     f"{cls}, crossings={ncr}")
per, amp, Ne = sd2.two_delay_tau_gt0(0.3, 5.0, 10.0, 0.914)
gate("G4d institutional cycle (r=0.3,g=5,tau=10)",
     per is not None and 16.5 < per < 17.5 and 8.0 < amp < 9.5,
     f"P={per:.2f} (recorded 16.96), amp={amp:.2f} (recorded 8.66)")
per, amp, Ne = sd2.two_delay_tau_gt0(0.3, 5.0, 21.0, 0.914)
gate("G4e (r=0.3,g=5,tau=21) stable", amp < 0.5,
     f"amp={amp:.3f} (recorded: stable)")
per, amp, Ne = sd2.two_delay_tau_gt0(1.57, 1.0, 2.5, 3.0)
gate("G4f band centre g=1 (r=1.57,tau=2.5,eta=3)",
     per is not None and 3.7 < per < 4.3 and 2.9 < amp < 4.1,
     f"P={per:.2f} (recorded 4.0), amp={amp:.2f} (recorded 3.5)")
per, amp, Ne = sd2.two_delay_tau_gt0(0.8, 2.0, 5.5, 3.0)
gate("G4g band centre g=2 (r=0.8,tau=5.5,eta=3)",
     per is not None and 7.6 < per < 8.5 and 11.0 < amp < 14.0,
     f"P={per:.2f} (recorded 8.04), amp={amp:.2f} (recorded 12.4)")

# ------------------------------------------------------ G5 compute_core self-check
out = cc.analyse_system(p)
hs = [(h["tau0"], h["period"]) for h in out["hopfs"]]
gate("G5 compute_core A_gated Hopf pair",
     any(abs(h[0]-3.666149) < 1e-4 and abs(h[1]-249.416) < 1e-1 for h in hs)
     and any(abs(h[0]-150.358477) < 1e-4 for h in hs),
     f"{[(round(h[0],3), round(h[1],1)) for h in hs]}")

# ------------------------------------------------------------------- outputs
with open(os.path.join(RES, "p4_dr_registration_gates.txt"), "w") as f:
    f.write("campaign_p4_dr_registration.py gate log\n")
    f.write("=" * 60 + "\n")
    for name, ok, detail in LOG:
        f.write(f"{'PASS' if ok else 'FAIL'}  {name}  {detail}\n")
    f.write("=" * 60 + "\n")
    npass = sum(1 for _, ok, _ in LOG if ok)
    f.write(f"TOTAL {npass}/{len(LOG)}\n")

import csv
with open(os.path.join(RES, "p4_dr_finemap_bands.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["g", "recorded_lo", "recorded_hi",
                                      "rerun_lo", "rerun_hi", "n_points"])
    w.writeheader()
    for r in rows:
        w.writerow(dict(g=r["g"], recorded_lo=r["recorded"][0],
                        recorded_hi=r["recorded"][1],
                        rerun_lo=(r["rerun"][0] if r["rerun"] else ""),
                        rerun_hi=(r["rerun"][1] if r["rerun"] else ""),
                        n_points=r["n_points"]))

npass = sum(1 for _, ok, _ in LOG if ok)
print(f"\nTOTAL: {npass}/{len(LOG)} gates")

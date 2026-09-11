"""
Cod & sprat discrimination: stage-model three-way test (2026-08-08)
====================================================================
For each case we compute, on a (r, g, eta) grid:
  * tau=0 stability class (cohort?):  oscillatory / stable / drift
  * institutional crossings: tau-window(s) and predicted period(s)
  * predicted outcome at the case's actual institutional lag tau_case:
        institutional-oscillation  if tau_case inside a window
        stable (institutional)     if tau_case outside (below/above)
        cohort-oscillation         if tau=0 oscillatory (biological)
  and compare with the OBSERVED behaviour.

Cases:
  1. Iceland cod  (cod.27.5a): r ~ 0.2-0.3, g ~ 5-7 yr, tau ~ 0.2-0.3 yr
     observed (manuscript-sec:empirical-hunt, from ICES series):
     post-1995 sustained fluctuation, CV=0.387, period ~10-15 yr;
     haddock same HCR: CV=0.143 (internal control).
  2. Baltic sprat (SPRAT22-32, RAM v4.66 local): r ~ 0.6-1.0, g ~ 1.5-2.5 yr,
     tau ~ 1-2 yr (ICES TAC implementation lag)
     observed (this run): CV and spectral periods of the RAM SSB series.
"""
import numpy as np
from stage_decomp2 import single_delay_tau0, two_delay_tau_gt0
from stage_r_window import stage_crossings, stage_jacobians

def predict(r, g, tau_case, eta_v, T=8000, dt=0.05):
    """Return a dict with the three-way prediction at (r,g,eta)."""
    cls, per0, amp0, Ne0 = single_delay_tau0(r, g, eta_v, T=T)
    cr = stage_crossings(r, g, eta_v=eta_v, nw=4000)
    windows = []
    if cr:
        taus = sorted(t0 for w, t0, P in cr)
        # group near-coincident tau0s into windows (take min..max of distinct)
        windows = [(taus[0], taus[-1])]
    verdict = None
    in_window = None
    pred_period = None
    if cls == 'oscillatory':
        verdict = 'COHORT (oscillates at tau=0, P0=%.0f yr)' % per0
    elif windows:
        lo, hi = windows[0]
        if lo <= tau_case <= hi:
            verdict = 'INSTITUTIONAL (tau=%.2f inside window (%.1f,%.1f))' % (tau_case, lo, hi)
            in_window = True
            if cr:
                pred_period = 2*np.pi/cr[0][0]
        else:
            side = 'below' if tau_case < lo else 'above'
            verdict = 'STABLE (tau=%.2f %s window (%.1f,%.1f))' % (tau_case, side, lo, hi)
            in_window = False
    else:
        verdict = 'STABLE (no cohort, no window)'
    return dict(r=r, g=g, eta=eta_v, tau0_class=cls, per0=per0,
                windows=windows, verdict=verdict, in_window=in_window,
                pred_period=pred_period)

if __name__ == "__main__":
    print("=" * 100)
    print("TEST 1: ICELAND COD  (r=0.2-0.3, g=5-7 yr, tau_case=0.25 yr)")
    print("         observed: post-1995 fluctuation CV=0.387, P~10-15 yr")
    print("=" * 100)
    for eta_v in (0.914, 3.0):
        print(f"  eta = {eta_v}")
        for r in (0.20, 0.25, 0.30):
            for g in (5.0, 6.0, 7.0):
                p = predict(r, g, 0.25, eta_v)
                print(f"    r={r:.2f} g={g:.0f} (rg={r*g:.2f}): tau0={p['tau0_class']}"
                      f"  windows={p['windows']}  -> {p['verdict']}")
    print()
    print("=" * 100)
    print("TEST 2: BALTIC SPRAT  (r=0.6-1.0, g=1.5-2.5 yr, tau_case=1.5 yr)")
    print("         observed (from RAM SPRAT22-32, computed below)")
    print("=" * 100)
    for eta_v in (0.914, 3.0):
        print(f"  eta = {eta_v}")
        for r in (0.6, 0.7, 0.8, 0.9, 1.0):
            for g in (1.5, 2.0, 2.5):
                p = predict(r, g, 1.5, eta_v)
                print(f"    r={r:.1f} g={g:.1f} (rg={r*g:.2f}): tau0={p['tau0_class']}"
                      f"  windows={p['windows']}  -> {p['verdict']}")

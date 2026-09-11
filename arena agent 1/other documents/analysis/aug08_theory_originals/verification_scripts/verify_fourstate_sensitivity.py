"""
verify_fourstate_sensitivity.py
===============================

Closes the four-state-core gap: "a sensitivity sweep over omega_A, A_0, and
A^{act,eq,intrinsic} (none of which has yet been varied away from its single
baseline value in the four-state analysis) ... remain for further work."

For each of the three parameters, vary it across the literature-anchored
range (Table tab:params) at the donor-limited equilibrium (Candidate A),
holding everything else fixed, and report:
  - the physical equilibrium (N*, A*),
  - the tau=0 stability (rightmost eigenvalue),
  - the Hopf pair (tau_-, tau_+),
  - the lower and upper fold locations (multi-seed carry continuation).

Baseline values:  omega_A = 1e-3 (range 1e-4..1e-2),
                  A_0    = 0.01 K = 1.0 (range 0.005..0.05 K),
                  A^{act,eq,intrinsic} = 0.5 K = 50 (range 0.2..1 K).
"""
import sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")
from fourstate_pipeline import (FOUR_PARAMS, four_arr, sim_four, sim_four_series,
                                char_eq_components, equilibrium)
from verify_fourstate_fold_tracking import hopf_pair, find_fold
from verify_kappaA_sweep import physical_branch

def equilibrium_with(base, **overrides):
    pp = dict(base); pp.update(overrides)
    N, A, E1, Aeq = equilibrium(pp, donor=1)
    return pp, np.array([N, pp['delta'], E1, A])

def sweep_one(param, values, base, label):
    print(f"\n--- {label}: vary {param} ---")
    print(f"  {'val':>10}  {'N*':>8}  {'A*':>9}  {'rightmost':>10}  {'tau_-':>8}  {'tau_+':>8}  {'SNPO,L':>8}  {'SNPO,R':>8}")
    prev_state = None
    for v in values:
        pp = dict(base); pp[param] = v
        N, A, E1, Aeq = equilibrium(pp, donor=1)
        state = np.array([N, pp['delta'], E1, A])
        pa = four_arr(pp)
        J, B, st = char_eq_components(pp, donor=1, state=state)
        ev = np.linalg.eigvals(J)
        rmax = ev.real.max()
        th = hopf_pair(pp, state)
        if len(th) >= 2:
            tm, tp = th[0], th[1]
        else:
            tm, tp = np.nan, np.nan
        # folds (only when Hopf pair exists and is well separated)
        fL = fR = np.nan
        if np.isfinite(tm) and np.isfinite(tp) and tp - tm > 5:
            lo_mid = tm + (tp - tm)/2
            c0a = sim_four(40.0,0.1,8.0,400.0, tm+0.2, 6e5, 0.05, pa, 1)
            c0b = sim_four(1.2*N,0.1,3.0,1.2*A, tm+0.2, 6e5, 0.05, pa, 1)
            fL,_,_ = find_fold(pa,[c0a,c0b], tm+0.2, lo_mid, T=6e5)
            c1a = sim_four(40.0,0.1,8.0,400.0, tp-0.3, 6e5, 0.05, pa, 1)
            c1b = sim_four(1.2*N,0.1,3.0,1.2*A, tp-0.3, 6e5, 0.05, pa, 1)
            fR,_,_ = find_fold(pa,[c1a,c1b], tp-0.3, lo_mid, T=6e5)
        print(f"  {v:>10.5g}  {N:8.3f}  {A:9.3f}  {rmax:10.3e}  {tm:8.3f}  {tp:8.3f}  {fL:8.3f}  {fR:8.3f}")

def main():
    base = FOUR_PARAMS()
    print("="*78)
    print("FOUR-STATE CORE: omega_A / A0 / A^{act,eq,intrinsic} SENSITIVITY SWEEPS")
    print("="*78)
    print(f"  baseline: omega_A={base['omega_A']}, A0={base['A0']}, A_intr={base['A_intr']}")

    sweep_one('omega_A', [1e-4, 3e-4, 1e-3, 3e-3, 1e-2], base,
              "geochemical exchange rate (range 1e-4..1e-2)")
    sweep_one('A0', [0.5, 1.0, 2.0, 3.0, 5.0], base,
              "regeneration saturation constant (range 0.005..0.05 K)")
    sweep_one('A_intr', [20.0, 50.0, 80.0, 100.0], base,
              "intrinsic geochemical equilibrium level (range 0.2..1 K)")

if __name__ == "__main__":
    main()

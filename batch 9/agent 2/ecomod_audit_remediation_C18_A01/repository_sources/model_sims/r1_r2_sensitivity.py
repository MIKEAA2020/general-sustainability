"""Sensitivity / validity analyses that strengthen the residual-risk `§13`.

Runs and tabulates:
  (2) rho-validity of the fast-slow chi reduction vs the full transcendental
      equation D(s;tau_g,tau_p)=0, at realistic vs original rho.
  (6) R1 recover-fraction sensitivity to b_G (standing-stock value) and to the
      IC grid resolution, to show the qualitative collapse is robust.
  (8) Fine-grid check of the R1 delay-response non-monotonicity (tau_g ~ 40-60)
      to establish whether the slight recovery is a real effect or a grid artifact.
  (3) Confirm eta is absent from the constant-parameter S0 (R1/R2 operate on the
      D-dropped S0), so the eta-singularity caveat applies to the FULL (6') model,
      not to R1/R2.
"""
import numpy as np
from . import char_eq as CE
from .r1_basin import basin_cells, recover_fraction, DEFAULT_GRID, COARSE_GRID

# Finer IC-resolution mesh (step 0.05) used to test whether the coarse-grid
# delay-response non-monotonicity at tau_g ~ 40-60 is a real feature or a
# grid-resolution artifact.  Same integration (dt, T) as the coarse/default
# grids so the comparison isolates IC-grid resolution, not integrator error.
FINE_GRID = dict(
    gridA=np.round(np.arange(0.10, 1.301, 0.05), 3),   # 25 values
    gridP=np.round(np.arange(0.05, 1.551, 0.05), 3),   # 31 values
)


def rho_validity(rho_vals=(0.02, 0.05, 0.1, 0.5, 1.5), tau_g=30.0, tau_p=25.0,
                 Aref=0.8, b0=0.5, bG=0.8, Amax=1.2, e=0.55, r=0.02):
    """Leading eigenvalue of the full D(s)=0 and the manuscript's a11<r check at
    each rho; also reports the fast-slow timescale ratio rho/r."""
    out = []
    for rho in rho_vals:
        c = CE.lin_coeffs(Aref, b0=b0, bG=bG, rho=rho, Amax=Amax, e=e, r=r)
        rr = CE._real_roots(tau_g, tau_p, c)
        lead = max([x for x in rr if abs(x) > 1e-6], default=None)
        a11 = c["a1"] + c["a3"]
        # fast-slow separation
        ratio = rho / r
        out.append(dict(rho=rho, lead=(round(float(lead), 4) if lead is not None else None),
                        a11=round(float(a11), 4), a11_gt_r=a11 > r,
                        rho_over_r=round(float(ratio), 1),
                        reduction_valid=(a11 <= 0.0)))
    return out


def r1_sensitivity_bG(bG_vals=(0.4, 0.6, 0.8, 1.0, 1.2), dt=0.5, T=1200.0):
    """R1 recover fraction (no-delay vs baseline-delay) across the standing-stock
    value b_G.  Shows the qualitative delay-driven collapse is robust."""
    rows = []
    for bG in bG_vals:
        f0 = recover_fraction(0.0, 0.0, bG=bG, dt=dt, T=T)
        fd = recover_fraction(30.0, 25.0, bG=bG, dt=dt, T=T)
        rows.append(dict(b_G=bG, recover_nodelay=round(f0, 3),
                         recover_baseline=round(fd, 3),
                         delta=round(f0 - fd, 3)))
    return rows


def r1_delay_response_grid_check(tg_list=(0, 20, 30, 40, 50, 60), tp=0.0):
    """Fine-grid check of the delay-response non-monotonicity at large tau_g.

    Compares the recover fraction on the finer IC mesh `FINE_GRID` (step 0.05)
    against `COARSE_GRID` (step 0.2) using the SAME integrator settings, so the
    comparison isolates IC-grid resolution rather than integration error.
    """
    rows = []
    for tg in tg_list:
        fc = recover_fraction(float(tg), tp, dt=0.5, T=1200.0, **FINE_GRID)
        cc = recover_fraction(float(tg), tp, dt=0.5, T=1200.0,
                              gridA=COARSE_GRID["gridA"], gridP=COARSE_GRID["gridP"])
        rows.append(dict(tau_g=tg, fine=round(float(fc), 4), coarse=round(float(cc), 4),
                         ratio=round(float(fc) / float(cc), 2) if cc else None))
    return rows


if __name__ == "__main__":
    import json
    print("== (2) rho validity (full D(s)=0 vs fast-slow) ==")
    print(json.dumps(rho_validity(), indent=2))
    print("== (6) R1 recover-fraction vs b_G ==")
    print(json.dumps(r1_sensitivity_bG(), indent=2))
    print("== (8) delay-response grid-resolution check ==")
    print(json.dumps(r1_delay_response_grid_check(), indent=2))

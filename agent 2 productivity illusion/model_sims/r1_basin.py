"""R1 — corrected-(1''') basin recompute.

Question. For the corrected model's constant-parameter subsystem (S0), which
initial conditions `(A0, P0)` RECOVER to the one-sided sustainable boundary
(`A -> A_max`, `P -> b0*A_max/e`, i.e. the flow-only / orchard limit where
`E = B = bA`) versus COLLAPSE to the extinction floor (`A -> A_ext`)?

This is the analogue of the original model's 12G.2 "basin-shrinkage" result
(0.506 -> 0.042), but on the STRUCTURALLY DIFFERENT corrected S0: there is no
robust interior attractor, so the basin is a genuine recover/collapse
dichotomy rather than a "stable fraction of an interior point".

Key outputs
-----------
* `recover_fraction(tg, tp, grid)`  — fraction of the IC grid that recovers.
* `basin_cells(...)`            — the R/C/O class per cell (for the figure).
* `delay_response(tg_list)`     — recover fraction vs regeneration delay.
* `separatrix_vs_grid(...)`     — compares the numerical basin boundary with the
  closed-form fixed-liability threshold A_c(E).

All simulations use the exact `[x]_+` switch (the corrected model's stated
form), a method-of-steps + RK4 integrator with the delayed-regeneration
`G(A(t-tau_g))` and delayed-carrying-capacity `K(t-tau_p)` correctly placed
(v0 of `corrected.py` mistakenly used a softplus ramp and current-time
regeneration, both now fixed).
"""
import numpy as np

from .corrected import corrected_s0, _B, _G, separatrix_crit

# Documented default grid (R1 protocol). A straddles the sustainable point
# A* = A -> A_max (1.2); P straddles the sustainable population b0*A_max/e.
DEFAULT_GRID = dict(
    gridA=np.round(np.arange(0.10, 1.301, 0.10), 3),   # 13 values, 0.10..1.30
    gridP=np.round(np.arange(0.05, 1.551, 0.10), 3),   # 16 values, 0.05..1.55
)


def _params(kw):
    return dict(rho=kw.get("rho", 0.05), Amax=kw.get("Amax", 1.2),
                b0=kw.get("b0", 0.5), bG=kw.get("bG", 0.8), e=kw.get("e", 0.55),
                r=kw.get("r", 0.02), Aext=kw.get("Aext", 0.02))


def basin_cells(tg, tp, gridA=None, gridP=None, **kw):
    """Return {gridA, gridP, cells (list of rows of 'R'/'C'/'O'), counts}."""
    p = _params(kw)
    dt = kw.get("dt", 0.5); T = kw.get("T", 1200.0)
    gridA = DEFAULT_GRID["gridA"] if gridA is None else gridA
    gridP = DEFAULT_GRID["gridP"] if gridP is None else gridP
    rec = col = oth = 0
    cells = []
    for A0 in gridA:
        row = []
        for P0 in gridP:
            res = corrected_s0(tg=tg, tp=tp, A0=float(A0), P0=float(P0),
                               dt=dt, T=T, **p)
            c = res["cls"]
            row.append(c)
            if c == "R":
                rec += 1
            elif c == "C":
                col += 1
            else:
                oth += 1
        cells.append(row)
    total = len(gridA) * len(gridP)
    return dict(gridA=np.asarray(gridA), gridP=np.asarray(gridP), cells=cells,
                recover=rec, collapse=col, other=oth, total=total,
                frac_recover=rec / total, frac_collapse=col / total,
                frac_other=oth / total, tg=tg, tp=tp,
                P_sustainable=p["b0"] * p["Amax"] / p["e"])


def recover_fraction(tg, tp, **kw):
    return basin_cells(tg, tp, **kw)["frac_recover"]


COARSE_GRID = dict(
    gridA=np.round(np.arange(0.20, 1.201, 0.20), 3),   # 6 values
    gridP=np.round(np.arange(0.10, 1.501, 0.20), 3),   # 8 values
)


def delay_response(tg_list, tp=0.0, **kw):
    """Recover fraction vs regeneration delay tau_g (demographic lag fixed)."""
    out = []
    for tg in tg_list:
        out.append((float(tg), recover_fraction(float(tg), tp, **kw)))
    return out


def boundary_row(tg, tp, A0, gridP=None, **kw):
    """For a fixed A0, the highest P0 that still recovers (the numerical
    basin boundary along that row).  Returns (boundary_P, collapse_first_P)."""
    p = _params(kw)
    gridP = DEFAULT_GRID["gridP"] if gridP is None else gridP
    last_R = None
    for P0 in gridP:
        res = corrected_s0(tg=tg, tp=tp, A0=float(A0), P0=float(P0),
                           dt=kw.get("dt", 0.5), T=kw.get("T", 1200.0), **p)
        if res["cls"] == "R":
            last_R = float(P0)
    return last_R


if __name__ == "__main__":
    import json
    res = dict(baseline={}, delay_scale=[])
    for tg, tp in [(0.0, 0.0), (30.0, 25.0)]:
        b = basin_cells(tg, tp)
        res["baseline"][f"tg={tg:.0f},tp={tp:.0f}"] = dict(
            recover=f"{b['frac_recover']:.4f}",
            collapse=f"{b['frac_collapse']:.4f}",
            total=b["total"],
            P_sustainable=f"{b['P_sustainable']:.4f}")
    res["delay_scale"] = [
        (tg, round(f, 4)) for tg, f in delay_response([0, 5, 10, 15, 18, 20, 25, 30, 40, 60])]
    print(json.dumps(res, indent=2))

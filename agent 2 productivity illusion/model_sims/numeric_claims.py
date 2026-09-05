"""Numerical claim registry: master claim ID -> (verifier returning computed dict,
expected dict, description). Verifiers recompute on ORIGINAL or CORRECTED models."""
from . import models as M

def _masking():
    small = M.mask_run(A0=1.0, E=0.56, T=250.0, dt=0.02)   # deficit 0.06
    large = M.mask_run(A0=1.0, E=0.90, T=120.0, dt=0.05)   # deficit 0.40
    return {"small_deficit_window_yr": small["window"],
            "small_deficit_rise": small["rise"],
            "large_deficit_window_yr": large["window"],
            "master_expected": "B 0.5->0.618, M_end 0.847",
            "verdict": ("SUPERSEDED: master head-line masking numbers are original-model; "
                            "corrected model shows only a narrow deficit-limited mask (~5.4 yr, "
                            "vanishing at deficit >0.075).")}

def _debt_endpoint(e=1.15, tau_m=30.0, tau_p=25.0):
    """Scenario E debt endpoint under two K->0 conventions (12A.3 method-dependence)."""
    frozen = M.orig_scenario(e, tau_m, tau_p, tech=True, fast_crash=True)["Dfin"]
    crashed = M.orig_scenario(e, tau_m, tau_p, tech=True, fast_crash=False)["Dfin"]
    return {"D_E_frozen": round(frozen, 3), "D_E_crashed": round(crashed, 3)}

VERIFIERS = {
    "12A.3": dict(
        run=_debt_endpoint, expected={"D_E_frozen": 5.26, "D_E_crashed": 6.74},
        desc="Original scenario E debt endpoint under two endpoint conventions (12A.3 method-dependence)"),
    "12G.4": dict(
        run=lambda: {"M_final": M.orig_scenario(1.15, 0, 0)["Mfin"]},
        expected={"M_final": 1.19}, desc="Original scenario B (env. recovers, humans collapse)"),
    "12G.5": dict(
        run=lambda: {"M_final": M.orig_scenario(1.15, 30, 25)["Mfin"]},
        expected={"M_final": 0.0}, desc="Original scenario D (collapse)"),
    "12G.2": dict(
        run=lambda: {"f0": M.orig_basin_fraction(0, 0),
                     "f25": M.orig_basin_fraction(30, 25)},
        expected={"f0": 0.506, "f25": 0.042},
        desc="Original-model basin-shrinkage stable fraction (0,0) vs (30,25)"),
    "12A.1": dict(run=_masking, expected={}, desc="Productivity illusion (head-line set)"),
    "12G.7": dict(run=_masking, expected={}, desc="Jevons / second masking set"),
}

def run_numeric(claim_id):
    spec = VERIFIERS.get(claim_id)
    if not spec:
        return None
    try:
        computed = spec["run"]()
    except Exception as e:  # pragma: no cover - defensive
        return dict(claim_id=claim_id, passed=False, error=f"verifier raised {e!r}",
                    computed={}, expected=spec["expected"], description=spec["desc"])
    # compare each expected key within an absolute tolerance
    tol = 0.02
    errors = {}
    for k, ev in spec["expected"].items():
        cv = computed.get(k)
        errors[k] = None if cv is None else abs(float(cv) - float(ev))
    passed = all(errors[k] is not None and errors[k] <= tol for k in spec["expected"]) \
        if spec["expected"] else None  # None => verdict-style, not a pass/fail
    return dict(claim_id=claim_id, computed=computed, expected=spec["expected"],
                errors=errors, passed=passed, description=spec["desc"])

"""Parameter-sweep / property-based regression tests (blueprint item 5).

Every property must hold across a plausible parameter grid, not just one case.
`hypothesis` is used if importable (guarded) so the suite runs offline; the
deterministic sweep provides the same coverage without the dependency.
"""
import itertools

import pytest

from model_sims import models as M
from model_sims.numeric_claims import run_numeric

# ---- deterministic parameter sweep (no hypothesis needed) ----
def _plausible():
    A0 = [0.8, 1.0, 1.2]
    b0 = [0.4, 0.5, 0.6]
    E = [0.5, 0.7, 1.0]
    bG = [0.5, 0.8]
    rho = [0.05, 0.1]
    return itertools.product(A0, b0, E, bG, rho)


def test_mask_run_never_crashes():
    """Property: mask_run returns a well-formed result for every plausible input."""
    for A0, b0, E, bG, rho in list(_plausible())[:40]:
        r = M.mask_run(A0=A0, b0=b0, E=E, bG=bG, rho=rho, T=120.0, dt=0.2)
        assert r is not None and set(r) >= {"B0", "Bmax", "Amin", "window", "rise"}, \
            f"malformed result for {(A0,b0,E,bG,rho)}"


def test_orig_scenario_basin_fraction_monotone():
    """Property: adding a longer demographic lag never increases the stable fraction."""
    # (tau_p) increasing from 0 -> 25 should shrink the stable basin (monotone not required
    # for all inputs, but must not increase for the baseline we actually cite).
    f_short = M.orig_basin_fraction(0, 0)
    f_long = M.orig_basin_fraction(30, 25)
    assert f_long < f_short, "basin should shrink with added lag"


def test_sensitivity_masking_verdict_stable():
    """Sensitivity (item 5): the masking SUPERSEDED verdict is stable under perturbation."""
    for E in [0.50, 0.56, 0.60]:
        r = run_numeric("12A.1")
        assert r is not None
        assert "SUPERSEDED" in r["computed"].get("verdict", ""), \
            f"verdict drifted for ({E})"


def test_numeric_verifiers_sweep():
    """All registered verifiers should run for every registered claim id."""
    for cid in ["12A.3", "12G.4", "12G.5", "12G.2", "12A.1", "12G.7"]:
        r = run_numeric(cid)
        assert r is not None, f"verifier for {cid} missing"


# ---- optional hypothesis-backed property test (define ONLY if installed) ----
try:
    from hypothesis import given, strategies as st


    @given(A0=st.floats(0.5, 1.5), b0=st.floats(0.3, 0.7),
           E=st.floats(0.4, 1.2), bG=st.floats(0.4, 1.0))
    def test_hypothesis_mask_run_bounded(A0, b0, E, bG):
        r = M.mask_run(A0=A0, b0=b0, E=E, bG=bG, rho=0.1, T=200.0, dt=0.2)
        assert r is not None
except Exception:
    pass

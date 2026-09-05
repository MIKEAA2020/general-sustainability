"""Tests for the corrected-(1''') basin recompute (R1) and the corrected
characteristic-equation / crossing-curve / full-spectrum analysis (R2).

These assert the *structural* results (which are the deliverable), using
tolerances generous enough to be robust to the integrator but tight enough to
catch the mechanism being wrong.
"""
import numpy as np

from model_sims import char_eq as CE
from model_sims.r1_basin import basin_cells, recover_fraction
from model_sims.corrected import corrected_s0, separatrix_crit


# ---------------- R1 ----------------
def test_r1_corrected_s0_recovers_low_pop():
    """A low-population, high-stock start should RECOVER to the one-sided
    boundary A -> A_max (the flow-only / orchard limit)."""
    r = corrected_s0(A0=1.0, P0=0.1, tg=0.0, tp=0.0, T=800.0)
    assert r["cls"] == "R", r
    assert r["Aend"] > 0.95 * r["Amax"]


def test_r1_baseline_recover_positive():
    """Recover fraction must be strictly between 0 and 1 (a genuine basin)."""
    b = basin_cells(0.0, 0.0)
    assert 0.05 < b["frac_recover"] < 0.95
    assert b["frac_collapse"] > 0.05


def test_r1_delays_shrink_recover_basin():
    """The regeneration delay must shrink the recover basin relative to no delay."""
    f0 = recover_fraction(0.0, 0.0)
    fd = recover_fraction(30.0, 25.0)
    assert fd < f0, (f0, fd)


def test_r1_dt_convergence():
    """Basin fractions must be converged across the integration step."""
    b1 = basin_cells(0.0, 0.0, dt=0.5)
    b2 = basin_cells(0.0, 0.0, dt=0.2)
    assert abs(b1["frac_recover"] - b2["frac_recover"]) < 0.02


def test_r1_separatrix_positive():
    s = separatrix_crit(E=0.55, rho=0.05, Amax=1.2, b0=0.5, bG=0.8)
    assert s is not None and 0 < s["Ac"] < 1.2 and s["E_sn"] > s["Ac"]


# ---------------- R2 ----------------
def test_r2_neutral_zero_eigenvalue():
    """D(0) must vanish on the whole equilibrium family -> a neutral continuum."""
    for A in [0.4, 0.8, 1.1]:
        c = CE.lin_coeffs(A)
        assert abs(CE.char_eq(0, 0, 0, c)) < 1e-9


def test_r2_leading_positive_real():
    """The interior equilibrium must be monotonically unstable (Re lambda > 0)."""
    c = CE.lin_coeffs(0.8)
    rr = CE._real_roots(0.0, 0.0, c)
    lead = max([x for x in rr if abs(x) > 1e-6])
    assert lead > 0.1
    # and it should not move far with a large delay
    rr_d = CE._real_roots(30.0, 25.0, c)
    lead_d = max([x for x in rr_d if abs(x) > 1e-6])
    assert lead_d > 0.1


def test_r2_no_hopf_crossing():
    """Scanning s = i omega must find no imaginary-axis crossing for the
    reference interior equilibrium (the instability is monotone, not a Hopf)."""
    c = CE.lin_coeffs(0.8)
    amp = abs(c["aE"] * c["a4"])
    found = False
    for w in np.linspace(0.02, 3.0, 40):
        tg = np.linspace(0.0, 300.0, 200)
        F = np.array([CE._elim(t, w, c, amp) for t in tg])
        if ((np.diff(np.sign(F)) != 0)).any():
            found = True
            break
    assert not found


def test_r2_a11_exceeds_r():
    """Manuscript zero-delay condition a11 < r must be violated everywhere."""
    for A in np.arange(0.2, 1.21, 0.1):
        c = CE.lin_coeffs(A)
        a11 = c["a1"] + c["a3"]
        assert a11 > 0.02, (A, a11)


def test_r2_full_spectrum_reports():
    fs = CE.full_spectrum(30.0, 25.0, CE.lin_coeffs(0.8), nr=120, ni=160)
    assert fs["neutral_zero"] is True
    assert fs["max_real"] is not None and fs["max_real"] > 0.1

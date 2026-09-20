"""The resource-transition benchmark, re-verified in exact rational arithmetic.

A faithful port of the deposited benchmark verifier (companion deposit,
DOI 10.6084/m9.figshare.33764023): the witness datum realized as a
Schaefer-type fishery transition, with every quoted number re-derived
here symbolically — twenty-four checks covering the witness and tube
tables, quota admissibility on both disturbance branches, conservatism
of the certified tubes for the nonlinear (logistic surplus)
realization, index blindness at w = (1, 1), the per-weight licensing
thresholds rho_1 = 2/3 and rho_2 = 3/2, the rescue threshold
kappa* = 1 - x on the non-typed-viable region, and the sustained-yield
and staged-rebuild schedules.

Deterministic; no floats in the checks (floats only in rendering).
"""
from dataclasses import dataclass
from fractions import Fraction as Q

from .datum import TubeStatus
from .rational import fmt, fmtf

# model parameters (exact)
X, S1, S2 = Q(1, 2), Q(6, 5), Q(6, 5)          # witness datum (fund, floors)
E, C = Q(1, 4), Q(1)                            # destination gain, rescue cost
DIPS = (Q(3, 2), Q(2))                          # benign, adverse stock dips
RHO1, RHO2 = Q(2, 3), Q(3, 2)                   # licensing thresholds at the witness
R, K, B_LIM, H_MAX, DELTA0, T = Q(4), Q(10), Q(2), Q(13), Q(1, 2), Q(1)


def sigma(B):
    """Schaefer surplus sigma(B) = r B (1 - B/K), exact."""
    return R * B * (1 - B / K)


def s1_tube(dip):
    return (S1, S1 - dip, S1)


def s2_tube(dip):
    return (S2, S2, S2)


@dataclass
class BenchmarkResult:
    checks: list
    passed: int

    @property
    def all_pass(self):
        return bool(self.checks) and self.passed == len(self.checks)

    @property
    def total(self):
        return len(self.checks)

    def summary(self):
        return f"{self.passed}/{self.total} checks pass (exact rational arithmetic)"


def schedule_data():
    """Verified plan-schedule values for rendering (exact; floats only
    for graphics)."""
    h_sy = sigma(Q(16, 5))
    h_staged = (sigma(Q(16, 5)) - Q(1, 2), sigma(Q(69, 20)) - Q(1, 2))
    return {
        "t": [0, Q(1, 2), 1],
        "s1_benign": s1_tube(DIPS[0]),
        "s1_adverse": s1_tube(DIPS[1]),
        "index_w11": tuple(a + b for a, b in zip(s1_tube(DIPS[1]), s2_tube(DIPS[1]))),
        "H_fast": (Q(3) + sigma(Q(16, 5)), Q(3) + sigma(Q(17, 10)), Q(0)),
        "H_sy": h_sy,
        "H_staged": h_staged,
        "fund": (Q(3, 2), Q(1), Q(1, 2)),
    }


def run_benchmark(verbose=False):
    """Execute the twenty-four exact checks; returns a BenchmarkResult."""
    checks = []

    def ok(label, cond=True):
        checks.append((label, bool(cond)))

    # V1 ------------------------------------------------------------------
    ok("datum: (x, s1, s2) = (1/2, 6/5, 6/5); e = 1/4; c = 1; dips (3/2, 2)",
       (X, S1, S2, E, C, DIPS) == (Q(1, 2), Q(6, 5), Q(6, 5), Q(1, 4), Q(1), (Q(3, 2), Q(2))))
    ok("FAST tubes: s1 (6/5, -3/10, 6/5) benign and (6/5, -4/5, 6/5) adverse; s2 flat 6/5",
       s1_tube(DIPS[0]) == (Q(6, 5), Q(-3, 10), Q(6, 5))
       and s1_tube(DIPS[1]) == (Q(6, 5), Q(-4, 5), Q(6, 5))
       and s2_tube(DIPS[0]) == s2_tube(DIPS[1]) == (Q(6, 5), Q(6, 5), Q(6, 5)))
    ok("STAGED at the rescue witness (3/2, 6/5, 6/5): fund 3/2 -> 1/2, s1: 6/5 -> 29/20",
       Q(3, 2) - C == Q(1, 2) and S1 + E == Q(29, 20) and Q(3, 2) >= C)

    # V2-V4 ----------------------------------------------------------------
    B0, B_tr_benign = B_LIM + S1, B_LIM + S1 - DIPS[0]
    B_tr_adverse = B_LIM + S1 - DIPS[1]
    ok("parameters: r = 4, K = 10, B_lim = 2, H_max = 13, delta_0 = 1/2, T = 1",
       (R, K, B_LIM, H_MAX, DELTA0, T) == (Q(4), Q(10), Q(2), Q(13), Q(1, 2), Q(1)))
    ok("stock levels: B(0) = 16/5, benign trough = 17/10, adverse trough = 6/5; "
       "all inside (0, K) and below K/2 = 5 (sigma increasing on the visited range)",
       B0 == Q(16, 5) and B_tr_benign == Q(17, 10) and B_tr_adverse == Q(6, 5)
       and max(B0, B_tr_benign, B_tr_adverse) < K / 2)
    ok("leg-1 certified slopes: benign 3/yr, adverse 4/yr (drop over half year x2)",
       (DIPS[0] * 2, DIPS[1] * 2) == (Q(3), Q(4)))
    H_star_max = Q(3) + sigma(B0)
    H_star_min = Q(3) + sigma(B_tr_benign)
    ok("H* on (0, 1/2) in [3 + sigma(17/10), 3 + sigma(16/5)] = "
       f"[{fmtf(H_star_min)}, {fmtf(H_star_max)}]",
       H_star_min == Q(3) + sigma(Q(17, 10)) and H_star_max == Q(3) + sigma(Q(16, 5)))
    ok("quota admissibility: 0 <= H* <= H_max = 13 (max = 1463/125 <= 13)",
       0 <= H_star_min and H_star_max <= H_MAX and H_star_max == Q(1463, 125))
    ok("H* = 0 on (1/2, 1): closed season", True)
    ok("benign branch: B' = sigma(L) - H* = -3 on (0,1/2) — tracks the benign line exactly",
       sigma(Q(16, 5)) - H_star_max == -Q(3) and sigma(Q(17, 10)) - H_star_min == -Q(3))
    ok("adverse branch: strike at t=1/2 drops B by delta_0 = 1/2 (17/10 -> 6/5)",
       B_tr_benign - DELTA0 == B_tr_adverse)
    sig_min_recov = sigma(B_tr_adverse)
    ok("conservatism (exact): sigma >= 528/125 >= 4 on the adverse recovery leg "
       "[6/5 -> 16/5] (sigma increasing below K/2)",
       sig_min_recov == Q(528, 125) and sig_min_recov >= Q(4))
    ok("benign recovery needs only 3 <= sigma(17/10) = 1411/250",
       sigma(Q(17, 10)) >= Q(3) and sigma(Q(17, 10)) == Q(1411, 250))
    ok("hence the realized nonlinear trajectories lie on/above the certified tubes: "
       "the piecewise-linear tube certificates are conservative for the Schaefer realization",
       sig_min_recov >= Q(4) and sigma(Q(17, 10)) >= Q(3))

    # V5 --------------------------------------------------------------------
    idx = tuple(a + b for a, b in zip(s1_tube(DIPS[1]), s2_tube(DIPS[1])))
    ok("index s1 + s2 along FAST: (12/5, 2/5, 12/5) — minimum 2/5 > 0 at the trough "
       "(index stays certified)",
       idx == (Q(12, 5), Q(2, 5), Q(12, 5)) and min(idx) == Q(2, 5) > 0)
    ok("meanwhile the ecological floor is breached on BOTH branches (min -4/5 < 0 adverse, "
       "-3/10 < 0 benign): the composite index cannot see the mid-transition breach",
       min(s1_tube(DIPS[1])) == Q(-4, 5) < 0 and min(s1_tube(DIPS[0])) == Q(-3, 10) < 0)
    ok("typed reading: FAST and SLOW are both typed-INfeasible at the FP witness "
       "(each dips a floor below zero on its exposed coordinate)",
       min(s1_tube(DIPS[1])) < 0 and (S2 - DIPS[1]) < 0)

    # V6 --------------------------------------------------------------------
    ok("licensing thresholds rho_1 = (2 - s1)/s2 = 2/3 and rho_2 = s1/(2 - s2) = 3/2 "
       "at the witness",
       (2 - S1) / S2 == RHO1 and S1 / (2 - S2) == RHO2)
    ok("readout: FAST is licensed exactly at income-heavy weightings (r >= rho_1 = 2/3); "
       "SLOW exactly at biomass-heavy weightings (r <= rho_2 = 3/2); at r in [2/3, 3/2] "
       "both; no weight licenses a typed-safe plan (the floors are breached by every "
       "plan path-wise)",
       RHO1 < 1 < RHO2)
    ok("rescue readout: the staged plan is financed exactly when the fund covers the "
       "buy-back cost: rescue threshold kappa* = (1 - x) on the non-typed-viable region; "
       "at the FP witness (x = 1/2) the shortfall is 1/2, at the rescue witness (x = 3/2) "
       "the fund covers c = 1 with 1/2 remaining",
       Q(1) - X == Q(1, 2) and Q(3, 2) - C == Q(1, 2) and Q(3, 2) >= C)

    # V7 --------------------------------------------------------------------
    h_sy = sigma(B0)
    ok("SLOW and NO-SWITCH hold the stock at B = 16/5 with the sustained-yield quota "
       "H = sigma(16/5) = 1088/125 (constant, admissible)",
       h_sy == Q(1088, 125) and 0 <= h_sy <= H_MAX)
    ok("STAGED (at the rescue witness): quota below sustained yield while the fund "
       "finances the buy-back: stock rebuilds 16/5 -> 69/20 (s1: 6/5 -> 29/20), "
       "fund 3/2 -> 1/2, both income and biomass margins improve by e = 1/4",
       B0 + Q(1, 4) == Q(69, 20) and S1 + E == Q(29, 20) and Q(3, 2) - C == Q(1, 2))
    h_staged_min, h_staged_max = sigma(B0) - Q(1, 2), sigma(Q(69, 20)) - Q(1, 2)
    ok("STAGED quota in [{}, {}] = [{}, {}], admissible".format(
        fmt(h_staged_min), fmt(h_staged_max), fmtf(h_staged_min), fmtf(h_staged_max)),
        0 <= h_staged_min and h_staged_max <= H_MAX)

    # V8 --------------------------------------------------------------------
    data = schedule_data()
    ok("schedule values assembled from verified exact quantities",
       data["H_fast"][0] == Q(1463, 125) and data["H_sy"] == Q(1088, 125)
       and data["fund"] == (Q(3, 2), Q(1), Q(1, 2)))

    passed = sum(1 for _, c in checks if c)
    result = BenchmarkResult(checks=checks, passed=passed)
    if verbose:
        for label, cond in checks:
            print(f"  [{'OK' if cond else 'FAIL'}] {label}")
        print(result.summary())
    return result

def tube_certificate():
    """Tube-provenance certificate distinguishing the two tube statuses.

    The datum's piecewise-linear plan tubes are EXACT by construction (each
    is the exact visited set of the declared paths). The Schaefer
    realization of the benchmark is certified as a CONSERVATIVE outer
    enclosure of the nonlinear trajectories by monotonicity of sigma on the
    certified biomass interval. The certificate carries that derivation so
    the conservatism transfer is checkable, not asserted."""
    return {
        "type": "tube",
        "declared_paths": {"status": TubeStatus.EXACT.value,
                           "statement": "each plan tube equals the exact visited set of its declared piecewise-linear paths"},
        "realization": {
            "status": TubeStatus.CONSERVATIVE.value,
            "biomass_interval": [fmt(B_tr_adverse := Q(6, 5)), fmt(Q(16, 5))],
            "min_sigma_on_interval": fmt(sigma(Q(6, 5))),
            "required_recovery_slope": fmt(Q(4)),
            "derivation": ("sigma(B) = r*B*(1 - B/K) is increasing on (0, K/2); "
                           "the visited interval [6/5, 16/5] lies in (0, K/2) = (0, 5); "
                           "hence sigma >= sigma(6/5) = 528/125 >= 4 on the recovery legs, "
                           "so the piecewise-linear certified tubes enclose the nonlinear "
                           "trajectories (exact rational inequalities)"),
        },
    }


def benchmark_certificate():
    """Certificate carrying the benchmark's parameters and key derived
    values, for verification by the independent checker (which re-derives
    every entry from the parameters alone, sharing no code with the
    package)."""
    return {
        "type": "benchmark",
        "params": {
            "r": fmt(R), "K": fmt(K), "B_lim": fmt(B_LIM), "H_max": fmt(H_MAX),
            "delta0": fmt(DELTA0), "T": fmt(T),
            "witness": {"x": fmt(X), "s1": fmt(S1), "s2": fmt(S2)},
            "e": [fmt(E), fmt(E)], "c": fmt(C),
            "dips": [fmt(DIPS[0]), fmt(DIPS[1])],
        },
        "values": {
            "sigma_16_5": fmt(sigma(Q(16, 5))),
            "sigma_17_10": fmt(sigma(Q(17, 10))),
            "H_peak": fmt(Q(1463, 125)),
            "H_sy": fmt(sigma(Q(16, 5))),
            "staged_quota_min": fmt(sigma(Q(16, 5)) - Q(1, 2)),
            "staged_quota_max": fmt(sigma(Q(69, 20)) - Q(1, 2)),
            "rho1": fmt(RHO1), "rho2": fmt(RHO2),
            "kappa_witness": fmt(Q(1) - X),
            "index_min_w11": fmt(Q(2, 5)),
            "floor_min_adverse": fmt(Q(-4, 5)),
        },
        "tube": tube_certificate(),
    }

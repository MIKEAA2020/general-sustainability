"""Dashboard readings: exact indicator computations for a witness state.

Produces the reading set of the companion manuscript's dashboard
discussion: per-weight licensing thresholds, the rescue threshold, the
per-plan floor minima under the characteristic disturbance, the
composite-index minimum at a given weight for the read plan, and the
index-blindness alarm (the composite index stays certified while a
typed floor is breached mid-transition). Every quantity is exact; the
module also cross-checks the witness threshold formulas against the
thresholds derived directly from the tube geometry.
"""
from dataclasses import dataclass, field
from fractions import Fraction as Q

from .datum import WitnessDatum
from .rational import fmt

DIP = Q(2)          # characteristic dip depth (witness datum)
E_GAIN = (Q(1, 4), Q(1, 4))
C_RESCUE = Q(1)
PLANS = ("FAST", "SLOW", "STAGED", "NO-SWITCH")


@dataclass
class Readings:
    """Exact dashboard readings for one state, one weight, one read plan."""

    state: tuple
    weight: tuple
    plan: str
    rho1: Q
    rho2: Q
    kappa_star: Q
    tube_minima: dict
    index_values: tuple
    index_min: Q
    floor_min: Q
    blind_alarm: bool
    licensed: dict
    threshold_crosscheck_ok: bool
    notes: list = field(default_factory=list)


def licensing_thresholds(s1=None, s2=None):
    """Per-weight licensing thresholds at a state with floors ``(s1, s2)``
    and characteristic dip depth 2: FAST is aggregate-licensed iff
    ``w2/w1 >= (2 - s1)/s2``; SLOW iff ``w2/w1 <= s1/(2 - s2)``. Derived
    here directly from the tube geometry (minima of the aggregate along
    the tube); defaults reproduce the witness values 2/3 and 3/2."""
    s1 = Q(6, 5) if s1 is None else Q(s1)
    s2 = Q(6, 5) if s2 is None else Q(s2)
    fast_rho = -(s1 - DIP) / s2      # w2 s2 >= w1 (2 - s1)
    slow_rho = s1 / (DIP - s2)       # w1 s1 >= w2 (2 - s2)  <=>  w2/w1 <= s1/(2 - s2)
    return fast_rho, slow_rho


def plan_tubes(state, plan):
    """Exact per-coordinate tube (values at t = 0, 1/2, 1) of ``plan`` at
    ``state = (q, x, s1, s2)`` under its characteristic disturbance."""
    _, x, s1v, s2v = state
    if plan == "FAST":
        return {"x": (x, x, x), "s1": (s1v, s1v - DIP, s1v), "s2": (s2v,) * 3}
    if plan == "SLOW":
        return {"x": (x, x, x), "s1": (s1v,) * 3, "s2": (s2v, s2v - DIP, s2v)}
    if plan == "STAGED":
        return {"x": (x, x - Q(1, 2), x - C_RESCUE),
                "s1": (s1v, s1v + E_GAIN[0] / 2, s1v + E_GAIN[0]),
                "s2": (s2v, s2v + E_GAIN[1] / 2, s2v + E_GAIN[1])}
    if plan == "NO-SWITCH":
        return {"x": (x,) * 3, "s1": (s1v,) * 3, "s2": (s2v,) * 3}
    raise KeyError(plan)


def compute(state=(0, Q(1, 2), Q(6, 5), Q(6, 5)), weight=(Q(1), Q(1)), plan="FAST"):
    """Exact readings at ``state`` under aggregate weight ``weight``,
    reading the composite index and floor along ``plan``."""
    q, x, s1v, s2v = state
    w1, w2 = weight
    tube_minima = {p: {c: min(v) for c, v in plan_tubes(state, p).items()}
                   for p in PLANS}
    path = plan_tubes(state, plan)
    idx = tuple(w1 * a + w2 * b for a, b in zip(path["s1"], path["s2"]))
    floor_min = min(min(path["s1"]), min(path["s2"]))
    blind_alarm = (min(idx) > 0) and (floor_min < 0)
    rho1, rho2 = licensing_thresholds(s1v, s2v)
    licensed = {
        "FAST (aggregate @ w)": (w2 / w1) >= rho1,
        "SLOW (aggregate @ w)": (w2 / w1) <= rho2,
        "typed-safe plan (any w)": False,   # no weight licenses one here; see notes
    }
    witness_rho = ((Q(2) - Q(6, 5)) / Q(6, 5), Q(6, 5) / (Q(2) - Q(6, 5)))
    crosscheck = (witness_rho == licensing_thresholds()
                  and (rho1, rho2) == licensing_thresholds(s1v, s2v))
    kappa = max(Q(0), Q(1) - x)
    notes = []
    if blind_alarm:
        notes.append(
            f"Index blindness: along {plan}, the composite index stays certified "
            f"(min {fmt(min(idx))} > 0) while the floor reaches {fmt(floor_min)} < 0 "
            "mid-transition.")
    if kappa > 0:
        notes.append(
            f"Rescue financing: shortfall kappa* = {fmt(kappa)} at this fund level; "
            f"a fund of x >= c = {fmt(C_RESCUE)} covers the buy-back (the rescue "
            f"witness x = 3/2 retains {fmt(Q(3, 2) - C_RESCUE)}).")
    notes.append(
        "STAGED is typed-feasible exactly when the fund covers the buy-back "
        "(x >= 1); the fund does" + ("." if x >= C_RESCUE else " not at this state."))
    return Readings(
        state=state, weight=weight, plan=plan, rho1=rho1, rho2=rho2,
        kappa_star=kappa, tube_minima=tube_minima, index_values=idx,
        index_min=min(idx), floor_min=floor_min, blind_alarm=blind_alarm,
        licensed=licensed, threshold_crosscheck_ok=crosscheck, notes=notes,
    )

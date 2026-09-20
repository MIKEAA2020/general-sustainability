"""Typed transition data for exact transition-safety assessment.

Implements the assessment-datum structure of the companion manuscript
*Aggregate Indices and Transition Safety: A Quantifier-Order Separation
Between Scalarized and Coordinate-Wise Feasibility* (A. Abaee; verified
companion deposit, DOI 10.6084/m9.figshare.33764023): phase states
``(q, x, s1, s2)`` (phase flag, physical fund, typed floors), actions
given as piecewise-linear coordinate paths on the review-period
breakpoints ``t = 0, 1/2, 1``, action-indexed disturbances applied at
the midpoint, and exact tubes (the visited set, with no outer
approximation).

The module ships one fully specified instance, :class:`WitnessDatum`,
the companion manuscript's witness datum with gain vector
``e = (1/4, 1/4)`` and rescue cost ``c = 1``. Custom data may subclass
:class:`TransitionDatum`.
"""
from dataclasses import dataclass
from enum import Enum
from fractions import Fraction as Q

from .rational import frac, fmt

class TubeStatus(str, Enum):
    """Provenance status of a tube.

    EXACT: the tube is the exact visited set of the datum's declared
    piecewise-linear paths (true by construction for every datum in this
    package). CONSERVATIVE: the tube is a certified outer enclosure of an
    underlying nonlinear realization (e.g. the Schaefer benchmark, where
    monotonicity of the surplus on the certified biomass interval yields the
    enclosing inequalities). The distinction matters: exact arithmetic on a
    supplied tube certifies verdicts relative to that tube, and a
    conservative enclosure transfers them to the realization only with the
    enclosure certificate attached."""

    EXACT = "EXACT"
    CONSERVATIVE = "CONSERVATIVE"


COORDS = ("x", "s1", "s2")
BREAKPOINTS = (Q(0), Q(1, 2), Q(1))


@dataclass(frozen=True)
class Disturbance:
    """Instantaneous excess dips (coordinate, depth) applied at the
    review-period midpoint. An empty dip list is the benign regime."""

    dips: tuple

    def __init__(self, dips=()):
        object.__setattr__(self, "dips", tuple((c, frac(d)) for c, d in dips))


@dataclass(frozen=True)
class Action:
    """An action declared by relative coordinate offsets at the
    breakpoints ``t = 0, 1/2, 1`` (monotone on each piece), together
    with its characteristic (worst-case) disturbance."""

    name: str
    offsets: dict
    characteristic: Disturbance

    def path(self, start, coord, disturbance=None):
        """Absolute coordinate values at the breakpoints under ``disturbance``."""
        base = {("x",): start[1], ("s1",): start[2], ("s2",): start[3]}
        off = self.offsets.get(coord, (Q(0), Q(0), Q(0)))
        vals = [base[(coord,)] + o for o in off]
        dip = Q(0)
        if disturbance is not None:
            dip = sum((d for c, d in disturbance.dips if c == coord), Q(0))
        return (vals[0], vals[1] - dip, vals[2])

    def tube(self, start, coord, disturbance=None):
        """Exact visited set (min, max) of the coordinate: the paths are
        monotone on each linear piece, so extremes fall at breakpoints."""
        v = self.path(start, coord, disturbance)
        for (a0, a1), (b0, b1) in (((v[0], v[1]), (v[1], v[2])),):
            if (a1 - a0) * (b1 - b0) < 0:
                raise ValueError(f"action {self.name}: path on {coord} is not monotone per piece")
        return (min(v), max(v))

    def end(self, start, coord, disturbance=None):
        """Endpoint values (t = 0 and t = 1) of the coordinate."""
        v = self.path(start, coord, disturbance)
        return (v[0], v[2])


class TransitionDatum:
    """Interface: constraint sets, action table, successors."""

    n_floors = 2

    def actions(self, z):  # pragma: no cover - interface
        raise NotImplementedError

    def successor(self, z, action_name):  # pragma: no cover - interface
        raise NotImplementedError

    def in_S_phys(self, z):  # pragma: no cover - interface
        raise NotImplementedError

    def in_S(self, z):  # pragma: no cover - interface
        raise NotImplementedError

    def in_G_phys(self, z):  # pragma: no cover - interface
        raise NotImplementedError

    def in_G(self, z):  # pragma: no cover - interface
        raise NotImplementedError

    def dot_s(self, z, w):
        """Weighted aggregate w . s of the floor coordinates of ``z``."""
        return sum(wi * si for wi, si in zip(w, z[2:]))


class WitnessDatum(TransitionDatum):
    """The companion manuscript's witness datum.

    Phase state ``(q, x, s1, s2)``; transition-safe set
    ``S = {x >= 0, s1 >= 0, s2 >= 0}``; destination ``G = {q = 1, x, s >= 0}``;
    destination reset gain ``e = (1/4, 1/4)``; rescue cost ``c = 1``.
    Four actions: NO-SWITCH, FAST (s1 dip of depth 2, worst case),
    SLOW (s2 dip of depth 2, worst case), STAGED (fund spend of 1,
    floors gain e).
    """

    e_gain = (Q(1, 4), Q(1, 4))
    c_rescue = Q(1)

    def actions(self, z):
        zero = (Q(0), Q(0), Q(0))
        e = self.e_gain
        return {
            "NO-SWITCH": Action("NO-SWITCH", {"x": zero, "s1": zero, "s2": zero},
                                Disturbance()),
            # FAST/SLOW move no coordinate intrinsically; the worst-case
            # drop is their characteristic disturbance (depth 2, action-
            # indexed per the companion manuscript's convention), so the
            # worst-case tube of FAST is (s1, s1 - 2, s1), and symmetrically
            # for SLOW — matching the deposited benchmark tube function.
            "FAST": Action("FAST", {"x": zero, "s1": zero, "s2": zero},
                           Disturbance((("s1", Q(2)),))),
            "SLOW": Action("SLOW", {"x": zero, "s1": zero, "s2": zero},
                           Disturbance((("s2", Q(2)),))),
            "STAGED": Action("STAGED",
                             {"x": (Q(0), -Q(1, 2), -Q(1)),
                              "s1": (Q(0), e[0] / 2, e[0]), "s2": (Q(0), e[1] / 2, e[1])},
                             Disturbance()),
        }

    def successor(self, z, action_name):
        q, x, s1, s2 = z
        e = self.e_gain
        if action_name == "NO-SWITCH":
            return (0, x, s1, s2)
        if action_name == "FAST":
            return (1, x, s1 + e[0], s2 + e[1])
        if action_name == "SLOW":
            return (1, x, s1 + e[0], s2 + e[1])
        if action_name == "STAGED":
            return (1, x - self.c_rescue, s1 + e[0], s2 + e[1])
        raise KeyError(action_name)

    @staticmethod
    def in_S_phys(z):
        return z[1] >= 0

    @staticmethod
    def in_S(z):
        return z[1] >= 0 and z[2] >= 0 and z[3] >= 0

    @staticmethod
    def in_G_phys(z):
        return z[0] == 1 and z[1] >= 0

    @staticmethod
    def in_G(z):
        return z[0] == 1 and z[1] >= 0 and z[2] >= 0 and z[3] >= 0


def witness_state(x, s1, s2):
    """Phase-0 state with exact rational coordinates."""
    return (0, frac(x), frac(s1), frac(s2))


def describe_state(z):
    q, x, s1, s2 = z
    return f"(q={q}, x={fmt(x)}, s1={fmt(s1)}, s2={fmt(s2)})"

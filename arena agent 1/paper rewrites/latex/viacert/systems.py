"""Finite systems: the audited instances and the pluggable container."""
from dataclasses import dataclass, field
from fractions import Fraction as Q
from itertools import product
from typing import Callable, Hashable, Sequence


@dataclass(frozen=True)
class FiniteSystem:
    """A finite deterministic system with adversarial-free reach step.

    states:    finite sequence of hashable states
    actions:   finite sequence of actions
    safe:      set (or predicate) of safe states
    step:      transition, step(x, u) -> x+
    null:      the null (no-instrument) action, excluded from viable choices
    """
    states: Sequence[Hashable]
    actions: Sequence[Hashable]
    safe: frozenset
    step: Callable[[Hashable, Hashable], Hashable]
    null: Hashable = None

    def __post_init__(self):
        if not callable(self.step):
            raise TypeError("step must be callable: step(x, u) -> x+")

    def is_safe(self, x) -> bool:
        return x in self.safe

    def pairs(self):
        """All two-element belief subsets of the safe set."""
        S = sorted(self.safe, key=repr)
        return [frozenset({x, y}) for i, x in enumerate(S) for y in S[i + 1:]]


def audit_system() -> FiniteSystem:
    """The programme's shared three-coordinate audit system.

    States (z1, z2) in {0,1,2,3}^2; safe set {z1 >= 1 and z2 >= 1};
    instruments u in {0, 1, 2}: u = 0 executes no instrument (both
    coordinates decay one); u = j acts coordinate j (regeneration +1,
    cap 3) while the other decays one. Source: Abaee 2026a, Section 8;
    provenance-locked as the concordance's shared system.
    """
    CAP = 3

    def step(x, u):
        z1, z2 = x
        if u == 0:
            return (max(0, z1 - 1), max(0, z2 - 1))
        return (max(0, min(CAP, z1 + 1 - (0 if u == 1 else 2))),
                max(0, min(CAP, z2 + 1 - (0 if u == 2 else 2))))

    states = tuple(product(range(4), repeat=2))
    safe = frozenset(x for x in states if x[0] >= 1 and x[1] >= 1)
    return FiniteSystem(states=states, actions=(0, 1, 2), safe=safe,
                         step=step, null=0)


def timing_grid():
    """The 48-cell review grid: 16 z0 values x 3 deadline values."""
    return [(Q(n, 10), T) for n in range(10, 26) for T in (1, 2, 3)]


def benchmark_caps():
    """The continuous benchmark's floor caps and their identities.

    Returns (cap1, cap2, critical_aggregate) with cap_i(Y) exact rational;
    cap sum equals 2 exactly at Y* = 27/5. Source: minimax dual
    certificates v1 / concordance C8.
    """
    def cap1(Y): return Q(3, 2) - (Y - 2) / 10
    def cap2(Y): return Q(59, 50) - (Y - 2) / 10
    Ssum = lambda Y: cap1(Y) + cap2(Y)
    Ystar = Q(4) + (Ssum(Q(4)) - Q(2)) * 5
    return cap1, cap2, Ystar


def ce_laws():
    """The canonical (uncorrected, corrected) certainty-equivalence laws.

    Uncorrected: index g(s) = s^2 read one step ahead of the state;
    corrected: the debiased reading. Source: the programme's corrected
    labels — uncorrected drift >= 21/100 on [1,2]; corrected identically 0.
    """
    g = lambda s: s * s
    uncorrected = lambda s: s + Q(1, 10)
    corrected = lambda s: s + Q(1, 10) - Q(1, 10)
    return g, uncorrected, corrected

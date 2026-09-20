"""The five assessment operators and accepted-state sets.

Direct implementation of the operator family of the companion
manuscript *Aggregate Indices and Transition Safety*: the noncompensatory
typed operator ``E_typ``, the scalarized aggregate operator ``E_w``,
the exact-tube physical operator ``E_tube,phys``, the endpoint-only
physical operator ``E_end``, and the typed-endpoint operator
``E_end,typ``, together with the accepted-state sets
``V[E] = {z : E(z) != empty}`` and the compensatory accepted set
``V_weak = intersection_w V_w``.

Because ``End(a, d)`` is contained in ``Tube(a, d)`` and ``S`` in
``S^w`` in ``S^phys``, the operator chain
``E_typ(z) <= E_w(z) <= E_tube,phys(z) <= E_end(z)`` holds for every
positive weight ``w`` (:func:`check_chain`); the tests verify it
exactly on the witness datum.
"""
from fractions import Fraction as Q

from .rational import frac

MODES = ("typ", "w", "tube_phys", "end", "end_typ")
TUBE_MODES = ("typ", "w", "tube_phys")
END_MODES = ("end", "end_typ")


def _breakpoint_values(datum, z, action, disturbance, mode):
    """Per-breakpoint snapshots of (x, s1, s2) under the mode's evaluation
    discipline: the full tube for tube modes, endpoints only for end modes."""
    coords = ("x", "s1", "s2")
    paths = {c: action.path(z, c, disturbance) for c in coords}
    idx = (0, 1, 2) if mode in TUBE_MODES else (0, 2)
    return [{c: paths[c][i] for c in coords} for i in idx]


def _snapshot_admissible(datum, snap, mode, w):
    if not snap["x"] >= 0:
        return False
    if mode == "typ":
        return snap["s1"] >= 0 and snap["s2"] >= 0
    if mode == "end_typ":
        return snap["s1"] >= 0 and snap["s2"] >= 0
    if mode == "w":
        return w[0] * snap["s1"] + w[1] * snap["s2"] >= 0
    return True  # tube_phys / end: physical constraint only


def admissible(datum, z, action_name, mode="typ", w=None):
    """Is ``action_name`` admissible at ``z`` under operator ``mode``?

    Quantifies over both disturbance regimes (benign and the action's
    characteristic worst case), evaluates the tube (or endpoints), and
    additionally requires the successor to lie in the mode's destination
    set (``G`` for typ/end_typ, ``G^w`` for w, ``G^phys`` otherwise).
    """
    if mode == "w":
        w = (frac(w[0]), frac(w[1]))
    a = datum.actions(z)[action_name]
    regimes = (None, a.characteristic)
    for d in regimes:
        for snap in _breakpoint_values(datum, z, a, d, mode):
            if not _snapshot_admissible(datum, snap, mode, w):
                return False
    g = datum.successor(z, action_name)
    if mode == "w":
        return datum.in_G_phys(g) and w[0] * g[2] + w[1] * g[3] >= 0
    if mode in ("typ", "end_typ"):
        return datum.in_G(g)
    return datum.in_G_phys(g)


def E(datum, z, mode="typ", w=None):
    """The operator's action set at ``z`` (a frozenset of action names)."""
    return frozenset(name for name in datum.actions(z)
                     if admissible(datum, z, name, mode=mode, w=w))


def V(datum, states, mode="typ", w=None):
    """Accepted-state set ``V[E_mode]`` restricted to ``states``."""
    return {z for z in states if E(datum, z, mode=mode, w=w)}


def V_weak(datum, states, weights):
    """Compensatory accepted set: intersection of ``V_w`` over a weight grid.

    The true set quantifies over all positive weights; on grid points the
    intersection is an inner approximation. :mod:`safetransition.indicators`
    complements this with the exact per-weight licensing thresholds, which
    characterize membership analytically on the witness datum.
    """
    acc = set(states)
    for w in weights:
        acc &= V(datum, states, mode="w", w=w)
    return acc


def check_chain(datum, z, w):
    """Verify the operator chain ``E_typ <= E_w <= E_tube,phys <= E_end``
    and the typed-endpoint chain ``E_typ <= E_end,typ <= E_end`` at ``z``.
    Returns a list of (inclusion, holds) pairs, all exact."""
    sets = {m: E(datum, z, mode=m, w=w) for m in MODES}
    return [
        ("E_typ <= E_w", sets["typ"] <= sets["w"]),
        ("E_w <= E_tube_phys", sets["w"] <= sets["tube_phys"]),
        ("E_tube_phys <= E_end", sets["tube_phys"] <= sets["end"]),
        ("E_typ <= E_end_typ", sets["typ"] <= sets["end_typ"]),
        ("E_end_typ <= E_end", sets["end_typ"] <= sets["end"]),
    ]

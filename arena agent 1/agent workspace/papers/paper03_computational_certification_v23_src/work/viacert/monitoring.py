"""Fibre/partition criteria and the monitoring design rules (exact)."""
import math
from fractions import Fraction as Q
from itertools import combinations


def safe_actions(sys, x):
    """R(x): the actions keeping x safe for one step."""
    return [u for u in sys.actions if u != 0 and sys.is_safe(sys.step(x, u))]


def common_safe(sys, fibre) -> list:
    """The common safe-action set of a fibre (empty => the obstruction)."""
    sets = [set(safe_actions(sys, x)) for x in fibre]
    if not sets:
        return []
    out = sets[0]
    for s in sets[1:]:
        out = out & s
    return sorted(out)


def fibre_partition(states, info):
    """The partition induced by an observation map."""
    p = {}
    for x in states:
        p.setdefault(info(x), set()).add(x)
    return [frozenset(v) for v in p.values()]


def adequate(sys, partition) -> bool:
    """Partition-form adequacy: every fibre has a nonempty common safe set.

    The one-step converse of the monitoring companion (the calculus's
    design reading; concordance C2 on the audited target).
    """
    return all(common_safe(sys, F) for F in partition)


def maximal_common_action_sets(sys, states):
    """Maximal subsets of `states` with a nonempty common safe-action set."""
    out = []
    for r in range(len(states), 0, -1):
        for S in combinations(sorted(states, key=repr), r):
            FS = frozenset(S)
            if common_safe(sys, FS) and not any(FS < M for M in out):
                out.append(FS)
    return out


def partition_census(sys, target):
    """All partitions of `target`: counts of total, adequate, minimal-size.

    Returns (total, adequate_list, min_size). Enumerative; the audited
    target of four states gives 15 total, 7 adequate, min size 2.
    """
    target = sorted(target, key=repr)

    def parts(S):
        if not S:
            yield []
            return
        first, rest = S[0], S[1:]
        for p in parts(rest):
            for i in range(len(p)):
                yield p[:i] + [[first] + p[i]] + p[i + 1:]
            yield p + [[first]]

    total, adm = 0, []
    for P in parts(target):
        total += 1
        Pt = tuple(frozenset(F) for F in P)
        if adequate(sys, Pt):
            adm.append(Pt)
    return total, adm, min(len(P) for P in adm)


def sigma_star(z0):
    """The hold-class discrete survival supremum: floor(z0 - 1)."""
    return math.floor(float(z0) - 1)


def delay_identity(grid, strict=False):
    """Cells where the review-timing rule disagrees with {z0 >= 1 + T_obs}.

    Non-strict rule (T_obs <= z0 - 1): zero disagreements on the audited
    grid. Strict rule (T_obs < z0 - 1): fails at exactly the boundary cell
    (2, 1) — the corrected identity's reason.
    """
    bad = []
    for z, T in grid:
        rule = ((z - 1) > T) if strict else ((z - 1) >= T)
        if rule != (z >= 1 + T):
            bad.append((z, T))
    return bad


def ce_drift_report(law_pair, grid_n=101, lo=1, hi=2):
    """Minimum drift of each CE law on [lo, hi] (exact).

    The audited pair: uncorrected min drift >= 21/100; corrected 0.
    """
    g, uncorrected, corrected = law_pair
    step = Q(1, 100)
    n_lo, n_hi = int(Q(lo) / step), int(Q(hi) / step)
    d_u = min(g(uncorrected(Q(n, 100))) - g(Q(n, 100)) for n in range(n_lo, n_hi + 1))
    d_c = min(g(corrected(Q(n, 100))) - g(Q(n, 100)) for n in range(n_lo, n_hi + 1))
    return d_u, d_c

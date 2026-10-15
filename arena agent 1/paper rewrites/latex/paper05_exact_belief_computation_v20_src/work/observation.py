"""Observation studies: (i) blind value of a belief = max mass of a set that is
blind-survivable at the level (antichain formula), the probe ladder on
subcube supports; (ii) the z-feedback game (stock observed, information
classes split by drift) and its thresholds; (iii) deadline / total-ignorance
horizon.  Exact."""
import time
from fractions import Fraction as Q
from itertools import combinations, product
from collections import Counter

from p05_core import (cells, ham, actions, sign_actions, D, game_value, certified_threshold,
                      forward_horizon, horizon_bound, feedback_threshold, classes, HOLD)


def subcubes(m, j):
    """all j-dimensional subcubes as frozensets of cells"""
    C = cells(m)
    out = set()
    for fixed in combinations(range(m), m - j):
        for vals in product((1, -1), repeat=m - j):
            out.add(frozenset(th for th in C if all(th[i] == v for i, v in zip(fixed, vals))))
    return sorted(out, key=sorted)


def ladder(m, maximal_by_level):
    """value of the uniform prior on each j-subcube at each level:
    max_{A maximal at L} |A n Q| / 2^j; returns {L: [best value for j = m..0]}"""
    out = {}
    for L, fam in maximal_by_level.items():
        row = []
        for j in range(m, -1, -1):
            best = Q(0)
            for Qc in subcubes(m, j):
                v = max(Q(len(A & Qc), len(Qc)) for A in fam)
                best = max(best, v)
            row.append(best)
        out[L] = row
    return out


def blind_threshold_fn(cache):
    def f(T):
        T = frozenset(T)
        if T not in cache:
            if len(T) == 1:
                cache[T] = 0
            else:
                V = game_value(T)[0]
                cache[T] = None if V < Q(5, 2) else certified_threshold(T, caps=(6, 12, 24, 48), max_steps=200)["L"]
        return cache[T]
    return f


def feedback_study(m, max_L=40):
    C = cells(m)
    cache = {}
    thr = blind_threshold_fn(cache)
    res = {}
    t = time.time()
    res["cube"] = feedback_threshold(C, thr, max_L=max_L)
    # subcubes
    res["subcubes"] = {}
    res["subcubes_blind"] = {}
    for j in range(1, m):
        Qc = subcubes(m, j)[0]
        res["subcubes"][j] = feedback_threshold(Qc, thr, max_L=max_L)
        res["subcubes_blind"][j] = thr(Qc)
    # information classes after one matched action from the full cube: distance shells
    res["shells"] = {}
    u = C[0]
    for h in range(0, m + 1):
        shell = frozenset(th for th in C if ham(th, u) == h)
        res["shells"][h] = {"size": len(shell), "blind": thr(shell), "feedback": feedback_threshold(shell, thr, max_L=max_L)}
    res["time_s"] = round(time.time() - t, 2)
    return res


def first_split_requirement(m):
    """minimal slack for the far cell to survive the first (necessarily
    splitting) action from total ignorance: a sign action costs the antipode
    5 + 2m (tenths); the hold splits nothing."""
    return 2 * m + 5


def deadline_table(m, Ls):
    C = cells(m)
    V = game_value(C)[0]
    rows = []
    for L in Ls:
        h, fr = forward_horizon(C, L, max_steps=60)
        rows.append({"L": L, "exact_horizon": h, "lp_bound": horizon_bound(L, V), "hold_steps": L // 5})
    return {"V_cube": str(V), "rows": rows}


def cell_sum_identity(m):
    C = cells(m)
    sums = {str(u): sum(D(u, th) for th in C) for u in actions(m)}
    vals = set(sums.values())
    return {"all_equal": len(vals) == 1, "value_tenths": vals.pop(), "per_cell_stock_units": str(Q(-5, 10))}


if __name__ == "__main__":
    import json
    out = {}
    for m in (4, 5):
        out[m] = {"feedback": feedback_study(m), "deadline": deadline_table(m, [0, 5, 10, 13, 15, 20, 25]),
                  "cell_sum": cell_sum_identity(m), "first_split": first_split_requirement(m)}
        print(m, out[m])
    json.dump(out, open("observation_out.json", "w"), indent=1, default=str)

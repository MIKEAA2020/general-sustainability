"""Exact versus floating-point arithmetic on the knife-edge sets (V = 5/2):
(i) float LP values and the sign of their error; (ii) float simulation of an
exact winning word whose slack touches the floor every period."""
import time
import numpy as np
from fractions import Fraction as Q
from p05_core import (cells, ip, D, game_value, winning_word, distance_graph, maximal_cliques, HOLD)


def float_lp_value(S):
    from scipy.optimize import linprog
    S = list(S)
    m = len(S[0])
    # maximise t s.t. t - theta.y <= 0, -1 <= y <= 1   (variables y_1..y_m, t)
    c = np.zeros(m + 1); c[-1] = -1.0
    A = np.array([[-x for x in th] + [1.0] for th in S])
    b = np.zeros(len(S))
    bounds = [(-1, 1)] * m + [(None, None)]
    r = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs")
    return -r.fun, r.x[:m]


def simulate_float(word_pre, word_per, S, L, steps, dtype=np.float64, formula="affine"):
    """stock units: z0 = 1 + L/10; floor 1; returns dict cell -> first step with z < 1 (or None)
    and the maximal absolute deviation from the exact trajectory"""
    S = list(S)
    first_death = {}
    maxdev = 0.0
    for th in S:
        z = dtype(1) + dtype(L) / dtype(10)
        zexact = L  # tenths
        fd = None
        for t in range(steps):
            u = word_pre[t] if t < len(word_pre) else word_per[(t - len(word_pre)) % len(word_per)]
            k = ip(u, th)
            if formula == "affine":
                d = dtype(-0.5) + dtype(0.2) * dtype(k)
            elif formula == "ratio":
                d = dtype(2 * k - 5) / dtype(10)
            else:
                raise ValueError
            z = z + d
            zexact += D(u, th)
            dev = abs(float(z) - (1 + zexact / 10))
            maxdev = max(maxdev, dev)
            if z < dtype(1) and fd is None:
                fd = t + 1
        first_death[th] = fd
    return first_death, maxdev


def run(steps=10 ** 5, sweep_steps=2000):
    out = {}
    V, adj = distance_graph(6, 3)
    cl = maximal_cliques(V, adj)
    ten = sorted([c for c in cl if len(c) == 10], key=sorted)[0]
    Vex, y, q = game_value(ten)
    t = time.time()
    Vfl, yfl = float_lp_value(ten)
    out["ten_set"] = {"cells": [list(c) for c in sorted(ten)], "V_exact": str(Vex), "V_float": repr(float(Vfl)),
                      "float_error": repr(float(Vfl) - 2.5), "float_says_survivable_strict": bool(Vfl >= 2.5),
                      "lp_time_s": round(time.time() - t, 4)}
    pre, per = winning_word(ten, 3, 12)
    out["word"] = {"prefix": [list(u) if u is not HOLD else "hold" for u in pre],
                   "period": [list(u) if u is not HOLD else "hold" for u in per]}
    res = {}
    for dtype, name in ((np.float64, "float64"), (np.float32, "float32")):
        for formula in ("affine", "ratio"):
            fd, dev = simulate_float(pre, per, ten, 3, steps, dtype, formula)
            deaths = {str(list(th)): v for th, v in fd.items() if v is not None}
            res[f"{name}_{formula}"] = {"n_false_deaths": len(deaths), "first_false_death_step": min(deaths.values()) if deaths else None,
                                        "max_abs_deviation": repr(dev)}
    out["simulation"] = res
    out["steps"] = steps
    # also the m=4 adjacent pair from L=1 (the edge of the pair band) -- the same touch-the-floor pattern
    C4 = cells(4)
    a, b = C4[0], C4[1]
    res4 = {}
    for dtype, name in ((np.float64, "float64"), (np.float32, "float32")):
        for formula in ("affine", "ratio"):
            fd, dev = simulate_float([], [a, b], [a, b], 1, steps, dtype, formula)
            deaths = {str(list(th)): v for th, v in fd.items() if v is not None}
            res4[f"{name}_{formula}"] = {"n_false_deaths": len(deaths), "first_false_death_step": min(deaths.values()) if deaths else None,
                                         "max_abs_deviation": repr(dev)}
    out["pair_m4"] = res4
    # all 1280 knife-edge ten-sets: their own game words from L* = 3, float64, two formulas
    t = time.time()
    tens = [c for c in cl if len(c) == 10]
    cnt = {"affine": 0, "ratio": 0}
    earliest = {"affine": None, "ratio": None}
    for c in tens:
        pre, per = winning_word(c, 3, 12)
        for formula in ("affine", "ratio"):
            fd, dev = simulate_float(pre, per, c, 3, sweep_steps, np.float64, formula)
            deaths = [v for v in fd.values() if v is not None]
            if deaths:
                cnt[formula] += 1
                e = min(deaths)
                earliest[formula] = e if earliest[formula] is None else min(e, earliest[formula])
    out["sweep"] = {"n_sets": len(tens), "steps": sweep_steps, "sets_with_false_death": cnt,
                    "earliest_false_death": earliest, "time_s": round(time.time() - t, 1)}
    return out


if __name__ == "__main__":
    import json
    r = run(10 ** 5)
    print(json.dumps(r, indent=1)[:3000])
    json.dump(r, open("float_out.json", "w"), indent=1)

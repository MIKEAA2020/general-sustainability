"""Point-based (alpha-set) evaluation, exactly: distinct k-step outcome masks,
finite-horizon values at probed beliefs versus the indefinite blind value,
minimal obstructions and the slowest death rate per cube."""
import time, random
from fractions import Fraction as Q
from itertools import product
from collections import Counter
import numpy as np

from p05_core import cells, actions, D, game_value, alpha_masks, ham


def masks_k(m, k, L):
    """distinct k-step survival masks (as sorted uint64 array) over all words"""
    C = cells(m)
    U = actions(m)
    d = np.asarray([[D(u, th) for th in C] for u in U], dtype=np.int16)
    nU = len(U)
    seq = np.indices((nU,) * k, dtype=np.uint8).reshape(k, -1)
    stock = np.full((seq.shape[1], len(C)), L, dtype=np.int16)
    alive = np.ones_like(stock, dtype=bool)
    for t in range(k):
        stock += d[seq[t]]
        alive &= stock >= 0
    w = (np.uint64(1) << np.arange(len(C), dtype=np.uint64))
    masks = (alive.astype(np.uint64) * w).sum(axis=1, dtype=np.uint64)
    return np.unique(masks)


def mask_to_set(mask, C):
    return frozenset(th for i, th in enumerate(C) if (int(mask) >> i) & 1)


def value_from_masks(b, masks, n):
    """max over masks of the b-mass (b: list of Fractions)"""
    best = Q(0)
    for mk in masks:
        mk = int(mk)
        s = sum(b[i] for i in range(n) if (mk >> i) & 1)
        if s > best:
            best = s
    return best


def beliefs(m, seed=7, n_random=5):
    C = cells(m)
    n = len(C)
    rng = random.Random(seed)
    out = {"uniform": [Q(1, n)] * n}
    for r in range(n_random):
        w = [rng.randint(1, 20) for _ in range(n)]
        s = sum(w)
        out[f"random{r+1}"] = [Q(x, s) for x in w]
    # adversarial: mass on a far pair (distance m-2 >= pair bound+1) and on an antipodal pair
    a = C[0]
    far = next(th for th in C if ham(a, th) == m - 2)
    anti = tuple(-x for x in a)
    b = [Q(0)] * n
    b[C.index(a)] = Q(1, 2); b[C.index(far)] = Q(1, 2)
    out["far_pair"] = b
    b = [Q(0)] * n
    b[C.index(a)] = Q(1, 2); b[C.index(anti)] = Q(1, 2)
    out["antipodal_pair"] = b
    # mass spread on a radius-1 ball plus the antipode
    ballc = [i for i, th in enumerate(C) if ham(a, th) <= 1]
    b = [Q(0)] * n
    for i in ballc:
        b[i] = Q(1, 2 * len(ballc))
    b[C.index(anti)] += Q(1, 2)
    out["ball_plus_antipode"] = b
    return out


def study(m, levels, k, census_masks, census_thr):
    """for each level: number of k-step masks, how many are survivable sets,
    values at beliefs for horizons 1..k and the indefinite value."""
    C = cells(m)
    n = len(C)
    out = {"m": m, "k": k, "levels": {}}
    B = beliefs(m)
    for L in levels:
        t = time.time()
        row = {"n_masks": {}, "n_masks_survivable": {}, "values": {}}
        surv_masks = census_masks[census_thr <= L]
        maximal = None
        for kk in range(1, k + 1):
            mk = masks_k(m, kk, L)
            row["n_masks"][kk] = int(len(mk))
            row["n_masks_survivable"][kk] = int(np.isin(mk, surv_masks).sum())
            for name, b in B.items():
                row["values"].setdefault(name, {})[kk] = str(value_from_masks(b, mk, n))
        # indefinite value = max over survivable-at-L sets (use maximal ones: all of surv_masks is fine for m<=5)
        for name, b in B.items():
            row["values"][name]["inf"] = str(value_from_masks(b, surv_masks, n))
        row["time_s"] = round(time.time() - t, 2)
        out["levels"][L] = row
    return out


def obstructions(m, census_masks, cliques):
    """minimal non-survivable sets among sets of diameter <= pair bound
    (every proper subset survivable): count, sizes, max V (slowest death)"""
    C = cells(m)
    n = len(C)
    nonsurv = cliques[~np.isin(cliques, census_masks)]
    minimal = np.ones(len(nonsurv), dtype=bool)
    for i in range(n):
        bit = np.uint64(1) << np.uint64(i)
        has = (nonsurv & bit) != 0
        sub = nonsurv[has] & ~bit
        ok = np.isin(sub, census_masks) | (sub == 0)
        idx = np.nonzero(has)[0]
        minimal[idx[~ok]] = False
    mins = nonsurv[minimal]
    sizes = Counter(int(bin(int(x)).count("1")) for x in mins)
    # V of each minimal obstruction (exact LP); group by (size, V)
    byV = Counter()
    Vmax = Q(0)
    examples = {}
    for mk in mins:
        S = mask_to_set(mk, C)
        V = game_value(S)[0]
        byV[(len(S), str(V))] += 1
        if V > Vmax:
            Vmax = V
        examples.setdefault((len(S), str(V)), sorted(S))
    # pairs beyond the pair bound are minimal obstructions too (V = m - h)
    from p05_core import pair_bound_distance
    dmax = pair_bound_distance(m)
    far_pairs = Counter()
    for i in range(n):
        for j in range(i + 1, n):
            h = ham(C[i], C[j])
            if h > dmax:
                far_pairs[h] += 1
    pairV = {h: str(Q(m - h)) for h in far_pairs}
    worst_pair_V = Q(m - dmax - 1)
    Vmax_all = max(Vmax, worst_pair_V)
    return {"n_nonsurvivable_cliques": int(len(nonsurv)), "n_minimal_obstructions": int(len(mins)),
            "far_pairs_by_distance": sorted(far_pairs.items()), "far_pair_V": pairV,
            "V_max_all": str(Vmax_all), "death_rate_min_tenths_all": str(5 - 2 * Vmax_all),
            "sizes": sorted(sizes.items()), "by_size_V": sorted((list(k), v) for k, v in byV.items()),
            "V_max": str(Vmax), "death_rate_min_tenths": str(5 - 2 * Vmax),
            "examples": {f"{k[0]}|{k[1]}": [list(th) for th in v] for k, v in examples.items()}}


if __name__ == "__main__":
    import json, sys
    out = {}
    for m in (4, 5, 6):
        z = np.load(f"census_m{m}.npz")
        if m < 6:
            out[m] = {"pbvi": study(m, list(range(0, 16)), 4, z["masks"], z["thr"])}
        else:
            out[m] = {"pbvi": study(m, [0, 1, 3, 5, 10, 15], 3, z["masks"], z["thr"])}
        out[m]["obstructions"] = obstructions(m, z["masks"], z["cliques"])
        print(m, {L: (r["n_masks"], r["n_masks_survivable"]) for L, r in out[m]["pbvi"]["levels"].items()})
        print(out[m]["obstructions"])
    json.dump(out, open("pbvi_out.json", "w"), indent=1, default=str)

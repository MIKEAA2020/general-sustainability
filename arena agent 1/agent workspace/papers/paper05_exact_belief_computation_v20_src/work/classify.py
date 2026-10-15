"""Complete classification of blind-survivable cell sets for m = 4, 5, 6
(and the explicit census per level).  Exact; writes a dict (see run_all)."""
import time
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from collections import Counter, defaultdict
import numpy as np

from p05_core import (cells, ham, distance_graph, maximal_cliques, game_value,
                      maximal_survivable_in, globally_maximal, certified_threshold,
                      orbit_size, kleitman_bound, pair_bound_distance, rstar,
                      first_step_bound, product_mixture, periodic_word, word_dip,
                      actions, D)


def profile(c):
    c = list(c)
    return tuple(sorted(tuple(sorted(ham(a, b) for b in c if b is not a)) for a in c))


def group_elements(m):
    for perm in permutations(range(m)):
        for flips in product((1, -1), repeat=m):
            yield perm, flips


def apply(g, th):
    perm, flips = g
    return tuple(th[perm[i]] * flips[i] for i in range(len(th)))


def orbit_images(M, m):
    """dict frozenset(image) -> ordered image tuple, over the whole group"""
    M = list(M)
    out = {}
    for g in group_elements(m):
        img = tuple(apply(g, th) for th in M)
        out.setdefault(frozenset(img), img)
    return out


def classify(m, levels=None, verbose=True, max_steps=400):
    t0 = time.time()
    C = cells(m)
    idx = {th: i for i, th in enumerate(C)}
    dmax = pair_bound_distance(m)
    res = {"m": m, "n_cells": len(C), "pair_distance_bound": dmax,
           "kleitman": kleitman_bound(m, dmax), "rstar": rstar(m)}
    V, adj = distance_graph(m, dmax)
    cl = maximal_cliques(V, adj)
    res["n_maximal_cliques"] = len(cl)
    res["maximal_clique_sizes"] = sorted(Counter(len(c) for c in cl).items())
    res["max_clique_size"] = max(len(c) for c in cl)
    # all cliques (sets of diameter <= dmax) by subset enumeration of maximal cliques
    masks = []
    for c in cl:
        ids = [idx[th] for th in c]
        k = len(ids)
        sub = np.arange(1, 2 ** k, dtype=np.uint64)
        g = np.zeros_like(sub)
        for j, i in enumerate(ids):
            g |= ((sub >> np.uint64(j)) & np.uint64(1)) << np.uint64(i)
        masks.append(g)
    all_cliques = np.unique(np.concatenate(masks))
    res["n_cliques_nonempty"] = int(len(all_cliques))
    # orbits of maximal cliques via invariant classes checked by orbit sizes
    groups = defaultdict(list)
    for c in cl:
        groups[profile(c)].append(c)
    reps = []
    for key, g in sorted(groups.items(), key=lambda kv: (-len(kv[1][0]), kv[0])):
        c = g[0]
        osz = orbit_size(c)
        assert osz == len(g), "invariant class is not a single orbit"
        Vc, y, q = game_value(c)
        reps.append({"size": len(c), "orbit": len(g), "V": str(Vc), "y": [str(v) for v in y],
                     "survivable": Vc >= Q(5, 2), "cells": [list(th) for th in sorted(c)]})
    res["maximal_clique_orbits"] = reps
    if verbose:
        print(f"m={m}: {len(C)} cells, {len(cl)} maximal cliques, {len(reps)} orbits, "
              f"{res['n_cliques_nonempty']} cliques, {time.time()-t0:.1f}s")
    # maximal survivable sets
    lp = {}
    found = {}
    for key, g in groups.items():
        c = g[0]
        for T in maximal_survivable_in(c, lp):
            gm = globally_maximal(T, dmax, lp)
            if gm:
                found[frozenset(T)] = True
    # orbits of globally maximal survivable sets
    maxorbits = []
    seen = set()
    for T in found:
        if T in seen:
            continue
        imgs = orbit_images(T, m)
        for f in imgs:
            seen.add(f)
        VT, y, q = lp[T] if T in lp else game_value(T)
        p = product_mixture(y)
        w = periodic_word(p)
        thr = certified_threshold(T, caps=(6, 12, 24, 48, 96), max_steps=max_steps)
        maxorbits.append({"size": len(T), "orbit": len(imgs), "V": str(VT), "y": [str(v) for v in y],
                          "threshold": thr["L"], "threshold_cert": thr,
                          "first_step_bound": first_step_bound(T),
                          "word_period": len(w), "word_dip": word_dip(w, T),
                          "profile0": list(profile(T)[0]),
                          "cells": [list(th) for th in sorted(T)], "_images": imgs, "_rep": T})
    maxorbits.sort(key=lambda d: (-d["size"], d["orbit"]))
    res["n_maximal_survivable"] = sum(d["orbit"] for d in maxorbits)
    if verbose:
        for d in maxorbits:
            print(f"  maximal survivable: size {d['size']} orbit {d['orbit']} V={d['V']} L*={d['threshold']} "
                  f"cert={d['threshold_cert'].get('certified')} fsb={d['first_step_bound']}")
    # thresholds of all subsets of each representative (exact, certified)
    glob_masks, glob_thr, glob_V = [], [], []
    subset_records = []
    n_uncert = 0
    for d in maxorbits:
        T = list(d["_rep"])
        k = len(T)
        thr_by_mask = {}
        V_by_mask = {}
        for mask in range(1, 2 ** k):
            sub = [T[j] for j in range(k) if mask >> j & 1]
            VT = game_value(sub)[0]
            V_by_mask[mask] = VT
            ct = certified_threshold(sub, caps=(6, 12, 24, 48, 96), max_steps=max_steps)
            assert ct["L"] is not None
            if not ct.get("certified", True):
                n_uncert += 1
            thr_by_mask[mask] = ct["L"]
        d["subset_threshold_hist"] = sorted(Counter(thr_by_mask.values()).items())
        d["subset_knife_edge"] = sum(1 for v in V_by_mask.values() if v == Q(5, 2))
        # map to all images
        sub = np.arange(1, 2 ** k, dtype=np.uint64)
        thr_arr = np.array([thr_by_mask[i] for i in range(1, 2 ** k)], dtype=np.int16)
        V_arr = np.array([float(V_by_mask[i]) for i in range(1, 2 ** k)], dtype=np.float64)
        for f, img in d["_images"].items():
            ids = [idx[th] for th in img]
            g = np.zeros_like(sub)
            for j, i in enumerate(ids):
                g |= ((sub >> np.uint64(j)) & np.uint64(1)) << np.uint64(i)
            glob_masks.append(g)
            glob_thr.append(thr_arr)
            glob_V.append(V_arr)
    gm = np.concatenate(glob_masks)
    gt = np.concatenate(glob_thr)
    gV = np.concatenate(glob_V)
    uniq, first = np.unique(gm, return_index=True)
    # consistency: same set reached through different maximal sets must have equal threshold
    order = np.argsort(gm, kind="stable")
    gm_s, gt_s = gm[order], gt[order]
    same = gm_s[1:] == gm_s[:-1]
    assert np.all(gt_s[1:][same] == gt_s[:-1][same]), "threshold mismatch across images"
    thr_u = gt[first]
    V_u = gV[first]
    res["n_survivable_some_level"] = int(len(uniq))
    saved = {"masks": uniq, "thr": thr_u, "V": V_u, "cliques": all_cliques}
    res["n_uncertified_thresholds"] = n_uncert
    res["knife_edge_sets"] = int(np.sum(np.isclose(V_u, 2.5)))
    res["threshold_hist"] = sorted((int(k), int(v)) for k, v in Counter(thr_u.tolist()).items())
    Lmax = int(thr_u.max())
    levels = list(range(0, Lmax + 1)) if levels is None else levels
    census = []
    for L in levels:
        A = uniq[thr_u <= L]
        Aset = A  # sorted
        nonmax = np.zeros(len(A), dtype=bool)
        for i in range(len(C)):
            bit = np.uint64(1) << np.uint64(i)
            cand_idx = np.nonzero((A & bit) == 0)[0]
            sup = A[cand_idx] | bit
            hit = np.isin(sup, Aset, assume_unique=False)
            nonmax[cand_idx[hit]] = True
        maxi = A[~nonmax]
        saved[f"max_L{L}"] = maxi
        sizes = Counter(int(bin(int(x)).count("1")) for x in maxi)
        census.append({"L": L, "n_survivable": int(len(A)), "n_maximal": int(len(maxi)),
                       "maximal_sizes": sorted(sizes.items())})
        if verbose:
            print(f"  level L={L}: survivable sets {len(A)}, maximal {len(maxi)}, sizes {sorted(sizes.items())}")
    res["census"] = census
    np.savez_compressed(f"census_m{m}.npz", **saved)
    res["power_set"] = 2 ** len(C)
    for d in maxorbits:
        d.pop("_images")
        d.pop("_rep")
    res["maximal_survivable_orbits"] = maxorbits
    res["time_s"] = round(time.time() - t0, 1)
    return res


if __name__ == "__main__":
    import json, sys
    ms = [int(a) for a in sys.argv[1:]] or [4, 5, 6]
    out = {}
    for m in ms:
        out[str(m)] = classify(m)
    json.dump(out, open("classify_out.json", "w"), indent=1, default=str)

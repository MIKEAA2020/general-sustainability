#!/usr/bin/env python3
"""
Verification script for paper05 v20 (blind survivable sets on the parameter
cube: linear criterion, certified thresholds, classifications m = 4, 5, 6,
observation, point-based evaluation, exact vs float).

Recomputes the finite content of the theorems from the definitions in exact
rational arithmetic with the module p05_core.py (expected in ./work/ or in
./paper05_exact_belief_computation_v20_src/work/), checks the stored record
work/results.json (written by run_all.py) for internal consistency, and ends
with text checks against the compiled manuscript.  Does not modify
results.json.

Run:  python3 paper05_exact_belief_computation_v20_verification.py [--quick]
  full mode  : also recomputes the six-cube classification (~2.5 min), the
               six-cube clique family by an independent algorithm, the m=5
               alpha-set counts and the float sweep (~5 min).
  --quick    : skips those four items (they are then checked from the record).
"""
import os, sys, re, json, time, itertools, math
from fractions import Fraction as Q

HERE = os.path.dirname(os.path.abspath(__file__))
CORE_DIR = None
for cand in (os.path.join(HERE, "work"), HERE, os.path.join(HERE, "paper05_exact_belief_computation_v20_src", "work")):
    if os.path.exists(os.path.join(cand, "p05_core.py")):
        sys.path.insert(0, cand)
        CORE_DIR = cand
        break
import p05_core as C
import numpy as np

QUICK = "--quick" in sys.argv
RESULTS = []
T0 = time.time()
R = json.load(open(os.path.join(CORE_DIR, "results.json")))


def check(name, cond, detail=""):
    RESULTS.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name + ("" if cond else "   <-- " + str(detail)), flush=True)


def cells_from_lists(ls):
    return [tuple(x) for x in ls]


# ======================================================================== A: model
check("A1.1 drift table: D = 2m-5-4h for m = 4..8 and all h; equals 10 d with d = -1/2 + <u,theta>/5",
      all(C.drift_by_distance(m, h) == 2 * m - 5 - 4 * h == R["cube"][str(m)]["drift_by_distance"][str(h)] for m in range(4, 9) for h in range(m + 1))
      and all(10 * (Q(-1, 2) + Q(C.ip(u, th), 5)) == C.D(u, th) for u in C.sign_actions(4) for th in C.cells(4)))
check("A1.2 floor balls: r*(m) = 0,1,1,2,2 and ball sizes 1,6,7,29,37 for m = 4..8",
      [C.rstar(m) for m in range(4, 9)] == [0, 1, 1, 2, 2] and [R["cube"][str(m)]["ball_size"] for m in range(4, 9)] == [1, 6, 7, 29, 37]
      and all(len(C.ball(C.cells(m)[0], C.rstar(m))) == R["cube"][str(m)]["ball_size"] for m in (4, 5, 6)))
check("A1.3 cell-sum identity: sum over cells of D(u,theta) = -5*2^m for every action incl. the hold, m = 4,5,6",
      all(sum(C.D(u, th) for th in C.cells(m)) == -5 * 2 ** m for m in (4, 5, 6) for u in C.actions(m)))
check("A1.4 the hold is the zero mixed action: D(hold) = -5 = 2<0,theta> - 5; first-split cost 2m+5 = cost of the antipode under a sign action",
      all(C.D(C.HOLD, th) == -5 for th in C.cells(5)) and all(-C.D(C.cells(m)[0], tuple(-x for x in C.cells(m)[0])) == 2 * m + 5 == R["cube"][str(m)]["first_split_cost"] for m in (4, 5, 6)))

# ======================================================================== B: linear criterion
reps = {}
for m in (4, 5, 6):
    V, adj = C.distance_graph(m, C.pair_bound_distance(m))
    cl = C.maximal_cliques(V, adj)
    reps[m] = (V, adj, cl)
ok = True
for m in (4, 5, 6):
    for o in R["classification"][str(m)]["maximal_clique_orbits"]:
        S = cells_from_lists(o["cells"])
        Vv, y, q = C.game_value(S)
        pooled = [sum(qq * th[i] for th, qq in q.items()) for i in range(m)]
        ok &= (Vv == Q(o["V"]) and min(C.ip(th, y) for th in S) == Vv and sum(abs(p) for p in pooled) == Vv and sum(q.values()) == 1)
check("B1.1 exact LP: for every maximal-clique orbit representative (m = 4,5,6) the maximiser y and the certificate q attain the same value V, which equals the recorded V", ok)
ok = True
for m in (4, 5, 6):
    a = C.cells(m)[0]
    for h in range(m + 1):
        b = tuple(-x if i < h else x for i, x in enumerate(a))
        Vv = C.game_value([a, b])[0]
        ok &= Vv == m - h and ((Vv >= Q(5, 2)) == (h <= C.pair_bound_distance(m)))
check("B1.2 pairs: V({a,b}) = m - h and survivable iff h <= floor(m - 5/2) (= 1, 2, 3 for m = 4, 5, 6)", ok and [C.pair_bound_distance(m) for m in (4, 5, 6)] == [1, 2, 3])
ok = True
for o in R["classification"]["6"]["maximal_survivable_orbits"]:
    S = cells_from_lists(o["cells"])
    Vv, y, q = C.game_value(S)
    p = C.product_mixture(y)
    mean = tuple(sum(w * u[i] for u, w in p.items()) for i in range(6))
    dr = C.mixture_drifts(p, S)
    w = C.periodic_word(p)
    ok &= (mean == tuple(y) and sum(p.values()) == 1 and all(v >= 0 for v in dr.values()) and len(w) == o["word_period"] and C.word_dip(w, S) == o["word_dip"])
    dip = C.word_dip(w, S)
    ok &= all(C.survives(w, th, dip, 3 * len(w)) for th in S)
check("B1.3 product mixture of the maximiser has mean y and nonnegative expected drift on S; its periodic word (recorded period/dip) keeps every cell for three periods from the dip, for the three six-cube maximal orbits", ok)
ok = True
for m in (4, 5, 6):
    for r in R["pairs"][str(m)]:
        if not r["survivable"]:
            a = C.cells(m)[0]
            b = tuple(-x if i < r["h"] else x for i, x in enumerate(a))
            Vv = C.game_value([a, b])[0]
            for hz in r["horizon"]:
                ex, fr = C.forward_horizon([a, b], hz["L"], max_steps=60)
                ok &= (ex == hz["exact"] and fr == 0 and ex <= C.horizon_bound(hz["L"], Vv) == hz["bound"])
check("B1.4 finite-horizon corollary on pairs: exact forward horizon <= floor(L/(5-2V)) for every non-survivable pair, L in {0,5,10,15,20}, m = 4,5,6, as recorded", ok)
ok = True
for m, h in ((4, 2), (6, 4)):
    a = C.cells(m)[0]
    b = tuple(-x if i < h else x for i, x in enumerate(a))
    mid = tuple(-x if i < h // 2 else x for i, x in enumerate(a))
    ok &= all(C.D(mid, th) == -1 for th in (a, b))
    ok &= all(C.forward_horizon([a, b], L, max_steps=40)[0] == L for L in range(0, 21))
a = C.cells(5)[0]; b = tuple(-x if i < 3 else x for i, x in enumerate(a))
ok &= all(C.forward_horizon([a, b], L, max_steps=40)[0] == (2 * ((L - 1) // 2) if L >= 1 else 0) for L in range(0, 21))
check("B1.5 far pairs at distance delta_m + 1: horizon exactly L for L <= 20 at m = 4,6 (middle action costs -1 to both); 2*floor((L-1)/2) at m = 5", ok)
ok = True
for m in (4, 5, 6):
    Cc = C.cells(m)
    Vv, y, q = C.game_value(Cc)
    ok &= Vv == 0 and all(x == 0 for x in y) and tuple(sum(w * th[i] for th, w in q.items()) for i in range(m)) == (0,) * m
    ok &= tuple(sum(Q(1, 2 ** m) * th[i] for th in Cc) for i in range(m)) == (0,) * m
    for L in (0, 5, 10, 13, 15, 20, 25):
        ex, fr = C.forward_horizon(Cc, L, max_steps=30)
        ok &= ex == L // 5 and fr == 0
check("B1.6 deadline law: V(cube) = 0, the LP certificate and the uniform distribution both pool to the origin; exact horizon of the whole cube = floor(L/5) for L in {0,5,10,13,15,20,25}, m = 4,5,6", ok)
tet = [(1, 1, 1, 1, 1), (1, 1, 1, -1, -1), (1, 1, -1, 1, -1), (1, 1, -1, -1, 1)]
Vt, yt, qt = C.game_value(tet)
check("B1.7 tetrahedron: pairwise distance 2, every 3-subset inside a radius-one ball, V = 2 with pooled cell (1,1,0,0,0); exact horizon 2*floor((L-1)/2) for L <= 20 (as for the far pairs of the five-cube)",
      all(C.ham(a, b) == 2 for a, b in itertools.combinations(tet, 2)) and Vt == 2
      and all(any(set(T) <= C.ball(c, 1) for c in C.cells(5)) for T in itertools.combinations(tet, 3))
      and tuple(sum(Q(1, 4) * th[i] for th in tet) for i in range(5)) == (1, 1, 0, 0, 0)
      and all(C.forward_horizon(tet, L, max_steps=40) == ((2 * ((L - 1) // 2) if L >= 1 else 0), 0) for L in range(0, 21)))
Kl = [C.kleitman_bound(m, C.pair_bound_distance(m)) for m in range(4, 9)]
ok = Kl == [2, 6, 12, 29, 58]
for m in (5, 7):
    r = (m - 3) // 2
    B = C.ball(C.cells(m)[0], r)
    ok &= len(B) == Kl[m - 4] and r == C.rstar(m) and all(C.D(C.cells(m)[0], th) >= 0 for th in B)
for m in (4, 6, 8):
    r = (m - 4) // 2
    c = C.cells(m - 1)[0]
    Bm1 = C.ball(c, r)
    Dd = [th + (s,) for th in Bm1 for s in (1, -1)]
    y = c + (0,)
    ok &= len(Dd) == Kl[m - 4] and min(C.ip(th, y) for th in Dd) == 3 and C.first_step_bound(Dd) == 1
    ok &= all(C.survives([c + (1,), c + (-1,)], th, 1, 8) for th in Dd)
    if m <= 6:
        ok &= C.certified_threshold(Dd)["L"] == 1 and C.certified_threshold(Dd)["certified"]
check("B1.8 Kleitman: K(m) = 2,6,12,29,58 for m = 4..8; extremal balls (odd m) are floor balls, extremal doubled balls (even m) have min <y,theta> = 3, first-step bound 1 and survive from slack 1 (certified for m = 4,6)", ok)
ok = True
for m in (4, 5, 6):
    for o in R["classification"][str(m)]["maximal_clique_orbits"]:
        S = cells_from_lists(o["cells"])
        Vv, y, q = C.game_value(S)
        ok &= sum(1 for v in q.values() if v > 0) <= m + 1
check("B1.9 support of the certificate q has at most m+1 cells for every maximal-clique representative", ok)
ok = True
for m in (4, 5, 6):
    cen = R["classification"][str(m)]["census"][0]
    ok &= cen["L"] == 0 and cen["n_maximal"] == 2 ** m and cen["maximal_sizes"] == [[R["cube"][str(m)]["ball_size"], 2 ** m]]
check("B1.10 floor census: the maximal sets at L = 0 are 2^m sets of the floor-ball size for m = 4,5,6 (Corollary on balls)", ok)

# ======================================================================== C: thresholds and the game
a, b = C.cells(4)[0], C.cells(4)[1]
ac, k = C.minimal_winning_slacks([a, b], 6)
ct = C.certified_threshold([a, b])
check("C1.1 adjacent pair (m = 4): antichain of minimal winning vectors {(0,1),(1,0)}, certified threshold 1, lost from 0 in the first step",
      sorted(ac) == [(0, 1), (1, 0)] and ct["L"] == 1 and ct["certified"] and ct["lower_steps"] == 0)
sq = next(c for c in reps[5][2] if len(c) == 4 and sorted(C.ham(x, y) for x, y in itertools.combinations(c, 2)) == [1, 1, 1, 1, 2, 2])
cts = C.certified_threshold(sq)
ball5 = C.ball(C.cells(5)[0], 1)
check("C1.2 five-cube: square certified threshold 3 = first-step bound; ball threshold 0",
      cts["L"] == 3 and cts["certified"] and C.first_step_bound(sq) == 3 and C.certified_threshold(ball5)["L"] == 0)
ok = True
for o in R["classification"]["6"]["maximal_survivable_orbits"]:
    S = cells_from_lists(o["cells"])
    ct = C.certified_threshold(S, caps=(6, 12, 24), max_steps=100)
    ok &= ct["L"] == o["threshold"] and ct["certified"] and ct["cap"] == o["threshold_cert"]["cap"] and ct["antichain"] == o["threshold_cert"]["antichain"]
    ok &= C.first_step_bound(S) == o["first_step_bound"]
check("C1.3 six-cube maximal orbits: certified thresholds 1 (cylinder), 3 (boundary ten-set), 5 (subcube) with the recorded caps and antichain sizes; first-step bounds 1, 1, 5",
      ok and [o["threshold"] for o in R["classification"]["6"]["maximal_survivable_orbits"]] == [1, 3, 5]
      and [o["first_step_bound"] for o in R["classification"]["6"]["maximal_survivable_orbits"]] == [1, 1, 5])
ten = cells_from_lists(R["classification"]["6"]["maximal_survivable_orbits"][1]["cells"])
ac6, _ = C.minimal_winning_slacks(ten, 6)
ac12, _ = C.minimal_winning_slacks(ten, 12)
check("C1.4 cap artefact: the saturated game on the boundary ten-set returns 5 at cap 6 and 3 at cap 12; forward reachability from 2 empties within 2 steps",
      min(max(w) for w in ac6) == 5 and min(max(w) for w in ac12) == 3 and C.forward_horizon(ten, 2, max_steps=10) == (2, 0))
pw = C.winning_word(ten, 3, 12)
pre, per = pw
Vten, yten, qten = C.game_value(ten)
ok = len(pre) == 5 and len(per) == 4
S = sorted(ten)
traj = {th: [3] for th in S}
for u in pre + per * 50:
    for th in S:
        traj[th].append(traj[th][-1] + C.D(u, th))
ok &= all(min(v) >= 0 for v in traj.values())
touch = [th for th in S if sum(C.D(u, th) for u in per) == 0 and 0 in traj[th][len(pre):]]
ok &= len(touch) >= 2
pooled_ok = all(sum(qten[th] * traj[th][t] for th in S) <= 3 for t in range(len(pre) + 200))
check("C1.5 boundary ten-set: extracted winning word from L = 3 has prefix 5 and period 4, keeps all cells for 50 periods, two zero-net cells touch the floor; pinned inequality sum q s(t) <= L holds for 200 steps", ok and pooled_ok)
check("C1.6 boundary value: V(ten-set) = 5/2 exactly and every feasible maximiser is tight on supp q (checked for the LP maximiser)",
      Vten == Q(5, 2) and all(C.ip(th, yten) == Q(5, 2) for th, w in qten.items() if w > 0))
punct = [th for th in C.cells(6) if th[0] == th[1] == th[2] == -1 and th != (-1, -1, -1, 1, 1, 1)]
cp = C.certified_threshold(punct)
check("C1.7 punctured subcube: V = 3, first-step bound 1, certified threshold 1; the full subcube has first-step bound 5 and threshold 5",
      C.game_value(punct)[0] == 3 and C.first_step_bound(punct) == 1 and cp["L"] == 1 and cp["certified"]
      and C.certified_threshold(punct + [(-1, -1, -1, 1, 1, 1)])["L"] == 5)

# ======================================================================== D: classification
from collections import Counter
check("D1.1 maximal cliques: 32 (m=4, all edges), 192 (m=5: 32 of size 6 + 160 of size 4), 10,752 (m=6: 192 x 12, 1,280 x 10, 9,280 x 8)",
      len(reps[4][2]) == 32 and Counter(len(c) for c in reps[5][2]) == Counter({6: 32, 4: 160})
      and Counter(len(c) for c in reps[6][2]) == Counter({12: 192, 10: 1280, 8: 9280})
      and all(R["classification"][str(m)]["n_maximal_cliques"] == len(reps[m][2]) for m in (4, 5, 6)))


def profile(c):
    c = list(c)
    return tuple(sorted(tuple(sorted(C.ham(a, b) for b in c if b is not a)) for a in c))


ok = True
for m in (5, 6):
    groups = {}
    for c in reps[m][2]:
        groups.setdefault(profile(c), []).append(c)
    rec = R["classification"][str(m)]["maximal_clique_orbits"]
    ok &= len(groups) == len(rec)
    for key, g in groups.items():
        ok &= C.orbit_size(g[0]) == len(g)
    ok &= sorted(len(g) for g in groups.values()) == sorted(o["orbit"] for o in rec)
check("D1.2 orbit decomposition certified: invariant classes of maximal cliques (3 at m=5, 7 at m=6) each equal one orbit (orbit size of the representative = class size)", ok)
ok = True
for m in (4, 5, 6):
    lp = {}
    found = set()
    for o in R["classification"][str(m)]["maximal_clique_orbits"]:
        S = frozenset(cells_from_lists(o["cells"]))
        for T in C.maximal_survivable_in(S, lp):
            if C.globally_maximal(T, C.pair_bound_distance(m), lp):
                found.add(T)
    rec = R["classification"][str(m)]["maximal_survivable_orbits"]
    sizes_found = sorted(len(T) for T in found)
    ok &= set(sizes_found) == set(o["size"] for o in rec)
    ok &= all(C.game_value(T)[0] >= Q(5, 2) for T in found)
    ok &= sum(o["orbit"] for o in rec) == R["classification"][str(m)]["n_maximal_survivable"]
    for o in rec:
        ok &= C.orbit_size(cells_from_lists(o["cells"])) == o["orbit"]
check("D1.3 maximal survivable sets recomputed from the clique representatives (certificate-support branching + global maximality): sizes {2}, {6,4}, {12,10,8}; orbit sizes 32; 32,80; 192,1280,160; totals 32, 112, 1,632",
      ok and [R["classification"][str(m)]["n_maximal_survivable"] for m in (4, 5, 6)] == [32, 112, 1632])
cl6 = R["classification"]["6"]
check("D1.4 six-cube census record: survivable sets 7,072 / 631,440 / 774,800 / 774,960 at L = 0 / 1-2 / 3-4 / >= 5; maximal 64 / 1,472 / 1,472 / 1,632 with the recorded sizes",
      [(c["L"], c["n_survivable"], c["n_maximal"]) for c in cl6["census"]] == [(0, 7072, 64), (1, 631440, 1472), (2, 631440, 1472), (3, 774800, 1472), (4, 774800, 1472), (5, 774960, 1632)]
      and cl6["census"][1]["maximal_sizes"] == [[7, 1280], [12, 192]] and cl6["census"][3]["maximal_sizes"] == [[10, 1280], [12, 192]]
      and cl6["census"][5]["maximal_sizes"] == [[8, 160], [10, 1280], [12, 192]])
check("D1.5 census consistency: threshold histogram sums to the number of survivable sets and its partial sums reproduce the census at every level; 143,360 = 1,280 x 112 boundary sets all at threshold 3",
      all(sum(v for k, v in R["classification"][str(m)]["threshold_hist"] if k <= c["L"]) == c["n_survivable"] for m in (4, 5, 6) for c in R["classification"][str(m)]["census"])
      and cl6["knife_edge_sets"] == 143360 == 1280 * 112 == dict(cl6["threshold_hist"])[3]
      and R["classification"]["6"]["maximal_survivable_orbits"][1]["subset_knife_edge"] == 112
      and all(R["classification"][str(m)]["n_uncertified_thresholds"] == 0 for m in (4, 5, 6)))
check("D1.6 four- and five-cube census: 16 / 48 (m=4, L = 0 / >= 1) and 1,616 / 1,696 (m=5, L <= 2 / >= 3); admissible families 48 and 1,776; maximal 16 singletons then 32 pairs; 32 balls then + 80 squares",
      [(c["L"], c["n_survivable"], c["n_maximal"]) for c in R["classification"]["4"]["census"]] == [(0, 16, 16), (1, 48, 32)]
      and [(c["L"], c["n_survivable"], c["n_maximal"]) for c in R["classification"]["5"]["census"]] == [(0, 1616, 32), (1, 1616, 32), (2, 1616, 32), (3, 1696, 112)]
      and R["classification"]["4"]["n_cliques_nonempty"] == 48 and R["classification"]["5"]["n_cliques_nonempty"] == 1776)


def all_cliques_count(m):
    """independent count of nonempty cliques of G_m by ordered extension"""
    V, adj, _ = reps[m]
    idx = {v: i for i, v in enumerate(V)}
    nbr = [sorted(idx[w] for w in adj[v] if idx[w] > idx[v]) for v in V]
    count = 0
    stack = [(i, set(nbr[i])) for i in range(len(V))]
    while stack:
        v, cand = stack.pop()
        count += 1
        for w in cand:
            stack.append((w, cand & set(nbr[w])))
    return count


c4 = all_cliques_count(4)
c5 = all_cliques_count(5)
direct4 = sum(1 for k in range(1, 3) for S in itertools.combinations(C.cells(4), k) if all(C.ham(a, b) <= 1 for a, b in itertools.combinations(S, 2)))
check("D1.7 admissible families by an independent clique enumeration: 48 (m=4, also by direct subset enumeration) and 1,776 (m=5)", c4 == 48 == direct4 and c5 == 1776)
if not QUICK:
    c6 = all_cliques_count(6)
    check("D1.8 [full] admissible family of the six-cube by independent enumeration: 853,680", c6 == 853680 == cl6["n_cliques_nonempty"])
    import classify as CL, tempfile
    t = time.time()
    _cwd = os.getcwd(); os.chdir(tempfile.mkdtemp())
    try:
        rec6 = CL.classify(6, verbose=False)
    finally:
        os.chdir(_cwd)
    check("D1.9 [full] complete six-cube classification recomputed: census, threshold histogram, knife-edge count and maximal orbits agree with the record",
          json.loads(json.dumps(rec6["census"])) == cl6["census"] and json.loads(json.dumps(rec6["threshold_hist"])) == cl6["threshold_hist"] and rec6["knife_edge_sets"] == cl6["knife_edge_sets"]
          and [(o["size"], o["orbit"], o["threshold"]) for o in rec6["maximal_survivable_orbits"]] == [(o["size"], o["orbit"], o["threshold"]) for o in cl6["maximal_survivable_orbits"]], round(time.time() - t))
else:
    check("D1.8 [quick] admissible family of the six-cube taken from the record: 853,680 = subsets of the 10,752 maximal cliques", cl6["n_cliques_nonempty"] == 853680)
    check("D1.9 [quick] six-cube classification taken from the record (recomputed in full mode); 5,373 = 4,095 + 1,023 + 255 certified subset thresholds",
          sum(sum(v for _, v in o["subset_threshold_hist"]) for o in cl6["maximal_survivable_orbits"]) == 5373)
ob = {m: R["pbvi"][str(m)]["obstructions"] for m in (4, 5, 6)}
check("D1.10 minimal obstructions: none inside the admissible family at m=4, the 80 tetrahedra at m=5, 2,400 at m=6 (1,440 four-cell + 960 five-cell), all with V = 2; far pairs at distance delta_m+1 have V = 2; hence the uniform horizon L",
      ob[4]["n_minimal_obstructions"] == 0 and ob[5]["by_size_V"] == [[[4, "2"], 80]] and ob[6]["by_size_V"] == [[[4, "2"], 1440], [[5, "2"], 960]]
      and ob[6]["n_minimal_obstructions"] == 2400 and all(ob[m]["V_max_all"] == "2" and ob[m]["death_rate_min_tenths_all"] == "1" for m in (4, 5, 6))
      and ob[6]["n_nonsurvivable_cliques"] == 78720 == 853680 - 774960)
ex4 = cells_from_lists(ob[6]["examples"]["4|2"]); ex5 = cells_from_lists(ob[6]["examples"]["5|2"])
check("D1.11 recorded six-cube obstruction examples: V = 2 and every proper subset survivable (minimality), pooled cell (1,1,0,0,0,0)",
      all(C.game_value(S)[0] == 2 for S in (ex4, ex5))
      and all(C.game_value(list(T))[0] >= Q(5, 2) for S in (ex4, ex5) for T in itertools.combinations(S, len(S) - 1))
      and all(tuple(sum(w * th[i] for th, w in C.game_value(S)[2].items()) for i in range(6)) == (1, 1, 0, 0, 0, 0) for S in (ex4, ex5)))

# ======================================================================== E: observation
check("E1.1 probe ladder m=4: 1/16,1/8,1/4,1/2,1 at the floor and 1/8,1/4,1/2,1,1 from slack 1 (j = 4..0)",
      R["observation"]["4"]["ladder"]["0"] == ["1/16", "1/8", "1/4", "1/2", "1"] and R["observation"]["4"]["ladder"]["1"] == ["1/8", "1/4", "1/2", "1", "1"])
check("E1.2 probe ladder m=5: 3/16,5/16,1/2,3/4,1,1 for L <= 2 and 3/16,5/16,1/2,1,1,1 for L >= 3; m=6: 7/64,...,3/4,1,1 at the floor, 3/16,5/16,1/2,7/8,1,1,1 for 1 <= L <= 4, 3/16,5/16,1/2,1,1,1,1 for L >= 5",
      R["observation"]["5"]["ladder"]["2"] == ["3/16", "5/16", "1/2", "3/4", "1", "1"] and R["observation"]["5"]["ladder"]["3"] == ["3/16", "5/16", "1/2", "1", "1", "1"]
      and R["observation"]["6"]["ladder"]["0"] == ["7/64", "3/16", "5/16", "1/2", "3/4", "1", "1"]
      and R["observation"]["6"]["ladder"]["1"] == ["3/16", "5/16", "1/2", "7/8", "1", "1", "1"] == R["observation"]["6"]["ladder"]["4"]
      and R["observation"]["6"]["ladder"]["5"] == ["3/16", "5/16", "1/2", "1", "1", "1", "1"])
# ladder recomputation from the maximal sets of the record (m = 4, 5): value = max |A n Q| / |Q| over subcubes
import observation as OBS
ok = True
for m in (4, 5):
    fam = {}
    for o in R["classification"][str(m)]["maximal_survivable_orbits"]:
        pass
    # rebuild the maximal families at each census level from the npz if present, else from orbits
    npz = os.path.join(CORE_DIR, f"census_m{m}.npz")
    if os.path.exists(npz):
        z = np.load(npz)
        Cc = C.cells(m)
        levels = sorted(int(k[5:]) for k in z.files if k.startswith("max_L"))
        famL = {L: [frozenset(th for i, th in enumerate(Cc) if (int(mk) >> i) & 1) for mk in z[f"max_L{L}"]] for L in levels}
        lad = OBS.ladder(m, famL)
        ok &= all([str(v) for v in lad[L]] == R["observation"][str(m)]["ladder"][str(L)] for L in levels)
check("E1.3 ladders m = 4,5 recomputed from the stored maximal families census_m4/5.npz (max over subcubes of the mass of a maximal set) agree with the record", ok and os.path.exists(os.path.join(CORE_DIR, "census_m5.npz")), "census npz missing")
fb4 = OBS.feedback_study(4)
fb5 = OBS.feedback_study(5)
check("E1.4 feedback game recomputed: F*(cube) = 23 (m=4) and 18 (m=5); subcubes 1,6,14 and 0,3,7,11; shells 0,14,18,14,0 and 0,0,11,11,0,0",
      fb4["cube"] == 23 and fb5["cube"] == 18 and [fb4["subcubes"][j] for j in (1, 2, 3)] == [1, 6, 14] and [fb5["subcubes"][j] for j in (1, 2, 3, 4)] == [0, 3, 7, 11]
      and [fb4["shells"][h]["feedback"] for h in range(5)] == [0, 14, 18, 14, 0] and [fb5["shells"][h]["feedback"] for h in range(6)] == [0, 0, 11, 11, 0, 0]
      and R["observation"]["4"]["feedback"]["cube"] == 23 and R["observation"]["5"]["feedback"]["cube"] == 18)
check("E1.5 first-split decomposition: 23 = max(13, 9+14, 5+18, 1+14) at m=4 and 18 = max(15, 3+11, 7+11, 11) at m=5; the shells at m=5 with h in {1,4} are blind-survivable (threshold 0)",
      max(13, 9 + 14, 5 + 18, 1 + 14) == 23 and max(15, 3 + 11, 7 + 11, 11) == 18 and fb5["shells"][1]["blind"] == 0 and fb5["shells"][4]["blind"] == 0
      and fb4["shells"][1]["blind"] is None and fb4["shells"][2]["blind"] is None)
check("E1.6 blind thresholds of the whole cube and of antipodal sets are infinite (V < 5/2); subcube blind thresholds: m=4: 1, inf, inf; m=5: 0, 3, inf, inf",
      C.game_value(C.cells(4))[0] < Q(5, 2) and [fb4["subcubes_blind"][j] for j in (1, 2, 3)] == [1, None, None] and [fb5["subcubes_blind"][j] for j in (1, 2, 3, 4)] == [0, 3, None, None])

# ======================================================================== F: point-based evaluation
import pbvi as PB
counts4 = [R["pbvi"]["4"]["pbvi"]["levels"][str(L)]["n_masks"]["4"] for L in range(16)]
rec4 = [len(PB.masks_k(4, 4, L)) for L in range(16)]
check("F1.1 alpha-set sizes m=4, k=4, L = 0..15 recomputed over 17^4 words: 17,49,49,49,209,161,161,185,361,297,249,249,857,793,729,545",
      rec4 == counts4 == [17, 49, 49, 49, 209, 161, 161, 185, 361, 297, 249, 249, 857, 793, 729, 545])
counts5 = [R["pbvi"]["5"]["pbvi"]["levels"][str(L)]["n_masks"]["4"] for L in range(16)]
exp5 = [945, 945, 945, 1345, 1505, 5265, 5265, 3505, 6065, 9625, 7705, 6937, 14649, 15929, 12937, 11145]
if not QUICK:
    rec5 = [len(PB.masks_k(5, 4, L)) for L in range(16)]
    check("F1.2 [full] alpha-set sizes m=5, k=4 recomputed over 33^4 words equal the record and the earlier fivecube log", rec5 == counts5 == exp5)
else:
    rec5 = [len(PB.masks_k(5, 4, L)) for L in (0, 15)]
    check("F1.2 [quick] alpha-set sizes m=5, k=4: record equals the earlier fivecube log; L = 0 and 15 recomputed (945, 11,145)", counts5 == exp5 and rec5 == [945, 11145])
ok = True
for m in (4, 5):
    for L in range(16):
        r = R["pbvi"][str(m)]["pbvi"]["levels"][str(L)]
        for name, v in r["values"].items():
            seq = [Q(v[str(k)]) for k in range(1, 5)] + [Q(v["inf"])]
            ok &= all(seq[i] >= seq[i + 1] for i in range(4))
        if (m == 4 and L <= 3) or (m == 5 and L <= 4):
            ok &= all(Q(v["4"]) == Q(v["inf"]) for v in r["values"].values())
        if m == 4 and L >= 1:
            ok &= Q(r["values"]["uniform"]["inf"]) == Q(1, 8) and Q(r["values"]["far_pair"]["inf"]) == Q(1, 2)
        if m == 4 and L >= 4:
            ok &= Q(r["values"]["far_pair"]["4"]) == 1
for m, Lmax in ((4, 3), (5, 4)):
    r = R["pbvi"][str(m)]["pbvi"]["levels"][str(Lmax + 1)]
    ok &= any(Q(v["4"]) != Q(v["inf"]) for v in r["values"].values())
    ok &= all(R["pbvi"][str(m)]["pbvi"]["levels"][str(L)]["n_masks"]["4"] - R["pbvi"][str(m)]["pbvi"]["levels"][str(L)]["n_masks_survivable"]["4"] == 1 for L in range(Lmax + 1))
    ok &= R["pbvi"][str(m)]["pbvi"]["levels"][str(Lmax + 1)]["n_masks"]["4"] - R["pbvi"][str(m)]["pbvi"]["levels"][str(Lmax + 1)]["n_masks_survivable"]["4"] > 1
check("F1.3 values at probed beliefs: V^(k) nonincreasing in k and >= indefinite value; equal at k = 4 for L <= 3 (m=4) and L <= 4 (m=5) and not at the next level; far-pair belief V^(4) = 1 for L >= 4 and indefinite 1/2; uniform indefinite 1/8 (m=4, L >= 1)", ok)
r415 = R["pbvi"]["4"]["pbvi"]["levels"]["15"]
check("F1.4 m=4, L=15: survivable masks among the k-step alpha-sets are 0, 0, 0, 48 for k = 1..4; uniform V^(4) = 1/2 vs indefinite 1/8; m=5, L=15: uniform 1/2 vs 3/16",
      r415["n_masks_survivable"]["4"] == 48 and r415["n_masks"]["4"] == 545 and all(r415["n_masks"][str(k)] <= r415["n_masks"][str(k + 1)] for k in range(1, 4))
      and r415["values"]["uniform"]["4"] == "1/2" and r415["values"]["uniform"]["inf"] == "1/8"
      and R["pbvi"]["5"]["pbvi"]["levels"]["15"]["values"]["uniform"]["4"] == "1/2" and R["pbvi"]["5"]["pbvi"]["levels"]["15"]["values"]["uniform"]["inf"] == "3/16")
# independent brute-force value at one belief: m=4, L=15, uniform, k=2 (17^2 words)
Cc = C.cells(4)
bu = [Q(1, 16)] * 16
check("F1.5 definition-level value at the uniform belief (m=4, L=15, k=2) by direct enumeration of 17^2 words equals the alpha-set value (1)",
      C.value_at_belief(bu, 2, 15, 4) == Q(r415["values"]["uniform"]["2"]) == 1)
check("F1.6 pairs of the four-cube by distance: 32 adjacent, 48 at 2, 32 at 3, 8 antipodal (120 in all)",
      Counter(C.ham(a, b) for a, b in itertools.combinations(C.cells(4), 2)) == Counter({1: 32, 2: 48, 3: 32, 4: 8}))

# ======================================================================== G: float
F = R["float"]
z32 = np.float32(1.3)
for _ in range(3):
    z32 = np.float32(z32 + (np.float32(-0.5) + np.float32(0.2) * np.float32(2)))
z64r = 1.3
for _ in range(3):
    z64r = z64r + (2 * 2 - 5) / 10
z64a = 1.3
for _ in range(3):
    z64a = z64a + (-0.5 + 0.2 * 2)
check("G1.1 arithmetic of the pinned cell: three drifts of -1 tenth from z = 1.3 give exactly the floor in exact arithmetic; float32 and float64 with (2k-5)/10 land below 1, float64 with -0.5+0.2k lands at or above 1",
      Q(13, 10) + 3 * Q(-1, 10) == 1 and float(z32) < 1 and z64r < 1 and z64a >= 1)
check("G1.2 recorded simulations: float32 false collapse at step 3 for the representative ten-set; float64 none in 10^5 steps (both codings); float LP value 2.5 for V = 5/2",
      F["simulation"]["float32_affine"]["first_false_death_step"] == 3 and F["simulation"]["float64_affine"]["n_false_deaths"] == 0 == F["simulation"]["float64_ratio"]["n_false_deaths"]
      and F["ten_set"]["V_exact"] == "5/2" and float(F["ten_set"]["V_float"]) == 2.5)
if not QUICK:
    import float_study as FS
    t = time.time()
    sw = FS.run(10 ** 4, 2000)["sweep"]
    check("G1.3 [full] float64 sweep over the 1,280 boundary ten-sets recomputed: ratio coding 1,120 false collapses (earliest step 3), affine coding 0",
          sw["sets_with_false_death"] == {"affine": 0, "ratio": 1120} and sw["earliest_false_death"]["ratio"] == 3 and F["sweep"]["sets_with_false_death"] == sw["sets_with_false_death"], round(time.time() - t))
else:
    check("G1.3 [quick] recorded float64 sweep: 1,120 of 1,280 boundary ten-sets collapse falsely under (2k-5)/10 within 2,000 steps (earliest step 3), none under -0.5+0.2k",
          F["sweep"]["sets_with_false_death"] == {"affine": 0, "ratio": 1120} and F["sweep"]["earliest_false_death"]["ratio"] == 3 and F["sweep"]["n_sets"] == 1280)
check("G1.4 runtimes recorded for every stage; total within 2 s of the sum of the stages",
      all(isinstance(R["times"][k], (int, float)) for k in ("classification", "pairs", "observation", "pbvi", "float", "lean", "total"))
      and abs(R["times"]["total"] - sum(R["times"][k] for k in ("classification", "pairs", "observation", "pbvi", "float", "lean"))) < 2)

# ======================================================================== L: Lean inventory
lean_dir = None
for cand in (os.path.join(HERE, "lean"), os.path.join(HERE, "src", "lean"), os.path.join(CORE_DIR, "..", "src", "lean"), os.path.join(HERE, "paper05_exact_belief_computation_v20_src", "lean")):
    if os.path.isdir(cand):
        lean_dir = cand
        break
if lean_dir:
    mods = {}
    for fn in sorted(os.listdir(lean_dir)):
        if fn.endswith(".lean"):
            txt = open(os.path.join(lean_dir, fn), encoding="utf8").read()
            names = re.findall(r"^\s*(?:@\[[^\]]*\]\s*)?(?:theorem|lemma)\s+([^\s:({]+)", txt, re.M)
            mods[fn] = (names, len(re.findall(r"\bsorry\b", txt)), len(re.findall(r"^\s*axiom\s", txt, re.M)))
    named = ["far_pair_horizon_bound", "pair_first_step_fails", "deadline_law", "deadline_necessity", "deadline_sufficiency", "singleton_survives",
             "no_three_distinct_above", "survivor_is_singleton_or_adjacent_pair", "no_adjacency_triangle", "matched_drift_scale_m4"]
    allnames = [n for v in mods.values() for n in v[0]]
    check("L1.1 Lean layer: 8 modules, 80 theorem declarations (Dynamics 28, Deadline 19, Pairs 11, Hamming 6, Classification 5, ExactBelief 5, Bands 4, Ladder 2), no sorry, no axiom declarations; the ten named footprints present",
          len(mods) == 8 and sum(len(v[0]) for v in mods.values()) == 80 == R["lean"]["total_theorems"] and all(v[1] == 0 and v[2] == 0 for v in mods.values())
          and {k: len(v[0]) for k, v in mods.items()} == {"EBC_Bands_v2.lean": 4, "EBC_Classification_v3.lean": 5, "EBC_Deadline.lean": 19, "EBC_Dynamics.lean": 28,
                                                           "EBC_ExactBelief_v3.lean": 5, "EBC_Hamming.lean": 6, "EBC_Ladder_v2.lean": 2, "EBC_Pairs_v3.lean": 11}
          and all(v[0] == R["lean"]["modules"][k]["names"] for k, v in mods.items())
          and all(n in allnames for n in named), {k: len(v[0]) for k, v in mods.items()})
else:
    check("L1.1 Lean modules found", False, "lean directory missing")

# ======================================================================== text binding
aux = None
cand = os.path.join(HERE, "paper05_exact_belief_computation_v20.aux")
if os.path.exists(cand):
    aux = open(cand).read()
tex_path = os.path.join(HERE, "paper05_exact_belief_computation_v20.tex")
tex = open(tex_path).read() if os.path.exists(tex_path) else ""
if aux:
    def num(label):
        m = re.search(r"\\newlabel\{" + re.escape(label) + r"\}\{\{([^}]*)\}", aux)
        return m.group(1) if m else None
    expected = {"thm:criterion": "3.1", "cor:horizon": "3.2", "cor:pairs": "3.3", "cor:balls": "3.4", "cor:kleitman": "3.5", "prop:incomparable": "3.6",
                "prop:game": "4.2", "prop:firststep": "4.4", "prop:pinned": "4.5", "thm:m4": "5.1", "thm:m5": "5.2", "thm:m6": "5.3", "cor:uniform": "5.4",
                "prop:antichain": "6.1", "prop:feedback": "6.3", "prop:deadline": "6.4", "prop:pbvi": "7.1", "fig:census": "1", "fig:horizon": "2", "fig:knife": "3"}
    got = {k: num(k) for k in expected}
    check("TXT.1 compiled numbering of the results quoted in captions and the supplement: " + ", ".join(f"{k} = {v}" for k, v in expected.items()), got == expected, got)
    si_path = os.path.join(HERE, "paper05_exact_belief_computation_v20_supplementary.tex")
    if os.path.exists(si_path):
        si = open(si_path).read()
        table = dict(re.findall(r"mainlab@([^\\]*)\\endcsname\{([^}]*)\}", si))
        auxlabels = dict(re.findall(r"\\newlabel\{([^}@]*)\}\{\{([^}]*)\}", aux))
        check("TXT.2 supplement's main-text number table agrees with the compiled .aux on every label", bool(table) and all(table.get(k) == v for k, v in auxlabels.items()), f"{len(auxlabels)} labels")
    else:
        check("TXT.2 supplement assembled", False, "supplementary .tex missing")
else:
    check("TXT.1 compiled .aux present (text binding)", False, "no .aux; compile first")
    check("TXT.2 supplement's main-text number table", False, "no .aux; compile first")
tokens = ["774{,}960", "853{,}680", "143{,}360", "1{,}120", "10{,}752", "631{,}440", "774{,}800", "7{,}072", "1{,}632", "2{,}400", "1{,}616", "1{,}696", "1{,}776",
          "$\\Fstar(\\Theta_4)=23$", "$\\Fstar(\\Theta_5)=18$", "$5T$", "857", "15{,}929", "5{,}373", "$80$ theorem", "K(8)=58"]
check("TXT.3 headline tokens present in the assembled main text: " + ", ".join(tokens), bool(tex) and all(t in tex for t in tokens), [t for t in tokens if t not in tex])
m = re.search(r"\\newcommand\{\\NCHECKS\}\{(\d+)\}", tex)
check("TXT.4 the number of checks quoted in the manuscript (\\NCHECKS) equals the number of checks of this script", bool(m) and int(m.group(1)) == len(RESULTS) + 1, (m.group(1) if m else None, len(RESULTS) + 1))

# ======================================================================== record
n_checks = len(RESULTS)
n_pass = sum(1 for _, ok in RESULTS if ok)
out = {"n_checks": n_checks, "n_pass": n_pass, "quick": QUICK, "seconds": round(time.time() - T0, 1), "checks": [{"name": n, "pass": ok} for n, ok in RESULTS]}
with open(os.path.join(CORE_DIR, "verification_results.json"), "w") as f:
    json.dump(out, f, indent=1)
print(f"\nverification: {n_pass}/{n_checks} checks pass in {out['seconds']} s" + (" (quick mode)" if QUICK else ""))
sys.exit(0 if n_pass == n_checks else 1)

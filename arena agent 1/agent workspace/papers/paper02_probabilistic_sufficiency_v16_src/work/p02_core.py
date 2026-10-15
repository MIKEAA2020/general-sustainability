#!/usr/bin/env python3
"""
p02_core.py -- exact module for paper02 v16 (belief-state safety values).

Everything is computed from the definitions in exact rational arithmetic
(fractions.Fraction, standard library only).  The module exposes:

  * SafetyPOMDP      finite safety POMDP with absorbing unsafe state, exact
                     alpha-vector backup (masked), belief update, open-loop
                     values, contaminated (rho) operator;
  * delayed instance closed forms and brute-force enumerations (hold,
                     open-loop, sequential-blind, observed classes), census,
                     class-difference set, deficit profile;
  * declining instance (hidden drift gate): learning deadlines, noisy probes,
                     majority repetition, probe-count bound, additive law;
  * feedback-vs-blind family (value-of-observation bound attained);
  * two-floor instance; sensor instance; two-patch instance (SI).

Run `python3 p02_core.py` to print the headline numbers.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb
import random

# --------------------------------------------------------------------------
# Generic finite safety POMDP
# --------------------------------------------------------------------------
class SafetyPOMDP:
    """states: list of safe states; actions: list; obs: list.
    T[(x,a)]   : dict x' -> prob (sub-stochastic over safe states; the rest to bottom)
    g[(x,a,x')]: dict y  -> prob (normalised over obs) -- only needed for x' safe.
    """
    def __init__(self, states, actions, obs, T, g):
        self.S, self.A, self.Y, self.T, self.g = list(states), list(actions), list(obs), T, g
        self.idx = {x: i for i, x in enumerate(self.S)}
        for (x, a), row in T.items():
            assert sum(row.values(), Q(0)) <= 1, (x, a)
        for key, law in g.items():
            assert sum(law.values(), Q(0)) == 1, key

    # ---- beliefs are dicts x -> mass over safe states (mass at bottom implicit)
    def joint(self, b, a):
        """P(y, x' | b, a) over safe x'."""
        out = {}
        for x, m in b.items():
            if m == 0:
                continue
            for x2, p in self.T[(x, a)].items():
                for y, q in self.g[(x, a, x2)].items():
                    out[(y, x2)] = out.get((y, x2), Q(0)) + m * p * q
        return out

    def step_masses(self, b, a):
        """y -> unnormalised posterior mass vector (dict over safe states)."""
        res = {y: {} for y in self.Y}
        for (y, x2), m in self.joint(b, a).items():
            if m:
                res[y][x2] = res[y].get(x2, Q(0)) + m
        return res

    # ---- exact alpha-vector value iteration (masked backup)
    def alpha0(self):
        return {tuple(Q(1) for _ in self.S)}

    def backup(self, Gamma, actions=None, prune=True):
        Gamma = sorted(Gamma)
        acts = self.A if actions is None else actions
        new = set()
        for a in acts:
            for sel in product(range(len(Gamma)), repeat=len(self.Y)):
                alpha = []
                for x in self.S:
                    s = Q(0)
                    for x2, p in self.T[(x, a)].items():
                        for yi, y in enumerate(self.Y):
                            q = self.g[(x, a, x2)].get(y, Q(0))
                            if q:
                                s += p * q * Gamma[sel[yi]][self.idx[x2]]
                    alpha.append(s)
                new.add(tuple(alpha))
        return self.prune(new) if prune else new

    @staticmethod
    def prune(vecs):
        vecs = set(vecs)
        keep = set()
        for v in vecs:
            dominated = any(w != v and all(wi >= vi for wi, vi in zip(w, v)) for w in vecs)
            if not dominated:
                keep.add(v)
        return keep

    def alpha_sets(self, k, actions=None):
        G = [self.alpha0()]
        for _ in range(k):
            G.append(self.backup(G[-1], actions))
        return G

    def value(self, Gamma, b):
        bv = [b.get(x, Q(0)) for x in self.S]
        return max(sum(ai * bi for ai, bi in zip(alpha, bv)) for alpha in Gamma)

    # ---- open-loop (blind) value: fixed action sequence, survival mass
    def openloop_value(self, b, k):
        best = Q(0)
        bestseq = None
        for seq in product(self.A, repeat=k):
            cur = dict(b)
            for a in seq:
                nxt = {}
                for x, m in cur.items():
                    for x2, p in self.T[(x, a)].items():
                        nxt[x2] = nxt.get(x2, Q(0)) + m * p
                cur = nxt
            v = sum(cur.values(), Q(0))
            if v > best:
                best, bestseq = v, seq
        return best, bestseq

    # ---- contaminated (rho) recursion on belief points, exact
    def value_rho(self, b, k, rho):
        if k == 0:
            return sum(b.values(), Q(0))
        best = None
        for a in self.A:
            masses = self.step_masses(b, a)
            vals, probs = [], []
            for y in self.Y:
                m = masses[y]
                py = sum(m.values(), Q(0))
                # continuation at every outcome: normalised posterior if py>0, else value 0
                if py > 0:
                    post = {x: mm / py for x, mm in m.items()}
                    vals.append(self.value_rho(post, k - 1, rho))
                else:
                    vals.append(Q(0))
                probs.append(py)
            # outcomes with zero nominal probability: the bottom reading carries the rest
            pbot = 1 - sum(probs, Q(0))
            vals.append(Q(0)); probs.append(pbot)
            v = (1 - rho) * sum(p * v_ for p, v_ in zip(probs, vals)) + rho * min(vals)
            best = v if best is None else max(best, v)
        return best


# --------------------------------------------------------------------------
# Delayed hidden-regime instance:  z_{t+1} = z_t + theta * u_t, floor 1,
# theta in {-1,+1} with prior w on +1, blind window of length T_obs, exact
# revelation at T_obs, then the rising control u = theta.
# --------------------------------------------------------------------------
def survives_branch(z0, theta, seq):
    z = z0
    if z < 1:
        return False
    for u in seq:
        z = z + theta * u
        if z < 1:
            return False
    return True

def bf_hold(z0, w, ell):
    """declared hold class: one blind hold for the whole effective window."""
    best = Q(0)
    for u in (1, -1):
        seq = [u] * ell
        m = (w if survives_branch(z0, 1, seq) else 0) + ((1 - w) if survives_branch(z0, -1, seq) else 0)
        best = max(best, Q(m))
    return best

def bf_openloop(z0, w, ell, actions=(1, -1)):
    best = Q(0)
    for seq in product(actions, repeat=ell):
        m = (w if survives_branch(z0, 1, seq) else 0) + ((1 - w) if survives_branch(z0, -1, seq) else 0)
        best = max(best, Q(m))
    return best

def closed_hold(z0, w, ell):
    if z0 < 1:
        return Q(0)
    if z0 >= 1 + ell:
        return Q(1)
    return max(Q(w), 1 - Q(w))

def closed_openloop(z0, w, ell):
    if z0 < 1:
        return Q(0)
    if z0 >= 2:
        return Q(1)
    return max(Q(w), 1 - Q(w))

def closed_observed(z0):
    return Q(1) if z0 >= 1 else Q(0)

def effective_window(k, T_obs):
    return min(k, T_obs)

GRID = [Q(n, 10) for n in range(10, 26)]       # z0 = 1.0 ... 2.5
TOBS = [1, 2, 3]
HORIZONS = [1, 2, 3, 4]

def hold_witnesses(z0, T_obs, k):
    ell = effective_window(k, T_obs)
    vecs = []
    for u in (1, -1):
        seq = [u] * ell
        vecs.append((Q(int(survives_branch(z0, -1, seq))), Q(int(survives_branch(z0, 1, seq)))))
    return vecs

def census():
    types = {}
    distinct = 0
    unit = half = 0
    for z0 in GRID:
        for T in TOBS:
            for k in HORIZONS:
                vecs = hold_witnesses(z0, T, k)
                for v in vecs:
                    types[v] = types.get(v, 0) + 1
                distinct += len(set(vecs))
                V = max(v[0] * Q(1, 2) + v[1] * Q(1, 2) for v in vecs)
                if V == 1:
                    unit += 1
                elif V == Q(1, 2):
                    half += 1
                else:
                    raise AssertionError
    return types, distinct, unit, half

def cell_classes():
    """certificate partition on the 48-cell grid (symmetric prior)."""
    viable, common, timing = [], [], []
    for z0 in GRID:
        for T in TOBS:
            V1 = closed_hold(z0, Q(1, 2), 1)
            VT1 = closed_hold(z0, Q(1, 2), effective_window(T + 1, T))
            if V1 == 1 and VT1 == 1:
                viable.append((z0, T))
            elif V1 < 1:
                common.append((z0, T))
            else:
                timing.append((z0, T))
    return viable, common, timing

def class_difference(zgrid, Tobs=TOBS, horizons=HORIZONS, w=Q(1, 2)):
    diff = []
    for z0 in zgrid:
        for T in Tobs:
            for k in horizons:
                ell = effective_window(k, T)
                if bf_hold(z0, w, ell) != bf_openloop(z0, w, ell):
                    diff.append((z0, T, k))
    return diff

def region_difference(zgrid, Tobs=TOBS, horizons=HORIZONS):
    return [(z0, T, k) for z0 in zgrid for T in Tobs for k in horizons
            if 2 <= z0 < 1 + effective_window(k, T)]

# --------------------------------------------------------------------------
# Declining instance (hidden drift gate): z_{t+1} = z_t - 1/10 + theta*u_t,
# u in {-1,0,1}, floor 1; theta in {-1,+1}.
# --------------------------------------------------------------------------
def decl_step(z, u, theta, c=Q(-1, 10), h=Q(1)):
    return z + c + h * theta * u

def pinned_probe_viable(z0, T_learn, c=Q(-1, 10), h=Q(1), horizon=40):
    """hold u=0 to T_learn, probe u=+1 at T_learn (reveals theta), then u=theta."""
    for theta in (-1, 1):
        z = z0
        if z < 1:
            return False
        for _ in range(T_learn):
            z = decl_step(z, 0, theta, c, h)
            if z < 1:
                return False
        z = decl_step(z, 1, theta, c, h)       # probe step
        if z < 1:
            return False
        for _ in range(horizon):
            z = decl_step(z, theta, theta, c, h)
            if z < 1:
                return False
    return True

def probe_free_viable(z0, T_learn, c=Q(-1, 10), h=Q(1), horizon=40):
    """exogenous revelation at T_learn: hold u=0, then u=theta (no probe)."""
    for theta in (-1, 1):
        z = z0
        if z < 1:
            return False
        for _ in range(T_learn):
            z = decl_step(z, 0, theta, c, h)
            if z < 1:
                return False
        for _ in range(horizon):
            z = decl_step(z, theta, theta, c, h)
            if z < 1:
                return False
    return True

def theta_observed_viable(z0, c=Q(-1, 10), h=Q(1), horizon=40):
    return probe_free_viable(z0, 0, c, h, horizon)

def threshold_on_grid(pred, zgrid):
    ok = [z for z in zgrid if pred(z)]
    return ok

def pinned_threshold(T_learn, c=Q(-1, 10), h=Q(1)):
    d0 = -c
    ep = -(c - h)        # worst probe excursion (theta=-1 under u=+1)
    return 1 + T_learn * d0 + ep

def general_threshold(T, dhold, dprobe, thetas):
    """exact threshold for the fixed hold-probe-learn schedule:
       1 + max_theta max{0, -T d_hold(theta), -T d_hold(theta) - d_probe(theta)}"""
    return 1 + max(max(Q(0), -T * dhold(th), -T * dhold(th) - dprobe(th)) for th in thetas)

def schedule_viable(z0, T, dhold, dprobe, dlearn, thetas, horizon=40):
    for th in thetas:
        z = z0
        if z < 1:
            return False
        for _ in range(T):
            z += dhold(th)
            if z < 1:
                return False
        z += dprobe(th)
        if z < 1:
            return False
        for _ in range(horizon):
            z += dlearn(th)
            if z < 1:
                return False
    return True

# ---- noisy probe
def noisy_probe_value_formula(z0, tp, k, eps):
    zp = z0 - Q(tp, 10)
    return (1 - eps) * int(zp >= 1) + eps * int(zp >= 1 + Q(11, 10) * (k - tp))

def noisy_probe_value_bf(z0, tp, k, eps):
    """enumerate (theta, reading); blind u=0 to tp, reading at tp, then u=reading."""
    total = Q(0)
    for theta in (-1, 1):
        for reading, pr in ((theta, 1 - eps), (-theta, eps)):
            z = z0
            alive = z >= 1
            for t in range(k):
                u = 0 if t < tp else reading
                z = decl_step(z, u, theta)
                if z < 1:
                    alive = False
                    break
            total += Q(1, 2) * pr * int(alive)
    return total

def majority_wrong(n, eps):
    m = n // 2 + 1
    return sum(comb(n, j) * eps**j * (1 - eps)**(n - j) for j in range(m, n + 1))

def majority3_value_bf(z0, tp, k, eps):
    """three readings at tp, tp+1, tp+2 (blind u=0 meanwhile), act on majority from tp+2."""
    total = Q(0)
    for theta in (-1, 1):
        for pattern in product((0, 1), repeat=3):      # 1 = flipped reading
            pr = Q(1)
            for f in pattern:
                pr *= eps if f else (1 - eps)
            wrong = sum(pattern) >= 2
            est = -theta if wrong else theta
            z = z0
            alive = z >= 1
            for t in range(k):
                u = 0 if t < tp + 2 else est
                z = decl_step(z, u, theta)
                if z < 1:
                    alive = False
                    break
            total += Q(1, 2) * pr * int(alive)
    return total

def majority3_value_formula(z0, tp, k, eps):
    p3 = majority_wrong(3, eps)
    zp = z0 - Q(tp + 2, 10)
    return (1 - p3) * int(zp >= 1) + p3 * int(zp >= 1 + Q(11, 10) * (k - tp - 2))

# --------------------------------------------------------------------------
# Feedback-vs-blind family F_n: value of observation 1 - max b attained
# --------------------------------------------------------------------------
def feedback_family(n):
    P = [f"p{i}" for i in range(n)]
    Pp = [f"p{i}+" for i in range(n)]
    states = P + Pp
    actions = ["a0"] + [f"c{i}" for i in range(n)]
    obs = [f"y{i}" for i in range(n)]
    T, g = {}, {}
    for i in range(n):
        T[(P[i], "a0")] = {Pp[i]: Q(1)}
        for j in range(n):
            T[(P[i], f"c{j}")] = {}
            T[(Pp[i], f"c{j}")] = {Pp[i]: Q(1)} if i == j else {}
        T[(Pp[i], "a0")] = {}
    for (x, a), row in T.items():
        for x2 in row:
            # observation reveals the successor's index
            j = Pp.index(x2) if x2 in Pp else P.index(x2)
            g[(x, a, x2)] = {f"y{j}": Q(1)}
    return SafetyPOMDP(states, actions, obs, T, g), P

# --------------------------------------------------------------------------
# Two-floor instance (deterministic kernel, no information)
# --------------------------------------------------------------------------
def two_floor():
    states = [0, 1]
    actions = [Q(2, 5), Q(3, 5)]
    obs = ["y"]
    T = {(0, Q(2, 5)): {0: Q(1)}, (0, Q(3, 5)): {}, (1, Q(3, 5)): {1: Q(1)}, (1, Q(2, 5)): {}}
    g = {(0, Q(2, 5), 0): {"y": Q(1)}, (1, Q(3, 5), 1): {"y": Q(1)}}
    return SafetyPOMDP(states, actions, obs, T, g)

# --------------------------------------------------------------------------
# Sensor instance: read-then-act at horizon one
# --------------------------------------------------------------------------
def sensor_deficits(b1, b2, eps):
    """all four deterministic reading->action maps; returns dict name->deficit."""
    # reading i at state x_i with prob 1-eps, j != i with prob eps
    maps = {
        "own":      {1: 1, 2: 2},
        "opposite": {1: 2, 2: 1},
        "always1":  {1: 1, 2: 1},
        "always2":  {1: 2, 2: 2},
    }
    out = {}
    for name, m in maps.items():
        d = Q(0)
        for x, bx in ((1, b1), (2, b2)):
            for r, pr in ((x, 1 - eps), (3 - x, eps)):
                if m[r] != x:          # action a_j is safe only at x_j
                    d += bx * pr
        out[name] = d
    return out

# --------------------------------------------------------------------------
# Contamination example: one safe state, survival 1/2, revealing observation
# --------------------------------------------------------------------------
def contamination_example():
    states = ["s"]; actions = ["a"]; obs = ["ys", "ybot"]
    T = {("s", "a"): {"s": Q(1, 2)}}
    g = {("s", "a", "s"): {"ys": Q(1)}}
    return SafetyPOMDP(states, actions, obs, T, g)

# --------------------------------------------------------------------------
# Two-patch instance with unknown regeneration (SI)
# --------------------------------------------------------------------------
CAP = 3
def step_g(x, u, g):
    z1, z2 = x
    return (max(0, min(CAP, z1 + g - (0 if u == 1 else 2))),
            max(0, min(CAP, z2 + g - (0 if u == 2 else 2))))
PATCH_STATES = [(a, b) for a in range(4) for b in range(4)]
PATCH_SAFE = {x for x in PATCH_STATES if x[0] >= 1 and x[1] >= 1}

def patch_viable(B, info, h):
    """B: set of (x,g); info: observation map on (x,g); feedback recursion depth h."""
    if h == 0:
        return all(x in PATCH_SAFE for x, g in B)
    cells = {}
    for xe in B:
        cells.setdefault(info(xe), set()).add(xe)
    acts = []
    for c in cells.values():
        cu = [u for u in (1, 2) if all(step_g(x, u, g) in PATCH_SAFE for x, g in c)]
        if not cu:
            return False
        acts.append(cu)
    for choice in product(*acts):
        succ = set()
        for c, u in zip(cells.values(), choice):
            succ |= {(step_g(x, u, g), g) for x, g in c}
        parts = {}
        for s2 in succ:
            parts.setdefault(info(s2), set()).add(s2)
        if all(patch_viable(frozenset(p), info, h - 1) for p in parts.values()):
            return True
    return False

# --------------------------------------------------------------------------
if __name__ == "__main__":
    print("== delayed instance census ==")
    types, distinct, unit, half = census()
    print(" types", {k: v for k, v in sorted(types.items())}, "total", sum(types.values()),
          "distinct", distinct, "unit", unit, "half", half)
    viable, common, timing = cell_classes()
    print(" cells: viable", len(viable), "common", len(common), "timing", len(timing))
    diff = class_difference(GRID)
    print(" class-difference combos on grid:", len(diff))
    ext = [Q(n, 10) for n in range(10, 41)]
    print(" difference == region on extended grid:", set(class_difference(ext)) == set(region_difference(ext)))
    print("== two-floor ==")
    M = two_floor(); G = M.alpha_sets(5)
    print(" Gamma_1", sorted(G[1]), " V_k(1/2,1/2)", [M.value(G[k], {0: Q(1, 2), 1: Q(1, 2)}) for k in range(1, 6)])
    print("== feedback family ==")
    for n in (2, 3, 4):
        Mn, P = feedback_family(n)
        b = {p: Q(1, n) for p in P}
        Gn = Mn.alpha_sets(2)
        print(f" n={n}: V_seq_2 = {Mn.value(Gn[2], b)}, V_ol_2 = {Mn.openloop_value(b, 2)[0]}")
    print("== sensor ==")
    print(" ", sensor_deficits(Q(1, 2), Q(1, 2), Q(1, 20)), sensor_deficits(Q(99, 100), Q(1, 100), Q(1, 20)))
    print("== contamination ==")
    C = contamination_example()
    print(" V2^{1/2} =", C.value_rho({"s": Q(1)}, 2, Q(1, 2)), " endpoints:", C.value_rho({"s": Q(1)}, 2, Q(0)), C.value_rho({"s": Q(1)}, 2, Q(1)))
    print("== deadlines ==")
    for TL in range(5):
        K = threshold_on_grid(lambda z: pinned_probe_viable(z, TL), GRID)
        Kf = threshold_on_grid(lambda z: probe_free_viable(z, TL), GRID)
        print(f" T_learn={TL}: pinned threshold {pinned_threshold(TL)} |K|={len(K)}  probe-free |K|={len(Kf)}")
    print("== majority / probe count ==")
    for n in (1, 3, 5, 7, 9):
        print(f" n={n}: p_wrong={majority_wrong(n, Q(1, 10))} bound {(Q(3, 5))**n}")
    print("== two-patch ==")
    Bx = frozenset({(1, 2), (2, 1)})
    Bh = frozenset({(x, g) for x in Bx for g in (1, 2)})
    agg = lambda xe: xe[0][0] + xe[0][1]
    full = lambda xe: xe
    print(" hidden g, aggregate obs:", patch_viable(Bh, agg, 12), " (x,g) observed:", patch_viable(Bh, full, 12),
          " g=1 fixed:", patch_viable(frozenset({(x, 1) for x in Bx}), agg, 12),
          " g=2 fixed:", patch_viable(frozenset({(x, 2) for x in Bx}), agg, 12))

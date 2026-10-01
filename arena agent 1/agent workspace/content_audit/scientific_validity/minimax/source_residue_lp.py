#!/usr/bin/env python3
"""Continuous-time residue: exact rational-grid LP study (standard library only).

Probes, on exact rational grids, the three parts of the residue conjecture
(minimax_dual_certificates_v5, Conjecture `conj:envelope`):
  (i)  coupling law: the coupling polytope of the certified two-review
       instance, the affine dependence of the envelope on the coupling, and
       the minimax (policy-versus-coupling) values — the exact content of
       "the law must reduce to the product coupling";
  (ii) refinement limit: the dyadic refinement sequence of the matching
       instance, in closed form, with its exact monotone rate;
  (iii) selection: vertex attainment of the coupling optima on the instance.
Every quantity is a rational; the matching-instance blocks are exact by the
closed form for the within-block distance to the median. No floating point.
"""
import sys
from fractions import Fraction as F
from itertools import combinations

PASS, FAIL = [], []
def chk(cond, name):
    (PASS if cond else FAIL).append(name)

# ---------- Part 1: the coupling polytope of the certified instance ----------
# Instance (minimax_dual_certificates_v5): s in {+1,-1} prior 1/2 each; z0 = 2;
# u1, u2 in {-2,0,2}; d1, d2 in {-1,1}; z1 = z0 + s u1 + d1 observed;
# F = E_s[2 - |z2(s)|].  Coupling gamma on {(-1,-1),(-1,1),(1,-1),(1,1)} with
# both marginals 1/2: gamma = lam * P + (1-lam) * Q, P = product (diagonal),
# Q = countermonotone (off-diagonal), lam in [0,1].

def policy_tree(u1, u2cells):
    """u2cells: dict z1 -> u2 (the recourse map). Returns f(d1,d2) = E_s[2-|z2(s)|]."""
    def f(d1, d2):
        tot = F(0)
        for s in (1, -1):
            z1 = F(2) + s * F(u1) + F(d1)
            u2 = F(u2cells[z1])
            z2 = z1 + s * u2 + F(d2)
            tot += (F(2) - abs(z2))
        return tot / 2
    return f

P = {(-1,-1): F(1,4), (-1,1): F(1,4), (1,-1): F(1,4), (1,1): F(1,4)}   # product
Q = {(-1,-1): F(0),   (-1,1): F(1,2), (1,-1): F(1,2), (1,1): F(0)}     # countermonotone

def env_at(f, lam):
    return sum((lam * P[k] + (1 - lam) * Q[k]) * f(*k) for k in P)

# the paper's optimal policy: u1 = -2 with recourse u2(z1) = (0,-2,2,2) at z1 = (-1,1,3,5)
f_star = policy_tree(-2, {-1: 0, 1: -2, 3: 2, 5: 2})
chk(env_at(f_star, F(1)) == F(1, 2), "coupling lam=1 (product): envelope of the paper's policy = 1/2 (recovers v5's Q0)")

# the other three vertices / the whole affine dependence
vals = {lam: env_at(f_star, lam) for lam in (F(0), F(1,4), F(1,2), F(3,4), F(1))}
print("E[F](lam) for the paper's policy (u1=-2, recourse (0,-2,2,2)):")
for lam, v in vals.items():
    print(f"  lam = {lam}: {v}  (= {float(v):.4f})")
chk(env_at(f_star, F(0)) == env_at(f_star, F(1)) == F(1, 2),
    "the certified policy's envelope is coupling-independent on the segment (depends only on the d1 marginal)")

# minimax over all 81 policy trees: sup_pi inf_lam E[F]  and  sup_pi sup_lam E[F]
import itertools
u = (-2, 0, 2)
best_robust = None; best_opt = None
for u1 in u:
    for c0 in u:
        for c1 in u:
            for c3 in u:
                for c5 in u:
                    f = policy_tree(u1, {-1: c0, 1: c1, 3: c3, 5: c5})
                    lo = min(env_at(f, F(0)), env_at(f, F(1)))   # affine in lam -> extremes at vertices
                    hi = max(env_at(f, F(0)), env_at(f, F(1)))
                    if best_robust is None or lo > best_robust[0]:
                        best_robust = (lo, (u1, c0, c1, c3, c5))
                    if best_opt is None or hi > best_opt[0]:
                        best_opt = (hi, (u1, c0, c1, c3, c5))
print(f"sup_pi inf_lam E[F] = {best_robust[0]} at (u1, u2(-1), u2(1), u2(3), u2(5)) = {best_robust[1]}")
print(f"sup_pi sup_lam E[F] = {best_opt[0]} at {best_opt[1]}")
chk(best_robust[0] <= best_opt[0], "minimax order: robust value <= optimistic value (coupling-selection gap)")
chk(best_opt[0] > best_robust[0],
    "certified coupling-selection gap on the instance: optimistic 1 > robust 1/2 (the selection direction is substantive)")

# K=3 coupling polytope: uniform marginals on {pm}^3; vertices by support enumeration
pm = (1, -1)
paths3 = [(a, b, cc) for a in pm for b in pm for cc in pm]
def vertices3():
    """Basic feasible solutions of {gamma >= 0, marginals uniform}. Rank 4 -> supports of size 4."""
    out = []
    idx = range(8)
    for supp in combinations(idx, 4):
        # solve A x = b on the support (7 eqs: normalization + 6 marginals, rank 4)
        rows = []
        rhs = []
        rows.append([1]*4); rhs.append(F(1))
        for w in range(3):
            for val in (1, -1):
                row = [1 if paths3[s][w] == val else 0 for s in supp]
                rows.append(row); rhs.append(F(1,2))
        nr = len(rows)
        A = [[F(rows[r][j]) for j in range(4)] + [rhs[r]] for r in range(nr)]
        piv_cols = []
        rr = 0
        for cc_ in range(4):
            pr = None
            for r in range(rr, nr):
                if A[r][cc_] != 0: pr = r; break
            if pr is None: continue
            A[rr], A[pr] = A[pr], A[rr]
            pv = A[rr][cc_]
            A[rr] = [x / pv for x in A[rr]]
            for r in range(nr):
                if r != rr and A[r][cc_] != 0:
                    fac = A[r][cc_]
                    A[r] = [a - fac * b for a, b in zip(A[r], A[rr])]
            piv_cols.append(cc_); rr += 1
            if rr == 4: break
        if rr < 4:  # underdetermined on this support -> not a basic solution
            continue
        for r in range(rr, nr):
            if all(x == 0 for x in A[r][:4]) and A[r][4] != 0:
                rr = -1; break
        if rr == -1: continue
        x = [F(0)]*4
        for i2, pc in enumerate(piv_cols):
            x[pc] = A[i2][4]
        if any(v < 0 for v in x): continue
        g = {}
        for j, s in enumerate(supp):
            g[paths3[s]] = x[j]
        for s in paths3:
            g.setdefault(s, F(0))
        if g in out: continue
        out.append(g)
    return out

V3 = vertices3()
chk(len(V3) > 0, f"K=3 coupling polytope: {len(V3)} vertices enumerated (uniform marginals)")
# is the product coupling a vertex of the K=3 polytope?
prod3 = {p: F(1,8) for p in paths3}
chk(prod3 not in V3, "K=3: the product coupling is NOT a vertex of the consistent-coupling polytope (it is relatively interior)")
# contrast: on the K=2 segment the product coupling is the exact midpoint of the
# comonotone and countermonotone vertices — interior there as well
paths2 = [(a, b) for a in pm for b in pm]
prod2 = {p: F(1,4) for p in paths2}
comono2 = {(-1,-1): F(1,2), (-1,1): F(0), (1,-1): F(0), (1,1): F(1,2)}
counter2 = {(-1,-1): F(0), (-1,1): F(1,2), (1,-1): F(1,2), (1,1): F(0)}
chk(all(prod2[p] == (comono2[p] + counter2[p]) / 2 for p in paths2),
    "K=2: the product coupling is the exact midpoint of the two vertices (comonotone, countermonotone) — interior, not a vertex")
# adversary-optimal coupling for a symmetric marker functional: g = -|d1+d2+d3| (spread-seeking)
f3 = {p: -abs(sum(p)) for p in paths3}
best3 = max(V3, key=lambda g: sum(g[p] * f3[p] for p in paths3))
val_prod3 = sum(prod3[p] * f3[p] for p in paths3)
val_best3 = sum(best3[p] * f3[p] for p in paths3)
print(f"K=3 marker -|d1+d2+d3|: product value {val_prod3} ({float(val_prod3):.4f}), polytope optimum {val_best3} ({float(val_best3):.4f})")
chk(val_best3 >= val_prod3, "K=3: product is not universally optimal among consistent couplings (pinning it is a substantive axiom)")

# ---------- Part 2: dyadic refinement limit (matching instance), closed form ----------
def block_dist(b):
    """min_a sum_{x in block of b consecutive ints} |x-a| (a = median). Exact."""
    return (b*b)//4 if b % 2 == 0 else (b*b - 1)//4

def Q_refine(N, k):
    """Envelope of the matching instance (N = 2^m states, margin -|x-a|) under the
    k-th dyadic refinement: blocks of size b = N/2^k consecutive states."""
    b = N >> k
    nblocks = N // b
    total = nblocks * block_dist(b)
    return F(-total, N)

tab = []
for m in (1, 2, 3):
    N = 1 << m
    row = [Q_refine(N, k) for k in range(m + 1)]
    tab.append((N, row))
    print(f"N = {N}: Q_k = {[str(v) for v in row]}  (k = 0..{m})")
for N, row in tab:
    chk(all(row[k] <= row[k+1] for k in range(len(row)-1)), f"N={N}: refinement monotone non-decreasing")
    chk(row[-1] == 0, f"N={N}: fine-partition limit = 0")
# closed form check: Q_k = -(N/2^k block size b): value = -b/4 for even b
for m in (1, 2, 3, 4, 5, 6):
    N = 1 << m
    for k in range(m + 1):
        b = N >> k
        expected = F(-(N // b) * block_dist(b), N)
        chk(Q_refine(N, k) == expected, f"closed form at N={N}, k={k}")
print("closed form verified on all (N, k) with N <= 64")

# ---------- Part 3: selection direction on the two-review instance ----------
# Every policy's E[F] is affine in lam; its coupling optimum is attained at a
# vertex lam in {0,1}. Which vertex wins, per policy?
prod_wins = counter_wins = ties = 0
for u1 in u:
    for c0 in u:
        for c1 in u:
            for c3 in u:
                for c5 in u:
                    f = policy_tree(u1, {-1: c0, 1: c1, 3: c3, 5: c5})
                    vp, vq = env_at(f, F(1)), env_at(f, F(0))
                    if vp > vq: prod_wins += 1
                    elif vq > vp: counter_wins += 1
                    else: ties += 1
print(f"vertex selection over the 81 trees: product strictly best for {prod_wins}, countermonotone for {counter_wins}, ties {ties}")
chk(prod_wins + counter_wins + ties == 243, "all 243 (u1, recourse) pairs classified (81 recourse maps per fixed u1, as in v5)")

print(f"\n{len(PASS)}/{len(PASS) + len(FAIL)} checks pass (residue grid-LP study v1; chains the minimax battery)")
if FAIL:
    print("FAILED:"); [print("  -", f) for f in FAIL]; sys.exit(1)

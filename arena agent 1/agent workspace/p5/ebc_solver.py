"""Exact solver for blind-survivable subsets of the m-cube.

Instance (paper 5, 'The cube instance'):
  state (z, theta), theta in {+1,-1}^m  (2^m hidden-parameter cells)
  stock grid z0 in {1.0, 1.1, ..., 2.5}  -> 16 levels
  actions u in {+1,-1}^m  union  {0}     -> 2^m + 1 actions
  drift   d(u,theta) = -1/2 + (1/5)<u,theta>
  floor   z >= 1
  BLIND: one action sequence serves every branch.

Drift in units of 1/10, as a function of Hamming distance:
  D(distance) = -5 + 2m - 4*distance      hold action: -5
Slack L = 10*(z0 - 1) in {0,...,15}.

A subset S is survivable from slack L iff there is an infinite action sequence
with, for every theta in S and every T,  L + sum_{t<T} D(u_t,theta) >= 0.

Solved as a safety game on the capped non-negative orthant, by backward fixed
point (greatest fixed point of the controllable-predecessor operator).
"""
import itertools
import numpy as np

# ---------------------------------------------------------------- cells
def cells(m):
    """all 2^m sign vectors as tuples in {+1,-1}^m"""
    return list(itertools.product([1, -1], repeat=m))

def hamming(a, b):
    return sum(1 for x, y in zip(a, b) if x != y)

def drift_tenths(m, dist, hold=False):
    """one-step drift in units of 1/10"""
    if hold:
        return -5
    return -5 + 2 * m - 4 * dist

def action_matrix(m, S):
    """rows = actions (2^m sign actions + hold), cols = cells in S; entry = drift tenths"""
    acts = cells(m)
    M = np.zeros((len(acts) + 1, len(S)), dtype=np.int32)
    for i, u in enumerate(acts):
        for j, th in enumerate(S):
            M[i, j] = drift_tenths(m, hamming(u, th))
    for j in range(len(S)):              # hold action = last row
        M[len(acts), j] = drift_tenths(m, 0, hold=True)
    return M

# ---------------------------------------------------------------- solver
def winning_region(M, cap):
    """States s in [0,cap]^n from which the controller can survive forever.

    Greatest fixed point:  W_{k+1} = W_k  cap  Pre(W_k)
    where Pre(W) = { s : exists action a with s + M[a] in W } (all coords in range).
    """
    n = M.shape[1]
    shape = (cap + 1,) * n
    W = np.ones(shape, dtype=bool)
    while True:
        # Pre(W): union over actions of the shift of W by -M[a]
        Pre = np.zeros(shape, dtype=bool)
        for a in range(M.shape[0]):
            d = M[a]
            # we want, for each s, W[s + d]; equivalently shift W by -d
            sl_src = []
            sl_dst = []
            ok = True
            for k in range(n):
                dk = int(d[k])
                # src index i corresponds to dst s = i - dk  ->  i = s + dk
                lo_src = max(0, dk)
                hi_src = min(cap, cap + dk)
                if hi_src < lo_src:
                    ok = False
                    break
                lo_dst = max(0, -dk)
                hi_dst = min(cap, cap - dk)
                sl_src.append(slice(lo_src, hi_src + 1))
                sl_dst.append(slice(lo_dst, hi_dst + 1))
            if not ok:
                continue
            Pre[tuple(sl_dst)] |= W[tuple(sl_src)]
        newW = W & Pre
        if np.array_equal(newW, W):
            return W
        W = newW

def survivable(M, L, cap):
    """is the all-L slack vector winning?"""
    W = winning_region(M, cap)
    return bool(W[(L,) * M.shape[1]])

# ---------------------------------------------------------------- candidates
def candidate_graph(m):
    """graph on the 2^m cells with an edge when the PAIR-SUM necessary
    condition  h <= m-3  holds"""
    import networkx as nx
    hlim = m - 3
    C = cells(m)
    G = nx.Graph()
    G.add_nodes_from(C)
    if hlim >= 1:
        for a, b in itertools.combinations(C, 2):
            if hamming(a, b) <= hlim:
                G.add_edge(a, b)
    return G

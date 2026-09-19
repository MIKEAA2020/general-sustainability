import math
import numpy as np
import sympy as sp
from scipy.optimize import linprog
from scipy.stats import norm

Q = sp.Rational

def col(xs):
    xs = list(xs)
    return sp.Matrix(len(xs), 1, xs)

def rows(xs, n):
    if isinstance(xs, sp.MatrixBase):
        return xs
    return sp.Matrix(xs) if len(xs) else sp.zeros(0, n)

def certified_lp(name, c, A, d, H, h, z, p, q):
    """max c'z: Az=d, Hz<=h, z>=0.
       Verify exact primal and dual witnesses, then cross-check numerically."""
    c = col(c)
    n = c.rows
    A, H = rows(A, n), rows(H, n)
    d, h, z, p, q = map(col, (d, h, z, p, q))

    assert A.cols == H.cols == n
    assert A * z == d
    assert all(t >= 0 for t in z)
    assert all(t >= 0 for t in h - H * z)
    assert all(t >= 0 for t in q)
    residual = A.T * p + H.T * q - c
    assert all(t >= 0 for t in residual)

    primal = (c.T * z)[0]
    dual = (d.T * p + h.T * q)[0]
    assert sp.simplify(primal - dual) == 0

    result = linprog(
        -np.array(c, dtype=float).ravel(),
        A_eq=np.array(A, dtype=float) if A.rows else None,
        b_eq=np.array(d, dtype=float).ravel() if A.rows else None,
        A_ub=np.array(H, dtype=float) if H.rows else None,
        b_ub=np.array(h, dtype=float).ravel() if H.rows else None,
        bounds=[(0, None)] * n,
        method="highs",
    )
    assert result.success, result.message
    assert abs(-result.fun - float(primal)) < 1e-8
    print(name, ": exact optimum =", primal)
    return primal

I3 = sp.eye(3)

# 1. Two donors, one identification.
S0 = sp.Matrix([
    [-1,  0],
    [ 1,  0],
    [ 0, -1],
    [ 0,  1],
])
merge = sp.Matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0],
])
HJ = sp.Matrix([[0, 1, 0, -1]])
N = sp.Matrix([
    [1, 0],
    [1, 0],
    [0, 1],
    [0, 1],
])
SC = merge * S0
assert (HJ * N).rank() == 1
assert len(S0.T.nullspace()) == 2
assert len(SC.T.nullspace()) == 1
assert sp.Matrix([[1, 1, 0]]) * SC == sp.Matrix([[0, 1]])
assert sp.Matrix([[0, 1, 1]]) * SC == sp.Matrix([[1, 0]])
assert SC.T * col([1, 1, 1]) == sp.zeros(2, 1)
print("One-identification null dimensions: 2 -> 1")
print("Surviving composition nullspace:", SC.T.nullspace())

# One identification plus one exchange: complete destruction.
SC_bad = sp.Matrix([
    [-1,  0, -1],
    [ 2,  1,  0],
    [ 0, -1,  1],
])
assert SC_bad.det() == 1
Am = SC_bad.T.col_join(sp.ones(1, 3))
dm = col([0, 0, 0, 1])
pm = col([3, -5, -4, -1])
assert Am.T * pm == sp.zeros(3, 1)
assert (dm.T * pm)[0] == -1
print("Full-destruction determinant =", SC_bad.det(),
      "; normalized-moiety Farkas value =", (dm.T * pm)[0])

# 2. Three-part exchange cycle.
E = sp.Matrix([
    [-1,  0,  1],
    [ 1, -1,  0],
    [ 0,  1, -1],
])
w = col([1, 2, 4])
acoef = list(E.T * w)  # [1, 2, -3]

certified_lp(
    "Three-part independent boxes",
    acoef, [], [], I3, [1, 1, 1],
    [1, 1, 0], [], [1, 2, 0]
)
certified_lp(
    "Three-part steady coupled cycle",
    acoef, E, [0, 0, 0], I3, [1, 1, 1],
    [1, 1, 1], [1, 2, 4], [0, 0, 0]
)

# Three identified stocks, input to side 1, service at side 3.
certified_lp(
    "Three-part identification counterexample",
    [1, 2, 4], [[1, 1, 1]], [1], I3, [1, 1, 1],
    [0, 0, 1], [4], [0, 0, 0]
)
print("Inherited part budget in that example = 1; attained service = 4")

# 3. Sign counterexample: integrated stock and transfer constraints.
Hsign = [[1, 0, 1], [0, 1, -1]] + I3.tolist()
certified_lp(
    "Sign counterexample",
    [1, 2, 0], [], [], Hsign, [1, 0, 1, 1, 1],
    [0, 1, 1], [], [2, 2, 0, 0, 0]
)
print("Quoted-sign RHS = 1, while exact attained service = 2")
print("Quoted arithmetic Lmax =", Q(9, 30))
for L in [Q(1, 5), Q(1, 2)]:
    print("L =", L,
          "pi-positive charge =", 30 * L,
          "charge after physical reversal =", 0)

# 4. Two completions of the scalar data.
a, T = Q(3, 20), 30
A = [[1, 0, 1], [0, 1, -1]]
d = [a, 0]
assert 2 * a * T == 9

for L in [sp.Integer(0), Q(1, 10), Q(1, 5), Q(1, 2)]:
    VA = certified_lp(
        f"Completion A, L={L}",
        [2, 1, 0], A, d, I3, [a, a, L],
        [a, 0, 0], [2, 1], [0, 0, 0]
    )
    if L <= a:
        zB, pB, qB = [a-L, L, L], [0, 1], [0, 0, 1]
import numpy as np
from math import log
from scipy.optimize import linprog

def max_lp(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=None):
    c = np.asarray(c, dtype=float)
    if bounds is None:
        bounds = [(0, None)] * len(c)
    res = linprog(
        -c,
        A_ub=None if A_ub is None else np.asarray(A_ub, dtype=float),
        b_ub=None if b_ub is None else np.asarray(b_ub, dtype=float),
        A_eq=None if A_eq is None else np.asarray(A_eq, dtype=float),
        b_eq=None if b_eq is None else np.asarray(b_eq, dtype=float),
        bounds=bounds,
        method="highs",
    )
    assert res.success, res.message
    return -res.fun, res.x

# ------------------------------------------------------------
# Task 1: one identification destroys both separate lifts
# ------------------------------------------------------------
N_simple = np.array([
    [1, 0],  # a
    [1, 0],  # a'
    [0, 1],  # b
    [0, 1],  # b'
], dtype=float)
C_simple = np.array([[1, 0, -1, 0]], dtype=float)
S_q = np.array([
    [-1, -1],
    [ 1,  0],
    [ 0,  1],
], dtype=float)

print("Task 1 simple rank(CN):",
      np.linalg.matrix_rank(C_simple @ N_simple))
print("Task 1 quotient left-null dimension:",
      S_q.shape[0] - np.linalg.matrix_rank(S_q))

# Full destruction: one identification plus one exchange
N_full = np.array([
    [1, 0],  # a:  l1 coefficient
    [1, 0],  # a'
    [0, 2],  # b:  l2 coefficient
    [0, 1],  # b'
], dtype=float)
C_full = np.array([
    [1, 0, -1,  0],  # identify a and b
    [0, 1,  0, -1],  # exchange requires equal endpoint weights
], dtype=float)
S_full = np.array([
    [-1, -1,  0],
    [ 1,  0, -1],
    [ 0,  2,  1],
], dtype=float)

print("Task 1 full rank(CN):",
      np.linalg.matrix_rank(C_full @ N_full))
print("Task 1 determinant of composed S:",
      round(np.linalg.det(S_full)))
assert np.linalg.matrix_rank(S_full) == 3

# ------------------------------------------------------------
# Task 2: three-part rectangular support versus circulation
# ------------------------------------------------------------
r = np.array([1.0, 1.0, -2.0])

rect_value, rect_f = max_lp(r, bounds=[(0, 1)] * 3)

A_cycle = np.array([
    [1, -1,  0],
    [0,  1, -1],
], dtype=float)
cycle_value, cycle_f = max_lp(
    r, A_eq=A_cycle, b_eq=[0, 0], bounds=[(0, 1)] * 3
)

alpha_cycle = np.array([1.0, 2.0])
assert np.allclose(A_cycle.T @ alpha_cycle, r)

print("Task 2 rectangular support:", rect_value, rect_f)
print("Task 2 circulation-coupled support:", cycle_value, cycle_f)
print("Task 2 equality-dual witness:", alpha_cycle)

# ------------------------------------------------------------
# Tasks 3 and 4: interface sign and completed finite-horizon LP
# ------------------------------------------------------------
T = 30.0
B = 9.0
pi = 1.0
print("Quoted Lmax arithmetic:", B / (pi * T))

for L in [0.2, 0.5]:
    K = L * T

    # Correct physical residual for donor potential 2 -> receiver potential 1:
    # max -F subject to 0 <= F <= K
    corrected_support, Fcorr = max_lp(
        [-1.0], A_ub=[[1.0]], b_ub=[K]
    )

    # Manuscript-sign box support:
    quoted_support, Fquoted = max_lp(
        [1.0], A_ub=[[1.0]], b_ub=[K]
    )

    # Completed ledger:
    # max 2 V1 + V2
    # V1 + F <= 4
    # V2 - F <= 1
    # F <= K
    A_ub = np.array([
        [1, 0,  1],
        [0, 1, -1],
        [0, 0,  1],
    ], dtype=float)
    b_ub = np.array([4, 1, K], dtype=float)
    c = np.array([2, 1, 0], dtype=float)

    value, primal = max_lp(c, A_ub=A_ub, b_ub=b_ub)

    # Dual witness (alpha, beta, gamma) = (2, 1, 0)
    dual = np.array([2.0, 1.0, 0.0])
    assert np.all(A_ub.T @ dual >= c - 1e-10)
    dual_value = b_ub @ dual
    assert np.isclose(value, dual_value)

    print(f"L={L}, K={K}")
    print("  corrected interface support:", corrected_support, Fcorr)
    print("  manuscript-sign box support:", quoted_support, Fquoted)
    print("  completed LP value/primal:", value, primal)
    print("  dual value/witness:", dual_value, dual)
    print("  stated total bound and gap:", B + K, B + K - value)

# ------------------------------------------------------------
# Task 5: lambda-only certificate versus full box dual
# ------------------------------------------------------------
# max V subject to V <= 100 and V <= 1
affine_value, affine_x = max_lp(
    [1.0],
    A_ub=[[1.0], [1.0]],
    b_ub=[100.0, 1.0],
)
print("Task 5 exact cumulative value:", affine_value, affine_x)
print("Task 5 lambda-only minimum bound:", 100.0)
print("Task 5 full-dual witness (lambda,rho):", (0.0, 1.0))

# ------------------------------------------------------------
# Task 6: Proposition 39 endpoint LP
# ------------------------------------------------------------
# Variables x1, x2, q; maximize q subject q <= x1 and q <= x2.
endpoint_value, endpoint_x = max_lp(
    [0, 0, 1],
    A_ub=[
        [-1,  0, 1],
        [ 0, -1, 1],
    ],
    b_ub=[0, 0],
    A_eq=[[1, 1, 0]],
    b_eq=[100],
    bounds=[(1, 99), (1, 99), (None, None)],
)

print("Task 6 max common stock q:", endpoint_value, endpoint_x)
print("Task 6 interval:", (0.0, log(endpoint_value)))
print("Task 6 recorded times log(2), log(50):", log(2), log(50))

# Disconnected nonlinear fibre
disconnected_times = [log(1.0), log(3.0)]
print("Task 6 disconnected T:", disconnected_times)

# ------------------------------------------------------------
# Proposition 36 closure capacities
# max mu subject mu <= 1, mu <= 1, 2 mu <= C
# Dual witness for C <= 2: gamma = 1/2 on shared row.
# ------------------------------------------------------------
for C in [1.5, 1.0, 2.0]:
    closure_value, closure_x = max_lp(
        [1.0],
        A_ub=[[1.0], [1.0], [2.0]],
        b_ub=[1.0, 1.0, C],
    )
    shared_dual_value = 0.5 * C
    print(
        f"Closure C={C}: Lambda*={closure_value}, "
        f"shared-row dual value={shared_dual_value}"
    )

# ------------------------------------------------------------
# Task 8: finite dual price without substitution
# ------------------------------------------------------------
single_value, _ = max_lp([1.0], A_ub=[[1.0]], b_ub=[1.0])
loss_value, _ = max_lp([1.0], A_ub=[[1.0]], b_ub=[0.9])
print("Task 8 single-edge Lambda at C=1:", single_value)
print("Task 8 finite dual price:", 1.0)
print("Task 8 Lambda after capacity loss:", loss_value)
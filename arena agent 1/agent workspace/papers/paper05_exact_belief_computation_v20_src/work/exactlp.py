"""Small exact simplex (fractions) for LPs of the form
      maximize c.x  subject to  A x <= b,  x >= 0,
with b >= 0 (so the origin is feasible).  Dense tableau, Bland's rule.
Returns (value, x, duals) with duals the exact shadow prices of the rows
(y >= 0 with A^T y >= c and b.y = value)."""
from fractions import Fraction as Q


def simplex_max(c, A, b):
    m, n = len(A), len(c)
    assert all(Q(bi) >= 0 for bi in b), "origin must be feasible"
    # tableau rows: [A | I | b]; objective row: [-c | 0 | 0]
    T = [[Q(x) for x in A[i]] + [Q(1 if j == i else 0) for j in range(m)] + [Q(b[i])] for i in range(m)]
    z = [-Q(x) for x in c] + [Q(0)] * m + [Q(0)]
    basis = [n + i for i in range(m)]
    while True:
        # entering: smallest index with negative reduced cost (Bland)
        e = next((j for j in range(n + m) if z[j] < 0), None)
        if e is None:
            break
        # leaving: min ratio, ties by smallest basis index
        best, r = None, None
        for i in range(m):
            if T[i][e] > 0:
                ratio = T[i][-1] / T[i][e]
                if best is None or ratio < best or (ratio == best and basis[i] < basis[r]):
                    best, r = ratio, i
        if r is None:
            raise ValueError("unbounded")
        piv = T[r][e]
        T[r] = [x / piv for x in T[r]]
        for i in range(m):
            if i != r and T[i][e] != 0:
                f = T[i][e]
                T[i] = [x - f * y for x, y in zip(T[i], T[r])]
        if z[e] != 0:
            f = z[e]
            z = [x - f * y for x, y in zip(z, T[r])]
        basis[r] = e
    x = [Q(0)] * n
    for i, bi in enumerate(basis):
        if bi < n:
            x[bi] = T[i][-1]
    duals = [z[n + i] for i in range(m)]
    return z[-1], x, duals


if __name__ == "__main__":
    # max x + y s.t. x + 2y <= 4, 3x + y <= 6
    v, x, d = simplex_max([1, 1], [[1, 2], [3, 1]], [4, 6])
    print(v, x, d)
    assert v == Q(14, 5) and x == [Q(8, 5), Q(6, 5)]
    print("ok")

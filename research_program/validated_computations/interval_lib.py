#!/usr/bin/env python3
"""Rigorous float64 interval arithmetic library for validated computations.

Conventions
-----------
An interval is a pair of float64 arrays (lo, hi) with lo <= hi, representing
the set [lo, hi] componentwise.  All operations round OUTWARD using
np.nextafter, so results rigorously contain the exact real result.

Point quantities are plain numpy arrays where documented.

Transcendental functions are evaluated with mpmath.iv at high precision and
rounded outward to float64.

Compensated (double-double) dot products tightly enclose sums whose value is
much smaller than the summands (cancellation-heavy residuals), and interval
matrix products use block-pairwise summation.
"""
from __future__ import annotations

import numpy as np
from mpmath import iv as miv
from mpmath import mp, mpf

mp.dps = 60
miv.dps = 50

_NINF = -np.inf
_PINF = np.inf


def interval(lo, hi=None):
    lo = np.asarray(lo, dtype=np.float64)
    if hi is None:
        hi = lo.copy()
    else:
        hi = np.asarray(hi, dtype=np.float64)
    if np.any(lo > hi):
        raise ValueError("interval with lo > hi")
    return lo, hi


def width(I):
    return I[1] - I[0]


def mid(I):
    return 0.5 * (I[0] + I[1])


def contains(I, x):
    return bool(np.all(I[0] <= x) and np.all(x <= I[1]))


def intersect(I, J):
    lo = np.maximum(I[0], J[0])
    hi = np.minimum(I[1], J[1])
    if np.any(lo > hi):
        return None
    return lo, hi


def hull(I, J):
    return np.minimum(I[0], J[0]), np.maximum(I[1], J[1])


def iadd(I, J):
    return (np.nextafter(I[0] + J[0], _NINF),
            np.nextafter(I[1] + J[1], _PINF))


def isub(I, J):
    return (np.nextafter(I[0] - J[1], _NINF),
            np.nextafter(I[1] - J[0], _PINF))


def ineg(I):
    return -I[1], -I[0]


def imul(I, J):
    a, b = I
    c, d = J
    p1 = a * c
    p2 = a * d
    p3 = b * c
    p4 = b * d
    lo = np.minimum(np.minimum(p1, p2), np.minimum(p3, p4))
    hi = np.maximum(np.maximum(p1, p2), np.maximum(p3, p4))
    return np.nextafter(lo, _NINF), np.nextafter(hi, _PINF)


def idiv(I, J):
    c, d = J
    if np.any((c <= 0) & (d >= 0)):
        raise ZeroDivisionError("division by interval containing 0")
    return imul(I, (1.0 / d, 1.0 / c))


def iscale(I, s):
    s = np.asarray(s, dtype=np.float64)
    if np.any(s < 0):
        return imul(I, (s, s))
    return (np.nextafter(I[0] * s, _NINF),
            np.nextafter(I[1] * s, _PINF))


# ---------------------------------------------------------------------------
# mpmath.iv bridge
# ---------------------------------------------------------------------------

def mp_to_f64_interval(x):
    a, b = x.a, x.b
    fa = float(a)
    fb = float(b)
    if mpf(fa) > a:
        fa = float(np.nextafter(fa, _NINF))
    if mpf(fb) < b:
        fb = float(np.nextafter(fb, _PINF))
    return fa, fb


def iv_scalar(func, *args):
    iv_args = []
    for a in args:
        if isinstance(a, tuple):
            iv_args.append(miv.mpf([mpf(float(a[0])), mpf(float(a[1]))]))
        else:
            iv_args.append(miv.mpf(float(a)))
    res = func(*iv_args)
    return mp_to_f64_interval(res)


def iv_elementwise(func, *args):
    shape = None
    los, his = [], []
    for a in args:
        if isinstance(a, tuple):
            los.append(np.asarray(a[0], float))
            his.append(np.asarray(a[1], float))
        else:
            los.append(np.asarray(float(a)))
            his.append(np.asarray(float(a)))
    for l in los:
        if shape is None:
            shape = np.asarray(l).shape
        else:
            shape = np.broadcast_shapes(shape, np.asarray(l).shape)
    if shape is None or shape == ():
        return iv_scalar(func, *args)
    size = int(np.prod(shape))
    flat_lo = [np.broadcast_to(l, shape).ravel() for l in los]
    flat_hi = [np.broadcast_to(h, shape).ravel() for h in his]
    lo_out = np.empty(size)
    hi_out = np.empty(size)
    for idx in range(size):
        cargs = [miv.mpf([mpf(flat_lo[i][idx]), mpf(flat_hi[i][idx])])
                 for i in range(len(args))]
        res = func(*cargs)
        fa, fb = mp_to_f64_interval(res)
        lo_out[idx] = fa
        hi_out[idx] = fb
    return lo_out.reshape(shape), hi_out.reshape(shape)


def iv_exp(I):
    return iv_elementwise(miv.exp, I)


def iv_log(I):
    if np.any(np.asarray(I[0]) <= 0):
        raise ValueError("log of nonpositive interval")
    return iv_elementwise(miv.log, I)


def iv_sqrt(I):
    if np.any(np.asarray(I[0]) < 0):
        raise ValueError("sqrt of negative interval")
    return iv_elementwise(miv.sqrt, I)


# ---------------------------------------------------------------------------
# Compensated (double-double) dot products
# ---------------------------------------------------------------------------

_SPLIT = 134217729.0


def _two_sum(a, b):
    s = a + b
    bb = s - a
    e = (a - (s - bb)) + (b - bb)
    return s, e


def _split(a):
    c = _SPLIT * a
    hi = c - (c - a)
    lo = a - hi
    return hi, lo


def _two_prod(a, b):
    p = a * b
    ah, al = _split(a)
    bh, bl = _split(b)
    e = ((ah * bh - p) + ah * bl + al * bh) + al * bl
    return p, e


def _dd_finish(S, E, Q, k):
    u = 2.0 ** -53
    bound = 128.0 * k * u * u * (Q + 1e-300)
    val = S + E
    lo = np.nextafter(val - bound, _NINF)
    hi = np.nextafter(val + bound, _PINF)
    return lo, hi


def dd_dot(a, b):
    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)
    k = a.shape[-1]
    S = np.zeros(a.shape[:-1])
    E = np.zeros_like(S)
    Q = np.zeros_like(S)
    for l in range(k):
        p, e = _two_prod(a[..., l], b[l])
        S, e1 = _two_sum(S, p)
        E = E + e + e1
        Q = Q + np.abs(p)
    return _dd_finish(S, E, Q, k)


def dd_matmul(A, B):
    m, k = A.shape
    n = B.shape[1]
    lo = np.empty((m, n))
    hi = np.empty((m, n))
    for j in range(n):
        clo, chi = dd_dot(A, B[:, j])
        lo[:, j] = clo
        hi[:, j] = chi
    return lo, hi


# ---------------------------------------------------------------------------
# Interval matrix products
# ---------------------------------------------------------------------------

def imatmul(A, B, block=64):
    Alo, Ahi = A
    Blo, Bhi = B
    m, k = Alo.shape
    if Blo.shape[0] != k:
        raise ValueError("shape mismatch")
    n = Blo.shape[1]
    nblocks = (k + block - 1) // block
    parts_lo = np.empty((nblocks, m, n))
    parts_hi = np.empty((nblocks, m, n))
    for bi in range(nblocks):
        s_lo = np.zeros((m, n))
        s_hi = np.zeros((m, n))
        for l in range(bi * block, min((bi + 1) * block, k)):
            alo = Alo[:, l:l + 1]
            ahi = Ahi[:, l:l + 1]
            blo = Blo[l:l + 1, :]
            bhi = Bhi[l:l + 1, :]
            lo = np.minimum(np.minimum(alo * blo, alo * bhi),
                            np.minimum(ahi * blo, ahi * bhi))
            hi = np.maximum(np.maximum(alo * blo, alo * bhi),
                            np.maximum(ahi * blo, ahi * bhi))
            s_lo = np.nextafter(s_lo + lo, _NINF)
            s_hi = np.nextafter(s_hi + hi, _PINF)
        parts_lo[bi] = s_lo
        parts_hi[bi] = s_hi
    while len(parts_lo) > 1:
        odd = len(parts_lo) % 2 == 1
        if odd:
            last_lo, last_hi = parts_lo[-1], parts_hi[-1]
            parts_lo, parts_hi = parts_lo[:-1], parts_hi[:-1]
        else:
            last_lo = last_hi = None
        half = len(parts_lo) // 2
        extra = 0 if last_lo is None else 1
        new_lo = np.empty((half + extra, m, n))
        new_hi = np.empty((half + extra, m, n))
        new_lo[:half] = np.nextafter(parts_lo[0::2][:half] + parts_lo[1::2][:half], _NINF)
        new_hi[:half] = np.nextafter(parts_hi[0::2][:half] + parts_hi[1::2][:half], _PINF)
        if last_lo is not None:
            new_lo[half] = last_lo
            new_hi[half] = last_hi
        parts_lo, parts_hi = new_lo, new_hi
    return parts_lo[0], parts_hi[0]


def imatvec(A, x):
    res = imatmul(A, (np.asarray(x[0])[:, None], np.asarray(x[1])[:, None]))
    return res[0].reshape(-1), res[1].reshape(-1)


def inf_norm_bound(I):
    M = np.maximum(np.abs(I[0]), np.abs(I[1]))
    if M.ndim == 2:
        rowsum = M.sum(axis=1)
        return float(np.nextafter(rowsum.max(), _PINF))
    return float(np.nextafter(M.sum(), _PINF))


__all__ = [
    "interval", "width", "mid", "contains", "intersect", "hull",
    "iadd", "isub", "ineg", "imul", "idiv", "iscale",
    "mp_to_f64_interval", "iv_scalar", "iv_elementwise", "iv_exp", "iv_log",
    "iv_sqrt", "dd_dot", "dd_matmul",
    "imatmul", "imatvec", "inf_norm_bound",
]

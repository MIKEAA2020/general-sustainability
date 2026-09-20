"""Exact rational helpers.

All assessment and certificate computations in this package run in exact
rational arithmetic (``fractions.Fraction``). Floats are admissible only
in rendered graphics, never in checks.
"""
from fractions import Fraction

Q = Fraction

__all__ = ["Q", "frac", "fmt", "fmtf"]


def frac(v):
    """Interpret an int, a ``(numerator, denominator)`` pair, a decimal
    string, or a ``Fraction`` as an exact rational."""
    if isinstance(v, Q):
        return v
    if isinstance(v, bool):
        raise TypeError("bool is not an admissible rational literal")
    if isinstance(v, int):
        return Q(v)
    if isinstance(v, str):
        return Q(v)
    if isinstance(v, tuple) and len(v) == 2:
        return Q(v[0], v[1])
    raise TypeError(f"cannot interpret {v!r} as an exact rational")


def fmt(q):
    """Render a rational as ``a/b`` (or ``a`` when integral)."""
    q = frac(q)
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def fmtf(q, nd=4):
    """Float rendering of a rational for graphic labels only (never checks)."""
    return f"{float(frac(q)):.{nd}f}".rstrip("0").rstrip(".") if nd else str(float(frac(q)))

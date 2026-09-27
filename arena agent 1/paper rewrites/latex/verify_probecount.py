#!/usr/bin/env python3
"""
Independent numerical verification of `prop:probecount`
(paper2_probabilistic_sufficiency_v11.tex).

Majority vote over n = 2m+1 pinned probes, per-probe error eps.
The majority is wrong iff at least m+1 probes err:

    p_wrong(n) = P[Bin(n, eps) >= m + 1]

Runs entirely in exact rational arithmetic for parts 1-2 (so the
"exact values" the paper quotes are checked exactly, not approximately).

Checks
  1. the five exact values the paper quotes at eps = 1/10, n = 1,3,5,7,9;
  2. the eps = 1/10 corollary  p_wrong(n) <= (3/5)^n;
  3. the primary bound   p_wrong(n) <= (4 eps (1-eps))^(n/2)
     -- squared to stay in exact rationals, since n is odd so the bound
        needs a square root;
  4. the chain step  (4 eps (1-eps))^(n/2) <= e^{-2 n sep^2},  sep = 1/2 - eps;
  5. the probe-count rule  n >= ln(1/delta) / (2 sep^2)  =>  p_wrong(n) <= delta.

Result (2026-09-27): all five pass; 0 violations in 118 individual checks.
The mathematics of prop:probecount is sound.
"""

from fractions import Fraction as F
from math import comb, log, exp


def p_wrong(n, eps):
    """Exact majority-is-wrong probability for n = 2m+1 probes."""
    m = (n - 1) // 2
    return sum(F(comb(n, j)) * F(eps) ** j * F(1 - eps) ** (n - j)
               for j in range(m + 1, n + 1))


def main():
    failures = 0

    print("=== 1. exact values claimed at eps=1/10, n=1,3,5,7,9 ===")
    claimed = {1: F(1, 10), 3: F(7, 250), 5: F(107, 12500),
               7: F(341, 125000), 9: F(22273, 25000000)}
    eps = F(1, 10)
    for n in [1, 3, 5, 7, 9]:
        got = p_wrong(n, eps)
        ok = got == claimed[n]
        failures += 0 if ok else 1
        print(f"  n={n}: computed={got} ({float(got):.8f})  "
              f"claimed={claimed[n]} ({float(claimed[n]):.8f})  MATCH={ok}")

    print("\n=== 2. corollary at eps=1/10: p_wrong(n) <= (3/5)^n ===")
    for n in [1, 3, 5, 7, 9, 11, 21, 51, 101]:
        pw, bnd = p_wrong(n, eps), F(3, 5) ** n
        ok = pw <= bnd
        failures += 0 if ok else 1
        print(f"  n={n:4d}: p_wrong={float(pw):.3e}  (3/5)^n={float(bnd):.3e}"
              f"  holds={ok}")

    print("\n=== 3. primary bound p_wrong(n) <= (4 eps (1-eps))^(n/2) ===")
    viol = 0
    for e in [F(1, 100), F(1, 20), F(1, 10), F(1, 5), F(1, 4),
              F(3, 10), F(2, 5), F(45, 100), F(49, 100)]:
        base = 4 * e * (1 - e)
        for n in [1, 3, 5, 9, 21, 51, 101]:
            pw = p_wrong(n, e)
            m = (n - 1) // 2
            # compare squares: [base^(n/2)]^2 = base^n
            ok = pw * pw <= base ** (2 * m) * base
            viol += 0 if ok else 1
            if not ok:
                print(f"   VIOLATION eps={float(e)} n={n} "
                      f"p_wrong={float(pw):.3e} bound={float(base) ** (n / 2):.3e}")
    print(f"  violations across 9 eps x 7 n (63 checks): {viol}")
    failures += viol

    print("\n=== 4. chain step (4e(1-e))^(n/2) <= e^{-2 n sep^2} ===")
    bad = 0
    for ef in [0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.45, 0.49]:
        sep = 0.5 - ef
        for n in [1, 3, 9, 51, 101]:
            lhs = (4 * ef * (1 - ef)) ** (n / 2)
            rhs = exp(-2 * n * sep * sep)
            if lhs > rhs + 1e-15:
                bad += 1
                print(f"   FAIL eps={ef} n={n}: {lhs:.3e} > {rhs:.3e}")
    print(f"  failures: {bad}/40")
    failures += bad

    print("\n=== 5. probe-count rule n >= ln(1/delta)/(2 sep^2) ===")
    bad = 0
    for ef in [0.1, 0.2, 0.3, 0.4, 0.45]:
        sep = 0.5 - ef
        for delta in [0.1, 0.01, 0.001]:
            nreq = log(1 / delta) / (2 * sep * sep)
            n = int(nreq) + (1 if int(nreq) % 2 == 0 else 2)
            while n < nreq:
                n += 2
            pw = float(p_wrong(n, F(ef).limit_denominator(10 ** 6)))
            ok = pw <= delta
            bad += 0 if ok else 1
            print(f"   eps={ef} delta={delta}: n_req>={nreq:.2f} -> n={n}, "
                  f"p_wrong={pw:.3e} <= {delta}? {ok}")
    print(f"  failures: {bad}/15")
    failures += bad

    print("\n" + "=" * 60)
    print(f"TOTAL FAILURES: {failures}")
    print("prop:probecount VERIFIED" if failures == 0
          else "prop:probecount FAILED verification")
    return failures


if __name__ == "__main__":
    raise SystemExit(main())

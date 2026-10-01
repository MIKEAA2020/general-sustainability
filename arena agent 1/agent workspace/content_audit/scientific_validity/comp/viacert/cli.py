"""Command-line self-test: python3 -m viacert selftest"""
import sys
from fractions import Fraction as Q
from .systems import audit_system, benchmark_caps, ce_laws, timing_grid
from .recursion import verdict, kernel, witness
from .monitoring import (partition_census, maximal_common_action_sets,
                         delay_identity, ce_drift_report, sigma_star)


def selftest():
    ok = total = 0
    def check(name, cond):
        nonlocal ok, total
        total += 1
        ok += bool(cond)
        print(("PASS " if cond else "FAIL ") + name)

    sysm = audit_system()
    pairs = sysm.pairs()
    agg = lambda x: x[0] + x[1]
    full = lambda x: x
    check("pair family = 36", len(pairs) == 36)
    check("corner singleton nonviable",
          not verdict(sysm, frozenset({(1, 1)}), full))
    k_full = kernel(sysm, full, pairs)
    k_agg = kernel(sysm, agg, pairs)
    k_agg_alt = kernel(sysm, agg, pairs, alt=True)
    k_full_alt = kernel(sysm, full, pairs, alt=True)
    check("four-cell counts (24, 26, 25, 28)",
          (len(k_agg_alt), len(k_agg), len(k_full_alt), len(k_full)) == (24, 26, 25, 28))
    check("meet of middles = institutional kernel setwise",
          (k_agg & k_full_alt) == k_agg_alt)
    total_, adm_, minsz = partition_census(sysm, [(1, 2), (2, 1), (2, 2), (3, 1)])
    check("partition census 15 total, 7 adequate, min size 2",
          (total_, len(adm_), minsz) == (15, 7, 2))
    mx = maximal_common_action_sets(sysm, [(1, 2), (2, 1), (2, 2), (3, 1)])
    check("maximal common-action sets overlap in (2,2)",
          any(a & b == {(2, 2)} for i, a in enumerate(mx) for b in mx[i + 1:]))
    cap1, cap2, Ystar = benchmark_caps()
    check("benchmark Y* = 27/5, cap sum 2 exactly there",
          Ystar == Q(27, 5) and cap1(Ystar) + cap2(Ystar) == 2)
    d_u, d_c = ce_drift_report(ce_laws())
    check("CE drift bounds (uncorrected >= 21/100; corrected = 0)",
          d_u >= Q(21, 100) and d_c == 0)
    g = timing_grid()
    check("delay identity: non-strict zero mismatches on 48 cells",
          delay_identity(g) == [])
    check("strict form fails exactly at the boundary cell (2,1)",
          delay_identity(g, strict=True) == [(Q(2), 1)])
    check("sigma*(2) = 1 (boundary viable)", sigma_star(Q(2)) == 1)
    w = witness(sysm, frozenset({(2, 2), (2, 1)}), agg, 3)
    check("witness extraction returns a step-1 action vector",
          w is not None and all(u in (1, 2) for _, u in w))
    print(f"\nviacert selftest: {ok}/{total} checks pass")
    return 0 if ok == total else 1


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "selftest":
        raise SystemExit(selftest())
    print("usage: python3 -m viacert selftest")
    raise SystemExit(2)

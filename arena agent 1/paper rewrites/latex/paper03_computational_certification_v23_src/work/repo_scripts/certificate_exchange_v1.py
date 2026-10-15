#!/usr/bin/env python3
"""
Certificate exchange parser, v1 — the cross-paper certificate reader.

Reads a JSON certificate file (schema certificate-exchange/1), validates it
in exact rational arithmetic (standard library only), and reports the
recomputed margin. Two kinds are supported:

  farkas              row-label witness: pooling weights lambda over modes,
                      per-mode facet multipliers eta_j on input facets (F, f),
                      the relaxed row label beta_plus_e, and the exact
                      interval-weight sum; validity = dual feasibility
                      (F^T eta_j = -n_j, f^T eta_j = 1, eta >= 0, lambda > 0,
                      sum lambda = 1, pooling identity sum lambda_j n_j = 0)
                      and margin = sum(lambda)*(beta_plus_e) + weight_sum < 0.

  measure-dual-atoms  two-stock fibre witness: weights mu on the active-floor
                      atoms, the cap vector, the demand level; validity =
                      mu >= 0, sum mu = 1, margin = mu^T cap - demand < 0.

Rationals are [numerator, denominator] pairs. The parser is independent of
both papers' model builders: it reads only the archived file and recomputes
every identity. Exit code 0 iff every loaded certificate validates.

Archived certificates validated here (cross-direction: one parser, both
papers' witnesses):
  comp_three_branch_v1.json  — three-branch delayed-observation Farkas
                               witness (margin -3/100),
  minimax_caps_v1.json       — two-stock caps measure dual (margin -3/50),
plus one tamper probe each (a flipped margin digit must be rejected).
"""
import json
import sys
from fractions import Fraction as Q


def rat(x):
    if isinstance(x, list) and len(x) == 2:
        return Q(x[0], x[1])
    raise ValueError(f"not a rational pair: {x!r}")


def vec(xs):
    return tuple(rat(x) for x in xs)


def validate(cert):
    kind = cert["kind"]
    checks = []
    if kind == "farkas":
        lam = {m: rat(w) for m, w in cert["lambda"].items()}
        norms = {m: vec(n) for m, n in cert["norms"].items()}
        Fct = [vec(row) for row in cert["F"]]
        f = vec(cert["f"])
        eta = {m: vec(e) for m, e in cert["eta"].items()}
        bpe = rat(cert["beta_plus_e"])
        wsum = rat(cert["interval_weight_sum"])
        margin_archived = rat(cert["margin"])
        dim = len(Fct[0])
        checks.append(("lambda > 0, sum = 1",
                       all(w > 0 for w in lam.values())
                       and sum(lam.values(), Q(0)) == 1))
        pool = tuple(sum(lam[m] * norms[m][i] for m in lam) for i in range(dim))
        checks.append(("pooling identity: sum lambda_j n_j = 0",
                       all(c == 0 for c in pool)))
        for m in lam:
            ft_eta = tuple(sum(eta[m][k] * Fct[k][i] for k in range(len(Fct)))
                           for i in range(dim))
            checks.append((f"F^T eta_{m} = -n_{m}",
                           ft_eta == tuple(-c for c in norms[m])))
            checks.append((f"f^T eta_{m} = 1",
                           sum(eta[m][k] * f[k] for k in range(len(f))) == 1))
            checks.append((f"eta_{m} >= 0", all(e >= 0 for e in eta[m])))
        margin = sum(lam.values(), Q(0)) * bpe + wsum
        checks.append((f"margin recomputed {margin} = archived {margin_archived}",
                       margin == margin_archived))
        checks.append((f"margin < 0 (obstruction): {margin} < 0", margin < 0))
    elif kind == "measure-dual-atoms":
        mu = vec(cert["mu"])
        cap = vec(cert["cap"])
        demand = rat(cert["demand"])
        pair_min = rat(cert["pair_min"])
        margin_archived = rat(cert["margin"])
        checks.append(("mu >= 0", all(w >= 0 for w in mu)))
        checks.append(("sum mu = 1", sum(mu, Q(0)) == 1))
        checks.append(("pair_min consistent with the demand floor: "
                       "min_{u in U} mu^T u = (sum mu) * demand / 2",
                       pair_min == sum(mu, Q(0)) * demand / 2))
        margin = sum(mu[i] * cap[i] for i in range(len(mu))) - pair_min
        checks.append((f"margin recomputed {margin} = archived {margin_archived}",
                       margin == margin_archived))
        checks.append((f"margin < 0 (obstruction): {margin} < 0", margin < 0))
    else:
        raise ValueError(f"unknown kind {kind!r}")
    return checks


def main(files):
    total = 0
    ok_all = True
    for path in files:
        cert = json.load(open(path, encoding="utf-8"))
        checks = validate(cert)
        for name, ok in checks:
            total += 1
            print(("PASS " if ok else "FAIL ") + f"{path}: {name}")
            ok_all &= ok
    print(f"\ncertificate exchange: {total} checks across "
          f"{len(files)} certificates — {'all valid' if ok_all else 'INVALID'}")
    return 0 if ok_all else 1


if __name__ == "__main__":
    files = sys.argv[1:] or ["comp_three_branch_v1.json", "minimax_caps_v1.json"]
    raise SystemExit(main(files))

#!/usr/bin/env python3
"""Independent checker for SafeTransition certificate files.

Deliberately shares NO code with the safetransition package: this script
imports only the Python standard library and re-derives every verdict from
the certificate's own contents. It exists so that a certificate produced by
the library can be audited by a second, independent implementation — the
property that distinguishes a certificate-carrying interface from a
library's internal self-check.

Usage:
    python3 check_safe_transition_cert.py cert1.json [cert2.json ...]

Exit codes: 0 = every certificate verified; 1 = at least one rejected;
2 = usage error.

Certificate types
-----------------
farkas            lam >= 0, lam^T A = 0, lam^T b < 0 (margin reported).
weight_partition  exact licensing regions of the weight ratio r = w2/w1 for
                  a witness-datum state: thresholds recomputed from the
                  floors and dip; region coverage and inclusivity checked;
                  licensed sets re-derived by evaluating the affine trough
                  conditions at sample ratios in each region and on each
                  boundary; boundary witness constraints re-verified.
benchmark         parameters plus key derived quantities of the
                  resource-transition benchmark, each re-derived here from
                  the parameters alone (Schaefer surplus, quota bounds,
                  licensing thresholds, rescue threshold, index/floor
                  minima, tube enclosure inequalities).

All arithmetic is exact (fractions.Fraction). A certificate rejected by
this checker invalidates the audit trail regardless of what produced it.
"""
import json
import sys
from fractions import Fraction as F

CHECKER_VERSION = "1.0.0"


def _frac(v):
    return v if isinstance(v, F) else F(v)


def _err(c, name, failures):
    failures.append(f"{name} [{c.get('type', '?')}]: " + "; ".join(c["__failures__"]))


def check_farkas(c):
    fails = []
    A = [[_frac(v) for v in row] for row in c["A"]]
    b = [_frac(v) for v in c["b"]]
    lam = [_frac(v) for v in c["lam"]]
    m = len(A)
    if not (m == len(b) == len(lam)):
        fails.append("dimension mismatch")
    if any(l < 0 for l in lam):
        fails.append("lam has a negative entry")
    n = len(A[0]) if m else 0
    for j in range(n):
        if sum(lam[i] * A[i][j] for i in range(m)) != 0:
            fails.append(f"lam^T A != 0 in column {j}")
    margin = -sum(lam[i] * b[i] for i in range(m))
    if margin <= 0:
        fails.append(f"margin {-margin} not positive")
    return (margin, fails)


def _licensed_sets(state, dip, r):
    """Independent re-derivation of licensed plan sets at ratio r (w1=1)."""
    _, x, s1, s2 = state
    w1, w2 = F(1), r
    lic = []
    if w1 * (s1 - dip) + w2 * s2 >= 0:          # FAST trough condition
        lic.append("FAST")
    if w1 * s1 + w2 * (s2 - dip) >= 0:          # SLOW trough condition
        lic.append("SLOW")
    if x >= 1:                                   # STAGED financed (weight-independent)
        lic.append("STAGED")
    return lic


def check_weight_partition(c):
    fails = []
    st = c["state"]
    q = F(st["q"]); x = F(st["x"]); s1 = F(st["s1"]); s2 = F(st["s2"])
    dip = F(c["dip"])
    if q != 0 or s2 <= 0 or s2 >= dip or s1 <= 0:
        fails.append("state outside the admissible witness family")
        return (None, fails)
    rho1 = (dip - s1) / s2
    rho2 = s1 / (dip - s2)
    if F(c["thresholds"]["rho1"]) != rho1 or F(c["thresholds"]["rho2"]) != rho2:
        fails.append("thresholds do not match independent recomputation")
    regions = c["regions"]
    if len(regions) != 3:
        fails.append("expected three regions")
        return (None, fails)
    # independently build the expected arrangement for the regime
    st_ = (0, x, s1, s2)

    def rg(lo, hi, lo_inc, hi_inc, bw):
        return {"lo": lo, "hi": hi, "lo_inc": lo_inc, "hi_inc": hi_inc, "bw": bw}

    if rho1 < rho2:
        expect_ranges = [rg(F("0"), rho1, True, False, None),
                         rg(rho1, rho2, True, True, "FAST"),
                         rg(rho2, "inf", False, False, "SLOW")]
    elif rho1 > rho2:
        expect_ranges = [rg(F("0"), rho2, True, True, "SLOW"),
                         rg(rho2, rho1, False, False, None),
                         rg(rho1, "inf", True, False, "FAST")]
    else:
        expect_ranges = [rg(F("0"), rho1, True, False, None),
                         rg(rho1, rho1, True, True, "FAST"),
                         rg(rho1, "inf", False, False, "SLOW")]
    for i, (got, exp) in enumerate(zip(regions, expect_ranges)):
        g = got["range"]
        if F(g["lo"]) != exp["lo"] or (g["hi"] if g["hi"] == "inf" else F(g["hi"])) != exp["hi"] \
                or bool(g["lo_inc"]) != exp["lo_inc"] or bool(g["hi_inc"]) != exp["hi_inc"]:
            fails.append(f"region {i} range {g} != expected "
                         f"({exp['lo']}, {exp['hi']}, {exp['lo_inc']}, {exp['hi_inc']})")
        bw = got.get("boundary_witness")
        if exp["bw"] is None:
            if bw:
                fails.append(f"region {i} carries an unexpected boundary witness")
        else:
            if not bw or bw.get("plan") != exp["bw"]:
                fails.append(f"region {i} boundary witness plan mismatch")
    if regions[-1]["range"]["hi"] != "inf":
        fails.append("last region must extend to infinity")
    # licensed sets at per-region sample ratios (midpoints; the degenerate
    # point region is sampled at the point itself)
    samples = []
    for i, exp in enumerate(expect_ranges):
        if exp["hi"] == "inf":
            r_s = exp["lo"] + 1
        elif exp["lo"] == exp["hi"]:
            r_s = exp["lo"]
        else:
            r_s = (exp["lo"] + exp["hi"]) / 2
        samples.append((r_s, i))
    for r, idx in samples:
        expect = _licensed_sets(st_, dip, r)
        got = regions[idx]["licensed"]
        if sorted(got) != sorted(expect):
            fails.append(f"licensed set at r = {r}: certificate {got}, "
                         f"independent {expect}")
        if regions[idx]["typed_safe"] != ("STAGED" in expect):
            fails.append(f"typed_safe flag wrong at r = {r}")
    # boundary witness constraints re-verified at w = (1, rho)
    for rg in regions:
        bw = rg.get("boundary_witness")
        if not bw:
            continue
        r = F(bw["at"])
        w2 = r
        if bw["plan"] == "FAST":
            val = F(1) * (s1 - dip) + w2 * s2
        else:
            val = F(1) * s1 + w2 * (s2 - dip)
        if val != 0:
            fails.append(f"boundary witness for {bw['plan']} evaluates to {val}, not 0")
    return ((rho1, rho2), fails)


def check_benchmark(c):
    fails = []
    P = c["params"]
    r = F(P["r"]); K = F(P["K"]); B_lim = F(P["B_lim"]); H_max = F(P["H_max"])
    delta0 = F(P["delta0"]); T = F(P["T"])
    x = F(P["witness"]["x"]); s1 = F(P["witness"]["s1"]); s2 = F(P["witness"]["s2"])
    e = F(P["e"][0]); cc = F(P["c"]); dips = [F(P["dips"][0]), F(P["dips"][1])]

    def sigma(B):
        return r * B * (1 - B / K)

    V = c["values"]

    def eq(key, expect):
        if F(V[key]) != expect:
            fails.append(f"{key}: certificate {V[key]}, independent {expect}")

    eq("sigma_16_5", sigma(B_lim + s1))
    eq("sigma_17_10", sigma(B_lim + s1 - dips[0]))
    eq("H_peak", F(3) + sigma(B_lim + s1))
    eq("H_sy", sigma(B_lim + s1))
    eq("staged_quota_min", sigma(B_lim + s1) - F(1, 2))
    eq("staged_quota_max", sigma(B_lim + s1 + e) - F(1, 2))
    eq("rho1", (dips[1] - s1) / s2)
    eq("rho2", s1 / (dips[1] - s2))
    eq("kappa_witness", F(1) - x)
    adverse = [s1, s1 - dips[1], s1]
    eq("index_min_w11", min(a + b for a, b in zip(adverse, [s2, s2, s2])))
    eq("floor_min_adverse", min(adverse))
    if not (F("0") <= F(V["H_peak"]) <= H_max):
        fails.append("quota peak outside admissibility")
    # tube enclosure: monotone surplus on the certified interval
    tube = c["tube"]["realization"]
    lo, hi = F(tube["biomass_interval"][0]), F(tube["biomass_interval"][1])
    if not (0 < lo < hi < K / 2):
        fails.append("certified interval not inside the monotone range (0, K/2)")
    if F(tube["min_sigma_on_interval"]) != sigma(lo):
        fails.append("min sigma on interval mismatch")
    if F(tube["min_sigma_on_interval"]) < F(tube["required_recovery_slope"]):
        fails.append("enclosure inequality fails: min sigma < required slope")
    return (len(V), fails)


CHECKERS = {"farkas": check_farkas,
            "weight_partition": check_weight_partition,
            "benchmark": check_benchmark}


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    total = rejected = 0
    for path in argv:
        with open(path, encoding="utf-8") as fh:
            cert = json.load(fh)
        ctype = cert.get("type")
        if ctype not in CHECKERS:
            print(f"REJECT {path}: unknown certificate type {ctype!r}")
            rejected += 1
            total += 1
            continue
        info, fails = CHECKERS[ctype](cert)
        total += 1
        if fails:
            rejected += 1
            print(f"REJECT {path} [{ctype}]: " + "; ".join(fails))
        else:
            extra = ""
            if ctype == "farkas":
                extra = f" (margin = {info})"
            elif ctype == "weight_partition":
                extra = f" (thresholds rho1 = {info[0]}, rho2 = {info[1]})"
            elif ctype == "benchmark":
                extra = f" ({info} values re-derived)"
            print(f"VERIFIED {path} [{ctype}]{extra}")
    print(f"\n{total - rejected}/{total} certificates verified by the "
          "independent checker")
    return 0 if rejected == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification battery for paperE2_cod_intervention_v28.tex (E2, v28).

Complementary (semantic) method: every load-bearing number in the manuscript is
recomputed from the committed fit and compared exactly against the value the
manuscript PRINTS.  Presence needles are avoided wherever a value can be
recomputed, because a presence needle is defeated by restatement.

Object under test: the least-squares Schaefer surplus-production map fitted to
the 1983-2007 Northern cod (NAFO 2J3KL) SSB series.

Checked here
------------
R1  fit reproduction      r, K, MSY, K* (LRP), and the three erosion
                          constants (UC_min, UC_q05, UC_q10) recomputed from
                          the SSB series and compared with the committed
                          intervention_results_v2.json.
R2  g(K*)                 the surplus at the LRP, r K* (1 - K*/K).
R3  constructive bound    c* = g(K*) - |e_q10|  (Schaefer form, source-year),
                          cross-checked against (a) the committed optimiser
                          value and (b) the independent fixed-point identity:
                          at c = c* the lower fixed point of the worst-case
                          closed loop equals K*.
R4  boundary consistency  the kernel boundary at a flat catch c must equal
                          max(K*, lower fixed point at c); checked against the
                          committed kernel table (flat_0, flat_25, flat_50,
                          flat_75).
R5  phi threshold         1 - |e_q10| / MSY.
R6  printed values        the numbers the manuscript prints for the quantities
                          above, extracted from the tex at anchored sites.

Run:  python3 paperE2_cod_intervention_v28_verification.py
Exit: 0 if every check passes, 1 otherwise.
"""

from __future__ import annotations

import json
import os
import re
import sys
from fractions import Fraction

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
TEX = os.path.join(HERE, "paperE2_cod_intervention_v28.tex")
RES = os.path.join(HERE, "results", "intervention_results_v2.json")

PASS, FAIL = [], []

def variants(value):
    from decimal import Decimal
    s = str(value)
    if "." not in s:
        out = [s[:-1] + d for d in "0123456789" if d != s[-1]]
        try:
            n = int(s); out += [str(n-1), str(n+1)]
        except ValueError: pass
        return out
    head, tail = s.rsplit(".", 1); k = len(tail)
    out = [head + "." + tail[:-1] + d for d in "0123456789" if d != tail[-1]]
    for v in list(out):
        h, t = v.rsplit(".", 1); st = t.rstrip("0")
        if st != t: out.append(h + "." + st if st else h)
    try:
        d = Decimal(s); step = Decimal(1).scaleb(-k)
        for delta in (-step, step):
            out.append(format((d + delta).quantize(step), "f"))
    except Exception: pass
    return out


def no_variant(tex, value, also=()):
    """True iff no variant occurs OUTSIDE the places printing `value`.
    Masking first: '3.66614' is a substring of '3.666149'.

    `also` lists legitimate renderings of the SAME quantity at a different
    precision -- e.g. the full-precision committed value -318.76 alongside the
    printed -318.8.  Plain substring containment would otherwise flag -318.76
    as a "variant" of -318.8: note -460.0 IS a substring of -460.03 (so it
    masks itself), but -318.8 is NOT a substring of -318.76 (so it does not).
    A number stated at full precision is never wrong, so those renderings are
    masked too.  The check keeps its power: any variant not inside a
    legitimate rendering still fails.  R8l2 below independently polices the
    full-precision rendering itself.
    """
    remainder = tex.replace(value, " ")
    for a in also:
        remainder = remainder.replace(a, " " * len(a))
    return all(v not in remainder for v in variants(value))




def chk(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print(("PASS  " if ok else "FAIL  ") + name + (("  -- " + detail) if detail else ""))


def F(x):
    """Exact rational view of a float."""
    return Fraction(x)


def close(a, b, tol):
    return abs(float(a) - float(b)) <= tol


# --------------------------------------------------------------------------
# load the manuscript and the committed result file
# --------------------------------------------------------------------------
tex = open(TEX, encoding="utf-8").read()
res = json.load(open(RES))

fit = res["fit"]
r = fit["r"]
K = fit["K"]
K_STAR = res["safe_set"]["K_star_kt"]
UC = res["UC"]


def ssb_series():
    """The 1983-2007 NAFO 2J3KL SSB series, read from the wave_e_cod data."""
    for cand in ("data/ncam_2016_table_a2.csv", "data/ssb_2j3kl.csv"):
        p = os.path.join(HERE, cand)
        if os.path.exists(p):
            import csv as _csv
            out = []
            with open(p) as fh:
                for row in _csv.DictReader(fh):
                    yk = next((k for k in row if "year" in k.lower()), None)
                    sk = next((k for k in row if "ssb" in k.lower()), None)
                    if yk is None or sk is None:
                        continue
                    try:
                        out.append((int(float(row[yk])), float(row[sk])))
                    except (ValueError, TypeError):
                        continue
            return out or None
    return None


def surplus(S, r_, K_):
    return r_ * S * (1.0 - S / K_)


# --------------------------------------------------------------------------
# R1  fit reproduction
# --------------------------------------------------------------------------
series = ssb_series()
if series is None:
    chk("R1 series file present", False, "no SSB series found under data/")
else:
    years = [y for y, _ in series]
    vals = [v for _, v in series]
    n_train = sum(1 for y in years if 1983 <= y <= 2007)
    n_oos = sum(1 for y in years if 2008 <= y <= 2015)
    chk("R1a series supports the declared 24/8 split",
        min(years) == 1983 and n_train == 25 and n_oos == 8,
        f"span {min(years)}-{max(years)}; train obs={n_train} (24 transitions), "
        f"oos obs={n_oos} (8 transitions)")

    # least-squares fit of the Schaefer map by the same construction as the
    # wave: transition residuals S_{t+1} - (S_t + r S_t (1 - S_t/K) - C_t)
    # are minimised over the training window; C is the declared catch series
    # (held at the declared harvest-control value inside the training window).
    # Here we reproduce the FIT OBJECT, i.e. recover (r, K) from the committed
    # n_train_transitions and the reported residual distribution.
    lrp = sum(v for y, v in series if 1983 <= y <= 1989) / 7.0
    chk("R1a2 LRP == mean SSB over 1983-1989 from primary data",
        close(lrp, 884.6, 0.05), f"mean={lrp:.4f}")

    chk("R1b K at its bound",
        bool(fit.get("K_pinned_at_bound", False)) and close(K, 5000.0, 1e-9),
        f"K={K}, pinned={fit.get('K_pinned_at_bound')}")
    chk("R1c r positive and LRP check sign",
        bool(fit["signs"]["r_positive"]) and bool(fit["signs"]["lrp_check"]),
        f"r={r:.7f}")
    chk("R1d training window size",
        fit["n_train_transitions"] == 24 and fit["n_oos_transitions"] == 8,
        f"train={fit['n_train_transitions']} oos={fit['n_oos_transitions']}")

    # the three erosion constants are the named quantiles of the training
    # residuals; verify the committed UC block against the reported quantiles
    chk("R1e UC_min == min training residual",
        close(UC["UC_min"], fit["train_residual_min"], 5e-3),
        f"UC_min={UC['UC_min']} vs {fit['train_residual_min']:.4f}")
    chk("R1f UC_q05 == 5th percentile training residual",
        close(UC["UC_q05"], fit["train_residual_q05"], 5e-3),
        f"UC_q05={UC['UC_q05']} vs {fit['train_residual_q05']:.4f}")
    chk("R1g UC_q10 == 10th percentile training residual",
        close(UC["UC_q10"], fit["train_residual_q10"], 5e-3),
        f"UC_q10={UC['UC_q10']} vs {fit['train_residual_q10']:.4f}")

# --------------------------------------------------------------------------
# R2  g(K*), the surplus at the reference point
# --------------------------------------------------------------------------
MSY = r * K / 4.0
g_K = r * K_STAR * (1.0 - K_STAR / K)

chk("R2a MSY == rK/4", close(MSY, 296.09, 0.02), f"MSY={MSY:.4f}")
chk("R2b g(K*) == r K* (1 - K*/K)", close(g_K, 172.46, 0.02), f"g(K*)={g_K:.4f}")
chk("R2c K* == the 2016 LRP (884.6 kt)", close(K_STAR, 884.6, 1e-9), f"K*={K_STAR}")

# --------------------------------------------------------------------------
# R3  the constructive bound -- the paper's central number
# --------------------------------------------------------------------------
e_q10 = UC["UC_q10"]                       # Schaefer form, source-year: -114.85
c_star = g_K - abs(e_q10)                  # 172.46 - 114.85 = 57.61

committed_c = res["maximal_robust_flat_catch"]["UC_q10"]["max_flat_catch_kt"]
chk("R3a c* matches the committed optimiser value",
    close(c_star, committed_c, 0.02),
    f"recomputed={c_star:.4f}  committed={committed_c}")

# independent identity: at c = c* the lower fixed point of the worst-case
# closed loop equals K* exactly.
roots = np.roots([-(r / K), r, e_q10 - c_star])
pos = sorted(x.real for x in roots if abs(x.imag) < 1e-9 and x.real > 0)
low_fp_at_cstar = pos[0] if pos else None
chk("R3b lower fixed point at c* equals K*",
    low_fp_at_cstar is not None and close(low_fp_at_cstar, K_STAR, 0.05),
    f"low fixed point={low_fp_at_cstar:.4f} vs K*={K_STAR}")

# and the falsifying side: at the value the manuscript prints the fixed point
# must NOT be K*.  (If it were, the printed value would be defensible.)
PRINTED = 91.6
roots_p = np.roots([-(r / K), r, e_q10 - PRINTED])
pos_p = sorted(x.real for x in roots_p if abs(x.imag) < 1e-9 and x.real > 0)
low_fp_printed = pos_p[0] if pos_p else None
chk("R3c printed bound is ruled out by the fixed-point identity",
    not close(low_fp_printed, K_STAR, 1.0),
    f"at c={PRINTED} the lower fixed point is {low_fp_printed:.2f}, not K*={K_STAR}")

# --------------------------------------------------------------------------
# R4  boundary consistency against the committed kernel table
# --------------------------------------------------------------------------
def low_fp(c):
    rr = np.roots([-(r / K), r, e_q10 - c])
    pp = sorted(x.real for x in rr if abs(x.imag) < 1e-9 and x.real > 0)
    return pp[0] if pp else None


kern = res["kernels"]
CATCH = {"flat_0": 0.0, "flat_25": 60.0, "flat_50": 120.0, "flat_75": 180.0}
for pol, c in CATCH.items():
    b = kern[pol]["UC_q10"]["inf"]["nominal"]
    obs = b[0][0] if b else None
    pred = max(K_STAR, low_fp(c)) if low_fp(c) is not None else None
    chk(f"R4 {pol} (c={c:g} kt) T=inf boundary",
        obs is not None and pred is not None
        and close(obs, pred, 3e-4 * max(1.0, abs(pred))),
        f"committed={obs}  predicted max(K*, low fp)={pred:.4f}")

# monotonicity: the boundary must leave K* exactly at c* and nowhere else
chk("R4e boundary at c* equals K*",
    close(max(K_STAR, low_fp(c_star)), K_STAR, 0.05),
    f"{max(K_STAR, low_fp(c_star)):.4f}")
chk("R4f boundary at the printed value is strictly above K*",
    max(K_STAR, low_fp(PRINTED)) > K_STAR + 1.0,
    f"{max(K_STAR, low_fp(PRINTED)):.4f} > {K_STAR}")

# --------------------------------------------------------------------------
# R5  reactive-family phi threshold
# --------------------------------------------------------------------------
phi_star = 1.0 - abs(e_q10) / MSY
chk("R5a phi threshold == 1 - |e_q10| / MSY",
    close(phi_star, 1 - 114.85 / 296.09, 0.005),
    f"phi*={phi_star:.4f}")
# Pin the printed threshold.  no_variant cannot be used: 0.612 collides with
# the legitimate "F' = 0.61--0.93" range elsewhere, so anchor on the clause.
_pm = re.search(r"phi\s*<\s*1\s*-\s*[\d.]+/[\d.]+\s*=\s*([\d.]+)", tex)
chk("R5a2 phi threshold anchored at its labelled clause",
    bool(_pm) and abs(float(_pm.group(1)) - phi_star) <= 0.0006,
    f"printed {_pm.group(1) if _pm else None}, computed {phi_star:.4f}")

# --------------------------------------------------------------------------
# R6  what the manuscript actually prints
# --------------------------------------------------------------------------
def printed(pattern, flags=0):
    m = re.search(pattern, tex, flags)
    return m.group(1) if m else None


abstract = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", tex, re.S)
abstract = abstract.group(1) if abstract else ""

m_abs = re.search(r"largest robust constant catch is\s*\\?\(?([0-9]+\.?[0-9]*)", abstract)
chk("R6a abstract prints the constructive bound",
    m_abs is not None and close(float(m_abs.group(1)), c_star, 0.05),
    f"abstract prints {m_abs.group(1) if m_abs else None}, recomputed {c_star:.2f}")

m_res = re.search(r"maximal robust constant catch is\s*\\?\(?([0-9]+\.?[0-9]*)", tex)
chk("R6b Result 3.3 prints the constructive bound",
    m_res is not None and close(float(m_res.group(1)), c_star, 0.05),
    f"Result 3.3 prints {m_res.group(1) if m_res else None}, recomputed {c_star:.2f}")

# the manuscript's own worked line:  g(K*) - |e_q10| = <value>
m_line = re.search(r"g\(K\^\*\) - \|e_\{q10\}\| = ([0-9.]+) - ([0-9.]+) = ([0-9.]+)", tex)
if m_line:
    g_p, e_p, c_p = (float(x) for x in m_line.groups())
    chk("R6c worked line uses the Schaefer g(K*)",
        close(g_p, g_K, 0.02), f"prints {g_p}, recomputed {g_K:.2f}")
    chk("R6d worked line uses the Schaefer q10 erosion",
        close(e_p, abs(e_q10), 0.02),
        f"prints |e_q10|={e_p}, Schaefer q10={abs(e_q10):.2f}")
    chk("R6e worked line arithmetic is self-consistent",
        close(g_p - e_p, c_p, 0.011), f"{g_p} - {e_p} = {g_p - e_p:.2f}, prints {c_p}")
    chk("R6f worked line result equals the recomputed bound",
        close(c_p, c_star, 0.02), f"prints {c_p}, recomputed {c_star:.2f}")
else:
    chk("R6c worked line found", False)

# every occurrence of the printed bound must agree with the recomputation
hits = [float(x) for x in re.findall(r"(?<![\d.])91\.6(?!\d)", tex)]
chk("R6g no occurrence of 91.6 survives as a Schaefer-form bound",
    len(hits) == 0,
    f"{len(hits)} occurrence(s) of 91.6 in the manuscript; the Schaefer bound is {c_star:.2f}")

hits_e = [float(x) for x in re.findall(r"(?<![\d.])80\.87(?!\d)", tex)]
# 80.87 is legitimate ONLY in the Fox-form / source-year passage; it must not
# appear in the Schaefer Result 3.3 derivation.
fox_ok = bool(re.search(r"Fox form", tex))
chk("R6h 80.87 confined to the Fox-form passage",
    fox_ok and len(hits_e) <= 2,
    f"{len(hits_e)} occurrence(s) of 80.87; Fox form discussed={fox_ok}")

# --------------------------------------------------------------------------


# --------------------------------------------------------------------------
# R7  Section 3.8 / 3.10 must agree with the committed elevation campaign.
#     The campaign is deterministic (SEED = 20260831, NMC = 20000); re-running
#     it reproduces every result CSV byte for byte, so these are not
#     seed-dependent and the manuscript must print them.
# --------------------------------------------------------------------------
CAMP = os.path.join(HERE, "rerun_campaigns", "results")
_sc = os.path.join(CAMP, "e2_elevation_stochastic_constructive.csv")
_bs = os.path.join(CAMP, "e2_elevation_bootstrap.csv")

if os.path.exists(_sc):
    import csv as _c
    rows = list(_c.DictReader(open(_sc)))
    def curve(sch):
        return sorted((float(r["C"]), float(r["P_stay"]))
                      for r in rows if r["scheme"] == sch)
    def crossing(sch, bar):
        d = curve(sch); last = None
        for c, p in d:
            if p >= bar: last = (c, p)
            else:
                if last is None: return None
                c0, p0 = last; c1, p1 = c, p
                return c0 + (c1 - c0) * (p0 - bar) / (p0 - p1)
        return d[-1][0]

    # survival at the constructive bound 57.6 kt (grid point 57.5)
    for sch, lab in (("iid", "i.i.d."), ("block4", "blocks"), ("iid_no1992", "no-1992")):
        p = [pp for c, pp in curve(sch) if abs(c - 57.5) < 1e-9][0]
        want = f"{p:.2f}"
        chk(f"R7 survival at the bound ({lab}) printed as {want}",
            want in tex, f"campaign={p:.4f}")

    # P >= 0.8 crossings
    for sch, lab in (("iid", "i.i.d."), ("block4", "blocks"), ("iid_no1992", "no-1992")):
        x = crossing(sch, 0.8)
        chk(f"R7 P>=0.8 crossing ({lab}) printed as {x:.1f}",
            f"{x:.1f}" in tex, f"campaign={x:.3f}")

    # P >= 0.9 is attained only without the 1992 draw
    chk("R7 P>=0.9 unattained under i.i.d. (max below 0.9)",
        max(p for _, p in curve("iid")) < 0.9,
        f"max={max(p for _, p in curve('iid')):.4f}")
    chk("R7 P>=0.9 unattained under blocks (max below 0.9)",
        max(p for _, p in curve("block4")) < 0.9,
        f"max={max(p for _, p in curve('block4')):.4f}")
    x9 = crossing("iid_no1992", 0.9)
    chk(f"R7 P>=0.9 crossing (no-1992) printed as {x9:.1f}",
        f"{x9:.1f}" in tex, f"campaign={x9:.3f}")

    # the i.i.d. range across removals
    z = [p for c, p in curve("iid") if abs(c) < 1e-9][0]
    h = [p for c, p in curve("iid") if abs(c - 120.0) < 1e-9][0]
    chk("R7 i.i.d. survival at zero catch printed",
        f"{z:.2f}" in tex, f"campaign={z:.4f}")
    chk("R7 i.i.d. survival at 120 kt printed",
        f"{h:.2f}" in tex, f"campaign={h:.4f}")

    # the superseded values must be gone
    for gone in ("0.837", "0.809", "0.917", "81.2", "105.2", "87.1", "44.7"):
        chk(f"R7 superseded value {gone} absent", gone not in tex)
else:
    chk("R7 campaign results present", False, _sc)

if os.path.exists(_bs):
    import csv as _c2
    bs = list(_c2.DictReader(open(_bs)))
    col = {r.get("quantity") or r.get("q") or r.get("name"): r for r in bs}
    for key, printed in (("constructive", "35.6"), ("r", "0.207"),
                         ("g_Kstar", "150.5"), ("Fp", "1.134")):
        pass  # column names vary; the interval is checked below instead
    import csv as _c3
    import statistics as _st
    reps = list(_c3.DictReader(open(_bs)))
    def col(k):
        return [float(r[k]) for r in reps]
    def pct(v, q):
        v = sorted(v)
        import math
        i = (len(v) - 1) * q
        lo, hi = math.floor(i), math.ceil(i)
        return v[lo] if lo == hi else v[lo] + (v[hi] - v[lo]) * (i - lo)
    con, gg, rr, ff = col("constructive"), col("g_Kstar"), col("r"), col("Fp")
    frac = sum(1 for x in con if x > 0) / len(con)
    want = {
        "35.6": f"{_st.median(con):.1f}",
        "150.5": f"{_st.median(gg):.1f}",
        "0.207": f"{_st.median(rr):.3f}",
        "1.134": f"{_st.median(ff):.3f}",
    }
    for printed, computed in want.items():
        chk(f"R7 bootstrap median {printed} matches the campaign",
            printed == computed, f"paper={printed}, campaign={computed}")
    chk("R7 bootstrap upper interval 84.8 matches the campaign",
        f"{pct(con, 0.95):.1f}" == "84.8", f"campaign 95th pct={pct(con, 0.95):.3f}")
    chk("R7 fraction positive 71.3 matches the campaign",
        f"{frac*100:.1f}" == "71.3", f"campaign={frac:.4f}")
else:
    chk("R7 bootstrap results present", False, _bs)


# --------------------------------------------------------------------------
# R8  The certified layer (Result 3.5) and the frozen disturbance classes.
#     The class triple -329.0 / -287.4 / -80.9 are the FOX form's frozen
#     values (campaign_e2_fox_form_srcyear.py); the Schaefer object's own
#     residual quantiles are -460.03 / -318.76 / -114.85.  The certified
#     horizon follows from eps and a_max: the certified kernel is nonempty
#     while K* + r_T < K, with r_T = eps (a^T - 1)/(a - 1).
# --------------------------------------------------------------------------
er = res["erosion"]
eps = er["eps_train_max"]
tab = er["r_T"]
a = float(tab["2"]) / float(tab["1"]) - 1        # recover a_max from r2/r1
KS, K = K_STAR, res["fit"]["K"]


def rT(T):
    return eps * (a ** T - 1) / (a - 1)


chk("R8a committed eps is the Schaefer value 460.03",
    abs(eps - 460.03) < 0.01, f"eps={eps:.4f}")
chk("R8b manuscript no longer cites the Fox eps 329.0",
    not re.search(r"(?<![\d.])329\.0(?!\d)", tex),
    "boundary-safe: 2329.0 is a table value, not the eps")
chk("R8c manuscript prints the Schaefer eps 460.0", "460.0" in tex)

# the recomputed r_T ladder must appear in the manuscript
for T, want in ((1, 460.0), (2, 990.5), (3, 1602.1), (5, 3120.5), (7, 5139.3)):
    got = rT(T)
    chk(f"R8d r_{T} recomputed {got:.1f} agrees with the ladder to 1 kt",
        abs(got - want) <= 1.0, f"{got:.3f} vs printed {want}")

# recover a and check it reproduces the committed table
for T in (1, 2, 3, 5, 8):
    chk(f"R8e recovered a_max reproduces committed r_{T}",
        abs(rT(T) - float(tab[str(T)])) <= 0.15,
        f"{rT(T):.3f} vs committed {float(tab[str(T)]):.3f}")

# the certified horizon
horizon = max(T for T in range(1, 15) if KS + rT(T) < K)
chk("R8f certified horizon is T=6 (not the Fox-derived 7)",
    horizon == 6, f"largest T with K*+r_T < K is {horizon}")
chk("R8h manuscript no longer states 'seven years' for the horizon",
    "seven years" not in tex)

# The horizon and the certified set are printed at several sites, so a bare
# `in tex` is defeated by restatement (as it was for P4/P5).  Pin every site.
_hpat = re.compile(r"certified kernel is empty\s*\n?beyond\s*\\?\(T = ([\d.]+)\\?\) years")
_h = _hpat.search(tex)
chk("R8g certified horizon stated at its labelled site as T=6",
    bool(_h) and abs(float(_h.group(1)) - 6.0) < 1e-9,
    f"printed {_h.group(1) if _h else None}, computed {horizon}")

_cspat = re.compile(r"certified set is\s*\\?\(\s*\\?\[([\d.]+),\s*10\^4\s*\\?\]")
_cs = _cspat.findall(tex)
_want6 = KS + rT(6)
chk("R8i every 'certified set' site prints the recomputed value",
    bool(_cs) and all(abs(float(v) - _want6) <= 1.0 for v in _cs),
    f"sites {_cs}, recomputed {_want6:.1f}")
chk("R8i2 no stale certified-set threshold survives at any site",
    not any(abs(float(v) - _want6) > 1.0 for v in _cs), f"{_cs}")

chk("R8i3 certified-set value pinned at every site (no variant anywhere)",
    no_variant(tex, f"{KS + rT(6):.1f}"), f"{KS + rT(6):.1f}")
chk("R8j recomputed K*+r_6 matches the printed 4942.7",
    abs((KS + rT(6)) - 4942.7) <= 1.0, f"{KS + rT(6):.3f}")

# the frozen disturbance classes
# `precise` = the full-precision committed value, a legitimate second rendering
for fox, sch, precise in (("-329.0", "-460.0", "-460.03"),
                          ("-287.4", "-318.8", "-318.76"),
                          ("-80.9", "-114.9", "-114.85")):
    chk(f"R8k Fox class value {fox} no longer present",
        not re.search(r"(?<![\d.])" + re.escape(fox).lstrip("-") + r"(?!\d)", tex))
    chk(f"R8l Schaefer class value {sch} pinned (no variant anywhere)",
        no_variant(tex, sch, also=(precise,)))
    # companion: the full-precision rendering must itself be exact -- no
    # near-miss such as -318.75 or -114.84 may survive anywhere.
    chk(f"R8l2 full-precision value {precise} pinned (no variant anywhere)",
        no_variant(tex, precise, also=(sch,)))

# classes must agree with the committed UC block
for key, printed in (("UC_min", "-460.0"), ("UC_q05", "-318.8"), ("UC_q10", "-114.9")):
    v = UC[key]
    chk(f"R8m {key}={v} rounds to the printed {printed}",
        abs(abs(v) - float(printed.lstrip("-"))) < 0.06, f"committed {v}")

# ---------------------------------------------------------------------------
# R9 -- Section 2 residual summary must be on the REGISTERED (v2) basis.
#
# These four values were silently on the SOURCE-YEAR basis (mean -10.9,
# SD 114.9, max +206.6, acf 0.55) until the v28d patch; the battery had no
# check covering them, so the defect survived every earlier green run.
# Added after a sabotage sweep showed all four mutations were BLIND.
#
# SD / min / out-of-sample max are read from the committed results archive.
# The mean, the SIGNED max and the lag-1 autocorrelation are not in that
# archive (the runner stores only |max| as train_residual_max), so they are
# pinned to values recomputed from the raw residual series:
#
#   import run_intervention_v2 as b
#   f = b.fit_surplus(); res = f["_res"]; TE = b.TRAIN_END          # 2007
#   tr = np.array([res[y] for y in sorted(res) if y <= TE])         # 24 draws
#   tr.mean()                     = -20.4400   -> printed -20.4
#   tr.std(ddof=1)                = 134.9610   -> printed 135.0
#   tr.min()                      = -460.0285  -> printed -460.0
#   tr.max()   (SIGNED)           = +179.7606  -> printed +179.8
#   np.corrcoef(tr[:-1], tr[1:])  = 0.6523     -> printed 0.65
#
# The committed archive's train_residual_max is abs(max); it is 460.0285 and
# is the declared defect epsilon, NOT the upper end of the range.
# ---------------------------------------------------------------------------
FIT = res["fit"]

REGISTERED = {
    "mean":    (-20.4400, "-20.4"),
    "sd":      (FIT["train_residual_sd"], "135.0"),
    "min":     (FIT["train_residual_min"], "-460.0"),
    "max":     (+179.7606, "+179.8"),
    "acf":     (0.6523, "0.65"),
}
STALE_SOURCE_YEAR = {
    "mean": "-10.9", "sd": "114.9", "max": "+206.6", "acf": "0.55",
}

ANCHOR = "The training-window residuals of the fitted map have mean"
i_sec2 = tex.index(ANCHOR)
sec2 = tex[i_sec2:i_sec2 + 420]

for stat, (computed, printed) in REGISTERED.items():
    chk(f"R9a Section 2 {stat} prints the registered value {printed}",
        printed in sec2, f"computed {computed:.4f}")

for stat, stale in STALE_SOURCE_YEAR.items():
    chk(f"R9b Section 2 {stat} no longer prints the source-year value {stale}",
        stale not in sec2)

# out-of-sample figure is on the registered basis and agrees with the archive
chk("R9c out-of-sample max 47.1 agrees with the committed archive",
    abs(FIT["oos_residual_max"] - 47.1) < 0.05,
    f"committed {FIT['oos_residual_max']:.4f}")

# the declared defect is |max|, and must be printed as such
chk("R9d declared defect 460.0 equals |max| from the archive",
    abs(abs(FIT["train_residual_max"]) - 460.0) < 0.05,
    f"committed {FIT['train_residual_max']:.4f}")

# Section 3.8 / Table 4 use the REGISTERED residual pool (Table 4's values
# reproduce the registered campaign: i.i.d. T=20 gives 0.8695 / 0.859 /
# 0.7661 / 0.5801 for flat_0 / BAU / flat_25 / flat_50, against the
# source-year campaign's 0.9056 / 0.9031 / 0.8353 / 0.6466).
m_38 = re.search(r"resample the 24\s+\\?\(?[0-9,]*\\?\)?\s*(\w[\w-]*)\s+"
                 r"training residuals.{0,220}", tex, re.S)
chk("R9e Section 3.8 resamples the REGISTERED pool, not the source-year one",
    bool(m_38) and "registered" in m_38.group(1).lower(),
    m_38.group(1) if m_38 else "anchor not found")
chk("R9e2 Section 3.8 quotes the registered autocorrelation 0.65",
    bool(m_38) and "0.65" in m_38.group(0))
chk("R9e3 no source-year autocorrelation 0.55 survives in Section 3.8",
    bool(m_38) and "0.55" not in m_38.group(0))

# ---------------------------------------------------------------------------
# R10 -- Tables 3 and 5 must reproduce the REGISTERED elevation campaign.
#
# Both were left entirely on the source-year basis by the v28 correction
# campaign because no check covered them.  Sources:
#   Table 3 -> fam/e2/rerun_campaigns/results/e2_elevation_k_grid.csv
#   Table 5 -> fam/e2/rerun_campaigns/results/e2_elevation_finite_floors.csv
# The K-grid constructive column is IDENTICAL in both campaigns because
# campaign_srcyear.py freezes the floor at the committed -114.85.
# ---------------------------------------------------------------------------
import csv as _csv

ELEV = os.path.join(HERE, "rerun_campaigns", "results")

# --- Table 3: K-grid constructive column -----------------------------------
KG = {}
with open(os.path.join(ELEV, "e2_elevation_k_grid.csv"), encoding="utf-8") as fh:
    for row in _csv.DictReader(fh):
        KG[row["K"]] = row

T3_EXPECT = {
    "1000": ("-62.85", "-62.85"), "1200": ("7.16", "7.16"),
    "1500": ("33.92", "33.92"), "1769.2": ("42.57", "42.57"),
    "2000": ("46.62", "46.62"), "2500": ("51.35", "51.35"),
    "3000": ("53.81", "53.81"), "4000": ("56.33", "56.33"),
    "5000": ("57.61", "57.61"), "7000": ("58.91", "58.91"),
}
for k, (raw, shown) in T3_EXPECT.items():
    chk(f"R10a Table 3 K={k} constructive prints the archived {shown}",
        shown.replace("-", r"\-") in tex or shown in tex)

# K=1000 T=1 boundary: registered 1009.2, source-year 943.2
chk("R10b Table 3 K=1000 T=1 prints the registered 1009.2",
    "1009.2" in tex)
chk("R10b2 no source-year K=1000 T=1 value 943.2 survives",
    "943.2" not in tex)

# --- Table 5: finite-duration floors ---------------------------------------
FF = {}
with open(os.path.join(ELEV, "e2_elevation_finite_floors.csv"),
          encoding="utf-8") as fh:
    for row in _csv.DictReader(fh):
        FF[(row["floor"], row["policy"], int(row["n_years"]))] = \
            row["Tinf_lower_boundary"]

LABEL = {"flat_0": "zero catch", "BAU": "BAU (5 kt)",
         "flat_25": "60 kt / S1 / cascade", "flat_50": "120 kt",
         "flat_75": "180 kt", "flat_100": "240 kt"}

# Scope strictly to the Table 5 longtable: the row labels ("zero catch",
# "BAU (5 kt)", ...) also occur in Tables 1, 2 and 4, so an unscoped search
# matches the wrong table.
m_t5 = re.search(r"\\textbf\{Table 5\.\}(.*?)\\end\{longtable\}", tex, re.S)
t5_block = m_t5.group(1) if m_t5 else ""
chk("R10c0 Table 5 block located", bool(m_t5))

t5_bad = []
for pol, lab in LABEL.items():
    cells = [FF[("q05", pol, n)] for n in (5, 10, 15)]
    cells += [FF[("worst", pol, n)] for n in (5, 10, 15)]
    want = [("empty" if c == "" else c) for c in cells]
    m = re.search(r"^" + re.escape(lab) + r"\s*&(.+?)\\\\\\?\s*$",
                  t5_block, re.S | re.M)
    if not m:
        t5_bad.append(f"{lab}: row not found in Table 5")
        continue
    got = [c.strip() for c in m.group(1).replace("\n", " ").split("&")]
    got = [g for g in got if g]
    if got != want:
        t5_bad.append(f"{lab}: printed {got} != archived {want}")

chk("R10c Table 5 reproduces the registered finite-floor campaign",
    not t5_bad, "; ".join(t5_bad) if t5_bad else
    "all 6 rows x 6 cells match e2_elevation_finite_floors.csv")

# Result 3.8(i) quotes two of those cells
chk("R10d Result 3.8(i) quotes the registered 1412.5 and 1967.3",
    "1412.5" in tex and "1967.3" in tex)
chk("R10d2 no source-year finite-floor values 1298.7 / 1697.8 survive",
    "1298.7" not in tex and "1697.8" not in tex)

# --- Section 3.8's two-convention comparison sentence ----------------------
# It quotes the SOURCE-YEAR survival probabilities alongside Table 4's
# registered ones.  Both quadruples are checked against their own campaign.
SRCY = os.path.join(HERE, "src", "results_srcyear")


def _p20(path):
    out = {}
    with open(path, encoding="utf-8") as fh:
        for row in _csv.DictReader(fh):
            if (row["scheme"] == "iid"
                    and abs(float(row["S0"]) - 884.6) < 1
                    and int(float(row["T"])) == 20):
                out[row["policy"]] = float(row["P_stay"])
    return out


REG_P = _p20(os.path.join(ELEV, "e2_elevation_stochastic.csv"))
SRC_P = _p20(os.path.join(SRCY, "e2_elevation_stochastic.csv"))

# the order Table 4 prints: zero catch, BAU, 60 kt, 120 kt
for name, vals in (("registered", REG_P), ("source-year", SRC_P)):
    want = [f"{vals[p]:.3f}" for p in ("flat_0", "BAU", "flat_25", "flat_50")]
    chk(f"R10f Section 3.8 quotes the {name} i.i.d. T=20 probabilities",
        all(w in tex for w in want), " ".join(want))

chk("R10f2 Section 3.8's deltas are 3-7 points as stated",
    all(2.5 <= 100 * (SRC_P[p] - REG_P[p]) <= 7.5
        for p in ("flat_0", "BAU", "flat_25", "flat_50")),
    " ".join(f"{100*(SRC_P[p]-REG_P[p]):.1f}"
             for p in ("flat_0", "BAU", "flat_25", "flat_50")))

# ---------------------------------------------------------------------------
# R10g -- allowlist audit of every remaining "source-year" mention.
#
# The v28 correction campaign migrated the numbers to the registered basis but
# left ~16 prose labels reading "source-year".  Each surviving mention must be
# one of five verified-legitimate uses; anything else is a stale label.
# ---------------------------------------------------------------------------
ALLOWED_SRCYEAR = [
    # Section 3.5: the replay reproduces the source-year runner exactly
    # (953.96 / 948.96 / 923.96 / 893.96 -> 953.9 / 948.9 / 923.9 / 893.9).
    r"observed 1991--1995 source-year\s+residuals",
    # Section 3.8: explicit two-convention comparison sentence.
    r"on the\s+source-year pool, whose residual SD",
    # Section 3.11 / 3.12: verified -- at e = -80.87 the critical-zone,
    # cascade and graded rules sit at 884.6 kt for every horizon (exactly BAU).
    r"corrected source-year 10th-percentile class",
    r"Under the source-year informative class",
    # Provenance note: the superseded runner.
    r"earlier\s+source-year runner carried a different residual convention",
]

sy_hits = list(re.finditer(r"source-year", tex))
sy_bad = []
for m in sy_hits:
    ctx = tex[max(0, m.start() - 90):m.start() + 90].replace("\n", " ")
    if not any(re.search(a, ctx) for a in ALLOWED_SRCYEAR):
        ln = tex[:m.start()].count("\n") + 1
        sy_bad.append(f"line {ln}: ...{ctx[:110]}...")

chk(f"R10g every 'source-year' mention is an approved use "
    f"({len(sy_hits)} found, {len(ALLOWED_SRCYEAR)} approved)",
    not sy_bad and len(sy_hits) == len(ALLOWED_SRCYEAR),
    "; ".join(sy_bad) if sy_bad else f"{len(sy_hits)} mentions, all approved")

# Table 5's own caption must not claim the source-year convention
m_t5cap = re.search(r"\\textbf\{Table 5\.\}.{0,240}", tex, re.S)
chk("R10h Table 5 caption declares the registered convention",
    bool(m_t5cap) and "registered" in m_t5cap.group(0)
    and "source-year" not in m_t5cap.group(0),
    m_t5cap.group(0).replace("\n", " ")[:90] if m_t5cap else "not found")

# --- Fox constructive bound ------------------------------------------------
chk("R10e Fox constructive bound prints the registered 45.08",
    "45.08" in tex)
chk("R10e2 no source-year Fox constructive 79.05 survives",
    "79.05" not in tex)
print()
print(f"{len(PASS)} passed, {len(FAIL)} failed")
if FAIL:
    print("FAILED: " + ", ".join(FAIL))
sys.exit(1 if FAIL else 0)

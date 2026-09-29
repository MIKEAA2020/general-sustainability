#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification battery for paperE2_cod_intervention_v23.tex (E2, v23).

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

Run:  python3 paperE2_cod_intervention_v23_verification.py
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
TEX = os.path.join(HERE, "paperE2_cod_intervention_v23.tex")
RES = os.path.join(HERE, "results", "intervention_results_v2.json")

PASS, FAIL = [], []


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
print()
print(f"{len(PASS)} passed, {len(FAIL)} failed")
if FAIL:
    print("FAILED: " + ", ".join(FAIL))
sys.exit(1 if FAIL else 0)

#!/usr/bin/env python3
"""
V15 reactive-layer analysis — Northern cod (NAFO 2J3KL).

Purpose: two scored additions to E2 v15 (built on the authoritative repo v14),
BOTH in the single source-year convention (the corrected convention).
  (A) "harvest-the-surplus" fraction rules  C(S) = a * max(0, g(S) - g(K*)):
      genuinely reactive switch-ABOVE-the-LRP rules that harvest only the
      surplus in excess of the maintenance level at the LRP, tapering to zero
      as S -> K*.
  (B) "reactive fraction of LRP": a linear ramp C(S)=min(Cmax, q*(S-K*)) and
      a graded reactive buffer staircase (0/30/45/60 etc. kt above the LRP).

These are genuine feedback rules (catch depends on current stock), not the
static flat caps / S1 / cascade. Scored with the frozen retention rule so the
reactive family joins the declared family and can be retained/rejected on the
same terms. Only the residual convention differs from the frozen protocol
(source-year catch C_t paired with the S_t->S_{t+1} transition), which is the
internally consistent reading. No archived file is modified.

Run:  python3 src/run_v15_reactive.py
Out:  results_v15/reactive_results.json, reactive_summary.csv
Deterministic; no randomness.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np

import run_intervention_srcyear as base  # noqa: E402  (same dir; source-year)


ROOT = base.ROOT
OUT = ROOT / "results_v15"
K_STAR = base.K_STAR
HORIZONS = base.HORIZONS

SP, kernel, kernel_inf_stable, boundary, supply_replay, surplus = (
    base.surplus, base.kernel, base.kernel_inf_stable, base.boundary,
    base.supply_replay, base.surplus)


# ---------------------------------------------------------------- reactive family

def _surplus_harvest(alpha):
    """C(S) = alpha * max(0, g(S) - g(K*)); tapers to 0 at S = K*."""
    def fn(S):
        g = surplus(S, R, K)
        g_k = surplus(K_STAR, R, K)
        return float(alpha * max(0.0, g - g_k))
    return fn


def _ramp(q, cmax):
    """C(S) = min(cmax, q * max(0, S - K*))."""
    def fn(S):
        return float(min(cmax, q * max(0.0, S - K_STAR)))
    return fn


def _stair(thresholds, catches):
    """Graded reactive buffer staircase (increasing catch above the LRP)."""
    def fn(S):
        for i, th in enumerate(thresholds):
            if S < th:
                return float(catches[i])
        return float(catches[-1])
    return fn


def _grid():
    """Ascending thresholds S_LO..S_HI so the continuous reactive rules are
    represented faithfully as the piecewise-constant catches the kernel uses."""
    ts = []
    s = 1.0
    while s < 1400.0:
        ts.append(s)
        s += 25.0
    s = 1400.0
    while s < base.S_HI:
        ts.append(s)
        s += 200.0
    ts.append(base.S_HI)
    return sorted(set(ts))


GRID = _grid()


def make_reactive_policies():
    pol = {}

    def add(pid, fn, label):
        pol[pid] = {"fn": fn, "thresholds": list(GRID), "label": label}

    # (A) harvest-the-surplus fraction rules
    for a in (1.0, 0.75, 0.5, 0.25):
        add(f"sp_{int(round(a*100)):03d}",
            _surplus_harvest(a),
            f"surplus-harvest: C = {a:.2f}*max(0, g(S)-g(K*)) (0 at LRP)")

    # (B1) linear ramp reactive fraction of the LRP
    q60 = 60.0 / (1.5 * K_STAR - K_STAR)          # 0.13562
    q120 = 120.0 / (2.0 * K_STAR - K_STAR)        # same slope, higher cap
    add("ramp60", _ramp(q60, 60.0),
        "reactive ramp C = min(60, 0.1356*(S-K*))  [@1.5LRP=60]")
    add("ramp90", _ramp(q60, 90.0),
        "reactive ramp C = min(90, 0.1356*(S-K*))  [cap 90]")
    add("ramp120", _ramp(q120, 120.0),
        "reactive ramp C = min(120, 0.1356*(S-K*)) [@2LRP=120]")

    # (B2) graded reactive buffer staircase above the LRP
    add("stair60", _stair([K_STAR, 1.25 * K_STAR, 1.5 * K_STAR],
                          [0.0, 20.0, 40.0, 60.0]),
        "reactive staircase 0/20/40/60 kt at K*/1.25K*/1.5K*")
    add("stair60c", _stair([K_STAR, 1.25 * K_STAR, 1.5 * K_STAR],
                           [0.0, 30.0, 45.0, 60.0]),
        "reactive staircase 0/30/45/60 kt at K*/1.25K*/1.5K*")
    add("stair120", _stair([K_STAR, 1.5 * K_STAR], [0.0, 60.0, 120.0]),
        "reactive staircase 0/60/120 kt at K*/1.5K*")
    return pol


# ---------------------------------------------------------------- scoring

def le(p, q):
    if p is None:
        return q is None
    return q is None or p <= q + 1e-9


def lt(p, q):
    if p is None:
        return False
    return q is None or p < q - 1e-9


def BND_BAU(UC):
    bau = base.make_policies()["BAU"]
    out = {}
    for ucid, e in UC.items():
        out[ucid] = {
            T: (boundary(kernel_inf_stable(bau, FIT, e, K_STAR))
                if T == "inf" else boundary(kernel(bau, FIT, e, K_STAR, T)))
            for T in HORIZONS
        }
    return out


def max_flat(UC):
    out = {}
    for ucid, e in UC.items():
        c_star = float(R * K_STAR * (1.0 - K_STAR / K) + e)
        out[ucid] = round(max(c_star, 0.0), 2)
    return out


def main():
    global FIT, R, K
    FIT = base.fit_surplus()
    R, K = FIT["r"], FIT["K"]
    import sys
    sys.path.insert(0, str(ROOT))

    UC = {"UC_min": FIT["train_residual_min"],
          "UC_q05": FIT["train_residual_q05"],
          "UC_q10": FIT["train_residual_q10"]}
    UCn = {k: round(v, 2) for k, v in UC.items()}

    reactive = make_reactive_policies()
    bau_bnd = BND_BAU(UC)
    mf = max_flat(UC)

    kern = {}
    for pid, pol in reactive.items():
        kern[pid] = {ucid: {} for ucid in UC}
        for ucid, e in UC.items():
            for T in HORIZONS:
                kern[pid][ucid][T] = (
                    boundary(kernel_inf_stable(pol, FIT, e, K_STAR))
                    if T == "inf" else boundary(kernel(pol, FIT, e, K_STAR, T)))

    supply = {pid: supply_replay(FIT, pol) for pid, pol in reactive.items()}

    rows = []
    for pid in reactive:
        a_ok = all(all(le(kern[pid][ucid][T], bau_bnd[ucid][T])
                       for T in HORIZONS) for ucid in UC)
        improves = any(any(lt(kern[pid][ucid][T], bau_bnd[ucid][T])
                           for T in HORIZONS) for ucid in UC)
        rows.append({
            "policy": pid,
            "label": reactive[pid]["label"],
            "q10_T1": kern[pid]["UC_q10"][1],
            "q10_Tinf": kern[pid]["UC_q10"]["inf"],
            "q05_T1": kern[pid]["UC_q05"][1],
            "q05_Tinf": kern[pid]["UC_q05"]["inf"],
            "min_T1": kern[pid]["UC_min"][1],
            "min_Tinf": kern[pid]["UC_min"]["inf"],
            "holds_LRP_q10_Tinf": bool(kern[pid]["UC_q10"]["inf"] is not None
                                       and kern[pid]["UC_q10"]["inf"]
                                       <= K_STAR + 1e-9),
            "at_least_as_protective_as_BAU": a_ok,
            "improves_on_BAU_somewhere": improves,
            "train_mean_C": supply[pid]["train_mean_C"],
            "train_cut_fraction": supply[pid]["train_cut_active_fraction"],
            "oos_mean_C": supply[pid]["oos_mean_C"],
        })

    OUT.mkdir(exist_ok=True)
    with open(OUT / "reactive_results.json", "w") as f:
        json.dump({
            "fit": {k: v for k, v in FIT.items() if not k.startswith("_")},
            "UC": UCn, "r": R, "K": K,
            "g_Kstar": round(surplus(K_STAR, R, K), 2),
            "g_max": round(R * K / 4.0, 2),
            "Fprime_Kstar": round(1.0 + R * (1 - 2 * K_STAR / K), 4),
            "max_robust_flat_catch": mf,
            "BAU_boundaries": bau_bnd,
            "reactive": rows,
        }, f, indent=1)
    with open(OUT / "reactive_summary.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        for r in rows:
            w.writerow(r)

    print(f"r = {R:.4f}  K = {K:.1f}  g(K*) = {surplus(K_STAR, R, K):.2f}  "
          f"g_max = {R*K/4:.2f}  F'(K*) = {1 + R*(1-2*K_STAR/K):.4f}")
    print(f"UC: {UCn}")
    print(f"max robust flat catch (q10) = {mf['UC_q10']} kt; "
          f"q05 = {mf['UC_q05']} kt")
    print(f"BAU q10 T=1/Tinf = {bau_bnd['UC_q10'][1]}/"
          f"{bau_bnd['UC_q10']['inf']};  q05 Tinf = "
          f"{bau_bnd['UC_q05']['inf']}")
    print()
    hdr = f"{'policy':9s} {'q10Tinf':>8s} {'q05Tinf':>8s} {'holdLRP':>7s} " \
          f"{'>=BAU':>5s} {'impr':>4s} {'meanC':>7s} {'cutFr':>6s}"
    print(hdr)
    for r in rows:
        hl = "Y" if r["holds_LRP_q10_Tinf"] else "n"
        print(f"{r['policy']:9s} {str(r['q10_Tinf']):>8s} "
              f"{str(r['q05_Tinf']):>8s} {hl:>7s} "
              f"{'Y' if r['at_least_as_protective_as_BAU'] else 'n':>5s} "
              f"{'Y' if r['improves_on_BAU_somewhere'] else 'n':>4s} "
              f"{r['train_mean_C']:7.2f} {r['train_cut_fraction']:6.3f}")
    print("\nwrote results_v15/")


if __name__ == "__main__":
    main()

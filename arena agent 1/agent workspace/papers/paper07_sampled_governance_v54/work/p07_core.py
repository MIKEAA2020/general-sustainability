#!/usr/bin/env python3
"""Independent numerical core for Paper07 v53.

Rebuilds the registered illustrative three-state hold-map linearisation,
its forward-Euler and exponential frozen-assessment controller-flow multiplier records, one-at-a-time +/-2%
sensitivity, and the six-parameter joint-box crossing ranges. The joint
perturbation box is a numerical sensitivity design, not a confidence region.
"""
from __future__ import annotations
import argparse
import itertools
import json
import math
import time
from pathlib import Path
import numpy as np
from numpy.linalg import eigvals
from scipy.linalg import expm

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "work" / "results.json"
BASE = dict(r=0.02, K=100.0, q=0.001, eta=0.914, Emax=30.0,
            dref=1.0, d0=0.01, tm=5.0, Zref=1.0)
JOINT_PARAMETERS = ("r", "K", "q", "eta", "Emax", "dref")


def build(**updates):
    p = BASE.copy()
    p.update(updates)
    delta = math.log(2) / 10.0
    a = -p["eta"] / p["Emax"]
    b = p["eta"] * delta / p["dref"]
    c = p["d0"] * delta / (p["Zref"] + delta)
    disc = b * b - 4.0 * a * c
    if disc <= 0:
        raise ValueError("effort-law equilibrium has no real root")
    E_star = (-b - math.sqrt(disc)) / (2.0 * a)
    N_star = p["K"] * (1.0 - p["q"] * E_star / p["r"])
    if N_star <= 0:
        raise ValueError("equilibrium stock is non-positive")
    gate = 1.0 - E_star / p["Emax"]
    A_N = p["r"] * (1.0 - 2.0 * N_star / p["K"]) - p["q"] * E_star
    A_E = -p["q"] * N_star
    B_N = -A_N / (2.0 * p["tm"])
    B_E = -A_E / (2.0 * p["tm"])
    d = 1.0 / p["tm"]
    CE_m = gate * p["eta"] * (delta / p["dref"] - 2.0 * E_star / p["Emax"])
    CZ_m = gate * (p["eta"] * E_star / p["dref"] + p["d0"] * p["Zref"] / (p["Zref"] + delta) ** 2)
    CE_p = -gate * p["eta"]
    E0 = E_star * (p["Zref"] + delta) / p["Zref"]
    CZ_p = gate * p["eta"] * (-E0 * p["Zref"] / (p["Zref"] + delta) ** 2)
    A_hold = np.array([[A_N, 0.0, A_E],
                       [B_N, -d, B_E],
                       [0.0, 0.0, 0.0]], dtype=float)
    return {"parameters": p, "delta": delta, "E_star": E_star,
            "N_star": N_star, "Z_star": delta,
            "F_star": p["q"] * E_star,
            "exploitation_ratio": p["q"] * E_star / p["r"],
            "A_hold": A_hold,
            "mobilising": (CE_m, CZ_m),
            "protective": (CE_p, CZ_p)}


def exact_review(T: float, CE: float, CZ: float) -> np.ndarray:
    R = np.eye(3)
    eC = math.exp(CE * T)
    R[2, 1] = ((eC - 1.0) * CZ / CE) if abs(CE) > 1e-14 else T * CZ
    R[2, 2] = eC
    return R


def euler_review(T: float, CE: float, CZ: float) -> np.ndarray:
    R = np.eye(3)
    R[2, 1] = T * CZ
    R[2, 2] = 1.0 + T * CE
    return R


def rho(T: float, model, channel="mobilising", update="exact") -> float:
    CE, CZ = model[channel]
    R = exact_review(T, CE, CZ) if update == "exact" else euler_review(T, CE, CZ)
    return float(np.max(np.abs(eigvals(R @ expm(model["A_hold"] * T)))))


def crossing_scan(model, channel="mobilising", update="exact", Tmin=0.2,
                  Tmax=200.0, n=4001):
    Ts = np.linspace(Tmin, Tmax, n)
    rs = np.array([rho(float(T), model, channel, update) for T in Ts])
    signs = np.sign(rs - 1.0)
    idx = np.where((signs[1:] * signs[:-1] < 0.0)
                   & (signs[:-1] != 0.0) & (signs[1:] != 0.0))[0]
    out = []
    for i in idx:
        lo, hi, rlo = float(Ts[i]), float(Ts[i + 1]), float(rs[i])
        for _ in range(70):
            mid = 0.5 * (lo + hi)
            rm = rho(mid, model, channel, update)
            if (rlo - 1.0) * (rm - 1.0) < 0.0:
                hi = mid
            else:
                lo, rlo = mid, rm
        tstar = 0.5 * (lo + hi)
        ev = eigvals((exact_review(tstar, *model[channel]) if update == "exact"
                      else euler_review(tstar, *model[channel]))
                     @ expm(model["A_hold"] * tstar))
        near = sorted(ev, key=lambda x: abs(abs(x) - 1.0))[0]
        kind = "complex-pair" if abs(near.imag) > 1e-6 else ("real+1" if near.real > 0 else "real-1")
        direction = "unstable->stable" if rs[i] > 1.0 else "stable->unstable"
        out.append({"T_years": tstar, "kind": kind, "direction": direction,
                    "eigen_real": float(near.real), "eigen_imag": float(near.imag)})
    stats = {"rho_min": float(rs.min()), "rho_max": float(rs.max()),
             "rho_at_Tmin": float(rs[0]), "rho_at_Tmax": float(rs[-1]),
             "all_grid_stable": bool(np.all(rs < 1.0)),
             "all_grid_unstable": bool(np.all(rs > 1.0))}
    return out, stats


def crossings(model, channel="mobilising", update="exact", Tmin=0.2,
              Tmax=200.0, n=4001):
    return crossing_scan(model, channel, update, Tmin, Tmax, n)[0]


def _crossing_value(model):
    cr = crossings(model, "mobilising", "exact")
    return cr[0]["T_years"] if cr else None


def joint_box(percent: float, n=4001):
    records = []
    for signs in itertools.product((-1, 1), repeat=len(JOINT_PARAMETERS)):
        pert = {k: BASE[k] * (1.0 + signs[i] * percent)
                for i, k in enumerate(JOINT_PARAMETERS)}
        model = build(**pert)
        cr, stats = crossing_scan(model, "mobilising", "exact", n=n)
        records.append({"signs": list(signs), "parameters": pert,
                        "crossings": [x["T_years"] for x in cr],
                        "first_crossing": cr[0]["T_years"] if cr else None,
                        "scan": stats})
    values = [r["first_crossing"] for r in records if r["first_crossing"] is not None]
    no_cross = [r for r in records if r["first_crossing"] is None]
    return {"relative_radius": percent, "parameter_order": list(JOINT_PARAMETERS),
            "total_corners": len(records), "corners_with_crossing": len(values),
            "corners_without_crossing": len(records) - len(values),
            "no_crossing_corners_stable_on_grid": sum(r["scan"]["all_grid_stable"] for r in no_cross),
            "no_crossing_corners_unstable_on_grid": sum(r["scan"]["all_grid_unstable"] for r in no_cross),
            "crossing_min_years": min(values) if values else None,
            "crossing_max_years": max(values) if values else None,
            "corners": records}


def run(n=4001):
    m = build()
    base_crossings = {}
    for channel in ("mobilising", "protective"):
        for update in ("Euler", "exact"):
            cr = crossings(m, channel, update.lower(), n=n)
            base_crossings[f"{channel}_{update.lower()}"] = cr
    Ts = np.linspace(0.2, 200.0, n)
    radii = {f"{channel}_{update}": [rho(float(T), m, channel, update) for T in Ts]
             for channel, update in (("mobilising", "exact"), ("mobilising", "euler"),
                                     ("protective", "exact"), ("protective", "euler"))}
    annual = {name: rho(1.0, m, ch, upd)
              for name, ch, upd in (("mobilising_exact", "mobilising", "exact"),
                                    ("mobilising_euler", "mobilising", "euler"),
                                    ("protective_exact", "protective", "exact"),
                                    ("protective_euler", "protective", "euler"))}
    params = ("r", "K", "q", "eta", "Emax", "dref", "d0", "tm", "Zref")
    ota = {}
    for name in params:
        x = BASE[name]
        vals = {}
        for mult in (0.98, 0.99, 1.0, 1.01, 1.02):
            mm = build(**{name: x * mult})
            vals[f"{(mult-1)*100:+.0f}%"] = _crossing_value(mm)
        ota[name] = vals
    # Joint boxes are intentionally only on the six parameters identified
    # by the registered sensitivity note as influential.
    joint05 = joint_box(0.005, n=n)
    joint10 = joint_box(0.01, n=n)
    # A finite-difference slope of rho(T) at the exact crossing.
    T0 = base_crossings["mobilising_exact"][0]["T_years"]
    h = 1e-4
    slope = (rho(T0+h, m, "mobilising", "exact")
             - rho(T0-h, m, "mobilising", "exact")) / (2*h)
    result = {
        "edition": "paper07_sampled_governance_v53",
        "source_version": "paper07_sampled_governance_v52",
        "parameter_vector": BASE,
        "equilibrium": {k: float(m[k]) for k in ("N_star", "Z_star", "E_star", "F_star", "exploitation_ratio")},
        "linearised_gains": {k: {"CE": float(v[0]), "CZ": float(v[1])} for k, v in m.items() if k in ("mobilising", "protective")},
        "annual_spectral_radii": annual,
        "crossings": base_crossings,
        "protective_exact_grid_max": float(max(radii["protective_exact"])),
        "rho_slope_at_exact_crossing": float(slope),
        "one_at_a_time_pm2_percent": ota,
        "joint_boxes": {"0.5_percent": joint05, "1_percent": joint10},
        "scan": {"T_min_years": 0.2, "T_max_years": 200.0, "grid_points": n,
                 "refinement": "70 bisection iterations per sign change"}
    }
    return result


def main():
    ap = argparse.ArgumentParser(description="Paper07 v53 numerical core")
    ap.add_argument("--grid", type=int, default=4001,
                    help="number of review-interval grid points (default: 4001)")
    ap.add_argument("--joint-only", action="store_true",
                    help="run only the two six-parameter boxes and save their full-grid record")
    ap.add_argument("--output", default=None,
                    help="JSON output path; defaults to work/results.json or work/joint_box_fullgrid.json")
    args = ap.parse_args()
    if args.joint_only:
        t0 = time.perf_counter()
        boxes = {}
        for label, percent in (("0.5_percent", 0.005), ("1_percent", 0.01)):
            boxes[label] = joint_box(percent, n=args.grid)
            print(f"{label}: {boxes[label]['corners_with_crossing']}/64 crossing; "
                  f"{boxes[label]['corners_without_crossing']} without crossing", flush=True)
        out = {"T_min_years": 0.2, "T_max_years": 200.0,
               "grid_points": args.grid,
               "step_years": (200.0 - 0.2) / (args.grid - 1),
               "method": "all 64 sign corners per box, re-scanned from scratch and crossings bisected; no-cross status reported only as grid stability",
               "boxes": boxes}
        out["duration_seconds"] = time.perf_counter() - t0
        output = Path(args.output) if args.output else ROOT / "work/joint_box_fullgrid.json"
    else:
        out = run(n=args.grid)
        output = Path(args.output) if args.output else RESULTS
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if args.joint_only:
        print(json.dumps({"grid_points": out["grid_points"],
                          "boxes": {k: {x: v[x] for x in ("corners_with_crossing", "corners_without_crossing", "crossing_min_years", "crossing_max_years", "no_crossing_corners_stable_on_grid", "no_crossing_corners_unstable_on_grid")}
                                    for k, v in out["boxes"].items()}}, indent=2))
    else:
        print(json.dumps({"annual_spectral_radii": out["annual_spectral_radii"],
                          "crossings": out["crossings"],
                          "rho_slope_at_exact_crossing": out["rho_slope_at_exact_crossing"]}, indent=2))
    print(f"wrote {output}")

if __name__ == "__main__":
    main()

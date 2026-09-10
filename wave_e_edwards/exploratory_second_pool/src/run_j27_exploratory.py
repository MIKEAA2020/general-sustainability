#!/usr/bin/env python3
"""
EXPLORATORY second-pool replication — Uvalde Pool (J-27, TWDB 6950302).

STATUS: EXPLORATORY. This script is NOT part of the frozen Wave E spec
(wave_e_edwards/protocol.md) and its output may NOT be used to alter any
conclusion of paperE3 / paperE4 as they currently stand. Its purpose is to
generate evidence that could motivate a SPECIFICATION_v3 with an explicitly
relaxed no-pooling/no-transfer scope.

What it does
------------
Ports the frozen E3 (forecast-ladder) design to a SECOND, INDEPENDENT object:
the Uvalde Pool index well J-27, a different pool of the same aquifer. No
pooling is performed: J-27 is scored as its own object, exactly as Northern
cod is scored as its own object in wave_e_cod.

Construction mirrors wave_e_edwards/src/build_panel.py + run_ladder.py:
  * annual mean of daily-high elevation (ft AMSL)
  * year dropped if fewer than 240 daily values
  * rolling-origin out-of-sample scoring, min 15 training years, h = 1 and 5
  * the same frozen retention rule and the same M2m class demotion

Declared porting choices (comparability assumptions to be justified in v3)
--------------------------------------------------------------------------
  * Recharge driver  : R = Basin_1 + Basin_2  (Nueces-West Nueces and
    Frio-Dry Frio drainage basins = the Uvalde-area recharge basins in the
    committed USGS series). The J-17 object uses "Total" (San Antonio area).
  * Pumpage driver   : P = uvalde_kaf (committed EAA Table 1 column).
    The J-17 object uses wells_kaf (San Antonio area).
  * Clip bounds      : J-17 uses [610, 710] ft. J-27 head occupies a
    different datum band; bounds are set to the rounded extremes of the
    observed J-27 annual-mean series, declared below.

Sensitivity runs test whether the recharge-basin mapping is load-bearing.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
import pandas as pd
from numpy.linalg import lstsq

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "results"
OUT.mkdir(exist_ok=True)

MIN_TRAIN = 15
K_INST_J27 = None  # Uvalde Pool has its own critical-period levels; see below


# ---------------------------------------------------------------- panel build
def build_j27_panel() -> pd.DataFrame:
    raw = pd.read_csv(DATA / "j27_twdb_6950302_raw.csv")
    raw["date"] = pd.to_datetime(raw["datetime"], errors="coerce")
    raw["year"] = raw["date"].dt.year
    raw["H"] = pd.to_numeric(
        raw["daily_high_water_elevation(ft above msl)"], errors="coerce"
    )
    raw = raw.dropna(subset=["H", "year"])
    raw["year"] = raw["year"].astype(int)
    g = raw.groupby("year")
    out = pd.DataFrame(
        {
            "n_days": g.size(),
            "H_mean": g["H"].mean(),
            "H_min": g["H"].min(),
            "H_max": g["H"].max(),
            "n_provisional": g["status"].apply(lambda s: int((s == "R").sum())),
        }
    )
    # identical 240-day floor to the J-17 object
    out["H_mean"] = out["H_mean"].where(out["n_days"] >= 240)
    return out.reset_index()


def load_recharge_uv() -> pd.DataFrame:
    rec = pd.read_csv(DATA / "usgs_recharge_1934_2024.txt", sep="\t")
    rec.columns = [c.strip() for c in rec.columns]
    rec["year"] = rec["Year"].astype(int)
    nums = lambda cols: rec[cols].apply(pd.to_numeric, errors="coerce").sum(axis=1)
    rec["R_uv_12"] = nums(["Basin_1", "Basin_2"])          # primary Uvalde mapping
    rec["R_uv_1234"] = nums(["Basin_1", "Basin_2", "Basin_3", "Basin_4"])
    rec["R_sa_total"] = pd.to_numeric(rec["Total"], errors="coerce")  # SA object
    return rec[["year", "R_uv_12", "R_uv_1234", "R_sa_total"]]


def load_pumpage_uv() -> pd.DataFrame:
    p = pd.read_csv(DATA / "eaa_table1_discharge_1934_2023.csv")
    p["year"] = p["year"].astype(int)
    return p.rename(columns={"uvalde_kaf": "P_uv"})[["year", "P_uv"]]


# ------------------------------------------------------- the frozen E3 models
def clipf(x, lo, hi):
    return float(np.clip(x, lo, hi))


def fit_ar1(H):
    X = np.column_stack([np.ones(len(H) - 1), H[:-1]])
    y = H[1:]
    coef, *_ = lstsq(X, y, rcond=None)
    a, phi = float(coef[0]), float(coef[1])
    resid = y - X @ coef
    return {"a": a, "phi": float(np.clip(phi, -0.99, 1.05))}


def fit_m2(H, R, P):
    dH = H[1:] - H[:-1]
    X = np.column_stack([np.ones(len(dH)), R[1:], P[1:], H[:-1]])
    coef, *_ = lstsq(X, dH, rcond=None)
    alpha, beta, gamma, delta = [float(c) for c in coef]
    resid = dH - X @ coef
    phi = 0.0
    if len(resid) > 3:
        den = float(np.dot(resid[:-1], resid[:-1]))
        phi = float(
            np.clip((np.dot(resid[1:], resid[:-1]) / den) if den > 0 else 0.0, -0.95, 0.95)
        )
    return {"alpha": alpha, "beta": beta, "gamma": gamma, "delta": delta,
            "phi": phi, "sig": float(np.std(resid, ddof=1)) if len(resid) > 2 else 1.0,
            "last_resid": float(resid[-1]) if len(resid) else 0.0}


def forecast_m1(H0, p, h, lo, hi):
    H = H0
    for _ in range(h):
        H = clipf(p["a"] + p["phi"] * H, lo, hi)
    return H


def forecast_m2_vec(H0, R_path, P_path, p, use_ar=False, last_resid=0.0, lo=0, hi=1e9):
    """Faithful port of run_ladder.step_m2 / forecast_m2.

    step_m2:  nxt = H + alpha + beta*R + gamma*P + delta*H   (LEVEL update)
    """
    H = float(H0)
    resid = float(last_resid)
    for R_t, P_t in zip(R_path, P_path):
        if use_ar:
            resid = p["phi"] * resid
        else:
            resid = 0.0
        nxt = H + p["alpha"] + p["beta"] * R_t + p["gamma"] * P_t + p["delta"] * H + resid
        H = clipf(nxt, lo, hi)
    return H


def run_ladder(panel, Rcol, lo, hi):
    years = panel["year"].to_numpy()
    H = panel["H_mean"].to_numpy(float)
    R = panel[Rcol].to_numpy(float)
    P = panel["P_uv"].to_numpy(float)
    n = len(years)
    rows = []
    for origin in range(MIN_TRAIN - 1, n - 1):
        Htr, Rtr, Ptr = H[: origin + 1], R[: origin + 1], P[: origin + 1]
        p1 = fit_ar1(Htr)
        p2 = fit_m2(Htr, Rtr, Ptr)
        H0 = H[origin]
        H0d = H[origin - 1]
        Rl, Pl = R[origin], P[origin]
        Rm, Pm = float(np.mean(Rtr)), float(np.mean(Ptr))
        for h in (1, 5):
            if origin + h >= n:
                continue
            y = float(H[origin + h])
            preds = {
                "naive_persist": H0,
                "naive_mean": float(np.mean(Htr)),
                "M1": forecast_m1(H0, p1, h, lo, hi),
                "M2": forecast_m2_vec(H0, [Rl] * h, [Pl] * h, p2, lo=lo, hi=hi),
                "M2m": forecast_m2_vec(H0, [Rm] * h, [Pm] * h, p2, lo=lo, hi=hi),
                "M2_oracle": forecast_m2_vec(
                    H0, R[origin + 1: origin + h + 1], P[origin + 1: origin + h + 1],
                    p2, lo=lo, hi=hi),
            }
            for name, yhat in preds.items():
                rows.append({"origin": int(years[origin]), "horizon": int(h),
                             "model": name, "obs": y, "pred": float(yhat),
                             "sqerr": (float(yhat) - y) ** 2})
    df = pd.DataFrame(rows)
    summary = (df.groupby(["model", "horizon"], as_index=False)
                 .agg(n=("sqerr", "size"),
                      rmse=("sqerr", lambda s: float(np.sqrt(np.mean(s))))))
    return df, summary


def retention(summary):
    h1 = summary[summary["horizon"] == 1].set_index("model")["rmse"]
    persist = float(h1["naive_persist"])
    order = ["M1", "M2", "M2m"]
    simpler = {"M1": persist, "M2": min(persist, float(h1["M1"])),
               "M2m": min(persist, float(h1["M1"]))}
    listed = [m for m in order if float(h1[m]) < persist and float(h1[m]) < simpler[m]]
    class_demoted = [m for m in listed if m == "M2m"]
    return {"persist_h1": persist, "listed_by_point_rule": listed,
            "class_demoted": class_demoted,
            "retained_as_structure": [m for m in listed if m not in class_demoted],
            "rejected": [m for m in order if m not in listed]}


def validate_against_frozen_j17():
    """Run the SAME code path on the J-17 panel and check the frozen values.

    Frozen: persist 13.23 ; M1 12.84 ; M2 14.70 ; M2m 12.28 ; oracle 7.55.
    """
    j17 = pd.read_csv(DATA / "annual_panel.csv")
    m = j17[j17["H_mean"].notna() & j17["R_total"].notna()
            & j17["P_wells"].notna()].reset_index(drop=True)
    m = m.rename(columns={"R_total": "R_use", "P_wells": "P_uv"})
    # J-17 clip bounds are the frozen spec's own
    _, summ = run_ladder(m, "R_use", 610.0, 710.0)
    h1 = summ[summ.horizon == 1].set_index("model")["rmse"]
    h5 = summ[summ.horizon == 5].set_index("model")["rmse"]
    frozen = {"naive_persist": 13.23, "M1": 12.84, "M2": 14.70,
              "M2m": 12.28, "M2_oracle": 7.55}
    frozen5 = {"M2m": 17.44, "naive_persist": 21.11}
    print("\n-- PORT VALIDATION: same code path on the J-17 panel --")
    ok = True
    for k, v in frozen.items():
        got = float(h1[k]); good = abs(got - v) < 0.01
        ok &= good
        print(f"   {k:14s} frozen={v:7.2f}  port={got:7.2f}  {'OK' if good else 'MISMATCH'}")
    for k, v in frozen5.items():
        got = float(h5[k]); good = abs(got - v) < 0.02
        ok &= good
        print(f"   {k:14s} h5 frozen={v:6.2f} port={got:6.2f}  {'OK' if good else 'MISMATCH'}")
    print(f"   --> port faithful: {ok}")
    return ok


def main():
    j27 = build_j27_panel()
    rec = load_recharge_uv()
    pmp = load_pumpage_uv()
    panel = (j27.merge(rec, on="year", how="left").merge(pmp, on="year", how="left"))
    panel = panel[panel["H_mean"].notna()].reset_index(drop=True)

    # Clip bounds for J-27: rounded observed extremes of the annual-mean series
    lo = float(np.floor(panel["H_mean"].min() / 10) * 10)
    hi = float(np.ceil(panel["H_mean"].max() / 10) * 10)

    full = panel[panel["R_uv_12"].notna() & panel["P_uv"].notna()].reset_index(drop=True)
    panel.to_csv(OUT / "j27_annual_panel.csv", index=False)

    print("=" * 78)
    print("EXPLORATORY — Uvalde Pool (J-27) replication of the frozen E3 design")
    print("=" * 78)
    print(f"J-27 annual panel: {int(full.year.min())}–{int(full.year.max())} "
          f"({len(full)} usable years); clip bounds [{lo}, {hi}] ft; "
          f"head {full.H_mean.min():.1f}–{full.H_mean.max():.1f} ft")

    # ---- mechanism statistics: is Uvalde recharge near-white like San Antonio?
    def ac1(x):
        x = np.asarray(x, float)
        x = x[np.isfinite(x)]
        return float(np.corrcoef(x[1:], x[:-1])[0, 1])

    j17 = pd.read_csv(DATA / "annual_panel.csv")
    j17r = j17[j17["R_total"].notna()]
    saR_white = ac1(j17r["R_total"])
    uvR_white = ac1(full["R_uv_12"])

    Hg = full["H_mean"].to_numpy(float)
    dH = np.diff(Hg)
    dHcorr_uv = float(np.corrcoef(dH, full["R_uv_12"].to_numpy(float)[1:])[0, 1])
    saH = j17[j17["H_mean"].notna() & j17["R_total"].notna()]
    dHcorr_sa = float(np.corrcoef(np.diff(saH["H_mean"].to_numpy(float)),
                                  saH["R_total"].to_numpy(float)[1:])[0, 1])

    mech = {
        "recharge_ac1_san_antonio_Total": saR_white,
        "recharge_ac1_uvalde_Basin1_2": uvR_white,
        "corr_dH_R_san_antonio": dHcorr_sa,
        "corr_dH_R_uvalde": dHcorr_uv,
        "head_ac1_san_antonio": ac1(saH["H_mean"]),
        "head_ac1_uvalde": ac1(Hg),
    }
    print("\n-- mechanism statistics (the E3 explanation: recharge near-whiteness) --")
    for k, v in mech.items():
        print(f"   {k:38s} {v: .3f}")

    # ---- primary run + sensitivity on the recharge-basin mapping
    results = {}
    for label, Rcol in [("primary_Basin1+2", "R_uv_12"),
                        ("sens_Basin1-4", "R_uv_1234"),
                        ("falsify_SA_total", "R_sa_total")]:
        _, summ = run_ladder(full, Rcol, lo, hi)
        dec = retention(summ)
        h = summ.pivot(index="model", columns="horizon", values="rmse")
        results[label] = {"retention": dec,
                          "rmse": {m: {int(k): float(v) for k, v in h.loc[m].items()}
                                   for m in h.index}}
        print(f"\n-- {label} (R = {Rcol}) --")
        for m in ["naive_persist", "naive_mean", "M1", "M2", "M2m", "M2_oracle"]:
            if m in h.index:
                print(f"   {m:14s} h1={h.loc[m,1]:8.3f}  h5={h.loc[m,5]:8.3f}")
        print(f"   -> retained_as_structure = {dec['retained_as_structure']}"
              f" | listed = {dec['listed_by_point_rule']}"
              f" | rejected = {dec['rejected']}")

    with open(OUT / "j27_exploratory.json", "w") as f:
        json.dump({"status": "EXPLORATORY_NOT_FROZEN",
                   "object": "Uvalde Pool index well J-27 (TWDB 6950302)",
                   "no_pooling": True,
                   "mechanism": mech,
                   "clip_bounds": [lo, hi],
                   "years": [int(full.year.min()), int(full.year.max())],
                   "runs": results}, f, indent=2)
    print(f"\nwritten: {OUT/'j27_exploratory.json'}")


if __name__ == "__main__":
    main()

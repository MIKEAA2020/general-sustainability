#!/usr/bin/env python3
"""
Recomputation campaign E1 — baselines (registered revision items).

Discharges three registered revision requirements of paperE1_cod_forecast_ladder:
  C1  Spec-B naive baselines recomputed on the twelve-year origin set (the
      structural ladder's origins), all-origins and post-break (origin >= 1991);
  C1b Table 8 baselines: persistence scored on the exact origin set of the
      observed-acoustic index module (M_cap_index), Specifications A and B;
  C2  Table 3 baseline rows: persistence (frozen training-end state) and
      train-mean rows for every fixed window (Spec A collapse/recovery;
      Spec B pre_to_collapse/recovery_stall);
  C3  M4 separating control: one-year-delayed persistence (S_{origin-1})
      scored on the structural origins of both specifications — the control
      that separates the information cost of the one-year delay from the
      persistence mechanism.

Imports the committed runners from the repo clone; writes results only to
rerun_campaigns/results/. No committed artifact is modified.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

REPO = Path("/home/user/repo")
if not REPO.exists():
    REPO = Path(__file__).resolve().parents[1] / "repo"
COD = REPO / "wave_e_cod" / "src"
OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(exist_ok=True)

sys.path.insert(0, str(COD))


def _import(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


rl = _import("run_ladder", COD / "run_ladder.py")
xte = _import("run_xte", COD / "run_xte.py")
capi = _import("run_capelin_index", COD / "run_capelin_index.py")


def summary_from_rows(rows, group_cols=("model", "horizon")):
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    summ = (
        df.groupby(list(group_cols), as_index=False)
        .agg(
            n=("sqerr", "size"),
            rmse=("sqerr", lambda s: float(np.sqrt(np.mean(s)))),
            mae=("abserr", "mean"),
            log_rmse=("log_sqerr", lambda s: float(np.sqrt(np.mean(s)))),
        )
    )
    return summ


def naive_rows(years, ssb, lrp, min_train=8, post_break=None):
    """Persistence + train-mean rows on a declared origin set (mirrors
    run_ladder.naive_baselines, parameterized by min_train and a post-break
    origin-year filter)."""
    rows = []
    n = len(years)
    for origin in range(min_train - 1, n - 1):
        if post_break is not None and years[origin] < post_break:
            continue
        for h in (1, 5):
            if origin + h >= n:
                continue
            y = ssb[origin + h]
            for name, yhat in (
                ("naive_persist", ssb[origin]),
                ("naive_train_mean", float(np.mean(ssb[: origin + 1]))),
            ):
                rows.append(
                    {
                        "origin": int(years[origin]),
                        "horizon": h,
                        "model": name,
                        "sqerr": (yhat - y) ** 2,
                        "abserr": abs(yhat - y),
                        "log_sqerr": (np.log(max(yhat, rl.EPS)) - np.log(y)) ** 2,
                    }
                )
    return rows


def delayed_persist_rows(years, ssb, lrp, min_train=8):
    """M4 separating control: persistence issued from S_{origin-1} (the
    one-year information delay), scored on the structural origins."""
    rows = []
    n = len(years)
    for origin in range(min_train - 1, n - 1):
        for h in (1, 5):
            if origin + h >= n:
                continue
            y = ssb[origin + h]
            yhat = ssb[origin - 1]
            rows.append(
                {
                    "origin": int(years[origin]),
                    "horizon": h,
                    "model": "persist_delay1",
                    "sqerr": (yhat - y) ** 2,
                    "abserr": abs(yhat - y),
                    "log_sqerr": (np.log(max(yhat, rl.EPS)) - np.log(y)) ** 2,
                }
            )
    return rows


def fixed_window_baseline_rows(years, ssb, lrp, windows, omega):
    """Persistence (frozen at the training-end state) and train-mean rows for
    each declared fixed window, scored with the ladder's score() convention."""
    out = []
    for wname, (a0, a1, b0, b1) in windows.items():
        tr = (years >= a0) & (years <= a1)
        te = (years >= b0) & (years <= b1)
        i_tr = np.where(tr)[0]
        if len(i_tr) == 0:
            continue
        persist = float(ssb[i_tr[-1]])          # frozen training-end state
        mean = float(np.mean(ssb[tr]))          # training-window mean
        for name, yhat in (("persist", persist), ("mean", mean)):
            sc = rl.scores(ssb[te], np.full(np.sum(te), yhat), lrp)
            out.append(
                {
                    "omega": omega,
                    "window": wname,
                    "train": f"{a0}-{a1}",
                    "test": f"{b0}-{b1}",
                    "model": name,
                    **sc,
                }
            )
    return pd.DataFrame(out)


def main():
    # ---------- Specification A ----------
    years_a, ssb_a, c_reg_a, c_ann_a, idx_a, lrp_a = rl.load()
    # ---------- Specification B ----------
    years_b, ssb_b, c_b = xte.load_xte()
    lrp_b = xte.LRP_XTE

    out_lines = []

    # C1: Spec-B baselines on the twelve-year origin set
    b12 = naive_rows(years_b, ssb_b, lrp_b, min_train=12)
    b12_pb = naive_rows(years_b, ssb_b, lrp_b, min_train=12, post_break=1991)
    s12 = summary_from_rows(b12)
    s12_pb = summary_from_rows(b12_pb)
    out_lines.append("=== C1: Spec-B baselines, twelve-year origins ===")
    out_lines.append(s12.to_string(index=False, float_format=lambda x: f"{x:9.1f}"))
    out_lines.append("--- post-break (origin >= 1991), identical origin set ---")
    out_lines.append(s12_pb.to_string(index=False, float_format=lambda x: f"{x:9.1f}"))
    s12.to_csv(OUT / "e1_c1_specB_twelveyear_baselines.csv", index=False)
    s12_pb.to_csv(OUT / "e1_c1_specB_twelveyear_baselines_postbreak.csv", index=False)
    pd.DataFrame(b12).to_csv(OUT / "e1_c1_specB_twelveyear_rows.csv", index=False)

    # C1b: Table 8 baselines on the M_cap_index origin set (A and B)
    for tag, years, ssb, c, lrp in (
        ("A", years_a, ssb_a, c_reg_a, lrp_a),
        ("B", years_b, ssb_b, c_b, lrp_b),
    ):
        # reproduce the module's own origin set by running it
        if tag == "A":
            I = capi.carry_forward(
                years_a,
                pd.read_csv(rl.DATA / "capelin_acoustic_observed.csv"),
            )
            mdf, _ = capi.rolling(years_a, ssb_a, c_ann_a, I, lrp_a, 8, tag)
        else:
            mdf = pd.read_csv(COD.parent / "results" / "xte_rolling_summary.csv")
            # B-side M_cap origins: recompute with the committed runner's
            # module? The committed Table 8 B rows come from run_capelin_regime
            # (min_train=12); fall back to loading its outputs.
            I = capi.carry_forward(
                years_b,
                pd.read_csv(rl.DATA / "capelin_acoustic_observed.csv"),
            )
            mdf, _ = capi.rolling(years_b, ssb_b, c_b, I, lrp_b, 12, tag)
        origins = np.unique(mdf["origin"].to_numpy())
        rows = []
        for oy in origins:
            o = int(np.where(years == oy)[0][0])
            for h in (1, 5):
                if o + h >= len(years):
                    continue
                y = ssb[o + h]
                yhat = ssb[o]
                rows.append(
                    {
                        "origin": oy,
                        "horizon": h,
                        "model": "naive_persist_on_Mcap_origins",
                        "sqerr": (yhat - y) ** 2,
                        "abserr": abs(yhat - y),
                        "log_sqerr": (np.log(max(yhat, rl.EPS)) - np.log(y)) ** 2,
                    }
                )
        sm = summary_from_rows(rows)
        out_lines.append(f"=== C1b: persistence on M_cap_index origins, Spec {tag} ===")
        out_lines.append(f"(M_cap origin count: {len(origins)})")
        out_lines.append(sm.to_string(index=False, float_format=lambda x: f"{x:9.1f}"))
        sm.to_csv(OUT / f"e1_c1b_table8_baselines_spec{tag}.csv", index=False)

    # C2: Table 3 baseline rows for every fixed window
    win_a = {"collapse": (1983, 1990, 1991, 1995), "recovery": (1995, 2007, 2008, 2015)}
    win_b = {
        "pre_to_collapse": (1954, 1989, 1990, 1995),
        "recovery_stall": (1995, 2012, 2013, 2024),
    }
    fw_a = fixed_window_baseline_rows(years_a, ssb_a, lrp_a, win_a, omega="NCAM2016")
    fw_b = fixed_window_baseline_rows(years_b, ssb_b, lrp_b, win_b, omega="xteNCAM")
    out_lines.append("=== C2: fixed-window baseline rows (Table 3 addition) ===")
    out_lines.append(fw_a.to_string(index=False, float_format=lambda x: f"{x:8.1f}"))
    out_lines.append(fw_b.to_string(index=False, float_format=lambda x: f"{x:8.1f}"))
    fw_a.to_csv(OUT / "e1_c2_fixed_window_baselines_specA.csv", index=False)
    fw_b.to_csv(OUT / "e1_c2_fixed_window_baselines_specB.csv", index=False)

    # C3: M4 separating control — delayed persistence on structural origins
    da = delayed_persist_rows(years_a, ssb_a, lrp_a, min_train=8)
    db = delayed_persist_rows(years_b, ssb_b, lrp_b, min_train=12)
    sa = summary_from_rows(da)
    sb = summary_from_rows(db)
    out_lines.append("=== C3: delayed persistence (M4 separating control) ===")
    out_lines.append(sa.to_string(index=False, float_format=lambda x: f"{x:9.1f}"))
    out_lines.append(sb.to_string(index=False, float_format=lambda x: f"{x:9.1f}"))
    sa.to_csv(OUT / "e1_c3_delayed_persist_specA.csv", index=False)
    sb.to_csv(OUT / "e1_c3_delayed_persist_specB.csv", index=False)

    report = "\n\n".join(out_lines)
    (OUT / "campaign_e1_baselines.txt").write_text(report)
    print(report)


if __name__ == "__main__":
    main()

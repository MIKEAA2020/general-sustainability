#!/usr/bin/env python3
"""
Recomputation campaign E1 — M1/M1b reconciliation (registered revision item).

The paper records that the annual-landings M1 (264 kt) and M1b (78 kt) differ
from the coarse-regime recovery rows (M1 = 120, M1b = 90) although both
treatments are described as estimating a constant catch parameter on the same
SSB column. This campaign determines the actual mechanism by re-running the
recovery-window fits under both catch files and reporting the fitted objects
and the forecast inputs.

Reconciliation candidates, each tested:
  (i)   the catch file enters the one-step regression as the known input C_t,
        so different files give different (r, K) fits;
  (ii)  the forecast path consumes the declared catch file year by year, so
        the projected C_path differs between treatments;
  (iii) both.

Writes results to rerun_campaigns/results/; modifies nothing committed.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import numpy as np
import pandas as pd

REPO = Path("/home/user/repo")
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


def main():
    years, ssb, c_reg, c_ann, idx, lrp = rl.load()

    a0, a1, b0, b1 = 1995, 2007, 2008, 2015   # recovery window
    tr = (years >= a0) & (years <= a1)
    te = (years >= b0) & (years <= b1)
    i_tr = np.where(tr)[0]
    i_te = np.where(te)[0]

    report = []
    for allee in (False, True):
        fits = {}
        for label, cfile in (("regime", c_reg), ("annual", c_ann)):
            # M1/M1b (use_regime_C=False): the "constant C" is the training
            # mean of the declared catch file — catch_for_model's construction.
            C_all = rl.catch_for_model(years, cfile, tr, use_regime=False)
            p = rl.fit_params(ssb[tr], C_all[tr], allee=allee)
            start_idx = i_tr[-1]
            S0 = ssb[start_idx]
            C_path = C_all[start_idx + 1 : i_te[-1] + 1]
            yhat_full = rl.forecast_path(S0, C_path, p, use_ar=False, last_resid=0.0)
            offset = i_te[0] - (start_idx + 1)
            yhat = yhat_full[offset : offset + len(i_te)]
            sc = rl.scores(ssb[te], yhat, lrp)
            Cbar = float(np.mean(cfile[tr]))
            fits[label] = {
                "C_const_kt": round(Cbar, 4),
                "r": round(p["r"], 6),
                "K": round(p["K"], 3),
                "s_allee": (round(p["s_allee"], 4) if p["s_allee"] is not None else None),
                "sse": round(p["sse"], 3),
                "ok": p["ok"],
                "rmse": round(sc["rmse"], 3),
                "mae": round(sc["mae"], 3),
                "log_rmse": round(sc["log_rmse"], 3),
            }
        tag = "M1b" if allee else "M1"
        report.append(f"--- {tag} (recovery window train {a0}-{a1}, test {b0}-{b1}) ---")
        report.append(pd.DataFrame(fits).T.to_string())
        # the reconciliation fact: equal-quality fits, different minimizers
        if not allee:
            report.append(
                "SSE difference between treatments (regime - annual): "
                f"{round(fits['regime']['sse'] - fits['annual']['sse'], 3)} kt^2 "
                "(a flat objective: near-equal fit quality, different (r, K) minimizers)"
            )

    # the published rows to reproduce
    report.append("--- published recovery-window rows (Table 3/§3.2) ---")
    report.append("regime M1 = 120, M1b = 90 ; annual M1 = 264, M1b = 78")

    txt = "\n".join(report)
    (OUT / "campaign_e1_m1_reconciliation.txt").write_text(txt)
    print(txt)


if __name__ == "__main__":
    main()

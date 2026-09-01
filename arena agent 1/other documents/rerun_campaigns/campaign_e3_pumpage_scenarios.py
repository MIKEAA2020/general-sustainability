"""E3 Edwards forecast ladder: pumpage counterfactual scenarios (wave 7).

Declared scenario layer on the committed ladder's affine map fitted on the
pre-permit window (train 1980-1990, the ladder's window 3), simulated from the
observed 1990 head over 1991-2023 with the actual recharge sequence and
counterfactual pumpage paths. Status: counterfactual simulations of the fitted
map — declared scenarios, not forecasts, no retention implications, no module
promotion. The short-window identification caveat of the committed ladder
applies to the map itself.

Scenarios (1991-2023):
  actual      : observed pumpage (reference path)
  freeze90    : pumpage held at the 1990 value
  prepermit   : pumpage held at the 1980-1990 mean
  cut20       : 80% of observed pumpage
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import numpy as np
import pandas as pd

REPO = Path("/home/user/repo")
EDW = REPO / "wave_e_edwards" / "src"
HERE = Path(__file__).resolve().parent
OUT = HERE / "results"
OUT.mkdir(exist_ok=True)
sys.path.insert(0, str(EDW))

spec = importlib.util.spec_from_file_location("e4_intervention", EDW / "run_intervention.py")
ri = importlib.util.module_from_spec(spec)
sys.modules["e4_intervention"] = ri
spec.loader.exec_module(ri)

spec2 = importlib.util.spec_from_file_location("e3_ladder", EDW / "run_ladder.py")
rl = importlib.util.module_from_spec(spec2)
sys.modules["e3_ladder"] = rl
spec2.loader.exec_module(rl)


def main():
    panel = ri.load_panel()
    yr = panel["year"].to_numpy()
    H = panel["H_mean"].to_numpy(float)
    R = panel["R_total"].to_numpy(float)
    P = panel["P_wells"].to_numpy(float)

    m_pre = (yr >= 1980) & (yr <= 1990)
    p = rl.fit_m2(H[m_pre], R[m_pre], P[m_pre])
    a = 1.0 + p["delta"]
    alpha, beta, gamma = p["alpha"], p["beta"], p["gamma"]
    print(f"pre-permit map (1980-1990): dH = {alpha:.3f} + {beta:.5f} R + {gamma:.5f} P "
          f"+ {p['delta']:.5f} H  (a = {a:.4f})")

    i0 = int(np.where(yr == 1990)[0][0])
    i1 = int(np.where(yr == 2023)[0][0])
    R_fut = R[i0 + 1: i1 + 1]  # 1991..2023 recharge
    H_obs = H[i0 + 1: i1 + 1]
    P_act = P[i0 + 1: i1 + 1]
    P_90 = P[i0]
    P_pre = float(np.mean(P[m_pre]))

    scenarios = {
        "actual": P_act,
        "freeze90": np.full_like(P_act, P_90),
        "prepermit": np.full_like(P_act, P_pre),
        "cut20": 0.8 * P_act,
    }

    print(f"H(1990) = {H[i0]:.2f}; P(1990) = {P_90:.1f}; P_pre-permit mean = {P_pre:.1f}")
    rows = []
    for name, P_s in scenarios.items():
        h = H[i0]
        path = [h]
        for k in range(len(R_fut)):
            h = a * h + alpha + beta * R_fut[k] + gamma * P_s[k]
            path.append(h)
        path = np.array(path)
        rows.append(dict(scenario=name,
                         mean_P_1991_2023=round(float(np.mean(P_s)), 1),
                         end_head_2023=round(float(path[-1]), 2),
                         min_head=round(float(path.min()), 2),
                         mean_head=round(float(path.mean()), 2),
                         rmse_vs_observed=round(float(np.sqrt(np.mean((path[1:] - H_obs) ** 2))), 2),
                         obs_end_head_2023=round(float(H_obs[-1]), 2)))
        print(f"  {name:11} mean_P={np.mean(P_s):7.1f} end={path[-1]:7.2f} "
              f"min={path.min():7.2f} meanH={path.mean():7.2f} RMSE={np.sqrt(np.mean((path[1:] - H_obs) ** 2)):6.2f} "
              f"(obs 2023 = {H_obs[-1]:.2f})")
    pd.DataFrame(rows).to_csv(OUT / "e3_pumpage_scenarios.csv", index=False)
    print("saved:", OUT / "e3_pumpage_scenarios.csv")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exact one-step rolling-origin M2 error decomposition for J-17.

The fitted increment includes the intercept, the head-dependent drain term,
and the two flux terms. At each origin the actual-driver increment and the
persisted-flux increment use that origin's fitted coefficients. The algebraic
identity is checked per origin before summaries are written. The archived
output clip is evaluated separately because clipping is nonlinear.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
RESULTS = ROOT / "results"
OUT_CSV = RESULTS / "increment_identity_rolling.csv"
OUT_JSON = RESULTS / "increment_identity_rolling.json"
sys.path.insert(0, str(SRC))
import run_ladder  # noqa: E402


def main() -> None:
    panel = run_ladder.load_panel()
    years = panel["year"].to_numpy(dtype=int)
    head = panel["H_mean"].to_numpy(dtype=float)
    recharge = panel["R_total"].to_numpy(dtype=float)
    pumpage = panel["P_wells"].to_numpy(dtype=float)
    rows: list[dict[str, float | int]] = []

    for i in range(run_ladder.MIN_TRAIN - 1, len(years) - 1):
        fit = run_ladder.fit_m2(head[: i + 1], recharge[: i + 1], pumpage[: i + 1])
        delta = float(head[i + 1] - head[i])
        # Full fitted mechanism evaluated at realized target-year fluxes.
        m_actual = float(
            fit["alpha"]
            + fit["beta"] * recharge[i + 1]
            + fit["gamma"] * pumpage[i + 1]
            + fit["delta"] * head[i]
        )
        # Same fitted mechanism with last-observed fluxes; H_i is known at origin.
        m_persisted_flux = float(
            fit["alpha"]
            + fit["beta"] * recharge[i]
            + fit["gamma"] * pumpage[i]
            + fit["delta"] * head[i]
        )
        residual = delta - m_actual
        substitution = m_actual - m_persisted_flux
        raw_prediction = float(head[i] + m_persisted_flux)
        clipped_prediction = run_ladder.clip_H(raw_prediction)
        persistence_prediction = float(head[i])

        # Proposition 2 identity, evaluated as an empirical mean over origins.
        substitution_term = substitution**2 - m_actual**2
        residual_cross_term = -2.0 * residual * m_persisted_flux
        direct_raw_gap = (delta - m_persisted_flux) ** 2 - delta**2
        identity_error = direct_raw_gap - substitution_term - residual_cross_term
        if abs(identity_error) > 1e-8:
            raise AssertionError(f"identity failed at origin {years[i]}: {identity_error}")

        rows.append(
            {
                "origin": int(years[i]),
                "target": int(years[i + 1]),
                "delta_head_ft": delta,
                "mechanism_realized_flux_ft": m_actual,
                "mechanism_persisted_flux_ft": m_persisted_flux,
                "mechanism_residual_ft": residual,
                "substitution_term_ft2": substitution_term,
                "residual_cross_term_ft2": residual_cross_term,
                "raw_mse_gap_contribution_ft2": direct_raw_gap,
                "raw_prediction_ft": raw_prediction,
                "clipped_prediction_ft": clipped_prediction,
                "persistence_prediction_ft": persistence_prediction,
                "identity_abs_error_ft2": abs(identity_error),
            }
        )

    frame = pd.DataFrame(rows)
    archive_path = RESULTS / "rolling_forecasts.csv"
    archive = pd.read_csv(archive_path)
    archived_m2 = archive[(archive["horizon"] == 1) & (archive["model"] == "M2")].set_index("origin")
    archived_persist = archive[(archive["horizon"] == 1) & (archive["model"] == "naive_persist")].set_index("origin")
    if len(frame) != 75 or len(archived_m2) != len(frame) or len(archived_persist) != len(frame):
        raise AssertionError("unexpected h=1 origin count")
    if not np.allclose(frame["clipped_prediction_ft"], archived_m2.loc[frame["origin"], "pred"].to_numpy(), atol=1e-9, rtol=0):
        raise AssertionError("recomputed clipped M2 forecasts differ from the archived forecasts")
    if not np.allclose(frame["persistence_prediction_ft"], archived_persist.loc[frame["origin"], "pred"].to_numpy(), atol=1e-9, rtol=0):
        raise AssertionError("recomputed persistence forecasts differ from the archive")

    substitution_mean = float(frame["substitution_term_ft2"].mean())
    residual_cross_mean = float(frame["residual_cross_term_ft2"].mean())
    raw_gap_mean = float(frame["raw_mse_gap_contribution_ft2"].mean())
    raw_identity_gap = substitution_mean + residual_cross_mean
    # Use archived forecast rows for the reported, clipped score comparison.
    m2_archived = archived_m2.loc[frame["origin"], "sqerr"].to_numpy(dtype=float)
    persist_archived = archived_persist.loc[frame["origin"], "sqerr"].to_numpy(dtype=float)
    clipped_mse_gap = float(np.mean(m2_archived - persist_archived))
    target_indices = frame["target"].to_numpy(dtype=int) - int(years[0])
    observed_targets = head[target_indices]
    raw_m2_mse = float(np.mean((observed_targets - frame["raw_prediction_ft"]) ** 2))
    clipped_m2_mse = float(np.mean(m2_archived))
    persistence_mse = float(np.mean(persist_archived))
    upper_clips = frame[frame["raw_prediction_ft"] >= 710.0]
    lower_clips = frame[frame["raw_prediction_ft"] <= 610.0]

    summary = {
        "description": "Exact empirical increment-error identity for rolling h=1 M2 forecasts, before output clipping; clipped score gap reported separately.",
        "origins": int(len(frame)),
        "first_origin": int(frame["origin"].min()),
        "last_origin": int(frame["origin"].max()),
        "substitution_term_mean_ft2": substitution_mean,
        "residual_cross_term_mean_ft2": residual_cross_mean,
        "identity_sum_ft2": raw_identity_gap,
        "direct_raw_mse_gap_ft2": raw_gap_mean,
        "identity_abs_max_ft2": float(frame["identity_abs_error_ft2"].max()),
        "raw_m2_mse_ft2": raw_m2_mse,
        "persistence_mse_ft2": persistence_mse,
        "raw_mse_gap_ft2": raw_m2_mse - persistence_mse,
        "clipped_m2_mse_ft2": clipped_m2_mse,
        "clipped_mse_gap_ft2": clipped_mse_gap,
        "upper_clip_origins": [int(y) for y in upper_clips["origin"]],
        "lower_clip_origins": [int(y) for y in lower_clips["origin"]],
        "forecast_match_atol_ft": 1e-9,
        "checks": {
            "identity_holds_at_every_origin": True,
            "clipped_m2_matches_archived_forecasts": True,
            "persistence_matches_archived_forecasts": True,
            "origin_count_is_75": True,
        },
    }
    RESULTS.mkdir(parents=True, exist_ok=True)
    frame.to_csv(OUT_CSV, index=False, float_format="%.12g")
    OUT_JSON.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

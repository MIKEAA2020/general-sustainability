#!/usr/bin/env python3
"""Reproducible operating-characteristic simulation for Paper11 v68.

This version supersedes the v67 power-runner for reproduction, without
replacing the archived v67 outputs. It uses the cod estimator and rolling
scorer from rerun/src/run_ladder.py, SHA-256-derived per-replicate seeds,
within-origin caching of identical M2/M3/M4 fits, and fail-loudly accounting.
The cache reuses exactly the same deterministic optimizer result for identical
inputs; it does not change the fitted model or scoring rule.

Default run: 7 DGPs x 2 noise levels x 200 replicates; 14,000 module rows.
Use --rep-start with a separate --out-dir for restartable deterministic batches;
combine raw rows only after checking that replicate IDs are disjoint and complete.
Outputs are written beside this file unless --out-dir is supplied.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor
import hashlib
import json
import math
import os
import sys
from itertools import product
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
RUNNER_DIR = HERE / "rerun" / "src"
RUNNER_PATH = RUNNER_DIR / "run_ladder.py"
if not RUNNER_PATH.is_file():
    raise FileNotFoundError(f"registered run_ladder.py not found: {RUNNER_PATH}")
sys.path.insert(0, str(RUNNER_DIR))
import run_ladder as rl  # noqa: E402

T = 33
DEFAULT_REPS = 200
SIGMAS = (11.8, 33.8)
TIE = 0.05
HORIZONS = (1, 5)
SEED_NAMESPACE = "paper11-v68-operating-characteristics-sha256-v1"
MODULES = [
    "M1_autonomous_Schaefer",
    "M1b_autonomous_Allee",
    "M2_stockflow_regimeC",
    "M3_AR_residual",
    "M4_delayed_info",
]
COMPARATOR = {
    "M1_autonomous_Schaefer": None,
    "M1b_autonomous_Allee": "M1_autonomous_Schaefer",
    "M2_stockflow_regimeC": "M1_autonomous_Schaefer",
    "M3_AR_residual": "M2_stockflow_regimeC",
    "M4_delayed_info": "M3_AR_residual",
}

# The first five DGPs and their fitted parameters are unchanged from v67.
DGPS = {
    "D1_M1_collapse": dict(truth="M1_autonomous_Schaefer", r=1.935, K=1032.7,
                            s=None, catch="const240", S0=900.0),
    "D2_M1_recovery": dict(truth="M1_autonomous_Schaefer", r=0.458, K=500.0,
                            s=None, catch="const5", S0=30.0),
    "D3_M2_stockflow": dict(truth="M2_stockflow_regimeC", r=1.935, K=1032.7,
                             s=None, catch="regime", S0=900.0),
    "D4_M1b_depens": dict(truth="M1b_autonomous_Allee", r=0.458, K=500.0,
                           s=15.0, catch="const5", S0=30.0),
    "D5_persist_null": dict(truth=None, r=None, K=None, s=None,
                             catch="zero", S0=300.0),
    "D6_timevarying_r": dict(truth=None, kind="D6"),
    "D7_obs_error": dict(truth=None, kind="D7"),
}


def stable_seed(cell: str, sigma: float, rep: int) -> int:
    """Return a process- and platform-stable 64-bit seed for one replicate."""
    key = f"{SEED_NAMESPACE}|{cell}|{sigma:.1f}|{rep}".encode("utf-8")
    return int.from_bytes(hashlib.sha256(key).digest()[:8], "big", signed=False)


def catch_path(kind: str, years: np.ndarray) -> np.ndarray:
    if kind == "const240":
        return np.full(len(years), 240.0)
    if kind == "const5":
        return np.full(len(years), 5.0)
    if kind == "zero":
        return np.zeros(len(years))
    if kind == "regime":
        return np.array([240.0 if y <= 1991 else (120.0 if y == 1992 else 5.0)
                         for y in years], dtype=float)
    raise ValueError(f"unknown catch path: {kind}")


def simulate_d1_d5(dgp: dict, sigma: float, rng: np.random.Generator,
                   years: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    catch = catch_path(dgp["catch"], years)
    ssb = np.zeros(len(years), dtype=float)
    ssb[0] = dgp["S0"]
    for t in range(len(years) - 1):
        eps = rng.normal(0.0, sigma)
        if dgp["truth"] is None:
            ssb[t + 1] = max(ssb[t] + eps, rl.EPS)
        else:
            ssb[t + 1] = rl.step(ssb[t], catch[t], dgp["r"], dgp["K"], dgp["s"], eps)
    return ssb, catch


def simulate_d6(sigma: float, rng: np.random.Generator, T_: int) -> tuple[np.ndarray, np.ndarray]:
    """Time-varying productivity; catch is 55% of instantaneous MSY."""
    ssb = np.zeros(T_, dtype=float)
    catch = np.zeros(T_, dtype=float)
    ssb[0] = 900.0
    K = 1032.7
    for t in range(T_ - 1):
        r_t = 1.935 * math.exp(-0.05 * t) + 0.35
        catch[t] = 0.55 * r_t * K / 4.0
        ssb[t + 1] = rl.step(ssb[t], catch[t], r_t, K, None,
                             rng.normal(0.0, sigma))
    catch[-1] = catch[-2]
    return ssb, catch


def simulate_d7(sigma: float, rng: np.random.Generator, T_: int) -> tuple[np.ndarray, np.ndarray]:
    """Smooth deterministic Schaefer path observed with additive error."""
    state = np.zeros(T_, dtype=float)
    state[0] = 900.0
    r, K, catch_value = 0.9, 1032.7, 180.0
    for t in range(T_ - 1):
        state[t + 1] = rl.step(state[t], catch_value, r, K, None, 0.0)
    observed = np.maximum(state + rng.normal(0.0, sigma, T_), rl.EPS)
    return observed, np.full(T_, catch_value, dtype=float)


def rmse(values: np.ndarray) -> float:
    if not len(values):
        return float("nan")
    return float(np.sqrt(np.mean(np.square(values))))


def persistence_rmse(ssb: np.ndarray, origins: list[int], horizon: int) -> float:
    errors = [ssb[o + horizon] - ssb[o] for o in origins if o + horizon < len(ssb)]
    return rmse(np.asarray(errors, dtype=float))


def retained(scores: dict, persist: dict, module: str, tie: float = TIE) -> bool:
    comp = COMPARATOR[module]
    for h in HORIZONS:
        m = scores[module][h]
        p = persist[h]
        if not (math.isfinite(m) and math.isfinite(p)):
            return False
        if not m < p * (1.0 - tie):
            return False
        if comp is not None:
            c = scores[comp][h]
            if not math.isfinite(c) or not m < c * (1.0 - tie):
                return False
    return True


def wilson(k: int, n: int, z: float = 1.959963984540054) -> tuple[float, float]:
    if n <= 0:
        return (float("nan"), float("nan"))
    p = k / n
    den = 1.0 + z * z / n
    center = (p + z * z / (2.0 * n)) / den
    half = z * math.sqrt(p * (1.0 - p) / n + z * z / (4.0 * n * n)) / den
    return max(0.0, center - half), min(1.0, center + half)


def build_summaries(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    cell_rows = []
    power_rows = []
    chance_rows = []
    for (cell, sigma), group in df.groupby(["cell", "sigma"], sort=True):
        truth = group["truth"].iloc[0]
        rep_any = group.groupby("rep", sort=True)["retained"].any()
        any_k, n = int(rep_any.sum()), int(len(rep_any))
        any_lo, any_hi = wilson(any_k, n)
        true_rate = true_lo = true_hi = None
        true_k = None
        if isinstance(truth, str) and truth:
            true_rows = group[group.module == truth]
            true_k = int(true_rows.retained.sum())
            true_rate = true_k / n
            true_lo, true_hi = wilson(true_k, n)
            # H2-only and comparator attrition for the generating module.
            h2 = ((true_rows.rmse_h1 < true_rows.persist_h1 * (1.0 - TIE)) &
                  (true_rows.rmse_h5 < true_rows.persist_h5 * (1.0 - TIE)))
            h2_k = int(h2.sum())
            full_k = true_k
            power_rows.append({
                "cell": cell, "sigma": float(sigma), "truth": truth,
                "n_reps": n, "h2_alone_n": h2_k, "h2_alone_rate": h2_k / n,
                "full_rule_n": full_k, "full_rule_rate": true_rate,
                "removed_by_comparator_n": h2_k - full_k,
                "removed_by_comparator_given_h2": ((h2_k - full_k) / h2_k if h2_k else 0.0),
                "true_module_wilson95_low": true_lo,
                "true_module_wilson95_high": true_hi,
            })
            best_rows = group.loc[group.groupby("rep", sort=True)["rmse_h1"].idxmin()]
            first_k = int((best_rows.module == truth).sum())
            first_lo, first_hi = wilson(first_k, n)
            chance_rows.append({"cell": cell, "sigma": float(sigma), "truth": truth,
                                "n_reps": n, "truth_lowest_h1_n": first_k,
                                "truth_lowest_h1_rate": first_k / n,
                                "wilson95_low": first_lo, "wilson95_high": first_hi})
        metric = "true_module_power" if true_rate is not None else "any_module_false_retention"
        cell_rows.append({
            "cell": cell, "sigma": float(sigma), "truth": truth or "none",
            "n_reps": n, "metric": metric,
            "true_module_retained_n": true_k if true_k is not None else "",
            "true_module_rate": true_rate if true_rate is not None else "",
            "true_module_wilson95_low": true_lo if true_lo is not None else "",
            "true_module_wilson95_high": true_hi if true_hi is not None else "",
            "any_module_retained_n": any_k, "any_module_retention_rate": any_k / n,
            "any_module_wilson95_low": any_lo, "any_module_wilson95_high": any_hi,
            "specificity_rate": 1.0 - any_k / n,
            "specificity_wilson95_low": 1.0 - any_hi,
            "specificity_wilson95_high": 1.0 - any_lo,
        })
    summary = pd.DataFrame(cell_rows)
    decomposition = pd.DataFrame(power_rows)
    chance = pd.DataFrame(chance_rows)
    return summary, decomposition, chance


def run_rolling_cached(years: np.ndarray, ssb: np.ndarray, catch: np.ndarray,
                       lrp: float, min_train: int = 8) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Run the archived scorer while reusing identical per-origin fits.

    M2, M3 and M4 pass the same training state and catch arrays to
    ``fit_params`` at each origin; only their forecast residual/delay rules
    differ. Memoizing that deterministic fit saves duplicate optimizer work.
    The original function is restored even if the score run raises.
    """
    original_fit = rl.fit_params
    cache: dict[tuple, dict] = {}

    def cached_fit(S: np.ndarray, C: np.ndarray, allee: bool = False) -> dict:
        s = np.ascontiguousarray(S, dtype=float)
        c = np.ascontiguousarray(C, dtype=float)
        key = (bool(allee), s.shape, s.tobytes(), c.shape, c.tobytes())
        if key not in cache:
            cache[key] = original_fit(S, C, allee=allee)
        return cache[key]

    rl.fit_params = cached_fit
    try:
        return rl.run_rolling(years, ssb, catch, lrp, min_train=min_train)
    finally:
        rl.fit_params = original_fit


def evaluate_one(task: tuple[str, float, int]) -> list[dict]:
    """Evaluate one independently seeded replicate; exceptions propagate."""
    cell, sigma, rep = task
    dgp = DGPS[cell]
    years = np.arange(1983, 1983 + T)
    seed = stable_seed(cell, sigma, rep)
    rng = np.random.default_rng(seed)
    if dgp.get("kind") == "D6":
        ssb, catch = simulate_d6(sigma, rng, T)
    elif dgp.get("kind") == "D7":
        ssb, catch = simulate_d7(sigma, rng, T)
    else:
        ssb, catch = simulate_d1_d5(dgp, sigma, rng, years)
    _, scores_table = run_rolling_cached(years, ssb, catch, 884.6, min_train=8)
    scores, persist = {}, {}
    origins = sorted(range(7, len(years) - 1))
    for h in HORIZONS:
        subset = scores_table[scores_table.horizon == h]
        for module in MODULES:
            found = subset[subset.model == module]
            if len(found) != 1:
                raise RuntimeError(f"expected one summary row for {cell}/{sigma}/{rep}/{module}/h{h}; got {len(found)}")
            scores.setdefault(module, {})[h] = float(found.rmse.iloc[0])
        persist[h] = persistence_rmse(ssb, origins, h)
    if not all(math.isfinite(scores[m][h]) for m in MODULES for h in HORIZONS):
        raise RuntimeError(f"non-finite module score in {cell}/{sigma}/{rep}")
    if not all(math.isfinite(persist[h]) for h in HORIZONS):
        raise RuntimeError(f"non-finite persistence score in {cell}/{sigma}/{rep}")
    return [{
        "cell": cell, "dgp": cell, "truth": dgp.get("truth") or "",
        "T": T, "sigma": float(sigma), "rep": rep, "seed": seed,
        "module": module, "rmse_h1": scores[module][1],
        "rmse_h5": scores[module][5], "persist_h1": persist[1],
        "persist_h5": persist[5], "retained": retained(scores, persist, module),
    } for module in MODULES]


def run(reps: int, out_dir: Path, workers: int, rep_start: int = 0) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    rep_ids = range(rep_start, rep_start + reps)
    tasks = [(cell, float(sigma), rep)
             for cell, sigma, rep in product(DGPS, SIGMAS, rep_ids)]
    rows = []
    progress_every = max(1, len(tasks) // 20)
    if workers == 1:
        iterator = map(evaluate_one, tasks)
        for i, replicate_rows in enumerate(iterator, start=1):
            rows.extend(replicate_rows)
            if i % progress_every == 0 or i == len(tasks):
                print(f"completed {i}/{len(tasks)} replicates", flush=True)
    else:
        chunksize = max(1, len(tasks) // (workers * 16))
        with ProcessPoolExecutor(max_workers=workers) as pool:
            for i, replicate_rows in enumerate(pool.map(evaluate_one, tasks, chunksize=chunksize), start=1):
                rows.extend(replicate_rows)
                if i % progress_every == 0 or i == len(tasks):
                    print(f"completed {i}/{len(tasks)} replicates", flush=True)

    df = pd.DataFrame(rows)
    expected_rows = len(DGPS) * len(SIGMAS) * reps * len(MODULES)
    if len(df) != expected_rows:
        raise RuntimeError(f"row-count failure: expected {expected_rows}, got {len(df)}")
    expected_cells = len(DGPS) * len(SIGMAS)
    if df.groupby(["cell", "sigma"]).rep.nunique().ne(reps).any():
        raise RuntimeError("replicate-count failure in one or more DGP/noise cells")
    seed_keys = df[["cell", "sigma", "rep", "seed"]].drop_duplicates()
    if seed_keys.duplicated(["cell", "sigma", "rep"]).any():
        raise RuntimeError("inconsistent seed for one replicate key")
    if seed_keys["seed"].duplicated().any():
        # Seeds are keyed by cell, noise, and replicate; a collision would be
        # exceedingly unlikely at 64 bits, but it is checked explicitly.
        raise RuntimeError("unexpected cross-replicate seed collision")

    summary, decomposition, chance = build_summaries(df)
    raw_path = out_dir / "power_simulation_repro.csv"
    summary_path = out_dir / "power_simulation_repro_summary.csv"
    decomp_path = out_dir / "power_simulation_repro_decomposition.csv"
    chance_path = out_dir / "power_simulation_repro_chance.csv"
    df.to_csv(raw_path, index=False, float_format="%.12g")
    summary.to_csv(summary_path, index=False, float_format="%.8g")
    decomposition.to_csv(decomp_path, index=False, float_format="%.8g")
    chance.to_csv(chance_path, index=False, float_format="%.8g")

    def sha(path: Path) -> str:
        return hashlib.sha256(path.read_bytes()).hexdigest()

    manifest = {
        "edition": "Paper11 v68",
        "reps_per_cell": reps,
        "rep_start": rep_start,
        "rep_end_exclusive": rep_start + reps,
        "cells": len(DGPS) * len(SIGMAS),
        "modules_per_replicate": len(MODULES),
        "rows": len(df),
        "seed_algorithm": "SHA-256(namespace|cell|sigma-to-1-decimal|rep), first 8 digest bytes, unsigned big-endian",
        "seed_namespace": SEED_NAMESPACE,
        "generator": "numpy.random.default_rng (PCG64 in recorded environment)",
        "python_version": sys.version.split()[0],
        "numpy_version": np.__version__,
        "pandas_version": pd.__version__,
        "simulator_sha256": sha(Path(__file__).resolve()),
        "run_ladder_sha256": sha(RUNNER_PATH),
        "outputs": {
            raw_path.name: sha(raw_path),
            summary_path.name: sha(summary_path),
            decomp_path.name: sha(decomp_path),
            chance_path.name: sha(chance_path),
        },
        "workers": workers,
        "blas_thread_environment": {name: os.environ.get(name) for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
        "failed_replicates": 0,
        "note": "No exception is swallowed; the run aborts on a failed or non-finite replicate."
    }
    manifest_path = out_dir / "power_simulation_repro_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(f"\nWrote {len(df)} rows to {raw_path}")
    print("Cell summaries (rate; Wilson 95% interval):")
    for row in summary.to_dict(orient="records"):
        if row["true_module_rate"] != "":
            print(f"  {row['cell']:<22} sigma={row['sigma']:>4g} power={row['true_module_rate']:.3f} "
                  f"[{row['true_module_wilson95_low']:.3f}, {row['true_module_wilson95_high']:.3f}]")
        else:
            print(f"  {row['cell']:<22} sigma={row['sigma']:>4g} false-retention={row['any_module_retention_rate']:.3f} "
                  f"[{row['any_module_wilson95_low']:.3f}, {row['any_module_wilson95_high']:.3f}]")
    print(f"\nManifest: {manifest_path}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reps", type=int, default=DEFAULT_REPS,
                        help=f"replicates per DGP/noise cell (default: {DEFAULT_REPS})")
    parser.add_argument("--out-dir", type=Path, default=HERE,
                        help="output directory (default: directory containing this script)")
    parser.add_argument("--workers", type=int, default=min(4, os.cpu_count() or 1),
                        help="independent replicate workers (default: min(4, CPU count))")
    parser.add_argument("--rep-start", type=int, default=0,
                        help="first replicate id (useful for restartable deterministic batches)")
    args = parser.parse_args()
    if args.reps <= 0:
        parser.error("--reps must be positive")
    if args.workers <= 0:
        parser.error("--workers must be positive")
    if args.rep_start < 0:
        parser.error("--rep-start must be nonnegative")
    run(args.reps, args.out_dir.resolve(), args.workers, args.rep_start)


if __name__ == "__main__":
    main()

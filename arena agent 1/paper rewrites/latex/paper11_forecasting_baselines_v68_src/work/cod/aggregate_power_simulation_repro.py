#!/usr/bin/env python3
"""Combine deterministic replicate batches into the Paper11 v68 power archive.

Each input directory must have been produced by sim_retention_power_repro.py.
The aggregator checks each batch manifest and file hash, requires disjoint and
complete replicate IDs 0..199 in every DGP/noise cell, verifies stable seeds,
then writes the canonical raw and summary files plus a combined manifest.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import pandas as pd

HERE = Path(__file__).resolve().parent
SIM_PATH = HERE / "sim_retention_power_repro.py"
RUNNER_PATH = HERE / "rerun" / "src" / "run_ladder.py"
spec = importlib.util.spec_from_file_location("sim_retention_power_repro", SIM_PATH)
sim = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = sim
spec.loader.exec_module(sim)


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--batches", nargs="+", required=True, type=Path,
                   help="batch directories written by the deterministic simulator")
    p.add_argument("--out-dir", type=Path, default=HERE,
                   help="canonical output directory (default: work/cod)")
    p.add_argument("--reps", type=int, default=200,
                   help="expected replicate IDs per cell (default: 200)")
    args = p.parse_args()
    if args.reps <= 0:
        p.error("--reps must be positive")

    batch_frames = []
    batch_records = []
    intervals = []
    expected_cells = {(cell, float(sigma)) for cell in sim.DGPS for sigma in sim.SIGMAS}
    for batch_dir in args.batches:
        batch_dir = batch_dir.resolve()
        csv_path = batch_dir / "power_simulation_repro.csv"
        manifest_path = batch_dir / "power_simulation_repro_manifest.json"
        if not csv_path.is_file() or not manifest_path.is_file():
            raise FileNotFoundError(f"missing simulator output/manifest in {batch_dir}")
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest.get("edition") != "Paper11 v68" or manifest.get("failed_replicates") != 0:
            raise ValueError(f"unexpected or failed batch manifest: {manifest_path}")
        if manifest.get("simulator_sha256") != sha(SIM_PATH) or manifest.get("run_ladder_sha256") != sha(RUNNER_PATH):
            raise ValueError(f"batch used a different simulator or runner: {manifest_path}")
        if (manifest.get("cells") != len(expected_cells)
                or manifest.get("modules_per_replicate") != len(sim.MODULES)
                or manifest.get("rows") != len(expected_cells) * int(manifest.get("reps_per_cell", 0)) * len(sim.MODULES)):
            raise ValueError(f"inconsistent batch counts in {manifest_path}")
        for name, expected_hash in manifest.get("outputs", {}).items():
            path = batch_dir / name
            if not path.is_file() or sha(path) != expected_hash:
                raise ValueError(f"batch output hash mismatch: {path}")
        start = int(manifest["rep_start"])
        end = int(manifest["rep_end_exclusive"])
        if end - start != int(manifest["reps_per_cell"]):
            raise ValueError(f"bad replicate interval in {manifest_path}")
        if manifest["outputs"].get(csv_path.name) != sha(csv_path):
            raise ValueError(f"raw-output hash mismatch: {csv_path}")
        frame = pd.read_csv(csv_path)
        # pandas treats the empty truth field for null/out-of-class DGPs as NaN;
        # restore the simulator's canonical empty string before summarizing.
        frame["truth"] = frame["truth"].fillna("")
        if len(frame) != len(expected_cells) * (end - start) * len(sim.MODULES):
            raise ValueError(f"unexpected row count in {csv_path}")
        if set(zip(frame["cell"], frame["sigma"].astype(float))) != expected_cells:
            raise ValueError(f"missing DGP/noise cells in {csv_path}")
        if set(frame["module"]) != set(sim.MODULES):
            raise ValueError(f"missing module rows in {csv_path}")
        if set(frame["rep"].astype(int)) != set(range(start, end)):
            raise ValueError(f"incomplete replicate IDs in {csv_path}")
        if frame.duplicated(["cell", "sigma", "rep", "module"]).any():
            raise ValueError(f"duplicate replicate/module rows in {csv_path}")
        seed_rows = frame[["cell", "sigma", "rep", "seed"]].drop_duplicates()
        if seed_rows["seed"].duplicated().any():
            raise ValueError(f"unexpected cross-replicate seed collision in {csv_path}")
        for row in seed_rows.itertuples(index=False):
            if int(row.seed) != sim.stable_seed(str(row.cell), float(row.sigma), int(row.rep)):
                raise ValueError(f"seed mismatch in {csv_path}: {row}")
        intervals.append((start, end))
        batch_frames.append(frame)
        batch_records.append({
            "directory": batch_dir.name,
            "rep_start": start,
            "rep_end_exclusive": end,
            "rows": len(frame),
            "raw_sha256": sha(csv_path),
            "manifest_sha256": sha(manifest_path),
            "workers": manifest.get("workers"),
        })

    intervals.sort()
    if not intervals or intervals[0][0] != 0 or intervals[-1][1] != args.reps:
        raise ValueError(f"batches do not cover [0, {args.reps}): {intervals}")
    if any(left[1] != right[0] for left, right in zip(intervals, intervals[1:])):
        raise ValueError(f"batches overlap or leave gaps: {intervals}")

    df = pd.concat(batch_frames, ignore_index=True)
    if df.duplicated(["cell", "sigma", "rep", "module"]).any():
        raise ValueError("duplicate rows after batch merge")
    if len(df) != len(expected_cells) * args.reps * len(sim.MODULES):
        raise ValueError(f"wrong merged row count: {len(df)}")
    if df.groupby(["cell", "sigma"]).rep.nunique().ne(args.reps).any():
        raise ValueError("one or more merged cells lack the expected replicate count")

    # Canonical deterministic order: DGP order, noise order, replicate, module order.
    df["cell"] = pd.Categorical(df["cell"], categories=list(sim.DGPS), ordered=True)
    df["sigma"] = pd.Categorical(df["sigma"].astype(float), categories=list(sim.SIGMAS), ordered=True)
    df["module"] = pd.Categorical(df["module"], categories=sim.MODULES, ordered=True)
    df = df.sort_values(["cell", "sigma", "rep", "module"], kind="stable").reset_index(drop=True)
    summary, decomposition, chance = sim.build_summaries(df)

    out_dir = args.out_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    outputs = {
        "power_simulation_repro.csv": df,
        "power_simulation_repro_summary.csv": summary,
        "power_simulation_repro_decomposition.csv": decomposition,
        "power_simulation_repro_chance.csv": chance,
    }
    for name, table in outputs.items():
        path = out_dir / name
        table.to_csv(path, index=False, float_format="%.12g" if name.endswith(".csv") and name == "power_simulation_repro.csv" else "%.8g")
    manifest = {
        "edition": "Paper11 v68",
        "reps_per_cell": args.reps,
        "rep_start": 0,
        "rep_end_exclusive": args.reps,
        "cells": len(expected_cells),
        "modules_per_replicate": len(sim.MODULES),
        "rows": len(df),
        "seed_algorithm": "SHA-256(namespace|cell|sigma-to-1-decimal|rep), first 8 digest bytes, unsigned big-endian",
        "seed_namespace": sim.SEED_NAMESPACE,
        "generator": "numpy.random.default_rng (PCG64 in recorded environment)",
        "python_version": sys.version.split()[0],
        "numpy_version": sim.np.__version__,
        "pandas_version": pd.__version__,
        "simulator_sha256": sha(SIM_PATH),
        "run_ladder_sha256": sha(RUNNER_PATH),
        "aggregation_script_sha256": sha(Path(__file__).resolve()),
        "batches": batch_records,
        "outputs": {name: sha(out_dir / name) for name in outputs},
        "failed_replicates": 0,
        "note": "Four seeded replicate-ID batches were validated and merged; exceptions are not swallowed by the simulator.",
    }
    manifest_path = out_dir / "power_simulation_repro_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"rows": len(df), "reps_per_cell": args.reps,
                      "batches": intervals, "outputs": manifest["outputs"],
                      "manifest": str(manifest_path)}, indent=2))
    print("Cell summary:")
    for row in summary.to_dict(orient="records"):
        if row["true_module_rate"] != "":
            print(f"  {row['cell']:<22} sigma={row['sigma']:>4g} power={row['true_module_rate']:.3f} "
                  f"[{row['true_module_wilson95_low']:.3f}, {row['true_module_wilson95_high']:.3f}]")
        else:
            print(f"  {row['cell']:<22} sigma={row['sigma']:>4g} false-retention={row['any_module_retention_rate']:.3f} "
                  f"[{row['any_module_wilson95_low']:.3f}, {row['any_module_wilson95_high']:.3f}]")


if __name__ == "__main__":
    main()

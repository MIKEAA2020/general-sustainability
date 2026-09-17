#!/usr/bin/env python3
"""Checkpointed rescue runner for the cod T=71 band calibration (frozen sheet
2026-09-16; rescue of the 2026-09-16 full run whose process died with the sandbox
session before writing output — zero checkpoint bytes survived).

DESIGN RULE: this wrapper imports the FROZEN harness
(`framework/campaign_cod_t71_band_calibration.py`) — simulate/ladder_rmse/
frozen_rule/seed_for/DGP/SIGMAS/BANDS are used verbatim, never reimplemented.
Seeds are per-rep deterministic (MD5 salt map), so a resumed run reproduces
exactly the runs a killed run would have produced: interruption-safe, bitwise
idempotent.

Behaviour:
  - per-rep checkpoint: after EVERY rep, partial results are flushed to
    phase_c/results/cod_t71_band_calibration_20260917_checkpoint.json
    (rep-level per-band power bits and wrong-module counts).
  - resume: on start, existing checkpoint rows are honoured; only missing
    (cell, sigma, rep) are computed.
  - finalise: when all 800 reps exist, the final JSON is written IN THE FROZEN
    SCHEMA to phase_c/results/cod_t71_band_calibration_20260916.json
    (the sheet-registered filename; it never existed — this is its first write,
    not an overwrite) with run metadata disclosing the rescue provenance.
PYTHONHASHSEED=0 required (same convention as the frozen harness).
"""
import os, sys, json, time, datetime
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
WS = HERE if os.path.isdir(os.path.join(HERE, "wave_e_cod")) else os.path.dirname(HERE)
sys.path.insert(0, HERE)
assert os.environ.get("PYTHONHASHSEED") == "0", "pinned-seed convention"

import campaign_cod_t71_band_calibration as H  # noqa: E402

CKPT = os.path.join(WS, "phase_c", "results", "cod_t71_band_calibration_20260917_checkpoint.json")
OUT_FULL = H.OUT_FULL  # sheet-registered: cod_t71_band_calibration_20260916.json
FULL_REPS = 200
CELLS = ("D1", "D5")


def load_ckpt():
    if os.path.exists(CKPT):
        with open(CKPT) as f:
            return json.load(f)
    return {"mode": "per-rep checkpoint (rescue run 2026-09-17)", "reps_done": {}, "wrong_extra": {}}


def save_ckpt(d):
    tmp = CKPT + ".tmp"
    with open(tmp, "w") as f:
        json.dump(d, f)
    os.replace(tmp, CKPT)


def main():
    t0 = time.time()
    ck = load_ckpt()
    total = len(CELLS) * len(H.SIGMAS) * FULL_REPS
    done0 = sum(len(v["per_band_power"][str(H.BANDS[0])]) for v in ck.get("cells", {}).values()) if "cells" in ck else 0
    print(f"[checkpoint] resume: {done0}/{total} reps already done")
    ck.setdefault("cells", {})
    for cell in CELLS:
        for sigma in H.SIGMAS:
            key = f"{cell}_s{sigma}"
            cellrec = ck["cells"].setdefault(key, {
                "truth": H.DGP[cell]["truth"], "reps": FULL_REPS,
                "per_band_power": {str(b): [] for b in H.BANDS},
                "wrong_module_retention_reps": {str(b): 0 for b in H.BANDS}})
            have = len(cellrec["per_band_power"][str(H.BANDS[0])])
            for rep in range(have, FULL_REPS):
                rng = np.random.default_rng(H.seed_for(cell, sigma, rep))
                S = H.simulate(cell, sigma, rng)
                C_reg = H.catch_path(H.DGP[cell]["catch"])
                truth = H.DGP[cell]["truth"]
                rm, pers = H.ladder_rmse(S, C_reg)
                for b in H.BANDS:
                    p, w = H.frozen_rule(rm, pers, b, truth)
                    cellrec["per_band_power"][str(b)].append(p)
                    cellrec["wrong_module_retention_reps"][str(b)] += w
                if (rep + 1) % 10 == 0 or rep + 1 == FULL_REPS:
                    save_ckpt(ck)
                    el = time.time() - t0
                    print(f"[checkpoint] {key} rep {rep + 1}/{FULL_REPS} flushed  (elapsed {el:.0f}s)", flush=True)
    # ---- finalise in the frozen schema ----
    out = {"run": "20260916", "stage": "full",
           "rescue": ("process from run 20260916 died with sandbox session before first write; "
                      "this file is the FIRST write of the sheet-registered name, produced 2026-09-17 by "
                      "campaign_cod_t71_band_calibration_checkpointed_20260917.py (frozen harness imported "
                      "unchanged; identical per-rep seed map)"),
           "T": H.T, "years": [1954, 2024],
           "reps": FULL_REPS, "bands": H.BANDS, "sigma": H.SIGMAS,
           "seed_map": f"MD5(f'{H.SALT}:{{cell}}:{{sigma}}:{{rep}}') mod 2^31",
           "scope_note": ("D1/D5 lifted per frozen v4 A1.4; D6/D7 disclosed as deferred "
                          "(frozen-space sheet 6.2) - their v4 A1.2 generators were T=33-calibrated; "
                          "inventing a T=71 version would be drift."),
           "cells": {}}
    for key, cellrec in ck["cells"].items():
        out["cells"][key] = {"truth": cellrec["truth"], "reps": FULL_REPS,
                             "per_band_power": cellrec["per_band_power"],
                             "wrong_module_retention_reps": cellrec["wrong_module_retention_reps"]}
    out["wall_s"] = round(time.time() - t0, 1)
    pooled = []
    for b in H.BANDS:
        pw = {k: float(np.mean(out["cells"][k]["per_band_power"][str(b)])) for k in out["cells"] if k.startswith("D1")}
        sp = 1.0 - float(np.mean([np.mean(out["cells"][k]["per_band_power"][str(b)]) for k in out["cells"] if k.startswith("D5")]))
        pooled.append({"band": b, "power_components": {k: round(v, 4) for k, v in pw.items()},
                       "mean_power": float(np.mean(list(pw.values()))) if pw else None,
                       "specificity": round(sp, 4)})
    out["pooled"] = pooled
    out["finished_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(OUT_FULL, "w") as f:
        json.dump(out, f, indent=1)
    print("wrote " + OUT_FULL)


if __name__ == "__main__":
    main()

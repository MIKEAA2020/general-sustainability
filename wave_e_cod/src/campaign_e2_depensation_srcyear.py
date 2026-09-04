#!/usr/bin/env python3
"""
Recomputation campaign E2 — depensation sensitivity row (registered revision
item of paperE2_cod_intervention: the Allee/depensation term was declared off
and never tested).

Two rows are produced:
  (a) data-identified depensation: the intervention's own one-step LS refit
      with the Allee form surplus(S) = r S (1 - S/K) (S - s0)/(K - s0) on the
      frozen training window 1983-2007 (annual catch), kernels on the same
      policy family and UC floors; if s0 -> 0 the row records the
      non-identification explicitly;
  (b) declared-strength sensitivity: the same machinery at the declared
      strength s0 = 0.5 * K_star (a depensation threshold at half the safe-set
      boundary), showing the kernel's response to depensation independent of
      the training window's identification power.

The committed kernel machinery is concave-quadratic; the Allee map is cubic,
so kernels are computed on a fine grid over [K_star, S_HI] with the grid
membership test declared at its resolution. As a built-in self-check, the grid
kernel is first reproduced for the committed Schaefer fit and compared against
the committed boundaries (the grid must recover them within its resolution).

Writes results to rerun_campaigns/results/; modifies nothing committed.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

REPO = Path("/tmp/liverepo")
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
ri = _import("run_intervention", COD / "run_intervention_srcyear.py")

DS = 0.05  # kt grid resolution on [K_star, S_HI]


def grid_kernel(fit, policy, e, K_star, S_HI, T, s_allee=None):
    """T-step robust kernel of the worst-case closed loop on a grid.
    F(S) = S + surplus(S, r, K, s_allee) - c(piece) + e.
    Returns (list_of_intervals, mask) with intervals as (lo, hi)."""
    grid = np.arange(K_star, S_HI + DS, DS)
    mask = np.ones(len(grid), dtype=bool)
    pcs = ri._pieces(policy["thresholds"])

    def piece_c(plo, phi):
        return float(policy["fn"](0.5 * (plo + phi)))

    if T == "inf":
        iters, max_iters, stable = 0, 2000, False
        while not stable and iters < max_iters:
            nxt = np.zeros(len(grid), dtype=bool)
            for (plo, phi) in pcs:
                c = piece_c(plo, phi)
                sel = (grid >= plo) & (grid <= phi)
                if not sel.any():
                    continue
                F = grid[sel] + rl.surplus(grid[sel], fit["r"], fit["K"], s_allee) - c + e
                idx = np.rint((F - grid[0]) / DS).astype(int)
                ok = (F >= grid[0] - 1e-9) & (F <= grid[-1] + 1e-9)
                nxt[sel] = ok & mask[np.clip(idx, 0, len(grid) - 1)]
            stable = bool(np.array_equal(nxt, mask))
            mask = nxt
            iters += 1
            if not mask.any():
                return [], mask
        if not stable:
            raise RuntimeError("grid kernel did not converge")
        return intervals(mask, grid), mask
    else:
        for _ in range(int(T)):
            nxt = np.zeros(len(grid), dtype=bool)
            for (plo, phi) in pcs:
                c = piece_c(plo, phi)
                sel = (grid >= plo) & (grid <= phi)
                if not sel.any():
                    continue
                F = grid[sel] + rl.surplus(grid[sel], fit["r"], fit["K"], s_allee) - c + e
                idx = np.rint((F - grid[0]) / DS).astype(int)
                ok = (F >= grid[0] - 1e-9) & (F <= grid[-1] + 1e-9)
                nxt[sel] = ok & mask[np.clip(idx, 0, len(grid) - 1)]
            mask = nxt
            if not mask.any():
                return [], mask
        return intervals(mask, grid), mask


def intervals(mask, grid):
    out = []
    d = np.diff(mask.astype(int))
    starts = list(np.where(d == 1)[0] + 1)
    ends = list(np.where(d == -1)[0] + 1)
    if mask[0]:
        starts = [0] + starts
    if mask[-1]:
        ends = ends + [len(mask)]
    for s, e in zip(starts, ends):
        out.append((float(grid[s]), float(grid[e - 1])))
    return out


def main():
    years, ssb, c_reg, c_ann, idx, lrp = rl.load()
    m_tr = years <= ri.TRAIN_END
    K_STAR, S_HI = ri.K_STAR, ri.S_HI

    fit = ri.fit_surplus()
    UC = {
        "UC_min": fit["train_residual_min"],
        "UC_q05": fit["train_residual_q05"],
        "UC_q10": fit["train_residual_q10"],
    }
    policies = ri.make_policies()

    committed = json.loads(
        (REPO / "wave_e_cod" / "results" / "intervention_results.json").read_text()
    )

    allee_fit = rl.fit_params(ssb[m_tr], c_ann[m_tr], allee=True)
    fit_a = {"r": allee_fit["r"], "K": allee_fit["K"], "s_allee": allee_fit["s_allee"]}

    rows = []
    # (0) self-check: grid kernel reproduces the committed Schaefer boundaries
    schaefer = {"r": fit["r"], "K": fit["K"]}
    for pid, pol in policies.items():
        for ucid, e in UC.items():
            for T in (1, 3, 5, "inf"):
                committed_b = committed.get("kernels", {}).get(pid, {}).get(ucid, {}).get(str(T))
                intervals_, _ = grid_kernel(schaefer, pol, e, K_STAR, S_HI, T, s_allee=None)
                b = round(intervals_[0][0], 3) if intervals_ else None
                c_b = (
                    round(float(committed_b["nominal"][0][0]), 3)
                    if committed_b and committed_b.get("nominal")
                    else None
                )
                rows.append(
                    {
                        "variant": "grid_schaefer_check",
                        "policy": pid,
                        "UC": ucid,
                        "T": T,
                        "boundary_grid": b,
                        "boundary_committed": c_b,
                        "n_intervals": len(intervals_),
                    }
                )

    # (a) data-identified depensation
    for pid, pol in policies.items():
        for ucid, e in UC.items():
            for T in (1, 3, 5, "inf"):
                intervals_, _ = grid_kernel(fit_a, pol, e, K_STAR, S_HI, T, s_allee=fit_a["s_allee"])
                rows.append(
                    {
                        "variant": "depensation_fit",
                        "policy": pid,
                        "UC": ucid,
                        "T": T,
                        "boundary": round(intervals_[0][0], 3) if intervals_ else None,
                        "n_intervals": len(intervals_),
                    }
                )

    # (b) declared-strength sensitivity s0 = 0.5 * K_star
    fit_b = {"r": fit["r"], "K": fit["K"], "s_allee": 0.5 * K_STAR}
    for pid, pol in policies.items():
        for ucid, e in UC.items():
            for T in (1, 3, 5, "inf"):
                intervals_, _ = grid_kernel(fit_b, pol, e, K_STAR, S_HI, T, s_allee=0.5 * K_STAR)
                rows.append(
                    {
                        "variant": "depensation_s0=0.5Kstar",
                        "policy": pid,
                        "UC": ucid,
                        "T": T,
                        "boundary": round(intervals_[0][0], 3) if intervals_ else None,
                        "n_intervals": len(intervals_),
                    }
                )

    df = pd.DataFrame(rows)
    df.to_csv(OUT / "campaign_e2_depensation.csv", index=False)

    print("=== depensation fit on 1983-2007 (annual catch) ===")
    print("  Schaefer committed: r =", round(fit["r"], 4), " K =", fit["K"])
    print(
        "  Allee refit       : r =", round(fit_a["r"], 4),
        " K =", round(fit_a["K"], 2),
        " s0 =", round(fit_a["s_allee"], 4) if fit_a["s_allee"] is not None else None,
        " sse =", round(allee_fit["sse"], 2),
    )
    print("=== self-check: grid vs committed Schaefer boundaries ===")
    chk = df[df.variant == "grid_schaefer_check"]
    print(chk.to_string(index=False))
    print("=== depensation rows (boundary = lower end of lowest interval) ===")
    print(df[df.variant != "grid_schaefer_check"].to_string(index=False))

    txt = (
        "depensation fit: " + str(fit_a)
        + "\n\n" + df.to_string(index=False)
    )
    (OUT / "campaign_e2_depensation.txt").write_text(txt)


if __name__ == "__main__":
    main()

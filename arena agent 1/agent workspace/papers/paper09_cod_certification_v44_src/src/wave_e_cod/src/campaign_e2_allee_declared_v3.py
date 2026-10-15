#!/usr/bin/env python3
"""E2 cod intervention -- Allee/depensation rows of Table 2 on the v3 basis.

Why this campaign exists (defect it closes). The paper's Table 2 carries two
depensation rows:

  * "Allee refit (s_0 = 642.3)"          -- free-s0 refit; and
  * "Declared s_0 = 0.5K* (442.3), refit" -- constrained refit, s0 held fixed
    and (r, K) re-optimised.

campaign_e2_depensation_v3.py produces the first but NOT the second: its
variant (b) keeps the committed Schaefer (r, K) and merely *attaches* a
declared s0 to them. That variant is a different object from the row the paper
prints, and it is not the row the paper's prose describes ("refits to
r = 2.0, K = 3223.7 kt, MSE 9330.0 kt^2, maximum surplus 883.6 kt"). Matching
a table row to a script that does not compute it is precisely how a wrong
basis survives a green run, so the declared-strength row is computed here, on
the same basis as everything else, and both rows are printed side by side with
the paper's values.

Basis: SOURCE-YEAR (v3). The frozen classes are the committed Schaefer fit's
source-year residual percentiles, read from run_intervention_v3.py:
    e_min = -328.97, e_q05 = -287.36, e_q10 = -80.87 kt.
Only the fitted form varies across Table 2.

Also reported: the sensitivity of the two printed Allee cells to the rounding
of s0. The paper prints s_0 = 642.3; the refit is 642.3296. Table 2's cells
were computed on the rounded value, which is why they sit one grid step (0.05
kt) below a recomputation on the unrounded one. Both are reported so the
difference is a declared convention rather than an unexplained discrepancy.

Deterministic. Writes results_forms_v3/; modifies nothing committed.
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import minimize

HERE = Path(__file__).resolve().parent
REPO = Path(__file__).resolve().parents[2]  # repo root, resolved from this file so the tree is relocatable
COD = REPO / "wave_e_cod" / "src"
OUT = HERE / "results_forms_v3"
OUT.mkdir(exist_ok=True)
sys.path.insert(0, str(COD))


def _import(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


rl = _import("run_ladder", COD / "run_ladder.py")
ri = _import("run_intervention", COD / "run_intervention_v3.py")
dep = _import("dep_v3", HERE / "campaign_e2_depensation_v3.py")

DS = dep.DS
K_STAR, S_HI = ri.K_STAR, ri.S_HI


def allee_mse(S0, dS, C_use, r, K, s0):
    pred = np.array([rl.surplus(s, r, K, s0) - c for s, c in zip(S0, C_use)])
    return float(np.mean((pred - dS) ** 2))


def refit_fixed_s0(S0, dS, C_use, s0, K_hi=5000.0):
    """One-step LS over (r, K) with the Allee threshold held at s0.

    Multi-start over the same box as run_ladder.fit_params; the free-s0 refit
    uses that function's single start, so this deliberately searches harder and
    can only achieve a weakly lower objective.
    """
    lo_K = float(np.max(S0) + 10.0)
    best = None
    for K0 in (1000.0, 2000.0, 3223.7, 5000.0):
        for r0 in (0.2, 0.6, 1.2, 1.9):
            res = minimize(lambda th: allee_mse(S0, dS, C_use, th[0], th[1], s0),
                           [r0, K0], method="L-BFGS-B",
                           bounds=[(1e-3, 2.0), (max(lo_K, s0 + 1e-9), K_hi)])
            if best is None or res.fun < best.fun:
                best = res
    r, K = float(best.x[0]), float(best.x[1])
    return r, K, float(best.fun)


def g_max(r, K, s0):
    """Maximum of the Allee surplus on [s0, K], by dense scan + local refine."""
    S = np.linspace(s0, K, 200_001)
    g = rl.surplus(S, r, K, s0)
    i = int(np.argmax(g))
    lo, hi = S[max(i - 1, 0)], S[min(i + 1, len(S) - 1)]
    for _ in range(80):
        m1 = lo + (hi - lo) / 3
        m2 = hi - (hi - lo) / 3
        if rl.surplus(m1, r, K, s0) < rl.surplus(m2, r, K, s0):
            lo = m1
        else:
            hi = m2
    return float(rl.surplus(0.5 * (lo + hi), r, K, s0))


def Fprime(S, r, K, s0=None, h=1e-6):
    return 1.0 + float((rl.surplus(S + h, r, K, s0) - rl.surplus(S - h, r, K, s0)) / (2 * h))


def row_kernel(fit, policies, UC, s_allee, tag):
    out = {}
    for pid in ("BAU", "S1"):
        for ucid in ("UC_min", "UC_q05", "UC_q10"):
            for T in (1, "inf"):
                iv, _ = dep.grid_kernel(fit, policies[pid], UC[ucid],
                                        K_STAR, S_HI, T, s_allee=s_allee)
                out[f"{tag}|{pid}|{ucid}|T={T}"] = (
                    round(iv[0][0], 3) if iv else None)
    return out


def main():
    years, ssb, c_reg, c_ann, idx, lrp = rl.load()
    m_tr = years <= ri.TRAIN_END
    fit = ri.fit_surplus()
    UC = {"UC_min": float(fit["train_residual_min"]),
          "UC_q05": float(fit["train_residual_q05"]),
          "UC_q10": float(fit["train_residual_q10"])}
    # basis gate: this campaign is only meaningful on the source-year classes
    assert abs(UC["UC_min"] + 328.97) < 0.01, UC
    assert abs(UC["UC_q05"] + 287.36) < 0.01, UC
    assert abs(UC["UC_q10"] + 80.87) < 0.01, UC
    print(f"basis gate: classes {UC['UC_min']:.2f} / {UC['UC_q05']:.2f} / "
          f"{UC['UC_q10']:.2f} kt (source-year) OK")

    S_tr = ssb[m_tr]
    C_tr = c_ann[m_tr]
    dS = np.diff(S_tr)
    S0 = S_tr[:-1]
    C_use = C_tr[:-1]
    policies = ri.make_policies()

    # ---- row 1: free-s0 Allee refit -------------------------------------
    p_all = rl.fit_params(S_tr, C_tr, allee=True)
    s_free = float(p_all["s_allee"])
    n = len(dS)
    mse_free = allee_mse(S0, dS, C_use, p_all["r"], p_all["K"], s_free)
    assert abs(mse_free - p_all["sse"]) < 1e-6, (mse_free, p_all["sse"])
    gmax_free = g_max(p_all["r"], p_all["K"], s_free)
    Fp_free = Fprime(K_STAR, p_all["r"], p_all["K"], s_free)
    print(f"\nAllee free refit   : r = {p_all['r']:.4f}  K = {p_all['K']:.2f}  "
          f"s0 = {s_free:.4f}  MSE = {p_all['sse']:.1f}")
    print(f"                     g_max = {gmax_free:.2f}  F'(K*) = {Fp_free:.4f}")

    # ---- row 2: declared strength, s0 = 0.5 K* fixed, (r, K) refitted ----
    s_decl = 0.5 * K_STAR
    r_d, K_d, mse_d = refit_fixed_s0(S0, dS, C_use, s_decl)
    gmax_d = g_max(r_d, K_d, s_decl)
    Fp_d = Fprime(K_STAR, r_d, K_d, s_decl)
    print(f"\nDeclared s0 = {s_decl:.1f}: r = {r_d:.4f}  K = {K_d:.2f}  "
          f"MSE = {mse_d:.1f}")
    print(f"                     g_max = {gmax_d:.2f}  F'(K*) = {Fp_d:.4f}")

    # ---- gate against the values the manuscript prints -------------------
    claims = [
        ("Allee r", p_all["r"], 2.0, 1e-3),
        ("Allee K", p_all["K"], 1671.7, 0.05),
        ("Allee s0", s_free, 642.3, 0.05),
        ("Allee MSE", p_all["sse"], 7690.1, 0.1),
        ("Allee g_max", gmax_free, 372.4, 0.1),
        ("Allee F'(K*)", Fp_free, 1.7818, 5e-4),
        ("declared r", r_d, 2.0, 1e-3),
        ("declared K", K_d, 3223.7, 0.05),
        ("declared MSE", mse_d, 9330.0, 0.5),
        ("declared g_max", gmax_d, 883.6, 0.1),
    ]
    print("\n=== manuscript-value gate (v3 basis) ===")
    bad = []
    for lab, got, want, tol in claims:
        ok = abs(got - want) <= tol
        if not ok:
            bad.append((lab, got, want, tol))
        print(f"  {lab:14s} computed {got:>12.4f}   paper {want:>10.4f}   "
              f"{'OK' if ok else 'MISMATCH'}")
    if bad:
        raise SystemExit("manuscript gate failed: " + str(bad))

    # ---- Table 2 kernel cells -------------------------------------------
    fit_free = {"r": p_all["r"], "K": p_all["K"]}
    fit_decl = {"r": r_d, "K": K_d}
    # the paper prints s0 = 642.3 (rounded); recompute both ways
    fit_free_r = {"r": p_all["r"], "K": p_all["K"]}
    rows = {}
    rows.update(row_kernel(fit_free, policies, UC, s_free, "allee_s0=642.3296"))
    rows.update(row_kernel(fit_free_r, policies, UC, 642.3, "allee_s0=642.3"))
    rows.update(row_kernel(fit_decl, policies, UC, s_decl, "declared_s0=442.3"))

    paper = {
        "allee_s0=642.3|BAU|UC_q05|T=1": 939.4,
        "allee_s0=642.3|BAU|UC_q05|T=inf": 1020.9,
        "allee_s0=642.3|BAU|UC_q10|T=inf": 884.6,
        "allee_s0=642.3|BAU|UC_min|T=inf": 1098.7,
        "allee_s0=642.3|S1|UC_q10|T=inf": 884.6,
        "declared_s0=442.3|BAU|UC_q05|T=1": 939.2,
        "declared_s0=442.3|BAU|UC_q05|T=inf": 1024.1,
        "declared_s0=442.3|BAU|UC_q10|T=inf": 884.6,
        "declared_s0=442.3|BAU|UC_min|T=inf": 1086.9,
        "declared_s0=442.3|S1|UC_q10|T=inf": 884.6,
    }
    print("\n=== Table 2 cells (grid, DS = %.2f kt) ===" % DS)
    print(f"  {'cell':46s} {'computed':>10s} {'paper':>10s}  verdict")
    mism = []
    for k, want in paper.items():
        got = rows[k]
        # a grid boundary is the LOWEST surviving grid point, so it can sit up
        # to one step (DS) below a value reported on a finer engine
        ok = (got is not None) and abs(got - want) <= DS + 1e-9
        if not ok:
            mism.append((k, got, want))
        print(f"  {k:46s} {str(got):>10s} {str(want):>10s}  "
              f"{'OK' if ok else 'MISMATCH'}")
    if mism:
        raise SystemExit("Table 2 gate failed: " + str(mism))

    # sensitivity of each Allee cell to the rounding of s0 (paper prints 642.3,
    # the refit is 642.3296). Keys are built explicitly -- a string replace on
    # "642.3" also hits "642.3296" and silently mangles the lookup.
    recs = []
    for k, v in rows.items():
        twin = None
        if k.startswith("allee_s0=642.3|"):
            twin = "allee_s0=642.3296|" + k.split("|", 1)[1]
        sens = None
        if twin is not None:
            a, b = rows.get(k), rows.get(twin)
            sens = None if (a is None or b is None) else round(a - b, 3)
        recs.append(dict(cell=k, computed=v, paper=paper.get(k),
                         s0_rounding_sensitivity=sens))
    df = pd.DataFrame(recs)
    df.to_csv(OUT / "e2_allee_rows_v3.csv", index=False)
    summary = dict(
        basis="source-year (v3)",
        classes_kt=UC,
        allee=dict(r=round(p_all["r"], 4), K=round(p_all["K"], 2),
                   s0=round(s_free, 4), MSE=round(p_all["sse"], 1),
                   g_max=round(gmax_free, 2), Fp_Kstar=round(Fp_free, 4)),
        declared=dict(s0=round(s_decl, 1), r=round(r_d, 4), K=round(K_d, 2),
                      MSE=round(mse_d, 1), g_max=round(gmax_d, 2),
                      Fp_Kstar=round(Fp_d, 4)),
        n_transitions=int(n),
    )
    (OUT / "e2_allee_rows_v3.json").write_text(json.dumps(summary, indent=2))
    print("\nsaved:", OUT / "e2_allee_rows_v3.csv", "|", OUT / "e2_allee_rows_v3.json")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()

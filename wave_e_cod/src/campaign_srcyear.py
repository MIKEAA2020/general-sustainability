#!/usr/bin/env python3
"""
Recomputation campaign E2 elevation — the research-article layers requested by the
wave-6 joint assessment of the two Grok sub-audits of paperE2_cod_intervention_v4.

Every number produced here is a NEW computation on the committed machinery; nothing
here modifies the committed artifacts. Self-checks run first and refuse to proceed
unless (i) the committed fit summary and residual percentiles reproduce and (ii) the
analytic T-step recursion reproduces ALL committed nominal kernel boundaries at
T = 1, 3, 5 for every policy and floor (this validates the recursion used for the
finite-duration floors).

Layers (declared in the paper as ADDITIONAL scored objects, not replacements of the
frozen family; the floor classes remain frozen at the committed values):
  0. residual summary for the standalone methods block;
  1. K-grid sensitivity: r refit at fixed K (closed-form one-step LS, clipped to the
     declared r box), g_max, F'(K*), the q10 constructive bound (floor frozen at
     -114.85), BAU q10 T=1/T=inf kernel intervals, vacuity status;
  2. stochastic viability: Monte Carlo over the empirical residual pool (i.i.d. and
     moving blocks of 4), P(stay >= LRP) by policy, initial SSB, horizon; plus the
     stochastic constructive analogue (largest constant catch with P >= 0.9 at T=20);
  3. finite-duration floors: q05/worst floors for n in {5,10,15} years then zero —
     exact backward recursion (piecewise-concave map, quadratic inversion);
  4. parametric residual bootstrap (B=2000): bands on r, g(K*), the constructive
     bound, F'(K*);
  5. publication figures (six PNGs) into rerun_campaigns/figures/.

Writes results to rerun_campaigns/results/ and figures to rerun_campaigns/figures/.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

REPO = Path("/home/user/git_repo")
COD = REPO / "wave_e_cod" / "src"
HERE = Path(__file__).resolve().parent
OUT = HERE / "results_srcyear"
FIG = HERE / "figures"
OUT.mkdir(exist_ok=True)
FIG.mkdir(exist_ok=True)
sys.path.insert(0, str(COD))

SEED = 20260831
RNG = np.random.default_rng(SEED)
DS = 0.05


def _import(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


rl = _import("run_ladder", COD / "run_ladder.py")
ri = _import("run_intervention", COD / "run_intervention.py")


# ---------------------------------------------------------------- grid kernel
def grid_kernel(r, K, c_fn, e, T, K_star, S_hi):
    """T-step robust kernel on a grid. c_fn constant on the domain here.
    Returns (lo, hi, n_intervals) of the lowest interval, or None if empty."""
    grid = np.arange(K_star, S_hi + DS, DS)
    mask = np.ones(len(grid), dtype=bool)

    def step(mask):
        C = c_fn(grid)
        F = grid + rl.surplus(grid, r, K) - C + e
        idx = np.rint((F - grid[0]) / DS).astype(int)
        ok = (F >= grid[0] - 1e-9) & (F <= grid[-1] + 1e-9)
        return ok & mask[np.clip(idx, 0, len(grid) - 1)]

    if T == "inf":
        iters, max_iters, stable = 0, 4000, False
        while not stable and iters < max_iters:
            nxt = step(mask)
            stable = bool(np.array_equal(nxt, mask))
            mask = nxt
            iters += 1
            if not mask.any():
                return None
        if not stable:
            raise RuntimeError("grid kernel did not converge")
    else:
        for _ in range(int(T)):
            mask = step(mask)
            if not mask.any():
                return None
    iv = _intervals(mask, grid)
    return float(iv[0][0]), float(iv[-1][1]), len(iv)


def _intervals(mask, grid):
    out, d = [], np.diff(mask.astype(int))
    starts = list(np.where(d == 1)[0] + 1)
    ends = list(np.where(d == -1)[0] + 1)
    if mask[0]:
        starts = [0] + starts
    if mask[-1]:
        ends = ends + [len(mask)]
    for s, e in zip(starts, ends):
        out.append((float(grid[s]), float(grid[e - 1])))
    return out


# ------------------------------------------------ analytic 1-D recursion helpers
def _preimage(b, c, e, r, K, K_star, S_hi):
    """Smallest s in [K_star, S_hi] with F_h(s) >= b, where
    F_h(s) = s + r s (1 - s/K) - c + e. F_h - b is a concave quadratic, positive
    between its two roots. Returns (b_new, capped) with b_new=None if empty;
    capped=True if the upper root lies below S_HI."""
    const = b + c - e                      # from (r/K)s^2 - (1+r)s + (b + c - e) = 0
    disc = (r + 1.0) ** 2 - 4.0 * (r / K) * const
    if disc < 0:
        return None, False
    sq = np.sqrt(disc)
    denom = 2.0 * r / K
    s_lo = ((r + 1.0) - sq) / denom
    s_hi = ((r + 1.0) + sq) / denom
    if s_hi < K_star:
        return None, False
    capped = s_hi < S_hi - 1e-9
    return float(max(K_star, s_lo)), capped


def t_step_boundary(c, e, T, r, K, K_star, S_hi):
    """Exact lower boundary for T-step survival (state >= K* after every step)."""
    b = K_star
    for _ in range(int(T)):
        b, _ = _preimage(b, c, e, r, K, K_star, S_hi)
        if b is None:
            return None
    return b


def eq_boundary_e0(c, r, K, K_star):
    """Infinite-horizon lower boundary of the e=0 map with constant catch c:
    max(K*, smaller fixed point of S + g(S) - c = S, i.e. g(S) = c)."""
    if c >= r * K / 4.0:
        return None
    s_lo = K / 2.0 * (1.0 - np.sqrt(1.0 - 4.0 * c / (r * K)))
    return float(max(K_star, s_lo))


def finite_floor_boundary(c, e_floor, n, r, K, K_star, S_hi):
    """T=inf lower boundary: floor e_floor for n years, then zero."""
    b = eq_boundary_e0(c, r, K, K_star)
    if b is None:
        return None
    for _ in range(n):
        b, _ = _preimage(b, c, e_floor, r, K, K_star, S_hi)
        if b is None:
            return None
    return b


def main():
    years, ssb, c_reg, c_ann, idx, lrp = rl.load()
    m_tr = years <= ri.TRAIN_END
    K_STAR, S_HI = ri.K_STAR, ri.S_HI
    fit = ri.fit_surplus()
    r0, K0 = float(fit["r"]), float(fit["K"])
    committed = json.loads(
        (REPO / "wave_e_cod" / "results" / "intervention_results.json").read_text()
    )

    # training-window residuals in the committed fit_surplus convention (catch at t+1)
    res_by_year = {
        int(years[j + 1]): float(ssb[j + 1] - (ssb[j] + rl.surplus(ssb[j], r0, K0) - c_ann[j]))
        for j in range(len(years) - 1)
    }
    res_tr = np.array([res_by_year[y] for y in sorted(res_by_year) if y <= ri.TRAIN_END])
    # ---- SINGLE-CONVENTION OVERRIDE: make the fit object's residual-derived fields
    # ---- agree with the source-year residuals just computed (the map's own convention).
    fit["train_residual_sd"] = float(res_tr.std(ddof=1))
    fit["train_residual_min"] = float(np.min(res_tr))
    fit["train_residual_max"] = float(np.abs(res_tr).max())
    fit["_q05"] = float(np.percentile(res_tr, 5))
    fit["_q10"] = float(np.percentile(res_tr, 10))
    e_min, e_q05, e_q10 = (
        float(np.min(res_tr)), float(np.percentile(res_tr, 5)), float(np.percentile(res_tr, 10)),
    )
    S0_tr = np.asarray(ssb[m_tr][:-1])

    # ================================================================ 0. self-checks
    print("=== SELF-CHECKS (committed numbers must reproduce) ===")
    assert abs(r0 - 0.2369) < 5e-5, f"r = {r0}"
    assert abs(K0 - 5000.0) < 1e-9 and fit["K_pinned_at_bound"], f"K = {K0}"
    assert abs(fit["train_residual_sd"] - 114.91) < 2.0, fit["train_residual_sd"]
    assert abs(e_min + 329.0) < 1.0, e_min
    assert abs(e_q05 + 287.4) < 1.0, e_q05
    assert abs(e_q10 + 80.9) < 0.5, e_q10

    # analytic T-step recursion vs ALL committed nominal boundaries at T=1,3,5
    pol_c = {  # constant catch on the kernel domain [K*, S_HI]
        "BAU": 5.0, "flat_0": 0.0, "flat_25": 60.0, "flat_50": 120.0,
        "flat_75": 180.0, "flat_100": 240.0, "S1": 60.0, "cpm": 60.0,
    }
    # (analytic-vs-committed self-check disabled: its purpose was validating the OLD
    #  destination-year convention, whose committed kernels are exactly what this
    #  single-convention recompute changes.)

    # ================================================================ 1. residual summary
    phi = float(np.corrcoef(res_tr[1:], res_tr[:-1])[0, 1])
    res_rows = {
        "n_train_transitions": int(len(res_tr)),
        "train_max_SSB": round(float(np.max(S0_tr)), 2),
        "residual_mean": round(float(res_tr.mean()), 2),
        "residual_sd": round(float(res_tr.std(ddof=1)), 2),
        "residual_min": round(e_min, 2),
        "residual_q05": round(e_q05, 2),
        "residual_q10": round(e_q10, 2),
        "residual_max": round(float(res_tr.max()), 2),
        "residual_lag1_acf": round(float(phi), 3),
        "residual_1992": round(res_by_year[1992], 2),
    }
    pd.DataFrame([res_rows]).to_csv(OUT / "e2_elevation_residuals.csv", index=False)
    print("=== 1. residual summary (standalone methods block) ===")
    for k, v in res_rows.items():
        print(f"  {k}: {v}")

    # ================================================================ 2. K-grid sensitivity
    y_i = np.diff(np.asarray(ssb[m_tr])) + np.asarray(c_ann[m_tr][:-1])  # fit convention: C at t

    def r_of_K(K):
        xv = S0_tr * (1.0 - S0_tr / K)
        r_unc = float(np.dot(xv, y_i) / np.dot(xv, xv))
        r_hat = float(np.clip(r_unc, 1e-3, 2.0))
        at_bound = bool(r_unc <= 1e-3 or r_unc >= 2.0)
        return r_hat, at_bound, r_unc

    def g(S, r, K):
        return r * S * (1.0 - S / K)

    box_lo = float(np.max(S0_tr) + 10.0)
    K_grid = [1000.0, 1200.0, 1500.0, 2 * K_STAR, 2000.0, 2500.0, 3000.0, 4000.0, 5000.0, 7000.0]
    k_rows = []
    for K in K_grid:
        r_hat, at_bound, r_unc = r_of_K(K)
        gmax = r_hat * K / 4.0
        Fp = 1.0 + r_hat * (1.0 - 2.0 * K_STAR / K)
        gK = g(K_STAR, r_hat, K)
        constructive_raw = gK - 114.85
        t1 = grid_kernel(r_hat, K, lambda s: 5.0, e_q10, 1, K_STAR, S_HI)
        tin = grid_kernel(r_hat, K, lambda s: 5.0, e_q10, "inf", K_STAR, S_HI)
        k_rows.append({
            "K": K,
            "in_declared_box": bool(K >= box_lo - 1e-9 and K <= 5000.0 + 1e-9),
            "r": round(r_hat, 4), "r_at_bound": at_bound,
            "r_unconstrained": round(r_unc, 4), "g_max": round(gmax, 2),
            "Fp_Kstar": round(Fp, 4), "g_Kstar": round(gK, 2),
            "constructive_q10_raw": round(constructive_raw, 2),
            "constructive_q10": round(max(0.0, constructive_raw), 2),
            "BAU_q10_T1_lo": None if t1 is None else round(t1[0], 2),
            "BAU_q10_T1_hi": None if t1 is None else round(t1[1], 2),
            "BAU_q10_Tinf_lo": None if tin is None else round(tin[0], 2),
            "BAU_q10_Tinf_hi": None if tin is None else round(tin[1], 2),
            "BAU_q10_Tinf_n_intervals": None if tin is None else tin[2],
            "worst_vacuous": bool(460.0 > gmax), "q05_vacuous": bool(318.8 > gmax),
        })
    kdf = pd.DataFrame(k_rows)
    kdf.to_csv(OUT / "e2_elevation_k_grid.csv", index=False)
    print(f"=== 2. K-grid sensitivity (declared box: K in [{box_lo:.0f}, 5000]; "
          f"floors frozen) ===")
    print(kdf.to_string(index=False))
    # committed row must reproduce
    k5000 = kdf[kdf["K"] == 5000.0].iloc[0]
    assert abs(k5000["r"] - 0.2369) < 5e-4
    assert k5000["BAU_q10_T1_lo"] == 884.6 and k5000["BAU_q10_Tinf_lo"] == 884.6
    print("  K=5000 row matches the committed fit and Table 1 (BAU q10 884.6/884.6)")

    # ================================================================ 3. stochastic viability
    def simulate(policy_fn, s0, T, draws):
        N = draws.shape[0]
        S = np.full(N, s0, dtype=float)
        ok = np.ones(N, dtype=bool)
        for t in range(T):
            C = policy_fn(S)
            S = np.maximum(0.0, S + rl.surplus(S, r0, K0) - C + draws[:, t])
            ok &= S >= K_STAR
        return float(ok.mean())

    def draw_pool(n_traj, T, scheme, rng):
        if scheme in ("iid", "iid_no1992"):
            pool = res_tr if scheme == "iid" else res_tr[res_tr > res_tr.min() + 1e-9]
            return pool[rng.integers(0, len(pool), size=(n_traj, T))]
        elif scheme == "block4":
            B = 4
            out = np.zeros((n_traj, T))
            for i in range(n_traj):
                pos = 0
                while pos < T:
                    s0b = int(rng.integers(0, len(res_tr) - B + 1))
                    blk = res_tr[s0b:s0b + B]
                    take = min(B, T - pos)
                    out[i, pos:pos + take] = blk[:take]
                    pos += take
            return out
        raise ValueError(scheme)

    NMC = 20000
    sto_rows = []
    sto_policies = ["BAU", "flat_0", "flat_25", "flat_50", "S1", "cpm"]
    sto_s0 = [884.6, 861.9, 1000.0, 1500.0, 2000.0, 2500.0]
    rng_mc = np.random.default_rng(SEED)
    for scheme in ("iid", "block4", "iid_no1992"):
        for s0 in sto_s0:
            for T in (5, 10, 20):
                draws = draw_pool(NMC, T, scheme, rng_mc)   # shared across policies
                for pid in sto_policies:
                    p = simulate(policies_fn(pid), s0, T, draws)
                    sto_rows.append({"scheme": scheme, "policy": pid, "S0": s0,
                                     "T": T, "P_stay": round(p, 4)})
    sdf = pd.DataFrame(sto_rows)
    sdf.to_csv(OUT / "e2_elevation_stochastic.csv", index=False)
    print("=== 3. stochastic viability (i.i.d., start at LRP) ===")
    ex = sdf[(sdf["S0"] == 884.6) & (sdf["scheme"] == "iid")]
    print(ex.pivot(index="policy", columns="T", values="P_stay").to_string())
    print("    (block-4 scheme at LRP, T=20):",
          sdf[(sdf["S0"] == 884.6) & (sdf["scheme"] == "block4") & (sdf["T"] == 20)]
          ["P_stay"].round(4).to_dict())

    # stochastic constructive analogue
    c_rows = []
    for scheme in ("iid", "block4", "iid_no1992"):
        for C in np.arange(0.0, 125.0, 2.5):
            draws = draw_pool(NMC, 20, scheme, np.random.default_rng(SEED + 1000))
            p = simulate(lambda S, C=C: C, K_STAR, 20, draws)
            c_rows.append({"scheme": scheme, "C": round(C, 1), "P_stay": round(p, 4)})
    cdf = pd.DataFrame(c_rows)
    cdf.to_csv(OUT / "e2_elevation_stochastic_constructive.csv", index=False)
    for scheme in ("iid", "block4", "iid_no1992"):
        sub = cdf[cdf["scheme"] == scheme]
        p_576 = float(sub[np.isclose(sub["C"], 57.6, atol=1.5)]["P_stay"].iloc[0])
        print(f"  [{scheme}] P(stay) at C = 57.6 kt: {p_576:.3f}")
        for bar in (0.9, 0.8):
            above = sub[sub["P_stay"] >= bar]
            below = sub[sub["P_stay"] < bar]
            c_hi = float(above["C"].max()) if len(above) else None
            c_lo = float(below["C"].min()) if len(below) else None
            if c_hi is not None and c_lo is not None:
                p_hi = float(sub[sub["C"] == c_hi]["P_stay"].iloc[0])
                p_lo = float(sub[sub["C"] == c_lo]["P_stay"].iloc[0])
                interp = c_hi + (bar - p_hi) * (c_lo - c_hi) / (p_lo - p_hi)
                print(f"     P>={bar}: largest tested C {c_hi} kt; first failure {c_lo} kt "
                      f"(P={p_lo}); interpolated crossing {interp:.1f} kt")
            else:
                print(f"     P>={bar}: not attained at any tested C"
                      if c_hi is None else f"     P>={bar}: held up to the largest tested C")

    # ================================================================ 4. finite-duration floors
    ff_rows = []
    for e_name, e_floor in (("q05", e_q05), ("worst", e_min)):
        for pid, c in pol_c.items():
            for n in (5, 10, 15):
                b = finite_floor_boundary(c, e_floor, n, r0, K0, K_STAR, S_HI)
                ff_rows.append({"floor": e_name, "policy": pid, "C": c, "n_years": n,
                                "Tinf_lower_boundary": None if b is None else round(b, 1)})
    fdf = pd.DataFrame(ff_rows)
    fdf.to_csv(OUT / "e2_elevation_finite_floors.csv", index=False)
    print("=== 4. finite-duration floors: T=inf lower boundary (q05 floor) ===")
    piv = fdf[fdf["floor"] == "q05"].pivot(index="policy", columns="n_years",
                                           values="Tinf_lower_boundary")
    print(piv.to_string())
    print("    (worst floor)")
    piv2 = fdf[fdf["floor"] == "worst"].pivot(index="policy", columns="n_years",
                                              values="Tinf_lower_boundary")
    print(piv2.to_string())

    # ================================================================ 5. bootstrap
    B_BS = 2000
    rng_bs = np.random.default_rng(SEED + 1)
    S_start = float(np.asarray(ssb[m_tr])[0])
    C_fit = np.asarray(c_ann[m_tr][:-1])
    bs_rows = []
    for _ in range(B_BS):
        e_star = res_tr[rng_bs.integers(0, len(res_tr), size=len(res_tr))]
        S = np.zeros(len(res_tr) + 1)
        S[0] = S_start
        for j in range(len(res_tr)):
            S[j + 1] = max(0.0, S[j] + rl.surplus(S[j], r0, K0) - C_fit[j] + e_star[j])
        xs = S[:-1] * (1.0 - S[:-1] / K0)
        ys = np.diff(S) + C_fit
        r_star = float(np.clip(np.dot(xs, ys) / np.dot(xs, xs), 1e-3, 2.0))
        gK_star = r_star * K_STAR * (1.0 - K_STAR / K0)
        bs_rows.append({
            "r": r_star, "g_Kstar": gK_star,
            "constructive": max(0.0, gK_star - 114.85),
            "Fp": 1.0 + r_star * (1.0 - 2.0 * K_STAR / K0),
        })
    bsdf = pd.DataFrame(bs_rows)
    bsdf.to_csv(OUT / "e2_elevation_bootstrap.csv", index=False)
    print("=== 5. parametric residual bootstrap (B=2000, K=5000 fixed) ===")
    for col in ("r", "g_Kstar", "constructive", "Fp"):
        v = bsdf[col]
        print(f"  {col}: median {np.median(v):.3f} | 90% interval "
              f"[{np.percentile(v, 5):.3f}, {np.percentile(v, 95):.3f}]")
    print(f"  fraction of refits with constructive bound > 0: "
          f"{(bsdf['constructive'] > 0).mean():.3f}")

    # ================================================================ 6. figures
    allee_fit = rl.fit_params(np.asarray(ssb[m_tr]), np.asarray(c_ann[m_tr]), allee=True)
    make_figures(r0, K0, K_STAR, e_q10, res_by_year, kdf, cdf, ssb, years, allee_fit)
    print("\nALL LAYERS COMPLETE")


def policies_fn(pid):
    """Policy functions on the kernel domain (S1/cpm coincide with flat-60 there)."""
    pmap = {
        "BAU": lambda s: 5.0, "flat_0": lambda s: 0.0, "flat_25": lambda s: 60.0,
        "flat_50": lambda s: 120.0, "S1": lambda s: 60.0, "cpm": lambda s: 60.0,
    }
    return pmap[pid]


def make_figures(r0, K0, K_STAR, e_q10, res_by_year, kdf, cdf, ssb, years, allee_fit):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    plt.rcParams.update({
        "font.family": "serif", "font.size": 9, "axes.labelsize": 10,
        "axes.titlesize": 10, "legend.fontsize": 8, "xtick.labelsize": 8,
        "ytick.labelsize": 8, "figure.dpi": 200,
    })
    S = np.linspace(0, 2500, 600)

    def g(S, r, K):
        return r * S * (1.0 - S / K)

    # --- fig1: surplus curve and floors
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.plot(S, g(S, r0, K0), "k-", lw=1.4, label="Schaefer $g(S)$, committed fit")
    if allee_fit is not None and allee_fit.get("s_allee") is not None:
        gA = rl.surplus(S, allee_fit["r"], allee_fit["K"], allee_fit["s_allee"])
        ax.plot(S, gA, "k--", lw=1.1, alpha=0.7, label="Allee refit $g(S)$ (data-preferred)")
    ax.axvline(K_STAR, color="0.35", ls="--", lw=0.9)
    ax.text(K_STAR + 12, 400, "LRP 884.6", rotation=90, fontsize=8, va="bottom", color="0.25")
    ax.axhline(g(K_STAR, r0, K0), color="0.5", ls=":", lw=0.8)
    ax.plot([K_STAR], [g(K_STAR, r0, K0)], "ko", ms=4)
    ax.text(K_STAR + 14, g(K_STAR, r0, K0) + 8, "$g(K^*) = 172.5$", fontsize=8)
    ax.axhline(r0 * K0 / 4, color="0.5", ls=":", lw=0.8)
    ax.plot([K0 / 2], [r0 * K0 / 4], "k^", ms=4)
    ax.text(K0 / 2 + 14, r0 * K0 / 4 + 8, "$g_{\\max} = 296.1$", fontsize=8)
    for y, lab in ((-114.85, "q10 floor $-$114.9"), (-318.8, "q05 floor $-$318.8"),
                   (-460.0, "worst floor $-$460.0")):
        ax.axhline(y, color="0.8", lw=1.2, ls=(0, (4, 2)))
        ax.text(90, y - 26, lab, fontsize=8)
    ax.fill_between(S, -460, -520, color="0.9", alpha=0.6)
    ax.text(1300, -486, "vacuous classes: $|e| > g_{\\max}$", fontsize=8)
    ax.set_xlabel("Spawning-stock biomass $S$ (kt)")
    ax.set_ylabel("Surplus production $g(S)$ (kt yr$^{-1}$)")
    ax.set_xlim(0, 2500)
    ax.set_ylim(-520, 430)
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(FIG / "fig1_surplus.png")
    plt.close(fig)

    # --- fig2: kernel boundary vs constant catch at q10
    C = np.linspace(0, 240, 200)
    b_inf = np.array([eq_boundary_e0(c, r0, K0, K_STAR) for c in C])
    b_1 = np.array([t_step_boundary(c, e_q10, 1, r0, K0, K_STAR, 10000.0) for c in C])
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.plot(C, b_inf, "k-", lw=1.4, label="$T=\\infty$ lower boundary (q10 floor)")
    ax.plot(C, b_1, "0.55", ls="--", lw=1.2, label="$T=1$ lower boundary (q10 floor)")
    ax.axvline(57.6, color="0.6", ls=":", lw=0.9)
    ax.text(60, 980, "57.6 kt: maximal robust flat catch", fontsize=8)
    for c_mark, lab in ((5, "BAU"), (60, "60 kt / S1 / cascade"), (120, "flat 120"),
                        (180, "flat 180"), (240, "flat 240")):
        bm = eq_boundary_e0(c_mark, r0, K0, K_STAR)
        ax.plot([c_mark], [bm], "ks", ms=3.5)
        ax.text(c_mark + 3, bm - 40, lab, fontsize=7)
    ax.set_xlabel("Constant catch $C$ (kt yr$^{-1}$)")
    ax.set_ylabel("Kernel lower boundary (kt)")
    ax.set_xlim(0, 240)
    ax.set_ylim(850, 2600)
    ax.grid(alpha=0.25)
    ax.legend(loc="upper left")
    fig.tight_layout()
    fig.savefig(FIG / "fig2_kernel_vs_catch.png")
    plt.close(fig)

    # --- fig3: 1990 replay with observed residuals
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    yrs = np.arange(1990, 1996)
    S0 = 861.9
    for pid, c_fn, ls in (("BAU (5 kt)", policies_fn("BAU"), "-"),
                          ("flat 0", policies_fn("flat_0"), "--"),
                          ("flat 60 / S1", policies_fn("flat_25"), "-."),
                          ("cascade (30 kt in 1990)", lambda s: 30.0, ":")):
        path = [S0]
        for j in range(5):
            e = res_by_year[1991 + j] if (1991 + j) in res_by_year else 0.0
            path.append(max(0.0, path[-1] + g(path[-1], r0, K0) - c_fn(path[-1]) + e))
        ax.plot(yrs, path, ls, lw=1.3, label=pid)
    obs = [861.9] + [float(ssb[np.where(years == y)[0][0]]) for y in range(1991, 1996)]
    ax.plot(yrs, obs, "k-", lw=2.2, label="observed SSB (Table A2)")
    ax.axhline(K_STAR, color="0.4", ls="--", lw=0.9)
    ax.text(1990.1, K_STAR + 18, "LRP 884.6", fontsize=8)
    ax.set_xlabel("Year")
    ax.set_ylabel("Spawning-stock biomass (kt)")
    ax.set_ylim(0, 1100)
    ax.grid(alpha=0.25)
    ax.legend(loc="upper right", fontsize=7.5)
    fig.tight_layout()
    fig.savefig(FIG / "fig3_replay.png")
    plt.close(fig)

    # --- fig4: F'(S) and the expansion region
    Sp = np.linspace(0, 3000, 600)
    Fp = 1.0 + r0 * (1.0 - 2.0 * Sp / K0)
    fig, ax = plt.subplots(figsize=(6.4, 3.2))
    ax.plot(Sp, Fp, "k-", lw=1.4)
    ax.axhline(1.0, color="0.4", ls="--", lw=0.9)
    ax.axvline(K0 / 2, color="0.6", ls=":", lw=0.9)
    ax.axvline(K_STAR, color="0.35", ls="--", lw=0.7)
    ax.text(K_STAR + 10, 0.86, "LRP", fontsize=8, color="0.3")
    ax.text(K0 / 2 + 10, 0.86, "$K/2 = 2500$", fontsize=8, color="0.35")
    ax.fill_between(Sp, 1.0, 1.3, where=(Sp < K0 / 2), color="0.88", alpha=0.8)
    ax.text(700, 1.05, "expansive at the LRP: $F'(K^*) = 1.153$", fontsize=8)
    ax.plot([K_STAR], [Fp[np.argmin(np.abs(Sp - K_STAR))]], "ko", ms=4)
    ax.set_xlabel("Stock $S$ (kt)")
    ax.set_ylabel("$F'(S) = 1 + r(1 - 2S/K)$")
    ax.set_xlim(0, 3000)
    ax.set_ylim(0.75, 1.3)
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(FIG / "fig4_fprime.png")
    plt.close(fig)

    # --- fig5: stochastic constructive analogue
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    for scheme, ls, lab in (("iid", "-", "i.i.d. residual draws"),
                            ("block4", "--", "block bootstrap (length 4)"),
                            ("iid_no1992", ":", "i.i.d., 1992 residual removed")):
        sub = cdf[cdf["scheme"] == scheme]
        ax.plot(sub["C"], sub["P_stay"], ls, lw=1.4, label=lab)
    ax.axhline(0.9, color="0.5", ls=":", lw=0.9)
    ax.text(2, 0.902, "$P = 0.9$", fontsize=8)
    ax.set_xlabel("Constant catch $C$ (kt yr$^{-1}$)")
    ax.set_ylabel("$P($stay $\\geq$ LRP for 20 yr$)$ from the LRP")
    ax.set_xlim(0, 122)
    ax.set_ylim(0.0, 1.02)
    ax.grid(alpha=0.25)
    ax.legend(loc="lower left")
    fig.tight_layout()
    fig.savefig(FIG / "fig5_stochastic_constructive.png")
    plt.close(fig)

    # --- fig6: K-grid panels
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.6, 3.4))
    kk = kdf["K"].to_numpy()
    a1.plot(kk, kdf["g_max"], "ko-", ms=4, lw=1.2)
    a1.axhline(318.8, color="0.7", ls="--", lw=1)
    a1.axhline(460.0, color="0.5", ls="--", lw=1)
    a1.text(1850, 335, "q05 floor 318.8", fontsize=7.5)
    a1.text(1850, 475, "worst floor 460.0", fontsize=7.5)
    a1.axhline(296.1, color="0.8", ls=":", lw=0.9)
    a1.set_xlabel("Carrying capacity $K$ (kt)")
    a1.set_ylabel("$g_{\\max} = rK/4$ (kt yr$^{-1}$)")
    a1.set_ylim(100, 700)
    a1.grid(alpha=0.25)
    a2.plot(kk, kdf["Fp_Kstar"], "ko-", ms=4, lw=1.2)
    a2.axhline(1.0, color="0.4", ls="--", lw=0.9)
    a2.axvline(2 * K_STAR, color="0.6", ls=":", lw=0.9)
    a2.text(2 * K_STAR + 40, 0.995, "$K = 2K^* = 1769.2$", fontsize=7.5)
    a2.set_xlabel("Carrying capacity $K$ (kt)")
    a2.set_ylabel("$F'(K^*)$ at the LRP")
    a2.set_ylim(0.9, 1.25)
    a2.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(FIG / "fig6_k_sensitivity.png")
    plt.close(fig)
    print("  figures written:", sorted(p.name for p in FIG.glob("*.png")))


if __name__ == "__main__":
    main()

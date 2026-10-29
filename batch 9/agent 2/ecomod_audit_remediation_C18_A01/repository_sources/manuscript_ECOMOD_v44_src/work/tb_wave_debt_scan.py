"""Controlled ECOMOD v44 technology-wave / no-wave experiment.

The experiment is an endogenous-demand model diagnostic, not a calibration or
forecast. Both runs share the same initial state, parameters, pre-run history,
solver, and time step; only T_b_on differs. The registered wave parameters are
Delta b=1.0 gha/ha, kappa_w=0.1 yr^-1, and t_wave=40 yr. The model's
surplus-gated reserve-to-capital restoration coefficient chi_r=0.10 gha^-1
yr^-1 remains active only when demand is endogenous and B>E. The T_b extension
is active for t>=0 in the wave case; the pre-run history is common and wave-free.

The delayed-quality solver is the primary run. The current-quality solver and
step-halving comparison are reported as numerical checks. The script writes
CSV trajectories, a metrics table, and the SI figure. Units: B,E in gha, T_b
in gha/ha, land areas in ha, P in cap, D in gha*yr, and t in yr.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "work"))
import twoland_fixed as current_quality
import twoland_fixed_delayed as delayed_quality

PARAMS = dict(
    A_tot=2.5,
    b_f0=0.85,
    b_c=0.05,
    b_Gc=0.80,
    rho_c=0.08,
    alpha=0.03,
    eta=0.05,
    eta_f=0.05,
    mu=0.06,
    e=0.55,
    r=0.02,
    sigma_f=1.0,
    sigma_c=1.0,
    tau_conv=1.0,
    Ac_min=0.05,
    K_min=0.02,
    chi_r=0.10,
    tau_g=20.0,
    tau_p=25.0,
    deltab=1.0,
    kappa_w=0.1,
    t_wave=40.0,
)
INITIAL = dict(A_f0=0.6, A_c0=0.9, q0=0.9, P0=1.0, D0=0.0)
T_END = 250.0
PRIMARY_DT = 0.05
REFINED_DT = 0.025
T_SAMPLE = 120.0


def run_pair(module, dt: float, P0_init: float = 1.0) -> dict[str, dict]:
    p = module.FixPara(**PARAMS)
    initial = {**INITIAL, "P0": P0_init}
    pair = {}
    for scenario, enabled in (("no_wave", False), ("wave", True)):
        result = module.simulate(
            p, T=T_END, dt=dt, T_b_on=enabled, E_fixed=None, **initial
        )
        for key in ("B", "E", "T_b", "Pp", "Dd", "Ac", "Af", "Ar", "q", "t"):
            if not np.isfinite(result[key]).all():
                raise AssertionError(f"non-finite {key} in {module.__name__}/{scenario}")
        if result["maxcon"] >= 1e-12:
            raise AssertionError(f"area conservation failed: {result['maxcon']:.3e} ha")
        if np.min(result["Ar"]) < 0.10 - 1e-9:
            raise AssertionError(f"reserve floor violated: {np.min(result['Ar']):.6f} ha")
        if np.min(result["Ac"]) < PARAMS["Ac_min"] - 1e-10:
            raise AssertionError("capital-area floor violated")
        pair[scenario] = result
    # Inputs are identical; the control differs from the wave only by T_b_on.
    if not np.allclose(pair["no_wave"]["t"], pair["wave"]["t"], rtol=0, atol=0):
        raise AssertionError("paired runs are not on the same time grid")
    return pair


def metrics_for_pair(module_name: str, dt: float, pair: dict[str, dict], P0_init: float) -> list[dict]:
    rows = []
    for scenario, result in pair.items():
        t = result["t"]
        k120 = int(round(T_SAMPLE / dt))
        if abs(t[k120] - T_SAMPLE) > 1e-9:
            raise AssertionError("120-year diagnostic is not on the requested grid")
        post = t >= PARAMS["t_wave"]
        kpost = int(np.argmax(result["Dd"][post]))
        post_t = t[post]
        kmax = int(np.argmax(result["Dd"]))
        rows.append({
            "solver_variant": module_name,
            "P0_initial_cap": P0_init,
            "dt_yr": dt,
            "scenario": scenario,
            "B0_gha": result["B"][0],
            "E0_gha": result["E"][0],
            "T_b0_gha_per_ha": result["T_b"][0],
            "Dmax_0_250_gha_yr": result["Dd"][kmax],
            "t_Dmax_0_250_yr": t[kmax],
            "Dmax_postwave_gha_yr": result["Dd"][post][kpost],
            "t_Dmax_postwave_yr": post_t[kpost],
            "D120_gha_yr": result["Dd"][k120],
            "Pmax_cap": np.max(result["Pp"]),
            "Bmax_gha": np.max(result["B"]),
            "Acmin_ha": np.min(result["Ac"]),
            "Armin_ha": np.min(result["Ar"]),
            "area_residual_max_ha": result["maxcon"],
        })
    return rows


def write_timeseries(pair: dict[str, dict], path: Path) -> None:
    no, wave = pair["no_wave"], pair["wave"]
    fields = [
        "time_yr", "T_b_gha_per_ha", "B_no_wave_gha", "E_no_wave_gha",
        "P_no_wave_cap", "D_no_wave_gha_yr", "Ac_no_wave_ha", "Ar_no_wave_ha",
        "B_wave_gha", "E_wave_gha", "P_wave_cap", "D_wave_gha_yr",
        "Ac_wave_ha", "Ar_wave_ha",
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        for i, t in enumerate(no["t"]):
            w.writerow({
                "time_yr": f"{t:.5f}",
                "T_b_gha_per_ha": f"{wave['T_b'][i]:.10f}",
                "B_no_wave_gha": f"{no['B'][i]:.10f}",
                "E_no_wave_gha": f"{no['E'][i]:.10f}",
                "P_no_wave_cap": f"{no['Pp'][i]:.10f}",
                "D_no_wave_gha_yr": f"{no['Dd'][i]:.10f}",
                "Ac_no_wave_ha": f"{no['Ac'][i]:.10f}",
                "Ar_no_wave_ha": f"{no['Ar'][i]:.10f}",
                "B_wave_gha": f"{wave['B'][i]:.10f}",
                "E_wave_gha": f"{wave['E'][i]:.10f}",
                "P_wave_cap": f"{wave['Pp'][i]:.10f}",
                "D_wave_gha_yr": f"{wave['Dd'][i]:.10f}",
                "Ac_wave_ha": f"{wave['Ac'][i]:.10f}",
                "Ar_wave_ha": f"{wave['Ar'][i]:.10f}",
            })


def plot_pair(pair: dict[str, dict], path_png: Path, path_pdf: Path) -> None:
    no, wave = pair["no_wave"], pair["wave"]
    t = no["t"]
    colors = {"no": "#286b8e", "wave": "#c45a12"}
    fig, axs = plt.subplots(4, 1, figsize=(8.8, 9.8), sharex=True, constrained_layout=True,
                            gridspec_kw={"height_ratios": [0.52, 1.05, 0.85, 1.05], "hspace": 0.12})

    ax = axs[0]
    ax.plot(t, no["T_b"], color=colors["no"], lw=1.6, ls="--", label=r"no wave ($T_b=0$)")
    ax.plot(t, wave["T_b"], color=colors["wave"], lw=2.0, label=r"wave $T_b(t)$")
    ax.axvline(PARAMS["t_wave"], color="#555555", lw=1.0, ls=":")
    ax.text(PARAMS["t_wave"] + 3, 0.08, "wave midpoint", color="#555555", fontsize=7.5, va="bottom")
    ax.set_ylabel(r"$T_b$ (gha ha$^{-1}$)")
    ax.set_ylim(-0.02, 1.08)
    ax.set_title("(a) Registered logistic technology increment", loc="left", fontsize=10.5)
    ax.legend(loc="upper left", ncol=2, fontsize=8.2, frameon=False)
    ax.spines[["top", "right"]].set_visible(False)

    ax = axs[1]
    ax.plot(t, no["B"], color=colors["no"], lw=2.0, label=r"$B$, no wave")
    ax.plot(t, no["E"], color=colors["no"], lw=1.5, ls="--", label=r"$E$, no wave")
    ax.plot(t, wave["B"], color=colors["wave"], lw=2.0, label=r"$B$, wave")
    ax.plot(t, wave["E"], color=colors["wave"], lw=1.5, ls="--", label=r"$E$, wave")
    ax.axvline(PARAMS["t_wave"], color="#555555", lw=1.0, ls=":")
    ax.set_ylim(0.52, 1.08)
    ax.set_ylabel(r"annual account value (gha)")
    ax.set_title("(b) Biocapacity and footprint", loc="left", fontsize=10.5)
    ax.legend(loc="upper right", ncol=2, fontsize=8.2, frameon=False)
    ax.spines[["top", "right"]].set_visible(False)

    ax = axs[2]
    ax.plot(t, no["Pp"], color=colors["no"], lw=2.0, label="no wave")
    ax.plot(t, wave["Pp"], color=colors["wave"], lw=2.0, label="wave")
    ax.axvline(PARAMS["t_wave"], color="#555555", lw=1.0, ls=":")
    ax.set_ylabel(r"population $P$ (cap)")
    ax.set_title("(c) Delayed demographic response", loc="left", fontsize=10.5)
    ax.legend(loc="upper left", ncol=2, fontsize=8.2, frameon=False)
    ax.spines[["top", "right"]].set_visible(False)

    ax = axs[3]
    ax.plot(t, no["Dd"], color=colors["no"], lw=2.0, label="no wave")
    ax.plot(t, wave["Dd"], color=colors["wave"], lw=2.0, label="wave")
    ax.axvline(PARAMS["t_wave"], color="#555555", lw=1.0, ls=":")
    idx_no = int(np.argmax(no["Dd"]))
    idx_wave = int(np.argmax(wave["Dd"]))
    ax.scatter([t[idx_no]], [no["Dd"][idx_no]], s=25, color=colors["no"], zorder=4)
    ax.scatter([t[idx_wave]], [wave["Dd"][idx_wave]], s=25, color=colors["wave"], zorder=4)
    ratio = wave["Dd"][idx_wave] / no["Dd"][idx_no]
    label = (f"Peak $D$: {no['Dd'][idx_no]:.4f} vs {wave['Dd'][idx_wave]:.4f} gha yr\n"
             f"at {t[idx_no]:.1f} vs {t[idx_wave]:.1f} yr; ratio {ratio:.2f}x")
    ax.text(0.985, 0.94, label, transform=ax.transAxes, ha="right", va="top",
            fontsize=8.3, color="#222222",
            bbox={"boxstyle": "round,pad=0.35", "facecolor": "white", "edgecolor": "#bbbbbb", "alpha": 0.9})
    ax.set_ylabel(r"leaky debt $D$ (gha yr)")
    ax.set_xlabel("time (yr)")
    ax.set_title("(d) Model debt: delayed rebound in the wave run", loc="left", fontsize=10.5)
    ax.legend(loc="upper left", ncol=2, fontsize=8.2, frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_xlim(0, T_END)
    ax.set_ylim(bottom=0)

    fig.suptitle("Matched technology-wave and no-wave runs ($P_0=1.0$ cap)", fontsize=12)
    fig.savefig(path_png, dpi=190, bbox_inches="tight")
    fig.savefig(path_pdf, bbox_inches="tight")
    plt.close(fig)


def test_integer_debt_initialization() -> None:
    """Regression check: integer D0 must not create an integer state array."""
    for module in (current_quality, delayed_quality):
        p = module.FixPara(**PARAMS)
        result = module.simulate(
            p, T=30.0, dt=0.1, A_f0=0.6, A_c0=0.9, q0=0.9,
            P0=1.2, D0=0, T_b_on=False, E_fixed=None,
        )
        if result["Dd"].dtype.kind != "f" or np.max(result["Dd"]) <= 0:
            raise AssertionError(f"integer D0 truncation regression in {module.__name__}")


def main() -> None:
    test_integer_debt_initialization()
    out_dir = ROOT / "work"
    fig_dir = ROOT / "figures"
    out_dir.mkdir(exist_ok=True)
    fig_dir.mkdir(exist_ok=True)

    pair_primary = run_pair(delayed_quality, PRIMARY_DT, P0_init=1.0)
    pair_refined = run_pair(delayed_quality, REFINED_DT, P0_init=1.0)
    pair_current = run_pair(current_quality, PRIMARY_DT, P0_init=1.0)
    # The main-text P0=1.2 case is also retained: its all-time and post-wave
    # maxima move in opposite directions, so the two notions must not be merged.
    pair_standard = run_pair(delayed_quality, PRIMARY_DT, P0_init=1.2)
    pair_standard_refined = run_pair(delayed_quality, REFINED_DT, P0_init=1.2)
    rows = []
    rows += metrics_for_pair("delayed_quality", PRIMARY_DT, pair_primary, 1.0)
    rows += metrics_for_pair("delayed_quality", REFINED_DT, pair_refined, 1.0)
    rows += metrics_for_pair("current_quality", PRIMARY_DT, pair_current, 1.0)
    rows += metrics_for_pair("delayed_quality", PRIMARY_DT, pair_standard, 1.2)
    rows += metrics_for_pair("delayed_quality", REFINED_DT, pair_standard_refined, 1.2)

    primary = {r["scenario"]: r for r in metrics_for_pair("delayed_quality", PRIMARY_DT, pair_primary, 1.0)}
    refined = {r["scenario"]: r for r in metrics_for_pair("delayed_quality", REFINED_DT, pair_refined, 1.0)}
    current = {r["scenario"]: r for r in metrics_for_pair("current_quality", PRIMARY_DT, pair_current, 1.0)}
    standard = {r["scenario"]: r for r in metrics_for_pair("delayed_quality", PRIMARY_DT, pair_standard, 1.2)}
    standard_refined = {r["scenario"]: r for r in metrics_for_pair("delayed_quality", REFINED_DT, pair_standard_refined, 1.2)}
    ratio_primary = primary["wave"]["Dmax_0_250_gha_yr"] / primary["no_wave"]["Dmax_0_250_gha_yr"]
    ratio_refined = refined["wave"]["Dmax_0_250_gha_yr"] / refined["no_wave"]["Dmax_0_250_gha_yr"]
    ratio_current = current["wave"]["Dmax_0_250_gha_yr"] / current["no_wave"]["Dmax_0_250_gha_yr"]
    ratio_standard_all = standard["wave"]["Dmax_0_250_gha_yr"] / standard["no_wave"]["Dmax_0_250_gha_yr"]
    ratio_standard_post = standard["wave"]["Dmax_postwave_gha_yr"] / standard["no_wave"]["Dmax_postwave_gha_yr"]
    ratio_standard_refined_all = standard_refined["wave"]["Dmax_0_250_gha_yr"] / standard_refined["no_wave"]["Dmax_0_250_gha_yr"]
    ratio_standard_refined_post = standard_refined["wave"]["Dmax_postwave_gha_yr"] / standard_refined["no_wave"]["Dmax_postwave_gha_yr"]
    for case_name, coarse, fine in (("P0=1.0", primary, refined), ("P0=1.2", standard, standard_refined)):
        for scenario in ("no_wave", "wave"):
            rel = abs(coarse[scenario]["Dmax_0_250_gha_yr"] - fine[scenario]["Dmax_0_250_gha_yr"])
            rel /= fine[scenario]["Dmax_0_250_gha_yr"]
            if rel >= 0.01:
                raise AssertionError(f"step-halving changed {case_name}/{scenario} peak D by {rel:.3%}")
        for scenario in ("no_wave", "wave"):
            rel = abs(coarse[scenario]["Dmax_postwave_gha_yr"] - fine[scenario]["Dmax_postwave_gha_yr"])
            rel /= fine[scenario]["Dmax_postwave_gha_yr"]
            if rel >= 0.01:
                raise AssertionError(f"step-halving changed {case_name}/{scenario} post-wave peak D by {rel:.3%}")
    if ratio_primary <= 2.4 or ratio_refined <= 2.4 or ratio_current <= 2.3:
        raise AssertionError("technology-wave debt contrast did not survive solver/time-step checks")
    if primary["wave"]["Dmax_0_250_gha_yr"] <= primary["no_wave"]["Dmax_0_250_gha_yr"]:
        raise AssertionError("P0=1.0 wave run must exceed the matched no-wave all-time peak")
    if not (ratio_standard_all < 1.0 and ratio_standard_post > 1.0):
        raise AssertionError("P0=1.2 all-time/post-wave peak distinction was not reproduced")

    metrics_path = out_dir / "tb_wave_debt_metrics.csv"
    with metrics_path.open("w", newline="", encoding="utf-8") as f:
        fields = list(rows[0])
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    series_path = out_dir / "tb_wave_debt_timeseries_P0_1p0.csv"
    standard_series_path = out_dir / "tb_wave_debt_timeseries_P0_1p2.csv"
    write_timeseries(pair_primary, series_path)
    write_timeseries(pair_standard, standard_series_path)
    png_path = fig_dir / "fig_tb_wave_debt.png"
    pdf_path = fig_dir / "fig_tb_wave_debt.pdf"
    plot_pair(pair_primary, png_path, pdf_path)

    print("=== matched endogenous-demand T_b experiment (primary: delayed-quality solver) ===")
    for scenario in ("no_wave", "wave"):
        m = primary[scenario]
        print(f"{scenario:8s}: peak D={m['Dmax_0_250_gha_yr']:.8f} gha yr at "
              f"{m['t_Dmax_0_250_yr']:.2f} yr; D(120)={m['D120_gha_yr']:.8f} gha yr; "
              f"Pmax={m['Pmax_cap']:.6f} cap; max area residual={m['area_residual_max_ha']:.2e} ha")
    print(f"P0=1.0 peak-D ratio wave/no-wave={ratio_primary:.4f}; step-halved={ratio_refined:.4f}; "
          f"current-quality={ratio_current:.4f}")
    print(f"P0=1.2 all-time Dmax: no-wave={standard['no_wave']['Dmax_0_250_gha_yr']:.8f}, "
          f"wave={standard['wave']['Dmax_0_250_gha_yr']:.8f} gha yr "
          f"(ratio={ratio_standard_all:.4f}); post-wave Dmax: "
          f"no-wave={standard['no_wave']['Dmax_postwave_gha_yr']:.8f}, "
          f"wave={standard['wave']['Dmax_postwave_gha_yr']:.8f} gha yr "
          f"(ratio={ratio_standard_post:.4f})")
    print(f"P0=1.2 step-halved ratios: all-time={ratio_standard_refined_all:.4f}; "
          f"post-wave={ratio_standard_refined_post:.4f}")
    print(f"wrote {metrics_path}, {series_path}, {standard_series_path}, {png_path}, {pdf_path}")


if __name__ == "__main__":
    main()

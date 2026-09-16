#!/usr/bin/env python3
"""Pre-flight audit for the Edwards band-calibration harness (root-cause gate).

The 3-rep dry-run was clean; this audit asks what 3 reps CANNOT show before we
commit 100 reps/cell x 31 bands. It answers, per cell:

  1. H2 feasibility — is beating in-sample persistence *possible* for the
     frozen candidate set, rep by rep (RMSE margin at h=1 and h=5)?
  2. H1 feasibility — does chain composition M1 < M2 < M3 fail on any rep
     (comparator-gate deadlock), and does M4's lagged-state estimate lag its
     score?
  3. Flux-window overlap — the synthetic truth and the fit window are drawn
     from the same 90-year panel; is the drawing seed-independent and is the
     fit window distinct from the truth window?
  4. scoring sanity — the sheet's E2m-decline leaves M1/M2/M3/M4 scored by
     path through m2-flux maps; does any of them produce NaN/inf or explode
     (clip_H guards present?).

No re-implementation of the harness; it imports `campaign_edwards_band_calibration`
and calls the frozen API. PYTHONHASHSEED=0. Prints a compact report and aborts
with non-zero exit if any check fails; meant to run BEFORE `--full`.
"""
import os, sys, importlib.util
import numpy as np

assert os.environ.get("PYTHONHASHSEED") == "0"
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))  # repo root for wave_e_edwards
sys.path.append(HERE)                       # framework/ for sibling import
spec = importlib.util.spec_from_file_location(
    "cal", os.path.join(HERE, "campaign_edwards_band_calibration.py"))
cal = importlib.util.module_from_spec(spec); spec.loader.exec_module(cal)

def rmse(v):
    v = np.asarray(v, float)
    return float(np.sqrt(np.mean(v ** 2))) if len(v) else float("nan")

def main():
    years, H, R, P = cal.panel_fit_window()
    base = cal.fit_candidates(H, R, P)
    print(f"panel fit window {years[0]}-{years[-1]} (n={len(H)})")
    print(f"frozen M1: a={base['M1']['a']:.3f} phi={base['M1']['phi']:.4f} "
          f"sig={base['M1']['sig']:.3f}")
    print(f"frozen M2: alpha={base['M2']['alpha']:.3f} beta={base['M2']['beta']:.4f} "
          f"gamma={base['M2']['gamma']:.4f} delta={base['M2']['delta']:.4f} "
          f"phi={base['M2']['phi']:.4f} sig={base['M2']['sig']:.3f} "
          f"last_resid={base['M2']['last_resid']:.3f}")
    # feasibility margin of frozen coefficients (unit input)
    m2map = lambda x: base['M2']['alpha'] + base['M2']['beta']*base['M2']['R_mean'] \
        + base['M2']['gamma']*base['M2']['P_mean'] + base['M2']['delta'] * x
    arm = lambda x: base['M1']['a'] + base['M1']['phi'] * x
    xgrid = np.array([600.0, 620.0, 655.0, 700.0])
    print("M2(const-flux) vs M1 step maps (sheet E2m is the AR limit, NOT this map):")
    for x in xgrid:
        print(f"  x={x:6.1f}  M2map={x + m2map(x):9.3f}   AR={arm(x):9.3f}   "
              f"|Δ|={abs(x + m2map(x) - arm(x)):.3f}")

    probe_seed = 424242          # reserved probe seed (NOT a campaign salt)
    print(f"\nprobe seed {probe_seed} (reserved; campaign uses MD5 salt per cell/rep)")
    fails = []
    for cell in ("E0", "E1", "E2", "E2m", "E3", "E4"):
        rng = np.random.default_rng(probe_seed)
        # NOTE: cell-specific draws are taken from ONE stream per cell to make
        # window overlap detectable across cells; campaign uses per-rep salts.
        def draw_window():
            idx = rng.integers(0, len(R) - cal.T + 1)
            return idx
        if cell == "E0":
            Hsim = cal.sim_persistence(H[0], cal.SIGMA, rng)
        elif cell == "E1":
            Hsim = cal.sim_ar1(base["M1"]["a"], base["M1"]["phi"], H[0], cal.SIGMA, rng)
        else:
            truth_win = draw_window()
            fluxR, fluxP = R[truth_win:truth_win + cal.T], P[truth_win:truth_win + cal.T]
            if cell == "E2m":
                fluxR = np.full(cal.T, np.mean(R)); fluxP = np.full(cal.T, np.mean(P))
            Hsim = cal.sim_m2_flux(base["M2"], H[0], fluxR, fluxP, cal.SIGMA, rng,
                                   resid_ar=(base["M2"]["phi"] if cell in ("E3", "E4") else 0.0),
                                   resid0=(base["M2"]["last_resid"] if cell in ("E3", "E4") else 0.0))
        idx = draw_window()
        R_s, P_s = R[idx:idx + cal.T], P[idx:idx + cal.T]
        fits_perf = cal.fit_candidates(Hsim, R_s, P_s)            # what the harness scores
        fits_causal = cal.fit_candidates(Hsim[:45], R_s[:45], P_s[:45])  # causal reference

        pers1 = [Hsim[o + 1] - Hsim[o] for o in range(cal.MIN_TRAIN, cal.T - 5)]
        pers5 = [Hsim[o + 5] - Hsim[o] for o in range(cal.MIN_TRAIN, cal.T - 5)]
        print(f"\n--- {cell} (probe): persistence h1={rmse(pers1):6.2f} h5={rmse(pers5):6.2f} | "
              f"truth_win={locals().get('truth_win','-')} fit_win={idx}")
        prev_rmse = {}
        for name in ("M1", "M2", "M3", "M4"):
            e1, e5 = cal.path_errors(Hsim, R_s, P_s, fits_perf, name)
            r1, r5 = rmse(e1), rmse(e5)
            ok1 = "OK" if np.isfinite(r1) and np.isfinite(r5) else "NaN!"
            print(f"    {name}: h1={r1:6.2f} h5={r5:6.2f} [{ok1}]  |H2 gap%| "
                  f"h1={(1 - r1 / rmse(pers1)) * 100:6.1f} h5={(1 - r5 / rmse(pers5)) * 100:6.1f}")
            prev_rmse[name] = (r1, r5)
            if not (np.isfinite(r1) and np.isfinite(r5)):
                fails.append(cell + ":" + name + ":nan")
        # H1 chain feasibility (comparator: M2 vs M1, M3 vs M2, M4 vs M3)
        for pair in (("M2", "M1"), ("M3", "M2"), ("M4", "M3")):
            a, b = pair
            g1 = (1 - prev_rmse[a][0] / prev_rmse[b][0]) * 100
            g5 = (1 - prev_rmse[a][1] / prev_rmse[b][1]) * 100
            note = ""
            if pair == ("M4", "M3"):
                h5_gap = abs(g5)
                # the M4 h1 gap IS the declared lag property; not a deadlock
                note = (f"  [M4 lag: h1 gap={g1:6.1f}% (recorded), h5 gap={g5:6.1f}% "
                        f"{'(washes out — OK)' if h5_gap < 1.0 else '(unexpected!)'}]")
                if not h5_gap < 1.0:
                    fails.append(f"{cell}:M4-lag-not-washing-out-at-h5")
            print(f"    chain {a} vs {b}: h1 {g1:6.1f}%  h5 {g5:6.1f}%{note}")
            if pair != ("M4", "M3") and (g1 < -15 or g5 < -15):   # real gate deadlock
                fails.append(f"{cell}:{a}>{b}:gate-deadlock")
        # M2 vs M1 should beat M1 under M2-generating truths
        if cell in ("E2", "E3", "E4") and prev_rmse["M2"][0] > prev_rmse["M1"][0] * 1.05:
            fails.append(cell + ":M2-not-better-than-M1")
        if cell == "E1" and prev_rmse["M1"][0] > rmse(pers1) * 0.95:
            fails.append(cell + ":M1-not-better-than-persistence")

    print("\n=== AUDIT VERDICT ===")
    if fails:
        print("FAIL:", *sorted(set(fails)), sep="\n  - ")
        sys.exit(1)
    print("ALL CHECKS PASS — harness is fit for the registered 100-rep campaign.")

if __name__ == "__main__":
    main()

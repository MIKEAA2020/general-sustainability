#!/usr/bin/env python3
"""Phase C campaign 4 — Edwards cross-environment rerun (M2m context, 2000-2007).

Re-runs the e3_audit_uncertainty machinery (wave_e_edwards/src) in the current
numpy/scipy environment: the same archived per-origin forecast CSVs, the same
Diebold-Mariano + moving-block bootstrap functions, plus the M2m-vs-naive_persist
h=5 comparison that sits behind the framework's published D1 citation.

Nothing is re-implemented: load_main(), series(), dm_test(), block_bootstrap_margin()
are imported from e3_audit_uncertainty.py. The bootstrap seed (20260905) and block
length (8) are the module's frozen constants.

Output: phase_c/results/e3_audit_uncertainty_M2m_h5_20260913.json
"""
import os, sys, json, hashlib, datetime, time, math
import numpy as np

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(WS, "wave_e_edwards", "src"))
import e3_audit_uncertainty as e3  # noqa: E402

OUT = os.path.join(WS, "phase_c", "results", "e3_audit_uncertainty_M2m_h5_20260913.json")


def one_test(label, ma, mb, h, table):
    sa, oa = e3.series(table, ma, h)
    sb, ob = e3.series(table, mb, h)
    assert oa == ob, (label, "origin mismatch")
    dm, p = e3.dm_test(sa, sb, h)
    lo, hi = e3.block_bootstrap_margin(sa, sb)
    return {
        "comparison": f"{ma} vs {mb} (h={h}, n={len(sa)})",
        "rmse_a": round(math.sqrt(sa.mean()), 4),
        "rmse_b": round(math.sqrt(sb.mean()), 4),
        "margin_rmse": round(math.sqrt(sa.mean()) - math.sqrt(sb.mean()), 4),
        "dm_stat": round(dm, 3),
        "dm_p_two_sided": round(p, 4),
        "blockboot_margin_95ci": [round(lo, 3), round(hi, 3)],
        "ci_covers_zero": bool(lo <= 0.0 <= hi),
    }


def main():
    t0 = time.time()
    main_table, models, horizons = e3.load_main()
    tests = [
        one_test("M1_vs_persist_h1", "M1", "naive_persist", 1, main_table),
        one_test("M2m_vs_persist_h1", "M2m", "naive_persist", 1, main_table),
        one_test("M2m_vs_M1_h1", "M2m", "M1", 1, main_table),
        one_test("M2_vs_persist_h1", "M2", "naive_persist", 1, main_table),
        one_test("mean_vs_persist_h5", "naive_mean", "naive_persist", 5, main_table),
        one_test("M1_vs_persist_h5", "M1", "naive_persist", 5, main_table),
        one_test("M2m_vs_persist_h5_D1", "M2m", "naive_persist", 5, main_table),
    ]
    out = {
        "layer": "Phase C cross-environment rerun of the E3 audit layer + D1 citation cell",
        "seed": e3.SEED, "nboot": e3.NBOOT, "block": e3.BLOCK,
        "started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "wall_s": round(time.time() - t0, 2),
        "pyhashseed": os.environ.get("PYTHONHASHSEED"),
        "sha256": {
            "e3_audit_uncertainty.py": hashlib.sha256(
                open(os.path.join(WS, "wave_e_edwards", "src", "e3_audit_uncertainty.py"), "rb").read()).hexdigest(),
            "rolling_forecasts.csv": hashlib.sha256(
                open(os.path.join(WS, "wave_e_edwards", "results", "rolling_forecasts.csv"), "rb").read()).hexdigest(),
            "rerun_edwards.py": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
        },
        "versions": dict(numpy=np.__version__),
        "dm_tests": tests,
    }
    with open(OUT, "w") as f:
        json.dump(out, f, indent=2)
    print(f"wrote {OUT}")
    d1 = tests[-1]
    print("\n=== D1 citation cell (M2m vs naive_persist, h=5) ===")
    print(json.dumps(d1, indent=2))
    print("\n=== published (for comparison) ===")
    print("margin -3.6607 | dm z=-3.284 | p=0.0016 | CI [-5.7637, -2.1862]")


if __name__ == "__main__":
    main()

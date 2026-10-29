"""Baseline drawdown-depth sweep for ECOMOD v44.
Units: initial/capital land areas in ha, initial population in cap, annual
account values B and E in gha, debt in gha yr, and model time in yr. Writes the
package-local si_drawdown_depth.csv used by Figure 1(c) and SI tables.
"""
from pathlib import Path
import sys
import numpy as np, csv
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "work"))
import twoland_fixed as tf
def mk(chi_r=0.10, tau_g=20.0):
    return tf.FixPara(rho_c=0.08, b_f0=0.85, b_c=0.05, b_Gc=0.80, alpha=0.03, eta_f=0.05, e=0.55, r=0.02, eta=0.05,
               tau_g=tau_g, tau_p=25.0, A_tot=2.5, deltab=1.0, t_wave=40.0, kappa_w=0.1, mu=0.06, tau_conv=1.0, chi_r=chi_r)
P0s = np.round(np.arange(1.0, 4.01, 0.1), 2)
rows = []
for A_c0 in [0.40, 0.70, 1.00, 1.18]:
    for P0 in P0s:
        out = {"A_c0_ha": A_c0, "P0_cap": P0}
        for chi in [0.10, 0.0]:
            p = mk(chi)
            r = tf.simulate(p, T=400.0, dt=0.1, A_c0=A_c0, A_f0=0.6, q0=0.9, P0=P0)
            B = r["B"]; E = p.e * r["Pp"]
            out["minAc_ha_chi%.2f" % chi] = r["Ac"].min()
            out["finalAc_ha_chi%.2f" % chi] = r["Ac"][-1]
            out["maxD_gha_yr_chi%.2f" % chi] = r["Dd"].max()
            out["tmin_yr_chi%.2f" % chi] = float(np.argmin(r["Ac"])) * 0.1
        rows.append(out)
with (ROOT / "si_drawdown_depth.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), lineterminator="\n"); w.writeheader(); w.writerows(rows)
# Summary labels carry the physical units; all calculations above are unchanged.
for A_c0 in [0.40, 0.70, 1.00, 1.18]:
    sel = [r for r in rows if r["A_c0_ha"] == A_c0]
    samples = "  ".join("P0=%.1f cap: min A_c=%.3f ha" % (r["P0_cap"], r["minAc_ha_chi0.10"]) for r in sel if abs(r["P0_cap"]*10 % 5) < 1e-6)
    print("A_c0=%.2f ha: %s" % (A_c0, samples))
    # First initial population at which minimum capital land lies within a land-area tolerance of the floor.
    for tol in [1e-2, 1e-3, 1e-4]:
        hit = [r["P0_cap"] for r in sel if r["minAc_ha_chi0.10"] <= 0.05 + tol]
        if hit:
            print("   first P0 with min A_c <= floor + %.0e ha: %.1f cap" % (tol, hit[0]))
        else:
            print("   no P0 threshold within %.0e ha of floor on this grid" % tol)

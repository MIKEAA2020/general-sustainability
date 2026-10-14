"""Capital drawdown depth vs initial demand (endogenous demand runs), baseline parameters.
Writes ../si_drawdown_depth.csv; used by make_fig_model.py panel (c) and SI Table S4."""
import numpy as np, csv
import twoland_fixed as tf
def mk(chi_r=0.10, tau_g=20.0):
    return tf.FixPara(rho_c=0.08, b_f0=0.85, b_c=0.05, b_Gc=0.80, alpha=0.03, eta_f=0.05, e=0.55, r=0.02, eta=0.05,
               tau_g=tau_g, tau_p=25.0, A_tot=2.5, deltab=1.0, t_wave=40.0, kappa_w=0.1, mu=0.06, tau_conv=1.0, chi_r=chi_r)
P0s = np.round(np.arange(1.0, 4.01, 0.1), 2)
rows = []
for A_c0 in [0.40, 0.70, 1.00, 1.18]:
    for P0 in P0s:
        out = {"A_c0": A_c0, "P0": P0}
        for chi in [0.10, 0.0]:
            p = mk(chi)
            r = tf.simulate(p, T=400.0, dt=0.1, A_c0=A_c0, A_f0=0.6, q0=0.9, P0=P0)
            B = r["B"]; E = p.e * r["Pp"]
            out["minAc_chi%.2f" % chi] = r["Ac"].min()
            out["finalAc_chi%.2f" % chi] = r["Ac"][-1]
            out["maxD_chi%.2f" % chi] = r["Dd"].max()
            out["tmin_chi%.2f" % chi] = float(np.argmin(r["Ac"])) * 0.1
        rows.append(out)
with open("../si_drawdown_depth.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
# summary print
for A_c0 in [0.40, 0.70, 1.00, 1.18]:
    sel = [r for r in rows if r["A_c0"] == A_c0]
    print("A_c0=%.2f: " % A_c0 + "  ".join("P0=%.1f:%.3f" % (r["P0"], r["minAc_chi0.10"]) for r in sel if abs(r["P0"]*10 % 5) < 1e-6))
    # first P0 at which min A_c within 1e-3 and 1e-6 of floor
    for tol in [1e-2, 1e-3, 1e-4]:
        hit = [r["P0"] for r in sel if r["minAc_chi0.10"] <= 0.05 + tol]
        print("   first P0 with min A_c <= floor+%.0e : %s" % (tol, hit[0] if hit else None))

"""Re-derive effort_signal_power_report.md section 2 table from power_demo machinery.
Reconstruction hypotheses (driver script missing; parameters from the report):
integrate long (T=4000, dt=0.05) to develop the slow effort oscillation, take the
LAST H years as the horizon-H record, detect() with report bands, 50 trials,
trial seeds 0..49, null seed 7 / 120 sims (as in detect defaults).
Cells: sprat (r=0.8,g=2,Tr=7) band (30,120); anchovy (r=1.6,g=1,Tr=3) band (8,20).
Report targets: sprat H100 s0.1=1.00, s0.3=0.24; H200 s0.3=0.58; H400 s0.3=1.00;
anchovy range 0.02-0.14; cod FP 0.00-0.06."""
import numpy as np, time
from power_demo import integrate_E, detect

def power_cell(r, g, Tr, band, H, sig, n_real=50, T=4000.0):
    t0 = time.time()
    t, E = integrate_E(r, g, 0.914, Tr, T=T)
    Eh = E[-H:]
    dets = 0
    for k in range(n_real):
        eps = np.random.default_rng(k).normal(0, sig, len(Eh))
        d, bp, thr = detect(Eh * np.exp(eps), band)
        dets += d
    print(f'r={r} g={g} Tr={Tr} band={band} H={H} sig={sig}: power={dets/n_real:.2f} ({dets}/{n_real}) [{time.time()-t0:.0f}s]', flush=True)

print('--- sprat-class, band (30,120) ---')
power_cell(0.8, 2.0, 7.0, (30,120), 100, 0.1)
power_cell(0.8, 2.0, 7.0, (30,120), 100, 0.3)
power_cell(0.8, 2.0, 7.0, (30,120), 200, 0.3)
print('--- anchovy-class, band (8,20) ---')
power_cell(1.6, 1.0, 3.0, (8,20), 100, 0.1)
power_cell(1.6, 1.0, 3.0, (8,20), 100, 0.3)
power_cell(1.6, 1.0, 3.0, (8,20), 200, 0.3)

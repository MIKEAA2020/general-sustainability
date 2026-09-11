"""Second hypothesis: horizon-H window = FIRST H post-convergence years
(years 100..100+H of the long run), i.e. developing transient, not converged tail."""
import numpy as np
from power_demo import integrate_E, detect

CACHE = {}
def annual_E(r, g, Tr, T=4000.0):
    key = (r, g, Tr)
    if key not in CACHE:
        t, E = integrate_E(r, g, 0.914, Tr, T=T)
        CACHE[key] = (t, E)
    return CACHE[key]

def power_cell(r, g, Tr, band, H, sig, start=100, n_real=50):
    t, E = annual_E(r, g, Tr)
    Eh = E[start:start+H]
    dets = sum(detect(Eh*np.exp(np.random.default_rng(k).normal(0,sig,len(Eh))), band)[0]
               for k in range(n_real))
    print(f'r={r} g={g} Tr={Tr} band={band} yrs[{start},{start+H}] sig={sig}: power={dets/n_real:.2f} ({dets}/{n_real})', flush=True)

print('--- sprat (30,120): targets H100 s0.1=1.00, s0.3=0.24; H200 s0.3=0.58 ---')
power_cell(0.8, 2.0, 7.0, (30,120), 100, 0.1)
power_cell(0.8, 2.0, 7.0, (30,120), 100, 0.3)
power_cell(0.8, 2.0, 7.0, (30,120), 200, 0.3)
print('--- anchovy (8,20): target range 0.02-0.14 ---')
power_cell(1.6, 1.0, 3.0, (8,20), 100, 0.1)
power_cell(1.6, 1.0, 3.0, (8,20), 100, 0.3)
power_cell(1.6, 1.0, 3.0, (8,20), 200, 0.3)

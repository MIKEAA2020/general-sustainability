import numpy as np
from power_demo import integrate_E, detect
CACHE = {}
def annual_E(r, g, Tr, T=4000.0):
    key = (r, g, Tr)
    if key not in CACHE: CACHE[key] = integrate_E(r, g, 0.914, Tr, T=T)
    return CACHE[key]
def power_cell(r, g, Tr, band, H, sig, start, n_real=50):
    t, E = annual_E(r, g, Tr)
    Eh = E[start:start+H]
    dets = sum(detect(Eh*np.exp(np.random.default_rng(k).normal(0,sig,len(Eh))), band)[0]
               for k in range(n_real))
    print(f'start={start} r={r} g={g} Tr={Tr} H={H} sig={sig}: power={dets/n_real:.2f} ({dets}/{n_real})', flush=True)
for start in (20, 50):
    print(f'=== window start {start} ===')
    power_cell(0.8, 2.0, 7.0, (30,120), 100, 0.3, start)   # target 0.24
    power_cell(0.8, 2.0, 7.0, (30,120), 200, 0.3, start)   # target 0.58
    power_cell(1.6, 1.0, 3.0, (8,20), 100, 0.1, start)     # target <=0.14

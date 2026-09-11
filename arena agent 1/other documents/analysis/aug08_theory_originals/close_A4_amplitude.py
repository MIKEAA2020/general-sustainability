"""Close A4: track the small unstable orbit's amplitude as tau -> tau_- (3.666).
Continue from the checkpoint (tau=3.700) down toward tau_-, reconverging the
segment-map fixed point at each tau.  If amplitude -> 0 with a sqrt-like
scaling as tau -> tau_+, it confirms the subcritical-Hopf birth; if it stays
bounded (discontinuous), the small orbit does NOT shrink to zero.
"""
import numpy as np
import sys
sys.path.insert(0, '.')
from corrected_shooting import (advance_seg_corrected, converge_fixed_point,
                                segment_from_checkpoint, rhs_corrected_local,
                                params_arr, PARAMS_A)

CKPT = 'unstable_clean_ckpt.npz'
dt = 0.01
# load checkpoint orbit at tau=3.700 for the first seed
seg0, n_tau0, nseg0, T_c = segment_from_checkpoint(CKPT, 3.700, dt)
p = params_arr(PARAMS_A())

# pin: N at segment start = some value (phase condition) - use midpoint N
pin_idx = 0
pin_val = seg0[0]

def amplitude(seg, n_tau):
    # N block is every 3rd entry
    N = seg[0::3]
    return N.max() - N.min()

# continue downward from 3.700
taus = np.arange(3.700, 3.660, -0.004)
print(f"{'tau':>8s} {'amp(N)':>9s} {'res':>10s} {'conv':>5s}")
seg = seg0.copy()
for tau in taus:
    n_tau = int(round(tau/dt))
    # build segment for this tau from the previous converged orbit (resample)
    if abs(n_tau - len(seg)//3 + 1) != 0:
        # resample: reuse via periodic interpolation
        from scipy.interpolate import CubicSpline
        Nv, Zv, Ev = seg[0::3], seg[1::3], seg[2::3]
        tt = np.arange(len(Nv))*dt
        def mk(x):
            tp = np.concatenate([tt - tau, tt, tt + tau]); xp = np.concatenate([x,x,x])
            return CubicSpline(tp, xp)
        Nf, Zf, Ef = mk(Nv), mk(Zv), mk(Ev)
        seg = np.zeros(3*(n_tau+1))
        for k in range(n_tau+1):
            ttk = (k - n_tau)*dt
            seg[3*k] = float(Nf(ttk)); seg[3*k+1] = float(Zf(ttk)); seg[3*k+2] = float(Ef(ttk))
    try:
        seg, conv, rms = converge_fixed_point(seg, n_tau, int(round(2.0/dt)), dt, pin_idx, pin_val)
        if not conv:
            print(f"{tau:8.4f}  not-conv rms={rms:.1e}")
            break
    except Exception as e:
        print(f"{tau:8.4f}  conv-err {str(e)[:40]}")
        break
    res = 1.0
    # residual of the fixed-point (advance once)
    try:
        seg2 = advance_seg_corrected(seg, n_tau, int(round(2.0/dt)), dt)
        res = np.max(np.abs(seg2 - seg))
    except Exception:
        pass
    print(f"{tau:8.4f} {amplitude(seg, n_tau):9.4f} {res:10.2e}  conv")
PYEOF
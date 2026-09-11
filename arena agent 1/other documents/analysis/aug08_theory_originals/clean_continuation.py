"""
Clean natural-parameter continuation using ODD M (no Nyquist-mode null-space
defect), with an explicit checkerboard-contamination check at every accepted
step (reject any solution where the highest-frequency Fourier mode carries
non-negligible amplitude, even if the raw residual norm looks small).
"""
import numpy as np
from collocation_corrected import make_residual_fn
from continuation3 import lm_corrector
from corrected_core_common import PARAMS_A

def high_freq_contamination(v, M):
    N = v[0:M]
    Nk = np.fft.fft(N)
    return np.abs(Nk[M//2]) / M

def solve_at_tau(v_guess, tau, M, tol=1e-10, maxit=800, lam0=1e-9, contam_ceiling=1e-3,
                  prev_resn=None, growth_factor=3.0, abs_ceiling=8e-2):
    N = v_guess[0:M]
    pin_index = int(np.argmax(N))
    pin_value = float(N[pin_index])
    res_fixed, _, _ = make_residual_fn(M, PARAMS_A, pin_index, pin_value)
    res_fn = lambda vv: res_fixed(vv, tau)
    v_new, conv, resn = lm_corrector(res_fn, v_guess, tol=tol, maxit=maxit, lam0=lam0)
    contam = high_freq_contamination(v_new, M)
    # Accept if residual is below an absolute ceiling AND (no history yet, or it
    # didn't blow up relative to the previous accepted point's residual floor).
    rel_ok = (prev_resn is None) or (resn < growth_factor * prev_resn) or (resn < 1e-3)
    ok = (resn < abs_ceiling) and (contam < contam_ceiling) and rel_ok
    return v_new, ok, resn, contam

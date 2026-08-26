#!/usr/bin/env python3
"""A025 fold pipeline: m-point Fourier collocation -> branch switching from the
Hopf point -> tau continuation to the fold -> Moore-Spence fold solve.

REBUILT 2026-08-26. This version repairs the defects of the committed draft
(`fold_run.log`: Stage 2 never returned) and the two further defects found
during this rebuild:

1. Stage-2 infinite loop (draft). The draft's `branch_switch` accepted the
   Newton fallback seed (the equilibrium — an exact solution of the
   collocation system at every tau) without an amplitude check, and
   `continue_in_a` then halved `da` forever on the collapsed solution (the
   `pk <= 1e-6` branch had no exit).

2. Moore-Spence `want_jac` signature bug (draft). `ms_residual_jac(z, ell)`
   read a *global* `want_jac` and the line search called it with a
   `want_jac=False` keyword it did not accept (TypeError at the first
   line-search evaluation). Fixed: `want_jac` is a parameter, both call
   sites use it directly.

3. Nyquist (checkerboard) degeneracy (found in this rebuild). The Fourier
   differentiation and shift matrices zero the Nyquist symbol
   (`sym[FREQ == -N/2] = 0`), so the collocation system admits spurious
   "checkerboard" solutions alternating between two zeros of the vector
   field (here: the equilibrium and the second root of the E-quadratic on
   the N-nullcline, where `softplus(0) = Z*` makes the Z-equation close).
   The draft's un-projected branch-switch Newton falls into these from Hopf
   predictors. Fixed by Nyquist-projecting the Newton iterates ONLY in the
   branch switch (a checkerboard projects to its mean point, whose residual
   is large, so it becomes unreachable, while genuine smooth cycles are
   untouched). The continuation and the Moore-Spence stages must NOT
   project: the genuine collocation solutions carry a growing Nyquist
   spectral tail (measured here: 8e-8 at tau=5.39 rising to 1.6e-4 at the
   fold), and projecting it away creates a residual floor that stalls the
   continuation near tau~5.3-5.4. Those stages instead REJECT any solution
   whose Nyquist coefficient exceeds 1% of its spectral maximum (a
   checkerboard has ~100%; the branch never exceeds ~1e-3 relative).

4. Newton residual floor vs. tolerance (found in this rebuild). The
   collocation residual evaluation carries a floating-point floor
   (~2e-12 mid-branch, rising to ~1e-9 at the fold where the Jacobian
   turns singular). A hard tolerance at the floor stalls the continuation
   with spurious failures. Fixed with an explicit stall-acceptance
   criterion (accept a stalled Newton when the achieved residual is below
   `stall_accept`, default 3e-9) and a tau-progression stop rule.

With these repairs the natural-parameter tau continuation reaches the
turning region (last accepted tau ~ 5.587236..., amplitude ~22.3, period
~315.3, matching the manuscript's continuation evidence at tau=5.58667:
amplitude 21.80, period 313.76), and the Moore-Spence stage solves the fold
from there.

The collocation order m is parameterized (`python3 a025_fold_pipeline.py [m]`,
default 64) so the resolution cross-checks (m=96, 128) can run.

HONESTY NOTE — what this pipeline does and does not produce. It produces the
NOMINAL Moore-Spence fold point (tau_f, T_f, orbit, null vector) with the
achieved residual recorded. It does NOT perform the interval Krawczyk
certification of the lost artifact (which claimed tau_f in
[5.587236197890, 5.587236199490] with nondegeneracy certified): the interval
stage is not implemented in the committed code. The nominal tau_f is compared
against the lost interval as a cross-check only; no certified status is
claimed for the output of this script.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))
from a025_model import PAR, equilibrium, rhs, rhs_jac  # noqa: E402

TAU_H = 3.666149014274113          # certified Hopf tau (a025_interval_hopf.json)
LOST_CERT_INTERVAL = (5.587236197890, 5.587236199490)  # lost artifact's claim

# ---- parameterized collocation order ------------------------------------
N_NODES = 64
DIM_Y = 3 * N_NODES
DIM = DIM_Y + 1
FREQ = np.fft.fftfreq(N_NODES, d=1.0 / N_NODES)
D = None            # Fourier differentiation matrix
SIN1 = None         # phase-condition vector
KRON_DI = None      # kron(D, I_3), precomputed


def configure(n_nodes):
    global N_NODES, DIM_Y, DIM, FREQ, D, SIN1, KRON_DI
    N_NODES = int(n_nodes)
    DIM_Y = 3 * N_NODES
    DIM = DIM_Y + 1
    FREQ = np.fft.fftfreq(N_NODES, d=1.0 / N_NODES)
    D = _mat_from_symbol(2j * np.pi * FREQ)
    SIN1 = np.sin(2.0 * np.pi * np.arange(N_NODES) / N_NODES)
    KRON_DI = np.kron(D, np.eye(3))


def _mat_from_symbol(sym):
    sym = np.asarray(sym, complex).copy()
    sym[FREQ == -N_NODES // 2] = 0.0
    E = np.eye(N_NODES)
    return np.fft.ifft(sym[:, None] * np.fft.fft(E, axis=0), axis=0).real


def shift_matrix(phi):
    sym = np.exp(-2j * np.pi * FREQ * phi)
    return _mat_from_symbol(sym)


def shift_matrix_der(phi):
    """d/dphi of shift_matrix(phi)."""
    sym = (-2j * np.pi * FREQ) * np.exp(-2j * np.pi * FREQ * phi)
    return _mat_from_symbol(sym)


def unpack(w):
    return w[:DIM_Y].reshape(N_NODES, 3), w[DIM_Y]


def pack(Y, T):
    return np.r_[Y.reshape(-1), T]


def nyquist_project(w):
    """Remove the Nyquist mode from each state column of w (branch switch
    only — see module docstring, defect 3)."""
    w = np.asarray(w, float).copy()
    Y = w[:DIM_Y].reshape(N_NODES, 3)
    Yf = np.fft.fft(Y, axis=0)
    Yf[N_NODES // 2, :] = 0.0
    w[:DIM_Y] = np.fft.ifft(Yf, axis=0).real.reshape(-1)
    return w


def nyquist_relative(w):
    """Relative Nyquist content of the N-column (checkerboard detector)."""
    Y, _ = unpack(w)
    c = np.abs(np.fft.fft(Y[:, 0]))
    peak = float(np.max(c[1:])) if len(c) > 1 else 0.0
    if peak == 0.0:
        return 0.0
    return float(c[N_NODES // 2]) / peak


def residual_jac(w, tau, want_jac=True):
    Y, T = unpack(w)
    phi = tau / T
    S = shift_matrix(phi)
    Zd = S @ Y[:, 1]
    F = np.empty((N_NODES, 3))
    for i in range(N_NODES):
        F[i] = rhs(Y[i], Zd[i])
    R = D @ Y - T * F
    phase = SIN1 @ Y[:, 0]
    res = np.r_[R.reshape(-1), phase]
    if not want_jac:
        return res
    J = np.zeros((DIM, DIM))
    J[:DIM_Y, :DIM_Y] = KRON_DI
    Sp = shift_matrix_der(phi)
    dZd_dT = (Sp @ Y[:, 1]) * (-phi / T)
    for i in range(N_NODES):
        Ai, Di_ = rhs_jac(Y[i], Zd[i])
        J[3 * i:3 * i + 3, 3 * i:3 * i + 3] -= T * Ai
        J[3 * i:3 * i + 3, 1::3] -= T * np.outer(Di_, S[i, :])
        J[3 * i:3 * i + 3, DIM_Y] = -F[i] - T * Di_ * dZd_dT[i]
    J[DIM_Y, :DIM_Y:3] = SIN1
    return res, J


def newton(w0, tau, tol=1e-11, maxit=40, project=False,
           stall_accept=3e-9):
    """Newton on F(w, tau) = 0 (with phase row).

    `project` Nyquist-filters the iterates (branch switch only). A stalled
    line search is accepted when the achieved residual is below
    `stall_accept` (defect 4: the residual evaluation has a floating-point
    floor that a hard tolerance would convert into spurious failures).
    """
    w = nyquist_project(w0) if project else np.asarray(w0, float).copy()
    for it in range(maxit):
        res, J = residual_jac(w, tau)
        rn = np.linalg.norm(res, np.inf)
        if rn < tol:
            return w, True, rn
        try:
            dw = np.linalg.lstsq(J, -res, rcond=1e-12)[0]
        except Exception:
            return w, False, rn
        step = 1.0
        for _ in range(30):
            wn = w + step * dw
            if project:
                wn = nyquist_project(wn)
            rn_new = np.linalg.norm(residual_jac(wn, tau, want_jac=False),
                                    np.inf)
            if np.isfinite(rn_new) and rn_new < rn:
                w = wn
                break
            step *= 0.5
        else:
            return w, rn < stall_accept, rn
    rn = np.linalg.norm(residual_jac(w, tau, want_jac=False), np.inf)
    return w, rn < stall_accept, rn


def peak_to_peak(w):
    Y, _ = unpack(w)
    return float(np.ptp(Y[:, 0]))


def hopf_predictor(tau, amp, p=PAR):
    from a025_model import lin_coeffs, characteristic
    c = lin_coeffs(p)
    # find the complex Hopf eigenvalue near i*omega (omega ~ 0.0252)
    lam0 = 0.0015 + 1j * 0.0252
    for _ in range(100):
        h = 1e-10
        f0 = characteristic(lam0, tau)
        f1 = characteristic(lam0 + h, tau)
        f2 = characteristic(lam0 - h, tau)
        d = (f1 - f2) / (2 * h)
        if abs(d) < 1e-20:
            break
        lam_new = lam0 - f0 / d
        if abs(lam_new - lam0) < 1e-15:
            lam0 = lam_new
            break
        lam0 = lam_new
    # eigenvector
    z = 1.0 + 0j
    x = c['A_E'] * z / (lam0 - c['A_N'])
    y = (c['B_N'] * x + c['B_E'] * z) / (lam0 + c['d'])
    v = np.array([x, y, z])
    scale = np.max(np.abs(v))
    v = v / scale
    th = 2.0 * np.pi * np.arange(N_NODES) / N_NODES
    Y = np.empty((N_NODES, 3))
    eq = equilibrium(p)
    for cix in range(3):
        Y[:, cix] = eq[cix] + amp * (np.cos(th) * v[cix].real
                                      - np.sin(th) * v[cix].imag)
    T = 2.0 * np.pi / lam0.imag
    return pack(Y, T)


def branch_switch():
    """Switch onto the periodic branch emanating from the Hopf point.

    Scans a ladder of (tau, amplitude) Hopf predictors with a
    Nyquist-PROJECTED Newton (defects 1 and 3) and accepts only
    non-equilibrium solutions. The genuine branch point is found at
    tau = tau_h + 0.05, amplitude 8 (eigenvector units), Npk ~ 1.10.
    """
    for tau0 in (TAU_H + 0.05, TAU_H + 0.10, TAU_H + 0.20, TAU_H + 0.35):
        for amp in (0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 4.0, 8.0,
                    12.0, 16.0, 24.0, 32.0):
            w0 = hopf_predictor(tau0, amp)
            w, ok, _ = newton(w0, tau0, project=True, stall_accept=1e-10)
            if ok and peak_to_peak(w) > 1e-6:
                return tau0, w
    raise RuntimeError('branch switch failed: no non-equilibrium periodic '
                       'solution found on the (tau, amplitude) ladder')


def continue_to_fold(w_start, tau_start, tau_end=6.4, dtau0=0.02,
                     dtau_min=1e-7, verbose=False):
    """Natural-parameter continuation in tau toward the fold.

    Secant predictors + (unprojected) Newton corrections; dtau grows on
    success and shrinks on failure. Stops when dtau collapses (the fold is
    where the collocation Jacobian turns singular and Newton can no longer
    correct) or when tau stops progressing. Checkerboard solutions are
    rejected by their relative Nyquist content (defect 3, defensive).
    """
    tau = tau_start
    w_prev = w_start
    w_prev2 = None
    tau_prev2 = None
    dtau = dtau0
    pts = [(tau_start, w_start, 0.0)]
    n_fail = 0
    last_progress = tau_start
    while tau < tau_end:
        tau_new = tau + dtau
        if w_prev2 is None:
            w0 = w_prev.copy()
        else:
            sec = (w_prev - w_prev2) / (tau - tau_prev2)
            w0 = w_prev + (tau_new - tau) * sec
        w_new, ok, rn = newton(w0, tau_new)
        if (ok and peak_to_peak(w_new) > 1e-6
                and nyquist_relative(w_new) < 0.01):
            pts.append((tau_new, w_new, rn))
            w_prev2, tau_prev2 = w_prev, tau
            w_prev, tau = w_new, tau_new
            dtau = min(dtau * 1.3, 0.05)
            n_fail = 0
            if tau - last_progress > 1e-6:
                last_progress = tau
        else:
            dtau *= 0.4
            n_fail += 1
            if dtau < dtau_min:
                break
            if n_fail > 200:
                break
        # stop when tau no longer progresses (micro-stepping at the fold)
        if dtau < 1e-6 and tau - last_progress < 1e-8:
            break
    if verbose:
        taus = [p[0] for p in pts]
        print(f'  continuation: {len(pts)} points, '
              f'tau in [{taus[0]:.6f}, {taus[-1]:.6f}], '
              f'last residual {pts[-1][2]:.1e}')
    i_max = int(np.argmax([p[0] for p in pts]))
    return pts, pts[i_max]


def dF_dtau(w, tau):
    Y, T = unpack(w)
    phi = tau / T
    Sp = shift_matrix_der(phi)
    dZd_dtau = (Sp @ Y[:, 1]) / T
    out = np.zeros(DIM)
    S = shift_matrix(phi)
    Zd = S @ Y[:, 1]
    for i in range(N_NODES):
        _, Di_ = rhs_jac(Y[i], Zd[i])
        out[3 * i:3 * i + 3] = -T * Di_ * dZd_dtau[i]
    return out


def moore_spence(w_fold, tau_fold, tol=1e-10, maxit=40, verbose=False):
    """Moore-Spence fold solve: F(w,tau)=0, J v=0, ell.v=1 (NOMINAL point
    solve — no interval certification; see module docstring)."""
    res, J193 = residual_jac(w_fold, tau_fold)
    U, s, Vt = np.linalg.svd(J193)
    v0 = Vt[-1].copy()
    ell = v0 / (v0 @ v0)

    def ms_residual_jac(z, ell, want_jac=True):
        w = z[:DIM]
        tau = z[DIM]
        v = z[DIM + 1:]
        res, J193 = residual_jac(w, tau)
        M = np.r_[res, J193 @ v, ell @ v - 1.0]
        if not want_jac:
            return M
        Jms = np.zeros((2 * DIM + 1, 2 * DIM + 1))
        Jms[:DIM, :DIM] = J193
        Jms[:DIM, DIM] = dF_dtau(w, tau)
        Jms[DIM:2 * DIM, DIM + 1:] = J193
        # d(J v)/d(w, tau) by central finite differences over the w and tau
        # coordinates. e has DIM+1 entries: e[:DIM] perturbs w (indices 0..DIM-1
        # are the Y components, index DIM_Y is T), e[DIM] perturbs tau.
        eps = 1e-7
        for j in range(DIM + 1):
            e = np.zeros(DIM + 1)
            e[j] = eps
            wp = np.r_[w[:DIM_Y] + e[:DIM_Y], w[DIM_Y] + e[DIM_Y]]
            Jp = residual_jac(wp, tau + e[DIM])[1]
            wm = np.r_[w[:DIM_Y] - e[:DIM_Y], w[DIM_Y] - e[DIM_Y]]
            Jm = residual_jac(wm, tau - e[DIM])[1]
            Jms[DIM:2 * DIM, j] = ((Jp - Jm) @ v) / (2 * eps)
        Jms[2 * DIM, DIM + 1:] = ell
        return M, Jms

    z0 = np.r_[w_fold, tau_fold, v0]
    z = z0.copy()
    mn = np.inf
    for it in range(maxit):
        M, Jms = ms_residual_jac(z, ell)
        mn = np.linalg.norm(M, np.inf)
        if verbose:
            print(f'    MS it={it} |M|={mn:.3e} tau={z[DIM]:.12f}')
        if mn < tol:
            break
        try:
            dz = np.linalg.lstsq(Jms, -M, rcond=1e-12)[0]
        except Exception:
            break
        step = 1.0
        for _ in range(30):
            zn = z + step * dz
            mn_new = np.linalg.norm(ms_residual_jac(zn, ell, want_jac=False),
                                    np.inf)
            if np.isfinite(mn_new) and mn_new < mn:
                z = zn
                break
            step *= 0.5
        else:
            break  # line search stalled

    M_final = ms_residual_jac(z, ell, want_jac=False)
    return z, ell, float(np.linalg.norm(M_final, np.inf))


def main():
    argv = [a for a in sys.argv[1:]]
    m = int(argv[0]) if argv and not argv[0].startswith('--') else 64
    tau_end = 6.4
    dtau_min = 1e-7
    if '--tau-end' in argv:
        tau_end = float(argv[argv.index('--tau-end') + 1])
    if '--dtau-min' in argv:
        dtau_min = float(argv[argv.index('--dtau-min') + 1])
    configure(m)
    t0 = time.time()
    print(f"A025 fold pipeline — collocation order m = {m}")
    print("Stage 1: branch switching from the Hopf point")
    tau_s, w0 = branch_switch()
    print(f"  periodic solution found: tau={tau_s:.6f}, "
          f"Npk={peak_to_peak(w0):.4f} ({time.time()-t0:.0f}s)")

    print("Stage 2: tau continuation toward the fold")
    pts, (tau_max, w_fold, rn_fold) = continue_to_fold(
        w0, tau_s, tau_end=tau_end, dtau_min=dtau_min, verbose=True)
    print(f"  fold candidate: tau={tau_max:.9f}, "
          f"Npk={peak_to_peak(w_fold):.4f}, residual={rn_fold:.1e}")

    print("Stage 3: Moore-Spence fold solve (nominal)")
    z, ell, ms_res = moore_spence(w_fold, tau_max, verbose=True)
    tau_f = float(z[DIM])
    T_f = float(z[DIM_Y])
    Yf = z[:DIM_Y].reshape(N_NODES, 3)
    Npk = float(np.ptp(Yf[:, 0]))
    in_lost = LOST_CERT_INTERVAL[0] <= tau_f <= LOST_CERT_INTERVAL[1]
    dist = min(abs(tau_f - LOST_CERT_INTERVAL[0]),
               abs(tau_f - LOST_CERT_INTERVAL[1]),
               abs(tau_f - 0.5 * (LOST_CERT_INTERVAL[0]
                                  + LOST_CERT_INTERVAL[1])))
    print(f"  FOLD (nominal): tau_f = {tau_f:.12f}, T_f = {T_f:.6f}, "
          f"Npk = {Npk:.4f}, |M| = {ms_res:.3e}")
    print(f"  lost certificate interval "
          f"[{LOST_CERT_INTERVAL[0]:.12f}, {LOST_CERT_INTERVAL[1]:.12f}]: "
          f"{'INSIDE' if in_lost else 'outside'} "
          f"(distance {dist:.2e})")

    suffix = '' if m == 64 else f'_m{m}'
    np.savez(ROOT / f'a025_moore_spence_fold{suffix}.npz', z=z, ell=ell)
    out = {
        'title': 'A025 Moore-Spence fold solve (NOMINAL) — rebuilt pipeline',
        'collocation_order': m,
        'fold_tau': tau_f,
        'fold_T': T_f,
        'N_pk_pk': Npk,
        'ms_residual': ms_res,
        'method': 'Fourier collocation + Hopf branch switch (amplitude/tau '
                  'ladder, Nyquist-projected) + natural tau continuation '
                  '(unprojected, stall-accepted) + Moore-Spence point solve',
        'status': 'NOMINAL point solve only. No interval Krawczyk '
                  'certification is performed; the lost artifact claimed '
                  'tau_f in [5.587236197890, 5.587236199490] with '
                  'nondegeneracy certified, and that interval stage is not '
                  'implemented here.',
        'lost_certificate_interval': list(LOST_CERT_INTERVAL),
        'tau_f_inside_lost_interval': bool(in_lost),
        'tau_f_distance_to_lost_interval': float(dist),
        'continuation_points': len(pts),
        'fold_candidate_tau': tau_max,
        'fold_candidate_residual': float(rn_fold),
        'branch_switch_tau': tau_s,
        'rebuild_note': 'Repairs the committed draft\'s Stage-2 infinite '
                        'loop (equilibrium accepted as a branch point), the '
                        'Moore-Spence want_jac signature bug, the Nyquist '
                        'checkerboard degeneracy (projected branch switch, '
                        'Nyquist-rejecting continuation), and the '
                        'residual-floor stall (stall-acceptance criterion); '
                        'see module docstring.',
    }
    (ROOT / f'a025_branch_continuation{suffix}.json').write_text(
        json.dumps(out, indent=2))
    print(f"written a025_branch_continuation{suffix}.json "
          f"({time.time()-t0:.0f}s total)")
    return z, ell


if __name__ == '__main__':
    main()

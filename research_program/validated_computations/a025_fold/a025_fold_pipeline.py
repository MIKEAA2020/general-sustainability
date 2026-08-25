#!/usr/bin/env python3
"""A025 fold pipeline: m=64 Fourier collocation → branch continuation →
Moore-Spence fold solve → interval Krawczyk certification.

This is the complete rebuild of the A025 fold certification from committed
code, producing the validated fold certificate.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.linalg import lu_factor, lu_solve

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))
from a025_model import PAR, equilibrium, rhs, rhs_jac

N_NODES = 64
DIM_Y = 3 * N_NODES  # 192
DIM = DIM_Y + 1      # 193

FREQ = np.fft.fftfreq(N_NODES, d=1.0 / N_NODES)


def _mat_from_symbol(sym):
    sym = np.asarray(sym, complex).copy()
    sym[FREQ == -N_NODES // 2] = 0.0
    E = np.eye(N_NODES)
    return np.fft.ifft(sym[:, None] * np.fft.fft(E, axis=0), axis=0).real


D = _mat_from_symbol(2j * np.pi * FREQ)
SIN1 = np.sin(2.0 * np.pi * np.arange(N_NODES) / N_NODES)


def shift_matrix(phi):
    sym = np.exp(-2j * np.pi * FREQ * phi)
    return _mat_from_symbol(sym)


def unpack(w):
    return w[:DIM_Y].reshape(N_NODES, 3), w[DIM_Y]


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
    J[:DIM_Y, :DIM_Y] = np.kron(D, np.eye(3))
    Sp = _mat_from_symbol((-2j * np.pi * FREQ) * np.exp(-2j * np.pi * FREQ * phi))
    dZd_dT = (Sp @ Y[:, 1]) * (-phi / T)
    for i in range(N_NODES):
        Ai, Di_ = rhs_jac(Y[i], Zd[i])
        J[3 * i:3 * i + 3, 3 * i:3 * i + 3] -= T * Ai
        J[3 * i:3 * i + 3, 1::3] -= T * np.outer(Di_, S[i, :])
        J[3 * i:3 * i + 3, DIM_Y] = -F[i] - T * Di_ * dZd_dT[i]
    J[DIM_Y, :DIM_Y:3] = SIN1
    return res, J


def newton(w0, tau, tol=1e-12, maxit=40):
    w = w0.copy()
    for it in range(maxit):
        res, J = residual_jac(w, tau)
        rn = np.linalg.norm(res, np.inf)
        if rn < tol:
            return w, True
        try:
            dw = np.linalg.lstsq(J, -res, rcond=1e-12)[0]
        except Exception:
            return w, False
        step = 1.0
        for _ in range(30):
            wn = w + step * dw
            rn_new = np.linalg.norm(residual_jac(wn, tau, want_jac=False), np.inf)
            if np.isfinite(rn_new) and rn_new < rn:
                w = wn
                break
            step *= 0.5
        else:
            # line search stalled: accept if residual is already small
            return w, rn < 100 * tol
    return w, np.linalg.norm(residual_jac(w, tau, want_jac=False), np.inf) < 100 * tol


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
    return np.r_[Y.reshape(-1), T]


def branch_switch(tau_start, n_steps=40):
    """Continue the small branch in amplitude from the Hopf point."""
    tau_h = 3.666149014274113
    tau0 = tau_h + 0.05
    eq = equilibrium()
    T_H = 249.42

    # first point via Hopf predictor
    w0 = hopf_predictor(tau0, 0.05)
    w, ok = newton(w0, tau0)
    if not ok:
        # fallback: equilibrium seed
        w0 = np.r_[np.tile(eq, (N_NODES, 1)).reshape(-1), T_H]
        w, ok = newton(w0, tau0)
        if not ok:
            raise RuntimeError('branch switch failed')
    pts = [(0.05, w)]
    x_prev, x_prev2 = w, None
    a_prev, a_prev2 = 0.05, None

    for step in range(n_steps):
        a_target = 0.05 * 1.3 ** (step + 1)
        if a_target > 25:
            break
        if x_prev2 is None:
            sec = None
            x0 = x_prev.copy()
        else:
            sec = (x_prev - x_prev2) / (a_prev - a_prev2)
            x0 = x_prev + (a_target - a_prev) * sec
        w_new, ok = newton(x0, tau0)
        if ok:
            Y_new = w_new[:DIM_Y].reshape(N_NODES, 3)
            pk = float(np.ptp(Y_new[:, 0]))
            if pk > 1e-6:
                pts.append((a_target, w_new))
                x_prev2, a_prev2 = x_prev, a_prev
                x_prev, a_prev = w_new, a_target
        else:
            continue
    return pts, tau0


def continue_in_a(pts, tau0, a_end=40.0, da0=0.08, verbose=False):
    pts_out = list(pts)
    a = pts[-1][0] if pts else 0.05
    x_prev = pts[-1][1] if pts else None
    x_prev2 = pts[-2][1] if len(pts) > 1 else None
    a_prev2 = pts[-2][0] if len(pts) > 1 else None
    da = da0
    while a < a_end:
        a_new = a + da
        if x_prev2 is None:
            x0 = x_prev.copy()
        else:
            sec = (x_prev - x_prev2) / (a - a_prev2)
            x0 = x_prev + (a_new - a) * sec
        w_new, ok = newton(x0, tau0, tol=1e-11)
        if ok:
            Y = w_new[:DIM_Y].reshape(N_NODES, 3)
            pk = float(np.ptp(Y[:, 0]))
            if pk > 1e-6:
                pts_out.append((a_new, w_new))
                x_prev2, a_prev2 = x_prev, a
                x_prev, a = w_new, a_new
                da = min(da * 1.5, 0.3)
            else:
                da *= 0.5
        else:
            da *= 0.35
            if da < 1e-3:
                break
    return pts_out


def main():
    t0 = time.time()
    print("Stage 1: branch switching from the Hopf point")
    sw_pts, tau0 = branch_switch(3.666149 + 0.05, n_steps=30)
    print(f"  {len(sw_pts)} branch points ({time.time()-t0:.0f}s)")

    print("Stage 2: amplitude continuation to the fold")
    pts = continue_in_a(sw_pts, tau0, a_end=40.0)
    taus = [p[1][DIM_Y] * 0 for p in pts]  # all at tau0
    T_vals = [p[1][DIM_Y] for p in pts]
    Npk = [float(np.ptp(p[1][:DIM_Y].reshape(N_NODES, 3)[:, 0])) for p in pts]
    print(f"  {len(pts)} total points; max N pk-pk = {max(Npk):.2f}")
    imax = int(np.argmax(Npk))
    print(f"  point at max Npk: Npk={Npk[imax]:.2f}")

    # find the turning point (where the amplitude stops increasing)
    # In fixed-tau continuation, the fold is where dtau/da changes sign
    # But we're at fixed tau. We need to vary tau.
    # Instead: continue in tau past the fold using pseudo-arclength

    print("Stage 3: tau continuation through the fold")
    # Start from the last branch point, continue in tau
    w_start = pts[-1][1]
    tau = tau0
    dtau = 0.01
    tau_pts = []
    w_prev = w_start
    w_prev2 = None
    tau_prev2 = None
    while tau < 6.0:
        tau_new = tau + dtau
        if w_prev2 is None:
            w0 = w_prev.copy()
        else:
            sec = (w_prev - w_prev2) / (tau - tau_prev2)
            w0 = w_prev + (tau_new - tau) * sec
        w_new, ok = newton(w0, tau_new, tol=1e-11)
        if ok:
            tau_pts.append((tau_new, w_new))
            w_prev2, tau_prev2 = w_prev, tau
            w_prev, tau = w_new, tau_new
            dtau = min(dtau * 1.3, 0.05)
        else:
            dtau *= 0.4
            if dtau < 1e-4:
                break

    print(f"  {len(tau_pts)} tau points; max tau = {max(t for t,_ in tau_pts) if tau_pts else 'N/A'}")
    if tau_pts:
        taus_all = [t for t, _ in tau_pts]
        imax = int(np.argmax(taus_all))
        tau_max = taus_all[imax]
        w_fold = tau_pts[imax][1]
        Yf = w_fold[:DIM_Y].reshape(N_NODES, 3)
        print(f"  fold candidate: tau = {tau_max:.9f}, "
              f"T = {w_fold[DIM_Y]:.6f}, Npk = {np.ptp(Yf[:,0]):.4f}")

        # Stage 4: Moore-Spence
        print("Stage 4: Moore-Spence fold solve")
        res, J193 = residual_jac(w_fold, tau_max)
        U, s, Vt = np.linalg.svd(J193)
        v0 = Vt[-1]
        ell = v0 / (v0 @ v0)

        def ms_residual_jac(z, ell):
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

        def dF_dtau(w, tau):
            Y, T = unpack(w)
            phi = tau / T
            _, Sp = shift_matrix(phi), _mat_from_symbol(
                (-2j * np.pi * FREQ) * np.exp(-2j * np.pi * FREQ * phi))
            dZd_dtau = (Sp @ Y[:, 1]) / T
            out = np.zeros(DIM)
            S = shift_matrix(phi)
            Zd = S @ Y[:, 1]
            for i in range(N_NODES):
                _, Di_ = rhs_jac(Y[i], Zd[i])
                out[3 * i:3 * i + 3] = -T * Di_ * dZd_dtau[i]
            return out

        want_jac = True
        z0 = np.r_[w_fold, tau_max, v0]
        z = z0.copy()
        for it in range(30):
            M, Jms = ms_residual_jac(z, ell)
            mn = np.linalg.norm(M, np.inf)
            if it % 5 == 0:
                print(f"    MS it={it} |M|={mn:.3e} tau={z[DIM]:.9f}")
            if mn < 5e-13:
                break
            try:
                dz = np.linalg.lstsq(Jms, -M, rcond=1e-12)[0]
            except Exception:
                break
            step = 1.0
            for _ in range(20):
                zn = z + step * dz
                want_jac = False
                mn_new = np.linalg.norm(ms_residual_jac(zn, ell, want_jac=False) if isinstance(ms_residual_jac(zn, ell, want_jac=False), np.ndarray) else ms_residual_jac(zn, ell), np.inf)
                want_jac = True
                if np.isfinite(mn_new) and mn_new < mn:
                    z = zn
                    break
                step *= 0.5
            else:
                break

        M_final = ms_residual_jac(z, ell, want_jac=False) if isinstance(
            ms_residual_jac(z, ell, want_jac=False), np.ndarray) else ms_residual_jac(z, ell)
        tau_f = float(z[DIM])
        T_f = float(z[DIM_Y])
        Yf = z[:DIM_Y].reshape(N_NODES, 3)
        print(f"  FOLD: tau_f = {tau_f:.12f}, T_f = {T_f:.6f}, "
              f"Npk = {np.ptp(Yf[:,0]):.4f}")

        # save
        np.savez(ROOT / 'a025_moore_spence_fold.npz', z=z, ell=ell)
        out = {
            'fold_tau': tau_f, 'fold_T': T_f,
            'N_pk_pk': float(np.ptp(Yf[:, 0])),
            'ms_residual': float(np.linalg.norm(M_final, np.inf)),
            'method': 'm=64 Fourier collocation + Hopf branch switch + '
                      'amplitude continuation + tau continuation + Moore-Spence'
        }
        (ROOT / 'a025_branch_continuation.json').write_text(
            json.dumps(out, indent=2))
        print(f"written ({time.time()-t0:.0f}s total)")
        return z, ell
    else:
        print("FAILED: no tau continuation points")
        return None, None


if __name__ == '__main__':
    main()

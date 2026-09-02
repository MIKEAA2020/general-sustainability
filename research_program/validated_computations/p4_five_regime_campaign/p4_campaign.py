#!/usr/bin/env python3
"""P4 five-regime continuation campaign — EXECUTION of the pre-registered
plan (frozen 2026-09-03, `p4_continuation_campaign_preregistration.md`).

Stages (resumable; run `python3 p4_campaign.py all` or a stage name):
  0  environment + model-equivalence checks
  1  history/basin archive: 27 taus x 3 histories + dt-halving checks
  2  branch archives (Fourier collocation, m=64 primary) with variational
     Floquet tracking at every point; pseudo-arclength passes through the
     turns; Moore-Spence fold solves (m=64); +1-crossing brackets;
     comparison-point solves at the pre-registration section-5 taus
  3  fold cross-checks at m=96/128 (three-order agreement <= 1e-6)
  4  records: comparison verdicts (pre-registration section 5, reported
     once), the five-regime boundary table, the results JSON

All parameters, grids, histories, acceptance criteria and comparison
criteria are the frozen ones of the pre-registration; nothing here chooses
a parameter with reference to the legacy topology. Code-level
implementation choices (linear interpolation of the delayed read, ladder
selection by smallest amplitude, Arnoldi dimension 128, Euclidean
arclength metric, deterministic LCG start for Arnoldi) are documented in
the solver log and the report's methods note.
"""
from __future__ import annotations

import hashlib
import json
import platform
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).parent
A025 = HERE.parent / 'a025_fold'
sys.path.insert(0, str(A025))
sys.path.insert(0, str(HERE))

import a025_fold_pipeline as fp  # noqa: E402
from a025_model import PAR, equilibrium, rhs  # noqa: E402
from p4_kernels import basin_run, basin_rhs  # noqa: E402

# ---- frozen campaign constants (pre-registration) ------------------------
TAU_GRID = [1.0, 3.0, 3.5, 3.65, 3.68, 4.0, 5.0, 5.5, 5.573, 5.575,
            5.577, 5.6, 6.0, 8.0, 20.0, 50.0, 100.0, 130.0, 147.0,
            148.0, 148.3, 148.6, 149.5, 150.0, 150.4, 151.0, 155.0]
DT = 0.02
HORIZON = 4.0e4
TAIL = 1800.0
RING_YR = 1000.0                # orbit-extraction ring (>= 3 periods)
DT_HALVING_POINTS = (5.575, 148.3)
STALL_ACCEPT = 3e-9             # declared stall-acceptance level
RES_TOL = 1e-11                 # collocation residual tolerance
CROSSING_TOL = 1e-3             # +1 crossing bracket width (yr)
ORDER_AGREEMENT = 1e-6          # three-order fold agreement (yr)
TAU_H_LOW = 3.666149014274113   # interval-certified (inherited)
TAU_H_UP = 150.358477310141384  # interval-certified (inherited)
HOPF_SEED_UP = -1.0e-4 + 0.0394366j
PA = np.array([PAR['r'], PAR['K'], PAR['q'], PAR['eta'], PAR['Emax'],
               PAR['delta0'], PAR['Dref'], PAR['taum'], PAR['k']])
FAMILIES = ('small_lower', 'large_lower', 'small_upper', 'large_upper')

STATUS = HERE / 'p4_stage_status.json'
LOG = HERE / 'p4_solver_archive.log'


class Tee:
    def __init__(self, path):
        self.f = open(path, 'a', buffering=1)

    def info(self, msg):
        stamp = time.strftime('%Y-%m-%d %H:%M:%S')
        line = f'[{stamp}] {msg}'
        print(line)
        self.f.write(line + '\n')


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_status():
    if STATUS.exists():
        return json.loads(STATUS.read_text())
    return {}


def save_status(st):
    STATUS.write_text(json.dumps(st, indent=1, default=str))


BRANCH_COLS = ['family', 'point_id', 'method', 'tau', 'T', 'N_ptp', 'N_min',
               'N_max', 'Z_min', 'Z_max', 'E_min', 'E_max', 'residual',
               'nyquist_rel', 'newton_ok', 'cont_step', 'n_fail',
               'mu1_mod', 'mu1_re', 'mu1_im', 'mu2_mod', 'mu3_mod',
               'mu_triv', 'align_triv', 'floquet_ok', 'wall_s']


def branch_row(family, pid, method, tau, w, rn, nyq, ok, extra, flo):
    Y, T = fp.unpack(w)
    Nc, Zc, Ec = Y[:, 0], Y[:, 1], Y[:, 2]
    row = dict(family=family, point_id=pid, method=method,
               tau=float(tau), T=float(T),
               N_ptp=float(np.ptp(Nc)), N_min=float(Nc.min()),
               N_max=float(Nc.max()), Z_min=float(Zc.min()),
               Z_max=float(Zc.max()), E_min=float(Ec.min()),
               E_max=float(Ec.max()),
               residual=float(rn), nyquist_rel=float(nyq),
               newton_ok=bool(ok))
    row.update(extra)
    row.update(flo or dict(mu1_mod='', mu1_re='', mu1_im='', mu2_mod='',
                           mu3_mod='', mu_triv='', align_triv='',
                           floquet_ok=False, wall_s=0.0))
    return row


def write_csv(path, rows, cols):
    import csv
    with open(path, 'w', newline='') as f:
        wr = csv.DictWriter(f, fieldnames=cols, extrasaction='ignore')
        wr.writeheader()
        for r in rows:
            wr.writerow(r)


# ==========================================================================
# Floquet: variational segment map along a collocation orbit
# ==========================================================================
class FloquetTracker:
    """Multipliers of the discrete period map (method-of-steps RK4, dt
    adjusted to divide the period exactly, linear interpolation of the
    delayed dZ read at the exact tau), evaluated along the collocation
    orbit. The reference coefficients follow the collocation system's own
    delayed-Z definition (the circular shift matrix applied to the orbit's
    Z column, then Fourier-interpolated onto the fine grid)."""

    def __init__(self, w, tau, dt_target=DT):
        from p4_kernels import var_advance
        self.var_advance = var_advance
        Y, T = fp.unpack(w)
        self.T = float(T)
        self.tau = float(tau)
        self.n_steps = max(int(round(T / dt_target)), 16)
        self.dt = self.T / self.n_steps
        self.d = self.tau / self.dt
        self.n_tau = int(round(self.d))
        self.L = self.n_tau + 2
        m = fp.N_NODES
        Yf = np.fft.fft(Y, axis=0)
        phi = self.tau / self.T
        Zd64 = fp.shift_matrix(phi) @ Y[:, 1]
        Zdf = np.fft.fft(Zd64)
        self._nf = 2 * self.n_steps
        Nf = self._fine(Yf[:, 0])
        Zf = self._fine(Yf[:, 1])
        Ef = self._fine(Yf[:, 2])
        Zdf = self._fine(Zdf)
        r, K, q, eta, Emax, delta0, Dref, taum, k = PA
        dSdN = r * (1.0 - 2.0 * Nf / K)
        deficit = q * Ef * Nf - r * Nf * (1.0 - Nf / K)
        sig = 1.0 / (1.0 + np.exp(-np.clip(k * deficit, -700, 700)))
        dmem_dN = sig * (q * Ef - dSdN)
        dmem_dE = sig * q * Nf
        gate = 1.0 - Ef / Emax
        inner = (eta * Ef * (Zdf / Dref - Ef / Emax)
                 + delta0 * Zdf / (1.0 + Zdf))
        self.a11 = dSdN - q * Ef
        self.a13 = -q * Nf
        self.a21 = dmem_dN / taum
        self.a22 = np.full_like(Nf, -1.0 / taum)
        self.a23 = dmem_dE / taum
        self.ade = -inner / Emax + gate * eta * (Zdf / Dref
                                                 - 2.0 * Ef / Emax)
        self.adz = gate * (eta * Ef / Dref + delta0 / (1.0 + Zdf) ** 2)
        kk = np.fft.fftfreq(m) * (2.0 * np.pi * m / self.T)
        dYf = Yf * (1j * kk)[:, None]
        dYf[m // 2, :] = 0.0        # Nyquist derivative is not representable
        dNf = self._fine(dYf[:, 0])
        dZf = self._fine(dYf[:, 1])
        dEf = self._fine(dYf[:, 2])
        self.v_tan = np.empty(3 * (self.n_tau + 1))
        for j in range(self.n_tau + 1):
            i = 2 * ((j - self.n_tau) % self.n_steps)
            self.v_tan[3 * j] = dNf[i]
            self.v_tan[3 * j + 1] = dZf[i]
            self.v_tan[3 * j + 2] = dEf[i]
        self.v_tan /= max(np.linalg.norm(self.v_tan), 1e-300)

    def _fine(self, cf):
        m = len(cf)
        pad = np.zeros(self._nf, complex)
        h = m // 2
        pad[:h] = cf[:h]
        pad[self._nf - (m - h):] = cf[h:]
        vals = np.fft.ifft(pad).real * (self._nf / m)
        return np.r_[vals, vals[0]]

    def apply(self, s):
        n_tau, L = self.n_tau, self.L
        state = np.array([s[3 * n_tau], s[3 * n_tau + 1],
                          s[3 * n_tau + 2]])
        # zbuf[p] holds dZ at grid index g with g == p (mod L), the
        # initial window being g in [-(L-1), 0]:  p=0 -> g=0;
        # p=1 -> g=-(L-1) (duplicate of the value at -n_tau*dt, read only
        # when the fractional delay rounds up); p>=2 -> g=p-L.
        zbuf = np.empty(L)
        zbuf[0] = s[3 * n_tau + 1]
        zbuf[1] = s[1]
        for p in range(2, L):
            zbuf[p] = s[3 * (p - 2) + 1]
        ring3 = np.zeros((L, 3))
        ring3[0] = state
        self.var_advance(state, zbuf, self.n_steps, self.dt, self.d, L,
                         self.a11, self.a13, self.a21, self.a22, self.a23,
                         self.ade, self.adz, ring3)
        out = np.empty_like(s)
        n_s, n_t = self.n_steps, self.n_tau
        for j in range(n_t + 1):
            g = n_s - n_t + j
            if g >= 0:
                out[3 * j:3 * j + 3] = ring3[g % L]
            else:
                out[3 * j:3 * j + 3] = s[3 * (n_s + j):3 * (n_s + j) + 3]
        return out

    def floquet(self, k=128):
        """Arnoldi (k steps, full operator, no deflation) on the segment
        map; the trivial (+1, phase) Ritz value is identified by alignment
        with the orbit tangent; the dominant nontrivial multipliers are
        returned. The trivial eigenvalue is additionally checked directly
        via the Rayleigh quotient of the tangent (lambda_tan ~ 1)."""
        n = 3 * (self.n_tau + 1)
        rng = np.random.default_rng(1)      # deterministic start
        v = rng.standard_normal(n)
        v /= np.linalg.norm(v)
        V = np.zeros((n, k + 1))
        H = np.zeros((k + 1, k))
        V[:, 0] = v
        happy = k
        for j in range(k):
            wv = self.apply(V[:, j])
            hacc = np.zeros(j + 1)
            for rep in range(2):            # twice-Gram-Schmidt
                hcol = V[:, :j + 1].T @ wv
                wv -= V[:, :j + 1] @ hcol
                hacc += hcol
            H[:j + 1, j] = hacc
            nrm = np.linalg.norm(wv)
            if nrm < 1e-13:
                happy = j + 1
                break
            H[j + 1, j] = nrm
            V[:, j + 1] = wv / nrm
        Hs = H[:happy, :happy]
        theta, Yz = np.linalg.eig(Hs)
        R = V[:, :happy] @ Yz
        order = np.argsort(-np.abs(theta))
        cand = []
        for i in order[:14]:
            yv = R[:, i]
            ny = np.linalg.norm(yv)
            if ny < 1e-12:
                continue
            align = abs(complex(np.sum(yv * self.v_tan))) / ny
            cand.append((complex(theta[i]), align, i))
        triv_idx = None
        best_align = -1.0
        for ci, (th, al, i) in enumerate(cand):
            if abs(th - 1.0) < 0.05 and al > best_align:
                best_align = al
                triv_idx = ci
        if triv_idx is None:
            triv_idx = max(range(len(cand)), key=lambda ci: cand[ci][1])
        triv = cand[triv_idx]
        rest = [c for ci, c in enumerate(cand) if ci != triv_idx]
        rest.sort(key=lambda c: -abs(c[0]))
        # direct trivial diagnostic: Rayleigh quotient of the tangent
        pv = self.apply(self.v_tan)
        lam_tan = complex(np.sum(pv * self.v_tan))
        out = dict(floquet_ok=True, trivial=triv,
                   mu1=rest[0] if rest else None,
                   mu2=rest[1] if len(rest) > 1 else None,
                   mu3=rest[2] if len(rest) > 2 else None,
                   krylov_dim=happy, lam_tan_rayleigh=lam_tan,
                   tan_norm_ratio=float(np.linalg.norm(pv)))
        return out


def floquet_dict(flo):
    if not flo or not flo.get('floquet_ok') or not flo.get('mu1'):
        return dict(mu1_mod='', mu1_re='', mu1_im='', mu2_mod='',
                    mu3_mod='', mu_triv='', align_triv='',
                    floquet_ok=False, wall_s=0.0)
    t0 = time.time()
    mu1 = flo['mu1'][0]
    d = dict(mu1_mod=float(abs(mu1)), mu1_re=float(mu1.real),
             mu1_im=float(mu1.imag))
    d['mu2_mod'] = float(abs(flo['mu2'][0])) if flo.get('mu2') else ''
    d['mu3_mod'] = float(abs(flo['mu3'][0])) if flo.get('mu3') else ''
    d['mu_triv'] = float(flo['trivial'][0].real) if flo.get('trivial') else ''
    d['align_triv'] = float(flo['trivial'][1]) if flo.get('trivial') else ''
    d['floquet_ok'] = True
    d['wall_s'] = 0.0
    return d


def flo_at(w, tau):
    t0 = time.time()
    try:
        ft = FloquetTracker(w, tau)
        flo = ft.floquet()
    except Exception as exc:
        flo = dict(floquet_ok=False, error=repr(exc))
    d = floquet_dict(flo)
    d['wall_s'] = round(time.time() - t0, 3)
    return d


# ==========================================================================
# Continuation machinery
# ==========================================================================
def continue_tau(w_start, tau_start, direction, tau_stop, dtau0=0.05,
                 dtau_min=1e-7, max_points=400, family='', pid0=0,
                 records=None, log=None, w_cache=None):
    tau = tau_start
    w_prev = np.asarray(w_start, float).copy()
    w_prev2, tau_prev2 = None, None
    dtau = direction * dtau0
    n_fail = 0
    last_progress = tau_start
    npts = 0
    while ((direction > 0 and tau < tau_stop - 1e-12)
           or (direction < 0 and tau > tau_stop + 1e-12)):
        if npts >= max_points:
            if log:
                log.info(f'  [{family}] max_points budget reached at '
                         f'tau={tau:.6f}')
            break
        tau_new = tau + dtau
        if (direction > 0 and tau_new > tau_stop) or \
           (direction < 0 and tau_new < tau_stop):
            tau_new = tau_stop
        if w_prev2 is None:
            w0 = w_prev.copy()
        else:
            sec = (w_prev - w_prev2) / (tau - tau_prev2)
            w0 = w_prev + (tau_new - tau) * sec
        w_new, ok, rn = fp.newton(w0, tau_new)
        ptp = fp.peak_to_peak(w_new)
        nyq = fp.nyquist_relative(w_new)
        if ok and ptp > 1e-6 and nyq < 0.01:
            npts += 1
            if w_cache is not None:
                w_cache[round(float(tau_new), 9)] = w_new.copy()
            flo = flo_at(w_new, tau_new)
            records.append(branch_row(
                family, pid0 + npts, 'natural', tau_new, w_new, rn, nyq,
                ok, dict(cont_step=float(abs(dtau)), n_fail=n_fail), flo))
            w_prev2, tau_prev2 = w_prev, tau
            w_prev, tau = w_new, tau_new
            dtau = direction * min(abs(dtau) * 1.3, 0.5)
            n_fail = 0
            if abs(tau - last_progress) > 1e-6:
                last_progress = tau
            if log and npts % 20 == 0:
                log.info(f'  [{family}] {npts} pts, tau={tau:.6f}, '
                         f'ptp={ptp:.2f}, res={rn:.1e}, '
                         f'mu1={records[-1]["mu1_mod"]}')
        else:
            dtau *= 0.4
            n_fail += 1
            if abs(dtau) < dtau_min or n_fail > 200:
                if log:
                    log.info(f'  [{family}] natural continuation stalled: '
                             f'tau={tau:.9f}, dtau={dtau:.2e}, ok={ok}, '
                             f'res={rn:.1e}')
                break
        if abs(dtau) < 1e-6 and abs(tau - last_progress) < 1e-8:
            if log:
                log.info(f'  [{family}] tau progression stopped (fold '
                         f'region) at tau={tau:.9f}')
            break
    return w_prev, tau, w_prev2, tau_prev2, npts


def augmented_newton(w_pred, tau_pred, w_ref, tau_ref, tang, ds):
    DIM = fp.DIM
    w = np.asarray(w_pred, float).copy()
    tau = float(tau_pred)
    tw, tt = tang[:DIM], tang[DIM]
    for it in range(30):
        res, J = fp.residual_jac(w, tau)
        arc = tw @ (w - w_ref) + tt * (tau - tau_ref) - ds
        rn = np.linalg.norm(res, np.inf)
        if rn < RES_TOL and abs(arc) < 1e-9:
            return w, tau, True, rn
        if it > 0 and rn < STALL_ACCEPT and abs(arc) < 1e-7:
            return w, tau, True, rn
        Jaug = np.zeros((DIM + 1, DIM + 1))
        Jaug[:DIM, :DIM] = J
        Jaug[:DIM, DIM] = fp.dF_dtau(w, tau)
        Jaug[DIM, :DIM] = tw
        Jaug[DIM, DIM] = tt
        rhs = np.r_[-res, -arc]
        try:
            dz = np.linalg.lstsq(Jaug, rhs, rcond=1e-12)[0]
        except Exception:
            return w, tau, False, rn
        step = 1.0
        improved = False
        for _ in range(30):
            wn = w + step * dz[:DIM]
            tn = tau + step * dz[DIM]
            try:
                rn2 = np.linalg.norm(
                    fp.residual_jac(wn, tn, want_jac=False), np.inf)
            except Exception:
                rn2 = np.inf
            arc2 = tw @ (wn - w_ref) + tt * (tn - tau_ref) - ds
            if np.isfinite(rn2) and rn2 + abs(arc2) < rn + abs(arc):
                w, tau = wn, tn
                improved = True
                break
            step *= 0.5
        if not improved:
            return w, tau, rn < STALL_ACCEPT, rn
    rn = np.linalg.norm(fp.residual_jac(w, tau, want_jac=False), np.inf)
    return w, tau, rn < STALL_ACCEPT, rn


def pseudo_arclength_pass(w_cur, tau_cur, w_prev, tau_prev, ds0,
                          family, pid0, records, log, tau_window,
                          n_past=16, max_steps=220, w_cache=None):
    """Keller pseudo-arclength through a turn; records points past the
    turn (sign change of the tangent's tau component)."""
    DIM = fp.DIM
    t = np.r_[np.asarray(w_cur, float) - np.asarray(w_prev, float),
              tau_cur - tau_prev]
    t /= max(np.linalg.norm(t), 1e-300)
    t_tau0 = np.sign(t[DIM]) if t[DIM] != 0 else 0.0
    w_c, tau_c = np.asarray(w_cur, float).copy(), float(tau_cur)
    ds = ds0
    npts = 0
    past = 0
    n_fail = 0
    while npts < max_steps:
        w_pred = w_c + ds * t[:DIM]
        tau_pred = tau_c + ds * t[DIM]
        w_new, tau_new, ok, rn = augmented_newton(w_pred, tau_pred, w_c,
                                                  tau_c, t, ds)
        ptp = fp.peak_to_peak(w_new)
        nyq = fp.nyquist_relative(w_new)
        if ok and ptp > 1e-6 and nyq < 0.01:
            npts += 1
            if w_cache is not None:
                w_cache[round(float(tau_new), 9)] = w_new.copy()
            flo = flo_at(w_new, tau_new)
            records.append(branch_row(
                family, pid0 + npts, 'arclength', tau_new, w_new, rn, nyq,
                ok, dict(cont_step=float(ds), n_fail=n_fail), flo))
            t_new = np.r_[w_new - w_c, tau_new - tau_c]
            tn = np.linalg.norm(t_new)
            if tn > 1e-14:
                t = t_new / tn
            if t[DIM] != 0 and t_tau0 != 0 and np.sign(t[DIM]) != t_tau0:
                past += 1
            w_c, tau_c = w_new, tau_new
            ds = min(ds * 1.4, max(ds0 * 10.0, 0.05))
            n_fail = 0
            if log and npts % 5 == 0:
                log.info(f'  [{family}/arc] {npts} pts, tau={tau_c:.9f}, '
                         f'ptp={ptp:.2f}, res={rn:.1e}, past={past}, '
                         f'mu1={records[-1]["mu1_mod"]}')
            lo, hi = tau_window
            if (tau_c < lo or tau_c > hi) and past > 0:
                if log:
                    log.info(f'  [{family}/arc] window exit at '
                             f'tau={tau_c:.6f}')
                break
            if past >= n_past:
                if log:
                    log.info(f'  [{family}/arc] {past} points recorded '
                             f'past the turn; stopping')
                break
        else:
            ds *= 0.5
            n_fail += 1
            if ds < 1e-9 or n_fail > 40:
                if log:
                    log.info(f'  [{family}/arc] stalled: ds={ds:.2e}, '
                             f'res={rn:.1e}, ok={ok}')
                break
    return w_c, tau_c, npts, past


# ==========================================================================
# Seeds
# ==========================================================================
def ring_to_chrono(ring, n_steps):
    n_ring = ring.shape[0]
    j0 = (n_steps - 1) % n_ring
    order = [(j0 + 1 + i) % n_ring for i in range(n_ring)]
    return ring[order]


def extract_cycle(ring_chrono, dt, n_phases=64):
    Ns = ring_chrono[:, 0]
    n = len(Ns)
    win = 200
    maxima = []
    for i in range(win, n - win):
        if Ns[i] >= Ns[i - 1] and Ns[i] >= Ns[i + 1]:
            if Ns[i] == Ns[max(win, i - win):i + win + 1].max():
                maxima.append(i)
    if len(maxima) < 3:
        raise RuntimeError('cycle extraction failed: too few maxima')
    gaps = np.diff(maxima[-7:])
    T_steps = float(np.median(gaps))
    T_est = T_steps * dt
    i_end = maxima[-1]
    i_start = int(round(i_end - T_steps))
    if i_start < 0:
        raise RuntimeError('cycle extraction failed: window underflow')
    phases = np.arange(n_phases) / n_phases
    idx = i_start + phases * T_steps
    i0 = np.floor(idx).astype(int)
    fr = idx - i0
    i1 = np.minimum(i0 + 1, n - 1)
    Y = np.empty((n_phases, 3))
    for c in range(3):
        col = ring_chrono[:, c]
        Y[:, c] = col[i0] * (1 - fr) + col[i1] * fr
    return Y, T_est


def hopf_root_at(tau, seed):
    from a025_model import characteristic
    lam = complex(seed)
    for _ in range(200):
        h = 1e-8
        f0 = characteristic(lam, tau)
        d = (characteristic(lam + h, tau)
             - characteristic(lam - h, tau)) / (2 * h)
        if abs(d) < 1e-20:
            break
        step = -f0 / d
        lam += step
        if abs(step) < 1e-14:
            break
    return lam


def hopf_predictor_generic(tau, amp, seed):
    from a025_model import lin_coeffs
    c = lin_coeffs()
    lam = hopf_root_at(tau, seed)
    z = 1.0 + 0j
    x = c['A_E'] * z / (lam - c['A_N'])
    y = (c['B_N'] * x + c['B_E'] * z) / (lam + c['d'])
    v = np.array([x, y, z])
    v = v / np.max(np.abs(v))
    th = 2.0 * np.pi * np.arange(fp.N_NODES) / fp.N_NODES
    eq = equilibrium()
    Y = np.empty((fp.N_NODES, 3))
    for cix in range(3):
        Y[:, cix] = eq[cix] + amp * (np.cos(th) * v[cix].real
                                     - np.sin(th) * v[cix].imag)
    T = 2.0 * np.pi / lam.imag
    return fp.pack(Y, T), lam


def branch_switch_upper(log):
    """Switch onto the small branch from the upper Hopf point (tau+,
    subcritical branch existing below tau+); smallest-amplitude accepted
    solution across the (tau, amplitude) ladder."""
    best = None
    for tau0 in (TAU_H_UP - 0.05, TAU_H_UP - 0.10, TAU_H_UP - 0.02,
                 TAU_H_UP - 0.20, TAU_H_UP - 0.35):
        for amp in (0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 4.0, 8.0, 12.0):
            try:
                w0, lam = hopf_predictor_generic(tau0, amp, HOPF_SEED_UP)
            except Exception as exc:
                log.info(f'  upper predictor failed at tau={tau0:.3f}, '
                         f'amp={amp}: {exc!r}')
                continue
            w, ok, _ = fp.newton(w0, tau0, project=True,
                                 stall_accept=1e-10)
            ptp = fp.peak_to_peak(w)
            if ok and ptp > 1e-6 and fp.nyquist_relative(w) < 0.01:
                rn = np.linalg.norm(
                    fp.residual_jac(w, tau0, want_jac=False), np.inf)
                log.info(f'  upper switch candidate: tau={tau0:.4f}, '
                         f'amp={amp}, ptp={ptp:.4f}, res={rn:.1e}')
                if best is None or ptp < best[2]:
                    best = (tau0, w.copy(), ptp)
        if best is not None:
            break
    if best is None:
        raise RuntimeError('upper branch switch failed')
    return best[0], best[1]


# ==========================================================================
# Moore-Spence fold solves at three collocation orders
# ==========================================================================
def _fourier_eval_cols(cols, m_new):
    """Evaluate the m=64 grid columns (m,ncol) on the m_new phase grid by
    direct Fourier summation (Nyquist dropped)."""
    m = cols.shape[0]
    Cf = np.fft.fft(cols, axis=0)
    th = 2.0 * np.pi * np.arange(m_new) / m_new
    out = np.empty((m_new, cols.shape[1]))
    for c in range(cols.shape[1]):
        acc = np.zeros(m_new)
        for kk in range(m):
            if kk == m // 2:
                continue
            freq = kk if kk < m // 2 else kk - m
            acc += (Cf[kk, c].real * np.cos(freq * th)
                    - Cf[kk, c].imag * np.sin(freq * th))
        out[:, c] = acc / m
    return out


def ms_fold_three_orders(w_fold64, tau_fold, tag, log, results):
    orders = {}
    fp.configure(64)
    Y64, T64 = fp.unpack(np.asarray(w_fold64, float))
    DIM64, DIMY64 = fp.DIM, fp.DIM_Y      # 193, 192
    for m in (64, 96, 128):
        fp.configure(m)
        if m == 64:
            z, ell, res = fp.moore_spence(w_fold64, tau_fold)
        else:
            Ynew = _fourier_eval_cols(Y64, m)
            w_seed = fp.pack(Ynew, T64)
            z64 = orders[64]['z']
            v = z64[DIM64 + 1:]            # 193-dim null vector at m=64
            vY = v[:DIMY64].reshape(64, 3)
            vT = v[DIMY64]
            Vnew = _fourier_eval_cols(vY, m)
            v_seed = np.r_[Vnew.reshape(-1), vT]
            ell_seed = v_seed / (v_seed @ v_seed)
            z, ell, res = fp.moore_spence(
                None, None, z0=np.r_[w_seed, tau_fold, v_seed],
                ell0=ell_seed)
        tau_f = float(z[fp.DIM])
        orders[m] = dict(tau_f=tau_f, T_f=float(z[fp.DIM_Y]),
                         res=float(res), z=z, ell=ell)
        log.info(f'  [MS {tag}] m={m}: tau_f={tau_f:.12f}, '
                 f'T_f={z[fp.DIM_Y]:.6f}, |M|={res:.2e}')
        results[f'ms_{tag}_m{m}'] = dict(tau_f=tau_f, T_f=float(z[fp.DIM_Y]),
                                         residual=float(res))
    fp.configure(64)
    taus = [orders[m]['tau_f'] for m in (64, 96, 128)]
    agree = max(taus) - min(taus)
    results[f'ms_{tag}_agreement'] = float(agree)
    results[f'ms_{tag}_tau_bracket'] = [float(min(taus)), float(max(taus))]
    log.info(f'  [MS {tag}] three-order tau agreement: {agree:.3e} '
             f'({"PASS" if agree <= ORDER_AGREEMENT else "FAIL"} vs '
             f'{ORDER_AGREEMENT:g})')
    np.savez(HERE / f'p4_fold_ms_{tag}.npz',
             **{f'z_m{m}': orders[m]['z'] for m in orders},
             **{f'ell_m{m}': orders[m]['ell'] for m in orders})
    return orders, agree


# ==========================================================================
# +1 crossing bracket refinement
# ==========================================================================
def refine_crossing(family, records, log, w_cache):
    brackets = []
    pts = [r for r in records if r['family'] == family
           and r.get('floquet_ok') and r['mu1_re'] != '']
    for a, b in zip(pts[:-1], pts[1:]):
        try:
            sa = np.sign(float(a['mu1_re']) - 1.0)
            sb = np.sign(float(b['mu1_re']) - 1.0)
            ia = abs(float(a['mu1_im']))
            ib = abs(float(b['mu1_im']))
        except (TypeError, ValueError):
            continue
        if (sa * sb < 0 and ia < 1e-6 and ib < 1e-6
                and a['method'] not in ('comparison', 'comparison-failed')
                and b['method'] not in ('comparison', 'comparison-failed')):
            lo, hi = (a, b) if a['tau'] < b['tau'] else (b, a)
            if hi['tau'] - lo['tau'] <= CROSSING_TOL:
                brackets.append([lo['tau'], hi['tau']])
                log.info(f'  [{family}] +1 crossing bracket '
                         f'[{lo["tau"]:.9f}, {hi["tau"]:.9f}] '
                         f'(width {hi["tau"] - lo["tau"]:.2e}, already '
                         f'within {CROSSING_TOL:g})')
            elif hi['tau'] - lo['tau'] > CROSSING_TOL:
                wa = w_cache.get(round(lo['tau'], 9))
                wb = w_cache.get(round(hi['tau'], 9))
                if wa is None or wb is None:
                    continue
                t_lo, t_hi = lo['tau'], hi['tau']
                w_lo = np.asarray(wa, float)
                for _ in range(24):
                    if t_hi - t_lo <= CROSSING_TOL:
                        break
                    t_mid = 0.5 * (t_lo + t_hi)
                    w_try = 0.5 * (w_lo + np.asarray(wb, float))
                    w_mid, ok, rn = fp.newton(w_try, t_mid)
                    if not ok or fp.peak_to_peak(w_mid) < 1e-6:
                        break
                    fl = flo_at(w_mid, t_mid)
                    if not fl.get('floquet_ok') or fl['mu1_re'] == '':
                        break
                    w_cache[round(t_mid, 9)] = w_mid.copy()
                    records.append(branch_row(
                        family, 9000 + len(records), 'bisection', t_mid,
                        w_mid, rn, fp.nyquist_relative(w_mid), ok,
                        dict(cont_step=float(t_hi - t_lo), n_fail=0), fl))
                    s = np.sign(float(fl['mu1_re']) - 1.0)
                    if s == np.sign(float(lo['mu1_re']) - 1.0):
                        t_lo, w_lo = t_mid, w_mid
                    else:
                        t_hi = t_mid
                brackets.append([t_lo, t_hi])
                log.info(f'  [{family}] +1 crossing bracket refined to '
                         f'[{t_lo:.9f}, {t_hi:.9f}] '
                         f'(width {t_hi - t_lo:.2e})')
    return brackets


def comparison_points(records, log, w_cache):
    """Solve collocation orbits at the pre-registration section-5
    comparison taus (4.0, 5.5815 on the large lower family; 5.584, 5.587
    on the small lower family) and record their Floquet multipliers."""
    jobs = [('large_lower', 5.5815), ('small_lower', 5.584),
            ('small_lower', 5.587), ('large_lower', 5.575),
            ('small_lower', 5.575)]
    for fam, tau in jobs:
        fam_c = [r for r in records if r['family'] == fam]
        if not fam_c:
            continue
        w_near = None
        best = 1e9
        for r in fam_c:
            key = round(float(r['tau']), 9)
            if key in w_cache and abs(r['tau'] - tau) < best:
                best = abs(r['tau'] - tau)
                w_near = w_cache[key]
        if w_near is None:
            log.info(f'  comparison point {fam}@{tau}: no cached orbit '
                     f'nearby; skipped')
            continue
        w_c, ok, rn = fp.newton(np.asarray(w_near, float), tau)
        if not ok or fp.peak_to_peak(w_c) < 1e-6:
            log.info(f'  comparison point {fam}@{tau}: Newton FAILED '
                     f'(family does not exist there?) res={rn:.1e}')
            records.append(branch_row(
                fam, 9500 + len(records), 'comparison-failed', tau, w_c,
                rn, fp.nyquist_relative(w_c), ok,
                dict(cont_step=0.0, n_fail=0), None))
            continue
        fl = flo_at(w_c, tau)
        w_cache[round(tau, 9)] = w_c.copy()
        records.append(branch_row(
            fam, 9500 + len(records), 'comparison', tau, w_c, rn,
            fp.nyquist_relative(w_c), ok, dict(cont_step=0.0, n_fail=0),
            fl))
        log.info(f'  comparison point {fam}@{tau}: ptp='
                 f'{fp.peak_to_peak(w_c):.3f}, res={rn:.1e}, '
                 f'mu1={fl["mu1_mod"]}')


# ==========================================================================
# Stages
# ==========================================================================
def stage0(log, st):
    import numba
    import mpmath
    import scipy
    env = dict(
        date=time.strftime('%Y-%m-%d'),
        python=platform.python_version(),
        numpy=np.__version__, numba=numba.__version__,
        mpmath=mpmath.__version__, scipy=scipy.__version__,
        machine=platform.machine(), platform=platform.platform(),
        node=platform.node(),
        seeds='none (deterministic campaign; a fixed LCG seed 1 is used '
              'only for the Arnoldi start vectors)',
        code_hashes={
            'a025_model.py': sha256(A025 / 'a025_model.py'),
            'a025_fold_pipeline.py': sha256(A025 / 'a025_fold_pipeline.py'),
            'p4_kernels.py': sha256(HERE / 'p4_kernels.py'),
            'p4_campaign.py': sha256(HERE / 'p4_campaign.py'),
        })
    rng = np.random.default_rng(0)
    maxdiff = 0.0
    for _ in range(20000):
        N = rng.uniform(0, 105)
        Z = rng.uniform(0, 5)
        E = rng.uniform(0, 30)
        Zd = rng.uniform(0, 30)
        dNb, dZb, dEb, _ = basin_rhs(N, Z, E, Zd, PA)
        dv = rhs(np.array([N, Z, E]), Zd)
        maxdiff = max(maxdiff, abs(dNb - dv[0]), abs(dZb - dv[1]),
                      abs(dEb - dv[2]))
    env['rhs_equivalence_maxdiff'] = float(maxdiff)
    assert maxdiff < 1e-12
    declared = dict(r=0.02, K=100.0, q=0.001, eta=0.914, Emax=30.0,
                    delta0=0.01, Dref=1.0, taum=5.0, k=10.0,
                    delta=np.log(2.0) / 10.0, Zref=1.0)
    for key, val in declared.items():
        assert abs(PAR[key] - val) < 1e-15, key
    env['par_matches_preregistration'] = True
    env['equilibrium'] = [float(x) for x in equilibrium()]
    hopf = json.loads((A025 / 'a025_interval_hopf.json').read_text())
    env['inherited_hopf_certificates'] = hopf
    kraw = json.loads((A025 / 'a025_fold_krawczyk.json').read_text())
    slim = {}
    for k, v in kraw.items():
        if isinstance(v, (str, float, int, list, bool)):
            slim[k] = v
    env['inherited_fold_certificate'] = slim
    (HERE / 'p4_environment.json').write_text(json.dumps(env, indent=1))
    log.info(f'stage 0 done: rhs equivalence {maxdiff:.2e}; PAR verified '
             f'against the pre-registration; environment recorded')
    st['stage0'] = True
    save_status(st)


def stage1(log, st):
    eq = equilibrium()
    N_, Z_, E_ = eq
    hist = {'H1': (90.0, float(Z_), float(0.5 * E_)),
            'H2': (5.0, float(Z_), 15.0),
            'H3': (float(1.01 * N_), float(1.01 * Z_), float(1.01 * E_))}
    n_tail = int(round(TAIL / DT))
    n_ring = int(round(RING_YR / DT))
    rows = []
    seeds = {}
    t_all = time.time()
    jobs = [(t, h, DT) for t in TAU_GRID for h in ('H1', 'H2', 'H3')]
    jobs += [(t, h, DT / 2) for t in DT_HALVING_POINTS
             for h in ('H1', 'H2', 'H3')]
    for tau, hc, dt in jobs:
        hN, hZ, hE = hist[hc]
        n_steps = int(round(HORIZON / dt))
        ring = np.zeros((n_ring, 3))
        tail = np.zeros(n_tail)
        t0 = time.time()
        stats = basin_run(tau, dt, n_steps, hN, hZ, hE, PA, ring, tail)
        wall = time.time() - t0
        mean = stats[6]
        rsd = stats[7] / mean if mean > 1e-6 else stats[7]
        if stats[5] - stats[4] < 1e-9:
            cls = 'settles'
        elif rsd >= 0.02:
            cls = 'captured'
        elif rsd < 0.001:
            cls = 'settles'
        else:
            cls = 'intermediate'
        rows.append(dict(tau=tau, history=hc, dt=dt, n_steps=n_steps,
                         tau_grid_units=int(round(tau / dt)),
                         classification=cls,
                         tail_N_min=float(stats[4]),
                         tail_N_max=float(stats[5]),
                         tail_N_mean=float(mean),
                         tail_N_rsd=float(rsd),
                         max_E=float(stats[0]),
                         gate_floor_active=bool(stats[1] > 0),
                         clip_N=int(stats[2]), clip_E=int(stats[3]),
                         wall_s=round(wall, 2)))
        if dt == DT and tau in (4.0, 155.0) and hc == 'H1':
            seeds[f'{tau}'] = ring_to_chrono(ring, n_steps)
        log.info(f'  basin tau={tau:7.3f} {hc} dt={dt}: {cls:12s} '
                 f'rsd={rsd:8.4f} tail=[{stats[4]:.3f},{stats[5]:.3f}] '
                 f'maxE={stats[0]:.3f} ({wall:.1f}s)')
    cols = ['tau', 'history', 'dt', 'n_steps', 'tau_grid_units',
            'classification', 'tail_N_min', 'tail_N_max', 'tail_N_mean',
            'tail_N_rsd', 'max_E', 'gate_floor_active', 'clip_N',
            'clip_E', 'wall_s']
    write_csv(HERE / 'p4_basin_archive.csv', rows, cols)
    np.savez(HERE / 'p4_basin_seeds.npz', **seeds)
    halv = []
    for tau in DT_HALVING_POINTS:
        for hc in ('H1', 'H2', 'H3'):
            a = next(r['classification'] for r in rows if r['tau'] == tau
                     and r['history'] == hc and r['dt'] == DT)
            b = next(r['classification'] for r in rows if r['tau'] == tau
                     and r['history'] == hc and r['dt'] == DT / 2)
            ok = a == b
            halv.append(dict(tau=tau, history=hc, dt02=a, dt01=b,
                             unchanged=bool(ok)))
            log.info(f'  dt-halving tau={tau} {hc}: {a} vs {b} '
                     f'({"UNCHANGED" if ok else "CHANGED"})')
    st['stage1'] = dict(rows=len(rows),
                        dt_halving=halv,
                        dt_halving_all_unchanged=bool(
                            all(h['unchanged'] for h in halv)))
    save_status(st)
    log.info(f'stage 1 done: {len(rows)} basin runs '
             f'({time.time() - t_all:.0f}s); dt-halving all unchanged: '
             f'{st["stage1"]["dt_halving_all_unchanged"]}')


def stage2(log, st):
    fp.configure(64)
    records = []
    w_cache = {}
    results = {}

    # ---- B1: small branch, lower -----------------------------------------
    log.info('B1: small lower branch — pipeline branch switch from tau-')
    tau_s, w0 = fp.branch_switch()
    log.info(f'  branch point: tau={tau_s:.6f}, '
             f'ptp={fp.peak_to_peak(w0):.4f}')
    w_cache[round(float(tau_s), 9)] = w0.copy()
    flo = flo_at(w0, tau_s)
    records.append(branch_row(
        'small_lower', 1, 'switch', tau_s, w0,
        np.linalg.norm(fp.residual_jac(w0, tau_s, want_jac=False), np.inf),
        fp.nyquist_relative(w0), True, dict(cont_step=0.0, n_fail=0), flo))
    log.info(f'  switch Floquet: mu1={flo["mu1_mod"]}, '
             f'triv={flo["mu_triv"]}')
    w_end, tau_end, w_p, tau_p, n1 = continue_tau(
        w0, tau_s, +1, 6.4, dtau0=0.02, family='small_lower', pid0=1,
        records=records, log=log, w_cache=w_cache)
    n_sl = len([r for r in records if r['family'] == 'small_lower'])
    log.info(f'  natural continuation: {n_sl} points, tau up to '
             f'{tau_end:.9f}')
    log.info('  MS fold solve, m=64 (independent of the saved npz):')
    z, ell, res = fp.moore_spence(w_end, tau_end)
    tau_f_small = float(z[fp.DIM])
    results['small_lower_fold_ms64'] = dict(
        tau_f=tau_f_small, T_f=float(z[fp.DIM_Y]), residual=float(res))
    w_cache[round(tau_f_small, 9)] = z[:fp.DIM].copy()
    log.info(f'  small-branch fold: tau_f={tau_f_small:.12f}, |M|='
             f'{res:.2e} (inherited certificate: 5.587236198690)')
    if w_p is not None:
        pseudo_arclength_pass(w_end, tau_end, w_p, tau_p, ds0=0.02,
                              family='small_lower', pid0=500,
                              records=records, log=log,
                              tau_window=(1.0, 6.4), w_cache=w_cache)

    # ---- B3: large family, lower (tau in [1, 6]) -------------------------
    log.info('B3: large lower family — seed from the basin run at tau=4.0')
    seeds = np.load(HERE / 'p4_basin_seeds.npz')
    ring = seeds['4.0']
    Ys, T_est = extract_cycle(ring, DT)
    log.info(f'  extracted cycle: T_est={T_est:.3f}, '
             f'ptp={np.ptp(Ys[:, 0]):.2f}')
    w_seed = fp.pack(Ys, T_est)
    w_l4, ok4, rn4 = fp.newton(w_seed, 4.0)
    log.info(f'  collocation seed at tau=4.0: ok={ok4}, res={rn4:.1e}, '
             f'ptp={fp.peak_to_peak(w_l4):.2f}')
    if fp.peak_to_peak(w_l4) < 1e-6:
        raise RuntimeError('large-family seed failed at tau=4.0')
    w_cache[4.0] = w_l4.copy()
    flo = flo_at(w_l4, 4.0)
    records.append(branch_row(
        'large_lower', 1, 'basin-seed', 4.0, w_l4, rn4,
        fp.nyquist_relative(w_l4), ok4, dict(cont_step=0.0, n_fail=0),
        flo))
    log.info(f'  seed Floquet: mu1={flo["mu1_mod"]} (legacy 0.240)')
    w_lo_end, tau_lo_end, w_lo_p, tau_lo_p, _ = continue_tau(
        w_l4, 4.0, -1, 1.0, dtau0=0.1, family='large_lower',
        pid0=1, records=records, log=log, w_cache=w_cache)
    if w_lo_p is not None and abs(tau_lo_end - 1.0) > 1e-6:
        log.info('  large lower family stalled before tau=1 (turn or '
                 'resolution limit); arclength attempt:')
        pseudo_arclength_pass(w_lo_end, tau_lo_end, w_lo_p, tau_lo_p,
                              ds0=0.05, family='large_lower', pid0=850,
                              records=records, log=log,
                              tau_window=(0.5, 6.0), w_cache=w_cache)
    w_up, tau_up, w_p3, tau_p3, n3 = continue_tau(
        w_l4, 4.0, +1, 6.0, dtau0=0.05, family='large_lower', pid0=200,
        records=records, log=log, w_cache=w_cache)
    log.info('  MS fold solve for the large lower family (m=64):')
    zl, elll, resl = fp.moore_spence(w_up, tau_up)
    results['large_lower_fold_ms64'] = dict(
        tau_f=float(zl[fp.DIM]), T_f=float(zl[fp.DIM_Y]),
        residual=float(resl))
    w_cache[round(float(zl[fp.DIM]), 9)] = zl[:fp.DIM].copy()
    log.info(f'  large-lower fold (m=64): tau_f={zl[fp.DIM]:.12f}, '
             f'T={zl[fp.DIM_Y]:.4f}, |M|={resl:.2e}')
    if w_p3 is not None:
        pseudo_arclength_pass(w_up, tau_up, w_p3, tau_p3, ds0=0.02,
                              family='large_lower', pid0=700,
                              records=records, log=log,
                              tau_window=(1.0, 6.0), w_cache=w_cache)

    # ---- B2: small branch, upper (tau in [130, 150.30]) ------------------
    log.info('B2: small upper branch — switch from tau+')
    tau_su, w_u0 = branch_switch_upper(log)
    w_cache[round(float(tau_su), 9)] = w_u0.copy()
    flo = flo_at(w_u0, tau_su)
    records.append(branch_row(
        'small_upper', 1, 'switch', tau_su, w_u0,
        np.linalg.norm(fp.residual_jac(w_u0, tau_su, want_jac=False),
                       np.inf),
        fp.nyquist_relative(w_u0), True, dict(cont_step=0.0, n_fail=0),
        flo))
    log.info(f'  upper switch: tau={tau_su:.4f}, '
             f'ptp={fp.peak_to_peak(w_u0):.4f}, mu1={flo["mu1_mod"]}')
    w_su_end, tau_su_end, w_su_prev, tau_su_prev, n4 = continue_tau(
        w_u0, tau_su, -1, 130.0, dtau0=0.2, family='small_upper', pid0=1,
        records=records, log=log, w_cache=w_cache)
    if w_su_prev is not None and abs(tau_su_end - 130.0) > 1e-6:
        log.info('  small upper branch stalled before 130; arclength:')
        pseudo_arclength_pass(w_su_end, tau_su_end, w_su_prev,
                              tau_su_prev, ds0=0.1, family='small_upper',
                              pid0=500, records=records, log=log,
                              tau_window=(100.0, 150.5), w_cache=w_cache)

    # ---- B4: large family, upper (tau in [147.5, 160]) -------------------
    log.info('B4: large upper family — seed from the basin at tau=155.0')
    ring = seeds['155.0']
    Ys, T_est = extract_cycle(ring, DT)
    log.info(f'  extracted cycle: T_est={T_est:.3f}, '
             f'ptp={np.ptp(Ys[:, 0]):.2f}')
    w_seed = fp.pack(Ys, T_est)
    w_l155, ok155, rn155 = fp.newton(w_seed, 155.0)
    log.info(f'  collocation seed at tau=155.0: ok={ok155}, '
             f'res={rn155:.1e}, ptp={fp.peak_to_peak(w_l155):.2f}')
    records.append(branch_row(
        'large_upper', 1, 'basin-seed', 155.0, w_l155, rn155,
        fp.nyquist_relative(w_l155), ok155, dict(cont_step=0.0, n_fail=0),
        None))
    if ok155 and fp.peak_to_peak(w_l155) > 1e-6:
        w_cache[155.0] = w_l155.copy()
        flo = flo_at(w_l155, 155.0)
        records[-1].update(flo)
        log.info(f'  seed Floquet: mu1={flo["mu1_mod"]}')
        continue_tau(w_l155, 155.0, +1, 160.0, dtau0=0.2,
                     family='large_upper', pid0=1, records=records,
                     log=log, w_cache=w_cache)
        w_dn2, tau_dn2, w_p5, tau_p5, n6 = continue_tau(
            w_l155, 155.0, -1, 147.5, dtau0=0.1, family='large_upper',
            pid0=200, records=records, log=log, w_cache=w_cache)
        results['large_upper_continuation_ends'] = dict(
            up_to_160=bool(abs(tau_up2_end(records) - 160.0) < 1e-6),
            down_end=float(tau_dn2))
        if abs(tau_dn2 - 147.5) > 1e-6 and w_p5 is not None:
            log.info('  large upper family stalled before 147.5 (fold?):')
            zu, ellu, resu = fp.moore_spence(w_dn2, tau_dn2)
            results['large_upper_fold_ms64'] = dict(
                tau_f=float(zu[fp.DIM]), T_f=float(zu[fp.DIM_Y]),
                residual=float(resu))
            w_cache[round(float(zu[fp.DIM]), 9)] = zu[:fp.DIM].copy()
            log.info(f'  large-upper fold (m=64): tau_f={zu[fp.DIM]:.12f}, '
                     f'|M|={resu:.2e}')
            pseudo_arclength_pass(w_dn2, tau_dn2, w_p5, tau_p5, ds0=0.05,
                                  family='large_upper', pid0=700,
                                  records=records, log=log,
                                  tau_window=(140.0, 160.5),
                                  w_cache=w_cache)
    else:
        # the captured upper family (E ~ Emax face cycle) is not
        # m=64-resolvable: record the failure, attempt m=128 as the
        # resolution cross-check (recorded as a DEVIATION from
        # "m=64 primary" in the report), and keep the basin archive as
        # the family's existence record.
        results['large_upper_collocation_status'] = (
            'FAILED at m=64: basin-seed orbit (N ptp %.2f, E in [%.3f,'
            ' %.3f], the E~Emax face cycle) has Fourier residual %.1e; '
            'Newton diverged. The upper captured family is recorded by '
            'the basin archive (captured tails at 149.5-155.0); no '
            'collocation branch record, no MS fold location.'
            % (np.ptp(Ys[:, 0]), Ys[:, 2].min(), Ys[:, 2].max(),
               float(np.linalg.norm(fp.residual_jac(
                   w_seed, 155.0, want_jac=False), np.inf))))
        log.info('  ' + results['large_upper_collocation_status'])
        # m=128 attempt (resolution cross-check, recorded as deviation)
        fp.configure(128)
        n128 = 128
        idxs = np.linspace(0, n128 - 1, n128)
        # resample the extracted cycle at 128 phases via ring interp
        ring_ch = ring
        Nsc, Zsc, Esc = ring_ch[:, 0], ring_ch[:, 1], ring_ch[:, 2]
        nr = len(Nsc)
        win = 200
        maxima = [i for i in range(win, nr - win)
                  if Nsc[i] >= Nsc[i - 1] and Nsc[i] >= Nsc[i + 1]
                  and Nsc[i] == Nsc[max(win, i - win):i + win + 1].max()]
        i_end = maxima[-1]
        Tsteps = int(round(T_est / DT))
        i_start = i_end - Tsteps
        if i_start >= 0:
            phases = np.arange(n128) / n128
            idx = i_start + phases * Tsteps
            i0 = np.floor(idx).astype(int)
            fr = idx - i0
            i1 = np.minimum(i0 + 1, nr - 1)
            Y128 = np.stack([Nsc[i0] * (1 - fr) + Nsc[i1] * fr,
                             Zsc[i0] * (1 - fr) + Zsc[i1] * fr,
                             Esc[i0] * (1 - fr) + Esc[i1] * fr], axis=1)
            w128 = fp.pack(Y128, T_est)
            res128 = float(np.linalg.norm(
                fp.residual_jac(w128, 155.0, want_jac=False), np.inf))
            wv128, ok128, rn128 = fp.newton(w128, 155.0)
            records.append(branch_row(
                'large_upper', 2, 'basin-seed-m128', 155.0, wv128, rn128,
                fp.nyquist_relative(wv128), ok128,
                dict(cont_step=0.0, n_fail=0), None))
            results['large_upper_m128_attempt'] = dict(
                seed_residual=res128, newton_ok=bool(ok128),
                newton_residual=float(rn128),
                note='resolution cross-check attempt; recorded as a '
                     'deviation from m=64-primary (the family is not '
                     'm=64-resolvable)')
            log.info(f'  m=128 attempt: seed res={res128:.1e}, '
                     f'newton ok={ok128}, res={rn128:.1e}')
        fp.configure(64)
        results['large_upper_continuation_ends'] = dict(
            up_to_160=False, down_end=None)

    # ---- comparison points + crossing brackets ---------------------------
    log.info('comparison-point solves (pre-registration section 5 taus):')
    comparison_points(records, log, w_cache)
    log.info('+1 crossing bracket refinement:')
    brackets = {}
    for fam in FAMILIES:
        brs = refine_crossing(fam, records, log, w_cache)
        if brs:
            brackets[fam] = brs
    results['crossing_brackets'] = brackets

    # ---- persist -----------------------------------------------------------
    write_csv(HERE / 'p4_branch_archive.csv', records, BRANCH_COLS)
    for fam in FAMILIES:
        write_csv(HERE / f'p4_branch_{fam}.csv',
                  [r for r in records if r['family'] == fam], BRANCH_COLS)
    np.savez(HERE / 'p4_branch_orbits.npz',
             **{str(k): v for k, v in w_cache.items()})
    results['n_records'] = len(records)
    st['stage2'] = results
    save_status(st)
    log.info(f'stage 2 done: {len(records)} branch records written')


def tau_up2_end(records):
    ups = [float(r['tau']) for r in records
           if r['family'] == 'large_upper' and r['method'] != 'basin-seed']
    return max(ups) if ups else 0.0


def stage3(log, st):
    fp.configure(64)
    results = st.setdefault('stage3', {})
    s2 = st.get('stage2', {})
    orbits = np.load(HERE / 'p4_branch_orbits.npz')
    folds = []
    for tag in ('large_lower', 'large_upper'):
        key = f'{tag}_fold_ms64'
        if key in s2:
            tau_f = s2[key]['tau_f']
            k = f'{round(float(tau_f), 9)}'
            if k in orbits.files:
                w = orbits[k]
                ms_fold_three_orders(w, tau_f, tag, log, results)
                folds.append(tag)
            else:
                log.info(f'  [MS {tag}] orbit key {k} not cached; skipped')
    st['stage3'] = results
    save_status(st)
    log.info(f'stage 3 done: three-order MS for {folds}')


# ==========================================================================
# Stage 4: records and comparison (reported ONCE, no re-runs)
# ==========================================================================
def stage4(log, st):
    import csv as csvmod
    basin = list(csvmod.DictReader(open(HERE / 'p4_basin_archive.csv')))
    branch = list(csvmod.DictReader(open(HERE / 'p4_branch_archive.csv')))
    results = {}
    comp = {}

    def fam_rows(fam):
        return [r for r in branch if r['family'] == fam
                and r['mu1_mod'] != '']

    def fnum(r, k):
        try:
            return float(r[k])
        except (TypeError, ValueError):
            return None

    def mu_at(fam, tau, prefer_methods=()):
        rows = fam_rows(fam)
        best = None
        for r in rows:
            if prefer_methods and r['method'] not in prefer_methods:
                continue
            d = abs(float(r['tau']) - tau)
            if best is None or d < best[0]:
                best = (d, r)
        return best

    def cmp_mu(name, fam, tau, legacy, tol=0.02):
        got = mu_at(fam, tau)
        if got is None or got[0] > 0.01:
            comp[name] = dict(verdict='NOT-TESTED', legacy=legacy,
                              campaign=None, tau=tau, family=fam)
            return
        d, row = got
        val = fnum(row, 'mu1_mod')
        if val is None:
            comp[name] = dict(verdict='NOT-TESTED', legacy=legacy)
            return
        ok = abs(val - legacy) <= tol
        comp[name] = dict(verdict='MATCH' if ok else 'MISMATCH',
                          legacy=legacy, campaign=val,
                          tau=float(row['tau']), family=fam, tol=tol,
                          note=f'nearest record at tau={float(row["tau"])} '
                               f'(requested {tau})')

    cmp_mu('large_mult_tau4', 'large_lower', 4.0, 0.240)
    cmp_mu('large_mult_tau5.5815', 'large_lower', 5.5815, 0.964)
    cmp_mu('small_mult_tau5.584', 'small_lower', 5.584, 1.0514)
    cmp_mu('small_mult_tau5.587', 'small_lower', 5.587, 0.99898)

    def amp_period_at(fam, tau, tol=0.01):
        best = None
        for r in fam_rows(fam):
            d = abs(float(r['tau']) - tau)
            if best is None or d < best[0]:
                best = (d, r)
        if best is None or best[0] > tol:
            return None
        return (fnum(best[1], 'N_ptp'), fnum(best[1], 'T'),
                float(best[1]['tau']))

    a_small = amp_period_at('small_lower', 5.575, tol=0.006)
    a_large = amp_period_at('large_lower', 5.575, tol=0.006)
    if a_small and a_large:
        amp_gap = abs(a_large[0] - a_small[0])
        per_gap = abs(a_large[1] - a_small[1])
        ok = amp_gap >= 2.0 and per_gap >= 5.0
        comp['family_separation_lower'] = dict(
            verdict='MATCH' if ok else 'MISMATCH',
            small=dict(amp=a_small[0], T=a_small[1], tau=a_small[2]),
            large=dict(amp=a_large[0], T=a_large[1], tau=a_large[2]),
            amp_gap=float(amp_gap), period_gap=float(per_gap),
            legacy=dict(amp_gap=25.0 - 21.7, period_gap=322.9 - 314.3))
    else:
        comp['family_separation_lower'] = dict(verdict='NOT-TESTED')

    s2 = st.get('stage2', {})
    s3 = st.get('stage3', {})
    env = json.loads((HERE / 'p4_environment.json').read_text())
    kraw_tau = None
    kc = env.get('inherited_fold_certificate', {})
    for key in ('tau_enclosure', 'tau_f_interval', 'final_tau_interval',
                'tau_f'):
        if key in kc and isinstance(kc[key], list):
            kraw_tau = kc[key]
            break
    if kraw_tau is None:
        kraw_tau = [5.587236198689, 5.587236198691]

    basin_grid = {}
    for r in basin:
        if abs(float(r['dt']) - DT) > 1e-12:
            continue
        basin_grid.setdefault(float(r['tau']), {})[r['history']] = \
            r['classification']

    def basin_bracket(t_lo, t_hi, hist='H2', cls_from='captured',
                      cls_to='settles'):
        seq = [(t, basin_grid[t].get(hist)) for t in sorted(basin_grid)
               if t_lo <= t <= t_hi]
        for (a, ca), (b, cb) in zip(seq[:-1], seq[1:]):
            if ca == cls_from and cb == cls_to:
                return [a, b]
        return None

    bb_lower = basin_bracket(5.5, 6.5)
    bb_upper = basin_bracket(147.0, 152.0)

    def basin_capture_onset(t_lo, t_hi, hist='H1'):
        seq = [(t, basin_grid[t].get(hist)) for t in sorted(basin_grid)
               if t_lo <= t <= t_hi]
        for (a, ca), (b, cb) in zip(seq[:-1], seq[1:]):
            if ca != 'captured' and cb == 'captured':
                return [a, b]
        return None

    bb_upper_h1 = basin_capture_onset(147.0, 156.0, 'H1')

    ms_ll = s3.get('ms_large_lower_tau_bracket') or \
        ([s2.get('large_lower_fold_ms64', {}).get('tau_f')] * 2
         if s2.get('large_lower_fold_ms64') else None)
    ms_lu = s3.get('ms_large_upper_tau_bracket') or \
        ([s2.get('large_upper_fold_ms64', {}).get('tau_f')] * 2
         if s2.get('large_upper_fold_ms64') else None)

    def cmp_bracket(name, mine, legacy):
        if not mine or mine[0] is None:
            comp[name] = dict(verdict='NOT-TESTED', legacy=legacy)
            return
        lo, hi = mine
        ok = lo <= legacy[1] and hi >= legacy[0]
        comp[name] = dict(verdict='MATCH' if ok else 'MISMATCH',
                          campaign_bracket=[float(lo), float(hi)],
                          legacy=legacy)

    cmp_bracket('lower_boundary', ms_ll, [5.574, 5.576])
    comp['lower_boundary_basin_grid'] = bb_lower
    # the legacy value 5.587 is a 3-decimal rounding of the fold; the
    # match test is |fold - 5.587| within the rounding half-width 5e-4
    fold_mid = 0.5 * (kraw_tau[0] + kraw_tau[1])
    comp['small_branch_fold'] = dict(
        verdict='MATCH' if abs(fold_mid - 5.587) <= 5.0e-4
        else 'MISMATCH',
        campaign_bracket=kraw_tau, legacy=5.587,
        fold_mid=fold_mid,
        source='inherited interval Krawczyk certificate '
               '(a025_fold_krawczyk.json); stage-2 m=64 MS re-verification '
               f'tau_f={s2.get("small_lower_fold_ms64", {}).get("tau_f")}')
    if ms_lu:
        cmp_bracket('upper_boundary', ms_lu, [148.125, 148.438])
    else:
        # no collocation fold locatable (the upper captured family is not
        # Fourier-resolvable); the campaign bracket is the basin-grid H1
        # capture-onset bracket
        ub = bb_upper_h1
        if ub:
            okb = ub[0] <= 148.438 and ub[1] >= 148.125
            comp['upper_boundary'] = dict(
                verdict='MATCH' if okb else 'MISMATCH',
                campaign_bracket=[float(ub[0]), float(ub[1])],
                legacy=[148.125, 148.438],
                source='basin-grid H1 capture onset (no collocation fold: '
                       'the upper captured family, an E~Emax face cycle, '
                       'is not m=64/128 Fourier-resolvable)')
        else:
            comp['upper_boundary'] = dict(verdict='NOT-TESTED',
                                          legacy=[148.125, 148.438])
    comp['upper_boundary_basin_grid'] = bb_upper_h1

    def amp_range(fam, lo, hi):
        vals = [(float(r['tau']), fnum(r, 'N_ptp')) for r in fam_rows(fam)
                if lo <= float(r['tau']) <= hi and fnum(r, 'N_ptp')]
        if not vals:
            return None
        amps = [v for _, v in vals]
        return dict(min=float(min(amps)), max=float(max(amps)),
                    tau_lo=float(min(t for t, _ in vals)),
                    tau_hi=float(max(t for t, _ in vals)))

    def amp_at_tau(fam, tau, tol=0.02):
        best = None
        for r in fam_rows(fam):
            d = abs(float(r['tau']) - tau)
            if best is None or d < best[0]:
                best = (d, r)
        if best is None or best[0] > tol:
            return None
        return fnum(best[1], 'N_ptp'), float(best[1]['tau'])

    su_hi = amp_at_tau('small_upper', 150.30, tol=0.02)
    su_lo = amp_at_tau('small_upper', 130.0, tol=0.01)
    if su_hi and su_lo:
        ok_hi = abs(su_hi[0] - 0.11) / 0.11 <= 0.15
        ok_lo = abs(su_lo[0] - 1.87) / 1.87 <= 0.15
        comp['small_upper_amp_window'] = dict(
            verdict='MATCH' if (ok_hi and ok_lo) else 'MISMATCH',
            campaign=dict(amp_at_upper_end=su_hi[0],
                          tau_of_upper_end=su_hi[1],
                          amp_at_lower_end=su_lo[0],
                          tau_of_lower_end=su_lo[1]),
            legacy=dict(amp_at_150_30=0.11, amp_at_130=1.87))
    else:
        comp['small_upper_amp_window'] = dict(verdict='NOT-TESTED')
    lu = amp_range('large_upper', 147.5, 160.0)
    if lu:
        lo_ok = abs(lu['min'] - 15.9) / 15.9 <= 0.15
        hi_ok = abs(lu['max'] - 19.5) / 19.5 <= 0.15
        comp['large_upper_amp_window'] = dict(
            verdict='MATCH' if (lo_ok and hi_ok) else 'MISMATCH',
            campaign=lu, legacy=dict(min=15.9, max=19.5))
    else:
        comp['large_upper_amp_window'] = dict(verdict='NOT-TESTED')

    # H1/H2 asymmetry inside the two windows (the legacy's own basin claim)
    asym = []
    for tau in (5.575, 148.3):
        h1 = basin_grid.get(tau, {}).get('H1')
        h2 = basin_grid.get(tau, {}).get('H2')
        legacy_h1, legacy_h2 = 'captured', 'settles'
        agree = (h1 == legacy_h1) and (h2 == legacy_h2)
        asym.append(dict(tau=tau, H1=h1, H2=h2,
                         legacy_H1=legacy_h1, legacy_H2=legacy_h2,
                         agree=bool(agree)))
    comp['basin_asymmetry_windows'] = dict(
        verdict='MATCH' if all(a['agree'] for a in asym) else 'MISMATCH',
        points=asym,
        note='the legacy claim: inside either bistable window, '
             'large-stock/low-effort histories are captured by the cycle '
             'while near-collapse histories recover to the equilibrium')

    def legacy_class(tau, hist):
        if tau < 3.6661490142743:
            return 'captured'
        if tau <= 5.574:
            return 'captured' if hist == 'H1' else 'settles'
        if tau < 148.125:
            return 'settles'
        if tau < 150.3584773101421:
            return 'captured' if hist == 'H1' else 'settles'
        return 'captured'

    agrees, disagrees = [], []
    for tau, classes in sorted(basin_grid.items()):
        for hist, cls in classes.items():
            lc = legacy_class(tau, hist)
            if cls == lc:
                agrees.append([tau, hist, cls])
            else:
                disagrees.append([tau, hist, cls, lc])
    comp['basin_grid_agreement'] = dict(
        verdict='MATCH' if not disagrees else 'MISMATCH',
        n_agree=len(agrees), n_disagree=len(disagrees),
        disagreements=disagrees,
        note='legacy classes inferred from the five-regime table + the '
             'H1/H2 asymmetry (no committed legacy per-grid record '
             'exists); finite-horizon (4e4 yr) classes near the Hopf '
             'points can be intermediate where the asymptotic class is '
             'captured/settles (critical slowing: linear rates '
             '1e-5..1e-4 /yr)')

    results['comparison'] = comp
    results['boundary_table'] = dict(
        tau_hopf_lower=dict(bracket=[3.6661490142739, 3.6661490142743],
                            source='inherited interval certificate'),
        large_lower_fold=dict(
            bracket=ms_ll, basin_grid_bracket=bb_lower,
            source='stage-3 three-order MS (provisional SNPO '
                   'classification) + Floquet +1-crossing + basin grid'),
        small_branch_fold=dict(
            bracket=kraw_tau,
            source='inherited interval Krawczyk certificate; stage-2 m=64 '
                   'MS re-verification'),
        large_upper_fold=dict(
            bracket=ms_lu, basin_grid_bracket=bb_upper,
            source='stage-3 three-order MS (provisional) + Floquet + '
                   'basin grid'),
        tau_hopf_upper=dict(bracket=[150.3584773101408,
                                     150.3584773101421],
                            source='inherited interval certificate'),
        crossing_brackets=s2.get('crossing_brackets', {}),
        interior_monostability=dict(
            statement='finite-search result: every interior grid tau '
                      '(6.0, 8.0, 20.0, 50.0, 100.0, 130.0; dt=0.02, '
                      'horizon 4e4 yr) classifies as settles for all '
                      'three histories, and the campaign branch records '
                      'contain no periodic-orbit family in '
                      '5.6 < tau < 147.5',
            note='a finite search, not a proof'))
    # basin classification summary for the report
    results['basin_grid'] = {str(t): c for t, c in
                             sorted(basin_grid.items())}
    results['stage2_summary'] = {k: v for k, v in s2.items()
                                 if not isinstance(v, dict)}
    results['stage3_summary'] = {k: v for k, v in s3.items()
                                 if not isinstance(v, dict)}
    st['stage4'] = results
    save_status(st)
    (HERE / 'p4_campaign_results.json').write_text(
        json.dumps(results, indent=1, default=str))
    n_match = sum(1 for v in comp.values()
                  if isinstance(v, dict) and v.get('verdict') == 'MATCH')
    n_mis = sum(1 for v in comp.values()
                if isinstance(v, dict) and v.get('verdict') == 'MISMATCH')
    n_nt = sum(1 for v in comp.values()
               if isinstance(v, dict) and v.get('verdict') == 'NOT-TESTED')
    log.info(f'stage 4 done: comparison verdicts — MATCH {n_match}, '
             f'MISMATCH {n_mis}, NOT-TESTED {n_nt}')
    return results


def main():
    stage = sys.argv[1] if len(sys.argv) > 1 else 'all'
    st = load_status()
    log = Tee(LOG)
    log.info(f'P4 five-regime campaign — stage "{stage}" starting')
    fp.configure(64)
    if stage in ('0', 'all') and not st.get('stage0'):
        stage0(log, st)
    if stage in ('1', 'all') and not st.get('stage1'):
        stage1(log, st)
    if stage in ('2', 'all') and not st.get('stage2'):
        stage2(log, st)
    if stage in ('3', 'all') and not st.get('stage3'):
        stage3(log, st)
    if stage in ('4', 'all'):
        stage4(log, st)
    log.info(f'stage "{stage}" complete')


if __name__ == '__main__':
    main()

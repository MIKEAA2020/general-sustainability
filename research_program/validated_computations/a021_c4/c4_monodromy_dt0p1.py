#!/usr/bin/env python3
"""C4 monodromy at the second mesh level dt=0.1 (resumable companion).

Runs the SAME computation as c4_monodromy.run_level(0.1) — every mathematical
helper (simulate, build_A, eps_one_step, bauer_fike, norm_inf, jac_point,
rhs, TAU, P4) is imported unchanged from c4_monodromy — but the orchestration
is split into phases with checkpoints, because the sandbox kills long-running
background processes and the single-shot runtime (~20+ min, dominated by the
60000-SVD sigma_min contour scan at dim=184) exceeds the foreground budget.

Phases (run repeatedly with --resume until done):
  phase 1: simulate + forward/backward partials + ball + Bauer-Fike + discs
           -> checkpoint c4_monodromy_dt0p1_phase1.npz
  phase 2: sigma_min contour scan, chunked (checkpoint every chunk)
           -> c4_monodromy_dt0p1_contour.npz
  phase 3: assemble final artifacts (c4_monodromy_dt0p1.npz,
           c4_monodromy_dt0p1_enclosure.json)

The pinned dt=0.25 artifacts and their hashes in PROOF_MANIFEST.md Part II
are untouched; this file records the second mesh level only. Status labels
match the dt=0.25 enclosure honestly (e.g. exceeds_ball may be false; the
all-inside verdict rests on the individual eigen-discs).
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))
import c4_monodromy as cm  # noqa: E402

DT = 0.1
TAG = 'dt0p1'
PHASE1 = ROOT / f'c4_monodromy_{TAG}_phase1.npz'
CONTOUR = ROOT / f'c4_monodromy_{TAG}_contour.npz'
FINAL_NPZ = ROOT / f'c4_monodromy_{TAG}.npz'
FINAL_JSON = ROOT / f'c4_monodromy_{TAG}_enclosure.json'
CHUNK = 12000  # SVDs per phase-2 invocation (fits the foreground budget)


def log(msg):
    print(msg, flush=True)


def phase1():
    """Everything up to and including the individual eigen-discs."""
    t0 = time.time()
    d = int(round(cm.TAU / DT))
    log(f'phase 1: simulate + partials + ball (dt={DT}, d={d})')
    x_end = cm.simulate(dt=DT)
    n_total = 20000
    x0 = np.array([25., 300., 0.5, 10.])
    hist = np.tile(x0, (d + 1, 1))
    cur = x0.copy()
    traj = []
    for i in range(n_total):
        zd0 = hist[(i - d) % (d + 1), 2]
        zdhalf = 0.5 * (hist[(i - d) % (d + 1), 2]
                        + hist[(i - d + 1) % (d + 1), 2])
        zd1 = hist[(i - d + 1) % (d + 1), 2]
        k1 = cm.rhs(cur, zd0)
        k2 = cm.rhs(cur + 0.5 * DT * k1, zdhalf)
        k3 = cm.rhs(cur + 0.5 * DT * k2, zdhalf)
        k4 = cm.rhs(cur + DT * k3, zd1)
        nxt = cur + DT * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        hist[(i + 1) % (d + 1)] = nxt
        cur = nxt
        traj.append(cur.copy())
    traj = np.asarray(traj)
    ii = cm.maxima_indices(traj)
    start, end = ii[-2], ii[-1]
    nper = end - start
    dim = 4 * (d + 1)
    base = traj[start - d:end + 1]
    log(f'  period {nper} steps = {nper*DT:.1f} yr, dim {dim} '
        f'({time.time()-t0:.0f}s)')

    F = np.eye(dim)
    F_norms = np.zeros(nper + 1)
    F_norms[0] = 1.0
    eps_list = np.zeros(nper)
    for i in range(nper):
        F = cm.build_A(base, i, DT, d, dim) @ F
        F_norms[i + 1] = cm.norm_inf(F)
        ci = d + i
        eps_list[i] = cm.eps_one_step(base[ci], base[ci + 1],
                                      base[i, 2],
                                      0.5 * (base[i, 2] + base[i + 1, 2]),
                                      base[i + 1, 2], DT)
    M_nom = F
    log(f'  forward pass done ({time.time()-t0:.0f}s)')

    B = np.eye(dim)
    b_nom = np.zeros(nper + 1)
    b_nom[nper] = 1.0
    for j in range(nper - 1, -1, -1):
        B = cm.build_A(base, j, DT, d, dim) @ B
        b_nom[j] = cm.norm_inf(B)
    log(f'  backward pass done ({time.time()-t0:.0f}s)')

    nblk = 40
    bsize = (nper + nblk - 1) // nblk
    blocks = []
    for k in range(nblk):
        lo = k * bsize
        hi = min((k + 1) * bsize, nper)
        if lo >= hi:
            break
        Pk = np.eye(dim)
        for j in range(lo, hi):
            Pk = cm.build_A(base, j, DT, d, dim) @ Pk
        blocks.append(Pk)
    nb = len(blocks)
    W_max = 1.0
    for a in range(nb):
        W = blocks[a].copy()
        W_max = max(W_max, cm.norm_inf(W) * (1.0 + bsize * dim * cm.U16))
        for b in range(a + 1, nb):
            W = blocks[b] @ W
            W_max = max(W_max, cm.norm_inf(W)
                        * (1.0 + (b - a + 1) * bsize * dim * cm.U16))
    W_max = float(np.nextafter(W_max, np.inf))
    log(f'  block amplification done ({time.time()-t0:.0f}s)')

    delta_tot = float(eps_list.sum())
    max_b = float(b_nom.max())
    e_bound = float(np.nextafter(delta_tot * max_b * W_max, np.inf))
    infl = 3.0 * nper * dim * cm.U16
    E1 = 0.0
    for i in range(nper):
        E1 += b_nom[i + 1] * (1.0 + infl) * eps_list[i] * F_norms[i] \
            * (1.0 + infl)
    E1 = float(np.nextafter(E1, np.inf))
    gamma = (nper - 1) * dim * cm.U16 / (1.0 - (nper - 1) * dim * cm.U16)
    R_prod = gamma * F_norms[nper]
    ball = float(np.nextafter(E1 + R_prod, np.inf))
    log(f'  ball = {ball:.3e} ({time.time()-t0:.0f}s)')

    lam, kappa, delta_bf = cm.bauer_fike(M_nom, ball)
    order = np.argsort(-np.abs(lam))
    lam = lam[order]
    disc = kappa * ball if np.isfinite(kappa) else np.inf

    discs = []
    for j in range(min(3, len(lam))):
        lam_arr, X = np.linalg.eig(M_nom)
        idx = int(np.argmin(np.abs(lam_arr - lam[j])))
        xv = X[:, idx]
        lamH, Y = np.linalg.eig(M_nom.conj().T)
        jdx = int(np.argmin(np.abs(lamH - lam[j].conj())))
        yv = Y[:, jdx].conj()
        rx = float(np.linalg.norm(M_nom @ xv - lam[j] * xv, np.inf)) \
            + dim * cm.U16 * cm.norm_inf(M_nom) \
            * float(np.linalg.norm(xv, np.inf))
        ry = float(np.linalg.norm(M_nom.conj().T @ yv
                                  - lam[j].conj() * yv, np.inf)) \
            + dim * cm.U16 * cm.norm_inf(M_nom) \
            * float(np.linalg.norm(yv, np.inf))
        yx = abs(np.vdot(yv, xv))
        nx = float(np.linalg.norm(xv, np.inf))
        ny = float(np.linalg.norm(yv, np.inf))
        cond = nx * ny / yx * 1.1
        dj = cond * (ball + max(rx / nx, ry / ny))
        discs.append(dict(lam_re=float(lam[j].real),
                          lam_im=float(lam[j].imag),
                          modulus=float(abs(lam[j])), disc=float(dj)))
    log(f'  Bauer-Fike + discs done ({time.time()-t0:.0f}s)')

    i_phase = int(np.argmin(np.abs(lam - 1.0)))
    nontriv = [i for i in range(len(lam)) if i != i_phase]
    rho = max(float(abs(lam[i])) + disc for i in nontriv)
    d_ph = discs[0]['disc']
    d_dom = discs[1]['disc']
    sep = abs(lam[i_phase] - lam[1])
    ok_A = bool(sep > d_ph + d_dom)
    dom_cert = bool(discs[1]['modulus'] + d_dom < 1.0)

    np.savez(PHASE1, M=M_nom, lam=lam, ball=ball, E1=E1, R_prod=R_prod,
             W_max=W_max, delta_tot=delta_tot, max_b=max_b, nper=nper,
             dim=dim, d=d, discs=np.array(json.dumps(discs)),
             kappa=np.array([kappa if np.isfinite(kappa) else np.inf]),
             delta_bf=np.array([delta_bf]), rho=np.array([rho]),
             ok_A=np.array([ok_A]), dom_cert=np.array([dom_cert]),
             i_phase=np.array([i_phase]),
             max_eps=np.array([float(eps_list.max())]),
             F_norm_end=np.array([F_norms[nper]]))
    log(f'phase 1 complete ({time.time()-t0:.0f}s) -> {PHASE1.name}')


def coarse_scan(M_nom, ball):
    """Adaptive radius selection (identical logic to run_level)."""
    dim = M_nom.shape[0]
    best = None
    for r_try in (0.97, 0.96, 0.95, 0.9, 0.85, 0.8):
        smin_s = np.inf
        for k in range(512):
            th = 2 * np.pi * k / 512
            z = r_try * np.exp(1j * th)
            s = np.linalg.svd(z * np.eye(dim) - M_nom, compute_uv=False)[-1]
            smin_s = min(smin_s, float(s))
        slack = smin_s - ball
        need = (int(np.ceil(2 * np.pi * r_try / (2 * 0.8 * slack)))
                if slack > 0 else 10 ** 9)
        if best is None or need < best[1]:
            best = (r_try, need, smin_s)
    return best


def phase2():
    """Chunked sigma_min contour scan with resume."""
    t0 = time.time()
    ph = np.load(PHASE1, allow_pickle=True)
    M_nom = ph['M']
    ball = float(ph['ball'])
    dim = M_nom.shape[0]
    if CONTOUR.exists():
        ck = np.load(CONTOUR)
        r_in, need, k0, smin_b = (float(ck['r_in']), int(ck['need']),
                                  int(ck['k']), float(ck['smin_b']))
        log(f'phase 2: resume contour r={r_in} need={need} from k={k0}')
    else:
        r_in, need, smin_coarse = coarse_scan(M_nom, ball)
        need = max(4096, min(need, 60000))
        k0, smin_b = 0, np.inf
        log(f'phase 2: contour r={r_in} need={need} '
            f'(coarse smin {smin_coarse:.3e})')
    k = k0
    t_chunk = time.time()
    while k < need:
        th = 2 * np.pi * k / need
        z = r_in * np.exp(1j * th)
        s = np.linalg.svd(z * np.eye(dim) - M_nom, compute_uv=False)[-1]
        smin_b = min(smin_b, float(s))
        k += 1
        if (k - k0) % 2000 == 0:
            rate = (k - k0) / (time.time() - t_chunk)
            log(f'  k={k}/{need} smin={smin_b:.3e} '
                f'({rate:.0f} SVD/s, {time.time()-t0:.0f}s)')
        if (k - k0) >= CHUNK:
            break
    if k < need:
        np.savez(CONTOUR, r_in=r_in, need=need, k=k, smin_b=smin_b)
        log(f'phase 2: checkpoint at k={k}/{need} — rerun with --resume')
        return False
    np.savez(CONTOUR, r_in=r_in, need=need, k=k, smin_b=smin_b,
             done=np.array([True]))
    log(f'phase 2: contour complete ({time.time()-t0:.0f}s), '
        f'smin={smin_b:.3e}')
    return True


def phase3():
    t0 = time.time()
    ph = np.load(PHASE1, allow_pickle=True)
    ck = np.load(CONTOUR)
    M_nom, lam = ph['M'], ph['lam']
    dim = int(ph['dim'])
    ball = float(ph['ball'])
    discs = json.loads(str(ph['discs']))
    r_in, need, smin_b = float(ck['r_in']), int(ck['need']), float(ck['smin_b'])
    spacing = 2 * np.pi * r_in / need
    smin_rigorous = smin_b - 0.5 * spacing
    ok_B = bool(smin_rigorous > ball)
    n_inside = int(np.sum(np.abs(lam) < r_in))
    i_phase = int(ph['i_phase'])
    ok_A = bool(ph['ok_A'])
    dom_cert = bool(ph['dom_cert'])
    hyperbolic = bool(ok_A and dom_cert)
    nper, d = int(ph['nper']), int(ph['d'])

    lv = dict(
        dt=DT, dimension=dim, delay_steps=d, period_steps=int(nper),
        discrete_period_yr=float(nper * DT),
        nominal_monodromy_inf_norm=cm.norm_inf(M_nom),
        E1_exact_insertion=float(ph['E1']),
        R_product_rounding=float(ph['R_prod']),
        rigorous_ball_inf=ball,
        window_amplification_bound=float(ph['W_max']),
        max_eps=float(ph['max_eps']),
        kappa_inf=float(ph['kappa'][0]),
        multipliers=[dict(re=float(z.real), im=float(z.imag),
                          modulus=float(abs(z))) for z in lam[:8]],
        eigen_discs_top3=discs,
        phase_multiplier=dict(nominal=float(abs(lam[i_phase])),
                              simple_neutral_certified=ok_A),
        dominant_nontrivial=dict(nominal=float(abs(lam[1])),
                                 disc=discs[1]['disc'],
                                 below_one_certified=dom_cert),
        all_nontrivial_strictly_inside_unit_disc=hyperbolic,
        sigma_min_contour=dict(radius=r_in, rigorous_min=float(smin_rigorous),
                               sampled_min=float(smin_b), svds=int(need),
                               exceeds_ball=ok_B, nominal_inside=n_inside),
    )
    np.savez(FINAL_NPZ, M=M_nom, lam=lam)
    out = {
        'title': 'Monodromy/Floquet enclosure for the validated C4 cycle '
                 '(second mesh level dt=0.1)',
        'method': 'single-step insertion-identity sensitivity + Bauer-Fike '
                  'eigenvalue discs + sigma_min contour counting '
                  '(identical run_level method as the dt=0.25 enclosure; '
                  'execution split into resumable phases by '
                  'c4_monodromy_dt0p1.py)',
        'levels': {TAG: lv},
        'note': 'Companion to c4_monodromy_enclosure.json (dt=0.25, '
                'pinned). The dt=0.25 artifacts and hashes are untouched; '
                'this file records the second mesh level only. Status '
                'labels are honest: the all-inside verdict rests on the '
                'individual eigen-discs (ok_A + dom_cert); the contour '
                'check is informational and may show exceeds_ball=false '
                '(as at dt=0.25).',
    }
    FINAL_JSON.write_text(json.dumps(out, indent=2))
    log(f'phase 3: written {FINAL_NPZ.name} + {FINAL_JSON.name} '
        f'({time.time()-t0:.0f}s)')
    log(f'  period: {lv["period_steps"]} steps = '
        f'{lv["discrete_period_yr"]:.2f} yr')
    log(f'  ball: {lv["rigorous_ball_inf"]:.3e}')
    log(f'  phase: {lv["phase_multiplier"]}')
    log(f'  dominant: {lv["dominant_nontrivial"]}')
    log(f'  all inside: {lv["all_nontrivial_strictly_inside_unit_disc"]}')
    log(f'  contour: {lv["sigma_min_contour"]}')


def main():
    resume = '--resume' in sys.argv
    if PHASE1.exists() and resume:
        log('resuming from phase 1 checkpoint')
    else:
        phase1()
    if not phase2():
        return
    phase3()


if __name__ == '__main__':
    main()

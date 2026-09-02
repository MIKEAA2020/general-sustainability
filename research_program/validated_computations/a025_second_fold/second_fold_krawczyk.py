#!/usr/bin/env python3
"""Stage C of the second-fold search: interval Krawczyk certification of a
candidate second fold (pre-registered in SECOND_FOLD_PREREGISTRATION.md §4).

Reuses the lower-fold certificate's machinery verbatim (imported from
a025_fold/a025_fold_krawczyk.py: the exact circulant shift family, the
interval Jacobian assembly of the m=64 Moore-Spence system, the
double-double centered dots, the nullvector angle bound, and the FD
self-verification battery), applied at the NEW nominal point:

  - nominal (z, ell): second_fold_ms.npz z_m64/ell_m64 (the accepted
    Stage-B Moore-Spence solve);
  - tau-box: [min three-order tau_f - 1e-8, max + 1e-8] (constructed;
    no prior interval exists for the second fold);
  - radii ladder: (ry, rt, rv) = (2e-9, 2e-8, 1.5e-8) x {1, 2.5, 6, 15,
    40} — every attempt logged; a certificate at any rung is valid.

Certificate requirements (all must hold, per the pre-registration):
  1. Krawczyk inclusion K(Z) subset int(Z);
  2. left-nullvector angle bound sin(theta) < 0.1;
  3. both nondegeneracy constants exclude zero;
  4. the FD self-verification battery passes at the new nominal BEFORE
     the certificate is issued.

Usage: python3 second_fold_krawczyk.py
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import mpmath
import numpy as np

HERE = Path(__file__).parent
VC = HERE.parent
A025 = VC / 'a025_fold'
sys.path.insert(0, str(A025))
sys.path.insert(0, str(VC))

import a025_fold_krawczyk as kr  # noqa: E402
import interval_lib as il        # noqa: E402

DY, DIM, DIMZ = kr.DY, kr.DIM, kr.DIMZ      # 192, 193, 387 (N=64)
MS_NPZ = HERE / 'second_fold_ms.npz'
STATUS = HERE / 'second_fold_status.json'
OUT = HERE / 'second_fold_krawczyk.json'
BOX_PAD = 1e-8
LADDER = (1.0, 2.5, 6.0, 15.0, 40.0)
BASE_RADII = (2e-9, 2e-8, 1.5e-8)


def verify_and_polish(z_nom, ell, log):
    """Steps 0-2 of the lower-fold certificate at the new nominal:
    pipeline cross-checks, the FD battery, float polish. Returns
    (z_c, mn, fd_record) or None on assertion failure."""
    t0 = time.time()
    # ---- 0. cross-checks against the committed pipeline -------------
    res_p, J_p = kr.pipeline_residual_jac(z_nom)
    Gp_pt = kr.assemble_point(z_nom, ell)
    dJ = np.abs(Gp_pt[:DIM, :DIM] - J_p).max()
    dFt = np.abs(Gp_pt[:DIM, DIM] - kr.pipeline_dF_dtau(z_nom)).max()
    phi0 = z_nom[DY + 1] / z_nom[DY]
    dS = np.abs(kr.circ_mat_point(phi0, 0) - kr.pipeline_shift(phi0)).max()
    log(f'  cross-check: |J-pipeline J|={dJ:.2e}  '
        f'|F_tau-pipeline|={dFt:.2e}  |S-pipeline S|={dS:.2e}')
    if not (dJ < 1e-10 and dFt < 1e-10 and dS < 1e-12):
        log('  CROSS-CHECK FAILED — no certificate issued')
        return None
    # ---- 1. FD verification of the Jv-row block -----------------------
    v_c = z_nom[DY + 2:].copy()
    eps = 3e-6
    fd_err = 0.0
    for k in range(DIM + 1):
        e = np.zeros(DIM + 1)
        e[k] = eps
        zp = z_nom.copy()
        zp[:DIM + 1] += e[:DIM + 1]
        zm = z_nom.copy()
        zm[:DIM + 1] -= e[:DIM + 1]
        gp = kr.assemble_point(zp, ell)[:DIM, :DIM] @ v_c
        gm = kr.assemble_point(zm, ell)[:DIM, :DIM] @ v_c
        fd = (gp - gm) / (2 * eps)
        an = Gp_pt[DIM:2 * DIM, k]
        fd_err = max(fd_err, np.abs(fd - an).max()
                     / max(1.0, np.abs(an).max()))
    ps0 = np.linalg.svd(Gp_pt[:DIM, :DIM])[0][:, -1]
    if ps0 @ v_c < 0:
        ps0 = -ps0
    eps2 = 3e-4
    zp = z_nom.copy()
    zp[:DIM] += eps2 * v_c
    zm = z_nom.copy()
    zm[:DIM] -= eps2 * v_c
    Fp = kr.pipeline_residual_jac(zp)[0]
    Fm = kr.pipeline_residual_jac(zm)[0]
    fd_dot = ps0 @ (Fp - 2 * res_p + Fm) / eps2 ** 2
    an_dot = ps0 @ kr.D2vv_point(z_nom)
    d2_err = abs(fd_dot - an_dot) / max(abs(an_dot), 1e-12)
    log(f'  FD: Jv-block columns max rel err = {fd_err:.2e}; '
        f'psi^T D2F[v,v] rel err = {d2_err:.2e} '
        f'(fd {fd_dot:.4e} vs analytic {an_dot:.4e})')
    if not (fd_err < 1e-4 and d2_err < 0.1):
        log('  FD VERIFICATION FAILED — no certificate issued')
        return None
    fd_record = dict(J_vs_pipeline_max=float(dJ),
                     Ftau_vs_pipeline_max=float(dFt),
                     S_vs_pipeline_max=float(dS),
                     Jv_block_columns_fd_max_rel=float(fd_err),
                     psi_dot_D2vv_fd_rel=float(d2_err),
                     psi_dot_D2vv_fd=float(fd_dot),
                     psi_dot_D2vv_analytic=float(an_dot))
    # ---- 2. float polish of the nominal point -------------------------
    z_c = z_nom.copy()
    Gc = kr.eval_G_point(z_c, ell)
    mn = max(np.abs(Gc[0]).max(), np.abs(Gc[1]).max())
    log(f'  committed nominal |G|_inf ~ {mn:.2e}')
    for it in range(6):
        Gp = kr.assemble_point(z_c, ell)
        try:
            step = np.linalg.solve(Gp, -0.5 * (Gc[0] + Gc[1]))
        except np.linalg.LinAlgError:
            break
        z_try = z_c + step
        Gt = kr.eval_G_point(z_try, ell)
        mn_try = max(np.abs(Gt[0]).max(), np.abs(Gt[1]).max())
        if mn_try < mn:
            z_c, Gc, mn = z_try, Gt, mn_try
            log(f'  polish it={it}: |G|_inf -> {mn:.2e}')
        else:
            log(f'  polish it={it}: no improvement ({mn_try:.2e})')
            break
    log(f'  polished center: tau = {z_c[DY + 1]:.15f}, |G|_inf = {mn:.2e} '
        f'({time.time() - t0:.0f}s)')
    return z_c, mn, fd_record


def krawczyk_rung(z_c, ell, tau_lo, tau_hi, ry, rt, rv, iters, log):
    """One radii rung: steps 3-5 of the lower-fold certificate. Returns
    (ok, payload) — payload carries the final box, the iteration log,
    the nullvector record and the nondegeneracy intervals."""
    zlo = z_c.copy()
    zhi = z_c.copy()
    zlo[:DY] -= ry
    zhi[:DY] += ry
    zlo[DY] -= rt
    zhi[DY] += rt
    zlo[DY + 2:] -= rv
    zhi[DY + 2:] += rv
    zlo[DY + 1] = tau_lo
    zhi[DY + 1] = tau_hi
    YG = np.linalg.inv(kr.assemble_point(z_c, ell))
    log(f'  |Y_G|_inf = {np.abs(YG).max():.2e}, '
        f'max row 1-norm = {np.abs(YG).sum(axis=1).max():.2e}')
    Zlo, Zhi = zlo.copy(), zhi.copy()
    it_log = []
    K = None
    certified_box = None
    for it in range(iters):
        Gp_iv, J_iv, Ftau_iv = kr.assemble(Zlo, Zhi, ell)
        Gc = kr.eval_G_point(z_c, ell)
        YZG = il.imatvec((YG, YG), Gc)
        A_iv = il.imatmul((YG, YG), Gp_iv)
        ImYA = il.isub((np.eye(DIMZ), np.eye(DIMZ)), A_iv)
        dZ = (Zlo - z_c, Zhi - z_c)
        prod = il.imatvec(ImYA, dZ)
        K = il.isub(il.isub(il.interval(z_c), YZG), prod)
        ok = bool(np.all(K[0] > Zlo) and np.all(K[1] < Zhi))
        gap = float(np.min(np.minimum(K[0] - Zlo, Zhi - K[1])))
        kw = float(np.max(K[1] - K[0]))
        zw = float(np.max(Zhi - Zlo))
        it_log.append(dict(iteration=it, inclusion=ok, min_gap=gap,
                           k_max_width=kw, z_max_width=zw,
                           tau_K=[float(K[0][DY + 1]),
                                  float(K[1][DY + 1])]))
        log(f'  Krawczyk it={it}: inclusion={ok} min_gap={gap:.2e} '
            f'K_width={kw:.2e} (Z_width={zw:.2e}) '
            f'tau_K=[{K[0][DY + 1]:.15f},{K[1][DY + 1]:.15f}]')
        if not ok:
            if it == 0:
                log('    rung failed at it=0 (radii too small/large)')
                return False, dict(iterations=it_log)
            log('    (tightening saturated; keeping the previous '
                'certified box)')
            break
        certified_box = (Zlo.copy(), Zhi.copy())
        Zlo, Zhi = K[0].copy(), K[1].copy()
        z_c = 0.5 * (Zlo + Zhi)
        if kw < 1e-13:
            break
    if certified_box is None:
        return False, dict(iterations=it_log)
    Zlo, Zhi = certified_box
    # ---- 4. left-nullvector enclosure ---------------------------------
    Gp_iv, J_iv, Ftau_iv = kr.assemble(Zlo, Zhi, ell)
    J_c = 0.5 * (J_iv[0] + J_iv[1])
    U, s, Vt = np.linalg.svd(J_c)
    psi_c = U[:, -1].copy()
    v_fin = 0.5 * (Zlo[DY + 2:] + Zhi[DY + 2:])
    if psi_c @ v_fin < 0:
        psi_c = -psi_c
    r0 = float(np.linalg.norm(J_c.T @ psi_c)) * (1.0 + 1e-12) + 1e-300
    W = 0.5 * (J_iv[1] - J_iv[0])
    dJ2 = float(np.linalg.norm(W, 2)) * (1.0 + 1e-9) + 1e-300
    sig2 = float(s[-2])
    sig2_lb = sig2 * (1.0 - 1e-9) - 1e-12 * float(s[0]) - 1e-300
    sin_th = (dJ2 + r0) / (sig2_lb - dJ2)
    dpsi = np.sqrt(2.0) * min(sin_th, 1.0)
    log(f'  psi: sigma_min={s[-1]:.2e} sigma_2={sig2:.3e} dJ2={dJ2:.2e} '
        f'r0={r0:.2e} sin(theta)<={sin_th:.2e} halfwidth={dpsi:.2e}')
    if not sin_th < 0.1:
        log('    nullvector angle bound too weak — rung fails')
        return False, dict(iterations=it_log,
                           nullvector_angle_bound=float(sin_th))
    # ---- 5. nondegeneracy constants ------------------------------------
    Ftau_c = 0.5 * (Ftau_iv[0] + Ftau_iv[1])
    wFt = kr.idd_dot(psi_c, dpsi, Ftau_c, Ftau_iv)
    D2_iv = kr.D2vv_iv(Zlo, Zhi)
    D2_c = 0.5 * (D2_iv[0] + D2_iv[1])
    wD2 = kr.idd_dot(psi_c, dpsi, D2_c, D2_iv)
    excl = (wFt[0] > 0 or wFt[1] < 0) and (wD2[0] > 0 or wD2[1] < 0)
    log(f'  w^T F_tau    in [{wFt[0]:.6f}, {wFt[1]:.6f}]  '
        f'excludes 0: {wFt[0] > 0 or wFt[1] < 0}')
    log(f'  w^T D2F[v,v] in [{wD2[0]:.6e}, {wD2[1]:.6e}]  '
        f'excludes 0: {wD2[0] > 0 or wD2[1] < 0}')
    if not excl:
        log('    nondegeneracy constant includes zero — rung fails')
        return False, dict(iterations=it_log, wF_tau_interval=wFt,
                           wD2F_vv_interval=wD2)
    payload = dict(
        iterations=it_log,
        tau_final_enclosure=[float(Zlo[DY + 1]), float(Zhi[DY + 1])],
        Z_final_width=float(np.max(Zhi - Zlo)),
        left_nullvector=dict(
            sigma_min_J=float(s[-1]), sigma_2_J=sig2, dJ2_bound=dJ2,
            r0=r0, sin_theta_bound=float(sin_th),
            componentwise_halfwidth=float(dpsi)),
        wF_tau_interval=[float(wFt[0]), float(wFt[1])],
        wD2F_vv_interval=[float(wD2[0]), float(wD2[1])],
        nondegeneracy_excludes_zero=True)
    return True, payload


def main():
    t0 = time.time()
    logf = open(HERE / 'second_fold_krawczyk.log', 'a', buffering=1)

    def log(msg):
        stamp = time.strftime('%Y-%m-%d %H:%M:%S')
        print(msg)
        logf.write(f'[{stamp}] {msg}\n')

    if not MS_NPZ.exists():
        log('second_fold_ms.npz not found — no accepted fold candidate; '
            'stage C not applicable')
        OUT.write_text(json.dumps(
            dict(status='NOT APPLICABLE — no accepted fold candidate from '
                        'stage B', date=time.strftime('%Y-%m-%d'))))
        return
    saved = np.load(MS_NPZ)
    z_nom = saved['z_m64'].astype(float)
    ell = saved['ell_m64'].astype(float)
    st = json.loads(STATUS.read_text()) if STATUS.exists() else {}
    taus = st.get('stageB', {}).get('three_order_taus')
    if not taus:
        taus = [float(saved[f'z_m{m}'][3 * m + 1]) for m in (64, 96, 128)]
    tau_lo = float(np.nextafter(min(taus) - BOX_PAD, -np.inf))
    tau_hi = float(np.nextafter(max(taus) + BOX_PAD, np.inf))
    log('Second-fold interval Krawczyk (stage C, pre-registered §4)')
    log(f'  nominal m=64 tau = {z_nom[DY + 1]:.15f}')
    log(f'  three-order taus: {[f"{t:.12f}" for t in taus]}')
    log(f'  tau-box: [{tau_lo:.15f}, {tau_hi:.15f}] '
        f'(three-order spread ± {BOX_PAD:g})')

    # steps 0-2 once (independent of the radii)
    got = verify_and_polish(z_nom, ell, log)
    if got is None:
        OUT.write_text(json.dumps(
            dict(status='FAILED — self-verification battery did not pass '
                        'at the new nominal; no certificate issued',
                 date=time.strftime('%Y-%m-%d'),
                 tau_box=[tau_lo, tau_hi])))
        return
    z_c, mn, fd_record = got
    if not (tau_lo <= z_c[DY + 1] <= tau_hi):
        log('polished tau outside the constructed box — widening the box '
            'to contain the polished center (recorded as a deviation)')
        tau_lo = min(tau_lo, float(np.nextafter(z_c[DY + 1], -np.inf)))
        tau_hi = max(tau_hi, float(np.nextafter(z_c[DY + 1], np.inf)))

    ladder_log = []
    success = None
    for rung in LADDER:
        ry, rt, rv = [r * rung for r in BASE_RADII]
        log(f'--- radii rung x{rung:g}: ry={ry:.2e} rt={rt:.2e} '
            f'rv={rv:.2e} ---')
        ok, payload = krawczyk_rung(z_c, ell, tau_lo, tau_hi, ry, rt, rv,
                                    4, log)
        ladder_log.append(dict(rung=float(rung), ry=ry, rt=rt, rv=rv,
                               ok=ok))
        if ok:
            success = (rung, ry, rt, rv, payload)
            break
    if success is None:
        log('CERTIFICATE FAILED — all radii rungs exhausted; the candidate '
            'fold remains an uncertified nominal/MS finding')
        OUT.write_text(json.dumps(
            dict(status='FAILED — no Krawczyk inclusion at any radii '
                        'rung; the candidate second fold is NOT certified',
                 date=time.strftime('%Y-%m-%d'),
                 tau_box=[tau_lo, tau_hi],
                 nominal_tau=float(z_nom[DY + 1]),
                 polished_tau=float(z_c[DY + 1]),
                 polished_G_inf=float(mn),
                 fd_verification=fd_record,
                 radii_ladder=ladder_log,
                 runtime_s=round(time.time() - t0, 1)), indent=2))
        return
    rung, ry, rt, rv, payload = success
    out = dict(
        title='Second fold (upper branch) — interval Krawczyk certificate',
        status='CERTIFIED (interval Krawczyk on the m=64 Fourier '
               'collocation Moore-Spence system): unique zero of the MS '
               'system in the box, G\' nonsingular throughout the box '
               '(simple nondegenerate fold of the discretized system), '
               'and both nondegeneracy constants exclude zero. Scope: '
               'discrete m=64 system only; the continuum off-grid stage '
               'and the RFDE lift remain open (as for the lower fold).',
        collocation_order=64,
        system='F(w,tau) collocation map of a025_fold_pipeline.py with the '
               'exact circulant shift S(phi); MS system '
               'G(z)=[F; Jv; ell.v-1], z=(w,tau,v) in R^387 — the same '
               'assembly as a025_fold_krawczyk.py (the lower-fold '
               'certificate), applied at the second-fold nominal',
        seed_and_acceptance=dict(
            stageB_ms_m64_tau=float(z_nom[DY + 1]),
            three_order_taus=[float(t) for t in taus],
            three_order_agreement=float(st.get('stageB', {}).get(
                'three_order_agreement', float('nan')))),
        tau_box=[tau_lo, tau_hi],
        tau_box_source='constructed: three-order tau spread ± 1e-8 '
                       '(no prior interval exists for the second fold)',
        tau_final_enclosure=payload['tau_final_enclosure'],
        krawczyk_iterations=payload['iterations'],
        krawczyk_margin_definition='min_gap = min over components of '
                                   'min(K_lo - Z_lo, Z_hi - K_hi); '
                                   'inclusion requires min_gap > 0',
        radii_used=dict(ry=ry, rt=rt, rv=rv, ladder_rung=float(rung)),
        radii_ladder=ladder_log,
        center_after_polish=dict(tau=float(z_c[DY + 1]),
                                 G_inf=float(mn)),
        left_nullvector=payload['left_nullvector'],
        wF_tau_interval=payload['wF_tau_interval'],
        wD2F_vv_interval=payload['wD2F_vv_interval'],
        nondegeneracy_excludes_zero=True,
        fd_verification=fd_record,
        relation_to_lower_fold=dict(
            lower_fold_tau_enclosure=st.get('stage0', {}).get(
                'inherited_certificates', {}).get('lower_fold_krawczyk'),
            note='the lower fold keeps its own certificate '
                 '(a025_fold_krawczyk.json); this certificate is for the '
                 'second fold of the upper branch'),
        environment=f'Python {sys.version.split()[0]}, numpy '
                    f'{np.__version__}, mpmath {mpmath.__version__}',
        runtime_s=round(time.time() - t0, 1),
    )
    OUT.write_text(json.dumps(out, indent=2))
    log(f'written {OUT.name} ({time.time() - t0:.0f}s)')
    log(f"CERTIFICATE OK: unique MS zero with tau_f2 in "
        f"[{payload['tau_final_enclosure'][0]:.12f}, "
        f"{payload['tau_final_enclosure'][1]:.12f}] "
        f"(box {tau_lo:.12f}..{tau_hi:.12f})")


if __name__ == '__main__':
    main()

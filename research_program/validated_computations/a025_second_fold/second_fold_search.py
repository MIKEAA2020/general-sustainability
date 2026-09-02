#!/usr/bin/env python3
"""Second-fold search on the upper branch — EXECUTION of the pre-registered
plan (frozen in SECOND_FOLD_PREREGISTRATION.md, committed before this run).

Owner protocol (verbatim):
  1. Seeded carry continuation from the converged cycle near tau+ =
     150.358, stepping DOWNWARD in tau, carrying the delay history.
  2. Collocation / Moore-Spence refinement at any suspected turning point.
  3. (stage C, separate script second_fold_krawczyk.py) Krawczyk
     certification if a candidate fold is found.
  4. Report separately: mathematical branch existence, generic basin
     reachability, any collocation failures.

Stages (resumable; `python3 second_fold_search.py all` or a stage name):
  0   environment, model-equivalence, seed and certificate checks
  A   seeded carry continuation downward (natural parameter, the
      campaign's frozen rules) with Floquet tracking at every point
  B   turning-point adjudication: Moore-Spence m=64 (+ acceptance rules),
      pseudo-arclength pass, three-order MS if accepted, resolution
      ladder (m=96/128 cross-checks) if the pass cannot traverse and the
      MS solve is rejected
  D   generic basin reachability grids (A: the 130-147 gap; B/B':
      around the fold candidate or the stall point)
  R   results JSON assembly (the report .md is written from the records)

Everything writes into this directory only. The arena agent 1 folder is
never touched; the frozen P4 campaign directory is never written to.
"""
from __future__ import annotations

import csv as csvmod
import hashlib
import json
import platform
import re
import subprocess
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).parent
VC = HERE.parent                       # validated_computations
A025 = VC / 'a025_fold'
CAMP = VC / 'p4_five_regime_campaign'
sys.path.insert(0, str(A025))
sys.path.insert(0, str(CAMP))

import a025_fold_pipeline as fp        # noqa: E402
import p4_campaign as pc               # noqa: E402
from a025_model import PAR, equilibrium, rhs  # noqa: E402
from p4_kernels import basin_run, basin_rhs  # noqa: E402

# ---- frozen constants (SECOND_FOLD_PREREGISTRATION.md) --------------------
SEED_KEY = '150.30847731'
SEED_TAU = 150.30847731014137          # = tau+ - 0.05
TAU_FLOOR = 5.587236199                # certified lower fold tau + 1e-9
FAM = 'second_fold_upper'
LOWER_FOLD_LO = 5.5872361977           # certified enclosure widened 1e-6/2e-9
LOWER_FOLD_HI = 5.5872361997
MS_TOL = 1e-10                         # MS acceptance residual
MS_TAU_PROX = 1.0                      # MS acceptance: |tau_f - tau_stall| <=
ORDER_AGREEMENT = 1e-6                 # three-order agreement criterion
DT = 0.02                              # basin machinery (the campaign's)
HORIZON = 4.0e4
TAIL = 1800.0
RING_YR = 1000.0
GRID_A = [133.0, 136.0, 139.0, 142.0, 144.0, 145.0, 146.0]
GRID_B_OFFSETS = (-2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0)
PA = np.array([PAR['r'], PAR['K'], PAR['q'], PAR['eta'], PAR['Emax'],
               PAR['delta0'], PAR['Dref'], PAR['taum'], PAR['k']])

STATUS = HERE / 'second_fold_status.json'
LOG = HERE / 'second_fold_run.log'
RESULTS = HERE / 'second_fold_results.json'
BRANCH_CSV = HERE / 'second_fold_branch.csv'
BASIN_CSV = HERE / 'second_fold_basin.csv'
ORBITS_NPZ = HERE / 'second_fold_orbits.npz'
MS_NPZ = HERE / 'second_fold_ms.npz'


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_status():
    if STATUS.exists():
        return json.loads(STATUS.read_text())
    return {}


def save_status(st):
    STATUS.write_text(json.dumps(st, indent=1, default=str))


def git_head():
    try:
        return subprocess.run(
            ['git', 'rev-parse', 'HEAD'], cwd=str(VC.parent),
            capture_output=True, text=True, timeout=10).stdout.strip()
    except Exception:
        return 'unavailable'


def num(x):
    """Sanitize for JSON: finite float or None."""
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    return v if np.isfinite(v) else None


# ==========================================================================
# Stage 0 — environment, model equivalence, seed, inherited certificates
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
        seeds='none (deterministic; fixed LCG seed 1 only for the '
              'Arnoldi start vectors)',
        git_head_at_execution=git_head(),
        code_hashes={
            'a025_model.py': sha256(A025 / 'a025_model.py'),
            'a025_fold_pipeline.py': sha256(A025 / 'a025_fold_pipeline.py'),
            'p4_kernels.py': sha256(CAMP / 'p4_kernels.py'),
            'p4_campaign.py': sha256(CAMP / 'p4_campaign.py'),
            'second_fold_search.py': sha256(HERE / 'second_fold_search.py'),
        },
        preregistration_sha256=sha256(
            HERE / 'SECOND_FOLD_PREREGISTRATION.md'))
    # PAR bit-check against the declared numbers
    declared = dict(r=0.02, K=100.0, q=0.001, eta=0.914, Emax=30.0,
                    delta0=0.01, Dref=1.0, taum=5.0, k=10.0,
                    delta=np.log(2.0) / 10.0, Zref=1.0)
    for key, val in declared.items():
        assert abs(PAR[key] - val) < 1e-15, key
    env['par_matches_preregistration'] = True
    # numba RHS equivalence to the committed a025_model.rhs
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
    # seed verification (frozen: residual <= 1e-10 before any step)
    fp.configure(64)
    seed = np.load(CAMP / 'p4_branch_orbits.npz')[SEED_KEY]
    rn = float(np.linalg.norm(
        fp.residual_jac(seed, SEED_TAU, want_jac=False), np.inf))
    env['seed'] = dict(
        source='p4_five_regime_campaign/p4_branch_orbits.npz['
               + SEED_KEY + ']',
        tau=SEED_TAU, dim=int(seed.shape[0]),
        residual=rn, accepted=bool(rn <= 1e-10))
    assert rn <= 1e-10, f'seed residual {rn}'
    # inherited certificates: the two Hopf taus and the lower-fold box
    hopf = json.loads((A025 / 'a025_interval_hopf.json').read_text())
    certs = hopf['hopf_certificates']
    tau_minus_iv = [float(x) for x in re.findall(
        r'-?\d+\.?\d*(?:e-?\d+)?', certs[0]['tau_k0'])[:2]]
    tau_plus_iv = [float(x) for x in re.findall(
        r'-?\d+\.?\d*(?:e-?\d+)?', certs[1]['tau_k1'])[:2]]
    from a025_model import tau_of_omega
    tm = float(tau_of_omega(0.025191543577286703, branch_k=0))
    tp = float(tau_of_omega(0.0394366, branch_k=1))
    inside = (tau_minus_iv[0] <= tm <= tau_minus_iv[1]
              and tau_plus_iv[0] <= tp <= tau_plus_iv[1])
    env['inherited_certificates'] = dict(
        tau_minus_interval=tau_minus_iv,
        tau_plus_interval=tau_plus_iv,
        model_tau_minus_reproduction=tm,
        model_tau_plus_reproduction=tp,
        reproductions_inside=bool(inside),
        lower_fold_krawczyk=json.loads(
            (A025 / 'a025_fold_krawczyk.json').read_text()).get(
                'tau_final_enclosure'))
    assert inside, 'Hopf tau reproduction outside the certified intervals'
    env['equilibrium'] = [float(x) for x in equilibrium()]
    (HERE / 'second_fold_environment.json').write_text(
        json.dumps(env, indent=1))
    log.info(f'stage 0 done: rhs equivalence {maxdiff:.2e}; seed residual '
             f'{rn:.2e}; tau-/tau+ reproductions inside the certified '
             f'intervals; HEAD {env["git_head_at_execution"][:10]}')
    st['stage0'] = env
    save_status(st)


# ==========================================================================
# Stage A — seeded carry continuation downward
# ==========================================================================
def stageA(log, st):
    fp.configure(64)
    seed = np.load(CAMP / 'p4_branch_orbits.npz')[SEED_KEY]
    records = []
    w_cache = {round(SEED_TAU, 9): seed.copy()}
    flo = pc.flo_at(seed, SEED_TAU)
    records.append(pc.branch_row(
        FAM, 1, 'switch', SEED_TAU, seed,
        float(np.linalg.norm(fp.residual_jac(seed, SEED_TAU,
                                             want_jac=False), np.inf)),
        fp.nyquist_relative(seed), True,
        dict(cont_step=0.0, n_fail=0), flo))
    log.info(f'seed: tau={SEED_TAU:.9f}, ptp={fp.peak_to_peak(seed):.4f}, '
             f'mu1={flo["mu1_mod"]}')
    t0 = time.time()
    w_end, tau_end, w_prev, tau_prev, npts = pc.continue_tau(
        seed, SEED_TAU, -1, TAU_FLOOR, dtau0=0.2, family=FAM, pid0=1,
        records=records, log=log, w_cache=w_cache)
    wall = time.time() - t0
    # +1-crossing refinement (the campaign's own machinery)
    log.info('+1 crossing bracket refinement:')
    brackets = pc.refine_crossing(FAM, records, log, w_cache)
    reached_floor = bool(tau_end <= TAU_FLOOR + 1e-6)
    stalled = bool(not reached_floor)
    if npts == 0 and not reached_floor:
        log.info('continuation accepted no points below the seed '
                 '(immediate stall)')
    out = dict(
        n_records=len(records),
        n_natural=int(npts),
        tau_start=SEED_TAU, tau_end=float(tau_end),
        reached_floor=reached_floor,
        stalled_before_floor=stalled,
        wall_s=round(wall, 1),
        crossing_brackets=brackets,
        last=dict(tau=float(tau_end),
                  T=num(fp.unpack(w_end)[1]),
                  N_ptp=num(np.ptp(fp.unpack(w_end)[0][:, 0])),
                  residual=num(np.linalg.norm(
                      fp.residual_jac(w_end, tau_end, want_jac=False),
                      np.inf))))
    pc.write_csv(BRANCH_CSV, records, pc.BRANCH_COLS)
    np.savez(ORBITS_NPZ, **{str(k): v for k, v in w_cache.items()})
    np.savez(HERE / 'second_fold_stageA_end.npz',
             w_end=np.asarray(w_end, float), tau_end=float(tau_end),
             w_prev=(np.zeros(0) if w_prev is None
                     else np.asarray(w_prev, float)),
             tau_prev=(np.nan if tau_prev is None else float(tau_prev)))
    st['stageA'] = out
    save_status(st)
    a_status = 'floor reached' if reached_floor else 'STALLED before floor'
    log.info(f'stage A done: {len(records)} records, '
             f'tau_end={tau_end:.9f} ({a_status}), wall {wall:.0f}s')


# ==========================================================================
# Stage B — turning-point adjudication
# ==========================================================================
def ms_three_orders(w64, tau64, z64, ell64, res64, log, results):
    """Three-order Moore-Spence (the accepted m=64 solve + Fourier-resampled
    m=96/128 seeds — the campaign's method); writes second_fold_ms.npz."""
    orders = {64: dict(z=np.asarray(z64, float),
                       ell=np.asarray(ell64, float))}
    results['ms2_m64'] = dict(
        tau_f=num(orders[64]['z'][fp.DIM]),
        T_f=num(orders[64]['z'][fp.DIM_Y]),
        residual=float(res64))
    fp.configure(64)
    Y64, T64 = fp.unpack(np.asarray(w64, float))
    DIM64, DIMY64 = fp.DIM, fp.DIM_Y      # 193, 192
    for m in (96, 128):
        fp.configure(m)
        Ynew = pc._fourier_eval_cols(Y64, m)
        w_seed = fp.pack(Ynew, T64)
        v = orders[64]['z'][DIM64 + 1:]
        vY = v[:DIMY64].reshape(64, 3)
        vT = v[DIMY64]
        Vnew = pc._fourier_eval_cols(vY, m)
        v_seed = np.r_[Vnew.reshape(-1), vT]
        ell_seed = v_seed / (v_seed @ v_seed)
        t0 = time.time()
        z, ell, res = fp.moore_spence(
            None, None, z0=np.r_[w_seed, float(tau64), v_seed],
            ell0=ell_seed)
        orders[m] = dict(z=z, ell=ell)
        log.info(f'  [MS2 m={m}] tau_f={float(z[fp.DIM]):.12f}, '
                 f'T_f={float(z[fp.DIM_Y]):.6f}, |M|={res:.2e} '
                 f'({time.time() - t0:.0f}s)')
        results[f'ms2_m{m}'] = dict(tau_f=num(z[fp.DIM]),
                                    T_f=num(z[fp.DIM_Y]),
                                    residual=float(res))
    fp.configure(64)
    taus = [float(orders[m]['z'][3 * m + 1]) for m in (64, 96, 128)]
    agree = max(taus) - min(taus)
    results['three_order_taus'] = taus
    results['three_order_agreement'] = float(agree)
    results['three_order_pass'] = bool(agree <= ORDER_AGREEMENT)
    log.info(f'  [MS2] three-order tau agreement: {agree:.3e} '
             f'({"PASS" if agree <= ORDER_AGREEMENT else "FAIL"} vs '
             f'{ORDER_AGREEMENT:g})')
    np.savez(MS_NPZ,
             **{f'z_m{m}': orders[m]['z'] for m in orders},
             **{f'ell_m{m}': orders[m]['ell'] for m in orders})
    return orders, agree


def resolution_ladder(w_last, tau_last, records, log, results):
    """m=96/128 fresh Newton solves seeded by Fourier-resampling of the
    last converged m=64 orbit (pre-registered cross-checks)."""
    fp.configure(64)
    Y64, T64 = fp.unpack(np.asarray(w_last, float))
    for m in (96, 128):
        fp.configure(m)
        Ynew = pc._fourier_eval_cols(Y64, m)
        w_seed = fp.pack(Ynew, T64)
        t0 = time.time()
        w_new, ok, rn = fp.newton(w_seed, float(tau_last))
        wall = time.time() - t0
        ptp = fp.peak_to_peak(w_new)
        records.append(pc.branch_row(
            FAM, 7000 + m, f'resolution-m{m}', float(tau_last), w_new, rn,
            fp.nyquist_relative(w_new), bool(ok),
            dict(cont_step=0.0, n_fail=0), None))
        records[-1]['wall_s'] = round(wall, 1)
        results[f'resolution_m{m}'] = dict(
            tau=float(tau_last), newton_ok=bool(ok), residual=float(rn),
            N_ptp=num(ptp), nyquist=num(fp.nyquist_relative(w_new)),
            wall_s=round(wall, 1))
        log.info(f'  [resolution m={m}] ok={ok}, res={rn:.2e}, '
                 f'ptp={ptp:.3f} ({wall:.0f}s)')
    fp.configure(64)


def stageB(log, st):
    if 'stageA' not in st:
        raise RuntimeError('run stage A first')
    if not st['stageA'].get('stalled_before_floor'):
        log.info('stage B: not triggered (stage A reached the floor)')
        st['stageB'] = dict(triggered=False,
                            reason='floor reached without stall')
        save_status(st)
        return
    fp.configure(64)
    orb = np.load(ORBITS_NPZ)
    w_cache = {k: orb[k] for k in orb.files}
    end = np.load(HERE / 'second_fold_stageA_end.npz')
    w_end = np.asarray(end['w_end'], float)
    tau_end = float(end['tau_end'])
    w_prev = np.asarray(end['w_prev'], float)
    tau_prev = float(end['tau_prev'])
    records = []
    results = dict(triggered=True, stall_tau=float(tau_end))

    # ---- B.1: Moore-Spence m=64 from the stall point ---------------------
    log.info(f'B.1: Moore-Spence m=64 from the stall point '
             f'tau={tau_end:.9f}')
    t0 = time.time()
    z, ell, res = fp.moore_spence(w_end, tau_end)
    tau_f = num(z[fp.DIM])
    wall = time.time() - t0
    T_f = num(z[fp.DIM_Y])
    Yf = z[:fp.DIM_Y].reshape(fp.N_NODES, 3)
    results['ms_m64'] = dict(tau_f=tau_f, T_f=T_f,
                             residual=float(res),
                             N_ptp=num(np.ptp(Yf[:, 0])),
                             wall_s=round(wall, 1))
    log.info(f'  MS m=64: tau_f={tau_f}, T_f={T_f}, |M|={res:.2e} '
             f'({wall:.0f}s)')
    is_lower = bool(tau_f is not None
                    and LOWER_FOLD_LO <= tau_f <= LOWER_FOLD_HI)
    accepted = bool(res <= MS_TOL and tau_f is not None
                    and abs(tau_f - tau_end) <= MS_TAU_PROX
                    and not is_lower)
    results['ms_m64_acceptance'] = dict(
        residual_ok=bool(res <= MS_TOL),
        proximity_ok=bool(tau_f is not None
                          and abs(tau_f - tau_end) <= MS_TAU_PROX),
        is_lower_fold=is_lower,
        accepted=accepted)
    if is_lower:
        log.info(f'  MS converged to the ALREADY-CERTIFIED lower fold '
                 f'({tau_f} inside [{LOWER_FOLD_LO}, {LOWER_FOLD_HI}]) — '
                 f'a connection finding, NOT a second fold')
    elif accepted:
        log.info('  MS ACCEPTED: candidate second fold')

    # ---- B.2: pseudo-arclength pass through the suspected turn -----------
    if w_prev.size and np.isfinite(tau_prev):
        log.info('B.2: pseudo-arclength pass through the suspected turn')
        w_c, tau_c, n_arc, past = pc.pseudo_arclength_pass(
            w_end, tau_end, w_prev, tau_prev, ds0=0.05, family=FAM,
            pid0=500, records=records, log=log,
            tau_window=(TAU_FLOOR, 150.5), w_cache=w_cache)
        results['arclength'] = dict(n_points=int(n_arc),
                                    points_past_turn=int(past),
                                    tau_end=float(tau_c))
        arc_failed = bool(n_arc == 0 or past == 0)
    else:
        log.info('B.2: arclength not applicable (no secant available — '
                 'immediate stall)')
        results['arclength'] = dict(n_points=0, points_past_turn=0,
                                    not_applicable=True)
        arc_failed = True

    # ---- B.3: three-order MS if accepted ---------------------------------
    if accepted:
        log.info('B.3: three-order Moore-Spence (m=64/96/128)')
        orders, agree = ms_three_orders(w_end, tau_end, z, ell, res, log,
                                        results)
        results['fold_candidate'] = dict(
            tau_f_m64=tau_f, three_order_agreement=float(agree),
            next_stage='C (second_fold_krawczyk.py)')
    # ---- B.4: resolution ladder if MS rejected AND pass failed ------------
    if (not accepted) and arc_failed:
        log.info('B.4: resolution ladder (m=96/128 cross-checks) — the '
                 'stall is recorded as a collocation failure')
        resolution_ladder(w_end, tau_end, records, log, results)

    # persist: merge stage-B rows into the branch CSV, refresh orbits npz
    all_rows = list(csvmod.DictReader(open(BRANCH_CSV)))
    pc.write_csv(BRANCH_CSV, all_rows + records, pc.BRANCH_COLS)
    merged_cache = {k: orb[k] for k in orb.files}
    for k, v in w_cache.items():
        merged_cache[str(round(float(k), 9))] = v
    np.savez(ORBITS_NPZ, **merged_cache)
    st['stageB'] = results
    save_status(st)
    log.info('stage B done')


# ==========================================================================
# Stage D — generic basin reachability
# ==========================================================================
def stageD(log, st):
    eq = equilibrium()
    N_, Z_, E_ = eq
    hist = {'H1': (90.0, float(Z_), float(0.5 * E_)),
            'H2': (5.0, float(Z_), 15.0),
            'H3': (float(1.01 * N_), float(1.01 * Z_), float(1.01 * E_))}
    n_tail = int(round(TAIL / DT))
    n_ring = int(round(RING_YR / DT))
    jobs = [(t, h, DT) for t in GRID_A for h in ('H1', 'H2', 'H3')]
    center = None
    grid_b = []
    if st.get('stageB', {}).get('ms_m64_acceptance', {}).get('accepted'):
        center = num(st['stageB']['ms_m64']['tau_f'])
    elif st.get('stageA', {}).get('stalled_before_floor'):
        center = num(st['stageA']['tau_end'])
    c2 = None
    if center is not None:
        c2 = round(round(center / 0.05) * 0.05, 2)
        for off in GRID_B_OFFSETS:
            grid_b.append(round(round((center + off) / 0.05) * 0.05, 2))
        jobs += [(t, h, DT) for t in grid_b for h in ('H1', 'H2', 'H3')]
        jobs += [(c2, h, DT / 2) for h in ('H1', 'H2', 'H3')]
    seen = set()
    jobs = [j for j in jobs if (j[0], j[1], j[2]) not in seen
            and not seen.add((j[0], j[1], j[2]))]
    rows = []
    t_all = time.time()
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
        log.info(f'  basin tau={tau:8.3f} {hc} dt={dt}: {cls:12s} '
                 f'rsd={rsd:8.4f} tail=[{stats[4]:.3f},{stats[5]:.3f}] '
                 f'maxE={stats[0]:.3f} ({wall:.1f}s)')
    cols = ['tau', 'history', 'dt', 'n_steps', 'tau_grid_units',
            'classification', 'tail_N_min', 'tail_N_max', 'tail_N_mean',
            'tail_N_rsd', 'max_E', 'gate_floor_active', 'clip_N',
            'clip_E', 'wall_s']
    pc.write_csv(BASIN_CSV, rows, cols)
    halv = []
    if c2 is not None:
        for hc in ('H1', 'H2', 'H3'):
            a = next((r['classification'] for r in rows
                      if r['tau'] == c2 and r['history'] == hc
                      and r['dt'] == DT), None)
            b = next((r['classification'] for r in rows
                      if r['tau'] == c2 and r['history'] == hc
                      and r['dt'] == DT / 2), None)
            halv.append(dict(tau=c2, history=hc, dt02=a, dt01=b,
                             unchanged=bool(a == b) and a is not None))
            hstat = ('UNCHANGED' if (a == b and a is not None)
                     else 'CHANGED/MISSING')
            log.info(f'  dt-halving tau={c2} {hc}: {a} vs {b} ({hstat})')
    st['stageD'] = dict(rows=len(rows), grid_b_center=center,
                        grid_b_taus=grid_b, dt_halving=halv,
                        wall_s=round(time.time() - t_all, 1))
    save_status(st)
    log.info(f'stage D done: {len(rows)} basin runs '
             f'({time.time() - t_all:.0f}s)')


# ==========================================================================
# Stage R — results JSON
# ==========================================================================
def stageR(log, st):
    out = dict(
        title='Second-fold search on the upper branch (pre-registered '
              'protocol, SECOND_FOLD_PREREGISTRATION.md)',
        date=time.strftime('%Y-%m-%d'),
        git_head=git_head(),
        stages={k: v for k, v in st.items() if k != 'stageR'},
    )
    if BRANCH_CSV.exists():
        rows = list(csvmod.DictReader(open(BRANCH_CSV)))
        out['branch_summary'] = dict(
            n_records=len(rows),
            tau_min=min(float(r['tau']) for r in rows),
            tau_max=max(float(r['tau']) for r in rows),
            methods=sorted({r['method'] for r in rows}))
    if BASIN_CSV.exists():
        rows = list(csvmod.DictReader(open(BASIN_CSV)))
        out['basin_summary'] = dict(
            n_runs=len(rows),
            classifications=sorted({r['classification'] for r in rows}))
    if (HERE / 'second_fold_krawczyk.json').exists():
        out['stageC_status'] = json.loads(
            (HERE / 'second_fold_krawczyk.json').read_text()).get('status')
    RESULTS.write_text(json.dumps(out, indent=1, default=str))
    log.info(f'stage R done: {RESULTS.name} written')


STAGES = dict(stage0=stage0, stageA=stageA, stageB=stageB, stageD=stageD,
              stageR=stageR)


def main():
    argv = [a for a in sys.argv[1:]]
    which = argv[0] if argv else 'all'
    log = pc.Tee(LOG)
    st = load_status()
    order = ['stage0', 'stageA', 'stageB', 'stageD', 'stageR']
    log.info(f'=== second-fold search: {which} (HEAD {git_head()[:10]}) ===')
    if which == 'all':
        for name in order:
            STAGES[name](log, st)
    else:
        STAGES[which](log, st)
    log.info('=== done ===')


if __name__ == '__main__':
    main()

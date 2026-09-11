"""A11 sensitivity battery for the 42-stock cross-sectional screen (v31).

Baseline machinery replicates ram_crosssection.py + verify_bh.py exactly
(linear detrend, Lomb-Scargle nf=1500 grid, seed 7, 200 sims, empirical
p=(k+1)/201, BH-FDR over the 84 target-band cells at alpha=0.05).
Each variant changes ONE element; pass criterion throughout is verdict
stability of the BH-adjusted zero count.
Variants: base, arma, ts, bb5, bb10, bb15, hp, fd, reg_med, reg_low, reg_up.
"""
import numpy as np
from scipy.signal import lombscargle
from scipy.optimize import minimize
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve
from ram_crosssection import load, spectrum, band_power, BANDS

NSIM, SEED, ALPHA = 200, 7, 0.05

def ls_grid(years, nf=1500):
    return np.linspace(1/(2*(years[-1]-years[0])), 0.5, nf)

def periodogram(t, y, freq):
    P = lombscargle(t, y, 2*np.pi*freq)
    return P / P.sum()

def phi_hat(x):
    return float(np.corrcoef(x[:-1], x[1:])[0, 1]) if len(x) >= 4 else 0.0

def lin_detrend(t, y):
    b1, b0 = np.polyfit(t, y, 1)
    return y - (b0 + b1*t), (b0, b1)

def ar1_sim(n, phi, rng, burn=0):
    """Exact ram_crosssection/verify_bh recursion when burn=0 (x[0]=e[0],
    no burn-in); used for base/ts/regime so the baseline replicates bit-exactly.
    (ARMA(1,1) keeps its own 500-step burn-in: standard for ARMA simulation.)"""
    e = rng.standard_normal(n + burn)
    x = np.zeros(n + burn); x[0] = e[0]
    for i in range(1, n + burn):
        x[i] = phi*x[i-1] + e[i]
    return x[burn:]

def arma11_css(x, phi, theta):
    n = len(x); e = np.zeros(n)
    for i in range(1, n):
        e[i] = x[i] - phi*x[i-1] - theta*e[i-1]
    return e

def arma11_fit(x):
    """Gaussian CSS-MLE for ARMA(1,1); multi-start; stationary+invertible box."""
    n = len(x); ph0 = phi_hat(x)
    best = None
    for s0 in [(ph0, 0.0), (ph0, 0.3), (ph0, -0.3), (0.0, 0.0)]:
        def nll(v):
            ph, th = v
            e = arma11_css(x, ph, th)[1:]
            s2 = max(np.mean(e**2), 1e-12)
            return 0.5*(n-1)*np.log(s2)
        try:
            r = minimize(nll, s0, method='L-BFGS-B',
                         bounds=[(-0.999, 0.999), (-0.999, 0.999)],
                         options={'maxiter': 500})
        except Exception:
            continue
        if best is None or r.fun < best[0]:
            best = (r.fun, r.x)
    ph, th = best[1]
    e = arma11_css(x, ph, th)[1:]
    return float(ph), float(th), float(np.std(e))

def arma11_sim(n, phi, theta, sig, rng, burn=500):
    e = rng.standard_normal(n + burn)*sig
    x = np.zeros(n + burn)
    for i in range(1, n + burn):
        x[i] = phi*x[i-1] + e[i] + theta*e[i-1]
    return x[burn:]

def hp_cycle(y, lam=100.0):
    """HP-filter cycle component (annual-data lambda=100)."""
    n = len(y)
    d = np.ones(n-2)
    D = diags([d, -2*d, d], [0, 1, 2], shape=(n-2, n))
    F = (D.T @ D).tocsc()
    I = diags([np.ones(n)], [0], shape=(n, n)).tocsc()
    trend = spsolve(I + lam*F, y)
    return y - trend

def cbb(x, L, rng):
    """Circular block bootstrap draw, same length as x."""
    n = len(x); ext = np.concatenate([x, x])
    nb = int(np.ceil(n / L))
    starts = rng.integers(0, n, nb)
    return np.concatenate([ext[s:s+L] for s in starts])[:n]

def bh_reject(pvals, alpha=0.05):
    m = len(pvals); order = sorted(range(m), key=lambda i: pvals[i])
    maxrank = 0
    for rank, i in enumerate(order, start=1):
        if pvals[i] <= rank/m*alpha:
            maxrank = rank
    return set(order[:maxrank]), order

def run_variant(data, name, prep_data, sim_fn, fit_fn=None):
    """prep_data(years, ssb) -> (t, y, freq, aux); sim_fn(rng, n, aux) -> raw sim;
    fit_fn(t, sim) -> treated sim (same treatment as data side)."""
    rows = []
    for sid in sorted(data):
        yrs = data[sid]
        years = np.array([y for y, s in yrs]); ssb = np.array([s for y, s in yrs])
        if len(ssb) < 20:
            continue
        t, y, freq, aux = prep_data(years, ssb)
        P = periodogram(t, y, freq)
        rng = np.random.default_rng(SEED)
        sims = np.zeros((NSIM, 2))
        for s in range(NSIM):
            xs = sim_fn(rng, len(y), aux)
            xs = xs / np.std(xs)
            det = fit_fn(t, xs) if fit_fn else xs
            Ps = periodogram(t, det, freq)
            for bi, (_, lo, hi) in enumerate(BANDS[:2]):
                m = (freq > 1/hi) & (freq <= 1/lo)
                sims[s, bi] = Ps[m].sum()
        for bi, (bname, lo, hi) in enumerate(BANDS[:2]):
            bp = band_power(freq, P, lo, hi)
            p = float((np.sum(sims[:, bi] >= bp) + 1) / (NSIM + 1))
            rows.append((sid, bname, bp, p))
    pvals = [r[3] for r in rows]
    rej, order = bh_reject(pvals, ALPHA)
    print(f'=== {name}: tests={len(rows)} BH rejections={len(rej)} '
          f'[{"STABLE-ZERO" if not rej else "NONZERO !!"}]')
    for i in order[:5]:
        print(f'    {rows[i][0]:15s} {rows[i][1]:8s} bp={rows[i][2]:.3f} p={rows[i][3]:.4f}')
    for i in sorted(rej):
        print(f'    REJECT: {rows[i]}')
    return rows, rej

# ---- data-side preparations ----
def prep_base(years, ssb):
    t = years - years[0]
    det, _ = lin_detrend(t, ssb)
    return t, det, ls_grid(years), {'phi': phi_hat(det)}

def prep_ts(years, ssb):  # NO detrend; null carries the fitted trend
    t = years - years[0]
    det, (b0, b1) = lin_detrend(t, ssb)
    resid = det
    return t, ssb, ls_grid(years), {'phi': phi_hat(resid), 'b0': b0, 'b1': b1,
                                    'sig': float(np.std(resid))}

def prep_hp(years, ssb):
    t = years - years[0]
    cyc = hp_cycle(ssb)
    return t, cyc, ls_grid(years), {'phi': phi_hat(cyc)}

def prep_fd(years, ssb):
    d = np.diff(ssb); t = (years[1:] - years[1:])
    return t, d, ls_grid(years[1:]), {'phi': phi_hat(d)}

# ---- null simulators ----
def sim_ar1(rng, n, aux):
    return ar1_sim(n, aux['phi'], rng)

def sim_arma(rng, n, aux):
    return arma11_sim(n, aux['phi'], aux['theta'], aux['sig'], rng)

def sim_ts(rng, n, aux):  # trend (data-fitted, fixed) + AR(1) residuals
    t = np.arange(n)
    return aux['b0'] + aux['b1']*t + ar1_sim(n, aux['phi'], rng)*aux['sig']

def sim_reg(rng, n, aux):
    br = aux['br']
    x1 = ar1_sim(br, aux['phi1'], rng)*aux['sig1']
    x2 = ar1_sim(n-br, aux['phi2'], rng)*aux['sig2']
    return np.concatenate([x1, x2])

def fit_lin(t, x):
    d, _ = lin_detrend(t, x)
    return d

def fit_hp(t, x):
    return hp_cycle(x)

def fit_none(t, x):
    return x

if __name__ == '__main__':
    data = load()
    nstocks = sum(1 for s in data.values() if len(s) >= 20)
    print(f'stocks with n>=20: {nstocks}')
    phis = []
    for sid in sorted(data):
        yrs = data[sid]
        years = np.array([y for y, s in yrs]); ssb = np.array([s for y, s in yrs])
        if len(ssb) < 20:
            continue
        t = years - years[0]
        det, _ = lin_detrend(t, ssb)
        phis.append(phi_hat(det))
    print(f'median phi_hat={np.median(phis):.3f} range=[{min(phis):.3f},{max(phis):.3f}]')

    results = {}
    results['base'] = run_variant(data, 'base AR(1)+lindet', prep_base, sim_ar1, fit_lin)

    # ARMA(1,1): fit per stock once, stash in aux via prep wrapper
    arma_pars = {}
    for sid in sorted(data):
        yrs = data[sid]
        years = np.array([y for y, s in yrs]); ssb = np.array([s for y, s in yrs])
        if len(ssb) < 20:
            continue
        t = years - years[0]
        det, _ = lin_detrend(t, ssb)
        arma_pars[sid] = arma11_fit(det/np.std(det))
    ph_ = [v[0] for v in arma_pars.values()]; th_ = [v[1] for v in arma_pars.values()]
    print(f'ARMA(1,1) fits: phi med={np.median(ph_):.3f} range=[{min(ph_):.3f},{max(ph_):.3f}]; '
          f'theta med={np.median(th_):.3f} range=[{min(th_):.3f},{max(th_):.3f}]')
    def prep_arma(years, ssb):
        t, det, freq, aux = prep_base(years, ssb)
        sid = aux.pop('sid', None)
        return t, det, freq, aux
    # attach sid-keyed pars: rebuild prep with lookup by series identity
    sids = [sid for sid in sorted(data)
            if len(data[sid]) >= 20]
    it = {'i': -1}
    def prep_arma2(years, ssb):
        t = years - years[0]
        det, _ = lin_detrend(t, ssb)
        it['i'] += 1
        ph, th, sg = arma_pars[sids[it['i']]]
        return t, det, ls_grid(years), {'phi': ph, 'theta': th, 'sig': sg}
    it['i'] = -1
    results['arma'] = run_variant(data, 'arma ARMA(1,1)+lindet', prep_arma2, sim_arma, fit_lin)

    results['ts'] = run_variant(data, 'ts trend-stationary-no-detrend', prep_ts, sim_ts, fit_none)
    # block bootstrap needs the detrended series in aux: dedicated prep
    def prep_bb(years, ssb):
        t = years - years[0]
        det, _ = lin_detrend(t, ssb)
        return t, det, ls_grid(years), {'series': det}
    for L in (5, 10, 15):
        results[f'bb{L}'] = run_variant(
            data, f'bb{L} circular-block-bootstrap L={L}', prep_bb,
            lambda rng, n, aux, L=L: cbb(aux['series'], L, rng), fit_lin)
    results['hp'] = run_variant(data, 'hp HP-cycle AR(1)', prep_hp, sim_ar1, fit_hp)
    results['fd'] = run_variant(data, 'fd first-difference AR(1)', prep_fd, sim_ar1, fit_none)

    def prep_reg(br_frac):
        def f(years, ssb):
            t = years - years[0]
            det, _ = lin_detrend(t, ssb)
            br = max(4, min(len(det)-4, int(round(len(det)*br_frac))))
            s1, s2 = det[:br], det[br:]
            return t, det, ls_grid(years), {'br': br, 'phi1': phi_hat(s1),
                                            'sig1': float(np.std(s1)),
                                            'phi2': phi_hat(s2),
                                            'sig2': float(np.std(s2))}
        return f
    results['reg_med'] = run_variant(data, 'reg_med regime-median-break', prep_reg(0.5), sim_reg, fit_lin)
    results['reg_low'] = run_variant(data, 'reg_low regime-tercile1-break', prep_reg(1/3), sim_reg, fit_lin)
    results['reg_up'] = run_variant(data, 'reg_up regime-tercile2-break', prep_reg(2/3), sim_reg, fit_lin)

    print()
    print('VARIANT      BHrej  VERDICT')
    for k, (rows, rej) in results.items():
        print(f'{k:12s} {len(rej):>5d}  {"STABLE-ZERO" if not rej else "NONZERO !!"}')

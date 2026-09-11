"""
Cross-sectional RAM test (2026-08-08)
======================================
For each of the 58 RAM stocks (herring/sprat/anchovy), compute the SSB-series
CV and the normalized spectral power in bands:
    A: 2.5-5 yr   (anchovy-class predicted ~4-yr institutional period)
    B: 5-9 yr     (sprat-class predicted ~8-yr institutional period)
    C: 9-14 yr    (cohort/recruitment band)
    D: 14-30 yr   (low-frequency trend/regime band)
against a per-stock AR(1) red-noise null (200 sims, per-band 95%).

Model prediction under sampled governance (D10): at T_r=1 (annual TAC - the
documented regime for ~all these stocks), the institutional mechanism is
dormant -> expect NO robust excess power in bands A/B; any such peaks are
candidates for cohort/recruitment/ecosystem drivers (like the herring decadal
peaks found earlier), NOT the institutional mechanism.

T_r regime proxy (from general knowledge, honestly labeled - not per-stock
primary-verified): ICES/EU/GFCM annual TACs (T_r~1) for all ANCHMEDGSA*,
ANCHOBAYB, HERR*, SPRAT*; SA anchovy (ANCHOSA) annual-within-OMP (rule review
4-5 yr, but TAC annual); Peru/Chile (PANCH*, SSARDCH) annual quota + in-season;
Japan (JANCHO*) annual TAC; West Africa (ANCHOCWA*, ANCHONWA) annual TACs
(irregular enforcement).
"""
import numpy as np, csv
from scipy.signal import lombscargle

def load():
    rows = {}
    with open('ram_target_stocks.csv') as f:
        for d in csv.DictReader(f):
            sid = d['stockid']
            if d['SSB'] in ('', 'NA'):
                continue
            rows.setdefault(sid, []).append((int(d['tsyear']), float(d['SSB'])))
    return {k: sorted(v) for k, v in rows.items()}

def spectrum(years, ssb, nf=1500):
    t = years - years[0]
    b1, b0 = np.polyfit(t, ssb, 1)
    det = ssb - (b0 + b1 * t)
    freq = np.linspace(1/(2*(years[-1]-years[0])), 0.5, nf)
    P = lombscargle(t, det, 2*np.pi*freq)
    P = P / P.sum()
    return freq, P, phi_est(det)

def phi_est(det):
    if len(det) < 4:
        return 0.0
    return float(np.corrcoef(det[:-1], det[1:])[0, 1])

def band_power(freq, P, lo, hi):
    m = (freq > 1/hi) & (freq <= 1/lo)
    return float(P[m].sum()) if m.any() else 0.0

BANDS = [("A 2.5-5", 2.5, 5), ("B 5-9", 5, 9), ("C 9-14", 9, 14), ("D 14-30", 14, 30)]

def null_threshold(years, phi, nsim=200, seed=7):
    """Per-band 95% thresholds of normalized band power under AR(1) red noise."""
    t = years - years[0]
    n = len(years)
    rng = np.random.default_rng(seed)
    # frequencies matching the data window (same grid as spectrum)
    freq = np.linspace(1/(2*(years[-1]-years[0])), 0.5, 1500)
    sims = np.zeros((nsim, len(BANDS)))
    for s in range(nsim):
        e = rng.standard_normal(n)
        x = np.zeros(n); x[0] = e[0]
        for i in range(1, n):
            x[i] = phi * x[i-1] + e[i]
        x = x / np.std(x)
        b1, b0 = np.polyfit(t, x, 1)
        det = x - (b0 + b1 * t)
        P = lombscargle(t, det, 2*np.pi*freq)
        P = P / P.sum()
        for bi, (_, lo, hi) in enumerate(BANDS):
            m = (freq > 1/hi) & (freq <= 1/lo)
            sims[s, bi] = P[m].sum() if m.any() else 0.0
    return np.percentile(sims, 95, axis=0)

def regime(sid):
    if sid.startswith("ANCHOSA"):
        return "SA-OMP(annual TAC)"
    if sid.startswith("PANCH") or sid.startswith("SSARD"):
        return "Peru/Chile annual+in-season"
    if sid.startswith("JANCHO"):
        return "Japan annual TAC"
    if sid.startswith("ANCHOCWA") or sid.startswith("ANCHONWA"):
        return "W-Africa annual(irregular)"
    if sid.startswith("SPRBLK"):
        return "Black Sea annual"
    return "ICES/EU/GFCM annual TAC"

if __name__ == "__main__":
    data = load()
    print(f"{'stock':14s} {'n':>3s} {'CV':>5s} {'regime':28s} "
          + " ".join(f"{b:>9s}" for b, _, _ in BANDS))
    print("-" * 100)
    flagged = []
    for sid in sorted(data):
        yr_s = data[sid]
        years = np.array([y for y, s in yr_s]); ssb = np.array([s for y, s in yr_s])
        if len(ssb) < 20:
            continue
        freq, P, phi = spectrum(years, ssb)
        cv = ssb.std() / ssb.mean()
        thr = null_threshold(years, phi)
        bp = [band_power(freq, P, lo, hi) for _, lo, hi in BANDS]
        sig = [bp[i] > thr[i] for i in range(len(BANDS))]
        reg = regime(sid)
        print(f"{sid:14s} {len(ssb):3d} {cv:5.2f} {reg:28s} "
              + " ".join(f"{bp[i]:7.3f}{'*' if sig[i] else ' ':>2s}"
                         for i in range(len(BANDS))))
        if sig[0] or sig[1]:
            flagged.append((sid, bp[0], bp[1], thr[0], thr[1]))
    print("-" * 100)
    print(f"\nStocks with excess power in the predicted institutional bands "
          f"(A 2.5-5 yr and/or B 5-9 yr): {len(flagged)}")
    for sid, a, b, ta, tb in flagged:
        print(f"  {sid}: A={a:.3f} (95% {ta:.3f})  B={b:.3f} (95% {tb:.3f})")
    print("\nAll regimes are annual (T_r ~ 1). Model predicts NO institutional")
    print("oscillation at T_r=1; excess A/B power would be cohort/recruitment/")
    print("ecosystem driven, not the institutional mechanism.")

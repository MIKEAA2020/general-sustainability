#!/usr/bin/env python3
"""Gate 4 — springflow map-form pre-check (H1/H2) for the Barton Springs pool.

PRE-CHECK ONLY. Pre-specified in V3_SELECTION.md rev 2 §6 item 3 BEFORE any data
was pulled. It asks one question: is the E4 affine stock-flow map
    X_{t+1} = a*X_t + alpha + beta*R_t + gamma*P_t
a defensible form for Barton Springs springflow, i.e. do H1 (0<a<1) and H2
(gamma<0) hold?  NO SIGN TEST, NO MARGIN, NO KERNEL is computed here.
"""
import json, os, math, statistics as st

D = os.path.join(os.path.dirname(__file__), '..', 'data')
R = os.path.join(os.path.dirname(__file__), '..', 'results')

# ---- read daily mean discharge -----------------------------------------------
daily = {}
for line in open(os.path.join(D, 'bartonsprings_08155500_dv.rdb')):
    if not line.startswith('USGS'): continue
    f = line.rstrip('\n').split('\t')
    try: daily.setdefault(f[2][:4], []).append(float(f[3]))
    except (ValueError, IndexError): pass

MIN_DAYS = 240                     # same annual-completeness rule as J-17/J-27
ann = {int(y): st.mean(v) for y, v in daily.items() if len(v) >= MIN_DAYS}
years = sorted(ann)
out = {'coverage': {
    'daily_rows': sum(len(v) for v in daily.values()),
    'first_daily': min(min(daily), key=str), 'period_of_record_start': '1978-03-01',
    'annual_years_ge_240d': len(years), 'first_year': years[0], 'last_year': years[-1],
    'dropped_partial_years': sorted(set(map(int, daily)) - set(years))}}

# ---- H1: AR(1) core on annual springflow -------------------------------------
def ols(X, y):
    """least squares with intercept, no numpy dependency"""
    n, k = len(X), len(X[0])
    A = [[1.0] + list(r) for r in X]
    XtX = [[sum(A[i][p]*A[i][q] for i in range(n)) for q in range(k+1)] for p in range(k+1)]
    Xty = [sum(A[i][p]*y[i] for i in range(n)) for p in range(k+1)]
    m = [row[:] + [Xty[i]] for i, row in enumerate(XtX)]
    for c in range(k+1):
        p = max(range(c, k+1), key=lambda r: abs(m[r][c])); m[c], m[p] = m[p], m[c]
        for r in range(k+1):
            if r != c and m[c][c] != 0:
                f = m[r][c]/m[c][c]
                for j in range(c, k+2): m[r][j] -= f*m[c][j]
    return [m[i][k+1]/m[i][i] for i in range(k+1)]

xs = [[ann[y]] for y in years[:-1]]
ys = [ann[y+1] for y in years[:-1] if y+1 in ann]
xs = [[ann[y]] for y in years[:-1] if y+1 in ann]
b = ols(xs, ys)
a_hat = b[1]
resid = [ys[i] - (b[0] + a_hat*xs[i][0]) for i in range(len(ys))]
se_a = math.sqrt(sum(r*r for r in resid)/(len(ys)-2) /
                 sum((x[0]-st.mean([q[0] for q in xs]))**2 for x in xs))
out['H1_autoregression'] = {
    'a_hat': round(a_hat, 5), 'se': round(se_a, 5),
    'ci95': [round(a_hat-1.96*se_a, 5), round(a_hat+1.96*se_a, 5)],
    'n_transitions': len(ys), 'intercept': round(b[0], 4),
    'H1_holds_0_lt_a_lt_1': bool(0 < a_hat < 1),
    'H1_ci_strictly_inside_unit_interval': bool(a_hat-1.96*se_a > 0 and a_hat+1.96*se_a < 1)}

# ---- H2: requires a pumpage column -------------------------------------------
out['H2_gamma'] = {
    'checkable': False,
    'reason': ('H2 (gamma<0) is a fitted-sign assumption on a PUMPAGE regressor. No machine-retrievable '
               'annual BSEACD pumpage series exists in NWIS; District aggregate production is published only '
               'in annual reports/HCP tables as PDF. Without P_t the gamma sign cannot be estimated at all.'),
    'consequence': 'H2 is NOT verified for this pool. Per the pre-registered rule, unverified H2 = SCOPE EXCLUSION.'}

out['ruling'] = {
    'gate4': 'FAILS',
    'grounds': [
        'G1 RECORD LENGTH: daily discharge at 08155500 begins 1978-03-01 (site catalog dv|00060|00003). '
        f'That yields {len(years)} usable annual observations - NOT the long record the rev-2 mitigation assumed. '
        'The springflow specification does not escape the short-record problem it was introduced to solve.',
        'G2 H2 UNVERIFIABLE: no pumpage series => gamma cannot be signed => lemma hypotheses incomplete.',
        'G4 H1 IS DEGENERATE, NOT MERELY UNCERTAIN: a_hat = 0.178 with a 95% CI of [-0.109, 0.465] that '
        'CONTAINS ZERO. Annual springflow is close to white. H1 (0<a<1) is nominally satisfied by the point '
        'estimate, but a ~ 0 means the "attractor" H*_0 = (alpha+beta*F)/(1-a) collapses to roughly the '
        'unconditional mean and the contraction is essentially instantaneous. The margin then measures '
        'threshold-vs-mean, not threshold-vs-attractor - the dynamical content the lemma is about is absent. '
        'Contrast the head specifications, where a is far from 0 (J-17 head AC(1)=0.644, Uvalde 0.844).',
        'G3 The 1950s drought-of-record - the single most informative episode, and the basis for the 6.5 cfs DFC '
        'and the 5.2 cfs MAG - lies ENTIRELY OUTSIDE the gauge record. The v3 could not test the regime its own '
        'thresholds were derived from.'],
    'decision': 'Per V3_SELECTION.md rev 2 Verdict: gate 4 does not clear => WRITE NO v3.'}

json.dump(out, open(os.path.join(R, 'gate4_springflow_precheck.json'), 'w'), indent=2)
print(json.dumps(out, indent=2))

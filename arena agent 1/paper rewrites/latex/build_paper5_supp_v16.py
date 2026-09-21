"""Build paper5 supplementary v16 from v15: S12 calibration/cross-system/
precision records + S1/S8 updates for v40."""
import re

SRC = '/home/user/paper5_v39/paper5_supplementary_v15_NatSustain.md'
DST = '/home/user/paper5_v40/paper5_supplementary_v16_NatSustain.md'
s = open(SRC, encoding='utf-8').read()
n0 = len(s)

def rep(old, new, tag):
    global s
    c = s.count(old)
    assert c == 1, f'{tag}: count={c}\n---\n{old[:220]}'
    s = s.replace(old, new, 1)
    print(f'{tag}: OK')

# P1 intro: twelve bodies + S12 listing
rep('It carries eleven bodies of material:',
    'It carries twelve bodies of material:',
    'P1a-bodies')
rep('; and the sensitivity, F-grid, Neimark--Sacker, and alternative-band records (S11).',
    '; the sensitivity, F-grid, Neimark--Sacker, and alternative-band records (S11); and the F-calibration, ADH cross-system, and precision-certificate records (S12).',
    'P1b-s12list')

# P2 S1 rows
rep('the sensitivity battery, F-grid, and NS-verification records (S11).',
    'the sensitivity battery, F-grid, and NS-verification records (S11); the F-calibration and precision records (S12).',
    'P2a-s1-34')
rep('alternative-band screens at nominal tier (S11).',
    'alternative-band screens at nominal tier (S11); F-excess and ADH cross-system records at nominal tier (S12).',
    'P2b-s1-35')

# P3 S8 deposits
rep('`fig_nscircle_v39.png`). On the open docket:',
    '`fig_nscircle_v39.png`; the version-40 calibration records (`qcal_fplacement.py`, `qcal_fplacement.log`, `fplacement_table.csv`, `adh_verify.py`, `adh_verify.log`, `precision_cert.py`, `precision_cert.log`)). On the open docket:',
    'P3-deposits')

# P4 append S12
S12 = '''

---

## S12. F-calibration, ADH cross-system, and precision-certificate records (§3.4, §3.5)

### S12.1 F-calibration and placement (§3.4)

Catchability $q$ is not directly calibratable (model effort units are bare); the calibratable object is equilibrium fishing mortality $F^* = qE^*$ (yr$^{-1}$, the units of assessed $F$). `qcal_fplacement.py` places assessed-$F$ distributions against the §3.4 $F^*$ grid (S11.2: stable below $\\approx 0.002$, marginal at baseline $0.00209$, infeasible $F^* > r = 0.02$). Gates (all pass): the 42-stock screen cohort reproduces from the series ($n \\ge 20$ valid SSB points); the series-to-summary pipeline reproduces the deposited per-stock $F$ column (last-$F$, 42/43 — the sole exception uses median-$F$ against a terminal-year artifact); broader-pool $F$ quartiles reproduce the deposited record overall and in all 13 taxonomic groups.

| Pool | $n$ | Median $F$ | IQR | Scale vs baseline $F^*$ | Placement |
|---|---|---|---|---|---|
| Screen cohort (mean-$F$) | 38 | 0.37 | 0.27--0.72 | 175× | 37 beyond-feasible, 1 unstable-range |
| Broader pool ($F_{\\rm now}$) | 454 | 0.21 | 0.08--0.46 | 103× | 426 beyond, 20 unstable-range, 7 marginal, 1 below-stable |

Four cohort stocks carry no $F$ series (SA anchovy, three Japan anchovies) and are excluded from $F$ summaries. Vintage check (v444 vs v466, 396 paired stocks): median $|dF| = 0.017$, small against the placement scale. Total-catch cross-check (TC/SSB against $F$, $n = 1170$ stock-years): Spearman $\\rho = 0.82$, validating $F$ as the exploitation metric. Per-stock table: `fplacement_table.csv`; log: `qcal_fplacement.log`. Quantitative thresholds are therefore scale-conditional: the logistic core is a timing-qualitative model whose verdicts are functions of $F^*$, not point predictions at assessed scales.

### S12.2 Exploitation intensity vs spectral excess (§3.5)

Exploratory cross-system test of the dormancy prediction ($T_r = 1$ stocks should show no $F$-driven excess): per-stock mean $F$ against band null-excess (committed band powers over 95% per-stock thresholds). Full cohort ($n = 38$): band A Spearman $\\rho = 0.31$ ($p = 0.06$), band B $\\rho = 0.20$ ($p = 0.22$). With Peru/Chile (ENSO) stocks excluded ($n = 31$): band A $\\rho = 0.03$ ($p = 0.86$), band B $\\rho = 0.03$ ($p = 0.86$). The band-A hint is the documented ENSO confound (§3.7, S10); exploitation intensity carries no spectral excess beyond it. Computed in `qcal_fplacement.py`.

### S12.3 Buffer-years (ADH) cross-system verification (§3.5)

Buffer-years, ADH $= \\max(0, \\ln({\\rm SSB}/B_{\\rm lim})/F)$, is log stock-status over fishing mortality (reverse-engineered from the deposited tables; recomputation matches the deposited columns to $10^{-3}$). The prior broader-pool comparison is verified descriptively in full (overall, all taxonomic groups, zero fractions, vintage counterfactual: archived median 2.79 vs current-vintage 2.34 on the 33-stock overlap) and its random-draw core is independently re-executed with a new seed (20,000 draws of 43):

| Pool | Draw-median mean (mine/record) | % draws below archived median (mine/record) |
|---|---|---|
| Broad 454 | 3.35/3.35 | 2.33/2.12 |
| Forage 64 | 2.79/2.79 | 0.39/0.29 |

The archived-43 median (1.79) sits at the second percentile of broader-pool resampled medians: the screened cohort is buffer-poor relative to the RAM pool. Log: `adh_verify.log`.

### S12.4 Fifty-digit precision certificate (§3.4)

`precision_cert.py` recomputes the headline monodromy numbers in mpmath at 50 digits (scaling-and-squaring Taylor exponential, self-checked; characteristic-polynomial eigenvalues). The pipeline at 15 digits reproduces the scipy double-precision values to $4\\times 10^{-16}$ before the 50-digit run certifies: $\\rho_{\\rm exact}(1) = 1.00035065652277301318926820946$, $T_{rc} = 6.50129494807546836889974861684$, $\\theta_0 = 0.1754936732583932410001814$ ($|\\mu|-1 = 4\\times 10^{-23}$). The double-precision records are correct to 12+ digits. Log: `precision_cert.log`.

Deposited with this section: `qcal_fplacement.py`, `qcal_fplacement.log`, `fplacement_table.csv`, `adh_verify.py`, `adh_verify.log`, `precision_cert.py`, `precision_cert.log`.

**Status: executed computations; nominal tier (validation gates throughout; ADH random draws independently re-executed; S8).**
'''
s = s.rstrip('\n') + '\n' + S12.lstrip('\n')
print('P4-S12: appended')

print('len delta:', len(s) - n0)
import os
os.makedirs('/home/user/paper5_v40', exist_ok=True)
open(DST, 'w', encoding='utf-8').write(s)
print('WROTE', DST)

"""Build paper5 supplementary v15 from v14: S11 research records + S4 cod-row
correction + S1/S8 updates for v39."""
import re

SRC = '/home/user/paper5_v38/paper5_supplementary_v14.md'
DST = '/home/user/paper5_v39/paper5_supplementary_v15.md'
s = open(SRC, encoding='utf-8').read()
n0 = len(s)

def rep(old, new, tag):
    global s
    c = s.count(old)
    assert c == 1, f'{tag}: count={c}\n---\n{old[:220]}'
    s = s.replace(old, new, 1)
    print(f'{tag}: OK')

# P1 intro: ten -> eleven bodies + S11 listing
rep('It carries ten bodies of material:',
    'It carries eleven bodies of material:',
    'P1a-bodies')
rep('and the T_r-ranked test record (S10).',
    'and the T_r-ranked test record (S10); and the sensitivity, F-grid, Neimark--Sacker, and alternative-band records (S11).',
    'P1b-s11list')

# P2 S1 rows
rep('comparison with the legacy windows is a consistency check, not a validation).',
    'comparison with the legacy windows is a consistency check, not a validation); the sensitivity battery, F-grid, and NS-verification records (S11).',
    'P2a-s1-34')
rep('sensitivity battery and endpoint extension at nominal tier (S9.1).',
    'sensitivity battery and endpoint extension at nominal tier (S9.1); alternative-band screens at nominal tier (S11).',
    'P2b-s1-35')

# P3 S4 cod row correction (span replace to the haddock row)
i0 = s.find('- **Icelandic cod** (1995 harvest-control rule:')
i1 = s.find('(audit code, log, and series deposited).')
assert 0 < i0 < i1, f'P3 anchors: {i0} {i1}'
tail = '(audit code, log, and series deposited).'
assert '- **Icelandic haddock**' in s[i1:i1+400], 'P3: haddock row must follow'
NEW_COD = ('- **Icelandic cod** (1995 harvest-control rule: annual total allowable catch at 25% of fishable biomass, '
 'subject to a minimum catch provision): post-1995 spawning-stock-biomass coefficient of variation 0.387 on the archived '
 '1955\u20132023 ICES series and 0.394 on the 2026-09-11 current-vintage pull for the same window (audit code, log, and series '
 'deposited), and 0.369 on 1995\u20132026 recomputed this version \u2014 no detrending (level CV), ICES standardgraphs series. '
 'A detrended Lomb-Scargle periodogram of the post-1995 series shows no dominant peak in 5\u201330 yr (maximum at 22.9 yr, '
 '0.3% of spectral power); the post-1995 variability therefore carries no identified period, and no comparison with the '
 'four-state slow-stock prediction (slow-stock cohort cycle $P \\approx 250$\u2013360 yr in the archived record) is available '
 'on spectral grounds. The estimated implementation lag is approximately 0.2\u20130.3 yr (a lag that is not a review interval '
 'and is not inserted into the sampled model as $T_r$). Cohort resonance remains an alternative mechanism.')
s = s[:i0] + NEW_COD + s[i1+len(tail):]
print('P3-codrow: OK (span)')

# P4 S8 deposits
rep('and the conceptual-figure script (`fig_concept_v38.py`). On the open docket:',
    'and the conceptual-figure script (`fig_concept_v38.py`); the version-39 verification records (`sens_battery.py`, `sens_battery.log`, `sens_table.csv`, `fgrid_table.csv`, `rho_scan_v39.csv`, `ns_verify.py`, `ns_verify.log`, `bands_sensitivity.py`, `bands_sensitivity.log`, `bands_table.csv`, `fig_rho_scan_v39.png`, `fig_screen_v39.png`, `fig_cod_v39.png`, `fig_nscircle_v39.png`). On the open docket:',
    'P4-deposits')

# P5 residual 10-15 fluctuation claims (report count)
for old1015 in ('10\u201315 yr fluctuation', '10--15 yr fluctuation', '10-15 yr fluctuation'):
    c = s.count(old1015)
    s = s.replace(old1015, 'post-1995 variability (coefficient of variation 0.37\u20130.39) with no dominant spectral peak (S11)')
    print(f'P5-1015 {old1015!r}: replaced {c}')
print('P5-1525 residual count:', s.count('15\u201325') + s.count('15--25'))

# P6 append S11
S11 = '''

---

## S11. Sensitivity, F-grid, Neimark--Sacker, and alternative-band records (§3.4, §3.5, §3.8)

The monodromy core below is mathematically identical to the validated exact-hold implementation (equilibrium quadratic, Jacobian blocks, mobilising/protective gains, $M = R\\,\\exp(A_{\\rm hold} T_r)$). Every script reproduces its committed inputs before extension; gates are reported, not assumed.

### S11.1 One-at-a-time sensitivity battery (§3.4)

`sens_battery.py` perturbs each baseline parameter by $\\pm 5\\%$ and $\\pm 10\\%$. Validation gate (all pass): $\\rho(1) = 1.000351/1.000545/0.983796$ (exact mobilising, Euler mobilising, Euler protective), protective-exact maximum $0.996740$, crossings $6.5013/47.5360/79.1427/2.3064$ yr. Baseline records: crossing angle $\\theta_0 = 0.175494$ rad; continuous (undelayed) eigenvalues $\\lambda = -0.278147$, $+0.000360 \\pm 0.027683i$ (Table 3); the $6.5013$ yr crossing is identical across 2k/20k/200k coarse scans; the $C_E \\to 0$ update limit holds to machine precision.

| Parameter | $\\rho_{\\rm exact}(1)$ range | Exact-map first crossing (yr) | Protective max $\\rho$ |
|---|---|---|---|
| $r$ | 0.999871--1.000766 | 3.749--10.184 ($\\times 1.1$: none) | 0.9964--0.9971 |
| $K$ | 0.997461--1.003135 | 14.283--19.098 ($\\times 0.9/0.95$: none) | 0.9967--0.9968 |
| $q$ | 0.997687--1.002864 | 13.797--18.377 ($\\times 0.9/0.95$: none) | 0.9967--0.9968 |
| $E_{\\max}$ | 0.997690--1.002859 | 13.790--18.367 ($\\times 0.9/0.95$: none) | 0.9967--0.9968 |
| $\\eta$ | 0.999702--1.000962 | 2.194--10.314 ($\\times 0.9$: none) | 0.9967 |
| $\\delta_0$ | 1.000347--1.000355 | 6.468--6.535 | 0.9967 |
| $Z_{\\rm ref}$ | 1.000348--1.000354 | 6.479--6.527 | 0.9967--0.9968 |
| $\\Delta_{\\rm ref}$ | 0.997533--1.003935 | 15.173--20.857 ($\\times 1.05/1.1$: none) | 0.9967--0.9968 |
| $\\tau_m$ | 1.000251--1.000451 | 5.855--6.901 | 0.9967 |
| $\\delta$ | 0.999974--1.000641 | 4.688--8.544 ($\\times 0.9$: none) | 0.9967--0.9968 |

"None" means no unit-circle crossing on $[0.2, 120]$ yr. The protective channel is stable in every cell. Full 41-row table: `sens_table.csv`; log: `sens_battery.log`.

### S11.2 Equilibrium-fishing-mortality grid (§3.4)

The effort equilibrium $E^*$ solves a quadratic whose coefficients involve only $(\\eta, E_{\\max}, \\delta, \\Delta_{\\rm ref}, \\delta_0, Z_{\\rm ref})$; $N^* = K(1-qE^*/r)$ carries $(r, K, q)$. A $q$ log-grid at the remaining baseline vector ($F^* = qE^*$):

| $q$ | $E^*$ | $F^*$ | $\\rho_{\\rm exact}(1)$ | First crossing (yr) |
|---|---|---|---|---|
| 0.0001 | 2.0896 | 0.000209 | 0.968278 | none |
| 0.0001778 | 2.0896 | 0.000372 | 0.971425 | none |
| 0.0003162 | 2.0896 | 0.000661 | 0.977869 | none |
| 0.0005623 | 2.0896 | 0.001175 | 0.987320 | none |
| 0.001 | 2.0896 | 0.002090 | 1.000351 | 6.5013 |
| 0.001778 | 2.0896 | 0.003716 | 1.016819 | 51.1050 |
| 0.003162 | 2.0896 | 0.006608 | 1.060969 | 91.2183 |
| 0.005623 | 2.0896 | 0.011751 | 1.078545 | none on $[0.2,120]$ (unstable throughout) |
| $\\geq 0.01$ | 2.0896 | $\\geq 0.0209$ | — | infeasible ($N^*<0$; analytic boundary $F^* = r$) |

$q$ and $E_{\\max}$ act on the crossing almost entirely through $F^*$ ($\\times 1.05$: 13.797 vs 13.790 yr; $\\times 1.10$: 18.377 vs 18.367 yr at matched $F^*$). $\\Delta_{\\rm ref}$ and $\\delta$ shift the gains directly and do not collapse onto $F^*$ ($\\Delta_{\\rm ref}\\times 0.95$: $F^* = 0.00220$, crossing 15.173 yr, against 13.797 yr at $F^* = 0.00219$ via $q$). Full table: `fgrid_table.csv`. Figure 3 data: `rho_scan_v39.csv`.

### S11.3 Neimark--Sacker verification (§3.4)

`ns_verify.py` implements the nonlinear sampled (flow-then-update) map with effort held over each review interval. Gates (all pass): finite-difference Jacobian against the monodromy, $6.2\\times 10^{-9}$ at $T_r = 1$ and $1.2\\times 10^{-6}$ (best step; rounding floor identified by step study) at $T_r = 6.5013$, both updates; fixed-point residual $0$; nonlinear-map crossing $6.4976$ yr against the monodromy record $6.5013$ yr. At the crossing: $\\mu = 0.98464044+0.17459438i$, $\\theta_0 = 0.17549380$ rad; transversality $d|\\mu|/dT_r = -0.000683$; non-resonance $|e^{ik\\theta_0}-1| = 0.175/0.349/0.520/0.688$ for $k = 1/2/3/4$. First Lyapunov coefficient (Kuznetsov normal form; central finite-difference Hessian and third derivatives):

| FD step | $a(0)$ | Verdict |
|---|---|---|
| 2e-3 | -0.000815 | supercritical |
| 1e-3 | -0.000813 | supercritical |
| 5e-4 | -0.000798 | supercritical |
| 3e-4 | -0.000732 | supercritical |

Long-horizon iterates ($4000$ map steps) on both sides rotate at the predicted frequency (rotation numbers $0.0271$--$0.0287$ against $\\theta_0/2\\pi = 0.02793$); the invariant circle is not directly exhibited because convergence at $|\\rho-1| \\sim 10^{-4}$ is too slow for the tested horizons. Diagnostic figure deposited (`fig_nscircle_v39.png`); log: `ns_verify.log`.

### S11.4 Alternative-band screens (§3.5)

`bands_sensitivity.py` reuses the committed per-stock machinery (`load`, `spectrum`, `band_power`) and a $p$-value engine verified to reproduce `null_threshold()` cutoffs bit-exactly (identical RNG stream); it reproduces `tr_table.csv` band powers before extension. Exploratory Benjamini--Hochberg screens (resolution rule: record span at least three upper periods):

| Configuration | Cells | Resolvable | BH-significant | Min $q$ |
|---|---|---|---|---|
| Baseline A/B (2.5--5, 5--9) | 84 | 82 | 0 | 1.0000 |
| Broad (2--10) | 42 | 35 | 0 | 0.9900 |
| Cadence (1--3, 3--8, 8--20) | 126 | 88 | 0 | 0.8358 |
| Effort-proxy (8--80) | 42 | 0 | 0 | 0.2090 |

The effort-proxy band is unresolvable on all 42 records (longest span 77 yr against a 240 yr requirement). Full table: `bands_table.csv`; log: `bands_sensitivity.log`.

### S11.5 Cod post-1995 periodogram (§3.8)

Post-1995 SSB coefficient of variation: 0.387 (archived 1955--2023 ICES series), 0.394 (2026-09-11 current-vintage pull, same window), 0.369 (1995--2026, recomputed this version); no detrending (level CV); ICES standardgraphs series. Detrended (linear) Lomb-Scargle periodogram ($n_f = 3000$, $1/(2\\cdot{\\rm span})$--0.5 yr$^{-1}$) shows no dominant peak in 5--30 yr (maximum at 22.9 yr, 0.3% of spectral power). Computed in `bands_sensitivity.py`; Figure 5 plots the Table-2 series by window.

Deposited with this section: `sens_battery.py`, `sens_battery.log`, `sens_table.csv`, `fgrid_table.csv`, `rho_scan_v39.csv`, `ns_verify.py`, `ns_verify.log`, `bands_sensitivity.py`, `bands_sensitivity.log`, `bands_table.csv`, `fig_rho_scan_v39.png`, `fig_screen_v39.png`, `fig_cod_v39.png`, `fig_nscircle_v39.png`.

**Status: executed computations; nominal tier (single-execution records with validation gates; S8).**
'''
s = s.rstrip('\n') + '\n' + S11.lstrip('\n')
print('P6-S11: appended')

print('len delta:', len(s) - n0)
import os
os.makedirs('/home/user/paper5_v39', exist_ok=True)
open(DST, 'w', encoding='utf-8').write(s)
print('WROTE', DST)

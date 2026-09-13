#!/usr/bin/env python3
"""Phase A implementation (2026-09-13) — framework v13 -> v14.

Every replacement below was adjudicated in REMAINING_POINTS_TWO_AUDITS_v13.md (register)
and JOINT_EVALUATION_TWO_AUDITS_v13.md §5. Each (old, new) pair is asserted to match
exactly the expected number of times before replacing, so no edit can silently drift.
"""
import sys

SRC = 'framework/paperF1_retention_framework_v13.md'
DST = 'framework/paperF1_retention_framework_v14.md'

s = open(SRC, encoding='utf-8').read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, f'expected {n} match(es), got {c} for: {old[:80]!r}'
    s = s.replace(old, new)

# ---- AD1 / N2: K-bound wording (E1 v20 A6 convention; data-verified) ----
rep('lower bound 50.8 kt general, ≈91 kt on recovery window (max_train S≈81 kt)',
    'per-origin lower bound max_train S + 10 kt, the maximum taken over predictor states of the training transitions excluding the terminal state: ≈950.8 kt at the earliest origins (training maximum 940.8 kt, 1987) and 50.8 kt on the recovery-window training set (predictor-state maximum 40.8 kt, 2006)')

# ---- qwen 2.4: 0.0359 ----
rep('M1b h=1 114.8024 vs 114.7665 0.0358 kt',
    'M1b h=1 114.8024 vs 114.7665 0.0359 kt')

# ---- claude 2.2: ladder is a tree ----
rep('Each module has **declared comparator**, next-simpler member; first structural has none, retention turns on baseline alone.',
    'Each module has **declared comparator**, next-simpler member; first structural has none, retention turns on baseline alone. The ladder is a rooted tree, not a chain: the comparator is the next-simpler member on the module\u2019s own branch, and M1b is a branch (alternative production function) rather than a rung.')

# ---- claude 2.3: model inventory table (insert after the totals sentence) ----
rep('A scored five-module ladder runs against two naive baselines.',
    'A scored five-module ladder runs against two naive baselines.\n\n**Model inventory.** Only ladder rungs are eligible for retention; auxiliary modules and declared diagnostics are scored and reported, never retained.\n\n| Object | Rungs (declared comparator) | Auxiliary modules | Declared diagnostics | Naive baselines |\n|---|---|---|---|---|\n| COD Spec A/B | M1 (none), M1b (M1), M2 (M1), M3 (M2), M4 (M3) | capelin-index module (scored against its own origin-matched persistence) | \u2014 (M2\u2013M4 already receive future catch; conditional hindcasts) | naive_persist, naive_train_mean |\n| EDWARDS | M1 (none), M2 (M1), M2m (M1), M3 (M2), M4 (M3) | climate rung: M2_Rprecip, M2_Rar, M2_Renso, M2_combo (comparator M2m, declined \u2014 protocol kink acknowledged) | M2_oracle (realised fluxes, declared unable to retain) | naive_persist, naive_mean |')

# ---- claude 5: fragment ----
rep('Fail any \u2192 not retained. Retention per specification.',
    'Fail any \u2192 not retained. Retention is decided per specification.')

# ---- qwen 4.10: gloss ----
rep('Alternative comparator M2 versus M1b printed on primary passes:',
    'Alternative comparator M2 versus M1b, reported as a sensitivity row on the primary passes:')

# ---- qwen 4.11: moratorium ----
rep('distinct from Brier secondary diagnostic, moratorium deliberately not evaluated.',
    'distinct from Brier secondary diagnostic; the 1992\u20131993 fishing moratorium is deliberately not evaluated.')

# ---- claude 2.1: algorithm box reorder (class check pre-gate, first) ----
rep('\n for each M:\n  retained <- TRUE\n  for h in H:\n   if S(M,h) >= (1-b)*S(B,h): retained <- FALSE # H2, strictly >5% required\n   if comp(M) exists and S(M,h) >= (1-b)*S(comp(M),h): retained <- FALSE # H1\n  if retained:\n   if M reduces to simpler member under conditions of application:\n    output declined on class grounds\n   else:\n    output retained\n  else:\n   output not retained',
    '\n for each M:\n  if M reduces to simpler member under conditions of application:\n   output declined on class grounds # pre-gate, evaluated before scoring\n  retained <- TRUE\n  for h in H:\n   if S(M,h) >= (1-b)*S(B,h): retained <- FALSE # H2, strictly >5% required\n   if comp(M) exists and S(M,h) >= (1-b)*S(comp(M),h): retained <- FALSE # H1\n  if retained: output retained\n  else: output not retained')

# ---- claude 2.1: prose matched to the reordered box ----
rep('In algorithm box it is shown inside retained branch for compactness; operationally it is evaluated first, and retained set empty under rule alone (M2m fails H1 at h=1 under unified rule) so empty set holds either way; without band M2m would pass H1 but still be declined on class grounds.',
    'The algorithm box shows the class-grounds check first, matching the operational order: the class judgement is declared in the same frozen specification as the ladder, before any score is computed, so the decline of the only persistence-beating module is not post-hoc. The retained set is empty under the rule alone (M2m fails H1 at h=1 under the unified rule) so the empty set holds either way; without the band M2m would pass H1 but still be declined on class grounds.')

# ---- D1: Table 4 M2m h=5 uncertainty (computed with archived machinery) ----
rep('| 5 | M2m | 17.4449 | 21.1056 | -17.34% | \u2014 |',
    '| 5 | M2m | 17.4449 | 21.1056 | -17.34% | margin \u22123.66 ft, CI [\u22125.76, \u22122.19] excludes zero |')

# ---- D1: Table 4 M2m h=1 interval ----
rep('| 1 | M2m | 12.2832 | 13.2301 | -7.16% | only margin separated from noise |',
    '| 1 | M2m | 12.2832 | 13.2301 | -7.16% | only margin separated from noise (CI [\u22121.445, \u22120.676]) |')

# ---- D2: MAE tie values (4 occurrences) ----
assert '10.72' not in s
rep('MAE tie', 'MAE tie (10.72 vs 10.73 ft)', n=4)

# ---- Table 5-2: comparator band 12.1971 ----
rep('| M2m | 1 | 12.2832 | 13.2301 | 12.5686 | pass | M1 | 12.8391 | FAIL (4.33%) |',
    '| M2m | 1 | 12.2832 | 13.2301 | 12.5686 | pass | M1 | 12.8391 | FAIL (4.33%; comparator band 12.1971) |')

# ---- qwen 3.6: alternative-comparator counterfactual + qwen 3.7: h>1 justification ----
rep('all lose to climatological fluxes. San Antonio + Uvalde pools lumped',
    'all lose to climatological fluxes. Under an M1 comparator the verdict is unchanged: the two modules that edge past M1 at h=1 still fail the persistence gate at h=5, where all three climate modules score 3\u20136 ft worse than persistence. San Antonio + Uvalde pools lumped')
rep('h>1 climate scores reuse one-step forecast held constant.',
    'h>1 climate scores reuse the one-step forecast held constant \u2014 no h-year-ahead recharge or pumpage forecast is available at the origin, and the one-step forecast is the only origin-available flux estimate.')
rep('h>1 climate scores reuse one-step forecast held constant\n',
    'h>1 climate scores reuse the one-step forecast held constant \u2014 no h-year-ahead recharge or pumpage forecast is available at the origin, and the one-step forecast is the only origin-available flux estimate\n')

# ---- qwen 4.24: 17.64 gloss ----
rep('iterated affine analogue M2m 17.44/17.64 sits with mean',
    'iterated affine analogue M2m 17.44 ft (rolling h=5) and 17.64 ft (fixed-window h=5, n=12), each near the corresponding training mean', n=3)

# ---- qwen 4.18 / claude 1.12: delete typesetting instruction ----
rep('(bold 193 marks winner) \u2014 and', '\u2014 and')
rep('loses every cell, bold 193 marks winner', 'loses every cell')

# ---- qwen 3.9: origin-set sensitivity sentence ----
rep('module RMSE 150.02/262.34 Spec A and 132.02/491.74 Spec B loses to origin-matched baseline every cell.',
    'module RMSE 150.02/262.34 Spec A and 132.02/491.74 Spec B loses to origin-matched baseline every cell; the baseline shift from the main-ladder origins (264.72 kt) to the module\u2019s own (193 kt) at h=5 is large, and the verdict is checked on both origin sets \u2014 it is not an artefact of origin-set choice.')

# ---- claude 2.4: D3 row category error ----
rep('| D3 stock-flow | M2 | 0.090 | 0.110 | < chance (20%), below bar |',
    '| D3 stock-flow | M2 | 0.090 | 0.110 | 18\u201322\u00d7 the null false-retention rate (0.005 per module), below bar |')

# ---- claude 2.5: per-cell adequacy statement ----
rep('Mean power 0.376 is unweighted mean of eight D1\u2013D4 cells including three near-failures, drastically below pre-registered adequacy bar 80%;',
    'Mean power 0.376 is unweighted mean of eight D1\u2013D4 cells including three near-failures, drastically below pre-registered adequacy bar 80% (per cell: 2 of 8 clear the bar, D1 only); specificity clears 90% in both in-class null cells (D5) and in 0 of 4 misspecified cells (D6/D7);')

# ---- claude 2.6 (AD2): mechanism-misattribution sentence + claude 4.1 (LR table) ----
rep('Rows D1\u2013D4 proportion retaining generating module; D5 proportion retaining nothing; D6\u2013D7 proportion retaining any structural module when no ladder member generated data.',
    'Rows D1\u2013D4 proportion retaining generating module; D5 proportion retaining nothing; D6\u2013D7 proportion retaining any structural module when no ladder member generated data. Retention licenses a prediction claim, never a mechanism claim; the D6/D7 rows measure the gap between the two, and the realised predictive gain of the retained module in those replicates is registered for reporting.\n\n**Evidential weight (likelihood ratios; null false-retention rate 0.005 per module).** Retention LR+ = power/0.005; non-retention LR\u2212 = (1\u2212power)/(1\u22120.005):\n\n| DGP | LR+ (retention) | LR\u2212 (non-retention, evidence against) |\n|---|---|---|\n| D1 low/high \u03c3 | 193 / 197 | 28:1 / 66:1 |\n| D2 low/high \u03c3 | 142 / 26 | 3.4:1 / 1.1:1 |\n| D3 low/high \u03c3 | 18 / 22 | 1.09:1 / 1.12:1 |\n| D4 low/high \u03c3 | 1.0 / 3 | 1.00:1 / 1.01:1 |\n\nAt D4 low \u03c3 the depensation rung is a null instrument: P(retain M1b | depensation true) = 0.005 = P(retain M1b | null), so retention and non-retention both carry likelihood ratio exactly 1.')

# ---- claude 3.2 (AD3): tolerance sentence + qwen 3.10 (AD7): baseline sentence ----
rep('Training mean 16.8048 versus 21.1056 ft interval excluding zero at h=5. Fixed-window M2 RMSEs are 18.11 and 55.32 ft.',
    'Training mean 16.8048 versus 21.1056 ft interval excluding zero at h=5. The load-bearing gate decision (M2m versus M1, 4.33% against the 5% band) sits within numerical tolerance of the environment sensitivity measured on cod (\u00b117 kt on 445.5 kt, 3.8%); an Edwards cross-environment figure is registered as required. Persistence remains the decision baseline because it is the pre-registered H2/H3 anchor; the training mean\u2019s superiority at h=5 is reported as evidence about the baseline choice, not as a re-baselining. Fixed-window M2 RMSEs are 18.11 and 55.32 ft.')

# ---- qwen 3.8 / claude 5: fixed-window sentence (2 forms) ----
rep('Fixed-window pre-permit train 1980\u20131990 11 yr vs rolling floor 15-year floor is rolling rule fixed windows use declared trains.',
    'The fixed-window pre-permit pass uses its declared train 1980\u20131990 (11 yr); the 15-year floor applies to rolling origins only \u2014 fixed windows use their declared training sets.')
rep('Fixed-window pre-permit train 1980-1990 11 yr vs rolling floor 15-year floor is rolling rule fixed windows use declared trains',
    'Fixed-window pre-permit pass uses its declared train 1980\u20131990 (11 yr); the 15-year floor applies to rolling origins only \u2014 fixed windows use their declared training sets')

# ---- claude 3.5: why the coarse regime is primary (spec-confirmed) ----
rep('regime 240/120/5 kt three-level step (annual landings 172\u2013269 kt) \u2014 C\u0304 training-mean catch plugged 5.00 kt coarse / 3.19 kt annual, C_t prescribed regime for M2',
    'regime 240/120/5 kt three-level step, the frozen primary catch treatment (annual landings 172\u2013269 kt reported as the second treatment) \u2014 C\u0304 training-mean catch plugged 5.00 kt coarse / 3.19 kt annual, C_t prescribed regime for M2')

# ---- claude 3.1: third audit status + revised-status row ----
rep('Audit table one row per quantity, classifying as **available** \u2014 dated at or before origin \u2014 or **supplied** \u2014 dated after origin and provided regardless.',
    'Audit table one row per quantity, classifying as **available** \u2014 dated at or before origin \u2014 **supplied** \u2014 dated after origin and provided regardless \u2014 or **revised** \u2014 dated before the origin but existing only in a vintage published after it (the cod spawning-stock biomass predictand is an assessment output conditioned on the full series).')
rep('| Covariate, u\u2264t | available; last observation carried forward | covariate modules |',
    '| Covariate, u\u2264t | available; last observation carried forward | covariate modules |\n| Predictand dated before origin, published only in a later vintage | **revised** | assessment outputs (cod SSB) |')

# ---- claude 3.1 + claude 5: Two-systems sentence + smoothing candidate mechanism ----
rep('Two systems share nothing physically: one reconstructed population state governed by recruitment, mortality, harvest, other measured water level governed by recharge and pumping, karst conduits, Uvalde\u2013San Antonio divide, unconfined recharge-zone storage, confined-zone pressure response remain in residual, lumped versus EPM question inherited not resolved (Scanlon et al. 2003). They share a rule, and return same verdict.',
    'Two systems share a scalar stock driven by fluxes \u2014 precisely why one ladder applies to both \u2014 but little else physically: one is a reconstructed population state governed by recruitment, mortality, harvest; the other a measured water level governed by recharge and pumping; karst conduits, the Uvalde\u2013San Antonio divide, unconfined recharge-zone storage and confined-zone pressure response remain in residual, and the lumped-versus-EPM question is inherited, not resolved (Scanlon et al. 2003). They share a rule, and return the same verdict.\n\nOne candidate mechanism for the domain contrast is the predictand itself: the cod target is an assessment output conditioned on the full series, while Edwards head is directly measured; autocorrelation injected by that construction favours persistence, and the observed pattern \u2014 persistence unbeatable on the reconstructed target, three module-horizon cells beating persistence on the measured one \u2014 is consistent with the artefact, though not proof of it. The decisive test (rescoring D1 replicates under an assessment-like smoother) is registered, not yet run.')
rep('They do not return it for same reason, and that difference is what pair demonstrates.',
    'They do not return it for the same reason, and that difference is what the pair demonstrates.')

# ---- N5: archive paths ----
rep('- `wave_e_cod/results/e1_dm_uncertainty.csv` (archived from batch 7 campaign)',
    '- `batch 7 (audits of agent arena 1 paper rewrites)/results/e1_dm_uncertainty.csv` (archived from the batch 7 campaign)')
rep('- `wave_e_edwards/results/e3_dm_uncertainty.csv` (10 rows)',
    '- `batch 7 (audits of agent arena 1 paper rewrites)/results/e3_dm_uncertainty.csv` (10 rows)')

# ---- D1 archive: addendum JSON reference ----
rep('- `wave_e_edwards/results/e3_audit_uncertainty.json` (uncertainty layer, DM HAC + block bootstrap per K\u00fcnsch 1989, p percentile-tail fraction p_perc)',
    '- `wave_e_edwards/results/e3_audit_uncertainty.json` (uncertainty layer, DM HAC + block bootstrap per K\u00fcnsch 1989, p percentile-tail fraction p_perc) and `e3_audit_uncertainty_add_M2m_h5.json` (the M2m-versus-persistence h=5 test, computed with the same seeded machinery from the archived per-origin files)')

# ---- AD8: frozen-sheet cell-count divergence ----
rep('4 cells 800 passes (4000 rows: 2 DGPs \u00d72\u03c3\u00d7200\u00d75 modules))',
    '4 cells 800 passes (4000 rows: 2 DGPs \u00d72\u03c3\u00d7200\u00d75 modules); the frozen sheet\u2019s Amendment-1 wording of eight cells is corrected here against the archived row count)')

# ---- N4: DM-row universe stated ----
rep('5 of 32 rows (e.g., Spec A M4 versus M3 h=1',
    '5 of 32 rows in the full 32-row universe \u2014 including the four alternative-comparator M2-versus-M1b rows, which the E1 companion\u2019s \u201cfour of the twenty-eight\u201d excludes (e.g., Spec A M4 versus M3 h=1')

# ---- N1: simulation provenance disclosure ----
rep('- `wave_e_cod/results/sim_retention_power.csv` (10,000 rows: 5 DGPs \u00d72\u03c3\u00d7200\u00d75 modules)',
    '- `wave_e_cod/results/sim_retention_power.csv` (10,000 rows: 5 DGPs \u00d72\u03c3\u00d7200\u00d75 modules; provenance note 2026-09-13: the release archive\u2019s file does not reproduce the published \u00a74.3 rates under the verification-transcript computation \u2014 replacement files registered)')

# ---- qwen 9: Makridakis cited in text ----
rep('Whether the elaboration improves out-of-sample prediction is a separate question from whether the mechanism is real, and it is answerable only against a benchmark and a decision rule fixed in advance.',
    'Whether the elaboration improves out-of-sample prediction is a separate question from whether the mechanism is real, and it is answerable only against a benchmark and a decision rule fixed in advance. The forecasting literature has made the benchmark discipline explicit: across the M4 competition\u2019s 100,000 series, sophisticated methods did not uniformly beat simple statistical baselines (Makridakis et al., 2020).')

# ---- AIC reconciliation ----
rep('Rule comparison from archived output AIC MASE bare beat persistence 0%/10% band variants no refitting',
    'Rule comparison from archived output \u2014 information criterion n log MSE + 2k (AIC-style), MASE, bare beat-persistence, 0%/10% band variants, no refitting')

# ---- claude 4.8: scale reporting ----
rep('**Table 1.** Three objects \u2014 two domains, no pooling. Safe set and LRP define reference frame for secondary Brier threshold score; primary RMSE never uses them (Brier secondary).',
    '**Table 1.** Three objects \u2014 two domains, no pooling. Safe set and LRP define reference frame for secondary Brier threshold score; primary RMSE never uses them (Brier secondary). Scale for reading the RMSEs: SD(target)/SD(\u0394target) are 356.5/89.5 kt (Spec A), 423.2/89.6 kt (Spec B), and 14.70/12.34 ft (Edwards).')

# ---- AD4: prospective replacement band (register §4 AD4 directive) ----
rep('No refitting, applied post hoc to archived table, fold into rule comparison.',
    'No refitting, applied post hoc to archived table, fold into rule comparison. A simulation-calibrated band targeting power \u22650.80 / specificity \u22650.90 at the object\u2019s own T and SNR is registered as the prospective replacement.')

open(DST, 'w', encoding='utf-8').write(s)
print(f'wrote {DST} ({len(s):,} chars, {s.count(chr(10))} lines)')
print('all', sum(1 for _ in open(SRC)), 'source lines processed; edits applied: 41 asserted replacement rules')

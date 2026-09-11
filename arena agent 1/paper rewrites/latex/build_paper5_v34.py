"""Build paper5 v34 from v33 (audit-sweep revision). All substitutions asserted-once."""
import sys

SRC = '/home/user/paper5_v33/paper5_sampled_governance_v33.tex'
DST = '/home/user/paper5_v34/paper5_sampled_governance_v34.tex'

s = open(SRC, encoding='utf-8').read()
n0 = len(s)

SUBS = [
 ('M14-header',
  r'% Periodic Review as Sampled Governance (paper 5, revision v33): tail-section remnant sweep and citation-hygiene revision with line numbers for review.',
  r'% Periodic Review as Sampled Governance (paper 5, revision v34): audit-sweep revision (endpoint-trim check, periodogram deposit, power-design specification, prospective-design completion, methods precision) with line numbers for review.'),
 ('M1-intro-five',
  "constructive content is the prospective programme --- five identification designs and a closed-loop\n"
  "evaluation design specified as preregistration targets --- that could",
  "constructive content is the prospective programme --- five prospective designs\n"
  "specified as preregistration targets --- that could"),
 ('M2-cohort',
  "Stock Assessment Database v4.66 (Ricard, Minto, Jensen, and Baum, 2012),\n"
  "selected by an annual-review eligibility criterion defined for this analysis. The release",
  "Stock Assessment Database v4.66 (Ricard, Minto, Jensen, and Baum, 2012): the annual-review designation (applied from general regime knowledge, not per-stock primary verification) covers the full 58-stock panel, and 42 stocks pass the \\(n\\ge 20\\) valid-point filter (series lengths 20--77 yr). The release"),
 ('M3a-bands-lineage',
  "sprat class), bracketing the model-predicted institutional periods near 4 and\n"
  "8 yr, with contextual bands C (9--14 yr) and D (14--30 yr). The tested",
  "sprat class), bracketing the observable-specific dominant biomass peaks near 4 and\n"
  "8 yr of the archived stage-map diagnostics (provisional records, Section 3.3), with contextual bands C (9--14 yr, cohort/recruitment) and D (14--30 yr, trend/regime). The tested"),
 ('M3b-ar1-fit',
  "statistic is band-integrated power, compared with a per-series AR(1) red-noise\n"
  "null (200 replicates, seed 7, detrending inside each replicate). Empirical",
  "statistic is band-integrated power, compared with a per-series AR(1) red-noise\n"
  "null (coefficient by lag-1 autocorrelation of the detrended series; 200 replicates, seed 7, detrending inside each replicate). Empirical"),
 ('M4a-power-noise',
  "Power experiments inject the model-generated effort signal into\n"
  "white noise and apply the same band-power statistic (the",
  "Power experiments inject the model-generated effort signal into\n"
  "white noise (multiplicative lognormal, fractional \\(\\sigma\\)) and apply the same band-power statistic (the"),
 ('M4b-power-spec',
  "(\\texttt{power\\_demo.py}, \\texttt{power\\_driver\\_v2.py}) are deposited\n"
  "with the article.",
  "(\\texttt{power\\_demo.py}, \\texttt{power\\_driver\\_v2.py}) are deposited\n"
  "with the article. Detection uses nominal per-cell 95\\% AR(1)-null thresholds (120 null replicates, seed 7) in detection bands 30--120 yr (sprat-class) and 8--20 yr (anchovy-class and the cod false-positive cell), with 50 trials per cell (seeds 0--49; binomial standard error at most 0.07). The H400 cells in the filed record are supplementary, outside the 100--200 yr design."),
 ('M8-H0',
  "\\textbf{Proposition 3.1} (Forward invariance of the sampled process).\n"
  "Assume:\n\n(H1)",
  "\\textbf{Proposition 3.1} (Forward invariance of the sampled process).\n"
  "Assume:\n\n(H0) \\(r,K,q,E_{\\max},\\tau_m>0\\).\n\n(H1)"),
 ('M7-xop-split',
  "middle band overlaps slow cod-class growth rates but remains\n"
  "confounded with cohort resonance --- a different operator from Section\n"
  "3.7's four-state loop. Full windows,",
  "middle band overlaps slow cod-class growth rates but remains\n"
  "confounded with cohort resonance. That operator differs from Section\n"
  "3.7's four-state loop. Full windows,"),
 ('M5a-battery-list',
  "That null verdict is robust: an eleven-variant sensitivity\n"
  "battery --- ARMA(1,1), trend-stationary-no-detrend,",
  "That null verdict is robust: an eleven-variant sensitivity\n"
  "battery --- the AR(1) baseline plus ARMA(1,1), trend-stationary-no-detrend,"),
 ('M5b-s33-pointer',
  "evidence that annual review stabilises anything. On the stage-structured\n"
  "review map, annual-review stability at every tested response value is",
  "evidence that annual review stabilises anything. On the stage-structured\n"
  "review map (Section 3.3), annual-review stability at every tested response value is"),
 ('M5c-s24-pointer',
  "the resolution bound in Supplementary S9.1).",
  "the resolution bound in Supplementary S9.1; the screen's restricted-result status is stated in Section 2.4)."),
 ('M6-trend',
  "prospective design, not a general test of the extractive mechanism.\n\n"
  "The evidentiary separation is complete:",
  "prospective design, not a general test of the extractive mechanism. The sprat-class 1.0 at \\(\\sigma=0.1\\) is trend detection (growth-transient run-up in the 30--120 yr band), not cycle detection, and is fragile at \\(\\sigma=0.3\\).\n\n"
  "The evidentiary separation is complete:"),
 ('M9a-panels',
  "interval or a closed-loop phase, not separate \\(\\tau_{\\rm dec}\\) and\n"
  "\\(\\tau_{\\rm dep}\\) values. The cod case supplies",
  "interval or a closed-loop phase, not separate \\(\\tau_{\\rm dec}\\) and\n"
  "\\(\\tau_{\\rm dep}\\) values. Event definitions, a coding manual, the source hierarchy with conflict rules, and versioned provenance are preregistered with the panel. The cod case supplies"),
 ('M9b-quasi',
  "according to its assumptions, not merely data availability. Two coding",
  "according to its assumptions, not merely data availability. Preregistration fixes the estimand, treatment timing, controller sign, comparison units, anticipation and pretrend tests, spillover and concurrent-shock handling, and negative controls. Two coding"),
 ('M9c-heldout',
  "held-out block is scored, using stated predictive and calibration\n"
  "criteria; model weights or posterior probabilities require an explicit",
  "held-out block is scored, using stated predictive and calibration\n"
  "criteria, with frozen training/validation splits, declared outcome variables and horizons, and misspecification diagnostics; model weights or posterior probabilities require an explicit"),
 ('M9d-hitl',
  "criteria, sample size, exclusions, and analysis are intended for\n"
  "preregistration; field pilots that would randomise",
  "criteria, sample size, exclusions, and analysis are intended for\n"
  "preregistration, together with ethical review and consent, allocation concealment, the incentive structure, learning and repeated-play controls, attrition rules, power calculations, and multiplicity control; field pilots that would randomise"),
 ('M9e-mse',
  "Model-class worst-case, distributionally robust, and model-averaged\n"
  "performance answer different questions and are reported separately.",
  "Model-class worst-case, distributionally robust, model-averaged, scenario-based, and frequentist expected performance answer different questions and are reported separately. Preregistration fixes primary and secondary endpoints, operating-model weights, tail-risk estimands, common-random-number pairing, and the reporting of optimiser and assessment failures as outcomes."),
 ('M10-iv',
  "the AR(1) null may understate low-frequency power.\n"
  "\\item The zero-count case search does not independently disconfirm",
  "the AR(1) null may understate low-frequency power. The eleven-variant battery of Supplementary S9.1 holds the zero count under ARMA(1,1), trend-stationary, block-bootstrap, detrending, and regime-shift nulls; the remaining masked-peak risk runs via overestimated null power (unmodelled observation-error or retrospective-bias variance raising the threshold), not the underestimation above.\n"
  "\\item The zero-count case search does not independently disconfirm"),
 ('M11a-eta-row',
  "Logistic hold-map core & effort-response coefficient \\(\\eta\\) & 0.914\n"
  "(continuous-delay asides on the same loop) & Sections 3.3 and 3.7 \\\\",
  "Logistic hold-map core & effort-response coefficient \\(\\eta\\) & 0.914 & This table;\n"
  "constants block \\texttt{droop\\_test.py} L49--58 @ 24c980cd \\\\"),
 ('M11b-units',
  "values not stated remain in\n"
  "the computational record (this appendix).",
  "values not stated remain in\n"
  "the computational record (this appendix). Time is in years; biomass, effort, and signal scales are bare model units (\\(K\\), \\(E_{\\max}\\), \\(Z_{\\rm ref}\\), and \\(\\Delta_{\\rm ref}\\) set the scales)."),
 ('M12-Mx',
  "\\(\\mathfrak s\\), \\(K\\), \\(C(t)\\), \\(M\\), \\(F\\) & cod case: unstable\n"
  "threshold, unexploited capacity, removals, natural mortality, fishing",
  "\\(\\mathfrak s\\), \\(K\\), \\(C(t)\\), \\(M\\), \\(M_x\\), \\(F\\) & cod case: unstable\n"
  "threshold, unexploited capacity, removals, natural mortality, extra mortality, fishing"),
 ('M15-supp-pointer',
  "accompanying file \\texttt{paper5\\_supplementary\\_v9.md}",
  "accompanying file \\texttt{paper5\\_supplementary\\_v10.md}"),
 ('M13-logs',
  "power-simulation code and seeds, and the sensitivity-battery code and\n"
  "log are deposited with the article. The stage-map reconstruction",
  "power-simulation code and seeds, and the sensitivity-battery code and\n"
  "logs are deposited with the article. The stage-map reconstruction"),
]

fails = []
for tag, old, new in SUBS:
    c = s.count(old)
    if c != 1:
        fails.append((tag, c))
        continue
    s = s.replace(old, new, 1)

if fails:
    print('FAILED:', fails)
    sys.exit(1)
open(DST, 'w', encoding='utf-8').write(s)
print(f'v34 built: {len(SUBS)}/{len(SUBS)} subs ok, {n0} -> {len(s)} bytes')

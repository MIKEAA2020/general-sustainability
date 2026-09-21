"""Build paper5 v41 main tex from v40: surgical demotion (power grid, case
enumeration, cod ledgers, prospective specifications to S4/S5/S13)."""
import re

SRC = '/home/user/paper5_v40/paper5_sampled_governance_v40_NatSustain.tex'
DST = '/home/user/paper5_v41/paper5_sampled_governance_v41_NatSustain.tex'
s = open(SRC, encoding='utf-8').read()
n0 = len(s)

def repw(old_joined, new, tag):
    global s
    pat = re.compile(re.escape(old_joined).replace(r'\ ', r'\s+'))
    ms = pat.findall(s)
    assert len(ms) == 1, f'{tag}: count={len(ms)}\n---\n{old_joined[:250]}'
    s = pat.sub(lambda _: new, s, count=1)
    print(f'{tag}: OK (flex)')

def rep(old, new, tag):
    global s
    c = s.count(old)
    assert c == 1, f'{tag}: count={c}\n---\n{old[:250]}'
    s = s.replace(old, new, 1)
    print(f'{tag}: OK')

# V version comment
rep('% The decision clock (paper 5, revision v40): q-calibration and cross-system evidence (F-placement, ADH verification, F-excess dormancy test, 50-digit precision certificate), results-at-a-glance table, F-scale scope sentence with line numbers for review.',
    '% The decision clock (paper 5, revision v41): surgical demotion to supplementary (power grid, case enumeration, cod ledgers, prospective specifications to S4/S5/S13; main keeps theory spine, headline records, verdicts) with line numbers for review.',
    'V-version')

# D1 Section 2.5: grid configuration to S13.1
repw(r'Detection uses nominal per-cell 95\% AR(1)-null thresholds (120 null replicates, seed 7) in detection bands 30--120 yr (sprat-class) and 8--20 yr (anchovy-class and the cod false-positive cell), with 50 trials per cell (seeds 0--49; binomial standard error at most 0.07). The H400 cells in the filed record are supplementary, outside the 100--200 yr design.',
     r'The executed grid configuration is Supplementary S13.1.',
     'D1-power-grid')

# D2 Section 3.6: gain/phase design to S13.3
repw(r'A complementary prospective design estimates resolvable gain and phase rather than waiting for several complete endogenous cycles. For a locally linear specified model, the empirical target is the frequency response from an independently timed assessment or command perturbation to realised effort and stock response over the annual-to-decadal band the data support. Identification requires exogenous excitation, an intervention design, or a justified closed-loop method (Forssell and Ljung, 1999). The analysis reports phase margin and uncertainty, compares alternative ecological and controller factorisations, and rejects the mechanism when no admissible factorisation reproduces the pre-registered gain--phase curve.',
     r'The complementary prospective design is specified in Section 4.5 (detail in Supplementary S13.3).',
     'D2-gainphase')

# D3 Section 3.7 Sheridan/cod/haddock paragraph
repw(r"Sheridan-6 groundwater shows a decline--recovery--decline pattern with precipitation explaining approximately half the index-well variance (\(R^2\approx0.47\)). The official programme record establishes a 55 acre-inch block allocation over the five-year first period rather than a continuously adjusted feedback. Icelandic cod under the 1995 harvest-control rule (annual total allowable catch at 25\% of fishable biomass, subject to a minimum catch provision) has a post-rule coefficient of variation of 0.387 (calculated here; 0.394 on the 2026-09-11 current-vintage pull, Supplementary S4) with post-1995 variability (coefficient of variation 0.37--0.39) and no dominant spectral peak (Supplementary S11). The estimated implementation lag, however, is approximately 0.2--0.3 yr --- a lag that is not a review interval --- and cohort resonance supplies an alternative mechanism, its period 15--25 times shorter than the four-state prediction --- the stage-structured review map's closed loop of four state components (adults \(A\), juveniles \(J\), memory signal \(Z\), held effort \(E\)), whose slow-stock class carries the centuries-scale dominant timescales of Section 3.3. Icelandic haddock under a related rule has a post-2013 (own-HCR) SSB coefficient of variation of 0.24, lower despite higher recruitment variability.",
     r"Sheridan-6 groundwater (hydrological driver without a feedback rule) and Icelandic cod and haddock under harvest-control rules (rule present, no review-cycle identification) illustrate the confound patterns at case level (Supplementary S4). The four-state prediction is the stage-structured review map's closed loop of four state components (adults \(A\), juveniles \(J\), memory signal \(Z\), held effort \(E\)), whose slow-stock class carries the centuries-scale dominant timescales of Section 3.3.",
     'D3-case-para')

# D4 Section 3.7 anchoveta paragraph
repw(r'Peruvian anchoveta provides a further discriminator. The 1950--2019 catch series has a robust period near 3.7 yr, matching ENSO recurrence as a candidate driver, with cross-correlation \(|r|\approx0.31\) for ENSO leading catch (detrended log catch against NINO1 at one-year lead, \(r=-0.31\), \(p=0.009\)). A confirmatory battery on the archived Sea Around Us series behind that figure (Peru and global-taxon series, 1950--2019; Supplementary S4) reproduces the 3.7-yr peak (3.70 yr, co-dominant with 7.96 yr in a flat multi-peak spectrum). The Southern Oscillation Index (SOI) carries no multiplicity-robust association (0 of 90 index--lag cells at the Benjamini--Hochberg bound; Peru lag zero to two \(r=+0.07\)/\(+0.16\)/\(+0.01\), n.s.). The ninety index--lag cells define the Benjamini--Hochberg multiplicity family; the Granger tests are confirmatory and outside that family. Bivariate Granger tests find one-sided ENSO-to-catch dependence in both series (Peru \(p=0.00009\), global-taxon \(p=0.00016\), at lag two; reverse directions \(p\ge0.19\)). Convergent cross mapping remains directionally inconclusive even at seventy annual points. The association is therefore evidence of shared periodicity, not an identified mechanism --- its mechanistic-scale support is the documented El Ni\~no--anchoveta pathway (Ch\'avez et al., 2003) and the sediment fish-scale records (Guti\'errez et al., 2009) --- and the subannual review regime lies below the anchovy-class review-interval response region, so the unclassified controller prevents that comparison from testing the mechanism. The 3.7 yr catch periodicity is not a review interval.',
     r'Peruvian anchoveta provides a further discriminator: a robust 3.7 yr catch periodicity with ENSO as candidate driver, evidence of shared periodicity rather than an identified mechanism (Supplementary S4 for the battery, multiplicity family, and confirmatory tests). The subannual review regime lies below the anchovy-class review-interval response region, so the unclassified controller prevents that comparison from testing the mechanism. The 3.7 yr catch periodicity is not a review interval.',
     'D4-anchoveta')

# D5 Section 3.7 budworm paragraph
repw(r"One documented system sits at the window's edge rather than inside it. The spruce budworm's 30--40 yr outbreak cycle maps to an effective regeneration rate \(r \approx 0.025\)--\(0.033\) yr\textsuperscript{-1} under a \(1/\mathrm{period}\) reading (Ludwig, Jones, and Holling, 1978) --- above the upper edge of the companion delay study's baseline instability window (\(\approx 0.022\) yr\textsuperscript{-1} at \(\eta = 0.914\); Abaee, 2026) and inside it only at elevated effort response, whose window extends to \(\approx 0.061\) yr\textsuperscript{-1} at \(\eta = 3\). The cycle is endogenous predator--prey outbreak dynamics rather than institutionally driven: the system corroborates the mechanism class, not the institutional claim.",
     r"One documented system sits at the window's edge rather than inside it: the spruce budworm 30--40 yr outbreak cycle is endogenous predator--prey outbreak dynamics rather than institutionally driven (Supplementary S4 for the rate mapping and window comparison). The system corroborates the mechanism class, not the institutional claim.",
     'D5-budworm')

# D6a Section 3.8 rounding parenthetical (cut; caption + S13.2 cover)
repw(r'(e.g. underlying values 381.95, 101.05, 30.55 kt)',
     r'',
     'D6a-rounding')

# D6b Section 3.8 constrained-M quantities
repw(r'The constrained-M quantities (crash window \(M=0.46\), \(F=1.37\), unreported catch \(257.8\) kt yr\(^{-1}\) --- \(1.025\) yr\(^{-1}\) relative to mean spawning biomass (a yearly flow divided by a stock); non-recovery window \(M=0.43\), \(F=0.25\), \(3.7\) kt yr\(^{-1}\)) are unreproduced: they are targets for future reproduction requiring equations, source series, code, units, windows, and uncertainty, listed as open problems and stated here as hypotheses, not results.',
     r'The constrained-M quantities are unreproduced (Supplementary S13.2 for the quantities and reproduction requirements): they are listed as open problems and stated here as hypotheses, not results.',
     'D6b-constrainedM')

# D7 Section 3.8 Table-2 readout (cut; table stays)
repw(r'After the moratorium, the series both rises and falls across tens of thousands of tonnes --- 16.05, 34.42, and 20.07 kt in 1996, 2000, and 2004, before the recovery window of 25.18, 96.91, and 298.65 kt in 2005, 2010, and 2015 (selected years; the full annual record with uncertainty intervals is the assessment table).',
     r'After the moratorium, the series both rises and falls across tens of thousands of tonnes (Table 2; the full annual record with uncertainty intervals is the assessment table).',
     'D7-readout')

# D8 Section 3.8 ecosystem numbers (in S5 already)
repw(r'The ecosystem context (Supplementary S5) is background only: between 1985--87 and 2013--15, harp seal biomass rose from 49,600 t to 161,183 t (a 3.2-fold increase) and capelin biomass fell from 13.77 to 4.97 t km\(^{-2}\) (a 64\% decline) in the mass-balance record (Tam and Bundy, 2019). These are descriptive mass-balance inputs, not causal tests.',
     r'The ecosystem context (Supplementary S5) is background only: the harp seal increase and capelin decline in the mass-balance record (Tam and Bundy, 2019) are descriptive inputs, not causal tests.',
     'D8-ecosystem')

# D9a Section 4.5 governance-event panels
repw(r'For each resource--jurisdiction unit, construct a source-linked event record containing the raw-observation date, the public or scientific recognition date, assessment completion, scheduled review, formal decision, legal adoption, physical deployment, compliance, realised-pressure change, and subsequent ecological-response dates. Date uncertainty, interval censoring, revisions, missing stages, and overlapping interventions are kept distinct rather than collapsed to one lag. Such a panel estimates component-specific delay distributions only for stages actually observed; otherwise the estimand is a combined interval or a closed-loop phase, not separate \(\tau_{\rm dec}\) and \(\tau_{\rm dep}\) values. Event definitions, a coding manual, the source hierarchy with conflict rules, and versioned provenance are preregistered with the panel. The cod case supplies two dated decision events for such a panel --- the moratorium announcement of 2 July 1992 and the reopening of 26 June 2024 with an 18 kt total allowable catch --- with two negative constraints: no governance lead is inferred from annual biomass data, and a fast response does not establish adequacy.',
     r'For each resource--jurisdiction unit, a source-linked event record dates each stage from raw observation to ecological response, with date uncertainty kept distinct rather than collapsed to one lag (full specification in Supplementary S13.3). The cod case supplies two dated decision events --- the moratorium announcement of 2 July 1992 and the reopening of 26 June 2024 with an 18 kt total allowable catch --- with two negative constraints: no governance lead is inferred from annual biomass data, and a fast response does not establish adequacy.',
     'D9a-panels')

# D9b Section 4.5 quasi-experimental timing
repw(r'Candidate interventions include staggered adoption, discontinuities in review schedules, rule changes, jurisdictional borders, phased quota systems, and administrative reforms whose timing is plausibly independent of the outcome innovation. An event study, difference-in-differences design, synthetic control, interrupted time series, or state-space intervention model is chosen according to its assumptions, not merely data availability. Preregistration fixes the estimand, treatment timing, controller sign, comparison units, anticipation and pretrend tests, spillover and concurrent-shock handling, and negative controls. Two coding rules are binding: a change in implementation lag is not coded as a change in \(T_r\), and a nominal schedule change is not a treatment unless it changes a responsive decision opportunity.',
     r'Event-study, difference-in-differences, synthetic-control, interrupted-time-series, or state-space intervention designs on schedule variation plausibly independent of the outcome innovation, with preregistered estimands (full specification in Supplementary S13.3). Two coding rules are binding: a change in implementation lag is not coded as a change in \(T_r\), and a nominal schedule change is not a treatment unless it changes a responsive decision opportunity.',
     'D9b-quasi')

# D9c Section 4.5 displacement discipline
repw(r'For each candidate system, compare at least an environmental-forcing model, a cohort- or demographic-resonance model, an institutional-delay model with specified controller sign, a combined model, and a null time-series model. Models make predictions before the held-out block is scored, using stated predictive and calibration criteria, with frozen training/validation splits, declared outcome variables and horizons, and misspecification diagnostics; model weights or posterior probabilities require an explicit likelihood and prior, and predictive ranking alone does not identify a causal mechanism. The displacement rule: a delay explanation is weakened when it cannot reproduce the pre-registered phase ordering, and it is displaced when a competing mechanism predicts the held-out observations better --- complexity is admitted only on scored evidence, never by accumulation.',
     r'Held-out comparison across environmental-forcing, cohort-resonance, institutional-delay (specified controller sign), combined, and null time-series models, with frozen splits and declared outcomes (full specification in Supplementary S13.3). The displacement rule: a delay explanation is weakened when it cannot reproduce the pre-registered phase ordering, and displaced when a competitor predicts the held-out observations better.',
     'D9c-displacement')

# D9d Section 4.5 human-in-the-loop experiments
repw(r'A minimum design places participants in the same simulated renewable-resource environment and randomises review cadence and the timing or sign of decision feedback, with ecological shocks held common across arms where appropriate. Primary endpoints include realised pressure, threshold crossings, recovery time, variability, and the gain--phase relation between assessments, commands, and actions --- the gain--phase signature being the more diagnostic empirical target than periodicity alone, since a spectral peak cannot identify the loop direction. Treatment rules, stopping and safety criteria, sample size, exclusions, and analysis are intended for preregistration, together with ethical review and consent, allocation concealment, the incentive structure, learning and repeated-play controls, attrition rules, power calculations, and multiplicity control; field pilots that would randomise extractive response to decline require viability constraints and stopping rules before controller-sign randomisation is considered, and the randomisation described is a laboratory or advisory-interface design, not a field intervention on a live stock. Agent-based institutional experiments, digital-twin exercises, and carefully governed field pilots complement this design; extrapolation from a laboratory or simulated resource to a field institution remains a separate external-validity claim. Mechanism-class precedent exists --- controlled population and resource-management experiments show that delay- and parameter-driven transitions can be empirically studied (Costantino, Cushing, Dennis, and Desharnais, 1995), and commons-free fishery-management experiments in which subjects overshoot by approximately 60\% from stock-and-flow misperception show the behavioural substrate (Moxnes, 1998) --- but precedent for the mechanism class is not validation of the institutional equations.',
     r'Randomised review cadence and feedback timing or sign in a common simulated renewable-resource environment, with the gain--phase signature as the diagnostic target (full specification in Supplementary S13.3). The randomisation described is a laboratory or advisory-interface design, not a field intervention on a live stock; mechanism-class precedent exists (Costantino, Cushing, Dennis, and Desharnais, 1995; Moxnes, 1998) but is not validation of the institutional equations.',
     'D9d-humanloop')

# D9e Section 4.5 closed-loop MSE
repw(r'Because retrospective evidence does not identify the mechanism, policy comparison must be conducted in a closed loop that keeps process, observation and assessment, parameter, structural-model, decision, and implementation uncertainty distinct (the management-procedure tradition: Punt and Donovan, 2007). Each simulation replicate contains: an operating model (age- or stage-structured or other resource dynamics, environmental forcing, density dependence, structural alternatives); an observation model (survey and catch observations, missingness, bias, autocorrelated error); an assessment model (estimator, update frequency, retrospective bias, uncertainty); a decision rule (extractive, protective, fixed-plan, or hybrid, including caps on change and emergency clauses); an implementation model (compliance, deployment lag, effort creep, realised versus commanded pressure); and performance metrics (threshold risk, yield and service delivery, variability, closure frequency, effort cost, recovery time, distributional impacts). The core experimental design crosses \[ T_r\times\tau_{\rm dec}\times\tau_{\rm dep}\times\text{controller sign}\times\text{observation/assessment error}\times\text{parameter draw}\times\text{operating-model class}\times\text{process-noise regime}. \] At minimum, responsive extractive, responsive protective, and fixed-plan controllers are compared; a conclusion that compares only two review intervals inside the extractive class cannot be generalised to governance as a whole. Parameter uncertainty varies quantities within a specified operating model; process uncertainty governs stochastic state evolution; observation and assessment uncertainty govern the information supplied to the rule; and structural uncertainty varies the operating-model class itself, represented by multiple operating models rather than one parameter covariance matrix around a fitted model. Model-class worst-case, distributionally robust, model-averaged, scenario-based, and frequentist expected performance answer different questions and are reported separately. Preregistration fixes primary and secondary endpoints, operating-model weights, tail-risk estimands, common-random-number pairing, and the reporting of optimiser and assessment failures as outcomes.',
     r'Policy comparison in a closed loop keeping six uncertainty classes distinct (the management-procedure tradition: Punt and Donovan, 2007), crossing review timing, delays, controller sign, observation error, parameter draws, operating-model class, and process-noise regime (full specification in Supplementary S13.3). At minimum, responsive extractive, responsive protective, and fixed-plan controllers are compared; a conclusion that compares only two review intervals inside the extractive class cannot be generalised to governance as a whole.',
     'D9e-mse')

print('len delta:', len(s) - n0)
import os
os.makedirs('/home/user/paper5_v41', exist_ok=True)
open(DST, 'w', encoding='utf-8').write(s)
print('WROTE', DST)

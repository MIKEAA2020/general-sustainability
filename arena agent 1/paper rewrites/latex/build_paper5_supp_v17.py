"""Build paper5 supplementary v17 from v16: S13 demoted detail + S4 budworm
row + S1 touches for v41."""
import re

SRC = '/home/user/paper5_v40/paper5_supplementary_v16_NatSustain.md'
DST = '/home/user/paper5_v41/paper5_supplementary_v17_NatSustain.md'
s = open(SRC, encoding='utf-8').read()
n0 = len(s)

def rep(old, new, tag):
    global s
    c = s.count(old)
    assert c == 1, f'{tag}: count={c}\n---\n{old[:220]}'
    s = s.replace(old, new, 1)
    print(f'{tag}: OK')

# P1 intro: thirteen bodies + S13 listing
rep('It carries twelve bodies of material:',
    'It carries thirteen bodies of material:',
    'P1a-bodies')
rep('; and the F-calibration, ADH cross-system, and precision-certificate records (S12).',
    '; the F-calibration, ADH cross-system, and precision-certificate records (S12); and the demoted technical detail (S13).',
    'P1b-s13list')

# P2 S1 rows
rep('the five prospective designs (preregistration targets; not executed).',
    'the five prospective designs (preregistration targets; not executed; full specifications in S13.3).',
    'P2a-s1-45')
rep('The seal-predation threshold-shift reading is a directional application of Lemma 2.2(ii), explicitly non-quantitative.',
    'The seal-predation threshold-shift reading is a directional application of Lemma 2.2(ii), explicitly non-quantitative. The constrained-M quantities are hypotheses with reproduction requirements (S13.2).',
    'P2b-s1-38')
rep('the injected-signal power design (methods; code and seeds deposited; H400 cells supplementary).',
    'the injected-signal power design (methods; code and seeds deposited; H400 cells supplementary; grid configuration in S13.1).',
    'P2c-s1-25')

# P3 S4 budworm row (after produced-capital row)
rep('the resource model assumes.\n\nThe case-screening table',
    'the resource model assumes.\n- **Spruce budworm:** 30\u201340 yr outbreak cycle mapping to an effective regeneration rate $r \\approx 0.025$\u2013$0.033$ yr$^{-1}$ under a $1/{\\rm period}$ reading (Ludwig, Jones, and Holling, 1978) \u2014 above the upper edge of the companion delay study\u2019s baseline instability window ($\\approx 0.022$ yr$^{-1}$ at $\\eta = 0.914$; Abaee, 2026) and inside it only at elevated effort response (window to $\\approx 0.061$ yr$^{-1}$ at $\\eta = 3$). The cycle is endogenous predator\u2013prey outbreak dynamics rather than institutionally driven: the system corroborates the mechanism class, not the institutional claim.\n\nThe case-screening table',
    'P3-budworm')

# P4 append S13
S13 = '''

---

## S13. Demoted technical detail (§§2.5, 3.6–3.8, 4.5)

This section holds the technical detail summarised in the main text. Claims and statuses are as inventoried in S1.

### S13.1 Power-grid configuration (§2.5)

Executed grid configuration for the injected-signal power design. Grid points: sprat $(r,g,T_r) = (0.8,2,7)$, anchovy $(1.6,1,3)$, cod false-positive $(0.3,5,5)$; horizons $H \\in \\{100,200\\}$ yr (H400 cells supplementary, outside the design); detection bands 30–120 yr (sprat-class) and 8–20 yr (anchovy-class and the cod false-positive cell); Lomb-Scargle $n_f = 800$; nominal per-cell 95% AR(1)-null thresholds (120 null replicates, seed 7); 50 trials per cell (seeds 0–49; binomial standard error at most 0.07). Routines: `power_demo.py`, `power_driver_v2.py` (deposited).

### S13.2 Crash-window ledger detail (§3.8)

Displayed assessment values are rounded from the assessment table (underlying values 381.95, 101.05, 30.55 kt). Constrained-M quantities: crash window $M = 0.46$, $F = 1.37$, unreported catch $257.8$ kt yr$^{-1}$ ($1.025$ yr$^{-1}$ relative to mean spawning biomass, a yearly flow divided by a stock); non-recovery window $M = 0.43$, $F = 0.25$, $3.7$ kt yr$^{-1}$. Reproduction requirements: equations, source series, code, units, windows, uncertainty. Status: hypotheses (open problems), not results.

### S13.3 Prospective-design specifications (§§3.6, 4.5)

Full specifications of the prospective designs summarised in the main text. None has been executed; each is a preregistration target, with no registration identifier or archived protocol yet, and none is claimed.

**Gain–phase prospective identification (§3.6).** A complementary prospective design estimates resolvable gain and phase rather than waiting for several complete endogenous cycles. For a locally linear specified model, the empirical target is the frequency response from an independently timed assessment or command perturbation to realised effort and stock response over the annual-to-decadal band the data support. Identification requires exogenous excitation, an intervention design, or a justified closed-loop method (Forssell and Ljung, 1999). The analysis reports phase margin and uncertainty, compares alternative ecological and controller factorisations, and rejects the mechanism when no admissible factorisation reproduces the pre-registered gain–phase curve.

**Governance-event panels.** For each resource–jurisdiction unit, construct a source-linked event record containing the raw-observation date, the public or scientific recognition date, assessment completion, scheduled review, formal decision, legal adoption, physical deployment, compliance, realised-pressure change, and subsequent ecological-response dates. Date uncertainty, interval censoring, revisions, missing stages, and overlapping interventions are kept distinct rather than collapsed to one lag. Such a panel estimates component-specific delay distributions only for stages actually observed; otherwise the estimand is a combined interval or a closed-loop phase, not separate $\\tau_{\\rm dec}$ and $\\tau_{\\rm dep}$ values. Event definitions, a coding manual, the source hierarchy with conflict rules, and versioned provenance are preregistered with the panel. The cod case supplies two dated decision events for such a panel — the moratorium announcement of 2 July 1992 and the reopening of 26 June 2024 with an 18 kt total allowable catch — with two negative constraints: no governance lead is inferred from annual biomass data, and a fast response does not establish adequacy.

**Quasi-experimental timing.** Candidate interventions include staggered adoption, discontinuities in review schedules, rule changes, jurisdictional borders, phased quota systems, and administrative reforms whose timing is plausibly independent of the outcome innovation. An event study, difference-in-differences design, synthetic control, interrupted time series, or state-space intervention model is chosen according to its assumptions, not merely data availability. Preregistration fixes the estimand, treatment timing, controller sign, comparison units, anticipation and pretrend tests, spillover and concurrent-shock handling, and negative controls. Two coding rules are binding: a change in implementation lag is not coded as a change in $T_r$, and a nominal schedule change is not a treatment unless it changes a responsive decision opportunity.

**Out-of-sample mechanism comparison and the displacement discipline.** For each candidate system, compare at least an environmental-forcing model, a cohort- or demographic-resonance model, an institutional-delay model with specified controller sign, a combined model, and a null time-series model. Models make predictions before the held-out block is scored, using stated predictive and calibration criteria, with frozen training/validation splits, declared outcome variables and horizons, and misspecification diagnostics; model weights or posterior probabilities require an explicit likelihood and prior, and predictive ranking alone does not identify a causal mechanism. The displacement rule: a delay explanation is weakened when it cannot reproduce the pre-registered phase ordering, and it is displaced when a competing mechanism predicts the held-out observations better — complexity is admitted only on scored evidence, never by accumulation.

**Controlled and randomized human-in-the-loop experiments.** A minimum design places participants in the same simulated renewable-resource environment and randomises review cadence and the timing or sign of decision feedback, with ecological shocks held common across arms where appropriate. Primary endpoints include realised pressure, threshold crossings, recovery time, variability, and the gain–phase relation between assessments, commands, and actions — the gain–phase signature being the more diagnostic empirical target than periodicity alone, since a spectral peak cannot identify the loop direction. Treatment rules, stopping and safety criteria, sample size, exclusions, and analysis are intended for preregistration, together with ethical review and consent, allocation concealment, the incentive structure, learning and repeated-play controls, attrition rules, power calculations, and multiplicity control; field pilots that would randomise extractive response to decline require viability constraints and stopping rules before controller-sign randomisation is considered, and the randomisation described is a laboratory or advisory-interface design, not a field intervention on a live stock. Agent-based institutional experiments, digital-twin exercises, and carefully governed field pilots complement this design; extrapolation from a laboratory or simulated resource to a field institution remains a separate external-validity claim. Mechanism-class precedent exists — controlled population and resource-management experiments show that delay- and parameter-driven transitions can be empirically studied (Costantino, Cushing, Dennis, and Desharnais, 1995), and commons-free fishery-management experiments in which subjects overshoot by approximately 60% from stock-and-flow misperception show the behavioural substrate (Moxnes, 1998) — but precedent for the mechanism class is not validation of the institutional equations.

**Closed-loop management strategy evaluation.** Because retrospective evidence does not identify the mechanism, policy comparison must be conducted in a closed loop that keeps process, observation and assessment, parameter, structural-model, decision, and implementation uncertainty distinct (the management-procedure tradition: Punt and Donovan, 2007). Each simulation replicate contains: an operating model (age- or stage-structured or other resource dynamics, environmental forcing, density dependence, structural alternatives); an observation model (survey and catch observations, missingness, bias, autocorrelated error); an assessment model (estimator, update frequency, retrospective bias, uncertainty); a decision rule (extractive, protective, fixed-plan, or hybrid, including caps on change and emergency clauses); an implementation model (compliance, deployment lag, effort creep, realised versus commanded pressure); and performance metrics (threshold risk, yield and service delivery, variability, closure frequency, effort cost, recovery time, distributional impacts). The core experimental design crosses $$T_r \\times \\tau_{\\rm dec} \\times \\tau_{\\rm dep} \\times {\\rm controller\\ sign} \\times {\\rm observation/assessment\\ error} \\times {\\rm parameter\\ draw} \\times {\\rm operating\\mbox{-}model\\ class} \\times {\\rm process\\mbox{-}noise\\ regime}.$$ At minimum, responsive extractive, responsive protective, and fixed-plan controllers are compared; a conclusion that compares only two review intervals inside the extractive class cannot be generalised to governance as a whole. Parameter uncertainty varies quantities within a specified operating model; process uncertainty governs stochastic state evolution; observation and assessment uncertainty govern the information supplied to the rule; and structural uncertainty varies the operating-model class itself, represented by multiple operating models rather than one parameter covariance matrix around a fitted model. Model-class worst-case, distributionally robust, model-averaged, scenario-based, and frequentist expected performance answer different questions and are reported separately. Preregistration fixes primary and secondary endpoints, operating-model weights, tail-risk estimands, common-random-number pairing, and the reporting of optimiser and assessment failures as outcomes.

**Status: methods detail (S13.1, S13.3) and hypotheses (S13.2); claims and statuses as inventoried in S1.**
'''
s = s.rstrip('\n') + '\n' + S13.lstrip('\n')
print('P4-S13: appended')

print('len delta:', len(s) - n0)
import os
os.makedirs('/home/user/paper5_v41', exist_ok=True)
open(DST, 'w', encoding='utf-8').write(s)
print('WROTE', DST)

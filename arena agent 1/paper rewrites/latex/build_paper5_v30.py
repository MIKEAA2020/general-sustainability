#!/usr/bin/env python3
"""Build paper5 v30 from v29: A6 fork decided (rebuild) + battery repairs.

Every substitution asserts exactly one match. Scope (user-directed 2026-09-11):
A6 fork outcome (screens stay results; S2.4 rewritten to the executed screen),
SOI-block repair (artifact-contaminated S3.7 numbers replaced by artifact-free
values), Chile->global-taxon label correction, |r|~0.31 pipeline documentation,
S3.6 void-registration cut, S2.5 white-noise correction + deposit citations,
Appendix-A/Data-availability discharge updates, stale supp-pointer fix (v5->v8).
NOT touched (author-blocked, out of scope): A3 vector, A5 restructure, A8/A9,
A10 compression, A11 note/sensitivity, S4.2, S4.5, S3.3/S3.4/S3.8.
"""
import os
import sys

SRC = "/home/user/paper5_v29/paper5_sampled_governance_v29.tex"
DST = "/home/user/paper5_v30/paper5_sampled_governance_v30.tex"

r = lambda s: s  # marker: strings below are raw triple-quoted

SUBS = [
("VER-header",
r'''% Periodic Review as Sampled Governance (paper 5, revision v29): root-cause resolution revision with line numbers for review.''',
r'''% Periodic Review as Sampled Governance (paper 5, revision v30): screen verification and battery repair revision with line numbers for review.'''),

("A6-S2.4-exec-screen",
r'''For each eligible biomass and exploitation/effort proxy series, the
analysis detrends according to a stated rule, computes a Lomb--Scargle
periodogram (Lomb, 1976; Scargle, 1982), and integrates power in the
prespecified bands (4--8 yr for biomass, 12--60 yr for effort) --- bands
derived from the archived, unreproduced stage-map diagnostics of
Section 3.3 (its observable-specific dominant peaks near 4 and 8 yr in
biomass and 12 and 60 yr in effort) and carry that record's provisional
status into the screen's target definition. The tested statistic is
band-integrated power, and a peak is separately classified for
robustness. The result is compared with a per-series AR(1) red-noise
null. P-values are adjusted across the specified family (stocks,
observables, and bands) by the Benjamini--Hochberg false-discovery-rate
procedure (Benjamini and Hochberg, 1995), which controls the false
discovery rate, not the familywise error rate. Dependence across stocks
and observables (shared climate forcing, shared assessment methods) is
acknowledged, and the Benjamini--Yekutieli procedure under arbitrary
dependence (Benjamini and Yekutieli, 2001) is the prespecified fallback. The
reported zero count is the BH-adjusted result. One caveat: the 12--60 yr band is poorly resolved on records shorter
than about three candidate periods, and at the long-period end band
power is partly a trend test. A peak is classified as robust only if it
survives the null comparison, the multiplicity adjustment, and
sensitivity to detrending and endpoint choices.''',
r'''For each eligible biomass (spawning-stock biomass) series, the analysis
removes a linear trend, computes a Lomb--Scargle periodogram (Lomb, 1976;
Scargle, 1982), normalises it to unit total power, and integrates power in
prespecified bands: target bands A (2.5--5 yr, anchovy class) and B (5--9 yr,
sprat class), bracketing the model-predicted institutional periods near 4 and
8 yr, with contextual bands C (9--14 yr) and D (14--30 yr). The tested
statistic is band-integrated power, compared with a per-series AR(1) red-noise
null (200 replicates, seed 7, detrending inside each replicate). Empirical
\(p\)-values over the 84 target-band cells (42 stocks by bands A and B) are
adjusted by the Benjamini--Hochberg false-discovery-rate procedure (Benjamini
and Hochberg, 1995), which controls the false discovery rate, not the
familywise error rate. Dependence across stocks (shared climate forcing,
shared assessment methods) is acknowledged. The reported zero count is the
BH-adjusted result. A peak is classified as robust only if it survives the
null comparison and the multiplicity adjustment. The cohort table, screen
routine, and multiplicity reconstruction (\texttt{ram\_target\_stocks.csv},
\texttt{ram\_crosssection.py}, \texttt{verify\_bh.py}) are deposited with
the article.'''),

("A6-S2.5-white-noise",
r'''Power experiments inject the model-generated effort signal into
AR(1)-type noise and apply the same band-power statistic (the
conventional power-analysis framing of Cohen, 1988). Power is estimated
on 100--200 yr synthetic records across noise scales.''',
r'''Power experiments inject the model-generated effort signal into
white noise and apply the same band-power statistic (the
conventional power-analysis framing of Cohen, 1988). Power is estimated
on 100--200 yr synthetic records across noise scales. The demonstration
routine and grid driver with the executed configuration and seeds
(\texttt{power\_demo.py}, \texttt{power\_driver\_v2.py}) are deposited
with the article.'''),

("A6-S3.5-target-bands",
r'''No stock in the screened cohort has a peak in the specified biomass or
effort band meeting all robustness criteria.''',
r'''No stock in the screened cohort has a peak in the specified biomass target
bands meeting all robustness criteria.'''),

("SOI-S3.6-cut-registration",
r'''curve. For the anchoveta--ENSO association of Section 3.7, the
planned confirmatory tests are: the era-split attribution ---
explaining the post-1985 attenuation of the ENSO--catch coupling
(management change, reporting regime, or biological reorganisation) ---
as the focal test; a mechanistic pathway model from the SOI through
coastal temperature and upwelling to recruitment; and the index--lag
specification (SOI, lags zero to two, both stocks), fixed by the
executed battery.''',
r'''curve.'''),

("SOI-S3.7-anchoveta",
r'''Peruvian anchoveta provides a further discriminator. The 1950--2019
catch series has a robust period near 3.7 yr, matching ENSO recurrence
as a candidate driver, with cross-correlation \(|r|\approx0.31\) for
ENSO leading catch. A confirmatory battery on the archived Sea Around Us
series behind that figure (Peru and Chile, 1950--2019; Supplementary S4)
reproduces the 3.7-yr peak (3.70 yr, co-dominant with 7.96 yr in a flat
multi-peak spectrum) and resolves the association to the Southern
Oscillation Index: Peru--SOI \(r=+0.51\) contemporaneous (\(p<0.0001\))
and \(+0.42\)/\(+0.40\) at one- and two-year lags, with the Chilean
series replicating (\(r=+0.39\) at lag two, \(p=0.001\)). All ten of the
ninety tested index--lag cells that survive the Benjamini--Hochberg
bound are SOI cells, so the SOI association is multiplicity-robust where
no other index is. The ninety index--lag cells define the Benjamini--Hochberg multiplicity family; the Granger and split-half tests are confirmatory and outside that family. Bivariate Granger tests find one-sided ENSO-to-catch
dependence in both stocks (Peru \(p=0.00009\), Chile \(p=0.00016\), at
lag two; reverse directions \(p\ge0.19\)). The association is not
era-invariant: split-half analysis confines it to 1950--1984 (lag-one
\(r=+0.42\), \(p=0.013\); after 1985 it is absent, \(r=+0.13\), n.s.,
with the lag-two cell reversing sign), and the early-period strength
survives both the exclusion of the three collapse years and a
reported-catches-only sensitivity on the Chilean series, so the
attenuation is not a reconstruction artefact. Convergent cross mapping
remains directionally inconclusive even at seventy annual points, and
the post-1985 attenuation is treated as a focal test rather than
claimed as a regime effect. The association is therefore evidence of
shared, era-bounded periodicity, not an identified mechanism --- its
mechanistic-scale support is the documented El Ni\~no--anchoveta pathway
(Ch\'avez et al., 2003) and the sediment fish-scale records (Guti\'errez et
al., 2009) --- and the subannual review regime lies below the
anchovy-class review-interval response region, so the unclassified controller prevents
that comparison from testing the mechanism.''',
r'''Peruvian anchoveta provides a further discriminator. The 1950--2019
catch series has a robust period near 3.7 yr, matching ENSO recurrence
as a candidate driver, with cross-correlation \(|r|\approx0.31\) for
ENSO leading catch (detrended log catch against NINO1 at one-year lead,
\(r=-0.31\), \(p=0.009\)). A confirmatory battery on the archived Sea Around Us
series behind that figure (Peru and global-taxon series, 1950--2019;
Supplementary S4) reproduces the 3.7-yr peak (3.70 yr, co-dominant with
7.96 yr in a flat multi-peak spectrum). The Southern Oscillation Index (SOI)
carries no multiplicity-robust association (0 of 90 index--lag cells at
the Benjamini--Hochberg bound; Peru lag zero to two \(r=+0.07\)/\(+0.16\)/\(+0.01\),
n.s.). The ninety index--lag cells define the Benjamini--Hochberg
multiplicity family; the Granger tests are confirmatory and outside that
family. Bivariate Granger tests find one-sided ENSO-to-catch dependence
in both series (Peru \(p=0.00009\), global-taxon \(p=0.00016\), at lag
two; reverse directions \(p\ge0.19\)). Convergent cross mapping remains
directionally inconclusive even at seventy annual points. The association
is therefore evidence of shared periodicity, not an identified mechanism
--- its mechanistic-scale support is the documented El Ni\~no--anchoveta
pathway (Ch\'avez et al., 2003) and the sediment fish-scale records
(Guti\'errez et al., 2009) --- and the subannual review regime lies below
the anchovy-class review-interval response region, so the unclassified
controller prevents that comparison from testing the mechanism.'''),

("SOI-Box1-row",
r'''Anchoveta--ENSO association: 3.7 yr peak, \(r = +0.51\), era-split
1950--1984 & Archived-data battery; association, not an identified
mechanism & Section 3.7 \\''',
r'''Anchoveta--ENSO association: 3.7 yr peak, detrended-NINO1 \(r = -0.31\)
at one-year lead, one-sided NINO1 Granger dependence at lag two &
Archived-data battery; association, not an identified
mechanism & Section 3.7 \\'''),

("A6-AppA-identifiers",
r'''  The RAM stock identifiers and the eligibility table are
  registration requirements (Section 2.4).''',
r'''  The RAM stock identifiers and the eligibility table are
  archived with the computational materials (Section 2.4).'''),

("A6-AppA-simcode",
r'''  The simulation code and seeds are registration requirements
  (Section 2.5).''',
r'''  The simulation code and seeds are archived with the computational materials
  (Section 2.5).'''),

("A6-DataAvail-discharge",
r'''exact-update comparison of Section 3.4, the RAM stock
identifiers and eligibility table, the processed spectral series and
routines, the power-simulation code and seeds, and the case-screening
table and query log are registration requirements; the
corresponding stage-output values carry provisional status until those
artifacts are attached.''',
r'''exact-update comparison of Section 3.4, and the case-screening
table and query log are registration requirements; the
corresponding stage-output values carry provisional status until those
artifacts are attached. The spectral-screen materials (RAM stock identifiers
and eligibility table, processed spectral series and routines) and the
power-simulation code and seeds are deposited with the article.'''),

("B2-supp-pointer-v8",
r'''\texttt{paper5\_supplementary\_v5.md}''',
r'''\texttt{paper5\_supplementary\_v8.md}'''),

("A6-Box1-bands-row",
r'''Screen bands 4--8 yr (biomass) and 12--60 yr (effort) & Descend from the
archived stage peaks; inherit provisional status & Sections 2.4 and
3.3 \\''',
r'''Screen target bands A (2.5--5 yr) and B (5--9 yr) & Prespecified
institutional-period brackets; executed screen & Section 2.4 \\'''),
]

def main():
    s = open(SRC, encoding="utf-8").read()
    for name, old, new in SUBS:
        n = s.count(old)
        if n != 1:
            print(f"FAIL {name}: count={n}")
            sys.exit(1)
        s = s.replace(old, new)
        print(f"ok {name}")
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    open(DST, "w", encoding="utf-8").write(s)
    print("wrote", DST, len(s), "bytes")

if __name__ == "__main__":
    main()

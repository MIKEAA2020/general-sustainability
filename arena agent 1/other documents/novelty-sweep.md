# Novelty Sweep — nine-paper corpus vs. the literature (2026-08-30)

Per-paper: core novelty claim → closest literature found (named, citable) → verdict → binding citations.
Verdicts: **NOVEL-CORE** (unclaimed, build here) / **ENGAGE** (active literature owns the theme; position against it, do not present as new) / **CITE** (established; citation replaces restatement per the standing rule).

## Paper 2 (atlas)

| Claim | Closest literature | Verdict | Binding citations |
|---|---|---|---|
| ERViab obstruction calculus: Thm 6.4 common-action obstruction, Prop 6.12 output-feedback form, Thm 6.10 fibre-certification iff, delayed-information timing bound T_obs > inf q/ε | Veliov 1993 (SUFFICIENCY of output-feedback regulation maps, Set-Valued Anal. 1:305–317); Quincampoix–Cardaliaguet–Saint-Pierre 2007 (estimation-set reduction: imperfect measurement → estimation space, value functions equal; Dini-derivative HJB characterization). Neither gives impossibility witnesses or a certification iff. | **NOVEL-CORE** (the necessity/obstruction complement) — with the caveat below | Veliov 1993; Cardaliaguet–Quincampoix–Saint-Pierre 2007 |
| Thm 3.4 finite-time exit certificate (Dini strip, sup_u inf_d enforced-exit reading) | Barrier certificates: Prajna–Jadbabaie–Pappas 2004/2007 (sufficiency); **Prajna & Rantzer 2005, "On the necessity of barrier certificates"** (converse via convex duality/density functions); Maghenem & Sanfelice 2019 (necessary+sufficient barrier characterizations for hybrid inclusions). The atlas's exit certificate IS a barrier certificate. | **ENGAGE** — novelty is only the observation-timing twist (info arrives after the exit deadline), which must be the paper's stated delta | Prajna & Rantzer 2005; Prajna et al. 2007; Maghenem & Sanfelice 2019 |
| Noncompensation family (Thm 5.1, 5.5–5.8): no scalar weighting certifies the positive cone | Martinez-Alier, Munda & O'Neill 1998 (weak comparability, Ecol. Econ. 26:277–286 — the EE foundation paper, qualitative); Doyen & Gajardo 2020 (NRM 33:e12250 — maximin = "maximal viability", strong-vs-weak content of viable control); Martinet 2011 (JEEM 61:183–197, indicator characterization); Cairns & Martinet 2014 (maximin sustainability indicator, Eur. Econ. Rev. 69:4–17) | **ENGAGE** (the formalization can be a contribution FOR AN EE AUDIENCE — "we prove the mathematical limit the canon asserts verbally" — but it is not a new mathematical family) | Martinez-Alier–Munda–O'Neill 1998; Martinet 2011; Doyen & Gajardo 2020; Cairns & Martinet 2014 |
| Viability calculus, kernel recursion, Nagumo, capture basins, conservation/nonnegativity, small-gain delay certificate, modular composition | Aubin 1991/2001; Saint-Pierre 1994; Cardaliaguet–Quincampoix–Saint-Pierre 1999; Jacquez & Simon 1993; Lygeros–Tomlin–Sastry 1999; Hale 1977; "Using System Modularity to Simplify Viability Studies" (Environ. Model. Assess. 2024) | **CITE** (citation exception applies) | as listed |

**Verdict:** whole-atlas form fails novelty; the SVAA paper must be the obstruction calculus, with the barrier-certificate and estimation-tube literatures engaged as the measuring stick, and the timing twist (T_obs > inf q/ε) as the sharp headline. Everything else: cite (calculus), relocate to P1 (noncompensation, engaged against Martinez-Alier/Martinet/Doyen–Gajardo), or SI (apparatus).

## Paper 1 (typed architecture / assessment doctrines)

| Claim | Closest literature | Verdict | Binding citations |
|---|---|---|---|
| Separation theorem: endpoint ⊂ aggregate(price-parametrized) ⊂ noncompensatory hierarchy; "a plan for each price vector" ≠ "one plan for all" | Martinez-Alier–Munda–O'Neill 1998 (incommensurability, verbally); Martinet 2011 (indicator characterization — which criteria admit indicator representations); Doyen & Gajardo 2020 (maximin = maximal viability); Cairns & Martinet 2014; Neumayer 2013 (weak vs strong sustainability); Dasgupta & Mäler 2000 (NNP/wealth measures) | **NOVEL-CORE as a FORMALIZATION** — the EE canon asserts non-commensurability qualitatively; a proved quantifier/commutativity failure with a machine-witnessed datum is a genuine contribution FOR ECOLOGICAL ECONOMICS; flagged residual: check the exact claim against Dasgupta–Mäler 2000 and Asheim 1994 before finalizing | all listed |
| Typed 13-slot canonical system, claim-status discipline | no direct literature (methodology) | contribution = organizational; keep brief in the article | — |

## Paper 3 (material ledgers)

| Claim | Closest literature | Verdict | Binding citations |
|---|---|---|---|
| Typed donor-limited flux ledger; conservation from incidence structure; nonnegativity from donor limitation | MFA: Brunner & Rechberger 2004, Fischer-Kowalski et al. 2011 (cited); Feinberg 2019 (reaction-network incidence); Jacquez & Simon 1993 (compartmental nonnegativity); SFC: Godley & Lavoie | **ENGAGE** (formalism is the contribution; theorems are instances of known machinery) | as listed |
| Depletion taxonomy J^gross/H^loc/T_A; reserve-life ratio is arithmetic, not an exhaustion forecast | active critical literature: 2024 phosphorus review (JEST 21:9265 — USGS-based depletion timeframes "misleading", single-source-data critique); oil/gas R/P-ratio skepticism; Tilton | **ENGAGE** — the taxonomy formalizes an existing critique; cite the critics by name | 2024 JEST review; USGS 2026 |
| First-passage theorems (inverse-Gaussian groundwater; GBM fisheries) | Chhikara & Folks 1989; Redner 2001; Øksendal 2003 (all cited in v2) | **CITE** (the paper already does) | — |

## Paper 4 (delay dynamics)

| Claim | Closest literature | Verdict | Binding citations |
|---|---|---|---|
| Institutional-memory extractive controller (effort responds to filtered deficit after delay) with Hopf cubic + even-pairs algebra (A_E B_N − A_N B_E ≡ 0) | large delayed predator-prey-harvesting literature (maturation/age-selective/threshold harvesting delays — e.g., Zhang 2013 Nonlinear Dyn; 2016/2017/2025 delay-harvesting papers). None put the DELAY IN THE GOVERNANCE CONTROLLER (filtered-signal effort law) with the protective-vs-mobilising sign split | **NOVEL-CORE** (controller-as-delayed-object; must be positioned explicitly against ecological-delay harvesting models) | Zhang 2013; representative 2025 delay-harvesting paper; Gao & Zhang 2022; Khiyar et al. 2026 (already cited) |
| Sign separation: C_Z > 0 mobilising → Hopf pair; C_Z < 0 protective → no-Hopf (Descartes + Routh–Hurwitz, loop gain < 1) | not found in delayed-harvesting literature | **NOVEL-CORE** (elementary but specific; the no-Hopf theorem is the headline) | — |
| Interval-certified Hopf crossings (interval-Newton, outward-rounded) | **Church & Lessard 2022** (Physica D 429:133072 — "Rigorous verification of Hopf bifurcations in FDEs… to the best of our knowledge, this has never been achieved before"); Church & Queirolo 2024 (JDDE 36:3385–3439, BiValVe); van den Berg & Lessard 2018; Beretka & Vas 2020 (cited) | **ENGAGE** — the certified numbers are an APPLICATION of interval-Newton; the full-rigor precedent exists. The paper's certified-tier claim must be re-scoped against Church–Lessard | Church & Lessard 2022; Church & Queirolo 2024; van den Berg & Lessard 2018 |
| Sampled monodromy: annual review unstable; "the control is the review interval" (NS at 47.5 yr); T_r = 2.306 Euler-factor crossing is NOT a Hopf | Åström & Wittenmark 1997 (cited); Nešić & Teel 2004 (cited); no ecological-governance precedent found | **NOVEL-CORE** (the two review-map operator discipline) | — |

## Paper 5 (sampled governance / empirical identification)

| Claim | Closest literature | Verdict | Binding citations |
|---|---|---|---|
| 42-stock Lomb–Scargle spectral null with FDR | fisheries spectral tradition: "Is the Russell Cycle a true cycle?" (ICES JMS 73:227, 2015 — skeptical-null precedent); SSA/wavelet catch analyses (ICES JMS 73:2552, 2016); ENSO-linked catch periodicities | **ENGAGE** — method routine; the paper's contribution is the architecture-substitution framing + null discipline, not the periodogram | Russell-Cycle paper 2015; ICES JMS 2016 |
| Two review-map operators (det(M−e^{iθ}I)=0 discipline); hold-map NS at 47.54 yr | no direct precedent found | **NOVEL-CORE** | — |
| Phase-line obstruction (scalar autonomous ODE cannot cross equilibria) | elementary ODE fact (textbook) | **CITE** (one-line proof fine) | textbook |
| Falsification programme designs | Costantino et al. 1995; Moxnes 1998; Punt & Donovan 2007 (cited); MSE literature | **ENGAGE** (designs are contributions as preregistration targets) | as listed |

## E papers (Wave E)

| Claim | Closest literature | Verdict | Binding citations |
|---|---|---|---|
| E1: preregistered scored ladder on northern cod; persistence beats surplus-production ladder (negative certificate) | live northern-cod surplus-production literature: "Northern cod comeback: 10 years after" (CJFFAS 2025 — surplus/net production reconstructions 1983–2023, two models); sGSL cod LRP under time-varying productivity (2026); JABBA Bayesian SP models (Winker et al. 2018); Shelton & Healey 1999 (cited) | **NOVEL-CORE as design** (scored ladder + negative certificate on 2J3KL found nowhere); must engage the 2025 comeback paper's surplus-production reconstructions | Rose/Walters-model 2025 paper; Winker et al. 2018; Shelton & Healey 1999 |
| E2: viability-kernel intervention-selection test on cod | Béné–Doyen–Gabay 2001 (Ecol. Econ. 36:385–396 — viability for a fishery); Doyen et al. 2012 (stochastic viability EBFM); Martinet et al. 2007 (viable recovery paths); Krawczyk & Pharo 2013 §4.1 (Schaefer + profitability kernel) | **ENGAGE** — the method is the canon's; the contribution is the scored retention rule + expansive-map obstruction (F′>1 empties certified kernels by expansion, not defect) — that failure mode is unclaimed | Béné–Doyen–Gabay 2001; Doyen et al. 2012; Martinet et al. 2007; Krawczyk & Pharo 2013 |
| E4: viability kernels on Edwards Aquifer; reactive rules retained at matched protection | Edwards literature = MODFLOW/GAM modeling (TWDB GAMs; Scanlon et al. 2001/2003; Hutchison & Hill 2011); EAA critical-period management + HCP (National Academies 2015 review); NO viability-kernel application found | **NOVEL-CORE for this system** (approach unclaimed on this aquifer); must engage the GAM/CPM baseline | Scanlon et al. 2003; Hutchison & Hill 2011; HCP/NAS 2015 |
| E3: model ablation with persistence benchmark on J-17 | groundwater ML-benchmark literature: GEMS-GER 2026 (first ML benchmark dataset, benchmark model outputs, ESSD 18:77); karst ML benchmarking (Water 18:939, 2026); Daliakopoulos 2005, Adamowski & Chan 2011 (cited in glm) | **ENGAGE** — benchmark culture exists (ML-focused); the ablation-with-preregistered-retention design and the h=5 climatology-wins result are the contribution | GEMS-GER 2026; Water 2026 karst benchmark; Daliakopoulos 2005 |

## Sweep summary

- **No prior work found for (NOVEL-CORE):** P2 epistemic-obstruction calculus (vs Veliov's sufficiency); P1's proved quantifier-commutativity separation; P4's governance-controller delay channel + sign-separation no-Hopf + review-interval-as-control; P5's two review-map operators; E1's scored-ladder negative certificate; E4's viability application to the Edwards system; E2's expansive-map obstruction failure mode.
- **Must be ENGAGED, not presented as new:** P2's exit certificate (barrier certificates incl. NECESSITY results — Prajna & Rantzer 2005); P2/P1's noncompensation theme (Martinez-Alier–Munda–O'Neill 1998; Martinet 2011; Doyen & Gajardo 2020 — maximin = maximal viability); P4's interval-certified crossings (Church & Lessard 2022 — full rigor exists); P5's spectral screen (Russell-Cycle skepticism tradition); P3's reserve-life critique (2024 phosphorus review); E3's benchmark framing (GEMS-GER).
- **CITE instead of restating:** the viability calculus, conservation/nonnegativity, small-gain delay, first-passage laws, phase-line obstruction.
- **Flags for the writing phase:** (1) P4's "certified tier" language must be re-scoped to "interval-Newton enclosures of the local spectrum" with Church–Lessard cited as the full-rigor method; (2) P1's separation theorem needs one residual check against Dasgupta–Mäler 2000 / Asheim 1994 before the claim is finalized; (3) E1 must engage the 2025 northern-cod comeback paper's surplus-production reconstructions in its discussion.

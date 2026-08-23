# Article 011 Evaluation and Verification

## Bibliographic identity

**Source file:** `uploads/paper3_empirical.txt`  
**Title:** *Periodic Review and Resource Governance: Sampled-Data Models, Spectral Screens, and Case Evidence*  
**Format:** LaTeX analytical/computational/empirical article  
**Length:** approximately 4,706 words, 277 lines  
**Formal content:** one proved forward-invariance proposition, one conditional rapid-review consistency remark, sampled-data model, exploratory simulation summaries, spectral screen, power analysis, field-case search, prospective MSE design  
**Evaluation status:** evaluated; integration and empirical claims on hold pending computational/data record

## Executive assessment

The article makes several important and largely correct distinctions:

- continuous action delay versus periodic review and sample-and-hold control;
- observation, assessment, review, decision, deployment, ecological response, and memory times;
- extractive versus protective controller signs;
- review-time safety versus inter-sample behavior;
- trajectory-classified oscillation versus multiplier-verified bifurcation;
- fixed-parameter bifurcation versus rate-induced tipping;
- spectral null evidence versus causal policy evidence;
- retrospective case screening versus prospective closed-loop MSE.

The forward-invariance proposition is correct after minor consistency fixes. The finite-horizon rapid-review statement is credible under its stated smoothness, compact-enclosure, exact-assessment, inactive-projection, and no-queue assumptions and aligns with Article 002’s proved sample-and-hold theorem.

None of the reported simulation bands, spectral results, power estimates, or case calculations can be independently verified from the submitted file. The required delayed-recruitment equations, parameter vectors, code, histories, eligibility table, processed RAM data, spectral routines, power simulations, case-screening table, and shared bibliography were not attached. The article itself acknowledges most of these gaps and appropriately labels the outputs exploratory.

This article is a stronger candidate for a genuinely separate empirical/computational companion than the short domain templates, because it asks a distinct question and reports model, spectral, power, and case-search results. Under the minimum-paper rule, separate publication becomes merited only after full reproducibility and a coherent primary contribution are established. Until then it remains on integration hold.

---

## 1. Governance-time ontology

The distinction among

- \(T_{obs}\): observation interval;
- \(T_{assess}\): assessment interval;
- \(T_r\): command-review interval;
- \(\tau_{dec}\): decision lag;
- \(\tau_{dep}\): deployment lag;
- \(\tau_{eco}\): ecological response lag;
- \(\tau_m\): memory/filter timescale

is valid and should be preserved in the master temporal architecture.

The article correctly warns that stock and effort series usually identify only a combined closed-loop phase relation. Separating lag components requires dated observation releases, assessments, decisions, implementation records, exogenous excitation, or a structural-identifiability theorem.

Review opportunity and controller sign are independent. An annual protective rule and an annual extractive rule are not the same intervention.

---

## 2. Sampled-data model

The inter-review system is

\[
\dot N
=rN(1-N/K)-qE_nN,
\]

\[
\dot Z
=[\Phi(qE_nN-S(N))-Z]/\tau_m.
\]

The update is

\[
E_{n+1}^{cmd}
=
\Pi_{[0,E_{max}]}
\{E_n+T_rF_B(E_n,\widehat Z_n)\}.
\]

### 2.1 Required model conditions

- \(r,K,q,E_{max},\tau_m>0\);
- \(\Phi\ge0\) for the positivity theorem;
- assessment and update timing fixed as stated;
- initial histories/values and solution concept declared;
- projection and hold semantics explicit;
- units for \(Z,\Delta_{ref},Z_{ref},\eta,\delta_0\) declared.

### 2.2 Hold/interpolation inconsistency

The process equations use held \(E_n\), but the invariance proposition and proof allow a convex interpolation \(E(t)\) between commands. The proposition is valid for any measurable \(E(t)\in[0,E_{max}]\), but the displayed model is specifically zero-order hold. The text should either:

- keep the proposition specialized to held \(E_n\); or
- write the process equations using admissible \(E(t)\) and identify hold as one implementation.

### 2.3 Signal map

The shifted/floored softplus is nonnegative, as required. At \(s=0\), its value is \(\max\{0,\delta\}\), not zero unless \(\delta=0\). Any claim of exact zero-boundary behavior must therefore state the value of \(\delta\).

---

## 3. Forward-invariance proposition

### Verification

For \(N>0\),

\[
\dot N
=N[r(1-N/K)-qE(t)]
\]

preserves positivity. At \(N=0\), the vector field vanishes, so uniqueness preserves the zero solution.

For \(Z\), variation of constants gives

\[
Z(t)
=e^{-(t-t_n)/\tau_m}Z(t_n)
+
\frac1{\tau_m}
\int_{t_n}^{t}
e^{-(t-s)/\tau_m}
\Phi(\cdot)\,ds
\ge0
\]

when \(\tau_m>0\), \(Z(t_n)\ge0\), and \(\Phi\ge0\).

Projection keeps review commands in \([0,E_{max}]\); a convex interpolation also remains inside that interval.

The proposition is correct after adding \(\tau_m>0\) and resolving the hold/interpolation wording. It proves positivity and effort bounds, not boundedness of all dynamics, viability, or stability.

---

## 4. Rapid-review consistency

The claim of finite-horizon \(O(T_r)\) convergence to the continuous no-delay system is credible under the stated assumptions:

- common compact enclosure;
- smooth vector field with bounded derivatives;
- exact contemporaneous assessment;
- inactive projection;
- no deployment or decision queue;
- common initial state;
- exact inter-review flow plus explicit effort step.

It is not a stability theorem, not uniform in time, and not an equivalence between review period and DDE delay. Article 002 contains a complete theorem and proof and should be the canonical source.

---

## 5. Stability terminology

The article correctly defines local stability of a sampled fixed point through eigenvalues of the Poincaré map derivative inside the unit disk.

It correctly refuses to call trajectory-classified response bands Neimark–Sacker, flip, or other bifurcations without multiplier calculations.

It also correctly distinguishes:

- a sampled-data parameter bifurcation at fixed \(T_r\) varied across systems;
- rate-induced tipping requiring a time-varying/ramped parameter.

A complete boundary calculation needs flow/update order, information, lags, derivative construction, multiplier trajectories, crossing direction, nonlinear trajectories, and refinement.

---

## 6. Sampled-review simulation summaries

The delayed-recruitment variants SD-E-DR-AN, SD-E-DR-SP, SD-E-DR-CO, and SD-E-DR-SL are not fully registered in the source. Therefore the reported regions cannot be reproduced or attributed to the fully displayed SD-E-B3 model.

Unverified outputs include:

- anchovy-class responses near \(T_r\approx3\)–4 yr;
- sprat-class responses near \(T_r\approx6\)–12 yr;
- cod-class convergence over \([1,20]\) yr;
- slow-stock transition brackets near 30–50 yr;
- robustness under 30% assessment error;
- biomass and effort spectral peaks;
- continuous-delay response regions.

The article appropriately calls these finite-grid trajectory summaries. Before promotion to numerical propositions, provide:

- complete equations and state dimensions;
- all parameter vectors and units;
- signal/gate functions;
- initial histories;
- solver, step sizes, tolerances, and event handling;
- horizon and tail-classification rule;
- amplitude convention;
- parameter grids;
- convergence/refinement;
- machine-readable trajectories;
- independent rerun.

The statement that different variables of one stationary periodic orbit cannot have different fundamental periods is correct. Reported differing peaks may be harmonics, modulation, transients, or separate dynamics.

---

## 7. RAM spectral screen

The claimed 42-stock spectral null is not independently verifiable without:

- frozen stock IDs and annual-review eligibility rules;
- exact RAM release and extraction query;
- processed biomass and exploitation/effort series;
- missing-data handling;
- detrending rules;
- frequency grid and band definitions;
- AR(1) fitting and simulation method;
- multiplicity procedure and family definition;
- endpoint sensitivity analysis;
- code and outputs.

The interpretation is appropriately narrow: RAM does not identify controller sign, decision rules, or deployment queues. A null peak result cannot establish that annual review stabilizes governance.

Potential methodological concern: selection into the “annual-review” cohort must be based on dated institutional evidence and frozen before inspecting spectra to avoid outcome-dependent selection.

---

## 8. Power analysis

The reported power values cannot be checked without code, random seeds, signal normalization, noise model, significance rule, number of replications, and confidence intervals.

The qualitative conclusion is reasonable: long-period signals and short/noisy records can make the empirical null weakly informative. Power must be computed per stock or under a declared population model before interpreting the 42-stock screen.

Synthetic record lengths of 100–200 years exceed many empirical records, so those results cannot be transferred directly to the observed cohort.

---

## 9. Structured field-case search

The search protocol is conceptually strong, but the zero count is not reproducible without:

- candidate-universe list;
- screening dates and reviewers;
- inclusion/exclusion decisions;
- source documents;
- station/resource IDs;
- calculations and code;
- preregistered eligibility rules.

The article correctly states that stringent eligibility criteria prevent the zero count from functioning as independent disconfirmation.

Specific author calculations—\(R^2\), extraction averages, coefficients of variation, periods, cross-correlations, and lag estimates—require data and code. The missing exact ENSO product prevents reproduction of the anchoveta correlation.

---

## 10. Closed-loop MSE design

The proposed MSE structure is scientifically sound and one of the article’s strongest sections. It distinguishes:

- operating model;
- observation model;
- assessment model;
- decision rule;
- implementation model;
- performance metrics.

The factorial design

\[
T_r\times\tau_{dec}\times\tau_{dep}
\times\text{controller sign}
\times\text{assessment error}
\times\text{process model}
\]

is appropriate.

Additional requirements:

- preregister primary and secondary endpoints;
- define operating-model ensemble weights or scenario interpretation;
- estimate tail-risk uncertainty;
- use common random numbers only with documented pairing;
- report optimizer/assessment failures as outcomes;
- include distributional and implementation costs;
- avoid treating one fitted operating model as structural uncertainty.

A completed MSE could provide an independent and publication-worthy empirical/computational contribution.

---

## 11. Falsification criteria

The proposed criteria are directionally sound:

- lag predictions must match independently measured lags;
- phase ordering must match controller mechanism;
- sampled analysis can invalidate continuous-delay transfer;
- protective-controller dominance blocks anti-regulation conclusions;
- low-power field nulls cannot adjudicate the mechanism.

They require precise estimators, uncertainty, effect sizes, and rejection rules. “Weakens” and “rejected for that case” should be tied to preregistered statistical or model-comparison criteria.

---

## 12. Relationship to other programme sources

### Article 002

Provides the canonical typed architecture, finite-clopen/tube-safe kernels, RFDE/hybrid subclasses, and proved sample-and-hold comparison.

### Article 003

Provides the institutional-feedback stress-test scope, policy-sign distinctions, nonlinear safety relevance, and numerical standards.

### Article 010

Provides the ten-state admissibility audit and status-qualified historical reproduction targets.

### Article 001

Provides delay, viability, observer, institutional, stochastic, and resource-system results.

The current article should not duplicate those architectural sections. Its independent contribution, if completed, is the sampled-governance computational/empirical test and MSE.

---

## 13. Publication assessment

Unlike the short domain templates, Article 011 could merit a separate empirical/computational companion because it addresses a distinct research question and reports simulations, a spectral screen, power analysis, field-case search, and prospective MSE.

It does not yet meet that threshold because the computational and empirical records are incomplete. Two publication paths remain:

1. **If fully reproduced and registered:** a distinct empirical/computational paper may be merited.
2. **If reconstruction fails or results remain exploratory:** preserve the governance-time ontology, MSE design, and negative evidentiary lessons in the flagship or supplement.

---

## 14. Verification verdict

### Verified

- governance-time distinctions;
- forward-invariance proposition after minor conditions;
- finite-horizon rapid-review interpretation under stated assumptions;
- sampled-bifurcation versus rate-induced-tipping terminology;
- narrow interpretation of spectral nulls;
- closed-loop MSE architecture;
- falsification logic at a conceptual level.

### Valid but unverified from supplied files

- sampled-review response regions;
- continuous-delay comparison regions;
- assessment-error robustness;
- 42-stock spectral null;
- power values;
- field-case calculations;
- zero eligible-case count.

### Required corrections

- hold/interpolation consistency;
- \(\tau_m>0\) and parameter units;
- signal-map boundary interpretation;
- complete model registration;
- complete data/code/provenance;
- preregistered cohort and statistical procedures;
- explicit primary endpoints and uncertainty for MSE.

### Required status

**Integration hold — promising empirical/computational companion candidate, contingent on complete reproducibility and validation.**

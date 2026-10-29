# ECOMOD c10 — hard-bound decision and empirical-foundation verification

**Date:** 2026-10-28  
**Status:** Read-only verification of the proposed revision rationale. No ECOMOD source, audit file, checksum, or repository ref was changed in this pass.

## Verdict

The proposed position is sound and internally consistent:

- For the present revision, treat \(q_{\max}=1\) as an **imposed admissibility bound** on an uncalibrated, model-defined quality index—not an estimated ecological carrying capacity.
- Specify the boundary projection explicitly, so the written model matches the disclosed bound-enforcing numerical method.
- Do not transfer a characteristic-root stability result for the unconstrained DDE to the projected system.
- Treat the identical baseline \(\tau_g=20\) and 40 yr quality paths as a saturation-induced degeneracy, not evidence of general delay robustness.
- External measurement frameworks and recovery datasets make an ecosystem-specific empirical model feasible in principle; they do not identify ECOMOD's current \(q\), regeneration law, supply mapping, or parameter values.

## Mathematical checks

### Projected delayed-quality law

Write \(K_q=[0,q_{\max}]\), \(F_g(t)=G_c(q(t-\tau_g))\), and specify

\[
\dot q(t)=\Pi_{T_{K_q}(q(t))}F_g(t),\qquad
G_c(x)=\rho_c x\left(1-\frac{x}{q_{\max}}\right),
\]

where \(T_{K_q}(q)\) is the tangent cone and \(\Pi\) denotes projection onto it. State \(\rho_c>0\), \(q_{\max}>0\), and an admissible continuous history \(\phi\in C([ -\tau_g,0],[0,q_{\max}])\), with \(q(s)=\phi(s)\). Interpret the equation for an absolutely continuous solution, almost everywhere.

For admissible delayed values, \(F_g(t)\ge 0\). Thus the projected law agrees with the raw delayed RHS below the ceiling and sets \(\dot q=0\) at \(q=q_{\max}\); at \(q=0\), the RHS is nonnegative. This preserves the interval. The zero history remains identically zero, so \(q_{\max}\) is not a global attractor over every admissible history. Any stronger convergence claim should state its nonzero-history assumptions and be proved for this projected law.

For the disclosed baseline constant history \(q=0.9\), with \(\rho_c=0.08\), \(q_{\max}=1\), and \(\tau_g\ge 125/9\) yr, the interior slope is

\[
\dot q=0.08(0.9)(0.1)=0.0072\;\mathrm{yr}^{-1}.
\]

The projected trajectory reaches 1 at \(125/9\approx13.8889\) yr and remains there. Consequently, the entire baseline quality paths for \(\tau_g=20\) and 40 yr are identical. This exact degeneracy makes that pair uninformative about broader delay robustness.

The candidate smooth alternative \(\dot q=\rho_c q(t-\tau_g)(1-q(t)/q_{\max})\) is materially different, not a transcription correction. With the same baseline constant history and parameters, for \(0\le t\le20\),

\[
q(t)=1-0.1e^{-0.072t},\qquad q(20)=0.976307\ldots\approx0.9763.
\]

That calculation is correct. The alternative remains an unselected, unvalidated hypothesis and need not appear as a displayed equation in the present manuscript.

### Numerical implementation qualification

The C10 TeX discloses explicit Euler integration and enforcement of \(q\in[0,q_{\max}]\), but the exact historical C10 simulation code has not been verified against its archived outputs. A separate local working solver, `/home/user/ecomod_v45/work/twoland_fixed.py`, uses linear interpolation for delayed states and clips the Euler-updated quality into the interval. That is consistent with a projected-Euler implementation, but its exact provenance for the C10 figures/tables is not established by the pinned C10 source package.

The revision should state the actual update rule, interpolation, and timestep, then compare the discrete implementation against the continuous projected specification under step refinement. A finite-step clip and the continuous projected law are not identical at the boundary-crossing step; convergence should be demonstrated rather than assumed.

## Evidence review

### Measurement frameworks

The official SEEA Ecosystem Accounting framework describes a route from selecting measured ecosystem-condition variables, through defining reference levels and rescaling indicators, to optional aggregation into a condition index. That is a credible **measurement-design foundation**, not evidence for ECOMOD's state equation or for a hard biological ceiling. The official framework is the stronger primary citation; the Javorsek presentation is a useful explanatory source. [5](https://seea.un.org/sites/default/files/files/documents/2021/Oct/seea_ea_white_cover_final.pdf) [1](https://seea.un.org/sites/default/files/javorsek_ecosystem_condition_accounts.pdf)

A European forest-condition study operationalized a 0–1 composite index for 44 forest types, using primary or protected forests as references and comparing assessments for 2000 and 2018. This demonstrates that a reference-based condition index can be constructed and applied; it does not establish a one-dimensional recovery law, a discrete delay, or ECOMOD's supply linkage. The two assessment dates should not be described as dense within-site recovery trajectories. [12](https://www.nature.com/articles/s41467-023-39434-0)

### Recovery datasets

The Dryad 2ndFOR archive describes estimated aboveground biomass for 1,334 secondary-forest plots at different times since abandonment, assembled from chronosequence studies. The associated paper reports a broader dataset of about 1,468 plots across 45 sites; plot-level data for 41 sites were archived and four sites were available by request. This is a concrete basis for a **forest-specific** recovery analysis, but chronosequence age-response data do not by themselves identify a discrete feedback delay rather than a slow initial response, establishment lag, or site differences. A site-specific old-growth reference also is not directly available for every site in the study. [1](https://datadryad.org/dataset/doi:10.5061/dryad.82vr4) [4](https://www.nature.com/articles/nature16512) [7](https://ibifbolivia.org.bo/wp-content/uploads/2022/09/2016-Poorter-Nature_BiomassResilience_2016.pdf)

A proposed \(q(t)=\text{AGB}(t)/\text{reference AGB}\) would be an **illustrative operationalization**, not a validated mapping for the current generic ECOMOD index. Above-reference observations can exceed 1 unless an explicit rescaling or truncation convention is imposed. The stock (biomass), its growth, and the service/supply flow should not be conflated.

### Fisheries records

RAM Legacy v4.66 is a publicly archived stock-assessment database; its documentation identifies time-series for total and spawning-stock biomass, recruitment, catch/landings, and fishing mortality. The JRC description of RAM Legacy notes that biomass, recruitment, and fishing-mortality series are generally outputs of population-dynamics assessment models rather than raw observations, with catch/landings as exceptions. These records could support a stock-specific analysis with assessment uncertainty acknowledged; they do not calibrate a generic terrestrial quality index. [1](https://zenodo.org/records/14043031) [1](https://docs.ropensci.org/ramlegacy/articles/tables_description.html) [2](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC112485/ram_med_jrc_technical_report_final_1.pdf)

## Recommended manuscript framing

The proposed wording is suitable with only light tightening:

> We interpret \(q\) as a normalized, model-defined index of ecological condition on capital land. It is not presently identified with a measured ecological variable or calibrated against observations. Its dynamics encode a hypothesized regeneration process, and \(q_{\max}=1\) is an imposed admissibility bound rather than an estimated ecological threshold.

> We impose the state constraint by projecting the delayed regeneration vector field onto the tangent cone of \([0,q_{\max}]\). This constrained specification formalizes the disclosed numerical bound enforcement; it is not an empirically identified biological saturation mechanism. Its boundary dynamics are distinct from the stability properties of the unconstrained delay equation.

For future work, a concise statement is preferable to presenting an unsupported alternative equation: empirical condition-accounting frameworks and forest or stock-recovery datasets offer routes to define ecosystem-specific observations, but model selection would still need to connect the chosen observation to recovery dynamics and to the modeled supply term. The current \(\rho_c\) and \(\tau_g\) remain illustrative scenario parameters, not estimates from those records.

## Editorial / provenance checks before insertion

- The supplied citation markup is malformed (nested Markdown links and repeated numeric labels). Convert it to the manuscript's citation-key format and add complete bibliography entries only for sources actually cited.
- Cite the official SEEA manual as the primary standard; treat the Javorsek PDF as a presentation, not the governing standard.
- Keep any new forest/fisheries references in a future-work or measurement paragraph. Do not suggest they validate the present ECOMOD mechanism or parameters.
- This verification did not edit C10, its pins, c8/c9, `main`, checksums, or DOI deposits. The separate local-draft target remains distinct from those preserved outputs.

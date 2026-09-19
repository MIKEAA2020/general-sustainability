"""Second pass: restore the applied records, the Section 9 statements the compression dropped,
the quantitative content of the Section 10 reasons, and the back matter."""
import re
P='revision/v3/paper3_v3.md'; t=open(P,encoding='utf-8').read(); ok,bad=0,[]
def before(anchor,text):
    global t,ok
    if t.count(anchor)!=1: bad.append(f"[{t.count(anchor)}] {anchor[:60]!r}"); return
    t=t.replace(anchor,text+anchor,1); ok+=1
def rep(old,new):
    global t,ok
    if t.count(old)!=1: bad.append(f"[{t.count(old)}] {old[:60]!r}"); return
    t=t.replace(old,new,1); ok+=1

# abstract / intro fisheries wording (restore the log margin)
rep("A fisheries removals-only pressure scale divides a biomass margin by a removal rate.",
    "A fisheries removals-only pressure scale divides a log biomass margin by a fishing mortality.")
rep("A fisheries pressure indicator divides a biomass margin by a removal rate",
    "A fisheries pressure indicator divides a log biomass margin by a fishing mortality")

# Section 8.1 — applied record and identifiability boundary
before("### 8.2 The phosphate reserve-life ratio",
"""For the four-basin record on the reported April 2002 – September 2023 window: Indo-Gangetic \\(-49.7\\) cm/yr with index \\(\\approx2.7\\) yr; North China Plain \\(-18.6\\) with \\(\\approx7.9\\); Central Valley \\(-16.1\\) with \\(\\approx9.5\\); La Mancha \\(-3.2\\) with \\(\\approx21.4\\); High Plains \\(-7.9\\) with the series already at its window minimum, index \\(0.0\\); global mean \\(-0.4\\) with \\(\\approx47.5\\). The denominator carries the same extended-real convention as Definition 4: at \\(\\hat a'\\ge0\\) the index is \\(+\\infty\\).

The classification is stated at the product's own status. A re-labelling of an anomaly-based year cannot produce an exhaustion forecast, because the absolute stock-to-barrier distance is not identifiable from an anomaly series: adding a constant to the whole series and to the reference leaves every observation unchanged, so neither a tighter anomaly record nor a narrower posterior supplies the missing absolute anchor. A physical \\(H_A^{\\text{loc}}\\) requires an independent anchor — aquifer geometry or saturated thickness together with storage parameters, which is the registered requirement of the groundwater template — and not an anomaly series alone. The product of record is G3P v1.12 (Güntner et al., 2024).

""")
# Section 8.2 — phosphate arithmetic and vintage discipline
before("### 8.3 The fisheries removals-only pressure time",
"""At constant current production \\(C_G\\), \\(\\mathcal T_{\\mathrm{reserve}}=G_{\\mathrm{reserve}}/C_G\\). At approximately 74,000,000 kt of world reserves and 240,000 kt/yr of production (U.S. Geological Survey, 2026) this is approximately **309 years**, with the per-country figures China 3,400,000 kt and \\(\\approx28\\) yr, United States 1,000,000 kt and \\(\\approx45\\) yr, Jordan 820,000 kt and \\(\\approx62\\) yr, Morocco 50,000,000 kt and \\(\\approx1{,}250\\) yr. The implied-production column reproduces the production figure each horizon assumes, production = reserves/horizon, and thereby exposes the source arithmetic; each row reproduces the recorded reserve-life ratio.

The reserves/resources split is part of the classification. A resource-threshold calculation \\(\\mathcal T_{\\mathrm{resource},10\\%}=(1-\\varepsilon)G_{\\mathrm{resource}}/C_G\\) with \\(\\varepsilon=0.10\\) the share left unextracted answers a different question and must not share a column with the reserve-life ratio without the convention label: at resources above 300,000,000 kt the same production gives a horizon above **1,125 years**, more than three times the reserve-based figure. The label is printed with the row. That the reserve classification is economic rather than physical is visible in the record itself: United States reserves have remained near 1,000,000 kt while cumulative production since 1996 is of order 600,000 kt.

The vintage is pinned once. The single pinned source of record is *Mineral Commodity Summaries* 2026, and every figure quoted at pin status is that vintage's: the 2025 world-production column of \\(\\approx250{,}000\\) kt and Australia's reserves of 120,000 kt (JORC-compliant). The remaining country rows above are at their recorded pre-2026 vintage and are retained rather than blanked, as worked instances of the construction; Australia's 5,800,000 kt with \\(\\approx2{,}088\\) yr is one of them. Completing the re-pin row by row with the pinned vintage's per-country reserve figures is the registered open data action, and no classification stated in this section depends on it.

""")
# Section 8.4 (end of §8) — cohort record, scope discipline, non-example
before("\n---\n\n## 9. First-Passage Semantics on Declared Surrogates",
"""### 8.4 The fisheries cohort record, and the scope of the applied tables

The reported cohort figure is the archived-depletion-horizon (ADH) pure-decay proxy
\\[
\\mathrm{ADH}=F^{-1}\\log\\!\\bigl(\\mathrm{SSB}_{\\mathrm{now}}/(0.2\\max\\mathrm{SSB})\\bigr)
\\]
under current fishing mortality \\(F\\), with \\(\\mathrm{ADH}=0\\) entered for the **eight** stocks already at or below the reference, per the zero convention of the source table's caption, which the median includes: median **\\(\\approx1.8\\) yr across the 43** assessed stocks with finite SSB and \\(F\\) series, from the archived pull. Two disclosures accompany the value. The archived 43-stock cohort is reproduced by **neither** public RAM Legacy release, and the record of that retraction is the version-sensitivity analysis, executed row by row against the formula: all 43 rows reproduce \\(\\mathrm{ADH}=\\max(0,F^{-1}\\log(\\mathrm{SSB}/\\mathcal B_{\\mathrm{lim}}))\\) with \\(\\mathcal B_{\\mathrm{lim}}=0.2\\max\\mathrm{SSB}\\). On the public releases the same protocol qualifies **415** stocks (v4.44, median **2.57** yr) and **454** stocks (v4.66, median **3.39** yr), neither reproducing the archived cohort, whose stock list and extract-time series state differ from both releases.

The cohort is a selected class, not a random sample: all 43 stocks are small pelagics (18 anchovy, 20 herring, 4 sprat, 1 sardine), the fast-maturing class the companion review screen selects by its annual-review eligibility criterion, **42 of the 43** being annual-managed spectral-null stocks per the source caption. The \\(\\approx1.8\\) yr median is therefore a class-specific diagnostic for fast-maturing, annually managed pelagics, not a statistic of assessed fisheries in general. The qualifying positive sub-cohort (\\(F>0\\) and \\(\\mathrm{SSB}_{\\mathrm{now}}>\\mathcal B_{\\mathrm{lim}}\\); 35 stocks) has median **2.9 yr**, both medians coming from the archived pull; the long-lived groups carry the upper end of the broad cohort (elasmobranchs 11.5, sebastids 9.0, pleuronectids 6.0 yr), and only **2%** of random 43-stock draws from the 454-stock broad cohort have medians at or below the class cohort's 1.79 yr. Every cohort statistic is pinned to the archived pull (Ricard et al., 2012), whose date is archived with the analysis, and no cohort statistic is quoted from a different database version. The value is reported with its cohort conditions and is not promoted to a forecast.

**Scope of the applied records.** None of the numbers in Sections 8.1–8.4 is a computed instance of any model's first-hitting time: the groundwater column is a trend-to-window-minimum extrapolation, the phosphate column a reserve-life ratio, and the fisheries column a pure-decay proxy with recruitment omitted. They are descriptive, component-resolved diagnostics reported beside the pool each draws on, not dynamical predictions, and the classification of each row does not depend on the magnitudes.

**Non-example 1 — a boundary of aggregation, not a score of the framework.** The equal-weight inverse-horizon score of the four basins still above their window minimum and world phosphate reserves,
\\[
\\Sigma_{\\mathrm{reserves}}\\approx\\tfrac15\\left(\\tfrac1{2.7}+\\tfrac1{7.9}+\\tfrac1{9.5}+\\tfrac1{21.4}+\\tfrac1{309}\\right)\\approx0.130\\ \\mathrm{yr}^{-1},
\\]
is a ranking device, not a componentwise certificate: it mixes basins and reserves, incommensurable objects under the typing of Section 2.1, and it is retained only to mark the boundary of legitimate aggregation — a positive aggregate coexisting with componentwise deficits by construction, admissible as communication and inadmissible as certification. No reciprocal of it is reported as a horizon.

""")
# Corollary 19 and the boundary facts
before("### 9.4 Record-relative barrier discipline",
"""**Corollary 19 (Zero-noise limit and median).** As \\(\\varsigma\\to0^+\\), \\(T_{\\mathrm{GW}}\\to\\mathcal H^{\\mathrm{win}}_{\\mathrm{GW}}\\) in probability, and at \\(\\varsigma=0\\) the deterministic trajectory reaches the barrier exactly there. For every finite \\(\\varsigma>0\\) the inverse-Gaussian median \\(m\\) satisfies \\(m<\\nu=\\mathcal H^{\\mathrm{win}}_{\\mathrm{GW}}\\), with
\\[
F_{\\mathcal T}(\\nu)=\\tfrac12+e^{2\\lambda/\\nu}\\Phi\\bigl(-2\\sqrt{\\lambda/\\nu}\\bigr)>\\tfrac12 .
\\]
The variance scales as \\(\\varsigma^2\\), and the standard deviation and small-noise quantile widths as \\(\\varsigma\\). The median below the mean is the inverse Gaussian's right skew toward short passage times; the inequality must not be inverted. *Proof.* Evaluate \\(F_{\\mathcal T}(t)=\\Phi(\\sqrt{\\lambda/t}\\,(t/\\nu-1))+e^{2\\lambda/\\nu}\\Phi(-\\sqrt{\\lambda/t}\\,(t/\\nu+1))\\) at \\(t=\\nu\\): the first term is \\(\\Phi(0)=1/2\\) and the second is strictly positive for finite \\(\\lambda\\). \\(\\square\\)

These are conditional distributional statements about the surrogate. They are not corrections to the tabled years, and they do not show that physical water mass is depleted faster.

""")
before("### 9.5 Geometric-Brownian fisheries first passage",
"""Three boundary facts are part of the discipline. **Already at minimum.** If \\(A_0=A_{\\text{win}}^{\\min}\\) the stopping-time convention gives \\(T_{\\mathrm{GW}}=0\\) deterministically for every \\(\\varsigma\\); the inverse-Gaussian family has a degenerate boundary limit concentrated at zero, and \\(\\mathrm{IG}(0,0)\\) is not an ordinary inverse-Gaussian distribution. Zero cells report zero relative to the selected observational barrier — not zero physical uncertainty, and no confirmation of collapse. **Independent physical thresholds.** If a threshold \\(A^{\\sharp}<A_{\\text{win}}^{\\min}\\) is specified independently of the record, the same constant-drift surrogate gives \\(\\mathbb E[\\mathcal T^{\\sharp}]=(A_0-A^{\\sharp})/|\\mu|\\), longer than the record-relative proxy because the barrier is lower; this is a statement within the surrogate, not a general lower-bound theorem for the physical ledger, whose drift and state coupling may differ. **Classification.** The load-bearing content is the interpretation boundary itself: a record-relative barrier makes the passage time a property of the observation window, and no reading of the tabled numbers escapes that qualification.

""")
# Stratonovich clarification inside §9.5's region
before("### 9.6 Scope of the first-passage section",
"""Under the Stratonovich convention the log-drift would be \\(-h\\), and the deterministic limit would match the pure-decay horizon \\(h=F\\) exactly: the \\(\\varsigma^2/2\\) shortening is the Itô choice, not a property of the physical process.

""")
# seven non-claims + uncertainty, appended to §9
before("\n---\n\n## 10. Interface with Institutional Delay Dynamics",
"""### 9.7 Non-claims of the first-passage section

Seven statements bound the section and are part of its content. **(1)** The Brownian and geometric-Brownian processes are not stochastic completions of the ledger and do not conserve its mass compartments. **(2)** No theorem relates \\(\\hat\\mu\\) to \\(-\\dot A\\) of the reduced systems, to the finite-donor primitive system, or to the institutional delay equations. **(3)** The model hitting time \\(T_A\\) of Definition 5 is not shown to be inverse Gaussian; it would be inverse Gaussian only if the active-pool residual were Brownian with constant drift, which the coupled balance (2a)–(2d) does not supply, and the tabled groundwater numbers inherit inverse-Gaussian means from the surrogate of Section 9.2 and from nothing else. **(4)** The historical groundwater minimum is not an independently identified physical failure barrier. **(5)** A shorter surrogate median or Itô mean is not evidence of faster physical depletion. **(6)** The gross turnover horizon \\(\\mathcal H^{\\mathrm{gross}}_A\\) of Definition 3 and its productivity-illusion reading — the misreading of a large gross-turnover horizon as evidence of slow net depletion, recorded in Section 6.1 — are not first-passage results and are not treated here. **(7)** The fisheries calculation is not a stage-structured fisheries model, and the phosphate calculation is not a geological-reserve model.

The inverse-Gaussian results condition on the drift, the barrier and the noise scale. In the groundwater application \\(\\hat\\mu\\) is estimated from a finite, potentially autocorrelated record and the barrier is selected from that same record; measurement error, serial dependence, seasonal forcing, spatial aggregation, trend breaks and common climatic drivers are separate uncertainties, and integrating any of them out yields a predictive mixture rather than a single inverse-Gaussian law. A residual scale estimated from the same window does not by itself identify process noise. No calibrated predictive distribution is claimed; the full uncertainty treatment belongs to an empirical identification study.

""")
# §10.1 clauses
before("### 10.2 The non-reduction boundary",
"""The memory–effort pair that enters the institutional block is the registered object of the companion delay-dynamics analysis (Author, D., et al., *in review*; its equation (1) and Section 2.4) and is not analysed in this article; the projection statement — the semiconjugacy condition \\(\\mathcal D_\\pi(\\xi)f(\\xi)=F(\\pi(\\xi))\\) on the history phase space — is made under that citation and is not re-proved here. The contract fixes more than the identity: the shared object includes the non-negative orthant and the sign pattern of harvest as an outflow from the living stock, and a companion model that routes the unsustainable portion of a flow into a different compartment changes the incidence and thereby leaves the interface. The reduced core's constitutive replacement \\(R(N,A)\\to rN(1-N/K)\\) is separately an approximation with its own finite-time scope (Theorem 1, Remark 2). Under the institutional-failure specialization the macroeconomic block, prices and demand do not appear in the six right-hand sides of (2a)–(2d) together with the memory and effort laws: the ecological–institutional subsystem is an exact closed projection for every parameter value, with no singular limit required.

""")
# quantitative content of the five reasons + ε_G + trichotomy
before("**Theorem (Non-reduction).**",
"""The five reasons have quantitative content on the registered parameterization. (1) The three targets are \\(A_{\\text{eq,intrinsic}}=50\\), the working active pool \\(A_{\\text{act},*}=397.87\\), and \\(A_{\\text{eq},W}=50+\\kappa_AK/\\omega_A=5{,}050\\): the two equilibria differ by a factor of eight and the two targets by two orders of magnitude. (2) At the working equilibrium the two \\(A_{\\text{act}}\\) vector fields, written at the same state \\((N,A_{\\text{act}},U)\\), differ by \\(\\omega_A(A_{\\text{eq},W}-A_{\\text{eq,intrinsic}}\\sigma)-\\gamma_UU=\\kappa_AK-\\gamma_UU\\) under the registered scale separation: approximately **0.535** stock units per year at the working point's quasi-rest detritus level, where \\(\\gamma_UU=\\mathcal T^*\\approx4.47\\), and \\(\\kappa_AK=5.000\\) stock units per year at \\(U=0\\) — an \\(O(1)\\) to \\(O(\\kappa_AK)\\) discrepancy, not a small residual; the difference is \\(U\\)-dependent because the working field omits the detritus return \\(\\gamma_UU\\) the closed field carries, and \\(\\mathcal B^*-R^*=\\mathcal T^*\\) is the working system's turnover balance, not the field difference. (3) The working point \\((N^*,A_{\\text{act},*})=(89.526,\\,397.87)\\) at \\(E^*\\approx2.090\\) requires continuing geological support — the flux \\(\\omega_A(A_{\\text{eq},W}-A_{\\text{act},*})=4.652133\\ldots\\) stock units per year, supplied every year by a donor the working system treats as a parameter — and at the same state the closed primitive donor flow is \\(e_{GA}-e_{AG}=\\omega_A(A_{\\text{eq,intrinsic}}-A_{\\text{act},*})\\approx-0.348\\): the donor gains in the closed ledger where the working completion has it losing 4.652, opposite signs rather than different magnitudes. The reverse check \\(qE^*N^*=0.001\\times2.090\\times89.526\\approx0.187\\) is consistent to the quoted digits, and these working-point figures are imported at the companion's registered precision. (4) The donor-draw diagnostic
\\[
\\varepsilon_G(T)=G_0^{-1}\\int_0^T\\bigl|e_{GA}-e_{AG}\\bigr|\\,dt
\\]
measures the derived-target completion, not trajectory tracking; no finite-time tracking correspondence between the completions holds. (5) Extraction on the closed ledger is \\(L^1\\) in time (Theorem 14), which is what forbids indefinite persistence of the working positive-flux rest.

The five reasons form a trichotomy: (1)–(3) are short-time obstructions, since the fields differ by \\(O(1)\\) at the working point and trajectories diverge on \\(O(1)\\) timescales; (5) is the long-time obstruction; (4) is neither, because the diagnostic does not measure tracking at any timescale.

""")
# frozen-donor corollary, long-time budget, then limitations
before("## 11. Conclusion",
"""The frozen-donor limit is a corollary of the structural clause (1). Rescaling \\(G=G_0g\\) with \\(g(0)=1\\) gives \\(\\dot g=-G_0^{-1}(e_{GA}-e_{AG})\\); the limit \\(G_0\\to\\infty\\) freezes \\(g\\) but does not restore the working completion's derived target, because the limiting recharge field still uses \\(A_{\\text{eq,intrinsic}}\\). The scaling is therefore not a regular perturbation of the working vector field, and local Hopf persistence of the working system under this primitive scaling is not claimed; a different derived-target completion would be required before such a statement could be formulated.

On the closed system with the donor \\(G(t)\\) included as a state, the dynamics are an autonomous retarded equation with a slow donor coordinate. The companion's \\(\\tau_+\\approx150\\) yr upper cycle is a frozen-donor object and can persist only as a transient on the finite donor budget, where the transient-duration statement is an order-and-budget bound and not an asymptotic estimate: under a sustained lower extraction flux \\(c>0\\) the duration is bounded above by \\(G_0/c\\), and the scale must name its flux. At the closed-block extraction rate \\(c=qE^*N^*\\approx0.187\\) stock units per year the budget bound is \\(G_0/c\\approx2\\times10^{6}\\) years; at the working completion's recharge flux \\(\\mathcal B^*\\approx4.652\\) the draw scale is \\(G_0/\\mathcal B^*\\approx8.6\\times10^{4}\\) years, the "tens of thousands of years" heuristic using the working flux (at \\(G_0/A_{\\text{act},*}=10^3\\)); both scales sit far above the institutional delays of the companion family. Whether the frozen-donor local Hopf structure persists as a slowly drifting transient in the closed donor system is an open slow-passage problem; the mass budget alone does not establish it.

### 10.3 Negative content and limitations

The negative and boundary results of this article are stated as results. The classifications of Section 8 are negative results: the anomaly index is not a stock ratio, the reserve-life ratio is not a forecast, the removals-only time is not a depletion diagnostic. The non-reduction boundary fixes a rejected mapping with five reasons. The empty-kernel mechanisms of the sink obstruction are structural. A violation of a declared barrier is a loss of safety; a data or certificate failure — a quarantined row, a retraction, a stale vintage — is a loss of assurance, and the two are not interchangeable.

**Limitations.** (i) The two-pool exact specialization of the groundwater template remains open; the admitted object is the one-pool affine approximation of Section 8.1, and no two-pool model is claimed as established. (ii) The phosphorus and groundwater records are registered template obligations with no constitutive content behind them. (iii) The first-passage propositions of Section 9 concern declared surrogates, not the ledger. (iv) The applied records of Section 8 are classified diagnostics at their stated evidentiary levels and are not calibrated early-warning systems or forecasts. (v) The non-reduction boundary of Section 10.2 is permanent, not a gap. (vi) The conditional hybrid balance of Theorem 15 stays conditional, with its jump-interpretation and yield-routing obligations open per application. (vii) The support-saturation limits of Theorem 1 and Remark 2 are local and finite-time; neither is a full-system reduction. (viii) No theorem in this article identifies the maintainability kernel \\(K_{\\mathrm{maint}}\\) of Section 6.3 with any family of the rest set of Theorem 13: whether the carrying-capacity rest lies in the kernel is a question about the declared barrier values and the admissible control class, and it is not answered here. (ix) The article asserts nothing empirical about any named resource system beyond the classifications of public data products stated at their source status.

""")
# §11 closing phrasing
rep("No nonnegative weighting certifies componentwise adequacy. Scalar summaries may rank and communicate. Certification requires the vector.",
"No nonnegative weighting certifies componentwise adequacy: the obstruction is compensation, not the scalar form as such. A scalar summary may rank and communicate; it certifies only if it is non-compensatory, such as the binding margin of the conjunctive criterion reported with the name of the component that binds. Certification requires that test.")
# References and back matter
rep("**Declaration of competing interest.** None.",
"""**Supplementary material.** The accompanying file carries the ten-state admissibility template and its three audited negative witnesses, the registered identification ladders of the phosphorus and groundwater templates, the split-assignment mechanism table, the statement inventory with the status of every statement in the main text, and the fisheries cohort record with the archived-pull verification and the executed broad-cohort comparison.

## References

Blomqvist, L., Barrett, J., Galletti, S., et al. (2013). Ecological footprint for all nations shows trends 2000–2008. *Sustainability Science*, 8(2), 217–228. doi:10.1007/s11625-013-0208-3
Brunner, P.H., Rechberger, H. (2004). *Practical Handbook of Material Flow Analysis*. CRC Press.
Chhikara, R.L., Folks, J.L. (1989). *Inverse Gaussian Distribution: Statistical Concepts and Applications*. Chapman and Hall.
Clark, C.W. (1990). *Mathematical Bioeconomics: The Optimal Management of Renewable Resources*. 2nd ed., Wiley.
Daly, H.E. (1990). Toward some operational principles of sustainable development. *Ecological Economics*, 2(1), 1–6.
Ekins, P., Dewhurst, S., et al. (2003). *Environmental Sustainability in the European Union: Indicators for National and Local Policy*. Routledge.
Eurostat (2001). *A Practical Guide to Creating National Material Flow Accounts*. Statistical Office of the European Communities.
Feinberg, M. (2019). Foundations of chemical reaction network structure theory. *Lecture Notes*.
Farina, L., Rinaldi, S. (2000). *Positive Linear Systems: Theory and Applications*. Wiley.
Fischer-Kowalski, M., Singh, S.J., Wetzinger, E. (2011). Society's metabolic metabolism and its biophysical scale. *Ecological Economics*, 70(12), 2331–2344.
Güntner, A., et al. (2024). G3P v1.12: Global Gravity-based Groundwater Product. GFZ Data Services. doi:10.5880/G3P.2024.001
Illakwahhi, I., Vegbi, S., Srivastava, R.K. (2024). Phosphate depletion misconstrued. *One Earth*, 7(8), 1513–1523. doi:10.1016/j.oneear.2024.06.016
Jacquez, J.A., Simon, C.P. (1993). Qualitative analysis of nonnegative compartmental systems. *Mathematical Biosciences*, 116(2), 193–216.
Lin, D., et al. (2018). Earth Overshoot Day. *Ecological Modelling*.
Martinez-Alier, J., Munda, G., O'Neill, J. (1998). Weak comparability of values as a foundation for ecological economics. *Ecological Economics*, 26(1), 27–38.
Meadows, D.H., et al. (1972). *The Limits to Growth*. Universe Books.
Munda, G., Nardo, M. (2009). *Indicators of Sustainable Development*. Routledge.
Neumayer, E. (2013). *Weak versus Strong Sustainability*. 3rd ed., Edward Elgar.
Øksendal, B. (2003). *Stochastic Differential Equations*. 6th ed., Springer.
Redner, S. (2001). *A Guide to First-Passage Processes*. Cambridge University Press.
Ricard, D., et al. (2012). RAM Legacy Stock Assessment Database v4.44.
Tapley, B.D., et al. (2004). GRACE measurements of time-variable gravity. *Geophysical Research Letters*, 31, L09307. doi:10.1029/2004GL019492
Tilton, J.E. (2003). On borrowed time? *Mineral Economics*, 17(3–4).
Tilton, J.E., Lagos, G. (2007). *Powering Growth*. Earthscan.
U.S. Geological Survey (2026). *Mineral Commodity Summaries 2026*.
Wackernagel, M., Beyers, C., et al. (2019). Ecological Footprint and Earth Overshoot Day. *Ecological Indicators*, 107, 105621.

**Declaration of competing interest.** None.""")
open(P,'w',encoding='utf-8').write(t)
print(f"applied {ok}; skipped {len(bad)}")
for m in bad: print("  SKIP",m)
print("chars:",len(t))

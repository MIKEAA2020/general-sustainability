# Supplementary material, v9 candidate — sections to append to `paper3_supplementary_v8.md`

This file does the merge that `revision/v5/README_v5.md` §4.3 left to the author, and adds the two tables that
the review cycle kept deferring. Nothing here overwrites the existing supplementary: the sections are numbered as
a continuation of it (`S7`–`S10`) and the mapping below says where each piece of `supplementary_v5_additions.md`
lands. No cell needs the author: the two that once did were closed from the repository at
`refs/tags/edwards-framework-e1` and from the deposit server (see S11's fisheries row and S12's note), and the
main text was updated to match in v38.

## 0. Merge map

| source | lands in | note |
|---|---|---|
| `supplementary_v5_additions.md` S-A (proof obligations of the certification state) | **S7**, re-typed | its `Typed` row cited "§2.1, §2.2 incidence discipline"; that is now Definition 47 |
| S-B (the three linear programmes) | **S8** | unchanged |
| S-C (worked ledger exhibit) | **S9** | unchanged |
| S-D (promotion-rule table) | **S10** | unchanged |
| S-E (reproduction) | fold into the existing S5 reproduction paragraph, or keep as an appendix note | the code archive is `revision/v5/code/` |
| S-F (statement inventory at v5) | **replaces the existing S4 inventory rows for labels 21–47** | and reconciles with the existing S6 naming-offset table |
| this file, §2 | new **S11** per-parameter identifiability status | requested in the review cycle; the article carries the rule in §3.1, the table is here |
| this file, §3 | new **S12** material-and-energy-value correspondence | keeps the position out of the article's claim list while making it checkable |

## 1. S7 correction

| predicate | statement, in one line | article locus | witness | fails when |
|---|---|---|---|---|
| `Typed` | every compartment carries a declared type and unit, and no column of $S_{\mathcal T}$ is both a transfer and a conversion | **Definition 47**, Proposition 42 | the declaration $(\mathsf{Ty}, \mathrm{ty}, \mathsf{Cv})$ itself — no estimation is involved | a row sums unlike types, or a conversion is booked as a sum |

`Typed` is the only one of the eight predicates that is decidable from a declaration alone rather than from a
declaration *and* a trajectory: Definition 47 is a predicate on fluxes, so the check is syntactic, and
Proposition 42 says what no such check can buy — a conservation law that crosses a type class.

## 2. S11 · Per-parameter identifiability status

Status vocabulary is the article's own (§3.1): *established*, *not established*, *not applicable*. A value is
established when the observation map pins it relative to a declared model and record; not established when the
record leaves it free; not applicable when no identification question is live for it — which is the correct
status for a convention, and is not a failure. Status belongs to the pair (model, readout), never to the
parameter alone.

| quantity | enters | identification question | status | what would settle it |
|---|---|---|---|---|
| $\mathsf{Ty}, \mathrm{ty}, \mathsf{Cv}$ (type structure) | Def. 47, Prop. 42, `Typed` | none — declared | **not applicable** | — (a re-declaration, not an estimate) |
| $\Lambda^{*}$ closure capacity | Def. 21, `Closed` | is the LP feasible on the declared capacities? | **established** (as the value of a programme on declared data) | nothing further; its *inputs* are the declared capacities |
| $\kappa_m,\ \delta_m$ (reclassification deficit) | Def. 22, Prop. 28, Rem. 35 | is a reclassification series published by the reserve authority? | **not established** — read from a declared box in S9 | a publisher-declared reclassification series (none exists for USGS reserve classes) |
| $\tau_{\mathrm{use}}$ (timescale of the deficit readout) | Def. 22's $\kappa_m$ | none — declared by the analysis | **not applicable** | — |
| $\bar\delta,\ g_m$ (bounds on reclassification and demand growth) | Def. 22's horizon $T \le m_0/(\underline\delta g_m)$ | published bounds? | **not established** (bounds only, declared) | a declared source for the growth bound; the horizon is reported with it |
| $\mathcal A_{\min}$, $\mathcal A_{\max}$ (barriers) | `Safe`, Def. 45, Prop. 41 feasibility | none — declared | **not applicable** | — |
| $d_0,\ \rho,\ \tau$ (drawdown level, ramp rate, delay) | Prop. 41's $m_{\mathrm{needed}}$, $t_{\mathrm{last}}$ | published values for any named ledger? | **not established** — the article's two instances are illustrative | an empirical declaration by whoever runs the certificate |
| $H^{\mathrm{loc}}$ (frozen-rate ratio) | Prop. 26, Def. 46's corner | computable from the declared pair? | **established as a ratio**; its direction against $T$ is established **only under** Prop. 26's monotonicity hypothesis | the monotonicity (or a declared $\varphi$) |
| $q_i$ (normalisation choice) | Def. 23, Prop. 36 | none — freely chosen | **not applicable**, with Prop. 36's compatibility condition as the price | — |
| $\varepsilon_\ell$ (disturbance budget) | `Conserved` | declared, then checked against the record? | **established relative to the declaration** | the declared class |
| G3P $\widehat{\dot a}$, $a_{\mathrm{hist,min}}$ | $L_{\mathrm{hist}}^{\mathrm{anom}}$ (§6.5.1) | reproducible from the product's basin masks? | **not established numerically** — the rows are quarantined for reuse for exactly this reason, and the product documents a faulty June-2005 snow entry that the window spans | re-derivation from the masks, with the June-2005 choice declared |
| G3P anomaly reference period | the same index | is the baseline published? | **established** — April 2002 to December 2020, per the product documentation; coverage ends September 2023 | — |
| $\mathrm{SSB}_{\mathrm{now}},\ F_{\mathrm{now}},\ B_{\lim}$ | $\Theta_F$, the ADH proxy | defined by the protocol on the archived cohort | **established on the cohort**; **not established** as a statement about the population of assessed stocks | nothing further: the extract is pinned to release v4.66 (Zenodo 14043031, 6 Nov 2024) and its vintage is verified from its own contents in S5.1 (four of six published $F$ values reproduce that release exactly), with the cohort recomputed in S5.3 to $10^{-9}$ |
| reserves, production | $T_{\mathrm{reserve}}$ (§6.5.3) | published for a stated vintage? | **established for the vintage named**, not established forward | the vintage statement, which the row carries |
| $\tau_{\min},\ \tau_{\mathrm{agg}}$ (premium, Remark 33) | the overshoot premium | computable from the published accounts? | **established as arithmetic** on the published ratio; the zero-carbon-biocapacity row is **not applicable** as a modelling choice — it is the accounts' documented convention, cited in Remark 33 | whether the author also reports the carbon-demand-excluded variant |

`[author]` cells — **none**. Every row was read off the manuscript, the repository at
`refs/tags/edwards-framework-e1`, or a published source; the one cell that had needed your analysis repository
was closed instead by the release identifier plus S5.1's row-level vintage check, which is a stronger claim than
a pull date.

## 3. S12 · Material and energy value: what is checkable, and what is not

The position is recorded here so that it can be cited, tested, and kept out of the article's claim list. Each
row states the position's clause, the object in the article that carries it, and its status.

| clause of the position | object in the article | status | what is *not* claimed |
|---|---|---|---|
| value may be assessed only within a type; no substitution across types | Definition 47's predicate, and Proposition 42's splitting $\ker S_{\mathcal T}^{\top} = \bigoplus_\gamma \ker S_\gamma^{\top}$ | **established for conservation laws** | no theorem about worth: Proposition 42 says no conserved quantity prices one class against another, which is not the same statement as "value is not comparable" |
| no cross-type compensation in an aggregate | Proposition 29 (the calibrated monotone certifier is `= min`, and continuity with certification and strict monotonicity are incompatible) | **established** | no claim that a compensating index is useless; only that it is not a certificate |
| an effect at the interface must be re-declared, not summed | Definition 23 (free choice of normalisation) with Proposition 36 (conserved quantities do not compose unless compatible on the classes) | **established as a conditional** | no blanket invariance |
| boundary redrawing does not change what is conserved | Remark 36's reporting-boundary clause | **established under a hypothesis**: redrawing is harmless exactly while no conversion is declared or withdrawn | not invariance to redrawing *inside* a class — Proposition 36 governs that, and it can fail |
| reclassification is bounded by a declared elasticity | Definition 22's $\delta_m$, $\kappa_m$; Proposition 28 | **established as a deficit bound** | no forecast of reclassification, and no estimate of its rate |
| a certificate should carry an "MDV" field | no such field exists in the article | **not established here**; supplementary/project-side only | the article's `Cert` vector has eight entries and none of them is a value-type score |
| one umbrella invariance theorem covering all of the above | declined in favour of the per-case results (Propositions 28, 29, 36, 40, 42 and Definition 47) | — | the umbrella's hypotheses would have to include a primitive the article does not define |

## 4. Items this candidate closes from the repository and the deposit record

Closed by verification rather than by drafting: the Section 1.5 standards sentence in the main text (its clauses
are now each pinned to the 2025 SNA's own treatment — depletion of non-produced natural resources as a cost of
production, net domestic product less depreciation *and* depletion, the 2008 treatment as an other change in the
volume of assets, and the derivation from the SEEA Central Framework — and to the product documentation for the
groundwater exhibit), and the `Typed` row's dangling citation.

**Resolved since the first draft of this file:** the "current v4.66" of S5's version-sensitivity record is
correct. Deposit record **14043031** returns the title "RAM Legacy Stock Assessment Database v4.66", version
field `v4.66`, publication date 2024-11-06, CC-BY-4.0, file `RAMLDB v4.66.zip`; v4.65 (11995054, 2024-06-17)
is the immediately prior release, and v4.44 (2542919, 2018-12-22) is correct as printed in the table. An
earlier note here flagged v4.66 as unconfirmed because a paginated Zenodo search did not return it — that flag
is withdrawn.

# 6. Depletion arithmetic — three numbers that all get called "years left"

> **In plain words.** People ask one question — how long do we have? — and three different numbers answer it. (1) How hard the system is turning over right now. (2) How long the current decline would take if the rate were frozen at today's value. (3) When a *stated* model, under a *stated* scenario, first crosses a *stated* line. These are not three estimates of one thing. They are three different questions. This section defines all three, proves how far apart they can be, and then classifies the three public numbers everyone quotes.

The ledger supplies the net active-pool derivative needed to tell gross throughput apart from net decline and from a model-conditioned threshold time. The distinction matters because "time to depletion" is publicly used as if all three were one quantity. They are not, and the worked instances below make the differences explicit. Let $A_{\min}$ be a declared threshold for the active abiotic pool, with $A>A_{\min}$.

## 6.1 The three quantities

**Definition 3 (Gross turnover intensity and support coverage).** *With assimilation $g(X,A)>0$, the gross turnover intensity is $J^{\mathrm{gross}}_A=g(X,A)/A$ and the gross support-coverage ratio is $H^{\mathrm{gross}}_A=(A-A_{\min})/g(X,A)$. **Neither is a time to depletion.***

The implication $g>0\Rightarrow\dot A<0$ is false in general. At an interior steady state, $g$ can be positive while decomposition and geological transfer balance it exactly, so that $\dot A=0$. Gross uptake measures throughput or dependency. Net depletion is a balance property.

This false-implication record is the first rung of the taxonomy, and it governs every application below.

**Definition 4 (Local net-depletion ratio).**

$$\mathcal H^{\mathrm{loc}}_A(t)=\frac{A(t)-A_{\min}}{[-\dot A(t)]_+},\qquad\text{with the extended-real convention }\ \mathcal H^{\mathrm{loc}}_A=+\infty\ \text{when }\ \dot A\ge0.$$

The convention is not a courtesy. It correctly reports *no current net decline* at a stationary or replenishing state. The ratio is still not a trajectory forecast: it freezes the current net rate. If the fluxes change with $A$, policy, climate, prices or other states, the realized threshold time can differ substantially.

**Definition 5 (Scenario-conditioned hitting time).** *For a fully specified dynamical model, policy or scenario $\pi$, disturbance history $d$, and initial state $x_0$,*

$$T_A(x_0;\pi,d)=\inf\{t\ge0: A^{\pi,d}_t(x_0)\le A_{\min}\},\qquad T_A=+\infty\ \text{if the threshold is never reached}.$$

Under parameter, observation and scenario uncertainty, the appropriate output is a **distribution or robust interval** of $T_A$, not a single universal date.

| Quantity | Question it answers |
|---|---|
| $J^{\mathrm{gross}}_A,\ \mathcal H^{\mathrm{gross}}_A$ | How strongly does the system depend on, or turn over, the pool at the current gross rate? |
| $\mathcal H^{\mathrm{loc}}_A$ | If the current net decline were frozen, what is the local stock-to-rate ratio? |
| $T_A$ | Under a stated model, policy and disturbance scenario, when is the threshold first reached? |

The three quantities answer different questions and must not share one depletion-horizon label.

## 6.2 Uniform-drift bounds

**Proposition 17 (Local threshold-horizon bracket).** *Assume (H1) $A:[0,T]\to\mathbb R$ is absolutely continuous with $A(0)>A_{\min}$; (H2) constants $v_0>0$ and $0<\varepsilon<1$ are given, and $H_0=(A(0)-A_{\min})/v_0$; (H3) $T\ge H_0/(1-\varepsilon)$; (H4) $(1-\varepsilon)v_0\le-\dot A(t)\le(1+\varepsilon)v_0$ for almost every $t$ while $A$ stays above $A_{\min}$. Then a first crossing time $H$ exists no later than $H_0/(1-\varepsilon)$, and*

$$\frac{H_0}{1+\varepsilon}\ \le\ H\ \le\ \frac{H_0}{1-\varepsilon},\qquad |H-H_0|\ \le\ \frac{\varepsilon}{1-\varepsilon}\,H_0.$$

*Proof.* If no crossing occurs before $t^*=H_0/(1-\varepsilon)$, absolute continuity gives $A(t^*)\le A(0)-(1-\varepsilon)v_0t^*=A_{\min}$, a contradiction; hence $H\le t^*$. Integrating both rate bounds over $[0,H]$ and using $A(0)-A(H)=v_0H_0$ gives the two-sided bracket: from the upper rate bound $v_0H_0\le(1+\varepsilon)v_0H$, and from the lower rate bound $v_0H_0\ge(1-\varepsilon)v_0H$. $\blacksquare$

In words: promise that the decline stays within 10% of a fixed rate, and the frozen-rate ratio is guaranteed to be within about 11% of the true crossing time.

This is a **local** diagnostic only. It fails when depletion reverses, when the rate approaches zero, or when feedback moves the trajectory outside the declared rate bounds. Its companion is the one-sided exhaustion proposition of §3.6, whose counterexample — proportional extraction never exhausts in finite time — shows that the uniform margin $\varepsilon>0$ is load-bearing in both directions. The bracket bounds the frozen-rate ratio's error under declared rate bounds, and nothing more.

**When the clocks coincide.** Under the rate bracket the frozen-rate ratio and the true hitting time agree within the bracket: $-\dot A\in[(1-\varepsilon)v_0,(1+\varepsilon)v_0]$ gives $\mathcal H^{\mathrm{loc}}_A=(A(0)-A_{\min})/[-\dot A]_+\in[H_0/(1+\varepsilon),H_0/(1-\varepsilon)]$, hence

$$|H-\mathcal H^{\mathrm{loc}}_A|\le\frac{2\varepsilon H_0}{1-\varepsilon}$$

— the only regime in which the frozen-rate ratio *is* a horizon. At a stationary state ($\dot A=0$) with $g>0$, $\mathcal H^{\mathrm{loc}}_A=+\infty$ while $\mathcal H^{\mathrm{gross}}_A<\infty$. The three quantities of §6.1 coincide only under a declared rate bracket, and the false implication $g>0\Rightarrow\dot A<0$ is the reason.

## 6.3 Upper barriers, exit times, and maintainability

The lower-barrier setting of §6.1 is one half of the story. For each moiety $m$ define the lower and upper exit times

$$\tau_m^-=\inf\{t\ge0:S_m(t)\le\underline B_m(t)\},\qquad \tau_m^+=\inf\{t\ge0:S_m(t)\ge\overline B_m(t)\},\qquad \inf\varnothing=\infty,$$

and the overall admissibility exit time $\tau_{\mathrm{exit}}=\min_m\{\tau_m^-,\tau_m^+\}$; **horizon safety on $[0,T]$ is $\tau_{\mathrm{exit}}>T$**. Note the minimum is taken over all moieties $m$ — both signs, every component.

Two disciplines attach.

1. **Equality at the hitting time** — $S_m(\tau_m^-)=\underline B_m(\tau_m^-)$ — requires continuity of both $S_m$ and $\underline B_m$ and appropriate initial separation. If fluxes or barriers can jump, the stock can cross the barrier *without* satisfying equality.
2. **Lower barriers need not be exhaustion thresholds.** The diagnostic distinguishes physical exhaustion ($S_m=0$), functional failure ($S_m=\underline B_m^{\mathrm{func}}$), a resilience or regime-shift threshold, an economically recoverable reserve, and a minimum service-supporting stock. The term "exhaustion" is reserved for $S_m=0$; all other thresholds are barrier violations.

Upper-barrier violations matter symmetrically: a system may satisfy every lower-barrier condition while violating an upper barrier, $S_m(t)>\overline B_m(t)$. Atmospheric CO₂ accumulation violates an upper concentration barrier while fossil carbon stocks decline. The depletion diagnostic must check both barriers.

And a stock can remain above a barrier until an assessment horizon $T$ and still be unsustainable thereafter. If the assessment claims *sustainability* rather than *finite-horizon admissibility*, it needs a terminal condition $x(T)\in\mathcal K_{\mathrm{maint}}$, where

$$\mathcal K_{\mathrm{maint}}=\{x:\exists\ \text{an admissible continuation satisfying all barriers for } t\ge T\}$$

— the set from which barrier safety is indefinitely maintainable: the viability kernel of the barrier set under the admissible controls (Aubin, 1991). The finite-horizon diagnostic is a **necessary but not sufficient** condition for sustainability. The full certificate requires the terminal state to lie in the maintainability set.

## 6.4 Robust semantics

For uncertain parameters $\theta\in\Theta$ and admissible disturbances $d\in\mathcal D$, robust barrier safety is

$$\text{RobustBarrierSafe}(x(\cdot))\iff \underline B_m(t)\le S_m(t;\theta,d)\le\overline B_m(t)\ \ \forall m,\ \forall t,\ \forall\theta\in\Theta,\ \forall d\in\mathcal D,$$

and the depletion-horizon classification is fourfold: **nominal** ($\theta=\theta_0$, $d=0$); **worst-case** ($\inf_{\theta,d}\tau_{\mathrm{exit}}(\theta,d)$); **probabilistic** ($\Pr[\tau_{\mathrm{exit}}>T]\ge1-\varepsilon$); and **scenario-conditioned** ($\tau_{\mathrm{exit}}\mid\theta=\theta_s$). The componentwise diagnostic applies to each scenario, and the conjunctive criterion applies within each scenario and across scenarios. **No single number is promoted across the four classes without a declared map.**

## 6.5 Application classifications at their exact status

The classification matrix records, quantity by quantity, what each application computes and what each object is. The numerical exhibits that follow are worked instances of the constructions, and **the classification of each row does not depend on the magnitudes**.

| Time-like quantity | G3P $\mathcal L^{\mathrm{anom}}_{\mathrm{hist}}$ | Phosphate $\mathcal T_{\mathrm{reserve}}$ | Fisheries $\Theta_F$ |
|---|---|---|---|
| $J^{\mathrm{gross}}_A,\ \mathcal H^{\mathrm{gross}}_A$ — turnover / dependency | no | no | gross-loss analogue only — **not a member** (§6.5.4) |
| $\mathcal H^{\mathrm{loc}}_A$ — frozen net-rate ratio | no (anomaly, not stock) | no (classification, not stock) | no (no net $\dot B$) |
| $T_A$ — scenario hitting time | no | no | no |
| **What it is** | record-relative statistical index | arithmetic ratio of an economic class | removals-only pressure scale |

### 6.5.1 Groundwater anomaly-persistence indices

The G3P column of the matrix is the groundwater case. The Global Gravity-based Groundwater Product (G3P v1.12; Güntner et al., 2024; the GRACE line it descends from is Tapley et al., 2004) provides monthly **groundwater-storage anomalies relative to a reference period**, not absolute aquifer volumes. For a basin-mean anomaly series over the reported April 2002 – September 2023 window, the linear-trend anomaly persistence index is

$$\mathcal L^{\mathrm{anom}}_{\mathrm{hist}}=\frac{a_{\mathrm{latest}}-a_{\mathrm{hist,min}}}{[-\dot a]_+},$$

the fitted distance to the series' own historical minimum divided by the fitted decline rate. The four-basin record: Indo-Gangetic $-49.7$ cm/yr with index $\approx2.7$ yr; North China Plain $-18.6$ with $\approx7.9$; Central Valley $-16.1$ with $\approx9.5$; La Mancha $-3.2$ with $\approx21.4$.

Classification, stated at the product's own status: a **statistical anomaly index with units of time** — not the physical stock ratio $\mathcal H^{\mathrm{loc}}_A$, and not a forecast of aquifer exhaustion. Its value depends on the product window, the basin mask, the anomaly reference and the linear-trend convention. A physical $\mathcal H^{\mathrm{loc}}_A$ requires an absolute stock estimate and a net stock derivative — aquifer geometry or saturated thickness together with storage parameters — not an anomaly series alone.

A structural point sharpens the boundary. The **access structure** — a well, or an index well — is infrastructure rather than the resource. It draws on stored water (the stock), which is replenished by recharge (the flow). The anomaly series measures the stored stock as observed at the access point; it measures neither the access infrastructure nor the recharge. An index built on it therefore cannot distinguish a drawdown of stored water that is recoverable on the recharge timescale from one that is not — although heavy over-extraction can make the loss permanent through compaction, subsidence or saline intrusion, in which case it is not recoverable at all. The index is exactly the record-relative object analysed in §7.3, and its interpretive boundary is that record-relativity (§7.7).

### 6.5.2 The applied depletion-horizon tables

Component-resolved depletion horizons on public data products are tabulated below, computed **without fitting any dynamical parameter** of the reduced systems. Rows marked with a dagger (†) are quarantined and must not be taken at face value: the Australia phosphate row dates to a pre-2026 reserve vintage (§6.5.3), and the Indo-Gangetic groundwater magnitude sits an order of magnitude beyond published basin-mean trends (the quarantine note below). Both are retained only as worked instances of the constructions, and neither enters any classification below.

**Groundwater (G3P v1.12 basin series).**

| Basin | Trend (cm/yr) | 2023 anomaly (cm) | Window minimum (cm, implied) | Horizon to window minimum (yr) |
|---|---|---|---|---|
| Indo-Gangetic (N. India)† | −49.7 | −414 | −548 | ≈ 2.7 |
| North China Plain | −18.6 | −145 | −292 | ≈ 7.9 |
| Central Valley (US) | −16.1 | −84 | −237 | ≈ 9.5 |
| La Mancha (Spain) | −3.2 | −20 | −88.5 | ≈ 21.4 |
| High Plains (US) | −7.9 | −160 | −160 | already at minimum (0.0) |
| global mean | −0.4 | −14 | −33.0 | ≈ 47.5 |

> **Quarantine note, placed adjacent to the row it marks** (recorded data-vintage decision: the row stays first, daggered). The Indo-Gangetic magnitude **must not be reused numerically**: it sits an order of magnitude beyond published basin-mean trends and awaits re-derivation from the product's basin masks — the full quarantine record is the paragraph below. The basin rows are reported extractions from the G3P v1.12 basin series, used here only to exhibit the index construction of §6.5.1. The window-minimum column is implied by the displayed trend and horizon through the index formula of §6.5.1 — **arithmetic, not product-endorsed** — and every basin row must be re-derived from the product's basin masks before any numerical reuse. The Indo-Gangetic magnitude is the extreme case: it sits an order of magnitude beyond published basin-mean groundwater-equivalent trends (typically a few cm yr⁻¹), and a linear trend of −49.7 cm yr⁻¹ maintained over the reported ≈ 21.4 yr window would place the fitted 2002 value near **+6.5 m** above the anomaly reference — the fitted segment convention is part of the quarantine. The rows are retained only as the worked instance of the index construction, and the classification status assigned below does not depend on the magnitudes.

**Phosphate (reserve-life arithmetic).**

| Country | Reserves (kt) | Reserve-life horizon (yr) | Implied production (kt/yr) |
|---|---|---|---|
| China | 3,400,000 | ≈ 28 | 121,429 |
| United States | 1,000,000 | ≈ 45 | 22,222 |
| Jordan | 820,000 | ≈ 62 | 13,226 |
| Morocco | 50,000,000 | ≈ 1,250 | 40,000 |
| Australia† | 5,800,000 | ≈ 2,088 | 2,778 |
| World (reserves) | 74,000,000 | ≈ 309 | 239,482 |
| World (resources, $\varepsilon=0.10$) | > 300,000,000 | > 1,125 | 240,000 |

*How to read the last two rows.* They answer different questions, and they are kept apart on purpose. The reserve horizon is reserves ÷ production. The resources row applies the article's declared threshold convention of §6.5.3, $T_{\mathrm{resource},10\%}=0.9\,G_{\mathrm{resource}}/C_G$ — the horizon runs to the point where 10% of the resource base remains, which is why it is 0.9 × (resources ÷ production) rather than 0.1 × (resources ÷ production).

**Fisheries.** The column reports the **archived-depletion-horizon (ADH)** pure-decay proxy

$$\mathrm{ADH}=F^{-1}\log\!\big(\mathrm{SSB}_{\mathrm{now}}/(0.2\max \mathrm{SSB})\big)$$

under current fishing mortality $F$, with median **≈ 1.8 yr** across the **43** assessed stocks with finite spawning-stock-biomass (SSB) and $F$ series — the archived pull, kept in place as the headline cohort by the recorded data-vintage decision — computed with $\mathrm{ADH}=0$ entered for the **eight** stocks already at or below the reference: the zero convention of the source table's caption, **which the median includes**.

Two disclosures accompany the headline value (both recorded). The archived 43-stock cohort is reproduced by **neither** public RAM Legacy release — S5's version-sensitivity record, cross-referenced here, is the retraction and the row-by-row re-verification — and the v4.66 public-release broad-cohort reading (454 stocks, median 3.39 yr) is the primary public-release comparison, executed in S5 and detailed below. The qualifying positive sub-cohort ($F>0$ and $\mathrm{SSB}_{\mathrm{now}}>\mathcal B_{\mathrm{lim}}$; 35 stocks) has median 2.9 yr; both medians come from the archived pull alone.

The cohort is a **selected class, not a random sample** of assessed stocks: all 43 stocks are small pelagics (18 anchovy, 20 herring, 4 sprat, 1 sardine), the fast-maturing class the companion review screen (Author, E., et al., *in review*) selects by its annual-review eligibility criterion (42 of the 43 are that screen's annual-managed spectral-null stocks, per the source caption). The ≈ 1.8 yr median is therefore a class-specific diagnostic for fast-maturing, annually managed pelagics — not a statistic of assessed fisheries in general. The executed broad-cohort comparison (§5) runs the same protocol on the full public release — 454 stocks, median 3.39 yr, the upper end carried by the long-lived groups: elasmobranchs 11.5, sebastids 9.0, pleuronectids 6.0 yr — and only **2%** of random 43-stock draws from that broad cohort have medians at or below the class cohort's 1.79 yr.

The extract is the RAM Legacy cohort of Ricard et al. (2012), and the pull date is archived in the analysis repository; the archived pull has been re-verified row by row against the formula — all 43 rows reproduce $\mathrm{ADH}=\max(0,F^{-1}\log(\mathrm{SSB}/B_{\mathrm{lim}}))$ with $B_{\mathrm{lim}}=0.2\max\mathrm{SSB}$. The value is reported with its cohort conditions and is **not promoted to a forecast**. Because cohort composition is database-version-dependent, every cohort statistic is pinned to the archived pull: the quartile summary of $F$ and $\log(\mathrm{SSB}/B_{\mathrm{lim}})$ over the cohort belongs to that pull alone, and no cohort statistic is quoted from a different database version. The cohort protocol is fully specified in the accompanying supplementary material (S5) — including the zero entries for stocks at or below the reference, which enter the median — together with the version-sensitivity record: on the public RAM Legacy releases the same protocol qualifies **415** stocks (v4.44, median **2.57** yr) and **454** (v4.66, median **3.39** yr) — both reproduced to printed precision under the recovered micro-specification (S5) — **neither reproducing the archived 43-stock cohort**: the archived pull's 43-stock list and extract-time series state — supplied and re-verified — differ from both public releases.

**The scope discipline is the tables' load-bearing content.** None of the reported numbers is a computed instance of any model's first-hitting time. The groundwater column is a trend-to-window-minimum extrapolation, the phosphate column a reserve-life ratio, and the fisheries column a pure-decay proxy with recruitment omitted. They are descriptive, component-resolved diagnostics in the two-pool logic of the taxonomy — not dynamical predictions.

**Non-example 1 — a deliberate boundary of aggregation, not a score of the framework.** The equal-weight inverse-horizon score of the four basins still above their window minimum and world phosphate reserves,

$$\Sigma_{\mathrm{reserves}}\approx\frac15\Big(\frac1{2.7}+\frac1{7.9}+\frac1{9.5}+\frac1{21.4}+\frac1{309}\Big)\approx0.130\ \mathrm{yr}^{-1},$$

is a **ranking device, not a componentwise certificate**: it mixes basins and reserves, incommensurable objects under the typing of §2.1, and is retained only to mark the boundary of legitimate aggregation. It is exhibited as the worked instance of the non-compensation boundary of §10.1: a positive aggregate coexisting with componentwise deficits by construction — admissible as communication, **inadmissible as certification**. The article stops at the aggregate. It is not turned back into a horizon, and no reciprocal of it is reported here as a "blended years-left" figure — doing so would be exactly the move the non-example blocks.

### 6.5.3 The phosphate reserve-life ratio

The phosphate column of the classification matrix is the reserve-life ratio. At constant current production $C_G$,

$$\mathcal T_{\mathrm{reserve}}=G_{\mathrm{reserve}}/C_G ;$$

at approximately 74,000,000 kt (74,000 Mt) of world reserves and 240,000 kt/yr of production (U.S. Geological Survey, 2026) this is approximately **309 years**. The arithmetic is internally consistent as a reserve-life ratio to zero. It is **not a physical exhaustion forecast**, because reserve classification changes with prices, technology, exploration and regulation — the point made independently, and forcefully, by Illakwahhi, Vegi and Srivastava (2024) for the single-source USGS data behind the influential phosphate depletion estimates, and standard in mineral economics, where reserves have grown through a century of rising production for copper (Tilton, 2003; Tilton and Lagos, 2007).

The reserves/resources split discipline is part of the classification: a resource-threshold calculation $\mathcal T_{\mathrm{resource},10\%}=0.9\,G_{\mathrm{resource}}/C_G$ answers a different question and **must not share a column with the reserve-life ratio without an explicit convention label**. The reserve classification is economic — US reserves have remained near 1,000,000 kt while cumulative production since 1996 is of order 600,000 kt — and the resource-based world horizon (≈ 1,125 yr at $\varepsilon=0.10$) is more than three times the reserve-based figure (≈ 309 yr). The two-compartment split is what prevents these from being collapsed into one number.

The implied-production column of the §6.5.2 table reproduces the production figure each horizon assumes (production = reserves ÷ horizon) and thereby exposes the source arithmetic; the country horizons reproduce the recorded MCS-vintage ratios.

**The vintage is pinned once.** The single pinned source of record is the *Mineral Commodity Summaries* (MCS) 2026 (U.S. Geological Survey, 2026), and every figure this article quotes at pin status is that vintage's — the pinned source's 2025 world-production column ≈ 250,000 kt and Australia's reserves 120,000 kt (JORC-compliant). The displayed country rows remain at their recorded **pre-2026** vintage under the quarantine dagger (the Australian 5,800,000 kt among them, retained rather than blanked), kept in place as worked instances of the reserve-life construction. Completing the re-pin — replacing the displayed rows row by row with the pinned vintage's per-country reserve figures — is the **registered open data action**; it requires the per-country MCS 2026 reserve table, and no displayed classification depends on it.

### 6.5.4 The fisheries removals-only pressure time

The fisheries column of the classification matrix is the removals-only pressure time. When $\mathrm{SSB}_{\mathrm{now}}>\mathcal B_{\mathrm{lim}}>0$ and $F_{\mathrm{now}}>0$, define

$$R_{\mathcal B}=\log(\mathrm{SSB}_{\mathrm{now}}/\mathcal B_{\mathrm{lim}}),\qquad \Theta_F=\frac{R_{\mathcal B}}{F_{\mathrm{now}}},$$

the **fishing-only time-to-reference**: the crossing time of the deliberately incomplete comparison process $\dot B=-F_{\mathrm{now}}B$. With $\mathcal B_{\mathrm{lim}}=0.2\max\mathrm{SSB}$ this is the construction tabled as ADH in §6.5.2; the two notations are kept because the boundary hypotheses stated here ($F_{\mathrm{now}}>0$, $\mathrm{SSB}_{\mathrm{now}}>\mathcal B_{\mathrm{lim}}$) are exactly the conditions of the positive sub-cohort of §6.5.2 (35 stocks, median 2.9 yr). The reported §6.5.2 median (≈ 1.8 yr) additionally carries the eight zero entries for stocks at or below the reference, per the zero convention of the source caption.

It is a **removals-only pressure timescale**: the time unit comes from rescaling a stock-reference margin by one isolated gross-loss rate. Because recruitment, somatic growth, maturation, natural mortality, density dependence, environmental forcing and future policy are omitted, $\Theta_F$ is not a net biomass depletion diagnostic, not a demographic hitting-time estimate, and **not a member of the $J^{\mathrm{gross}}$–$\mathcal H^{\mathrm{loc}}$–$T_A$ hierarchy**. A genuinely local biomass-decline ratio $\mathcal H^{\mathrm{loc}}_{\mathcal B}=(\mathcal B-\mathcal B_{\mathrm{lim}})/[-\dot{\mathcal B}]_+$ would require a compatible net $\dot{\mathcal B}$ estimate, and a demographic hitting time would require a fully specified population model; RAM Legacy SSB and $F$ data (Ricard et al., 2012) do not by themselves supply these quantities or models.

Spawning biomass is **not** an abiotic support pool. The construction is retained specifically to show why an isolated gross-removal timescale must not be promoted to a net depletion diagnostic.

**The collective implication for material-flow measurement.** The three published "depletion time" numbers — G3P index, phosphate reserve-life, fisheries removals-only time — answer three distinct questions at three distinct evidentiary levels.

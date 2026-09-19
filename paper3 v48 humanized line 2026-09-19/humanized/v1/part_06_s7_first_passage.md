# 7. First-passage semantics on declared surrogates — a probability statement about a *statistic*, not about the aquifer

> **In plain words.** A "first-passage time" is the random moment at which something drifting and wobbling first crosses a line. Section 6 used deterministic ratios. Here the article adds noise, because that is what the published critiques and the public debate ask for. The discipline is what makes the result usable: the noise is attached to the *trend statistic* fitted to the data, not to the aquifer, the fish stock or the orebody. So every probability below is a statement about a fitted number. None of them is a forecast about nature, and the section ends with seven sentences that say so.

## 7.1 Two objects, not one

The ledger's own first-passage object is the model hitting time of Definition 5 — a quantity on trajectories of the mass-conserved ledger, or of a named reduced system. The public-data quantities of §6.5 are constructed proxies on observed series. That distinction is the entry discipline of this section: the surrogates below **do not compute the ledger's hitting time**, **do not complete the ledger stochastically**, and **do not identify physical failure thresholds**.

## 7.2 The observed-drift Brownian surrogate

**Definition 6 (Observed-drift Brownian surrogate).** *Let $A_0$ (local to §7.2–7.4; **not** the half-saturation constant of §2.2) be the latest observed anomaly and $\mu=\hat\mu<0$ the fitted drawdown rate. On the scale of the tabulated series, define*

$$A(t)=A_0+\mu t+\varsigma W_t,\qquad A(0)=A_0>\mathcal A^{\mathrm{win}}_{\min},$$

*where $W$ is a standard Wiener process, $\varsigma>0$ a chosen noise scale, and the process is stopped at first reaching the record-relative barrier $\mathcal A^{\mathrm{win}}_{\min}$. This is a statistical surrogate for the empirical trend extrapolation. It is not a hydrological constitutive law, is not mass-conserving, and is not a perturbation or stochastic completion of the ledger's active-pool equation or of the finite-donor primitive system of §2.2. **The non-completion non-claim is part of the definition.***

In words: take the straight line that was fitted to the observations, then allow it to wobble. Anything computed from that wobble is about the line.

## 7.3 The inverse-Gaussian groundwater first passage

**Proposition 18 (Inverse-Gaussian first passage — a standard fact, stated for notation).** *Let $T_{\mathrm{GW}}=\inf\{t>0: A(t)\le\mathcal A^{\mathrm{win}}_{\min}\}$ for the process of Definition 6, and $d=A_0-\mathcal A^{\mathrm{win}}_{\min}>0$. Conditional on treating $\mu$ and the barrier as fixed,*

$$T_{\mathrm{GW}}\sim \mathrm{IG}(\nu,\lambda),\qquad \nu=\frac{d}{|\mu|},\qquad \lambda=\frac{d^2}{\varsigma^2},$$

*in the mean–shape parameterization. In particular $\mathbb E[T_{\mathrm{GW}}]=\nu=\mathcal H^{\mathrm{win}}_{\mathrm{GW}}$ — the deterministic horizon to the window minimum, $=d/|\mu|$ — and $\mathrm{Var}(T_{\mathrm{GW}})=\nu^3/\lambda=d\varsigma^2/|\mu|^3$.*

*Proof.* The first-passage time of a Brownian motion with constant negative drift to a lower barrier is inverse Gaussian — the classical first-passage result (Chhikara and Folks, 1989; Redner, 2001) — with the stated mean and shape parameters; the standard inverse-Gaussian moments give the displayed mean and variance. $\blacksquare$

The mean of the stochastic surrogate equals the deterministic trend-to-window-minimum ratio of §6.5.1. That equality is the precise sense in which the tabled groundwater numbers are first-passage means of a declared surrogate.

**Corollary 19 (Zero-noise limit and median).** *As $\varsigma\to0^+$, $T_{\mathrm{GW}}\to\mathcal H^{\mathrm{win}}_{\mathrm{GW}}$ in probability, and at $\varsigma=0$ the deterministic trajectory reaches the barrier exactly there. For every finite $\varsigma>0$ the inverse-Gaussian median $m$ satisfies $m<\nu=\mathcal H^{\mathrm{win}}_{\mathrm{GW}}$,*

$$F_{\mathcal T}(\nu)=\tfrac12+e^{2\lambda/\nu}\,\Phi\big(-2\sqrt{\lambda/\nu}\big)>\tfrac12 .$$

*The variance scales as $\varsigma^2$ and the standard deviation and small-noise quantile widths as $\varsigma$. The median below the mean is the inverse Gaussian's right skew toward short passage times; **the inequality must not be inverted.***

*Proof.* Evaluate the inverse-Gaussian CDF $F_{\mathcal T}(t)=\Phi\big(\sqrt{\lambda/t}\,(t/\nu-1)\big)+e^{2\lambda/\nu}\Phi\big(-\sqrt{\lambda/t}\,(t/\nu+1)\big)$ at $t=\nu$: the first term is $\Phi(0)=1/2$ and the second is strictly positive for finite $\lambda$, so the median lies strictly below the mean; the concentration statement follows from the variance. $\blacksquare$

These are conditional distributional statements about the surrogate. **They are not corrections to the tabled years, and they do not show that physical water mass is depleted faster.**

## 7.4 The record-relative barrier discipline

The barrier $\mathcal A^{\mathrm{win}}_{\min}$ is selected from the *same finite observation window* used to estimate $\hat\mu$. It is therefore a path-dependent, record-relative threshold, not an independently identified hydrological failure floor. Future passage below it represents a record-breaking stress event under the surrogate, not physical exhaustion.

Three boundary facts complete the discipline.

1. **Already at minimum.** If $A_0=\mathcal A^{\mathrm{win}}_{\min}$, the stopping-time convention gives $T_{\mathrm{GW}}=0$ deterministically for every $\varsigma$. The inverse-Gaussian family has a degenerate boundary limit concentrated at zero, and $\mathrm{IG}(0,0)$ is not an ordinary inverse-Gaussian distribution. **Zero cells report zero relative to the selected observational barrier** — not zero physical uncertainty, and no confirmation of collapse.
2. **Independent physical thresholds.** If an independent physical threshold $\mathcal A^{\sharp}<\mathcal A^{\mathrm{win}}_{\min}$ is specified, the same constant-drift surrogate gives the conditional mean $\mathbb E[T^{\sharp}]=(A_0-\mathcal A^{\sharp})/|\mu|$, longer than the record-relative proxy because the barrier is lower. This is a statement *within the surrogate*, not a general lower-bound theorem for the physical ledger, whose drift and state coupling may differ.
3. **Classification.** The load-bearing content is the interpretation boundary itself: a record-relative barrier makes the passage time a property of the observation window, and no reading of the tabled numbers escapes that qualification.

## 7.5 The geometric-Brownian fisheries first passage

**Proposition 20 (Geometric-Brownian correction — a standard fact, stated for notation).** *Let $\mathrm dB_t=-h\mathcal B_t\,\mathrm dt+\varsigma\mathcal B_t\,\mathrm dW_t$ under the Itô convention, with $h>0$ and $0<\mathcal B_{\min}<\mathcal B_0$, and $\mathcal T_{\mathrm{fish}}=\inf\{t>0:\mathcal B_t\le\mathcal B_{\min}\}$. Then*

$$\mathcal T_{\mathrm{fish}}\sim \mathrm{IG}(\nu_F,\lambda_F),\qquad \nu_F=\frac{\log(\mathcal B_0/\mathcal B_{\min})}{h+\varsigma^2/2},\qquad \lambda_F=\frac{\log(\mathcal B_0/\mathcal B_{\min})^2}{\varsigma^2},$$

*so $\mathbb E[\mathcal T_{\mathrm{fish}}]=\log(\mathcal B_0/\mathcal B_{\min})/(h+\varsigma^2/2)$; as $\varsigma\to0^+$ this converges to the deterministic pure-decay horizon when $h=F$ and $\mathcal B_{\min}=\mathcal B_{\mathrm{lim}}$.*

*Proof.* Itô's lemma (Øksendal, 2003) gives $\mathrm d\log\mathcal B_t=-(h+\varsigma^2/2)\mathrm dt+\varsigma\,\mathrm dW_t$, so the logarithmic threshold is a Brownian first-passage problem with initial distance $\log(\mathcal B_0/\mathcal B_{\min})$ and downward drift $h+\varsigma^2/2$; Proposition 18 applies. Under the Stratonovich convention the log-drift would be $-h$ and the deterministic limit would match the pure-decay horizon $h=F$ exactly: **the $\varsigma^2/2$ shortening is the Itô choice, not a property of the physical process.** $\blacksquare$

For fixed arithmetic drift and the Itô parameterization, the finite-noise mean is strictly shorter than the deterministic horizon. This is a property of the chosen surrogate parameterization; it is **not** a universal claim that environmental variability accelerates physical biomass loss. The construction joins the removals-only classification of §6.5.4 — the same pure-decay process, now under a declared stochastic surrogate.

## 7.6 The constant-production phosphate passage time

Under the deterministic surrogate $\dot G=-P$ with constant production $P>0$, the first-passage time to a fixed threshold $G_{\min}\in[0,G_0)$ is

$$\mathcal T_{\mathrm{phos}}=\frac{G_0-G_{\min}}{P},$$

the reserve-life ratio being the $G_{\min}=0$ special case, and a threshold fraction $\varepsilon G_0$ giving $(1-\varepsilon)G_0/P$. This is a conditional reserve-classification proxy under constant production. Because reserves are an economic classification rather than a fixed physical stock, it is not a forecast of geological exhaustion without an explicit resource and production model. **No stochastic phosphate extension is required for the interpretation.**

## 7.7 The explicit non-claims

The first-passage semantics close with seven explicit non-claims, all of which hold in this article.

1. The Brownian and geometric-Brownian processes are **not** stochastic completions of the ledger and do not conserve its mass compartments.
2. No theorem relates $\hat\mu$ to $-\dot A$ of the reduced systems, to the finite-donor primitive system, or to the institutional delay equations.
3. The model hitting time $T_A$ of Definition 5 is **not shown to be inverse Gaussian**: it would be inverse Gaussian only if the active-pool residual were Brownian with constant drift, which the coupled balance (2) does not supply — the tabled groundwater numbers inherit inverse-Gaussian means from Definition 6's surrogate and from nothing else.
4. The historical groundwater minimum is not an independently identified physical failure barrier.
5. A shorter surrogate median or Itô mean is not evidence of faster physical depletion.
6. The gross active-pool horizon $\mathcal H^{\mathrm{gross}}_A$ of Definition 3 and its productivity-illusion interpretation — the misreading of a large gross-turnover horizon as evidence of slow net depletion, the false implication recorded in §6.1 — are not first-passage results treated here.
7. The fisheries calculation is not a stage-structured fisheries model, and the phosphate calculation is not a geological-reserve model.

## 7.8 Parameter and observation uncertainty

The inverse-Gaussian results condition on the drift, the barrier and the noise scale. In the groundwater application, $\hat\mu$ is estimated from a finite, potentially autocorrelated record, and the barrier is selected from that same record. Measurement error, serial dependence, seasonal forcing, spatial aggregation, trend breaks and common climatic drivers are **separate** uncertainties, and integrating any of them out yields a predictive mixture rather than a single inverse-Gaussian law. A residual scale estimated from the same window does not by itself identify process noise. **No calibrated predictive distribution is claimed**; the full uncertainty treatment belongs to an empirical identification study, not to this article.

For industrial-ecology measurement this discipline is the practical message: first-passage distributions on declared surrogates are usable as descriptive statistics, but their drift, barrier and noise inputs each carry their own identification story, and a calibrated forecast requires that story to be discharged.

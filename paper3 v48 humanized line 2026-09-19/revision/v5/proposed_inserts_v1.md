# `revision/v5` — staged inserts (applied → see README_v5.md)

> **Superseded 2026-09-15:** this staging file was the source for `build_v5.py`; its blocks are now applied as Definitions 21–23, Theorem 24, Propositions 25–32 and Remark 33 in `paper3_v5.md`, with three changes recorded in §2 of `README_v5.md` (Proposition 32's numbers restated from the re-run; the audit's 'iff' demotion; S11/S12 routed to the supplementary and to the companion). Kept for provenance.

**Status of this file:** thirteen blocks drawn (S1–S12, with S2′) from the five audits in `uploads/p3 profound upgrades.txt`, each written in the article's register at its placement anchor, each with the verification I ran. **Nothing here has been applied to `revision/v4/paper3_v4.md`, which remains the manuscript of record** (34-check verify run passes). New statements take the article's shared main counter at 21–29; the numbering convention of §3.1 keeps them apart from the layering counter (Propositions 1–2 of §3).

To adopt: copy a block into the anchor location, then re-run `revision/v4/verify_v4.py` on the new file with the added phrases, or extend it. To adopt none: nothing changes.

---

## S1 · §6.3 — conservation residual bound (fixes a defect in the article's own predicate)

**Anchor:** after the sentence ending "Barrier–conservation compatibility is a feasibility problem, not a slogan." (§3.5) and, in §2.2, after the definition of `b(t)=B_T u_∂+d_x`.
**Why:** v4 has six mentions of `d_x` and no bound on it. An unbounded distributed production term can absorb any imbalance, which makes "conservation consistency" vacuous exactly where it is used — as the certificate in Proposition 1 and in the envelope theorem.
**Text.**

> **Definition 23 (Bounded residual).** Conservation consistency is stated with a declared residual budget: for each left-null vector `\(\ell\)` of `\(S_T\)`,
> \[ \Bigl|\int_0^T \ell^{\top}C\,d_x(t)\,dt\Bigr| \;\le\; \epsilon_{\ell}(T), \qquad \epsilon_{\ell}\ \text{declared with the model}. \]
> The identity of Proposition 1 reads `\(\ell^{\top}Cx(T)=\ell^{\top}Cx(0)+\int_0^T\ell^{\top}b\,dt\)`, and `\(\epsilon_{\ell}\)` is the term the material-flow literature carries as statistical discrepancy. A barrier certificate derived from an envelope that does not carry `\(\epsilon_{\ell}\)` is void whenever the residual-inflated envelope leaves the declared barriers.

**Status to print:** registered requirement on the predicate, not an empirical claim. **Verification:** the identity is the article's own Proposition 1 with the `\(b=\dots+d_x\)` decomposition of §2.2 substituted; the corollary is immediate.

## S2 · §1.3 and §2.2 — the right null space: closure as a cone, not a slogan

**Anchor:** end of §1.3 (after the new Daly-rate sentence) and §2.2 after the incidence discussion.
**Why:** all five audits converge here and the article has 0 hits for right-null/closure-cone language. "The cycle closes at the rate of use" is currently a verbal predicate on a set the article already has.
**Text.**

> **Definition 24 (Closure cone).** With `\(\dot x=S_Tv+B_Tu\)`, `\(\mathcal K=\{v\ge 0: S_Tv+B_Tu=0,\ v\le\bar v\}\)` the admissible stationary flux patterns, and `\(P\)` the projection onto the use columns, a demanded use vector `\(D\)` closes at the rate of use iff `\(D\in P(\mathcal K)\)`. The closure capacity `\(\lambda^{*}=\max\{\lambda: \lambda D\in P(\mathcal K)\}\)` is a linear programme; `\(\lambda^{*}\ge1\)` is the regime in which the cycle closes at the demanded rate under the declared capacities, and `\(\lambda^{*}<1\)` is the regime in which every trajectory meeting `\(D\)` has a non-stationary stock, so by conservation the shortfall appears as support drawdown plus sink accumulation. Yield inflation is the same statement read on the projection: demand met outside `\(P(\mathcal K)\)`.
> Left-null vectors express conservation; right-null vectors express circulation. The article's weak and strong regimes are statements about the second set, and the depletion readouts are statements about the first.

**Status to print:** definition plus an LP; no new physics claimed, `\(\bar v\)` and `\(P\)` are declared. **Verification:** membership and the LP are definitional; the `\(\lambda^*<1\)` consequence uses Proposition 1 on the same `\(\ell\)`. The interpolation between `\(\mathcal K=\varnothing\)` and unlimited return capacity is the fable T2 cut condition (Gale–Hoffman); cite if adopted.

## S2′ · §1.3 or §5.3 — the closure deficit at the use timescale, with the bound the audit overstated

**Anchor:** §1.3, after S2's definition; or §5.3 with the support-provenance material.
**Text.**

> For each moiety `\(m\)`, let `\(\kappa_m(\tau;\Theta)\in[0,1]\)` be the fraction of the mobilised flux returned to a usable compartment within lag `\(\tau\)`, under the declared technology and knowledge set `\(\Theta\)`, and let `\(\delta_m=1-\kappa_m(\tau_{\mathrm{use}};\Theta)\)` be the closure deficit at the use timescale. With mobilisation rate `\(g_m\)`, the net drawdown of the support pool is `\(\delta_m g_m\)` **when the deficit is sustained**, so for any horizon on which `\(\delta_m\ge\underline\delta>0\)` holds,
> \[ \int_0^T\!\bigl(\text{liquidation}\bigr)\,dt\ \ge\ \underline\delta\int_0^T g_m\,dt, \qquad\text{and}\qquad T\ \le\ \frac{m_0}{\underline\delta\, g_m}, \]
> the second inequality being the frozen-rate horizon read on the liquidation flux rather than on gross use. Neither inequality reverses when `\(\delta_m\to0^+\)`, and a positive deficit is not by itself a barrier-reachability claim: a deficit that decays with the stock need never reach the barrier, and when the binding constraint is an upper barrier the relevant object is the complementary headroom.
> Two readings follow from the same definition. An indicator that reports a return fraction with no lag argument reports `\(\kappa_m(\infty)\)` while being read as `\(\kappa_m(\tau_{\mathrm{use}})\)`: this is the exact form of the defect in recycled-input-rate metrics, including the circularity-rate family. And "a material is waste" is the statement `\(\kappa_m(\tau_{\mathrm{use}};\Theta)<1\)` for the declared process graph, so unlocking a waste stream is an increase of `\(\kappa\)` at fixed `\(\tau\)`, which is measurable and does not require a new substance category.

**Verification:** the two inequalities were re-derived from `\(\text{net drawdown}=\delta_m g_m\)`; the audit's "barrier reachability iff `\(\delta_m>0\)` sustained" is **demoted to the one-sided bound above**, since the iff fails in both directions (see the review, §6, opus U5 row). **Status to print:** definitional plus a bound conditional on a declared sustained deficit and a declared `\(\tau_{\mathrm{use}}\)`; the circularity-metric reading is a claim about a published metric's argument list, not about its values.

## S3 · §4.8 or §6.2 — critical-margin budget theorem

**Anchor:** in §4.8, immediately after the three recharge-law rows of the table.
**Why:** it subsumes the article's one-way-valve instance and Theorem 14's `\(L^1\)` bound, and it turns the "excess service is backed by liquidation" claim into an inequality. Nothing in the article is softened; the qualification is the article's own.
**Text.**

> **Theorem 25 (Critical-margin budget).** Let the declared barrier margins be affine, `\(m(x)=Gx+a\ge0\)`, and let the declared service rate be `\(y=c^{\top}v\)`, `\(c\ge0\)`. Suppose some `\(\lambda\ge0\)` satisfies `\(\lambda^{\top}GS_T+c^{\top}\le0\)` componentwise, with `\(\lambda_j\)` carrying the units that convert margin `\(j\)` into cumulative service. Then `\(V=\lambda^{\top}m(x)\)` obeys `\(\dot V\le -y+\lambda^{\top}Gb\)` along every admissible trajectory, and for every trajectory remaining inside the declared barriers
> \[ \int_0^T y(t)\,dt \;\le\; V(x(0))+\int_0^T \lambda^{\top}Gb(t)\,dt . \]
> If `\(y\ge y_{\mathrm{req}}\)` and `\(\lambda^{\top}Gb\le\beta<y_{\mathrm{req}}\)`, then `\(T\le V(x(0))/(y_{\mathrm{req}}-\beta)\)`.
> *Proof.* `\(\dot V=\lambda^{\top}G(S_Tv+b)=(\lambda^{\top}GS_T)v+\lambda^{\top}Gb\le -c^{\top}v+\lambda^{\top}Gb\)`, using `\(v\ge0\)`; integrate and use `\(V(T)\ge0\)`, which holds because `\(m\ge0\)` and `\(\lambda\ge0\)`. `\(\square\)`
> The search for `\(\lambda\)` is a linear programme, and its infeasibility is no evidence of safety. The theorem bounds how long adequate service can coexist with componentwise safety; it is not a scalar safety certificate, and `\(V>0\)` does not establish that every margin is positive. Theorem 14 is the single-margin instance, and the valve row of Table … is the instance with `\(b=0\)`.

**Verification:** derived and checked line by line (review §1, V2). **Author input needed:** the `\(\lambda_j\)` unit declarations for whichever application is cited.

## S4 · §7.2 or §10.2 — aggregate dynamics do not identify component event times

**Anchor:** §7.2, after the sentence "the failure is universal to the method, not to a particular weighting."
**Why:** it converts the section from a static-algebraic impossibility to a dynamical one, with an explicit witness, and it is the article's own non-reduction argument in reusable form.
**Text.**

> **Proposition 26 (Aggregates do not transport event times).** Let two stocks and their sinks obey `\(\dot x_i=-kx_i,\ \dot w_i=kx_i\)`, so each pair conserves material and remains non-negative, and let the aggregate `\(Z=x_1+x_2\)` obey the exact closed dynamics `\(\dot Z=-kZ\)`. The initial states `\((x_1,x_2)=(2,98)\)` and `\((50,50)\)` produce the identical aggregate trajectory `\(Z(t)=100e^{-kt}\)` and, at the common lower barrier `\(x_i\ge1\)`, first hitting times `\(\log 2/k\)` and `\(\log 50/k\)`. No function of the aggregate trajectory determines the component event time.
> Dynamical closure and barrier observability are therefore separate obligations: an exact reduced model is not thereby competent about the events its components are declared to suffer. *Proof.* Direct evaluation of each exponential at its barrier. `\(\square\)`

**Verification:** arithmetic re-checked (review §1, V1). **Note:** the same witness, with `\(k\)` state-dependent, gives a version for nonlinear ledgers; do not add that without writing it.

## S5 · §8.1 — the index is an inverse trend-detection statistic

**Anchor:** §8.1, replacing the sentence "A physical \(H_A^{\text{loc}}\) requires an absolute stock estimate … and not an anomaly series alone." (retain it; append).
**Why:** the article's identifiability argument is currently an invariance statement; the following is a computed limit statement, and it is what a referee asks for.
**Text.**

> Within the declared linear-trend class the index has a further property. For `\(a_k=-\beta k+\varepsilon_k\)` with i.i.d. noise of scale `\(\sigma\)`, the record minimum lies at the end of the record once the trend dominates, so the fitted distance to it is a noise-scale gap and the index is `\(O_{\mathbb P}(\sigma/\beta)\)`: bounded in probability as the record length grows, and independent of the stock. A 400-replicate simulation with `\(\beta=\sigma=1\)`, at record lengths `\(10^2,10^3,10^4,10^5\)`, holds the index at `\(\approx0.2\)` years throughout while the stock declines by five orders of magnitude. Lengthening or densifying an anomaly record therefore cannot produce a horizon: the statistic converges to a trend-detection quantity expressed in years.

**Status to print:** a property of the declared class and a reported simulation, not a claim about any basin. **Verification:** simulated by me this turn (400 replicates per length, `np.random.default_rng(7)`), reproducing the fable T7 claim.

## S6 · §7.1–7.2 — what is admissible, uniquely, and why the calibration axiom matters

**Anchor:** §7.1, before "No nonnegative weighting certifies componentwise adequacy."
**Text.**

> **Proposition 27 (Uniqueness of the certifying aggregator).** Let `\(r\in\mathbb R^n\)` be component adequacies normalised to common units, and `\(\mathcal A:\mathbb R^n\to\mathbb R\)` satisfy monotonicity `\(r\le r'\Rightarrow \mathcal A(r)\le\mathcal A(r')\)`, calibration `\(\mathcal A(c\mathbf 1)=c\)`, and certification `\(\mathcal A(r)\ge c\Rightarrow r\ge c\mathbf1\)` for every `\(c\)`. Then `\(\mathcal A(r)=\min_i r_i\)`. *Proof.* Certification at `\(c=\mathcal A(r)\)` gives `\(\min_i r_i\ge\mathcal A(r)\)`; monotonicity and calibration applied to `\(r\ge(\min_i r_i)\mathbf1\)` give the reverse. `\(\square\)`
> The compensation premium `\(\Pi(r)=\mathcal A(r)-\min_i r_i\ge0\)` measures the part of any published aggregate produced by cross-component trades. Calibration cannot be dropped: the additively separable functional `\(\sum_i\min(0,r_i)\)` is continuous, monotone, faithful and complete, is not the minimum, and is not calibrated — so it reports the depth of the deficits while the minimum reports their existence, and either may be published provided neither is called the other.

**Verification:** both proved (V9); the second sentence is my counterexample to kimi §6's stronger claim (V10), which fails as stated. **Adoption effect:** §7 stops being purely prohibitive without weakening any existing statement.

## S7 · §6.2 — one-sided bias, and the reserve-life crossover

**Anchor:** §6.2, after the uniform-drift bounds (Propositions 17/18 region), before §6.3.
**Text.**

> **Proposition 28 (Sign of the frozen-rate error).** Let `\(\dot A=-\varphi(A)\)` with `\(\varphi>0\)` on `\((A_{\min},A_0]\)`, `\(T=\int_{A_{\min}}^{A_0}dA/\varphi(A)\)` and `\(H^{\mathrm{loc}}=(A_0-A_{\min})/\varphi(A_0)\)`. If `\(\varphi\)` is nondecreasing in `\(A\)`, then `\(T\ge H^{\mathrm{loc}}\)`: the frozen-rate number is conservative. If `\(\varphi\)` is nonincreasing in `\(A\)`, then `\(T\le H^{\mathrm{loc}}\)`: it is optimistic and unsafe. The sign is estimable by regressing the decline rate on the stock. Proportional extraction is the first case (`\(T=q^{-1}\ln(A_0/A_{\min})\)`, `\(H^{\mathrm{loc}}=(A_0-A_{\min})/(qA_0)\)`, and at `\(A_{\min}=0\)` the two disagree by being infinite against finite).
> **Proposition 29 (Reserve-life crossover).** With `\(\dot R=-(1-\eta)P\)`, `\(P=P_0e^{gt}\)`, `\(\tau=R_0/P_0\)`, exhaustion of the reserve class occurs at `\(T=g^{-1}\ln\bigl(1+g\tau/(1-\eta)\bigr)\)`, and `\(T\ge\tau\)` holds to first order exactly when `\(\eta\ge\tfrac12 g\tau\)`. A reserve-life ratio is a conservative bound on the reserve class only where reclassification keeps pace with growth; the article's own phosphate record (`\(\tau\approx309\)` years at a consumption growth of 3% per year) puts the threshold near `\(\eta\approx4.6\)`, and no reserve series in the record behaves that way outside a single-vintage snapshot.

**Verification:** both re-derived (V11), including the numeric threshold `\(0.5\cdot0.03\cdot309=4.635\)`. **Discipline check:** Proposition 29 speaks of the reserve *class*, so it does not promote the ratio to a geological horizon; `\(\eta\)` is a declared elasticity, and the "no reserve series behaves that way" clause must keep its registered status unless the four-mineral estimation is actually performed.

## S8 · §6.1 or §8.4 — the compensation premium of a published overshoot date

**Anchor:** §8.4, after the scope-of-applied-records paragraph, before Non-example 1.
**Text.**

> **Remark 30 (One-signed bias of an aggregate overshoot date).** With component biocapacities `\(b_i\)` and demands `\(d_i\)`, an aggregate overshoot date is
> \[ \tau_{\mathrm{agg}}=365\,\frac{\sum_i b_i}{\sum_i d_i}=365\sum_i w_i r_i,\qquad w_i=\frac{d_i}{\sum_j d_j},\quad r_i=\frac{b_i}{d_i}, \]
> a demand-weighted mean of the component ratios, so `\(\tau_{\mathrm{agg}}\ge\tau_{\min}:=365\min_i r_i\)` with equality iff all components with positive weight coincide. The difference `\(\tau_{\mathrm{agg}}-\tau_{\min}=365\sum_i w_i(r_i-r_{\min})\)` is the compensation premium: one-signed, exactly decomposable, unbounded in component dispersion, and computable from published component tables. It is reported here as arithmetic on a published construction; no recomputation of that construction's inputs is claimed in this article.

**Verification:** identity and inequality re-derived (V13). **Why it is the strongest cheap addition in the set:** it uses the article's own non-compensatory standard against a public number, and needs no data acquisition to state the inequality — only to report a premium figure, which stays out of this version.

---

### Not staged, and why

| Item | Reason |
|---|---|
| opus's cut list (first-passage derivations, five finite-donor propositions, applied prose, separation counterexamples) | would delete apparatus whose removal the last two revisions repaired; see the review §2 |
| Replacing Definition 5 with a control margin | displaces a registered object; the margin may be *added* (astra's `\(m_{\mathrm{needed}}=d_0\tau+d_0^2/2\rho\)` is correct and staged-ready if the author wants it as Proposition 31) |
| Exergy/affinity formalisation of the fourth predicate (fable T4, kimi §7) | needs a species table and a declared `\(\Omega\)`: new modelling, not a paragraph |
| MDV, standards amendments, Lean 4 formalisation, certificate schema, time-expanded checker, pilots | project deliverables, not claims of this article |
| fable T9's `\(\sigma\)` for liquidation share | collides with the declared donor-fraction symbol; renamed `\(\varrho\)` if adopted |
| sol's four-layer semantic architecture (physical / observation / classification / report) | an architecture for the reporting system, not a claim of this article; its one manuscript-relevant consequence is the certificate vector, staged as S11 |
| opus U5's `\(\delta_m\)` **as an iff** | the object is right and staged as S2′; the iff is demoted there to a one-sided bound because a decaying deficit need not reach a barrier and upper-barrier cases read the complementary headroom |
| kimi's "locally dictatorial" characterisation | false as stated; the corrected content is in S6 |


---

## S9 · §5.4 or §6.1 — cumulative output can certify a minimum of liquidation

**Anchor:** §5.4, after the specialization-identity paragraph (Remark 16 region); alternative home §6.1 after the three-quantity table.
**Text.**

> **Proposition 31 (Accumulated liquidation from a production relation).** Let the support pool obey `\(\dot A=r-c\)` and let the declared production relation require at least `\(\alpha\ge0\)` units of support use per unit of delivered service, `\(c(t)\ge\alpha Y(t)\)`. Then
> \[ A(0)-A(T)\;\ge\;\alpha\int_0^T Y(t)\,dt-\int_0^T r(t)\,dt . \]
> Whenever the right-hand side is positive, the observed cumulative service certifies that much support liquidation, whatever the interior allocation of fluxes. *Proof.* `\(A(0)-A(T)=\int_0^T(c-r)\,dt\ge\alpha\int_0^TY-\int_0^Tr\)`. `\(\square\)`
> The statement is falsifiable against the record: a stock change smaller than the certified lower bound exposes a wrong coefficient, a missing flux, or a measurement inconsistency, and each of the three is a registered obligation rather than a reconciliation licence.

**Verification:** one line, checked. **Why it is here rather than in S3:** it needs no dual multiplier, so it applies to an application that has a declared `\(\alpha\)` and a service series but no solved `\(\lambda\)`. **Status to print:** conditional on the declared production relation; `\(\alpha\)` is a registered coefficient, not an estimate.

## S10 · §7.1 — the concealed deficit, as an LP companion to the premium

**Anchor:** §7.1, immediately after S6's compensation-premium sentence.
**Text.**

> **Proposition 32 (Worst concealed deficit).** With declared component bounds `\(\ell\le b\le u\)` and a published aggregate value `\(z\)`, the most severe deficit an aggregate of that value can hide in component `\(j\)` is
> \[ \delta_j^{*}(z)=\max\Bigl\{-b_j:\; w^{\top}b=z,\ \ell\le b\le u\Bigr\}, \]
> a linear programme, finite whenever `\(u\)`, `\(\ell\)` are, and positive whenever the aggregate admits any such `\(b\)`. Reported with the premium, it converts the noncompensation theorem into a two-sided audit: the premium measures what the aggregate bought with cross-component trades, `\(\delta_j^{*}\)` measures what it can conceal.
> The exact statement of §7.1 is: for `\(n\ge2\)`, `\(w\ge0\)`, `\(w\ne0\), there is a `\(b\)` with `\(w^{\top}b\ge0\)` and `\(\min_i b_i<0\)`. It is not a claim that no scalar certifies: the non-compensatory minimum-margin functional certifies, at the cost of not saying how many components fail or by how much.

**Verification:** the LP is the article's own box/polytope discipline applied to the aggregate value; the restated claim matches what the section proves. **Author input needed:** which bounds `\(\ell,u\)` to print for each public indicator.

## S11 · §3.1 — the certificate vector, and the third truth value

**Anchor:** §3.1, after the numbering-convention note.
**Text.**

> **Certification state.** The obligations developed in this section are reported as a vector
> \[ \mathrm{Cert}=(\mathsf{Typed},\ \mathsf{Balanced},\ \mathsf{Conserved},\ \mathsf{Positive},\ \mathsf{Admissible},\ \mathsf{Safe},\ \mathsf{Adequate\ service},\ \mathsf{Closed}), \]
> each entry taking one of three values: established, not established, and **not applicable to this object**. The third value is not a failure and the second is not a refutation: a classification record that establishes an accounting identity and nothing else reports `\(\mathsf{Safe}=\text{not applicable}\)`, not `\(\mathsf{Safe}=\bot\)`. The predicates are separately certified and generally non-equivalent, not pairwise independent: the implications that hold among them are exactly the ones stated in Propositions 1–2, and an unlisted implication is not available by inference.

**Verification:** consolidation of statements already proved or registered in §2.1, §3.2–3.3, §5.4, §6.4 and §8; no new mathematics, and the last sentence closes the reading on which safety implies positivity only because the declared barrier set sits in the orthant.

## S12 · §10.1 — composition across the interface (note only, not staged text)

Three audits converge here: conservation certificates compose across ports carrying the same moiety with equal-and-opposite fluxes, positivity composes under donor-limited interface kinetics, and barrier safety does not compose without an interface contract. Each is correct and each is the article's own material in transport language (rule 4 of §7.3; Theorem 11's Nagumo condition at the port; the routing clause of §10.1). It is left as a note because stating it as a theorem requires a definition of ledger morphism and a pushforward lemma, which is new formal apparatus rather than a restatement — an author decision of the same kind as the closure cone in S2.

---

## Citation strings for S2 / S3 / S6 / S7 (verified this turn)

- Gale, D., 1957. A theorem on flows in networks. *Pacific Journal of Mathematics* 7, 1073–1082. — **verified**; use for the S2/T2 cut condition.
- Ahuja, R.K., Magnanti, T.L., Orlin, J.B., 1993. *Network Flows: Theory, Algorithms, and Applications*. Prentice-Hall. — for the lower/upper-bound circulation form, in place of the audits' "Hoffman 1960".
- Prajna, S., Jadbabaie, A., 2004. Safety verification of hybrid systems using barrier certificates. *HSCC 2004*, 477–492. Prajna, S., Jadbabaie, A., Pappas, G.J., 2007. A framework for worst-case and stochastic safety verification using barrier certificates. *IEEE Transactions on Automatic Control* 52, 1415–1428. — **verified**; the 2007 paper is the one that speaks to the article's stochastic surrogates (kimi §9).
- Smith, H.L., 1995. *Monotone Dynamical Systems: An Introduction to the Theory of Competitive and Cooperative Systems*. Mathematical Surveys and Monographs 41, AMS. — **verified** as the citation for the Müller (1926)/Kamke (1932) comparison theorem fable T5 leans on.
- Baez, J., Li, X., Libkind, S., Osgood, N.D., Patterson, E., 2023. Compositional modeling with stock and flow diagrams. *EPTCS* 380, 77–96. doi:10.4204/EPTCS.380.5 — **verified**; the correct anchor for any composition calculus (S12), replacing the audits' "Baez–Pollard".
- Do **not** add: a "Compositional Resource Flow Accounting" reference (does not exist) and, for the companion, no "in review" placeholder: `doi:10.5281/zenodo.22554217` **resolves** (Abaee, A., 2026, *Delay-Induced Regime Change in Harvested Stocks*, posted 2026-09-06) and its record carries the delay-window figures the article cites (Hopf crossings near 3.7 and 150 yr; mobilising review restabilising above ≈6.5 yr).

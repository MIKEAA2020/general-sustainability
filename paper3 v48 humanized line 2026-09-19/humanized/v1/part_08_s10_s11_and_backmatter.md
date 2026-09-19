# 10. What the ledger does not support — the section that says no, with proofs

> **In plain words.** Most papers end by listing what they did achieve. This one ends by listing what it refuses to license, and it proves the refusals. Two results matter here. First, no weighted average of components can certify that each component is safe — and this is shown to fail for *every* possible set of weights, by construction. Second, five bookkeeping rules make double counting impossible rather than unlikely.

## 10.1 Compensatory aggregation is rejected, not merely discouraged

On the unreduced ledger, **no scalar weighting of components is authorized by the accounting itself**. The precise statement is on the feasible balance domain (Definition 1): a weighted sum $\sum_m w_m s_m$ certifies componentwise adequacy $s_m\ge d_m$ for all $m$ on $\mathcal B(x,t)$ **only through an implication proved from the physical restrictions defining the domain** — and, in general, no such implication holds. The feasible domain can admit vectors with a positive aggregate and a negative component, exactly the geometry documented in the composite-indicator literature (Munda and Nardo, 2009). In short: a positive weighted sum never certifies componentwise non-negativity. Scalar summaries may rank and communicate; certification requires the vector.

**Proposition (No weighted certification).** *Let $\mathcal B(x,t)$ be the feasible balance domain (Definition 1). If $\mathcal B(x,t)$ contains a vector with $b_i<0$ and $w^{\top}b>0$ for a fixed $w\ge0$, then the certificate $\{w^{\top}b\ge0\}$ does not imply $b\ge0$; if $\mathcal B(x,t)$ is not known to exclude that pattern, no non-negative weighting is authorized as a componentwise certificate.*

*Proof.* On the exhibited vector the componentwise predicate fails ($b_i<0$) while the weighted predicate holds ($w^{\top}b>0$); the two predicates differ on $\mathcal B(x,t)$. The inverse-horizon score of §6.5.2 (Non-example 1) is the worked witness: a positive aggregate coexisting with componentwise deficits by construction. $\blacksquare$

The conditional form is not an accident of a particular domain. The compensating pattern is constructible against **any** weight, so the failure is universal to the method of weighted certification.

**Theorem (Universal failure of weighted certification).** *Let the ledger have $m\ge2$ components. For every weight vector $w\in\mathbb R^m_+$, $w\ne0$, there exist a typed ledger as in §2, a demand vector $d$, and an admissible state–operation pair $(x,u)$ with $u\in\mathcal U(x,t)$ whose attainable balance $b=O(x,u,\theta)-d$ satisfies $w^{\top}b\ge0$ while $b_m<0$ for some component $m$. No non-negative weighting is therefore a valid componentwise certificate in general.*

*Proof.* Take the two-compartment ledger with stock $x=(x_1,x_2)\in\mathbb R^2_+$, one donor-limited transfer flux $f=kx_1$ from compartment 1 to compartment 2 ($k>0$), identity readout $O(x,u,\theta)=x$, and demands $d=(d_1,d_2)$. Every non-negative state is admissible with the declared flux, because donor limitation holds ($f=0$ at $x_1=0$), so the balance $b=x-d$ is attainable for every $x\in\mathbb R^2_+$; the admissible operating set is the flux declaration itself. Fix $w$ and let $j$ be an index with $w_j>0$. If some $m\ne j$ has $w_m=0$, place the deficit there: choose $x_m<d_m$ and $x_j\ge d_j$, giving $w^{\top}b=w_j(x_j-d_j)\ge0$ while $b_m<0$. Otherwise $w_m>0$ for every $m\ne j$: choose any $m\ne j$ with $x_m<d_m$, and choose $x_j\ge d_j+\big(w_m(d_m-x_m)+\varepsilon\big)/w_j$ for any $\varepsilon>0$. Then

$$w^{\top}b=w_m(x_m-d_m)+w_j(x_j-d_j)\ \ge\ w_m(x_m-d_m)+w_m(d_m-x_m)+\varepsilon=\varepsilon\ \ge\ 0,$$

while $b_m=x_m-d_m<0$. The pair $(x,d)$ is the witness for $w$. $\blacksquare$

The construction **never uses the dynamics**: the failure is a property of non-negative weightings over mixed-sign balances, not of the donor-limited positivity mechanism. Consequently, on any feasible balance domain containing a compensating pair — and Definition 1's domain is exactly that whenever the operating set admits states with mixed balances — no non-negative weighting can stand in for the conjunctive criterion of §3.2. The reading is the algebraic form of the weak-comparability thesis stated in §1.1.

The companion assessment analysis (Author, F., et al., *in review*) proves the *dynamic* form of the same separation for transition operators; the ledger side contributes the *static prerequisite*: the aggregation question is only well posed after the balance domain is declared, and the burden of proof sits on the aggregation, not on the componentwise report.

The same separation holds at the service layer: a weighted sum on $\mathcal B(x,t)$ cannot see the directional support gap $(1-\alpha_{\mathrm{reg}})\bar s$ of Definition 2 — an aggregate that mixes regenerative and non-regenerative provenance never reports which component carries the gap.

In the terms of the ecological-economics literature of §1.1: componentwise adequacy on the typed ledger is **strong sustainability as a conjunctive predicate**; a positive weighted sum is **weak sustainability as a ranking device**. The ledger authorizes the first and does not authorize the second.

## 10.2 The double-counting discipline

Five rules, each carried by a proved or defined statement of this article, jointly prevent double counting and phantom mass.

1. **One balance per moiety.** Conservation laws attach to declared moieties (Theorems 7–8). Adding unlike units — biomass, money, biodiversity indices, exergy — into one conserved scalar is not authorized by any conservation theorem.
2. **Explicit stoichiometry.** Entries are added within an incidence row only when their types and units agree; every conversion is an explicit coefficient in $S^{\top}$, never an implicit sum (§2.1).
3. **Yield routing.** A transformation represented with yield below one must route the omitted fraction to a represented compartment or a declared boundary flow; otherwise the moiety balance holds only after silently dropping the moiety (Theorem 15).
4. **No ghost sinks.** Every primitive with an outflow from some compartment must have its routed inflow represented, and every inflow its source — opposite-sign incidence of the same primitive is checkable column by column. The six-state cancellation of §4.9 shows the check passing, while the same template shows that cancellation without donor-limited admissibility establishes nothing.
5. **Classification labels stay out of the columns.** Reserve-life and resource-threshold quantities answer different questions and share a column only under an explicit convention label (§6.5.3); diagnostic labels never determine material routing (§2.5).

Every unit of mass is routed once: the unit-sum split routing of Theorem 8 and the column-sum-zero incidence of Theorem 9 are the mechanism, and the yield-routing obligation of Theorem 15 is its enforcement. A flux omitted from the ledger is not thereby conserved. A recovery claimed in a quality-neutral loop is not thereby real. A diagnostic index that mixes basins and reserves (the ranking device of §6.5.2) is identified as such in the text that reports it. **Double counting is a representation error, and the representation that prevents it is the contribution.**

## 10.3 Negative and boundary content is first-class

The classification results of §6.5 are negative results stated as such: the anomaly index is not a stock ratio; the reserve-life ratio is not a forecast; the removals-only time is not a depletion diagnostic. The non-reduction boundary of §9 is a rejected mapping with five mathematical reasons. The sink obstructions of §2.4 are empty-kernel mechanisms.

None of these is a failure of the framework. A quantity that answers exactly one question, stated with that question, **is** the framework working — and the framework's claim about itself is limited to the accounting layer it establishes.

## 10.4 Limitations

These are stated as limitations of what follows, not as future work.

1. **(i)** The two-pool exact specialization of the groundwater template remains **open**. The admitted object is the one-pool affine approximation, and **no two-pool model is claimed as established** (§8.2).
2. **(ii)** The phosphorus and groundwater rows are **registered template obligations**: no constitutive content exists behind their identification ladders.
3. **(iii)** The first-passage propositions of §7 concern **declared stochastic surrogates, not the ledger**: they do not compute the ledger's hitting time, do not conserve its mass, and carry the record-relative-barrier and non-claim disciplines.
4. **(iv)** The applied records of §6.5 are classified diagnostics at their stated evidentiary levels — statistical index, arithmetic ratio, removals-only pressure scale — and **none is a calibrated early-warning system or a forecast**.
5. **(v)** The non-reduction boundary of §9 is **permanent mathematics, not a gap**: the closed primitive ledger and the open working system are different completions.
6. **(vi)** The conditional hybrid balance of Theorem 15 stays **conditional**, with its jump-interpretation and yield-routing obligations open per application.
7. **(vii)** The support-saturation limits of §2.6 are **local and finite-time**; neither is a full-system reduction.
8. **(viii)** The article asserts **nothing empirical** about any named resource system beyond the classifications of public data products stated at their source status.

---

# 11. Conclusion

The two failure modes of the introduction — compensatory aggregation and classification drift — are **representation errors**, and the representation that prevents them is the article's content.

Conservation is proved from the incidence structure, not assumed. Positivity is proved from donor limitation, not asserted. Services are readouts, not mass. And depletion time is three quantities, not one.

The closed finite-donor ledger carries its complete theorem set — the natural-block mass identity, orthant invariance, no interior rest at positive effort, the vanishing-extraction rest set (extinction, carrying capacity, and the frozen-biomass face), extraction integrability — and the non-reduction boundary records, with reasons, why the closed ledger and the open working systems of institutional dynamics are **different completions sharing one exact object**.

The depletion numbers of the applied record answer, each, exactly the question their construction poses: a statistical index of record-relative stress, an arithmetic ratio of an economic classification, a pressure scale of one gross loss rate. Stating them with those questions — against the published critiques they corroborate — is what makes them usable. Collapsing them into one "time to depletion" is what makes them false.

The article likewise locates substitution **within** the ledger rather than alongside it. The weak and strong regimes of §1.1 are two readings of one typed stock–flow ledger, distinguished by whether the material cycle closes at the rate of use; that reading is developed once, in the introduction, and is not re-argued here. They are not rival doctrines. The vector reading is the one that carries the certificate; the scalar $b\cdot M$ check of §1.1 is the operational reading on top of it. A substitute is either a recycled flux returned to the regenerating pool, or a non-renewable drawdown on a second compartment — different ledger entries with different statuses.

An exhaustion-horizon estimate built on a reserve figure carries the substitution and technology premises of the reserve classification, not a physical forecast. For ecological-economics measurement, that is the closing statement: not rival doctrines but two readings of one ledger — and the vector reading is what carries the certificate.

---

## Supplementary material

The accompanying file `paper3_supplementary_v8.md` carries: the ten-state admissibility template and its three audited negative witnesses (the non-donor-limited geological exchange, the variance-closure failure, the undefined output functional); the registered identification ladders of the phosphorus and groundwater templates at full detail; the split-assignment mechanism table; the statement inventory with the status of every statement in the main text (theorem with displayed proof, conditional theorem, definition, application record, or boundary statement) — read with the S6 statement-status naming offset, which maps the supplementary's status words to the main text's current labels; and the fisheries cohort record with the archived-pull verification and the executed broad-cohort comparison (S5).

## Declarations

**Data availability.** All computations underlying §6.5 are descriptive arithmetic on the cited public data products: the G3P groundwater anomaly product v1.12 (Güntner et al., 2024; GFZ Data Services, doi:10.5880/G3P.2024.001), the U.S. Geological Survey *Mineral Commodity Summaries* 2026 (the January 2026 release), and the RAM Legacy Stock Assessment Database (Ricard et al., 2012; the cohort pull date is archived in the analysis repository). The parameter tables of §2 are declared parameterizations. No other data were used.

**Declaration of competing interest.** None.

**AI declaration.** GLM (Z.ai), Qwen (AlibabaCloud) and DeepSeek AI assisted with drafting and iterative review.

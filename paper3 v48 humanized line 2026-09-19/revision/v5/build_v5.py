r"""v5 = v4 + the surviving points of both audit batches, at their recommended dispositions.

Sources of every item: review/deployment_plan_v1.md (register rows 1-15), whose verdicts trace to
review/five_audits_joint_verified_v1.md (batch 2, 23 verified proposals) and
review/ledger_audits_verified_v1.md (batch 1, buckets T/P). Every statement below was re-derived
before insertion; nothing is copied from an audit's wording.

Mechanics are identical to build_v4.py: unique-anchor insertions only, missing or ambiguous anchors
are reported and skipped, and no existing sentence is edited except the two authorised replacements
(the §10.1 citation placeholder and the supplementary/code Declarations entries).
"""
import json
SRC = 'revision/v4/paper3_v4.md'
DST = 'revision/v5/paper3_v5.md'
LOG = 'revision/v5/insert_log.json'
t = open(SRC, encoding='utf-8').read()
applied, skipped, replaced = [], [], []
log = []

def _ins(anchor, text, tag, pos):
    global t
    n = t.count(anchor)
    if n != 1:
        skipped.append(f"{tag}: anchor count {n} :: {anchor[:64]!r}")
        return
    i = t.find(anchor) + (len(anchor) if pos == 'after' else 0)
    t = t[:i] + text + t[i:]
    applied.append(tag); log.append({"kind": pos, "tag": tag, "text": text})

def after(anchor, text, tag):  _ins(anchor, text, tag, 'after')
def before(anchor, text, tag): _ins(anchor, text, tag, 'before')
def rep(old, new, tag):
    global t
    n = t.count(old)
    if n != 1:
        skipped.append(f"{tag}: replace count {n}")
        return
    t = t.replace(old, new, 1); replaced.append(tag)
    log.append({"kind": "rep", "tag": tag, "old": old, "text": new})

# ---------------------------------------------------------------- §1.5 antecedents
after("The contribution is the accounting grammar that keeps those tasks separate.",
r"""

**Antecedents.** The bookkeeping idiom and its reconciliation practice are those of material flow analysis (Section 1.1; Brunner and Rechberger, 2004), and the incidence apparatus is that of compartmental systems and reaction-network theory (Jacquez and Simon, 1993; Feinberg, 2019). The two regimes separated in Section 1.3 are the contested distinction of the weak-versus-strong sustainability and critical-natural-capital literatures (Ekins et al., 2003; Neumayer, 2013), and the aggregate-versus-component question is the non-compensatory-aggregation question posed for composite indicators (Munda and Nardo, 2009), where the footprint accounts that animate part of that debate are themselves under assessment (Wackernagel and Beyers, 2019; Lin et al., 2018; Blomqvist et al., 2013). The terminal-condition tradition is viability theory (Aubin, 1991); the horizon arithmetic sits on a bioeconomic and extractive-price literature (Clark, 1990; Tilton, 2003; Tilton and Lagos, 2007), as do the growth-limit arguments with which depletion horizons are confused (Meadows et al., 1972; Daly, 1990). The statistical standards are closer than that genealogy suggests: the System of National Accounts 2025 treats the depletion of natural resources as a cost of production alongside depreciation, following the treatment developed under the SEEA Central Framework (United Nations, 2014; United Nations, 2025), which leaves the classification of depletion settled and the identification of a horizon open. None of these sources is used as a premise here. The objects proved about are the ledger's own.""",
"§1.5 Antecedents paragraph")

# ---------------------------------------------------------------- §1.3 closure cone + deficit
after("The scenario-conditioned hitting time of Definition 5 exists to give that drift a horizon.",
r"""

The two regimes can be stated on the ledger's own objects rather than as attitudes toward them. Let \(S_T\) be the incidence operator of Section 2.2, let \(v\ge0\) be the primitive fluxes under declared capacities \(\bar v\), let \(B_Tu_\partial\) collect the declared boundary transfers, and let \(P\) project a flux vector onto its use columns. Write \(\mathcal K=\{v\ge0:\ S_Tv+B_Tu_\partial=0,\ v\le\bar v\}\) for the admissible stationary flux patterns.

**Definition 21 (Closure cone).** A demanded use vector \(D\) closes at the rate of use if and only if \(D\in P(\mathcal K)\). The closure capacity \(\lambda^{*}=\max\{\lambda:\ \lambda D\in P(\mathcal K)\}\) is a linear programme on the declared capacities, and its feasibility is the cut condition on return capacity (Gale, 1957; Ahuja et al., 1993). Where \(\lambda^{*}\ge1\), the cycle closes at the demanded rate. Where \(\lambda^{*}<1\), every trajectory meeting \(D\) has a non-stationary stock, and by conservation the shortfall appears as support drawdown together with sink accumulation; the deficit share is not a free parameter. Yield inflation is the same statement read outside the projection: demand met with no stationary pattern behind it.

Left-null vectors express conservation; right-null vectors express circulation. The regimes of this section are statements about the second set, and the depletion readouts of Section 6 are statements about the first; neither set's membership follows from the other's.

**Definition 22 (Closure deficit at the use timescale).** For each moiety \(m\), let \(\kappa_m(\tau;\Theta)\in[0,1]\) be the fraction of mobilised flux returned to a usable compartment within lag \(\tau\) under the declared technology and process graph \(\Theta\), and let \(\delta_m=1-\kappa_m(\tau_{\mathrm{use}};\Theta)\) be the closure deficit at the declared use timescale. The deficit is a property of a declared graph at a declared timescale, not a rate of the material itself. Where a mobilisation \(g_m\) is sustained with \(\delta_m\ge\underline\delta>0\), the net drawdown of the support pool is \(\delta_mg_m\), so
\[
\int_0^T(\text{liquidation})\,dt\ \ge\ \underline\delta\int_0^Tg_m\,dt,
\qquad
T\ \le\ \frac{m_0}{\underline\delta\,g_m},
\]
the second inequality being the frozen-rate horizon read on the liquidation flux rather than on gross use. Both bounds are one-sided by construction, and neither reverses in the limit \(\delta_m\to0^+\). A positive deficit is not a barrier-reachability claim: a deficit that decays with the stock need never reach a barrier, and where the binding constraint is an upper barrier the relevant object is the complementary headroom.

Two readings follow from the definition. An indicator that reports a return fraction with no lag argument reports \(\kappa_m(\infty)\) where \(\kappa_m(\tau_{\mathrm{use}})\) is being read; the recycled-input and circularity-rate families are of that form, since a ratio of fluxes carries no timescale. And "a material is waste" is, on this reading, the statement \(\kappa_m(\tau_{\mathrm{use}};\Theta)<1\) for the declared graph, so unlocking a stream is an increase of \(\kappa\) at fixed \(\tau\): measurable, and not in need of a new substance category.""",
"§1.3 Definitions 21-22 closure cone and deficit")

# ---------------------------------------------------------------- §2.2 residual forward reference
after("the two notations denote one object and are used interchangeably below.",
r""" Where no budget is declared for \(d_x\), the residual is not established at zero and is not bounded: the conservation predicate of Section 3.5 then carries the gap rather than closing it, and Definition 23 states the requirement.""",
"§2.2 disturbance-budget forward reference")

# ---------------------------------------------------------------- §3.1 certification state
before("### 3.2 Conservation implies accounting consistency for conserved quantities",
r"""**Certification state.** The obligations developed in this section are reported as a vector
\[
\mathrm{Cert}=(\mathsf{Typed},\ \mathsf{Balanced},\ \mathsf{Conserved},\ \mathsf{Positive},\ \mathsf{Admissible},\ \mathsf{Safe},\ \mathsf{Adequate\ service},\ \mathsf{Closed}),
\]
each entry taking one of three values: established, not established, and not applicable to this object. The third value is not a failure and the second is not a refutation. A classification record that establishes an accounting identity and nothing else reports \(\mathsf{Safe}\) as not applicable, not as refuted; a record that establishes every entry except closure is not thereby unsafe. The predicates are separately certified and generally non-equivalent rather than pairwise independent: the implications that hold among them are the ones stated in Propositions 1 and 2 and in the thermodynamic clause of Section 3.3, and an unlisted implication is not available by inference. The proof obligation attached to each entry, and the certificate vectors of the three classified indicators, are tabulated in the supplementary material.

""",
"§3.1 certification state")

# ---------------------------------------------------------------- §3.5 Definition 23
after("Barrier–conservation compatibility is a feasibility problem, not a slogan.",
r"""

**Definition 23 (Bounded residual).** Conservation consistency is stated with a declared residual budget. For every left-null vector \(\ell\) of \(S_T\), with \(C\) the readout matrix of Section 2.2,
\[
\Bigl|\int_0^T\ell^{\top}C\,d_x(t)\,dt\Bigr|\ \le\ \epsilon_\ell(T),
\qquad \epsilon_\ell\ \text{declared with the model}.
\]
Proposition 1 then reads \(\ell^{\top}Cx(T)=\ell^{\top}Cx(0)+\int_0^T\ell^{\top}C\,b(t)\,dt\) with the disturbance term carried rather than absorbed, and \(\epsilon_\ell\) is the quantity material-flow reconciliation books as statistical discrepancy. An envelope computed without \(\epsilon_\ell\) supports no barrier certificate once the residual-inflated envelope leaves the declared barriers, and where \(\epsilon_\ell\) is undeclared the conservation predicate is reported as not established rather than assumed at zero.""",
"§3.5 Definition 23 bounded residual")

# ---------------------------------------------------------------- §4.8 Theorem 24
before("**The closed-ledger portrait.**",
r"""**Theorem 24 (Critical-margin budget).** Let the declared barrier margins be affine, \(m(x)=Gx+a\ge0\), and let the delivered service rate be \(y=c^{\top}v\) with \(c\ge0\). Suppose some \(\lambda\ge0\) satisfies \(\lambda^{\top}GS_T+c^{\top}\le0\) componentwise, with \(\lambda_j\) carrying the units that convert margin \(j\) into cumulative service. Then \(V=\lambda^{\top}m(x)\) obeys \(\dot V\le-y+\lambda^{\top}Gb\) along every admissible trajectory, and for every trajectory that remains inside the declared barriers
\[
\int_0^Ty(t)\,dt\ \le\ V(x(0))+\int_0^T\lambda^{\top}Gb(t)\,dt .
\]
If additionally \(y\ge y_{\mathrm{req}}\) and \(\lambda^{\top}Gb\le\beta<y_{\mathrm{req}}\), then \(T\le V(x(0))/(y_{\mathrm{req}}-\beta)\).

*Proof.* \(\dot V=\lambda^{\top}G(S_Tv+b)=(\lambda^{\top}GS_T)v+\lambda^{\top}Gb\le-c^{\top}v+\lambda^{\top}Gb\) since \(v\ge0\); integrate and use \(V(T)\ge0\), which holds because \(m\ge0\) and \(\lambda\ge0\). \(\square\)

The search for \(\lambda\) is a linear programme, and its infeasibility is no evidence of safety: it certifies only that this multiplier family does not close. The theorem bounds how long adequate service can coexist with componentwise safety; it is not a scalar certificate, and \(V>0\) establishes nothing about the sign of any individual margin. Theorem 14 is the single-margin instance, and the one-way valve of Section 2.3 is the instance with \(b=0\).

""",
"§4.8 Theorem 24 critical-margin budget")

# ---------------------------------------------------------------- §5.4 Proposition 25
before("## 6. Depletion Arithmetic",
r"""**Proposition 25 (Accumulated liquidation certified by delivered service).** Let the support pool obey \(\dot A=r-c\), and let the declared production relation require at least \(\alpha\ge0\) units of support use per unit of delivered service, \(c(t)\ge\alpha Y(t)\). Then
\[
A(0)-A(T)\ \ge\ \alpha\int_0^TY(t)\,dt-\int_0^Tr(t)\,dt .
\]
Where the right-hand side is positive, the delivered service certifies that much support liquidation, whatever the interior allocation of fluxes.

*Proof.* \(A(0)-A(T)=\int_0^T(c-r)\,dt\ge\alpha\int_0^TY\,dt-\int_0^Tr\,dt\). \(\square\)

The statement is falsifiable against the record rather than self-sealing: a stock change smaller than the certified lower bound exposes a wrong coefficient, a missing flux, or a measurement inconsistency, and each of the three is a registered obligation, not a licence to reconcile. The coefficient \(\alpha\) is a declared relation, not an estimate; the proposition is conditional on it and is not computed anywhere in this article.

""",
"§5.4 Proposition 25 accumulated liquidation")

# ---------------------------------------------------------------- §6.2 Propositions 26-28
before("### 6.3 Upper barriers, exit times, and maintainability",
r"""**Proposition 26 (Sign of the frozen-rate error).** Let \(\dot A=-\varphi(A)\) with \(\varphi>0\) on \((A_{\min},A_0]\), and write the true horizon and the frozen-rate ratio as
\[
T=\int_{A_{\min}}^{A_0}\frac{dA}{\varphi(A)},
\qquad
H^{\mathrm{loc}}=\frac{A_0-A_{\min}}{\varphi(A_0)} .
\]
If \(\varphi\) is nondecreasing in \(A\) then \(T\ge H^{\mathrm{loc}}\), and the frozen-rate number is conservative. If \(\varphi\) is nonincreasing in \(A\) then \(T\le H^{\mathrm{loc}}\), and it is optimistic.

*Proof.* Nondecreasing \(\varphi\) gives \(\varphi(A)\ge\varphi(A_0)\) for \(A\le A_0\), hence \(T\ge(A_0-A_{\min})/\varphi(A_0)\); the second case reverses the inequality. The comparison is the standard one for one-dimensional monotone dynamics (Smith, 1995). \(\square\)

Proportional extraction is the first case, with \(T=q^{-1}\ln(A_0/A_{\min})\) against \(H^{\mathrm{loc}}=(A_0-A_{\min})/(qA_0)\); at \(A_{\min}=0\) the two disagree by being infinite against finite. The sign is estimable from the data the classification already requires, by regressing the decline rate on the stock; it is declared, not computed, in Sections 8.1 and 8.2.

**Proposition 27 (Curvature correction).** On the barrier distance \(u=A-A_{\min}\), let \(\dot u=-\varphi(u)\) and define the dimensionless curvature number
\[
\kappa=\frac{u\,\ddot u}{\dot u^{2}}=\frac{u\,\varphi'(u)}{\varphi(u)} .
\]
For the power-law family \(\varphi(u)=cu^{p}\) one has \(\kappa=p\) identically, and for \(\kappa<1\)
\[
T=\frac{H^{\mathrm{loc}}}{1-\kappa},
\qquad
T<\infty\iff\kappa<1,
\]
while for \(\kappa\ge1\) the integral diverges at the barrier and the family reaches it only asymptotically, so the frozen-rate ratio understates by an unbounded factor. Constant extraction is \(\kappa=0\), where the frozen-rate ratio is exact; stock-proportional decline is \(\kappa=1\), where the true horizon is infinite against a finite ratio; and \(\kappa=\tfrac12\) doubles the horizon exactly, which is the smallest correction with a real effect. The correction is a one-number statement about the bias, and it inherits its input requirement: \(\kappa\) needs \(\ddot u\), which is a second difference of the same noisy series whose first difference the classification already distrusts, so it is reported as declared or not at all. Where \(\varphi\) is not of the family, only the sign statement of Proposition 26 is available.

**Proposition 28 (Reserve-life crossover).** Let reserves obey \(\dot R=-(1-\eta)P\), with production \(P=P_0e^{gt}\), \(g>0\), and let \(\tau=R_0/P_0\) be the reserve-life ratio. Exhaustion of the reserve class occurs at
\[
T=\frac1g\ln\Bigl(1+\frac{g\tau}{1-\eta}\Bigr),
\]
and \(T\ge\tau\) holds to first order in \(g\tau\) exactly when \(\eta\ge\tfrac12g\tau\). A reserve-life ratio therefore bounds the reserve class from above only where reclassification keeps pace with growth. On the article's own pinned record, \(\tau\approx309\) yr at \(g=0.03\,\mathrm{yr}^{-1}\), the condition requires \(\eta\ge\tfrac12g\tau\approx4.6\), which exceeds unity: reclassification would have to outpace extraction itself, and no declared reserve convention admits that. At \(\eta=0\) the same record gives \(T=g^{-1}\ln(1+g\tau)\approx77.6\) yr against the tabulated 309. The direction of the error is therefore fixed by the model class rather than by the data, and the classification of Section 8.2 is strengthened, not changed: the ratio remains an arithmetic relation whose promotion to a forecast is unavailable at every admissible elasticity.

*Proof.* Integrate \(\dot R=-(1-\eta)P_0e^{gt}\) to \(R(T)=0\) and solve; the comparison with \(\tau\) is the first-order expansion \(\ln(1+x)=x-x^2/2+O(x^3)\) at \(x=g\tau/(1-\eta)\). \(\square\)

""",
"§6.2 Propositions 26-28")

# ---------------------------------------------------------------- §6.3 joint statement
after("The full certificate requires the terminal state to lie in the maintainability set.",
r""" One consequence for reporting. The exit time is itself a minimum, over moieties and over both barrier signs, so a statement about its joint distribution is already a componentwise statement: no product of marginal probabilities is required, and none is admissible in its place.""",
"§6.3 joint-probability sentence")

# ---------------------------------------------------------------- §7.1 Propositions 29-30
after("The failure is not an accident of a particular domain. The compensating pattern is constructible against any weight.",
r"""

**Proposition 29 (The certifying aggregator is unique).** Let \(r\in\mathbb R^{n}\) be component adequacies expressed in common units, and let \(\mathcal A:\mathbb R^{n}\to\mathbb R\) be monotone, \(r\le r'\Rightarrow\mathcal A(r)\le\mathcal A(r')\), calibrated, \(\mathcal A(c\mathbf 1)=c\) for every \(c\), and certifying, \(\mathcal A(r)\ge c\Rightarrow r\ge c\mathbf 1\) for every \(c\). Then \(\mathcal A(r)=\min_ir_i\).

*Proof.* Certification at \(c=\mathcal A(r)\) gives \(\min_ir_i\ge\mathcal A(r)\). Since \(r\ge(\min_ir_i)\mathbf 1\), monotonicity and calibration give \(\mathcal A(r)\ge\min_ir_i\). \(\square\)

For any admissible aggregator the compensation premium
\[
\Pi(r)=\mathcal A(r)-\min_ir_i\ \ge\ 0
\]
measures the part of a published aggregate that was produced by cross-component trades. Calibration cannot be dropped: the additively separable functional \(\sum_i\min(0,r_i)\) is continuous, monotone, faithful in the sense that a nonnegative value admits no deficit, and complete in the sense that no deficit forces a negative value; it is not the minimum and it is not calibrated. It reports the depth of the deficits where the minimum reports their existence, and either may be published provided neither is called the other. Nor can monotonicity be strengthened to strict monotonicity while keeping both directions: if a continuous \(\mathcal A\) satisfied \(\mathcal A(r)\ge0\Leftrightarrow r\ge0\), then \(\mathcal A\) would vanish on the faces of the nonnegative orthant, since it is negative wherever some component is and nonnegative on the orthant, and continuity forces equality at the boundary; a strictly increasing functional then cannot take one value at \((0,1)\) and another at \((0,2)\). Certification and strict monotonicity are incompatible, which is why the minimum is not an arbitrary convention.

**Proposition 30 (Worst concealed deficit).** Let the component balances lie in declared bounds \(\ell\le b\le u\), and let \(z\) be a published aggregate value \(z=w^{\top}b\) with \(w\ge0\), \(w\ne0\). The most severe deficit an aggregate of that value can conceal in component \(j\) is
\[
\delta^{*}_j(z)=\max\ \{-b_j:\ w^{\top}b=z,\ \ell\le b\le u\},
\]
a linear programme, finite whenever the bounds are, and positive whenever any admissible \(b\) has \(b_j<0\). Together with the premium it turns the noncompensation result into a two-sided audit: the premium measures what the aggregate bought with trades, and \(\delta^{*}_j\) measures what it can hide. Reported on declared bounds only, it is arithmetic on a published construction; where the bounds are not declared, the value is reported as not established.

""",
"§7.1 Propositions 29-30")

# ---------------------------------------------------------------- §7.2 alarm clause
after("A scalar summary may rank. It may communicate. It cannot certify componentwise adequacy.",
r""" The asymmetry is exact and one-directional: a coarse aggregate refutes, because a violated aggregate barrier is a violated component barrier, and it alarms, because a positive premium is a measured quantity; it does not certify, because the concealed deficit in Proposition 30 can be made positive at any published aggregate value the domain admits.""",
"§7.2 refute/alarm asymmetry clause")

# ---------------------------------------------------------------- §7.2 Proposition 31
before("### 7.3 The double-counting discipline",
r"""**Proposition 31 (Aggregates do not transport event times).** Let two stocks and their sinks obey \(\dot x_i=-kx_i\), \(\dot w_i=kx_i\) with \(k>0\), so that each pair conserves material and remains nonnegative, and let the aggregate \(Z=x_1+x_2\) obey the exact closed dynamics \(\dot Z=-kZ\). The initial states \((x_1,x_2)=(2,98)\) and \((50,50)\) generate the identical aggregate trajectory \(Z(t)=100e^{-kt}\) and, at the common lower barrier \(x_i\ge1\), first hitting times \((\log2)/k\) and \((\log50)/k\). No function of the aggregate trajectory determines the component event time.

Dynamical closure and barrier observability are therefore separate obligations: an exact reduced model is not thereby competent about the events its components are declared to suffer. *Proof.* Direct evaluation of each exponential at its own barrier; the two aggregate trajectories coincide identically. \(\square\)

""",
"§7.2 Proposition 31 event-time non-transport")

# ---------------------------------------------------------------- §8.1 Proposition 32
before("The access structure also matters.",
r"""**Proposition 32 (Boundedness of the persistence index on the declared trend class).** Let \(a_k=-\beta k+\varepsilon_k\) for \(k=1,\dots,n\), with \(\varepsilon_k\) independent of scale \(\sigma\) and \(\beta>0\). Within the declared class, the record minimum lies at the end of the record once the trend dominates the noise, so the fitted distance to that minimum is a noise-scale gap and the index
\[
\frac{\min_ka_k-a_n}{\text{fitted decline rate}}
\]
is \(O_{\mathbb P}(\sigma/\beta)\): bounded in probability as the record length grows, and independent of the stock. A simulation of 400 replicates at each of \(n=10^2,10^3,10^4,10^5\) with \(\beta=\sigma=1\) returns a mean index of 0.21, 0.25, 0.21 and 0.25 yr, and a 90th percentile of 0.81, 0.84, 0.95 and 1.00 yr, while the stock implied by the same series falls by five orders of magnitude; the median is zero at every length, because under a downward trend the current level is usually the record minimum. The index is therefore flat in the record length at the noise-to-trend scale \(\sigma/\beta\), which is the sense in which it cannot be extended into a horizon; the code and the seed are archived with the supplementary material. Lengthening or densifying an anomaly record therefore cannot produce a horizon, because the statistic converges to a trend-detection quantity expressed in years. This is a property of the declared linear-trend class and of the reported simulation, not a claim about any basin.

""",
"§8.1 Proposition 32 index boundedness")

# ---------------------------------------------------------------- §8.2 Tilton positioning
before("### 8.3 The fisheries removals-only pressure time",
r"""The classification addresses the status of the ratio, not the adequacy of the resource base. The reserve-life convention and its long defence against depletion-pessimistic readings are the subject of a separate literature (Tilton, 2003; Tilton and Lagos, 2007), whose arguments about substitution, price-induced discovery and economic recovery are exactly the premises this article registers as carried rather than discharged; nothing here contradicts them.

""",
"§8.2 Tilton positioning sentence")

# ---------------------------------------------------------------- §8.4 Remark 33
before("**Non-example 1 — a boundary of aggregation, not a score of the framework.**",
r"""**Remark 33 (One-signed bias of an aggregate overshoot date).** Let components carry biocapacity \(b_i\) and demand \(d_i\), and form an aggregate overshoot date from the aggregates:
\[
\tau_{\mathrm{agg}}=365\,\frac{\sum_ib_i}{\sum_id_i}=365\sum_iw_ir_i,
\qquad
w_i=\frac{d_i}{\sum_jd_j},
\qquad
r_i=\frac{b_i}{d_i}.
\]
Then \(\tau_{\mathrm{agg}}\) is a demand-weighted mean of the component ratios, so \(\tau_{\mathrm{agg}}\ge\tau_{\min}:=365\min_ir_i\), with equality exactly where every component of positive weight coincides. The difference
\[
\Pi_\tau=\tau_{\mathrm{agg}}-\tau_{\min}=365\sum_iw_i\bigl(r_i-r_{\min}\bigr)
\]
is the compensation premium of Section 7.1 in unit disguise: one-signed, exactly decomposable, unbounded in the dispersion of the components, and computable from published component tables. An aggregate overshoot date is therefore optimistic in a known direction, which is a statement about the construction rather than about any territory, and it is the one applied claim of this section that requires no recomputation of a public dataset to state. No premium figure is reported here, because the component tables of the published construction are not reproduced in this article.

""",
"§8.4 Remark 33 overshoot premium")

# ---------------------------------------------------------------- §9.6 lineage
before("### 9.7 Non-claims of the first-passage section",
r"""The surrogates used here are standard objects, and the section's content is the discipline attached to them rather than the passage-time formulae. The inverse-Gaussian law and its parameterisations are those of the first-passage literature on Brownian motion with drift (Chhikara and Folks, 1989; Redner, 2001); the stochastic machinery is Itô calculus in its textbook form (Øksendal, 2003). The comparison between a surrogate mean and the deterministic margin is a monotone-dynamics statement (Smith, 1995), and the barrier construction is the deterministic safety argument used in hybrid-systems verification, whose stochastic extension is the nearest formal relative of the record-relative discipline of Section 9.4 (Prajna and Jadbabaie, 2004; Prajna et al., 2007). None of these sources supplies a calibrated input: every drift, barrier and noise scale entering Sections 9.2 to 9.5 is declared by the analysis, and the results are statements about the declared class.

""",
"§9.6 surrogate lineage paragraph")

# ---------------------------------------------------------------- §10.1 companion citation + review interval
rep("(Author, D., et al., *in review*; its equation (1) and Section 2.4)",
    "(Abaee, 2026, doi:10.5281/zenodo.22554217; its equation (1) and Section 2.4)",
"§10.1 placeholder replaced by the registered companion DOI")
before("### 10.2 The non-reduction boundary",
r"""The companion analysis supplies the one numerical fact about governance timing that this article may use without re-deriving it: at its calibrated point, annual review under the mobilising law is unstable, and stability returns above a review interval of about 6.5 years, with the two subcritical Hopf crossings of the continuous-delay problem certified near 3.7 years and 150 years. The readout of Section 6.4 inherits the consequence. A margin computed at an interval longer than the admissible one is not conservative, because the declared object it is computed on has already changed between reviews; the admissible interval is a property of the institutional block, is reported there, and is not estimated here.

""",
"§10.1 review-interval sentence")

# ---------------------------------------------------------------- §3.1 numbering convention (kept true by this version's additions)
rep("Definitions 1–6, Theorems 1–15, the remaining propositions, the remarks and the corollary — so Proposition 4, Proposition 6, Proposition 17, Proposition 18 and Proposition 20 are main-counter statements",
    "Definitions 1–6 and 21–23, Theorems 1–15 and 24, the remaining propositions, the remarks and the corollary — so Proposition 4, Proposition 6, Proposition 17, Proposition 18, Proposition 20 and Propositions 25–32 are main-counter statements",
    "§3.1 numbering convention extended to the new labels")

# ---------------------------------------------------------------- inherited delimiter repair (one character)
# The source carries an unclosed inline-math delimiter in the Section 8.4 proof: "\(...i\ne j\}."
# instead of "\(...i\ne j\)."  It renders as a stray brace and leaves the span open through the end
# of the paragraph.  Fixing a delimiter changes no claim; logged so the insert-only reconstruction
# still accounts for every byte.
rep("\\(i\\ne j\\}. Choose any", "\\(i\\ne j\\). Choose any", "§8.4 proof: unclosed \\( delimiter repaired (inherited from source)")

# ---------------------------------------------------------------- References
before("Aubin, J.-P., 1991. Viability Theory. Birkhäuser, Boston.",
r"""Ahuja, R.K., Magnanti, T.L., Orlin, J.B., 1993. Network Flows: Theory, Algorithms, and Applications. Prentice-Hall, Englewood Cliffs. """,
"ref: Ahuja et al. 1993")
before("Blomqvist, L., Brook, B.W., Ellis, E.C., Kareiva, P.M., Nordhaus, T., Shellenberger, M., 2013.",
r"""Baez, J., Li, X., Libkind, S., Osgood, N.D., Patterson, E., 2023. Compositional modeling with stock and flow diagrams. In: Applied Category Theory 2022. Electronic Proceedings in Theoretical Computer Science 380, 77–96. https://doi.org/10.4204/EPTCS.380.5 """,
"ref: Baez et al. 2023")
before("Güntner, A., Sharifi, E., Haas, J., et al., 2024.",
r"""Gale, D., 1957. A theorem on flows in networks. Pacific Journal of Mathematics 7, 1073–1082. """,
"ref: Gale 1957")
before("Redner, S., 2001. A Guide to First-Passage Processes.",
r"""Prajna, S., Jadbabaie, A., 2004. Safety verification of hybrid systems using barrier certificates. In: Hybrid Systems: Computation and Control VII. Lecture Notes in Computer Science 2993, 477–492. Prajna, S., Jadbabaie, A., Pappas, G.J., 2007. A framework for worst-case and stochastic safety verification using barrier certificates. IEEE Transactions on Automatic Control 52, 1415–1428. """,
"ref: Prajna et al.")
before("Tapley, B.D., Bettadpur, S., Ries, J.C., Thompson, P.F., Watkins, M.M., 2004.",
r"""Smith, H.L., 1995. Monotone Dynamical Systems: An Introduction to the Theory of Competitive and Cooperative Systems. Mathematical Surveys and Monographs 41. American Mathematical Society, Providence. """,
"ref: Smith 1995")
before("Wackernagel, M., Beyers, B., 2019.",
r"""United Nations, European Commission, International Monetary Fund, Organisation for Economic Co-operation and Development, World Bank, 2014. SEEA Central Framework: 2012 Technical Implementation. United Nations, New York. Statistical Papers, Series M No. 96. United Nations, 2025. System of National Accounts 2025. United Nations Statistics Division, New York. Adopted by the United Nations Statistical Commission at its fifty-sixth session. https://unstats.un.org/unsd/nationalaccount/sna2025.asp """,
"refs: United Nations 2014 and 2025")

# ---------------------------------------------------------------- Declarations
after("**Supplementary material.** The accompanying file carries the ten-state admissibility template and its three audited negative witnesses, the registered identification ladders of the phosphorus and groundwater templates, the split-assignment mechanism table, the statement inventory with the status of every statement in the main text, and the fisheries cohort record with the archived-pull verification and the executed broad-cohort comparison.",
r""" It additionally carries the proof obligations attached to each entry of the certification state of Section 3.1, the two linear programmes of Definitions 21 and 22 and Theorem 24 with their input requirements, the certificate vectors of the three classified indicators, the promotion-rule table collecting the conditions under which each published ratio may be read as an event time, and the worked ledger exhibit with the code that reproduces every computed figure in Sections 6.2, 7.1, 8.1 and 8.4.""",
"Declarations: supplementary scope extended")
before("**Declaration of competing interest.**",
r"""**Code availability.** The scripts that generate every computed figure in this article — the persistence-index simulation of Section 8.1, the curvature and crossover arithmetic of Section 6.2, the compensation premium and worst-concealed-deficit linear programmes of Section 7.1, and the worked ledger exhibit of the supplementary material — are archived with the supplementary file, with the random seed and library versions recorded in the archive manifest. The scripts read no data other than the public products named in the data availability statement.

""",
"Declarations: code availability")

open(DST, 'w', encoding='utf-8').write(t)
json.dump(log, open(LOG, 'w', encoding='utf-8'), ensure_ascii=False)
print("applied %d, replaced %d, skipped %d" % (len(applied), len(replaced), len(skipped)))
for a in applied:   print("   OK   " + a)
for r in replaced:  print("   REPL " + r)
for s in skipped:   print("   SKIP " + s)
print("chars:", len(t), "| words:", len(t.split()), "| lines:", t.count("\n") + 1)

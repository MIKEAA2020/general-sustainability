# Prompt v2 — audit or extend the composition calculus for typed resource ledgers

**What v1 lacked, and what changed here.** v1 paraphrased the definitions instead of quoting them, left
the readout symbol inconsistent with the article (it said `y = Cv`; the article's readout is
`s = 𝒪(x,u,θ) = Q(θ)v` at §5.1), never fixed the orientation of an exchange flux, asked for "the
sharpest true form" without naming the two hypotheses that are actually wrong (the lift lemma's, and
Prop 39's monotonicity), and did not state the article's reporting vocabulary or claim-status discipline
that any answer must respect. v2 pins all of that and adds the structural questions (associativity,
unit, order-independence, tightness, completeness) that decide whether this is a calculus or a list of
lemmas.

---

You are reviewing Section 3.7 and Section 6.6 of a manuscript, and you may add definitions and
theorems. Nothing else in the manuscript is needed; everything you are entitled to assume is below.
You have no access to any companion paper; do not appeal to one.

## 1. The setting, in the article's own notation

A **typed ledger** is $L=(x,v,S_{\mathcal T},B_{\mathcal T},Q;\mathcal T,\mathfrak u)$:
compartments $x\in\mathbb R^{m}_{+}$, each carrying a material type in $\mathcal T$ and a unit in
$\mathfrak u$; primitive fluxes $v\ge0$ confined to declared boxes $\bar v$; typed stoichiometric
(incidence) operator $S_{\mathcal T}$; boundary matrix $B_{\mathcal T}$ with declared transfers
$u_\partial$; service readout $s=\mathcal O(x,u,\theta)=Q(\theta)v$ with each row of $Q$ declaring its
delivery boundary and unit conversion. Dynamics
$\dot x=S_{\mathcal T}v+B_{\mathcal T}u_\partial+d_x$, where $d_x$ is a declared disturbance whose
residual budget is part of the model: for every left-null $\ell$ of $S_{\mathcal T}$,
$\bigl|\int_0^T\ell^{\top}d_x\,dt\bigr|\le\epsilon_\ell(T)$. **Conservation** of a moiety means exactly
the existence of such an $\ell\ge0$ (not identically zero) with $\ell^{\top}S_{\mathcal T}=0$ and
$\ell^{\top}B_{\mathcal T}=0$.

**Barriers and certificates.** Declared margins $m_i(x)=G_i x+a_i\ge0$, readouts $y=c^{\top}v$. A
*certificate* is any $\lambda\ge0$ with $\lambda^{\top}GS_{\mathcal T}+c^{\top}\le0$ componentwise; it
yields $\int_0^T y \le \lambda^{\top}m(x(0))+\int_0^T\lambda^{\top}Gb\,dt$, and if $y\ge y_{\rm req}$
and $\lambda^{\top}Gb\le\beta<y_{\rm req}$ then $T\le \lambda^{\top}m(x(0))/(y_{\rm req}-\beta)$.
Infeasibility of the search for $\lambda$ is *not* evidence of danger, and is reported as "not
established", never as refuted.

**Closure.** For a demanded use vector $D$ and $\mathcal K=\{v\ge0:S_{\mathcal T}v+B_{\mathcal T}u_\partial=0,\ v\le\bar v\}$,
the **closure capacity** is $\Lambda^{*}=\max\{\mu:\mu D\in P(\mathcal K)\}$ where $P$ projects onto use
columns; closure at the rate of use means $\Lambda^{*}\ge1$. The **closure deficit** is
$\delta_m=1-\kappa_m(\tau_{\rm use})$ with $\kappa_m(\tau)$ the fraction of mobilised flux returned to a
usable compartment within lag $\tau$ — a property of a declared graph at a declared timescale.

**Reporting vocabulary.** Every predicate is reported as *established*, *not established*, or *not
applicable to this object*; every number as *bound*, *extrapolation*, *scenario-conditioned*, or
*illustrative*. Nothing is estimated: rates, capacities, barriers, lags and elasticities are declared
inputs, and a claim conditional on a declared input says so. **Do not soften, strengthen or re-frame any
claim's status**; flag disagreements instead of repairing them.

## 2. The statements under review (quoted, not paraphrased)

**Definition 34 (Composition).** For ledgers $L_1,L_2$ over disjoint compartment sets and an interface
$\Theta=(J,\Phi,\bar v)$ — $J$ a finite set of declared identifications pairing a compartment of each,
$\Phi$ declared exchange fluxes with boxes $0\le f_\varphi\le\bar v_\varphi$ and two named endpoints —
the composition $L_1\oplus_\Theta L_2$ is the ledger on the quotient compartment set
$(\text{ disjoint union})/\!\sim_J$ whose incidence is $\operatorname{diag}(S_1,S_2)$ extended by the
identification rows and the endpoint columns of $\Phi$, readouts carried over on each side.
Admissible iff (i) $\sum_{(a,b)\in J}\mathbf 1\{\text{type}(a)\ne\text{type}(b)\}+\mathbf 1\{\mathfrak u(a)\ne\mathfrak u(b)\}=0$;
(ii) no capacity constrains fluxes of both ledgers unless that sharing is declared; (iii) each exchange
enters one side as an outflow and the other as an inflow of the same magnitude.

**Definition 35 (Interface price).** For part certificates $\lambda_i$ and margins $m_i=G_i x^i+a_i$, and
an exchange $\varphi$ draining compartment $c$ on the paying side,
$\pi_\varphi=(\lambda_1^{\top}G_1)_c-(\lambda_2^{\top}G_2)_c$.

**Proposition 36.** Conservation composes; closure does not. Verified instance: two cycles, each with
demand $1$/yr and return capacity $1$/yr (so each has $\Lambda^{*}=1$), sharing one declared return
capacity of $1.5$/yr, give $\Lambda^{*}=0.75$ and deficit $0.25$; with a shared capacity of $1.0$ the
composition gives $0.50$, and with $2.0$ it gives $1.0$.

**Proposition 37.** The composition is certified for $y_1+y_2$ with budget
$B_1+B_2+\sum_\varphi\pi_\varphi^{+}\bar v_\varphi T$, where $B_i=\lambda_i^{\top}m_i(x^i(0))+\int_0^T\lambda_i^{\top}G_i b_i$;
the interface is free iff all $\pi_\varphi\le0$; with one exchange of box $[0,L]$, certification holds iff
$L\le L_{\max}=(B_1+B_2)/(\pi T)$. Verified instance: $G_1=G_2=1$, $\lambda_1=2$, $\lambda_2=1$ so
$\pi=1$; $B_1+B_2=9$, $T=30$ ⇒ $L_{\max}=0.30$, with $L=0.2$ costing $6\le9$ and $L=0.5$ costing $15>9$.

**Definition 38 / Proposition 39.** Fibre $\mathcal F(z)$ = admissible component initial states whose
induced aggregate equals $z$; $\mathrm T(z)=\{\tau(x_0):x_0\in\mathcal F(z)\}$; identifiable iff
$\mathrm T(z)$ is a singleton. Verified instance: $\dot x_i=-x_i$, $Z=100e^{-t}$, barrier $x_i\ge1$ ⇒
$\mathcal F(z)=\{x_1+x_2=100,\,1\le x_i\le99\}$, $\mathrm T(z)=[0,\log50]=[0,3.9120]$, with the two
recorded starts at $0.6931$ and $3.9120$.

## 3. Tasks

1. **The lift lemma is understated.** Decide whether "every left-null vector of each part lifts to a
   left-null vector of the composition" needs the extra hypothesis that no identification merges
   compartments belonging to *distinct* conserved moieties — i.e. that the map
   $\ell\mapsto \ell\circ\pi_J$ from the composition's left-null space to the direct sum of the parts' is
   injective/surjective as claimed. Give the exact rank condition, and, if it fails, an explicit witness
   (two donors, one identification, both conservations destroyed).
2. **Is this a calculus?** Determine whether $\oplus$ is associative, has a unit (the empty ledger), is
   commutative up to the relabelling isomorphism, and whether $L_1\oplus_{J_1}(L_2\oplus_{J_2}L_3)$
   depends on the order in which the identifications are imposed. For a three-part interface, decide
   whether the total interface cost is $\sum_\varphi\pi_\varphi^{+}\bar v_\varphi T$ or carries a
   many-sided residual; give a 3-part witness either way.
3. **Orientation and sign.** $\pi_\varphi$ is defined by which side "pays". Prove or refute that the
   *cost* $\pi_\varphi^{+}\bar v_\varphi T$ is invariant under reversing the declared direction of
   $\varphi$ (with the corresponding swap of $J$), and state the convention that makes Def 35
   orientation-covariant rather than convention-dependent.
4. **Tightness.** Is the budget of Prop 37 attained by an admissible trajectory, or can the joint
   programme do strictly better? Compute the value function of the exact LP over the fibre product
   (standard form: $\max c^\top v$ s.t. $S v = 0$, $\ell$-rows, box rows, $f_\varphi$ couplings) for the
   instance above and report the gap, with the dual (Farkas) witness that certifies it.
5. **Completeness of the certificate search.** For margin-affine barriers the $\lambda$-search is an LP.
   Is it *complete* for that class (every valid budget arises from some feasible $\lambda$)? What is lost
   and gained for quadratic barriers / sum-of-squares multipliers — state the tractability boundary
   precisely, and say whether Prop 37's sufficiency becomes an iff there.
6. **Fix Prop 39's hypothesis.** "$\tau$ monotone along the fibre" is the wrong condition (here $\tau$ is
   a minimum of two monotone functions, so it increases then decreases). Replace it with the minimal
   correct hypothesis under which $\mathrm T(z)$ is an interval — connectedness of the fibre plus
   continuity of $\tau$ gives an interval, and quasi-concavity/convex superlevel sets give the endpoint
   LPs. Then answer: for nonlinear or non-convex declared constraints, is $\mathrm T(z)$ ever disconnected?
   Give the polyhedral algorithm for the endpoints and its complexity.
7. **Extend to the stochastic case.** With the transfer-noise discipline (process noise on a conserved
   moiety is zero-sum across pools or an explicit boundary term; a diffusion that creates mass is a type
   error), state what $\mathrm T(z)$ becomes — a law on exit times — and whether the aggregate record
   identifies its mean. Then, for $dA=-b\,dt+\sigma\,dW$ with $b\in[b_{\min},b_{\max}]$, give the
   hitting-time comparison that brackets the passage-time law between the two deterministic bracket
   horizons, and the condition under which the bracket is strict.
8. **Connect the dual to substitution.** $\Lambda^{*}$ is an LP optimum; its sensitivity to a declared
   capacity is a dual price. Show whether "substitutability of a moiety" can be *defined* as that finite
   dual price, and, if so, prove that compensation between components is admissible exactly where that
   price is finite and the interface price is non-positive — i.e. whether Prop 36/37 plus Def 21 already
   contain a characterization of weak versus strong readings as properties of the declared substitution
   hypergraph rather than as stances.

## 4. Deliverable and rubric

Return: for each task, either a proof, a counterexample inside the declared class, or a precise statement
that it is open. New definitions must be computational (state the programme, its inputs, and its failure
mode), must not introduce an index, a score, or a new substance category, and must say which predicate
they establish. Every numeric instance must be reproducible from a script you supply; report LPs in
standard form with their dual witnesses. Label each result *established* / *conditional on declared
inputs* / *illustrative*, and keep the article's status words intact. Where you disagree with a
statement, quote it and mark it; do not rewrite it.

# The Formal Mathematical Foundations of Sustainability: A Typed Theorem Atlas

**Paper 2 of the programme's five-paper publication architecture (general-sustainability, A001–A025).** Statements are frozen against the row-closed concordance; proofs are included in full where short and summarized with verified-present status otherwise (the camera-ready version reproduces every proof verbatim from the audited sources).

---

## Abstract

Sustainability analysis across economics, ecology, and governance produces claims about stocks, services, observation, institutions, and time that look commensurable but are not. This article is the theorem atlas of a typed research programme: it collects, in one refereable unit, the formal results the programme has actually established — under exactly which assumptions, at exactly which claim status, and with exactly which failure boundaries. The atlas spans twelve families: core viability calculus; typed hybrid conservation and positivity; noncompensation and substitution feasibility; observation and epistemic viability; recovery and irreversibility; sampled, hybrid, and information-state kernels; projectability and exact reduction; diagnostics and delay certificates; restricted composition; and institutional implementation. Every statement carries a machine-checkable provenance identifier into a 409-row concordance inventory in which each source proposition is linked to canonical notation, assumptions, proof/evidence status, mapping type, and destination paper. The negative results are retained with the same discipline as the positive ones: epistemic kernels can be empty while physical kernels are full; observation fibres can defeat any exact safety certificate; substitution can be infeasible with an explicit dual certificate; coupling can destroy or create viability; and several results hold only conditionally — the atlas never promotes a conditional theorem to an unconditional one. The paper's contribution is two-fold: the results themselves, and the status discipline that makes a cross-domain corpus of sustainability mathematics auditable row by row.

---

## 1 Introduction

### 1.1 The question this paper answers

**Which formal results about sustainability are rigorously established, under which exact assumptions, and how do they compose or fail?**

The programme's intake audit registered twenty-six source manuscripts (A001–A025 plus a versioned master corpus) whose formal content decomposes into 409 inventoried rows — definitions, theorems, propositions, corollaries, conjectures, counterexamples, and research programmes. Left as a distributed corpus, this content cannot be cited, refereed, or reused: notation conflicts across sources, claim statuses are inconsistent, and duplicate statements mask genuine differences in assumptions. This article is the programme's theorem atlas: the canonical mathematical core, stated once, with every assumption explicit and every claim status declared.

### 1.2 What enters this paper

The retained set was selected by a substantive routing pass recorded in `research_program/paper2_retained_row_budget.csv` (63 main rows, 7 bounded-appendix rows) and then verified row by row by the scientific closure campaign over the two primary sources (A001, A002 — both sources read end to end; every inventoried item located; kind, module, mapping type, and evidence status verified per row). Nineteen further rows are carried at the direction of the closure campaign's destination passes and seam closures over seven further sources (A003, A005, A006, A007, A010, A013, A018 — all read end to end, 2026-08-28): the witness-construction and no-scalar rows behind the ledger paper's rejection argument, the response-sign H3 object and its groundwater restatement, the epistemic-institutional kernel pair, the output-feedback obstruction family, the model-audit restatements and algebra, and the multiscale-justice programme. The selection rules, applied family by family:

1. the exact corrected statement and proof are verified;
2. the result is canonical rather than model-specific;
3. it is not duplicated by a stronger row;
4. it is needed for the paper's autonomous question;
5. prerequisites can be stated locally without circular dependence;
6. it fits the main-text proof budget.

Model-specific delay dynamics belong to Paper 4 (named C3/C4 systems); ledger instances to Paper 3; empirical identification and observation-timing to Paper 5; the typed architecture narrative to Paper 1. Where a retained row's primary destination is one of those papers, this atlas states the canonical version and cross-references the owning paper; the atlas is the map, the destination papers own the applications.

### 1.3 Claim-status discipline

Every statement below carries a status label from the programme's claim-status hierarchy (the A002 source's own table, adopted programme-wide):

| Status | Admission rule |
|---|---|
| Axiom/definition | Declares an object, domain, type, or convention; asserts no empirical truth |
| Identity | Follows by construction or direct algebra |
| Theorem | Complete proof under explicit mathematical assumptions |
| Conditional theorem | Complete implication whose hypotheses are not established for every intended application |
| Conjecture | Precise unproved statement with a declared proof gap and disproof route |
| Counterexample/limit | An explicit construction establishing that an implication fails |

Two rules govern this article. **No promotion:** a conditional theorem is never stated as a theorem; the conditionality is part of the mathematical content. **No silent transfer:** a status is not transferred automatically to extensions, reductions, or applications.

### 1.4 Provenance and auditability

Every statement carries its concordance identifier (`CC-A00X-YYY`). The concordance row links the statement to its source location, canonical module, mapping type (exact specialization / projectable reduction / approximation / counterexample-or-limit), evidence status, and destination paper. The two primary sources of this paper (A001, A002) are completely row-closed at content level (152 rows `row_verified`, 2026-08-27): each row's existence, kind, proof presence, module, and mapping were verified against a full read of the source. Content-level acceptance is not theorem-status promotion, and the cross-module interface contract (the conditions under which a theorem transfers between modules) remains an open obligation recorded per row. The complete status ledger of this manuscript appears in §14.

### 1.5 Relationship to the programme

This is Paper 2 of five assured papers. Paper 1 (architecture) states the typed canonical system and its philosophy; this paper carries the mathematics that survives without the philosophy. Papers 3–5 carry the ledger, delay-dynamics, and empirical-identification applications. The monograph reintegrates everything at full length. No paper in the series depends on another for a locally load-bearing definition: each application paper carries a Minimal Working Realization of the canonical objects it needs.

---

## 2 Preliminaries: the typed canonical framework

The objects below are stated once and used throughout. Where the two sources use different symbols for the same object, the bridge is declared in §2.7 and used consistently thereafter. Local notation is retained inside quoted statements where it is unambiguous.

### 2.1 Type system and physical state [CC-A002-001 · axiom/definition]

A type records at least a conserved moiety, compartment, location or boundary, physical unit, and — when invoked — life stage and jurisdiction. Let

$$
x=(x_1,\ldots,x_m)\in\mathcal X_{\rm phys}\subseteq\mathbb R^m_+
$$

be typed physical amounts. Addition across components is permitted in a physical balance only through a declared conversion or moiety map.

### 2.2 Hybrid specialization data [CC-A002-002 · axiom/definition]

A hybrid specialization must additionally declare: a finite or otherwise typed mode set; a Markov phase space for each mode; mode-dependent flow laws; a jump set and branch rule; a reset whose codomain is the applicable phase space; admissible hybrid time domains; an execution rule such as review synchronisation, minimum dwell, or a per-interval jump budget; and an observation map specifying which information about the current state and mode is available. The physical jump equation constrains only the current physical coordinate; it does not by itself supply the remaining reset coordinates, a delayed-history restart, a solution concept, or local finiteness.

### 2.3 The canonical system [CC-A002-003 · axiom/definition]

A canonical sustainability system is the tuple

$$
\mathfrak S=
(\mathcal T,\mathcal Z,S,B,\mathcal V,\Gamma,
\mathcal O,\mathcal A,\mathcal C,\mathcal R,
\mathcal D,K,\mathbb P),
$$

where $\mathcal T$ is the type system; $S,B,\mathcal V$ define admissible physical fluxes and boundaries; $\Gamma$ is a service/technology possibility correspondence; $\mathcal O$ and $\mathcal A$ are observation and assessment operators; $\mathcal C$ and $\mathcal R$ are command and deployment/reset architectures; $\mathcal D$ is a disturbance class with a declared signal space and admissibility rule; $K$ is a safe-and-just set; and $\mathbb P$ is a class of causal observation-based policies. The tuple is not complete as a dynamical system until active modules, domains, flow/reset laws, phase spaces, and solution concepts have been specified.

*Status (source):* this is an architecture, not an empirical model, and not a claim that its modules are identifiable from one data stream.

### 2.4 Four uncertainty levels [CC-A002-004 · axiom/definition]

An application must distinguish: (i) parameter uncertainty within a fixed constitutive model; (ii) observation and assessment uncertainty; (iii) process disturbances and boundary forcing; and (iv) structural uncertainty over a declared model class $\mathbb M$. Robustness over $\mathbb M$ places the model index inside the adverse quantifier or a set-valued transition; it is not represented by a parameter covariance matrix unless equivalence is proved.

### 2.5 Diagnostic types [CC-A002-005 · axiom/definition]

A diagnostic claim must declare which of the following it measures: (i) *throughput excess* — a comparison of typed inflow, extraction, consumption, or waste rates; (ii) *stock drawdown* — a negative stock derivative or integrated typed loss; (iii) *threshold proximity* — a signed margin or distance to a declared boundary; (iv) *resilience loss* — a decline in return rate, viable-control margin, capture basin, or another specified recovery property; or (v) *service or welfare shortfall* — failure of a group-specific service or entitlement constraint. None of these names may be transferred to another type without a proved implication on the declared model class.

### 2.6 Threshold and intergenerational types [CC-A002-006 · axiom/definition]

A threshold is typed as a hard physical boundary, ecological functional boundary, service/basic-needs floor, harm/rights ceiling, precautionary policy trigger, or statistical detection threshold. Its units, spatial support, affected group, authority, uncertainty, and horizon are part of the declaration; a trigger or detection threshold is not thereby a physical tipping point. For generation intervals $I_g$ and group-indexed constraint sets $K_g$, an intergenerational recursive safety criterion requires (i) $z(t)\in K_g$ throughout $I_g$ and (ii) the terminal state to lie in a declared continuation set $C_{g+1}$ from which the next generation's constraints are viable under its policy and disturbance classes. A terminal aggregate stock alone is not this criterion.

### 2.7 Notation bridges

The two primary sources name the same objects differently. The bridges below (from the programme's canonical notation and variant registry) are declared once and used consistently:

| Concept | A002 form | A001 form | Bridge rule |
|---|---|---|---|
| State | $z$ (typed, phase-space declared) | $x$ (control-system state) | $z_q$ at interfaces; local $x$ retained with explicit map |
| Safe set | $K$ (safe-and-just set) | $\mathcal V$ (constraint set) | local $\mathcal V$ allowed with bridge; both are the viability constraint |
| Disturbance | $w\in W$ / declared $\mathcal D$ | $d\in D(x)$ | $w$ for signal segments; $d$ for pointwise values; classes declared |
| Viability kernels | — | $\operatorname{Viab},\operatorname{RViab},\operatorname{EViab},\operatorname{ERViab}$ | names retained only with quantifier, information, horizon, safe-set, and policy/disturbance signatures |
| Reserve | $\Omega$ (frozen specification) | — | $\Omega$ is reserved for the frozen specification object (NV-001); prediction-set families in §8 use it as declared there |

The A001 viability hierarchy is: $\operatorname{Viab}(\mathcal V;U,\pi)$ — the kernel under control correspondence $U$ and information/policy class $\pi$; $\operatorname{RViab}$ — the robust kernel against a disturbance class; $\operatorname{EViab}_{\mathcal I}$ — the epistemic kernel under observation structure $\mathcal I$ (states of information, not physical states); $\operatorname{ERViab}$ — the epistemic robust kernel. Each is a different object; none embeds in another without a theorem.

---

## 3 Core viability and obstruction calculus (family F13)

The four results of this section are the calculus every later family uses: monotonicity, product structure, the sharp distinction between face-level and kernel-level tangency, and the finite-time exit certificate.

**Theorem 3.1 (Constraint monotonicity) [CC-A001-001 · theorem].** If $\mathcal V_1 \subseteq \mathcal V_2$ are closed, then

$$
\operatorname{Viab}(\mathcal V_1) \subseteq \operatorname{Viab}(\mathcal V_2).
$$

*Proof.* Let $x_0 \in \operatorname{Viab}(\mathcal V_1)$. There exists a path with $x(t) \in \mathcal V_1 \subseteq \mathcal V_2$ for all $t$. Hence $x_0 \in \operatorname{Viab}(\mathcal V_2)$. $\blacksquare$

**Theorem 3.2 (Product structure) [CC-A001-003 · theorem].** If $\mathcal P = \prod_\ell \mathcal P_\ell$ is a product of uncoupled systems with constraint sets $\mathcal V_\ell$, then

$$
\operatorname{Viab}\!\left(\prod_\ell \mathcal V_\ell;\; \prod_\ell \mathcal P_\ell\right)
=
\prod_\ell \operatorname{Viab}(\mathcal V_\ell;\, \mathcal P_\ell).
$$

Under coupling, both inclusions can fail: coupling can destroy product viability (Counterexample A.1) or create viability absent in isolation (Example A.2).

*Proof.* Uncoupled: a product path stays in $\prod_\ell \mathcal V_\ell$ iff each component stays in $\mathcal V_\ell$, and the controls are independent. Coupled: see the two constructions in the appendix. $\blacksquare$

**Theorem 3.3 (Face necessity is not kernel necessity) [CC-A001-004 · theorem].** Let $\mathcal V$ be a closed product of intervals and let $\Gamma$ be a face. The Nagumo condition $F(x, U(x)) \cap T_{\mathcal V}(x) \neq \varnothing$ is necessary for $\Gamma \subset \operatorname{Viab}(\mathcal V)$ but not necessary for $\operatorname{Viab}(\mathcal V) \neq \varnothing$.

*Proof.* The first claim is Nagumo's theorem. For the second: take $g(S) = rS(1 - S/C)$, $H_{\min} > g(S_{\min})$, $H_{\min} < rC/4$. On the face $S = S_{\min}$: $\dot S = g(S_{\min}) - H \leq g(S_{\min}) - H_{\min} < 0$, so Nagumo fails. But the resource–sink kernel analysis of the source shows the kernel is $[S_-, \infty) \times [0, K_{\max}]$ with $S_- > S_{\min}$, which is nonempty. $\blacksquare$

**Theorem 3.4 (Finite-time exit certificate) [CC-A001-033 · theorem].** Suppose there is a constraint function $q$, constants $a, \varepsilon > 0$, and a strip $\mathcal S_a = \{x : 0 \leq q(x) \leq a\}$ such that

$$
\sup_{u \in U(x)}
\inf_{d \in D(x)}
D^+ q(x;\, f(x, u, d))
\leq -\varepsilon
\qquad
\forall x \in \mathcal S_a,
$$

where $D^+ q$ is the upper right Dini derivative. Then every trajectory entering $\mathcal S_a$ exits $\{q \geq 0\}$ within time at most $a / \varepsilon$.

*Proof.* Along every admissible controlled trajectory in $\mathcal S_a$, the disturbance can enforce $D^+ q(t) \leq -\varepsilon$. Hence $q(t) \leq q(t_0) - \varepsilon(t - t_0)$, and $q$ reaches zero within $q(t_0)/\varepsilon \leq a/\varepsilon$. $\blacksquare$

This theorem is the obstruction engine of the whole atlas: every "kernel empty" result below either constructs this certificate or argues nonexistence directly.

**Lemma 3.5 (Stability and safety are independent) [CC-A006-004 · lemma — mapping: counterexample/limit].** Local or asymptotic stability of an equilibrium does not imply that the equilibrium belongs to a declared safe set, and membership of a nominal equilibrium in a safe set does not imply robust safety under uncertainty.

*Proof (verified present).* For the first statement take $\dot x=-(x+1)$ with safe set $[0,\infty)$: the equilibrium $x^*=-1$ is asymptotically stable and lies outside the safe set. For the second, take a nominally safe stable system and admit a disturbance class that drives the state outside the set. $\blacksquare$

---

## 4 Typed conservation and physical admissibility (family F01)

*Primary destination note.* The ledger paper (Paper 3) owns the closed-ledger applications and the A018 seam; this section carries the canonical theorems. The non-negative invariance theorem's RFDE mode is one of three modes and does not make this a delay-dynamics result; the named delay systems belong to Paper 4.

**Theorem 4.1 (Typed hybrid conservation) [CC-A002-008 · theorem].** Let $L\in\mathbb R^{m\times k}$ collect $k$ moiety-accounting vectors. Consider a locally finite hybrid execution on its interval of existence and suppose $L^\top S=0$ and $L^\top S^J=0$. Along every classical flow and admissible jump of that execution,

$$
L^\top x(t)-L^\top x(0)
=\int_0^t L^\top B\varphi(s)\,ds
+\sum_{t_j\le t}L^\top B^J\beta_j.
$$

In particular, if all boundary rates and impulses vanish, each component of $L^\top x$ is constant.

*Proof (verified present; summary).* On every open flow segment the null-space condition removes the internal flux contribution, leaving the integrated boundary term; at each jump time the reset contributes $L^\top B^J\beta_j$; summing makes intermediate endpoints cancel telescopically. $\blacksquare$

*Scope (source status):* the balance requires local finiteness of the hybrid execution; it does not rule out finite-time Zeno accumulation in an application, and completeness through such an accumulation requires a separate solution concept and continuation result.

**Corollary 4.2 (Closed positive-moiety bound) [CC-A002-010 · theorem].** Consider a locally finite execution of a closed physical network with zero continuous and impulsive boundary transfer. If it has a strictly positive conservation vector $\ell\in\mathbb R^m_{++}$ satisfying $\ell^\top S=0$ and $\ell^\top S^J=0$ for every active flow and jump mode, then every non-negative trajectory of that execution satisfies

$$
0\le x_i(t)\le\frac{\ell^\top x(0)}{\ell_i}.
$$

*Proof (verified present; summary).* Conservation of the positive moiety gives $\ell^\top x(t)=\ell^\top x(0)$; non-negativity of every component bounds $x_i$ by the conserved total divided by $\ell_i$. $\blacksquare$

**Theorem 4.3 (Non-negative invariance for ordinary, hybrid, and RFDE modes) [CC-A002-011 · theorem].** For each retarded mode, fix a delay $\tau\ge0$ and use the standard phase space $\mathcal C_\tau=C([-\tau,0],\mathbb R^m)$ with the uniform norm; its non-negative histories form $\mathcal C_{\tau,+}$. Assume the physical right-hand side is continuous and locally Lipschitz in the current state (ordinary mode) or in the history under the uniform norm (retarded mode), so a unique local flow exists. For every admissible disturbance and every admissible non-negative current state or history, suppose the current physical value $x$ satisfies

$$
x_i=0 \quad\Longrightarrow\quad [Sv(z,d)+B\varphi(z,d)]_i\ge0
$$

for every physical component $i$ (in a retarded mode $x=\phi(0)$ for $\phi\in\mathcal C_{\tau,+}$). Suppose the execution is locally finite and every ordinary-mode reset and every retarded-mode history restart preserves non-negativity. Then every maximal execution originating in the non-negative cone (with non-negative initial history in retarded modes) has all components non-negative for all times at which it is defined.

*Proof (verified present; summary).* The tangent cone of the non-negative orthant at a boundary point admits only inward directions; the tangency condition makes the vector field subtangential in every mode, and reset preservation handles the jumps; a componentwise contradiction argument at a first exit time closes the proof. $\blacksquare$

*Scope (source status):* the invariance statement requires flow regularity, local finiteness, tangency, and reset preservation to be checked model by model; algebraic cancellation alone does not establish invariance.

**Corollary 4.4 (Donor limitation is sufficient) [CC-A002-012 · theorem].** Under the regularity and reset assumptions of Theorem 4.3, if every primitive outflow from compartment $i$ vanishes when $x_i=0$, all internal inflows are non-negative, and every negative boundary flow is donor limited, then the tangency condition of Theorem 4.3 holds.

*Proof (verified present; summary).* Fix a component at zero and separate the balance into internal inflows (non-negative), primitive outflows (zero by hypothesis), positive boundary inflows, and donor-limited negative boundary flows (zero at $x_i=0$ by donor limitation); every term is non-negative. $\blacksquare$

**Conditional Theorem 4.5 (Bounded-input bounded-state criterion) [CC-A002-013 · conditional theorem].** Let $\mathcal Z_{\rm ad}$ be a declared current-state or history phase space with norm $\|\cdot\|_{\mathcal Z}$, and let $V:\mathcal Z_{\rm ad}\to\mathbb R_+$ be continuous and coercive in that norm. Suppose every maximal execution under consideration is complete and locally finite, $V$ is locally absolutely continuous along its flow intervals, and, for all inputs and disturbances bounded by a declared magnitude $U$, the upper-right Dini derivative satisfies

$$
D^+V(z_t)\le-\alpha V(z_t)+\beta(U),\qquad \alpha>0,
$$

while every reset is non-expansive in $V$. Then

$$
V(z_t)\le e^{-\alpha t}V(z_0)
+\frac{\beta(U)}{\alpha}\left(1-e^{-\alpha t}\right),
$$

so every such trajectory is uniformly bounded in the declared phase-space norm.

*Proof (verified present; summary).* The comparison equation $\dot w=-\alpha w+\beta(U)$ with $w(0)=V(z_0)$ integrates to the displayed bound; non-expansive resets cannot increase $V$ at jump times; the Dini inequality chains the flow intervals. $\blacksquare$

*Why conditional (source status):* completeness, compact-time jump local finiteness, coercive dissipation, and non-expansive resets are substantive assumptions; bounded forcing and donor admissibility alone do not imply them — the source records the explicit counterexample $\dot x=u$ with constant $u>0$: bounded donor-admissible input, unbounded state.

**Remark A.3 (one balance per moiety)** [CC-A002-009 · remark, bounded appendix]: the conservation theorem gives one balance per declared moiety; it does not authorize addition of biomass, money, biodiversity indices, and exergy into a conserved scalar. (Stated in Appendix A with the other scope remarks.)

**Proposition 4.6 (Geological/support-pool noninvariance) [CC-A010-009 · boundary test — mapping: counterexample/limit].** The fixed-target geological exchange $\dot G=-\omega_A(A^{\rm eq}-A)$ is not donor limited: at $G=0$ with $A<A^{\rm eq}$ it gives $\dot G<0$, so the nonnegative geological orthant is not forward invariant. A physically admissible formulation must replace the fixed-target exchange by separate non-negative donor-limited fluxes $e_{GA}(G,A)$ and $e_{AG}(A,G)$ satisfying $e_{GA}(0,A)=0$ and $e_{AG}(0,G)=0$.

*Status:* recorded at its audited verdict as a conservation-admissibility limit of the ten-state audit template; the donor-limited reformulation is a registered obligation, not a discharged construction.

---

## 5 Noncompensation and substitution feasibility (family F02)

**Proposition 5.1 (Domain-qualified noncompensation) [CC-A002-007 · theorem].** Let $n\ge2$ and $w\in\mathbb R^n_{++}$. On the unrestricted balance space, $w^\top \Delta\ge0$ does not imply $\Delta\ge0$: for every component $k$ and every $L>0$, there is a balance vector with $\Delta_k=-L$ and $w^\top \Delta>0$. On a restricted feasible domain $\mathcal B$, the scalar is a component-safety certificate if and only if

$$
\mathcal B\cap\{\Delta: w^\top \Delta\ge0\}\subseteq\mathbb R^n_+.
$$

*Proof (verified present; summary).* Construct $\Delta_k=-L$, $\Delta_j=(w_kL+1)/w_j$ for $j\ne k$, zeros elsewhere: the weighted sum is $+1$ while component $k$ is $-L$. The domain-certificate biconditional is immediate. $\blacksquare$

The proposition rejects *unrestricted* compensation, not every scalar summary: a restricted technology or ecological domain may support a scalar certificate, but the implication must be proved on that domain. The next two results give the two canonical positive forms — a threshold classification and a dual infeasibility certificate.

**Theorem 5.2 (Capital–resource substitution thresholds) [CC-A001-049 · theorem].** For fixed $R > 0$, let $c_{\max}(R) = \sup_{A \geq 0} [F(A, R) - \delta_A A]$ in the dimensionally correct CES specification. Then: (1) if $\sigma < 1$, $F(A,R)$ converges to a finite ceiling and $c_{\max}(R) < \infty$; (2) if $\sigma = 1$, $F(A,R)/A \to 0$ and $c_{\max}(R) < \infty$ for $\delta_A > 0$; (3) if $\sigma > 1$ and $\mu_A < \delta_A$, $c_{\max}(R) < \infty$; (4) if $\sigma > 1$ and $\mu_A > \delta_A$, $c_{\max}(R) = +\infty$; (5) the boundary case $\mu_A = \delta_A$ also gives $c_{\max}(R) = +\infty$. The threshold is

$$
\frac{Y_0}{A_0}\,\alpha^{\sigma/(\sigma-1)}
\gtreqless
\delta_A,
$$

a comparison of two rates, both with units of inverse time.

**Corollary 5.3 (Essentiality and unbounded-substitution thresholds) [CC-A001-050 · theorem].** In the dimensionally correct CES specification, $\sigma = 1$ is the sharp threshold for two distinct properties. (1) *Essentiality of the resource flow:* for all $\sigma \leq 1$, $F(A, 0) = 0$ for every $A$ (the resource is essential); for $\sigma > 1$, $F(A, 0) > 0$ for $A > 0$ (non-essential). (2) *Unbounded substitution:* for fixed $R^* > 0$, $F(A, R^*) \to +\infty$ as $A \to \infty$ if and only if $\sigma \geq 1$; for $\sigma < 1$ output converges to the finite ceiling $Y_0 (1-\alpha)^{\sigma/(\sigma-1)} (R^*/R_0)$.

*Proofs (verified present).* The threshold analysis is a direct computation in the CES parameters; the corollary follows from the limiting forms of $F(A,0)$ and $F(A,R^*)$. Full proofs are reproduced from the source at camera-ready. $\blacksquare$

**Definition 5.4 (Support provenance and directional support gap) [CC-A002-014 · definition].** Partition pathway requirements by declared provenance — for example renewable flow, recovered/recycled material, imports, and non-renewable drawdown — without adding unlike physical units. Let $\Gamma_{\rm all}(z)$ be the service set using all admissible pathways and $\Gamma_{\rm reg}(z)\subseteq\Gamma_{\rm all}(z)$ the set after imposing the declared regenerative, boundary, quality, and exergy restrictions. For a nonzero service direction $\bar s\ge0$, define

$$
\alpha_{\rm reg}(\bar s;z)=\sup\{\alpha\in[0,1]:\alpha\bar s\in\Gamma_{\rm reg}(z)\}.
$$

The vector $(1-\alpha_{\rm reg})\bar s$ is the *directional support gap*. A realised service $s\in\Gamma_{\rm all}\setminus\Gamma_{\rm reg}$ is support-dependent under that declaration even when current service demand is met.

**Theorem 5.5 (Linear substitution alternative) [CC-A002-015 · theorem, finite linear model].** Exactly one of the following holds: (i) there exists a non-negative pathway vector $a\ge0$ satisfying the linear substitution constraints; or (ii) there exist multipliers $\alpha,\beta,\gamma\ge0$ such that

$$
\alpha^\top R+\beta^\top E-\gamma^\top Q\ge0 \quad\text{componentwise},\qquad
\gamma^\top s^{\rm req}>\alpha^\top x+\beta^\top e.
$$

The second statement is a certificate that the declared substitution pathways cannot meet demand within the typed resource and capacity bounds.

*Proof (verified present; summary).* Writing all constraints as $Aa\le\rho$, the alternative is exactly the Farkas lemma pair: primal feasibility or a dual separation certificate. $\blacksquare$

*Scope:* the multipliers are a separation certificate, not universal exchange rates; nonlinear, nonconvex, path-dependent, spatial, or irreversible technologies require their own feasibility analysis (Remark A.4).

**Lemma 5.6 (Compensatory reporting limit) [CC-A007-001 · lemma — mapping: counterexample/limit].** For unrestricted margins $b\in\mathbb R^n$ with $n\ge2$ and any $w\in\mathbb R^n_{++}$, $w^{\top}b>0$ does not imply $b\in\mathbb R^n_+$. The noncompensatory margin discipline follows: safety requires $m\in\mathbb R^{q+p}_+$, and a scalar certificate exists only in noncompensatory form ($\min_i m_i$, or a restricted-domain implication proved from the physical restrictions).

*Proof (verified present).* The two-coordinate witness $b_k=-L$, $b_j=(w_kL+1)/w_j$, $b_i=0$ otherwise, gives $w^{\top}b=1>0$ with $b_k=-L<0$ for any severity $L$. $\blacksquare$

**Proposition 5.7 (Witness construction on the unrestricted balance space) [CC-A013-001 · logical observation with explicit construction — mapping: counterexample/limit].** For any $n\ge2$, any component $k$, any deficit $L>0$, and any $j\ne k$, the witness vector of Lemma 5.6 lies in the positive half-space $\{b: w^{\top}b>0\}$ outside the nonnegative orthant. On a restricted feasible domain $\mathcal B(x,t)$ a scalar certificate requires the separately proved implication $b\in\mathcal B(x,t)$, $w^{\top}b\ge0\Rightarrow b\ge0$; the unrestricted construction decides nothing where the physical restrictions exclude all witnesses, and arbitrarily large compensating surpluses need not be physically attainable in a particular application.

**Proposition 5.8 (No scalar weighting certifies componentwise sustainability) [CC-A018-001 · proposition].** Let $n\ge2$ and let $b\in\mathbb R^n$ be a service-component balance ($b_i>0$ surplus, $b_i<0$ deficit). For every $w\in\mathbb R^n_{>0}$, every index $k$, and every $M>0$ there exist $b, b'$ with $b_k\le-M$ and $w^{\top}b>0$, and with $b_k'\ge M$ and $w^{\top}b'<0$. Hence no threshold on $w^{\top}b$ certifies $b\in\mathbb R^n_+$: no positive linear functional certifies the positive cone, and for $n\ge2$ no linear half-space equals the positive orthant. By contrast $\min_i b_i\ge0$ if and only if $b\in\mathbb R^n_+$, and $\|[-b]_+\|_2=\operatorname{dist}_2(b,\mathbb R^n_+)=0$ if and only if $b\in\mathbb R^n_+$. On a bounded admissible set a conservative scalar threshold can give one-sided safety but still cannot identify which component fails.

*Proof (verified present).* The witness construction of Lemma 5.6 with $L=M$; for $b'$ reverse the sign pattern, $b_k'=M$, $b_j'=-(w_kM+1)/w_j$. $\blacksquare$

---

## 6 Observation and epistemic viability (family F03)

This family carries the paper's central negative results: information structure, not just dynamics, controls what safety is achievable. Three rows of this family have primary destination Paper 5 (the observation-timing empirics paper); they are stated here because the atlas question — what is established and where does it fail — requires the complete obstruction calculus, and the owning paper carries their full treatment.

**Theorem 6.1 (Epistemic emptiness) [CC-A001-020 · theorem — mapping: counterexample/limit].** There exist systems with $\operatorname{Viab}(\mathcal V; U, \pi_{\mathrm{perf}}) = \mathcal V \neq \varnothing$ and $\operatorname{EViab}_{\mathcal I}(\mathcal V) = \varnothing$ for a non-injective observation $\mathcal I$.

*Proof (verified present; summary).* The source constructs $\dot S = u - r(S)$ on $\mathcal V=[1,2]$ with $U(S)=\{0,r(S)\}$ and the constant observation $\mathcal I(S)\equiv 0$: perfect information holds every point of $\mathcal V$; under the uninformative observation the belief is all of $\mathcal V$, no single action is safe for all compatible states, and the epistemic kernel is empty. $\blacksquare$

**Theorem 6.2 (Observer-to-viability transfer with safety buffer) [CC-A001-022 · theorem].** Consider the output-feedback system $\dot x = f(x,u)$, $y = h(x)$, with $x$ not fully observed. Suppose: (1) $K_\varepsilon \subset \operatorname{int} K$ is a compact controlled-invariant subset of the perfect-information kernel $K = \operatorname{Viab}(\mathcal V)$; (2) the perfect-information feedback $u = k(x)$ is Lipschitz with constant $L_k$; (3) the output-feedback controller is $u = k(\hat x)$ with observer estimate $\hat x$; (4) the observer satisfies the exponential convergence bound $\|\hat x(t) - x(t)\| \leq M e^{-\lambda t}\|\hat x(0) - x(0)\|$; (5) there exists a compact invariant subset $K_*$ with $K_\varepsilon \subseteq K_* \subseteq K$ and a constant $\bar e > 0$ such that whenever $x \in K_*$ and $\|k(\hat x) - k(x)\| \leq \bar e$, the trajectory remains in $K_*$; (6) the initial estimation error satisfies $L_k M \|\hat x(0) - x(0)\| \leq \bar e$. Then $K_\varepsilon$ is viable under output feedback.

*Proof (verified present; summary).* Lipschitz feedback and exponential observation error give $\|k(\hat x)-k(x)\|\le L_kMe^{-\lambda t}\|\hat x(0)-x(0)\|\le\bar e$ for all $t\ge0$; the $K_*$-margin absorbs the resulting perturbation and the invariance of $K_*$ closes the loop. $\blacksquare$

**Theorem 6.3 (Robust invariance / tangency) [CC-A001-023 · theorem].** If $K \subseteq \mathcal V$ is closed, $\mathcal R_K(x) \neq \varnothing$ for every $x \in K$, and $\mathcal R_K$ admits a measurable feedback selection $k(x)$ with well-posed closed-loop, then $K$ is robustly controlled invariant, $K \subseteq \operatorname{RViab}(\mathcal V)$. Under the usual regularity and convexity assumptions of discriminating-kernel theory the converse holds, so $\operatorname{RViab}(\mathcal V)$ is the largest closed subset of $\mathcal V$ satisfying the robust tangency condition.

*Proof (verified present; summary).* Measurable selection gives $k$; the closed-loop field satisfies the Nagumo subtangential condition at every point of $K$ because $k(x)\in\mathcal R_K(x)$; the viability theorem for differential inclusions yields, for each initial condition, a trajectory remaining in $K$ simultaneously for every admissible disturbance realization. $\blacksquare$

**Theorem 6.4 (Instantaneous common-action obstruction) [CC-A001-026 · theorem — mapping: counterexample/limit].** Suppose $B$ is a possible information set containing a state on $\partial \mathcal V$, and

$$
\mathcal R_{\mathcal V}^{B}(B) := \bigcap_{x \in B} \mathcal R_{\mathcal V}(x) = \varnothing,
$$

and no informative observation arrives before an action must be chosen. Then $B \notin \operatorname{ERViab}_{\mathcal I}(\mathcal V)$. Every compatible state may be individually robustly viable while the belief is nonviable, because the state-specific safe actions are incompatible.

*Proof status.* The source states the theorem without proof; the row-closure pass registers an explicit one-step proof obligation (the belief is nonviable because any action chosen at $B$ is unsafe for at least one compatible state at the boundary). The one-step proof will be supplied at camera-ready; the theorem's content is witnessed by Example 6.5, which is proved by direct construction.

**Example 6.5 (Hidden-mode conflict) [CC-A001-027 · example — mapping: counterexample/limit; primary destination Paper 5].** Let an unobserved parameter satisfy $\theta \in \{-1,+1\}$, with $\dot z = \theta u$, $u \in \{-1,+1\}$, $z \ge 0$. At $z=0$: if $\theta=+1$ only $u=+1$ is safe; if $\theta=-1$ only $u=-1$ is safe. Both states are individually robustly viable, but $B = \{(0,+1),(0,-1)\}$ admits no common safe action, so $B \notin \operatorname{ERViab}$. This is a purely informational failure: no stochasticity or estimation quality is involved.

**Theorem 6.6 (Delayed-information obstruction) [CC-A001-028 · theorem — mapping: counterexample/limit; primary destination Paper 5].** If every possible action at belief $B_0$ allows a disturbance and a compatible state to reach a locally nonviable boundary point before the next informative observation time $T_{\mathrm{obs}}$, then $B_0 \notin \operatorname{ERViab}$. A sufficient condition is the existence of a constraint function $q$ and $\varepsilon > 0$ with $\inf_{x \in B_t} \inf_{d} D^+ q(x;f(x,u,d)) \leq -\varepsilon$ throughout an uncertainty branch and $T_{\mathrm{obs}} > \inf_{x \in B_0} q(x)/\varepsilon$. Information may be accurate but arrive too late.

*Proof (verified present; summary).* Fix an action and an uncertainty branch; the Dini inequality integrates to $q(x_t)\le\inf_{x\in B_0}q(x)-\varepsilon t$, so the constraint is violated by time $t^*=\inf q/\varepsilon < T_{\mathrm{obs}}$ — before any informative observation can alter the control; since this holds for every action and branch, no observation-based policy can save $B_0$. $\blacksquare$

**Theorem 6.7 (Observer safety buffer) [CC-A001-029 · theorem].** Let $Q = \{x : b_j(x) \ge 0\}$ with each $b_j \in C^1$, and let a nominal feedback $k$ satisfy, on active boundaries, $\inf_{d \in D(x)} \nabla b_j(x) \cdot f(x, k(x), d) \ge \eta_j$ for constants $\eta_j > 0$. Assume the control-perturbation sensitivity $| \nabla b_j(x) \cdot [ f(x, k(\hat x), d) - f(x, k(x), d) ] | \le L_j \| \hat x - x \|$. If the observer guarantees $\| \hat x(t) - x(t) \| \le \bar e$ and $L_j \bar e \le \eta_j$ for all $j$, then the output-feedback law $u(t) = k(\hat x(t))$ preserves $Q$ robustly. If the observer is exponentially convergent, it suffices that $L_j M \|\hat x(0)-x(0)\| \le \eta_j$; otherwise an emergency controller must act until uncertainty falls below the threshold.

*Proof (verified present; summary).* The strict barrier margin $\eta_j$ absorbs the perturbation bound $L_j\bar e$ on the active boundaries, so the perturbed vector field remains subtangential. $\blacksquare$

**Proposition 6.8 (Eroded kernels under output feedback) [CC-A001-030 · proposition].** Suppose: (i) $K$ is robustly invariant under full-state feedback; (ii) the feedback has a strict inward margin on $\partial K$; and (iii) estimation and implementation errors are bounded by $\varepsilon$ in a compatible norm. Then, for sufficiently small $\varepsilon$, an eroded set $K^{-c\varepsilon}$ is invariant under output feedback for some sensitivity constant $c > 0$.

*Proof (verified present; summary).* The strict inward margin absorbs the bounded error: eroding $K$ by a margin proportional to the error bound keeps the nominal feedback inside the strict-margin region, so invariance is preserved under output feedback. $\blacksquare$

**Definition 6.9 (Exact safety certifier) [CC-A002-016 · definition].** For an admissible domain $Z$ and safe set $K\subseteq Z$, an exact certifier based on an observation map $O:Z\to \mathcal Y_{\rm obs}$ is a function $C:\mathcal Y_{\rm obs}\to\{0,1\}$ such that $C(O(z))=1 \Longleftrightarrow z\in K$ for every $z\in Z$.

**Theorem 6.10 (Observation-fibre criterion) [CC-A002-017 · theorem, deterministic exact observation].** An exact safety certifier exists if and only if membership in $K$ is constant on every observation fibre:

$$
O(z_1)=O(z_2)\quad\Longrightarrow\quad[z_1\in K \Longleftrightarrow z_2\in K],
$$

equivalently $K=O^{-1}(O(K))$ on the admissible domain.

*Proof (verified present; summary).* If $C$ exists and $O(z_1)=O(z_2)$, then $\mathbf 1_K(z_1)=C(O(z_1))=C(O(z_2))=\mathbf 1_K(z_2)$. Conversely, if membership is fibre-constant, define $C(y)=\mathbf 1_K(z)$ for any $z$ with $O(z)=y$; fibre-constancy makes $C$ well defined and exact. $\blacksquare$

**Corollary 6.11 (Safety-crossing fibres) [CC-A002-018 · theorem].** If two admissible states have the same observation and lie on opposite sides of a component safety constraint, no exact observation-only certificate exists. The largest set of observations that can soundly be labelled safe without completeness is

$$
\mathcal Y_{\rm certainly\ safe}=\{y\in O(Z): O^{-1}(y)\subseteq K\}.
$$

*Proof (verified present; summary).* A safety-crossing fibre violates the fibre condition of Theorem 6.10; the certainly-safe set is the sound (but possibly incomplete) relaxation. $\blacksquare$

**Proposition 6.12 (Common-action obstruction under output feedback) [CC-A006-008 · proposition — mapping: counterexample/limit; output-feedback form of Theorem 6.4's family].** Suppose no informative observation arrives before the next action must be selected. If the compatible common-action set $\mathcal U_{\rm com}(B)=\varnothing$ for the information state $B$, then $(B,h)$ is not robustly viable under output feedback, even if every compatible physical state is individually viable under full information.

*Proof (verified present).* Output feedback must choose one prescription before the uncertainty within $B$ is resolved; no single action is robustly safe for all compatible states. $\blacksquare$

**Proposition 6.13 (Conditional observer-to-safety transfer) [CC-A006-009 · proposition; conditional-margin form of Proposition 6.8's family].** Let a full-state feedback law have a uniform inward margin $\eta_i>0$ for the active safety constraint $b_i$. If the implementation error induced by an estimator obeys $|\nabla b_i(x)\,[f(x,k(\hat x),w)-f(x,k(x),w)]|\le L_i\|\hat x-x\|$, then the inward inequality is preserved whenever $L_i\|\hat x-x\|\le\eta_i$.

*Proof (verified present).* Subtract the estimation-induced error bound from the full-state inward margin. $\blacksquare$ *Scope:* a local sufficient condition — it motivates eroded safe sets and does not supply an observer or establish estimator bounds.

**Lemma 6.14 (Static diagnostic aliasing) [CC-A007-002 · lemma — mapping: counterexample/limit; static twin of Theorem 6.10].** If a safe and an unsafe point state have the same instantaneous observation, no memoryless deterministic classifier of that observation correctly classifies both.

*Proof (verified present).* A deterministic memoryless classifier assigns one verdict to the shared observation value. $\blacksquare$ *Scope:* the lemma does not establish dynamic unobservability; observer, filter, and set-membership claims require dynamic observability, error, and structural-discrepancy conditions.

**Template 6.15 (Safe learning) [CC-A006-014 · remark/template].** Compatible-state updates depend on action. An action is safely informative only if it is tube-safe and contracts a declared belief-size functional for every compatible observation branch. This is a domain-specific dual-control obligation; learning is not presumed harmless.

---

## 7 Recovery and irreversibility (family F04)

**Proposition 7.1 (Kernel equals its own capture basin) [CC-A001-007 · theorem].** Let $K = \operatorname{Viab}(\mathcal V)$. Then $\operatorname{Capt}_{\mathcal V}(K) = K$, where $\operatorname{Capt}_{\mathcal V}(K)$ is the set of states in $\mathcal V$ from which $K$ can be reached while remaining in $\mathcal V$.

*Proof (verified present; summary).* $K\subseteq\operatorname{Capt}_{\mathcal V}(K)$ by stationary viability; conversely a state from which $K$ is reachable inside $\mathcal V$ can be held in $\mathcal V$ (follow the reaching path), so it is viable. $\blacksquare$

**Corollary 7.2 (Recovery resilience vanishes at the kernel boundary) [CC-A001-008 · theorem — mapping: counterexample/limit].** Every state in $\mathcal V \setminus K$ has infinite recovery time to $K$ if recovery is required to remain in $\mathcal V$. Any definition of "recovery resilience" based on reaching $K$ while staying in $\mathcal V$ is identically zero on $\partial K$.

*Proof.* Immediate from Proposition 7.1: if $x\notin K=\operatorname{Capt}_{\mathcal V}(K)$, no $\mathcal V$-confined path reaches $K$. $\blacksquare$

**Definition 7.3 (Capture basin and the three-part statement) [CC-A001-009 · definition].** Let $\mathcal E \supseteq \mathcal V$ be a closed emergency envelope. Define

$$
\operatorname{Capt}_{\mathcal E}(K)
=
\left\{
x_0 \in \mathcal E :
\exists\, u,\; \exists\, T < \infty:\;
x(t) \in \mathcal E \;\; \forall t \in [0, T],\;\;
x(T) \in K
\right\}.
$$

A complete sustainability statement has three parts: $K \neq \varnothing$; $x_0 \in K$; or at least $x_0 \in \operatorname{Capt}_{\mathcal E}(K)$.

**Definition 7.4 (Envelope-relative recovery time) [CC-A001-010 · definition].** For $x \in \operatorname{Capt}_{\mathcal E}(K)$, define

$$
\tau_{\mathcal E}(x; K)=\inf\left\{T \geq 0 : \exists\, u:\; x(t) \in \mathcal E \;\; \forall t \in [0, T],\;\; x(T) \in K\right\},
$$

and the local recovery-speed measure $v_{\mathrm{rec}}(x,\nu) = \liminf_{\delta \downarrow 0} \delta / \tau_{\mathcal E}(x + \delta\nu; K)$ for a direction $\nu$ pointing outside $K$ but inside $\mathcal E$. The ratio $\delta/\tau$ has units of state per unit time and remains finite when recovery time is proportional to displacement.

**Definition 7.5 (Robust informational capture basin) [CC-A001-011 · definition].** An initial belief $B_0 \subseteq \mathcal E$ belongs to $\operatorname{ERCapt}_{\mathcal E}(K_{\mathcal I})$ if there exists an observation-based policy and a finite $T$ such that, for every compatible initial state, disturbance, and observation error: (1) $x(t) \in \mathcal E$ for all $t \in [0, T]$; and (2) the information state at time $T$ belongs to the epistemic viability kernel, $B_T \in \operatorname{EViab}_{\mathcal I}(\mathcal V)$. Requiring only that the physical state enter the full-information kernel is insufficient: the belief $B_T$ must itself be epistemically viable.

**Definition 7.6 (Worst-case informational recovery time) [CC-A001-012 · definition].** For an initial belief $B_0$,

$$
\tau_{\mathcal E}^{\mathcal I}(B_0)
=
\inf_{\pi}\sup_{x_0, d, v}
\inf\left\{T: x(t) \in \mathcal E \;\; \forall t \le T,\;\; B_T \in \operatorname{EViab}_{\mathcal I}(\mathcal V)\right\},
$$

with $\tau_{\mathcal E}^{\mathcal I}(B_0) = +\infty$ if no such policy exists.

**Proposition 7.7 (Information monotonicity of recovery time) [CC-A001-013 · theorem; primary destination Paper 5].** If $\mathcal I_1 \succeq \mathcal I_2$ ($\mathcal I_1$ more informative), then $\tau_{\mathcal E}^{\mathcal I_1}(B) \le \tau_{\mathcal E}^{\mathcal I_2}(B)$ whenever both are compared from corresponding initial information states.

*Proof.* Any policy implementable under the coarser structure $\mathcal I_2$ is implementable under the finer structure $\mathcal I_1$ by applying the garbling map; hence the optimal worst-case recovery time under $\mathcal I_1$ is no larger. $\blacksquare$

**Definition 7.8 (Capture basin, recoverability, and relative irreversibility — typed form) [CC-A002-020 · definition].** For a constraint set $D$, target $C\subseteq D$, horizon $H\in(0,\infty]$, policy class $\mathbb P$, and disturbance class $\mathcal D$, define

$$
\operatorname{Capt}^{H}_{\mathbb P,\mathcal D}(C;D)
=\{z_0\in D:\exists\pi\in\mathbb P\ \forall d\in\mathcal D\ \exists t_C(d)\le H:\;
z^{\pi,d}(t;z_0)\in D\ \text{for }0\le t\le t_C(d),\quad
z^{\pi,d}(t_C(d);z_0)\in C\}.
$$

A state is *robustly recoverable to $C$* precisely when it belongs to this set. It is *irreversible relative to $(C,D,H,\mathbb P,\mathcal D)$* when it does not. Irreversibility under this definition is therefore indexed by the target, horizon, constraint set, policy class, and disturbance class — it is never an unqualified predicate of a state.

---

## 8 Sampled, hybrid, and information-state kernels (family F05)

This is the largest family: the restricted closed theorem chain for systems under periodic review. The two RFDE results (Theorems 8.8 and 8.9) carry primary destination Paper 4 (the delay-dynamics paper owns the named RFDE families); they are stated here because the kernel construction is one object across its ODE and RFDE instantiations.

**Definition 8.1 (Three policy questions) [CC-A002-019 · definition; primary destination Paper 1/monograph].** Let $z^{\pi,d}(t;z_0)$ be the trajectory under a causal policy $\pi$ and disturbance signal $d\in\mathcal D$, where $\mathcal D$ includes the declared signal space, regularity, bounds, and nonanticipation convention. (1) *Actual-policy safety* asks whether a specified $\pi_0,d_0$ keeps the trajectory in $K$. (2) *Viability* asks whether some $\pi\in\mathbb P$ keeps the trajectory in $K$. (3) *Robust viability* asks whether one admissible causal policy works for every disturbance in $\mathcal D$:

$$
\Viab_{\mathbb P,\mathcal D}(K)
=\{z_0\in K:\exists\pi\in\mathbb P\ \forall d\in\mathcal D:\;
z^{\pi,d}(t;z_0)\in K\ \forall t\ge0\}.
$$

**Theorem 8.2 (Sampled robust-viability kernel) [CC-A002-021 · theorem, restricted architecture].** Assume $K$, $U$, and $W$ are non-empty compact metric spaces, $F$ is continuous, the augmented state is available at each decision, and the policy class contains arbitrary state-feedback selectors. Then: (1) every $K_n$ is compact and $K_{n+1}\subseteq K_n$; (2) $K_n$ is exactly the set of states from which a causal policy can keep the sampled transition in $K$ for at least $n$ transitions against every disturbance sequence; (3) the intersection $K_\infty=\bigcap_{n}K_n$ is the largest robust controlled-invariant subset of $K$ and equals the robust viability kernel of the sampled system.

*Proof (verified present; summary).* Compactness: for compact $A\subseteq K$ the admissible state–action relation $\{(z,u): F(z,u,w)\in A\ \forall w\in W\}$ is closed by continuity and compact; the predecessor is its projection. The finite-horizon characterization is by induction on $n$; the infinite-horizon intersection identity follows because every $n$-step-safe state family is decreasing and compact. $\blacksquare$

**Corollary 8.3 (Monotonicity under policy-set expansion) [CC-A002-022 · theorem].** For fixed $F$, $K$, and $W$, if $U_1\subseteq U_2$, then the sampled robust viability kernels satisfy $K_\infty(U_1)\subseteq K_\infty(U_2)$.

*Proof (verified present; summary).* The predecessor sequences share $K_0=K$ and expand with the action set by induction; the intersections inherit the inclusion. $\blacksquare$

*(The source records the rebound caveat: a larger action set can improve the kernel while worsening other declared objectives — monotonicity is about the kernel object only.)*

**Theorem 8.4 (Finite-clopen observation knowledge kernel) [CC-A002-023 · theorem, finite-clopen sampled observation model].** Under the preceding hypotheses (finite-clopen observation structure): (1) every $\mathcal L_n$ is compact and $\mathcal L_{n+1}\subseteq\mathcal L_n$; (2) $\Omega\in\mathcal L_n$ exactly when a policy in the finite-clopen observation policy class keeps every latent trajectory with initial state in $\Omega$ inside $K$ for the next $n$ transitions, for every disturbance sequence and every symbol sequence induced by those latent trajectories; (3) if every $\mathcal L_n$ is non-empty, then $\mathcal L_\infty=\bigcap_n\mathcal L_n$ is non-empty and is the largest robustly controlled-invariant family of pre-observation prediction sets; and (4) if $O$ is injective on $K$, then for the full-state iterates $K_n$ of Theorem 8.2, $\Omega\in\mathcal L_n \Longleftrightarrow \Omega\subseteq K_n$.

*Proof (verified present; summary).* The hyperspace of compact subsets of $K$ is compact (distance-function embedding); the predecessor acts continuously on it; the finite-clopen filter construction makes the observation update exactly representable; injectivity collapses prediction sets to singletons and identifies the two kernel families. $\blacksquare$

**Definition 8.5 (Held-control tube predecessor) [CC-A002-024 · definition].** Fix $h>0$. Let $\mathsf X$ be a metric state space, $K\subseteq\mathsf X$, $U$, $W_h$ non-empty compact metric spaces, and $\Phi:[0,h]\times K\times U\times W_h\to\mathsf X$ continuous with $\Phi(0,z,u,w)=z$. The element $w\in W_h$ encodes an admissible disturbance segment and any registered model branch over one held interval, while $u$ is held fixed. For compact $A\subseteq K$, define

$$
\Pre_h^{\rm tube}(A)=
\left\{z\in K:\begin{array}{l}
\exists u\in U\ \forall w\in W_h:\\
\Phi(t,z,u,w)\in K\quad\forall t\in[0,h],\\
\Phi(h,z,u,w)\in A
\end{array}\right\}.
$$

A connection to the continuous disturbance class $\mathcal D$ is exact only when $W_h$ is declared to encode it exactly.

**Theorem 8.6 (Inter-sample-safe sampled kernel) [CC-A002-025 · theorem, restricted fixed-period full-state model].** Under the hypotheses of Definition 8.5, suppose the augmented state is available at each review and arbitrary state-feedback selection is allowed. Set $K^{\rm tube}_0=K$, $K^{\rm tube}_{n+1}=\Pre_h^{\rm tube}(K^{\rm tube}_n)$. Then every $K^{\rm tube}_n$ is compact, the sequence is decreasing, and $K^{\rm tube}_n$ is exactly the set of initial states from which a causal fixed-period held-control policy keeps every point of the first $n$ arcs in $K$. Moreover $K^{\rm tube}_\infty=\bigcap_n K^{\rm tube}_n$ is the largest subset $C\subseteq K$ such that, for every $z\in C$, one held action keeps the entire next arc in $K$ for every $w\in W_h$ and places every endpoint in $C$. Concatenating the resulting review-time selections therefore guarantees inter-sample safety for all times in the fixed-period held-control model.

*Proof (verified present; summary).* The admissible state–action relation for tube containment is closed (continuity of $\Phi$ on a compact domain); its projection is compact; the $n$-step characterization is induction; the largest-invariant-set property is the intersection argument of Theorem 8.2 applied to tubes. $\blacksquare$

**Theorem 8.7 (Finite-clopen inter-sample-safe knowledge kernel) [CC-A002-026 · theorem, finite-clopen fixed-period held model].** The preceding tube construction, lifted to the finite-clopen observation structure: (1) every $\mathcal M_n$ is compact and $\mathcal M_{n+1}\subseteq\mathcal M_n$; (2) $\Omega\in\mathcal M_n$ exactly when one policy in the finite-clopen class keeps every physical trajectory with initial state in $\Omega$ inside $K$ at every instant of the next $n$ held intervals, under each admissible disturbance sequence and its resulting observation record; (3) $\mathcal M_\infty=\bigcap_n\mathcal M_n$ is the largest robustly tube-invariant family of pre-observation prediction sets, non-empty whenever every $\mathcal M_n$ is; and (4) if the observation map is injective, $\Omega\in\mathcal M_n \Longleftrightarrow \Omega\subseteq K_n^{\rm tube}$ for the full-state tube iterates.

*Proof (verified present; summary).* The tube maps $(A,u)\mapsto\{\Phi(t,z,u,w)\}$ are continuous into the hyperspace; the finite-clopen filter construction composes with them exactly as in Theorem 8.4; injectivity again collapses the two families. $\blacksquare$

**Conditional Theorem 8.8 (Sampled RFDE finite-clopen knowledge kernel) [CC-A002-027 · conditional theorem, compact single-delay history model; primary destination Paper 4].** In the sampled single-delay RFDE model on the compact equi-Lipschitz history class: (1) every $\mathcal Q_n$ is compact and $\mathcal Q_{n+1}\subseteq\mathcal Q_n$; (2) $\Omega\in\mathcal Q_n$ exactly when one causal, stage-dependent observation policy keeps the current value of every RFDE trajectory with initial history in $\Omega$ inside $K$ at every instant of the next $n$ held intervals, for every piecewise-constant disturbance sequence and every induced symbol sequence; and (3) $\mathcal Q_\infty=\bigcap_n\mathcal Q_n$ is the largest robustly tube-invariant family of compact history prediction sets; a declared prior $\Omega_0$ admits one indefinitely safe policy for all of its histories exactly when $\Omega_0\in\mathcal Q_\infty$. When $\tau=0$ the canonical identification of a history with its current value recovers the ODE kernel of Theorem 8.4.

*Why conditional (source status line: "Conditional theorem, compact single-delay history model"):* the total jointly-continuous held-solution map and the compact equi-Lipschitz history class are substantive hypotheses, not consequences of the sampled architecture. The theorem environment carries a complete proof; the source's own status line demotes it to conditional.

**Conditional Theorem 8.9 (Review-synchronised hybrid RFDE knowledge kernel) [CC-A002-028 · conditional theorem, review-clock hybrid RFDE; primary destination Paper 4].** Under the compactness, total-solution, speed, continuous phase-reset, clopen review-branch, finite-clopen observation, and arbitrary-selector hypotheses: (1) every $\mathcal H_n^H$ is compact and nested; (2) $\Omega\in\mathcal H_n^H$ exactly when one causal observation policy keeps every current value in $K$ throughout the next $n$ review intervals, including every pre-reset and post-reset review state, against every admissible reset- and flow-parameter sequence; and (3) $\mathcal H_\infty^H=\bigcap_n\mathcal H_n^H$ is the largest robustly tube-invariant family of compact hybrid-history predictions; a declared prior $\Omega_0$ admits one indefinitely safe policy exactly when $\Omega_0\in\mathcal H_\infty^H$.

*Why conditional:* the review-clock hybrid RFDE hypotheses (total solutions, continuous phase-space reset, speed bounds) are declared, not derived.

**Proposition 8.10 (Outer semicontinuity does not close universal tube constraints) [CC-A002-029 · proposition — mapping: counterexample/limit].** Compact-valued outer semicontinuity of the reachable-tube and endpoint maps is not sufficient to make the universal-safety predecessor closed.

*Proof (verified present; summary).* The source constructs the compact state space $[0,1]$, safe set $[0,1/2]$, a singleton action space, and the tube map $\mathscr T(z)=\{0,z\}$ for $z>0$, $\mathscr T(0)=\{0,1\}$: outer semicontinuous at every point, yet the universal-safety predecessor fails to be closed at the grazing guard. $\blacksquare$

This proposition is why Theorem 8.11 needs Hausdorff continuity, a strictly stronger hypothesis.

**Conditional Theorem 8.11 (Bounded-jump hybrid ODE kernel with continuous exact tubes) [CC-A002-030 · conditional theorem, continuous exact hybrid tubes].** Assume $U$ is compact; every admissible hybrid arc is ordinary-time complete on $[0,h]$ and obeys the declared finite jump budget; and the exact non-empty compact reachable-tube and endpoint maps are Hausdorff-continuous. Under arbitrary review-time state-feedback selectors, every $K_n^M$ is compact, the sequence is nested, and $K_n^M$ is exactly the set of states from which one held-command policy keeps every admissible hybrid arc in $K_H$ for $n$ review intervals. The intersection $K_\infty^M=\bigcap_nK_n^M$ is the largest robustly tube-invariant set for this fixed-review hybrid game. The finite-clopen observation lift carries the same properties with the injective collapse.

*Why conditional:* the continuous-exact-tube hypothesis is the exact price of defeating Proposition 8.10; it is declared, not derived from the hybrid structure.

**Definition 8.12 (Compact sampled information model) [CC-A002-032 · definition].** Fix $h>0$. Let $I,U,W_I$ be non-empty compact metric spaces, $K\subseteq\mathsf X$ compact, and $\mathsf B:I\to\mathcal K_c(\mathsf X)$, $\mathsf T:[0,h]\times I\times U\times W_I\to\mathcal K_c(\mathsf X)$, $G:I\times U\times W_I\to I$ continuous (set-valued continuity in the Hausdorff metric) with $\mathsf T(0,i,u,w)=\mathsf B(i)$ and $\mathsf T(h,i,u,w)\subseteq\mathsf B(G(i,u,w))$. The information state $i_k$ is assumed computable from the available observation–action history; the compact parameter space $W_I$ parametrises the admissible process, registered-model, and next-observation branches exactly.

**Theorem 8.13 (Restricted sampled information-state tube kernel) [CC-A002-033 · theorem, restricted compact information model].** Under Definition 8.12, assume arbitrary selectors on the available information state are admissible. Set $I_0=I_K$, $I_{n+1}=\Pre_I^{\rm tube}(I_n)$. Then $I_K$ and every $I_n$ are compact, $I_{n+1}\subseteq I_n$, and $I_n$ is exactly the set of information states from which one causal information-state policy guarantees latent-state safety throughout the next $n$ held intervals. The intersection $I_\infty=\bigcap_n I_n$ is the largest robust tube-invariant subset of $I_K$. Any selector that keeps the next information state in $I_\infty$ guarantees $x(t)\in K$ for every actual branch represented by the model and for all inter-sample times.

*Proof (verified present; summary).* $I_K$ is closed by Hausdorff continuity of $\mathsf B$; the tube predecessor is compact by continuity of $\mathsf T$ and $G$ on compact domains; the $n$-step and largest-invariant characterizations are the standard induction-plus-intersection argument. $\blacksquare$

**Conditional Theorem 8.14 (Finite-time sample-and-hold convergence) [CC-A002-034 · conditional theorem, finite-horizon consistency].** Fix $T<\infty$. Suppose there are $h_0>0$ and a compact set $N$ such that, for every $0<h\le h_0$, the exact trajectory, the sampled trajectory, and the one-step exact and frozen-input comparison arcs initiated at sampled review states all exist on the required portions of $[0,T]$ and remain in $N$. Suppose $f$ and $g$ are continuously differentiable on a neighbourhood of $N$ with bounded derivatives there, deployment is immediate, assessment is exact and contemporaneous, and no command projection or event trigger activates. With common initial conditions, the piecewise-held sampled system converges uniformly on $[0,T]$ to the continuous-controller system as $h\to0$; the global error is $O(h)$.

*Why conditional:* the comparison-arc existence, compact trapping, and no-trigger hypotheses are substantive; the result is a finite-horizon consistency statement, not an infinite-horizon equivalence.

*(Scope remark A.5, bounded appendix: what the conservation and BIBS theorems require before they apply to the restricted hybrids — none of those conditions follows from a history reset, a jump budget, or the canonical tuple.)*

---

## 9 Projectability and exact reduction (family F06)

**Definition 9.1 (Four model maps) [CC-A002-035 · definition; primary destination Paper 1/monograph].** A *specialisation* fixes parameters or restricts to an invariant subset. An *exact projection* semiconjugates full and reduced flows. An *approximation* has a declared residual or error bound. A *singular reduction* supplies a small parameter, a limiting invariant object, and convergence on a stated time domain.

**Theorem 9.2 (Projectability criterion) [CC-A002-036 · theorem — mapping: projectable reduction].** Let $\dot z=F(z)$ have unique solutions on a domain $Z$, and let $p:Z\to R$ be continuously differentiable. There exists a reduced vector field $G$ satisfying the semiconjugacy $p(\Phi_t(z))=\Psi_t(p(z))$ for the full and reduced flows only if

$$
Dp(z)F(z)=G(p(z)).
$$

Conversely, if this holds and the reduced system has unique solutions, then the semiconjugacy holds while both solutions exist.

*Proof (verified present; summary).* Differentiate the semiconjugacy at $t=0$; the converse integrates the fibre-constant field $G$ on the image and pushes forward. $\blacksquare$

**Corollary 9.3 (Fibre obstruction) [CC-A002-037 · theorem — mapping: counterexample/limit].** If there exist $z_1,z_2$ with $p(z_1)=p(z_2)$ but

$$
Dp(z_1)F(z_1)\ne Dp(z_2)F(z_2),
$$

then no exact autonomous reduced model on that projection exists.

*Proof.* The projectability equation would evaluate $G(p(z_i))$ two ways. $\blacksquare$

**Theorem 9.4 (Support-saturated logistic stock limit) [CC-A002-038 · theorem, partial reduction — mapping: approximation; primary destination Paper 3].** Fix $T<\infty$ and non-negative parameters $\mu,\delta,c,q$. For $\kappa>0$, assume $A_\kappa$ is measurable, $A_\kappa(t)\ge a_0>0$, $0\le X_\kappa(t)\le X_{\max}$, and the common effort $E\in L^\infty([0,T])$. Assume the corresponding absolutely continuous solutions exist on $[0,T]$, and let $X_0$ solve

$$
\dot X_0=(\mu-\delta)X_0-cX_0^2-qE(t)X_0
$$

with the same initial value. Then the vector-field defect is bounded by $\big|\mu X_\kappa \tfrac{A_\kappa}{\kappa+A_\kappa}-\mu X_\kappa\big|\le\frac{\mu X_{\max}}{a_0}\kappa$, and $\sup_{t\le T}|X_\kappa(t)-X_0(t)|=O(\kappa)$. If $\mu>\delta$ and $c>0$, the limit equation has the logistic form $\dot X_0=rX_0(1-X_0/K_{\log})-qE(t)X_0$ with $r=\mu-\delta$ and $K_{\log}=(\mu-\delta)/c$.

*Proof (verified present; summary).* The saturation-defect bound is algebraic; the trajectory bound is Grönwall on the defect; the logistic form is a rearrangement. $\blacksquare$

**Theorem 9.5 (Logistic variance correction and curvature bound) [CC-A002-039 · theorem, static spatial aggregation — mapping: approximation].** Fix $r,q\ge0$ and a logistic carrying capacity $K_{\log}>0$. Let $X$ be a square-integrable spatial stock field on a probability-normalised domain, with mean $\bar X$, and $E_s$ a square-integrable effort field with mean $\bar E$. Then

$$
\mathbb E\!\left[rX\left(1-\frac{X}{K_{\log}}\right)-qE_sX\right]
=r\bar X\left(1-\frac{\bar X}{K_{\log}}\right)
-\frac{r}{K_{\log}}\operatorname{Var}(X)
-q\bar E\bar X-q\,\operatorname{Cov}(E_s,X).
$$

More generally, if $X$ is supported in an interval $I$, $f\in C^2(I)$, and $M=\sup_{u\in I}|f''(u)|<\infty$, then $\big|\mathbb E[f(X)]-f(\mathbb E[X])\big|\le\frac{M}{2}\operatorname{Var}(X)$.

*Proof (verified present; summary).* The variance correction is an exact identity (expanding the square); the second bound is Taylor's theorem with the bounded second derivative. The variance identity is exact; the curvature bound is the error-bound half, which is why the family carries the approximation mapping. $\blacksquare$

*Restatement record (model-audit source) [CC-A010-004, CC-A010-005 · identities].* The model-audit source states the logistic variance correction $\mathbb E[R(X)]=r\mu_X(1-\mu_X/K)-(r/K)\operatorname{Var}(X)$ and the general $C^2$ curvature bound $|\mathbb E[f(X)]-f(\mathbb E[X])|\le\tfrac12\|f''\|_{\infty,I}\operatorname{Var}(X)$ independently; both are the Theorem 9.5 family, recorded at their audited status with the source's own caveat that neither identity closes the dynamics of the variance — exact dynamic moment closure occurs only for special functional forms or distributions.

**Conjecture 9.6 (Finite-time reduction to the five-state core under residual macroeconomic feedback) [CC-A018-006 · conjecture].** Assume the strict specialisation is relaxed so that a $C^1$ macroeconomic feedback of size $\varepsilon$ remains, and assume the scale, Hurwitz, and Lipschitz hypotheses of the source. Then for every finite $T>0$ there exist $\varepsilon_0,C>0$ such that for all $\varepsilon\in(0,\varepsilon_0)$ the specialised solution tracks the five-state core: $\sup_{t\in[0,T]}\|x^\varepsilon(t)-x^0(t)\|\le C(\varepsilon+\omega_A T)$ and $\|y^\varepsilon(t)-h(x^\varepsilon(t))\|\le C(\varepsilon+\omega_A T)+Ce^{-\gamma_y t/\varepsilon}$ on $[0,T]$; if $y^\varepsilon(0)=h(x^\varepsilon(0))+O(\varepsilon)$ the boundary layer is absorbed and both suprema are $O(\varepsilon+\omega_A T)$, the $\omega_A T$ term being absent when the geological pool is exactly frozen (add $O(1-\sigma_{\rm geo})$ for a finite reservoir).

*Status:* conjecture (conditional on the source's Tikhonov spectral hypothesis, which a finite-difference sweep supports on the literature-anchored class but which is not proved on the whole domain). Under the strict specialisation the triangular-projection theorem applies instead and no conjecture is needed. The delay-dynamics paper (Paper 4) inherits exactly this statement as the hypothesis behind its Hopf-persistence theorem.

---

## 10 Diagnostics and delay certificates (family F07)

**Conditional Theorem 10.1 (Local-horizon bracket) [CC-A002-040 · conditional theorem, local diagnostic].** Suppose $0\le\epsilon<1$ and $y$ is continuously differentiable on $[0,H_*]$ for some $H_*\ge H_{\rm loc}/(1-\epsilon)$, and suppose throughout that interval that $(1-\epsilon)v_0\le-\dot A(t)\le(1+\epsilon)v_0$. Then a first hitting time $T_A\in[0,H_*]$ exists and satisfies

$$
\frac{H_{\rm loc}}{1+\epsilon}\le T_A\le\frac{H_{\rm loc}}{1-\epsilon}.
$$

*Why conditional:* a local diagnostic under slow rate variation — the bracket degrades without the differentiability and rate-band hypotheses. *Proof (verified present):* integrate the rate bounds between the hitting endpoints.

**Conditional Theorem 10.2 (Small-gain delay-independent stability) [CC-A002-041 · conditional theorem, sufficient certificate; primary destination Paper 4].** For the linear delay system, if for some $\alpha_0>\beta_0\ge0$ the logarithmic matrix measure satisfies $\mu_*(A_0)\le-\alpha_0$ and $\|A_1\|_*\le\beta_0$, then the zero solution is exponentially stable for every fixed $\tau\ge0$. A valid decay rate is the unique $\eta>0$ satisfying

$$
\eta=\alpha_0-\beta_0e^{\eta\tau}.
$$

*Why conditional:* a sufficient certificate via the Halanay-type argument — the unique decay rate exists because the right side is a contraction in $\eta$; the small-gain constants are substantive hypotheses. The delay-dynamics paper (Paper 4) owns the family; the atlas records the certificate.

**Proposition 10.3 (Effort sensitivity coefficients of the audit template) [CC-A010-013 · algebraic result, registered audit template].** At a regular interior equilibrium of the delayed-effort audit template with deployable-capital gate $g_0\in(0,1)$, the effort sensitivities are $C_Z=h_0g_0\eta E^*/\Delta_{\rm ref}$ and $C_K=\mu_EE^*(1-g_0)/(K_0g_0)$. $C_Z$ is the local sensitivity of effort growth to the delayed decline signal, multiplied by the gate; $C_K$ becomes a damping pathway only through its coupling to the separate capital dynamics, not by its sign alone. The factor $1/g_0$ cannot be extrapolated to $g_0=0$, where the assumed regular positive interior branch and the algebra behind the coefficients need not persist.

**Proposition 10.4 (Interior effort upper bound of the audit template) [CC-A010-014 · algebraic result, registered audit template].** An interior equilibrium with $Z^*=0$ and $E^*>0$ must satisfy $h_0g_0(\delta_0-\eta(E^*)^2/E_{\max})=\mu_EE^*>0$, hence $E^*<\sqrt{\delta_0E_{\max}/\eta}\approx0.573$ at $\delta_0=0.3$, $E_{\max}=1$, $\eta=0.914$. This is an equilibrium consequence of placing the linear loss outside the multiplicative gate, not a failure of boundary invariance ($\dot E\ge0$ at $E=0$ and $\dot E<0$ at $E=E_{\max}$ both hold); moving the loss terms defines a different model and requires renewed analysis.

---

## 11 Restricted composition and coupling (family F10)

**Theorem 11.1 (Compositional viability) [CC-A001-088 · theorem].** Suppose each subsystem has an input tolerance $\bar z_i$ such that $\|z_i\| \leq \bar z_i$ implies $\exists\, u_i : D^+ b_i(x_i) \geq 0$ on $\partial Q_i$. If

$$
\sup_{x \in \prod_j Q_j} \|C_i(x_{-i})\| \leq \bar z_i\qquad \forall i,
$$

then $\prod_i Q_i$ is controlled invariant.

*Proof.* For each subsystem $i$: when $x_i \in \partial Q_i$ and $\|z_i\| \leq \bar z_i$, there exists $u_i$ keeping $x_i$ in $Q_i$. The coupling constraint $\|C_i(x_{-i})\| \leq \bar z_i$ holds for all $x \in \prod_j Q_j$ by hypothesis. Therefore each subsystem can be kept in $Q_i$ while the product state remains in $\prod_j Q_j$: apply the feedbacks simultaneously. $\blacksquare$

The two appendix constructions show both directions of failure: coupling can empty a product of individually viable factors (Counterexample A.1, at MSY floors) and can create viability absent in an isolated factor (Example A.2, equilibrium-defined floors). Restricted composition is exactly that — restricted; the general typed interface theorem remains open (recorded in the programme's open-problems register).

---

## 12 Institutional implementation (family F11)

**Theorem 12.1 (Institutional equivalence) [CC-A001-071 · theorem].** If two institutions induce the same belief dynamics, effective control correspondence, allocation correspondence, and physical actuator map, then they have the same viability kernel.

*Proof (verified present; summary).* The viability kernel depends only on the state space, dynamics, constraint set, and admissible control correspondence; two institutions inducing the same effective objects generate the same kernel by construction. $\blacksquare$

**Theorem 12.2 (Institutional viability condition) [CC-A001-073 · theorem].** Let $Q \subseteq \mathcal V$ be closed. For every reachable information set $B$ intersecting $Q$, suppose

$$
U_{\mathrm{eff}}(B)\cap\bigcap_{x \in B \cap Q}\left\{u: F(x, u, D(x)) \subseteq T_Q(x)\right\}\neq \varnothing.
$$

Then $Q$ is robustly viable under the institution.

*Proof (verified present; summary).* The condition states that for every reachable belief there exists an institutionally implementable control keeping every compatible state in $Q$ against every admissible disturbance; measurable selection and the viability theorem for differential inclusions close the argument. $\blacksquare$

**Hypothesis object 12.3 (The three response-sign hypotheses, H3 residual) [CC-A003-003 · defined source object].** The institutional-response taxonomy of the stress-test frame: H1, scarcity-amplifying extraction; H2, protective restraint or restoration; H3, inertia, capture, or state-dependent response. No result for one hypothesis is generalized to another, and a model-specific bifurcation threshold is not a universal policy threshold. H1 and H2 carry named instantiations in the delay-dynamics paper (Paper 4); H3 is the residual institutional-response hypothesis, the object against which the implementation operator of this section is read. Its groundwater-module restatement — the competing-institutional-hypothesis ladder of the domain template — is registered as a template obligation [CC-A005-006 · defined source object, registered template obligation]: the same three response structures declared as one identification object, with no constitutive content supplied until a named basin, data boundary, uncertainty model, and preregistration exist.

**Definition 12.4 (Finite-horizon epistemic-institutional kernel) [CC-A006-005 · definition].** For the joint institutional information state $(B,h)$ — compatible physical histories and parameters together with an institutional mode, prescription authority $a\in\Gamma(B,h)$, and implementation correspondence $u\in\mathcal E(B,h,a)$, under the lower-game quantifier order — define $\operatorname{Pre}_{\mathfrak I}(\mathfrak Q)$ as the set of information states from which some prescription is tube-safe and lands in $\mathfrak Q$ for every compatible observation, covariate, and implementation outcome. The finite-horizon epistemic-institutional kernel is given by the safe-base recursion $\mathfrak K_0=\mathfrak S$, $\mathfrak K_{n+1}=\mathcal T(\mathfrak K_n):=\mathfrak S\cap\operatorname{Pre}_{\mathfrak I}(\mathfrak K_n)$. The deflationary implementation $\mathfrak K_n\cap\operatorname{Pre}_{\mathfrak I}(\mathfrak K_n)$ generates the same descending orbit from $\mathfrak S$ when $\operatorname{Pre}_{\mathfrak I}$ is monotone; the safe-base form is official because it remains safe under arbitrary initialization.

**Conditional Theorem 12.5 (Sampled epistemic-institutional viability, safe-base form) [CC-A006-006 · conditional theorem].** Assume: (i) the compatible-state update is nonempty for every compatible branch; (ii) all transition and authority/implementation correspondences are defined on $\mathfrak S$; (iii) the required non-anticipative prescriptions exist whenever the predecessor condition holds; (iv) $\operatorname{Pre}_{\mathfrak I}$ is monotone. Then $\mathfrak K_n$ is exactly the set of information states from which safety can be guaranteed for $n$ decision intervals, and $\mathcal T$ has a greatest fixed point on the powerset lattice of $\mathfrak S$. If, in addition, $\mathcal T$ preserves decreasing countable intersections (an $\omega$-continuity-from-above condition) and the strategy-selection assumptions are closed under the infinite-horizon limit, then $\mathfrak K_\infty:=\bigcap_{n\ge0}\mathfrak K_n$ is that greatest fixed point; without the additional condition the greatest fixed point is obtained by transfinite descending iteration rather than necessarily by the countable intersection.

*Proof (verified present; summary).* Induction on $n$: membership in $\mathfrak K_{n+1}$ supplies a current safe prescription and a successor in $\mathfrak K_n$ for every branch; monotonicity makes $\mathcal T$ monotone, so Tarski's theorem gives the greatest fixed point; the continuity and closure hypotheses identify the countable descending limit. $\blacksquare$ *Scope:* an abstract characterization — it does not claim that $B_t$ is tractable, that $\mathfrak K_\infty$ is nonempty, or that any particular ecological system meets the assumptions. The empirical-identification paper (Paper 5) reads its benchmark against exactly this object at exactly this conditional status.

---

## 13 Intergenerational and stochastic bounds (family F12, bounded appendix)

**Theorem 13.1 (Nested-constraint impossibility) [CC-A001-084 · theorem — mapping: counterexample/limit].** Assume the trajectory $x(\cdot)$ is confined to a compact set $\mathcal K$ (verified per instance via dissipativity). If $\mathcal V^{(k+1)} \subseteq \mathcal V^{(k)}$ and $\bigcap_k \mathcal V^{(k)} = \varnothing$: no intergenerationally viable path exists.

*Proof (verified present; summary).* A single path confined to the compact set must lie in every $\mathcal V^{(k)}$ for the corresponding generations; the empty total intersection makes this impossible. $\blacksquare$

**Theorem 13.2 (Finite-horizon small-noise viability) [CC-A001-091 · theorem].** Consider the deterministic system $\dot x = f(x)$ under a viable feedback, and the stochastic perturbation $dX_t^\varepsilon = f(X_t^\varepsilon)\,dt + \varepsilon\,\Sigma(X_t^\varepsilon)\,dW_t$. Let $K_0$ be a compact subset of the kernel interior, and suppose deterministic trajectories from $K_0$ remain at distance at least $2\delta$ from $\partial\mathcal V$ on $[0,T]$. Assume $f$ is Lipschitz and $\Sigma$ is bounded on a neighbourhood of these trajectories. Then

$$
\inf_{x_0 \in K_0}\mathbb P_{x_0}\left(X_t^\varepsilon \in \mathcal V\;\;\forall t \in [0,T]\right)\to 1\qquad\text{as }\varepsilon\to 0.
$$

*Proof (verified present; summary).* With a $2\delta$ deterministic margin and bounded diffusion coefficient, the probability of a $\delta$-deviation over $[0,T]$ vanishes as $\varepsilon\to0$ (standard concentration for bounded-coefficient diffusions); on the complement event the trajectory never reaches $\partial\mathcal V$. $\blacksquare$

**Programme 13.3 (Justice and multiscale viability) [CC-A002-050 · research programme, open].** Place group- and location-specific minimum services and maximum harms inside $K$ — the group-indexed safe-set construction $\{z: g_j(z)\ge0 \text{ for all } j\}$ with the recursive intergenerational criterion ($z(t)\in K_g$ throughout generation interval $I_g$, and the terminal state in a declared continuation set $C_{g+1}$ from which the next generation's constraints are viable under its policy and disturbance classes; a terminal aggregate stock alone is not this criterion). Distinguish positive predictions from normative entitlement choices; study when local kernels compose into a global kernel under cross-boundary transfers, and when aggregate feasibility masks an empty kernel or capture basin for one group.

---

## Appendix A — bounded-appendix constructions and scope remarks

**A.1 Counterexample (Emptiness despite factorwise viability at MSY) [CC-A001-055 · counterexample/limit].** Take $d > 0$, $C_1 \neq C_2$, $H_{\min,i} = r_i C_i / 4$ (MSY level). Each isolated system has kernel $[C_i/2, \infty) \times [0, K_{\max,i}]$. At MSY: $\phi_i(S_i) = -\frac{r_i}{C_i}(S_i - C_i/2)^2 \leq 0$ with equality only at $S_i = C_i/2$. Adding the equilibrium equations requires $\phi_1 + \phi_2 = 0$, so both must vanish: $S_i = C_i/2$. Substituting into the first equation: $d(C_2/2 - C_1/2) = 0$, requiring $C_1 = C_2$. For $C_1 \neq C_2$: no equilibrium, empty kernel. *The counterexample is specific to the MSY parameter choice; for $H_{\min,i} < r_i C_i / 4$, equilibria may exist.*

**A.2 Example (Coupling creates viability absent in a factor) [CC-A001-056 · example; primary destination Paper 1/monograph].** Take $g_i(s) = s(1-s)$, $d = 0.2$. Choose $(S_1^*, S_2^*) = (0.5, 0.8)$. Define harvest floors by the equilibrium equations: $H_{\min,1} = g_1(0.5) + 0.2(0.8 - 0.5) = 0.31$; $H_{\min,2} = g_2(0.8) + 0.2(0.5 - 0.8) = 0.10$. Patch 1 in isolation: $\max_s g_1(s) = 0.25 < H_{\min,1} = 0.31$, so patch 1 is not viable in isolation. Yet the coupled system has the equilibrium $(0.5, 0.8)$, so its kernel is nonempty, provided sink and harvest-capacity constraints hold.

**A.3 Remark (One balance per moiety) [CC-A002-009 · remark].** The conservation theorem gives one balance per declared moiety. It does not authorize addition of biomass, money, biodiversity indices, and exergy into a conserved scalar.

**A.4 Remark (Farkas multipliers are separation certificates) [CC-A002-053 · remark].** The multipliers of Theorem 5.5 are a separation certificate, not universal exchange rates. Nonlinear, nonconvex, path-dependent, spatial, or irreversible technologies require their own feasibility analysis. An elasticity fitted near one operating point cannot establish global substitutability.

**A.5 Remark (Accounting and boundedness on the restricted hybrids) [CC-A002-031 · remark].** Review synchronisation makes the history-reset specialization locally finite, while the jump budget makes the bounded-jump ODE specialization locally finite on every finite union of review intervals. The typed conservation theorem can therefore be applied along their executions when each current physical reset satisfies the physical jump equation and its null-space assumptions; an abstract RFDE memory tail is not itself a conserved moiety. Applying the BIBS theorem additionally requires a coercive storage functional (history-reset model) or a coercive storage function (bounded-jump model), the flow Dini inequality, and reset non-expansiveness. None of those conditions follows from a history reset, a jump budget, or the canonical tuple.

---

## 14 Status ledger

Every retained row of this manuscript, with claim status, evidence status (post-closure), and primary destination. `P` = provenance concordance row in `research_program/canonical_concordance_A001_A025.csv`. Review state: all 89 rows `row_verified` (A001/A002 scientific closure passes, 2026-08-27; A003/A005/A006/A007/A010/A013/A018 closure passes, 2026-08-28 — every source read end to end; kind, module, mapping type, and evidence status verified per row) — content-level acceptance; no theorem status promoted; the §8 interface contract remains open per row. Rows 1–70 are the budgeted selection (63 main + 7 bounded-appendix); rows 71–89 are the closure-campaign seam routings — rows the destination passes and seam closures of the 2026-08-28 campaign assign to this atlas from the seven further closed sources, stated here at exactly their verified statuses.

| # | P | Statement | Manuscript | Claim status | Evidence | Primary destination |
|---|---|---|---|---|---|---|
| 1 | CC-A002-001 | Type system and physical state | Def 2.1 | definition | defined source object | Paper 1/monograph (restated) |
| 2 | CC-A002-002 | Hybrid specialization data | Def 2.2 | definition | defined source object | Paper 2 |
| 3 | CC-A002-003 | Canonical system | Def 2.3 | definition | defined source object | Paper 1/monograph (restated) |
| 4 | CC-A002-004 | Four uncertainty levels | Def 2.4 | definition | defined source object | Paper 1/monograph (restated) |
| 5 | CC-A002-005 | Diagnostic types | Def 2.5 | definition | defined source object | Paper 1/monograph (restated) |
| 6 | CC-A002-006 | Threshold and intergenerational types | Def 2.6 | definition | defined source object | Paper 1/monograph (restated) |
| 7 | CC-A002-007 | Domain-qualified non-compensation | Prop 5.1 | theorem | proof verified present | Paper 2 |
| 8 | CC-A001-001 | Constraint monotonicity | Thm 3.1 | theorem | proof reproduced | Paper 2 |
| 9 | CC-A001-003 | Product structure | Thm 3.2 | theorem | proof reproduced | Paper 2 |
| 10 | CC-A001-004 | Face necessity ≠ kernel necessity | Thm 3.3 | theorem | proof reproduced | Paper 2 |
| 11 | CC-A001-033 | Finite-time exit certificate | Thm 3.4 | theorem | proof reproduced | Paper 2 |
| 12 | CC-A002-008 | Typed hybrid conservation | Thm 4.1 | theorem | proof verified present | Paper 3 (atlas entry) |
| 13 | CC-A002-010 | Closed positive-moiety bound | Cor 4.2 | theorem | proof verified present | Paper 3 (atlas entry) |
| 14 | CC-A002-011 | Non-negative invariance (3 modes) | Thm 4.3 | theorem | proof verified present | Paper 4 (atlas entry) |
| 15 | CC-A002-012 | Donor limitation is sufficient | Cor 4.4 | theorem | proof verified present | Paper 3 (atlas entry) |
| 16 | CC-A002-013 | BIBS criterion | Cond Thm 4.5 | conditional theorem | conditional (source-declared) | Paper 2 |
| 17 | CC-A001-049 | Capital–resource substitution thresholds | Thm 5.2 | theorem | proof verified present | Paper 2 |
| 18 | CC-A001-050 | Essentiality / unbounded substitution | Cor 5.3 | theorem | proof verified present | Paper 2 |
| 19 | CC-A002-014 | Support provenance / support gap | Def 5.4 | definition | defined source object | Paper 3 (atlas entry) |
| 20 | CC-A002-015 | Linear substitution alternative | Thm 5.5 | theorem (finite linear model) | proof verified present | Paper 2 |
| 21 | CC-A001-020 | Epistemic emptiness | Thm 6.1 | theorem | proof verified present | Paper 2 |
| 22 | CC-A001-022 | Observer-to-viability transfer | Thm 6.2 | theorem | proof verified present | Paper 2 |
| 23 | CC-A001-023 | Robust invariance / tangency | Thm 6.3 | theorem | proof verified present | Paper 2 |
| 24 | CC-A001-026 | Instantaneous common-action obstruction | Thm 6.4 | theorem | proof omitted in source; one-step proof obligation registered | Paper 2 |
| 25 | CC-A001-027 | Hidden-mode conflict | Ex 6.5 | example | explicit construction | Paper 5 (atlas entry) |
| 26 | CC-A001-028 | Delayed-information obstruction | Thm 6.6 | theorem | proof verified present | Paper 5 (atlas entry) |
| 27 | CC-A001-029 | Observer safety buffer | Thm 6.7 | theorem | proof verified present | Paper 2 |
| 28 | CC-A001-030 | Eroded kernels under output feedback | Prop 6.8 | proposition | proof verified present | Paper 2 |
| 29 | CC-A002-016 | Exact safety certifier | Def 6.9 | definition | defined source object | Paper 2 |
| 30 | CC-A002-017 | Observation-fibre criterion | Thm 6.10 | theorem | proof verified present | Paper 2 |
| 31 | CC-A002-018 | Safety-crossing fibres | Cor 6.11 | theorem | proof verified present | Paper 2 |
| 32 | CC-A001-007 | Kernel = capture basin | Prop 7.1 | theorem | proof verified present | Paper 2 |
| 33 | CC-A001-008 | Recovery resilience vanishes at ∂K | Cor 7.2 | theorem (limit) | immediate | Paper 2 |
| 34 | CC-A001-009 | Capture basin / three-part statement | Def 7.3 | definition | defined source object | Paper 2 |
| 35 | CC-A001-010 | Envelope-relative recovery time | Def 7.4 | definition | defined source object | Paper 2 |
| 36 | CC-A001-011 | Robust informational capture basin | Def 7.5 | definition | defined source object | Paper 2 |
| 37 | CC-A001-012 | Worst-case informational recovery time | Def 7.6 | definition | defined source object | Paper 2 |
| 38 | CC-A001-013 | Information monotonicity of recovery | Prop 7.7 | theorem | proof reproduced | Paper 5 (atlas entry) |
| 39 | CC-A002-020 | Capture basin / relative irreversibility (typed) | Def 7.8 | definition | defined source object | Paper 2 |
| 40 | CC-A002-019 | Three policy questions | Def 8.1 | definition | defined source object | Paper 1/monograph (restated) |
| 41 | CC-A002-021 | Sampled robust-viability kernel | Thm 8.2 | theorem | proof verified present | Paper 2 |
| 42 | CC-A002-022 | Monotonicity under policy-set expansion | Cor 8.3 | theorem | proof verified present | Paper 2 |
| 43 | CC-A002-023 | Finite-clopen observation knowledge kernel | Thm 8.4 | theorem | proof verified present | Paper 2 |
| 44 | CC-A002-024 | Held-control tube predecessor | Def 8.5 | definition | defined source object | Paper 2 |
| 45 | CC-A002-025 | Inter-sample-safe sampled kernel | Thm 8.6 | theorem | proof verified present | Paper 2 |
| 46 | CC-A002-026 | Finite-clopen inter-sample-safe kernel | Thm 8.7 | theorem | proof verified present | Paper 2 |
| 47 | CC-A002-027 | Sampled RFDE finite-clopen kernel | Cond Thm 8.8 | conditional theorem | conditional (source-declared) | Paper 4 (atlas entry) |
| 48 | CC-A002-028 | Review-synchronised hybrid RFDE kernel | Cond Thm 8.9 | conditional theorem | conditional (source-declared) | Paper 4 (atlas entry) |
| 49 | CC-A002-029 | OSC does not close tube constraints | Prop 8.10 | proposition (counterexample) | proof verified present | Paper 2 |
| 50 | CC-A002-030 | Bounded-jump hybrid ODE kernel | Cond Thm 8.11 | conditional theorem | conditional (source-declared) | Paper 2 |
| 51 | CC-A002-032 | Compact sampled information model | Def 8.12 | definition | defined source object | Paper 2 |
| 52 | CC-A002-033 | Sampled information-state tube kernel | Thm 8.13 | theorem | proof verified present | Paper 2 |
| 53 | CC-A002-034 | Finite-time sample-and-hold convergence | Cond Thm 8.14 | conditional theorem | conditional (source-declared) | Paper 2 |
| 54 | CC-A002-035 | Four model maps | Def 9.1 | definition | defined source object | Paper 1/monograph (restated) |
| 55 | CC-A002-036 | Projectability criterion | Thm 9.2 | theorem (projectable reduction) | proof verified present | Paper 2 |
| 56 | CC-A002-037 | Fibre obstruction | Cor 9.3 | theorem (limit) | proof verified present | Paper 2 |
| 57 | CC-A002-038 | Support-saturated logistic stock limit | Thm 9.4 | theorem (approximation) | proof verified present | Paper 3 (atlas entry) |
| 58 | CC-A002-039 | Logistic variance correction | Thm 9.5 | theorem (approximation) | proof verified present | Paper 2 |
| 59 | CC-A002-040 | Local-horizon bracket | Cond Thm 10.1 | conditional theorem | conditional (source-declared) | Paper 2 |
| 60 | CC-A002-041 | Small-gain delay-independent stability | Cond Thm 10.2 | conditional theorem | conditional (source-declared) | Paper 4 (atlas entry) |
| 61 | CC-A001-088 | Compositional viability | Thm 11.1 | theorem | proof reproduced | Paper 2 |
| 62 | CC-A001-071 | Institutional equivalence | Thm 12.1 | theorem | proof verified present | Paper 2 |
| 63 | CC-A001-073 | Institutional viability condition | Thm 12.2 | theorem | proof verified present | Paper 2 |
| 64 | CC-A001-084 | Nested-constraint impossibility | Thm 13.1 | theorem (limit) | proof verified present | Paper 1 gate / Paper 2 |
| 65 | CC-A001-091 | Finite-horizon small-noise viability | Thm 13.2 | theorem | proof verified present | Paper 2 |
| 66 | CC-A001-055 | Emptiness despite factorwise viability | App A.1 | counterexample | explicit construction | Paper 2 |
| 67 | CC-A001-056 | Coupling creates viability | App A.2 | example | explicit construction | Paper 1/monograph (atlas entry) |
| 68 | CC-A002-009 | One balance per moiety | App A.3 | remark | scope note | Paper 2 |
| 69 | CC-A002-053 | Farkas multipliers are separation certificates | App A.4 | remark | scope note | Paper 2 |
| 70 | CC-A002-031 | Accounting/boundedness on hybrids | App A.5 | remark | scope note | Paper 2 |
| 71 | CC-A006-004 | Stability and safety are independent | Lem 3.5 | lemma (counterexample/limit) | proof verified present | Paper 2 |
| 72 | CC-A010-009 | Geological/support-pool noninvariance | Prop 4.6 | boundary test (counterexample/limit) | audited verdict, source-stated | Paper 2 |
| 73 | CC-A007-001 | Compensatory reporting limit | Lem 5.6 | lemma (counterexample/limit) | proof verified present | Paper 2 |
| 74 | CC-A013-001 | Witness construction on the unrestricted balance space | Prop 5.7 | logical observation + construction (counterexample/limit) | explicit construction | Paper 2 (seam: Paper 3 §9.1) |
| 75 | CC-A018-001 | No scalar weighting certifies componentwise sustainability | Prop 5.8 | proposition (counterexample/limit) | proof verified present | Paper 2 (seam: Paper 3 §9.1) |
| 76 | CC-A006-008 | Common-action obstruction under output feedback | Prop 6.12 | proposition (counterexample/limit) | proof verified present | Paper 2 |
| 77 | CC-A006-009 | Conditional observer-to-safety transfer | Prop 6.13 | proposition (conditional margin) | proof verified present | Paper 2 |
| 78 | CC-A007-002 | Static diagnostic aliasing | Lem 6.14 | lemma (counterexample/limit) | proof verified present | Paper 2 |
| 79 | CC-A006-014 | Safe learning | Template 6.15 | remark/template | defined source object | Paper 2 |
| 80 | CC-A010-004 | Logistic variance correction (model-audit restatement) | §9 restatement record | identity (exact specialization) | line-checked identity, Theorem 9.5 family | Paper 2 |
| 81 | CC-A010-005 | General C² curvature bound (model-audit restatement) | §9 restatement record | bound (exact specialization) | line-checked bound, Theorem 9.5 family | Paper 2 |
| 82 | CC-A018-006 | Finite-time reduction to the five-state core | Conj 9.6 | conjecture (demoted at correction) | conditional on source hypotheses; sweep-supported, unproved | Paper 2 (seam: Paper 4 §4.3) |
| 83 | CC-A010-013 | Effort sensitivity coefficients of the audit template | Prop 10.3 | algebraic result (registered template) | source-verified algebra | Paper 2 |
| 84 | CC-A010-014 | Interior effort upper bound of the audit template | Prop 10.4 | algebraic result (registered template) | source-verified algebra | Paper 2 |
| 85 | CC-A003-003 | H3: inertia/capture/state-dependent response | Hypothesis object 12.3 | defined source object | defined source object | Paper 2 (seam: Paper 4 §8.1) |
| 86 | CC-A005-006 | Competing-institutional-hypothesis ladder (groundwater restatement) | Hypothesis object 12.3 | defined source object (registered template obligation) | defined source object | Paper 2 |
| 87 | CC-A006-005 | Finite-horizon epistemic-institutional kernel | Def 12.4 | definition | defined source object | Paper 2 (seam: Paper 5 §4.4) |
| 88 | CC-A006-006 | Sampled epistemic-institutional viability (safe-base form) | Cond Thm 12.5 | conditional theorem | conditional (source-declared; repaired safe-base form) | Paper 2 (seam: Paper 5 §4.4) |
| 89 | CC-A002-050 | Justice and multiscale viability | Programme 13.3 | research programme (open) | declared open programme | Paper 2 / monograph |

**Ledger discipline.** The mapping-type column of the concordance (exact specialization / projectable reduction / approximation / counterexample-or-limit) is preserved per row; the atlas never re-types a result. Destination cross-references are annotations, not transfers: where the primary destination is another paper, that paper owns the full treatment and its seam contract, and this atlas states the canonical form exactly once.

---

## 15 Provenance, reproducibility, and limits

**Sources.** This manuscript's retained set derives from nine fully row-closed sources. The budgeted selection (rows 1–70: 63 main + 7 bounded-appendix) derives from A001 (`uploads/topdown.txt`, 99 concordance rows, closure 2026-08-27) and A002 (`uploads/general_theory.txt`, 53 concordance rows, closure 2026-08-27), recorded in `research_program/paper2_retained_row_budget.csv`. The closure-campaign seam rows (71–89) derive from A003 (`uploads/Paper_V_Institutional_Feedback_and_Nonlinear_Transitions.txt`), A005 (`uploads/Paper_III_Groundwater_Module.txt`), A006 (`uploads/Paper_II_Robust_Epistemic_Viability_V2.txt`), A007 (`uploads/Paper_I_Hybrid_Sustainability_Architecture_V4.txt`), A010 (`uploads/paper4_perspective.txt`), A013 (`uploads/paper1_accounting.txt`), and A018 (`uploads/manuscript.txt`) — each closed 2026-08-28 with the source read end to end. The per-row verification record is `research_program/concordance_row_closure_twenty_sources.md`; the row-level evidence is `research_program/canonical_concordance_A001_A025.csv` (409 rows; all nine sources fully `row_verified`).

**Proof handling.** Proofs marked *reproduced* are printed in full above from the source. Proofs marked *verified present; summary* exist in full in the source (the closure pass verified proof presence and read it); the summary given here is faithful to the source argument, and camera-ready reproduces each proof verbatim. One proof is omitted in the source (Theorem 6.4), and the obligation to supply an explicit one-step proof is registered rather than silently discharged.

**What this paper does not claim.** No result here is empirical; no conditional theorem is promoted; no result transfers across modules without the interface contract (open, recorded per row); the atlas does not close any open conjecture (the three A002 conjectures and the research programmes are docketed, not asserted). The general typed composition theorem, the variable-event delayed-hybrid kernel, and the delay-separation principle remain open.

**Length gate.** The measured retained budget is ≈27.2k words at full proof expansion — above many journal main-text limits. The pre-authorized response is the coherent split by question (2A: typed viability under observation and implementation; 2B: projectability, noncompensation, substitution, and composition limits), never destructive condensation. The split decision is taken at venue-policy check, not now.

**Data and code.** This paper is mathematical; it cites no computational artifact as evidence. The concordance, closure scripts, and verification suite (`reaudit/verify_concordance_rows.py`, 12/12 checks) are the audit trail and are committed to the programme repository.

---

## References (provenance-first)

The cited mathematical literature is that of the sources: Aubin (1991) *Viability Theory* (Nagumo theorem, measurable selection, viability theorem for differential inclusions); Hale (2009) for comparison-ODE attractivity; Halanay-type arguments for delay-independent stability; Farkas' lemma for the substitution alternative. The programme-internal provenance documents:

- A001 source: `uploads/topdown.txt` (*Top-Down Sustainability Architecture*), 99-row concordance block.
- A002 source: `uploads/general_theory.txt` (*A Typed Flux–Observation–Governance Theory of Sustainability*), 53-row concordance block.
- Canonical concordance: `research_program/canonical_concordance_A001_A025.csv` (409 rows).
- Retained-row budget: `research_program/paper2_retained_row_budget.csv` (152 rows; 63 main + 7 bounded-appendix for this paper).
- Closure report: `research_program/concordance_row_closure_twenty_sources.md`.
- Publication architecture: `research_program/revised_optimal_publication_architecture_A001_A025.md`.
- Length budget and split trigger: `research_program/content_retention_and_length_budget_A001_A025.md`, `research_program/paper2_theorem_atlas_content_budget.md`.

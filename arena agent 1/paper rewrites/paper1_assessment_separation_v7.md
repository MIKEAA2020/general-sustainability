# The Limits of Compensatory Aggregation: A Formal Separation of Weak and Strong Sustainability Assessment

## Abstract

Sustainability assessments routinely aggregate heterogeneous capital stocks and floors into single indices, on the implicit premise that a deficit in one dimension can be compensated by a surplus in another. This paper proves a separation result for a typed transition datum under exact-tube semantics showing where that premise fails. On an explicit rational witness there exist states at which, for every nonnegative scalarization weight $w$, some action keeps the aggregate floor $w\cdot s \ge 0$ along its worst-case tube, while no single action keeps all typed floors nonnegative along its tube; the per-weight accepted state set therefore strictly contains the common-plan accepted state set. The same witness's discrepancy region splits by a resource threshold into a rescue set, whose states are already typed-transformable through the resource-controlled action, and an impossibility region, whose states admit no typed-safe transition under any weight and can be bridged only by resource augmentation at a defined cost; the genuine acceptance gap $\mathrm{FP}_{\mathrm{agg}} = \mathcal{V}_{\mathrm{weak}} \setminus \mathcal{V}_{\mathrm{typ}}$ is exactly the impossibility region, a region with nonempty open interior. Two companion results bound the separation: a two-stage datum on which a later interval erases the gap, and a blend theorem under which time-shared convexification of the menu closes the gap exactly at the compensatory region — so the "only" claim is scoped to the deterministic menu. The continuum statements are proved in full; an exact-integer computation checks the finite rational instance; implications for composite indices are stated at their actual strength.

**Keywords:** sustainability assessment; weak and strong sustainability; compensatory aggregation; scalarization; viability theory; composite indicators
**Mathematics Subject Classification:** 49J53; 93B03; 91B76; 90B50


---

## 1. Introduction

### 1.1 Two failure modes

Sustainability assessment sits on a fault line that has structured the field since its foundation. The weak-sustainability tradition, formalized in the genuine-savings and inclusive-wealth frameworks (World Bank, 2011; Boos, 2015; Neumayer, 2013), treats distinct capital forms as substitutable through prices: a decline in one stock is consistent with sustainability if the aggregate value of the capital base does not decline. The strong-sustainability tradition holds that certain stocks and services are separately binding — critical natural capital whose loss cannot be compensated at any price (Ekins et al., 2003) — and its foundation statement in ecological economics is the thesis of weak comparability: values relevant to environmental decisions may not be commensurable in a single metric at all (Martinez-Alier, Munda, and O'Neill, 1998). The debate is mature in the policy and multi-criteria decision literatures (Cinelli, Coles, and Kirwan, 2014; Schär, Pohl, and Geldermann, 2025; Hanley et al., 1999; Usubiaga-Liaño, 2025), and the theory of sustainability indicators is correspondingly well developed (Martinet, 2011; Cairns and Martinet, 2014), including the maximin formulation in which strong sustainability emerges from the viability of the constraints rather than from an optimality criterion (Solow, 1974; Doyen and Gajardo, 2020).

This paper addresses a question that the indicator literature has left comparatively open: the *dynamic* question. During a sustainability transition, when can a compensatory aggregate certify a trajectory that a noncompensatory assessment rejects? Two failure modes motivate the question.

The first is *commensurability drift*. Assessments aggregate stocks, services, liabilities, and floors into single indices whose compensation principles are rarely stated as explicit mathematics. Composite indices are routinely criticized on exactly this ground — the weights they embed are value judgements presented as measurement (Hickel, 2020; Martinez-Alier, Munda, and O'Neill, 1998) — but the critique typically targets the *choice* of weights. The stronger possibility, which this paper proves to be real, is that no choice of weights repairs the difficulty: the failure is structural, in the logic of aggregation itself.

The second is *status drift*. Conceptual frameworks state aspirations as theorems, and conditional results circulate as unconditional ones. This paper guards against that failure in its own presentation by labelling every claim with its logical status — definition, theorem, conditional statement, or open question — and by stating at each point what has been proved, what is verified on a finite machine artifact, and what is merely asserted.

### 1.2 The central result

The paper's organizing result is a quantifier noncommutation. Fix a typed transition datum: a state space carrying typed floors $s_i \ge 0$ (normalized at zero), an action set, a disturbance set, and exact-tube semantics under which a transition is safe only if every state visited along it — not merely its endpoint — satisfies the constraints. For each nonnegative scalarization weight $w$ in the full cone $W_+ = \mathbb{R}^n_+ \setminus \{0\}$, let $E_w(z)$ be the set of actions admissible at state $z$ under the aggregate floor $w \cdot s \ge 0$, and let $E_{\mathrm{typ}}(z)$ be the set of actions admissible under the typed floors $s_i \ge 0$ taken separately. Two acceptance criteria then differ by quantifier order:

- **Common-plan acceptance (noncompensatory):** there exists one action lying in every $E_w(z)$ —
  $$\exists a\; \forall w:\; a \in E_w(z).$$
- **Per-weight acceptance (compensatory):** for each weight there exists some admissible action, possibly depending on the weight —
  $$\forall w\; \exists a_w:\; a_w \in E_w(z).$$

The first implies the second; the converse fails. The failure is not a defect of any particular weight: it is the noncommutativity of the existential quantifier over actions with the universal quantifier over weights. The noncommutation is the assessment-theoretic instance of the strict minimax pattern of game theory: for the binary payoff "action $a$ is admissible at $z$ under $w$", the two quantifier orders are the two orders of the minimax interchange, and the witness of Section 4.5 exhibits the interchange failing strictly. The paper proves the always-valid inclusion (Proposition 1), proves the pointwise identity of the noncompensatory accepted set with the common-plan set over the full cone (Theorem 3(ii)), isolates the general mechanism in Proposition 1, and exhibits an explicit rational witness on which the acceptance gap $\mathrm{FP}_{\mathrm{agg}} = \mathcal{V}_{\mathrm{weak}} \setminus \mathcal{V}_{\mathrm{typ}}$ is a region with nonempty interior — the *impossibility region* (Theorem 5(4)). The witness further partitions the aggregate-versus-direct-floor discrepancy region $\mathrm{FP}_0$ by a resource threshold into the impossibility region and the *rescue set*, whose states are already typed-transformable through the resource-controlled action (Theorem 5(7)); the rescue operation of Section 5.5 — resource augmentation — acts on the impossibility region, not on the rescue set.

### 1.3 Contribution and scope

**Claimed.** (i) The action-set identity $E_{\mathrm{typ}}(z) = \bigcap_{w \in W} E_w(z)$, with the full-cone choice (the cone without the origin) isolating the separation as purely dynamic (Theorem 3(ii)). (ii) A general quantifier-separation proposition (Proposition 1). (iii) Monotonicity of the accepted-state hierarchy in the weight family (Theorem 4). (iv) An explicit rational witness with an open region of strict separation, the discrepancy-region split $\mathrm{FP}_0 = R \cup I$, the identity $\mathrm{FP}_{\mathrm{agg}} = I$, and the exact per-weight licensing thresholds (Theorem 5). (v) Persistence of the separation under hold-prefix extension of the horizon (Theorem 6). (vi) An explicit two-stage erasure datum on which a later interval removes the gap (Theorem 7), delimiting the propagation claim. (vii) The blend-collapse theorem: time-shared convexification of the witness menu closes the acceptance gap exactly at the compensatory region (Theorem 8).

**Not claimed.** A universal ranking of all weak- and strong-sustainability doctrines; a proof that any particular set of environmental boundaries ought to be treated noncompensatorily; an empirical result about any specific resource system; or the governance, intergenerational, and composition extensions, which are stated at their actual (partial) status in the Supplementary Material.

To our knowledge this provides an explicit exact-tube witness for this dynamic separation in a compensatory/noncompensatory assessment setting. We do not assert priority over the elementary quantifier fact $\exists a\, \forall w \neq \forall w\, \exists a_w$, which is standard.

---

## 2. A Typed Framework for Transition Assessment

This section fixes the typed framework that the theorems require. It is a minimal realization, not a completed universal architecture.

### 2.1 Types and physical state

Physical state is typed: a state variable denotes a *moiety* — a named conserved substance — with a unit, and typed fluxes connect typed stocks. Conservation claims are per-moiety; the framework does not authorize adding biomass, money, and biodiversity into one conserved scalar. Services, thresholds, information states, and institutional variables are separate types. No claim mixes types without a declared bridge. Typing serves two purposes: it makes the domain of every conservation law explicit, and it records the provenance of every floor — physical, contractual, or normative — as part of the floor's type.

### 2.2 The canonical tuple

The canonical object is the tuple
$$\mathfrak{S} = (T, Z, S_{st}, B_{out}, V, \Gamma, O, A, C, R, D, K, P),$$
comprising a type system $T$; state space $Z$; stock–flux structure $S_{st}$; boundary interface $B_{out}$; constitutive laws $V$; service–technology correspondence $\Gamma$; observation operator $O$; assessment operator $A$; command architecture $C$; deployment/reset architecture $R$; disturbance class $D$; safe-and-just set $K$; and policy class $P$. A model is a specified tuple; a claim is a statement about a tuple with a status; an application is a tuple plus data. Throughout this paper $P$ denotes the policy class; accepted-state sets use the distinct notation $\mathcal{V}[\cdot]$ introduced in Section 3.2. The weight cone of Section 3.1 is written $W$, the command architecture keeps the letter $C$, and the action set of Section 5.5 is written $\mathcal{A}$ — the three objects never share a symbol.

### 2.3 Uncertainty and the quantifier discipline

Uncertainty is stratified into four declared levels — parameter, observation/assessment, process disturbance, and structural model uncertainty — each with a fixed quantifier discipline. Every application poses its safety question in one of three forms: *actual-policy safety* (a specified policy–disturbance pair $(\pi_0, d_0)$ stays in $K$); *viability* (some $\pi \in P$ stays in $K$); *robust viability* (one causal policy works for every $d \in D$). The order is fixed: $\exists \pi\, \forall d$, not $\forall d\, \exists \pi$. Section 3 keeps the disturbance quantifier fixed in its innermost position, $\forall d$, inside every assessment operator, and studies a second quantifier — over scalarization weights — placed outside it: the noncommutation analysed there is $\exists a\, \forall w$ versus $\forall w\, \exists a_w$.

### 2.4 Model maps

Cross-model claims are licensed by four declared maps — specialisation, exact projection (semiconjugacy), approximation with a declared residual, and singular reduction — which are not interchangeable. This paper needs only the taxonomy and the discipline it enforces: no claim transfers from one model to another without a declared map.

### 2.5 Claim status

Every statement carries a status: definition, identity, theorem, conditional theorem, conjecture, or counterexample. Two rules govern: *no promotion* — a conditional theorem is never stated as a theorem — and *no silent transfer* — a status proved for one model class does not transfer without a declared map.

### 2.6 Typed failure classes

An assessment verdict must name the failure class it establishes. The taxonomy used here is definitional, not predictive: material inconsistency; physical infeasibility; epistemic/common-prescription infeasibility; authority infeasibility; implementation infeasibility; temporal infeasibility; recovery failure; architecture-transition failure; model-credibility failure; and normative incompatibility. The discipline is to identify the earliest discharged obstruction rather than relabel an institutional failure as physical impossibility.

### 2.7 The witness as a specialization

Section 4.5 instantiates the framework on a minimal typed datum; the mapping is recorded here so that the tuple is a specialization map rather than parallel text. On the witness: $T$ = the three moieties (reserve stock, protected-group service surplus, remediation-liability coverage) with their units; $Z$ = the phase space $(q, x, s_1, s_2)$; $S_{st}$ = the linear spend/growth flows of Section 4.5; $B_{out}$ = none (closed interval); $V$ = the piecewise-linear tube laws; $\Gamma$ = the four named actions; $O$ = the exact state observation; $A$ = the typed assessment operators of Section 3; $C$ = the single-command architecture (one action per interval); $R$ = the destination reset $s \mapsto s + e$; $D$ = $\{\alpha, \beta\}$ as specified in Section 4.5; $K = S_0$; $P$ = the four-element menu. The remaining tuple slots — multi-command architectures, partially observed states, and policy classes larger than the menu — are not used by the witness and are stated only as framework scope.

---

## 3. Assessment Operators

### 3.1 Four operators

Fix a typed exact-tube transition datum with transition-safe sets and a destination set. For a state $z$ and action $a$, let $\mathrm{Tube}(a,d)$ be the full set of states visited during the interval under disturbance $d$, let $\mathrm{End}(a,d)$ be the endpoint values visited, and let $\mathrm{Succ}(a,d)$ be the successor set after any endpoint reset. Four operators are distinguished; they share the same disturbance quantifier and differ in constraint structure, with one additional difference for the fourth: the endpoint operator also replaces the tube evaluation map by the endpoint map.

The **noncompensatory typed** operator (each floor separately binding):
$$E_{\mathrm{typ}}(z) = \{ a : \forall d,\; \mathrm{Tube}(a,d) \subseteq S \ \text{ and } \ \mathrm{Succ}(a,d) \subseteq G \},$$
where $S = S^{\mathrm{phys}} \cap \{ s_i \ge 0,\ i = 1..n \}$ and $G = G^{\mathrm{phys}} \cap \{ s \ge 0 \}$.

The **scalarized aggregate** operator at weight $w \in W_+ = \mathbb{R}^n_+ \setminus \{0\}$:
$$E_w(z) = \{ a : \forall d,\; \mathrm{Tube}(a,d) \subseteq S^w \ \text{ and } \ \mathrm{Succ}(a,d) \subseteq G^w \},$$
where $S^w = S^{\mathrm{phys}} \cap \{ w \cdot s \ge 0 \}$ and $G^w = G^{\mathrm{phys}} \cap \{ w \cdot s \ge 0 \}$.

The **exact-tube physical** operator (physical constraints only, full tube):
$$E_{\mathrm{tube,phys}}(z) = \{ a : \forall d,\; \mathrm{Tube}(a,d) \subseteq S^{\mathrm{phys}} \ \text{ and } \ \mathrm{Succ}(a,d) \subseteq G^{\mathrm{phys}} \}.$$

The **endpoint-only physical** operator (physical constraints at endpoints only):
$$E_{\mathrm{end}}(z) = \{ a : \forall d,\; \mathrm{End}(a,d) \subseteq S^{\mathrm{phys}} \ \text{ and } \ \mathrm{Succ}(a,d) \subseteq G^{\mathrm{phys}} \}.$$

The endpoint operator is included because aggregated accounting in practice is frequently endpoint accounting: the index is evaluated on audited snapshots, while the typed floors of strong sustainability are constraints on the whole trajectory. The distinction is exactly the distinction between an assessment that sees the trajectory and one that sees only its photograph. Because $\mathrm{End}(a,d) \subseteq \mathrm{Tube}(a,d)$, the endpoint operator is the weakest, and the chain
$$E_{\mathrm{typ}}(z) \;\subseteq\; E_w(z) \;\subseteq\; E_{\mathrm{tube,phys}}(z) \;\subseteq\; E_{\mathrm{end}}(z)$$
holds for every $w \in W_+$ (Theorem 3(i) below). The last inclusion is strict in general, though it collapses on the witness of Section 4.5 because the witness's physical constraint touches only the monotone reserve stock.

### 3.2 Accepted-state operators

For any operator $E$, write
$$\mathcal{V}[E] \;=\; \{ z : E(z) \neq \varnothing \}$$
for the set of states at which $E$ admits at least one action. Thus $\mathcal{V}_{\mathrm{typ}} = \mathcal{V}[E_{\mathrm{typ}}]$, $\mathcal{V}_w = \mathcal{V}[E_w]$, $\mathcal{V}_{\mathrm{phys}} = \mathcal{V}[E_{\mathrm{tube,phys}}]$, $\mathcal{V}_{\mathrm{end}} = \mathcal{V}[E_{\mathrm{end}}]$, and the compensatory accepted set
$$\mathcal{V}_{\mathrm{weak}} \;=\; \bigcap_{w \in W_+} \mathcal{V}_w .$$
With this notation the central noncommutation is visually explicit:
$$\underbrace{\{ z : \textstyle\bigcap_w E_w(z) \neq \varnothing \}}_{\mathcal{V}_{\mathrm{typ}} \ \text{(common plan)}} \;\subseteq\; \underbrace{\bigcap_w \{ z : E_w(z) \neq \varnothing \}}_{\mathcal{V}_{\mathrm{weak}} \ \text{(per weight)}}.$$

---

## 4. Results: The Separation Theorem

### 4.1 A general quantifier-separation proposition

**Proposition 1.** *Let $\{E_\lambda(z)\}_{\lambda \in \Lambda}$ be a family of action sets. Then always*
$$\Big\{ z : \textstyle\bigcap_{\lambda} E_\lambda(z) \neq \varnothing \Big\} \;\subseteq\; \bigcap_{\lambda} \big\{ z : E_\lambda(z) \neq \varnothing \big\}.$$
*Equality holds exactly when, for every $z$ in the right-hand set, the family $\{E_\lambda(z)\}_\lambda$ admits a common selector. No topology on the action space is imposed; in finite menus the check is combinatorial: if the action set is finite, only finitely many distinct $E_\lambda(z)$ occur and common-selector existence is a finite enumeration (on the witness of Section 4.5, $|A| = 4$). For infinite families, classical sufficient conditions (finite-intersection property plus compactness/closedness in a declared topology) are available; they are not needed anywhere in this paper and are stated only to delimit the mechanism.*

*Proof.* If $a \in \bigcap_\lambda E_\lambda(z)$, then each $E_\lambda(z)$ is nonempty, so $z$ lies in the right-hand set. The inclusion fails at $z$ precisely when each $E_\lambda(z)$ is nonempty but $\bigcap_\lambda E_\lambda(z) = \varnothing$, i.e. when no common selector exists; this is the stated equality condition. $\square$

Proposition 1 isolates the mechanism: the separation exhibited in Section 4.5 is a strict instance of this inclusion, witnessed by states at which the nonemptiness witnesses differ with the weight.

### 4.2 The full-cone identity

**Lemma 2 (full-cone pointwise equivalence).** *For $v \in \mathbb{R}^n$:*
$$v \ge 0 \ \text{componentwise} \iff w \cdot v \ge 0 \ \text{for every } w \in W_+ = \mathbb{R}^n_+ \setminus \{0\}.$$

*Proof.* ($\Rightarrow$) $w \ge 0$, $w \neq 0$, $v \ge 0$ gives $w \cdot v = \sum_i w_i v_i \ge 0$. ($\Leftarrow$) If $v_k < 0$, take $w = e_k \in W_+$: then $w \cdot v = v_k < 0$. $\square$

Lemma 2 says that at a *fixed* trajectory the full-cone aggregate is lossless: nonnegativity of every weighted sum is equivalent to componentwise nonnegativity. The separation established below is therefore entirely dynamic — a matter of quantifier order — not static scalarization blindness.

### 4.3 The assessment identity and hierarchy

**Theorem 3 (assessment identity and hierarchy).**

*(i) Hierarchy.* For every $w \in W_+$ and every $z$:
$$E_{\mathrm{typ}}(z) \;\subseteq\; E_w(z) \;\subseteq\; E_{\mathrm{tube,phys}}(z) \;\subseteq\; E_{\mathrm{end}}(z).$$

*(ii) Localization.* For every $z$:
$$E_{\mathrm{typ}}(z) \;=\; \bigcap_{w \in W_+} E_w(z).$$
Hence $\mathcal{V}_{\mathrm{typ}} = \{ z : \bigcap_w E_w(z) \neq \varnothing \}$.

*Proof.* (i) Let $a \in E_{\mathrm{typ}}(z)$. For every disturbance $d$, $\mathrm{Tube}(a,d) \subseteq S = S^{\mathrm{phys}} \cap \{s \ge 0\}$; by Lemma 2 every tube point satisfies $w \cdot s \ge 0$ for every $w \in W_+$, and likewise every successor state lies in $G^w$; hence $a \in E_w(z)$. The remaining inclusions follow from $S^w \subseteq S^{\mathrm{phys}}$, $G^w \subseteq G^{\mathrm{phys}}$, and $\mathrm{End}(a,d) \subseteq \mathrm{Tube}(a,d)$. (ii) The inclusion $\subseteq$ is part (i) intersected over $w$. For the reverse inclusion, let $a \in \bigcap_{w \in W_+} E_w(z)$. For every $d$ and every tube point $p \in \mathrm{Tube}(a,d)$, every $w \in W_+$ gives $w \cdot s(p) \ge 0$, so by Lemma 2 $s(p) \ge 0$ componentwise; hence $\mathrm{Tube}(a,d) \subseteq S$. The same argument with $\mathrm{Succ}$ gives $\mathrm{Succ}(a,d) \subseteq G$. Thus $a \in E_{\mathrm{typ}}(z)$. $\square$

Part (i) is constraint-set monotonicity of viability/reachability operators under nested safe sets (Aubin, 1991; Frankowska, 1989). The claim of this paper is part (ii) and the witnessed strictness of the resulting inclusion.

### 4.4 Price-family monotonicity

**Theorem 4 (price-family monotonicity).** *For a weight family $W \subseteq W_+$ define $\mathcal{V}_W = \bigcap_{w \in W} \mathcal{V}_w$. Then*
$$\mathcal{V}_{\mathrm{typ}} \;\subseteq\; \mathcal{V}_W \;\subseteq\; \mathcal{V}_{\mathrm{phys}},$$
*and if $W_1 \subseteq W_2$ then $\mathcal{V}_{W_2} \subseteq \mathcal{V}_{W_1}$.*

*Proof.* For the second inclusion: by Theorem 3(i), $E_w(z) \subseteq E_{\mathrm{tube,phys}}(z)$ for every $w$, so $\mathcal{V}_w \subseteq \mathcal{V}_{\mathrm{phys}}$, and intersecting over $w \in W$ preserves the inclusion. For the first: if $z \in \mathcal{V}_{\mathrm{typ}}$, then by Theorem 3(ii) there exists $a \in \bigcap_{w \in W_+} E_w(z)$; this same $a$ lies in $\bigcap_{w \in W} E_w(z)$, so $E_w(z) \neq \varnothing$ for every $w \in W$, i.e. $z \in \mathcal{V}_W$. Monotonicity: intersecting over a larger family can only shrink the intersection. $\square$

Theorem 4 makes precise the claim that *restricting* the price family *enlarges* the compensatory accepted set; the full cone is therefore the strictest compensatory reading, and any separation exhibited at the full cone persists for every restricted family.

### 4.5 The witness datum

Two architectures — extraction ($q = 0$) and regeneration ($q = 1$) — share one review interval $[0,1]$, with phase state $(q, x, s_1, s_2)$: a physical reserve stock $x$ and two typed floors $s_1$ (protected-group service surplus) and $s_2$ (remediation-liability coverage), both normalized to $0$. The transition-safe set is $S_0 = \{ x \ge 0, s_1 \ge 0, s_2 \ge 0 \}$; the destination set is $G = \{ (1, x, s) : x \ge 0, s \ge 0 \}$, with destination maintainability witnessed by the destination hold policy, a declared datum. The destination reset applies the gain vector $e = (1/4, 1/4)$ componentwise to both typed floors; $e$ is declared strictly positive so that successors are interior to $G$, and no inequality of Theorem 5 binds on its magnitude. The rescue cost is $c = 1$ (STAGED spends one unit of $x$).

**Disturbance convention (action-indexed).** The disturbance set is $\{\beta, \alpha\}$, where $\alpha$ triggers the worst-case dip — of fixed depth 2, per the action table below — in the *active action's characteristic coordinate* ($s_1$ for FAST, $s_2$ for SLOW) and $\beta$ is the analogous disturbance applied to the other coordinate; the two disturbances are never required to hit a coordinate the action does not move. Each action's worst-case tube below is the tube under its own characteristic dip, which is the worst case for that action's constraint; a disturbance label shared across the two actions still takes effect only on the coordinate each action moves, so FAST's $s_2$-tube and SLOW's $s_1$-tube are unchanged, and the distinction does not affect the separations of Theorem 5.

The four actions available from any initial state $(0, x, s)$ with $x \ge 0$, $s \ge 0$, written as piecewise-linear maps on the breakpoints $\{0, \tfrac12, 1\}$, monotone on each piece (so every tube is the exact visited set — there is no outer approximation):

| Action | Within-interval trajectory (worst case) | Successor |
|---|---|---|
| NO-SWITCH | state constant | $\{(0, x, s)\}$ — misses $G$ |
| FAST | $s_1(t) = s_1 - 4t$ on $[0,\tfrac12]$, $s_1 - 4(1-t)$ on $[\tfrac12,1]$; $s_2, x$ constant | $\{(1, x, s + e)\}$ |
| SLOW | $s_2(t) = s_2 - 4t$ on $[0,\tfrac12]$, $s_2 - 4(1-t)$ on $[\tfrac12,1]$; $s_1, x$ constant | $\{(1, x, s + e)\}$ |
| STAGED | $x(t) = x - t$ on $[0,1]$; floors grow to $s + e$ | $\{(1, x - 1, s + e)\}$ |

The worst-case tube of FAST is thus $[s_1 - 2, s_1]$ in the $s_1$ coordinate with $s_2$ and $x$ constant; the worst-case tube of SLOW is symmetric; the worst-case tube of STAGED is $[x - 1, x]$ in the $x$ coordinate with both floors nondecreasing.

### 4.6 Witnessed separation

**Theorem 5 (witnessed separation).** *On the witness datum of Section 4.5, over initial states $X_0 = \{(0, x, s) : x \ge 0, s \ge 0\}$:*

**(1)** $\mathcal{V}_{\mathrm{typ}} = \{ x \ge 1 \} \cup \{ s_1 \ge 2 \} \cup \{ s_2 \ge 2 \}.$

**(2)** $\mathcal{V}_{\mathrm{weak}} = \bigcap_{w \in W_+} \mathcal{V}_w = \{ x \ge 1 \} \cup \{ s_1 + s_2 \ge 2 \}.$

**(3)** $\mathcal{V}_{\mathrm{phys}} = \mathcal{V}_{\mathrm{end}} = X_0.$

*Define the following sets, distinguished precisely:*
- $\mathrm{FP}_0 = \{ s_1 < 2,\ s_2 < 2,\ s_1 + s_2 \ge 2 \}$ — the aggregate-versus-direct-floor discrepancy region, with $x$ unrestricted. This is **not** entirely a false-positive set, because for $x \ge 1$ the STAGED action is typed-admissible.
- $R = \mathrm{FP}_0 \cap \{ x \ge 1 \}$ — the **rescue set**: the already-typed slice of the discrepancy region, whose states are typed-transformable at the declared cost, witnessed by STAGED.
- $I = \mathrm{FP}_0 \cap \{ x < 1 \}$ — the **impossibility region**.
- $\mathrm{FP}_{\mathrm{agg}} = \mathcal{V}_{\mathrm{weak}} \setminus \mathcal{V}_{\mathrm{typ}}$ — the genuine compensatory-versus-noncompensatory acceptance gap.

**(4)** $\mathrm{FP}_{\mathrm{agg}} = I.$ *The genuine acceptance gap is exactly the impossibility region; it is nonempty, and its open interior (in the state space) is $\{ 0 < x < 1,\ 0 < s_1 < 2,\ 0 < s_2 < 2,\ s_1 + s_2 > 2 \}$. The rescue set $R$ is a subset of $\mathcal{V}_{\mathrm{typ}}$, not of the gap: it is the part of $\mathrm{FP}_0$ that is not a false positive.*

**(5)** *Both hierarchy inclusions are strict: every point of $I$ lies in $\mathcal{V}_{\mathrm{weak}} \setminus \mathcal{V}_{\mathrm{typ}}$, and the point $(x, s_1, s_2) = (\tfrac12, \tfrac1{10}, \tfrac1{10})$ lies in $\mathcal{V}_{\mathrm{phys}} \setminus \mathcal{V}_{\mathrm{weak}}$.*

**(6) Per-weight plan disagreement.** *On the relative interior of $\mathrm{FP}_0$ (where $s_2 > 0$ and $s_2 < 2$), writing $r = w_2 / w_1$, the FAST-certifying weight ratios are exactly $\{ r \ge \rho_1 \}$ and the SLOW-certifying ratios exactly $\{ r \le \rho_2 \}$, with*
$$\rho_1 = \frac{2 - s_1}{s_2}, \qquad \rho_2 = \frac{s_1}{2 - s_2}, \qquad \rho_2 \ge \rho_1 \iff s_1 + s_2 \ge 2.$$
*High-$s_2$-weight assessors ($r > \rho_2$) license FAST only; low-$s_2$-weight assessors ($r < \rho_1$) license SLOW only; intermediate assessors license both. On $I$ no single action serves every weight — $\bigcap_w E_w(z) = E_{\mathrm{typ}}(z) = \varnothing$ by Theorem 3(ii) — while on $R$ the STAGED action is typed-admissible and hence serves every weight.*

**(7) The rescue split.** *$R$ is typed-transformable, witnessed by STAGED: bridging at physical cost $c = 1$ keeps both floors intact and lands in $G$. $I$ is aggregate-feasible for every cone weight yet admits **no** typed-admissible action, with four exhibited violations: FAST violates the $s_1$ floor under the adverse disturbance; SLOW violates the $s_2$ floor; STAGED drives $x$ negative; NO-SWITCH misses $G$.*

*Proof.* **(1)** Typed admissibility requires the worst-case tube in $S_0$ and the successor in $G$. NO-SWITCH never reaches $G$ (its successor retains $q = 0$), so it is never admissible. For FAST, the worst-case $s_1$-tube is $[s_1 - 2, s_1]$, safe if and only if $s_1 \ge 2$; its successor $(1, x, s + e)$ lies in $G$ given $x \ge 0$. Hence FAST is typed-admissible exactly when $s_1 \ge 2$. Symmetrically, SLOW is typed-admissible exactly when $s_2 \ge 2$. For STAGED, the floors grow through the interval and the successor lies in $G$; the binding constraint is the $x$-tube $[x - 1, x]$, safe if and only if $x \ge 1$. Therefore $E_{\mathrm{typ}}(z) \neq \varnothing$ exactly on $\{x \ge 1\} \cup \{s_1 \ge 2\} \cup \{s_2 \ge 2\}$.

**(2)** Fix $w = (w_1, w_2) \in W_+$. NO-SWITCH misses $G^w$ and is never admissible. FAST is $w$-admissible if and only if its worst-case aggregate value stays nonnegative: $w_1(s_1 - 2) + w_2 s_2 \ge 0$, i.e. $w_1 s_1 + w_2 s_2 \ge 2 w_1$ (automatic when $w_1 = 0$). Symmetrically SLOW is $w$-admissible if and only if $w_1 s_1 + w_2 s_2 \ge 2 w_2$. STAGED is $w$-admissible if and only if $x \ge 1$ (the physical constraint within $S^w$), since $w \cdot s \ge 0$ holds automatically along its tube. Hence $z \in \mathcal{V}_w$ whenever $x \ge 1$; and if $x < 1$, then $z \in \mathcal{V}_w$ if and only if at least one of the two inequalities above holds.

Suppose first $x \ge 1$: then $z \in \mathcal{V}_w$ for every $w$, so $z \in \mathcal{V}_{\mathrm{weak}}$. Suppose $x < 1$ and $s_1 \ge 2$ or $s_2 \ge 2$: say $s_1 \ge 2$; then FAST is typed-admissible by (1), hence $w$-admissible for every $w$, so $z \in \mathcal{V}_{\mathrm{weak}}$. It remains to treat $x < 1$ with $s_1 < 2$ and $s_2 < 2$. For $w_1 > 0$, write $r = w_2/w_1$: FAST is $w$-admissible exactly when $s_1 + r s_2 \ge 2$, i.e. $r \ge (2 - s_1)/s_2 = \rho_1$ (using $s_2 > 0$; when $s_2 = 0$ the condition reduces to $s_1 \ge 2$, which is excluded). SLOW is $w$-admissible exactly when $s_1 + r s_2 \ge 2r$, i.e. $r \le s_1/(2 - s_2) = \rho_2$ (using $s_2 < 2$). The boundary weights are the same limiting cases: at $w_1 = 0$ ($r \to \infty$) FAST is licensed provided $s_2 \ge 0$, while SLOW is strictly rejected on the region $s_2 < 2$; symmetrically, at $w_2 = 0$ ($r = 0$) SLOW is licensed provided $s_1 \ge 0$, while FAST is rejected on the region $s_1 < 2$. Therefore $z \in \mathcal{V}_w$ for every $w \in W_+$ if and only if the intervals $\{r \ge \rho_1\}$ and $\{r \le \rho_2\}$ together cover all of $[0, \infty]$, which holds exactly when $\rho_2 \ge \rho_1$. Computing:
$$\rho_2 \ge \rho_1 \iff \frac{s_1}{2 - s_2} \ge \frac{2 - s_1}{s_2} \iff s_1 s_2 \ge (2 - s_1)(2 - s_2) \iff s_1 + s_2 \ge 2,$$
with both denominators positive in the present case. Hence, in this case, $z \in \mathcal{V}_{\mathrm{weak}}$ if and only if $s_1 + s_2 \ge 2$. Assembling the three cases, and noting $\{s_1 \ge 2\} \cup \{s_2 \ge 2\} \subseteq \{s_1 + s_2 \ge 2\}$ under nonnegativity:
$$\mathcal{V}_{\mathrm{weak}} = \{ x \ge 1 \} \cup \{ s_1 + s_2 \ge 2 \}.$$

**(3)** In the physical operators the only constraint is $x \ge 0$ (with $q = 1$ at the destination). FAST and SLOW have tubes within $S^{\mathrm{phys}}$ and successors in $G^{\mathrm{phys}}$ for every $z \in X_0$ (their dips affect only $s$, which is unconstrained physically); STAGED does so exactly for $x \ge 1$. Hence $E_{\mathrm{tube,phys}}(z) \neq \varnothing$ for every $z \in X_0$, so $\mathcal{V}_{\mathrm{phys}} = X_0$. For the endpoint operator, the endpoint values of FAST and SLOW lie in $S^{\mathrm{phys}}$ for every $z \in X_0$, so $\mathcal{V}_{\mathrm{end}} = X_0$ as well.

**(4)** By (1)–(2):
$$\mathrm{FP}_{\mathrm{agg}} = \mathcal{V}_{\mathrm{weak}} \setminus \mathcal{V}_{\mathrm{typ}} = \big[ \{x \ge 1\} \cup \{s_1 + s_2 \ge 2\} \big] \setminus \big[ \{x \ge 1\} \cup \{s_1 \ge 2\} \cup \{s_2 \ge 2\} \big] = \{ x < 1,\ s_1 < 2,\ s_2 < 2,\ s_1 + s_2 \ge 2 \} = I.$$
This set is nonempty (e.g. $(x, s_1, s_2) = (\tfrac12, \tfrac65, \tfrac65)$), and its relatively open interior is the stated region.

**(5)** By (4), $I = \mathrm{FP}_{\mathrm{agg}} = \mathcal{V}_{\mathrm{weak}} \setminus \mathcal{V}_{\mathrm{typ}} \neq \varnothing$, so the first inclusion is strict. For the second, the point $(\tfrac12, \tfrac1{10}, \tfrac1{10})$ satisfies $x < 1$ and $s_1 + s_2 = \tfrac15 < 2$, so it lies outside $\mathcal{V}_{\mathrm{weak}}$ by (2), while by (3) it lies in $\mathcal{V}_{\mathrm{phys}}$.

**(6)** The threshold characterization was derived in the proof of (2): with $r = w_2 / w_1$, FAST is licensed exactly for $r \ge \rho_1$ and SLOW exactly for $r \le \rho_2$, and $\rho_2 \ge \rho_1 \iff s_1 + s_2 \ge 2$. On $\mathrm{FP}_0$ the inequality $s_1 + s_2 \ge 2$ holds, so the two licensing intervals overlap and together cover all weights; strictly on the relative interior ($s_1 + s_2 > 2$) both thresholds are finite and the intervals overlap in a nondegenerate interval, with $r > \rho_2$ licensing FAST only and $r < \rho_1$ licensing SLOW only. On $I$ (where $x < 1$), STAGED is inadmissible for every $w$, so $E_{\mathrm{typ}}(z) = \bigcap_w E_w(z) = \varnothing$ by Theorem 3(ii): no single action serves every weight. On $R$ (where $x \ge 1$), STAGED lies in $E_{\mathrm{typ}}(z) = \bigcap_w E_w(z)$ and serves every weight.

**(7)** On $R$, STAGED's tube is $[x - 1, x] \times \{s \to s + e\}$: the $x$-tube stays nonnegative because $x \ge 1$, the floors grow, and the successor $(1, x - 1, s + e) \in G$. On $I$, the four exhibited violations exhaust the action set and each violates a typed constraint: FAST's $s_1$-tube reaches $s_1 - 2 < 0$; SLOW's $s_2$-tube reaches $s_2 - 2 < 0$; STAGED's $x$-tube reaches $x - 1 < 0$; NO-SWITCH's successor misses $G$. $\square$

*Boundary conventions.* The formulas for $\rho_1, \rho_2$ require $s_2 > 0$ and $s_2 < 2$. On the boundary faces ($s_2 = 0$, $s_2 = 2$, $s_1 = 0$, $s_1 = 2$, $s_1 + s_2 = 2$) the classification follows directly from the closed-set identities of (1)–(2); no interior formula is applied there.

**Remark.** The compensatory assessment's binding condition is the total budget $s_1 + s_2 \ge 2$; the noncompensatory assessment requires either one floor to survive its own worst-case dip or the bridge stock to be fundable. The region between the two conditions is where the compensatory doctrine certifies — per weight, with weight-dependent plans — transitions the noncompensatory doctrine rejects.

### 4.7 Figure 1

**Figure 1.** The discrepancy region $\mathrm{FP}_0$ is the portion of the square $0 \le s_1, s_2 \le 2$ lying on or above $s_1 + s_2 = 2$: the closed upper-right triangle with vertices $(0,2)$, $(2,0)$, $(2,2)$, minus the two legs $s_1 = 2$ and $s_2 = 2$ (strict boundaries); the vertices themselves are outside $\mathrm{FP}_0$, and the axis vertices $(0,2)$, $(2,0)$ are not even limit points of it along the axes. Its interior is $0 < s_1, s_2 < 2$ with $s_1 + s_2 > 2$. **Panel A ($x < 1$, shown at $x = 0$):** the region is the genuine impossibility region $I = \mathrm{FP}_{\mathrm{agg}}$; the interior witness $(s_1, s_2) = (6/5, 6/5)$ is marked. **Panel B ($x \ge 1$, shown at $x = 1$):** the same aggregate-versus-floor region is the rescue set $R$, witnessed by STAGED. The threshold curves $\rho_1, \rho_2$ are drawn only on the open subregion where $s_1 > 0$, $s_2 > 0$ and $s_2 < 2$ ($\rho_2 = 0$ when $s_1 = 0$). The point $(x, s_1, s_2) = (\tfrac12, \tfrac1{10}, \tfrac1{10})$ is annotated separately in Panel A's caption, since it is not a point of the two-dimensional $s$-plane alone. The same region is not to be labelled "false positive" without fixing $x$: at $x \ge 1$ it is rescue, at $x < 1$ it is impossibility.

### 4.8 Propagation under hold-prefix extension

**Theorem 6 (propagation).** *Extend the witness datum to $m \ge 2$ review intervals by prepending hold intervals (sole action HOLD: constant tube $\{z\}$, successor $\{z\}$, safe set $S_0$; the final interval carries the witness). Assume: HOLD is available at every prefix state; the hold tube is exactly $\{z\}$; the prefix safe sets contain the witness states; terminal and successor architecture labels are unchanged; and no additional reset or disturbance branches are introduced. Then:*

*(i) Hierarchy.* For every stage $j$:
$$\mathcal{V}^{\mathrm{typ}}_j \;\subseteq\; \bigcap_{w \in W_+} \mathcal{V}^{w}_j \;\subseteq\; \mathcal{V}^{\mathrm{phys}}_j.$$
*This inclusion holds for every multi-interval typed exact-tube datum; it is constraint monotonicity under backward induction.*

*(ii) Persistence of strictness.* *The stage-0 accepted regions are the witness regions pulled back through the holds, so both strictness witnesses of Theorem 5 persist under this hold-prefix extension.*

*(iii)* *The displayed separation is not an artifact of the one-interval framing for the constructed hold-prefixed datum. Strictness for arbitrary multi-stage systems does not follow without a separate persistence theorem: a later stage can erase the gap if every aggregate-feasible state has a common typed-safe continuation, if the weak and typed terminal sets coincide on the reachable subset, or if actions couple across stages.*

*Proof.* (i) Backward induction on stages. Base: at the final stage the terminal sets satisfy $G \subseteq G^w \subseteq G^{\mathrm{phys}}$ by Lemma 2 and the definition of the terminal sets. Step: the accepted set of a stage is the set of states from which some action keeps the tube in the safe set and the successor in the next-stage accepted set; applying Theorem 3(i) to the stage's action sets and the induction hypothesis to the next-stage accepted sets preserves the three-way inclusion at the stage level. (ii) With HOLD the unique prefix action, a prefix state is accepted exactly when it lies in the prefix safe set and in the next-stage accepted set; the stage-0 regions are therefore the witness regions of Theorem 5 pulled back through the (identity) holds, and the strictness witnesses $(I \neq \varnothing$ and the point $(\tfrac12, \tfrac1{10}, \tfrac1{10}))$ persist. (iii) The three listed mechanisms are each sufficient to erase the gap in a multi-stage setting, so no unconditional generalization is asserted. $\square$

**Theorem 7 (erasure witness).** *The propagation claim of Theorem 6 is architecture-conditional: there is a two-interval datum whose single-interval truncation exhibits the acceptance gap and whose two-stage extension erases it, through the terminal-coincidence mechanism of Theorem 6(iii).*

*Datum.* Two capital forms, floors at zero, the bridge stock absent ($x \equiv 0$); states are pairs $s = (s_1, s_2)$. Stage 2 (final interval): safe set $S_0^{(2)} = \mathbb{R}^2$ (no path constraint), terminal sets $G^{(2)} = G^{w,(2)} = G = \{ s \ge 0 \}$ — coincident for every weight — and a single action REPAIR with tube $\{s\}$ (safe trivially) and successor $(1, 1) \in G$. Stage 1: safe set $S_0 = \{ s \ge 0 \}$; two actions with constant tubes, safe at every state of $S_0$: A1 with successor $(s_1 - 1, s_2 + 1)$ and A2 with successor $(s_1 + 1, s_2 - 1)$; the stage-1 terminal architecture is the stage-2 accepted sets. Initial state $z^* = (\tfrac25, \tfrac25)$.

*In the two-stage datum the gap is erased.* REPAIR is typed-admissible — hence $w$-admissible for every weight — from every state, so $\mathcal{V}_{\mathrm{typ}}^{(2)} = \mathcal{V}_w^{(2)} = \mathbb{R}^2$ for every $w$: the stage-2 accepted sets coincide. Backward induction then admits both A1 and A2 at $z^*$ (safe tubes; successors in $\mathcal{V}_{\mathrm{typ}}^{(2)} = \mathbb{R}^2$), so $z^*$ is typed-accepted at stage 0, and weak acceptance follows from typed acceptance.

*In the single-interval truncation — the same stage-1 datum with the final interval collapsed to its terminal sets, $G = \{s \ge 0\}$ and $G^w = \{w \cdot s \ge 0\}$ — the gap is present.* Both successors leave $G$ ($s_1 - 1 = -\tfrac35 < 0$ and $s_2 - 1 = -\tfrac35 < 0$), so $z^*$ is typed-rejected. For the weak doctrine, writing $r = w_2 / w_1$ on the interior of the weight cone: A1 is $w$-admissible exactly when $(s_1 - 1) + r (s_2 + 1) \ge 0$, i.e. $r \ge \tfrac{1 - s_1}{s_2 + 1} = \tfrac37$; A2 exactly when $(s_1 + 1) + r (s_2 - 1) \ge 0$, i.e. $r \le \tfrac{s_1 + 1}{1 - s_2} = \tfrac73$; the two intervals cover $[0, \infty]$ because $\tfrac37 < \tfrac73$, and the boundary weights are covered directly ($r = 0$: A2 gives $w_1(s_1 + 1) \ge 0$; $r \to \infty$: A1 gives $w_2(s_2 + 1) \ge 0$). Hence $z^* \in \mathcal{V}_{\mathrm{weak}}$ in the truncation, and the gap $\mathcal{V}_{\mathrm{weak}} \setminus \mathcal{V}_{\mathrm{typ}}$ contains $z^*$. $\square$

The witness datum of Section 4.5 is immune to this erasure. Its gap is tube-driven: on $I$ every member of the four-action menu violates the stage-1 path constraint $S_0$ itself (the two dips and the bridge deficit of Theorem 5(7)), and a later stage cannot repair a violated tube — the stage-1 constraint is local to stage 1. Theorem 6's safe direction is secured by exactly the assumptions the erasure datum violates (unchanged terminal architecture, no new branches); the two results together delimit the persistence claim: hold-prefix extension preserves the separation, arbitrary multi-stage extension does not, and the erasure mechanisms of Theorem 6(iii) are realizable.

### 4.9 Machine verification

The continuum statements of Theorems 3–8 are established by the displayed proofs. A companion software artifact (deterministic, exact integer arithmetic at scale 40; no floating point, tolerances, or randomness) checks the finite rational instance of Theorems 3–6: it verifies the action classifications, the region identities, and the accepted-set identities on a $31^3 = 29{,}791$-state grid (a product of 31-point chains on $x, s_1, s_2$; the box endpoints are part of the artifact's configuration and are archived with it), with a finite verification set containing the analytically identified critical weight ratios $\rho_1, \rho_2$ and their midpoint $(\rho_1 + \rho_2)/2$ for every enumerated grid state. All 25 checks pass; re-execution reproduces the outputs exactly. The verification levels are kept distinct:

| Claim layer | What is established | By what |
|---|---|---|
| Symbolic theorem | Exact continuum identities and inequalities for the declared witness | Displayed proofs |
| Machine artifact | Exact finite rational checks of the classification on the enumerated grid | Deterministic computation |
| Empirical implication | Conditional design requirements only | Not established here |

The finite grid does not by itself prove the continuum identities; it validates the symbolic classification on the enumerated instance.

### 4.10 Menu convexification: the blend family

The declared action space is the finite menu {FAST, SLOW, STAGED, NO-SWITCH} of deterministic actions; time-shared policies are not members of it. The convexification instrument is the blend family: for each $\delta \in (0,1)$, the action BLEND$_\delta$ time-shares FAST and SLOW at intensity $\delta$ — its tube is the pointwise convex mixture of the two worst-case tubes and its successor the corresponding mixture of the two successors.

**Theorem 8 (blend collapse).** *On the witness datum of Section 4.5, over initial states $X_0$:*

*(i) BLEND$_\delta$ is typed-admissible at $z$ exactly when*
$$\delta \in \left[\,1 - \frac{s_2}{2},\; \frac{s_1}{2}\,\right],$$
*an interval nonempty exactly when $s_1 + s_2 \ge 2$ (a singleton at equality), independent of $x \ge 0$ and of the weight.*

*(ii) The typed acceptance set of the menu augmented by the blend family is exactly the compensatory region:*
$$\mathcal{V}_{\mathrm{typ}}^{\mathrm{blend}} \;=\; \{ x \ge 1 \} \cup \{ s_1 + s_2 \ge 2 \} \;=\; \mathcal{V}_{\mathrm{weak}}.$$
*Convexification of the menu collapses the acceptance gap: $\mathrm{FP}_{\mathrm{agg}}$ vanishes under the augmented menu, and the blend family reaches exactly the compensatory region and nothing beyond — on $\mathcal{V}_{\mathrm{phys}} \setminus \mathcal{V}_{\mathrm{weak}}$ no blend is typed-admissible.*

*(iii) The admissible window depends on the state through $(s_1, s_2)$ alone: a single $\delta$ serves every weight $w \in W_+$. On the impossibility region the blend is therefore the common action that no member of the finite menu supplies — the acceptance gap is a property of the deterministic menu, not of the doctrines.*

*Proof.* (i) FAST's worst-case tube has $s_1$-coordinates $[s_1 - 2, s_1]$ and $s_2$-coordinate $\{s_2\}$; SLOW's has $s_1$-coordinate $\{s_1\}$ and $s_2$-coordinates $[s_2 - 2, s_2]$; both keep $x$ nonnegative throughout (their dips affect only $s$). The blended tube therefore has $s_1$-coordinates $[s_1 - 2\delta, s_1]$, $s_2$-coordinates $[s_2 - 2(1-\delta), s_2]$, and nonnegative $x$-coordinates (convex combinations of nonnegative quantities). Typed admissibility requires the tube within $S_0 = \{x \ge 0, s \ge 0\}$ and the successor in $G$. The tube condition is exactly the displayed window. The successor is the mixture of the two successors, which the datum fixes to the same value — the action table of Section 4.5 gives both FAST and SLOW the successor $(1, x, s + e)$ — so the blended successor is $(1, x, s + e) \in G$: $x \ge 0$ and the destination label is $1$. The window is nonempty exactly when $1 - s_2/2 \le s_1/2$, i.e. $s_1 + s_2 \ge 2$; at equality it is the singleton $\delta = s_1/2 = 1 - s_2/2$, feasible because $S_0$ is closed. On the boundary faces ($s_1 = 0$ or $s_2 = 0$) the window is closed at the corresponding endpoint, and the classification follows the boundary conventions of Section 4.6.

(ii) If $s_1 + s_2 \ge 2$, (i) supplies a typed-admissible blend whatever the value of $x \ge 0$; if $s_1 + s_2 < 2$, no blend is typed-admissible by (i), and the deterministic menu contributes exactly $\mathcal{V}_{\mathrm{typ}} = \{x \ge 1\} \cup \{s_1 \ge 2\} \cup \{s_2 \ge 2\} \subseteq \{x \ge 1\} \cup \{s_1 + s_2 \ge 2\}$. Hence the augmented typed set equals $\{x \ge 1\} \cup \{s_1 + s_2 \ge 2\} = \mathcal{V}_{\mathrm{weak}}$ by Theorem 5(2) — and nothing beyond, since every admissible blend satisfies $s_1 + s_2 \ge 2$ and the deterministic actions stay within $\mathcal{V}_{\mathrm{typ}}$.

(iii) Immediate from the window's state dependence and from typed admissibility implying $w$-admissibility for every weight. $\square$

*Remark.* The collapse is exact and weight-independent: a single time-shared plan serves every assessor on $I$, where the per-weight plans of Theorem 5(6) necessarily differ. The nonconvexity at work is menu geometry — the finiteness and determinism of the declared action space — not the Pareto-frontier geometry under which weighted sums fail to reach nonconvex frontier parts (Das and Dennis, 1997); the two mechanisms are distinct, and both are now explicit.

---

## 5. Interpretation

### 5.1 The doctrinal reading

The scalarized operators $\{E_w\}_{w \in W_+}$ formalize **one** compensatory assessment doctrine: a single aggregate index $w \cdot s$, nonnegative scalarization weights on capital forms, substitution across floors permitted at those weights, disturbances respected. We refer to this as *the scalarized aggregate doctrine as formalized here*, not as "weak sustainability" simpliciter. The weak-sustainability literature is broader than this operator: it encompasses aggregate wealth, constant total capital, nondeclining comprehensive consumption, substitutability assumptions, discounting, shadow prices, and intertemporal investment conditions (Neumayer, 2013; World Bank, 2011; Boos, 2015; Dasgupta and Mäler, 2000; Asheim, 1994). Likewise, strong sustainability is not always equivalent to requiring every stock coordinate to remain nonnegative at every instant; critical-natural-capital frameworks may use thresholds, safe operating spaces, irreversibility, resilience, or minimum-service conditions (Ekins et al., 2003; Doyen and Gajardo, 2020). The typed operator $E_{\mathrm{typ}}$ is a formal idealization of the separately-binding-floor reading, in the same sense that the scalarized operators idealize one aggregation doctrine.

Within this precise scope, Theorem 5 reads: **the two formalized doctrines can disagree on the same transition datum, with the same robustness standard and the same action set, in the direction compensatory-accepts / noncompensatory-rejects, on a relatively open region — and the disagreement is not an artifact of one bad weight: every weight accepts, each licensing a different physical transition.** The plans are genuinely different transitions (FAST and SLOW violate different floors at different times), which is the dynamic formalization of substitution across floors. By Theorem 3(ii), the precise seat of the disagreement is the noncommutativity of "choose an action" with "for all weights." At the static level the full-cone aggregate is lossless (Lemma 2), so the compensatory doctrine's blind spot is not the existence of an aggregate index but the *policy dependence* of the aggregate-feasible transition: the index certifies a set of transitions, no one of which the noncompensatory assessment accepts. The two quantifier orders also carry an information reading: $\exists a\, \forall w$ is a commitment made before the weight is known — the strong doctrine's robustness demand — while $\forall w\, \exists a_w$ lets the action be chosen after the weight is observed; on the witness, the acceptance gap between the two orders measures the value of information about the assessment weight. Theorem 8 closes this reading on the menu side: a single time-shared blend serves every weight on the impossibility region, so the measured value of information is the cost of the finite deterministic menu rather than of the weight information itself.

Throughout, we use "nonnegative scalarization weights" for elements of $W_+$ and reserve the word "prices" for the interpretive discussion, because actual prices may be strictly positive, endogenous, dynamically determined, state-dependent, or dimensionally heterogeneous, and the theorems require none of those properties. The operators are linear scalarizations with weights fixed over the review interval; nonlinear aggregate indices — CES-type substitutability or endogenous, state-dependent weighting of the kind that diverges near zero-stock boundaries — are different assessment operators, and the theorems claim nothing for them.

### 5.2 Positioning against established theory

**Conceded as established.** The backward recursion of Section 3 is a typed instance of established robust-predecessor, reach-avoid, capture-basin, and hybrid-reachability constructions (Aubin, 1991; Aubin, Bayen, and Saint-Pierre, 2011; Saint-Pierre, 1994; Lygeros, Tomlin, and Sastry, 1999). Theorem 3(i) is constraint-set monotonicity of viability kernels and reachability sets (Aubin, 1991; Frankowska, 1989). The foundation statement that values may be only weakly comparable — and that this incommensurability is constitutive of ecological economics — is due to Martinez-Alier, Munda, and O'Neill (1998); our operators give one formal model of the distinction that paper draws between strong and weak commensurability. The characterization of which sustainability criteria admit indicator representations, and the role of maximin and MSY-type reasoning in making strong sustainability operational, are developed in Martinet (2011), Cairns and Martinet (2014), and Doyen and Gajardo (2020); the latter in particular shows that the multicriteria maximin value is the solution of a static Pareto problem over the viability kernel, which is the strongest formal statement in the literature of the position — strong sustainability as constraint viability rather than optimality — that the typed operator formalizes here. Static scalarization limitations are established: weighted sums cannot reach nonconvex parts of Pareto fronts (Das and Dennis, 1997), a mechanism of frontier geometry under a single optimization, different from the action-quantifier mechanism of this paper. Compensability analysis is established in multi-criteria decision analysis, including the explicit mapping of compensatory aggregation to weak sustainability and outranking methods to strong sustainability (Cinelli, Coles, and Kirwan, 2014; Schär, Pohl, and Geldermann, 2025). Scalarization-dependent optimal policies are a staple of multi-objective optimization.

**Claimed.** (i) The action-set identity $E_{\mathrm{typ}} = \bigcap_{w \in W_+} E_w$ with the full-cone choice isolating the separation as purely dynamic (Theorem 3(ii)). (ii) The general quantifier-separation proposition (Proposition 1). (iii) The price-family monotonicity theorem (Theorem 4). (iv) The explicit exact-tube witness with a relatively open region of strict separation and the rescue/impossibility split (Theorem 5). (v) Persistence of the witness hierarchy under hold-prefix extension (Theorem 6). (vi) The explicit two-stage erasure datum delimiting that persistence (Theorem 7). (vii) The blend-collapse theorem, under which time-shared convexification of the menu closes the gap exactly at the compensatory region (Theorem 8).

**Novelty qualification.** To our knowledge, this paper provides an explicit exact-tube witness for this dynamic separation in a compensatory/noncompensatory assessment setting. We do not assert priority over the elementary quantifier fact $\exists a\, \forall w \neq \forall w\, \exists a_w$, which is standard. Whether an equivalent dynamic separation appears in adjacent literatures (multi-objective robust control, viability theory, multi-criteria decision analysis) is a bounded absence in our review, not an established universal negative.

### 5.3 What the theorem does not say

- **No aggregate blindness at fixed trajectories.** Lemma 2 establishes the opposite: at a fixed trajectory, the full-cone aggregate is lossless.
- **No separation on every datum.** Where a single action is safe for all weights, the assessments coincide. The theorem is an existence separation with an open region, plus the always-valid hierarchy and localization.
- **No infinite-horizon, stochastic, partial-observation, or endogenous-event extension.** All statements are for finite-horizon exact-tube data with declared disturbance sets.
- **No claim that the full nonnegative cone is the only reasonable weight family.** Theorem 4 shows that restricting the family enlarges the compensatory accepted set, so the full cone is the strictest compensatory reading; a practitioner restricting weights to a policy-relevant family obtains a strictly weaker separation guarantee.
- **No welfare claim about prices.** The weights model an assessment doctrine, not a normative endorsement.
- **No transfer to empirical systems.** The theorem is about assessment operators on a declared datum; it asserts nothing about any fishery or aquifer.
- **No claim that $\mathcal{V}_{\mathrm{weak}}$ is the genuine-savings or inclusive-wealth criterion.** The operator is the strictest compensatory reading (every weight, each licensing an action); the genuine-savings literature's criterion is a different object, and the witness's reserve stock is deliberately kept out of the weighted aggregate (a design choice recorded in Section 4.5, not a consequence of aggregation).
- **No absolute impossibility.** The impossibility region is a negative certificate relative to the declared four-action menu; with a larger menu it can shrink or vanish, and Section 5.5 states the completeness status that an application must report.
- **No universal doctrinal ranking.** The inclusion $\mathcal{V}_{\mathrm{typ}} \subseteq \mathcal{V}_{\mathrm{weak}} \subseteq \mathcal{V}_{\mathrm{phys}}$ is a theorem about the defined operators under common action and disturbance classes, common safe-set inclusion, common horizon, common tube semantics, and common terminal condition. It does not establish a universal ranking of endpoint, weak, and strong sustainability doctrines.
- **No separation under coupled all-floor shocks.** The witness disturbance convention is action-indexed (Section 4.5): each action's worst case is its own characteristic dip. A datum whose disturbance class couples simultaneous dips across all floors of every action degenerates the per-weight licensing structure — the principal actions fail together and the compensatory/noncompensatory divergence collapses into universal rejection. The separation is exhibited on, and claimed for, the declared action-indexed class only.
- **Convexification of the menu.** Time-shared or fractional action policies are not members of the declared action space, and every stated separation is scoped to the finite deterministic menu. The convexification question is nevertheless answered, not bracketed: the blend family of Theorem 8 collapses the typed acceptance set exactly onto the compensatory region, so the separation is a property of the deterministic menu, not of the doctrines — menu geometry, distinct from the Pareto-frontier geometry of scalarization limits (Das and Dennis, 1997).

### 5.4 Policy implications

The separation theorem has four implications, each stated at its actual strength.

**First.** Aggregate indices alone cannot certify noncompensatory transition safety under the present assessment semantics. A scalarized assessment can certify its own criterion — aggregate feasibility; what it cannot certify is typed safety unless an additional bridge theorem is supplied. This follows from Theorem 5: the compensatory accepted set strictly contains the noncompensatory accepted set, and the excess region is where the two criteria diverge.

**Second.** When the typed recursion identifies an admissible rescue action whose feasibility is controlled by a resource margin, investment in that margin is a candidate remedy; reweighting alone cannot substitute for it within the witness semantics (Section 5.5). This is a theorem about the witness, not a universal policy law: it applies where a resource-controlled rescue action exists.

**Third.** Per-floor reporting alongside aggregate reporting is necessary for detecting this class of discrepancy. It is not universally necessary for every sustainability judgement; but where the question is whether a transition respects separately-binding floors, an aggregate index alone cannot distinguish the rescue region from the impossibility region. A minimum report for such an assessment should include: (1) typed floors and their provenance; (2) aggregate weights or the weight family; (3) policy quantifiers; (4) the disturbance set; (5) the observation and implementation model; (6) exact versus conservative tube status; (7) terminal maintainability; (8) action-exhaustion status; (9) uncertainty and approximation bounds; (10) normative premises.

**Fourth.** Reporting regimes that evaluate endpoints only — audited annual snapshots, the form taken by much aggregated sustainability accounting — evaluate only the weakest operator of the chain of Section 3.1, and under those semantics they license transitions that violate typed floors mid-interval without the assessment detecting it; the per-floor reporting of the Third implication is what detects the discrepancy. The paper asserts nothing empirical about any particular reporting regime.

### 5.5 Rescue as action synthesis, and data requirements

**Rescue as an action-synthesis theorem.** Rescue is an operation on the impossibility region: rather than saying the recursion "names the binding resource," define a resource-augmentation map
$$\mathsf{Aug}_r : (x, s, \mathcal{A}) \mapsto (x + r,\; s,\; \mathcal{A} \cup \{\mathrm{STAGED}_r\})$$
and the minimal rescue threshold
$$r^* = \inf\{\, r : \exists a \in \mathcal{A}_r,\; a \in E_{\mathrm{typ}}(z) \,\},$$
where $\mathcal{A}_r$ denotes the augmented menu. On the witness, for the STAGED action and $x < 1$: $r^* = 1 - x$, the exact resource increment that converts an impossibility-region state into a typed-transformable one. States of the rescue set $R$ need no augmentation — STAGED is typed-admissible there as it stands — which is exactly why $R$ is not part of the acceptance gap. This turns the second policy implication into a theorem.

**Data requirements for empirical application.** The theorem is a result about assessment operators on a declared datum. Empirical application requires, in addition to the typed floors, disturbance set, action set, tube model, and destination maintainability witness of Section 4.5, the following load-bearing data:

1. **Action-set completeness status.** A negative certificate over a finite action set proves impossibility only relative to that set. The application must state whether $A$ is exhaustive, a registered policy menu, a sampled subset, or an inner approximation. If incomplete, the verdict is "no safe transition exists among the registered actions," not "no safe transition exists."
2. **Calibration and identifiability data.** Parameter estimates, uncertainty sets, structural alternatives, validation data, observation error, model discrepancy, missing-data treatment, disturbance dependence. A declared $D$ is necessary but not sufficient; it must be justified, or the verdict marked conditional on model credibility.
3. **Policy and authority data.** Who may select each action, what information they possess, decision timing, enforcement assumptions, compliance uncertainty, strategic responses, resource and legitimacy constraints.
4. **Threshold-uncertainty semantics.** A physical or normative floor is rarely known exactly. Distinguish the deterministic floor $s_i(z) \ge 0$ from robust threshold safety $s_i(z;\theta) \ge 0$ for all $\theta \in \Theta$, and from probabilistic or confidence-level versions if admitted.
5. **Destination maintainability status.** Whether the destination maintainability witness is physical, simulated, or merely declared.

---

## 6. Discussion

### 6.1 Negative certificates as first-class results

The framework treats a **negative certificate** — a rejection with an exhibited violated constraint, per action, exhausting the action set — as a first-class result. Theorem 5(7) is the assessment-side instance: four actions, four exhibited violations, a certified impossibility together with the resource and the weight at which the impossibility dissolves. The methodological content is that complexity is retained only on scored evidence; an unfalsified model class is not an achievement, and a rejected complexity is a finding. The admission discipline is the same one the empirical papers of this research programme instantiate — preregistered scoring against declared baselines, held-out defect audits, frozen retention rules — and those empirical results belong to the companion papers, not here.

### 6.2 Limitations

(i) The assessment-separation theorem is an existence result with an open region, not a claim that the gap is always large; on data in which the assessments coincide, it yields nothing. (ii) Its novelty verdicts at no-match-found are bounded-search absences; if external review overturns a verdict, the claim is weakened to the supported subset. (iii) The framework covers no infinite horizons, no partial observation, no stochastic chance constraints, and no endogenous event times at the operator level. (iv) The paper asserts nothing empirical. (v) The framework extensions (governance constructors, intergenerational structures, composition interfaces) are stated at partial or conditional status in the Supplementary Material; they are not completed mathematics. (vi) Computational tractability: on a finite explicit state–action–disturbance graph with constant-time predicate evaluation, the backward recursion is polynomial in the graph size and horizon. For continuous, hybrid, or belief-state models, the graph itself may be exponentially large, infinite, or only approximately representable; exact tube inclusion may be computationally hard or undecidable; and grid cardinality grows as $N_{\mathrm{grid}} = \prod_{i=1}^n N_i$ — exponentially in dimension when floors are coordinates. The witness's tractability is a property of its small finite rational datum.

---

## 7. Conclusions

The weak-sustainability and strong-sustainability traditions are usually compared as doctrines — as different normative stances on substitutability. This paper shows that their divergence survives translation into assessment mechanics, at the level of a theorem. On a typed transition datum under exact-tube semantics, the compensatory reading (per-weight acceptance) and the noncompensatory reading (common-plan acceptance) are related by a quantifier commutation that can fail on an open region of state space; where it fails, every scalarization weight certifies a transition, but no single transition is certified by all weights, and the certified set splits into states rescuable by a resource-controlled action and states that are impossible under every weight. The mechanism is not scalarization blindness — at fixed trajectories the full-cone aggregate is lossless — but the policy dependence of the aggregate-feasible transition.

For the construction of composite sustainability indices, the theorem has a concrete consequence. An index can be sound at the level of accounting and still over-certify at the level of assessment, because certification is a quantifier statement about transitions, not a property of a number. Where separately-binding floors matter, per-floor reporting is not a presentation preference but a detection requirement: the aggregate alone cannot distinguish the rescue region from the impossibility region. The bridge theorem a composite index needs — that some single transition serves every admissible weight — is exactly what the frameworks' reporting conventions should be asked to exhibit.

---

## Data availability statement

The symbolic proofs are contained in this article. The companion verification artifact (exact-integer regression checks of the finite rational instance, all 25 checks, deterministic and re-executable) is deposited in a public repository with stable identifier, software version, execution command, and expected output hashes; a link is provided with the submission.

## Declaration of competing interest

None.

---

## References

Asheim, G. B. (1994). Net national product as an indicator of sustainability. *Scandinavian Journal of Economics*, 96(2), 257–265.

Aubin, J.-P. (1991). *Viability Theory*. Birkhäuser, Boston.

Aubin, J.-P., Bayen, A. M., and Saint-Pierre, P. (2011). *Viability Theory: New Directions*, 2nd ed. Birkhäuser, Boston.

Boos, A. (2015). Genuine savings as an indicator for "weak" sustainability: Critical survey and possible ways forward in measuring weak sustainability. *Sustainability*, 7(4), 4146–4163.

Cairns, R. D., and Martinet, V. (2014). An environmental-economic measure of sustainable development. *European Economic Review*, 69, 4–17.

Cinelli, M., Coles, S. R., and Kirwan, K. (2014). Analysis of the potentials of multi criteria decision analysis methods to conduct sustainability assessment. *Ecological Indicators*, 46, 138–148.

Das, I., and Dennis, J. E. (1997). A closer look at drawbacks of minimizing weighted sums of objectives for Pareto set generation in multicriteria optimization problems. *Structural Optimization*, 14, 63–69.

Dasgupta, P., and Mäler, K.-G. (2000). Net national product, wealth, and social well-being. *Environment and Development Economics*, 5(1), 69–93.

Doyen, L., and Gajardo, P. (2020). Sustainability standards, multicriteria maximin, and viability. *Natural Resource Modeling*, 33(3), e12250.

Ekins, P., Simon, S., Deutsch, L., Folke, C., and De Groot, R. (2003). A framework for the practical application of the concepts of critical natural capital and strong sustainability. *Ecological Economics*, 44(2), 165–185.

Frankowska, H. (1989). Optimal trajectories associated with a solution of contingent Hamilton–Jacobi equations. *Applied Mathematics and Optimization*, 19, 291–311.

Hanley, N., Moffatt, I., Faichney, R., and Wilson, M. (1999). Measuring sustainability: A time series of alternative indicators for Scotland. *Ecological Economics*, 28(1), 55–73.

Hickel, J. (2020). The sustainable development index: Measuring the ecological efficiency of human development in the Anthropocene. *Ecological Economics*, 167, 106331.

Lygeros, J., Tomlin, C., and Sastry, S. (1999). Controllers for reachability specifications for hybrid systems. *Automatica*, 35(3), 349–370.

Martinez-Alier, J., Munda, G., and O'Neill, J. (1998). Weak comparability of values as a foundation for ecological economics. *Ecological Economics*, 26(3), 277–286.

Martinet, V. (2011). A characterization of sustainability with indicators. *Journal of Environmental Economics and Management*, 61(2), 183–197.

Neumayer, E. (2013). *Weak versus Strong Sustainability: Exploring the Limits of Two Opposing Paradigms*, 4th ed. Edward Elgar, Cheltenham.

Saint-Pierre, P. (1994). Approximation of the viability kernel. *Applied Mathematics and Optimization*, 29, 187–209.

Schär, S., Pohl, E., and Geldermann, J. (2025). Analysing the compensatory properties of the outranking approach PROMETHEE. *Journal of Multi-Criteria Decision Analysis*, 32, e70013.

Solow, R. M. (1974). Intergenerational equity and exhaustible resources. *Review of Economic Studies*, 41, 29–45.

Usubiaga-Liaño, A. (2025). Strong sustainability in the SEEA and the wider indicator debate. *One Ecosystem*, 10, e141086.

World Bank. (2011). *The Changing Wealth of Nations: Measuring Sustainable Development in the New Millennium*. World Bank, Washington, D.C.

---

## Supplementary Material

Framework extensions (governance constructors with declared support, the implementability ladder, the commons obstruction, intergenerational structures, the nested-impossibility theorem, composition interfaces), the planetary-boundaries application note, the full set of framework definitions, and the declared conjectures are provided in the accompanying supplementary file `paper1_supplementary.md`, together with their status declarations.

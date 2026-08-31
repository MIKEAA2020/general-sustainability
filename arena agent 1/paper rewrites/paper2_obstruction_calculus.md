# An Obstruction Calculus for Viability under Incomplete Observation

## Abstract

Viability under perfect measurement has a complete theory: the viability kernel characterizes the states from which some feedback keeps the system within its constraints. When the state is observed only through an incomplete map, the sufficiency direction has a canonical answer — Veliov's output-feedback regulation condition, and the estimation-set reduction to perfect information. This paper supplies the complementary necessity theory: an obstruction calculus certifying when *no observation-based policy exists*. Four mechanisms are developed with complete proofs. (i) A finite-time exit certificate: under an Isaacs-type drift condition the disturbance forces constraint violation within a computable time, defeating every control of any information structure. (ii) A common-action obstruction: if the safe controls of the states compatible with the current information set intersect emptily, no observation-based policy is viable, though every compatible state is individually viable. (iii) A delayed-information obstruction with timing bound: information accurate but arriving after the enforced exit time cannot save the belief state. (iv) A certification limit: an exact observation-only certifier exists if and only if safe-set membership is constant on observation fibres. A fifth mechanism shows certainty-equivalence control under a biased observation emptying a nonempty perfect-information kernel. The calculus is positioned against barrier certificates and estimation tubes, and its consequences for monitoring design are drawn.

**Keywords:** viability theory; incomplete observation; output feedback; safety certification; differential inclusions; sustainability

**Mathematics Subject Classification (2010):** 34A60; 93B03; 93B07; 93C41; 91B76

---

## 1. Introduction

### 1.1 The problem

Viability theory characterizes the states of a constrained control system from which there exists at least one control keeping every future state within a constraint set (Aubin, 1991). For sustainability problems the constraint set is a set of floors — stock levels, service thresholds, safety margins — and viability is the formal counterpart of the requirement that a development path be maintained rather than merely optimized (Béné, Doyen, and Gabay, 2001; De Lara and Doyen, 2008; Doyen et al., 2012; Doyen and Gajardo, 2020). The theory under *perfect measurement* is complete in the relevant sense: the viability kernel exists as the largest viable subset, and Nagumo-type tangency conditions certify it.

Sustainability governance, however, operates under *incomplete observation*. Stocks are assessed at discrete review intervals; indicators are coarser than the state; some stocks are unobserved altogether; and the information that does arrive may arrive late. The question this paper addresses is: under an incomplete observation structure, when can we *certify that no policy works* — that the viability problem is infeasible for reasons of information, not of dynamics?

The question has a natural split. The *sufficiency* direction has a canonical literature. Veliov (1993) gives conditions under which an output-feedback regulation map exists when only incomplete and inexact measurement is available, and shows that under perfect measurement his condition reduces to the classical viability condition of Haddad (1981). The estimation-tube programme of Quincampoix, Cardaliaguet, and Saint-Pierre (see Cardaliaguet, Quincampoix, and Saint-Pierre, 2007) passes from imperfect information in the measurement space to perfect information in an estimation space, with equality of the corresponding value functions and a Dini-derivative characterization. In the control-verification literature, barrier certificates certify safety for continuous and hybrid systems (Prajna and Jadbabaie, 2004; Prajna, Jadbabaie, and Pappas, 2007), and converse results show that — under convex-duality conditions on density functions — the existence of a barrier certificate is also *necessary* for safety (Prajna and Rantzer, 2005), with necessary-and-sufficient characterizations for hybrid inclusions under mild regularity (Maghenem and Sanfelice, 2019).

What is missing, and what this paper supplies, is the *necessity* side of the viability question itself under incomplete observation: a calculus of obstruction certificates. An obstruction certificate is a finite, checkable argument that a prescribed class of observation-based policies fails — not because a particular policy is bad, but because the information structure leaves no room for any policy. The two directions are complementary: Veliov's condition tells us when output feedback *can* work; the obstruction calculus tells us when it *cannot* — and, for the borderline cases, which quantitative feature of the observation design (timing, coarseness, bias, aggregation) is responsible.

### 1.2 Contributions

Four obstruction mechanisms are developed, each with a complete proof, and one further mechanism is exhibited by construction:

1. **The finite-time exit certificate** (Theorem 1). Under a Dini-drift condition of Isaacs type — the disturbance chooses after the control — the disturbance can force exit from the safe set within an explicit time bound, for *every* admissible control of any information structure. This is the base obstruction: when it applies, the viability question is closed without any observation-theoretic argument.

2. **The instantaneous common-action obstruction** (Theorem 2, Example 1). If the safe-control sets of the states compatible with the current information set intersect emptily, then no observation-based policy is viable, even though every compatible state is individually viable under full information. The failure is purely informational: no stochasticity, no estimation error.

3. **The delayed-information obstruction** (Theorem 3). If the information needed to distinguish safe from unsafe compatible states arrives only at time $T_{\mathrm{obs}}$, and the disturbance can force constraint violation earlier than $T_{\mathrm{obs}}$, then no observation-based policy is viable. The timing bound $\inf q / \varepsilon < T_{\mathrm{obs}}$ is stated explicitly: information may be accurate but arrive too late.

4. **The fibre certification criterion** (Theorem 4, Corollary 5). An exact observation-only safety certifier — a function of the observation that returns "safe" exactly on the safe set — exists if and only if safe-set membership is constant on every observation fibre. The certainly-safe set is the sound relaxation: the largest set of observations that can be labelled safe without further information.

5. **The certainty-equivalence trap** (Remark 1). Even an *injective* observation empties a nonempty perfect-information kernel if the policy class is restricted to certainty-equivalence controllers that apply a fixed state-feedback law to the uncorrected observation. The kernel empties by restriction of the policy class, not by loss of information.

Throughout, "obstruction" means a *certified* failure: each theorem exhibits the violating constraint, the admissible disturbance, and the quantitative bound that make failure inevitable, for every policy in the declared class. The calculus is positioned against the barrier-certificate literature (Section 6.2) and the estimation-tube programme (Section 6.3), and its consequences for the design of monitoring and indicators in sustainability governance are drawn in Section 6.4.

### 1.3 Related work

The viability theory background is Aubin (1991) and Aubin, Bayen, and Saint-Pierre (2011); approximation of kernels is due to Saint-Pierre (1994). Robust (disturbance-averse) viability is developed in Aubin and Frankowska (1990) and Frankowska (1989). Under incomplete measurement, Veliov (1993) gives the sufficiency theorem already mentioned; Quincampoix and Veliov (1994) treat viability with a priori unknown but observable parameters; and the estimation-set reduction is presented in Cardaliaguet, Quincampoix, and Saint-Pierre (2007). In verification, barrier certificates originate with Prajna and Jadbabaie (2004); their worst-case framework and converse are Prajna, Jadbabaie, and Pappas (2007) and Prajna and Rantzer (2005); hybrid necessary-and-sufficient characterizations are Maghenem and Sanfelice (2019). The sustainability application domain is represented by Béné, Doyen, and Gabay (2001), De Lara and Doyen (2008), Doyen et al. (2012), and Doyen and Gajardo (2020). To our knowledge, the obstruction certificates of Theorems 2–4 — in particular the certification criterion of Theorem 4 and the timing bound of Theorem 3 — have not been stated in this form; we do not claim the underlying elementary facts (quantifier commutation; Dini comparison) as new.

### 1.4 Organization

Section 2 fixes the framework: the control system, the viability kernel hierarchy, observation structures, information states, and the safe-control correspondence. Section 3 develops the obstruction calculus (Theorems 1–3, Example 1). Section 4 develops the certification limits (Theorem 4, Corollary 5, Proposition 6, Remark 1). Section 5 reviews the sufficiency landscape, which this paper does not re-derive, with citations. Section 6 discusses the position of the calculus relative to barrier certificates and estimation tubes, and draws the governance consequences. Section 7 concludes. Proofs are complete in the main text; results whose proofs repeat established literature are cited rather than reproduced, and are marked as such.

---

## 2. Framework

### 2.1 The control system and the kernel hierarchy

Fix a state space $X \subseteq \mathbb{R}^n$, a control set $U$, a disturbance set $D$, and dynamics
$$\dot x(t) = f(x(t), u(t), d(t)), \qquad u(t) \in U(x(t)), \quad d(t) \in D(x(t)),$$
with $f$ continuous, $U$ and $D$ set-valued with closed graph and nonempty compact values, and admissible controls and disturbances taken to be measurable selections. Let $\mathcal{V} \subseteq X$ be a closed constraint set. A *causal policy* $\pi$ is a map from the observation record to controls, respecting the declared information structure. The standard objects are:

- $\mathrm{Viab}(\mathcal{V}; U, \pi_{\mathrm{perf}})$: the **viability kernel** under full-information (state-feedback) policies — the largest closed subset of $\mathcal{V}$ from which there exists a state-feedback control keeping the trajectory in $\mathcal{V}$ for all time (Aubin, 1991).
- $\mathrm{RViab}(\mathcal{V})$: the **robust kernel**, the largest subset of $\mathcal{V}$ from which there exists a state-feedback policy keeping every trajectory — for *every* admissible disturbance realization — in $\mathcal{V}$ (Aubin and Frankowska, 1990).
- $\mathrm{EViab}_{\mathcal{I}}(\mathcal{V})$, $\mathrm{ERViab}_{\mathcal{I}}(\mathcal{V})$: the **epistemic kernels** — the objects of this paper. Their elements are *states of information*, not physical states (Section 2.3).

Projected to physical state space, the informational hierarchy reads
$$\mathrm{IRViab}_{\mathfrak{I}}(\mathcal{V}) \;\subseteq\; K_{\mathcal{I}} \;\subseteq\; \mathrm{RViab}(\mathcal{V}) \;\subseteq\; \mathrm{Viab}(\mathcal{V}),$$
where $K_{\mathcal{I}}$ is the epistemic kernel projected to physical states and $\mathrm{IRViab}_{\mathfrak{I}}$ its institutionally restricted counterpart (Section 6.4). Each strict inclusion has a distinct cause: robust contraction arises from disturbances; epistemic contraction from indistinguishability; institutional contraction from restricted authority, enforcement, and allocation. The present paper characterizes the *epistemic* contraction: the mechanisms by which indistinguishability empties or shrinks the kernel.

### 2.2 The safe-control correspondence

For a constraint set $\mathcal{V}$ described by finitely many $C^1$ constraint functions, $\mathcal{V} = \{ x : q_j(x) \ge 0,\ j = 1..m \}$, define the **safe-control correspondence** at $x \in \mathcal{V}$:
$$\mathcal{R}_{\mathcal{V}}(x) \;=\; \Big\{ u \in U(x) : \forall d \in D(x),\; \forall j \text{ with } q_j(x) = 0,\; \nabla q_j(x) \cdot f(x, u, d) \ge 0 \Big\},$$
the set of controls whose drift is inward (subtangential) on every active constraint face, uniformly over the disturbance. For $x$ in the interior of $\mathcal{V}$ (no active constraints), $\mathcal{R}_{\mathcal{V}}(x) = U(x)$. By Nagumo's theorem in its robust form, $x_0 \in \mathrm{RViab}(\mathcal{V})$ if and only if $x_0 \in \mathcal{V}$ and there is a measurable selection $u(x) \in \mathcal{R}_{\mathcal{V}}(x)$ along the trajectory it generates (Aubin, 1991; Frankowska, 1989). The correspondence is the bridge between the pointwise (tangency) and the global (kernel) description, and it is the object the observation structure acts upon: an observation-based policy can select controls only as a function of the observation record.

### 2.3 Observation structures, information states, and epistemic kernels

An **observation structure** $\mathcal{I} = (Y, O)$ is a measurable space $Y$ and an observation map $O : X \to Y$. The policy observes $y(t) = O(x(t))$. At time $t$, the **information set** (belief) of a regulator who knows the dynamics, the disturbance class, and the record $(y(s))_{s \le t}$ is
$$B_t \;=\; \big\{ x \in X : O(x(\tau)) = y(\tau) \text{ for } \tau \le t \text{ along some admissible realization} \big\},$$
the set of states compatible with the record; we assume the standard set-membership semantics, so that $B_t$ contains every state consistent with the observations and the applied controls. A policy is **observation-based** if $u(t)$ depends on the record only through $B_t$ (equivalently, through the record itself). We write $U^B(B) = \bigcap_{x \in B} U(x)$ for the controls available at every compatible state — the only controls an observation-based policy may select without risking inadmissibility.

**Definition (epistemic kernels).** (i) $B_0 \in \mathrm{EViab}_{\mathcal{I}}(\mathcal{V})$ if there exists an observation-based policy such that, for every admissible disturbance, every trajectory compatible with the record remains in $\mathcal{V}$ for all time. (ii) $B_0 \in \mathrm{ERViab}_{\mathcal{I}}(\mathcal{V})$ if the same holds robustly — the policy must work against *every* admissible disturbance realization compatible with the record. We use $\mathrm{ERViab}$ throughout, since the disturbance classes of sustainability problems are adverse by construction; the theorems hold a fortiori for the weaker (non-robust) notion.

With these definitions, the informal statement of the paper is precise: **the epistemic kernel is the set of information states whose *compatible common* controls can enforce viability, and the obstruction calculus characterizes, with certificates, the information states outside it.**

---

## 3. The Obstruction Calculus

### 3.1 The finite-time exit certificate

The base obstruction operates before any observation-theoretic argument: a drift condition under which *no* control — of any information structure — can be viable.

**Theorem 1 (finite-time exit certificate).** *Let $q : X \to \mathbb{R}$ be a constraint function with $\mathcal{V} \subseteq \{ q \ge 0 \}$, and suppose there exist $a > 0$ and $\varepsilon > 0$ such that on the strip $\mathcal{S}_a = \{ x : 0 \le q(x) \le a \}$:*
$$\sup_{u \in U(x)} \inf_{d \in D(x)} D^+ q(x; f(x,u,d)) \;\le\; -\varepsilon \qquad \forall x \in \mathcal{S}_a, \tag{1}$$
*where $D^+ q(x; v) = \limsup_{h \downarrow 0} [q(x + hv) - q(x)]/h$ is the upper right Dini derivative of $q$ in direction $v$. Then for every admissible control and every initial state $x_0 \in \mathcal{S}_a$ there exists an admissible disturbance realization under which the trajectory leaves $\{ q \ge 0 \}$ — hence leaves $\mathcal{V}$ — within time at most $a/\varepsilon$.*

*Proof.* Fix an admissible control $u(\cdot)$. For each $x \in \mathcal{S}_a$, condition (1) gives $\inf_{d \in D(x)} D^+ q(x; f(x,u(t),d)) \le -\varepsilon$; by the measurable-selection theorem for set-valued maps with closed graph (Aubin and Frankowska, 1990, Thm. 8.1.3), there is a measurable selection $d(\cdot)$ with $d(t) \in D(x(t))$ and
$$D^+ q(x(t); f(x(t), u(t), d(t))) \le -\varepsilon$$
at every $t$ at which $x(t) \in \mathcal{S}_a$. Along the realization $(u(\cdot), d(\cdot))$ from $x_0$, the Dini comparison lemma (e.g. Aubin, 1991, Ch. 2) integrates the inequality to
$$q(x(t)) \;\le\; q(x_0) - \varepsilon t$$
as long as $x(t)$ remains in $\mathcal{S}_a$. Hence $q$ reaches $0$ at a time not exceeding $q(x_0)/\varepsilon \le a/\varepsilon$, and by continuity of $q$ along the trajectory the state leaves $\{ q \ge 0 \} \supseteq \mathcal{V}$ no later. The disturbance realization was chosen after the control — an enforcement, not an ambiguity. $\square$

Two readings of (1) matter. First, it is an **Isaacs-type condition**: the disturbance chooses after the control, so the certificate asserts that the disturbance can *enforce* exit against any policy. Second, (1) is the exact negation of a barrier condition: if instead $\inf_{d} \sup_{u} D^+ q \ge 0$ held on the boundary with a suitable Lyapunov-type margin, a barrier certificate of the classical form would certify safety (Section 6.2). Theorem 1 is the "unsafety" side of that duality, and it is unconditional: it needs no observation argument because it defeats all controls, including clairvoyant ones.

### 3.2 Epistemic emptiness: hidden modes

The remaining obstructions are *purely informational*: they apply to systems in which every state is individually viable under full information, and the kernel empties only because the observation structure merges states with incompatible safe controls.

**Theorem 2 (epistemic emptiness).** *There exist systems with $\mathrm{Viab}(\mathcal{V}; U, \pi_{\mathrm{perf}}) = \mathcal{V} \neq \varnothing$ and $\mathrm{ERViab}_{\mathcal{I}}(\mathcal{V}) = \varnothing$ for a non-injective observation map.*

*Proof (by construction).* Let $X = [1,2]$, $\dot S = u - r(S)$ with $r : [1,2] \to \mathbb{R}_{++}$ continuous, $U(S) = \{0, r(S)\}$, $\mathcal{V} = [1,2]$, and the constant observation $O(S) \equiv 0$. Under perfect information, the state-feedback control $u = r(S)$ gives $\dot S = 0$, so every $S_0 \in \mathcal{V}$ is viable: $\mathrm{Viab}(\mathcal{V}; U, \pi_{\mathrm{perf}}) = \mathcal{V}$. Under the constant observation, the information set is $B_t = [1,2]$ at every time, and the common control set is
$$U^B(B_t) = \bigcap_{S \in [1,2]} U(S) = \{0\} \cap \bigcap_{S} \{r(S)\} = \{0\},$$
because $r(S) > 0$ for every $S$ and no constant control equals $r(S)$ for all $S$. An observation-based policy is a function of the (constant) record, hence selects a constant $u \equiv 0$, giving $\dot S = -r(S) \le -\min_{[1,2]} r < 0$; every trajectory exits $\mathcal{V}$ downward in finite time. Hence $\mathrm{ERViab}_{\mathcal{I}}(\mathcal{V}) = \varnothing$. The system has no disturbance and no estimation error: the failure is caused entirely by the non-injectivity of $O$. $\square$

The construction isolates the mechanism: the observation merges states whose safe controls differ, and the merged belief admits no common control. The example also shows the empty-kernel phenomenon at its minimal size — two control values, one scalar state. The next theorem generalizes the mechanism from constant observations to arbitrary information sets.

### 3.3 The instantaneous common-action obstruction

**Theorem 3 (common-action obstruction).** *Let $B$ be an information set of the declared observation structure containing a boundary state of $\mathcal{V}$, and suppose no informative observation arrives before the next action must be selected. If*
$$\mathcal{R}_{\mathcal{V}}^B(B) \;:=\; \bigcap_{x \in B} \mathcal{R}_{\mathcal{V}}(x) \;=\; \varnothing, \tag{2}$$
*then $B \notin \mathrm{ERViab}_{\mathcal{I}}(\mathcal{V})$: every compatible state may be individually robustly viable, and the belief is nevertheless nonviable, because the state-specific safe actions are incompatible.*

*Proof.* Let $\pi$ be any observation-based policy, and let $a = \pi(B)$ be the single action it selects at the information set $B$ — a single action, since no informative observation arrives before the selection must be made. Because $\bigcap_{x \in B} \mathcal{R}_{\mathcal{V}}(x) = \varnothing$ while $\mathcal{R}_{\mathcal{V}}(x) = U(x)$ at interior points of $\mathcal{V}$ (no constraint is active there), the emptiness of the intersection must be caused by the boundary: there is a state $\bar x \in B \cap \partial \mathcal{V}$ with $a \notin \mathcal{R}_{\mathcal{V}}(\bar x)$. By the defining inequality of the safe-control correspondence, there are an active constraint $j$ (with $q_j(\bar x) = 0$) and a disturbance $\bar d \in D(\bar x)$ such that
$$\nabla q_j(\bar x) \cdot f(\bar x, a, \bar d) < 0.$$
By continuity of the right-hand side, the same strict inequality holds for all $(x, d)$ in a neighbourhood of $(\bar x, \bar d)$ intersected with $D$. Let the disturbance realize the constant (or piecewise-constant, matching measurability) selection $\bar d$ on a small initial interval; then along the compatible trajectory from $\bar x$ (compatible, since $\bar x \in B$), $q_j$ strictly decreases from $q_j(\bar x) = 0$, so the trajectory leaves $\mathcal{V}$ within the first sampling period — before any informative observation can arrive, whichever action the policy takes. Since $\pi$ was arbitrary, no observation-based policy keeps every compatible trajectory in $\mathcal{V}$: $B \notin \mathrm{ERViab}_{\mathcal{I}}(\mathcal{V})$. $\square$

Condition (2) is checkable: it requires computing the intersection of the safe-control sets over the information set, which for polyhedral constraint and control sets is a finite linear program. When the intersection is nonempty, the common action is a candidate for viability — Theorem 3 is a *necessary* condition with a constructive witness of failure, not a sufficient condition for success.

**Example 1 (hidden-mode conflict).** Let an unobserved parameter satisfy $\theta \in \{-1, +1\}$, with $\dot z = \theta u$, $u \in \{-1, +1\}$, and constraint $z \ge 0$. At $z = 0$: if $\theta = +1$, only $u = +1$ is safe; if $\theta = -1$, only $u = -1$ is safe. Both compatible states are individually robustly viable under full information (each admits its safe control), but the information set $B = \{(0, +1), (0, -1)\}$ satisfies $\mathcal{R}_{\mathcal{V}}^B(B) = \{+1\} \cap \{-1\} = \varnothing$, so $B \notin \mathrm{ERViab}_{\mathcal{I}}(\mathcal{V})$. This is a purely informational failure: no stochasticity and no estimation-quality argument is involved. The example is the two-action skeleton of every "the stock is either recovering or collapsing, and the safe policy differs between the two" situation.

### 3.4 The delayed-information obstruction

**Theorem 4 (delayed-information obstruction).** *Let $B_0$ be an initial information set, and let no informative observation arrive before time $T_{\mathrm{obs}} > 0$; between observations the information set evolves by the set-membership semantics of Section 2.3. Suppose there exist a constraint function $q$ with $\mathcal{V} \subseteq \{ q \ge 0 \}$, a constant $\varepsilon > 0$, and — for every observation-based policy — a compatible state $x^* \in B_0$ with $q(x^*) = \inf_{x \in B_0} q(x)$ and an admissible disturbance realization such that, along the realized trajectory from $x^*$ under the policy's actions, the record remains compatible and*
$$D^+ q(x(t); f(x(t), u(t), d(t))) \;\le\; -\varepsilon \qquad \text{while } q(x(t)) > 0, \tag{3}$$
*with*
$$T_{\mathrm{obs}} \;>\; \frac{\inf_{x \in B_0} q(x)}{\varepsilon}. \tag{4}$$
*Then $B_0 \notin \mathrm{ERViab}_{\mathcal{I}}(\mathcal{V})$: information may be accurate but arrive too late.*

*Proof.* Fix any observation-based policy. By hypothesis there is a compatible initial state $x^*$ with $q(x^*) = \inf_{x \in B_0} q(x)$ and an admissible disturbance realization satisfying (3). The Dini comparison lemma integrates (3) to
$$q(x(t)) \;\le\; q(x^*) - \varepsilon t \;=\; \inf_{x \in B_0} q(x) - \varepsilon t$$
while $q(x(t)) > 0$, so the trajectory violates the constraint at a time not exceeding $t^* = \inf_{x \in B_0} q(x) / \varepsilon$, which by (4) is strictly less than $T_{\mathrm{obs}}$. Until $t^*$, the record contains no informative observation (by construction of the compatible realization, the record up to any time before $T_{\mathrm{obs}}$ is consistent with the belief $B_t$), so the policy cannot have altered its action in response to the violation before it occurs. Since the policy was arbitrary and the violating realization is compatible with the observation record, no observation-based policy is robustly viable: $B_0 \notin \mathrm{ERViab}_{\mathcal{I}}(\mathcal{V})$. $\square$

The hypothesis (3) is the set-membership form of the drift condition: for *every* policy there is a compatible state and disturbance enforcing the drift; the adversary selects the true state and the disturbance, and the observations cannot expose the selection in time. Condition (4) is the **timing bound**: the first informative observation must precede the enforced exit time $\inf q / \varepsilon$. Theorem 4 is the quantitative refinement of Theorem 3 — the common-action obstruction is its instantaneous limit $T_{\mathrm{obs}} \to \infty$ with $\inf q = 0$ — and it is the obstruction that governs discrete-review governance: a review interval longer than the worst-case exit time is an information structure in which the exit is inevitable.

---

## 4. Certification Limits

### 4.1 Exact certification and the fibre criterion

The obstruction theorems of Section 3 concern *policies*. Sustainability governance also consumes *certificates*: verdicts — safe or unsafe — computed from observations alone, without reference to a policy. The question is when such verdicts can be exact.

**Definition (exact certifier).** For an admissible domain $Z \subseteq X$ and a safe set $K \subseteq Z$, an **exact certifier** based on the observation map $O : Z \to Y$ is a function $C : Y \to \{0,1\}$ such that
$$C(O(z)) = 1 \iff z \in K \qquad \text{for every } z \in Z.$$

**Theorem 5 (observation-fibre criterion).** *An exact certifier based on $O$ exists if and only if membership in $K$ is constant on every observation fibre:*
$$O(z_1) = O(z_2) \;\Longrightarrow\; \big[ z_1 \in K \iff z_2 \in K \big] \qquad \forall z_1, z_2 \in Z, \tag{5}$$
*equivalently, $K = O^{-1}(O(K))$ on the admissible domain.*

*Proof.* ($\Rightarrow$) If $C$ exists and $O(z_1) = O(z_2)$, then $\mathbf{1}_K(z_1) = C(O(z_1)) = C(O(z_2)) = \mathbf{1}_K(z_2)$, so membership is fibre-constant. ($\Leftarrow$) If (5) holds, define $C(y) = \mathbf{1}_K(z)$ for any $z \in Z$ with $O(z) = y$; (5) makes $C$ well defined on $O(Z)$ and exact by construction; extend $C$ arbitrarily on $Y \setminus O(Z)$. $\square$

**Corollary 6 (safety-crossing fibres and the certainly-safe set).** *If two admissible states share an observation and lie on opposite sides of a component safety constraint, no exact observation-only certificate exists. The largest set of observations that can soundly be labelled safe without further information is the certainly-safe set*
$$\mathcal{Y}_{\mathrm{safe}} \;=\; \big\{ y \in O(Z) : O^{-1}(y) \subseteq K \big\}.$$

*Proof.* A safety-crossing fibre violates (5), so Theorem 5 denies the certifier. On $\mathcal{Y}_{\mathrm{safe}}$ every compatible state is safe, so the constant verdict "safe" is sound; outside $\mathcal{Y}_{\mathrm{safe}}$ some compatible state is unsafe, so no sound "safe" verdict exists there. $\square$

The fibre criterion has a direct governance reading. A composite sustainability index is an observation map from the state of a socio-ecological system to a scalar; a floor is a safe set. Corollary 6 then states: an index whose fibres cross a floor boundary — whose value cannot distinguish a state violating the floor from one satisfying it — cannot support an exact certification of that floor, however carefully the index is thresholded. Per-floor observation is not a reporting preference; it is the only observation structure under which exact floor certification is possible at all. The certainly-safe set is the honest relaxation: the region where the index may certify safety, and the region where it must fall silent.

### 4.2 Output-feedback form

**Proposition 7 (common-action obstruction under output feedback).** *Suppose no informative observation arrives before the next action must be selected. If the compatible common-action set satisfies $\mathcal{U}_{\mathrm{com}}(B) = \bigcap_{x \in B} \mathcal{R}_{\mathcal{V}}(x) = \varnothing$ for the information state $B$, then $B$ is not robustly viable under output feedback — even if every compatible physical state is individually viable under full information.*

*Proof.* Output feedback must choose one prescription before the uncertainty within $B$ is resolved; by hypothesis no single action is robustly safe for all compatible states. This is Theorem 3 restated for the output-feedback policy class; the proof of Theorem 3 applies verbatim. $\square$

### 4.3 The certainty-equivalence trap

The obstruction of Theorem 2 relies on a non-injective observation — information genuinely lost. The same emptying occurs with a fully *injective* observation when the policy class is restricted to certainty-equivalence controllers.

**Remark 1 (certainty-equivalence obstruction).** Consider $\dot S = u - g(S)$ with $u \in [0, \bar u]$, $g$ strictly increasing, $g(0) = 0$, and $\mathcal{V} = [S_{\min}, S^*]$. Under perfect information the feedback $u(t) = g(S(t))$ gives $\dot S = 0$, so every $S_0 \in \mathcal{V}$ is viable and $\mathrm{Viab}(\mathcal{V}; U, \pi_{\mathrm{perf}}) = \mathcal{V} \neq \varnothing$. Now take the injective, biased observation $\hat S = S + b$ with $b > 0$, and restrict the policy class to **certainty-equivalence controllers** — causal maps that apply a fixed state-feedback law directly to the observation without correcting the bias: $u = g(\hat S)$. Then
$$\dot S = g(S + b) - g(S) > 0 \qquad \forall S,$$
and since $g$ is strictly increasing on the compact interval $[S_{\min}, S^* + b]$, $\dot S$ is bounded below by a positive constant there; hence $S$ strictly increases and exits above $S^*$ in finite time from every $S_0 \in \mathcal{V}$:
$$\mathrm{Viab}(\mathcal{V}; U, \pi_{\mathrm{CE}}) = \varnothing.$$
Because $\hat S \mapsto S = \hat S - b$ is invertible, an observer who inverts the bias — $u = g(\hat S - b) = g(S)$ — recovers the perfect-information kernel. The kernel emptied by a restriction of the admissible *policy class*, not by loss of information. The remark is the mechanism behind the monitoring-design consequence of Section 6.4: monitoring bounds observation error so that a desired state-feedback law is implementable, but the bound is useful only if the controller uses the correction; an uncorrected biased indicator empties the kernel that a corrected one preserves.

---

## 5. The Sufficiency Landscape (Cited)

For completeness and contrast, we record the sufficiency results against which the obstruction calculus is defined. Their proofs repeat established literature and are cited, not reproduced.

**(a) Veliov's output-feedback condition.** Veliov (1993) considers the same problem as Section 3 — a tube in the state space, incomplete and inexact measurement — and gives a sufficient condition for the existence of an *output-feedback regulation map*: a set-valued feedback of the measurement under which all trajectories starting from the graph of the tube remain in it. Under perfect measurement his condition reduces to the classical viability condition (Haddad, 1981). The complementarity with this paper is exact: Veliov's theorem certifies existence; the obstruction calculus certifies nonexistence; a problem that satisfies neither is the open middle ground, where a stronger observer or a finer observation structure is the only remedy.

**(b) The estimation-tube programme.** Cardaliaguet, Quincampoix, and Saint-Pierre (2007) pass from imperfect information in the measurement space to perfect information in an estimation space of *sets* of compatible states: the value functions of the two problems coincide, and the estimation-space problem admits a Dini-derivative characterization. The reduction is exact for value functions; what it does not supply is a *common prescription* — the estimation-space policy is a set-valued feedback, and its pointwise selections need not be jointly admissible. The common-action obstruction (Theorem 3) is precisely the certificate that no such joint selection exists at the information state in question.

**(c) Observer-and-buffer transfer.** When a full-information feedback exists with a strict inward margin, and an observer supplies exponentially convergent estimates, output feedback of the estimate preserves safety on a buffered subset: if $K_\varepsilon$ is a compact controlled-invariant subset of the interior of the kernel, the state feedback $u = k(x)$ is Lipschitz with constant $L_k$, the observer satisfies $\|\hat x(t) - x(t)\| \le M e^{-\lambda t}\|\hat x(0) - x(0)\|$, and the initial estimation error is small enough that $L_k M \|\hat x(0) - x(0)\|$ is absorbed by the margin, then $K_\varepsilon$ is viable under output feedback (observer-to-viability transfer with safety buffer; standard arguments in the observer-based control literature). Similarly, eroded kernels: if $K$ is robustly invariant under full-state feedback with a strict inward margin on $\partial K$, and estimation and implementation errors are bounded by $\varepsilon$, then an eroded set $K^{-c\varepsilon}$ is invariant under output feedback for a sensitivity constant $c > 0$ (erosion absorbs the error; see the buffer constructions of Section 1.3's cited literature). These results delimit the middle ground: under margins and convergence, output feedback *can* work; the obstruction calculus of Sections 3–4 states the conditions under which it *cannot*.

**(d) The linear substitution alternative.** For the finite linear model in which a resource-typed system must meet a demand vector through declared substitution pathways, exactly one of the following holds (Farkas, 1902; Gale, 1960): (i) there exists a non-negative pathway vector $a \ge 0$ satisfying the linear substitution constraints; or (ii) there exist multipliers $\alpha, \beta, \gamma \ge 0$ such that
$$\alpha^\top R + \beta^\top E - \gamma^\top Q \ge 0 \quad\text{componentwise},\qquad \gamma^\top s^{\mathrm{req}} > \alpha^\top x + \beta^\top e.$$
The second statement is a certificate that the declared substitution pathways cannot meet demand within the typed resource and capacity bounds; writing all constraints as $Aa \le \rho$, the pair is exactly the Farkas lemma alternative. The multipliers are a separation certificate, not universal exchange rates: nonlinear, nonconvex, path-dependent, spatial, or irreversible technologies require their own feasibility analysis, and an elasticity fitted near one operating point cannot establish global substitutability. This is the feasibility-side complement of the observation-side obstructions of Sections 3–4: where the present paper's certificates bound what *information* can achieve, the substitution alternative bounds what *material pathways* can achieve, and the same infeasibility discipline — exhibit the separating multiplier rather than assert impossibility — applies to both.

---

## 6. Discussion

### 6.1 The shape of the calculus

The five mechanisms form a complete small taxonomy of information-theoretic failure. The exit certificate (Theorem 1) is the dynamic obstruction: it defeats all controls, so it needs no observation argument. The common-action obstruction (Theorem 3) is the static obstruction: it defeats all policies at a single information state. The delayed-information obstruction (Theorem 4) interpolates between them in time. The fibre criterion (Theorem 5) is the certification obstruction: it limits not policies but verdicts. The certainty-equivalence trap (Remark 1) limits policy classes. A governance failure of observation can be diagnosed by which certificate applies: if the exit certificate holds, no monitoring design helps — the dynamics are adverse under every control; if only the common-action obstruction holds, the remedy is a finer observation structure (an informative measurement distinguishing the incompatible states); if the delayed-information obstruction holds with a slack timing bound, the remedy is a shorter review interval or a faster indicator; if the fibre criterion fails, the remedy is per-floor observation rather than a better threshold on the aggregate.

### 6.2 Relation to barrier certificates

Barrier certificates certify safety of continuous and hybrid systems from a scalar function whose zero level set separates the unsafe region from all trajectories (Prajna and Jadbabaie, 2004; Prajna, Jadbabaie, and Pappas, 2007). The converse direction — that safety implies, under convex-duality conditions on density functions, the existence of a barrier certificate — is Prajna and Rantzer (2005); necessary-and-sufficient barrier characterizations for hybrid inclusions under mild regularity are Maghenem and Sanfelice (2019). Theorem 1 is the observation-theoretic counterpart of that converse: it is a certificate of *unsafety* — a Dini-drift condition under which failure is inevitable — and it is constructive, exhibiting the enforcing disturbance and the exit time. The two literatures meet at the boundary: a system for which no barrier certificate exists and for which the exit certificate holds is unsafely classified by two independent arguments; the interest of the present calculus is that its remaining certificates (Theorems 3–5) act at the level of *information*, where barrier certificates have nothing to say: the barrier literature presupposes that the state is available for feedback.

### 6.3 Relation to estimation tubes

The estimation-tube programme shows that imperfect measurement can be absorbed into set-valued dynamics on an estimation space with no loss in value (Cardaliaguet, Quincampoix, and Saint-Pierre, 2007). The present theorems do not contradict that reduction; they delimit its reach. The reduction preserves *values* — whether the problem has a solution at a given information state. It does not supply the solution itself as an implementable observation-based control; and when the value is "infeasible," the reduction states the infeasibility but not its mechanism. The obstruction calculus supplies the mechanism, and each mechanism identifies the design change that removes it. The two directions are thus complementary at the level of governance: estimation tubes answer *whether*, the obstruction calculus answers *why not, and what to change*.

### 6.4 Consequences for monitoring and indicator design

Four consequences follow directly from the certificates.

**Timing.** Theorem 4 gives the minimal monitoring frequency in closed form: the first informative observation must precede the enforced exit time $\inf q / \varepsilon$. A review interval longer than the worst-case time from the least-constrained compatible state to constraint violation is an information structure under which the violation is undetectable in time, whatever the review then concludes. The bound is computable from the drift certificate (1), which is the same certificate a robustness analysis computes anyway.

**Coarseness.** Theorem 3 states that an observation structure merging two compatible states with incompatible safe controls is nonviable *at that information state*, even though both states are viable in isolation. The design consequence is that the observation must separate safety classes, not states: coarse indicators are admissible exactly when they are constant on the safe-control partition of the state space, and no finer.

**Aggregation.** Theorem 5 and Corollary 6 apply verbatim to composite indices, which are observation maps from the system state to a scalar. An index whose fibres cross a floor boundary cannot support exact floor certification; the certainly-safe set is the honest domain of an index-based verdict. Where separately-binding floors matter, per-floor observation is the only observation structure that admits exact certification — a formal complement to the thesis, argued verbally since Martinez-Alier, Munda, and O'Neill (1998), that weakly comparable values cannot be fused into one metric without loss.

**Bias.** Remark 1 shows that the loss need not be in the measurement: a biased indicator with an uncorrected certainty-equivalence policy empties a nonempty perfect-information kernel. Monitoring therefore has two obligations — bounding the observation error and supplying the correction — and the second is the one governance structures most often omit: the indicator is published, the correction is not applied, and the kernel empties although the information was sufficient.

**Institutions.** The hierarchy of Section 2.1 records that epistemic contraction is one of three causes of kernel shrinkage, the others being disturbances and institutional restriction (authority, enforcement, allocation). The epistemic-institutional kernel $\mathrm{IRViab}_{\mathfrak{I}}$ combines them: an institution restricted in what it may observe *and* in what it may command inherits both contractions. The obstruction calculus characterizes the first; its certificates remain valid — and typically tighten — when the institution's command set is further restricted, since restriction of the action correspondence can only empty kernels, never create them (one-sided monotonicity of viability under correspondence restriction).

### 6.5 Limitations

(i) The certificates are sufficient conditions for nonviability, not necessary-and-sufficient characterizations of the epistemic kernel; the middle ground (neither a Veliov-type condition nor an obstruction certificate) is open. (ii) The information-set semantics is set-membership; probabilistic or belief-space formulations require separate statements, although the common-action obstruction transfers mutatis mutandis to any semantics in which the policy must choose a single action per information state. (iii) The results are finite-dimensional and time-invariant; the delay-free setting makes the timing bound of Theorem 4 sharp, and delay systems require the retarded extension of the Dini comparison argument (Hale and Verduyn Lunel, 1993). (iv) Theorem 1's measurable-selection step presupposes the closed-graph regularity of Section 2.1; without it the certificate remains a heuristic. (v) The institutional consequences of Section 6.4 are design conclusions from the certificates, not empirical findings; their empirical testing belongs to applied studies.

---

## 7. Conclusion

Viability under perfect measurement has a complete theory and a mature numerical practice. Viability under incomplete observation has, until now, had half a theory: the sufficiency half, from Veliov's output-feedback condition and the estimation-tube programme. This paper has supplied the necessity half. The obstruction calculus certifies — with displayed proofs and explicit witnesses — four ways in which an observation structure can make robust viability impossible: the disturbance can enforce exit in finite time against every control; the compatible states can demand incompatible actions at a single information state; the information can arrive after the enforced exit; and the observation fibres can cross the safe-set boundary, defeating every exact certifier. A fifth mechanism empties the kernel through the policy class alone, under an injective observation. Each certificate identifies the design change that removes it: a faster indicator, a separating observation, per-floor instead of aggregate certification, or the correction of a known bias. For sustainability governance, where observation is conducted through coarse indicators at discrete reviews, the calculus states the quantitative limits of what monitoring can deliver — and converts each impossibility into a design specification.

---

## Declarations

**Funding.** None declared. **Competing interests.** None. **Data availability.** No data were used; all constructions are symbolic. **Code availability.** Verification code for the worked examples is available from the authors on request.

---

## Appendix A: Bounded Constructions and Scope Remarks

The following bounded constructions complement the obstruction theorems of Sections 3–4. They are stated in full because each carries a scope remark that is itself part of the contribution; none of them is promoted to a theorem of the main text.

**A.1 Example (coupling creates viability absent in a factor).** Take $g_i(s) = s(1-s)$, $d = 0.2$. Choose $(S_1^*, S_2^*) = (0.5, 0.8)$. Define harvest floors by the equilibrium equations: $H_{\min,1} = g_1(0.5) + 0.2(0.8 - 0.5) = 0.31$; $H_{\min,2} = g_2(0.8) + 0.2(0.5 - 0.8) = 0.10$. Patch 1 in isolation: $\max_s g_1(s) = 0.25 < H_{\min,1} = 0.31$, so patch 1 is not viable in isolation. Yet the coupled system has the equilibrium $(0.5, 0.8)$, so its kernel is nonempty, provided sink and harvest-capacity constraints hold. The example is the constructive counterpart of the emptiness results of Section 3: where the obstruction theorems certify that no policy works for reasons of information, patch coupling exhibits the opposite direction — a jointly viable operating point that no factor sustains alone.

**A.2 Counterexample (emptiness despite factorwise viability at MSY).** Take $d > 0$, $C_1 \ne C_2$, $H_{\min,i} = r_i C_i / 4$ (MSY level). Each isolated system has kernel $[C_i/2, \infty) \times [0, K_{\max,i}]$. At MSY: $\phi_i(S_i) = -\frac{r_i}{C_i}(S_i - C_i/2)^2 \le 0$ with equality only at $S_i = C_i/2$. Adding the equilibrium equations requires $\phi_1 + \phi_2 = 0$, so both must vanish: $S_i = C_i/2$. Substituting into the first equation: $d(C_2/2 - C_1/2) = 0$, requiring $C_1 = C_2$. For $C_1 \ne C_2$: no equilibrium, empty kernel. The counterexample is specific to the MSY parameter choice; for $H_{\min,i} < r_i C_i / 4$, equilibria may exist. Together with A.1 it delimits what coupling can and cannot repair: factorwise nonviability is repairable (A.1), but factorwise viability at an incompatible operating point is not (A.2).

## References

Aubin, J.-P.: Viability Theory. Birkhäuser, Boston (1991)

Aubin, J.-P., Bayen, A.M., Saint-Pierre, P.: Viability Theory: New Directions, 2nd edn. Birkhäuser, Boston (2011)

Aubin, J.-P., Frankowska, H.: Set-Valued Analysis. Birkhäuser, Boston (1990)

Béné, C., Doyen, L., Gabay, D.: A viability analysis for a bio-economic model. Ecol. Econ. **36**, 385–396 (2001)

Cardaliaguet, P., Quincampoix, M., Saint-Pierre, P.: Differential games through viability theory: old and recent results. In: Jørgensen, S., Quincampoix, M., Vincent, T.L. (eds.) Advances in Dynamic Game Theory. Annals of the International Society of Dynamic Games, vol. 9, pp. 3–35. Birkhäuser, Boston (2007)

De Lara, M., Doyen, L.: Sustainable Management of Natural Resources: Mathematical Models and Methods. Springer, Berlin (2008)

Doyen, L., Gajardo, P.: Sustainability standards, multicriteria maximin, and viability. Nat. Resour. Model. **33**(3), e12250 (2020)

Doyen, L., Thébaud, O., Béné, C., Martinet, V., Gourguet, S., Bertignac, M., Fifas, S., Blanchard, F.: A stochastic viability approach to ecosystem-based fisheries management. Ecol. Econ. **75**, 32–42 (2012)

Farkas, J.: Theorie der einfachen Ungleichungen. J. Reine Angew. Math. **124**, 1–27 (1902)

Frankowska, H.: Optimal trajectories associated with a solution of contingent Hamilton–Jacobi equations. Appl. Math. Optim. **19**, 291–311 (1989)

Gale, D.: The Theory of Linear Economic Models. McGraw-Hill, New York (1960)

Haddad, G.: Monotone viable trajectories for functional-differential inclusions. J. Differ. Equ. **42**, 1–24 (1981)

Hale, J.K., Verduyn Lunel, S.M.: Introduction to Functional Differential Equations. Springer, New York (1993)

Maghenem, M., Sanfelice, R.G.: Characterizations of safety in hybrid inclusions via barrier functions. In: Proceedings of the 22nd ACM International Conference on Hybrid Systems: Computation and Control (HSCC), pp. 109–118 (2019)

Martinez-Alier, J., Munda, G., O'Neill, J.: Weak comparability of values as a foundation for ecological economics. Ecol. Econ. **26**(3), 277–286 (1998)

Prajna, S., Jadbabaie, A.: Safety verification of hybrid systems using barrier certificates. In: Alur, R., Pappas, G.J. (eds.) Hybrid Systems: Computation and Control (HSCC 2004). LNCS, vol. 2993, pp. 477–492. Springer, Berlin (2004)

Prajna, S., Jadbabaie, A., Pappas, G.J.: A framework for worst-case and stochastic safety verification using barrier certificates. IEEE Trans. Autom. Control **52**(8), 1415–1428 (2007)

Prajna, S., Rantzer, A.: On the necessity of barrier certificates. IFAC Proc. Vol. **38**(1), 526–531 (2005)

Quincampoix, M., Veliov, V.M.: Viability with a target: theory and applications. In: Control Theory, Multivariate Analysis and Applications, pp. 47–63. Springer (1994)

Saint-Pierre, P.: Approximation of the viability kernel. Appl. Math. Optim. **29**, 187–209 (1994)

Veliov, V.M.: Sufficient conditions for viability under imperfect measurement. Set-Valued Anal. **1**, 305–317 (1993)

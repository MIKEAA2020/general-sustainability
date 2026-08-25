# Class 2 and Class 3 — remaining elevations

**This file is not a repository edit.** It elevates every remaining
row of `batch 4/PROOF_REAUDIT.md` Classes 2 and 3. Each section is one
theorem, proved in place. Class 1 and E2.B2(a) already live in their
own files and are not repeated.

Already delivered, not re-treated:

| file | row |
|---|---|
| `A3_Thm1_corrected_compactness.md` | A3.Thm1 |
| `B6_Thm1_strict_substitution_stability.md` | B6.Thm1(1) |
| `E4_Thm2_budget_solvability.md` | E4.Thm2 budget |
| `E4_Lem1_jump_margin_nonvacuity.md` | E4.Lem1(ii) |
| `E2_B2a_measurable_selection.md` | E2.B2(a) |

Standing rule, kept: do not regress a claim unless it is false; demote
to conjecture only if plausible and out of reach; punish inflation as
well as softening.

---

# Class 2 — proof gaps

---

## I. E2.B1(a) — post-fixed inheritance

**Source.** `batch 2/02_elevation/E2_SELECTORS_AND_CERTIFICATES.md`,
B1.Theorem (a). **Reaudit.** Finding 6.

### 0. What is true, and what is backwards

Let \(\mathcal K(X)\) be the complete lattice of closed subsets of
compact metric \(X\), ordered by inclusion. Let
\(\Gamma:\mathcal K(X)\to\mathcal K(X)\) be monotone. Knaster–Tarski
gives a greatest fixed point

\[
\mathcal V^\ast
\;=\;
\bigvee\{\,C\in\mathcal K(X):C\subseteq\Gamma(C)\,\}
\;=\;
\max\{\,C:\Gamma(C)=C\,\}.
\]

That core is correct (and was re-derived in the reaudit). The last
sentence of the recorded proof is not:

> R02.Thm1 applies to any subfamily \((C,c)\) with \(C\subseteq\mathcal V^\ast\),
> which is consistent because consistency is inherited by subfamilies
> (monotonicity).

Monotonicity yields, for \(C\subseteq\mathcal V^\ast=\Gamma(\mathcal V^\ast)\),

\[
\Gamma(C)\;\subseteq\;\Gamma(\mathcal V^\ast)\;=\;\mathcal V^\ast.
\]

That is the **wrong direction** for post-fixedness. Post-fixedness is
\(C\subseteq\Gamma(C)\). It is not inherited downward.

**Witness.** Discrete \(X=\{0,1,2\}\). Define \(\Gamma\) on subsets by

\[
\begin{align*}
\Gamma(\emptyset)&=\emptyset,&
\Gamma(\{0\})&=\emptyset,&
\Gamma(\{1\})&=\emptyset,&
\Gamma(\{2\})&=\{2\},\\
\Gamma(\{0,1\})&=\emptyset,&
\Gamma(\{0,2\})&=\{2\},&
\Gamma(\{1,2\})&=\{1,2\},&
\Gamma(X)&=\{1,2\}.
\end{align*}
\]

Monotone (check every inclusion). Fixed points: \(\emptyset\),
\(\{2\}\), \(\{1,2\}\). Greatest: \(\mathcal V^\ast=\{1,2\}\). The
subset \(C=\{1\}\subseteq\mathcal V^\ast\) has \(\Gamma(C)=\emptyset\),
so \(C\not\subseteq\Gamma(C)\). A state set inside the maximal
certificate set need not itself be a consistent certificate set.

### 1. What R02 actually transfers

R02.Thm1 consumes a **family** \(\mathcal V\) on which (REG) holds at
every member, and which is downward closed in the set argument
(R02 Field 3, item 7): \((C,c)\in\mathcal V\) and
\(\emptyset\neq C'\subseteq C\) closed imply \((C',c)\in\mathcal V\).
That downward closure is extra structure, not a consequence of
monotonicity of \(\Gamma\).

**Lemma I.1 (downward transfer of (REG)).** Suppose \(\mathcal V\) is
downward closed in \(C\), and \((C,c)\) satisfies (REG) with witness
\(u^{\mathrm{cmd}}\) and realized-action set
\(\widetilde U=\mathsf I(u^{\mathrm{cmd}},c,C)\). Then every
\((C',c)\) with \(\emptyset\neq C'\subseteq C\) closed satisfies
(REG) with the **same** witness, provided the implementation map is
monotone in the set argument in the sense
\(\mathsf I(u^{\mathrm{cmd}},c,C')\subseteq\widetilde U\)
(or is independent of \(C\), the usual case).

*Proof.* Tube clause: every \(x\in C'\) is in \(C\), so every branch
from \(x\) under any \(u\in\widetilde U\) stays in \(K\). If the
implementation at \(C'\) is a subset of \(\widetilde U\), the same
holds for it. Successor clause: \(\Phi(C',\widetilde U')\subseteq
\Phi(C,\widetilde U)\). For every observation \(Y'\) with
\(\Phi(C',\widetilde U')\cap O^{-1}(Y')\neq\emptyset\), the large
intersection is nonempty as well, hence lies in \(\mathcal V\) by
(REG) at \((C,c)\). Downward closure puts the small intersection in
\(\mathcal V\). ∎

This is the inheritance the recorded sentence was reaching for. It
uses R02's downward-closed hypothesis, not \((P1)\) of \(\Gamma\).

### 2. Corrected theorem

**E2.B1(a)\(^\ast\).** Let \(\Gamma:\mathcal K(X)\to\mathcal K(X)\) be
monotone.

1. \(\Gamma\) has a nonempty complete lattice of fixed points. The
   greatest is \(\mathcal V^\ast=\bigvee\{C:C\subseteq\Gamma(C)\}\).
2. Every post-fixed point sits under the gfp:
   \(C\subseteq\Gamma(C)\) implies \(C\subseteq\mathcal V^\ast\).
3. An arbitrary closed \(C\subseteq\mathcal V^\ast\) need **not** be
   post-fixed (witness above). R02.Thm1 does **not** apply to the
   family \(\{(C,c):C\subseteq\mathcal V^\ast\}\) on monotonicity of
   \(\Gamma\) alone.
4. R02.Thm1 applies to \(\{(\mathcal V^\ast,c)\}\) as soon as (REG)
   holds at \(\mathcal V^\ast\). It applies to every
   \((C,c)\) with \(C\subseteq\mathcal V^\ast\) **if** the ambient
   family is downward closed and (REG) holds at \((\mathcal V^\ast,c)\)
   (Lemma I.1). Those are R02's hypotheses, not E2.B1(a)'s.

E2.B1(b) (backward iteration equals the gfp under closed Vietoris
graph) is untouched and was verified.

### 3. Status

Recorded inheritance sentence: **false**. Knaster–Tarski core:
**true**. Closed-loop transfer: **true** on a downward-closed (REG)
family, **not** on every sublevel of \(\mathcal V^\ast\).

---

## II. E3.C6.3 — delayed revelation

**Source.** `batch 2/02_elevation/E3_CLASSIFICATION_THEOREMS.md`,
C6.3. **Reaudit.** Finding 7.

### 0. The recorded iff is false

**Recorded.** Delayed information is inert
(\(K_{\mathrm{del}}=K_{\mathrm{full}}\)) iff no trajectory from the
kernel hits \(X\setminus K\) before \(t_d\) under **any**
prior-admissible policy.

The “any policy” buffer is far stronger than inertness: a single
stupid prior-admissible control that drives a kernel state out of
\(K\) before \(t_d\) is generic, and does not make the kernels differ.
Its negation therefore does not prove \(K_{\mathrm{del}}\subsetneq
K_{\mathrm{full}}\). The recorded \((\Longrightarrow)\) cites
R02.Prop3 as if a witness were a general argument. It is not.

The recorded \((\Longleftarrow)\) has the inclusions written
backwards in the parenthetical (“\(\supseteq\) is trivial”). Under
C6.1, more information cannot shrink the kernel:
\(K_{\mathrm{del}}\subseteq K_{\mathrm{full}}\). The nontrivial
direction is the other inclusion.

### 1. Objects

Let \(\mathbb F^{\mathrm{full}}\) be the full-information filtration
and \(\mathbb F^{\mathrm{del}}\) the delayed one (prior only on
\([0,t_d)\), full after). Let \(K_{\mathrm{full}}\) and
\(K_{\mathrm{del}}\) be the corresponding robust viability kernels
on a common compact horizon, same \(K\), same non-strategic
implementation. Assume C6.1's typed-lift hypotheses, so refinement
is monotone.

### 2. Corrected theorem

**E3.C6.3\(^\ast\) (delayed revelation).**

**(A) Monotonicity.** \(K_{\mathrm{del}}\subseteq K_{\mathrm{full}}\).

**(B) Sufficiency (landing buffer).** Suppose there exists an
\(\mathbb F^{\mathrm{del}}\)-adapted policy \(\pi_0\) such that every
trajectory starting in \(K_{\mathrm{full}}\) under \(\pi_0\) satisfies
\(x(t)\in K\) for all \(t\in[0,t_d]\) and \(x(t_d)\in K_{\mathrm{full}}\).
Then \(K_{\mathrm{del}}=K_{\mathrm{full}}\).

**(C) Necessity of a landing policy.** If
\(K_{\mathrm{del}}=K_{\mathrm{full}}\), then for every
\(x\in K_{\mathrm{full}}\) there exists an
\(\mathbb F^{\mathrm{del}}\)-adapted policy keeping \(x([0,t_d])\subset K\)
and \(x(t_d)\in K_{\mathrm{full}}\).

**(D) Recorded “any-policy” buffer.** If *every* prior-admissible
policy keeps every kernel trajectory in \(K\) on \([0,t_d)\), then
(B) holds (play any safe prior policy, then a full-info selector).
This is sufficient and strictly stronger than (B). Its negation does
**not** imply \(K_{\mathrm{del}}\neq K_{\mathrm{full}}\).

**(E) Sharpness, not \((\Longrightarrow)\).** R02.Prop3 is a system in
which the *relevant* buffer fails (common-action obstruction reached
at \(t=2\) under forced safe play of the conservative filter) and
\(K_{\mathrm{del}}\subsetneq K_{\mathrm{full}}\) (conservative
nonviable by \(t=3\); exact viable forever). It is a witness that
inertness can fail, not a proof that every failure of the recorded
buffer produces unequal kernels.

### 3. Proof

**(A)** A delayed-adapted policy is full-adapted. Any state viable
under the smaller policy class is viable under the larger. ∎

**(B)** Take \(x\in K_{\mathrm{full}}\). Run \(\pi_0\) on
\([0,t_d)\). By hypothesis the path stays in \(K\) and lands in
\(K_{\mathrm{full}}\). From \(t_d\) on, play a measurable full-info
selector on \(K_{\mathrm{full}}\) (E2.B2(a)\(^\ast\), applied to the
safe-action map of the full-information successor). The concatenation
is \(\mathbb F^{\mathrm{del}}\)-adapted, and the trajectory stays in
\(K\). Thus \(x\in K_{\mathrm{del}}\). With (A), equality. ∎

**(C)** If \(x\in K_{\mathrm{full}}=K_{\mathrm{del}}\), a witnessing
delayed policy exists. Its restriction to \([0,t_d)\) is the required
landing policy: the path stays in \(K\), and \(x(t_d)\) must lie in
\(K_{\mathrm{full}}\) or the tail could not be completed under full
information. ∎

**(D)** Immediate from (B). For the negation: a prior-admissible
policy that exits does not constrain the *existential* kernel. ∎

**(E)** Recorded, not re-proved. The plant, the two observation maps,
and the sum decay \(z^++z^-=6-2k\) are R02 Field 8. ∎

The recorded iff is not a conjecture. The “any-policy” reading is
false. The correct characterisation is (B) and (C).

---

## III. B1.Thm1 — sampled-data erosion depth

**Source.** `batch 2/04_open_problems/B_TIER_BRIDGES.md`, B1.
**Reaudit.** Finding 8.

### 0. What the hypotheses deliver

Hypotheses: (1) inter-sample envelope \(x(t)\in\overline B(x_k,\rho)\);
(2) \(V_{\max}T_s\le r/2\); (3) sampled successor carries
\(K_{-r/2}\) into \(K_{-r/2}\).

The induction in the recorded proof starts at \(x_0\in K_{-r/2}\),
keeps \(x_k\in K_{-r/2}\), and uses \(\|x(t)-x_k\|\le r/2\) to get
\(x(t)\in K\). That is all. The closing sentence —

> replacing \(K\) by \(K_{-r}\) throughout yields the \(r\)-eroded
> statement verbatim

— requires a successor certificate at depth \(3r/2\), which is not
supplied. The recorded conclusion is stronger than the hypotheses.

### 1. Corrected theorem

**B1.Thm1\(^\ast\).** Under (1)–(3), with (1) implied by (2) on
compacts:

**(A) Sample invariance.** \(K_{-r/2}\) is forward invariant at
sample times: \(x_0\in K_{-r/2}\) implies \(x_k\in K_{-r/2}\) for all
\(k\).

**(B) Intersample confinement to \(K\).** For every
\(t\in[t_k,t_{k+1})\), \(\|x(t)-x_k\|\le V_{\max}T_s\le r/2\), hence
\(\operatorname{dist}(x(t),X\setminus K)\ge r/2-r/2=0\), i.e.
\(x(t)\in K\).

**(C) Safe initials.** Every trajectory with \(x_0\in K_{-r/2}\)
(in particular \(x_0\in K_{-r}\)) stays in \(K\) on the finite
horizon. This is R02.Cor6's *true-state safety in \(K\)*, at the
declared half-depth certificate.

**(D) Verbatim replacement needs one more half-depth.** If (3) is
strengthened to “the sampled successor carries \(K_{-3r/2}\) into
\(K_{-3r/2}\)” and \(x_0\in K_{-3r/2}\), then \(x_k\in K_{-3r/2}\)
and \(x(t)\in K_{-r}\) between samples. That is the statement
obtained by replacing the constraint \(K\) by \(K_{-r}\) in (A)–(B).
It is not a corollary of the recorded (3).

### 2. Proof

**(A)** Induction. Base \(x_0\in K_{-r/2}\). Step: hypothesis (3). ∎

**(B)** Triangle inequality for the distance to \(X\setminus K\):
\(\operatorname{dist}(x(t),X\setminus K)
\ge\operatorname{dist}(x_k,X\setminus K)-\|x(t)-x_k\|
\ge r/2-r/2=0\). ∎

**(C)** Concatenate (A) and (B) over finitely many samples. ∎

**(D)** Repeat (A)–(B) with \(r\) replaced by \(2r\) on the set
\(K_{-r}\), which is \((K_{-r})_{-r/2}=K_{-3r/2}\) at sample times
and \(K_{-r}\) between samples. ∎

No part of R02.Cor6's bridge is lost: the bridge asked for true-state
safety in \(K\) from an eroded initial condition. That is (C). The
verbatim-replacement sentence is dropped, not weakened into a
conjecture.

---

## IV. B9.Thm1(1) — chance-kernel recursion

**Source.** `B_TIER_BRIDGES.md`, B9 part (1). **Reaudit.** Finding 9.
Parts (2) and (3) are not re-treated. The Fatou closedness step was
verified and is kept.

### 0. Two different inclusions

The recorded recursion uses a **quantile-set** inclusion
\(Q_{p_k}(x';\mathcal L)\subseteq W_k\). The kernel \(K_p\) is a
**scalar** chance set
\(\{x_0:\exists\pi,\;\mathbb P(\text{safety on }[0,T])\ge p\}\).
Set inclusion implies the scalar bound, so the forward inclusion
survives. The reverse — “a policy with \(\mathbb P\ge p\) induces
quantiles that satisfy the budget split *somehow*” — is the content,
and is not given. It is false for a uniform product split, even
scalar.

### 1. Product-split incompleteness

**Witness.** Two reviews. From \(x\), one action sends the state to
\(y_1\) or \(y_2\) with probability \(1/2\) each. From \(y_1\),
terminal safety has probability \(0.2\); from \(y_2\), \(0.8\). Then

\[
\mathbb P(\text{survive both})
\;=\;
\tfrac12\cdot 0.2+\tfrac12\cdot 0.8
\;=\;
0.5,
\]

so \(x\in K_{1/2}\). For any split \(p_0 p_1=1/2\):

- if \(p_0\le 0.2\), then \(W_1\supset\{y_1,y_2\}\), hence
  \(\mathbb P(X'\in W_1)=1\), but \(p_1=1/(2p_0)\ge 2.5>1\);
- if \(0.2<p_0\le 0.8\), then \(W_1=\{y_2\}\),
  \(\mathbb P(X'\in W_1)=1/2\), and \(1/2\ge 1/(2p_0)\) forces
  \(p_0\ge 1\), a contradiction;
- if \(p_0>0.8\), then \(W_1=\emptyset\).

So \(x\) lies in no product-split \(W_2\). The recorded reverse
inclusion is false of the scalar product recursion, and a fortiori
of the set-valued one.

### 2. Corrected theorem

Let reviews be \(k=0,\ldots,N\), \(X\) compact metric, \(K\) closed,
controls compact, successor laws weakly measurable in \((x,u)\).

**B9.Thm1(1)\(^\ast\).**

**(A) Soundness of any product split.** Fix \(p_0,\ldots,p_{N-1}\) in
\((0,1]\) with \(\prod p_k=p\). Let \(W_0=K\) and

\[
W_{k+1}
=\bigl\{x:\exists u,\;
\mathbb P(X'\in W_k\mid x,u)\ge p_k\bigr\}
\]

(the scalar recursion), or the stronger set-valued recursion with
\(Q_{p_k}\subseteq W_k\). Then \(\bigcap_k W_k\subseteq K_p\),
provided a measurable selector of the witnessing actions exists
(E2.B2(a)\(^\ast\)).

**(B) Incompleteness.** The inclusion in (A) may be strict. The
witness of §1 lies in \(K_{1/2}\) and in no product-split \(W\).

**(C) Complete residual-budget DP.** Define \(V_N(x,q)=1\) iff
\(q\le 0\) or (\(x\in K\) and \(q\le 1\)), and \(V_N(x,q)=0\)
otherwise. Backward:

\[
V_k(x,q)=1
\;\iff\;
x\in K
\text{ and }
\exists u,\;
\exists\text{ measurable }r:X\to[0,1]
\text{ with }
\mathbb E[r(X')\mid x,u]\ge q
\text{ and }
V_{k+1}(y,r(y))=1
\text{ for \(r_{\#}\mathcal L(\,\cdot\mid x,u)\)-a.e. }y.
\]

Then \(x\in K_p\) if and only if \(V_0(x,p)=1\).

**(D) The \(p=1\) reduction.** Under support alignment
\(\operatorname{supp}\mathcal L(\,\cdot\mid x,u)=D(x,u)\), the case
\(p=1\) of (C) is the robust predecessor
\(\{x:\exists u,\; D(x,u)\subseteq K\}\), and is complete.

**(E) Closedness of \(K_p\).** Unchanged: compact policy class,
pointwise convergence, closed \(K\), reverse Fatou on
\(1_{\mathrm{survive}}\).

### 3. Proof of (A)

If \(x\in W_N\), a measurable policy exists so that
\(\mathbb P(X_1\in W_{N-1}\mid X_0)\ge p_{N-1}\). On
\(\{X_1\in W_{N-1}\}\) the same holds one step on. The tower

\[
\mathbb P(X_1\in W_{N-1},\,X_2\in W_{N-2})
=\mathbb E\bigl[1_{X_1\in W_{N-1}}
\mathbb P(X_2\in W_{N-2}\mid X_1)\bigr]
\ge p_{N-2}\,p_{N-1}
\]

iterates to \(\mathbb P(\text{all memberships})\ge\prod p_k=p\).
Set-valued hypotheses imply the scalar ones. ∎

### 4. Proof of (C)

*Forward.* If \(V_k(x,q)=1\), choose \(u\) and \(r\). Then

\[
\mathbb P(\text{survive from }k\mid x)
=\mathbb E\bigl[\mathbb P(\text{survive from }k+1\mid X')\bigr]
\ge\mathbb E[r(X')]\ge q,
\]

using the inductive identification of \(V_{k+1}(y,r(y))\) with
tail-survival probability at least \(r(y)\).

*Reverse.* If a measurable policy realises
\(\mathbb P(\text{survive from }k\mid x)\ge q\), set
\(r(y)=\mathbb P(\text{survive from }k+1\mid X'=y)\). Then
\(\mathbb E[r]\ge q\) and \(V_{k+1}(y,r(y))=1\) a.e. by induction.
The terminal step is the indicator of \(K\). ∎

The ambition — a chance-kernel calculus — is met by (C), which the
recorded product split is not. The product split remains a sound
inner bound and a cheap certificate when it closes. It is not the
kernel.

---

## V. B10.Thm1 — Stackelberg: pessimistic existence, not coincidence

**Source.** `B_TIER_BRIDGES.md`, B10. **Reaudit.** Findings 10 and 11.
CIRC-3 is scope, not repaired here: strategic \(\mathsf I\) stays
outside the typed judgment family. This section is the mathematical
content of the recorded “foundational” theorem only.

### 0. Two false sentences

**Coincidence.** The proof produces a maximiser of the *pessimistic*
objective \(\psi(c)=\min_{\pi\in\mathrm{BR}(c)}v_l(c,\pi)\). It does
not produce
\(v_l(c^\ast,\pi^\ast)=\max_c\min_{\pi\in\mathrm{BR}(c)}v_l(c,\pi)\)
unless \(\pi^\ast\) attains the inner min, and it does not equate
optimistic and pessimistic values.

**Witness (coincidence fails).** Let \(\Pi=\{a,b\}\),
\(v_f\equiv 0\), \(v_l(c,a)=0\), \(v_l(c,b)=1\). Then
\(\mathrm{BR}(c)=\Pi\) for every \(c\),
\(\psi\equiv 0\), \(\varphi(c)=\max_{\mathrm{BR}}v_l\equiv 1\).
Both maps are continuous. Optimistic value \(1\), pessimistic value
\(0\).

**Closed-graph inheritance.** Berge gives usc compact-valued
\(\mathrm{BR}\), hence closed graph of \(\mathrm{BR}\). It does not
make \(\{c:\mathrm{BR}(c)\subseteq F\}\) closed for closed \(F\).

**Witness (reaudit, reproduced).** \(v_f(c,a)=0\),
\(v_f(c,b)=-|c|\). Then \(\mathrm{BR}(c)=\{a\}\) for \(c\neq 0\) and
\(\mathrm{BR}(0)=\{a,b\}\). For \(F=\{a\}\),

\[
\{c:\mathrm{BR}(c)\subseteq\{a\}\}
=\mathbb R\setminus\{0\},
\]

not closed. The existential set
\(\{c:\mathrm{BR}(c)\cap\{b\}\neq\emptyset\}=\{0\}\) *is* closed.

The recorded (2) writes the universal set
\(\{c:\mathrm{BR}(c)\subseteq W\text{-successors}\}\) and claims
E2's Step 2. E2 had Hausdorff continuity of \(\operatorname{Succ}\)
(both directions). Berge is only upper.

The *words* of recorded (2) ask an existential question: “a command
after which **some** follower response keeps the system viable.”
That is the set that is closed.

### 1. Semicontinuity, and why the recorded max fails

Berge gives upper hemicontinuity of the *argmax*, and upper
semicontinuity of the *maximum*. The pessimistic objective is a
minimum:

\[
\psi
\;=\;
-\max_{\mathrm{BR}}(-v_l).
\]

So \(\psi\) is **lower** semicontinuous, not upper. An lsc function
on a compact set attains its minimum. It need not attain a maximum.

**Witness (\(\sup\psi\) not attained).** \(C=[0,1]\),
\(\Pi=\{a,b\}\), \(\mathrm{BR}(c)=\{a\}\) for \(c<1\),
\(\mathrm{BR}(1)=\{a,b\}\), \(v_l(c,a)=c\), \(v_l(1,b)=0\). Then
\(\mathrm{BR}\) is usc (values jump up at \(1\)): if \(c_n\to 1^-\),
\(\mathrm{BR}(c_n)=\{a\}\subseteq\mathrm{BR}(1)\). And
\(\psi(c)=c\) for \(c<1\), \(\psi(1)=\min(1,0)=0\). So
\(\sup\psi=1\) is not attained.

The recorded “\(\psi\) is usc, hence attains its max” is false, and
false in the direction that flatters existence. This is strictly
worse than Finding 10.

Honest existence is therefore:

- Optimistic \(\varphi=\max_{\mathrm{BR}}v_l\) is usc and attains
  its maximum.
- Pessimistic \(\psi\) is lsc and attains its minimum.
- A pessimistic Stackelberg *equilibrium* (a maximiser of \(\psi\))
  needs an extra hypothesis that restores upper semicontinuity of
  \(\psi\): lower hemicontinuity of \(\mathrm{BR}\) (then Berge both
  ways, \(\psi\) continuous), or single-valued \(\mathrm{BR}\), or
  \(v_l\) constant on fibres.

### 2. Corrected theorem

Assume \(C,\Pi\) compact metric, \(v_f,v_l\) continuous.

**B10.Thm1\(^\ast\).**

**(A) Berge.** \(\mathrm{BR}\) is nonempty, compact-valued, and
upper hemicontinuous (closed graph). The follower value
\(\bar v_f(c)=\max_\pi v_f(c,\pi)\) is continuous.

**(B) Semicontinuity.** \(\varphi=\max_{\mathrm{BR}}v_l\) is usc and
attains its maximum on \(C\) (optimistic existence).
\(\psi=\min_{\mathrm{BR}}v_l\) is lsc and attains its minimum.
\(\psi\) need **not** attain a maximum (witness of §1).

**(C) Pessimistic existence under an extra hypothesis.** If
\(\mathrm{BR}\) is lower hemicontinuous, or single-valued, or
\(v_l(c,\cdot)\) is constant on \(\mathrm{BR}(c)\), then \(\psi\) is
usc (in the last two cases \(\psi=\varphi\), or \(\psi\) is
continuous along the unique selection), and a pessimistic
Stackelberg pair exists. Coincidence of optimistic and pessimistic
*values* is exactly the third of these, or single-valuedness.

**(D) Existential reduction (the recorded question).** For
\(F\subseteq\Pi\) closed, \(\{c:\mathrm{BR}(c)\cap F\neq\emptyset\}\)
is closed. Writing \(F_W\) for the closed set of follower policies
that keep a declared closed \(W\) invariant, the set of leader
commands for which **some** best response is \(W\)-safe is closed.
Measurable selection of such a command is E2.B2(a)\(^\ast\).

**(E) Universal reduction (not Berge).**
\(\{c:\mathrm{BR}(c)\subseteq F\}\) is closed for every closed \(F\)
if and only if \(\mathrm{BR}\) is lower hemicontinuous, or is
single-valued. The recorded “closed-graph inheritance” of the
universal set is **false**.

### 3. Proof of (A)–(B)

**(A)** Berge's maximum theorem. Closed graph of \(\mathrm{BR}\):
if \(\pi_n\in\mathrm{BR}(c_n)\) and \((c_n,\pi_n)\to(c,\pi)\), then
for any \(\pi'\) one has
\(v_f(c,\pi)=\lim v_f(c_n,\pi_n)\ge\lim v_f(c_n,\pi')=v_f(c,\pi')\).

**(B)** \(\varphi(c)=\max_{\pi\in\mathrm{BR}(c)}v_l(c,\pi)\):
\(v_l\) continuous, \(\mathrm{BR}\) usc compact-valued
\(\Rightarrow\) \(\varphi\) usc (Aliprantis–Border 17.30). An usc
function on compact \(C\) attains its max.
\(\psi=-\max(-v_l)\): the same theorem applied to \(-v_l\) makes
\(\max(-v_l)\) usc, hence \(\psi\) lsc. Lsc on compact attains its
min. The non-attainment witness is §1: \(\mathrm{BR}\) is usc
(values jump *up* at \(1\)), \(\psi\) jumps *down* at \(1\). ∎

### 4. Proof of (D)

If \(c_n\to c\) and \(\pi_n\in\mathrm{BR}(c_n)\cap F\), compactness
gives \(\pi_{n_k}\to\pi\in F\); closed graph of BR gives
\(\pi\in\mathrm{BR}(c)\). So the existential set is closed. Apply
E2.B2(a)\(^\ast\) to the correspondence
\(c\mapsto\mathrm{BR}(c)\cap F_W\) on that closed (hence measurable)
domain. ∎

### 5. Status

| Recorded claim | Disposition |
|---|---|
| BR closed graph / usc | **True** (Berge). |
| \(\psi\) usc, attains its max | **False.** \(\psi\) is lsc. Max need not be attained. |
| Optimistic = pessimistic | **False** without extra hyp (constant-on-fibre witness). |
| \(v_l(c^\ast,\pi^\ast)=\max\min\) for arbitrary \(\pi^\ast\in\mathrm{BR}(c^\ast)\) | **False.** |
| Universal set \(\{\mathrm{BR}\subseteq F\}\) closed | **False** (reaudit witness). |
| Existential set \(\{\mathrm{BR}\cap F\neq\emptyset\}\) closed | **True.** This is the recorded *question*. |
| “All R02/E2 theorems transfer with \(U:=C\)” | **Inflation.** Only the existential reduction is licensed. |

The foundational ambition — a Stackelberg pair the leader can count
on, and a reduction of “some safe follower response” to E2 — survives
as (C) plus (D), not as the recorded paragraph.

---

## VI. C-a.Thm3 — definable, not arbitrary, subsets

**Source.** `batch 2/04_open_problems/CA_EXECUTION.md`, C-a.Thm3.
**Reaudit.** Finding 12. C-a.Thm2's complexity convention is folded
in at the end of this section (Finding 20).

### 0. The language does not read successor tables

The eight atomic families are kernel-membership claims
(\(x\in\mathrm{Viab}\), \(x\in\mathrm{RViab}\), …). Two successor
tables that induce the same eight kernels at every grid point are
**language-indistinguishable**.

**Witness (reaudit, written out).** \(X_h=\{a,b\}\), \(K=\{a,b\}\),
\(U=D=\{\ast\}\).

- Table \(M_1\): \(\operatorname{Succ}(a)=\{\,b\,\}\),
  \(\operatorname{Succ}(b)=\{\,b\,\}\).
- Table \(M_2\): \(\operatorname{Succ}(a)=\{\,a,b\,\}\),
  \(\operatorname{Succ}(b)=\{\,b\,\}\).

In both cases the only subset of \(K\) that is a one-step predecessor
of itself is \(\{a,b\}\): from \(a\), \(M_1\) goes to \(b\in K\) and
\(M_2\) goes into \(K\); from \(b\), both stay at \(b\). So
\(\mathrm{Viab}(M_1)=\mathrm{Viab}(M_2)=\{a,b\}\). The same identity
holds for fixed-policy safety (one control), for robust viability
(one disturbance), and for the remaining six families on this
two-point instance (information, institution, chance, capture,
transformability all collapse to the same discrete predecessor).
\(M_1\neq M_2\) as tables. No atomic claim separates them.

Hence not every subset of the raw model lattice is the satisfying
set of a sentence.

### 1. Corrected theorem

Let \(\mathbb M\) be the finite set of instantiations of the declared
class. Let \(\mathcal L\) be the judgment language of TCS-1.0 §4
(Boolean combinations of the eight kernel atoms, finite quantifiers
over finite policy tables). Write \(M\equiv_{\mathcal L}M'\) if \(M\)
and \(M'\) satisfy the same sentences, equivalently (because the
language is the Boolean algebra generated by the atoms) if they
satisfy the same atoms. Let \(\mathbb M/\equiv_{\mathcal L}\) be the
quotient.

**C-a.Thm3\(^\ast\).**

**(A) Definable algebra.** For every sentence \(\Phi\in\mathcal L\),
the satisfying set \(\{M\in\mathbb M:\Phi(M)\}\) is a union of
\(\equiv_{\mathcal L}\)-classes. Equivalently, it is the preimage of
an arbitrary subset of the quotient.

**(B) Completeness on the quotient.** Every subset of
\(\mathbb M/\equiv_{\mathcal L}\) is
\(\{[\Phi]:\Phi\text{ a sentence}\}\) for some \(\Phi\): take the
disjunction, over classes in the subset, of a finite conjunction of
atoms and negated atoms pinning the class. (Finite, because there
are finitely many atoms: eight families \(\times\) \(G\) states,
plus the finitely many decorated variants Thm2 enumerates.)

**(C) Failure on the raw lattice.** There exist table-distinct
models with \(M_1\equiv_{\mathcal L}M_2\) (witness above). The
recorded sentence “every subset of the model lattice arises” is
false.

**(D) Zero-one law does not extend.** Non-monotone sentences can cut
the definable algebra arbitrarily. There is still no extremal
evaluation shortcut for them. The U/M boundary stands: the
registered U-inventory captures the monotone fragment; everything
beyond is per-instance.

**(E) Thm2 untouched.** Every sentence is decidable at each fixed
instantiation, by computing the atoms and evaluating the Boolean
tree. Logical completeness over *all* instantiations remains OPEN,
as recorded.

### 2. Proof

**(A)** If \(M\equiv_{\mathcal L}M'\) then \(M\models\Phi\) iff
\(M'\models\Phi\), by definition. ∎

**(B)** Each class is the set of models satisfying a particular
finite atom-valuation \(v\). The conjunction
\(\Phi_v=\bigwedge_{\text{atoms }\alpha}\alpha^{v(\alpha)}\)
(negating when \(v(\alpha)=0\)) holds exactly on that class, because
two models with the same atom-valuation satisfy the same sentences.
Disjoin the \(\Phi_v\) over the chosen classes. ∎

**(C)** The two-point tables. ∎

**(D)** On the quotient the recorded arbitrariness holds, by (B). A
non-monotone subset of the quotient (neither up-set nor down-set
for the induced order) is realised by a sentence, so the zero-one
shortcut fails for that sentence. The recorded instance
“\(\emptyset\neq\mathrm{Viab}\neq K\)” is still a non-monotone
sentence; its satisfying set is definable, and neither an up-set
nor a down-set. ∎

### 3. C-a.Thm2 complexity (Finding 20)

A predecessor step scans \(G\cdot|U|\cdot|D|\) table entries and,
for each, tests subsethood of a set of size at most \(G\). That is
\(O(G^2\cdot|U|\cdot|D|)\) **bit** operations, or
\(O(G\cdot|U|\cdot|D|)\) **word** operations if a \(G\)-bit
characteristic vector is one word. The recorded
\(O(N\cdot G\cdot|U|\cdot|D|)\) headline is the word-parallel
convention and should be named. Under bit cost the honest bound is
\(O(N\cdot G^2\cdot|U|\cdot|D|)\). The decision procedure is
unaffected.

---

# Class 3 — definitional, sign, and scope defects

---

## VII. \(L_G\) is an envelope modulus — E7.Cor3 and C-e

**Sources.** Packet
`corrected_theorems/02_operator_I_strong_invariance_and_erosion.md`,
Lemma 2; `E7_CONSERVATION_VIABILITY_COUPLING.md` Cor3;
`C_TIER_COMPLETIONS.md` C-e. **Reaudit.** Finding 13.

### 0. The controlling definition

Lemma 2 of the packet: \(L_G\) is the Hausdorff–Lipschitz modulus of
the **velocity envelope** \(G\),

\[
d_H\bigl(G(x),G(p)\bigr)\;\le\; L_G\,\|x-p\|
\quad\text{in the inner tube,}
\]

together with an inward Hamiltonian bound
\(\sup_{v\in G(p)}\langle n(p),v\rangle\le-\alpha<0\) on \(\partial K\).
Then \(L_G r+\Delta_\varepsilon\le\alpha\) yields strong invariance
of \(K_{-r}\).

\(L_G\) is a property of the **dynamics**, not of the barrier.

E7.Cor3 sets \(L_G=0\) for affine barriers because “the normal is
constant.” An affine constraint with a Lipschitz-varying envelope
has \(L_G>0\). The claim is false of the packet's \(L_G\).

C-e sets \(L_G=\inf\{2\sqrt{x^\top M^2 x}:B(x)=b\}\), a lower bound
on \(\|\nabla B\|\). That is barrier geometry.

### 1. Two constants

**Definition VII.1.** \(L_G\) is the packet modulus of \(G\), as
above.

**Definition VII.2.** For a \(C^{1,1}\) barrier \(B\) with nonvanishing
gradient on a band, the **barrier comparison constants** on that band
are

\[
m_B\;:=\;\inf\|\nabla B\|,
\qquad
M_B\;:=\;\sup\|\nabla B\|.
\]

Write \(L_B:=M_B\) when only an upper Lipschitz constant of \(B\) is
needed. Metric and barrier erosions are related by the packet's own
warning: \(K_{-r}\) and \(\{B\ge\eta\}\) are different sets unless
comparison constants are proved. If \(m_B>0\),

\begin{equation}
\label{eq:compare}
\{B\ge B|_{\partial K}+M_B r\}
\;\subseteq\;
K_{-r}
\;\subseteq\;
\{B\ge B|_{\partial K}+m_B r\}
\end{equation}

up to the usual orientation (inward \(B\) increasing). The left
inclusion uses \(M_B\); the right uses \(m_B\). C-e's displayed
infimum is \(m_B\) on the level \(\{B=b\}\), not \(L_G\).

### 2. What *is* true of affine barriers

**E7.Cor3\(^\ast\).** Let \(K=\{x:\langle n,x\rangle\le c\}\) with
\(\|n\|=1\). Then:

1. Signed distance to \(K\) is affine, hence \(C^\infty\), and the
   two-sided tubular radius is \(\rho=+\infty\). Lemma 2's geometric
   hypotheses hold **without a radius restriction**. The erosion
   calculus applies globally.
2. The outward normal is constant. That does **not** force
   \(L_G=0\). \(L_G\) is the Lipschitz constant of \(G\), which may
   vary along the hyperplane.
3. If in addition \(G\) is translation-invariant in a neighbourhood
   of \(K\) (in particular if \(G\) is state-independent), then one
   may take \(L_G=0\), and Lemma 2 reduces to \(\Delta_\varepsilon\le\alpha\).
4. E7.Thm1(a)'s integral identity is a **ledger** statement. It is
   not Lemma 2 at \(L_G=0\). The two coincide on the floor
   \(\{q_L\ge 0\}\) when the velocity of \(q_L\) is
   state-independent, which is exactly case (3).

### 3. C-e, restated

**C-e.Thm1\(^\ast\).** Let \(B(x)=x^\top Mx-c\) with \(M\succ 0\),
and let \(\Phi^\pm\) be the declared quadratic flux bounds of the
source file.

**(A) Sandwich (ledger).** The telescoping identity
\(B(x(t))=B(x(0))+\int 2x^\top M\dot x\) plus the flux bounds give

\[
\{B\ge\Phi^-_T\}
\;\subseteq\;
\mathrm{Viab}_T(\{B\ge 0\})
\;\subseteq\;
\{B\ge\Phi^-_T\}
\]

when the worst-case drain \(dB=-\Phi^-\) is an admitted realisation
(inner and outer meet). If the drain is not forced, the outer bound
is the necessary condition against the worst admitted drain, still
\(\Phi^-_T\), not \(\Phi^+_T-\Phi^-_T\). The recorded outer
\(\{B\ge\Phi^+_T-\Phi^-_T\}\) is the same \(F^+\)-for-\(F^-\)
substitution as E7.Thm1(c) and is weaker than the proof.

**(B) Barrier constants, not \(L_G\).** On a compact level band of
\(B\), \(m_B=\inf 2\sqrt{x^\top M^2 x}>0\) and \(M_B<\infty\).
Metric and barrier erosions compare by \eqref{eq:compare}. The
packet modulus \(L_G\) is independent data of the envelope and is
not computed from \(M\).

**(C) Semidefinite interpolation.** If \(M\succeq 0\) is singular,
\(m_B=0\) along the kernel of \(M\), and barrier comparison loses
one direction. That is the honest boundary toward the affine case,
and it is a statement about \(m_B\), not about \(L_G\).

### 4. Status

Recorded \(L_G=0\) for affine barriers: **false** of the packet
constant. Recorded \(L_G=\inf\|\nabla B\|\): **false** (wrong
object). Affine global tubular geometry: **true**. Ledger sandwiches:
**true**, with the sharp outer bound of §X below. The ambition —
affine ledgers are the exactly integrable case of the erosion
calculus — is true under translation-invariant \(G\), and is not
true as a statement about \(L_G\).

---

## VIII. A4.Thm1 — packet sign

**Source.** `A4_NONLINEAR_SMALL_GAIN.md`, Thm1 Step 2, and the
Setting-section lemma. **Reaudit.** Findings 14 and 20 (the
\(\varphi_i(s)=\varphi_i(r^\ast)\) slip). Thm2's lattice theory was
verified and is kept.

### 1. The sign

Packet Lemma 2 uses an **inward** margin
\(\langle n,v\rangle\le-\alpha<0\) and closes by addition:

\[
\langle n,w\rangle
\;\le\;
-\alpha+L_G r+\Delta_\varepsilon
\;\le\;
0
\qquad\text{once}\qquad
L_G r+\Delta_\varepsilon\le\alpha.
\]

Recorded Step 2 writes
\(\langle n_i,f_i\rangle\le\alpha_i+L_i r^\ast_i\) and “the
encroachment is covered by \(\alpha_i+L_i r^\ast_i\)”. That is the
packet inequality with the sign of \(\alpha\) flipped and the
encroachment placed on the wrong side.

**A4.Thm1 Step 2\(^\ast\).** On an active face \(i\in I(x)\), with
the shared \(u\in A(x)\) of hypothesis 2,

\begin{equation}
\label{eq:A4sign}
\langle n_i,f_i(x_i,u)\rangle
\;\le\;
-\alpha_i
+L_i r^\ast_i
+\Lambda_i\sum_j\delta_{ij}(r^\ast_j)
+\Delta_i
\;\le\;
0,
\end{equation}

the last inequality being exactly \((*)\) of Step 1 at the genuine
contract \(r^\ast\). Here \(L_i\) **is** the packet \(L_G\) of
module \(i\)'s envelope, not a barrier constant. Strong invariance
of \(K_{r^\ast}\) then follows from packet Lemma 2 plus the
measurable selector of \(A\) (E2.B2(a)\(^\ast\)).

The conclusion of Thm1 survives. The displayed step is replaced, not
the theorem.

### 2. Setting-section lemma

The recorded line \(\varphi_i(s)=\varphi_i(r^\ast)\) is false.
Monotonicity of \(\varphi_i\) in the *other* coordinates and
\(s\ge r^\ast\) give \(\varphi_i(s)\ge\varphi_i(r^\ast)\). That is
what A4.Thm2's own proof already uses, and it is enough: if
truncation is active at \(r^\ast\) then
\(\varphi_i(s)\ge\varphi_i(r^\ast)>\rho_i=s_i\), contradicting
\(\varphi(s)\le s\).

### 3. A4.Thm1-Explicit, equality (Finding 20)

The composite condition is \(\delta_{12}(\delta_{21}(r))\le r\),
non-strict. In the linear shadow this is \(\gamma_{12}\gamma_{21}\le 1\),
not the strict \(\rho(\Gamma)<1\) of R05.Cor3. At equality, with
\(\delta(0)=0\) and \(\alpha_i=\Delta_i\), every point of a ray is a
feasible contract and there is no *least positive* contract; the
lattice least fixed point is \(0\). R05.Cor3 is strict because it
wants geometric convergence to a unique interior point. One clause,
not a retreat: the explicit theorem's \(\exists r>0\) is correct at
equality; uniqueness and the linear spectral gap are not.

---

## IX. E7.Thm2 — noncompensation against the outer bound

**Source.** E7.Thm2. **Reaudit.** Finding 15.

### 0. The recorded exit claim is false

Thm2 claims that \(q_{L_i}(0)<D_{i,T}\) (a deficit relative to the
**committed** budget of rule (a)) cannot be compensated and that the
state is outside the product kernel. Rule (a) is an *inner* bound.
It is conservative by construction. The same file's E5 sanity check
says so: “the floor's \(D_T=0.4\cdot T\) is conservative against the
true kernel \(S\ge 2\)”. A state with \(S(0)<0.4\cdot T\) can still
be viable because regeneration is ignored by (a).

### 1. Corrected theorem

**E7.Thm2\(^\ast\).** Ledgers \(L_1,\ldots,L_m\) with **no** declared
conversion pathway.

**(A) Product inner rule.** Componentwise (a):

\[
\prod_i\{q_{L_i}\ge D_{i,T}\}
\;\subseteq\;
\mathrm{Viab}_T\Bigl(\prod_i\{q_{L_i}\ge 0\}\Bigr).
\]

**(B) Independence, not Farkas.** The identity for \(q_{L_i}\)
contains no term from ledger \(j\neq i\). A surplus in \(j\) cannot
change \(q_{L_i}(t)\). That is the noncompensation axiom on this
hypothesis, and it does not use B6.

**(C) Kernel-exit only from an outer deficit.** If

\[
q_{L_i}(0)
\;<\;
D^-_{i,T}-F^-_{i,T}
\]

(the sharp outer bound of §X), then no admissible policy keeps
\(\{q_{L_i}\ge 0\}\) on \([0,T]\) against the worst admitted flow,
regardless of every other ledger. The recorded substitution of
\(D_{i,T}\) for this bound is false.

Farkas / B6 re-enters only when a pathway *is* declared. That is
E3.C2 / B6, not this theorem.

---

## X. E7.Thm1(b),(c),(d) — split conclusions, sharp outer bound

**Source.** E7.Thm1. **Reaudit.** Finding 16. Rule (a) was verified
and is kept.

### 1. Rule (b), split

The two disjuncts in the hypothesis support two different
conclusions.

**E7.Thm1(b1)\(^\ast\) (adversarial-exit / empty kernel).** If
\(D(t)\ge\gamma>0\) policy-independently and \(F\equiv 0\) is an
admitted realisation (or the worst admitted net inflow on
\([0,T]\) is \(\le 0\)), then

\[
\mathrm{Viab}_T(\{q_L\ge 0\})=\emptyset
\qquad\text{for all }T>q_L(0)/\gamma.
\]

This is an R03 first-branch certificate: the kernel is empty because
one admitted flow drains the floor. It does **not** say that every
trajectory exits.

**E7.Thm1(b2)\(^\ast\) (universal exit).** If \(F\le 0\) along
**every** admitted realisation and \(D\ge\gamma\), then every
trajectory satisfies \(q_L(t)\le q_L(0)-\gamma t\) and exits the
floor by time \(q_L(0)/\gamma\).

The recorded “moreover every trajectory exits” is (b2) and requires
the universal hypothesis, not “\(F\equiv 0\) is possible.”

### 2. Rule (c), sharp bound

The proof takes the adversarial inflow \(F\equiv F^-\) and obtains

\[
q_L(0)\;\ge\; D^-_T-F^-_T
\]

as a necessary condition for floor-viability. The recorded display
replaces \(F^-\) by \(F^+\) (“best-case relief”). That inequality is
true and strictly weaker:
\(D^--F^+\le D^--F^-\) whenever \(F^+\ge F^-\), so the necessary
lower bound on \(q_L(0)\) is loosened, and the sandwich gap is
inflated.

**E7.Thm1(c)\(^\ast\).** If \(x\in\mathrm{Viab}_T(\{q_L\ge 0\})\),
then \(q_L(x)\ge D^-_T-F^-_T\).

(The ceiling-slack reading is the same identity applied to
\(\ell=c-q_R\), with the worst admitted fill of \(q_R\).)

### 3. Sandwich (d)

**E7.Thm1(d)\(^\ast\).**

\[
\{q_L\ge D_T\}
\;\subseteq\;
\mathrm{Viab}_T(\{q_L\ge 0\})
\;\subseteq\;
\{q_L\ge D^-_T-F^-_T\},
\]

with \(D_T\) the committed budget of (a) (not the recorded
“\(D^+_T\)-budget”). The gap is regeneration and unused optional
outflow. It collapses when \(F\equiv 0\) and \(D\) is forced. The
mixed-regime honesty paragraph of the source is unchanged: a floor
and a ceiling linked by the same extraction are not decided by
either ledger rule alone.

---

## XI. A3.Thm2 — finite versus compact information

**Source.** `A3_VARIABLE_EVENT_KERNEL.md`, Thm2. **Reaudit.**
Finding 17.

### 0. The typing

The statement has \(W\subseteq\mathcal A\times\mathcal B_{\mathrm{info}}\)
with \(\mathcal A\) finite and \(\mathcal B_{\mathrm{info}}\)
**compact**. The proof treats \(\mathcal A\times\mathcal B\) as a
**finite** lattice, claims termination in “\(\le|\mathcal A|\cdot\dim\)
steps” with \(\dim\) undefined, and calls \(\mathrm{Pre}_{\mathcal A}(W)\)
clopen (vacuous on a finite discrete space; unjustified if
\(\mathcal B\) is infinite).

### 1. Corrected theorem

**A3.Thm2\(^\ast\).** Let \(\mathcal A\) be a finite observation
alphabet, \(O\) have clopen fibres in \(\tau_{\mathrm{IS}}\).

**(A) What clopen buys.** \(O\) is locally constant, so the
event-time information update depends on the history only through
the letter \(a\in\mathcal A\). The predecessor is well-defined on
the quotient by \(O\).

**(B) Finite information state.** If \(\mathcal B\) is finite, the
predecessor is a monotone self-map of a finite lattice of cardinality
\(2^{|\mathcal A|\,|\mathcal B|}\). The backward recursion reaches
its gfp in at most \(|\mathcal A|\,|\mathcal B|\) *strict decreases*
(lattice height in the inclusion order, for a decreasing iteration
from the top, is at most the number of points). Every subset is
clopen. Termination is genuine.

**(C) Compact information state.** If \(\mathcal B\) is merely
compact metric, Knaster–Tarski still gives a gfp of a monotone
self-map of \(\mathcal K(\mathcal A\times\mathcal B)\), provided
\(\mathrm{Pre}_{\mathcal A}\) sends closed sets to closed sets
(transversality plus closed \(\Sigma\), as in Thm3). Termination is
**not** claimed. Clopenness of \(\mathrm{Pre}_{\mathcal A}(W)\) is
not claimed.

The recorded theorem is (B) with a compact \(\mathcal B\) written in
the statement. That mixture is the defect. Governance-relevant
mode/quota alphabets are (B). Compatible-set information blocks are
(C) and need Thm3's closed-graph argument, not a finite counter.

---

## XII. A3.Thm3 — inherit segment Lipschitz

**Source.** A3.Thm3. **Reaudit.** Finding 1 (propagation) and the
Class 3 listing of A3.Thm2/3.

A3.Thm3 composes Thm2 with “compactness from A3.Thm1”. Recorded
A3.Thm1 is false. The repaired space is
\(\mathcal H(B,J,M,L)\) of
`A3_Thm1_corrected_compactness.md`. Lipschitz hybrid flows already
lie in that space.

**A3.Thm3\(^\ast\).** On the declared class **plus** a uniform
segment Lipschitz bound \(L<\infty\) (or a uniform modulus of
continuity on inter-break segments), the variable-event kernel
exists as the gfp of the combined predecessor on
\(\mathcal H(B,J,M,L)\times\) (information). The recorded proof
pattern — flow-predecessor off breaks, clopen information update at
transversal events, closed graph, Knaster–Tarski — stands on that
space. Conditionality is now four declarations: budget,
transversality, clopenness, segment Lipschitz. The three residues
of the source file (non-clopen, grazing, unbounded breaks) remain,
and a fourth is named: unbounded segment Lipschitz, the
\(\sin(ks)\) obstruction.

No other recorded conclusion is changed. B8 remains conditional on
both parents.

---

## XIII. C-f.Thm1 — lock the statement to the proof

**Source.** `C_TIER_COMPLETIONS.md`, C-f. **Reaudit.** Finding 18.

The statement quantifies over an arbitrary observable
\(\pi:C([-\tau,0],\mathbb R^n)\to Y\). The proof of
\((\Longrightarrow)\) is written for restriction-type / window
observables and says so in a parenthetical.

**C-f.Thm1\(^\ast\).** Let \(\dot x=f(x_t)\) with \(f\) locally
Lipschitz on bounded sets. Let \(\pi_{\tilde\tau}\) be restriction
to \([-\tilde\tau,0]\), \(\tilde\tau\le\tau\).

**(A)** \(f\) factors through \(\pi_{\tilde\tau}\) if and only if the
window \(Y=C([-\tilde\tau,0],\mathbb R^n)\) carries a closed
autonomous RFDE of delay \(\tilde\tau\).

**(B)** The minimal such \(\tilde\tau\), when it exists, is the
memory horizon. \(\tilde\tau<\tau\) iff the discarded prefix is
invisible to \(f\).

**(C)** For a general observable \(\pi\), autonomy of the aggregate
is fibre-constancy of \(f\) on the \(\sigma\)-algebra generated by
the *aggregate history*, not on a window unless \(\pi\) is a window.
That general form is the definition of a factor system and is not a
theorem of this file.

*Proof of (A).* \((\Longleftarrow)\): if \(f=\tilde f\circ\pi_{\tilde\tau}\),
the window state \(y_t=x|_{[t-\tilde\tau,t]}\) satisfies an RFDE
driven by \(\tilde f\) alone. \((\Longrightarrow)\): if the window
closes autonomously, \(\dot x(t)\) is a function of
\((x|_{[t-\tilde\tau,t]})\), i.e. of \(\pi_{\tilde\tau}(x_t)\). ∎

The recorded general-\(\pi\) sentence is not a conjecture; it is a
statement whose \((\Longrightarrow)\) was not proved. The window
case is the governance-relevant class the source already named
(moving averages, windowed extrema). Full-window functionals
(\(\int_{-\tau}^0\)) have horizon \(\tilde\tau=\tau\), the honest
negative reading, unchanged.

---

## XIV. B7.Thm1(3) — genericity is not a one-parameter theorem

**Source.** `B_TIER_BRIDGES.md`, B7. **Reaudit.** Finding 19. Parts
(1) and (2) are kept, with the uniform exhaustion in (1) named.

### 1. Jet transversality is about families of maps

Thom's theorem: for a submanifold \(S\) of a jet space, a residual
set of \(C^k\) maps (Whitney topology) has jets transverse to \(S\).
It does **not** say that a residual set of *parameters* in a fixed
one-parameter family \(f(\,\cdot\,,\lambda)\) is a transversal-contact
value. An arbitrary path \(\lambda\mapsto f(\,\cdot\,,\lambda)\) may
miss the residual set of maps entirely, or meet the contact stratum
non-transversally on a positive-measure set of \(\lambda\).

**B7.Thm1(3)\(^\ast\).**

- **(3a) In a space of families.** For a residual set of
  \(C^k\) families \((f,K)\) (Whitney, finite-jet order as declared),
  the set of \(\lambda\in\Lambda\) at which a maximally-safe
  trajectory meets \(\partial K(\lambda)\) is either empty or
  consists of transversal contacts. This is Thom applied to the
  evaluation map of the family, i.e. an unfolding-level statement.
- **(3b) For a fixed family.** Transversality at a given \(\lambda_1\)
  is a hypothesis of part (2), not a conclusion. No residual-in-\(\Lambda\)
  claim is made for an arbitrary declared path.

The recorded sentence is (3a) mislabelled as a statement about a
given \(\Lambda\).

### 2. Part (1), the exhaustion

Hausdorff continuity of each finite iterate \(V_n(\lambda)\) follows
from Hausdorff continuity of \(\mathrm{Pre}_\lambda\), itself from
uniform successor hypotheses plus Hausdorff continuity of
\(\partial K(\lambda)\) and structural stability of the boundary
flow (no new orbit types). The passage

\[
\mathrm{Viab}(\lambda)=\bigcap_n V_n(\lambda)
\]

is Hausdorff-continuous at \(\lambda_0\) if the exhaustion is
**uniform** on a neighbourhood \(U\) of \(\lambda_0\):

\[
\sup_{\lambda\in U}\,
d_H\bigl(V_n(\lambda),\mathrm{Viab}(\lambda)\bigr)
\;\xrightarrow{n\to\infty}\;0.
\]

That uniform radius is an extra hypothesis. Structural stability
supplies it when the conjugacy modulus and the boundary variation
are themselves uniform on \(U\); that implication is plausible and
used in hybrid-limit arguments, but it is not written in the source.
**B7.Thm1(1)\(^\ast\)** is the recorded no-change rule with the
uniform exhaustion named as a hypothesis. The conclusion
(Hausdorff continuity of the kernel, no jump) is unchanged.

Part (2) (transversal contact \(\Rightarrow\) membership flip) is
the implicit-function argument on the exit time, and is kept.

---

## XV. E3.C2 — one Farkas alternative

**Source.** E3.C2. **Reaudit.** Finding 20.

The statement writes \(y^\top A\le 0\); the proof writes
\(y^\top A=0\). Both appear in the literature; they are not the same
alternative.

**E3.C2\(^\ast\) (linear substitution).** The system \(Ax\le b\) is
feasible if and only if every \(y\ge 0\) with \(y^\top A=0\)
satisfies \(y^\top b\ge 0\). Equivalently, exactly one of the
following holds: (a) \(\exists x,\;Ax\le b\); (b) \(\exists y\ge 0\),
\(y^\top A=0\), \(y^\top b<0\). Alternative (b) is the
noncompensability certificate.

(The cone form \(y^\top A\le 0\), \(y^\top b<0\) is Farkas for
\(Ax=b\), \(x\ge 0\), a different system.) Typo “surflux” in the
source is “surplus.” Nonlinear local stability is B6.Thm1(1)\(^\ast\),
already delivered, not the recorded MFCQ iff.

---

## XVI. Finding 20 remainder — E1.A1 Move 1

**Source.** `E1_LANGUAGE_COMPLETENESS.md`, A1 Move 1.

Recorded: promoting a disturbance to a state block, versus leaving
it as an input and reading the robust kernel, “are definitionally
the same set.”

They are the same set only if the promoted block's admissible
trajectories **coincide** with the declared disturbance class. That
is a hypothesis on the promotion (complete, exactly the measurable
inputs \(d(\cdot)\in D\), no extra ODE constraint that thins the
class, no Filippov enlargement that thickens it). It is not a
definition.

**E1.A1 Move 1\(^\ast\).** The two readings define the same subset of
the physical state space if and only if the promoted disturbance
block realises exactly the admissible input class of the robust
reading. Under that matching hypothesis the eight-family
representation is unaffected. Without it, adversary promotion can
strictly shrink or enlarge the kernel, and the move is a modelling
choice, not a definitional identity.

(The rest of A1 — the eight typed representations — is not re-opened.
The reaudit listed A1 as verified except for this clause.)

---

# Status register

Per TCS-1.0 §9 axiom 5, every move below is a demotion, a scope-lock,
or a replacement of a false sentence by a true one of equal or
greater force. None is a promotion of a recorded `PROVEN` tag that
the argument did not earn.

| Row | Recorded | Here |
|---|---|---|
| E2.B1(a) | PROVEN (reconstructed) | gfp **proved**; inheritance **false**; transfer on downward-closed (REG) families **proved** |
| E3.C6.3 | PROVEN (reconstructed) | iff **false**; (B)(C) characterisation **proved**; Prop3 sharpness **kept** |
| B1.Thm1 | PROVEN (reconstructed) | (A)–(C) **proved** at the delivered depth; verbatim replacement **false** without hyp at \(3r/2\) |
| B9.Thm1(1) | PROVEN restricted | product-split \(\subseteq K_p\) **proved**; reverse **false**; residual-budget DP **proved** and complete |
| B10.Thm1(1) | PROVEN foundational | optimistic max **proved**; pessimistic max **false** without extra hyp; coincidence **false** |
| B10.Thm1(2) | PROVEN foundational | existential reduction **proved**; universal closed-graph **false** |
| C-a.Thm3 | PROVEN (reconstructed) | arbitrariness on the **quotient** **proved**; raw-lattice claim **false** |
| E7.Cor3 / C-e | PROVEN (reconstructed) | \(L_G=0\) / \(L_G=\inf\|\nabla B\|\) **false**; affine tubular geometry and ledger sandwich **proved** |
| A4.Thm1 Step 2 | PROVEN (reconstructed) | sign **replaced**; conclusion **survives** |
| E7.Thm2 | PROVEN (reconstructed) | inner product **proved**; exit from \(D_{i,T}\) **false**; exit from outer bound **proved** |
| E7.Thm1(b)(c)(d) | PROVEN (reconstructed) | (b) **split**; (c)(d) **sharpened** to \(F^-\) |
| A3.Thm2 | PROVEN (reconstructed) | finite case **proved**; compact case **gfp only** |
| A3.Thm3 | PROVEN_CONDITIONAL | condition list **adds** \(L<\infty\) |
| C-f.Thm1 | PROVEN (reconstructed) | statement **scope-locked** to windows; both directions **proved** |
| B7.Thm1(3) | PROVEN (reconstructed) | residual-in-\(\Lambda\) **false** for a fixed path; unfolding-level genericity **stated** |
| B7.Thm1(1) | PROVEN (reconstructed) | uniform exhaustion **named** |
| E3.C2 | PROVEN (reconstructed) | one alternative **fixed** |
| C-a.Thm2 complexity | PROVEN (reconstructed) | word-parallel convention **named** |
| E1.A1 Move 1 | PROVEN (reconstructed) | matching hypothesis **named** |

No part of this file modifies the repository.

Class 1 files and `E2_B2a_measurable_selection.md` together with this
file exhaust `PROOF_REAUDIT.md` Findings 1–20.

# Notation identity in the reuse set

A line-level read of the 306 sentences the ledger cleared for verbatim reuse, following
`v48_reuse_audit_v1.py` (words) with `v48_notation_drift_v1.py` (the maths inside them). 16 of the
306 reuse a symbol in a form the deposited article does not use for that object. This is not a spelling
quibble: in this paper the fonts are load-bearing, and in four of the six classes the form the draft chose is a
letter the deposited article has already given something else.


| class | occurrences in the 306 | in the whole draft | in the deposited article | already in the shipped v47 |
|---|---|---|---|---|
| `reserved-operator` | 6 | 30 | 0 | 4 |
| `reserved-font` | 4 | 4 | 2 | 6 |
| `dropped-font` | 1 | 1 | 0 | 0 |
| `colliding-decoration-A` | 4 | 9 | 0 | 1 |
| `colliding-decoration-B` | 4 | 7 | 0 | 5 |
| `renamed-object-H` | 4 | 18 | 0 | 6 |

The columns are counts of the pattern, not of flaws: the deposited article's own `\mathsf{S}` and `\mathcal{B}(x,t)` are correct uses of the same glyphs, which is exactly the point - the document would print one glyph for two objects.

## The rows, with the line each rule is measured against

### `colliding-decoration-A`

**D0574** · draft §front · nearest deposit sentence at ratio 0.502 · ledger verdict: supported at high confidence

- the article writes the barrier $A_{\min}^{\mathrm{win}}$; $\mathcal{A}$ is its adequacy functional
- disposition: strip the $\mathcal$, or regenerate the row

- the deposited article writes: `adequacies expressed in common units, and let $\mathcal A:\mathbb R^{n}\to\mathbb R$ be monotone, $r\le r'\Rightarrow\mathcal A(r)\le\mathcal A(r')$, calibrated, $\mathca`

> *where $W$ is a standard Wiener process, $\varsigma>0$ a chosen noise scale, and the process is stopped at first reaching the record-relative barrier $\mathcal A^{\mathrm{win}}_{\min}$.

**D0594** · draft §front · nearest deposit sentence at ratio 0.298 · ledger verdict: supported at high confidence

- the article writes the barrier $A_{\min}^{\mathrm{win}}$; $\mathcal{A}$ is its adequacy functional
- disposition: strip the $\mathcal$, or regenerate the row

- the deposited article writes: `adequacies expressed in common units, and let $\mathcal A:\mathbb R^{n}\to\mathbb R$ be monotone, $r\le r'\Rightarrow\mathcal A(r)\le\mathcal A(r')$, calibrated, $\mathca`

> The inverse-Gaussian family has a degenerate boundary limit concentrated at zero, and $\mathrm{IG}(0,0)$ is not an ordinary inverse-Gaussian distribution. **Zero cells report zero relative to the selected observational barrier** — not zero physical uncertainty, and no confirmation of collapse. 2. **

### `colliding-decoration-B`

**D0561** · draft §6.5.4 · nearest deposit sentence at ratio 0.684 · ledger verdict: supported at high confidence

- the article writes $B_{\lim}$, and keeps $\mathcal{B}(x,t)$ for the attainable-balance domain
- disposition: strip the $\mathcal$, or regenerate the row

- the deposited article writes: `and a declared demand set $\mathcal{D}(t)$,* $$\mathcal{B}(x,t) = \{ \mathcal{O}(x,u,\theta) - d : u \in \mathcal{U}(x,t),\ d \in \mathcal{D}(t) \}.$$ The geometry of the`

> With $\mathcal B_{\mathrm{lim}}=0.2\max\mathrm{SSB}$ this is the construction tabled as ADH in §6.5.2; the two notations are kept because the boundary hypotheses stated here ($F_{\mathrm{now}}>0$, $\mathrm{SSB}_{\mathrm{now}}>\mathcal B_{\mathrm{lim}}$) are exactly the conditions of the positive sub

**D0565** · draft §6.5.4 · nearest deposit sentence at ratio 0.69 · ledger verdict: supported at high confidence

- the article writes $B_{\lim}$, and keeps $\mathcal{B}(x,t)$ for the attainable-balance domain
- disposition: strip the $\mathcal$, or regenerate the row

- the deposited article writes: `and a declared demand set $\mathcal{D}(t)$,* $$\mathcal{B}(x,t) = \{ \mathcal{O}(x,u,\theta) - d : u \in \mathcal{U}(x,t),\ d \in \mathcal{D}(t) \}.$$ The geometry of the`

> A genuinely local biomass-decline ratio $\mathcal H^{\mathrm{loc}}_{\mathcal B}=(\mathcal B-\mathcal B_{\mathrm{lim}})/[-\dot{\mathcal B}]_+$ would require a compatible net $\dot{\mathcal B}$ estimate, and a demographic hitting time would require a fully specified population model; RAM Legacy SSB an

**D0597** · draft §front · nearest deposit sentence at ratio 0.34 · ledger verdict: supported at high confidence

- the article writes $B_{\lim}$, and keeps $\mathcal{B}(x,t)$ for the attainable-balance domain
- disposition: strip the $\mathcal$, or regenerate the row

- the deposited article writes: `and a declared demand set $\mathcal{D}(t)$,* $$\mathcal{B}(x,t) = \{ \mathcal{O}(x,u,\theta) - d : u \in \mathcal{U}(x,t),\ d \in \mathcal{D}(t) \}.$$ The geometry of the`

> *so $\mathbb E[\mathcal T_{\mathrm{fish}}]=\log(\mathcal B_0/\mathcal B_{\min})/(h+\varsigma^2/2)$; as $\varsigma\to0^+$ this converges to the deterministic pure-decay horizon when $h=F$ and $\mathcal B_{\min}=\mathcal B_{\mathrm{lim}}$.*

### `dropped-font`

**D0415** · draft §front · nearest deposit sentence at ratio 0.652 · ledger verdict: supported at high confidence

- the hypothesis in the deposited article reads $\dot\chi = \mathsf{S}\eta + b$
- disposition: restore $\mathsf{S}$, or regenerate the row

- the deposited article writes: `times with left and right limits at events.* *(H2) $\dot \chi = \mathsf{S}\eta + b$ with $\eta \ge 0$, separate reverse columns, and donor-limited negative boundary flows`

> Assume (H1) $\chi$ is absolutely continuous between locally finite event times, with left and right limits at events; (H2) $\dot\chi=S\eta+b$ with $\eta\ge0$, separate reverse columns, and donor-limited negative boundary flows; (H3) $L^{\top}S=0$.

### `renamed-object-H`

**D0486** · draft §6.2 · nearest deposit sentence at ratio 0.523 · ledger verdict: supported at high confidence

- the article defines $H_A^{\mathrm{loc}}$ and $H_A^{\mathrm{gross}}$ and never uses $\mathcal{H}$
- disposition: strip the $\mathcal$, or regenerate the row

- the deposited article writes: `**Definition 4 (Local net-depletion ratio).** $$H_A^{\mathrm{loc}}(t) = \frac{A(t) - A_{\min}}{\bigl[ -\dot A(t) \bigr]_+},$$ *with the extended-real convention $H_A^{\ma`

> **When the clocks coincide.** Under the rate bracket the frozen-rate ratio and the true hitting time agree within the bracket: $-\dot A\in[(1-\varepsilon)v_0,(1+\varepsilon)v_0]$ gives $\mathcal H^{\mathrm{loc}}_A=(A(0)-A_{\min})/[-\dot A]_+\in[H_0/(1+\varepsilon),H_0/(1-\varepsilon)]$, hence

**D0565** · draft §6.5.4 · nearest deposit sentence at ratio 0.69 · ledger verdict: supported at high confidence

- the article defines $H_A^{\mathrm{loc}}$ and $H_A^{\mathrm{gross}}$ and never uses $\mathcal{H}$
- disposition: strip the $\mathcal$, or regenerate the row

- the deposited article writes: `**Definition 4 (Local net-depletion ratio).** $$H_A^{\mathrm{loc}}(t) = \frac{A(t) - A_{\min}}{\bigl[ -\dot A(t) \bigr]_+},$$ *with the extended-real convention $H_A^{\ma`

> A genuinely local biomass-decline ratio $\mathcal H^{\mathrm{loc}}_{\mathcal B}=(\mathcal B-\mathcal B_{\mathrm{lim}})/[-\dot{\mathcal B}]_+$ would require a compatible net $\dot{\mathcal B}$ estimate, and a demographic hitting time would require a fully specified population model; RAM Legacy SSB an

**D0585** · draft §front · nearest deposit sentence at ratio 0.482 · ledger verdict: supported at high confidence

- the article defines $H_A^{\mathrm{loc}}$ and $H_A^{\mathrm{gross}}$ and never uses $\mathcal{H}$
- disposition: strip the $\mathcal$, or regenerate the row

- the deposited article writes: `**Definition 4 (Local net-depletion ratio).** $$H_A^{\mathrm{loc}}(t) = \frac{A(t) - A_{\min}}{\bigl[ -\dot A(t) \bigr]_+},$$ *with the extended-real convention $H_A^{\ma`

> For every finite $\varsigma>0$ the inverse-Gaussian median $m$ satisfies $m<\nu=\mathcal H^{\mathrm{win}}_{\mathrm{GW}}$,*

**D0611** · draft §7.7 · nearest deposit sentence at ratio 0.924 · ledger verdict: supported at high confidence

- the article defines $H_A^{\mathrm{loc}}$ and $H_A^{\mathrm{gross}}$ and never uses $\mathcal{H}$
- disposition: strip the $\mathcal$, or regenerate the row

- the deposited article writes: `**Definition 4 (Local net-depletion ratio).** $$H_A^{\mathrm{loc}}(t) = \frac{A(t) - A_{\min}}{\bigl[ -\dot A(t) \bigr]_+},$$ *with the extended-real convention $H_A^{\ma`

> The gross active-pool horizon $\mathcal H^{\mathrm{gross}}_A$ of Definition 3 and its productivity-illusion interpretation — the misreading of a large gross-turnover horizon as evidence of slow net depletion, the false implication recorded in §6.1 — are not first-passage results treated here. 7.

### `reserved-font`

**D0255** · draft §2.4 · nearest deposit sentence at ratio 0.382 · ledger verdict: supported at high confidence

- $\mathsf{S}$ is the hybrid incidence matrix of Conditional Theorem 15 and $\mathsf{L}$ its left null basis; the §2.4 state is written undecorated
- disposition: regenerate the row, or drop the decoration

- the deposited article writes: `and donor-limited negative boundary flows.* *(H3) $\mathsf{L}^\top \mathsf{S} = 0$.* *Then* $$\mathsf{L}^\top \chi(t) - \mathsf{L}^\top \chi(0) = \int_0^t \mathsf{L}^\top`

> The state is $(\mathsf{S},\mathsf{K},\mathsf{N},\mathsf{P})\in\mathbb{R}^4_+$ — in this block's local notation, resource stock, sink stock, nutrient stock and input flux; the carrying capacity and living stock of §2.2 do not enter — with

### `reserved-operator`

**D0195** · draft §2.1 · nearest deposit sentence at ratio 0.291 · ledger verdict: signposting: asserts nothing

- the deposited article calls it $S_{\mathcal{T}}$ and reserves plain $S$ for the moiety readout $S_m
- disposition: normalize the span to $S_{\mathcal{T}}$, or regenerate the row

- the deposited article writes: `u_{\partial}(t) + d_x(t), \qquad v \ge 0, \tag{1}$$ where $S_{\mathcal{T}}$ is the typed stoichiometric (incidence) operator, $y$ collects the declared boundary states — `

> Read this line in words: *what changes in each box equals the wiring applied to the flows, plus what crosses the boundary, plus a stated disturbance.* Here $S^{\top}$ is the typed stoichiometric (incidence) operator; $y$ collects declared boundary states — environmental or companion variables that l

**D0201** · draft §front · nearest deposit sentence at ratio 0.715 · ledger verdict: supported at high confidence

- the deposited article calls it $S_{\mathcal{T}}$ and reserves plain $S$ for the moiety readout $S_m
- disposition: normalize the span to $S_{\mathcal{T}}$, or regenerate the row

- the deposited article writes: `u_{\partial}(t) + d_x(t), \qquad v \ge 0, \tag{1}$$ where $S_{\mathcal{T}}$ is the typed stoichiometric (incidence) operator, $y$ collects the declared boundary states — `

> A physical disturbance on represented material is a different object from a structural discrepancy term. 2. $S^{\top}$ may contain signed entries even though $v\ge 0$.

**D0310** · draft §3.1 · nearest deposit sentence at ratio 0.707 · ledger verdict: supported at high confidence

- the deposited article calls it $S_{\mathcal{T}}$ and reserves plain $S$ for the moiety readout $S_m
- disposition: normalize the span to $S_{\mathcal{T}}$, or regenerate the row

- the deposited article writes: `u_{\partial}(t) + d_x(t), \qquad v \ge 0, \tag{1}$$ where $S_{\mathcal{T}}$ is the typed stoichiometric (incidence) operator, $y$ collects the declared boundary states — `

> **Proposition 1 (Layer 2 ⇒ Layer 1, for the conserved quantities).** *If $\ell^{\top}S^{\top}=0$, then $\tfrac{d}{dt}(\ell^{\top}x)=\ell^{\top}b$, and in a closed system ($b=0$) $\ell^{\top}x$ is invariant.*

**D0331** · draft §front · nearest deposit sentence at ratio 0.925 · ledger verdict: supported at high confidence

- the deposited article calls it $S_{\mathcal{T}}$ and reserves plain $S$ for the moiety readout $S_m
- disposition: normalize the span to $S_{\mathcal{T}}$, or regenerate the row

- the deposited article writes: `u_{\partial}(t) + d_x(t), \qquad v \ge 0, \tag{1}$$ where $S_{\mathcal{T}}$ is the typed stoichiometric (incidence) operator, $y$ collects the declared boundary states — `

> **Proposition 4 (Conservation-law reduction).** *If $\ell^{\top}S^{\top}=0$ for some vector $\ell\in\mathbb R^n$, then $\ell^{\top}x(t)=\ell^{\top}x(0)+\int_0^t\ell^{\top}b(\tau)d\tau$; in a closed system ($b=0$), $\ell^{\top}x$ is invariant.*

**D0380** · draft §4.2 · nearest deposit sentence at ratio 0.442 · ledger verdict: supported at high confidence

- the deposited article calls it $S_{\mathcal{T}}$ and reserves plain $S$ for the moiety readout $S_m
- disposition: normalize the span to $S_{\mathcal{T}}$, or regenerate the row

- the deposited article writes: `u_{\partial}(t) + d_x(t), \qquad v \ge 0, \tag{1}$$ where $S_{\mathcal{T}}$ is the typed stoichiometric (incidence) operator, $y$ collects the declared boundary states — `

> Every column is a two-compartment transfer under the unit-sum routing constraints, so $\mathbb 1^{\top}S^{\top}=0$ column by column — Theorem 8's conservation, at sight.

**D0693** · draft §10.2 · nearest deposit sentence at ratio 0.724 · ledger verdict: supported at high confidence

- the deposited article calls it $S_{\mathcal{T}}$ and reserves plain $S$ for the moiety readout $S_m
- disposition: normalize the span to $S_{\mathcal{T}}$, or regenerate the row

- the deposited article writes: `u_{\partial}(t) + d_x(t), \qquad v \ge 0, \tag{1}$$ where $S_{\mathcal{T}}$ is the typed stoichiometric (incidence) operator, $y$ collects the declared boundary states — `

> Adding unlike units — biomass, money, biodiversity indices, exergy — into one conserved scalar is not authorized by any conservation theorem. 2. **Explicit stoichiometry.** Entries are added within an incidence row only when their types and units agree; every conversion is an explicit coefficient in

## The cosmetics, for completeness

- `\\hat(?![a-zA-Z])` - 2 occurrences in the reuse set; the deposited article writes \widehat. No object changes, so nothing needs a decision; a build that wants one spelling can fold them in the same pass as the classes above.

- `\\dfrac` - 1 occurrences in the reuse set; the deposited article writes \frac. No object changes, so nothing needs a decision; a build that wants one spelling can fold them in the same pass as the classes above.

- `\\blacksquare` - 1 occurrences in the reuse set; the deposited article ends a proof with □. No object changes, so nothing needs a decision; a build that wants one spelling can fold them in the same pass as the classes above.

- `\{,\}` - 1 occurrences in the reuse set; the deposited article writes thousands inside maths differently. No object changes, so nothing needs a decision; a build that wants one spelling can fold them in the same pass as the classes above.


## What this changes about the reuse ruling

The ruling was: reuse what the ledger found supported, and the ledger compared *stripped* prose, so it never saw the
maths a reused sentence carries. The 306 are clean on names, pointers, status labels, universals and hedges - the
audit's own planted-defect test (`v48_audit_selftest.md`) catches 6 of 6 on those checks - and they are not clean
on notation. Nothing here argues for trusting the deposit's *prose* over the draft's; the sentences below are not
a register problem either. They are the reuse decision importing a second name for a defined object.

`v48_overrules_notation_candidate.csv` holds these 16 rows marked `regenerate`: move the sentence to the
deposit's wording and the notation comes with it, with no hand-editing. Renaming that file to `v48_overrules.csv`
applies it, and `v48_reuse_split_v1.py` will re-partition and log every row it moves. Deleting it keeps the reuse,
and then the normalisation is a build-time decision the README has to state.


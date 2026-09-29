# Paper 3 (computational certification) — prior art added, 2026-09-29

## What the paper does

Outer moment relaxation of information-adapted controls + inner adversarial scenario
discretisation → a finite **linear program** whose value and error inflation sandwich the
continuous-time safety value:

`ρ_{H,G} ≤ J_I(T) ≤ ρ_{H,G} + ē + δ_β + L h_t`

Every dual-feasible solution gives a finite lower-bound certificate covering **every**
measurable policy; a strictly positive certified margin is an obstruction certificate.
Results: `thm:bridge`, `prop:rows`, `prop:value`, `prop:rank`, `prop:beliefcells`,
`prop:ladder`, `prop:redesign`. Solved by HiGHS; optimality certified in **exact rational
arithmetic** by independent primal/dual witnesses; solver agrees to 4.2e−17 but is explicitly
**not** a proof object.

## The honest baseline: the sandwich is not new

This is the main concession. **Maidens, Kaynama, Mitchell, Oishi and Dumont (2013)** already
produce a guaranteed **under**-approximation of the viability kernel together with a free
**over**-approximation, and use the latter to bound the error of the former. The two-sided
structure has a precedent, and the text says so rather than claiming it.

What differs, and this is what is claimed:
- **The object.** Classical schemes discretise a *state space* and approximate a *kernel* —
  a set of states. Paper 3 bounds a safety **value** over an **information state**, and the
  certificate must hold against **every measurable information-adapted policy**, not against
  one synthesised controller.
- **The approximations.** Not a grid: an outer moment relaxation of the admissible controls
  plus an inner adversarial selection of stored labels and scenarios.

## The four neighbour groups

1. **Viability kernel computation.** Saint-Pierre (1994), *Appl. Math. Optim.* **29**,
   187–209 — the canonical gridded backward recursion with a convergence statement for open
   sets. Mitchell, Bayen & Tomlin (2005), *IEEE TAC* **50**(7), 947–957 — level-set/HJ
   formulations. Maidens et al. (2013), *Automatica* **49**(7), 2017–2029 — Lagrangian
   reformulation via reachable sets for higher dimension.
2. **Moment relaxations.** Lasserre (2001), *SIAM J. Optim.* **11**(3), 796–817; Parrilo
   (2003). Nested relaxations with nondecreasing lower bounds, asymptotic convergence, and
   **checkable rank/flat-extension conditions certifying exactness** — the direct ancestor of
   the certification idea here. Differences: POP over semialgebraic sets solved by **SDP**
   versus a linear program here; convergence in relaxation **degree** versus in **mesh and
   scenario/enclosure widths**; and Lasserre's exactness certificate licenses extracting a
   global minimiser, whereas a positive margin here certifies **nonviability**.
3. **Scenario approach.** Calafiore & Campi (2005, 2006); Campi & Garatti (2008, 2011);
   Campi, Garatti & Prandini (2009). Superficially the same "sample finitely many instances"
   move, but the guarantee is **probabilistic** (violation ≤ ε with confidence 1−β) against
   paper 3's **worst-case** (adversarially selected scenarios, valid for every measurable
   policy, no measure and no confidence parameter).
4. **Verified numerics.** Interval arithmetic and validated ODE integration. Paper 3
   deliberately does not use it: exact integer/rational paths with independent primal and
   dual witnesses, solver demoted to confirmation. Stated as a division of labour, **not** as
   a claim that interval methods are inferior.

## A citation trap avoided

The 2013 *Automatica* paper is **Maidens, Kaynama, Mitchell, Oishi and Dumont** — Mitchell is
the **third** author, not the first. It is easy to mis-cite as "Mitchell et al." by analogy
with the better-known Mitchell/Bayen/Tomlin 2005 paper. Cited correctly, and the `.tex`
carries a warning comment not to "correct" it.

## A notation collision flagged, not silently resolved

Paper 3's error term is `δ_β`. In the scenario literature, β is a **confidence parameter**.
The two are unrelated — paper 3's β is deterministic. The text flags the collision and states
that ε and β have no counterpart in this paper's guarantee, rather than renaming to hide it.

## What is claimed (five items)

1. A continuous-to-finite bridge for information states with two-sided certified bounds and
   convergence along any admissible refinement (`thm:bridge`).
2. Dual feasibility as a **universal** certificate — covering every measurable policy — with
   a positive margin as an obstruction certificate.
3. **Witness count governed by information–time rank, not input dimension**: at most r+1
   labels at rank r, saturated by a scalar-input construction requiring arbitrarily many
   witnesses (`prop:rank`). The negative half is flagged as the part most likely to surprise.
4. The certificate is **prescriptive** — exact shared-authority hierarchy and redesign
   sensitivities separating what buys tolerance from what buys nothing (`prop:ladder`,
   `prop:redesign`).
5. Exact verification paths by construction; solver demoted to numerical confirmation.

Not claimed: the sandwich as such, moment relaxation as such, scenario discretisation as
such, interval enclosure.

## Checks

- All 18 `\ref` targets resolve; zero missing.
- All cited labels verified present: `thm:bridge`, `prop:rank`, `prop:ladder`,
  `prop:redesign`, `prop:rows`, `prop:value`, `prop:beliefcells`, `priorart`.
- All ten new bibliography entries verified against publisher records.

## Result

`paper03_computational_certification_v12.tex`: 12,160 → 13,796 words.

## Remaining

Paper 4 (6,508 words, 10 years, 10 author-initials) is the last of 2/3/4 and the thinnest.
Then 9, 10, 11.

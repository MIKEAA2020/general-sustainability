# Audit v5 — what remains unformalized in the current paper editions

Method: extract every numbered result (`thm:`/`prop:`/`lem:`/`cor:`/`conj:`)
declared via `\label{}` in each **current** edition, then ask whether that
label is cited anywhere in the Lean layer (all module doc-comments +
`lean/README.md`). Spot-checked: `beliefcells`, `stationary`,
`envelope-finite` appear in papers and **nowhere** in the Lean text, so the
gaps are real, not string-matching artefacts.

## Coverage of core results

| Slot | Paper (current) | Core results | Cited in Lean | Gap |
|---|---|---:|---:|---:|
| obstr P1 | `paper2_obstruction_calculus_v55_Automatica_routes` | 21 | 8 | **13** |
| comp | `paper2_computational_certification_v18` | 8 | 4 | **4** |
| ws | `paper2_worked_systems_v17` | 14 | 1 | **13** |
| minimax | `minimax_dual_certificates_v11` | 14 | 5 | **9** |
| ebc | `paper2_exact_belief_computation_v10` | 8 | 2 | **6** |
| P3 | `paper2_probabilistic_sufficiency_v11` | 18 | 2 | **16** |
| ARV | `applied_regime_viability_v9` | 14 | 1 | **13** |
| **Total (label-using papers)** | | **97** | **23** | **74** |

## Two caveats that stop this being a bigger number than it is

**1. "Not in Lean" ≠ "unverified".** `lean/README.md` states a two-tier
architecture: the Lean layer proves *statement-level soundness*, while the
Python batteries (48/48, 54/54, 30/30, 32/32, 238/238, 53/53 …) certify
*concrete instances*. A large share of the 74 are instance-level or applied
results that are Python's job **by design**, not Lean's. Rough triage by
label semantics:

- **≈19 are applied/instance-level** — e.g. ARV's `prop:capelin`,
  `prop:survey`, `prop:experiment`, `prop:breach`, `prop:catchrecord`,
  `prop:moratorium`; ebc's `prop:census`, `prop:deadline`. Verified by the
  deposited batteries; formalizing them in Lean would add nothing.
- **≈55 are structural** and are the genuine Lean backlog (below).

This split is judgement from label names and the supersession map, not a
deep read of each proposition — worth confirming before committing effort.

**2. Two papers are not measurable this way.** The head paper
(`paper1_assessment_separation_v62`) and E1 use bare descriptive labels
(`the-central-result`, `the-witness-datum`, …), not `thm:` prefixes, so they
score 0/0 in the table above. Separately:
- **Head paper** — `lean/README.md` claims broad coverage (Theorem 5 (1)–(7),
  Remark 2 + Prop 3, Theorem 9, Prop 10, Lemma A, Lemma B, Theorem S2), and
  the module carries 199 theorems. Substantively covered.
- **E1** — the module has 5 theorems (telescoping, two-sided bracket, ascent
  law): a thin slice of a 37-page applied paper, but most of that paper is
  empirical and Python-certified.

## The genuine Lean backlog (structural, not cited anywhere)

- **obstr P1 (13)** — `thm:delayed`, `thm:lp-instant`, `thm:exit`,
  `thm:static-complete`, `thm:pomdp`, `prop:uniform-margin`, `prop:helly`,
  `prop:emptiness`, `prop:recourse`, `prop:decomposition`,
  `prop:window-nogo`, `prop:chance`, `prop:degenerate`
- **P3 (16)** — `thm:support`, `thm:parametric`, `thm:lattice`, `thm:class`,
  `prop:antichain`, `prop:pl`, `prop:degen`, `prop:freeze`, `prop:deficit`,
  `prop:learn`, `prop:pathdeficit`, `prop:noisyprobe`, `prop:dr`,
  `prop:probecount`, `prop:additivelaw`, `cor:closed`
  ← largest structural gap *relative to module size* (module has 4 theorems)
- **ws (13)** — `prop:stationary`, `prop:decomp`, `prop:lattice`,
  `prop:req`, `prop:timing`, `prop:regime`, `prop:adequacy`, `prop:saddle`,
  `prop:helly`, `prop:margins`, (+ `prop:register`/`prop:authority`/`prop:bench`)
- **ARV (4 structural of 13)** — `prop:windows`, `prop:brackets`,
  `prop:profile`, `prop:bands` (the §D roadmap added in v9: window profile,
  band certificates, vintage typology, backward extension)
- **minimax (8 + 1 conjecture)** — `thm:envelope-finite`, `thm:general`,
  `lem:bridge`, `prop:recourse-id`, `prop:tower`, `prop:strict`,
  `prop:refine`, `cor:three-branch`
- **ebc (4–6)** — `cor:hamming`, `lem:triangle`, `prop:bands`, `prop:pbvi`
- **comp (4)** — `cor:dual`, `prop:rank`, `prop:beliefcells`, `prop:redesign`

## Two things worth flagging

**`conj:envelope` (minimax) is a conjecture, and correctly is not**
formalized. If a future pass ever makes it a `theorem`, that is a red flag
worth catching — it would mean an unproved claim entered the layer.

**Editions moved, the layer did not.** `lean/README.md` says the theorem
layer is "unchanged across these presentation-pass editions — round 27/28
touched navigation, keywords, and reference hygiene only". That holds for
27/28, but later rounds added substance: ARV v8→v9 alone went 185→229
certified items via the §D roadmap, and minimax v9→v11 went 23→34. The
coverage table shows the layer did not follow those additions. The README's
"unchanged" sentence is now doing work it should not — it is the same
category of over-claim as the vacuous lemmas in v4, just at the level of the
index rather than a declaration.

## Recommendation

Prioritise by fault-risk, not by size: **obstr's five theorems**
(`thm:delayed`, `thm:pomdp`, `thm:exit`, `thm:static-complete`,
`thm:lp-instant`) are the classic hard cases where a statement/proof
mismatch is most likely and most consequential, then **P3's** structural
core (18 results against a 4-theorem module is the worst ratio in the
layer). ARV's `prop:windows`/`prop:brackets` are the cheapest wins (they
extend an existing bracket formalization).

On tooling: the playground is not needed and would be worse. The layer has
no Mathlib, so a full `lake build` here takes **14 s** and is authoritative
for the pinned toolchain, where the playground is not. The binding
constraint is judgement about which statements to formalize, which no
tooling shortens.

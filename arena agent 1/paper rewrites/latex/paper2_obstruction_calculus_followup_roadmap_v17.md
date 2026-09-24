# Paper 2 — Obstruction Calculus: Follow-up Roadmap (v17)

**Subject:** *An Obstruction Calculus for Viability under Incomplete Observation*
(current: `paper2_obstruction_calculus_v49_Automatica_routes.tex` + supplementary v46).
**Scope:** consolidated follow-up programme — in-manuscript open problems, the
adjudicated nonstandard proposals, the unification and generalization
programmes, the review-of-record demand list, the evidence-gap closure sweep,
and editorial items.
**Disambiguation:** the general-theory programme's separate "Paper 2" (the
Typed Theorem Atlas, `papers/paper2_theorem_atlas/`) is a different paper;
its venue/split memo is out of scope here.

**Sources consolidated:** all sources of v16 (q.v.) plus the joint-audit
records `paper2_trackd_joint_audit_v1.md`, `paper2_elevation_joint_audit_v1.md`,
`paper2_selector_principle_joint_audit_v1.md`, the review blueprints
adjudicated in rounds 5–6, and the owner's consolidation directive of the
seventh decision round.

**v17 changes:** Two closures. (1) **v49 shipped** — the selector-principle
consolidation section (new §8) inserts the recursively viable selector Γ_N,
the seven dual witnesses, the weak/strong duality scoping with the residual
Open Problem, and the monitoring-adequacy reading with the corrected
non-strict delay identity (boundary viable); Sections 8–10 renumber to 9–11
with four cross-reference updates; the two-patch table's residual overfull
(v48) is repaired; first zero-overfull edition of the main text (19 pp,
probes 21/21; addendum `paper2_obstruction_calculus_v49_addendum.md`). The
round-6 verdict that the audited results were "already latent" is thereby
incorporated: §8 claims no new theorem, only the consolidation. (2) **The
flagship consolidation is DECIDED** (owner directive: full flagship
architecture; optimal count delegated). The determination is recorded below
with the fold map; execution of each fold is a NEW consolidated edition and
waits on the owner's confirmation of the concrete plan.

## The consolidation decision (v17)

**Question.** The audit rounds recommend consolidating the short works while
the programme kept producing them (ten Track-D notes, two selector papers, a
successor paper, an applications note, two elevation papers since the audits
began). The owner has chosen the full flagship architecture and delegated the
optimal number of papers.

**Inputs (adjudicated review blueprints).**
*gemini:* two flagships — (i) selectors → calculus, (ii) Vector-Floors /
Lattice / Monitoring → a computational paper; DROP the decentralized and
regimes material; plus library, case studies, pyViabCert.
*grok:* calculus (theory) + Track-B computational paper + belief-state paper
+ a supplement for the catalogue facts + library MVP + an applied paper
(fisheries/carbon); fold the catalogue notes.
*gemini (third block):* insert the duality into the calculus; retire the
micro-drafts into a supplement.
*Shared by all three:* a library; one real application; folding the catalogue
facts out of standalone circulation.

**Determination: N = 4 flagships (+ 1 pending applied paper, owner data).**

| # | Flagship | Claim type | Status / seeds |
|---|----------|-----------|----------------|
| P1 | Obstruction calculus (theory of necessity) | Necessity-side certificate calculus; completeness in the exact classes; residual gap | **Continuing — now v49**; absorbs the viable-selector and successor lineages by v49 §8 and §7 |
| P2 | Computational viability certification and the library (Track B) | Algorithms, exactness on finite systems, solver campaign, artefact | **To build**; seeds: companion bridge (`paper2_companion_recourse_bridge_v1`), LP-solver campaign, library MVP (merited — see below) |
| P3 | Stochastic / belief-state safety values (probabilistic sufficiency) | Belief-state values V_k, deficit duals, support recursion | **To build**; seeds: v49 §10, `paper2_stochastic_selector_v2`, `hidden_parameter_learning_v1` (D10) |
| P4 | Worked-systems supplement (exact audit of the catalogue) | Every count identity across all audited systems, dual-witness tables, design rules | **To build**; backbone: `paper2_selector_concordance_v1`; absorbs the Track-D facts and the applications note |
| P5 | Applied calibration (fisheries / carbon) | One real calibrated application | **Pending owner data** (roadmap item R12); not counted in N |

**Why not N = 2 (gemini).** The two-flagship plan requires DROPPING the
decentralized/institutional and regimes material — finished, machine-verified
lineages — and has no home for the belief-state theory except inside a
computational paper, mixing claim types. Rejected as destructive; the drop is
replaced by absorption into P4.
**Why not N = 3 (grok).** Grok's plan splits the supplement and the applied
paper as separate counted works, but the applied paper cannot start before
the owner supplies calibration data; counting it now repeats the
short-works sprawl. The supplement stays one flagship (P4) and the applied
paper stays pending (P5).
**Why not N ≥ 5.** Each additional split re-creates the consolidation problem.
**Why the four claim types are the right joints.** P1 necessity, P2
computation + artefact, P3 probabilistic sufficiency, P4 exact audit — no two
share a theorem class; every existing lineage maps into exactly one primary
home; nothing verified is dropped.

## Fold map (lineage → destination; execution = NEW consolidated editions; originals retained, marked superseded)

| Lineage (current latest) | Destination |
|---|---|
| `paper2_obstruction_calculus` v45–v49 (+ supplementary v46) | **P1** (continues) |
| `paper2_viable_selector` v1–v3 | **P1** — superseded by v49 §8 (consolidation); editions retained |
| `successor_five_layer` v1 | **P1** — layers now v49 §7 + §8; retained |
| `paper2_companion` bridge v1 | **P2** (seeds; LP-solver campaign) |
| library MVP (to build; Theorem-1 recursion + fibre criterion) | **P2** artefact — MERITED (the computational flagship is a paper, not a report, only with the artefact) |
| `paper2_stochastic_selector` v1–v2 | **P3** (seeds) |
| `hidden_parameter_learning` v1 (D10) | **P3** (instance) |
| `paper2_selector_concordance` v1 | **P4** (backbone) |
| `minimax_dual_certificates` v1 | **P4** (static-duality subsection; benchmark Y* = 27/5) |
| `monitoring_design` v3, `policy_class_lattice` v2, `vector_floor_certificates` v2, `institutional_observation` v2, `hybrid_mode_viability` v2 | **P4** (facts and design rules; P2 keeps the algorithms) |
| `finite_horizon_completeness` v1, `certificate_duality` v1, `comparison_drift_exit` v1, `buffered_viability` v1 | **P4** (worked instances); theory pointers stay in P1 |
| applications note + utility record | **P4** (practitioner section) |
| spine (`paper2_spine_*` v1–v3) | internal source; retained |
| all superseded editions | retained in place; no deletions |

**Merit verdicts recorded.** (a) v49: SHIPPED — both reviewers requested the
consolidation, the content existed and was machine-verified (concordance
C1–C8), and the insertion retires two lineages without deleting anything.
(b) Library MVP: MERITED as P2's artefact — implements exactly the Theorem-1
backward recursion and the partition-form fibre criterion, both already
verified 9/9 and 8/8 in shipped scripts; scheduled with the P2 build.
(c) Standalone micro-papers: RETIRED as editions (roadmap marks supersession;
files retained).

## Build order (each step a new edition or new paper, zero-overfull, verify-script discipline)

1. **P4** worked-systems supplement (backbone concordance; absorbs the fold-map rows above) — largest job, no dependencies.
2. **P2** computational paper + library MVP (companion bridge + solver campaign).
3. **P3** stochastic/belief-state paper (v49 §10 + stochastic selector v2 + D10).
4. **P5** applied calibration — waits on owner data (R12).
5. Supersession banners on absorbed lineages' README/addenda; final roadmap.

## Track E — Sequencing (updated)

| Priority | Item | Depends on |
| --- | --- | --- |
| 1 | Track A complete (v45–v49; A1/A4 v45, A5/A6 v46, A3 v48, consolidation §8 v49) → Automatica submission (owner: venue decision) | nothing |
| 2 | Flagship build step 1: P4 supplement | owner confirmation of this fold map |
| 3 | Flagship build step 2: P2 + library | nothing (parallel) |
| 4 | Flagship build step 3: P3 | nothing (parallel) |
| 5 | B1–B5 companion campaign → folded into P2 | 3 |
| 6 | P5 applied | owner data (R12) |

*Every claim above is a pointer into the cited sources; nothing here creates
theorem status. The strengthened-verification discipline (exact rational
re-derivation before acceptance; solver runs before LP-optimality claims)
applies to all tracks.*

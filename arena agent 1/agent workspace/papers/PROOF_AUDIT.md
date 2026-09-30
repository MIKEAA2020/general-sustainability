# Structural proof audit — theory units 1–6 and 11

**Date:** 2026-09-30. **Scope:** remaining-work item (b). All eleven units were
scanned; units 7 and 9 were drawn in because the instrument found them.
**Instruments:** `papers/proof_audit2.py` (current) and `papers/proof_audit.py`
(superseded — see §5). **Supplement cross-check:** `papers/supprec/`.

> **§6 of an earlier version of this record is RETRACTED.** It reported that
> units 6, 7 and 9 had "75 pointers to supplements that do not exist." That was
> wrong. The supplements exist; they are filed under the **old** paper
> numbering (paper1–paper5), which a search scoped to the **new** unit names
> (paper06, paper08, paper10) could not see. §6 below is the corrected account,
> and §9 records the error.

---

## 0. Summary

| | |
|---|---|
| Claim environments in the family | 112 |
| Claims with **no evidence of proof of any convention** | **1** |
| Claims evidenced informally (worked instance / unmarked prose / computation) | 3 |
| Pointers to the paper's own supplementary sections | 75 |
| Pointers that resolve against a supplement found on the branch | **74** |
| **Pointers that resolve to nothing** | **1** (unit 7, Supplementary S9.5) |

Three findings, all narrower than first reported:

- **Finding A — 1 claim.** Unit 1's *selector principle* (`calc-prop:selector`)
  has no proof of any kind in the main text. It is the only one of 112 claims
  in that state. Its complete proof exists in the unit's supplement.
- **Finding B — corrected.** 74 of the 75 supplement pointers resolve. The
  supplements for units 6, 7 and 9 exist on the branch. One pointer does not
  resolve: unit 7's **Supplementary S9.5**, which has never existed in any
  version of the supplement.
- **Finding C — packaging/staleness.** All four supplements are unattached to
  the current unit files, and unit 1's is **twelve versions stale**: the main
  text advanced from v51 to v63 and no supplement was produced after v51.

No finding here is a proof-correctness finding. This audit checks that a proof
is *evidenced*, not that it is *correct*.

---

## 1. What the audit measures

For each labelled `theorem` / `proposition` / `lemma` / `corollary`, the
instrument looks forward to the next claim environment and asks whether a proof
marker of **any** convention appears in between. Conventions accepted:
`\begin{proof}`, `\emph{Proof.}`, `\emph{Proof sketch.}`, `\textbf{Proof.}`.

Separately it counts the paper's references to *its own* supplement, matched as
`Supplementary S<n>`, `supplementary material (S<n>)`, `the supplementary's
S<n>`, and `Figure~S<n>`.

---

## 2. Per-unit result

| Unit | file | claims | `\begin{proof}` | markers, any style | unproven | own-supplement pointers |
|---|---|---:|---:|---:|---:|---:|
| 1 | paper01_obstruction_calculus_v63 | 21 | 0 | 20 | **1** | **17** (S1,S2,S3 + 2× Figure~S) |
| 2 | paper02_probabilistic_sufficiency_v12 | 18 | 18 | 18 | 2→0 | 0 |
| 3 | paper03_computational_certification_v16 | 7 | 6 | 8 | 0 | 0 |
| 4 | paper04_minimax_dual_certificates_v16 | 13 | 9 | 9 | 4→0 (3 informal) | 0 |
| 5 | paper05_exact_belief_computation_v16 | 9 | 8 | 8 | 1→0 | 0 |
| 6 | paper06_assessment_separation_v67 | 0 | 0 | 30 | 0 | **3** (S8,S9,S10) |
| 7 | paper08_governance_delay_v46 | 16 | 0 | 19 | 0 | **44** (S1…S13.3) |
| 8 | paper09_cod_certification_v32 | 14 | 14 | 14 | 0 | 0 |
| 9 | paper10_depletion_ledgers_v53 | 0 | 0 | 38 | 0 | **11** (S2,S2.1,S5,S5.4,S14,S17) |
| 10 | paper11_forecasting_baselines_v64 | 0 | 0 | 0 | 0 | 0 |
| 11 | paper11c_worked_systems_audit_v2 | 14 | 14 | 14 | 0 | 0 |

`x→0` marks a flag that context-checking cleared (§3).

Units 6, 9 and 10 state results as `Remark`/`Definition`/`Lemma` numbered
inline rather than in claim environments, hence their claim count of 0; units 6
and 9 carry 30 and 38 proof markers regardless.

---

## 3. Context-check of the eight flags — five were instrument artifacts

Standing rule: a flag is a candidate, not a finding. Each was read.

| flag | verdict |
|---|---|
| U2 `cor:closed` | **PROVED.** L572 `\begin{proof}[Derivation of Proposition \ref{cor:closed}]`. Deferred to later in the document; the instrument stopped at the next claim environment and missed it. |
| U2 `prop:freeze` | **PROVED.** An unmarked prose paragraph immediately after the statement carries the argument ("Survivability over a longer window is the conjunction of survivability over the shorter…"). Unmarked, not missing. |
| U5 `scale-cor:hamming` | **PROVED.** The proof is *inside* the statement body ("(ii) forces the pair average to reach 5 while (i) caps it at 2(4−h)…"). |
| U4 `prop:recover` | **Informal.** Stated with worked instances; no proof marker. |
| U4 `prop:gap` | **Informal.** A counterexample instance; the exhibit *is* the demonstration. |
| U4 `thm:benchmark` | **Informal.** Closed-form values with the fibre-width derivation in prose plus a verification script. |
| U4 `cor:three-branch` | **Informal.** Computed inline; "the verification script evaluates the identity exactly". |
| U1 `calc-prop:selector` | **GENUINE GAP — Finding A.** |

The three U4 items are a house style for computed results, not missing
mathematics. They are not defects.

---

## 4. Finding A — the selector principle

Unit 1, `paper01_obstruction_calculus_v63.tex` L609, `calc-prop:selector`.
Stated at L609–L630; the next claim environment is at L666. Between them there
is only a `\subsection` heading. **No proof of any convention.**

This matters out of proportion to its size because §1.2 Contributions (L160)
states:

> "Five obstruction mechanisms are developed, **each with a complete proof**,
> and a sixth is exhibited under a policy-class restriction"

The selector principle is one of the five. Its complete proof exists in the
supplement (§6.1) and is not in v63.

---

## 5. Instrument error — recorded because it is the tenth of its class

`proof_audit.py` counted only `\begin{proof}` environments and reported units 1
and 7 as having **zero proofs** against 21 and 16 claims. That reading is
wrong. Both units write proofs as inline `\emph{Proof.}` /
`\emph{Proof sketch.}` paragraphs with no environment at all: unit 1 has 20
such markers, unit 7 has 19. Units 2, 8 and 11 use real environments.

Trusting the count would have produced a badly false report — "37 theorems with
no proofs" — from a stylistic difference. It was caught by reading the file
rather than trusting the count. `proof_audit.py` is superseded by
`proof_audit2.py`; both are kept and this section records why.

Two further false-positive modes in the corrected instrument, both found by
context-checking: **deferred proofs** (proof placed after the next claim
environment) and **embedded proofs** (argument inside the statement body).
Neither is a defect.

---

## 6. Supplement cross-check (CORRECTED)

### 6.1 What exists, and under what name

The family was originally five papers (paper1–paper5) and was later partitioned
into eleven units (paper01–paper11c). **The supplements were never renamed**,
so they live under the old numbering. That is why a search scoped to the new
unit filenames found nothing.

| Unit | supplement found on branch | size | resolves? |
|---|---|---:|---|
| 1 | `arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v51_Automatica_routes_supplementary.tex` | 85,563 B | S1, S2, S3 + Figure~S1, Figure~S2 — **all resolve** |
| 6 | `arena agent 1/paper rewrites/paper1_supplementary_v12.md` | 36,553 B | **3 / 3** (S8, S9, S10) |
| 7 | `arena agent 1/paper rewrites/paper5_supplementary_v19_NatSustain.md` | 77,327 B | **15 / 16** — S9.5 missing (§6.3) |
| 9 | `paper3/latest-2026-09-19/manuscript/paper3_supplementary_v18.tex` (and `.md`, 59,801 B) | 73,881 B | **6 / 6** (S2, S2.1, S5, S5.4, S14, S17) |

Corroborating evidence that each is the right supplement, not a lookalike:

- **Unit 9** — the supplement's "Accompanies" line is *"Typed Flux Ledgers and
  Depletion Arithmetic: Conservation, Componentwise Diagnostics, and the
  Semantics of Depletion Horizons"*, which is **character-identical** to
  `paper10_depletion_ledgers_v53`'s `\title`. Its unusual cited sections S5.4
  ("G3P basin-row extraction provenance") and S17 ("The overshoot-date
  recomputation") are present.
- **Unit 7** — the supplement's thirteen sections (S1 statement inventory …
  S13 demoted technical detail) are exactly the ones the main text cites,
  including S13.1 Power-grid configuration, S13.2 Crash-window ledger detail
  and S13.3 Prospective-design specifications.
- **Unit 6** — cited S8 (25-check enumeration), S9 (data requirements), S10
  (positioning notes) all present.
- **Unit 1** — v51's main text and v63 contain **identical** sets of 21 claims
  compared by (environment type, statement name): zero added, zero dropped.

Two section citations resolve as **bolded body text** rather than headings, so
a heading-only scan reports them missing when they are present: unit 7's S2.3
("**S2.3 The dimensionless identifiability chart**") and unit 9's S2.1
("S2.1 (Phosphorus identification ladder)"). Both counted as resolved above.

### 6.2 Unit 7 must use v19, not v20

Two candidates exist. `paper5_supplementary_v20_blinded_NatSustain.md` is
headed *"Blinded review copy. Unblinded counterpart:
paper5_supplementary_v19_NatSustain.md. Accompanies blinded main v47."* and
replaces real citations with "citation blinded for review" and real paths with
`[repository]`. The diff between v19 and v20 is **27 lines, all blinding**.

Unit 7's main text is the **unblinded** `paper08_governance_delay_v46` (the
blinded main is v47, a separate file). So the matching supplement is **v19**.

### 6.3 The one pointer that resolves to nothing

Unit 7, L1207:

> "The registered compute-core Hopf pair \(3.666149\) / \(150.358477\) yr —
> the base core (1)'s institutional-delay certificates, reproduced by the
> recovered compute core (**Supplementary S9.5**) — certifies this pair"

v19 contains S9.1 and S9.2 but **no S9.5**. Checked across every available
supplement version (v14–v20): **S9.5 occurs zero times in all of them**, and
neither "compute core" nor the values 3.666149 / 150.358477 appear anywhere in
v19. This content has never been written.

This is the single genuinely dead pointer in the family. It is one pointer, not
44.

### 6.4 Staleness

| Unit | main | latest supplement | gap |
|---|---|---|---|
| 1 | v63 | **v51** | **12 versions — no supplement exists for v52–v63** |
| 6 | v67 (old paper1 lineage reached v42) | v12 | numbering differs across lineages; all cited sections resolve |
| 7 | v46 | v19 (paired with main v46) | current for the paired main |
| 9 | v53 (old paper3 lineage reached v50) | v18 | numbering differs; all cited sections resolve |

Unit 1 is the only demonstrable staleness. A content search for *"Complete proof
of the selector principle"* returns v47–v51 and nothing later, confirming no
supplement was produced after v51.

For unit 1 the supplement still **fits exactly** despite being stale: v51 main
and v63 contain identical 21-claim sets (§6.1). The recovery proposed in §7 is
therefore sound.

---

## 7. Remediation

| # | action | resolves |
|---|---|---|
| 1 | **Unit 1** — recover the v51 supplement, retitle to match v63, attach. Mechanical apart from the title; labels need no rewrite since the supplement is a standalone document (0 dangling refs, braces balanced, environments balanced as committed). Add `\renewcommand{\thefigure}{S\arabic{figure}}` immediately before S4 so its figures render S1/S2/S3 and match the main text's `Figure~S1` (ladder) and `Figure~S2` (obstruction tree) — the fibre figure earlier in the document keeps ordinary numbering and does not consume an S-slot. | Finding A + 17 pointers |
| 2 | **Unit 7** — attach `paper5_supplementary_v19_NatSustain.md` (unblinded). Do **not** attach v20. | 43 of 44 pointers |
| 3 | **Unit 7** — resolve S9.5: either write the compute-core Hopf-pair record, or remove the parenthetical and state the values' provenance in the main text. | the 1 dead pointer |
| 4 | **Units 6 and 9** — attach `paper1_supplementary_v12.md` and `paper3_supplementary_v18.tex`. Update unit 6's stale "Accompanies" title (the main text is now *"Aggregation is a claim, not a presentation…"*, not *"Aggregate Indices and Transition Safety…"*). | 14 pointers |

Nothing has been edited yet.

---

## 8. Limitations

- Structural only. This audit checks that a proof is *evidenced*, not that it
  is *correct*. No theorem has been verified by reading its argument.
- The claim scan is confined to `theorem`/`proposition`/`lemma`/`corollary`
  environments. Units 6, 9 and 10 number results inline ("Definition 47,
  Lemma 4, Proposition 43, Theorem 24"), so their results are not in the claim
  totals.
- Supplement-pointer matching is regex-based on `S<n>` forms; a pointer written
  another way would be missed, so **75 is a lower bound**.
- Section resolution was checked against headings *and* bolded body text. A
  section defined in some third way would still be missed.
- "Informal" verdicts in §3 reflect the presence of a computation or worked
  instance, not an assessment of whether it suffices.
- Version numbers are not comparable across file lineages (unit 9's main is
  v53 while its supplement is v18), so §6.4's staleness column rests on content
  checks, not version arithmetic.
- Compilation remains unverified; no TeX engine is available and all checks
  are static.

---

## 9. Error log — the search that produced the retracted finding

The retracted §6 came from a filename-regex search for supplement-like files
**scoped to the new unit names** (`governance_delay`, `depletion_ledger`,
`assessment_separation`) across 7,240 branch paths. It returned "no
supplementary file ever committed" for all three units and I reported that
without a second check.

It was wrong because the supplements are named `paper1_supplementary_v12.md`,
`paper3_supplementary_v18.tex` and `paper5_supplementary_v19_NatSustain.md` —
old numbering, no unit-name substring. A content search for `S13.3` (a section
only unit 7 cites) found them immediately.

Two lessons, both versions of errors already on record:

1. **A null result from a scoped search is not evidence of absence.** Filename
   matching proves nothing when the naming scheme may differ; search content,
   or enumerate everything and read the list. All 166 supplement-like files
   were one listing away.
2. **The reported severity was an artifact of the search, and it ran the wrong
   way.** A too-narrow search inflated the defect count from 1 to 75. Earlier
   errors of this class also inflated counts. Narrow searches that miss files
   and loose regexes that over-match both produce false findings; only reading
   the candidate distinguishes them.

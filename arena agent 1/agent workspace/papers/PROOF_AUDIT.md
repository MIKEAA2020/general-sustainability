# Structural proof audit — theory units 1–6 and 11

**Date:** 2026-09-30. **Scope:** remaining-work item (b). All eleven units were
scanned; the theory units were the intended target and units 7 and 9 were
drawn in because the instrument found them.
**Instrument:** `papers/proof_audit2.py` (see §5 for why the first instrument
was discarded).

---

## 0. Summary

| | |
|---|---|
| Claim environments in the family | 112 |
| Claims with **no evidence of proof of any convention** | **1** |
| Claims evidenced informally (worked instance / unmarked prose / computation) | 3 |
| **Pointers to the paper's OWN supplementary sections** | **75** |
| **Of those, pointing to a supplement that does not ship** | **75 (all)** |

Two separate findings, of very different severity:

- **Finding A (narrow, 1 claim).** Unit 1's *selector principle*
  (`calc-prop:selector`) has no proof of any kind in the main text. It is the
  only one of the 112 claims in this state.
- **Finding B (systemic, 75 pointers across 4 units).** Units 1, 6, 7 and 9
  repeatedly cite their own supplementary sections — S1 … S17 — and **no such
  supplementary document exists for any of them.** Under a preprints.org
  target, where nothing is screened and publication is irreversible, every one
  of those 75 pointers is a dead link in the published record.

Finding B is the one that matters. It is not a proof defect.

---

## 1. What the audit measures

For each labelled `theorem` / `proposition` / `lemma` / `corollary`, the
instrument looks forward to the next claim environment and asks whether a
proof marker of **any** convention appears in between. Conventions accepted:
`\begin{proof}`, `\emph{Proof.}`, `\emph{Proof sketch.}`, `\textbf{Proof.}`.

Separately it counts the paper's references to *its own* supplement, matched as
`Supplementary S<n>`, `supplementary material (S<n>)`, `the supplementary's
S<n>`, and `Figure~S<n>`. This is reported independently of the proof analysis,
because a pointer to a supplement is a dangling dependency whether or not the
claim it attaches to is also proved inline.

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

Units 6, 9 and 10 state their results as `Remark`/`Definition`/`Lemma`
numbered inline rather than in claim environments, which is why their claim
count is 0; unit 6 has 30 and unit 9 has 38 proof markers regardless.

---

## 3. Context-check of the eight flags — five were instrument artifacts

Standing rule: a flag is a candidate, not a finding. Each was read.

| flag | verdict |
|---|---|
| U2 `cor:closed` | **PROVED.** L572 `\begin{proof}[Derivation of Proposition \ref{cor:closed}]`. The proof is deferred to later in the document; the instrument stopped at the next claim environment and missed it. |
| U2 `prop:freeze` | **PROVED.** An unmarked prose paragraph immediately after the statement carries the argument ("Survivability over a longer window is the conjunction of survivability over the shorter…"). Unmarked, not missing. |
| U5 `scale-cor:hamming` | **PROVED.** The proof is *inside* the statement body ("(ii) forces the pair average to reach 5 while (i) caps it at 2(4−h)…"). Not a gap. |
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
The proposition is stated at L609–L630; the next claim environment is at L666.
Between them there is only a `\subsection` heading. **No proof of any
convention.**

This matters out of proportion to its size because of what the paper says about
it. §1.2 Contributions (L160):

> "Five obstruction mechanisms are developed, **each with a complete proof**,
> and a sixth is exhibited under a policy-class restriction"

The selector principle is one of the five. The complete proof exists — it is
`\noindent\textbf{Complete proof of the selector principle (main text,
Section 8).}` in the v51 supplement (§6), and is not in v63.

---

## 5. Instrument error — recorded because it is the tenth of its class

`proof_audit.py` counted only `\begin{proof}` environments and reported units 1
and 7 as having **zero proofs** against 21 and 16 claims. That reading is
wrong. Both units write proofs as inline `\emph{Proof.}` /
`\emph{Proof sketch.}` paragraphs with no environment at all: unit 1 has 20
such markers and unit 7 has 19. Units 2, 8 and 11 use real environments.

The first reading would have produced a badly false report — "37 theorems with
no proofs" — from a stylistic difference. It was caught by reading the file
rather than trusting the count. `proof_audit.py` is superseded by
`proof_audit2.py`; both are kept, and this section records why.

Two further false-positive modes in the corrected instrument, both found by
context-checking: **deferred proofs** (proof placed after the next claim
environment) and **embedded proofs** (argument inside the statement body).
Neither is a defect.

---

## 6. Finding B — 75 pointers to supplements that do not exist

### 6.1 What each unit points at and whether it was ever written

| Unit | pointers | sections cited | did the supplement ever exist? |
|---|---:|---|---|
| 1 | 17 | S1, S2, S3, Figure~S1, Figure~S2 | **Yes — and it was dropped.** `paper2_obstruction_calculus_v{40..51}_Automatica_routes_supplementary.tex` exist on the branch (v51 is 85,563 B). **v52 and every later version has no supplementary file.** The in-text pointers survived the deletion. |
| 6 | 3 | S8, S9, S10 | No. No supplementary file for this paper anywhere in 7,240 branch paths. |
| 7 | 44 | S1, S2.3, S4, S5, S6, S8, S9, S9.1, S9.2, S9.5, S10, S11, S12, S13.1, S13.2, S13.3 | No. 114 matching branch paths, none supplementary. |
| 9 | 11 | S2, S2.1, S5, S5.4, S14, S17 | No. 3 matching branch paths, none supplementary. |

Unit 1's case is a **regression** — content existed and was lost. Units 6, 7
and 9 are **unkept promises** — the material was never written in any form.

### 6.2 Unit 1's supplement is recoverable

The v51 supplement is not merely similar to what v63 needs; it covers exactly
the same claims.

- v51 main text and v63 contain **identical** sets of 21 claims, compared by
  (environment type, statement name). Zero added, zero dropped between v51 and
  v63.
- v51 supplement structure: `S1. Complete proofs` (L28–799), `S2. The
  sufficiency landscape (full)`, `S3. Bounded constructions and scope remarks`,
  `S4. Additional figures`, plus an auxiliary definitions section.
- S1 contains the complete proofs v63 defers to, including
  `thm:finite-horizon`, `thm:exit`, and
  `Complete proof of the selector principle` (L443).
- S4 contains **Figure~S1** (`fig_p2_ladder.png`) and **Figure~S2**
  (`fig_p2_obstruction_tree.png`) — precisely the two supplementary figures
  v63 cites.
- v51 supplement carries 25 `\label`s; 19 of 25 match v63's names once the
  `calc-` prefix is stripped. The 6 that do not are the supplement's own
  internal figures, table and appendix heading.

**The only adaptation required is a mechanical label rewrite** (`thm:` →
`calc-thm:`, `prop:` → `calc-prop:`, `fig:` → `calc-fig:`, etc.), plus
reconciling the supplement's preamble to v63's title and abstract.

### 6.3 Why this is severe under the ratified target

The standard is unchanged and the safety net is gone: under preprints no one
performs error detection, scope moderation or prior-art screening but us, there
is no revision round, and publication is irreversible. A reader who checks
Theorem (finite-horizon completeness) finds "Proof sketch", then a pointer to
S1, then nothing. Forty-four such pointers in unit 7 make the paper
unverifiable at exactly the points where it invites verification.

---

## 7. Remediation options

**Unit 1** — one clean option: recover `v51_Automatica_routes_supplementary.tex`,
rewrite labels to the `calc-` namespace, attach as the supplementary file.
Resolves 17 pointers and Finding A together.

**Units 6, 7, 9** — 58 pointers, no source material. Options:
1. **Strip** the pointers and fold any load-bearing content into the main text
   or an appendix. Honest and cheap; loses nothing that exists, but the papers
   get shorter where they currently promise supporting detail.
2. **Write** the supplements. Feasible only where the content is reconstructable
   from the computation (`comp/`); unit 7's S1–S13.3 apparatus is large and its
   intended content is not documented anywhere.
3. **Leave and disclose** — state in each paper that the supplement is
   forthcoming. Not compatible with an irreversible first posting.

Pending decision; nothing has been edited.

---

## 8. Limitations

- Structural only. This audit checks that a proof is *evidenced*, not that it
  is *correct*. No theorem here has been verified by reading its argument.
- The claim scan is confined to `theorem`/`proposition`/`lemma`/`corollary`
  environments. Units 6, 9 and 10 number results inline
  ("Definition 47, Lemma 4, Proposition 43, Theorem 24"), so their results are
  not counted in the claim totals. Unit 9's inline results do not appear in
  the 0-claim row.
- Supplement-pointer matching is regex-based on `S<n>` forms. A pointer written
  some other way would be missed, so **75 is a lower bound.**
- "Informal" verdicts in §3 reflect the presence of a computation or worked
  instance, not an assessment of whether it suffices.
- Compilation remains unverified; no TeX engine is available and all checks
  are static.

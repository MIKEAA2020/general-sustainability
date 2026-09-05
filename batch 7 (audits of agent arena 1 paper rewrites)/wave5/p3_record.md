# Wave-5 P3 record — paper3_material_ledgers_v29.md (from v28) + supplementary S6 append

**Task ID:** 75-c. **Directive:** owner gate opened — re-evaluate the registered
follow-ups; re-open what is now worth doing.

## The verified finding (the statement-numbering confusion)

The v28 theorem demotions were status relabels on the unchanged 1–20 counter,
and **five of them landed on the "Proposition" type-word** (Theorems 4, 6, 17,
18, 20 → Propositions 4, 6, 17, 18, 20). But the paper already carried a
separate two-item proposition stream — the layering Propositions 1–2 of §3.1
("conservation consistency implies accounting consistency"; "barrier safety
does not follow from accounting consistency"). The propositions therefore now
read **1, 2, 4, 6, 17, 18, 20**: every label is unique and resolves directly
(verified: each "Proposition N" token has exactly one target), but the ordinal
expectation is broken and nothing in the paper declared the convention. Worse,
the supplementary's S4 statement inventory still lists the eight statements
under their pre-v28 status words (Theorems 2, 3, 4, 6, 17, 18, 20; Lemma 16),
with the offset recorded only in the main-text version log — a
supplementary-side reader had no fence (unlike P1, whose one S7 token is
fenced by the S8 preamble inside the supplementary itself).

## The controlled fix (declaration, not re-letter)

A re-letter was considered and declined on verification: renumbering the
layering propositions (e.g. to "Claim 1/2") would be an un-adjudicated status
change on two proved statements, and renumbering the demoted items would break
the number resolution with the supplementary that the relabels were chosen to
preserve. The controlled measure is the declaration:

| Item | Disposition | Evidence |
|---|---|---|
| §3.1 numbering note (the site where the two counters first meet) | **IMPLEMENTED** | v29 L245: "(Numbering note: the two layering propositions of this section carry their own counter, Propositions 1–2; every other numbered statement of this article runs on the single 1–20 sequence counter, whose status words reflect the audited demotions — 'Proposition 4', 'Proposition 6', 'Proposition 17', 'Proposition 18', and 'Proposition 20' are the demoted Theorems 4, 6, 17, 18, and 20, not further members of the layering counter — so every label is unique and resolves directly; the supplementary's statement inventory and this offset are reconciled in its S6.)" |
| Supplementary S6 (the ONE allowed append this wave) | **IMPLEMENTED** | `paper3_supplementary_v7.md` +43 lines, 0 deletions (git-verified append-only): "S6. Statement-Status Naming Offset (Appended at Main-Text v29)" — the eight-row old-label→new-label table (Theorem 2→Remark 2, Theorem 3→Lemma 3, Theorem 4→Proposition 4, Theorem 6→Proposition 6, Lemma 16→Remark 16, Theorem 17→Proposition 17, Theorem 18→Proposition 18, Theorem 20→Proposition 20), the unchanged-label statement, and the two-counter declaration. |
| Main-text supplementary pointer names S6 | **IMPLEMENTED** | v29 L884: "…the statement inventory with the status of every statement in the main text … — read with the S6 statement-status naming offset, which maps this file's pre-v28 status words to the main text's demotion relabels; and the fisheries cohort record…" |

## Build and verification

- `apply_batch7_wave5_p3.py` (fail-loud: two asserted-once sub1 anchors + the
  version-log splice + the idempotent S6 append). Ran clean twice: v29 MD5
  **b778d6f0c53f36a51a80d80a5e6bdc61** both runs; the second run verifies S6
  byte-identical and never re-appends. Diff = exactly 3 hunks (L3 version log,
  L245 numbering note, L884 pointer).
- Mechanical checks: the eight old status-word headers absent from the body;
  the demotion labels' body counts pinned at v28 values (Remark 2 ×3, Lemma 3
  ×8, Proposition 4 ×5+1, Proposition 6 ×1+1, Remark 16 ×2, Proposition 17
  ×2+1, Proposition 18 ×2+1, Proposition 20 ×1+1 — the +1s are the numbering
  note's own mentions); layering Propositions 1–2 untouched; frozen needles
  (exhaustion-horizon, ρ_P, 74,000,000, 0.535, κ_A K − γ_U U, MCS 2026)
  unchanged.

## Still behind the gate (reasons re-verified, still valid)

- **The 21k→12k length remainder** — restructure-level cuts would remove
  content the auditors called the publishable core.
- **The per-row USGS re-pin** — requires the per-country MCS 2026 reserve
  table (external data not in this repo).

## Non-destructiveness

No statement, proof, table row, recorded value, or verdict changes; the
supplementary edit is append-only (43 insertions, 0 deletions, git-verified).

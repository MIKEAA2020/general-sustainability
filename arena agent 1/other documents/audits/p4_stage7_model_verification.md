# P4 §7 Model-Label Verification and Correction; orchard/hen/elevator Attachment Evaluation (2026-09-04)

Two-part turn. (A) The owner asked whether we made the mistake an external agent's trace
describes: that P4's §7 code system is a two-stage adult/juvenile structured stock and
§7.1's prose describes a different model. (B) The owner's attachment
`orchard, hen, elevator.txt` (previously unread) was evaluated.

## A. P4 §7 — verification against the recovered code (uploads)

**Evidence reviewed:** `stage_core.txt`, `stage_r_window.txt`, `stage_tau0_decomposition.txt`,
`stage_robust_check.txt`, `stage_decomp2.txt`, `stage_hopf.json`, `stage_decomp_results.md`
(2026-08-08), `readme.txt`, and the supplementary's S9 registration records.

### What the code actually implements (verified from the files)

Two distinct stage objects exist in the recovered material:

1. **The stage-analysis machinery** (`stage_r_window.py` + `stage_tau0_decomposition.py` +
   `stage_robust_check.py` + `stage_decomp2.py`; readme: "the stage analysis was done with
   [these]"): the delayed-recruitment (stage-lumped, Gurney–Blythe–Nisbet) plant
   dN/dt = r·N(t−g)(1 − N(t−g)/K) − qEN, with **g = maturation delay** in the stock and the
   deficit signal, and **τ = institutional delay** entering only the effort equation through
   the delayed memory Z(t−τ); effort law with the multiplicative saturation gate
   (1 − E/Emax) and the **effort-response coefficient η**. Its recorded results file
   (`stage_decomp_results.md`) carries: g=0 validation windows (0.00796, 0.0219) at η=0.914
   and (0.00676, 0.0603) at η=3.0; the four fine-map bands g=1: 1.565–1.585, g=2: 0.77–0.81,
   g=3: 0.50–0.55, g=5: 0.28–0.33 on the locus r·g ≈ 1.5–1.6; the nonlinear ground truth
   358.8-yr (r=0.02, g=5), ~20-yr (r=0.5, g=5), 16.96-yr (r=0.3, g=5, τ=10; τ=21 stable),
   4.0-yr (r=1.57, g=1, τ=2.5) and 8.04-yr (r=0.8, g=2, τ=5.5) cycles.

2. **`stage_core.py`** — a *separate* 4-state adult/juvenile model (XA, XJ, Z, E), g =
   juvenile→adult stage duration, birth P0·XA·exp(−XA/Nc)·s, harvest adult-take or
   juvenile-take; outputs (stage_hopf.json): adult-take Hopfs 52.07/321.43 (g=5),
   16.76/121.80 (g=1), 31.66/200.88 (g=2); juvenile-take none.

### Verdict on the pasted finding — claim by claim

| Claim in the external trace | Verified verdict |
|---|---|
| "§7's numbers don't reproduce from the code (which gives 52/321, 269-yr periods)" | **Not applicable to the §7 records.** Those numbers are `stage_core.py`'s outputs. Every §7.2–7.4 number in P4 v14 matches `stage_decomp_results.md` (the recorded stage-analysis results) and the S9 fine-map table, and §7.4's re-run values (358.7 / 20.1 / 16.95 / 4.00 / 8.05) come from our earlier re-execution of the recovered GBN machinery. The numbers are NOT phantom. |
| "The code implements the two-stage adult/juvenile model; §7.1 describes a different model" | **Half-right, as applied to us.** The registered §7 machinery (readme + results file) is the GBN delayed-recruitment plant, not stage_core. So the model family in our §7 is the right one. **But §7.1–7.3's prose scrambles the parameter roles**, which is the mistake the finding is picking up: "gate strength g" (no such parameter — the gate is the multiplicative (1−E/Emax)); "social-weight coefficient η" (η is the effort-response coefficient); the maturation lag called τ and the gate g (the code's maturation delay is g, the institutional delay is τ); "at g=0 the institutional channel is switched off" (g=0 switches off the maturation delay; the base-core validation). |
| "η=3.0 contradiction" | None in our prose: §7.2's η=3.0 row is the g=0 two-delay validation window; §7.3's "absence of institutional τ=0-stable cells at η=3.0" is the band-cell statement — distinct tests, both traceable (S9.2 documents the rejected fine-map cell at g=5, η=3.0, r≈1.54–1.60, root +0.2445). |
| "§11.5(vi) contradiction" | **True and fixed:** v14's (vi) said "stage structure … outside the analysed class" while §7 exists. |
| "Rebuild §7 around stage_core (adult vs juvenile take)" | **Not adopted.** stage_core is a separate object whose records are not the registered §7 campaign; adopting it would orphan the verified GBN records (which the trace itself admits don't reproduce from stage_core). The correct fix is the label correction on the true provenance. stage_core's adult-vs-juvenile result is noted as a separate available object, not merged into §7. |

### Fixes issued — P4 v15 (five assert-counted edits)

1. §7.1 rewritten: the GBN plant stated explicitly (ġN = r·N(t−g)(1−N(t−g)/K) − qEN),
   g = maturation delay, deficit signal qEN − r·N(t−g)(1−N(t−g)/K), multiplicative gate
   (1−E/Emax), η = effort-response coefficient, τ = institutional delay entering only the
   effort equation; switches corrected (g=0 → scalar logistic core, the base-core
   validation; τ=0 → undelayed-institutional stage plant).
2. §7.2: "g=0 (institutional channel off)" → "(maturation delay off)"; "the window widens
   with the social weight" → "with the effort response η".
3. §7.3: "Stronger gate strength moves the band…" → "Longer maturation delay moves the
   band to lower recruitment rates — the recorded bands sit on the locus r·g ≈ 1.5–1.6…".
4. §7.4: the bracketed window named correctly — institutional-delay window (the cycle at
   τ=10 vs stable at τ=21 is the τ-window), not "maturation-delay window".
5. §11.5(vi): scoped — the core's ecological subsystem is scalar logistic; §7 is the
   registered stage-structured analogue; spatial structure and multispecies interactions
   remain outside; the GBN/Costantino citations supply §7's model class (both references
   already in the list — Gurney, Blythe, and Nisbet 1980; Costantino et al. 1995).

Supplementary unchanged: S9.2 already documents the fine-map caveat cell correctly.
§9.6's "maturation times g ≈ 1, 2, 5 yr (anchovy/sprat/cod)" was already consistent and
now agrees with §7. **Answer to "have we made a mistake?": yes — the §7.1–7.3 labels and
the §11.5(vi) scope; no — the model family and every number were correct and traceable.
Both defects are corrected in P4 v15.**

## B. The orchard/hen/elevator attachment — read and evaluated

The file is the source dialogue behind the three restored analogies. Alignment check
against the papers: **P1 v10** carries the hen+orchard masking picture (a healthy hen or
full orchard while the pond behind is drained — the compensatory productivity illusion);
**P4 v14/15** carries the hen as the single-asset overshoot loop (eggs = flow, slaughter =
stock liquidation, with the channel distinction adult cull vs recruitment suppression);
**P3 v16/17** carries the elevator (rated 10, holds 14, invisible wear, sudden snap — the
yield-inflation channel). The attachment's one refinement not yet used anywhere: the
rope-only reading — reversible elastic cycling within the endurance limit is the *flow*,
fatigue life plus strand integrity are the *capital*, so the flow/stock split is not
between the living and the nonliving but between using the yield and consuming the
structure that generates it. **Added to P3 v17** as one sentence in the §1.1 elevator
paragraph. The attachment's remaining content (the "absence of immediate failure is not
evidence of safety" point, the lagging-indicator reading) is already present in P3's
elevator paragraph and P1's masking paragraph; nothing further was missing.

## Files issued this turn

| New version | Built from | Changes |
|---|---|---|
| `paper4_delay_dynamics_v15.md` | v14 | §7.1–7.4 corrected labels/roles; §11.5(vi) scoped (5 edits) |
| `paper3_material_ledgers_v17.md` | v16 | rope/integrity sentence in the elevator paragraph (1 edit) |

Prior versions untouched; supplementary files unchanged (S9.2 verified correct).

## Postscript — owner correction (2026-09-04)

The rope addition of §B above is **withdrawn on the owner's direction**: the
"flow/stock split is not about life" thread is a strawman the source dialogue's AI
introduced and then argued against — chat-level meta-commentary with no place in a
journal article. The elevator paragraph's scientific payload is the invisible-wear /
sudden-snap asymmetry, which the paragraph states without the rope sentence.
**Applied:** `paper3_material_ledgers_v17_corrected.md` = v17 with the single rope
sentence removed (v17 itself left untouched per the never-overwrite rule; the live
chain v18–v26 verified already clean of the sentence).

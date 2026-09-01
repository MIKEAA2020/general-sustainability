# Clarity, Flow, Remnants, and Redundancy Scan (Turn 52)

**Scope.** Each final version scanned for (a) structural-numbering consistency and flow, (b) leftover artifacts ("remnants"), and (c) internal redundancy. Versions scanned: the turn-51 finals (P1 v7, P2 v4, P3 v7, P4 v8, P5 v8, E1 v6, E2 v9, E3 v6, E4 v7); fixes issued as the next versioned files (P1 v8, P3 v8, P4 v9, P5 v9, E2 v10, E3 v7, E4 v8).

## Findings

### 1. P4 — subsection numbering desynchronized from section headers (defect, fixed in v9)
The turn-50 renumbering (new Section 7 inserted; old §§7–11 → 8–12) renumbered the top-level headers and the "Section N" cross-references, but **not the subsection headers**: "### 8.1 … 8.6" sat under "## 9. Global Numerics", "### 9.1 … 9.4" under "## 10. The Loop-Gain Family", and "### 10.1 … 10.6" under "## 11. Discussion". A reader navigating §9 finds subsections labelled 8.x — a genuine internal-numbering break. **P4 v9** renumbers the 16 subsection headers (8.x→9.x, 9.x→10.x, 10.x→11.x). All "Section N.x" textual references were already correct (verified: zero "Section 8.x" remain; the "Section 9.4/9.5/9.6/10.2/10.5" references resolve to the renumbered targets). This defect had been pushed in v6–v8; v9 supersedes.

### 2. E2 — caption remnants (fixed in v10)
Figure captions carried repository filenames inside the caption text ("(`fig1_surplus.png`)"), inconsistent with the E1/E3 convention (clean captions + image embeds). Figures 5 and 6 additionally lacked caption blocks (inline mentions only). **E2 v10**: filename parentheticals removed; all six committed PNGs embedded as image links; Figures 5 and 6 received proper caption blocks. The filenames remain as the on-disk/GitHub file names, preserving provenance.

### 3. E3 — trailing "--" abstract remnant (fixed in v7)
The abstract ended with a dangling "--" (an editing residue). Removed by the structured-abstract conversion in **E3 v7** (the same residue had been fixed in P5's abstract rewrite in turn 51).

### 4. Duplicate-sentence sweep — all judged legitimate (no action)
Automated near-duplicate detection across all nine papers flagged five repeated passages. Each was inspected: they are statement/proof pairs or front-matter/body echoes, not redundancy defects:
- P4: "Rigorous saddle-node results for delay equations exist…" (Contributions list + §11.3 certification levels — a deliberate scoping echo); "Between reviews the variational system is…" and "The sampled equilibrium is exponentially stable iff…" (Theorem 5 statement + its proof/companion proposition contexts).
- P1: "We do not assert priority…" (§1.3 + §5.2 novelty qualification — the second occurrence is the qualified form).
- P5: "The displayed values are rounded renderings of the assessment table…" (§2.7 methods declaration + §3.8 results detail with added underlying values).
- E1: table-header repetition (table artifact, not text).

### 5. Organization paragraphs — verified accurate
P2 §1.4, P3 §1.3, and P4 §1.3 organization paragraphs checked against the actual section headers: all match (P4's was rewritten in v6 and correctly describes the renumbered structure including the new Section 7).

### 6. Flow verdicts
- P1–P3: sequential theorem development with no broken cross-references found (all "Section N"/"Theorem N" references resolve; the reference-integrity scan of turn 51 remains clean).
- P4: after the v9 numbering fix, the only structural irregularity is the known §4-without-subsections pattern (deliberate: "## 4. The Complete Hopf Cubic" carries a single subsection 4.1; unchanged from v1 by design).
- E1–E4: methods→results→discussion ladders intact; the E3/E4 structured abstracts (v7/v8) now carry the four-headed Groundwater structure, and their Results sections open with the same headlines as the abstracts (verified word-level for all abstract numbers).

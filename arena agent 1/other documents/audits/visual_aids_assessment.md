# Visual-Aids Assessment (Turn 52)

**Question.** For each of the nine papers, does it merit additional non-decorative, non-superficial tables, figures, or visual aids?

**Criterion.** An aid is merited only if (i) it visualizes a load-bearing result that is currently buried in prose, (ii) its data is fully backed by committed computations or by the paper's own displayed numbers, and (iii) it is idiomatic for the target venue. Decorative repetition of existing tables was excluded.

## Verdicts and actions

| Paper | Existing aids | Verdict | Action |
|---|---|---|---|
| **P1** (SVAA) | 1 figure described in text (no image), 1 table | **Merited — implemented.** §4.7's "Figure 1" was a full geometric caption with no rendered image. The witness geometry is exactly specified (square $[0,2]^2$, region $s_1+s_2\ge 2$ minus legs, witness $(6/5,6/5)$, threshold curves $\rho_1,\rho_2$ with the analytic forms of Theorem 5's proof), so a faithful two-panel rendering was generated from that specification. | `figs_p1/fig1_witness.png`, embedded in **P1 v8** |
| **P2** (SVAA) | none | **Not merited.** A pure theorem paper with six results organized by section and an enumerating abstract; SVAA exemplars are figure-free. A lookup table of certificates would be decorative. | none |
| **P3** (EE) | multiple tables | **Not merited.** Already table-rich (ledger tables, classification tables, split-assignment table). A Sankey-style flow diagram would re-present the ledger equations decoratively. | none |
| **P4** (EM) | parameter table + registration tables | **Merited but data-gated.** The five-regime attractor topology (§9.2) is the paper's headline global result and currently lives in dense prose. A regime diagram requires the continuation/Floquet/basin data — **inherited corpus content from the original authoring** (`papers/paper4_delay_dynamics/manuscript.md`, repo Task 52 2026-08-28; `uploads/paper4_final.md`), whose fold-status discipline declares the publication-artifact archives an open obligation; no attractor CSVs exist in the workspace or the repo (verified turn 53 by full-tree + full-history scan). Generating it now would require a full pre-registered recomputation campaign. Recorded as a prospective campaign; nothing fabricated. | future campaign (pre-registered), then a new P4 version |
| **P5** (ICES JMS) | multiple tables | **Merited — implemented.** The crossing record (`p5_crossing_record.csv`, committed) visualizes the paper's central operator contrast: four update pairs, stable/unstable ranges, crossing markers. | `figs_p5/fig1_crossing_record.png`, embedded in **P5 v9** |
| **E1** (Fisheries Research) | 4 figures with images | **Already complete.** | none |
| **E2** (Fisheries Research) | 6 figures referenced; PNGs existed but were not wired into the manuscript, and captions carried filename parentheticals | **Merited — implemented.** The six committed figures (`fig1_surplus`…`fig6_k_sensitivity`) are now embedded as image links with clean captions (E1/E3 convention); the repo-filename parentheticals removed from caption text. | **E2 v10** with `figs_e2/` |
| **E3** (Groundwater) | 5 figures with images | **Already complete.** | none |
| **E4** (Groundwater) | 2 tables, no figures | **Merited — implemented.** The worst-case-attractor ladder (Table 1) is the core §3.1 result; a bar figure shows at a glance that BAU's attractor (615.72 ft) sits below the 618-ft threshold while every cut policy clears it. Data: `e4_floor_supply.csv` (committed) — BAU 615.72, flat-90% 618.88, flat-80% 622.04, S1 622.04, flat-70% 625.20, flat-60% 628.36, CPM 628.36, flat-50% 631.52, flat-0% 647.32. | `figs_e4/fig1_attractors.png`, embedded in **E4 v8** |

## Non-decorative discipline applied

- Every implemented figure is drawn from committed CSVs or from the paper's own displayed analytic specification; no new computation, no invented data.
- The P4 topology figure is explicitly deferred (data-gated) rather than approximated schematically — a schematic regime map risks misrepresenting the provisional saddle-node/crisis classification, which the paper itself leaves open.
- No table was duplicated; existing tables were left untouched.

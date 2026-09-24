# Worked-Systems Audit, Edition 2 — Addendum (formal-register revision)

**Edition:** `paper2_worked_systems_v2` (tex + pdf + verification + this record). **Base:** edition 1 (retained unmodified). **Scope:** register repair per the owner's editorial directive — the manuscript is restated as a journal article presenting findings; internal project narration is removed; references are restricted to published works and the submitted theory paper. **No scientific content changed.**

## 1. Removed (register repair)

- Project narration: "the programme's worked-systems flagship", "this paper is that home", "the consolidation decision", the consolidation-registry table, "source edition:" pointers, absorbed/retained/superseded language, lineage and roadmap references.
- Phantom references: the companion lettering (Abaee 2026a–i) that pointed to unpublished internal manuscripts is gone. The reference list now carries two entries: Abaee 2026a (Zenodo 10.5281/zenodo.22552060, the applied source of the audit system) and Abaee 2026b (the obstruction calculus, submitted).
- Over-hedging: none found of the metaphor-apology type; the three coincidence statements are retained deliberately — they are legitimate scope statements (each marks a numerical agreement under which no identity is claimed: the 16/256 sustaining laws against the 16 lost pairs; the mode-blind 28 against the full-information 28).
- Verification-wording: "crown jewels" and similar informal terms removed from the verification script's documentation; the script's three layers (chain, recomputation, text) are unchanged in substance.

## 2. Content-parity audit (edition 1 → edition 2; nothing lost)

| Scientific fact | Edition 1 location | Edition 2 location |
|---|---|---|
| Delay identity, 48 cells, zero mismatches; strict form fails exactly at (2,1); σ* = ⌊z0−1⌋, level sets {z0 ≥ 1+k} | §3 | §3 |
| Adequacy census: 15 partitions, 7 adequate, two minimal 2-cell; maximal common-action sets overlap in (2,2); no coarsest design; pairwise necessary-not-sufficient | §3 (C2), §5 | §4 |
| Four-cell kernels 24/26/25/28; incomparable middles with witness pairs; meet = institutional setwise; join = top 28 = C(8,2); corner singleton nonviable; C(9,2)=36 | §3 (C3), §6.2 | §5 |
| Decentralized: 256 = 2⁴×2⁴ laws; kernel 12; 16 lost; 16 sustain (coincidence); authority restriction 12→0; loss instance {(1,2),(3,1)}; deadlock transition declared; local memory (delayed own reading), not common knowledge | §3 (C4), §6.4 | §6 |
| Regimes: frozen 36 = 36 (corner viable); mode-blind 28, singleton-generated loss; causal timing (adversary's end-of-step choice); setwise agreement coincidental | §3 (C5), §6.3 | §7 |
| Benchmark: caps 3/2−(Y−2)/10, 59/50−(Y−2)/10; Y* = 27/5 at cap sum 2; Y=5 witness (6/5,4/5); Y=6 sum 47/25, dual (1/2,1/2), margin 3/50; fibre width Y−4 | §3 (C8) | §8 |
| Static duality: −1/10 two-floor; λ=(1/2,1/2) normalized Farkas; convexity gap (−1 vs 0); Helly-tight triple (m+1=3); weak/strong scoping | §4 | §8 |
| CE drift: uncorrected ≥ 21/100 on [1,2]; corrected identically 0 | §3 (C6), §5 | §2, §10 |
| Multiple floors: joint Farkas obstruction; minimal infeasible subsystem with witnesses; corner dynamic nonviability; first-breach bound and corner-cone reading recorded | §6.1 | §9 |
| Design rules (timing boundary-inclusive; fibre split; certainly-safe reporting; structural bias repair) | §5, §7 | §4, §10 |

## 3. Verification and build

`paper2_worked_systems_v2_verification.py`: 16/16 — chain (seven per-system scripts, 57/57), independent recomputation of the headline identities, and text needles for every number above. Build: 3 pages two-column, zero errors, zero overfull (the four-term kernel display split via `gather*`).

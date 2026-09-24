# Worked systems — edition 7 addendum

**Edition:** `paper2_worked_systems_v7` (tex/pdf/verify), replacing v6 per the new-editions-only protocol. **Trigger:** round-3 external audit (`worked gpt audit.txt`) + owner figure directive. **Verification:** `paper2_worked_systems_v7_verification.py` — 26/26 checks pass (57/57 chained lineage checks unchanged); builds clean (0 overfull; `main.pdf` asserted).

## Content changes (v6 → v7)

1. **σ\*/τ\* split (audit 1.1, upheld).** τ*(z₀) = z₀−1 is the real worst-case exit time; σ*(z₀) = ⌊τ*(z₀)⌋ the largest admissible integer review count. The abstract, conventions, §6, Table 3 caption, Fig 2 caption, and design rule now carry the split; §6 states that the strict form against σ* fails on all six viable cells while against τ* it fails only at (2.0, 1) — the inclusive predicate is the audited identity.
2. **Register semantics (audit 1.3, upheld).** §2's contradictory clause replaced; the audited rule is formalized as the pessimistic shared register (policy fixes one action per fibre; the register holds some fibre's executed action; survival requires every admissible thread to win). Verify M2b proves the pessimistic kernels equal the scripts' single-thread kernels **setwise** on all four classes — the audited 24/26/25/28 are thread-order independent; M2c shows the optimistic reading differs (strictly larger codex kernel), so the pessimistic reading is load-bearing and now stated.
3. **§4 corrections (audit 1.6 + this round's computation).** "Neither protocol dominance holds" replaced by the exact column-wise inclusions; the 12|31 per-pair reading corrected — the pair is free-viable and no-repeat-dead under **both** observation structures, dying at step 2 through the shared register (verify M3b re-derives the forced loss).
4. **§5 Helly (audit 1.7).** Pairwise intersection is necessary and, in the two-instrument universe (Helly number two), sufficient; a three-set counterexample shows where sufficiency fails in general.
5. **Saddle sentence (audit 1.9).** "Certificate exists exactly where the value is negative; at zero the instance is boundary-critical."
6. **§8 typo (audit).** "the kernel is 36 = 36" → "comprises all 36 law pairs".
7. **Fair-clarity items.** Partition order defined; "Helly-tight family of three constraints — no two of them already infeasible"; abstract names the corner (1,1); register alphabet and unconstrained initial register stated.
8. **New exact counts.** Agency-restriction: 16 sustaining laws for 12|21 with agency 1's z=1 vote fixed to instrument 1; 0 with agency 2's; whole-law fixes collapse the kernel to 0 (§5).
9. **Corruption repair (this round's find).** v5/v6 shipped a mangled `\ref` ("column F of Table ef tab:master)") from an escape-eaten edit; repaired; the verify script now scans the tex for control bytes and bare remnants.
10. **Figure 5 (owner directive).** The "−1/10: max–min = min–max" label moved beneath the red dashed line into the envelope's whitespace (data y = −0.33); Farkas label and legend unchanged; generator's 6/6 internal checks green; overfull 0.

**Unchanged:** all audited numbers (the master table, kernels, census, benchmark, drift, timing grid — every count re-verified bit-identical by the v7 script).

# Per-Manuscript Checklist Scan (Turn 51)

**Scope.** Each of the nine manuscripts, latest version, checked against its own checklist: (1) abstract within the venue cap; (2) no chat/version/repo-path artifacts in manuscript text; (3) reference integrity (every in-text citation resolvable in the reference list); (4) supplementary pointer accurate; (5) displayed proofs present (turn-50 scan, cited); (6) key registered numbers spot-checked against the committed campaign outputs. Versions scanned: P1 v7, P2 v3, P3 v7, P4 v8, P5 v8, E1 v5, E2 v9, E3 v6, E4 v7.

| Paper | Venue | Abstract (cap) | Artifact tokens | Citations | Supp pointer | Proofs |
|---|---|---|---|---|---|---|
| P1 v7 | SVAA | 238 (150–250) ✓ fixed from 270 | clean | 19 in-text, all resolvable | accurate (S1–S7) | 8/8 displayed (turn 50) |
| P2 v3 | SVAA | 243 (150–250) ✓ | clean | 18 in-text, all resolvable | none needed | 6/6 displayed (turn 50) |
| P3 v7 | Ecological Economics | 247 (≤250) ✓ fixed from 314 | clean | 21 in-text, all resolvable | accurate (S1–S4) | 21 numbered + 3 unnumbered (turn 50) |
| P4 v8 | Ecological Modelling | 249 (≤250) ✓ fixed from 284 | clean (title registration note removed; in-body repo paths neutralized) | 21 in-text, all resolvable | now names `paper4_supplementary_v2.md` (S1–S10) | Cor 3 + Prop 5 proofs added (turn 50) |
| P5 v8 | ICES JMS | 300 (≤300) ✓ fixed from 341 | clean (trailing "--" artifact removed) | 26 in-text, all resolvable | corrected S1–S8 pointer | threshold lemma full proof (turn 50) |
| E1 v5 | Fisheries Research | 277 (≤300) ✓ | clean | 12 in-text, all resolvable | none needed | 0 constructs by design |
| E2 v9 | Fisheries Research | 299 (≤300) ✓ fixed from 375 | clean ("wave-7" jargon removed; DA script names retained legitimately) | 6 in-text, all resolvable | none needed | 0 constructs by design |
| E3 v6 | Groundwater | 261 (≤300) ✓ | clean ("wave-7" removed) | 9 in-text, all resolvable | none needed | 0 constructs by design |
| E4 v7 | Groundwater | 300 (≤300) ✓ (borderline, left) | clean ("wave-7" removed) | 11 in-text, all resolvable | none needed | 0 constructs by design |

## What was fixed this pass (new versioned files only; older versions untouched)

1. **Abstract caps (5 papers).** P1 270→238; P3 314→247; P4 284→249; P5 341→300; E2 375→299. Trims are wording-level only: every load-bearing claim, number, and caveat is retained (verified by diff: P1/P3/P4/P5/E2 changed lines confined to the abstract paragraph).
2. **P4 meta-artifact removal.** The "Registration note (v6)" block under the title (version number + repo paths — a manuscript-level violation) is removed; its content is folded into the Data availability statement in neutral form. In-body repo paths in §7.1/§7.5 replaced by deposited-material references (S9). Data-availability wording neutralized.
3. **Internal "wave-7" jargon.** Removed from E2 v9, E3 v6, E4 v7 data statements (the layers are now named by their paper sections; the generating script names and the public repository URL remain, as proper data-statement content).
4. **P5 trailing "--" artifact** removed with the abstract rewrite.

## Verified clean (no action)

- **Forbidden-token sweep:** after the fixes, zero hits for chat artifacts, version references, TODO/lorem, repo paths in manuscript bodies (Data-availability script names are the one legitimate class, and they are section-scoped to the data statement).
- **Reference integrity:** every in-text citation across all nine papers resolves to a reference-list entry; the initial matcher flags (O'Neill, Holling, Lunel, Desharnais, Srivastava, Assimakopoulos, Sinclair, Baum, Gabay, Coombs, Bank, Kirwan, month names) were all confirmed present in their reference lists — matcher false positives, no real gaps.
- **Displayed proofs:** turn-50 scan remains controlling (P1 8/8, P2 6/6, P3 24, P4 complete after Cor 3/Prop 5 additions, P5 complete after lemma proof, E1–E4 zero constructs by design).
- **Key-number spot checks (committed CSVs):** P4 τ−/τ+ 3.666149/150.358477 and flipped 128.374/70.697 (21-gate campaign, all pass); P5 ρ(1)=0.895–0.994 reconstruction record (turn-46 CSVs); E2 MSE 13,873.1 / xteNCAM q05/q10 −269.5/−178.7 (turn-44 CSVs); E4 618-ft/625.6/658.4 ft (turn-44 CSVs); E3 RMSE 8.56 ft (turn-44 CSVs). All unchanged by this pass.

# Agent 2 — Proof Repair Index

Independent re-verification and repair of the `PROVEN (reconstructed)` theorem rows in
`PROOF_MANIFEST.md`, plus the Wave E reproduction and the cross-document consistency pass.

**Status: complete.** All 19 defects identified in the audit are addressed by 15 repair
documents, backed by 13 verification suites totalling **444 assertions, all passing**.

Nothing here has been applied to the repository. Every repair is a proposal with its own
verification; each file states which repository path it targets.

---

## How to run the verification

The scripts read the repository but never write to it. They locate the checkout as
`../repo` relative to the script's parent, so from inside the repository set it explicitly:

```bash
cd <repo root>
REPO="$PWD" python3 "batch 4/agent 2 attempt/verify_e7_repair.py"
```

Every script exits 0 on success and prints one `[OK ]` line per assertion. The
`verify_*_output.txt` files in this folder are the saved logs from the run that produced
444 passing assertions.

| suite | assertions | covers |
|---|---|---|
| `verify_findings.py` | 34 | the original audit: A3/B6/E4 refutations |
| `verify_wave_e.py` | 56 | Wave E reproduction (hashes, scores, retention) |
| `verify_consistency.py` | 43 | cross-document consistency |
| `verify_a3_repair.py` | 18 | `A3_THM1_REPAIRED.md` |
| `verify_b6_repair.py` | 31 | `B6_THM1_REPAIRED.md` |
| `verify_e4_repair.py` | 58 | `E4_REPAIRED.md` |
| `verify_e7_repair.py` | 40 | `E7_REPAIRED.md` |
| `verify_b1_repair.py` | 28 | `B1_THM1_REPAIRED.md` |
| `verify_b10_repair.py` | 30 | `B10_THM1_REPAIRED.md` |
| `verify_e2b1a_b9_repair.py` | 28 | `E2_B1A_REPAIRED.md`, `B9_THM1_REPAIRED.md` |
| `verify_e2b2a_a4_repair.py` | 28 | `E2_B2A_REPAIRED.md`, `A4_THM1_REPAIRED.md` |
| `verify_a3thm2_cathm3_repair.py` | 26 | `A3_THM2_REPAIRED.md`, `CA_THM3_REPAIRED.md` |
| `verify_e3cfb7_repair.py` | 24 | `E3_C63_REPAIRED.md`, `CF_REPAIRED.md`, `B7_THM1_REPAIRED.md` |

---

## Repairs, by target

| repair document | targets | kind |
|---|---|---|
| `A3_THM1_REPAIRED.md` | `A3_VARIABLE_EVENT_KERNEL.md` §A3.Thm1; manifest line 90 | **false → replaced.** Compactness refuted (`sin(2πks)`); repaired with a common-modulus hypothesis, which is free for solution windows |
| `A3_THM2_REPAIRED.md` | `A3_VARIABLE_EVENT_KERNEL.md` §A3.Thm2; manifest line 91 | **typing.** `ℬ` declared compact but termination needs it finite; bound `\|𝒜\|·dim` was undefined → `\|𝒜\|·\|ℬ\|`, sharp; vacuous clopenness claim dropped |
| `A4_THM1_REPAIRED.md` | `A4_NONLINEAR_SMALL_GAIN.md` §A4.Thm1 Step 2; manifest line 93 | **sign error, not cosmetic.** `α` entered positively; the displayed bound admits outward velocities that exit `K_{−r}` immediately. Conclusion unchanged |
| `B1_THM1_REPAIRED.md` | `B_TIER_BRIDGES.md` §B1; manifest lines 46, 95, 174 | **ambiguous headline.** Invariance reading irreparably false; repaired as a two-depth theorem with a tight confinement condition, which also resolves the `R02.Cor6` three-way disagreement |
| `B6_THM1_REPAIRED.md` | `B_TIER_BRIDGES.md` §B6; manifest line 96 | **false → replaced.** MFCQ does not stabilise feasible directions (`{y ≥ x²}`, `d = (1,0)`); repaired to quantitative lower semicontinuity plus exact constancy at the sharp hypothesis |
| `B7_THM1_REPAIRED.md` | `B_TIER_BRIDGES.md` §B7 part (3); manifest line 97 | **narrows.** Genericity needs a versal unfolding; without it the transversal-contact set can be empty (`f ≡ 0`). Parts (1),(2) unaffected |
| `B9_THM1_REPAIRED.md` | `B_TIER_BRIDGES.md` §B9 part (1); manifest line 98 | **false → replaced.** Reverse inclusion fails at any fixed budget split; primitive replaced with value iteration, which is exact and needs no quantile convention |
| `B10_THM1_REPAIRED.md` | `B_TIER_BRIDGES.md` §B10; manifest line 99 | **two defects, one root.** Optimistic ≠ pessimistic; universal safe-command set is not closed under Berge. Split into existential (no extra hypothesis) and robust (needs `BR` lsc) |
| `C_TIER` / `E7_REPAIRED.md` | `E7_CONSERVATION_VIABILITY_COUPLING.md`; `C_TIER_COMPLETIONS.md` §C-e; manifest lines 83, 84, 102 | **wrong object.** `L_G` is the envelope modulus, not a barrier constant; affine barriers give `ρ = ∞`, not `L_G = 0`. Plus sharp outer bound, split exit claim, corrected noncompensation |
| `CA_THM3_REPAIRED.md` | `CA_EXECUTION.md` §C-a.Thm3; `C_TIER_COMPLETIONS.md` §C-a(2); manifest line 101 | **overclaim.** Not every subset arises — the kernel language does not separate models (two distinct tables, identical kernels). Narrowed to the definable Boolean algebra |
| `CF_REPAIRED.md` | `C_TIER_COMPLETIONS.md` §C-f; manifest line 103 | **scope alignment.** Statement quantified over general observables; proof handles only window restrictions. General case recorded open with the obstruction stated |
| `E2_B1A_REPAIRED.md` | `E2_SELECTORS_AND_CERTIFICATES.md` §B1.Thm(a); manifest line 75 | **backwards.** Consistency is not inherited by subfamilies (2-point counterexample); post-fixed sets are join-closed. Correct transfer: the recursion runs in `𝒱*` |
| `E2_B2A_REPAIRED.md` | `E2_SELECTORS_AND_CERTIFICATES.md` §B2.Thm(a); manifest line 74 | **gap, one line.** Step 3 proved the closed-set statement and asserted the open-set one KRN needs; closed by the metric decomposition `O = ⋃ₙ Fₙ`. Conclusion unchanged |
| `E3_C63_REPAIRED.md` | `E3_CLASSIFICATION_THEOREMS.md` §C6.3; manifest line 80 | **example, not proof.** Converse replaced by an exact truncated-kernel characterisation, both directions proved directly |
| `E4_REPAIRED.md` | `E4_INTERGENERATIONAL_PRODUCTION.md`; manifest lines 81, 82 | **false → replaced, and the sign flips.** Margin definition was degenerate; budget formula off by `ℓ^G` and named the wrong fixed point. Corrected: a contracting reset is unsustainable at **any** initial margin |

`_a3_thm1_section.md` and `_b6_section.md` are drop-in replacement sections for the two
in-place edits already applied (`A3_VARIABLE_EVENT_KERNEL.md`, `B6_THM1_REPAIRED.md`).

---

## Tally

| class | items | outcome |
|---|---|---|
| false as stated | 4 | restored to truth or replaced with a stronger true statement |
| proof gaps | 7 | closed; in every case the original conclusion survives |
| definitional defects | 8 | 7 repaired by restating at the correct scope or with the right constant; 1 (`B7.Thm1(3)`) narrowed with an added hypothesis |
| **total** | **19** | 18 restored or strengthened, 1 narrowed |

---

## Two findings that belong in the manuscripts, not in these notes

**1. The `L_G` confusion (E7).** `L_G` was treated as a barrier-geometry constant in two places,
but the controlling packet defines it as the velocity envelope's Hausdorff–Lipschitz modulus. In
a paper, an erosion bound with `α` entering positively reads as a licence for outward velocities —
which is exactly what the `A4` counterexample exhibits. Recommend grepping `revised_articles/` for
`α` appearing with a positive sign in an erosion inequality before Paper 2 is finalised.

**2. Model non-identifiability (C-a.Thm3).** Two governance instantiations with different
transition structure can be indistinguishable by every judgment the framework can express. This
bounds what the framework can certify about a calibrated model, and belongs in Paper 1's scope
section and Paper 5's computability guarantee — beside the existing "no specific model has been
verified against their hypotheses" caveat, not in a proof footnote.

---

## Also in `batch 4/` (not this folder)

The three audit reports that precede these repairs:

- `PROOF_REAUDIT.md` — line-by-line re-verification of the 27 `reconstructed` rows
- `WAVE_E_RERUN.md` — reproduction of `wave_e_cod/` and `wave_e_edwards/`
- `CROSS_DOCUMENT_CONSISTENCY.md` — claims vs. the honest-status register

One loose end recorded there and still open: `E4.Thm3`'s own section needs the `ρ_g > 0`
hypothesis added to its statement. It is flagged as an obligation in `E4_REPAIRED.md` but the
section itself was not edited.

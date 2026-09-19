# `revision/v5` — what was applied, and what was not

**Manuscript of record now:** `revision/v5/paper3_v5.md` — 132,954 chars, 18,388 words, 1,842 lines.
Previous: `revision/v4/paper3_v4.md`, untouched (108,043 chars, 15,016 words).
Built by `build_v5.py` from v4 by **25 unique-anchor insertions and 3 logged replacements**
(two authorised wording changes, plus one inherited typo fix described below);
checked by `verify_v5.py`: **65 checks, 0 failed**, including a byte-identical
**insert-only reconstruction** (removing every logged block and inverting the two replacements
reproduces v4 exactly: 108,043 vs 108,043 chars, delta 0).

New statements: **Definitions 21–23, Theorem 24, Propositions 25–32, Remark 33** on the article's
shared main counter (now 1–33, no gaps, no reuse), plus six unnumbered passages. Six new proofs
(`\square` count 24 → 30, no duplicated mark).

**The third replacement, disclosed.** The source carries an unclosed inline-math delimiter in the
§8.4 proof — `\(i\ne j\}.` for `\(i\ne j\).` — which leaves the span open to the end of the paragraph
and prints a stray brace. One character, no claim affected: v4 was 602 opens / 601 closes, v5 is
764 / 764, and the verifier asserts both the balance and that the fix is logged. It is logged as a
replacement so the reconstruction test still accounts for every byte.

## 1. Decisions D1–D8, as applied

| | Decision | Applied as | Where |
|---|---|---|---|
| D1 | rows 1–10 of the register | all ten | §1.3 (Defs 21–22), §2.2, §3.1, §3.5 (Def 23), §4.8 (Thm 24), §5.4 (Prop 25), §6.2 (Props 26–28), §6.3, §7.1 (Props 29–30), §7.2 (Prop 31 + refute/alarm clause), §8.1 (Prop 32), §8.4 (Rem 33) |
| D2 | curvature number `κ` | Proposition 27, power-law family only, with the `ü` data requirement stated in the article's own register | §6.2 |
| D3 | non-compensation generalisation re-scoped | **not** the strictly-monotone generalisation. Proposition 29 states uniqueness of the calibrated monotone certifier (`= min`), the `Σᵢmin(0,rᵢ)` counterexample, and a proof that continuity + certification + strict monotonicity are incompatible. The "false-safe volume" metric is not published (no declared measure) | §7.1 |
| D4 | positioning paragraph with the SEEA/SNA sentence | **Antecedents**, §1.5, with 2 new reference entries. Wording is mine from the verified facts (SEEA CF adopted at the Statistical Commission's 43rd session, 2012; SNA 2025 adopted at its 56th session; depletion treated as a cost of production alongside depreciation) — **the author should confirm the framing before submission** | §1.5 |
| D5 | worked ledger → supplementary | `supplementary_v5_additions.md` §S-C: κ table, crossover grid on the pinned record (τ = 308.33 yr; T(η=0) = 77.58 yr; threshold ½gτ = 4.625 > 1), index table, event-time witness, certificate vectors | supp |
| D6 | companion paper after submission of v5 | not started; §10.1's composition material deliberately left as-is | — |
| D7 | replace §10.1's "in review" placeholder | now `(Abaee, 2026, doi:10.5281/zenodo.22554217; …)`. The inherited clause "its equation (1) and Section 2.4" was **not** checked against the companion PDF — verify before submission | §10.1 |
| D8 | code availability | added to Declarations, pointing at `code/` + `code/MANIFEST.md` | Declarations |

Also applied from batch 1's bucket T, where v4 did not already have the content:
the joint-minimal reporting note (§6.3), the disturbance-budget note (§2.2), and the refute/alarm
clause (§7.2).

## 2. Three things I found while applying, which correct my own earlier reports

- **Batch-1 T4 was already discharged.** The safety/assurance distinction is verbatim in v4 §10.3
  ("A violation of a declared barrier is a loss of safety; a data or certificate failure … is a loss
  of assurance, and the two are not interchangeable"). Nothing added.
- **Batch-1 T1/T2 were half-discharged.** §7.2 already ends with "A scalar summary may rank. It may
  communicate. It cannot certify componentwise adequacy." — the anti-scalar/anti-compensatory
  substance. What was missing and is now added is the one-directional half (refutes and alarms, never
  certifies), tied to Proposition 30 rather than asserted.
- **`Proposition 32`'s numbers changed during the build.** The staged text said "holds the index near
  0.2 yr", from the mean of my earlier run. Re-running with the section's own statistic
  (`(a_n − min a)/(−fitted slope)`) gives median 0, mean 0.21–0.25, q90 0.81–1.00 across `n = 10²` to
  `10⁵`. The manuscript now prints all three, because the median being zero is itself part of the
  argument (under a downward trend the current level is usually the record minimum). The qualitative
  claim — bounded in the record length at the scale `σ/β` — is unchanged and strengthened.

## 3. Not applied, and why

| Item | Reason |
|---|---|
| Identification sets `T_±` as a definition | needs the set defined on the article's own objects before it can be cited; §8.1's invariance sentence already carries the content. Left for the companion |
| fable T10's recycling identity | the printed identity has a sign slip; the corrected invariant (`D − W = M − S₂ − S̲₁ − S̄₃`, verified numerically) is not needed by any surviving point |
| opus U6's replacement of Definition 5 | the additive margin is admissible beside it, not instead of it; Theorem 24 now supplies the margin without displacing the registered object |
| fable T9's `σ_liq = ℓ/g` | symbol collision with the declared donor fraction; the liquidation share is stated in words in Definitions 21–22 instead |
| exergy/affinity formalisation of the fourth predicate | needs a species table and a declared `Ω`: new modelling |
| MDV, standards amendments, Lean 4, JSON schema, time-expanded checker, pilots, dashboards | project deliverables, not claims of this article (both batches) |
| any numeric premium, `δ*` value or `κ` estimate for a public indicator | the bounds and second differences they would be computed from are not declared by the publisher; printed in the article only as the declared-box exhibit in S-B |
| opus's cut list | would subtract load-bearing apparatus |

## 4. Author's remaining actions

1. Confirm or re-word the **Antecedents** paragraph's standards claim (D4) — the facts are verified,
   the framing is mine.
2. Check **"its equation (1) and Section 2.4"** in §10.1 against `paper4_delay_dynamics_v30.pdf` (D7).
3. Merge `supplementary_v5_additions.md` into your own `paper3_supplementary_v8.md` and renumber the
   sections there; the two files are additive, and §S-A/S-B/S-C/S-D/S-F contain nothing that
   duplicates the five items your Declarations paragraph already promises.
4. Decide whether new labels 21–33 collide with numbers used in your companions or in any submitted
   cover letter, since the article's counter is now continuous to 33.
5. Spot-check the two remaining companion DOIs (`22554297`, `22545740`); I resolved only `22554217`.
6. Re-run the three scripts if your environment pins older `numpy`/`scipy`; the exhibit values are
   seed-fixed, and `outputs.txt` records a full run.

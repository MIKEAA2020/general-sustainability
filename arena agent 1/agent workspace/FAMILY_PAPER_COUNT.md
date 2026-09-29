# Optimal number of papers — recommendation, 2026-09-29

**REVISED 2026-09-29 (see §0): recommendation is 10, not 8.**
~~Recommendation: 8.~~ Reasoning, and the evidence it rests on, below.

The question reduces to something sharper than "how many". Since preprints.org is a
*staging* venue with **no length limit**, posting more preprints buys nothing on its own.
Each preprint should map to exactly one eventual journal submission. So the real question
is: **how many journal articles does this content merit?** The answer is driven by one
test, applied per candidate paper:

> Does it pose one answerable question, stand on its own, and survive separation without
> being weakened?

## 1. Evidence: the P2 companions are separate papers

Checked directly. The four companions are **not** absorbed into `obstr_v57`:

| companion | words | sections | section-title overlap with `obstr` |
|---|---|---|---|
| `psuff` (`paper2_probabilistic_sufficiency_v9`) | 11,804 | 13 | **0/13** |
| `comp` (`paper2_computational_certification_v9`) | 9,924 | 14 | **0/14** |
| `minimax` (`minimax_v11`) | 6,107 | 12 | 1/12 |
| `ebc` (`paper2_exact_belief_computation_v9`) | 3,420 | 11 | **0/11** |

Their objects are distinct — measure duals and envelopes; adjoint safety rows and a
continuous-to-finite theorem; a support identity and exact sufficiency; a
pairwise-Hamming classification and antichain census. This is a programme with several
papers in it, not one paper with four drafts.

## 2. The eight

| # | paper | from | words | venue |
|---|---|---|---|---|
| 1 | Obstruction certificates under incomplete observation | `obstr` + `minimax` | ~28,700 | Automatica, Regular |
| 2 | Computation of obstruction certificates | `comp` + `ebc` | ~13,300 | SIAM J. Optimization |
| 3 | Exact probabilistic sufficiency | `psuff` | ~11,800 | IEEE TAC, Full |
| 4 | Quantifier-order separation in assessment | `P1` | ~30,600 | Math. OR / SIAM J. Opt |
| 5 | The decision clock | `P5` + `P4` | ~45,600 | preprints first |
| 6 | Certified horizons on a real record | `E2` + `ARV` | ~23,500 | CJFAS |
| 7 | What depletion numbers can certify | `P3` + `E4` | ~45,000 | Ecological Economics |
| 8 | Forecasting baselines and the null | `E1` + `E3` + `ws` | ~41,000 | Int. J. Forecasting |

Total roughly 240,000 words.

## 3. Why these merges, and not fewer or more

**Five P2 papers become three.** `minimax` folds into `obstr` because dual certificates are
part of the certificate theory and 6.1k words is thin alone; `ebc` folds into `comp`
because both are computational and 3.4k words is a section, not an article. `psuff` stays
alone: exact sufficiency is a different question from obstruction and is a full paper at
11.8k.

**`P1` stands alone (this reverses the current plan).** At 30,600 words the separation
result is a full article. The present plan files it as "Supplement S1" of Paper A, which
buries 30k words of real result inside someone else's paper. It merits its own preprint and
its own submission.

**`P5` + `P4` merge because they share a result.** Both report the 6.5-year crossing: `P5`
as the exact map's single crossing, `P4` as the mobilising rule restabilising above 6.5 yr
through a Neimark--Sacker crossing. Split, each would have to cite the other for the same
number — the worst outcome. Merged, one paper owns it. This is the one merge the content
demands rather than merely permits.

**`E2` + `ARV` merge because they are two directions on one record.** Already reconciled:
obstruction/necessity in exact rational arithmetic against construction/sufficiency in
floating point, with no numbers to reconcile. `ARV` at 7,256 words is too thin alone.

**Measurement splits by question, not by length.** What depletion numbers can certify
(`P3`, `E4`) is a different question from what forecasts can certify (`E1`, `E3`, `ws`).
`E3`'s null result — benchmarks beating process models — is the lead of paper 8.

## 4. Preprints.org specifics

- **Post all eight.** Each gets a DOI and is independently citable.
- **Do not split for length.** Papers 5 and 8 are long; that is fine on preprints.org. If a
  journal later requires splitting, decide then.
- **Resolve overlap before posting, not after.** This is the main risk of eight preprints.
  The shared framework (selector principle, epistemic kernel, observation structures) must
  be derived **once**, in paper 1, and cited by 2 and 3. Re-deriving it three times is what
  makes a programme look like salami-slicing.
- **Cross-cite explicitly.** Each preprint should name its siblings and say what it does
  not do.

## 5. Caveats on this recommendation

- The companions were checked by **section-title overlap**, which is crude. It establishes
  they are not absorbed; it does not rule out content-level duplication. Papers 1--3 need a
  proper content diff before posting.
- **`ebc` remains moderate-confidence identification** — no file is named `ebc*`;
  `paper2_exact_belief_computation` is the only stem whose initials fit an Automatica
  Technical Communiqué slot. Confirm before folding it into paper 2.
- Word counts for `E1`, `E3`, `E4`, `ws` are inferred from file sizes, not counted.
- The economics material (`ecomod_v37`, `manuscript_ECOMOD_v37`, `paper3_JIE_submission`,
  `JIE_cover_letter`) is **not** in any of the eight. If it is live, it is a ninth.

---

## 0. Revision — the count is 10, not 8

The §1 check used **section-title** overlap and proved the P2 companions are not absorbed.
It did not test content. That test has now been run: sentences of eight or more words were
extracted from all five P2 manuscripts and intersected.

| pair | shared sentences | overlap of the smaller |
|---|---|---|
| `obstr` ↔ `psuff` | 0 | **0.0%** |
| `obstr` ↔ `comp` | 0 | **0.0%** |
| `obstr` ↔ `ebc` | 0 | **0.0%** |
| `obstr` ↔ `minimax` | 1 | 0.7% |
| `minimax` ↔ `psuff` | 2 | 1.5% |
| `psuff` ↔ `comp` | 4 | 1.9% |
| `psuff` ↔ `ebc` | 3 | 3.4% |
| `comp` ↔ `ebc` | 4 | 4.5% |
| `minimax` ↔ `comp` / `ebc` | 1 / 0 | 0.7% / 0.0% |

Sentence counts: `obstr` 557, `psuff` 248, `comp` 216, `minimax` 137, `ebc` 89.

**The five are essentially disjoint in content.** This reverses the two merges of §3:

- `minimax` → `obstr` was justified by thinness, not duplication. With no duplication to
  remove, folding it in buries an independent result. **It stands alone** at 6,107 words,
  which is a legitimate length for a Mathematics of OR research article.
- `ebc` → `comp` likewise. **It stands alone** at 3,420 words — which is about right for an
  Automatica *Technical Communiqué*, the short format it was already assigned.

The revised count therefore matches the original venue assignment, which gave the five P2
papers five separate venues.

### The revised ten

| # | paper | from | words | venue |
|---|---|---|---|---|
| 1 | Obstruction certificates under incomplete observation | `obstr` | 22,615 | Automatica, Regular |
| 2 | Exact probabilistic sufficiency | `psuff` | 11,804 | IEEE TAC, Full |
| 3 | Computational certification | `comp` | 9,924 | SIAM J. Optimization |
| 4 | Minimax dual certificates | `minimax` | 6,107 | Mathematics of OR |
| 5 | Exact belief computation | `ebc` | 3,420 | Automatica, Tech. Communiqué |
| 6 | Quantifier-order separation in assessment | `P1` | ~30,600 | Math. OR / SIAM J. Opt |
| 7 | The decision clock | `P5` + `P4` | ~45,600 | preprints first |
| 8 | Certified horizons on a real record | `E2` + `ARV` | ~23,500 | CJFAS |
| 9 | What depletion numbers can certify | `P3` + `E4` | ~45,000 | Ecological Economics |
| 10 | Forecasting baselines and the null | `E1` + `E3` + `ws` | ~41,000 | Int. J. Forecasting |

### What still justifies merging, and what does not

**Paper 7 survives as a merge** because `P5` and `P4` share an actual *result* — both report
the 6.5-year crossing. That is content overlap, not thinness, and splitting would make each
cite the other for the same number. This is the one merge the evidence supports.

**Papers 1–5 stand apart** because the overlap test found nothing to remove by merging.
Each poses its own question and carries its own result.

**Papers 8, 9, 10** are unchanged: 8 because two directions on one record were already
reconciled and `ARV` is thin alone; 9 and 10 because they split by question, not length.

### Consequence for preprints.org

Ten preprints, ten DOIs, ten journal submissions. The salami-slicing risk is smaller than it
looks precisely because the overlap is near zero — but the corollary is that each paper must
cite its siblings for the shared framework rather than re-deriving it. With five disjoint
P2 papers, a reader of paper 3 needs to be told, in one line, that the selector principle and
epistemic kernel are defined in paper 1.

### Remaining caveats

- The overlap test is sentence-level on shared strings. It would miss paraphrase-level
  duplication. It is strong evidence of disjointness, not proof.
- `ebc` identification remains moderate confidence (no file named `ebc*`).
- Word counts for `E1`, `E3`, `E4`, `ws`, `P1` are inferred from file size, not counted.
- The economics material is in none of the ten; if live, that is an eleventh.

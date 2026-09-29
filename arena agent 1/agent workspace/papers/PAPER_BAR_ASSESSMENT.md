# Bar assessment: do the eleven papers meet the top-journal standard?

Assessed 2026-09-29 against the stated bar: **sufficient novelty and impact, substantial
methodological development, and/or empirical or applied contributions of broad practical
interest**. Applied even though the papers are destined for preprints.org, because a
preprint is the front of a journal submission and should be built to survive one.

## Headline

**No paper is ready as it stands.** Two are close. Four carry a specific recorded gap that
blocks them. Three are below the bar on length or positioning and need a decision rather
than an edit. The remaining two are strong but carry a duplicated or ill-conditioned
number.

Measured, not asserted: word counts, formal-result counts, empirical density, and whether
each paper states a prior-art position.

| # | paper | words | formal results | empirical density | prior-art stated | verdict |
|---|---|---|---|---|---|---|
| 1 | obstruction calculus | 22,399 | **23** | 24 | **yes** | close; one gap |
| 2 | probabilistic sufficiency | 11,962 | 19 | 7 | **no** | blocked |
| 3 | computational certification | 10,077 | 5 | 1 | **no** | blocked |
| 4 | minimax dual certificates | 6,263 | 14 | 9 | **no** | blocked |
| 5 | exact belief computation | 3,578 | 8 | 6 | **no** | **below bar** |
| 6 | assessment separation | 28,066 | 0 | 155 | weak | **highest risk** |
| 7 | sampled governance | 18,441 | 0 | 170 | yes | strong; ill-conditioned |
| 8 | governance delay | 27,518 | 0 | 143 | yes | strong; duplicate |
| 9 | cod certification | 22,520 | 14 | **664** | no | **strongest applied** |
| 10 | depletion ledgers | 43,147 | 0 | 290 | weak | typology risk |
| 11 | forecasting baselines | 39,704 | 14 | 581 | no | strong empirical |

Papers 6, 7, 8 and 10 record zero formal results **because they are empirical papers** that
state findings in prose and tables, not because they are empty — their top LaTeX
environments are `tabular`, `figure` and `longtable`. For those the bar is the substance of
the empirical contribution, and it is assessed as such below.

## Per paper

**1. Obstruction calculus — close, one gap.** The strongest on methodology: 23 formal
results, and the only paper whose prior art has been fully worked and integrated. Outstanding:
the plan records that it needs **at least one worked case where a certificate bites on a
system whose kernel cannot be computed** — without it the instrument is unfalsified in the
regime that motivates it. That is new computation, not editing.

**2, 3, 4. The companions — blocked on positioning.** All three have formal results (19, 5,
14) and none states a prior-art position. Novelty has to be *demonstrated* against named
work, and they demonstrate nothing. Specific requirement blocks naming the literature each
must engage have been inserted into all three. Paper 3 is the weakest of the three: five
formal results for a computational paper, with no comparator for its complexity claims.

**5. Exact belief computation — below the bar.** 3,578 words, no prior art. Against
"substantial methodological development" this does not clear at this length. It needs a
scope decision: expand beyond the cube instance, or fold into paper 3. Inserted block says
this explicitly.

**6. Assessment separation — highest novelty risk.** 28,066 words, 42 sections, no formal
results, and the plan already records the problem: the separation result **sits close to
known robust-optimisation and MCDM separation results**, and it "either carries an
aggressive prior-art paragraph or it does not go in". That paragraph does not exist. This is
the paper most likely to be rejected for want of novelty, and the fix is research, not
editing.

**7. Sampled governance — strong, with an ill-conditioned headline.** 170 empirical markers,
two screens. But the plan records that its headline 6.5-year figure moves by 55% under a
0.2% change in the exploitation ratio. A top journal will find this. It needs a sensitivity
band, not a point.

**8. Governance delay — strong, with a duplicate.** The no-Hopf theorem and the five-regime
topology are substantial, though stated without theorem environments, which should be
corrected. It still contains the duplicated 6.5-year passage owned by paper 7.

**9. Cod certification — strongest applied paper.** 664 empirical markers, 14 formal
results, a real record, and two directions already reconciled. Clearest fit to the bar of
any of the eleven.

**10. Depletion ledgers — typology risk.** 43,147 words. The plan records that a typology
("three diagnostics are widely misread") is a clarification at top-journal level **unless
tied to a measurable consequence**. That tie has not been made explicit.

**11. Forecasting baselines — strong empirical with a leading null.** 581 empirical markers
and a null result positioned to lead, which is the correct treatment.

## What was done in this pass

Prior-art requirement blocks were inserted into papers 2, 3, 4 and 5, naming the specific
literature each must engage and the claim each must establish. These are requirements, not
prose: they turn an absence into a specified task rather than filling the gap with a stub.

## What remains, honestly

| gap | kind | papers |
|---|---|---|
| prior-art paragraph, written | research | 6, 9, 11 |
| prior-art paragraph, write from the inserted requirement | writing | 2, 3, 4, 5 |
| worked case on an uncomputable kernel | new computation | 1 |
| tie the typology to a measurable consequence | writing | 10 |
| sensitivity band on the 6.5-year figure | writing + computation | 7 |
| remove the duplicated 6.5-year passage | editing | 8 |
| scope decision on the short paper | decision | 5 |
| promote results to theorem environments | editing | 8 |
| framework de-duplication | editorial | 1–5 |
| bibliography merge | editing | 9, 10, 11 |

## Root cause

The recurring pattern across every failing item is the same one recorded earlier in this
project: **results were developed before their novelty was established against the
literature.** Prior art was treated as something to write at the end. That is why paper 1 —
the one paper where prior art was done first, and where doing it changed the paper's central
claim — is the one that is closest to the bar, and why the four papers with no prior-art
position at all are the ones that cannot yet be assessed.

The remedy is not more writing. It is, for each paper, naming the nearest neighbour and
saying what it does not deliver. That is the only thing that converts a result into a
contribution.

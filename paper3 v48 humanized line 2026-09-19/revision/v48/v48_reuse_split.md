# v48: what is reused, what is regenerated

Written by `v48_reuse_split_v1.py` from the claim ledger, so the ruling is one file the build reads instead of a decision re-made at each seam. **290 sentences are reused as the draft wrote them; 268 are written again from the deposit in the draft’s register.** The two sets partition the 558 ledgered sentences; the 161 sentences the draft shares verbatim with the deposit are outside the question, since they are the deposit’s own wording.

| set | n | why |
|---|---|---|
| reused: high-confidence supported | 260 | a partner passage was found and no marker diverges |
| reused: signposting | 30 | the sentence reports what the document does and asserts nothing about the world |
| regenerated: medium or low confidence | 188 | the pairing itself is uncertain, so the draft’s sentence is not a safe input; go to the deposit |
| regenerated: flagged | 64 | a value, hedge, condition, attribution or inference differs from the passage it restates |
| regenerated: by the author’s markup | 16 | moved out of the reused set by `v48_overrules.csv`; the reuse was sound on words and unsound on notation |

## The medium and low-confidence rows, in the author’s words

Thin confidence is not a finding against the draft; it is a finding about the alignment - a plain-English sentence and its technical original share few words, so the pairing is thin and the marker comparison is only as good as it. The ruling therefore sends those rows to the deposit rather than asking the build to touch up the draft: where the alignment is uncertain, the truth source is the safer input. The draft supplies the voice for them, not the sentence.

## The one sentence the draft wrote on its own authority

`D0081` reads: "That is why support drawdowns cannot be traded against revenue anywhere in the ledger." The deposit’s claim is narrower and differently worded: "The first is *compensatory aggregation*: heterogeneous physical stocks and service flows are summarized by scalar indices whose cross-component trades are never declared as mathematics, so a severe deficit in one component can coexist with a positive aggregate" and "measures the part of a published aggregate that was produced by cross-component trades". The word *revenue* does not appear in the deposited article. It is kept - it is the draft’s own synthesis and the one place the humanizer said something its source did not - and it is regenerated at the deposit’s scope: non-compensation is a claim about what a weighted sum can certify, not a prohibition written into every line of the ledger. Disclosed here, in the build note, and in the package README.

## Screening, not certification

The line-level read of these sentences (`v48_reuse_audit.md`, `v48_reuse_read.md`, `v48_reuse_findings.md`) raised three prose flaws the marker rules could not see - D0089, D0108, D0158 - and found 16 sentences carrying a symbol form the deposited article reserves for another object. `v48_overrules_notation_candidate.csv` moves those 16 to the regenerated set; nothing has been applied, and the counts below are the ruling as the ledger gives it.

The 290 reused sentences are **screened, not certified**. What the ledger checked is that a partner passage exists and that values, hedges, conditions, attributions and inference markers do not diverge from it. It did not check that the draft understood the argument, and a sentence can pass every test here while carrying a claim the paper means differently. The register of the reused set is owed to the draft being its own source; the accuracy of the regenerated set is owed to coming from the deposit; the accuracy of the reused set is owed to the author, and this file is where that is said out loud instead of being implied by a green check.

## The regenerated rows, by class

| verdict | n |
|---|---|
| `supported (reworded)` | 192 |
| `needs check: attribution` | 28 |
| `needs check: strength` | 18 |
| `needs check: scope` | 12 |
| `supported (near-verbatim)` | 11 |
| `needs check: inference` | 5 |
| `unsupported: no partner located` | 1 |
| `not a claim (signposting)` | 1 |

Every row is in `v48_reuse_split.json`: the reused ones with the reason they are reused, the regenerated ones with the deposit passage to write from and the flags that sent them there.

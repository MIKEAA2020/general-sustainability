# The 306, read by hand

Nothing here is generated; the numbers come from four runs, listed at the end with what each one produced. The
reuse ruling (`v48_reuse_split.md`) said *screened, not certified*, and this is the screening read as a person
does it: each reused sentence beside the deposit's own text, and a verdict written down.

## What the instruments said

| run | result |
|---|---|
| `v48_reuse_audit_v1.py` | 306 sentences read at line level: **10 flagged, 296 nothing raised** (voice 2, name 2, status 2, universal 5) |
| `v48_audit_selftest_v1.py` | six defects planted in rows the audit had cleared: **6/6 caught**, control row clean |
| `v48_notation_drift_v1.py` | 221 inline `$…$` spans in the 306: 126 as the deposit writes them, 20 grouping/QED only, 19 font wrapper, 25 sub/superscript swap, **31 in no form at all** |
| `v48_reuse_findings_v1.py` | of those 31: **16 sentences / 23 spans rename or redecorate an object the deposit has reserved**, rest cosmetic |

The audit needed fixing before it could be trusted, and it is fair to say so: the first version crashed on a
`re.sub` replacement, then flagged `000 kt` because its figure regex read `240,000 kt/yr` as three numbers, then
called `Finally` and `Illakwahhi`-adjacent capitalised words author surnames, and — the one that mattered — its
unit test was **inverted**, so it raised a flag when the deposit *did* contain the figure and stayed silent when it
did not. Its section-pointer test accepted `§2.9` because `§2` exists. Both fixed, and the self-test exists to make
sure the fixed version still sees a planted flaw: `unit`, `ref`, `name`, `status`, `universal`, `voice` each fire on
their planted case and the untouched control stays clear. So "296 clean" is the reading of a filter that demonstrably
works, not the silence of a broken one — for the six classes it claims to cover.

## The 10 flagged rows, and what each one actually is

Six are instrument noise, and saying which is part of the result:

- **D0549, D0556, D0110** — the `unit` flags were the comma bug. Read against the deposit's own sentence: the
  figures are the deposit's (`74{,}000{,}000` kt, `240{,}000` kt/yr, `309` years, `250{,}000` kt, `120{,}000` kt,
  `1{,}000{,}000` kt, `600{,}000` kt). **Keep.**
- **D0024** — `name: Finally`. The surname regex caught a sentence opener. The row's real content — the interface
  contract fixes the one shared object — matches the deposit's §"The interface with institutional dynamics". **Keep.**
- **D0053, D0023** — first person (`what we call`, `as fast as we use things`). Not a defect: the deposited article
  writes `A further failure mode is what we call the *productivity illusion*`, so the draft is copying the
  article's own voice, and measured across the files the count is 2 first-person instances in the deposit against 6
  in the draft (0.1 vs 0.3 per 1k words). **Keep, as register.**
- **D0077** — `status: non-example` raised only because the sentence was paired with an unrelated deposit sentence
  (ratio 0.402); the deposit does label this object **Non-example 1** and calls it "a deliberate boundary of
  aggregation, not a score of the framework". **Keep.**

Four are worth the author's eye, and only two of those are flaws in *content*:

- **D0357** — "The uniform-margin assumption is **doing all the work**" against the deposit's "is **essential**".
  Same claim, more idiom. Keep, on register.
- **D0158** — the deposit: "**each** depletion quantity carries its own classification, stated at its actual
  strength". The draft: "**every** depletion quantity". In a paper whose whole point is that there are exactly
  three such quantities, `each → every` is a scope word swapped in a definitional list. Regenerate.
- **D0156** — the draft adds "which is why it is read as a ratio, **never** as a forecast" where the deposit says
  the estimate "carries the substitution and technology premises of the reserve classification, **not a physical
  forecast**". The inference is the deposit's own, the `never` is the draft's emphasis. Keep, with the note.
- **D0089** — "every depletion horizon in this article is stated against a rate **and** a barrier". The deposit's
  taxonomy, verbatim: `| $J_A^{\mathrm{gross}}$, $H_A^{\mathrm{gross}}$ | How strongly does the system depend on,
  or turn over, the pool at the current gross rate? |`, `| $H_A^{\mathrm{loc}}$ | …local stock-to-rate ratio? |`,
  `| $T_A$ | Under a stated model, policy, and disturbance scenario, when is the threshold first reached? |`. The
  three are rate, ratio, first-passage-under-scenario. "Against a rate and a barrier" describes two of the three and
  mis-describes the third. **Regenerate** — and note that this row sits in the 31 that the ledger reused *because
  they "assert nothing"*; 20 of those 31 carry a universal, a negation or a pointer, so that class was the weakest
  part of the ruling and is where this kind of slip lives.

## Two things the line-level read found that no marker rule could have

**1. A dropped abbreviation definition.** D0108 as the draft wrote it: "…single-source **US** Geological Survey data
of questionable credibility…". The deposit's sentence: "…single-source **U.S.** Geological Survey **(USGS)** data
whose credibility is questionable…". `U.S.` is the style both documents use everywhere else (draft 5 instances,
deposit 6, against 1 and 0 for `US`), and the parenthetical is where `USGS` is defined for a reader — the draft has
three `USGS` uses and **zero** definitions of them, while the deposit defines it once at the mention the reuse drops. v47 shipped the
definition (1) because its prose came from the deposit; reusing this sentence would delete it. **Regenerate**, or at
minimum re-insert `(USGS)`; both are one-line decisions.

**2. The notation is not the deposit's, and the fonts are load-bearing here.** The humanizer re-typeset inline
maths document-wide, and in six cases the form it chose collides with something the deposited article has already
defined. The table is in `v48_reuse_findings.md`; the substance:

| the reused sentence writes | the deposited article writes | what collides |
|---|---|---|
| `S^{\top}` (6 rows) | `S_{\mathcal{T}}`, "carries the subscript for that reason" | plain `S` is the moiety readout $S_m$ |
| `\mathsf{S},\mathsf{K}` for the §2.4 state (4) | `S, K` undecorated | `\mathsf{S}` is the hybrid incidence matrix, `\mathsf{L}` its left null basis |
| `\dot\chi = S\eta + b` (1) | `\dot\chi = \mathsf{S}\eta + b` | the two matrices become one letter |
| `\mathcal A^{\mathrm{win}}_{\min}` (4) | `A_{\min}^{\mathrm{win}}` | `\mathcal A` is the adequacy functional (§8) |
| `\mathcal B_{\mathrm{lim}}`, `\mathcal B_{\min}` (4) | `B_{\lim}` | `\mathcal{B}(x,t)` is the attainable-balance domain |
| `\mathcal H^{\mathrm{loc}}_A`, `\mathcal H^{\mathrm{gross}}_A` (4) | `H_A^{\mathrm{loc}}`, `H_A^{\mathrm{gross}}` | the article never uses `\mathcal H` |

Four of the `S^{\top}` occurrences and six of `\mathcal H` **are already in the packaged v47** — its text carries
`S^{\top}` 4 times next to `S_{\mathcal{T}}` 44 times and the notation-table row defining the latter, and it prints
`\mathsf{S}` for both the §2.4 state and the hybrid incidence matrix. That is inherited, so v47 stays as
shipped unless the author chooses otherwise; but v48 would add to it, because the sentences that do it are precisely
the ones the ledger cleared for reuse. `v48_overrules_notation_candidate.csv` (16 rows, `regenerate`) is the
mechanical way out — a regenerated sentence is written from the deposit and brings the deposit's symbols with it.
Dry-run: accepting it moves 16 rows, reuse 306 → 290, regenerate 252 → 268, partition still 558 of 558, every move
logged by `v48_reuse_split_v1.py`. The live `v48_overrules.csv` was left at the default ruling; the numbers above
came from a temporary copy that was restored byte-identically.

The alternative is to keep the reuse and normalise the spans at build time — mechanical, reversible, changes no
word, but it is a rule that touches maths, and this project's standing rule is that the pipeline decides nothing
about content. So it is offered, not applied.

## What is still not checked

- The 31 `not-a-claim` rows were reused because they assert nothing *about the world*. 20 of them assert something
  about the document — a section number, a count, a discipline (D0089 above). Pointers were verified for existence;
  they were not verified for *what the target says*.
- `scope` remains a floor, not a measurement: the ledger's condition detector caught 0 of 4 planted removals
  (`claim_ledger_v1_mutation_test.md`), and the audit does not test condition removal either.
- Spans that matched the deposit "as written" were not re-derived; agreement in spelling is not proof the draft
  attached the right formula to the right object. The 7 sentences furthest from anything in the deposit (ratio
  under 0.35: D0653, D0544, D0195, D0594, D0530, D0597, D0162) are where that risk is largest, and they are short
  enough to read in one sitting. That read is the author's, not this file's.
- D0218's `(Author, D., et al., *in review*; …)` stays in the reuse set under the attribution ruling (the draft
  anonymised its own companion citations, 4 of them; the deposit names `Abaee, 2026a, doi:10.5281/zenodo.22554217`).
  It is disclosed in `v48_reuse_split.md` and must be in the build note and the README, with one more thing the
  line-level read makes visible: the shipped reference list is **not** anonymised, so the in-text placeholder reads
  as an unfinished edit rather than as anonymity.

## Files

`v48_reuse_audit.{md,json,csv}` (the 306 read against the deposit), `v48_reuse_audit_selftest.{md,json}` plus
`v48_reuse_split_selftest*.json` (the planted-defect test), `v48_notation_drift.{md,csv,json}` (the maths),
`v48_reuse_findings.{md,csv,json}` (the 16 rows with evidence), `v48_overrules_notation_candidate.csv` (accept, edit
or delete). Scripts: `v48_reuse_audit_v1.py`, `v48_audit_selftest_v1.py`, `v48_notation_drift_v1.py`,
`v48_reuse_findings_v1.py`. No document was built or edited, and the live `v48_overrules.csv` is the header-only
template as before.

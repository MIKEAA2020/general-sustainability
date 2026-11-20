# Orchard/elevator analogy — provenance findings (2026-11-13)

Searched: `MIKEAA2020/general-sustainability` (all 26 repos listed; the analogy lives in this one),
code search for `orchard`, `hens`, `intensively managed beds`, `census of the orchard`,
`fast-provisioning`, `killing trees to cover your liabilities`; plus commit timestamps.

## 1. Verdict

**The clear original prose survives nowhere in the repository.** Every manuscript file that contains
an analogy contains the *same* 1,617-character paragraph, byte-identical. There is no blob in the repo
holding the hen version as manuscript prose. Your clear prose is in exactly one place:
`agent 2 productivity illusion/reviews/RESPONSE_to_reviewer.md` (and its two copies) — as a quotation
inside a reviewer response.

## 2. Where each variant lives

| File | Version present | Date |
|---|---|---|
| `orchard, hen, elevator.txt` | **Your original, in full**: the conversation where you say *"imagine u have an orchard that grows apples. in overshoot, where your needs exceed the productivity of apples, u can meet your excess needs by cutting down trees…"* and *"or if you start killing your hens to provide food because all the eggs they produce does not suffice"* | pre-manuscript |
| `agent 2 productivity illusion/reviews/RESPONSE_to_reviewer.md` | Your clear prose **quoted** (number of trees × average productivity rate; killing trees to cover liabilities; hens and eggs) | review response |
| `batch 9/agent 2/ecomod_c11_review/c11_extracted_text.txt` | **The rewritten paragraph already in place** — C11, the *earliest* manuscript text in the repo | 2026-10-28 |
| `ecomod_continued_10.tex` (repo reference), C15, C16, C17, C18, C19, C20 | same 1,617-character paragraph, ratio 1.000 to C17 in every case | 2026-10-28 onward |
| `batch 9/agent 2/ecomod_c14/ecomod_main.tex` | **The analogy is absent entirely** — no "orchard", no "elevator" | 2026-10-29 |

## 3. The timeline

1. **Your original** (orchard + hens + well) — plain, concrete, and it maps to the algebra you were
   testing: trees × productivity = flow; killing trees to cover a liability creates the vicious cycle.
2. **The rewrite** appears fully formed in **C11** (commit `8bd970f1`, 2026-10-28). It is not a
   gradual degradation you can point at in a diff — the first draft that exists in version control
   already has it, complete with "fast-provisioning ground, such as intensively managed beds",
   the qualification clauses, and the elevator sentence.
3. **C14** (2026-10-29) drops both analogies. The revision audit records this as deliberate:
   *"Orchard analogy… the full paragraph was replaced"; "Elevator analogy… the entire ten-person-rated
   elevator carrying fourteen people example was removed."*
4. **C15** (2026-10-29, commit `2f146c40`) restores them. `metadata/revision_record.md` says:
   *"Restored exactly — Introductory exposition, both orchard/elevator analogies and the three research
   questions… The concluding orchard paragraph, including 'A harvest total is not a census of the
   orchard.'"* — but what was restored is the **C13/C11 form**, i.e. the rewritten paragraph, not your
   original prose. The record calls that "restored exactly" because it is exactly C13; C13 was already
   the rewrite.
5. C16 → C20 carry it unchanged.

So: the substitution happened **before or at C11**, on 2026-10-28, and every later version — including
the one that advertises itself as a restoration — copied it forward.

## 4. Why it reads like that: the standing style policy

`tools/MANUSCRIPT_STYLE_POLICY.md` (standing, all papers, from 2026-09-10) is the pressure that
produced this register. Rule 7, verbatim:

> **No metaphor apologies / naive over-hedging.** Readers understand that an orchard analogy is not an
> empirical claim about global ecology. Saying so explicitly reads like "note: the map is not the
> territory". Remove: "the metaphor is not an empirical claim"…

The paragraph in the manuscript does precisely what rule 7 forbids: *"This is a conditional model
mechanism, not evidence that NFA accounts measure physical stocks or that a particular real-world
conversion occurred"*, *"it does not assert that the classes map directly to NFA categories"*. Three
disclaimers bolted onto a five-sentence analogy. That is where the readable orchard went.

Note the policy distinguishes over-hedging from legitimate scope: *"a scope statement constrains the
claim; an over-hedge apologises for the prose."* The manuscript's clauses are the second kind. The
policy's own scan table still lists `paper1_assessment_separation_v23` with **4 outstanding blockers:
"parable apology + self-commentary"** — the same defect, flagged and never cleared.

## 5. Two corrections to what I said last turn

**(a) I said the prose is "yours".** That was wrong, and it is the third time I have mis-scoped
something by checking the wrong object. What the record shows is that the *idea* is yours and the
*narrative is yours*, while the **sentences in the manuscript are a rewrite that dropped your concrete
detail** — the hens, the apples-per-tree arithmetic, the feedback loop spelled out. My provenance check
established only that C10–C20 all agree with each other, which says nothing about whether they agree
with you. They do not.

**(b) I said "content is yours, I only fix layout" applies to this.** Wrong. That instruction came from
the keywords/abstract-column episode and covers *what the paper claims* — evidence, scope, numbers. It
does not license leaving damaged prose alone when you ask for it to be fixed, and it certainly does not
extend to protecting a paragraph you are telling me is not yours. Retracting that.

## 6. Where the cut-off actually is

Your rule, as I now understand it: claims, scope, evidence, numbers — untouchable without instruction.
Wording that obscures your argument — fair game, and if I am touching it, restore *your* concreteness
rather than inventing phrasing. The elevator fix I proposed last turn ("the ride itself does not
establish" → "its continuation does not establish") is grammar only and preserves the same flatness;
under this standard it is a patch on the wrong paragraph. The real repair is the one C14 accidentally
demonstrated the need for and C15 then undid: go back to what you actually wrote.

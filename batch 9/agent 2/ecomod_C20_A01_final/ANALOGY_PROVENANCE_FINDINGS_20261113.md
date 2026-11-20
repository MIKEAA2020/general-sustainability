# The clear prose was in v41 — recovered, and the replacement is now dated (rev. 2)

Supersedes `ANALOGY_PROVENANCE_FINDINGS_20261113.md` rev. 1, which was wrong on the headline point.
Rev. 1 checked only the C-series (`ecomod_continued_10`, C11–C20) and concluded "the clear original
prose survives nowhere in the repository." That conclusion was false. The `agent 2 productivity illusion/`
lineage holds twenty versions (v30–v44) on `main`, and the clear prose **is** there.

## 1. Recovered

`recovered_prose/manuscript_ECOMOD_v41.tex` — 124,430 bytes, sha256
`beeb8aa59b7f0a910d4451f06fd7cba6ead3a3b20c4ec1a6867026f4ceca382b`
Git blob `36763b8dbfcfe542c29c55f1ff1c0d203648659b`, path
`agent 2 productivity illusion/manuscript_ECOMOD_v41.tex`, `main`.

## 2. What v41 actually says

Three paragraphs, concrete throughout, no disclaimer furniture:

> **The setting is an orchard with two kinds of ground.** Each year some of the ground bears fruit that
> can be gathered without harming the ground itself — a *flow*… The trees and soil remain standing — a
> stock of natural capital — and it is this stock that generates the flow… One sort is fast provisioning
> land — cropland and intensively managed systems — whose yield is high and quickly restored, but whose
> regenerative standing value is small. The other sort is ecological capital land — forest, soil,
> wetland, long-rotation and regenerative systems…

> **The arithmetic is the arithmetic of any productive stock.** The harvest is the sum over the land of
> (productivity per unit) × (number of units)… So long as needs stay within total productivity the
> harvest can be taken without touching the base: **the orchard yields fruit and the flock yields eggs.
> But if needs exceed total productivity, the shortfall has to be covered by eating into the base itself
> — cutting branches, felling trees, killing hens**, and in the two-land model converting ecological
> capital into provisioning land. That covers the current liability, but it changes the *composition* of
> future production.

> **The elevator** (attributed to the ledger study): *"a system can bear overload for a while — an
> elevator rated for ten people will still carry fourteen, showing little visible strain before the
> cable gives way — while its underlying integrity is quietly eroding. Judged by what it delivers (the
> harvest) the elevator still runs; judged by its reserve (the stock, the cable) it is already failing."*

That last sentence is why the C-series version is a degradation and not a variation: v41 says the
elevator *is already failing judged by its reserve*, and supports it with two parallel judgements. The
C-series version ends in the category error you flagged — "the ride itself does not establish whether…
".

## 3. Version table (marker = "killing hens" present in the file)

| Version | Size | orchard | hen | elevator | Verdict |
|---|---|---|---|---|---|
| v30 | 107,330 | 17 | 39 | 2 | clear lineage |
| v31, v32 | 113,938 / 115,086 | 17 | 45 | 2 | clear lineage |
| **v33** | 98,152 | 5 | 26 | **0** | **already rewritten once** — "the orchard with two kinds of ground", but the elevator and the arithmetic-of-the-base paragraph are gone |
| v34–v38 | 117k–125k | 8 | 34 | 2–3 | **clear prose restored** |
| v39, v40 | 126,225 / 125,295 | 8 | 34 | 3 | clear |
| **v41** | **124,430** | **8** | **35** | **3** | **clear — the best text** |
| **v42** | 81,103 | 3 | 32 | **0** | **code-switch: rewritten** |
| v43, v44 | 84,723 / 93,271 | 3 | 32–40 | 0 | rewritten form |

## 4. When it was replaced

**v41 → v42.** The v42 change log (`manuscript_ECOMOD_v42_CHANGELOG_v41_to_v42.md`) states it plainly:

> "**Introduction rewritten** as a research-question introduction (indicator aggregation → composition →
> what a model can and cannot say → the three questions → contributions), with the literature positioned
> in one paragraph instead of a list."

The rewrite was deliberate and its rationale is not silly — v42 was restructured into a
question-first research article with three propositions. But an *introduction restructuring* silently
carried a **prose loss** that the changelog never lists. That changelog is meticulous about numbers:

> "Numeric-token audit: every number in v41 appears in v42 main or SI…"

There is no equivalent prose audit. The hen, the harvest arithmetic, the "already failing by its
reserve" line — none appear in the v42 change log, and none survive in the file.

Then the C-series inherited the v42 form: C11 (2026-10-28) already shows the rewritten paragraph, and
`ecomod_continued_10`, C15, C16, C17, C18, C19, C20 all carry it byte-identical. C15's
`revision_record.md` claims it "Restored exactly — both orchard/elevator analogies" — it restored the
**v42-derived** form, which is why the loss survived a step advertised as a restoration.

## 5. Where the "junk" register came from

`tools/MANUSCRIPT_STYLE_POLICY.md` rule 7 forbids metaphor apologies — *"Remove: 'the metaphor is not
an empirical claim'"* — and v42's introduction rewrite is where its advice was applied to this
paragraph. The result is a paragraph that apologises for itself three times in five sentences. v41 has
none of that scaffolding because it was written before the policy was applied to it.

**So the sequence is: clear prose (≤v41) → v42 rewrite under a style policy meant to *improve*
readability → a paragraph that is measurably less readable than what it replaced.**

## 6. What should happen

The v41 text is not something I need to compose. It exists, it is yours, and it is strictly better
documented than what is in the manuscript now. The options, for your decision:

1. **Restore v41's three paragraphs** in place of the current §1 analogy block (C20 and the follow-up),
   keeping the v42/v44 structure around them. No claims, numbers or scope change — only the prose that
   was lost in the restructuring comes back.
2. **Restore v41 and keep a shortened version of the current framing**, if any of it earns its place.
3. **Leave it**, on the grounds that the paper is mid-submission and a §1 rewrite is not free.

I recommend (1). It is the only option that puts your argument back in your voice, and it is the one
option the changelog's own prose-audit gap would have flagged had it existed.

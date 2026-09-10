# Manuscript Style Policy (standing, all papers)

Applies to every manuscript in this project from 2026-09-10 onward, without needing to be
restated per paper. Enforced by `tools/manuscript_style_scan.py` (exit 1 on any BLOCKER)
and by `.github/workflows/manuscript-style.yml` in CI.

The audience is domain experts. They want **claims, methods, evidence, implications**.
They do not want project reports, technical diaries, or implementation summaries.

---

## Hard rules (BLOCKER — must not ship)

**1. No reference to unpublished or superseded versions of the manuscript.**
Superseded drafts are never published and are superseded anyway. A journal article is not a
changelog. Never write "earlier versions of this article", "v15 reported", "the previous
draft", "as printed in the source".

**2. No self-correction narrative.**
Do not narrate the authors' own prior mistakes: "that was an error, and it is corrected
here", "we previously stated", "this has been fixed". Silently state the correct result.
The sole exception is where a correction carries genuine methodological or pedagogical
value for the reader — and even then it must be framed as a substantive point about
method, never tied to an unpublished draft of this paper.

**3. No phantom or strawman contrasts.**
The manuscript may debunk or contrast positions **in the published literature**, with
citation. It may not argue against naive positions nobody holds, or against unpublished
work, or against its own earlier drafts.

**4. No project-diary register.**
Remove "in this pass", "post-freeze layer", "freeze-discipline record", "pre-score
protocol file", "the machine layer", "this round", "we then implemented". Describe what
the method *is*, not the order in which the authors did it. Where provenance genuinely
matters (protocol status, what was fixed before scoring), state it once, factually, in a
single short paragraph.

**5. No editorial, self-praise, or self-assessment.**
Remove "this is a strength", "the paper is honest/rigorous/careful", "this paper guards
against that failure in its own presentation", "we are careful to". Also remove
promotional adjectives: "novel", "unprecedented", "state-of-the-art". Let the result
carry itself.

**6. No metaphor apologies / naive over-hedging.**
Readers understand that an orchard analogy is not an empirical claim about global ecology.
Saying so explicitly reads like "note: the map is not the territory". Remove:
"the metaphor is not an empirical claim", "this needs one sentence, not a parable",
"the narrative that usually carries the point", "should not be taken literally",
"is only an analogy".

**KEEP legitimate scope statements.** These are not hedging and must survive: what was
tested, on what data, under what estimator, what does not generalise, what the design
cannot identify, conditional-hindcast vs operational-forecast status. The distinction is
that a scope statement constrains *the claim*; an over-hedge apologises for *the prose*.

---

## Soft rules (REVIEW — judgement call)

**7. Project-internal coinages.** Terms like "negative certificate", "machine layer",
"observation fibre", "class-level incompatibility", "safe-set map", "specification-matching
discipline" are invisible to readers. Replace with plain equivalents, or define once at
first use and then speak normally. A coinage that *is* formally defined in the paper
(e.g. "scored ladder" via a numbered definition) is acceptable.

**8. Editorial intensifiers.** "Importantly", "notably", "crucially", "it is worth noting".
If the sentence matters, its content shows that.

**9. Stacked hedges.** "may possibly", "could potentially". One hedge is enough.

---

## Usage

```bash
# single paper
python3 tools/manuscript_style_scan.py path/to/paper.tex

# whole directory, machine-readable, CI-style
python3 tools/manuscript_style_scan.py latex/*.tex --json style_report.json
echo $?     # 1 if any BLOCKER
```

Run it before every commit that touches a manuscript, and before any submission.

---

## Applied history

| paper | blockers found | status |
|---|---|---|
| `paperE1_cod_forecast_ladder` | 13 → 0 | cleared in v18 |
| `paper1_assessment_separation_v23` | 4 | **outstanding** (orchard/parable apology + self-commentary, §1.1) |
| `paper3_material_ledgers_v32` | 0 | clean |
| `paper5_sampled_governance_v26` | 0 | clean |
| `paperE3_edwards_forecast_ladder_v16` | 0 | clean |
| `paperE4_edwards_intervention_v14` | 1 | **outstanding** ("post-freeze layer", §closed-loop re-check) |
| others (2, 4, E2) | 0 | clean |

---

## CI installation

`tools/manuscript-style.yml.workflow-template` is the GitHub Actions workflow. It is shipped
as a template because the token used for automated pushes lacks the `workflow` scope. To
activate:

```bash
mkdir -p .github/workflows
cp tools/manuscript-style.yml.workflow-template .github/workflows/manuscript-style.yml
git add .github/workflows/manuscript-style.yml && git commit && git push
```

(Requires a token with `workflow` scope, or a commit made through the web UI.)

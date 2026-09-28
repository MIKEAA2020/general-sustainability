# Lean audit — v42

Branch `lean-audit-v4`. Range: `a461d38` → (this push).

Build unchanged: **rc = 0, 60 jobs** (54 imported modules), zero
warnings, zero `sorry`, zero axioms.

---

## 1. The question, answered plainly

Two questions were put: are the papers up to date with everything in
this chat, and had I updated them.

**No, and no.** In this chat I have pushed Lean modules, READMEs v9–v17
and audits v28–v41. I have pushed **no paper edits**. The one exception
— repair A in the companion paper — was **already merged** when I
verified it in v41; `9a77531` added the draft and v12 carries the
content, but neither was done by me here.

## 2. The finding: the EBC paper has no knowledge of the Lean layer

`paper2_exact_belief_computation_v10.tex`:

| string | count |
|---|---|
| `Lean` / `formaliz` / `mechanized` / `machine-check` / `proof assistant` | **0** |

The entire 60-job layer is invisible in the paper. The gap runs in one
direction — **the theorems outrun the prose**, the inverse of the
defect this audit normally catches:

| the paper says | what now exists |
|---|---|
| `prop:deadline`: *"verified by direct simulation on the grid"* | **proved** — `deadline_law`, an `↔` over an arbitrary ordered field, `T` symbolic |
| `prop:ladder`: *"the ten ladder values by survivable-subset enumeration"* | **proved** — value `= M/\|S\|`, `\|S\|` symbolic |
| §methods: *"one deterministic script … standard library only"* | a 30/30 script **and** a machine-checked layer |

## 3. The root cause, and why a sentence-level fix would be shallow

The defect is not three wrong sentences. It is that **§Verification
methods describes an apparatus that predates the Lean layer**. Editing
the deadline sentence alone would leave the paper still claiming a
single script as its whole verification story. The fix is to describe
the apparatus as it now is, and to say which warrant each result
actually carries.

## 4. What was changed — `paper2_exact_belief_computation_v11.tex`

Three edits (v10 is never overwritten):

**(a) `prop:deadline`** — statement now reads *"verified by direct
simulation on the grid and, independently, by a mechanized proof"*; the
proof notes the layer establishes the threshold as an *equivalence* over
an arbitrary ordered field with `T` symbolic, so neither the grid nor
`T ≤ 4` is load-bearing.

**(b) §Verification methods** — a second paragraph describing the
mechanized layer (Lean 4, 54 modules, 60 jobs, no axioms, no oracle,
ordered-field interface only), noting the two apparatus were built
separately and agree where they overlap, followed by an explicit
three-way attribution:

* **Proved** — band structure, ladder value form, deadline threshold.
* **Enumerated, not proved** — the census, the 84 pairings, the
  83,521 → 545 deduplication, the `m ≠ 4` dimension-scope battery.
* **Simulated** — the `m = 5, 7` ball certificates; and the deadline
  grid check, now redundant but retained as a cross-check.

**(c) §Delimitations** — the blind-class restriction was motivated by a
passing citation to the companion's "class discipline". Now stated
precisely, **with the caveat that honesty requires**: the companion
proves the blind and observation-dependent recursions differ *in the
companion's model*; the correspondence with the cube is one of **form,
not type**, so it **motivates** the restriction rather than proving it
necessary. It does fix the meaning of the paper's open question: since
the disciplines differ strictly somewhere, whether a non-blind
discipline beats the pairs *on the cube* cannot be settled by transfer.

This is the one place where a superficially stronger claim was available
and deliberately not made.

## 5. Strengthening: only what is merited

Three candidate cross-paper strengthenings were considered; one was
rejected on the user's criterion.

| candidate | verdict |
|---|---|
| Make the blind-class restriction load-bearing on the companion's strictness | **Merited**, with the structural caveat above |
| State the two-method corroboration | **Merited** — it is evidence about reliability, which is what a methods section is for |
| Have the ladder cite the companion's formula | **Rejected** — the paper already invokes it; more would be padding |

## 6. A defect introduced and caught

The first draft used `\ref{bands}`, which has **no matching `\label`**
— it would have rendered as `??`. The band proposition is
`\label{prop:bands}` inside `\subsection{...}\label{hamming}`. Both
references corrected.

A second defect: `\noindent` was written with a single backslash in a
Python string, so `"\n"` was interpreted as a newline and the command
was destroyed. Repaired.

Post-fix integrity: **unresolved refs NONE**, braces balanced,
`itemize` environments matched.

## 7. Deliverables

* `arena agent 1/paper rewrites/latex/paper2_exact_belief_computation_v11.tex`
  (549 lines) — the first paper edit of this chat.
* `lean_README_v18.md`, this audit.

**Caveat, stated rather than hidden:** there is no `pdflatex` in this
environment, so v11 has **not been compiled**. Verification was by
reference resolution, brace balance, environment matching and
inspection — not by a build.

## 8. Open, and not yet checked

* The glance table reports **736** stored antichain while the abstract
  reports **496** stored maximal sets. Possibly different measures (ZDD
  nodes vs maximal sets), but not verified.
* Titles, abstracts and any supplementary material of the other papers
  have not been reviewed against the findings.

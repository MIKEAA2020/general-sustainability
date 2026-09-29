# Paper 9 — split into two papers, prior art added, 2026-09-29

## The defect that drove everything

`paper09_cod_certification_v30.tex` was **two complete LaTeX documents concatenated**, and it
did **not compile at all**.

| | Part I (E2) | Part II (Arv) |
|---|---|---|
| `\documentclass` | `[11pt]{article}` @ char 2,790 | `[10pt,twocolumn]{article}` @ char 116,643 |
| own preamble, `\begin{document}`, `\title`, `\maketitle` | yes | yes |
| `\end{document}` | char 116,595 | char 162,724 |
| words | 16,183 | 6,088 |

- `\part{E2}`, `\label{part:p9-a}` and the "How the parts fit together" `\paragraph` sat at
  chars 1,036–2,400 — **before** the first `\documentclass`. Fatal: *Missing `\begin{document}`*.
- `\part{Arv}` sat at char 116,612 — **after** the first `\end{document}` (116,595). LaTeX
  ignores everything past it, so all 46,127 chars and **38 labels** were dead text,
  including **all 14 labelled results** of the merged file.

**Compile proof (tectonic, figures stubbed):**

| file | pages | PDF |
|---|---|---|
| `v30` (merged) | **NO PDF** | 0 B |
| `v31` (Part I) | **35** | 203,967 B |
| `v1` (Part II) | **8** | 165,922 B |

Both new files compile with **zero errors and zero undefined references**.

## Why split, on content and merits

The user's criterion: *"merge or split, depending on contents and merit. is the work unified
enough to merit a single paper?"* It is not.

| marker | Part I (E2) | Part II (Arv) |
|---|---|---|
| `Schaefer` | 11 | **0** |
| `LRP` (Part I's central object) | 87 | **0** |
| `surplus production` | 3 | **0** |
| `exact rational` | 1 | **10** |
| `harvest-free` | 1 | **17** |
| `breach` | 2 | **27** |
| labelled results | **0** | **14** (all of them) |
| mentions of the other part | 2 | **0** |

- **Different method.** Part I fits Schaefer (1983–2007), floating point, N=20,000
  trajectories, B=2,000 bootstrap refits. Part II uses **no fitted model at all**, exact
  rational arithmetic.
- **No shared formalism.** Part II never mentions Schaefer, surplus production, or the LRP.
- **No shared literature.** Overlapping bibliography entries are *data sources only*
  (Regular et al. 2025; Schijns et al. 2021), not works of scholarship.
- **One-directional at best.** Part II never cites Part I.
- **Corroboration:** `arv` is a **separate unit in the authoritative eight-paper scope**, and
  Part II *is* `arv`.

The framing paragraph's one claimed link — that harvest-free contractions evidence
non-stationarity, which is why the constructive bound is regime-dependent — is
**motivational, not logical**. Part I establishes regime-dependence on its own
(post-moratorium 171 kt vs modern series 0 ± 8 kt); it does not use Part II's theorems.

## Result

- `paper09_cod_certification_v31.tex` — Part I, constructive (E2). 16,927 words, 35 pp.
- `paper09b_arv_certification_v1.tex` — Part II, obstructive (ARV). 6,970 words, 8 pp.

Neither required preamble surgery: both halves were already complete standalone documents.
`v30` is preserved untouched.

## Prior art — Part I (`v31`)

New `\subsection{Related work}`, inserted before `\subsection{2. Methods}`.

1. **Viability in fisheries** — Aubin (1991); Béné, Doyen & Gabay (2001) (time-of-crisis
   function as overexploitation indicator); Martinet, Thébaud & Doyen (2007) (viable recovery
   paths); Doyen et al. (2012) (stochastic viability, EBFM); Krawczyk & Pharo (2013);
   Krawczyk et al. (2013) (satisficing vs optimal control). All save the new ones were
   already in the bibliography.
2. **Robust viability kernel — NEW.** Regnier & De Lara (2015), *Environ. Model. Assess.*
   **20**, 687–698. Their definition is the object Part I computes, and their finding that
   uncertainty shrinks the kernel is the phenomenon Part I is built around. **What is new is
   the method of obtaining it:** numerically by descending set iteration there, versus a
   **collapse to algebra** here — two constants `C* = g(LRP) − |e| = 91.59` kt and
   `g_max − |e| = 215.2` kt reproduce the kernel table in closed form, and every rule's
   protection margin is exactly `C*` minus its catch.
3. **Harvest control rules / MSE — NEW.** Butterworth (2007), *ICES J. Mar. Sci.* **64**,
   613–617; Punt et al. (2016), *Fish Fish.* **17**, 303–334. Paper 9's own opening line
   ("reference points are usually defended by simulation") is a description of MSE. The delta
   is stated without rhetoric: an MSE verdict is **conditional on the operating model and the
   ensemble simulated**; the no-dominance verdict here falls out of an **identity** and holds
   for every rule in the class, including rules never simulated. **The narrowing is conceded:**
   MSE handles multiple objectives, implementation error and observation error simultaneously,
   which the scalar reduction gives up.

## Prior art — Part II (`v1`)

New `\section{Related work}`, inserted before `\section{Data and provenance}`.

**THE TENSION, NAMED RATHER THAN BURIED.** Part II certifies collapse steps as
**harvest-free contractions**. That looks like it contradicts the collapse literature:

- **Hutchings & Myers (1994)**, *CJFAS* **51**, 2126–2146 — collapse attributable *solely* to
  overexploitation.
- **Myers & Cadigan (1995)**, *CJFAS* **52**, 1274–1285 — tested whether an increase in
  natural mortality in H1 1991 caused the collapse; **did not support** that hypothesis;
  overfishing was sufficiently high to cause the collapse.
- **Myers, Hutchings & Barrowman (1997)**, *Ecol. Appl.* **7**(1), 91–106 — rejected the
  hypothesis that juvenile mortality is unrelated to fully recruited fishing mortality.

Resolution, stated precisely: those papers ask about the **historical cause** of the collapse;
Part II asks about the **arithmetic of the record** — was the step a contraction even at zero
removals? Both hold. Removals on top of a contractionary productivity term make things worse,
which `prop:moratorium` says outright (loss exceeds removals by certified factors while the
fishery was closing).

**Where a real tension remains, and is not resolved:** Myers & Cadigan specifically declined
elevated natural mortality as the explanation. To the extent harvest-free contractions are
read as evidence of a productivity collapse, they sit against that finding, and **this paper
does not adjudicate it** — the certificates are statements about transitions as recorded and
identify no biological mechanism.

**THE SERIES-DISCREPANCY CONCERN IS MET, NOT ASSUMED AWAY.** Myers et al. (1997) documented
that for these stocks the VPA-based and survey-based trends diverge — from the early 1980s
VPA shows a decline where the survey does not — plausibly from discarding. Any certificate
computed on one series inherits its artefacts. Part II therefore checks the raw survey
directly (`prop:survey`): certified factor `21797/2127417` over 1989–1994, falling **2.6×
further** than the assessment series over their common window. Robust to series choice, and
stronger in the raw survey than in the record the main certificates use.

Also added: **Aubin (1991)** for the viability framing (Part II's bibliography lacked it);
Hutchings & Myers (1994) was already present.

## Verification

- Both files: exactly 1 `\documentclass`, 1 `\begin{document}`, 1 `\end{document}`,
  1 `\maketitle` after stripping comments.
- All `\ref` targets resolve in both (Part I 0 refs/23 labels; Part II 16 refs/38 labels).
- Compiled with tectonic: 35 pp and 8 pp, zero errors, zero undefined references.
- Stub figures were used only for the compile check in `/tmp`; no stub was written into
  `/home/user/papers`.

## Caution on one earlier count

A first recount reported Part I as having 2 `\begin{document}` and 3 `\end{document}`. That
was a **false positive**: the provenance comment I had just added mentions those control
sequences, inflating the raw grep. Recounting with comments stripped gave 1/1/1/1. Same
failure family as the retracted paper-6 `sorry` grep — an unexamined raw grep reported as
evidence.

## Next

Papers 10 (depletion ledgers, 43,147 w — typology needs a measurable consequence) and
11 (forecasting baselines, 39,704 w) remain.

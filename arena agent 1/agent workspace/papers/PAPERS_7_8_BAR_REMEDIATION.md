# Papers 7 and 8 — bar remediation — 2026-09-30

## Why these two

Of the 15 current papers, 12 met the top-journal bar. Papers 7 and 8 did not, and for the
same fixable reason: **neither had a prior-art section**. Paper 8 had a second defect — its
18 numbered results were written as bold prose (`\textbf{Theorem 6.1 (...).}`) rather than in
labelled theorem environments.

Neither paper had ever been LaTeX-compiled before this turn.

## Compile baseline established first

| file | pages | bytes | errors | undefined refs |
|---|---|---|---|---|
| paper07 … v49 | 37 | 267,319 | 0 | 0 |
| paper08 … v43 | 46 | 335,706 | 0 | 0 |

Both compile cleanly. (An earlier run reported paper 7 as "2 pages" — that was purely
`\includegraphics` aborting on missing figure stubs, not a structural defect.)

## Paper 8: 18 results converted to theorem environments

Version: v43 → **v45**.

Source used no `\newtheorem` at all. Two dead ends before the working solution:

1. **`\newtheorem{theorem}{Theorem}[section]` failed.** The preamble sets
   `\setcounter{secnumdepth}{-1}`, so the section counter never steps and every result
   rendered as "Theorem 0.1", "Corollary 0.2", … — 30 phantom results instead of 18.
2. **`\newtheorem*` failed.** It wraps the optional argument in parentheses, giving
   "Corollary (2.1(Boundedness and global continuation))" instead of
   "Corollary 2.1 (Boundedness and global continuation)".

**Working solution**: a shared counter with a manually-set printed number.

```latex
\usepackage{amsthm}
\theoremstyle{definition}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{remark}[theorem]{Remark}
\newcommand{\resultnum}{}
\renewcommand{\thetheorem}{\resultnum}
```
then `\renewcommand{\resultnum}{6.1}` immediately before each `\begin{theorem}...\label{thm:6-1}`.

This reproduces the paper's existing manual numbering **exactly** (verified: 18/18 distinct
results identical to baseline, zero "Theorem 0.x" artefacts) while making `\label`/`\ref`
work — `\ref{thm:6-1}` prints "6.1".

`\theoremstyle{definition}` was chosen deliberately: the source wraps every statement in
`\emph{...}`, and under the default `plain` style that would flip the emphasis to upright.
`definition` keeps the original visual reading.

Result split: 5 theorems, 5 propositions, 4 corollaries, 2 lemmas, 2 remarks = 18.
Statement ends were found by locating `\emph{Proof.}`; the four results without proofs
(Remark 5.1, Corollary 5.1, Proposition 6.1, Remark 7.1) end at the next heading.

## Bug caught during the conversion

Applying all `\begin{...}` replacements first and then all `\end{...}` insertions corrupted
the text — replacements change string length, so the pre-computed insertion offsets were
stale. It split a word: "for as long as it ex|ists." with `\end{theorem}` wedged inside.
**Fix**: perform each result's replacement and insertion as one atomic operation, processed
in reverse position order.

## Prior art added

**Paper 7** (`\subsection{Related work}`, 4 strands): sampled-data control; periodic review
as practice and the interval as a design variable; continuous-delay literature and the
substitution this paper questions; position.

**Paper 8** (`\subsubsection{1.4 Related work}`, 5 strands): delays in population dynamics;
informational/knowledge delay; management delay as a cost; where this paper departs;
certification.

All citations verified against Crossref (DOI lookup) rather than written from memory:

| citation | verified |
|---|---|
| Shertzer & Prager 2007, *ICES JMS* 64: 149–159, doi:10.1093/icesjms/fsl005 | ✓ |
| Brown, Fulton, Possingham & Richardson 2012, *Ecol. Appl.* 22: 298–310, doi:10.1890/11-0419.1 | ✓ |
| Karlsson & Gilek 2020, *Ambio* 49: 1067–1075, doi:10.1007/s13280-019-01265-z | ✓ |
| Hocherman, Trop & Ghermandi 2025, *Ambio* 54: 2042–2059, doi:10.1007/s13280-025-02211-y | ✓ |
| Butterworth 2007, *ICES JMS* 64: 613–617, doi:10.1093/icesjms/fsm003 | ✓ |
| Butterworth & Punt 1999, *ICES JMS* 56: 985–998, doi:10.1006/jmsc.1999.0532 | ✓ |
| Punt, Butterworth, de Moor, De Oliveira & Haddon 2016, *Fish Fish.* 17: 303–334, doi:10.1111/faf.12104 | ✓ |
| Adamson & Hilker 2020, *Theor. Ecol.* 13: 425–434, doi:10.1007/s12080-020-00462-x | ✓ |
| Chen & Francis 1995, *Optimal Sampled-Data Control Systems*, Springer | ✓ |

Nine new entries for paper 7, four for paper 8, each inserted in correct alphabetical
position in the flat hand-formatted reference lists (neither file uses `\bibitem`).

## The substantive positioning

**Paper 8's** novelty is now stated against the literature rather than merely asserted. The
governance-delay literature uniformly treats delay as a cost — more is worse, the question is
how much is tolerable (Shertzer & Prager; Brown et al.; Karlsson & Gilek; the 2025 review of
101 studies). Paper 8's central finding is **different in kind**: under the mobilising rule,
*intermediate* delay stabilises, within a window bracketed by two interval-certified
subcritical Hopf crossings. Because the window is bounded above, this localises the range
over which the literature's monotonicity holds rather than contradicting it. The 2025
review's own methodological call — that response lags must be decoupled from ecosystem lags —
is met by construction, since these models carry governance delay and no ecological delay.

**Paper 7's** positioning is that the question it asks is *prior* to the delay literature's:
whether substituting a continuous lag for a sampled review is admissible at all. Sections 3.3
and 4.1 show it is not, so results about the continuous operator do not transfer.

## Result

| file | pages | bytes | errors | undefined refs |
|---|---|---|---|---|
| paper07_sampled_governance_v50.tex | 38 (was 37) | 274,064 | 0 | 0 |
| paper08_governance_delay_v45.tex | 47 (was 46) | 341,947 | 0 | 0 |

Both verified by PDF text extraction: Related work heading present, new in-text citations
present, and paper 8's 18 results numbered identically to baseline.

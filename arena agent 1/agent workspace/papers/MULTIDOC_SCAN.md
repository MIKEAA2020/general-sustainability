# Set-wide multi-document scan — 2026-09-30

## What was found

A scan of all LaTeX files for the paper-9 failure mode found **three** merged files that were
actually multiple complete documents concatenated. In every case the `\part` merge marker sat
in the **gap between documents — outside any document** — which is why the merge never worked.

| merged file | docs | outcome |
|---|---|---|
| `paper09_cod_certification_v30.tex` | 2 | split → `v31` (E2) + `paper09b_arv_certification_v1` |
| `paper10_depletion_ledgers_v51.tex` | 2 | split → `v52` (ledgers) + `paper10b_edwards_aquifer_v1` |
| `paper11_forecasting_baselines_v61.tex` | 3 | split → `v62` + `paper11b_edwards_forecast_v1` + `paper11c_worked_systems_audit_v1` |

Papers 1–8 were clean throughout.

## Why it mattered

LaTeX stops at the first `\end{document}`. Every document after that was **silently dead text** —
no error, no warning, just missing pages.

| merged | pages | PDF |
|---|---|---|
| `v30` | **NO PDF** | 0 B |
| `v51` | **NO PDF** | 0 B |
| `v61` | **NO PDF** | 0 B |

None of the three compiled at all. In `v30` and `v51` there was a further fatal cause: content
(`\part`, `\paragraph`) sat **before** the first `\documentclass`, giving *Missing
`\begin{document}`*.

## After the split

| paper | pages | PDF |
|---|---|---|
| `paper09_cod_certification_v31` (E2, constructive) | 35 | 203,967 B |
| `paper09b_arv_certification_v1` (ARV, obstructive) | 8 | 165,922 B |
| `paper10_depletion_ledgers_v52` (typed flux ledgers) | 55 | 393,179 B |
| `paper10b_edwards_aquifer_v1` (Edwards J-17) | 17 | 131,022 B |
| `paper11_forecasting_baselines_v62` (Northern cod) | 41 | 240,533 B |
| `paper11b_edwards_forecast_v1` (Edwards forecast) | 21 | 134,496 B |
| `paper11c_worked_systems_audit_v1` (Ws) | 12 | 200,939 B |

**7 papers, 189 pages recovered from 0.** All compile with zero errors and zero undefined
references.

## Split criterion used

The user's criterion: *"merge or split, depending on contents and merit… is the work unified
enough to merit a single paper?"*

- **Papers 9 and 10**: split, on **zero** vocabulary overlap and **zero** cross-reference.
  Paper 10's halves: `ledger` 135/0, `Edwards` 0/22, `pumping` 0/70. They shared a study
  system but no method, formalism, result set or literature.
- **Paper 11**: split into three, but on **different** evidence — D1 and D2 *do* share a method
  and *do* cross-cite. They were split anyway because **the author already treats them as
  separate companion papers under separate review**, each with its own Zenodo DOI, stating
  explicitly that scores are never pooled and no retention verdict is transferred. D3 (`ws`)
  shares no vocabulary with either and is a separate unit in the authoritative eight-paper
  scope.

## Current set state

| | files | status |
|---|---|---|
| Current versions | 26 | **all clean** — 1 `\documentclass`, 1 `\begin{document}`, 1 `\end{document}`, all `\ref` resolved |
| Archived originals | 3 (`v30`, `v51`, `v61`) | intentionally preserved, multi-doc |

## Root cause

The 2026-09-29 content-and-merits partition assembled merged papers by **naive concatenation**
of complete LaTeX source files, leaving each file's `\documentclass`, preamble,
`\begin{document}`, `\maketitle` and `\end{document}` in place, and placing the `\part` markers
outside all documents. No compile check was run at assembly time.

## Recommendation

Any future merge in this project should be compile-verified immediately. The check is cheap:

```python
c = "\n".join(re.sub(r'(?<!\\)%.*$','',l) for l in src.split('\n'))
assert c.count('\\documentclass') == 1
assert c.count('\\begin{document}')  == 1
assert c.count('\\end{document}')    == 1
```

Note the comment-stripping: a raw grep over a file whose provenance header mentions these
control sequences gives a false positive. That error was made once here and caught.

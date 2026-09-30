# Paper 11 — split into three papers, prior art added, 2026-09-30

## The defect

`paper11_forecasting_baselines_v61.tex` was **three** complete LaTeX documents concatenated —
2 more `\documentclass`, 3 `\begin{document}`, 3 `\end{document}` — the worst instance of the
assembly bug found in this set. `\part{E3}` and `\part{Ws}` sat in the **gaps between
documents**, outside any document, so nothing past the first `\end{document}` compiled and
**Parts II and III (141k chars, 19.2k words) were dead text.**

| | chars | words | title |
|---|---|---|---|
| D1 | 139,352 | 20,048 | *Does a surplus-production ladder improve forecasts of Northern cod? A scored test on NAFO 2J3KL* |
| D2 | 64,194 | 8,819 | *Does a one-pool water-balance model improve forecasts of Edwards Aquifer head? A scored test at J-17* |
| D3 | 74,770 | 10,374 | *Exact Audits of Worked Systems for the Obstruction Calculus: Counts, Witnesses, and Monitoring* |

**Compile proof (tectonic, figures stubbed):**

| file | pages | PDF |
|---|---|---|
| `v61` (merged) | **NO PDF** | 0 B |
| `v62` (Northern cod) | **41** | 240,533 B |
| `v1` (Edwards forecast) | **21** | 134,496 B |
| `v1` (Worked systems) | **12** | 200,939 B |

All three: **zero undefined references, zero LaTeX errors.**

## Why three — the decisive evidence

Unlike papers 9 and 10, whose halves had **zero** cross-reference, **D1 and D2 explicitly cite
each other as separate companion papers**, each with its own Zenodo DOI:

- D2: *"A **companion study under separate review** applies the same scored design to a marine
  fishery stock (Northern cod, NAFO 2J3KL)… The two systems' scores are never pooled, and no
  retention verdict is transferred between them."*
- D1: *"The same scored design is applied to a groundwater system, the Edwards Aquifer, Texas,
  in Abaee (2026…). The two systems' series are not pooled, and no retention outcome is
  transferred between them."*

The author already treats these as separate papers; the concatenation was purely an assembly
artefact.

D3 shares no vocabulary with either (`forecast` 1, `scored` 0, `ladder` 1, `Northern cod` 0,
`Edwards` 0; versus `obstruction` 24, `witness` 12, `audit` 81). It is `ws` — **a separate unit
in the authoritative eight-paper scope.**

## Result

- `paper11_forecasting_baselines_v62.tex` — Northern cod, 20,648 w, 41 pp.
- `paper11b_edwards_forecast_v1.tex` — Edwards Aquifer, 9,295 w, 21 pp.
- `paper11c_worked_systems_audit_v1.tex` — Worked systems, 10,924 w, 12 pp.

`v61` preserved untouched.

## Prior art

**D1 (`v62`) — new `\subsection{Related work}`.** The core finding is that *no*
surplus-production module is retained against last-value persistence on either specification.
The cross-domain anchor for that is **NEW**: the M-competitions (Makridakis, Spiliotis &
Assimakopoulos 2018, *IJF* **34**(4), 802–808; 2018, *PLoS ONE* **13**(3), e0194889; 2020,
*IJF* **36**(1), 54–74) — in M4 all six pure ML methods performed poorly, none better than the
combination benchmark and only one better than Naïve2. **The scope difference is stated, not
claimed away:** M4 aggregates 100,000 series and 61 methods; this is one stock under two
specifications. Also positioned against the collapse/non-recovery literature (Myers, Hutchings
& Barrowman 1997; Hutchings 2005) — that literature establishes the empirical fact, this paper
measures what it does to *forecast skill* from a fixed origin. And an explicit non-claim: the
predictand is retrospectively reconstructed with catch supplied along the horizon, so this is a
**conditional hindcast, not an operational forecast evaluation**.

**D2 (`v1`) — new `\subsection{Related work}`.** Positioned against the groundwater-level
forecasting literature (Daliakopoulos, Coulibaly & Tsanis 2005; Adamowski & Chan 2011), with
the departure stated: the contribution is **not a new forecasting model but a locked evaluation
design applied to a familiar model family**, with the negative result as the finding — the
ladder, baselines and rule were fixed before any score was read, and a protocol clause declines
the best one-step forecaster (M2m). **The mechanism is named:** annual recharge is near-white
(r(R_t,R_{t−1}) = 0.17) while the head increment is strongly coupled to contemporaneous
recharge (r(ΔH,R) = 0.74), so a model that persists last year's recharge persists a quantity
with almost no memory; given realised fluxes the same map nowcasts well (7.55 ft), which
separates a forecasting failure from a structural one. Added Hyndman & Koehler (2006) and
Makridakis & Hibon (2000).

**D3 (`v1`) — new `\subsection{Related work}`; the largest gap in the set.** This half's
bibliography had **six surnames total** — Abaee, Baccelli, Cohen, Olsder, Quadrat, Wiley —
four of which are one book. It cited **no viability theory and no verification literature.**
Six verified entries added:
- **Aubin (1991)** *Viability Theory* — the founding framing, previously absent.
- **ARCH-COMP** (Althoff et al. 2020; Geretti et al. 2020; EPiC Series in Computing vol. 74) —
  the verification community's annual friendly competition applying tools to fixed benchmark
  problems. **This paper's worked-systems family plays the analogous role for the obstruction
  calculus.** The difference is stated: ARCH benchmarks are reachability problems solved by
  reachability tools; these are information-constrained viability problems under partial
  observation, tabulating survivable belief-pair counts, kernel sizes under policy-class
  restrictions, and minimal witness-set sizes. No reachability tool computes these.
- **Farkas (1902)** (the duality certificate); **Helly (1923)** (tightness of the sparse
  witness); **Baccelli, Cohen, Olsder & Quadrat (1992)** (max-plus, already cited, now
  contextualised).

## Error caught

A first draft of D1's section referenced `\ref{sec:power}` — a label **I invented**; it does
not exist in the document. Detected by the `\ref`-vs-`\label` check and replaced with plain
text before compiling. Had it shipped, it would have produced a `??` in the PDF.

## Verification

- All three files: exactly 1 `\documentclass`, 1 `\begin{document}`, 1 `\end{document}` after
  stripping comments.
- All `\ref` targets resolve in all three (2, 0 and 29 refs respectively).
- Compiled: 41, 21 and 12 pages; zero errors, zero undefined references.
- Stub figures created only under `/tmp/p11`; none written into `/home/user/papers`.

## Status

This closes the systemic multi-document defect: papers 9, 10 and 11 all split; papers 1–8
verified clean. See `MULTIDOC_SCAN.md` for the final set-wide scan.

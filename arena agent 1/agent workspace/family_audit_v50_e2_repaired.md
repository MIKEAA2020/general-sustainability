# E2 v25 — the Schaefer/Fox leak is repaired

**Pushed `ef806a6`** — `paperE2_cod_intervention_v25.tex` + v25 battery.

## What was wrong

Result 3.3 computed the constructive bound as
`g(K*) − |e_q10| = 172.46 − 80.87 = 91.59` kt. The `172.46` is the **Schaefer**
surplus at the reference point; the `80.87` is the erosion constant of a
**different functional form** — the Fox fit, frozen in
`campaign_e2_fox_form_srcyear.py` (`e_q10 = -80.87 kt … the Fox fit`).

The Schaefer fit's own floors are min −460.03, q05 −318.76, **q10 −114.85**, so

```
172.46 − 114.85 = 57.61 kt      (committed optimiser: 57.62)
```

**Ruled out the alternative explanation.** Before editing I checked whether
"source-year" was itself what moved the floors. It is not: re-fitting under both
catch conventions gives q10 = −114.85 (annual) and −82.29 (regime). Neither is
−80.87. The Fox campaign's docstring confirms the elevation layers froze the q10
floor at **−114.85** — i.e. every downstream number (K-grid, stochastic
viability, bootstrap) was computed with the *correct* floor. Only the label 91.6
was wrong.

**Corroboration.** The paper's own bootstrap 90% interval for the bound is
`[0, 87.1]`. A point estimate of 91.6 lies outside its own interval — impossible.
57.6 sits inside it.

## What v25 changes

| item | v23/v24 | v25 |
|---|---|---|
| constructive bound (10 occurrences) | 91.6 kt | **57.6 kt** |
| Result 3.3 worked line | `172.46 − 80.87 = 91.59` | `172.46 − 114.85 = 57.61` |
| q05 companion quantity | `172.46 − 287.36 = −114.9` | `172.46 − 318.76 = −146.3` |
| perpetual-worst companion | −156.5 kt | −287.6 kt |
| φ threshold | `1 − 80.87/296.09 = 0.727` | `1 − 114.85/296.09 = 0.612` |
| φ criteria at 0.25 / 0.5 / 0.75 | 141.2 / 67.2 / −6.8 kt | 107.2 / 33.2 / −40.8 kt |
| K-grid endpoints | −32.2 → 91.6 kt | −62.9 → 57.6 kt |
| "corrective shift from 57.6 to 91.6" | asserted | removed; the bound is 57.6 |
| "makes the 60-kt rules protective" | asserted | reversed (60 kt → boundary 900.3 > 884.6) |
| "reproduced byte for byte" | claimed | "to nine significant figures" |

The φ=0.25 and φ=0.5 conclusions are unchanged in direction (both still
positive, kernel still the whole safe set); φ=0.75 still fails. Only the values
move.

Battery: **29 passed, 0 failed** (was 23/6).

---

# Flaw inventory — entire chat

## Corrected and pushed

| flaw | fixed in |
|---|---|
| minimax: 8192 printed where 16384 was computed (survived six versions) | v12, `fcc30c05` |
| EBC verifier computed 496 but required 736 (self-inconsistent, passed 30/30) | v13, `45469b1` |
| psuff, Repair A | v14, `d491826` |
| SI v2→v3; `viacert` resolvable 12/12 contrary to v45 | `e87ea20` |
| README v21 / audit v46 | `7bcda722` |
| obstr v56, E3 v17, E4 v16 batteries | `b5bc11de` |
| E1 v60 + E2 v24 declarations (Funding, Code availability, responsibility) | `d800c0a` |
| **E2 Schaefer/Fox leak + byte-for-byte claim** | **v25, `ef806a6`** |

Sperner is "cited, not formalized" by decision and is not reopened.

## Open — found, not corrected

1. **E2 §3.8 stochastic viability does not reproduce from the committed
   elevation campaign.** Paper: P ≥ 0.8 crossings at 81.2 (i.i.d.), 72.3
   (blocks), 105.2 (no-1992) kt. Campaign: 47.5, 37.5, 95.0. Paper: survival at
   the bound 0.74 / 0.73 / 0.85; campaign at 57.6 kt: 0.77 / 0.79 / 0.88.
   Bootstrap 90% interval: paper [0, 87.1], campaign [0.000, 84.777]. These are
   **not** caused by the Fox leak — the campaign froze the floor at −114.85.
   Either the paper is stale w.r.t. the campaign, or the campaign changed.
   **Merits revision**, but I will not hand-edit Monte-Carlo numbers I cannot
   reproduce.
2. **E2 certified horizon "to T = 7".** Depends on the floors; I left it and did
   not verify it against −114.85. Needs checking.
3. **E2 Figure 2.** The caption now says 57.6 kt. The PNG
   (`figs_e2/fig2_kernel_vs_catch_v21.png`) should be confirmed against the
   campaign's regenerated `fig2_kernel_vs_catch.png`.

## Battery gaps, not paper defects

E3 v17 pins **0 of 8** abstract numbers; ARV v9 **0 of 8**; obstr v56 3/8;
E4 v16 3/8; E1 v60 2/2 pinnable (14 legitimately unpinnable). These say the
*batteries* are thin, not that the *papers* are wrong.

Sabotage tests were never run for ws v17, comp v20, psuff v14, EBC v13 — their
green counts are unproven.

## P3 v32 / P4 v41 / P5 v47 — no revision merited on present evidence

I did **not** build batteries for them, and I recommend against it unless you
want the assurance for its own sake. A structural sweep (point estimates outside
their own intervals; table rows not summing to stated totals; abstract numbers
absent from the body) found **zero** defects across all three. Their existing
`verify_retained_rows.py` checkers verify concordance ID/citation sets only.

Pulling three more pipeline trees and recomputing their headline claims is a
large investment with no prior evidence of a problem — exactly the expenditure
you asked me not to make. The honest status is *unchecked numerically*, not
*clean*.

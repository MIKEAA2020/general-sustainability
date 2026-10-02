# Family audit v48 — the empirical footprint: correcting v47

**This note retracts a specific claim in v47.** v47 §2.1 said:

> **The program's entire empirical footprint is one fish stock.** E1 and ARV both
> work Northern cod, NAFO 2J3KL.

**That is wrong, and I should not have written it.** I measured the eight papers
you listed and generalised from them. The repository holds a larger programme —
at least fifteen live manuscripts across three tracks — and its empirical work
spans **six independent real-world systems in four domains**. Everything below
was verified today against the repo tree, the file contents, and the API.

---

## 1. What is actually there

### 1.1 Six empirical systems

| # | system | papers | data in repo |
|---|---|---|---|
| 1 | **Northern cod, NAFO 2J3KL** | E1, E2, ARV | DFO 2016 assessment + 2025 reassessment, NCAM M-shift SSB, xteNCAM vintage, RV fall survey, Schijns 3-century catch reconstruction, capelin acoustic index — 8 CSVs under `wave_e_cod/data/` with a `SOURCES.md` |
| 2 | **Edwards Aquifer, J-17 index well** | E3, E4 | TWDB J-17 head, EAA discharge 1934–2023, USGS recharge 1934–2024, USGS Comal Springs gauge, CPC ONI, PSL Niño 1/3/3.4/4, SOI — 8 inputs under `wave_e_edwards/data/` with a `SOURCES.md`, plus an exploratory second pool (J-27 well, Barton Springs gauge) |
| 3 | **Multi-stock fisheries screens** | paper5 | RAM Legacy cohorts — **454** distinct `stockid` in `v466_broader_cohort.csv`, **415** in `v444_adh_cohort.csv`, a **55,605**-row B/BMSY panel. The paper's screen itself is 42 stocks with a 32-system cross-sector case search |
| 4 | **Peru–Chile anchoveta + ENSO** | (analysis track) | SAU catch reconstructions, Niño 1/3/3.4/4 and SOI, with a frozen-input battery and rerun logs under `anchoveta_enso/verify/` |
| 5 | **Global land and footprint accounts** | ECOMOD / SI line | GFN world biocapacity & footprint 1961–2022, NFA land-type 1961–2023, OWID cereal yield / production / cropland, FAOSTAT crop index, 2ndFOR above-ground biomass |
| 6 | **Typed-ledger applications** | paper3 | public-data classifications: G3P anomaly index, phosphate reserve-life ratio, and a third |

Two of these (1 and 2) are full **wave-E replications** with a frozen
pre-scoring protocol, dated before any score was computed — the strongest
empirical design in the programme.

### 1.2 `research_program`

A parallel 1,890-file track, 25 articles A001–A025, including
`article_004_phosphorus`, `article_005_groundwater`, `article_014_northern_cod`,
`article_011_periodic_review`, `article_012_delay_dynamics`,
`article_013_component_accounting`. It carries a
`validated_computations/` directory of 96 files doing computer-assisted
analysis — Krawczyk operators, interval enclosures, Moore–Spence folds,
piecewise-Chebyshev stages, preregistered second-fold searches — and 107
`external_reviews/`. This is not a footnote; it is a second research programme.

### 1.3 Releases

Two pre-releases, three assets, 278 MB, both targeting `main`:

| tag | date | assets |
|---|---|---|
| `compendium-v1.0` | 2026-09-04 | `workspace-01a00d79…zip` (142.0 MB, 10 downloads) |
| `edwards-framework-e1` | 2026-09-12 | `workspace-edwards-ecomod.sustainability.zip` (58.9 MB, 5 dl); `workspace-edwards.framework.2nd.zip` (77.3 MB, 3 dl) |

Body text on the newer release reads only *"ecomod-sustainability workspace"*.
These are whole-workspace archives, not per-article deposits — there is no
versioned, citable data release tied to any single manuscript.

---

## 2. The programme already answered question 2 — and it changes the answer

`research_program/paper_types_and_venues_decision.md` (2026-08-29, 15.9 KB) is
a venue strategy for a **nine-paper set** (five core + four wave-E), two
conditional papers, and a monograph. A second memo,
`paper2_venue_and_split_recommendation.md` (2026-08-28), handles paper 2.

| paper | type | primary venue | alternates |
|---|---|---|---|
| P1 assessment separation | theory/methods | Environmental Modelling & Software | Ecological Modelling; Ecological Economics |
| **P2 obstruction calculus** | **mathematics** | **Set-Valued and Variational Analysis** | JMAA; MMAS (only if the 2A/2B split fires) |
| P3 material ledgers | methods/formal | Ecological Modelling | J. Industrial Ecology; EM&S |
| P4 delay dynamics | applied nonlinear dynamics | Comm. Nonlinear Sci. Numer. Simul. | Nonlinear Dynamics; JEDC |
| P5 sampled governance | methodology + case study | ICES J. Marine Science | CJFAS; Fisheries Research |
| E1 cod ladder | empirical forecast evaluation | Fisheries Research | ICES JMS; CJFAS |
| E2 cod intervention | applied management (short) | Fisheries Research (short comm.) | ICES JMS; CJFAS |
| E3 Edwards ladder | empirical forecast evaluation | Groundwater | J. Hydrology; Hydrogeology J. |
| E4 Edwards intervention | applied management | J. Water Resour. Plan. Mgmt | Water Resour. Mgmt; WRR |

Three consequences for the question you asked:

**The criteria differ per paper, and I applied the wrong ones in v47.** I judged
obstr against a generic "top journal" standard including *"empirical or applied
contributions of broad practical interest."* But obstr is routed to **SVVA — a
mathematics journal**, deliberately, as a pure-proof corpus with proofs in
electronic supplementary material. "Broad practical interest" is not the
criterion there; correctness, depth and fit to set-valued analysis are. My
v47 criticism of obstr on applied breadth was aimed at a target the programme
never chose. E1 is routed to *Fisheries Research*, E3 to *Groundwater* —
specialist applied venues where a single well-executed case study is the norm,
not a weakness.

**An external review already delivered the harsh verdict, and the response was
sound.** The memo records the review's line — *"Will not pass peer review at any
mainstream sustainability science venue"* — and explicitly **accepts it as a
constraint on venue choice, not as a verdict on the science**, rerouting the
apparatus-bearing papers to methods and formal venues. It also rejects the
review's harsher options: no rewrite from scratch (the non-loss rule and pin
discipline require transformation with verifiable provenance), and no deletion
of the claim-ledger discipline (the review itself conceded it is *"a legitimate
methodological contribution"*). That is the right set of calls.

**Nothing is submitted.** The memo states plainly: *"no paper is represented as
formatted for, or submitted to, any venue; the venue rows above are the
evaluated routing, to be executed per paper at its venue pass."* So the v47
question "do they meet the bar" is, at the programme's own reckoning, still
open — the venue passes have not been run.

### 2.1 Two obligations registered in that memo: one closed, one partly closed

**E3/E4 literature engagement — closed.** The memo registered: *"the Edwards
pair's reference lists are exclusively data agencies — journal-submission
readiness requires engaging the peer-reviewed forecasting/groundwater-modelling
literature."* That is no longer true. E3 v16 now cites Adamowski & Chan (2011,
*J. Hydrol.*), Daliakopoulos et al. (2005, *J. Hydrol.*), Diebold & Mariano
(1995, *JBES*), Küensch (1989), Makridakis et al. (2020, M4), Scanlon et al.
(2003), Ropelewski & Halpert (1986), Nölscher & Broda (2026), Hu et al. (2026).
E4 v15 has ten references. The gap is closed.

**P5's computational tier — partly closed.** The memo called this *"the one
material strengthening obligation in the set"*: P5's screen was nominal-tier
with *"code not committed."* The code is now in the repo —
`screen_battery_v31.py`, `screen_extensions_v34.py`, `adh_verify.py`, the cohort
CSVs and results JSONs. But it sits under
`other documents/analysis/paper5_aug08_originals/`, and **P5's text names none
of it** — there is no code-availability pointer and no battery. The letter of
the obligation is met; the spirit is not.

---

## 3. What changes in the assessment, and what does not

**Withdrawn from v47:** the "one fish stock" claim and the argument built on it
that the family cannot claim applied breadth. The programme has real breadth.

**Revised, not withdrawn:** the criticism should be redirected. The programme is
not short of empirical breadth — it is short of **machine-checked** empirical
breadth outside the cod leg. Concretely:

| paper | battery | status |
|---|---|---|
| E1 v59 | 73/73 | green, sabotage-tested |
| ARV v9 | 250/250 **+ 11/11 figure assertions** | green (figure script re-run today) |
| E2 v23 | **none** | pipeline under `wave_e_cod/src/` |
| E3 v16 | **none** | pipeline under `wave_e_edwards/src/` |
| E4 v15 | **none** | pipeline under `wave_e_edwards/src/` |
| P3 v32 | **none** | `verify_retained_rows.py` exists, not named |
| P4 v41 | **none** | `verify_retained_rows.py` exists, not named |
| P5 v47 | **none** | screen code exists, not named |

Six of the fifteen manuscripts have no assertion battery at all. The Edwards
leg — the programme's second empirical system, and the one that most needs to
convince a hydrology referee — is reproducible by pipeline but not checked by
assertion. Given that the entire minimax lineage v2–v11 turned out to be
unfalsifiable while reporting clean, "reproducible by pipeline" is materially
weaker than it sounds.

**Unchanged from v47:** the obstr gap (no battery, and one unsupported
"machine-verified… regenerates the table verbatim" claim for `tab:patch`), the
minimax findings, the self-citation load, and the abstract-density note.

**Softened:** my suggestion to consolidate `minimax` into `obstr`. The programme
has already considered splitting paper 2 and decided **against** it (single
paper to SVVA, B-1 families monograph-carried). Consolidation is therefore a
bigger departure from the recorded plan than I implied, and the owner should
weigh it against that decision rather than on my say-so. The `ebc` → `psuff`
suggestion stands; nothing in the memos addresses the notes.

---

## 4. Revised bottom line

Against the programme's **own** chosen venues, the picture is considerably
better than v47 painted it:

- **E1 → Fisheries Research** is a strong fit: real data, a pre-frozen scoring
  protocol, an honest null result, and the best artifact in the family (73/73).
- **E3 → Groundwater** is a credible fit now that the literature gap is closed,
  and the Edwards leg doubles the programme's empirical domain coverage.
- **P5 → ICES JMS** has the broadest empirical asset in the programme (42-stock
  screen, 32-system cross-sector search) and reads as the most likely
  general-interest paper of the set.
- **obstr → SVVA** is defensible on novelty, but carries the two gaps already
  recorded: no battery, and 19.0k words against the memo's planned 14–16k main
  text with ESM proofs.

The single highest-value action is unchanged from v47 and now better supported:
**build assertion batteries for obstr and for the Edwards leg.** Those are the
two places where a strong claim currently rests on an unverified artifact, and
today's minimax result is the object lesson in why that matters.

---

## 5. Method and caveats

- Tree enumerated for `lean-audit-v4` (5,959 blobs) and `main` (5,826). **`main`
  is a strict subset** — zero files exist only on `main` — so `lean-audit-v4` is
  the superset branch and the complete picture.
- Data files were downloaded and inspected directly (RAM cohorts row-counted,
  not assumed). All fetched payloads were size-checked; no 404 body was read as
  content.
- The two release zips (278 MB) were **not** downloaded; only their metadata was
  read. Their contents are unverified.
- I did not run the Edwards or paper5 pipelines, only the ARV figure script.
  Whether `wave_e_edwards/src/` reproduces E3/E4's printed numbers is untested.
- The venue table is the programme's own evaluated routing, not evidence of
  submission or acceptance.

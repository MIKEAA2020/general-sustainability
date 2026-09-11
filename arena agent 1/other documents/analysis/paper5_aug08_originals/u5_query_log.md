# U5 query log — case-screening table provenance (2026-09-11)

Accompanies `u5_case_table.csv` (32 systems, zero eligible under §2.6 criteria
(i)–(iv)). Each entry records the search performed, the source obtained, and
the rows it supports. Curated inventory, not a systematic review (§2.6).

## 1. Repository searches (GitHub API; no clone)

| # | Query / action | Result | Rows |
|---|---|---|---|
| R1 | Recursive tree @HEAD (4367 entries), path grep for case/query/screen/eligibility/iceland/cod/eta/lemma/rank/RAM/review-interval terms | Located analysis corpus: `paper5_aug08_originals/` (RAM cross-section, cod/sprat discrimination, droop, sampled-governance records), `anchoveta_enso/`, `ram_adh_fisheries/`; no pre-existing case table | all (corpus) |
| R2 | Code search: `query log OR case table OR screening table` (441 hits, top 15 inspected) | All hits are mentions of the table/log as missing; no pre-existing table exists | — (absence) |
| R3 | Code search: `0.387 OR 0.143 OR peak-to-trough` (1 hit) | Sole record: `cod_sprat_discrimination.md` (unreverified provenance note) | 21, 22 |
| R4 | Code search: `T_r-ranked` (1 hit) | Sole record: recommendations memo ("never executed") | — (test spec) |
| R5 | Release `compendium-v1.0` (2026-08-26) workspace ZIP, 2086 files; listing grep + targeted extraction of 162 text files | `tau_window_search.md` (20-system fishery screen, 2026-08-08); `ram_target_stocks.csv` (58 RAM stocks); `ram_crosssection.py/.log` (42-stock cross-section); `cod_sprat_*`; `sampled_governance_results.md` (T_r test spec, window tables); `droop_test_results.md` | 1–20 (re-verdicts), 21–22 (provenance) |
| R6 | `paper4_delay_dynamics_v30.md` (delay companion), parameter table + limitations | η=0.914 declared Candidate-A baseline, explicitly uncalibrated ("institutional coefficients have not been identified from field data") | — (η basis) |
| R7 | `grok claude paper 5.txt` + `JOINT_AUDIT_EVALUATION.md` (review record) | E7 text recovered (Lemma 2.2 apply-or-drop; Prop 2.1 demotion); prior decline was scope-only | — (E7) |
| R8 | `A014_northern_cod_revised.md`; `formal_result_inventory.md` (article 011) | Table-2 values cross-confirmed; case table + query log listed as missing program-level artifacts | — (register) |

## 2. Public-data pulls

| # | Action | Result | Rows |
|---|---|---|---|
| D1 | ICES standardgraphs stock list → source-data tables: cod.27.5a (key 22640), had.27.5a (key 22494); parsed to `ices_cod_27_5a.csv` (1955–2026), `ices_had_27_5a.csv` (1979–2026) | Post-1995 SSB CV: cod 0.394 (confirms 0.387), haddock 0.359; post-2013 haddock SSB CV 0.243 | 21, 22 |
| D2 | RAM Legacy v4.66 `ram_target_stocks.csv` (58 stocks, repo) + `ram_crosssection.py` re-execution | Bit-identical reproduction (42 stocks n≥20); regime column = annual-TAC groups | T_r test |
| D3 | ICES advice table (cod.27.5a catch/TAC series, web) | Corroborates catch scale; not used numerically | 21 (context) |

## 3. Web searches (2026-09-11; first-page results inspected, primary sources preferred)

| # | Query | Source used | Rows |
|---|---|---|---|
| W1 | ICES cod.27.5a stock assessment data download | standardgraphs.ices.dk endpoints (keys above) | 21, 22 |
| W2 | Murray-Darling water allocations responsive storage inflows | SA Dept for Environment and Water allocation announcements; BoM National Water Account 2024 (MDB) | 26 |
| W3 | BLM grazing allotment adjustments responsive monitoring | BLM Instruction Memorandum 2018-109 (flexibility); outcome-based grazing authorizations | 27 |
| W4 | Scandinavia moose harvest quotas responsive monitoring | Månsson et al. 2011 (Wildl. Biol. 17:176–190, quota-setting); Solea et al. 2021 (climate–recruitment); Sand et al. 2020 Sci. Rep. (wolf-predation response) | 28 |
| W5 | Norway salmon aquaculture traffic light biomass sea lice | PubMed 38609075 (regional coordination); doi:10.1080/13657305.2025.2602481 (TLS design, 13 areas, 2017+) | 29 |
| W6 | Iceland haddock harvest control rule adopted year | government.is management-strategy page (HCR adopted April 2013, 35% of B45cm+); hafogvatn.is advice page (rule formula) | 22 |
| W7 | cod.27.5a standardgraphs stock data XML | stockList.aspx (key lookup) | 21, 22 |

## 4. Re-verdicting rule (rows 1–20)

The 2026-08-08 tau-window screen used continuous-delay criteria (r·g band +
τ-class), not the §2.6 criteria. Each row was re-adjudicated: (i) from the
Management/TAC-cycle column (responsive rule vs fixed/held/deadlock/none);
(ii) from the τ-estimate column (dateable continuous lag vs irregular);
(iii) from the mechanism-of-gap analysis + case knowledge (competing driver
present in every responsive row); (iv) from series availability (RAM/assessment
series = yes). Binding fail recorded per row; non-binding cells marked `yes`
only where the cited evidence supports them, else `~`.

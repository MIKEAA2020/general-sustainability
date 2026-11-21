# NFI Data Use Agreement (V8_1) — clause-by-clause review

Source: `batch 9/agent 2/NFI data use agreement_English_V8_1.pdf` (3 pp). Retrieved and read 2026-11-21.

## Obligations and where each is already satisfied

| # | Clause | Obligation | Our compliance | Where |
|---|---|---|---|---|
| 1 | Use | Data used only for the purpose requested; derived products must acknowledge Canada's NFI | Objective in R1 states the purpose exactly | R1 Objectives block |
| 2 | Distribution | No distribution beyond authorised users | We publish national/ecozone aggregates only, never plot records | R1 Deliverables; F16 data statement |
| 3 | Interpretation | **Ecozone or national level only**; low-intensity sample may not represent smaller areas | R1 Study Area = Canada (national); no jurisdiction inference | R1 form, Study Area row |
| 4 | Updates | Products revised without notice; **record version number and access date** | Not yet done — must be logged on receipt | to do |
| 5 | Plot locations | Confidential; ±10 km rounding; no plot visits | Requested ±10 km; no field work planned | R1 Request Details |
| 6 | No warranty | No accuracy guarantee; metadata must be read | Already treat compiled values as provider-compiled | F16 §Canada |

## Citations the agreement prescribes

Use verbatim, with access dates:

- **Ground-plot data:** National Forest Inventory. 2026. *Canada's National Forest Inventory – ground-plot data, version 5.0.* (requests fulfilled **November 2026 or later**)
- **Data dictionary:** National Forest Inventory. 2026. *… ground plots data dictionary, version 5.3.2.*
- **Compilation procedures:** National Forest Inventory. 2021. *… ground plots compilation procedures, version 2.4.*
- **Standard reports cited in F16:** National Forest Inventory. 2025. *First Remeasurement Standard Reports, version 3.1.*

Note the mismatch worth flagging to Michael if it matters: the agreement lists photo-plot dictionary **v6.1** for the second remeasurement, while MAGPlot v1.3 (deferred) is a separate compiled product. Not a blocker.

## One consequence for the paper

The agreement's "revised without notice" clause plus the version requirement means the F-paper must state a **frozen data version and access date**, not "the current NFI data". Any number derived from the extract is then tied to version 5.0 (or whatever is delivered). This is already how the F16 text treats every other provider product — NFA Edition 2026, Luke API pulls, MapBiomas collections — so it costs nothing, but it must be written in, not assumed.

## Still open with Michael

1. When does the review period end, and who are the collaborators?
2. `BMEQ_*` → published-equation mapping (his team, pending).
3. Whether NFI will publish a short note that change RSE tables are withdrawn, so we cite a document rather than a private email.

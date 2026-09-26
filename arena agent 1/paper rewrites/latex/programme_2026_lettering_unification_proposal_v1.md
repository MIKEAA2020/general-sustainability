# 2026 lettering collision — evidence, registry, and unification proposal

**Date:** September 26, 2026. **Status:** decision-ready; execution gated on owner approval (cross-cutting convention change). **Flagged at:** round 27 report; re-flagged in rounds 28–30 session summaries.

## 1. The collision, verified line-by-line

Every Abaee self-citation in the nine live manuscripts is author-year lettered, and the letters are assigned **per paper**, not globally. The same letter denotes different works in different papers:

| Work cited | Programme six (minimax v11, comp v18, ws v17, ebc v10, psuff v11; family keying since round 25) | ARV v9 (local) | E1 v59 (local) | paper1 v62 (JMCDA, sealed) |
|---|---|---|---|---|
| ARV — robust viability (Zenodo 22552060) | **2026a** | — (self) | **2026c** | unlettered (2026) + title |
| P1 — obstruction calculus | **2026b** | **2026a** | **2026d** | unlettered (2026) + title |
| ws — worked systems | 2026c | — | — | — |
| comp — computational certification | 2026d | — | — | — |
| psuff — probabilistic sufficiency | 2026e | — | — | — |
| ebc — exact belief computation | 2026f | — | — | — |
| minimax — dual certificates | 2026g | — | — | — |
| Edwards Aquifer deposit (22552680) | — | — | **2026a** | unlettered (2026) + title |
| sampled-governance deposit (22554297) | — | — | **2026b** | — |
| forecast-ladder deposit (22553609) | — | **2026c** (as "frozen specification" preprint) | — (self) | unlettered (2026) + title |
| calibration data record | — | **2026d** | — (uses the files directly) | — |
| typed flux ledgers (22554177) | — | — | — | unlettered (2026) + title |

Evidence lines: E1 v59 references (`2026a` Edwards, `2026b` sampled governance, `2026c` robust viability, `2026d` obstruction calculus); ARV v9 references (`2026a` obstruction calculus, `2026c` forecast ladder, `2026d` calibration record); psuff v11 references (`2026a` = "Robust viability of the 2J3KL limit reference point…" = ARV); paper1 v62 references (all "Abaee, A. (2026)." + italic title + DOI).

## 2. Why it matters

1. **Companion exposure:** ARV (CJFAS) and E1 (IJF) are companion submissions on the same stock. "Abaee (2026a)" means the ARV paper in E1's list and the obstruction calculus in ARV's list; an editor or referee holding both manuscripts sees the same label denoting different works.
2. **Theory-pool exposure:** the six theory papers share referee pools (Automatica briefs/regulars; TAC/SICON/MoOR margins). Within the six the keying is consistent (round-25 family keying) — the exposure is only where their lists meet ARV's or E1's.
3. **Audit-trail cost:** every cross-paper audit (rounds 25–30) has had to carry the two-layer keying translation; a single registry removes a standing error source. (The never-mix rule for the two paper-1 lineages is a symptom of the same disease.)

Each paper is *internally* consistent — nothing is technically broken — which is why this is a convention decision rather than a defect repair.

## 3. Options

- **A (recommended): extend the family keying repo-wide.** The six theory papers' alphabet becomes the global alphabet; new works take the next letters:
  - `2026h` = forecast-ladder deposit (22553609; E1's own deposit — cited by ARV and others as 2026h; E1 itself does not self-cite)
  - `2026i` = Edwards Aquifer deposit (22552680)
  - `2026j` = sampled-governance deposit (22554297)
  - `2026k` = calibration data record
  - `2026l` = typed flux ledgers (22554177) — reserved; used only where cited
  The registry lives in the supersession map next to the family-keying table. paper1 v62 keeps its unlettered title-distinguished style (sealed package, internally consistent, DOI-anchored); its entries map onto the registry without edits.
  - **Execution cost (one round, on approval):** ARV v10 — replace `2026a`→`2026b` (3 in-text sites), `2026c`→`2026h`, `2026d`→`2026k`, reorder reference block alphabetically; E1 v60 — `2026a`→`2026i`, `2026b`→`2026j`, `2026c`→`2026a`, `2026d`→`2026b`, reorder; regenerate both verifiers' needles; full gates. The six theory papers: zero changes (already conformant).
  - **Benefit:** "Abaee 2026X" unambiguous across all live manuscripts and every future audit; the map's family-keying table becomes complete rather than partial.
- **B: keep local keys, add titles at every cross-citation.** No edition churn, but clutters text and leaves the bibliographic collision in place.
- **C: numeric deposit keys ("Abaee, 2026-ARV").** Unambiguous but nonstandard for author-year venues; worst submission-polish outcome.

## 4. Related conventions this decision settles

1. The ECOMOD manuscript (separate "productivity illusion" lineage) uses its own local `2026a/2026b` — same treatment at its next edition if A is adopted.
2. Future deposits join the registry at the next letter; the map's table is the single source of truth.
3. Zenodo deposit **titles** remain owner-side (the carried refresh item); the lettering fix is independent of it.

## 5. Owner decision (September 26, 2026)

**Letter-free formal citation adopted. No new versions for this.** The
two-tier scheme (unlettered title-distinguished reference entries;
in-text plain "(Abaee, 2026)" when unique, shortened-title form when
several 2026 works are cited) is the family convention from now on, and
it **rides the next organic edition** of each affected manuscript — no
standalone version-creating round is to be executed for citation form.

Concrete disposition:

- **ARV / E1:** apply the scheme to their deposit/preprint keys at their
  next organic editions (whenever substantive content next changes).
  Until then the shipped editions stand as-is — internally consistent;
  the collision remains documented in the registry table above for
  audit purposes only.
- **New manuscripts:** apply the letter-free scheme from birth.
- **Cover letters, submission portals, data statements:** letter-free
  immediately (no versions involved).
- **Sealed packages** (paper1 v62 JMCDA, ECOMOD v37): untouched — v62
  already uses the unlettered entry style.
- The global lettering registry (2026a–l) is **not adopted**; the table
  in §1 remains as the audit-trail record of the historical keying.
- Standing rule added: **never create editions for citation-form
  changes alone.**

- **Owner override (round 32, September 26, 2026, executed in place):**
  "cite formally without letters" applied programme-wide immediately,
  including the theory cluster's internal keying — superseding the
  rides-on-organic-editions deferral above for all live manuscripts.
  Superseded editions stay byte-frozen lettered; sealed packages
  untouched; the standing rule against citation-only editions remains
  in force for the future (this round was explicit owner execution).

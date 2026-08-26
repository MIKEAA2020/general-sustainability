# General Sustainability Programme — Versioned Compendium Archive

**Release v1.0 (26 August 2026).** This repository is the programme's **versioned reproducibility compendium**, released together with the programme's **monograph working preprint**. It holds the proof corpus, the registers and concordances, the corrected articles, the validated computations with committed code and data, and the scored real-system trees — the reference and verification layer for the planned journal papers.

## What is released here

| Product | Entry point | Status |
|---|---|---|
| **Monograph working preprint v1.0** | [`revised_sustainability_manuscript.md`](revised_sustainability_manuscript.md) | Clearly labeled working preprint — a public, citable record of the architectural kernel ahead of peer review; will be updated or superseded by the definitive monograph if one is written after the papers pass external scrutiny |
| **Versioned compendium archive** | this repository (tag `compendium-v1.0`) | Bookkeeping + verification + versioning + gated-conditional archival; contains **no separately unpublished mathematical claims** — every theorem is routed to a planned paper, the conditional docket, or the negative register |

The publication architecture is **journal-first**: five planned journal papers (see [`batch 2/03_publication_strategy/PUBLICATION_STRATEGY.md`](batch%202/03_publication_strategy/PUBLICATION_STRATEGY.md) and [`research_program/revised_optimal_publication_architecture_A001_A025.md`](research_program/revised_optimal_publication_architecture_A001_A025.md)); the monograph is deferred to Wave 3 and is optional. The compendium is not a book: it is the artifact layer that journal articles cannot host (full proof corpus, code/data/hashes, non-loss retention).

## Contents map

| Path | Contents |
|---|---|
| `revised_sustainability_manuscript.md` | The monograph working preprint v1.0 (earlier drafts: `general_theory_of_sustainability_*` files; traceability: `revised_manuscript_traceability.md`) |
| `PROOF_MANIFEST.md` | **Register of record**: every theorem with its honest status, every computation artifact with its SHA-256 and reproduction command, the Wave E support table, the reproducibility/disclosure status |
| `revised_articles/` | The corrected articles A001–A025 (the sources of the planned papers) |
| `batch 2/` | The proof corpus: result records R01–R09, elevation documents E1–E7, open-problem registers, publication strategy |
| `batch 4/` | The repaired theorem records, the proof-elevation adjudication, and the reaudit suites |
| `reaudit/` | Verification suites (444+ assertions over the repaired corpus) |
| `research_program/` | The compendium registers: canonical schema TCS-1.0, the 409-row concordance routing every source item to its publication destination (machine row-verification executed; two intake collisions repaired), claim ledger, the two closure packets, external-review registry |
| `research_program/validated_computations/` | The interval-certified computations (A025 Hopf, C4 orbit Krawczyk, off-grid residual, monodromy, E5 admission) with code and artifacts |
| `wave_e_cod/`, `wave_e_edwards/` | The scored real-system forecast ladders (Northern cod; Edwards J-17 aquifer) — data, code, results, working manuscripts |
| `uploads/` | The original source manuscripts of the programme (provenance layer; referenced by the claim ledger and article inventories) |

## Status discipline (read before citing anything)

- **Independent rerun:** the five committed Part II certificates (A025 Hopf, C4 orbit Krawczyk, C4 off-grid residual, C4 monodromy dt=0.25, E5 admission) and both Wave E scored trees were independently rerun on 2026-08-26 by a second agent on a different toolchain — Hopf, E5, and the monodromy hash-identical; Krawczyk and off-grid re-certified at a nearby Newton centre; scored trees 30/30 byte-identical (`batch 4/VALIDATED_COMPUTATIONS_RERUN.md`, `batch 4/WAVE_E_RERUN.md`). The A025 fold pipeline and the C4 monodromy at dt=0.1 remain NOT REBUILT. Original artifacts were computed by a single AI agent (Z.ai Code) on one machine. See `PROOF_MANIFEST.md` → "Reproducibility status".
- Theorem statuses are honest: `PROVEN`, `PROVEN (reconstructed)` (same-agent reconstruction pending independent line-by-line re-verification), `COMPUTED_PARTIAL`, `NOT CONFIRMED`, withdrawn/false where applicable. The manifest is the authoritative status register.
- The Wave E scored trees are **single-run forecast-ladder artifacts with an independent byte-identical rerun, not kernel certificates**; no real-system transfer claim is made (the R04 five-map certificate is not constructed).
- The E5 interval-verified admission is a method demonstration on a linear toy module only; Wave E Part III support rows remain NOT CONFIRMED (no specification frozen, no matching performed).

## Curation

Working notes — AI-commissioning prompts, raw AI transcripts, and the standalone disclosure working note — were removed from the release tree (they remain retrievable in git history at commit `270f5f7`). The original source manuscripts in `uploads/` were **retained** as the provenance layer. See [`RELEASE_NOTES.md`](RELEASE_NOTES.md) for the complete curation log.

## How to cite

- The preprint: see the suggested-citation block in `revised_sustainability_manuscript.md`.
- The archive: *General Sustainability Programme — Versioned Compendium Archive, v1.0* (tag `compendium-v1.0`), with `PROOF_MANIFEST.md` as the companion status register.
- Individual theorems/computations: cite the register row in `PROOF_MANIFEST.md` and the source file it points to.

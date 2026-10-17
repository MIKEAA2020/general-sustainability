# Paper08 v51 changelog — 2026-10-17

**Base:** Published Paper08 v50, preserved unchanged. This authorized successor corrects only the first-page title/abstract ordering.

## Front-matter correction

- Moved `\date{October 17, 2026}` and `\maketitle` ahead of the abstract in `paper08_governance_delay_v51.tex`.
- The title, author/contact block, and date now precede the unchanged abstract on page 1. Keywords and the table of contents follow.
- No abstract wording, scientific claims, equations, data, numerical results, or supplementary material changed. A normalized source comparison confirms the abstract is byte-identical and all content outside the edition header/front-matter block is byte-identical to v50.

## Build and pagination

Tectonic 0.15.0 produced an 86-page PDF. The body starts on page 4 (v50: page 5); the table of contents was regenerated with the corresponding page references. The final page-1 visual check shows title before abstract, with no overlap or clipping. The full build record and exact file hashes are in `paper08_governance_delay_v51_BUILD_LOG_2026-10-17.txt`; the version and layout audit is in `PAPER08_V51_LAYOUT_AUDIT_2026-10-17.md`.

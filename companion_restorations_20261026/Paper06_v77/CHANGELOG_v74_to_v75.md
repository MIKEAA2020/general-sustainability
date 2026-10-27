# Changelog: Paper06 v74 → v75

**Parent:** Paper06 v74, preserved unchanged. V75 is a separate source-edited derivative.

## Prose changes

- Reworked §§1.1–1.2 from Gemini’s supplied humanized drafts as the sentence-level base, rather than using Grok as the structural or stylistic base. The opening question, accessible transition from fixed profiles to transitions, and plain-language explanation of the quantifier fork are retained in source-checked form.
- Preserved the v74 citation set and manuscript order. The literature claim is bounded to “much of this work”; unsupported claims about a literature-wide blind spot, fair weight selection, observed policy practice, generic failure, or a “clean bill of health” were not imported.
- In §1.2, retained shared physical-safety, destination, and universal-disturbance requirements for both `E_w` and `E_typ`; both floor tests apply over the full tube and successor set. The quantifier formulas state their domains and set membership, and the full-cone identity is explained.
- Kept Table 1 unchanged. The here-and-now/wait-and-see comparison is explicitly limited to an analogy for quantifier order.
- Replaced the generic illustration with a source-bounded account of the action-indexed four-plan witness. At `(x,s₁,s₂)=(1/2,6/5,6/5)`, `s₁+s₂=12/5≥2`; every full-cone weight licenses FAST or SLOW, but no plan in the declared menu is typed-admissible. No claim is made about all real-world menus.
- Updated current-edition, file-name, source-path, and SI labels to v75. The abstract, contribution list, theorem statements, proofs, model, parameters, numerical results, and substantive SI text are unchanged.

## Validation

- Built main and SI with Tectonic 0.17.0: 48 and 40 pages, respectively.
- No unresolved `??` markers, undefined-reference messages, missing-file errors, or fatal build errors.
- Main/SI URI-link counts remain 12/9, with target multisets matching v74.
- SI extracted text matches v74 after normalizing `v75` to `v74`. Main extracted text differs after that normalization only on pages 2–3.
- Warning-signature multisets match v74 after normalizing source filenames and line numbers: 46 main and 69 SI warnings. Existing warnings remain.
- Main pages 2–4 were visually reviewed; all seven figure files are byte-identical to v74.
- Modular and assembled §§1.1–1.2 were checked for exact synchronization. The new v75 directory passed whitespace and source-diff checks before publication.

V74 and all earlier releases remain unchanged. V75 is a separate archive-branch directory, not a DOI deposit.

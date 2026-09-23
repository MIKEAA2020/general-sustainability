# hidden_parameter_learning_v1 — addendum

**Lineage:** `hidden_parameter_learning_v1` (standalone name from birth; no paperN prefix — the
naming rule adopted after the paper-2 prefix lesson). **D-item:** Hidden Parameters (D10)
of Track D (source: `uploads/suggested generalizations.txt`).

**Content.** Augmented beliefs; probe reveals theta exactly (branch separation 2); probe threshold 21/10; learning-deadline identity z0 >= 21/10 + T_learn/10 (T_learn = 0..4); kernel antitone 5>4>3>2; two-patch unknown-regeneration instance.

**Verification.** Exact rational/integer arithmetic; stdlib only;
deterministic. 6/6 check families:
E1 theta-observed 16/16; E2 probe threshold 21/10; E3 deadline identity T_learn = 0..4; E4 injective revelation (separation 2); E5 antitone chain 5>4>3>2; E6 unknown-regeneration instance.

**Build.** Tectonic 0.15.0, first build: 0 overfull boxes; 2 pages;
67522 bytes; post-build probes pass (title/author/ORCID/AI declaration/
no unresolved references/declarations block).

**Defects found during verification (before ship).** The post-learning law initially applied u=+1 on both branches instead of u=theta, yielding empty kernels; corrected to u=theta (drift 9/10). The claim 'T_learn >= 4 empties the grid' was false (the top cell 25/10 survives); corrected to the inclusive threshold identity z0 >= 21/10 + T_learn/10 at T_learn = 0..4.

**Status.** Shipped to `latex/` (tex + pdf + verify + this addendum) via
cp + cmp; source zip `hidden_parameter_learning_v1_source.zip` (4 entries); pushed to the
programme repository under the batch commit for this item.

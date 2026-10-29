# Governance P4 v41 audit — R01

Read **AUDIT_GOVERNANCE_P4_V41_20261029_R01.md** first. This package audits the precise governance working paper cited in ECOMOD C17. It does not modify either manuscript or replace the paper with an older deposited version.

## Reproduce the independent checks

Tested with Python 3.13. Install the pinned packages in `requirements_R01.txt`, then run from this directory:

```bash
python src/verify_governance_R01.py
python src/check_mixed_delay_R01.py
python -m unittest discover -s src -p 'test*_R01.py' -v
python -O -m unittest discover -s src -p 'test*_R01.py' -v
```

The first two commands regenerate the two result JSON files; they do not edit the manuscript. Execution is bounded and ordinarily takes seconds, not the original campaign's multi-million-year integrations. The tests include a separate direct-ODE implementation of the native ZOH map.

`mpmath.iv` checks use outward interval arithmetic at 80 decimal digits. Serialized interval endpoints use exact integer conversion from binary endpoints to outward decimal bounds. The scalar checks certify local frequency roots/phase images, not nonlinear RFDE Hopf bifurcations. The mixed-channel witness certifies a Hurwitz finite Jacobian at zero delays and a right-half-plane characteristic root at protective delay 110 years. It does not contradict the pure-protective no-Hopf theorem or weighted small gain inside its certified region.

The global continuation, long-horizon histories, fold Krawczyk pipelines, Lyapunov coefficients and maturation-delay computations were **not independently rerun**. Fold certificate observations are record inspections, not newly established continuum theorems. Finite sampled-data grids are not universal cadence certificates. No empirical model fit or field validation was performed.

## Sources and integrity

`data/source_registry_R01.json` identifies 14 governance sources at the C17-pinned commit and both C17 citation sources by Git blob and SHA256. It records the main HEAD against which v41 was confirmed latest. Original paper/campaign files remain at their existing repository paths; they are not unnecessarily duplicated here. The external-reference JSON records selected source context and the failed supplementary-PDF retrieval; it is not a republication of the external article.

`artifact_manifest_R01.json` covers every package artifact except itself. Re-running result generation or tests can change environment/timing fields and therefore invalidate the archived manifest, even when the scientific results agree. Do not overwrite the published R01 package; use a new revision if changing it.

## Publication safeguards

`src/publish_governance_R01.py` is the one-shot authorized additive publisher. It requires `--publish`, privately reads the credential file, checks a fresh main HEAD, rejects pre-existing package/receipt paths, preserves every prior non-tree path/mode/hash, uses non-force updates and byte-verifies new files. It archives a separate publication receipt in a second additive commit. **Do not rerun it after successful publication.** Neither the private credential nor downloaded caches belong in this package.

Report scope: substantive bounded mathematical/numerical and citation audit, not a full formal proof review, exhaustive novelty search, global simulation replication, or empirical validation.

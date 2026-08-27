# A025 fold pipeline m=96 / m=128 — fresh same-environment rerun, hash-identical (2026-08-26)

**Scope note (honest):** this is a same-environment second-session rerun of the
committed code (`a025_fold_pipeline.py` at HEAD) using the invocations recorded
in the artifact-manifest builder (`build_artifact_manifests.py`). What it
verifies: committed-code reproducibility, determinism, and freedom of the
artifacts from the first-run session's uncommitted state. What it does not
verify: numerical stability across library versions (the cross-toolchain
standard of the Task-29 Part II reruns remains available). **All four
artifacts reproduce BYTE-IDENTICALLY** — the m=96/128 first-run limitation is
discharged at the same level as the m=64 and dt=0.1 reruns.

## The invocations matter (a documentation note)

An initial rerun attempt with the pipeline's DEFAULT arguments
(`python3 a025_fold_pipeline.py 96` / `128`) reproduced every headline verdict
(tau_f to 12+ digits, INSIDE the lost interval, |M| at the same 1e-12 scale)
but NOT the bytes: the default path takes a different continuation route (48
accepted points vs the committed 45, m=96) because the committed runs used
non-default arguments — recorded in `build_artifact_manifests.py` but easy to
miss. With the recorded arguments the reproduction is exact. The lesson
(recorded here): the invocation arguments are part of the reproducibility
contract; the builder's command strings are the canonical record.

## Verdict reproduction (all re-observed, byte-identical)

| quantity | m=96 (committed = rerun) | m=128 (committed = rerun) |
|---|---|---|
| tau_f (fold) | 5.587236198663 | 5.587236198663 |
| in lost interval | INSIDE (dist 2.66e-11) | INSIDE (dist 2.69e-11) |
| \|M\| (MS residual) | 3.311e-12 | 7.442e-12 |
| T_f | 315.322196 | 315.322196 |
| N_pk_pk | 22.3583 | 22.3629 |

The lost certificate interval is [5.587236197890, 5.587236199490] (the
committed m=64 interval Krawczyk certificate). All three resolutions
(m=64/96/128) agree to ~2.7e-11 in tau_f — the spectral-convergence
cross-check re-established on fresh executions.

## Hashes (committed pins == rerun outputs, verified identical)

```
7b2e1c14ce93b923fbea37ef9e721d48113c31a3a74e26419579c292c331d715  a025_fold/a025_moore_spence_fold_m96.npz
c952aa08e1f4702440d2ecb96a3da725388afc180748a76d6a5b76d6c0758180  a025_fold/a025_branch_continuation_m96.json
6025254279ea68432a339e5c5a8bd4cf994044fa4039e6de864370d279e83424  a025_fold/a025_moore_spence_fold_m128.npz
baba85aafa2ecb412f28ab0e03decf817dff5d615b1437cf8f2aebd58bde5fc8  a025_fold/a025_branch_continuation_m128.json
```

## The recorded invocations (the canonical reproducibility contract)

- m=96 (exit 0, 205 s, console log `rerun_console_m96.log`):
  `python3 research_program/validated_computations/a025_fold/a025_fold_pipeline.py 96 --dtau-min 5e-6 --tau-end 5.62`
- m=128, two steps (exit 0, 313 s + 13 s, logs `rerun_console_m128_fresh.log`
  / `rerun_console_m128_resume.log`):
  `python3 research_program/validated_computations/a025_fold/a025_fold_pipeline.py 128 --dtau-min 5e-6 --tau-end 5.62`
  then `... 128 --dtau-min 5e-6 --tau-end 5.62 --resume-ms`
  (the committed m=128 artifact is the output of the resume step, whose input
  npz is the fresh step's output — both steps re-executed here from scratch).

The default-argument attempt's console logs are kept as
`rerun_console_m96_defaults.log` / `rerun_console_m128_defaults.log` for the
record of the continuation-path difference noted above.

## What this does and does not close

- CLOSED: the first-run limitation on the m=96/128 resolution cross-checks —
  all four artifacts are rerun hash-identical on fresh executions of the
  committed code with the recorded invocations. Every post-v1.0 computation
  (the dt=0.1 monodromy, the fold m=64/96/128, both intervention legs) is now
  rerun-verified.
- NOT closed: the interval Krawczyk stage of the fold pipeline (unchanged
  status: unimplemented); the cross-toolchain standard (available to a future
  rerun).

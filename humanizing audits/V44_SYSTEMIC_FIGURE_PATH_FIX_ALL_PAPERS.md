# V44 round record — the systemic figure-path fix applied to ALL papers (the "31-path" class closed) + the v41 line-2055 report diagnosed and closed

**Task 103, 2026-09-19.** Owner directives: *(1)* "what do u mean: the 31-path
systemic figure fix for the other papers? if there's something wrong with the
figures, fix it." — the explanation requested and, with that sentence, the
owner authorization to execute it; *(2)* fix the reported errors on
`paper4_delay_dynamics_v41.tex` — *"Package pdftex.def Error: File
`figs_p4/fig2_five_regime_topology_v2.png' not found: using draft setting"* at
line 2055, with the matching input-line warning. A PAT was supplied for the
push.

---

## Part I — the two questions, answered

### 1. What "the 31-path systemic figure fix" meant — and that it is now done

When Task 101 fixed the P4 missing-figure error (V42), it also scanned **every
tex file in `latex/`** and found the *same latent bug class* in the *other*
papers: of the **45 distinct figure paths** referenced across the 150 texs,
most figure PNGs lived **one directory above `latex/`** (`paper
rewrites/figs_e1…figs_p5/`), reachable only through the `\graphicspath{{../}}`
fallback. Every in-repo build therefore worked — but any compile of a
downloaded/copied `latex/` folder (Overleaf upload, flat download, journal
portal upload) would hit **exactly the pdftex.def error the owner had just
reported on P4**, for every one of those papers. Task 101 flagged the class
(V42 Part III, "31 paths") but took no action — those papers belong to other
waves — so it waited for an owner decision. This round's directive *("if
there's something wrong with the figures, fix it")* is that decision, so the
fix is applied to all of them, mechanically, additively, with the same
verification discipline as Task 101.

**The fix:** every referenced figure folder now also lives **inside `latex/`**
(byte-identical copies, sha256-verified): `figs_e1/` (8 files), `figs_e2/`
(10), `figs_e3/` (5), `figs_e4/` (1), `figs_p5/` (7) — plus the four older
`figs_p1/` files referenced by superseded P1 versions (`fig1_witness_v22.png`,
`fig1_witness_v25.png`, `fig1_witness_v26.png`, `fig2_weight_intervals_v31.png`)
into the already-existing `latex/figs_p1/`. **No tex, md, or pdf file was
touched** — graphicx tries the direct relative path first, so the in-folder
copies resolve with zero source changes and the `{{../}}` graphicspath
entries remain valid in the repo structure. After the fix, **every current
version of every paper (P1 v43, P2 v43 + supplement, P3 v32, P4 v41, P5
v47-blinded, E1 v49, E2 v23, E3 v16, E4 v15) compiles standalone** — tex plus
its `figs_*` folder(s) alone, no parent structure — verified by the flat
matrix below.

### 2. The reported v41 error at line 2055 — reproduced, diagnosed, closed

The reported error was reproduced exactly: with the v41 tex **alone** in a
scratch folder (no `figs_p4/` subfolder), tectonic fails at precisely line
2055 — `Unable to load picture or PDF file
'figs_p4/fig2_five_regime_topology_v2.png'` (pdflatex phrases it as the
reported `pdftex.def … not found: using draft setting`). With the PNG placed
alongside (`figs_p4/fig2_five_regime_topology_v2.png`, sha256
`a4bbddc6221476a9adbc0562ca5dc0a4e0ca0517572567f5420b379a4be6e058` — the
byte-identical asset committed by Task 101), the compile is clean: 45 pp, the
full text layer **identical to the shipped PDF on all 45 pages**, Figure 1 on
p27.

**Diagnosis:** the repository is *not* in the error state — `latex/figs_p4/`
has carried the PNG since Task 101 (commit `4484745`), and the Task-102
submission zip carries it at both resolution paths (compile-verified flat at
build time). The error means the **compile folder the owner used contains the
tex without the `figs_p4/` subfolder** — e.g. a single-file download of
`paper4_delay_dynamics_v41.tex`, or a partial extraction. **User-side
remedies:** download the whole `latex/` folder *including subfolders*, or use
`submission_zips/paper4_delay_dynamics_v41_TE.zip` (the portal-ready package,
which compiles as-is after extraction). With this round's systemic fix, the
same now holds for **every** paper's `latex/` folder.

---

## Part II — the machine-exact audit (and the count reconciled)

The wave25 audit script enumerates every `\includegraphics` path in all 150
texs (pre-fix state):

| class | count | detail |
|---|---|---|
| resolve directly inside `latex/` | 12 | `figs_p2` ×7, `figs_p4` ×1 (Task 101), `figs_p1` recent ×4 |
| plain `../`-fallback (folder-prefixed path, parent copy only) | 30 | `figs_e1` ×8, `figs_e2` ×7, `figs_e3` ×5, `figs_e4` ×1, `figs_p5` ×5, `figs_p1` older ×4 |
| explicit `../`-prefixed path in the tex source | 3 | `../figs_p5/fig_{cod,rho_scan,screen}_v39.png` in the superseded P5 v39/v40/v41_NatSustain texs |

V42's hand count ("14 direct, 31 on the fallback") and this machine count
describe the same systemic class; the machine count is exact (V42 undercounted
`figs_e1` by one — 8 distinct paths, `fig4_production` and `fig4_xtencam`
being separate files — and the older-`figs_p1` set by one). Post-fix:
**42 direct, 0 plain fallback, 3 explicit-parent (the documented residual).**

---

## Part III — the fix (purely additive; frozen artifacts untouched)

35 new files, all byte-identical sha256-verified copies of the parent-level
originals:

- `latex/figs_e1/` — 8 files (836 KB)
- `latex/figs_e2/` — 10 files (932 KB; includes 3 files referenced by no
  current tex, copied for folder completeness)
- `latex/figs_e3/` — 5 files (488 KB)
- `latex/figs_e4/` — 1 file (128 KB)
- `latex/figs_p5/` — 7 files (672 KB; includes 2 unreferenced earlier
  crossing-record generations, copied for folder completeness)
- `latex/figs_p1/` — +4 older referenced files (the pre-existing 3 files in
  `latex/figs_p1/` were verified byte-identical to their parent copies;
  `fig1_witness_v40.png` exists only inside `latex/` and is untouched)

Driver: `batch 7 (audits of agent arena 1 paper
rewrites)/wave25/fix_fig_paths_v25.py` — fail-loud and **idempotent** (a
second run copies 0 files and still passes every gate). The script asserts:
0 plain `../`-fallback paths remain; the explicit-parent residual is exactly
the 3 documented paths; every tex's every plain figure reference exists inside
`latex/`.

---

## Part IV — the verification battery (fail-loud)

1. **The owner's exact error reproduced and closed** (Part I.2): scratch
   folder, tex alone → error at line 2055; tex + `figs_p4/` → clean, 45 pp,
   text layer identical to the shipped PDF on all 45 pages. Log:
   `wave25/logs/user_error_repro_v41.log`.
2. **Flat-compile matrix** (`wave25/verify_flat_compiles_v25.py`, log
   `wave25/logs/flat_matrix.log`): for each of the 10 current-version texs,
   tex + figs folder(s) alone in a scratch dir, tectonic compile, page count +
   full text-layer comparison against the shipped PDF:
   - P2, P3, P4, P5, E1, E2, E4: **text layer identical** to the shipped PDF.
   - P1 v43 and the P2 supplement: **date-only** differences (the `\today`
     footer/byline lines — Sep 14/18 shipped vs Sep 19 this build); content
     identical. These two texs are the only current versions with
     compile-date lines; any rebuild shows the same.
   - E3 v16: 18 pp vs the shipped 17 pp — **a pre-existing stale shipped PDF,
     not a figure issue** (Part V.2).
   - P5 v39_NatSustain (superseded): fails on exactly the 3 explicit
     `../figs_p5/…` paths — the documented residual, demonstrated.
3. **In-repo spot checks** (the repo scenario must not regress): E1 v49, P5
   v47-blinded, and the older P1 v31 (exercising the newly added older
   `figs_p1` files) compiled inside `latex/` — all **identical** to the
   shipped PDFs (these texs pin their dates, so even date lines match); the
   shipped PDFs were restored byte-exact afterwards (`git diff` clean over
   the whole tree — zero modified tracked files).
4. **Tree state**: `git status` under `paper rewrites/` shows exactly the 9
   new untracked entries (5 folders + 4 files); no tex/md/pdf modified
   anywhere.

---

## Part V — honest findings and residuals

1. **The 3 explicit `../`-prefixed paths** (superseded
   `paper5_sampled_governance_v39/v40/v41_NatSustain.tex`, three figures
   each written `../figs_p5/…` in the tex source): no in-folder copy can
   satisfy these — the path escapes the folder by construction. They compile
   fine in the repo structure and are superseded (the current P5
   v47-blinded uses plain `figs_p5/…` paths and is now fully
   self-contained). The remedy is a 3-line tex edit per file (drop the
   `../` prefix); it touches frozen tex sources, so it stays owner-gated.
2. **The E3 v16 shipped PDF is stale** (found by the strict text-layer
   comparison): the current tex (commit `307857a`, "current E3/E4 sources")
   contains a discussion paragraph ("A second question is why the AR(1)'s
   edge…", verbatim in the tex source) that the shipped PDF (last built at
   `0ef2e6b`, from the wave-13 state, 16→17 pp) predates; the current tex
   compiles to 18 pp. This is a pre-existing repo condition unrelated to
   figures — an in-repo rebuild shows the same 18 pp. Rebuilding the shipped
   `paperE3_edwards_forecast_ladder_v16.pdf` is a one-command owner decision
   (it changes a shipped artifact), so it was not done unilaterally.
3. **Compile-date lines**: P1 v43 (Elsevier "Preprint submitted…" footer) and
   the P2 v43 supplement (byline date) print the compile date; every rebuild
   updates those lines. Content-identical otherwise.
4. **Standing owner-level items** (unchanged): the Zenodo deposit refresh;
   submission-time guideline/masthead checks; the v41 DOI go/no-go already
   executed in Task 102 (the reference list now carries 23 DOIs).

---

## Part VI — implementation record

- New files: the 35 figure assets under `arena agent 1/paper
  rewrites/latex/figs_{e1,e2,e3,e4,p5,p1}` (Part III).
- New scripts + logs: `batch 7 (audits of agent arena 1 paper
  rewrites)/wave25/{fix_fig_paths_v25.py, verify_flat_compiles_v25.py,
  logs/{fix_fig_paths_idempotent_run.log, flat_matrix.log,
  user_error_repro_v41.log}}`.
- No manuscript, supplementary, tex, md, or pdf file changed; the shipped
  PDFs re-verified byte-exact after the in-repo spot compiles; the
  submission zips untouched.
- This record; repo worklog Task 103; committed and pushed with the owner's
  PAT (the pasted token's stray `.1` suffix stripped — fifth occurrence;
  in-memory only; zero residue under `.git`; rotation advised).

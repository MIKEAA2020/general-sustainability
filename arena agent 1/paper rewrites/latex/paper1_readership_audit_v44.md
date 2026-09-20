# Paper 1 v44 — Audit of the "Environmental Enhancement" Suggestions

**Input:** `uploads/p1 environmental enhancement.txt` — a two-route recommendation set:
(A) pivot to OR/control venues (EJOR, JOTA, DGA, AnOr; SVVA, MCSS) with a benchmark
dynamical model, de-doctrinated terminology, an OR-style introduction, and elevated
blend/time-sharing results; (B) an "EMA template" elevation (case-study-first anatomy,
proofs to appendix, policy translation, dashboard/software angle for EMS-type venues).

**Adopted into v44 (master manuscript), adapted to the master-deposit strategy:**

1. **Benchmark dynamical model (attachment's Step 1 — the single highest-value item).**
   Adopted and *strengthened beyond the suggestion*: not an illustrative simulation but
   the manuscript's exact rational witness datum re-expressed as a Schaefer (1954)
   stock-specific fishery transition (new Section 4.12 + new Figure 4). The floor/action
   semantics are domesticated exactly as the attachment proposed (spawning-stock limit,
   income margin, adjustment fund; pulse-plus-closure / sustained-yield /
   reserve-financed staged plans; heatwave strike as the disturbance), and — going past
   the attachment — the certified piecewise-linear tubes are proved conservative for the
   nonlinear logistic realization by an exact inequality
   (σ(6/5) = 528/125 > 4 = the certified adverse recovery rate; σ increasing below K/2
   on the visited range), so no simulation is needed anywhere: every quoted value is
   verified in exact rational arithmetic (24 checks, `make_benchmark_v44.py`, deposited).
   The attachment's "learn a standard ecological model and run simulations" cost is thus
   avoided entirely while its readership benefit is captured.
2. **Accessibility layer in the main body (answers the EMA readership verdict directly).**
   New paragraph in Section 1.1 ("What the abstraction buys a modeller") states, in plain
   language, what transfers between managed systems and why the operator-level statements
   are the point; the benchmark section itself is written as management language
   (dashboard, quota schedule, closed season, adjustment fund) with the theorem numbers
   as scaffolding. The main body now contains the discussion an interdisciplinary
   readership needs, while the theorem spine is untouched.
3. **Policy translation hooks (attachment's translation map — partially adopted).**
   The safe-operating-space / composite-index hooks were already present (O'Neill et al.
   2018 was cited); v44 adds the four missing canonical anchors (Rockström et al. 2009;
   Raworth 2012; De Lara and Doyen 2008; Schaefer 1954) at first use in Section 4.12.
   The renamings ("Aggregation Illusion", "Hidden Collapse Zone") were *not* adopted as
   replacements — the paper's doctrinal reading is a genuine contribution and its terms
   are load-bearing — but Section 4.12 supplies exactly the translation the map wanted,
   in one section, where a reader needs it.
4. **Blend/time-sharing prominence (attachment's Step 4).** Verified: the requested
   elevation is already present in v43's converse discussion ("the structural character
   of the gap is a property of the convexity of the action space, not of the assessment
   doctrine and not of temporal sharing as such"). v44 completes it with the attachment's
   framing in the standard controls vocabulary: relaxed (convexified) programs vs
   chattering.

**Evaluated and deferred (with reasons):**

- **Wholesale de-doctrination (Step 2) and intro rewrite (Step 3).** Venue-specific
  edits: right for a dedicated EJOR/JOTA submission, wrong for the venue-agnostic
  master. The bridge paragraph + benchmark give the master its interdisciplinary
  readability; if the EJOR route is later chosen, the renaming map is in this file,
  ready to apply as a focused diff.
- **The "EMA template" restructure (route B) and the EMS software-tool angle.**
  Contradicts the master-deposit strategy (one spine, many venues); the attachment
  itself concedes route B costs more and targets different journals. The tool angle
  remains cheap to execute later: the recursion and Farkas certificates are already
  deposited, verified code.
- **Empirical case study.** Correctly ruled out by the attachment itself for now; the
  benchmark's exact conservatism argument is the honest middle ground.
- **Paper-2 advice (JOTA/SVVA/EJC as a pure viability contribution).** Noted; paper 2
  is currently Automatica-routed and was just strengthened independently (v43).
  Revisit if the Automatica route fails.

**Verification protocol (all before inclusion):** 24 exact-rational checks
(`make_benchmark_v44.py`): witness datum and tube tables; quota admissibility
(0 ≤ H* ≤ 13 with H* ∈ [2161/250, 1463/125] on the pulse leg, 0 on the closure);
benign-branch exact tracking (B' = −3 on the pulse leg); strike bookkeeping
(17/10 → 6/5); conservatism (σ(6/5) = 528/125 ≥ 4; σ(17/10) = 1411/250 ≥ 3);
index blindness at w = (1,1) (index ≥ 2/5 > 0 while floors breach at −4/5 and −3/10);
licensing thresholds ρ₁ = 2/3, ρ₂ = 3/2; rescue readout κ* = 1 − x; sustained yield
σ(16/5) = 1088/125; STAGED rebuild 16/5 → 69/20 with fund 3/2 → 1/2; all figure
coordinates. Compile QA: exit 0; 59 pp; 4 images; 0 `??`; 0 new overfull boxes
(the only two are v43's pre-existing pair); abstract unchanged.

**Master deposit updated to match:** `figure_code/make_benchmark_v44.py` and
`figures/fig_benchmark_v44.png` added; `run_all.sh` extended (regenerates the
benchmark figure and folds in its 24 checks); `SHA256SUMS` re-sealed; README mapping
row added. Fresh-extraction test: `ALL REPRODUCTION CHECKS PASS` (7/7 images
byte-identical; 25/25 artifact checks; benchmark checks green).

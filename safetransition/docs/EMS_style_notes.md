# EMS software-paper style notes — landmarks read for SafeTransition drafting

Compiled 2026-09-20. Sources read in full or near-full text; all DOIs verified
via Crossref/Unpaywall. Companion to `EMS_submission_plan.md`.

## Sources read

1. **Pywr** — Tomlinson, J.E., Arnott, J.H., Harou, J.J. (2020). *A water
   resource simulator in Python.* Environmental Modelling & Software, 126,
   104635. doi:10.1016/j.envsoft.2020.104635 (open-access AAM, Manchester
   repository; read in full). THE canonical modern EMS software paper.
2. **SPOTPY** — Houska, T., Kraft, P., Chamorro-Chavez, A., Breuer, L. (2015).
   *SPOTting Model Parameters Using a Ready-Made Python Package.* PLOS ONE
   10(12):e0145180. doi:10.1371/journal.pone.0145180 (read: abstract,
   introduction, discussion). Famous Python-package paper; PLOS venue but the
   tone is the genre's.
3. **SALib** — Herman, J., Usher, W. (2017). *SALib: An open-source Python
   library for Sensitivity Analysis.* JOSS 2(9):97. doi:10.21105/joss.00097
   (read in full; 1-page minimal template, useful as the floor of brevity).
4. **EMS Guide for Authors** (ScienceDirect) — house requirements extracted.
5. **Jakeman, A.J., Letcher, R.A., Norton, J.P. (2006).** *Ten iterative steps…*
   EMS 21:602–614, doi:10.1016/j.envsoft.2006.01.004 — EMS's most-cited
   position paper (1,100+ citations); its opening move is the journal's
   house framing style.

Also verified (not read in full; comparison-section candidates):
airGR (Coron et al. 2017, EMS 94:166–171, doi:10.1016/j.envsoft.2017.05.002);
Raven (Craig et al. 2020, EMS 128:104728, doi:10.1016/j.envsoft.2020.104728);
FloPy (Bakker et al. 2016, Groundwater 54:733–739, doi:10.1111/gwat.12413);
SAFE toolbox (Pianosi et al. 2015, EMS 70, doi:10.1016/j.envsoft.2015.04.009).

## EMS house requirements (from the Guide for Authors)

- Abstract: **concise and factual, ≤ 150 words**, stands alone, no/uncommon
  abbreviations avoided, references avoided.
- **Highlights mandatory**: 3–5 bullets, each ≤ 85 characters incl. spaces,
  separate file with "highlights" in the name.
- **Graphical abstract mandatory** (5 × 13 cm readable).
- **Software/data availability section**: name, developer + contact, year
  first available, hardware/software required, availability + cost; program
  language and size. **"Contact the author" is not acceptable.**
- Scope language to answer explicitly: software "usability, reliability,
  verification and validation … backed up with quantitative results";
  "development and maintenance costs, and adoption and penetration … should
  be addressed. Licensing issues and open source access should be clearly
  specified."
- Numbered sections; cross-reference by number ("Section 3"), never "the text".

## Anatomy of the landmark software paper (Pywr shape)

1. **Abstract** (Pywr, 6 sentences, ~120 words): (i) "X, a new … library,
   is presented." (ii) core mechanism in one sentence; (iii) object/input
   design; (iv) the flagship capability + quantified gain ("almost 4-fold
   improvement in model run-times"); (v) what it enables for users; (vi)
   licence, examples, test suite. No citations, no self-praise adjectives
   beyond factual "novel" — we drop even that per our tone rules.
2. **Software availability block** right after the abstract: labelled fields
   (name, description, developers, language, systems, licence, source URL,
   distributions). Note Pywr lists **license and test suite in the abstract
   itself** — verifiability as a selling point, stated plainly.
3. **Introduction** (≈ 5 paragraphs):
   - P1: the practice the software serves, with decades-deep citations
     ("Planning and management … has used simulation models for decades as
     its core approach (…1986; 1962; 1981…)"). Establish the reader's world.
   - P2–P3: a *classification* of existing approaches, each with strengths
     and concrete limitations, dense but fair citations. No strawmen: each
     prior class is credited with what it does well ("Rule-based models can
     be computationally efficient … but these models can be cumbersome to
     develop further, maintain and apply to new systems").
   - P4: the gap as an *improvement of current practice*, not a villain:
     "Common to all of these approaches is … However … Therefore, the current
     approach … can be improved."
   - P5: "In this work we present …" — what the software is, its mechanism,
     its flagship capability, its extendability, integration API — followed
     by a plain technology/licence paragraph (cross-platform, open formats,
     regression test suite, GPL v3), then a **roadmap paragraph**: "We
     describe … in section 2. … Performance benchmarks are given in section
     4, followed by a discussion and conclusions in sections 5 and 6."
4. **Methods/core design**: mathematics first, then architecture; pseudocode
   for the main loop; formal notation introduced as needed ("We define the
   set of … as P. These paths contain no repeated nodes."). Constraint lists
   as numbered items.
5. **Benchmarks/examples**: quantified, reproducible; comparisons credited to
   their sources; honesty about settings ("This difference in efficiency is
   most likely due to the setting of the algorithm").
6. **Discussion** (SPOTPY exemplar tone): "All algorithms work well in X,
   which was shown by the different case studies. Our intention was not to
   accept or reject algorithms but rather show their functionality…" —
   plain recaps, comparisons to published results with citations, explicit
   recommendations ("We recommend using …").
7. **Conclusions**: capabilities recap + limitations stated plainly + one
   forward sentence.
8. **Acknowledgements**: funding + disclosure sentences, formal.

## Sentence-level tone and flow patterns worth copying

- **Purposeful paragraph openers** that orient: "Planning and management of
  X has used Y for decades…"; "Common to all of these approaches is…";
  "The utility of X stems from its use in…"; "Pywr is a generic dynamic
  modelling library for…".
- **Declarative capability sentences**, subject = the tool: "The library
  facilitates the generation of samples…, and then provides functions to…"
  (SALib); "SPOTPY has a model-independent structure and can be run in
  parallel…".
- **"We" as agent of testable acts, never of admiration**: "We developed…",
  "We tested SPOTPY in five different case studies…", "We note immediately
  that…", "We refer the reader to…". No "we believe this excellent…".
- **Benefit sentences tied to user workflows**: "These features enable
  analysts to apply advanced … approaches … to real systems." (Pywr);
  "The case studies reveal that the implemented methods can be used for any
  model with just a minimal amount of code…" (SPOTPY).
- **Fair-classification flow**: for each existing approach — credit, cite,
  limitation, all in one or two sentences; the gap emerges arithmetically.
- **Quantified claims everywhere**: "eight widely used algorithms, 11
  objective functions", "almost 4-fold improvement", "after 4,000
  iterations, exactly as we found it".
- **Honesty markers**: "should be used with caution (Ilich, 2009)";
  limitations named in conclusions.
- **Flow devices**: roadmap paragraph at the end of the intro; forward
  references by section number; short "reader-positioning" sentences between
  hard sections ("It is necessary to describe X prior to a detailed
  description of Y.").

## Humanization techniques that stay formal (EMS-idiomatic)

- One aphoristic, factual opening sentence is allowed and idiomatic (SPOTPY):
  "The choice for specific parameter estimation methods is often more
  dependent on its availability than its performance." — a motivation
  statement, not editorializing. SafeTransition equivalent: composite
  dashboards are trusted because they are computed, not because they are
  certified; availability of verifiable safety readings is the bottleneck.
- Concrete numbers as texture (counts, thresholds, run-times) — reads as
  human precision, not marketing.
- Modest, factual first-person plural for choices made: "We implement two
  alternative linear programmes to demonstrate the flexibility of the
  approach."
- User-perspective sentences: "From the user's perspective this means…"
  (Pywr). One or two per paper maximum.
- No exclamation, no "exciting/remarkable/powerful", no weasel superlatives.
  Pywr uses "novel" once in the abstract; we omit even that and let the
  claim's content carry the weight.

## Reconciliation with standing tone rules

| EMS-idiomatic | Our rule | Resolution |
| --- | --- | --- |
| "we present/develop/test" | formal, factual | allowed: describes verifiable acts |
| "novel", "powerful" | no self-praise | omit; state the capability |
| change-log flavor ("currently contains…") | no diary | acceptable: states software content, versioned in repo not prose |
| related-software comparison | no phantom/naive strawmen | cite real tools (verified DOIs above), credit + locate, never caricature |
| companion papers | formal citations | cite the two companion manuscripts + verification deposit by author–year + DOI |

## Application skeleton — SafeTransition manuscript

- **Title**: *SafeTransition: exact rational certification of transition
  safety for sustainability assessment* (keep; matches genre convention
  "Name: description").
- **Abstract** (≤150 words, Pywr shape): "SafeTransition, a Python library
  for certifying the transition safety of sustainability assessments, is
  presented." → mechanism (typed operators, exact tubes) → flagship
  capability (Farkas obstruction certificates with verified infeasibility
  margins; index-blindness alarm) → quantified anchor (24/24 exact benchmark
  checks re-deriving the deposited verification values) → user benefit
  (auditable dashboards for regulatory composite indicators) → licence,
  tests, zero dependencies.
- **Availability block** immediately after abstract (fields above; figshare
  DOI as the archive, GitHub mirror, PyPI-able source).
- **Introduction** (5 paragraphs, Pywr shape): P1 decades-of-practice
  (composite indicators in sustainability monitoring; cite Jakeman 2006 for
  good practice framing); P2–P3 classification (floating-point viability
  kernels; MCDA/composite-indicator packages; certificate-based formal
  verification — each credited then located); P4 gap as improvement
  (readings are computed, not verifiable); P5 "In this work we present…"
  + technology paragraph (standard library only, MIT) + roadmap.
- **Section 2 Mathematical basis**: the implemented specification — typed
  datum, five operators, chain, recursions, certificates — with proofs
  delegated by citation to the companions.
- **Section 3 Software description**: module table, datum interface,
  exact-arithmetic discipline ("Floats appear only in rendered SVG
  geometry, never in checks" — this is the paper's signature sentence),
  complexity note, CLI/API.
- **Section 4 Illustrative examples**: benchmark (24/24; blindness alarm;
  ρ band [2/3, 3/2]; κ*), dashboard figure, partial-observation demo
  (recourse failure; fibre criterion; margin 1/10 certificate).
- **Section 5 Comparison**: Pywr/SPOTPY/SALib/airGR/Raven/FloPy/SAFE as
  functional neighbours; the comparison axis is exactness and
  verifiability, stated with credit.
- **Section 6 Availability**: EMS-required fields verbatim-formatted.
- **Section 7 Conclusions**: capability recap + limits (finite explicit
  graphs; no predictive claim) + one forward sentence (extensions:
  continuous-state data, additional certificate families).
- **Highlights** (draft, each ≤85 chars): "Exact rational certificates for
  transition safety" / "Typed operators expose what composite indices miss"
  / "Farkas infeasibility margins computed and verified exactly" /
  "24/24 benchmark checks re-derive deposited verification values" /
  "Single-file HTML dashboard with zero runtime dependencies".
- **Graphical abstract**: the dashboard render (already exists as
  `safetransition/dashboard.html`; export PNG at 1328 × 531).

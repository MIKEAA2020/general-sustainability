# EMS submission plan — SafeTransition software paper

Target journal: **Environmental Modelling & Software** (Elsevier).
Status: package complete and verified (v1.0.0); manuscript not yet drafted.
This note records the submission plan and the decisions already taken.

## Why EMS fits

- EMS publishes original contributions describing **scientific software**
  whose availability is a condition of publication. SafeTransition is a
  working, tested, zero-dependency package implementing the certificate
  machinery of the two companion manuscripts, with a twenty-four-check
  exact benchmark — a natural software-description submission.
- The recursion + Farkas certificate machinery is already **verified
  deposited code** (figshare DOI 10.6084/m9.figshare.33764023); the
  software paper formalizes the tool without new mathematical claims.

## Decisions already taken (standing constraints)

- **Deposit**: the package enters the *same* figshare item as a **new
  version** (DOI stable; never a new item) — consistent with the venue
  strategy for the master deposit.
- **Citations**: formal author–year + italic short-title + DOI only; no
  shorthand; companion manuscripts cited as companions (no version
  numbers, no unpublished-version references).
- **Tone**: journal-formal throughout; no change-log/diary/meta content;
  no phantom or naive strawman comparisons — the related-software section
  cites only real, verifiable tools.
- **Figures**: submitted separately; the dashboard render and the
  benchmark panel are the natural figures/graphical abstract.

## Proposed title

*SafeTransition: exact rational certification of transition safety for
sustainability assessment*

(Alternative emphasis: "…certificates, recursions, and dashboards for
transition-safety assessment".)

## Section plan

1. **Introduction.** Aggregate indices certify transitions that breach
   typed floors; the quantifier-order separation; why verifiable
   (exact-rational) outputs matter for regulatory dashboards.
2. **Mathematical basis.** Assessment operators and the operator chain;
   witnessed separation; belief-space recursion under partial
   observation; Farkas/common-action/fibre certificates. Stated as the
   implemented specification, with proofs delegated to the companion
   manuscripts.
3. **Software description.** Architecture (module table), the datum
   interface, exact-arithmetic discipline (floats only in rendering),
   CLI and library API; complexity note (polynomial on explicit graphs).
4. **Illustrative examples.** (a) The resource-transition benchmark:
   24/24 exact checks, index-blindness alarm, licensing band [2/3, 3/2],
   rescue threshold; (b) the dashboard (single-file HTML, inline SVG);
   (c) partial observation: post-observation recourse failure, fibre
   criterion, Farkas certificate with margin 1/10.
5. **Comparison with related software.** Viability-kernel implementations,
   MCDA/composite-indicator packages, and certificate-based verification
   tools — **each candidate must be verified (real, current, DOI'd)
   before drafting**; the comparison is functional (exactness,
   verifiability, typed floors, obstruction certificates), not
   benchmarked performance claims.
6. **Availability and requirements.** Python ≥ 3.9; zero runtime
   dependencies; MIT; package + tests in the figshare deposit new
   version; repository mirror.
7. **Conclusions.** Verifiable safety readings for transition governance;
   limits (finite explicit graphs; no predictive claim) stated plainly.

## Pre-drafting checklist

- [ ] Verify 3–5 real related-software citations (with DOIs).
- [ ] Refresh the figshare deposit as a NEW VERSION including
      `safetransition/` (source, tests, examples, this plan).
- [ ] Generate figures: benchmark panel (deposited pipeline) + dashboard
      render (PNG export for submission).
- [ ] Draft in Elsevier house style (elsarticle, `3p`), abstract < 265
      words, highlights (3–5 bullets, ≤ 85 characters).
- [ ] Full tone/alignment scan per standing rules before any version is
      pushed as a candidate manuscript.

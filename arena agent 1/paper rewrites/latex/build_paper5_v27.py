#!/usr/bin/env python3
"""Build paper5 v27 from v26: audit cleanup + line numbers + Sept 10 date (single version).
Usage: cp paper5_sampled_governance_v26.tex paper5_v27/paper5_sampled_governance_v27.tex && python3 build_paper5_v27.py
Every substitution asserts its expected match count; any mismatch aborts.
"""
import sys

PATH = '/home/user/paper5_v27/paper5_sampled_governance_v27.tex'
t = open(PATH).read()
n0 = len(t)

def sub(old, new, count=1, tag=''):
    global t
    c = t.count(old)
    assert c == count, f'MISMATCH ({tag or old[:60]!r}): found {c}, expected {count}'
    t = t.replace(old, new)

# ---------- M1: clean header ----------
sub("""% LaTeX source generated from paper5_sampled_governance_v26.md by wave13/build_latex_v13.py (batch 7 (audits of agent arena 1 paper rewrites)/wave13).
% Pandoc body identical to the wave-9/11 output (asserted at build time), with the
% declaration subsections relocated to a trailing Declarations section.
% Front matter: Amin Abaee, Independent Researcher, clickable ORCID
%(https://orcid.org/0000-0002-0019-1842) and email (amin_abaee@ut.ac.ir)
% beneath the name; date September 6, 2026.
% Back matter: the paper's own declarations, each a titled subsection, plus
% the AI declaration (GLM (Z.ai), Qwen (Alibaba Cloud) and DeepSeek AI
% assisted with drafting and iterative review).
% References carry the owner's Zenodo DOIs (see wave13/apply_md_doi.py).
% Edit the markdown source and re-run the build script to regenerate.
% Compiles error-free with tectonic (also compatible with pdflatex/xelatex).""",
"""% Periodic Review as Sampled Governance (paper 5, revision v27): cleaned revision with line numbers for review.
% Amin Abaee, Independent Researcher, ORCID https://orcid.org/0000-0002-0019-1842, amin_abaee@ut.ac.ir.
% Compiles with tectonic (also compatible with pdflatex/xelatex).""", tag='M1 header')

# ---------- M11: lineno + date ----------
sub("\\usepackage[font=small,labelfont=bf]{caption}\n",
    "\\usepackage[font=small,labelfont=bf]{caption}\n\\usepackage[mathlines]{lineno}\n", tag='lineno pkg')
sub("\\begin{document}\n", "\\begin{document}\n\\linenumbers\n", tag='linenumbers')
sub("\\date{September 6, 2026}", "\\date{September 10, 2026}", tag='date')

# ---------- M2: submission-target kicker ----------
sub("""\\maketitle

{\\centering\\small \\emph{Methodology and case study --- prepared in the style of the ICES
Journal of Marine Science}\\par}

\\begin{abstract}""",
"""\\maketitle

\\begin{abstract}""", tag='M2 kicker')

# ---------- abstract ----------
sub("robust to the catchability scale the stage record never declares: at",
    "robust to the catchability scale the stage record never specifies: at", tag='abs declares')

# ---------- Box 1 ----------
sub("""Each load-bearing claim, its evidential status, and its record pointer.
Nothing in this box is new; the body sections carry the full statements.""",
"""Each central claim, its evidential status, and its record pointer.""", tag='M9 box footer')
sub("Companion delay study (in review) & Section 3.4 \\\\",
    "Companion study (Abaee, 2026) & Section 3.4 \\\\", tag='M3 box companion')
sub("""Relation between the three undelayed-limit statements & Recorded as an
open tension; continuous eigenvalue not printed & Section 3.4 \\\\""",
"""Relation between the three undelayed-limit statements & Reconciled conditional on the companion's undelayed sign (\\(\\lambda > 0\\)); \\(\\lambda\\) itself unlisted here & Section 3.4 \\\\""",
    tag='M10 box row')
sub("""& Declared,
pre-registered reconstruction (plan frozen before any run)""",
"""& Specified,
pre-registered reconstruction (plan fixed before any run)""", tag='box recon')
sub("""& Declared
sensitivity layer of the reconstruction""",
"""& Sensitivity layer of the reconstruction""", tag='box sens')
sub("uninformative at the undeclared \\(q\\)", "uninformative at the unspecified \\(q\\)", tag='box q')
sub("& Author-curated inventory &", "& Curated inventory &", tag='box curated')
sub("& Registered-data battery;", "& Archived-data battery;", tag='box battery')
sub("""Unreproduced hypotheses on the
open-problem docket""", "Unreproduced hypotheses (open problems)", tag='box docket')
sub("& Declared, not operationalised &", "& Stated, not operationalised &", tag='box decl')

# ---------- 1 Introduction ----------
sub("""It is the same architecture the abstract, the
keywords, and the title's second clause name""",
    """It is the same architecture the title and abstract call""", tag='terminology ptr')
sub("with declared comparator classes", "with specified comparator classes", tag='224')
sub("""is reported at its exact
evidential status: a multiplicity-controlled""",
    """is reported: a multiplicity-controlled""", tag='intro mantra')
sub("are declared as comparators.", "serve as comparators.", tag='250')
sub("must declare which operator", "must state which operator", tag='256')

# ---------- 2.1 ----------
sub("the aggregation rule is declared (Table 1)", "the aggregation rule is stated (Table 1)", tag='269')
sub("The separation is not decorative. Reviews can be", "Reviews can be", tag='decorative')
sub("""for the declared observation model
can serve. Two further conventions are registered.""",
    """for the specified observation model
can serve. Two further conventions apply.""", tag='308+309')
sub("are defined at their use sites.", "are defined where they are used.", tag='use sites')
sub("""by construction. The
reason is technical: the effort law's""",
    """by construction. The effort law's""", tag='technical')
sub("""(Author et
al., in review). The effort law is""", "(Abaee, 2026). The effort law is", tag='M3 396')
sub("""is stated at its
use site in Section 3.4 and collected""",
    """is stated where it is used in Section 3.4 and collected""", tag='use site')
sub("are not printed in this manuscript (Appendix A).", "are not listed here (Appendix A).", tag='419')
sub("""Three comparators receive distinct
declarations:""", """Three comparators are distinctly specified:""", tag='425')
sub("The comparators are declared for the prospective", "The comparators are specified for the prospective", tag='429')
sub("""at the declared evidential status (deterministic,
seed-fixed, on the declared architecture only).""",
    """at the stated evidential status (deterministic,
seed-fixed, on the specified architecture only).""", tag='435')

# ---------- 2.2 ----------
sub("""and the recorded map is
the pre-review""", """and the map used is
the pre-review""", tag='448 recorded')
sub("""requires an explicitly
registered hold or interpolation rule.""",
    """requires an explicitly
specified hold or interpolation rule.""", tag='454')
sub("that boundary calculation is now reported in Section 3.4.",
    "that boundary calculation is reported in Section 3.4.", tag='now 2.2')
sub("""a newly declared, pre-registered
object""", """a newly specified, pre-registered
object""", tag='467')
sub("is on the record there.", "is given there.", tag='on the record')
sub("""The declared and registered computational requirements of this
section and of""", """The computational requirements of this
section and of""", tag='472')
sub("""which also fixes the vocabulary convention for `declared',
`registered', and `pre-registered'.""",
    "which also fixes the pre-registration convention.", tag='477')

# ---------- 2.3 ----------
sub("not a demolition of the loop.", "not a refutation of the loop mechanism.", tag='demolition')

# ---------- 2.4 ----------
sub("is a frozen 42-stock cohort", "is a fixed 42-stock cohort", tag='frozen cohort')
sub("""is therefore an analysis-side cohort criterion, not a
database classification""",
    """is therefore a criterion applied in this analysis, not a
database classification""", tag='analysis-side')
sub("according to a declared rule,", "according to a stated rule,", tag='531')
sub("""predeclared bands (4--8 yr for biomass, 12--60 yr for effort) --- bands
that descend from the archived""",
    """prespecified bands (4--8 yr for biomass, 12--60 yr for effort) --- bands
derived from the archived""", tag='533')
sub("across the declared family (stocks,", "across the specified family (stocks,", tag='540')
sub("is the declared fallback.", "is the prespecified fallback.", tag='546')
sub("""One caveat is also
registered:""", "One caveat:", tag='548')

# ---------- 2.6 ----------
sub("is an author-curated inventory, not a systematic review.",
    "is a curated inventory, not a systematic review.", tag='curated')
sub("""must outperform
  preregistered alternatives""", """must outperform
  pre-registered alternatives""", tag='580 hyphen')
sub("""Behind criterion (iii) stands a named enumeration of the alternative
mechanisms""", """Behind criterion (iii) is an explicit list of the alternative
mechanisms""", tag='enumeration')

# ---------- 2.7 ----------
sub("""is carried as a bounded empirical
object.""", """is treated as a bounded empirical
object.""", tag='carried')
sub("""The constitutive assumption stands as such --- the equation is an
illustrative model, not a fit ---""",
    "The constitutive equation is illustrative, not a fit ---", tag='stands as such')
sub("The argument is elementary. Case (i) subtracts", "Case (i) subtracts", tag='elementary')
sub("--- the stated distinction. \\ensuremath{\\square}", "--- as claimed. \\ensuremath{\\square}", tag='stated distinction')
sub("are rounded renderings of the assessment table, and the",
    "are rounded values from the assessment table, and the", tag='renderings 2.7')

# ---------- 3.1 ----------
sub("""The check is elementary and is reported first because every
later result relies on""", """This check comes first because every
later result relies on""", tag='738')
sub("""is automatic on the stock equation and is used
implicitly in the induction:""", """holds automatically on the stock equation and is used
in the induction:""", tag='implicitly')
sub("""is modest but
load-bearing: the projected Euler step does not push the state outside
its declared admissible set""",
    """is modest but
essential: the projected Euler step does not push the state outside
its specified admissible set""", tag='3.1 load-bearing')

# ---------- 3.2 ----------
sub("The converse caution is equally load-bearing.", "The converse caution is equally important.", tag='3.2 load-bearing')

# ---------- 3.3 ----------
sub("""the delayed-recruitment oscillation
lineage of Gurney, Blythe, and Nisbet, 1980, supplies the classical
reference point)""",
    """the delayed-recruitment oscillation
literature of Gurney, Blythe, and Nisbet, 1980, supplies the classical
reference point)""", tag='lineage')
sub("""they are retained below at
provisional status, and --- decisively --- the paper's own
pre-registered stage-map reconstruction of Section 3.4""",
    """they are reported below at
provisional status, and the
pre-registered stage-map reconstruction of Section 3.4""", tag='decisively')
sub("""experiments retain the anchovy-class
trajectory region""", """experiments preserve the anchovy-class
trajectory region""", tag='890 retain')
sub("""for the declared multiplicative
perturbation only.""", """for the specified multiplicative
perturbation only.""", tag='893')
sub("These are retained only as observable-specific dominant peaks",
    "These are reported only as observable-specific dominant peaks", tag='897')
sub("""because the
available convention does not distinguish""",
    """because the
archived record does not distinguish""", tag='available convention')

# ---------- 3.4 ----------
sub("carries the declared computation objects in", "gives the computation objects in", tag='912')
sub("""That comparison is now reported: executed and
verified on the companion delay study's identical hold map (Author et
al., in review;""",
    """That comparison is reported here: executed and
verified on the companion delay study's identical hold map (Abaee, 2026;""", tag='M3 933')
sub("and the restabilising direction survives.", "and the restabilising direction is preserved.", tag='survives')
sub("The complete crossing record (reported).}", "The complete crossing record.}", tag='(reported)')
sub("""(seed-free;
it reproduces the registered numbers on the range they cover)""",
    """(deterministic;
it reproduces the numbers reported here on the range they cover)""", tag='seed-free')
sub("The multiplier types are recorded with the crossings",
    "The multiplier types are reported with the crossings", tag='976')
sub("""are not printed in this manuscript; they belong to the
declared computational record (Appendix A).""",
    """are not listed here; they are in the
computational record (Appendix A).""", tag='982')
sub("""--- the
printed precision record is the 200,001-point scan""",
    """--- the
stated precision record is the 200,001-point scan""", tag='printed precision')
sub("""--- and on the unprinted parameter vector (Table 3). What
the margin does not condition is the ordering""",
    """--- and on the unlisted parameter vector (Table 3). What
the margin does not affect is the ordering""", tag='unprinted+condition')
sub("""the headline ``annual
review is unstable'' is read at that status.""",
    "the annual-instability verdict is read at that status.", tag='headline')
sub("{Registered crossing record of the logistic hold map:",
    "{Crossing record of the logistic hold map:", tag='caption')
sub("(Author et al., in review); the sampled operator's",
    "(Abaee, 2026); the sampled operator's", tag='M3 1003')
sub("(Author et al., in review). Annual review is", "(Abaee, 2026). Annual review is", tag='M3 1008')
sub("observation of Section 2.3 is now a same-plant one.",
    "observation of Section 2.3 is a same-plant one.", tag='now same-plant')
sub("""and are now read together
rather than left implicit. Section 2.3 declares the continuous-delay""",
    """and are read together.
Section 2.3 states the continuous-delay""", tag='now read together')
sub("""--- no
unreported crossings are needed.""", """--- no
additional crossings are required.""", tag='unreported crossings')
sub("""as the one-plant contrast above
records. The eigenvalue \\(\\lambda\\) is not printed in this manuscript""",
    """as the one-plant contrast above
shows. The eigenvalue \\(\\lambda\\) is not listed here""", tag='above records')
sub("Section 2.3's same-loop declaration and", "Section 2.3's same-loop statement and", tag='same-loop')
sub("""stand
as recorded --- annual instability""", """stand
as stated --- annual instability""", tag='1045 recorded')
sub("""The declared
comparator run (protective, sign-reversed response)""",
    """The protective
comparator run (sign-reversed response)""", tag='1050')
sub("""The declared
protective and fixed-plan comparators are run""",
    """The protective
and fixed-plan comparators are run""", tag='1057')
sub("""seeds fixed; the certified object remains the spectral
record, and the prospective real-system design of Section 4.5 is
untouched).""",
    """seeds fixed; the spectral record remains the authoritative
result, and the prospective real-system design of Section 4.5 remains
unexecuted).""", tag='certified object')
sub("""and the paper's own
reconstruction does not reproduce""",
    """and the pre-registered reconstruction below does not reproduce""", tag='1084 own')
sub("not part of the declared core.", "not part of the model core.", tag='1092')
sub("""in the declared case search
(Section 2.6)""", "in the case search of Section 2.6", tag='1093')
sub("carry a declared limitation:", "carry a stated limitation:", tag='1102')
sub("""Rather than leave the stage operator without any boundary
record, a new stage map was declared, pre-registered (plan dated and
frozen 2026-09-01, before any run;""",
    """To supply the stage operator's boundary record, a new stage map was
specified and pre-registered (plan dated and fixed
2026-09-01, before any run;""", tag='rather than leave')
sub("The reconstruction is a labelled new object:", "The reconstruction is a newly specified object:", tag='labelled')
sub("--- a declared scale convention matching", "--- a scale convention matching", tag='1119')
sub("or a declared convention; none was chosen", "or a stated convention; none was chosen", tag='1123')
sub("""with a declared sensitivity layer
\\(h \\in \\{0.6, 0.9\\}\\). The controller is the paper's declared object
unchanged:""",
    """with a sensitivity layer
\\(h \\in \\{0.6, 0.9\\}\\). The controller of Section 2.1 is unchanged:""", tag='1133')
sub("""with a declared sensitivity \\(q = 0.1\\) (the archived stage
record declares no \\(q\\);""",
    """with a sensitivity case \\(q = 0.1\\) (the archived stage
record states no \\(q\\);""", tag='1138')
sub("""computed with the paper's
declared quota-tracking gains""", """computed with
quota-tracking gains""", tag='1146')
sub("At the declared controller value every class", "At the specified controller value every class", tag='1149')
sub("at the declared value is a long-horizon band", "at the specified value is a long-horizon band", tag='1155')
sub("from the declared initial condition", "from the specified initial condition", tag='1160')
sub("""The declared
catchability sensitivity is informative:""",
    "The catchability sensitivity analysis is informative:", tag='1184')
sub("""is a strong function of the catchability scale
the paper leaves undeclared for this plant.""",
    """depends strongly on the catchability scale,
which is unspecified for this plant.""", tag='1191')
sub("""(criteria pre-registered;
the verdict is the first complete run's record):""",
    """(criteria pre-registered;
verdicts from the first complete run):""", tag='first run')
sub("on this declared plant family", "on this specified plant family", tag='1229')
sub("""The stage map declares no
catchability;""", """The stage map states no
catchability;""", tag='1234 declares')
sub("""and at the declared sensitivity \\(q = 0.1\\) every verdict in the table
flips""",
    """and at the sensitivity case \\(q = 0.1\\) every verdict in the table
flips""", tag='1236')
sub("""about this declared family at an
undeclared scale, not an adjudication""",
    """about this specified family at an
unspecified scale, not an adjudication""", tag='1239')

# ---------- 3.5 ----------
sub("""in the declared biomass or
effort band""", """in the specified biomass or
effort band""", tag='1249')
sub("The null carries its three-way restriction on the line: it is not",
    "The null carries a three-way restriction: it is not", tag='on the line')
sub("under the declared screen, target-band", "under this screen, target-band", tag='1258')

# ---------- 3.6 ----------
sub("""under
the declared test, and the sprat-class result""",
    """under
this test, and the sprat-class result""", tag='1274')
sub("The evidentiary separation is total:", "The evidentiary separation is complete:", tag='is total')
sub("""For a locally linear
registered model,""", """For a locally linear
specified model,""", tag='1285')
sub("""reproduces the preregistered gain--phase
curve.""", """reproduces the pre-registered gain--phase
curve.""", tag='1292 hyphen')
sub("""the
registered strengthening tests are:""", """the
planned confirmatory tests are:""", tag='1294')
sub(""", now fixed by the
executed battery rather than selected after the fact.""",
    """, fixed by the
executed battery.""", tag='now fixed')

# ---------- 3.7 ----------
sub("Bangkok (durably) and La Mancha Oriental (on the",
    "Bangkok (durably responsive institutional feedback: the groundwater-extraction control regime persisted across multiple review cycles rather than being a one-time cap or ban) and La Mancha Oriental (on the",
    tag='durably gloss')
sub("""are author calculations from
registered input series and are recorded at that status in the
Supplementary material;""",
    """use archived input series and are reported at that status in the
Supplementary material (S4);""", tag='1311 author calcs')
sub("""has an author-calculated
post-rule coefficient of variation of 0.387""",
    """has a post-rule coefficient of variation of 0.387 (calculated here)""", tag='author-calculated')
sub("""A registered-data battery on the Sea Around Us
series behind that figure""",
    """A confirmatory battery on the archived Sea Around Us
series behind that figure""", tag='1337 battery')
sub("""is registered as a focal test rather than
claimed as a regime effect.""",
    """is treated as a focal test rather than
claimed as a regime effect.""", tag='1356')
sub("""so controller nonclassification prevents
that comparison""", """so the unclassified controller prevents
that comparison""", tag='nonclassification')
sub("""; Author et al., in
review)""", "; Abaee, 2026)", tag='M3 1386')

# ---------- 3.8 ----------
sub("""\\textbf{The
exact data split the phenomenon""", """\\textbf{The
data split the phenomenon""", tag='exact data split')
sub("""are registered with the assessment
table's documentation;""", """are documented with the assessment
table;""", tag='1408')
sub("""rounded renderings of the assessment table (the underlying values are
381.95, 101.05, 30.55 kt, and so on), and the survival column""",
    """rounded values from the assessment table (e.g. underlying values 381.95, 101.05, 30.55 kt), and the survival column""",
    tag='renderings 3.8')
sub("""registered on the open-problem docket and stated here as
hypotheses, not results.""", """listed as open problems and stated here as
hypotheses, not results.""", tag='1426 docket')
sub("""For the
present analysis the decisive point is the persistence""",
    """For the
present analysis the key point is the persistence""", tag='decisive point')

# ---------- 4.1 ----------
sub("""confound is kept adjacent --- the operator effect is not claimed to be
isolated by this comparison)""",
    """confound is stated alongside --- the operator effect is not claimed to be
isolated by this comparison)""", tag='kept adjacent')
sub("carries a declared limitation of its own:", "has its own stated limitation:", tag='1519')
sub("""and at the declared sensitivity \\(q = 0.1\\) every
verdict""", """and at the sensitivity case \\(q = 0.1\\) every
verdict""", tag='1521')
sub("""at the undeclared scale rather than a
non-reproduction""", """at the unspecified scale rather than a
non-reproduction""", tag='1525')
sub("With the complete crossing record in hand the operator finding sharpens.",
    "The complete crossing record sharpens the operator finding:", tag='in hand')

# ---------- 4.3 ----------
sub("""allocation is exactly that --- an allocation of unobserved deaths""",
    """allocation is that --- an allocation of unobserved deaths""", tag='exactly that')

# ---------- 4.4 ----------
sub("""Five declared
outcomes:""", "Five outcomes:", tag='1583')
sub("anti-regulation conclusion may be retained.", "anti-regulation conclusion may be drawn.", tag='1605')

# ---------- 4.5 ----------
sub("""are retained rather than collapsed to one
lag.""", """are kept distinct rather than collapsed to one
lag.""", tag='1627')
sub("--- and its discipline is negative: no governance lead is inferred from",
    "--- with two negative constraints: no governance lead is inferred from", tag='discipline negative')
sub("with registered controller sign, a combined", "with specified controller sign, a combined", tag='1651')
sub("""using declared predictive and calibration
criteria;""", """using stated predictive and calibration
criteria;""", tag='1653')
sub("cannot reproduce the preregistered phase ordering",
    "cannot reproduce the pre-registered phase ordering", tag='1657 hyphen')
sub("complexity is retained only on scored evidence, never by",
    "complexity is admitted only on scored evidence, never by", tag='1659')
sub("""and the
timing or sign of decision feedback in a simulated environment, with""",
    """and the
timing or sign of decision feedback, with""", tag='simulated dup')
sub("""within a
declared operating model;""", """within a
specified operating model;""", tag='1716')

# ---------- 4.6 ----------
sub("""the undeclared
floor),""", """the unspecified
floor),""", tag='1730')
sub("""is carried at measurement level, but
outside the Discussion's technical flow:""",
    """is presented at measurement level (Appendix B):""", tag='4.6 carried')
sub("are relocated to Appendix B, with the full", "are given in Appendix B, with the full", tag='relocated')
sub("""is the
summary:""", """is the
point:""", tag='is the summary')
sub("remain declared rather than resolved (Section 4.7 (viii)).",
    "remain stated rather than resolved (Section 4.7 (viii)).", tag='1739')

# ---------- 4.7 Limitations rebuild (M5) ----------
sub("""\\item
  Diagnostics are not causal claims: the spectral null, the response
  regions, the power values, the case calculations, and the cod split
  carry their declared types and no more. (ii) The stage-structured
  response regions are exploratory finite-grid, trajectory-classified
  records pending complete stage registration and multiplier analysis;
  the logistic hold-map multiplier record is complete (Section 3.4), and
  the stage operator's multiplier and trajectory record is supplied by
  the labelled reconstruction of Section 3.4 --- a new declared object
  whose comparison with the archived windows is a consistency check, not
  a validation. No Poincar\\'e-map multiplier classification is claimed for
  the archived stage-output values, and they are not reproducible
  numerical propositions until the original computational record is
  attached. (iii) The two review-map operators are distinct: statements
  computed on the hold map, on the stage-structured map, and on the
  continuous-delay equation do not transfer to one another. (iv) The
  screen is a selected-cohort consistency check whose power is high only
  in favourable noise and record-length regimes; the null is not proof
  of absence and adjudicates nothing about controller sign. (v) The
  zero-count case search is not independent disconfirmation under its
  own eligibility criteria. (vi) The cod case establishes a descriptive
  partition, and no mechanism is identified. (vii) The obstruction
  mathematics concerns exact trajectories of the fixed-parameter,
  fixed-removals autonomous class and is not a rejection under
  measurement error, process noise, age structure, migration,
  time-varying mortality, or state-space observation models. (viii) The
  social object is not operationalised: the human series is not
  assembled, the normative floors are unoperationalised, and the gap is
  the result. (ix) The prospective designs are preregistration targets,
  not executed studies, and they convert nothing retroactively.""",
"""\\item Diagnostics are not causal claims: the spectral null, the response regions, the power values, the case calculations, and the cod split carry their stated types and no more.
\\item The stage-structured response regions are exploratory finite-grid, trajectory-classified records pending complete stage registration and multiplier analysis; the logistic hold-map multiplier record is complete (Section 3.4), and the stage operator's multiplier and trajectory record is supplied by the reconstruction of Section 3.4 --- a newly specified object whose comparison with the archived windows is a consistency check, not a validation. No Poincar\\'e-map multiplier classification is claimed for the archived stage-output values, and they are not reproducible numerical propositions until the original computational record is attached.
\\item The two review-map operators are distinct: statements computed on the hold map, on the stage-structured map, and on the continuous-delay equation do not transfer to one another.
\\item The screen is a selected-cohort consistency check whose power is high only in favourable noise and record-length regimes; the null is not proof of absence and adjudicates nothing about controller sign.
\\item The zero-count case search does not independently disconfirm the mechanism: finding no eligible cases under these criteria is not evidence against it.
\\item The cod case establishes a descriptive partition, and no mechanism is identified.
\\item The obstruction mathematics concerns exact trajectories of the fixed-parameter, fixed-removals autonomous class and is not a rejection under measurement error, process noise, age structure, migration, time-varying mortality, or state-space observation models.
\\item The social object is not operationalised: the human series is not assembled, the normative floors are unoperationalised, and documenting the gap is the finding.
\\item The prospective designs are preregistration targets, not executed studies, and they do not retroactively change the status of the retrospective results.""",
    tag='M5 4.7 enumerate')

# ---------- 5 Conclusion ----------
sub("""Its empirical
layer, reported at exact evidential status, contains one case whose""",
    """Its empirical
layer contains one case whose""", tag='conclusion mantra')
sub("""and a discipline for everything else: a selected-cohort
screen with no target-band discoveries and declared power,""",
    """and a falsification discipline for the rest: a selected-cohort
screen with no target-band discoveries and stated power,""", tag='1787')

# ---------- Appendix A ----------
sub("""This appendix consolidates the registration meta-text out of the Methods
--- Sections 2.2, 2.4, and 2.5 --- so that the Methods keep only
load-bearing status statements; each consolidated statement is preserved
here. The vocabulary convention: \\textbf{declared} fixes an object in
this manuscript's own record (a convention, a comparator class, or a
sensitivity layer stated in the text); \\textbf{registered} attaches a
computational artifact to the archive (solver configuration, seeds,
identifiers, calibration records); \\textbf{pre-registered} dates and
freezes a plan before any run, as the stage-map reconstruction of
Section 3.4 does. The consolidated requirements:""",
"""This appendix collects the registration and reproducibility requirements stated in Sections 2.2, 2.4, and 2.5. The convention: an analysis is pre-registered when its plan is dated and fixed before any run, as the stage-map reconstruction of Section 3.4 is; computational artifacts (solver configuration, seeds, identifiers, calibration records) are archived with the materials. The consolidated requirements:""",
    tag='M8 appendix opener')
sub("""are a declared
  registration requirement""", """are
  registration requirements""", count=2, tag='registration req plural')
sub("""are a declared registration requirement
  (Section 2.5).""", """are registration requirements
  (Section 2.5).""", tag='1829')
sub("""--- is a registered requirement
  attached with the computational archive (Section 2.4).""",
    """--- is archived with the computational materials (Section 2.4).""", tag='1826')
sub("that the text never prints (", "that the text does not list (", tag='never prints')
sub("""are part of this declared computational record;
Table 3 collects what the manuscript itself prints.""",
    """are part of the computational record;
Table 3 collects the parameter values stated in the text.""", tag='1840')
sub("""the Data
availability statement tracks the deposit status""",
    """the Data
availability statement records the deposit status""", tag='tracks')
sub("Parameter values printed in this manuscript for the",
    "Parameter values stated in this manuscript for the", tag='T3 caption printed')
sub("""entries the text does not print are marked as
such and remain attached to the declared computational record (this
appendix).""",
    """values not stated in the text remain in the computational record (this
appendix).""", tag='T3 caption marked')
sub("\nValue as printed\n", "\nValue as stated\n", tag='T3 head value')
sub("\nPrinted at\n", "\nStated at\n", tag='T3 head printed')
sub("""& not
printed in this manuscript & declared computational record (this
appendix) \\\\""", """& not
listed here & computational record (this
appendix) \\\\""", count=2, tag='T3 rows')
sub("""0.75; declared sensitivity
layer""", """0.75; sensitivity
layer""", tag='1895')
sub("""0.001; declared sensitivity
0.1""", """0.001; sensitivity
0.1""", tag='1900')

# ---------- Appendix B ----------
sub("""\\subsection{Appendix B. Distributive constraints where reproducible
(relocated from Section
4.6)}\\label{appendix-b.-distributive-constraints-where-reproducible-relocated-from-section-4.6}""",
"""\\subsection{Appendix B. Distributive constraints where reproducible}
\\label{appendix-b.-distributive-constraints-where-reproducible}""", tag='M6 appB title')
sub("can be carried, it is carried at\nmeasurement level.",
    "can be presented, it is presented at\nmeasurement level.", tag='AppB carried')
sub("""and the declared candidate
constituency for 2J3KL is the registered inshore harvesters""",
    """and the candidate
constituency for 2J3KL is the registered inshore harvesters""", tag='1920')
sub("each row declared rather than resolved:", "each row stated rather than resolved:", tag='1923')
sub("""Floor & declared cutoff \\((I_k, c_k)\\) & none operational & not declared
& declared instrument and cutoff \\\\""",
    """Floor & specified cutoff \\((I_k, c_k)\\) & none operational & not specified
& specified instrument and cutoff \\\\""", tag='1951 floor')
sub("""all require declaration before a floor
measures anything.""", """all must be specified before a floor
measures anything.""", tag='require declaration')

# ---------- References (M4) ----------
sub("""
Abaee, A. 2026. Delay-induced regime change in harvested stocks: the
mobilising and protective channels of institutional feedback, and the
review interval as control. Zenodo.
https://doi.org/10.5281/zenodo.22554217. Companion delay-dynamics study.
""", "\n", tag='M4 remove Abaee')
sub("""\\label{references}

Alkire, S., and Foster, J. 2011.""",
    """\\label{references}

Abaee, A. 2026. Delay-induced regime change in harvested stocks: the
mobilising and protective channels of institutional feedback, and the
review interval as control. Zenodo.
https://doi.org/10.5281/zenodo.22554217.

Alkire, S., and Foster, J. 2011.""", tag='M4 insert Abaee first')

# ---------- Supplementary paragraph ----------
sub("hypotheses with declared tests (S7),", "hypotheses with specified tests (S7),", tag='2120')
sub("""are the declared registration
requirements that the register tracks.""",
    """are registration
requirements tracked in the register.""", tag='2123')
sub("""by the labelled pre-registered reconstruction of
Section 3.4 --- a new declared object with registered plan, code, and
outputs ---""",
    """by the pre-registered reconstruction of
Section 3.4 --- a newly specified object with archived plan, code, and
outputs ---""", tag='2126')

# ---------- Declarations ----------
sub("are declared registration requirements; the", "are registration requirements; the", tag='2142')
sub("""the dated
pre-registration plan (parameter table""",
    """the dated
preregistration plan (parameter table""", tag='2146 hyphen')
sub("The authors declare no competing interests.", "The author declares no competing interests.", tag='M7 authors')

open(PATH, 'w').write(t)
print(f'OK - all v27 substitutions applied ({n0} -> {len(t)} bytes)')

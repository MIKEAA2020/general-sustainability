"""Merge paper 6 (assessment separation) + paper 10 (typed flux ledgers).

Both close on the SAME general claim, from different directions:
  6:  "...not of either tradition ... an index can be sound at the level of accounting
       and still over-certify at the level of assessment."
  10: "For ecological-economics measurement, that is the closing statement: not rival
       doctrines but two readings of one ledger, and the vector reading is what carries
       the certificate."
Paper 6 gives the GEOMETRIC reason (a quantifier commutation that fails on an open
region; the gap is the part of the convex hull no single plan dominates).
Paper 10 gives the CONSERVATION reason (typed moieties cannot be summed; conservation is
proved from incidence structure, not assumed).
Together: compensatory aggregation is not a doctrine to be weighed but a representation
error that over-certifies -- and the error is structural, not a knife-edge.
"""
import sys
sys.path.insert(0, '/home/user/p5')
from mergelib import merge

BASE = '/home/user/papers/'
A = 'paper06_assessment_separation_v65.tex'
B = 'paper10_depletion_ledgers_v52.tex'
OUT = 'paper06_assessment_separation_v66.tex'

TITLE = ("Aggregation is a claim, not a presentation: the geometry of the acceptance gap "
         "and the typed ledger that forbids closing it")

ABSTRACT = r"""
\begin{abstract}
\noindent\textbf{The general claim.} Aggregating incommensurable quantities into a single index is
standardly treated as a \emph{doctrine} --- weak sustainability versus strong, substitution
permitted versus floors separately binding --- to be weighed against its alternative. This paper
argues that it is better understood as a \emph{representation error with a geometric signature},
and that the error is structural rather than a knife-edge. Two independent lines establish it. The
first is geometric: on a common finite-horizon datum with path-wise constraints, the compensatory
reading (per-weight acceptance) and the noncompensatory reading (common-plan acceptance) are
related by a \emph{quantifier commutation that can fail on an open region of state space}, and for
any finite menu the acceptance gap is exactly the part of the convex hull of the required margins
that \emph{no single plan dominates}. The second is conservation-theoretic: in a correctly typed
stock--flow ledger, biomass, financial flows and biodiversity metrics are different \emph{moieties}
and cannot lawfully be summed, conservation being proved from the incidence structure of the
compartment--flux network rather than assumed. \emph{An index can therefore be sound at the level
of accounting and still over-certify at the level of assessment}, because certification is a
quantifier statement about transitions, not a property of a number. Where separately-binding floors
matter, per-floor reporting is not a presentation preference but a \textbf{detection requirement}:
the aggregate alone cannot distinguish the rescue region from the impossibility region.

\noindent\textbf{Why two parts.} Each part supplies the reason the other does not. Part I proves
the separation as a theorem about operators on a finite deterministic menu, and explicitly does
\emph{not} rank doctrines --- the structural character of the separation is a property of the menu,
not of either tradition. It gives the gap its shape: nonempty interior, so not a measure-zero
pathology; and the mechanism is identified as the \emph{policy dependence} of the
aggregate-feasible transition, not scalarization blindness, since at fixed trajectories the
full-cone aggregate is lossless. Part II supplies the accounting in which the noncompensatory
reading is the correct one, by showing what a lawful aggregate would have to be: conservation
proved from incidence, positivity proved from donor limitation, services as readouts rather than
mass, and substitution located \emph{within} the ledger as either a recycled flux or a drawdown on
a second compartment --- different entries with different statuses. Part I says the gap is real and
geometric; Part II says the coordinate-wise reading is the one that carries the certificate.

\noindent\textbf{What is found.} Part I: on an explicit rational datum the acceptance gap is a
region with nonempty interior --- every nonnegative weighting licenses some transition, no
transition is licensed by all, and no transition satisfies the floors path-wise. Mixing plans as
fractional blends closes every aggregate-certified state exactly, while alternating between plans
over time does not, so the two ways of combining plans are not equivalent. The certified set splits
into states rescuable by a resource-controlled action and states impossible under every weight.
Part II: the closed finite-donor ledger carries its complete theorem set --- the natural-block mass
identity, orthant invariance, no interior rest at positive effort, the vanishing-extraction rest
set (extinction, carrying capacity, and a frozen-biomass face), extraction integrability --- and
``depletion time'' is unpacked into three mutually non-interchangeable quantities: gross turnover
intensity, a frozen-rate local ratio, and a scenario-conditioned hitting time with uniform-drift
bounds. Three widely cited public-data indicators are then classified within that taxonomy at their
exact status.

\noindent\textbf{Structure.} Part I is the assessment-separation theorem and Part II the typed
ledger and depletion arithmetic. Each is self-contained and reproduced in full from its companion
paper without condensation, opening with that paper's own abstract. A cross-part conclusion
follows.
\end{abstract}
"""

CROSS = r"""
\section{Cross-part conclusion}
\label{conclusion}

The two parts above converge on one claim from different directions, and the convergence is worth
stating carefully because it is easy to mistake for a normative position. It is not one.

\emph{The claim.} Compensatory aggregation is not a doctrine to be weighed against its alternative;
it is a \emph{representation error} that over-certifies, and the error has a geometric signature.
Part I supplies the geometry: for any finite menu of margin-reducible plans, the acceptance gap is
the part of the convex hull of the required margins that \emph{no single plan dominates} --- so the
constructed witness is an instance of a geometric fact rather than an isolated pathology. Part II
supplies the accounting: in a typed stock--flow ledger, the moieties are not commensurable,
conservation is proved from the incidence structure rather than assumed, and substitution is located
\emph{within} the ledger --- as either a recycled flux returned to the regenerating pool or a
non-renewable drawdown on a second compartment, which are different entries with different
statuses. \emph{It is therefore not rival doctrines but two readings of one ledger, and the vector
reading is what carries the certificate.}

\emph{Why the gap is not a knife-edge, and why that matters.} The failure is a quantifier
commutation that can fail on an \emph{open region} of state space, and on the explicit rational
datum the gap has nonempty interior: every nonnegative weighting licenses some transition, no
transition is licensed by all, and no transition satisfies the floors path-wise. This is the
difference between a caution and a theorem. A measure-zero pathology could be dismissed as a
construction; an open region cannot. It is also why \emph{per-floor reporting is a detection
requirement rather than a presentation preference}: the aggregate alone cannot separate the states
that are rescuable by a resource-controlled action from the states that are impossible under every
weight, and those two regions demand opposite responses.

\emph{The mechanism, precisely stated.} Part I is explicit that the mechanism is \emph{not}
scalarization blindness: at fixed trajectories the full-cone aggregate is lossless. It is the
\emph{policy dependence} of the aggregate-feasible transition --- the aggregate is a statement about
\emph{there exists a weight}, while the floors are a statement about \emph{for all coordinates},
and the two quantifiers do not commute once the plan may depend on the weight. Part II gives the
same distinction its accounting form: a substitute is not a neutral re-labelling but a specific
ledger entry with a specific status. Both parts therefore locate the problem in the same place ---
not in the number, but in what is being quantified over.

\emph{What this implies for composite indices.} An index can be sound at the level of accounting
and still over-certify at the level of assessment. That is the practical content, and it is a
statement about \emph{use} rather than about construction: the arithmetic can be impeccable and the
inference drawn from it unsupported. Part II makes the same point from the other side by unpacking
``depletion time'' into three mutually non-interchangeable quantities --- gross turnover intensity,
a frozen-rate local ratio, and a scenario-conditioned hitting time --- and then classifying three
widely cited public-data indicators within that taxonomy \emph{at their exact status}. Each of
those indicators answers exactly the question its construction poses: a statistical index of
record-relative stress, an arithmetic ratio of an economic classification, a pressure scale of one
gross loss rate. Stating them with those questions is what makes them usable; reading any of them
as a literal ``time to depletion'' is the classification drift Part II identifies as a failure mode.

\emph{Scope, stated once.} Part I's theorem establishes \emph{no ranking of doctrines}: the
structural character of the separation is a property of the finite deterministic menu, not of
either the weak- or the strong-sustainability tradition. Part II records, with reasons, why the
closed ledger and the open working systems of institutional dynamics are different completions
sharing one exact object. Neither part claims that aggregation is never permissible; the claim is
that where separately-binding floors matter, the aggregate cannot be the instrument that detects
their violation.
"""

HEAD_A = r"""
\part*{Part I --- The assessment separation: a quantifier commutation that fails}
\label{part:separation}
\addcontentsline{toc}{part}{Part I --- The assessment separation}
"""

HEAD_B = r"""
\part*{Part II --- The typed ledger: what a lawful aggregate would have to be}
\label{part:ledger}
\addcontentsline{toc}{part}{Part II --- The typed ledger}
"""

merge(BASE, A, B, OUT, TITLE, ABSTRACT, CROSS, HEAD_A, HEAD_B, 'sep-', 'led-')

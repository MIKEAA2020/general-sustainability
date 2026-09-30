"""Merge paper 1 (obstruction calculus) + paper 2 (probabilistic sufficiency).

Paper 2 is explicitly a companion: "The belief-state safety value carries the obstruction
calculus into the probabilistic setting without loss of exactness." Merged, the two
establish that nonviability under incomplete observation is certifiable in exact arithmetic
in BOTH the set-valued and the probabilistic reading, and that the two readings are the
same object at different resolutions rather than competing approximations.
"""
import sys
sys.path.insert(0, '/home/user/p5')
from mergelib import merge

BASE = '/home/user/papers/'
A = 'paper01_obstruction_calculus_v61.tex'
B = 'paper02_probabilistic_sufficiency_v12.tex'
OUT = 'paper01_obstruction_calculus_v62.tex'

TITLE = ("Certifying nonviability under incomplete observation: the obstruction calculus "
         "and its probabilistic counterpart, in exact arithmetic")

ABSTRACT = r"""
\begin{abstract}
\noindent\textbf{The general claim.} Under incomplete observation, the question ``is any
observation-based policy viable?'' has two answers that the literature treats as different
subjects: a combinatorial one, phrased on information states, and a probabilistic one, phrased
on distributions over them. This paper develops both and shows they are the \emph{same object at
two resolutions}, not competing approximations. The probabilistic theory does not soften the
combinatorial one into a degree of belief; it \emph{prices} it. The value-one level of the
belief-state safety recursion coincides exactly with the viable-set recursion of the calculus,
and the $\alpha$-vectors that represent the value are exactly the indicators of the maximal
jointly survivable subsets of the posterior support --- an antichain, and therefore
Sperner-bounded. So the probabilistic reading inherits the certificate structure rather than
replacing it: where the calculus says \emph{nonviable}, the belief value is bounded away from one
by a deficit that is itself exact and attained on natural instances. \emph{Certifying that
something cannot be done is a finite, checkable, exact act --- and it survives the passage from
sets to measures without any loss of exactness.}

\noindent\textbf{Why two parts.} Each part supports half of that claim. Part I develops the
instrument on \emph{information states}: sound sufficient conditions for nonviability ---
equivalently, necessary conditions for viability --- finitely checkable in the common-action,
fibre-certification and finite-horizon forms, with analytic drift-and-timing conditions
elsewhere. Part II asks what those certificates imply when the information state is a
\emph{distribution}, and carries the whole theory in exact rational arithmetic. Neither is the
other's corollary. The calculus is complete in finite systems by backward recursion and says
nothing about probability; the belief value assigns a number to every belief and says nothing
about the shape of the certificate. Their exact agreement at the value-one level is a theorem
relating them, not a reduction of one to the other, and the paper keeps the two theories
distinct so that the agreement stays a result rather than a definition.

\noindent\textbf{What is found.} Part I establishes six mechanisms --- two finitely checkable,
two closed-form conditional, one minimal, and a sixth under a policy-class restriction --- as a
nonexhaustive taxonomy of information-theoretic failure, each paired with the response
correspondence it empties and the \emph{design consequence} it licenses. They do not exhaust the
complement of the epistemic kernel; in finite systems backward recursion is complete. Part II
gives six matching results: the support identity above; exactness and parametric closed forms
over rational input data; the survival of the certificates as deficit lower bounds, attained on
natural instances under both symmetric and asymmetric priors; cell-by-cell agreement of the
certified delayed-regime class with its closed form, with the class declaration responsible for
exactly the 36 timing combinations on the grid; and an adaptive-observation audit that prices
late resolution exactly. Across both parts, \emph{the observation layer, not the forecast layer,
sets the value} --- the design rules are the ones the deterministic audits impose, now with a
price attached.

\noindent\textbf{Structure.} Part I is the obstruction calculus and Part II its probabilistic
counterpart. Each is self-contained --- its own results, tables, discussion and conclusions ---
and each is reproduced in full from its companion paper without condensation, opening with that
paper's own abstract. A cross-part conclusion follows, stating what transfers between the
set-valued and the probabilistic readings and what does not.
\end{abstract}
"""

CROSS = r"""
\section{Cross-part conclusion}
\label{conclusion}

The two parts above ask one question --- \emph{can any observation-based policy keep this system
within its constraints?} --- in the two languages available for it, and the answer is the same in
both. That agreement is the paper's central result, and it is worth stating precisely, because it
is easy to overstate.

\emph{What the two readings share, exactly.} The probabilistic theory is not an approximation to
the combinatorial one, and the combinatorial one is not the degenerate case of the probabilistic
one. They meet at an identity: the value-one level of the belief-state safety recursion
coincides with the viable-set recursion of the calculus, the posterior support coincides with the
set-valued post-state on finite models with deterministic kernels and observation maps, and
outside the value-one level the deficit satisfies
$1 - V_k(b) \ge \min_{x \in \mathrm{supp}(b)} b(x)$, attained on natural instances. Moreover the
$\alpha$-vectors are exactly the indicators of the maximal jointly survivable subsets of the
support --- an \emph{antichain}, Sperner-bounded, which is why the certified witness census
realizes three types rather than the continuum a generic belief-space value would permit. So the
probabilistic reading does not add a degree of confidence to a set-valued verdict; it \emph{prices}
the same verdict, and the price is exact.

\emph{Why this matters more than the identity itself.} The direction that has received the
systematic treatment in the literature is \emph{sufficiency}: Veliov's output-feedback regulation
condition, and the estimation-tube reduction, give the canonical answer to ``is there a policy
that works?''. The complementary direction --- certifying that \emph{no} observation-based policy
is viable --- has received less. That asymmetry is a practical problem, because a negative verdict
is what licenses a redesign: it is the difference between ``no policy we tried worked'' and
``no policy can work, and here is the finite object that proves it.'' Both parts supply finite,
checkable, \emph{exact} witnesses for that negative direction, and the fact that they do so in
integer and rational arithmetic means the witness can be re-inspected at script level rather than
trusted. \emph{A nonviability certificate is an artefact that a reader can check, not a claim a
reader must accept.}

\emph{What does not transfer.} The taxonomy is explicitly nonexhaustive: the mechanisms do not
exhaust the complement of the epistemic kernel, and only in finite systems is backward recursion
complete. So a system on which every mechanism here fails to fire is not thereby shown to be
viable --- the certificates are sound sufficient conditions for nonviability, not necessary ones,
and the paper states the gap rather than papering over it. Correspondingly, the agreement between
the two readings is proved under the stated structural hypotheses (finite models, deterministic
kernels and observation maps, rational input data); where those fail the two readings may come
apart, and nothing here asserts otherwise.

\emph{The design consequence, stated generally.} Every mechanism in Part I empties a specific
response correspondence, and each therefore licenses a specific \emph{design} response rather
than a generic appeal to better information: enlarging the command set when the admissible safe
actions are empty; a separating observation, or a shorter review interval, when the common safe
action set is empty; an earlier informative observation when the deadline is exceeded; a refined
index when the fibre criterion fails; correcting a known bias when the certainty-equivalence trap
binds. Part II's contribution to this is to attach a \emph{price} to each --- the adaptive-observation
audit prices late resolution exactly, and the stochastic layer prices observation noise. The
general lesson is that \emph{the observation layer, not the forecast layer, sets the value}: when
a managed system is failing, the remedial leverage is usually in what is measured and when, not
in predicting better from what is already measured.
"""

HEAD_A = r"""
\part*{Part I --- The obstruction calculus on information states}
\label{part:calculus}
\addcontentsline{toc}{part}{Part I --- The obstruction calculus}
"""

HEAD_B = r"""
\part*{Part II --- Probabilistic sufficiency on belief states}
\label{part:probabilistic}
\addcontentsline{toc}{part}{Part II --- Probabilistic sufficiency}
"""

merge(BASE, A, B, OUT, TITLE, ABSTRACT, CROSS, HEAD_A, HEAD_B, 'calc-', 'prob-')

"""Merge paper 3 (computational certification) + paper 4 (minimax dual certificates).

The two are explicitly cross-referenced as reaching the SAME finding in different
languages. Paper 4's conclusion: "A companion paper reaches an analogous conclusion for a
different pipeline: there the count is the information--time product rather than the input
dimension ... The two are the same finding in different languages, and the recurrence is the
point --- obstruction certificates are small objects whose size is set by the decision
variables, not by the uncertainty."

Merged, that recurrence stops being an observation about a sibling paper and becomes the
paper's own result, evidenced by two independent pipelines.
"""
import sys
sys.path.insert(0, '/home/user/p5')
from mergelib import merge

BASE = '/home/user/papers/'
A = 'paper03_computational_certification_v14.tex'
B = 'paper04_minimax_dual_certificates_v16.tex'
OUT = 'paper03_computational_certification_v15.tex'

TITLE = ("Obstruction certificates are small: computable bounds for nonviability and the "
         "measure dual that explains why")

ABSTRACT = r"""
\begin{abstract}
\noindent\textbf{The general claim.} A certificate that \emph{no} policy can keep a system within
its constraints is only useful if it is a small object --- finite, attainable by standard solvers,
and independently checkable. This paper establishes that it is, in two independent pipelines, and
identifies what sets its size: \emph{obstruction certificates are small objects whose size is set
by the decision variables, not by the uncertainty.} In the linear-programming pipeline a strictly
positive certified margin is a finite obstruction certificate and, whenever a positive certificate
exists, one can be chosen with at most $r+1$ safety rows --- $r$ an information--time rank, not an
input dimension. In the measure-dual pipeline the certificate is an adversarial probability measure
supported on at most $k+1$ points, $k$ the \emph{control} dimension, and that bound is tight.
Neither the state dimension, nor the cardinality of the disturbance set, nor the resolution of any
discretisation appears in either bound. \emph{The complexity of certifying nonviability is governed
by how many independent decisions the agent has, not by how large the world it operates in is.}
That is what makes these certificates usable rather than merely correct.

\noindent\textbf{Why two parts.} The two pipelines establish the same finding for different objects
and neither contains the other. Part I gives the \emph{computational} pipeline: an outer moment
approximation of all measurable information-adapted controls combined with an inner adversarial
approximation yields a finite linear program whose optimum is a certified lower bound on the
continuous-time safety value and whose error inflation is a certified upper bound; every
dual-feasible solution yields a finite lower-bound certificate covering every measurable policy.
Part II gives the \emph{duality} pipeline: it asks whether the Farkas multiplier that the
polyhedral case happens to carry is an accident of that case or the shadow of something general,
and shows it is the latter --- the obstruction is not a failed search but the existence of a
measure witness. Part I says the certificate can be computed; Part II says what it \emph{is}. The
recurrence of the size bound across them is a result about obstruction certificates, not a
coincidence between two papers, and merging is what makes it visible.

\noindent\textbf{What is found.} Part I: along every admissible refinement sequence whose mesh and
stored-scenario widths vanish, nonviability is eventually detected; and the rank result shows the
bound is not an artefact of the construction --- for every $q$ there is a continuous-time system
with \emph{scalar} input and $q+1$ indistinguishable modes in which every proper subbelief is
viable, the full belief is not, and every certificate must involve all $q+1$ modes. So the
dimension that counts is the information--time product, and the Helly-type bound that would follow
from input dimension is \emph{false} for a common blind control function. Part II: for
control-affine dynamics with compact convex control set, the common safe-action set is empty
precisely when an adversarial measure drives expected inward drift strictly negative against every
control, with the $k+1$ bound tight; the polyhedral case recovers the $\ell_1$-normalised Farkas
multiplier exactly, and the singleton case recovers the Isaacs drift with the adversarial
\emph{distribution} load-bearing. A two-action instance exhibits a strict minimax gap --- without
convexity the equivalence fails and no measure certifies.

\noindent\textbf{Structure.} Part I is the computational certification pipeline and Part II the
measure dual. Each is self-contained and reproduced in full from its companion paper without
condensation, opening with that paper's own abstract. A cross-part conclusion follows, stating the
shared size principle, the two recoveries, and where the equivalence fails.
\end{abstract}
"""

CROSS = r"""
\section{Cross-part conclusion}
\label{conclusion}

The two parts above build obstruction certificates by two different routes --- a finite linear
program over moment relaxations, and a measure-dual characterisation of emptiness --- and they
arrive at the same structural conclusion. That recurrence is the paper's central result.

\emph{The shared principle.} \textbf{Obstruction certificates are small objects whose size is set
by the decision variables, not by the uncertainty.} Part I: whenever a positive certificate exists,
one can be chosen with at most $r+1$ safety rows, $r$ the information--time rank. Part II: the
witness measure is supported on at most $k+1$ points, $k$ the control dimension, and the bound is
\emph{tight} --- attained, not merely approached. In neither bound does the state dimension, the
cardinality of the disturbance set, or the resolution of any discretisation appear. The two counts
are not the same number and are not claimed to be: they count different decision variables in
different pipelines. What is shared is the \emph{form} of the dependence. Certifying that something
cannot be done costs a number of degrees of freedom set by what the agent may decide, and is
otherwise insensitive to how much the agent does not know.

\emph{Why the bound is substantive rather than decorative.} A bound is only interesting if it can
fail, and Part I exhibits the failure of the natural alternative. A Helly-type statement --- at most
$m+1$ compatible states suffice to witness nonviability --- is valid for convex common-action sets
in $\mathbb{R}^m$ and is \emph{false} for a common blind control function: for every $q$ there is a
system with scalar input and $q+1$ indistinguishable modes in which every proper subbelief is
viable while the full belief is not, so every certificate must involve all $q+1$ modes. The
correct dimension therefore counts independent \emph{temporal and informational} control decisions,
not inputs. This is not a technical footnote: it decides whether certificate-size claims for
review intervals, delayed sensing, and adaptive observation are true, and it is the reason the
information--time product --- rather than any input dimension --- is the quantity that appears in
Part I's bound.

\emph{What the obstruction is, and why that matters.} Part II's contribution is ontological rather
than algorithmic: the obstruction is not \emph{merely a failure of a search to find a safe action};
it is the existence of a \emph{witness} to that failure, and the witness is a measure. This is the
same movement that carries linear programming from ``the solver found nothing'' to ``here is a dual
ray,'' and it carries the same benefit: the certificate is checkable without re-running the search,
and it localises the failure on the active set. Read together with Part I, the two parts therefore
give the negative verdict the same standing that a positive one enjoys --- a nonviability claim
becomes an artefact a reader can verify, not an assertion a reader must trust.

\emph{Where the equivalence fails, stated plainly.} The measure characterisation requires convexity.
A two-action instance exhibits a strict minimax gap: without convexity the equivalence fails and
\emph{no measure certifies}. Part I's guarantee is correspondingly one-directional in general ---
nonviability is eventually detected along admissible refinement sequences, but a failure to detect
at finite refinement is not a proof of viability. Both parts state their own scope delimitations
rather than letting the shared principle imply more than it does.

\emph{The two recoveries, and what they license.} The polyhedral case recovers the
$\ell_1$-normalised Farkas multiplier exactly, and the singleton case recovers the Isaacs drift
with the adversarial distribution over disturbances load-bearing. So the classical objects --- Farkas
infeasibility certificates and Isaacs minimax drift conditions --- are not rival frameworks but
specialisations of one duality, and a practitioner already using either is already using this one.
What the unification licenses is the transfer of the checkability property: a certificate that can
be verified without re-running the search, whose size is known in advance, and which localises the
failure it reports.
"""

HEAD_A = r"""
\part*{Part I --- Computational certification: a finite linear program covering every measurable policy}
\label{part:computational}
\addcontentsline{toc}{part}{Part I --- Computational certification}
"""

HEAD_B = r"""
\part*{Part II --- The measure dual: what the obstruction is dual to}
\label{part:measure-dual}
\addcontentsline{toc}{part}{Part II --- The measure dual}
"""

merge(BASE, A, B, OUT, TITLE, ABSTRACT, CROSS, HEAD_A, HEAD_B, 'lp-', 'dual-')

#!/usr/bin/env python3
"""
v43 — joint-audit implementation for paper 2 (Automatica routes).

Accepted items from the nonstandard-proposals joint audit
(paper2_nonstandard_joint_audit.md; verification: 51/51 exact checks):

1. New Section 3.7 "A recourse certificate for the post-observation mode":
   oracle-recourse proposition (sound against every measurable
   information-adapted policy; generally incomplete, stated as such) + the
   compressed three-branch braking instance with exact threshold
   tau_max = 7/50 and certificate Gamma(tau) = tau - 7/50.
2. Section 3.4 scoping remark: the m+1 sparse-witness bound is instantaneous;
   blind window-policies are governed by information-time rank (q+1
   scalar-input counterexample).
3. Section 3.2 remark: numerical robustness of the polyhedral certificate
   (graceful degradation eps < mu_0/||mu||_1; residual-tolerant test
   c + h_U(-r) < 0; relax-toward-the-controller orientation rule).
4. Section 6.5(ii) limitation rewritten to credit the new certificate while
   keeping completeness open; limitation (i) range extended to 3.7;
   Organization (1.4) updated; Supplementary A.3 aligned with a pointer.

No other content is modified. v42 files are left untouched.
"""

LATEX = "/home/user/arena agent 1/paper rewrites/latex"
MAIN_IN = f"{LATEX}/paper2_obstruction_calculus_v42_Automatica_routes.tex"
SUPP_IN = f"{LATEX}/paper2_obstruction_calculus_v42_Automatica_routes_supplementary.tex"
MAIN_OUT = f"{LATEX}/paper2_obstruction_calculus_v43_Automatica_routes.tex"
SUPP_OUT = f"{LATEX}/paper2_obstruction_calculus_v43_Automatica_routes_supplementary.tex"


def replace_once(text, old, new, what):
    n = text.count(old)
    assert n == 1, f"{what}: expected exactly 1 occurrence, found {n}"
    return text.replace(old, new)


REM_ROBUST = r"""\begin{remark}[numerical robustness of the polyhedral certificate]\label{rem:robust-farkas}
Linearity makes the Farkas certificate robust in two practical senses. First,
bounded data perturbation degrades the margin gracefully: if
\(\mu \ge 0\) certifies \(\mu^{\top} A = 0\) and \(\mu^{\top} b \le -\mu_0 < 0\),
then for perturbed right-hand sides \(b + \Delta b\) with
\(\|\Delta b\|_\infty \le \epsilon\) the same multipliers give
\(\mu^{\top}(b + \Delta b) \le -\mu_0 + \|\mu\|_1 \epsilon\), still negative
while \(\epsilon < \mu_0/\|\mu\|_1\); the margin \(\mu_0\) is exactly the
certificate's numerical robustness, and normalized multipliers
(\(\|\mu\|_1 = 1\), as in Section~3.4's worked certificate) maximize the
tolerable perturbation. Second, verified approximate data suffice: if the
multipliers are computed with residual \(r := \hat\mu^{\top} \hat A\) and
objective \(c := \hat\mu^{\top} \hat b\), then feasibility of some
\(u \in U\) would imply \(-h_U(-r) \le r^{\top} u \le c\), where
\(h_U(g) := \sup_{v \in U} g^{\top} v\) is the support function of the action
set; hence the test \(c + h_U(-r) < 0\) --- with all integration, rounding,
and enclosure errors charged into \(c\) and \(r\) before it is applied ---
certifies infeasibility without exact stationarity. Both extensions share the
orientation rule for nonviability certificates: uncertain row data must be
relaxed toward a larger feasible controller set, never toward a smaller one;
tightening \(\hat b\) on the strength of an unverified worst case can
manufacture a false obstruction.
\end{remark}
"""

REM_SCOPE = r"""\textbf{Scope of the count: instantaneous actions, not window-policies.}
The \(m+1\) bound counts independent instantaneous decisions: it applies to a
common action \(u \in U \subseteq \mathbb{R}^m\), and it fails for common blind
control \emph{functions}. Partition a blind window into \(Q\) blocks
\(I_1, \dots, I_Q\) and let \(q + 1\) branches be indistinguishable throughout,
with scalar input (\(m = 1\)): branch \(j \le q\) evolves as
\(\dot x_j = \mathbf{1}_{I_j}(t)(u - 1)\) from \(x_j(0) = 0\) under the floor
\(x_j \ge 0\), which forces \(u \equiv 1\) on every block (each
\(w_j = \int_{I_j} u \, dt = 1\)), while branch \(q+1\) evolves as
\(\dot x_{q+1} = -u\) from \(x_{q+1}(0) = q - \varepsilon\) under the same
floor, forcing \(\sum_j w_j \le q - \varepsilon\). Summing the forced
withdrawals gives \(0 \le -\varepsilon\): the full system is infeasible, while
removing any single branch restores feasibility (\(u \equiv 1\), or \(u = 0\)
on the dropped branch's block and \(1\) elsewhere), so every obstruction
involves all \(q+1\) branches --- far more than \(m + 1 = 2\). The adjoint
kernels here are the block indicators, of rank \(q\): for window-policies the
governing count is the information--time rank, and sparsity claims for
review-interval and delayed-sensing certificates must be stated in the block
dimension \(mQ\), not the instantaneous dimension \(m\) (cf.\ the block
structure of the delayed-information check in Section~8).
"""

SEC37 = r"""\subsubsection{3.7 A recourse certificate for the post-observation
mode}\label{recourse-certificate}

The certificates so far fire before information discriminates: the
common-action obstruction is instantaneous (Section 3.2) and the timing
obstruction exits within the blind window (Section 3.3, Remark
\ref{rem:sigma}). Section 6.5(ii) isolates the complementary mode:
insufficient post-observation recourse. In that mode a common blind-window
control keeps every branch safe, yet no observation-adapted control can
recover every branch once the distinguishing observation arrives; the discrete
instance of Supplementary A.3 exhibits the mode while no certificate fires.
This subsection supplies a continuous-time certificate for the mode. Its
soundness covers every measurable information-adapted policy. Completeness is
not claimed, because the certificate relaxes the post-observation class
upward: an oracle grants each stored branch its own controller whether or not
the sensor reveals that much, and an oracle failure is only a sufficient
condition for real failure.

\begin{proposition}[oracle-recourse obstruction]\label{prop:recourse}
Let the dynamics be affine in the control,
\(f(x,u,d) = f_0(x,d) + B(x)\,u\), with compact convex
\(U \subseteq \mathbb{R}^m\), and let branches
\(x_1, \dots, x_L \in B_0\) be observation-equivalent on \([0, \tau)\) with
horizon \(T > \tau\) (disturbances admitted, \(D\) compact). Fix a label
\(\ell = (\theta, j, t)\) --- branch \(\theta\), constraint \(j\), time
\(t \in (\tau, T]\) --- and a disturbance realization \(d(\cdot)\). Let
\(\bar x_\theta^d(\cdot)\) denote branch \(\theta\)'s zero-control
realization under \(d(\cdot)\), \(X_\theta^d(\cdot, \cdot)\) its
state-transition matrix, and \(B^d(\sigma) := B(\bar x_\theta^d(\sigma))\).
Define the input kernel
\[k_\ell^d(\sigma) = \mathbf{1}_{\{\sigma \le t\}}\,
\big(B^d(\sigma)\big)^{\top}
\big(X_\theta^d(t, \sigma)\big)^{\top}
\nabla q_j\big(\bar x_\theta^d(t)\big),\]
let \(\beta_\ell^d = q_j\big(\bar x_\theta^d(t)\big)\) denote the
zero-control facet margin at the label, and write
\(\phi_U(g) := \min_{v \in U} g^{\top} v\). For weights
\(\lambda_\ell \ge 0\), \(\sum_\ell \lambda_\ell = 1\), define the
recourse certificate
\[\begin{aligned}
\Gamma(\lambda) = \inf_{d(\cdot)} \Big\{ &\int_0^{\tau}
\phi_U\Big(\sum_{\ell} \lambda_\ell k_\ell^d(\sigma)\Big) d\sigma \\
&\quad + \sum_{\ell} \int_{\tau}^{T}
\phi_U\big(\lambda_\ell k_\ell^d(\sigma)\big) d\sigma
- \sum_{\ell} \lambda_\ell \beta_\ell^d \Big\},
\end{aligned}\]
the infimum over admissible disturbance realizations (for affine dynamics
each bracket is computable in closed form by variation of constants). If
\(\Gamma(\lambda) > 0\), then
\(B_0 \notin \mathrm{ERViab}_{\mathcal{I}}(\mathcal{V})\): some stored
facet is violated along some branch, for every policy in the stated class and
every branch selection.
\end{proposition}

\emph{Proof sketch.} On \([0, \tau)\) every policy acts through one common
measurable signal (the blind-window reduction of Theorem~\ref{thm:delayed});
on \([\tau, T)\) the oracle grants each branch its own arbitrary measurable
signal. Fix \(d(\cdot)\). Safety of every branch at every stored label
would require, for each \(\ell\), a realized facet value
\(\beta_\ell^d + \int \big(k_\ell^d\big)^{\top} u\, d\sigma \ge 0\).
Weight by \(\lambda\) and sum: the pre-\(\tau\) term pools,
\(\big(\sum_\ell \lambda_\ell k_\ell^d\big)^{\top} u \ge
\phi_U\big(\sum_\ell \lambda_\ell k_\ell^d\big)\) pointwise, and the
post-\(\tau\) terms separate,
\(\lambda_\ell \big(k_\ell^d\big)^{\top} u_\theta \ge
\phi_U(\lambda_\ell k_\ell^d)\). Summing and rearranging, weighted
safety implies the bracket is nonnegative for every \(d(\cdot)\), hence its
infimum is nonnegative --- contradicting \(\Gamma(\lambda) > 0\). The
relaxation is lossy exactly through the pooled pre-\(\tau\) term:
superadditivity of the support minimum,
\(\phi_U(g_1 + g_2) \ge \phi_U(g_1) + \phi_U(g_2)\), shows that
separating the branches earlier only weakens the certificate, so delaying
information to \(\tau\) is what the first integral measures.
\hfill\(\square\)

\begin{example}[three branches, delayed recourse]\label{ex:three-branch}
A planar braking instance in which the obstruction is purely one of
post-observation recourse. Branches \(j = 1, 2, 3\) run \(\dot p = v\),
\(\dot v = u\) (no disturbance) from
\(p_j(0) = \tfrac{34}{25} n_j\), \(v_j(0) = n_j\), where
\(n_1 = (1, 0)\), \(n_2 = (-\tfrac{3}{5}, \tfrac{4}{5})\),
\(n_3 = (-\tfrac{3}{5}, -\tfrac{4}{5})\); the actuator set is
\(U = \mathrm{conv}\{\pm n_1, \pm n_2, \pm n_3\}\) (the hexagon
\(|u_2| \le \tfrac45\), \(|2u_1 \pm u_2| \le 2\)); safety is
\(n_i^{\top} p \le 2\) for \(i = 1, 2, 3\) with
\(\|v\|_\infty \le \tfrac65\); the realized branch is revealed at time
\(\tau\). Every branch is viable under full information --- brake along
\(-n_j\) for one second; peak critical position
\(\tfrac{34}{25} + \tfrac12 = \tfrac{93}{50} < 2\) --- and \(u \equiv 0\)
keeps every branch strictly safe through any blind window of length up to
\(\tfrac{16}{25}\) \((n_j^{\top} p_j(\tau) = \tfrac{34}{25} + \tau)\):
no instantaneous or blind-window certificate fires. Yet the label
\((j,\ n_j^{\top} p \le 2,\ \tau + 1)\) along branch \(j\) has
zero-control margin \(\beta_j = \tfrac{16}{25} - \tau - 1\) and kernel
\(\mathbf{1}_{\{\sigma \le \tau + 1\}} (\tau + 1 - \sigma) n_j\); the
weights \(\lambda = (\tfrac38, \tfrac5{16}, \tfrac5{16})\) pool the
pre-observation kernel to zero, and the recourse certificate evaluates to
\[\Gamma(\tau) = -\int_{\tau}^{\tau+1} (\tau + 1 - \sigma)\, d\sigma
- \Big(\tfrac{16}{25} - \tau - 1\Big) = \tau - \tfrac{7}{50}.\]
For \(\tau > \tfrac{7}{50}\) the triple is nonviable --- the blind window
accumulates braking liability that the post-observation authority cannot
discharge on every branch at once --- while the hold-then-brake policy
(\(u = 0\), then \(-n_j\) for one second) is safe exactly to
\(\tau = \tfrac{7}{50} = 0.14\): the threshold is exact. The obstruction
is genuinely three-way: at \(\tau = \tfrac15\), every pair of branches is
jointly viable under a common blind control (worst critical positions
\(\tfrac{2469}{1250} = 1.9752\) and \(\tfrac{2419}{1250} = 1.9352\), both
below \(2\)), so six of the seven nonempty priors over these branches are
viable at a delay where the triple is not. The discrete analogue in which no
certificate fires is Supplementary A.3; here the recourse certificate fires,
with margin \(\Gamma(\tfrac15) = \tfrac3{50}\).
\end{example}

The certificate is deliberately asymmetric, like the calculus it joins: it is
sound against every measurable policy of the information class, its stored
labels are finite and independently checkable (exact arithmetic throughout the
instance above), and its incompleteness is explicit --- a complete
continuous-time characterization of the recourse mode remains open
(Section 6.5(ii)).
"""

SUPP_APPEND = r""" The main text supplies the continuous-time counterpart (Section 3.7 there): an oracle-relaxed recourse obstruction whose three-branch braking instance fires exactly in this regime --- blind-window safety with insufficient post-observation braking authority --- with exact delay threshold \(\tau = 7/50\)."""


def main():
    m = open(MAIN_IN, encoding="utf-8").read()
    s = open(SUPP_IN, encoding="utf-8").read()

    # 1. Section 3.2 robustness remark (after the Farkas witness paragraph)
    m = replace_once(
        m,
        "supplies one under the\nconvexity hypotheses stated in Section 3.4.\n",
        "supplies one under the\nconvexity hypotheses stated in Section 3.4.\n\n" + REM_ROBUST,
        "3.2 robustness remark anchor")

    # 2. Section 3.4 scoping remark (after the nonconvexity paragraph)
    m = replace_once(
        m,
        "The convexity hypotheses of Proposition~\\ref{prop:helly} exclude exactly this failure mode.\n",
        "The convexity hypotheses of Proposition~\\ref{prop:helly} exclude exactly this failure mode.\n\n" + REM_SCOPE,
        "3.4 scope remark anchor")

    # 3. New Section 3.7 before Section 4
    m = replace_once(
        m,
        "\\subsection{4. Certification Limits}\\label{certification-limits}",
        SEC37 + "\n\\subsection{4. Certification Limits}\\label{certification-limits}",
        "3.7 insertion anchor")

    # 4. Limitation (i): extend the certificate range
    m = replace_once(
        m,
        "The continuous-time certificates of Sections 3.2--3.3 and 3.5--3.6 are sufficient conditions",
        "The continuous-time certificates of Sections 3.2--3.3 and 3.5--3.7 are sufficient conditions",
        "limitation (i) range")

    # 5. Limitation (ii): credit the new certificate, keep completeness open
    m = replace_once(
        m,
        "the finite-horizon recursion (Section 3.1) captures that mode, but no continuous-time certificate for it is supplied here. An explicit instance --- a three-state system whose root belief is one-step viable yet whose post-observation belief is nonviable, with no certificate firing --- is given in the Supplementary Material (S3, A.3).",
        "the finite-horizon recursion (Section 3.1) captures that mode exactly, and the oracle-recourse certificate of Section 3.7 certifies it in continuous time --- soundly against every measurable information-adapted policy under an oracle relaxation of the post-observation class, with a worked three-branch instance whose delay threshold is exact; what remains open is a complete continuous-time characterization that does not relax the post-observation class. A discrete instance in which every one-step certificate is silent is given in the Supplementary Material (S3, A.3).",
        "limitation (ii) rewrite")

    # 6. Organization: announce the new certificate
    m = replace_once(
        m,
        "--- as supporting certificates --- the finite-time exit certificate and the admissibility obstruction.",
        "--- as supporting certificates --- the finite-time exit certificate and the admissibility obstruction, together with a recourse certificate for the post-observation mode (Proposition~\\ref{prop:recourse}, Example~\\ref{ex:three-branch}).",
        "organization update")

    # 7. Supplementary A.3 alignment pointer
    s = replace_once(
        s,
        "and the timing certificate is silent because the observation arrives without delay.",
        "and the timing certificate is silent because the observation arrives without delay." + SUPP_APPEND,
        "supplementary A.3 pointer")

    assert "\\tfrac{7}{50}" in m
    assert "prop:recourse" in m and "ex:three-branch" in m

    open(MAIN_OUT, "w", encoding="utf-8").write(m)
    open(SUPP_OUT, "w", encoding="utf-8").write(s)
    print(f"wrote {MAIN_OUT} ({len(m)} bytes)")
    print(f"wrote {SUPP_OUT} ({len(s)} bytes)")


if __name__ == "__main__":
    main()

"""Build paper3_v3.md from uploads/qwen p3 starting point.txt by applying the verified
repairs recorded in review/starting_point_audits_verified_v1.md. Every anchor must occur
exactly once in the current text; otherwise the edit is skipped and reported."""
import re
SRC = 'uploads/qwen p3 starting point.txt'
OUT = 'revision/v3/paper3_v3.md'
t = open(SRC, encoding='utf-8').read()
ok, bad = 0, []

def rep(old, new):
    global t, ok
    n = t.count(old)
    if n != 1:
        bad.append(f"[count={n}] {old[:70].strip()!r}")
        return
    t = t.replace(old, new, 1); ok += 1

# ---- Section 2 -----------------------------------------------------------------
rep("## 2. The Typed Primitive Ledger\n", """## 2. The Typed Primitive Ledger

Notation is fixed once and is not re-assigned silently. One letter carries one sort wherever a computation is displayed. Symbols recurring in more than one role are declared with their scopes: \\(B\\) denotes gross turnover \\(R+T\\) (Section 2.3), the barrier pair \\(\\underline{B},\\overline{B}\\) (local to Section 3.1), the aggregate regeneration flow \\(b\\cdot M\\) (local to Section 1.3), and fisheries biomass \\(\\mathcal{B}\\) with its barrier \\(\\mathcal{B}_{\\min}\\) and reference \\(\\mathcal{B}_{\\mathrm{lim}}\\) (local to Sections 8.3 and 9.5); \\(b\\) denotes the boundary-transfer term of equation (1) and the service balance of Section 5.1; \\(d\\) denotes a disturbance (Section 2.2), the demand vector (Section 5.2) and the drift distance (local to Section 9.3); \\(s\\) and \\(\\sigma\\) denote the support and donor fractions (Section 2.3), distinct from the service readouts \\(s_i\\) (Section 5.1) and from the integration dummy of Theorem 14; \\(S\\) is the moiety readout \\(S=Cx\\), while \\(S_T\\) is the typed stoichiometric (incidence) operator, never written \\(N\\), which names the living stock; \\(X\\) is the living stock of the six-compartment scaffold of Section 4.2; \\(K\\) is the carrying capacity, the sink stock of the same scaffold, and the maintainability kernel when subscripted \\(K_{\\mathrm{maint}}\\); \\(\\tau\\) indexes hitting and exit times (\\(\\tau_{\\mathcal{B}},\\tau_m^{\\pm},\\tau_{\\mathrm{exit}}\\)); \\(\\varsigma\\) is the surrogate noise scale (Section 9); \\(\\varepsilon\\) is the drift bracket of Proposition 17, the resource-threshold fraction (Sections 8.2 and 9.6), the donor-draw diagnostic \\(\\varepsilon_G\\) (Section 10.2) and the slack in Section 7.2.

""")
rep("- \\(d_x\\) belongs to a stated disturbance class.",
"""- \\(d_x\\) belongs to a stated disturbance class.

Where a single vector is more convenient, \\(b(t) := B_T u_\\partial(t) + d_x(t)\\) collects the boundary-transfer and disturbance terms; the two notations denote one object and are used interchangeably below.""")
rep("If \\(L^\\top S_T = 0\\), then", "If \\(L^{\\top}S_T = 0\\) (the same covector written \\(\\ell\\) in Section 3), then")
rep("with \\(A_0 > 0\\), \\(A_{g0} > 0\\).",
"""with \\(A_0 > 0\\), \\(A_{g0} > 0\\). With \\(A_{g0}>0\\) the donor fraction \\(\\sigma\\) is smooth and strictly increasing in the donor level. The registered regime is the separation of scales \\(A_{\\text{geo}}\\gg A_{g0}\\), in which \\(\\sigma\\approx1\\); the separation is registered rather than assigned a numerical value, and the corner \\(A_{g0}=0\\) is the discontinuous limit \\(\\sigma\\equiv1\\) for \\(A_{\\text{geo}}>0\\), not the registered regime.""")
rep("\\[\nB = R + T.\n\\]\n\nThe donor-limited geo-interface primitives are:",
"""\\[\nB = R + T.\n\\]

Net regeneration is the difference of two non-negative primitives — gross regeneration \\(rNs\\) (support → stock) and density-dependent return \\(rN^2s/K\\) (stock → support) — so (2a)–(2d) below stay within the primitive-flux discipline of Section 2.1 despite the signed entry. Where the two primitives must be tracked separately they appear as their own columns of the incidence matrix rather than folded into \\(R\\).

The donor-limited geo-interface primitives are:""")
rep("""Under the institutional-failure specialization,

\\[
\\mu = \\nu = \\rho = 0,
\\qquad
C_A = 0,
\\]

the closed natural block is:""",
"""Under the institutional-failure specialization,

\\[
\\mu = \\nu = \\rho = 0,
\\qquad
C_A = 0,
\\]

the product, waste and price parameters of the unreduced ledger — its macroeconomic-feedback, recycling and price-response channels, set to zero together with the mining intensity \\(C_A\\) — are switched off, and the closed natural block is:""")
rep("The geological donor is an internal state throughout. No infinite reservoir is declared. Recharge is donor-limited and cannot run backward: at \\(A_{\\text{geo}}=0\\), \\(e_{GA}=0\\).",
"""Equations (2a)–(2d) are written for the specialization with mining inactive. With mining restored, (2c) reads \\(\\dot A_{\\text{geo}} = -e_{GA} + e_{AG} - C_{A,\\lim}\\) and the mass identity of Theorem 7 acquires its second export term. The mined fraction routes out of the four-coordinate block; the full-ledger theorems record the mining column as an internal transfer between compartments outside it, which is consistent because the block boundary, not the ledger boundary, is crossed.

Three recharge specifications occur in this article and in the companion analysis, and they are distinct objects:

| Recharge law | Form | Status |
|---|---|---|
| Primitive donor-limited exchange | \\(e_{GA}=\\omega_A A_{\\text{eq,intrinsic}}\\sigma\\) | the closed block's law: the forward rate depends on the donor alone, not on how empty the receiver is; the rest state is \\(A_{\\text{act}}=A_{\\text{eq,intrinsic}}\\sigma\\) (Theorem 13) |
| Target-relaxation | \\(\\omega_A(A_{\\text{eq}}-A)\\) | admissible only when donor-limited (Theorem 11): run backward at an empty donor it violates the primitive discipline, and it may be used only with the source declared an effectively infinite external reservoir, which makes the system open |
| Working derived target | \\(A_{\\text{eq},W}=A_{\\text{eq,intrinsic}}+\\kappa_A K/\\omega_A\\) | the companion delay-dynamics analysis's working completion; not a closed-block law, and one of the reasons recorded in Section 10.2 for the failure of reduction. No derived target appears in the closed block |

Recharge is donor-limited and cannot run backward: at \\(A_{\\text{geo}}=0\\), \\(e_{GA}=0\\). Mining \\(C_{A,\\lim}=C_A\\sigma\\) is donor-limited in the same sense as extraction. The geological donor is an internal state throughout; no infinite reservoir is declared.

The registered parameterization is \\(r=0.02\\), \\(K=100\\), \\(q=0.001\\), \\(\\kappa_A=0.05\\), \\(\\omega_A=10^{-3}\\), \\(A_0=1\\), \\(A_{\\text{eq,intrinsic}}=50\\) and \\(\\gamma_U=0.2\\). With \\(A_0>0\\) and \\(A_{g0}>0\\) the right-hand side of (2a)–(2d) is locally Lipschitz on the closed orthant, and the comparison \\(\\dot N\\le rN(1-N/K)\\), together with \\(\\dot N\\le0\\) once \\(N\\ge K\\), bounds the stock by \\(\\max\\{N(0),K\\}\\). Classical solutions therefore exist globally and remain in the orthant by Theorem 10; that is the sense in which "classical solution" is used throughout.

Harvest routing in the block is the corner \\(\\alpha=0\\) of the routing example below: harvest \\(qEN\\) exits the natural block entirely as product, and a positive detritus-routed fraction \\(\\alpha>0\\) would add \\(\\alpha qEN\\) to \\(\\dot U\\) and reduce the block export to \\((1-\\alpha)qEN\\). The mass identity of Theorem 7 is stated for the declared routing. The positive-part convention \\([\\cdot]_+\\), read as a one-way valve at a non-positive target, never binds here: the registered intrinsic target is positive.""")
rep("""S_{\\text{block}} =
\\begin{pmatrix}
1 & -1 & -1 & 0 & 0 & 0 & 0 & 0 \\\\
0 & -1 & 1 & 1 & -1 & 0 & 0 & 0 \\\\
0 & 0 & 0 & -1 & 1 & -1 & 0 & 0 \\\\
0 & 0 & 0 & 1 & -1 & 0 & 1 & -1
\\end{pmatrix}.
\\]""",
"""S_{\\text{block}} =
\\begin{pmatrix}
1 & -1 & -1 & 0 & 0 & 0 & 0 & 0 \\\\
-1 & 1 & 0 & -1 & 1 & 1 & -1 & 0 \\\\
0 & 0 & 0 & 0 & 0 & -1 & 1 & -1 \\\\
0 & 0 & 0 & 1 & -1 & 0 & 0 & 0
\\end{pmatrix},
\\]

with rows \\((N,A_{\\text{act}},A_{\\text{geo}},U)\\) and columns, in order, gross regeneration, density-dependent return, harvest, uptake, detritus return, \\(e_{GA}\\), \\(e_{AG}\\) and mining.""")
rep("Every column is a two-compartment transfer or a block-boundary export. The internal columns sum to zero. The export columns—harvest and, when restored, mining—carry column sums \\(-1\\). Summing the rows reads off the mass identity directly:",
"""Every column is a two-compartment transfer or a block-boundary export. The six internal columns — gross regeneration, density-dependent return, uptake, detritus return, \\(e_{GA}\\) and \\(e_{AG}\\) — have column sums \\(0\\); the two exports, harvest and mining, carry column sums \\(-1\\) each:

\\[
\\mathbf{1}^{\\top}S_{\\text{block}}=\\begin{pmatrix}0&0&-1&0&0&0&0&-1\\end{pmatrix}.
\\]

Summing the rows therefore reads off the mass identity directly; under the specialization \\(C_A=0\\) mining is inactive and only the harvest term survives:""")
# ---- new §2.4 -------------------------------------------------------------------
rep("\n---\n\n## 3. Certification Layers", """
### 2.4 Support saturation: the logistic equation as a readout

**Theorem 1 (Support-saturated logistic stock limit).** Fix \\(T<\\infty\\) and non-negative \\(\\mu,\\delta,c,q\\). Assume (H1) \\(A_\\kappa\\) is measurable with \\(A_\\kappa(t)\\ge a_0>0\\) and \\(0\\le X_\\kappa(t)\\le X_{\\max}\\), and (H2) \\(E\\in L^\\infty([0,T])\\). Let \\(X_\\kappa\\) solve
\\[
\\dot X_\\kappa=\\mu X_\\kappa\\frac{A_\\kappa}{\\kappa+A_\\kappa}-\\delta X_\\kappa-cX_\\kappa^2-qE(t)X_\\kappa
\\]
and let \\(X_0\\) solve the limiting equation with the same initial value. Then \\(\\sup_{0\\le t\\le T}\\lvert X_\\kappa(t)-X_0(t)\\rvert=O(\\kappa)\\). If \\(\\mu>\\delta\\) and \\(c>0\\) the limit is the logistic stock equation with extraction,
\\[
\\dot X_0=rX_0\\left(1-\\frac{X_0}{K_{\\log}}\\right)-qEX_0,\\qquad r=\\mu-\\delta,\\quad K_{\\log}=\\frac{\\mu-\\delta}{c}.
\\]
*Proof.* With \\(e(t)=\\lvert X_\\kappa(t)-X_0(t)\\rvert\\), the saturation defect is \\(\\bigl\\lvert\\tfrac{A_\\kappa}{\\kappa+A_\\kappa}-1\\bigr\\rvert=\\tfrac{\\kappa}{\\kappa+A_\\kappa}\\le\\tfrac{\\kappa}{a_0}\\), so \\(\\lvert\\dot X_\\kappa-\\dot X_0\\rvert\\le L_1\\kappa+L_2e(t)\\) with \\(L_1=\\mu X_{\\max}/a_0\\) and \\(L_2=\\mu+\\delta+2cX_{\\max}+q\\lVert E\\rVert_\\infty\\), using \\(\\lvert\\mu-\\delta\\rvert\\le\\mu+\\delta\\) and \\(c(X_\\kappa+X_0)\\le2cX_{\\max}\\); Gronwall's inequality gives \\(e(t)\\le(L_1/L_2)\\kappa(e^{L_2t}-1)\\le C_T\\kappa\\). The bound \\(X_\\kappa\\le X_{\\max}\\) is satisfiable in the registered family, since \\(\\dot X_\\kappa\\le X_\\kappa(\\mu-\\delta-cX_\\kappa)\\) keeps \\(X_\\kappa\\le\\max\\{X(0),(\\mu-\\delta)/c\\}\\). \\(\\square\\)

**Remark 2 (Registered-family identity).** In the primitive-flux core with \\(g=\\mu XA/(K_A+A)\\), \\(m=dX+cX^2\\) and \\(h=qEX\\), the saturated stock equation is, for each fixed interior \\(A>0\\) as \\(K_A\\to0\\),
\\[
\\dot X=(\\mu-d)X-cX^2-qEX=rX(1-X/K)-qEX,\\qquad r=\\mu-d,\\quad K=(\\mu-d)/c,
\\]
requiring \\(\\mu>d\\) and \\(c>0\\). The identity is pointwise on the interior support region and is not uniform through the depleted-pool boundary, since \\(A/(K_A+A)=0\\) at \\(A=0\\) for every \\(K_A>0\\).

The scope of the limit is part of the statement: it does not eliminate \\(U\\), it does not make \\(A\\) constant near its boundary, and it does not transform the memory or effort laws. It is an ecological stock-equation identity, not a full-system reduction and not a transfer principle for bifurcation thresholds; bifurcation numbers of the two families do not transfer. A logistic stock equation is therefore a saturated support-pool readout rather than a primitive physical law, and substituting it for stock-support dynamics is legitimate only at interior saturation and only on timescales where the approximation holds.

---

## 3. Certification Layers""")
# ---- Section 3 ------------------------------------------------------------------
rep("The logical relations are the content of the next two propositions.",
"""The logical relations are the content of the next two propositions.

**Numbering convention.** The two layering propositions of this section carry their own counter, Propositions 1 and 2; every other numbered statement runs on a single sequence — Definitions 1–6, Theorems 1–15, the remaining propositions, the remarks and the corollary — so Proposition 4, Proposition 6, Proposition 17, Proposition 18 and Proposition 20 are main-counter statements rather than further members of the layering counter, and all labels are unique. Four results are stated without a number (*Depletion is compartmental*, *No weighted certification*, *Universal failure of weighted certification*, *Non-reduction*) because they are recorded as boundary statements rather than as entries in the sequence.""")
rep("The bounds are conservative. They hold for all flux selections in the declared boxes, including selections not jointly realizable by the coupled dynamics.",
"""Two qualifications are part of the theorem. The bounds are conservative: they hold for all flux selections in the declared boxes, including selections not jointly realizable by the coupled dynamics, so the certificate may fail where a trajectory with jointly realizable fluxes would pass, and attainability requires solving or bounding the coupled system. And when \\(v=v(x)\\) is state-dependent, the declared box must additionally be forward-invariant under the coupled dynamics for the envelopes to bound the reachable set; without it the corollary certifies flux-admissible paths only, not the trajectories of the differential equation. The envelope is an interval computation on the flux data, not a forecast: it says nothing about what the fluxes will be, only what every admissible path implies for the stock. Row indices in the display are rows of the matrices \\((CS_T)^+\\), \\((CS_T)^-\\), \\(C^+\\) and \\(C^-\\).

Stoichiometric and donor-limit constraints make the jointly admissible selections a polytope rather than a box; the tight certificate is the linear programme over that polytope, and the box envelope above is its auditing relaxation — the box is what is audited, the polytope what is realizable.

**Worked envelope on the closed block.** On (2a)–(2d) with declared boxes \\(N\\in[0,K]\\) and \\(E\\in[0,E_{\\max}]\\), the mass row gives
\\[
\\dot M=-qEN-C_{A,\\lim}\\in\\bigl[-(qE_{\\max}K+C_A),\\,0\\bigr],\\qquad
M(t)\\in\\bigl[M(0)-(qE_{\\max}K+C_A)t,\\;M(0)\\bigr].
\\]
The conservatism is visible in the extremes: maximal extraction \\(qE_{\\max}K\\) is realizable only at \\(N=K\\), where regeneration vanishes, and maximal recharge coincides with minimal extraction — box extremes the coupled dynamics cannot realize jointly.""")
rep("**Proposition 6.** Assume \\(S\\) is absolutely continuous,",
"""**Proposition 6.** In this proposition \\(S\\) is a scalar readout of the declared moiety, with \\(C\\) the identity composition on that moiety, and \\(\\underline B\\) is a constant lower barrier. Assume \\(S\\) is absolutely continuous,""")
rep("The uniform-margin assumption is essential.",
"""The uniform-margin assumption is essential, and the barrier is a positive one: the statement is about crossing \\(\\underline B>0\\), and the counterexample below shows that no such conclusion is available at \\(\\underline B=0\\).""")
# ---- Section 4 ------------------------------------------------------------------
rep("Conservation is structural. It is read from the columns of the incidence matrix.",
"""Conservation is structural. It is read from the columns of the incidence matrix, and it is exact under the routing constraints on a state vector that includes the product, waste and inert compartments: harvest and mining are internal transfers of the full ledger and exports of the natural block, which is why Theorem 7 records a nonzero right-hand side while this theorem records zero.""")
rep("### 4.3 Orthant invariance",
"""### 4.3 Six-compartment conservation

For one conserved limiting material the scaffold can be instantiated as six compartments \\((X,U,A,G,P,W)\\) — living stock, detritus, active abiotic pool, geological pool, product and waste — with eight non-negative primitives: assimilation \\(g\\) from \\(A\\) to \\(X\\), mortality \\(m\\) from \\(X\\) to \\(U\\), harvest \\(h\\) from \\(X\\) to \\(P\\), decomposition \\(d_U\\) from \\(U\\) to \\(A\\), the two-way geological exchange \\(e_{GA}\\) and \\(e_{AG}\\) between \\(G\\) and \\(A\\), direct mining \\(c_G\\) from \\(G\\) to \\(P\\), and product retirement \\(r_P\\) from \\(P\\) to \\(W\\), split by a declared fraction \\(\\rho_P\\). The constant splits \\(\\alpha,\\rho_P\\), the compartment set and the absorbing-sink convention are declared choices of the example, and the construction is a monomaterial projection: recovery claims require \\(U\\) and \\(P\\) split by material, location and grade with declared yields and residual routes.

**Theorem 9.** *For the six-compartment system, \\(\\mathbf{1}^{\\top}\\dot z=0\\): the total material mass \\(M_6=X+U+A+G+P+W\\) is constant along every trajectory on which the classical solution is defined.* *Proof.* Each primitive is a two-compartment transfer, so every column of the incidence matrix carries one \\(+1\\) and one \\(-1\\) and \\(\\mathbf{1}^{\\top}S(\\alpha,\\rho_P)v=0\\) column by column: \\(g-g=0\\), \\(-m+m=0\\), \\(-d_U+d_U=0\\), \\(e_{GA}-e_{GA}=0\\), \\(-e_{AG}+e_{AG}=0\\), \\(-c_G+c_G=0\\), \\(-h+\\alpha h+(1-\\alpha)h=0\\), and \\(\\rho_Pr_P-r_P+(1-\\rho_P)r_P=0\\). The argument applies to the expanded typed incidence system when quality grades are split, and not automatically to an undifferentiated quality-neutral loop. Open systems are explicit: imports, exports, atmospheric losses and cross-boundary transport enter as typed boundary fluxes giving \\(\\dot M_6=I_\\partial-O_\\partial\\), which is preferable to preserving a nominal invariant by allowing an unobserved or finite donor compartment to become negative. \\(\\square\\)

The four-block system (2a)–(2d) is not a specialization of this scaffold: in the scaffold assimilation \\(g\\) is a slow \\(A\\to X\\) flux and mortality \\(m\\) a slow \\(X\\to U\\) flux, while in (2a)–(2d) the uptake \\(T\\) transfers \\(A_{\\text{act}}\\to U\\) with the living stock catalytic and no separate mortality primitive. The two are different timescale lumpings of the same physical story, and no incidence specialization maps one onto the other. Theorems 7–9 are three instances of Proposition 1 with \\(\\ell=\\mathbf{1}\\), differentiated only by which compartments the declaration includes.

### 4.4 Orthant invariance""")
rep("### 4.4 No interior rest at positive effort",
"""**Theorem 11 (Orthant invariance of the general closed block).** *For the general closed block in which every primitive outflow of a compartment vanishes when that compartment is empty — including a two-way exchange \\(e_i=k_i\\Pi_i\\Pi_{1i}x_i\\) and a donor-scaled \\(e_{GA}\\) — the non-negative orthant is forward invariant. A target-relaxation law \\(e_{GA}=\\omega(A_{\\mathrm{eq}}-A)\\) does not satisfy the donor boundary assumption unless it is also limited by the donor stock; it may be used only with the source declared an effectively infinite external reservoir, in which case the system is open rather than closed.* *Proof.* On the face \\(x_1=0\\) every primitive out of \\(x_1\\) vanishes, so \\(\\dot x_1=\\sum_i k_i\\Pi_i\\Pi_{1i}x_i+\\omega_A A_{\\mathrm{eq,intrinsic}}\\sigma\\ge0\\). On the face \\(x_2=0\\) with a single non-empty donor, the exchange inflow is donor-scaled and \\(\\dot x_2\\ge0\\), vanishing only if the declared exchange fraction is zero, which is a decoupled transfer. In both cases this is the inward-pointing (Nagumo) condition on each face; a target-relaxation law violates it because it changes sign at an empty donor, the inadmissible case recorded in the recharge-law table of Section 2.3. The classical lineage is the compartmental-systems non-negativity theory, including donor-limited Michaelis–Menten uptake and outflow vanishing at the donor (Jacquez and Simon, 1993); the donor-limitation condition is the exact sufficiency requirement, and algebraic cancellation alone does not establish invariance. \\(\\square\\)

### 4.5 No interior rest at positive effort""")
rep("**Theorem 12.** Assume \\(E \\equiv E^* > 0\\) is constant.",
"""**Theorem 12.** Assume \\(E \\equiv E^* > 0\\) is constant. Rest points are sought in the closed orthant with \\(N^*>0\\), so the boundary branches must be excluded by the flow rather than by interiority.""")
rep("**Theorem 13.** With \\(E \\equiv 0\\), the rest points of the closed natural block are exactly three sets:",
"""**Theorem 13.** With \\(E \\equiv 0\\), the rest points of the closed natural block are exactly""")
rep("3. the frozen-biomass face \\(\\mathcal{R}_{\\text{frozen}}\\).\n\nThey are:",
"""\\(\\mathcal{R}_{\\text{ext}}\\cup\\mathcal{R}_K\\), together with the frozen-biomass face \\(\\mathcal{R}_{\\text{frozen}}\\). The families are not disjoint: the origin lies in \\(\\mathcal{R}_{\\text{ext}}\\) and in \\(\\mathcal{R}_{\\text{frozen}}\\), and \\((K,0,0,0)\\) lies in \\(\\mathcal{R}_K\\) at \\(A_{\\text{geo}}=0\\) and in the frozen face. They are:""")
rep("\\mathcal{R}_K\n=\n\\{N=K,\\; U = \\kappa_A K s/\\gamma_U,\\; A_{\\text{act}} = A_{\\text{eq,intrinsic}}\\sigma(A_{\\text{geo}})\\},",
"""\\mathcal{R}_K\n=\n\\{N=K,\\; U = \\kappa_A K s/\\gamma_U,\\; A_{\\text{act}} = A_{\\text{eq,intrinsic}}\\sigma(A_{\\text{geo}}),\\; A_{\\text{geo}}\\ge0\\},
\\qquad(\\text{$s$ evaluated at the solution}),""")
rep("The three families are exactly the stated rest set. \\(\\square\\)",
"""Apart from the frozen-biomass face, no rest point exists away from extinction or carrying capacity. If \\(A_{g0}=0\\) and \\(\\sigma\\equiv1\\) are imposed for \\(A_{\\text{geo}}>0\\), the shared active-pool ray of both families is \\(A_{\\text{act}}=A_{\\text{eq,intrinsic}}\\) with \\(A_{\\text{geo}}>0\\), and the endpoint \\(A_{\\text{geo}}=0\\) is excluded because there the donor-limited recharge vanishes and \\(\\dot A_{\\text{act}}=-\\omega_AA_{\\text{eq,intrinsic}}<0\\). The constitutive laws of this section carry no basal mortality independent of the support factor; adding one, a stock-to-detritus flux \\(\\mu_{\\mathrm{basal}}N\\), collapses the frozen-biomass face and leaves Theorems 7–12 and 14 unchanged. With \\(E>0\\) constant the extinction family persists as a boundary rest, since \\(qEN\\) vanishes identically at \\(N=0\\), while no interior rest exists by Theorem 12; the institutional memory can therefore yield \\(E\\to E^*\\) at \\(N=0\\) with extraction vanishing identically. \\(\\square\\)""")
rep("**Theorem 14.** Assume \\(E(s) \\ge 0\\) along the trajectory. Let",
"""**Theorem 14.** Assume \\(E(s) \\ge 0\\) along the trajectory, where \\(s\\) is a dummy integration variable and not the support factor of Section 2.3. Let""")
rep("This is the depletion-horizon semantics of the closed ledger in its strongest form. The donor budget is finite, and extraction is integrable against it.",
"""This is the depletion-horizon semantics of the closed ledger in its strongest form: the donor budget is finite and extraction is integrable against it. In particular no trajectory maintains extraction at the working value \\(qE^*N^*\\approx0.187\\) for all time (Section 10.2), and with mining restored the same argument bounds \\(\\int_0^\\infty(qEN+C_{A,\\lim})\\,ds\\) by \\(M(0)\\). A constant extraction flux \\(c>0\\) — a comparison flux only, not a donor-limited primitive the ledger's discipline admits as a sustained law — exhausts the budget in finite time, with \\(M\\) reaching its lower bound no later than \\(M(0)/c\\), whereas proportional extraction \\(qEN\\) need not drive \\(M\\) to zero in finite time: the integral bound is the whole statement, and the hitting time of \\(M=0\\) may be infinite. The theorem does not select among the vanishing-extraction rests of Theorem 13; the \\(L^1\\) bound alone decides nothing between them. This finite-budget fact is the long-time obstruction recorded in Section 10.2.""")
rep("\n---\n\n## 5. Service Readouts and the Componentwise Deficit", """
### 4.6 The conditional hybrid moiety balance, and the limit of cancellation

**Theorem 15 (Conditional hybrid moiety balance).** Let \\(\\chi\\) denote the hybrid state and \\(\\eta\\ge0\\) its primitive fluxes, letters chosen so that \\(r\\) retains the growth-rate meaning of Section 2.3 and \\(\\nu\\) remains a macroeconomic parameter of the unreduced ledger. Assume (H1) \\(\\chi\\) is absolutely continuous between locally finite event times, with left and right limits at each event; (H2) \\(\\dot\\chi=S\\eta+b\\) with \\(\\eta\\ge0\\), separate reverse columns for two-way exchange, and donor-limited negative boundary flows; and (H3) \\(L^{\\top}S=0\\). Then
\\[
L^{\\top}\\chi(t)-L^{\\top}\\chi(0)=\\int_0^tL^{\\top}b\\,ds+\\sum_{t_k\\le t}L^{\\top}\\bigl[\\chi(t_k^+)-\\chi(t_k^-)\\bigr].
\\]
*Proof.* Integrate between events and telescope the jumps. \\(\\square\\)

The theorem is conditional, and its jump interpretation is part of the content: an internal-transformation jump requires \\(L^{\\top}(\\chi^+-\\chi^-)=0\\) or a jump incidence factorization with left-kernel conservation, while a boundary-crossing jump is a boundary impulse and belongs in the boundary term. Two obligations ride the statement. The yield-routing obligation: a transformation represented with yield below one must route the omitted fraction to a represented compartment or a declared boundary flow, or the balance holds only after silently dropping that moiety from \\(L\\). The separation obligation: this is the hybrid variant of Proposition 4, retained at its own conditional status, and the two statements are not merged.

**Cancellation is cheap.** Summing the six material equations of the ten-state admissibility template of the supplementary material gives the exact identity \\(\\tfrac{d}{dt}(\\bar X_A+X_J+P+U+A+G)=0\\). This is an algebraic cancellation only: it does not prove forward invariance of the six material states or physical admissibility of every term. The ghost-sink check is part of the discipline — the birth-transfer rate \\(gB\\) enters \\(\\dot X_J\\) and \\(\\dot A\\) with opposite signs, so material not transferred to juveniles remains in \\(A\\) and no unmodelled sink absorbs it — and the check passes while the same template fails elsewhere, because its geological exchange is not donor-limited. Conservation (Theorems 7–9) and positivity (Theorems 10–11) are proved separately in every well-posed ledger of this article, exactly because cancellation is cheap and admissibility is not. The template's remaining negative witnesses — a variance closure not realizable by a non-negative spatial distribution, and an output functional without a displayed state equation — are recorded in the supplementary material as audited admissibility failures.

**The closed-ledger portrait.** Theorems 7–14 assemble into a complete qualitative portrait of the closed orthant: conservation (Theorems 7–9), positivity (Theorems 10–11), no interior rest at positive effort (Theorem 12), the two-family vanishing-extraction rest set with the frozen-biomass face (Theorem 13), and the finite donor budget (Theorem 14). The portrait is the source object handed to the interface of Section 10: the closed system's candidate long-time set is the rest set of Theorem 13, and the budget of Theorem 14 bounds how long any positive-flux configuration can persist. A "balanced" closed ledger is thus a finite-budget object, and any sustained extraction against it must integrate to a quantity no greater than the initial budget.

---

## 5. Service Readouts and the Componentwise Deficit""")
# ---- Section 5 / 6 --------------------------------------------------------------
rep("\n---\n\n## 6. Depletion Arithmetic", """**Remark 16 (Exact specialization deficit identity).** On every trajectory of the specialized system (\\(\\mu=\\nu=\\rho=0\\), \\(C_A=0\\)), and of every reduced system whose stock equation is \\(\\dot N=R-qEN\\),
\\[
\\Lambda(t):=\\bigl[qE(t)N(t)-R(N(t),A_{\\text{act}}(t))\\bigr]_+=\\bigl[-\\dot N(t)\\bigr]_+.
\\]
*Proof.* The stock equation gives \\(qEN-R=-\\dot N\\) identically; taking the positive part of both sides proves the claim. \\(\\square\\)

The identity does not hold on the general ledger, where the deficit is the diagnostic \\(C(t)-\\hat M^{\\top}S(t)\\) and need not equal \\(-\\dot N\\): the collapse of the deficit to the stock-decline rate is a property of the specialization, not a definition of liquidation. In the registered delay family the depletion-pressure input \\(\\Lambda=\\max\\{0,qEN-R\\}\\) is therefore a smoothed stock-decline rate and not a scarcity signal: it vanishes at the saturated rest \\(R=qEN\\) with \\(N>0\\), and it vanishes at the extinction face because the extraction flux vanishes there.

---

## 6. Depletion Arithmetic""")
rep("\n---\n\n## 7. Noncompensation and Double Counting", """
### 6.4 Robust semantics

For uncertain parameters \\(\\theta\\in\\Theta\\) and admissible disturbances \\(d\\in\\mathcal D\\), robust barrier safety is
\\[
\\underline B_m(t)\\le S_m(t;\\theta,d)\\le\\overline B_m(t)\\qquad\\forall m,\\ \\forall t,\\ \\forall\\theta\\in\\Theta,\\ \\forall d\\in\\mathcal D,
\\]
and the depletion-horizon classification is fourfold: nominal (\\(\\theta=\\theta_0\\), \\(d=0\\)); worst-case (\\(\\inf_{\\theta,d}\\tau_{\\mathrm{exit}}(\\theta,d)\\)); probabilistic (\\(\\Pr[\\tau_{\\mathrm{exit}}>T]\\ge1-\\varepsilon\\)); and scenario-conditioned (\\(\\tau_{\\mathrm{exit}}\\mid\\theta=\\theta_s\\)). The componentwise diagnostic applies to each scenario, and the conjunctive criterion applies within each scenario and across scenarios. No single number is promoted across the four classes without a declared map. In the probabilistic class \\(\\tau_{\\mathrm{exit}}\\) is the minimum over moieties and over both barrier signs, so \\(\\Pr[\\tau_{\\mathrm{exit}}>T]\\) is the probability that every component remains inside its barriers simultaneously — a joint pathwise event, not a collection of per-component reliabilities.

---

## 7. Noncompensation and Double Counting""")
# ---- Section 7.2 scoped renumbering of the component index ----------------------
a = t.index("### 7.2 Universal failure of weighted certification"); b = t.index("### 7.3 The double-counting discipline")
seg = t[a:b]
seg = seg.replace("for some component \\(m\\)", "for some component index \\(i\\)")
for k in "bxdw":
    seg = seg.replace(f"{k}_m", f"{k}_i")
seg = seg.replace("If some \\(m \\ne j\\)", "If some index \\(i\\ne j\\)").replace("for every \\(m \\ne j\\)", "for every \\(i\\ne j\\}").replace("for every \\(m \\ne j\\)", "for every \\(i\\ne j\\)").replace("Choose any \\(m \\ne j\\)", "Choose any \\(i\\ne j\\)")
seg = seg.replace("Every nonnegative state is admissible under the declared flux, because donor limitation holds: \\(f=0\\) at \\(x_1=0\\).",
 "The witness is exhibited on two components; in a ledger with \\(m>2\\) components the remaining coordinates are placed at their demands, which contributes nothing to the aggregate and cannot restore a certificate. Every nonnegative state is admissible under the declared flux, because donor limitation holds: \\(f=0\\) at \\(x_1=0\\).")
seg = seg.replace("The pair \\((x,d)\\) is the witness for \\(w\\).", "The pair \\((x,d)\\) is the witness for \\(w\\), in every dimension \\(m\\ge2\\).")
seg = seg.replace("The construction does not use the dynamics. The failure is a property of nonnegative weightings over mixed-sign balances.",
 "The construction does not use the dynamics: the failure is a property of non-negative weightings over mixed-sign balances, not of the donor-limited positivity mechanism. The conditional form of Section 7.1 is therefore not an accident of a particular domain — the compensating pattern is constructible against any weight, so the failure is universal to the method of weighted certification — while a non-compensatory test is equivalent to componentwise adequacy: the conjunctive criterion of Section 3.2, or the min-margin functional \\(\\min_m(S_m-\\underline B_m)\\) reported together with the name of the binding component.")
t = t[:a] + seg + t[b:]; ok += 1

open(OUT, 'w', encoding='utf-8').write(t)
print(f"applied {ok} edits; {len(bad)} skipped")
for m in bad: print("  SKIPPED", m)
print("chars:", len(t))

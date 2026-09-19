#!/usr/bin/env python3
"""v33 revisions to the repository's `paper3_material_ledgers_v32.md` — the surviving points of the
nine audits, re-anchored onto the markdown of record from which wave13 builds the LaTeX.

Convention follows the repository: this file is the revision script, the previous version is never
modified, and every operation is logged so that removal of the logged blocks reproduces v32
byte-for-byte (see verify_v33.py).  Sources of the items: `review/deployment_plan_v1.md` register
rows 1-15, whose verdicts trace to `review/five_audits_joint_verified_v1.md` (batch 2) and
`review/ledger_audits_verified_v1.md` (batch 1).  Each statement below was re-derived; none is
copied from an audit's wording.  Cross-references are to *this* manuscript's section numbers, which
differ from those of the parallel markdown revision (see README_v33.md).

Run from the repository root:  python3 revisions_v33.py
"""
import json
import os
import re
import sys

SRC = os.environ.get("SRC", "github/gs/arena agent 1/paper rewrites/paper3_material_ledgers_v32.md")
DST = os.environ.get("DST", "revision/v6/paper3_material_ledgers_v33.md")
LOG = os.environ.get("LOG", "revision/v6/revisions_v33_log.json")

t = open(SRC, encoding="utf-8").read()
applied, skipped, log = [], [], []


def _rep(old, new, tag, optional=False):
    global t
    n = t.count(old)
    if n != 1:
        skipped.append("%s: target count %d :: %r" % (tag, n, old[:60]))
        return False
    t = t.replace(old, new, 1)
    applied.append(tag)
    log.append({"kind": "rep", "tag": tag, "old": old, "text": new})
    return True


def _md(text):
    r"""Re-type the parallel revision's LaTeX dialect into this markdown's dialect:
    single-line $$...$$ displays, $...$ inline math, \mathcal{T} subscripts, unicode QED."""
    text = re.sub(r"\\\\[ \t]*\n", "\n", text)                       # drop LaTeX line breaks
    text = re.sub(r"\\\[\s*(.*?)\s*\\\]",
                  lambda m: "$$" + re.sub(r"\s+", " ", m.group(1)) + "$$", text, flags=re.S)
    text = re.sub(r"\\\((.*?)\\\)", lambda m: "$" + m.group(1) + "$", text, flags=re.S)
    text = re.sub(r"\bS_T\b", lambda _m: r"S_{\mathcal{T}}", text)
    text = re.sub(r"\bB_T\b", lambda _m: r"B_{\mathcal{T}}", text)
    text = text.replace(r"$\square$", "\u25a1")
    return text


HEAD = re.compile(r"^(#{2,4}) (\d[\d.]*)[ \t]+(.*\S)[ \t]*$", re.M)


def after_subsection(frag, text, tag):
    """Append a paragraph at the end of the subsection whose heading contains `frag`."""
    global t
    hs = list(HEAD.finditer(t))
    hits = [m for m in hs if frag in m.group(0)]
    if len(hits) != 1:
        skipped.append("%s: heading frag %r matched %d" % (tag, frag, len(hits)))
        return
    h = hits[0]
    level = len(h.group(1))
    nxt = [m for m in hs if m.start() > h.start() and len(m.group(1)) <= level]
    end = nxt[0].start() if nxt else len(t)
    text = _md(text)
    msep = re.search(r"\n+---\s*\n+\s*$", t[h.end():end])
    ins_at = h.end() + msep.start() if msep else h.end() + len(t[h.end():end].rstrip())
    ins = "\n\n" + text.strip("\n") + "\n"
    t = t[:ins_at] + ins + t[ins_at:]
    applied.append(tag)
    log.append({"kind": "after_sub", "tag": tag, "frag": frag, "text": ins,
                "anchor_head": h.group(0).strip()})


# ============================================================ Section 1.2 — antecedents
after_subsection("1.2 Contributions", r"""
**Antecedents.** The bookkeeping idiom and its reconciliation practice are those of material flow
analysis (Section 1.1; Brunner and Rechberger, 2004), and the incidence apparatus is that of
compartmental systems and reaction-network theory (Jacquez and Simon, 1993; Feinberg, 2019). The
regime distinction the ledger formalises is the contested distinction of the weak-versus-strong
sustainability and critical-natural-capital literatures (Ekins et al., 2003; Neumayer, 2013), and
the aggregate-versus-component question is the non-compensatory-aggregation question posed for
composite indicators (Munda and Nardo, 2009), where the footprint accounts that animate part of that
debate are themselves under assessment (Wackernagel and Beyers, 2019; Lin et al., 2018; Blomqvist
et al., 2013). The terminal-condition tradition is viability theory (Aubin, 1991); the horizon
arithmetic sits on a bioeconomic and extractive-price literature (Clark, 1990; Tilton, 2003; Tilton
and Lagos, 2007), as do the growth-limit arguments with which depletion horizons are confused
(Meadows et al., 1972; Daly, 1990). The statistical standards are closer than that genealogy
suggests: the System of National Accounts 2025 treats the depletion of natural resources as a cost
of production alongside depreciation, following the treatment developed under the SEEA Central
Framework (United Nations, 2014; United Nations, 2025), which leaves the classification of depletion
settled and the identification of a horizon open. None of these sources is used as a premise here.
The objects proved about are the ledger's own.
""", "1.2 Antecedents paragraph")

# ============================================================ Section 2.1 — closure cone, deficit, residual note
after_subsection("2.1 Typed stocks", r"""
**Definition 21 (Closure cone).** The regimes above can be stated on the ledger's own objects rather
than as attitudes toward them. Let \(S_T\) be the incidence operator declared here, let \(v\ge0\)
be the primitive fluxes under declared capacities \(\bar v\), let \(B_Tu_\partial\) collect the
declared boundary transfers, and let \(P\) project a flux vector onto its use columns. Write
\(\mathcal K=\{v\ge0:\ S_Tv+B_Tu_\partial=0,\ v\le\bar v\}\) for the admissible stationary flux
patterns. A demanded use vector \(D\) closes at the rate of use if and only if
\(D\in P(\mathcal K)\). The closure capacity
\(\lambda^{*}=\max\{\lambda:\ \lambda D\in P(\mathcal K)\}\) is a linear programme on the declared
capacities, and its feasibility is the cut condition on return capacity (Gale, 1957; Ahuja et al.,
1993). Where \(\lambda^{*}\ge1\), the cycle closes at the demanded rate. Where \(\lambda^{*}<1\),
every trajectory meeting \(D\) has a non-stationary stock, and by conservation the shortfall appears
as support drawdown together with sink accumulation; the deficit share is not a free parameter. Yield
inflation is the same statement read outside the projection: demand met with no stationary pattern
behind it.

Left-null vectors express conservation; right-null vectors express circulation. The regimes of
Section 1.1 are statements about the second set, and the depletion readouts of Section 6 are
statements about the first; neither set's membership follows from the other's.

**Definition 22 (Closure deficit at the use timescale).** For each moiety \(m\), let
\(\kappa_m(\tau;\Theta)\in[0,1]\) be the fraction of mobilised flux returned to a usable compartment
within lag \(\tau\) under the declared technology and process graph \(\Theta\), and let
\(\delta_m=1-\kappa_m(\tau_{\mathrm{use}};\Theta)\) be the closure deficit at the declared use
timescale. The deficit is a property of a declared graph at a declared timescale, not a rate of the
material itself. Where a mobilisation \(g_m\) is sustained with \(\delta_m\ge\underline\delta>0\),
the net drawdown of the support pool is \(\delta_mg_m\), so
\[
\int_0^T(\text{liquidation})\,dt\ \ge\ \underline\delta\int_0^Tg_m\,dt,
\qquad
T\ \le\ \frac{m_0}{\underline\delta\,g_m},
\]
the second inequality being the frozen-rate horizon read on the liquidation flux rather than on gross
use. Both bounds are one-sided by construction, and neither reverses in the limit
\(\delta_m\to0^+\). A positive deficit is not a barrier-reachability claim: a deficit that decays
with the stock need never reach a barrier, and where the binding constraint is an upper barrier the
relevant object is the complementary headroom.

Two readings follow from the definition. An indicator that reports a return fraction with no lag
argument reports \(\kappa_m(\infty)\) where \(\kappa_m(\tau_{\mathrm{use}})\) is being read; the
recycled-input and circularity-rate families are of that form, since a ratio of fluxes carries no
timescale. And "a material is waste" is, on this reading, the statement
\(\kappa_m(\tau_{\mathrm{use}};\Theta)<1\) for the declared graph, so unlocking a stream is an
increase of \(\kappa\) at fixed \(\tau\): measurable, and not in need of a new substance category.
""", "2.1 Definitions 21-22 closure cone and deficit")

# ============================================================ Section 3.1 — certification state
after_subsection("3.1 Three predicates", r"""
**Certification state.** The obligations developed in this section are reported as a vector
\[
\mathrm{Cert}=(\mathsf{Typed},\ \mathsf{Balanced},\ \mathsf{Conserved},\ \mathsf{Positive},\
\mathsf{Admissible},\ \mathsf{Safe},\ \mathsf{Adequate\ service},\ \mathsf{Closed}),
\]
each entry taking one of three values: established, not established, and not applicable to this
object. The third value is not a failure and the second is not a refutation. A classification record
that establishes an accounting identity and nothing else reports \(\mathsf{Safe}\) as not applicable,
not as refuted; a record that establishes every entry except closure is not thereby unsafe. The
predicates are separately certified and generally non-equivalent rather than pairwise independent:
the implications that hold among them are the ones stated in Propositions 1 and 2 and in the
thermodynamic clause of Section 3.2, and an unlisted implication is not available by inference. The
proof obligation attached to each entry, and the certificate vectors of the indicators classified in
Section 6.5, are tabulated in the supplementary material.
""", "3.1 certification state")

# ============================================================ Section 3.4 — bounded residual
after_subsection("3.4 The conservation-law reduction", r"""
**Definition 23 (Bounded residual).** Conservation consistency is stated with a declared residual
budget. For every left-null vector \(\ell\) of \(S_T\), with \(C\) the readout matrix of Section 2.1,
\[
\Bigl|\int_0^T\ell^{\top}C\,d_x(t)\,dt\Bigr|\ \le\ \epsilon_\ell(T),
\qquad \epsilon_\ell\ \text{declared with the model}.
\]
Proposition 1 then reads \(\ell^{\top}Cx(T)=\ell^{\top}Cx(0)+\int_0^T\ell^{\top}C\,b(t)\,dt\) with
the disturbance term carried rather than absorbed, and \(\epsilon_\ell\) is the quantity
material-flow reconciliation books as statistical discrepancy. An envelope computed without
\(\epsilon_\ell\) supports no barrier certificate once the residual-inflated envelope leaves the
declared barriers, and where \(\epsilon_\ell\) is undeclared the conservation predicate is reported
as not established rather than assumed at zero. Where no budget is declared for \(d_x\), the
residual is not established at zero and is not bounded: the predicate carries the gap rather than
closing it.
""", "3.4 Definition 23 bounded residual")

# ============================================================ Section 3.6 — critical-margin budget
after_subsection("3.6 Finite exhaustion", r"""
**Theorem 24 (Critical-margin budget).** Let the declared barrier margins be affine,
\(m(x)=Gx+a\ge0\), and let the delivered service rate be \(y=c^{\top}v\) with \(c\ge0\). Suppose some
\(\lambda\ge0\) satisfies \(\lambda^{\top}GS_T+c^{\top}\le0\) componentwise, with \(\lambda_j\)
carrying the units that convert margin \(j\) into cumulative service. Then \(V=\lambda^{\top}m(x)\)
obeys \(\dot V\le-y+\lambda^{\top}Gb\) along every admissible trajectory, and for every trajectory
that remains inside the declared barriers
\[
\int_0^Ty(t)\,dt\ \le\ V(x(0))+\int_0^T\lambda^{\top}Gb(t)\,dt .
\]
If additionally \(y\ge y_{\mathrm{req}}\) and \(\lambda^{\top}Gb\le\beta<y_{\mathrm{req}}\), then
\(T\le V(x(0))/(y_{\mathrm{req}}-\beta)\).

*Proof.* \(\dot V=\lambda^{\top}G(S_Tv+b)=(\lambda^{\top}GS_T)v+\lambda^{\top}Gb\le
-c^{\top}v+\lambda^{\top}Gb\) since \(v\ge0\); integrate and use \(V(T)\ge0\), which holds because
\(m\ge0\) and \(\lambda\ge0\). \(\square\)

The search for \(\lambda\) is a linear programme, and its infeasibility is no evidence of safety: it
certifies only that this multiplier family does not close. The theorem bounds how long adequate
service can coexist with componentwise safety; it is not a scalar certificate, and \(V>0\)
establishes nothing about the sign of any individual margin. The uniform-drift bound above is its
single-margin instance, and the two-sided demand version replaces no statement of Section 5.
""", "3.6 Theorem 24 critical-margin budget")

# ============================================================ Section 5.4 — accumulated liquidation
after_subsection("5.4 The componentwise deficit", r"""
**Proposition 25 (Accumulated liquidation certified by delivered service).** Let the support pool
obey \(\dot A=r-c\), and let the declared production relation require at least \(\alpha\ge0\) units
of support use per unit of delivered service, \(c(t)\ge\alpha Y(t)\). Then
\[
A(0)-A(T)\ \ge\ \alpha\int_0^TY(t)\,dt-\int_0^Tr(t)\,dt .
\]
Where the right-hand side is positive, the delivered service certifies that much support liquidation,
whatever the interior allocation of fluxes.

*Proof.* \(A(0)-A(T)=\int_0^T(c-r)\,dt\ge\alpha\int_0^TY\,dt-\int_0^Tr\,dt\). \(\square\)

The statement is falsifiable against the record rather than self-sealing: a stock change smaller than
the certified lower bound exposes a wrong coefficient, a missing flux, or a measurement inconsistency,
and each of the three is a registered obligation, not a licence to reconcile. The coefficient
\(\alpha\) is a declared relation, not an estimate; the proposition is conditional on it and is not
computed anywhere in this article.
""", "5.4 Proposition 25 accumulated liquidation")

# ============================================================ Section 6.2 — sign law, curvature, crossover
after_subsection("6.2 Uniform-drift bounds", r"""
**Proposition 26 (Sign of the frozen-rate error).** Let \(\dot A=-\varphi(A)\) with \(\varphi>0\) on
\((A_{\min},A_0]\), and write the true horizon and the frozen-rate ratio as
\[
T=\int_{A_{\min}}^{A_0}\frac{dA}{\varphi(A)},
\qquad
H^{\mathrm{loc}}=\frac{A_0-A_{\min}}{\varphi(A_0)} .
\]
If \(\varphi\) is nondecreasing in \(A\) then \(T\ge H^{\mathrm{loc}}\), and the frozen-rate number
is conservative. If \(\varphi\) is nonincreasing in \(A\) then \(T\le H^{\mathrm{loc}}\), and it is
optimistic.

*Proof.* Nondecreasing \(\varphi\) gives \(\varphi(A)\ge\varphi(A_0)\) for \(A\le A_0\), hence
\(T\ge(A_0-A_{\min})/\varphi(A_0)\); the second case reverses the inequality. The comparison is the
standard one for one-dimensional monotone dynamics (Smith, 1995). \(\square\)

Proportional extraction is the first case, with \(T=q^{-1}\ln(A_0/A_{\min})\) against
\(H^{\mathrm{loc}}=(A_0-A_{\min})/(qA_0)\); at \(A_{\min}=0\) the two disagree by being infinite
against finite. The sign is estimable from the data the classification already requires, by
regressing the decline rate on the stock; it is declared, not computed, in Section 6.5.

**Proposition 27 (Curvature correction).** On the barrier distance \(u=A-A_{\min}\), let
\(\dot u=-\varphi(u)\) and define the dimensionless curvature number
\[
\kappa=\frac{u\,\ddot u}{\dot u^{2}}=\frac{u\,\varphi'(u)}{\varphi(u)} .
\]
For the power-law family \(\varphi(u)=cu^{p}\) one has \(\kappa=p\) identically, and for \(\kappa<1\)
\[
T=\frac{H^{\mathrm{loc}}}{1-\kappa},
\qquad
T<\infty\iff\kappa<1,
\]
while for \(\kappa\ge1\) the integral diverges at the barrier and the family reaches it only
asymptotically, so the frozen-rate ratio understates by an unbounded factor. Constant extraction is
\(\kappa=0\), where the frozen-rate ratio is exact; stock-proportional decline is \(\kappa=1\),
where the true horizon is infinite against a finite ratio; and \(\kappa=\tfrac12\) doubles the
horizon exactly, which is the smallest correction with a real effect. The correction is a one-number
statement about the bias, and it inherits its input requirement: \(\kappa\) needs \(\ddot u\), which
is a second difference of the same noisy series whose first difference the classification already
distrusts, so it is reported as declared or not at all. Where \(\varphi\) is not of the family, only
the sign statement of Proposition 26 is available.

**Proposition 28 (Reserve-life crossover).** Let reserves obey \(\dot R=-(1-\eta)P\), with
production \(P=P_0e^{gt}\), \(g>0\), and let \(\tau=R_0/P_0\) be the reserve-life ratio. Exhaustion of
the reserve class occurs at
\[
T=\frac1g\ln\Bigl(1+\frac{g\tau}{1-\eta}\Bigr),
\]
and \(T\ge\tau\) holds to first order in \(g\tau\) exactly when \(\eta\ge\tfrac12g\tau\). A
reserve-life ratio therefore bounds the reserve class from above only where reclassification keeps
pace with growth. On the article's own pinned record, \(\tau\approx309\) yr at
\(g=0.03\,\mathrm{yr}^{-1}\), the condition requires \(\eta\ge\tfrac12g\tau\approx4.6\), which
exceeds unity: reclassification would have to outpace extraction itself, and no declared reserve
convention admits that. At \(\eta=0\) the same record gives \(T=g^{-1}\ln(1+g\tau)\approx77.6\) yr
against the tabulated 309. The direction of the error is therefore fixed by the model class rather
than by the data, and the classification of Section 6.5 is strengthened, not changed: the ratio
remains an arithmetic relation whose promotion to a forecast is unavailable at every admissible
elasticity.

*Proof.* Integrate \(\dot R=-(1-\eta)P_0e^{gt}\) to \(R(T)=0\) and solve; the comparison with \(\tau\)
is the first-order expansion \(\ln(1+x)=x-x^2/2+O(x^3)\) at \(x=g\tau/(1-\eta)\). \(\square\)
""", "6.2 Propositions 26-28")

# ============================================================ Section 6.3 — joint statement note
after_subsection("6.3 Upper barriers", r"""
One consequence for reporting. The exit time is itself a minimum, over moieties and over both barrier
signs, so a statement about its joint distribution is already a componentwise statement: no product
of marginal probabilities is required, and none is admissible in its place.
""", "6.3 joint-minimal reporting note")

# ============================================================ Section 6.5 — persistence index boundedness
after_subsection("6.5 Application classifications", r"""
**Proposition 32 (Boundedness of the persistence index on the declared trend class).** Let
\(a_k=-\beta k+\varepsilon_k\) for \(k=1,\dots,n\), with \(\varepsilon_k\) independent of scale
\(\sigma\) and \(\beta>0\). Within the declared class, the record minimum lies at the end of the
record once the trend dominates the noise, so the fitted distance from the current level up to that
minimum is a noise-scale gap and the index
\[
\frac{a_n-\min_ka_k}{\text{fitted decline rate}}
\]
is \(O_{\mathbb P}(\sigma/\beta)\): bounded in probability as the record length grows, and
independent of the stock. A simulation of 400 replicates at each of \(n=10^2,10^3,10^4,10^5\) with
\(\beta=\sigma=1\) returns a mean index of 0.21, 0.25, 0.21 and 0.25 yr, and a 90th percentile of
0.81, 0.84, 0.95 and 1.00 yr, while the stock implied by the same series falls by five orders of
magnitude; the median is zero at every length, because under a downward trend the current level is
usually the record minimum. The index is therefore flat in the record length at the noise-to-trend
scale \(\sigma/\beta\), which is the sense in which it cannot be extended into a horizon; the code
and the seed are archived with the supplementary material. Lengthening or densifying an anomaly
record cannot produce a horizon, because the statistic converges to a trend-detection quantity
expressed in years. This is a property of the declared linear-trend class and of the reported
simulation, not a claim about any basin.
""", "6.5 Proposition 32 index boundedness")

# ============================================================ Section 10.1 — uniqueness, concealed deficit, alarm, non-transport
after_subsection("10.1 Compensatory aggregation", r"""
**Proposition 29 (The certifying aggregator is unique).** Let \(r\in\mathbb R^{n}\) be component
adequacies expressed in common units, and let \(\mathcal A:\mathbb R^{n}\to\mathbb R\) be monotone,
\(r\le r'\Rightarrow\mathcal A(r)\le\mathcal A(r')\), calibrated, \(\mathcal A(c\mathbf 1)=c\) for
every \(c\), and certifying, \(\mathcal A(r)\ge c\Rightarrow r\ge c\mathbf 1\) for every \(c\). Then
\(\mathcal A(r)=\min_ir_i\).

*Proof.* Certification at \(c=\mathcal A(r)\) gives \(\min_ir_i\ge\mathcal A(r)\). Since
\(r\ge(\min_ir_i)\mathbf 1\), monotonicity and calibration give \(\mathcal A(r)\ge\min_ir_i\).
\(\square\)

For any admissible aggregator the compensation premium
\[
\Pi(r)=\mathcal A(r)-\min_ir_i\ \ge\ 0
\]
measures the part of a published aggregate that was produced by cross-component trades. Calibration
cannot be dropped: the additively separable functional \(\sum_i\min(0,r_i)\) is continuous, monotone,
faithful in the sense that a nonnegative value admits no deficit, and complete in the sense that no
deficit forces a negative value; it is not the minimum and it is not calibrated. It reports the depth
of the deficits where the minimum reports their existence, and either may be published provided
neither is called the other. Nor can monotonicity be strengthened to strict monotonicity while
keeping both directions: if a continuous \(\mathcal A\) satisfied \(\mathcal A(r)\ge0\Leftrightarrow
r\ge0\), then \(\mathcal A\) would vanish on the faces of the nonnegative orthant, since it is
negative wherever some component is and nonnegative on the orthant, and continuity forces equality
at the boundary; a strictly increasing functional then cannot take one value at \((0,1)\) and another
at \((0,2)\). Certification and strict monotonicity are incompatible, which is why the minimum is not
an arbitrary convention.

**Proposition 30 (Worst concealed deficit).** Let the component balances lie in declared bounds
\(\ell\le b\le u\), and let \(z\) be a published aggregate value \(z=w^{\top}b\) with \(w\ge0\),
\(w\ne0\). The most severe deficit an aggregate of that value can conceal in component \(j\) is
\[
\delta^{*}_j(z)=\max\ \{-b_j:\ w^{\top}b=z,\ \ell\le b\le u\},
\]
a linear programme, finite whenever the bounds are, and positive whenever any admissible \(b\) has
\(b_j<0\). Together with the premium it turns the noncompensation result into a two-sided audit: the
premium measures what the aggregate bought with trades, and \(\delta^{*}_j\) measures what it can
hide. Reported on declared bounds only, it is arithmetic on a published construction; where the
bounds are not declared, the value is reported as not established.

**Proposition 31 (Aggregates do not transport event times).** Let two stocks and their sinks obey
\(\dot x_i=-kx_i\), \(\dot w_i=kx_i\) with \(k>0\), so that each pair conserves material and remains
nonnegative, and let the aggregate \(Z=x_1+x_2\) obey the exact closed dynamics \(\dot Z=-kZ\). The
initial states \((x_1,x_2)=(2,98)\) and \((50,50)\) generate the identical aggregate trajectory
\(Z(t)=100e^{-kt}\) and, at the common lower barrier \(x_i\ge1\), first hitting times \((\log2)/k\)
and \((\log50)/k\). No function of the aggregate trajectory determines the component event time.
Dynamical closure and barrier observability are therefore separate obligations: an exact reduced
model is not thereby competent about the events its components are declared to suffer.

*Proof.* Direct evaluation of each exponential at its own barrier; the two aggregate trajectories
coincide identically. \(\square\)

The asymmetry is exact and one-directional. A coarse aggregate refutes, because a violated aggregate
barrier is a violated component barrier, and it alarms, because a positive premium is a measured
quantity; it does not certify, because the concealed deficit of Proposition 30 can be made positive
at any published aggregate value the domain admits.
""", "10.1 Propositions 29-31 and the alarm clause")

# ============================================================ Section 10.2 — overshoot premium
after_subsection("10.2 The double-counting discipline", r"""
**Remark 33 (One-signed bias of an aggregate overshoot date).** Let components carry biocapacity
\(b_i\) and demand \(d_i\), and form an aggregate overshoot date from the aggregates:
\[
\tau_{\mathrm{agg}}=365\,\frac{\sum_ib_i}{\sum_id_i}=365\sum_iw_ir_i,
\qquad
w_i=\frac{d_i}{\sum_jd_j},
\qquad
r_i=\frac{b_i}{d_i}.
\]
Then \(\tau_{\mathrm{agg}}\) is a demand-weighted mean of the component ratios, so
\(\tau_{\mathrm{agg}}\ge\tau_{\min}:=365\min_ir_i\), with equality exactly where every component of
positive weight coincides. The difference
\[
\Pi_\tau=\tau_{\mathrm{agg}}-\tau_{\min}=365\sum_iw_i\bigl(r_i-r_{\min}\bigr)
\]
is the compensation premium of Section 10.1 in unit disguise: one-signed, exactly decomposable,
unbounded in the dispersion of the components, and computable from published component tables. An
aggregate overshoot date is therefore optimistic in a known direction, which is a statement about
the construction rather than about any territory, and it is the one applied claim here that requires
no recomputation of a public dataset to state. No premium figure is reported in this article, because
the component tables of the published construction are not reproduced here.
""", "10.2 Remark 33 overshoot premium")

# ============================================================ Section 7.1 and 7.6 — positioning
after_subsection("7.1 Two objects", r"""
The surrogates used here are standard objects, and the section's content is the discipline attached
to them rather than the passage-time formulae. The inverse-Gaussian law and its parameterisations are
those of the first-passage literature on Brownian motion with drift (Chhikara and Folks, 1989;
Redner, 2001); the stochastic machinery is Itô calculus in its textbook form (Øksendal, 2003). The
comparison between a surrogate mean and the deterministic margin is a monotone-dynamics statement
(Smith, 1995), and the barrier construction is the deterministic safety argument used in hybrid-systems
verification, whose stochastic extension is the nearest formal relative of the record-relative
discipline of Section 7.4 (Prajna and Jadbabaie, 2004; Prajna et al., 2007). None of these sources
supplies a calibrated input: every drift, barrier and noise scale entering Sections 7.2 to 7.6 is
declared by the analysis, and the results are statements about the declared class.
""", "7.1 surrogate lineage paragraph")

after_subsection("7.6 The constant-production phosphate", r"""
The classification addresses the status of the ratio, not the adequacy of the resource base. The
reserve-life convention and its long defence against depletion-pessimistic readings are the subject of
a separate literature (Tilton, 2003; Tilton and Lagos, 2007), whose arguments about substitution,
price-induced discovery and economic recovery are exactly the premises this article registers as
carried rather than discharged; nothing here contradicts them.
""", "7.6 Tilton positioning sentence")

# ============================================================ Section 9 — review interval
after_subsection("9. The Interface with Institutional Delay", r"""
The companion analysis supplies the one numerical fact about governance timing that this article may
use without re-deriving it: at its calibrated point, annual review under the mobilising law is
unstable, and stability returns above a review interval of about 6.5 years, with the two subcritical
Hopf crossings of the continuous-delay problem certified near 3.7 years and 150 years. The readout of
Section 6.4 inherits the consequence. A margin computed at an interval longer than the admissible
one is not conservative, because the declared object it is computed on has already changed between
reviews; the admissible interval is a property of the institutional block, is reported there, and is
not estimated here.
""", "9 review-interval sentence")

# ============================================================ companion placeholders
DOIPHR = "Abaee, 2026, doi:10.5281/zenodo.22554217"
for old, new, tag in [
    ("the companion delay-dynamics analysis (Author, D., et al., in review); the three are distinct objects",
     "the companion delay-dynamics analysis (%s); the three are distinct objects" % DOIPHR,
     "placeholder: recharge laws"),
    ("the companion delay-dynamics analysis (Author, D., et al., in review; eq. (1) and Section 2.4 of that analysis)",
     "the companion delay-dynamics analysis (%s; eq. (1) and Section 2.4 of that analysis)" % DOIPHR,
     "placeholder: memory-effort pair"),
    ("the companion review screen (Author, E., et al., in review)",
     "the companion review screen (Abaee, 2026, doi:10.5281/zenodo.22554297)",
     "placeholder: review screen"),
    ("the companion delay-dynamics analysis (Author, D., et al., in review) is fixed by an interface contract",
     "the companion delay-dynamics analysis (%s) is fixed by an interface contract" % DOIPHR,
     "placeholder: interface contract"),
    ("The companion assessment analysis (Author, F., et al., in review)",
     "The companion assessment analysis (Abaee, 2026, doi:10.5281/zenodo.22545740)",
     "placeholder: assessment separation"),
]:
    _rep(old, new, tag)

# ============================================================ references
REFS = [
    ("Aubin, J.-P., 1991.",
     "Ahuja, R.K., Magnanti, T.L., Orlin, J.B., 1993. Network Flows: Theory, Algorithms, and Applications. Prentice-Hall, Englewood Cliffs."),
    ("Blomqvist, L., Brook,",
     "Baez, J., Li, X., Libkind, S., Osgood, N.D., Patterson, E., 2023. Compositional modeling with stock and flow diagrams. In: Applied Category Theory 2022. Electronic Proceedings in Theoretical Computer Science 380, 77\u201396. https://doi.org/10.4204/EPTCS.380.5"),
    ("G\u00fcntner, A., Sharifi,",
     "Gale, D., 1957. A theorem on flows in networks. Pacific Journal of Mathematics 7, 1073\u20131082."),
    ("Redner, S., 2001.",
     "Prajna, S., Jadbabaie, A., 2004. Safety verification of hybrid systems using barrier certificates. In: Hybrid Systems: Computation and Control VII. Lecture Notes in Computer Science 2993, 477\u2013492.\n\nPrajna, S., Jadbabaie, A., Pappas, G.J., 2007. A framework for worst-case and stochastic safety verification using barrier certificates. IEEE Transactions on Automatic Control 52, 1415\u20131428."),
    ("Tapley, B.D., Bettadpur,",
     "Smith, H.L., 1995. Monotone Dynamical Systems: An Introduction to the Theory of Competitive and Cooperative Systems. Mathematical Surveys and Monographs 41. American Mathematical Society, Providence."),
]
for anchor, entry in REFS:
    _rep(anchor, entry + "\n\n" + anchor, "reference inserted before %r" % anchor[:22])

UN = ("United Nations, 2025. System of National Accounts 2025. United Nations Statistics Division, New York. Adopted by the United Nations Statistical Commission at its fifty-sixth session. https://unstats.un.org/unsd/nationalaccount/sna2025.asp\n\n"
      "United Nations, European Commission, International Monetary Fund, Organisation for Economic Co-operation and Development, World Bank, 2014. SEEA Central Framework: 2012 Technical Implementation. Statistical Papers, Series M No. 96. United Nations, New York.\n\n")
_rep("Wackernagel, M., Beyers, B., 2019.", UN + "Wackernagel, M., Beyers, B., 2019.",
     "references inserted: United Nations 2025, United Nations et al. 2014")

# ---- the numbering note of Section 3.1, extended to the new labels -----------------
_rep("runs on the single 1\u201320 sequence counter",
     "runs on the single 1\u201333 sequence counter", "numbering note: counter range")
_rep("not further members of the layering counter",
     "not further members of the layering counter; the statements added at this revision carry the consecutive labels Definitions 21\u201323, Theorem 24, Propositions 25\u201332 and Remark 33, so no label is repeated",
     "numbering note: extension at 21-33")

# ---- back matter -------------------------------------------------------------------
_rep("`paper3_supplementary_v8.md`", "`paper3_supplementary_v9.md`", "supplementary pointer: version")
_rep("the executed broad-cohort comparison (S5).",
     "the executed broad-cohort comparison (S5). At this revision it additionally carries the proof obligations attached to each entry of the certification state of Section 3.1 with the certificate vectors of the classified indicators (S7), the linear programmes of Definitions 21\u201322 and Theorem 24 with their input requirements and the reading rule for an infeasible programme (S8), and the worked exhibits of Sections 6.2, 6.5 and 10.1 with their reproduction record and the statement inventory extended to the new labels (S9).",
     "supplementary pointer: S7-S9")

CODE = ("## Code availability\n\n"
        "The scripts that generate every computed figure in this article \u2014 the persistence-index simulation of Section 6.5, the curvature and crossover arithmetic of Section 6.2, and the compensation-premium and worst-concealed-deficit linear programmes of Section 10.1 \u2014 are archived with the supplementary material, with the random seed and the library versions recorded in the archive manifest. The scripts read no data other than the public products named in the data availability statement.\n\n")
_rep("## Declaration of competing interest", CODE + "## Declaration of competing interest",
     "Code availability section")

os.makedirs(os.path.dirname(DST), exist_ok=True)
open(DST, "w", encoding="utf-8").write(t)
json.dump(log, open(LOG, "w", encoding="utf-8"), ensure_ascii=False)
print("applied %d, skipped %d, logged %d ops" % (len(applied), len(skipped), len(log)))
for a in applied:
    print("   OK   " + a)
for x in skipped:
    print("   SKIP " + x)
print("chars: %d | words: %d | lines: %d" % (len(t), len(t.split()), t.count("\n") + 1))

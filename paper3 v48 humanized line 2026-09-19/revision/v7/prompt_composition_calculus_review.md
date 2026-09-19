# Self-contained prompt: audit or extend the composition calculus for typed resource ledgers

You are reviewing Section 3.7 and Section 6.6 of a manuscript, including new definitions you may add.
No other part of the manuscript is needed; everything used below is stated here.

**Setting.** A *typed ledger* is $L=(x,v,S,B,C;\mathcal T,\mathfrak u)$: compartments $x\in\mathbb R^m$,
each carrying a material type from $\mathcal T$ and a unit from $\mathfrak u$; primitive fluxes
$v\ge0$ bounded in declared boxes; a typed incidence operator $S$; boundary matrix $B$; readouts
$y=Cv$. Dynamics $\dot x = Sv+Bu+d_x$ with a declared residual budget $|\int\ell^\top C\,d_x|\le\epsilon_\ell$
for every left-null $\ell$ of $S$ (consistency). A *barrier system* adds margins $m_i(x)=G_i x+a_i\ge0$,
and a *certificate* is any $\lambda\ge0$ with $\lambda^\top G S+c^\top\le0$; it yields
$\int_0^T y \le \lambda^\top m(x(0))+\int_0^T\lambda^\top G b$. Closure at demanded rate $D$ means
$D\in P(\{v\ge0:Sv+B u_\partial=0,\,v\le\bar v\})$, whose capacity is the LP optimum
$\lambda^*=\max\{\lambda:\lambda D\in P(\cdot)\}$.

**Claims to audit.** (i) Under an *admissible* interface (type/unit-matched identifications, joint
capacity boxes declared, exchanges antisymmetric), conserved quantities lift from the parts to the
composition. (ii) Closure capacity is not compositional: two cycles with return capacity exactly equal
to demand ($\lambda^*=1$ each) composed over one shared return capacity of 1.5 give $\lambda^*=0.75$,
hence a closure deficit 0.25 that conservation forces into support drawdown. (iii) Composing two
budget certificates costs $\sum_\varphi \pi_\varphi^+\bar v_\varphi T$ where the *interface price* is
$\pi_\varphi=(\lambda_1^\top G_1-\lambda_2^\top G_2)_c$; the interface is free iff all $\pi_\varphi\le0$;
for one exchange of box $[0,L]$, certification of the composition holds iff $L\le(B_1+B_2)/(\pi T)$.
(iv) With $\dot x_i=-x_i$, $Z=x_1+x_2=100e^{-t}$, barrier $x_i\ge1$, the identifiability set of the
first exit time over the fibre $\{x_1+x_2=100,1\le x_i\le99\}$ is $[0,\log 50]$, so no aggregate record
fixes the event time; identifiability is equivalent to the fibre being a point, and the endpoints are
LP extrema whenever the constraints are linear and the event time monotone.

**Your task.** 1. Check each claim; produce a counterexample or a proof, and state the sharpest true
form (e.g. replace "monotone in the initial state" by the exact condition under which the fibre image is
an interval). 2. Determine what is preserved under composition among: positivity/orthant invariance,
flux-reconstruction consistency, barrier reachability, maintainability over an infinite horizon, and
adequacy of a service floor; give the necessary-and-sufficient side condition for each, in the declared
data. 3. Decide whether a *galois* connection exists between the closure LP and the certificate LP
(duality between return-capacity feasibility and multiplier existence), and if so write it: it would
replace (iii)'s sufficient condition with a necessary-and-sufficient one. 4. Extend to $n>2$ parts:
is the total interface cost the sum of pairwise prices, or is there a many-sided residual? Prove it.
5. Name one published indicator or public accounting practice (footprint accounts, SEEA-based national
accounts, groundwater stress indices, circularity metrics) whose headline number changes sign of
interpretation under (ii) or (iv), and state what data would be needed to quantify the change.

**Constraints.** Do not soften or re-classify any claim's status (established / conditional / illustrative
/ negative witness). Do not introduce a new "sustainability index". Every numeric instance must be
reproducible from a script you provide; report the LPs in standard form. Flag, do not repair, any place
where the manuscript's own vocabulary would have to change.

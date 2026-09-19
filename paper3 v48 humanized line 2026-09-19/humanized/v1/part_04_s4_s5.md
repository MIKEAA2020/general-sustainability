# 4. Conservation and positivity of the closed ledger — what the wiring guarantees

> **In plain words.** Here the article stops building and starts proving, for the closed system of §2.2. Eight things are shown. Nothing disappears from the natural block except through the named exits. Nothing ever goes negative. The system cannot sit still while people keep extracting at effort. When extraction stops, there are exactly three kinds of place it can settle. The total amount ever extracted is capped by the budget you started with. A hybrid (jump) version of the balance holds on stated conditions. Summing equations is not a proof of anything. And all of that together forms a complete portrait of the closed ledger, which §9 then uses as the boundary against an open system.

## 4.1 The natural-block mass identity

**Theorem 7 (Natural-block mass identity).** *Let $M=N+A_{\mathrm{act}}+A_{\mathrm{geo}}+U$. Along every trajectory of the closed natural block (2) with optional mining restored,*

$$\dot M=-qEN-C_{A,\mathrm{lim}},$$

*i.e. mass leaves the natural block exactly at the extraction rate, plus the donor-limited mining rate. Under the institutional-failure specialization ($C_A=0$), $\dot M=-qEN$. The identity is stated for the declared harvest routing $\alpha=0$ of §2.2; with a detritus-routed harvest fraction $\alpha>0$ the block export is $(1-\alpha)qEN$ and the identity reads $\dot M=-(1-\alpha)qEN-C_{A,\mathrm{lim}}$.*

*Proof.* Sum the four equations of (2), with the mining term subtracted from $\dot A_{\mathrm{geo}}$:

$$\dot M=(R-qEN)+(-B+e_{GA}-e_{AG}+\gamma_UU)+(-e_{GA}+e_{AG}-C_{A,\mathrm{lim}})+(T-\gamma_UU)=R-B+T-qEN-C_{A,\mathrm{lim}},$$

and $R-B+T=R-(R+T)+T=0$. The mined fraction routes out of the four-coordinate natural block; the full-ledger theorems of §4.2–4.3 record the mining column as an internal transfer between compartments outside the block — consistent because the **block** boundary, not the **ledger** boundary, is crossed. $\blacksquare$

## 4.2 Stoichiometric conservation of the full ledger

**Theorem 8 (Stoichiometric conservation).** *Let $X=(N,P,W,I,U,A_{\mathrm{act}},A_{\mathrm{geo}})$ be the mass compartments of one resource system and $S^{\top}$ the incidence matrix of its flux ledger. One-way transfers are non-negative and donor-limited; net regeneration is the difference of two such primitives and is signed when $N>K$. Under the unit-sum routing constraints with $0\le\alpha\le1$,*

$$\dot X=S^{\top}F(X),\qquad \frac{d}{dt}\mathbb 1^{\top}X=0.$$

*Proof.* Every primitive is a transfer between two compartments, or a pair of opposite primitives implementing a two-way exchange; the corresponding column of $S^{\top}$ has entries $+1$ and $-1$ in the receiving and donating rows and zeros elsewhere. Routing tensors are column-stochastic in the destination-indexed convention by construction: each unit of a split flux sums to one across destinations. Hence $\mathbb 1^{\top}S^{\top}=0$ and $\mathbb 1^{\top}\dot X=\mathbb 1^{\top}S^{\top}F=0$. The theorem is an exact conservation identity **under the routing constraints**. $\blacksquare$

The seven-compartment incidence claimed by Theorem 8 is displayed here — in the compartment order of its statement, with the closed block's primitive fluxes, the pattern of the six-compartment $S(\alpha,\rho_P)$ of Theorem 9 with the inert column (no outflow from the inert compartment) appended, and the harvest column split by $(\alpha,1-\alpha)$. Rows $(N,P,W,I,U,A_{\mathrm{act}},A_{\mathrm{geo}})$; columns gross regeneration, density-dependent return, harvest, uptake, detritus return, $e_{GA}$, $e_{AG}$, mining (to product), product retirement, inert-bound transfer (waste → inert):

$$S^{\top}=\begin{pmatrix} 1&-1&-1&0&0&0&0&0&0&0\\ 0&0&1-\alpha&0&0&0&0&1&-1&0\\ 0&0&0&0&0&0&0&0&1-\rho_P&-1\\ 0&0&0&0&0&0&0&0&0&1\\ 0&0&\alpha&1&-1&0&0&0&\rho_P&0\\ -1&1&0&-1&1&1&-1&0&0&0\\ 0&0&0&0&0&-1&1&-1&0&0 \end{pmatrix}$$

Every column is a two-compartment transfer under the unit-sum routing constraints, so $\mathbb 1^{\top}S^{\top}=0$ column by column — Theorem 8's conservation, at sight. The natural-block rows $(N,U,A_{\mathrm{act}},A_{\mathrm{geo}})$ reproduce the four-row display of §2.2, with the harvest column now carrying its full routing ($\alpha$ to $U$, $1-\alpha$ to $P$) instead of the block-export convention of the $\alpha=0$ corner. The waste-routed mining variant appends a column with $-1$ in the $A_{\mathrm{geo}}$ row and $+1$ in the $W$ row under the same pattern. The retirement split $(\rho_P,1-\rho_P)$ and the inert-bound source (the absorbing stock $W$) are **declared routing choices of this displayed instance**; the incidence pattern — every primitive a two-compartment transfer, column sums zero — is the theorem's content, and no classification depends on the declared choices.

## 4.3 Conservation of the six-compartment ledger

**Theorem 9 (Six-compartment conservation).** *For the system of §2.3, $\tfrac{d}{dt}\mathbb 1^{\top}z=0$; the total mass $M_6=X+U+A+G+P+W$ is constant along every trajectory on which the classical solution is defined.*

*Proof.* With $M_6=\mathbb 1^{\top}z$, $\dot M_6=\mathbb 1^{\top}S(\alpha,\rho)v=0$ because each column of $S$ sums to zero. Term by term: assimilation gives $g-g=0$; mortality gives $-m+m=0$; decomposition gives $-d_U+d_U=0$; geological exchange gives $e_{GA}-e_{GA}=0$ and $-e_{AG}+e_{AG}=0$; mining gives $-c_G+c_G=0$; and the remaining harvest and retirement terms satisfy $-h+\alpha h+(1-\alpha)h=0$ and $\rho_Pr_P-r_P+(1-\rho_P)r_P=0$. $\blacksquare$

**Two scope notes are part of the theorem.** The conservation argument applies to the *expanded typed incidence system* when quality grades are split — not automatically to an undifferentiated quality-neutral loop. And open systems are explicit: imports, exports, atmospheric losses and cross-boundary transport enter as typed boundary fluxes, giving $\dot M_6=I_\partial-O_\partial$. Writing these flows explicitly is preferable to preserving a nominal invariant by allowing an unobserved or finite donor compartment to become negative.

Theorems 7–9 are three instances of the conservation lemma of Proposition 1. Each is the identity $\tfrac{d}{dt}(\ell^{\top}x)=\ell^{\top}b$ for a declared ledger and boundary with $\ell=\mathbb 1$, differentiated only by which compartments the declaration includes.

## 4.4 Orthant invariance

**Theorem 10 (Orthant invariance of the closed ledger).** *The non-negative orthant in $(N,A_{\mathrm{act}},A_{\mathrm{geo}},U)$ is forward invariant for the closed natural block (2).*

*Proof.* The right-hand side is locally Lipschitz on a neighbourhood of the closed orthant: each Michaelis–Menten factor, and $\sigma$, is $C^\infty$ on the non-negative half-line because the registered regime keeps $A_0>0$ and $A_{g0}>0$. Face by face. On $A_{\mathrm{geo}}=0$ one has $\sigma=0$, hence $e_{GA}=0$ and $\dot A_{\mathrm{geo}}=e_{AG}=\omega_AA_{\mathrm{act}}\ge0$. On $A_{\mathrm{act}}=0$ one has $s=0$, so $R=B=T=e_{AG}=0$ and $\dot A_{\mathrm{act}}=e_{GA}+\gamma_UU\ge0$. On $N=0$, extraction and uptake vanish and $\dot N=0$. On $U=0$, $\dot U=T\ge0$. Nagumo's inward-pointing criterion (Aubin, 1991) yields forward invariance of the orthant. $\blacksquare$

**Theorem 11 (Forward invariance of the six-compartment cone).** *Under the donor boundary assumptions of §2.3 — each primitive flux vanishes when its donor is empty, fluxes continuous in effort and locally Lipschitz in the state — $\mathbb R^6_+$ is forward invariant for the six-compartment system.*

*Proof.* Face by face: at $X=0$, $g=m=h=0$ so $\dot X=0$; at $U=0$, $\dot U=m+\alpha h+\rho_Pr_P\ge0$; at $A=0$, $\dot A=-g+d_U+e_{GA}-e_{AG}=d_U+e_{GA}\ge0$, the two negative terms vanishing by donor limitation ($A$ is the donor of both $g$ and $e_{AG}$); at $G=0$, $\dot G=e_{AG}\ge0$; at $P=0$, $\dot P=(1-\alpha)h+c_G\ge0$; at $W=0$, $\dot W=(1-\rho_P)r_P\ge0$. The vector field belongs to the tangent cone at every boundary point, and the tangent-cone invariance theorem applies.

Conservation and boundary admissibility are separate obligations, and the finite-donor condition carries a discipline: a target-relaxation law $e_{GA}=\omega(A_{\mathrm{eq}}-A)$ **does not satisfy it** unless also limited by $G$. It may be used only with the source declared an effectively infinite external reservoir, in which case the system is open rather than closed. $\blacksquare$

The classical lineage of these statements is the compartmental-systems non-negativity theory (Jacquez and Simon, 1993). The donor-limitation condition is the exact sufficiency requirement — **algebraic cancellation alone does not establish invariance**.

## 4.5 No interior rest at positive effort

**Theorem 12 (No interior rest at positive effort).** *Assume (H1) $E\equiv E^*>0$ is constant. Then a rest point of the closed natural block satisfies $R+C_{A,\mathrm{lim}}=0$ after restoring optional mining; with $C_A=0$ this is $R=0$, hence $N=0$ or $N=K$ or $A_{\mathrm{act}}=0$. None of these is compatible with $E^*>0$ and $N^*>0$: (i) $N=K$ and $E^*>0$ give $\dot N=-qE^*K<0$; (ii) $A_{\mathrm{act}}=0$ and $A_{\mathrm{geo}}>0$ give $\dot A_{\mathrm{act}}=\omega_AA_{\mathrm{eq,intrinsic}}\sigma>0$; (iii) $N=0$ forces $R=T=0$ and reduces to the extinction family $\mathsf R_{\mathrm{ext}}$ of Theorem 13. In particular the working point $(N^*,A_{\mathrm{act}}{}^*)=(89.526,\,397.87)$ **is not** a rest point at $E=E^*\approx2.090$: $\dot N=0$ holds there by construction ($R^*=qE^*N^*\approx0.187>0$), and the rest condition of the proof fails on the abiotic pair.*

*Proof.* At a rest point, $\dot U=0$ forces $\gamma_UU=T$. Adding $\dot A_{\mathrm{act}}+\dot A_{\mathrm{geo}}$ gives $-B+\gamma_UU-C_{A,\mathrm{lim}}=0$; with $\gamma_UU=T$ and $B=R+T$ this is $R+C_{A,\mathrm{lim}}=0$. With mining declared ($C_A>0$) this forces $R\le0$; with $C_A=0$ it is $R=0$, and from the constitutive law $R=rN(1-N/K)s=0$ implies $N=0$ or $N=K$ or $s=0$ (that is, $A_{\mathrm{act}}=0$). Cases (i)–(iii) exclude each branch at positive effort. In the mining case the contradiction is more direct: $\dot N=0$ with $E^*>0$ and $N^*>0$ gives $R=qE^*N^*>0$, while the abiotic rest condition gives $R=-C_{A,\mathrm{lim}}\le0$. At the working point $\dot N=0$ by construction while rest would require $R=0$; with $\dot U=0$ the abiotic pair would satisfy $\dot A_{\mathrm{act}}+\dot A_{\mathrm{geo}}=-R<0$. $\blacksquare$

In words: you cannot have a steady state with living stock in it while effort stays positive. The bookkeeping forces one pool or another to keep moving.

## 4.6 The extinction–geochemical rest set

**Theorem 13 (Vanishing-extraction rest set).** *With vanishing extraction ($E\equiv0$), the rest points of the closed natural block (2) are **exactly** the three sets — the extinction family $\mathsf R_{\mathrm{ext}}$, the carrying-capacity family $\mathsf R_K$, and the frozen-biomass face $\mathsf R_{\mathrm{frozen}}$; the union symbol $\mathsf R_0=\mathsf R_{\mathrm{ext}}\cup\mathsf R_K$ is retained for the two geochemical families:*

$$\mathsf R_{\mathrm{ext}}=\{N=0,\;U=0,\;A_{\mathrm{act}}=A_{\mathrm{eq,intrinsic}}\sigma(A_{\mathrm{geo}}),\;A_{\mathrm{geo}}\ge0\},$$
$$\mathsf R_K=\{N=K,\;U=\kappa_AKs/\gamma_U,\;A_{\mathrm{act}}=A_{\mathrm{eq,intrinsic}}\sigma,\;A_{\mathrm{geo}}\ge0\},$$

*where in the second family $s=A_{\mathrm{act}}/(A_{\mathrm{act}}+A_0)$ is evaluated at the solution — together with the frozen-biomass face $\mathsf R_{\mathrm{frozen}}=\{(N,0,0,0):N\ge0\}$, on which $s=0$ identically and the biomass is frozen at its initial value. With $E>0$ constant, no interior rest point (with $N^*>0$) exists (Theorem 12); the extinction face $\mathsf R_{\mathrm{ext}}$ of this set persists at positive effort, because extraction $qEN$ vanishes identically at $N=0$, and it is a boundary rest rather than an interior one. If $A_{g0}=0$ and $\sigma\equiv1$ is imposed for $A_{\mathrm{geo}}>0$, the shared active-pool ray of $\mathsf R_{\mathrm{ext}}$ and $\mathsf R_K$ is $A_{\mathrm{act}}=A_{\mathrm{eq,intrinsic}}$, $A_{\mathrm{geo}}>0$ — the endpoint $A_{\mathrm{geo}}=0$ is excluded, because there the donor-limited recharge vanishes and $\dot A_{\mathrm{act}}=-\omega_AA_{\mathrm{eq,intrinsic}}<0$. The constitutive laws carry no basal mortality independent of the support factor; adding one ($\mu_{\mathrm{basal}}N$, stock → detritus) collapses the frozen-biomass face and does not touch Theorems 7–12 or 14.*

*Proof.* With $E\equiv0$, set the four derivatives to zero. From $\dot A_{\mathrm{geo}}=-e_{GA}+e_{AG}=0$: $\omega_AA_{\mathrm{eq,intrinsic}}\sigma=\omega_AA_{\mathrm{act}}$, so $A_{\mathrm{act}}=A_{\mathrm{eq,intrinsic}}\sigma$ — the geological-exchange balance, in which the active pool is pinned to the donor-scaled intrinsic target. From $\dot N=R=0$: $rN(1-N/K)s=0$. If $A_{\mathrm{geo}}>0$ the geo-balance pins $A_{\mathrm{act}}>0$, so $s>0$ and $N=0$ or $N=K$. At the boundary $A_{\mathrm{geo}}=0$ the geo-balance forces $A_{\mathrm{act}}=0$ (since $\sigma(0)=0$), hence $s=0$ and $\dot N=0$ for every $N\ge0$; with $U=0$ the remaining equations vanish identically, so the frozen-biomass face is a rest set. From $\dot U=T-\gamma_UU=0$: $U=T/\gamma_U=\kappa_ANs/\gamma_U$, which vanishes in the $N=0$ branch and is positive in the $N=K$ branch. From $\dot A_{\mathrm{act}}=-(R+T)+0+\gamma_UU$: this vanishes in both branches, since $\gamma_UU=T$ and $R=0$ hold there. The two families together with the frozen-biomass face are exactly the stated rest set. "Geochemical" names the mechanism of both families' active-pool rest: the pool rests at the donor-scaled intrinsic target. Apart from the frozen-biomass face, no rest point exists away from extinction or carrying capacity. The institutional memory yields $E\to E^*$ at $N=0$ with extraction vanishing identically — consistent with the rest set, and not an interior rest. $\blacksquare$

## 4.7 Extraction integrability

**Theorem 14 (Integrable extraction).** *Assume $E(s)\ge0$ along the trajectory (effort is non-negative; $N\ge0$ along classical solutions is Theorem 10's). Let $M=N+A_{\mathrm{act}}+A_{\mathrm{geo}}+U$. Then*

$$M(t)=M(0)-\int_0^t qE(s)N(s)\,ds\ \ge\ 0,\qquad\text{so}\qquad \int_0^\infty qE(s)N(s)\,ds\ \le\ M(0)<\infty,$$

*in particular $qEN\in L^1(0,\infty)$, and **no trajectory maintains extraction at the working value $qE^*N^*\approx0.187$ for all time**; with mining restored, $\int_0^\infty(qE(s)N(s)+C_{A,\mathrm{lim}}(s))\,ds\le M(0)$.*

*Proof.* By Theorem 7, $M(t)=M(0)-\int_0^tqE(s)N(s)ds$; forward invariance (Theorem 10) gives $M(t)\ge0$, so the improper integral is at most $M(0)$. If $qEN\equiv qE^*N^*$ for all $t\ge0$, the integral would diverge. $\blacksquare$

This is the depletion-horizon semantics of the closed ledger in its strongest form: the donor budget is finite, and extraction is integrable against it. A constant extraction flux $c>0$ — a comparison flux only, not a donor-limited primitive the ledger's own discipline admits as a sustained law — exhausts the budget in finite time ($M$ reaches its lower bound no later than $M(0)/c$), while proportional extraction $qEN$ need not drive $M$ to zero in finite time. The integral bound of the theorem **is** the whole statement, and the hitting time of $M=0$ may be infinite. This is the finite-budget fact that §9 turns into the non-reduction boundary with the open working system.

The theorem does not select among the vanishing-extraction rests of Theorem 13: integrable extraction is compatible with approach to either the extinction family or the carrying-capacity–geochemical family, and the $L^1$ bound alone decides nothing between them.

## 4.8 The conditional hybrid moiety balance

**Conditional Theorem 15 (Hybrid moiety balance).** *Let $\chi$ denote the hybrid state and $\eta\ge0$ its primitive-flux vector — letters local to this statement, chosen so that $r$ stays the growth rate of §2.2 and $\nu$ a macro parameter of §5.4. Assume (H1) $\chi$ is absolutely continuous between locally finite event times, with left and right limits at events; (H2) $\dot\chi=S\eta+b$ with $\eta\ge0$, separate reverse columns, and donor-limited negative boundary flows; (H3) $L^{\top}S=0$. Then*

$$L^{\top}\chi(t)-L^{\top}\chi(0)=\int_0^tL^{\top}b\,ds+\sum_{t_k\le t}L^{\top}\big[\chi(t_k^+)-\chi(t_k^-)\big].$$

*Proof.* Integrate the continuous balance between consecutive events and telescope the left/right state differences. $\blacksquare$

The theorem is conditional, and its jump interpretation is part of the content: an internal-transformation jump requires $L^{\top}(\chi^+-\chi^-)=0$ or a jump incidence factorization with left-kernel conservation; a boundary-crossing jump is a boundary impulse and belongs in the boundary term. Two obligations ride the theorem. The **yield-routing obligation**: if a transformation is represented with a yield below one for a declared moiety, the omitted fraction must be routed to another represented compartment or a declared boundary flow — otherwise the claimed moiety balance holds only after silently dropping that moiety from $L$. And the **separation obligation**: this is the hybrid variant of Proposition 4, retained at its own conditional status; the two statements are not merged.

## 4.9 Cancellation is cheap

Summing the six material equations of a ten-state admissibility template gives the exact identity

$$\frac{d}{dt}\big(\bar X_A+X_J+P+U+A+G\big)=0 .$$

This is an algebraic cancellation only. It does **not** prove forward invariance of the six material states, or physical admissibility of every term. The ghost-sink check is part of the discipline: the same birth-transfer rate $gB$ enters $\dot X_J$ and $\dot A$ with opposite signs, so material not transferred to juveniles remains in $A$ — there is no unmatched sink in the six-state ledger.

The identity is retained precisely for its discipline. Formal cancellation coexists with boundary failure elsewhere in the same template (its geological exchange is **not** donor-limited), and the cancellation by itself establishes nothing about admissibility. Conservation (Theorems 7–9) and positivity (Theorems 10–11) are proved separately in every well-posed ledger of this article, exactly because **cancellation is cheap and admissibility is not**. The template's remaining negative witnesses — a variance closure that is not realizable by a non-negative spatial distribution, and an output functional without a displayed state equation — are recorded in the supplementary material as audited admissibility failures.

**The closed-ledger portrait.** Theorems 7–14 assemble into a complete qualitative portrait of the closed orthant: conservation (Theorems 7–9), positivity (Theorems 10–11), no interior rest at positive effort (Theorem 12), the two-family vanishing-extraction rest set with the frozen-biomass face (Theorem 13), and the finite donor budget (Theorem 14). The portrait is the source object handed to the interface of §9: the closed system's candidate long-time set is the rest set of Theorem 13, and the budget of Theorem 14 bounds how long any positive-flux configuration can persist.

For industrial-ecology measurement the message is direct: a "balanced" closed ledger is a **finite-budget** object, and any sustained extraction against it must integrate to a quantity no greater than the initial budget.

---

# 5. Services and the componentwise deficit — what is delivered, and what is missing

> **In plain words.** A service is not a substance. Drinking water, crop yield, fish landed: these are readings taken off the physical state, not extra mass in the boxes. This section says what a reading has to declare before it can be used, and then builds the deficit — the shortfall, component by component, which is a vector and never a number.

Services are observations or feasible outputs of the physical state, not additional conserved mass. Internal physical transfers are not services merely because they appear in a ledger. A typed readout identifies the delivered flow, its boundary, and any unit conversion. This distinction is the accounting counterpart of the ecological-economics point that a service flow — Ayres' useful-work reading, Daly's throughput-of-services reading — is not the same object as the mass that delivers it.

## 5.1 The service readout and the contemporaneous balance

For services indexed by $i=1,\dots,n$, write $s_i(t)=O_i(x(t),u(t),\theta)$, where $u$ denotes admissible operating or extraction choices and $s_i$ and the demand $d_i$ share service-specific units. Where delivered services are selected or converted ledger fluxes, the readout is linear in the primitives,

$$s=O(x,u,\theta)=Q(\theta)v(x,u),$$

with every row of $Q$ declaring the delivery boundary and the conversion into one service-specific unit. More general state-dependent readouts are possible. The contemporaneous component balance is

$$b_i(t)=s_i(t)-d_i(t),$$

and $b_i(t)\ge0$ means measured supply meets measured demand for component $i$ at that instant. It does not by itself imply that the underlying trajectory is sustainable. A stock can meet current demand while declining toward a threshold, and a stock below a desired level can have a positive current balance while recovering.

## 5.2 The state-dependent feasible balance domain

**Definition 1 (Feasible balance domain).** *For an admissible operating set $\mathcal U(x,t)$ and a declared demand set $\mathcal D(t)$,*

$$\mathcal B(x,t)=\{O(x,u,\theta)-d: u\in\mathcal U(x,t),\ d\in\mathcal D(t)\}.$$

The geometry of the balance domain is state dependent and inherited partly from the stock–flow model. **No unrestricted argument can replace an application-specific analysis of $\mathcal B(x,t)$.** This domain is the object against which any scalar certificate claim must be checked (§10.1): a weighted sum certifies componentwise non-negativity on $\mathcal B(x,t)$ only through an implication proved from the physical restrictions that define the domain.

## 5.3 Support provenance and the directional support gap

Current service adequacy and regenerative feasibility are different claims. Let $\Gamma_{\mathrm{all}}(x,t)\subseteq\mathbb R^n_+$ contain the service vectors feasible through all pathways admitted by an application, and $\Gamma_{\mathrm{reg}}(x,t)\subseteq\Gamma_{\mathrm{all}}(x,t)$ the feasible set after imposing the declared regenerative-flow, system-boundary, material-quality, and exergy or capacity restrictions. These correspondences are **application inputs** obtained from a typed pathway or technology model; the stock ledger alone does not construct them.

**Definition 2 (Directional regenerative-support fraction and gap).** *Assume (H1) $0\in\Gamma_{\mathrm{reg}}(x,t)$; (H2) a nonzero service direction $\bar s\ge0$ is chosen. Define*

$$\alpha_{\mathrm{reg}}(\bar s;x,t)=\sup\{\alpha\in[0,1]:\alpha\bar s\in\Gamma_{\mathrm{reg}}(x,t)\}.$$

*The vector $(1-\alpha_{\mathrm{reg}})\bar s$ is the directional support gap, measured in the same service units as $\bar s$. A realized service $s\in\Gamma_{\mathrm{all}}\setminus\Gamma_{\mathrm{reg}}$ is **support-dependent under that declaration** even when $s\ge d$.*

Attainment requires closedness: if $\Gamma_{\mathrm{reg}}$ is not closed the supremum may not be attained, and the gap is relative to a supremal fraction, not necessarily to an achievable boundary service. The **non-interpretation discipline** is equally part of the definition: the statement neither subtracts raw material from service nor proves that a physical stock is declining. Net depletion still requires a negative stock balance or a trajectory argument. The provenance partition behind $\Gamma_{\mathrm{reg}}$ — renewable flow, recovered or recycled material, imports, non-renewable drawdown — never adds unlike physical units.

## 5.4 The componentwise deficit and the specialization identity

On the unreduced ledger the physical deficit is the diagnostic

$$\Delta_{\mathrm{phys}}(t)=C(t)-\hat M^{\top}S(t),$$

with $C$ the operative extraction-law readout and $\hat M$ the declared demand-coverage matrix mapping the moiety readout $S=Cx$ — the composition matrix $C$ of Lemma 3, **a different object from the coverage vector $C(t)$ despite the shared letter** — into the units of that coverage vector: rows indexed by covered services, columns by moieties, entries the declared stoichiometric coefficients of the coverage convention. The hat distinguishes the matrix from the scalar natural-block mass $M$ of §4.1. It does not drive the physical equations, and it is not equal to $-\dot N$ unless waste–product feedback vanishes and the service is identified with regeneration. The single-resource specialization (the omitted product, waste and price parameters $\mu,\nu,\rho$ of the unreduced ledger set to zero, together with $C_A=0$) makes that identification, and **on that class — and only on that class — the deficit collapses to the stock-decline rate.**

**Remark 16 (Exact specialization deficit identity).** *On every trajectory of the specialized system, and of every reduced system whose stock equation is $\dot N=R(N,A)-qEN$,*

$$qEN-R(N,A)=-\dot N,\qquad \Lambda(t):=[qEN-R]_+=[-\dot N]_+ .$$

*Proof.* Substitute the stock equation: $qEN-R=-(R-qEN)=-\dot N$. $\blacksquare$

The collapse is a **property of the specialization**, not a definition of liquidation on the unreduced ledger. The general diagnostic remains $C-\hat M^{\top}S$.

**Decline pressure.** In the registered delay family the depletion-pressure classification is

$$\Lambda(t)=\max\{0,\;qE(t)N(t)-R(N(t),A_{\mathrm{act}}(t))\}=\max\{0,-\dot N(t)\}:$$

the memory input of the institutional dynamics is a smoothed stock-decline rate, exactly the positive part of the decline. It is **not** a stock-level scarcity measure, **not** an unmet-consumption measure, and **not** an independently observed service deficit.

Since $qEN-R(N,A_{\mathrm{act}})=O(N)$ as $N\to0$, the raw decline input vanishes near extinction while the positive baseline source of the effort law can still sustain commanded effort. The incremental decline amplification disappears, but the effort command need not. A controller intended to respond to low stock *irrespective of its current rate of change* requires a separately registered level-dependent channel.

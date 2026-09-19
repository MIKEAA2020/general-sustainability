# 8. Domain templates at registered status — what a real application would still have to do

> **In plain words.** A "template" is a scaffold with its holes visible. The article names the data and the checks that would have to arrive before a domain claim could be made, and it says plainly that they have not arrived. Nothing in this section is a result. This is also where the paper keeps its promise about the groundwater two-pool model: the requirements are registered, not discharged.

## 8.1 The phosphorus template

The phosphorus domain enters at **registered template status**: an identification ladder for the resource–product–waste–detritus structure of §2.3 (phosphate rock → fertilizer → soil pool → runoff, with the mining flux $c_G$ and the recycling routes $\alpha,\rho_P$), whose constitutive content — the yield and loss functions, the recovery fractions, the price response of the reserve classification — is **declared, not established**. The reserve and production quantities used in §6.5.3 carry their source vintage (U.S. Geological Survey, 2026). The template's competing-model ladder is an identification object, and its falsification protocols — *which observation would reject which routing assumption* — are recorded obligations, not results.

## 8.2 The groundwater template and the two-pool gap

The groundwater template enters at registered status with an admitted object and a declared gap.

- **Admitted object.** The one-pool affine approximation behind the anomaly-persistence index of §6.5.1.
- **Not established.** The two-pool model — active storage with a slow donor pool, the two-compartment structure of §2.2.

The registered identification requirements for closing the gap are: geological geometry (aquitard depth and extent); multi-depth heads; pumping tests; tracer, isotope or water-age evidence; recharge estimates; prior ranges for the storage and fast–slow coupling parameters; and the discipline that **leakage terms may not absorb unexplained residuals**.

## 8.3 Extractor-side harvest economics

On the extractor side, the same discipline applies to economic steady states.

In the open-access equilibrium of a single-species fishery (Clark, 1990), the bioeconomic equilibrium stock

$$S_{\mathrm{OA}}=\frac{c}{pq}$$

is set by cost, price and catchability — and is **infeasible as a management target** under a conservation floor $S_{\min}>S_{\mathrm{OA}}$: the unregulated equilibrium lies below the floor, and no open-access trajectory is viable against it. The modified golden rule in its constant-unit-cost form, $g'(S_\delta)=\delta$, sets the optimal steady stock for the discount rate $\delta$ (Clark's general form carries an additional marginal-stock-effect term). A harvest tax shifts the open-access equilibrium to

$$S_{\mathrm{OA}}=\frac{c}{(p-\tau)q}.$$

The tax moves the economic equilibrium, but it does not move the physical floor. That distinction is the extractor-side counterpart of the accounting discipline of §6: **instrument parameters and constraint thresholds are different objects, and no tax schedule substitutes for a constraint the ledger must satisfy.**

The growth function $g$ of this paragraph is a declared constitutive readout on the stock **for this extractor-side remark only**. It is not a primitive of the closed natural block of §2, and nothing in this section is promoted into the typed ledger.

---

# 9. The interface with institutional delay dynamics — one shared equation, and a wall

> **In plain words.** There is a companion paper about institutions that review extraction periodically, with delays. This article is about the material ledger. They agree on exactly one object, an identity for the deficit. Beyond that object they cannot be merged, and this section proves the impossibility rather than asserting compatibility. That is the unusual part: a paper naming the bridge *and* the gap, with numbers for both.

The partition between this article and the companion delay-dynamics analysis (Author, D., et al., *in review*) is fixed by an **interface contract**. This article owns the closed material accounting: the primitive ledger equations and full routing, the conservation and positivity theorems of §4, the componentwise deficit and depletion diagnostics of §§5–6, and the closed-donor no-rest and extraction-integrability limitations. The companion owns the open frozen-donor retarded systems and their bifurcation results. The interface is viable — but **not** because the closed primitive ledger dynamically reduces to the open working system. The two are different completions, and the contract records both the exact shared object and the rejected mapping.

**The exact shared object.** Under the single-resource specialization of §5.4 ($\mu=\nu=\rho=0$ — the product, waste and price parameters of the unreduced ledger: its macroeconomic-feedback, recycling and price-response channels, per the §2.2 gloss — and the mining intensity $C_A=0$), with the local stock equation $\dot N=R-qEN$, the deficit identity

$$D(t):=qE(t)N(t)-R(N(t),A(t))=-\dot N(t),\qquad \Lambda(t):=[D(t)]_+=[-\dot N(t)]_+$$

holds for every trajectory of either the specialized ledger or the reduced core (Remark 16). The identity is the **one** object both analyses may use without substantive duplication. The reduced core's constitutive replacement $R(N,A)\to rN(1-N/K)$ is separately an approximation and carries its own finite-time scope (Theorem 1 and Remark 2: the replacement is pointwise on the interior support region and non-uniform through the depleted-pool boundary).

The contract fixes more than the deficit identity. The shared object includes the non-negative orthant and the sign pattern of harvest as an outflow from the living stock. **A companion model that routes the "unsustainable portion" of a flow into a different compartment changes the incidence and thereby leaves the interface** (§2.5).

**The hand-off projection.** Under the institutional-failure specialization, the macroeconomic block, prices and demand do not appear in $(\dot N,\dot A_{\mathrm{act}},\dot A_{\mathrm{geo}},\dot U,\dot Z,\dot E)$ — the closed block's six right-hand sides, geological donor included: each depends only on the block's own variables and the delayed memory, and none contains the macroeconomic states, prices or demand. The ecological–institutional subsystem is an exact closed projection **for every parameter value**, with no singular limit required. The memory–effort pair $(Z,E)$ is the gated three-state core and working four-state core of the companion delay-dynamics analysis (*in review*; eq. (1) and §2.4 of that analysis), not an object of this article; the projection claim — the semiconjugacy condition $\mathcal D_\pi(\xi)f(\xi)=F(\pi(\xi))$ on the history phase space — is made under that citation and is **not re-proved here**.

**The non-reduction boundary.** There is no exact dynamic reduction from the closed primitive finite-donor ledger to the open working system — not as a projectable reduction and not as a regular perturbation. The reasons are mathematical.

1. **Different targets.** The primitive ledger uses the intrinsic donor-limited target $A_{\mathrm{eq,intrinsic}}$; the working system uses the derived target $A_{\mathrm{eq},W}=A_{\mathrm{eq,intrinsic}}+\kappa_AK/\omega_A$. The three registered numbers display the separation: $A_{\mathrm{eq,intrinsic}}=50$, the working active pool $A_{\mathrm{act},*}=397.87$, and $A_{\mathrm{eq},W}=50+\kappa_AK/\omega_A=5{,}050$ — the two equilibria differ by a factor of eight and the two targets by two orders of magnitude.
2. **Same state, different fields.** At the working equilibrium the two $A_{\mathrm{act}}$ vector fields, written at the same state $(N,A_{\mathrm{act}},U)$, differ by

$$\omega_A\big(A_{\mathrm{eq},W}-A_{\mathrm{eq,intrinsic}}\sigma\big)-\gamma_UU=\kappa_AK-\gamma_UU$$

under the registered scale separation ($\sigma\approx1$): approximately **0.535** stock units per year at the working point's quasi-rest detritus level (where $\gamma_UU=\mathcal T^*\approx4.47$, the gross uptake at the working point) and $\kappa_AK=\mathbf{5.000}$ stock units per year at $U=0$ — an $O(1)$ to $O(\kappa_AK)$ discrepancy, not a small residual. The two same-state flux readings behind it are the working recharge $\omega_A(A_{\mathrm{eq},W}-A_{\mathrm{act},*})=4.652$ and the closed donor flow $e_{GA}-e_{AG}\approx-0.348$, whose signed difference is $4.652+0.348=5.000=\kappa_AK$. The difference is $U$-dependent because the working field omits the detritus return $\gamma_UU$ that the closed field carries — the $U$-handling split is part of this obstruction, and $\mathcal B^*-R^*=\mathcal T^*$ is the working system's turnover balance, **not** the field difference.
3. **The working point is not at rest in the closed system.** It requires continuing geological support — the flux $\omega_A(A_{\mathrm{eq},W}-A_{\mathrm{act},*})=4.652133\ldots$ stock units per year, supplied every year by a donor the working system treats as a parameter — and is not a rest point of the closed finite-donor system (Theorem 12). At the same state the closed primitive donor flow is $e_{GA}-e_{AG}=\omega_A(A_{\mathrm{eq,intrinsic}}-A_{\mathrm{act},*})\approx-0.348$: **the donor gains in the closed ledger where the working completion has it losing 4.652** — the two fields have opposite signs on the donor coordinate, not merely different magnitudes. The working-point figures $E^*\approx2.090$, $N^*=89.526$, $A_{\mathrm{act},*}=397.87$ and the recharge $4.652$ are imported at the companion's registered precision; the reverse check $qE^*N^*=0.001\times2.090\times89.526\approx0.187$ is consistent to the quoted digits.
4. **The draw diagnostic is not an error measure.** The cumulative donor-draw quantity $\varepsilon_G(T)=G_0^{-1}\int_0^T|e_{GA}-e_{AG}|\,dt$ is a diagnostic of the *derived-target completion*, not a trajectory-tracking error between the two fields; **no finite-time tracking theorem between the completions holds**.
5. **Integrability forbids indefinite persistence.** The closed primitive system makes sustained extraction integrable (Theorem 14) and therefore cannot possess the working positive-flux rest indefinitely.

The five reasons form a trichotomy: **(1)–(3)** are short-time obstructions — the two $A_{\mathrm{act}}$ fields differ by $\kappa_AK-\gamma_UU$ at the same state, which is $O(1)$ at the working point's quasi-rest detritus level ($\approx0.535$) and at most $\kappa_AK=O(5)$ (at $U=0$), and trajectories of the two systems diverge on $O(1)$ timescales; **(5)** is the long-time obstruction — extraction on the closed ledger is $L^1$ in time (Theorem 14); **(4)** is neither — $\varepsilon_G$ is not a tracking error between the two fields at any timescale.

**Theorem (Non-reduction of the open working completion).** *There is no exact dynamic reduction, no regular perturbation, and no finite-time tracking correspondence from the closed primitive ledger (2) to the open working system, because (i) the targets differ by $\kappa_AK/\omega_A=5{,}000$ stock units (structural); (ii) the $A_{\mathrm{act}}$ fields differ by $O(1)$ at the working point (short-time); (iii) the working point is not a rest point of (2) (Theorem 12; equilibrium); (iv) $\varepsilon_G$ is not a tracking metric (diagnostic misuse); and (v) extraction on (2) is $L^1$ in time (Theorem 14; long-time).*

The mapping type for exact dynamic reduction is **rejected**. The permitted relation is analogy for shared mechanism language, plus diagnostic reconstruction of omitted mass flows. The companion's global periodic results are properties of its reduced systems and do not transfer to the closed primitive ledger; in particular, Hopf or periodic orbits of the frozen-donor working system are not properties of (2). In the other direction, the working system is an open projection: omitted turnover is routed to a diagnostic detritus or inert sink, imposed recharge corresponds to geological draw, and the reduced trajectory's mass discrepancy is reconstructible from the omitted flows.

**The frozen-donor limit is a corollary of the structural clause (i).** Rescaling the donor as $G=G_0g$ with $g(0)=1$ gives $\dot g=-G_0^{-1}(e_{GA}-e_{AG})$. The limit $G_0\to\infty$ freezes $g$ but does not restore the working completion's derived target: the limiting recharge field still uses $A_{\mathrm{eq,intrinsic}}$, not $A_{\mathrm{eq},W}$, so the scaling is **not** a regular perturbation of the working vector field. Local Hopf persistence of the working system under this primitive scaling is not claimed; a different derived-target completion would be required before a regular-perturbation theorem could be formulated.

**The long-time finite-budget interpretation.** With the donor $G(t)$ included as a state, the closed system is an autonomous retarded equation with a slow donor coordinate. The companion's $\tau_+\approx150$ yr upper cycle is a frozen-donor object; on the closed system it can persist only as a *transient* on the finite donor budget. The transient-duration statement is an order/budget bound, not an asymptotic estimate: under a sustained lower extraction flux $c>0$ the duration is bounded above by $G_0/c$.

The scale must name its flux. At the closed-block extraction rate $c=qE^*N^*\approx0.187$ stock units per year, the budget bound is $G_0/c\approx2\times10^{6}$ years; at the working completion's recharge flux $\mathcal B^*\approx4.652$ stock units per year, the draw scale is $G_0/\mathcal B^*\approx8.6\times10^{4}$ years. The "tens of thousands of years" heuristic uses the working flux (at $G_0/A_{\mathrm{act},*}=10^3$), and both scales sit far above the institutional delays of the companion family. Whether the frozen-donor local Hopf structure persists as a slowly drifting transient in the closed donor system is an **open slow-passage problem**; the mass budget alone does not establish it.

**The implication for industrial-ecology coupling** is concrete: a closed physical ledger and an open working system can share one diagnostic identity without sharing a dynamics, and the temptation to import one system's theorems into the other must be resisted.

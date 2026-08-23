
## 14. Interface principles and operational principles

The previous manuscript’s twelve principles are retained but reclassified as interface or operational principles rather than undifferentiated axioms.

1. **Boundary principle [D/M]:** every claim declares a model boundary and interfaces.
2. **Dependency principle [D/E]:** persistence depends on internal or external stocks, services, structures, or relations.
3. **Dynamic-balance principle [L]:** persistent net depletion of a finite essential non-substitutable stock is incompatible with indefinite preservation of a positive lower bound.
4. **Capacity principle [D/E]:** sources, sinks, institutions, and adaptive processes have state-dependent capacities and rates.
5. **Viability principle [D]:** essential predicates must remain satisfied along the relevant trajectory, not only on average.
6. **Feedback principle [E/L]:** sensing and response must be adequate relative to the modeled dynamics.
7. **Disturbance principle [D]:** robustness claims specify a disturbance class.
8. **Typed-dependency principle [D/N]:** obligations follow declared support, impact, and normative edges rather than mere nesting.
9. **Burden-allocation principle [D/N]:** transferring risk or depletion does not discharge responsibility unless the transfer satisfies the registered allocation and affected-population constraints.
10. **Adaptive-capacity principle [E]:** changing conditions may require robustness, adaptation, or architecture transformation.
11. **Plural-value principle [N/D]:** non-commensurable protected values are not silently converted into one weighted sum.
12. **Legitimacy principle [N]:** social constraints and permissible revisions identify their authority and procedure.

These principles organize model construction. They do not all have the same epistemic status.

---

## 15. Conditional lemmas

The following statements are intentionally modest. They are consequences of particular model signatures, not novel universal laws.

### Lemma 1. Finite essential-stock condition [L]

Given

\[
\dot s=I+R-O-D,
\]

if \(s(0)<\infty\), viability requires \(s\ge s_{\min}>0\), the stock is non-substitutable, and

\[
\liminf_{T\to\infty}
\frac{1}{T}
\int_0^T(O+D-I-R)\,dt
>0,
\]

then indefinite viability is impossible.

This applies to \(\operatorname{Sust}_\infty\), not to every finite-horizon assessment. For finite \(T\), the same balance estimates time to threshold.

### Lemma 2. Rate–buffer condition [L]

If load \(L(t)>C(t)\) persists long enough to exhaust every relevant buffer before corrective action is effective, a dependent constraint is violated. The model must specify the buffer and dependence; the statement is not an independent empirical law.

### Lemma 3. Zero-margin fragility [L]

If a necessary process operates at its exact capacity and an admissible disturbance can increase load or reduce capacity, robust viability requires a sufficiently fast response or another buffer. Otherwise the robustness margin is zero for that disturbance direction.

### Lemma 4. Delay condition [L/M]

Let \(T_c\) be modeled time to a critical threshold without effective intervention. If

\[
T_r\ge T_c
\]

and no adequate buffer or anticipatory action exists, reactive feedback cannot prevent threshold crossing. Empirical use depends on valid estimates of \(T_r\) and \(T_c\).

### Lemma 5. Obligatory-support condition [L]

If \(A\) has a registered obligatory-support edge to function \(q\) supplied by \(B\), policy \(\pi\) removes \(q\), and no registered adequate substitute exists, then \(\pi\) violates \(A\)’s functional constraints.

### Lemma 6. Non-compensation [L/N]

If a registry entry is tagged non-compensable, improvement in another dimension does not discharge its violation. This follows from the selected decision rule; the designation itself may be normative or empirical.

### Lemma 7. Conditional growth bound [L]

Suppose output \(Y\) imposes burden

\[
L(Y)\ge\alpha Y
\]

for persistent \(\alpha>0\), while admissible capacity satisfies \(C(t)\le\bar C<\infty\). Then

\[
Y\le\frac{\bar C}{\alpha}.
\]

The result does not state that every measure of economic value must stop growing. It states that unbounded growth is incompatible with bounded capacity when burden intensity remains bounded away from zero.

### Lemma 8. Local corridor failure [L]

If \(a_{\min}(z)>a_{\max}(z)\), no action at state \(z\) simultaneously satisfies the relevant lower and upper bounds. Structural transformation follows only under the stronger reachability condition stated in Section 7.2.

---

## 16. Efficiency, sufficiency, circularity, and distribution

### 16.1 Efficiency

Efficiency is output per unit input or burden:

\[
\eta=\frac{Y}{L}.
\]

Total load is

\[
L_{tot}=\frac{Y_{tot}}{\eta}.
\]

Efficiency can enlarge a corridor but does not guarantee sustainability when scale grows faster than efficiency.

### 16.2 Sufficiency

Sufficiency concerns the level, composition, and distribution of demand:

\[
a_{\min}\le a\le a_{\max}.
\]

Efficiency modifies conversion; sufficiency addresses total required activity and who receives provision.

### 16.3 Circularity

If material demand is \(m\) and recovered fraction \(\chi\), virgin input is approximately

\[
m_{virgin}=(1-\chi)m+\text{quality and process losses}.
\]

Circularity can reduce burden but does not eliminate collection losses, energy requirements, dissipation, or scale constraints.

### 16.4 Distribution and justice

For groups \(g\), the registry may contain

\[
y_g\ge y_g^{\min},
\qquad
b_g\le b_g^{\max},
\qquad
r_g\le r_g^{\max},
\]

for provision, burden, and risk. Procedural constraints may restrict admissible policies. These are explicit [N] commitments, not deductions from viability theory. The architecture prevents their disappearance inside aggregate averages once adopted.

---

## 17. Resilience, time, and latent liabilities

### 17.1 Dynamical resilience

Dynamical or ecological resilience is persistence of a declared regime or functional identity under disturbance. It may be measured through basin geometry, recovery, or disturbance sets depending on the model. An undesirable regime may be dynamically resilient.

### 17.2 Sustainability robustness

Sustainability robustness is persistence of the complete typed judgment under a specified disturbance family. The margin \(\Gamma(z_0)\) in Section 7.3 is one representation.

These terms should not be merged. Resilience is not automatically desirable; sustainability robustness includes normative and relational projections.

### 17.3 Horizon typing

All primary assessments are indexed by \(T\):

\[
\operatorname{Sust}_T(S)
\not\Rightarrow
\operatorname{Sust}_{T+\Delta T}(S).
\]

Infinite-horizon claims use a separate object \(\operatorname{Sust}_\infty\). Average-balance statements apply to that object or to sufficiently large finite horizons under additional assumptions.

### 17.4 Latent liabilities

Some deferred burdens may be represented by vector \(\lambda(t)\):

\[
\dot\lambda
=
\text{burden creation}
-
\text{burden resolution}.
\]

Constraints such as \(\lambda_j\le\lambda_j^{\max}\) can prevent deferred harm from appearing as present success. This is a modeling device, not a claim that all intergenerational obligations reduce to one known scalar.

---

## 18. Observability, measurement, power, and strategy

### 18.1 Measurement architecture

For critical indicator \(i\), record

\[
\mathcal I_i
=(z_i,\hat z_i,\theta_i,\tau_i,\sigma_i,\rho_i),
\]

where \(z_i\) is the construct, \(\hat z_i\) its estimate, \(\theta_i\) threshold, \(\tau_i\) delay, \(\sigma_i\) uncertainty, and \(\rho_i\) spatial, temporal, or demographic resolution.

An indicator is inadequate if it measures the wrong construct, arrives too late, aggregates away protected groups, is strategically manipulable, or reacts only after irreversible harm.

### 18.2 Observability audit

For each critical state:

1. Is it directly measurable?
2. If not, what proxy is used?
3. What causal relation links proxy and construct?
4. What are error and delay?
5. Can actors manipulate the indicator?
6. Does aggregation hide local violations?
7. Is measurement frequent relative to system dynamics?
8. Which action changes when the threshold is crossed?

### 18.3 Control-authority audit

For each intervention, record responsible actor, legal authority, resources, implementation delay, affected interests, resistance, enforcement, unintended effects, and reversal conditions.

### 18.4 Strategic behavior and power

Actors may have conflicting objectives and unequal control. Power influences:

- who defines identity and constraints;
- whose burdens are visible;
- who controls data and intervention;
- which alternatives enter the architecture registry;
- whose risk is accepted.

Power therefore affects \(\Omega\), \(U_{\mathrm{impl}}\), interface evidence, and transformation feasibility. The first manuscript locates these effects without claiming a universal theory of power.

### 18.5 Adaptive monitoring

Let

\[
\varepsilon(t)
=z_{observed}(t)-z_{predicted}(t).
\]

If error exceeds a declared tolerance or an interface assumption fails, the certificate must be reviewed, narrowed, suspended, or replaced.

### 18.6 Multi-model uncertainty

Let

\[
\mathfrak M=\{M_1,\ldots,M_n\}
\]

be plausible models. A model-robust policy satisfies constraints across the credible set. Where none does, use adaptive pathways, reversible experiments, discriminating monitoring, and precaution around irreversible states. Uncertainty changes decision architecture; it is not merely an error bar.

---

# Part V. Instantiation Sketches

## 19. Minimal stock–capacity–support model

Let \(s\) be an essential stock, \(c\) internal capacity, \(e\) supporting-system state, and \(a\) activity:

\[
\dot s=R(s,c,e)-U(a)-D_s(s,w),
\]

\[
\dot c=I_c(a)-\delta_c c-\Phi_c(a,c,w),
\]

\[
\dot e=R_e(e)-B_e(a,e,w).
\]

Require

\[
s\ge s_{\min},
\qquad
c\ge c_{\min},
\qquad
e\ge e_{\min},
\]

and minimum provision

\[
P(s,c,e,a)\ge y_{\min}.
\]

The sketch distinguishes stock depletion, capacity erosion, support degradation, and underprovision. It also represents cascades in which declining support lowers renewal, shrinking the stock and overloading capacity.

### Box 12. Instantiation status

> The following ODEs exhibit the architecture’s interfaces and candidate failure loops. They are not calibrated models, computed kernels, or empirical validation.

---

## 20. Ecological instantiation

For managed grassland, let \(B\) be vegetation biomass, \(N\) soil condition, and \(H\) harvest or grazing pressure:

\[
\dot B
=r(N)B\left(1-\frac{B}{K(N)}\right)-H-D_B(w),
\]

\[
\dot N
=R_N(N,B)-E_N(H,w).
\]

Ecological constraints require minimum biomass and soil condition while provisioning requires minimum yield. This produces

\[
H_{\min}
\le H
\le H_{\max}(B,N,w).
\]

The relevant conclusion is not that sustainability maximizes conservation or harvest. It seeks a viable corridor under the declared identity and disturbance set.

### 20.1 Physical ecological foundation

Ecological systems are materially constrained. Models must respect mass balance, energy conservation, finite process rates, and entropy production. Open ecosystems maintain organized structure through energy throughput and material exchange; local material cycling is not perfectly closed. Carbon, nitrogen, phosphorus, sulfur, water, biomass, and waste sinks can be represented through explicit balances.

Non-equilibrium thermodynamics, stoichiometry, kinetics, transport, and temperature may supply domain-specific bounds. The maximum entropy production principle is not adopted as an indubitable universal axiom. Onsager relations and Carnot efficiency should not be indiscriminately applied to whole ecosystems, economies, or societies. Their use requires scope conditions. Thermodynamics constrains social systems through physical embodiment but does not derive rights, justice, legitimacy, or meaning.

---

## 21. Economic instantiation

Let \(K\) be productive capital, \(I\) essential inventories, \(D\) obligations, \(E\) ecological support, \(q\) output, and \(c_g\) provision to group \(g\):

\[
\dot K
=\operatorname{Inv}(q)-\delta K-\Phi_K(q,K),
\]

\[
\dot I
=q-\sum_g c_g-\operatorname{loss}(I),
\]

\[
\dot D
=r_DD+\operatorname{borrowing}-\operatorname{repayment},
\]

\[
\dot E
=R_E(E)-\operatorname{burden}(q).
\]

Output growth alone does not establish sustainability. Provision, solvency, maintenance, ecological support, distribution, and commons allocation must be jointly assessed. Behavioral equations require empirical contract types; accounting identities may be deterministic.

---

## 22. Social-institutional instantiation

For a public health service, let \(Q\) be unresolved cases, \(C\) treatment capacity, \(A_g\) access, \(T_g\) waiting time, \(V_g\) procedural violations, and \(\lambda\) incoming demand:

\[
\dot Q
=\lambda(t)-\mu(C,Q),
\]

\[
\dot C
=I_C-\delta C-\Phi_C(Q/C).
\]

Constraints may include

\[
A_g\ge A_g^{\min},
\qquad
T_g\le T_g^{\max},
\qquad
V_g\le V_g^{\max},
\qquad
C\ge C_{\min}.
\]

This model uses a common grammar of load, capacity, delay, and distribution without treating rights, legitimacy, or cooperation as conserved physical stocks. Its equations remain empirical placeholders requiring measurement, uncertainty, and strategic semantics.

---

## 23. Coupled community instantiation

Consider a community whose economy depends on a renewable resource and generates pollution.

### 23.1 Ecological module

Let \(R\) be resource stock, \(P\) pollution, and \(E\) regenerative capacity:

\[
\dot R
=r(E)R\left(1-\frac{R}{K_R(E)}\right)
-H-\phi(P)R+w_R,
\]

\[
\dot P
=\epsilon_YY-A-\lambda_E(E)P+w_P,
\]

\[
\dot E
=J_E-\delta_EE-\psi_H(H,R)-\psi_P(P).
\]

Constraints include

\[
R\ge R_{\min},
\qquad
P\le P_{\max},
\qquad
E\ge E_{\min}.
\]

### 23.2 Economic module

Let output be

\[
Y=F(K,H,L_b),
\]

with

\[
\dot K
=J_K-\delta_KK-\chi(P,R)K,
\]

\[
\dot I
=Y-\sum_gC_g-J_E-J_K-J_G-A-\operatorname{loss}(I).
\]

Distribution shares satisfy \(C_g=\theta_gC\), \(\sum_g\theta_g=1\).

### 23.3 Governance module

Let incoming workload be

\[
\Lambda
=\Lambda_0
+\alpha_PP
+\alpha_I\max(0,I_{\min}-I)
+\alpha_DD_{ineq},
\]

with

\[
\dot Q=\Lambda-\mu(G,Q),
\]

\[
\dot G
=J_G-\delta_GG-\Phi_G(Q/G).
\]

Actual extraction may be

\[
H_{actual}
=H_{authorized}
+H_{unregulated}(G,\text{incentives}).
\]

The sign and form of this relation are empirical.

### 23.4 Joint interfaces and candidate loops

The policy vector is

\[
u=(H,A,J_E,J_K,J_G,\theta_1,\ldots,\theta_n).
\]

Candidate failure loops include:

- extraction lowers resource and regenerative capacity, raising future pressure;
- production raises pollution, which damages ecological and productive capacity;
- present provision pressure suppresses maintenance, intensifying later pressure;
- inequality may raise conflict and governance workload, weakening compliance;
- aggregate output may rise while ecological, governance, or group-specific constraints deteriorate.

These loops are hypotheses and interface demonstrations, not validated predictions.

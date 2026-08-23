# Article 009 Evaluation and Verification

## Bibliographic identity

**Source file:** `uploads/paper3_rev2.md`  
**Title:** *Smooth-Krein Barrier Formulation of the Distributive Boundary*  
**Format:** Markdown article draft  
**Evaluation status:** evaluated; integration prohibited pending mathematical and empirical redesign

## Executive verdict

The article contains a legitimate research objective: distributive sustainability should be multidimensional, noncompensatory, bottom-sensitive, and intergenerational. However, the central mathematical theorem is false for finite smoothing parameter, the proposed LogSumExp expression is dimensionally invalid because it exponentiates and sums unlike units, the construction is not yet a control-barrier-function result, the global-bottom-decile pooling formula is incorrect, the cohort transition condition is malformed, and the empirical claims exceed the supplied data.

The paper should not be integrated or published in its current form. Its valid content should be preserved and redesigned as a typed distributive-viability module using normalized margins, an exact nonsmooth minimum or conservative smooth inner approximation, explicit dynamics and robust barrier conditions, correct mixture-distribution quantiles, and separately validated indicators for each adaptive-capacity dimension.

---

## 1. Terminology

The title says “Smooth-Krein,” while the text invokes the Kreisselmeier–Steinhauser (KS) function and LogSumExp. These are not interchangeable names. The construction should be called a **Kreisselmeier–Steinhauser smooth minimum** or LogSumExp soft minimum. “Krein” should be removed unless a distinct Krein-theoretic result is intended.

The article also uses “equilibrium” for a static conjunction of constraints. No equilibrium is defined. The appropriate term is admissibility, safe set, or viability condition.

---

## 2. Dimensional failure of the KS expression

The article defines

\[
h_{dist}(a)
=-\frac1\rho
\log\left(
\sum_k
\exp\bigl(\rho(a_{floor,k}-a_k)\bigr)
\right).
\]

The four coordinates include USD/day and dimensionless 0–1 indices. Exponential arguments must be dimensionless, and quantities with unlike units cannot be summed inside one LogSumExp.

### Required normalization

Define a positive scale \(s_k\) with the units of axis \(k\), and use dimensionless margins

\[
m_k(a)
=
\frac{a_k-a_{floor,k}}{s_k}.
\]

Then a soft minimum is

\[
h_\rho(a)
=-\frac1\rho
\log\left(
\sum_{k=1}^n e^{-\rho m_k(a)}
\right),
\qquad \rho>0.
\]

The choice of \(s_k\) affects conservatism and must be justified; normalization is not normatively neutral.

---

## 3. The stated “iff” theorem is false for finite \(\rho\)

For dimensionless margins \(m_k\), the KS soft minimum satisfies

\[
\min_k m_k-rac{\log n}{\rho}
\le
h_\rho(m)
\le
\min_k m_k.
\]

Therefore:

\[
h_\rho(m)\ge0
\quad\Longrightarrow\quad
m_k\ge0\ \forall k.
\]

So \(h_\rho\ge0\) is a conservative sufficient certificate for conjunction.

The converse fails. If every margin equals zero, then

\[
h_\rho
=-\frac{\log n}{\rho}<0,
\]

although every exact floor is satisfied. More generally, all margins may be nonnegative while the soft minimum is negative.

Thus the theorem

> a region is admissible iff the finite-\(\rho\) smooth-KS barrier is nonnegative

is false.

### Valid replacements

1. **Exact nonsmooth conjunction**
   \[
   h_{min}(a)=\min_k m_k(a),
   \qquad
   h_{min}\ge0
   \Longleftrightarrow
   m_k\ge0\ \forall k.
   \]

2. **Conservative smooth inner certificate**
   \[
   h_\rho(a)\ge0
   \Longrightarrow
   a\in K.
   \]

3. **Known approximation error**
   use the displayed \(\log n/\rho\) bound to quantify conservatism.

The limit

\[
\lim_{\rho\to\infty}h_\rho=\min_km_k
\]

is correct.

---

## 4. This is not yet a control-barrier-function theorem

A scalar function defining or approximating a safe set is not by itself a control barrier function. A CBF result requires dynamics and a control condition, for example

\[
\dot a=f(a,u,w)
\]

and a robust inward condition such as

\[
\exists u\in U(a)
\quad\forall w\in W(a):
\quad
\nabla h_\rho(a)\cdot f(a,u,w)
+\alpha(h_\rho(a))
\ge0.
\]

Additional conditions are needed for nonsmooth \(h_{min}\), relative degree, sampled implementation, partial observation, and institutional authority.

The regional quantity

\[
H_{region}(t)
=
\inf_{i\in D1(t)}h_\rho(a_i(t))
\]

also reintroduces nonsmoothness and may not be observable for all individuals. It should be treated as a population worst-case statistic or robust constraint, not automatically a smooth CBF.

The named theorem should therefore be demoted until dynamics and barrier conditions are supplied.

---

## 5. Adaptive-capacity variables are not operationalized

The proposed vector is

\[
a_i=(a_{i,1},a_{i,2},a_{i,3},a_{i,4}).
\]

Problems include:

- “net exergy / disposable income” conflates physical and monetary quantities;
- the stated unit is PPP USD/day, so the coordinate is income/consumption, not exergy;
- biophysical, infrastructure, and agency indices lack measurement models;
- “Ashby bandwidth” is not an operational indicator;
- floors 0.70, 0.60, and 0.50 are unsupported;
- axis dependence and double counting are not addressed;
- the relevant unit—individual, household, fractile, region—changes without a mapping theorem.

Each axis requires a construct definition, unit or scale, data source, uncertainty, affected population, normative authority, and floor rationale.

PIP income/consumption data cannot validate the other three axes.

---

## 6. Poverty-line update and PPP consistency

The article uses the former World Bank international poverty line of \$2.15/day in 2017 PPP. That line is valid for historical analyses explicitly maintained in 2017 PPP units, but it is no longer the current World Bank international poverty line.

In June 2025, the World Bank replaced it with \$3.00/day in 2021 PPP. A revised empirical study must either:

- remain explicitly in 2017 PPP with the historical \$2.15 line and consistent PIP series; or
- convert all observations and thresholds to 2021 PPP and use the current \$3.00 line.

Values in different PPP vintages cannot be compared directly.

Official source: World Bank, “June 2025 Update to Global Poverty Lines,” https://www.worldbank.org/en/news/factsheet/2025/06/05/june-2025-update-to-global-poverty-lines.

---

## 7. Global bottom-decile pooling is incorrect

The expression

\[
P_{global}^{D1}
=
\sum_r
\frac{P_r}{P_{total}}
F_r^{D1}
\]

is not, in general, the global bottom-decile distribution or mean. Population-weighting regional bottom deciles does not identify the lowest 10% of the pooled global population because regional decile thresholds differ.

### Correct mixture construction

Let \(F_r(y)\) be the full income/consumption CDF for region \(r\) and \(w_r=P_r/P_{total}\). Then

\[
F_{global}(y)
=
\sum_r w_rF_r(y).
\]

The global bottom-decile threshold is

\[
q_{0.1}
=
F_{global}^{-1}(0.1).
\]

The share of the global bottom decile coming from region \(r\) is proportional to

\[
w_rF_r(q_{0.1}),
\]

with tie handling where needed. The bottom-decile mean requires integration of the pooled distribution below \(q_{0.1}\), not averaging regional bottom-decile means.

The reported values for Sub-Saharan Africa, South Asia, and the global pooled decile cannot be verified without PIP query definitions, country coverage, survey years, welfare concepts, PPP vintage, interpolation, weights, and code.

---

## 8. Simpson’s paradox claim is unsupported

Aggregation can conceal subgroup deprivation, but the paper does not demonstrate a Simpson reversal. Calling the issue “Simpson paradox in joint-distribution form” is unjustified without showing a reversal of an association or ordering under aggregation.

Use “aggregation concealment” or provide an explicit Simpson-paradox construction.

---

## 9. Regional table exceeds the evidence

The table reports income values and then claims pass/fail outcomes on four axes. PIP supports monetary welfare estimates, not direct biophysical, infrastructure, or agency measurements.

Specific unsupported claims include:

- “SSA: NO (all four axes)”;
- “South Asia: a2 low” without an a2 dataset;
- “East Asia and Pacific: yes” on all axes;
- “Latin America: marginal” on the complete vector.

The article also asserts 1990–2024 multi-axis trajectories without displaying or sourcing data for three axes.

These statements must be removed or replaced by separately sourced, uncertainty-aware indicators.

---

## 10. Cohort transition tensor is malformed

The article defines

\[
T_{t,t+1}(j,j')
=
\Pr(a_{t+1,j'}\mid a_{t,j}).
\]

Then writes

\[
\sum_j
T_{t,t+1}(1,j')\,
\bar a(t+1)
\ge
\bar a(t),
\]

which has inconsistent indices and does not specify scalar or vector ordering.

A coherent formulation is:

\[
T_{jj'}(t)
=
\Pr(S_{t+1}=j'\mid S_t=j),
\qquad
\sum_{j'}T_{jj'}(t)=1,
\]

and, for vector adaptive-capacity means \(\bar a_{j'}(t+1)\),

\[
\sum_{j'}
T_{jj'}(t)
\bar a_{j'}(t+1)
\succeq
\bar a_j(t),
\]

componentwise or under another explicitly declared partial order.

Intergenerational claims additionally require cohort identity, attrition, migration, household composition, survey comparability, and normative justification.

---

## 11. Operational falsification section is incoherent

The proposed conditions do not define a clear hypothesis and falsifier.

- “Region inversion” appears to describe crossing a floor but the direction is unclear.
- The text says the barycenter “falls below” the barrier when a trajectory crosses the floor, although upward crossing should improve the margin.
- “A previously admissible region remains admissible” is confirmation, not falsification.
- No estimator, confidence interval, sample design, or multiple-axis decision rule is specified.

A valid empirical design must preregister:

- unit of analysis;
- each indicator and floor;
- smoothing parameter and normalization;
- uncertainty propagation;
- bottom-decile estimator;
- transition hypothesis;
- direction of predicted change;
- observation that counts against the hypothesis.

---

## 12. Normative and distributive scope

The central normative concern is legitimate: adaptive capacity is held and distributed, and aggregate viability can coexist with severe deprivation. The module should remain explicit that floors and worst-off criteria are normative commitments.

The four-axis truncation does not fully represent:

- who causes burdens;
- who benefits;
- procedural rights;
- power and capture;
- within-group heterogeneity;
- future persons;
- spatial and environmental exposure.

The master typed registry, commons allocation, and normative authority structure are more appropriate than treating the vector as complete B6 operationalization.

---

## 13. Salvage design

### 13.1 Exact distributive safety

Use dimensionless normalized margins

\[
m_{i,k}
=
\frac{a_{i,k}-a_{floor,k}}{s_k}
\]

and exact conjunction

\[
h_{min}(a_i)=\min_km_{i,k}.
\]

A bottom-group safety condition may use a quantile or essential infimum, depending on data and normative choice.

### 13.2 Conservative smooth certificate

Use

\[
h_\rho(a_i)
=-\frac1\rho
\log\sum_ke^{-\rho m_{i,k}},
\]

with the approximation bound and only the valid implication

\[
h_\rho\ge0
\Longrightarrow
h_{min}\ge0.
\]

### 13.3 Dynamic barrier

After defining dynamics and implementable policies, impose a robust CBF or viability condition. Do not label a static soft minimum a control barrier.

### 13.4 Correct pooled distribution

Construct the global mixture CDF and bottom-decile threshold from microdata or harmonized grouped distributions.

### 13.5 Separate empirical axes

Use validated sources for monetary welfare, nutrition/health stability, infrastructure access, and agency. Report each axis and uncertainty separately before applying a conjunctive rule.

### 13.6 Intergenerational transition

Define states, cohorts, transition probabilities, and componentwise expectations consistently; test non-decline as a separate empirical/normative hypothesis.

---

## 14. Publication assessment

The article should not be integrated or published in its current form. Under the non-loss rule:

- preserve the distributive research question;
- reject the finite-\(\rho\) “iff” theorem as stated;
- reject dimensional mixing in the KS expression;
- reject the pooled-decile formula;
- reject unsourced regional four-axis conclusions;
- retain the exact conjunction, conservative smooth approximation, worst-off focus, intergenerational objective, and empirical-design ambition after correction.

A redesigned distributive-methods paper could become independently merited if it provides validated multidimensional indicators, correct global distribution construction, uncertainty propagation, and a genuine dynamic viability/barrier result. Until then, the material belongs as a deferred distributive module rather than a standalone result.

---

## 15. Verification verdict

### Valid content

- distributive sustainability is multidimensional and noncompensatory;
- worst-off or bottom-group conditions cannot be replaced by aggregate means;
- smooth minimums can provide differentiable conservative approximations;
- intergenerational non-decline is a legitimate normative hypothesis;
- population weighting and global distribution construction require care;
- a short-horizon empirical programme is desirable.

### Invalid or unsupported in the current draft

- finite-\(\rho\) equivalence theorem;
- dimensionally heterogeneous LogSumExp;
- control-barrier-function terminology without dynamics;
- regional-bottom-decile pooling formula;
- Simpson-paradox claim;
- four-axis regional pass/fail table;
- floor values for non-income axes;
- cohort tensor inequality;
- five-year falsification logic;
- current PIP values without reproducible queries;
- current use of \$2.15 as the present World Bank poverty line;
- claim of complete B6 operationalization.

### Required status

**Integration hold — rejected with reason in current form; full redesign possible.**

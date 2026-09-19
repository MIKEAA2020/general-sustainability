**Definition 45 (Latest safe intervention time).** Let a critical support pool have margin
$m_0 = A_0 - A_{\min} > 0$ over its declared barrier and net drawdown $d_0 > 0$, so $\dot A = -d$.
Let $\tau$ be the declared unavoidable delay before drawdown can begin to fall, and let $\rho > 0$ be the
declared maximum rate of that fall, with the reaching of $d = 0$ declared achievable. The *latest safe
intervention time* is the largest further postponement that still admits a service-preserving transition:
$$t_{\mathrm{last}} \;=\; \sup\Bigl\{\, L \;:\; m_0 \;\ge\; \inf_{d(\cdot)} \int_0^{\,\tau+L+d_0/\rho} \!\! d(t)\,dt
\;\text{over}\; d \equiv d_0 \;\text{on}\; [0,\tau],\ \dot d \ge -\rho,\ d \ge 0 \Bigr\} .$$
It is a feasibility deadline, not a forecast: the quantifier order is "there exists one response, and every
declared disturbance is then respected", not "every disturbance has some response of its own", and the inner
infimum prices the best admissible response rather than an expected one.

**Proposition 41 (The deadline has a closed form, and it is not the horizon).** Under the declaration of
Definition 45 the least attainable additional loss is
$$m_{\mathrm{needed}} \;=\; d_0\tau + \frac{d_0^{2}}{2\rho} ,$$
a transition respecting $A \ge A_{\min}$ exists exactly when $m_0 \ge m_{\mathrm{needed}}$, and
$$t_{\mathrm{last}} \;=\; \frac{m_0}{d_0} - \tau - \frac{d_0}{2\rho} \;=\; H^{\mathrm{loc}} - \tau - \frac{d_0}{2\rho} ,$$
with $H^{\mathrm{loc}} = m_0/d_0$ the frozen-rate ratio of Proposition 26, read on the support pool in
the manner of Definition 22. The two objects differ by the
physical cost of delay and of finite deployment speed, so $t_{\mathrm{last}} < H^{\mathrm{loc}}$ whenever
$\tau$ and $\rho$ are finite, and the gap is not a discount applied to the horizon but a different
quantifier over the same declaration. Where $t_{\mathrm{last}} < 0$ the pool can lie above its barrier,
every trajectory inside the declared corridor, while the service-preserving transition is already
infeasible --- which is the case a horizon cannot express.
Illustration, declared as illustrative and not empirical: $m_0 = 100$ units, $d_0 = 10$ units per year,
$\tau = 2$ yr, $\rho = 1$ unit per year$^2$ gives $H^{\mathrm{loc}} = 10$ yr and $m_{\mathrm{needed}} = 70$,
so ten years of coverage leaves three years to begin: $t_{\mathrm{last}} = 10 - 2 - 5 = 3$ yr. With
$m_0 = 25$, $d_0 = 4$, $\tau = 3$ yr and $\rho = 0.5$ the horizon reads $6.25$ yr while
$t_{\mathrm{last}} = -0.75$ yr. Replacing $H^{\mathrm{loc}}$ by the true horizon $T$ is a step Proposition 26
licenses in direction only: where the depletion law is nondecreasing in the stock, $T \ge H^{\mathrm{loc}}$
and the deadline moves later, never earlier, while the two ramp terms are untouched; the closed form above is
then the conservative side of the substituted expression, and no equality is claimed for it.

*Proof.* The integrand $d$ is non-negative and the constraint set is lower-bounded in slope, so the loss is
minimised by letting $d$ fall as early and as fast as it is allowed to: any postponement of the ramp adds
area and nothing else. On $[0, \tau]$ the drawdown is held at $d_0$, contributing $d_0 \tau$; the ramp from
$d_0$ to $0$ at slope $-\rho$ lasts $d_0/\rho$ and contributes the triangle $\tfrac{1}{2} d_0^{2}/\rho$.
Adding gives $m_{\mathrm{needed}}$; the equivalence is the definition of the supremum; and solving
$d_0(\tau + L) + d_0^2/(2\rho) = m_0$ for $L$ gives the stated $t_{\mathrm{last}}$. □

**Definition 46 (Supportable-output envelope).** For a declared ledger, barrier family and horizon,
$$\mathcal Y(T) \;=\; \bigl\{\, y \ge 0 \;:\; \exists\ \text{an admissible trajectory on } [0,T]
\ \text{with service at least } y \ \text{throughout and } x(t) \in \mathcal K(t) \ \forall t \bigr\}$$
is the set of service rates supportable for the whole horizon. Three readings and no fourth. The set is
decreasing in $T$ by restriction, so an envelope number is always a pair (rate, horizon). A single quoted
rate is a selection from the set, and Proposition 29 says which selections can be certified aggregators;
the envelope itself is the report. And at the frozen-rate corner the first empty horizon is the
$T = m_0/(\underline\delta g_m)$ of Definition 22, so a published "years of supply" measures the declared
drawdown path together with the barrier, never the stock alone: it is an envelope statement, and a
sustained deficit below the declared $\underline\delta$ moves it without moving the stock.

**Remark 35 (What a non-displacement gate can say on this apparatus).** An additionality or
non-displacement claim is a comparison of two declarations, not a forecast of a counterfactual world: on this
apparatus the intervention is non-displacing at the declared timescale when the closure deficit of
Definition 22, evaluated on the composition of the project block with the host ledger, is not below the
deficit of the host ledger alone. The gate is then checkable from the declarations, and it fails in the
ordinary way --- a project that re-labels an existing mobilisation as its own leaves the composed deficit
where it was, and a predicate on deficits reports that, where a predicate on attributions would not. What
the gate cannot say is carried by its baseline: the host ledger is declared, not estimated, and where the
two declarations share a compartment the deficit is read on the quotient, so it is not the sum of the two
deficits --- Proposition 36's warning about conserved quantities applies to deficits as well.

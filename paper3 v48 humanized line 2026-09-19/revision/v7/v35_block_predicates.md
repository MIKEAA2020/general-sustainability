**Definition 41 (Control margin).** Let $(\mathcal K_\rho)_{\rho \ge 0}$ be the declared nested family of
corridor sets. The *control margin* of a state is
$$\mu(x_0) \;=\; \sup\{\, \rho \;:\; x_0 \in \mathcal K_\rho \,\}.$$
Two readings are licensed and no third is: with a normalised margin $\mu$ is dimensionless, and it is a
min-type quantity in the sense that $\mu(x_0) \ge \rho$ if and only if $x_0 \in \mathcal K_\rho$, so what it
answers is whether a declared corridor contains the state. It prices no recovery, it bounds no exit time on
its own, and it inherits every conservatism of the envelope that produced the family.

**Definition 42 (Affinity, the fourth admissibility predicate).** Conservation, capacity and typing are the
three predicates a declared flux must pass. Where the declaration also carries a specific Gibbs energy
$g_j$ for each compartment, a fourth is available: a conversion with stoichiometric row $\nu$ (products
positive) has *affinity* $\mathsf{A} = -\nu^{\top} g$, and the conversion is admissible only when
$\mathsf{A} \cdot J \ge 0$ along its declared rate $J$ --- equivalently, only when it does not raise the
total Gibbs energy in the direction it is booked. A flux with $\mathsf{A} \cdot J < 0$ is not a noisy
observation of an allowed process but an impossible one, and the reparation is to re-declare the ledger,
never to re-estimate the flux. Where energies are not declared the predicate is reported as not
established, exactly as the conservation residual of Definition 23 is.

**Proposition 40 (An empty corridor comes with a named conflict).** For declared bounds $A v \le b$ and
declarative identities $C v = d$, the corridor $\{v : A v \le b,\ C v = d\}$ is empty if and only if there
are $y \ge 0$ and free $z$ with
\[
y^{\top} A + z^{\top} C = 0 \qquad \text{and} \qquad y^{\top} b + z^{\top} d \;<\; 0 .
\]
Any such pair is a *corridor-infeasibility witness*, and its support --- the rows with $y_i > 0$ --- names
the declared floors and ceilings that cannot hold at once. The empty-corridor findings of Section 6.5 are of
this kind: they say not that the system is unstable but that the declaration is jointly unsatisfiable, and
the remedy is to withdraw a bound, not to re-tune a controller.

*Proof.* Append the identities as $C v \le d$ and $-C v \le -d$ and apply Gale's theorem of the
alternative (Gale, 1957; Ahuja et al., 1993): its second system is the displayed pair, with $z$ the
difference of the two multiplier blocks and the strict inequality normalised from $-1$. □

**Definition 43 (Circulation time).** On a stationary pattern in which a cycle of $n$ pools carries the
common rate $q > 0$ past masses $m_1, \dots, m_n$, the *circulation time* is
$$\tau^{\mathrm{circ}} \;=\; \frac{\sum_i m_i}{q} \;=\; \sum_i \frac{m_i}{q} ,$$
the mean time a unit of the moiety takes per revolution of that cycle. It is a property of the declared
pattern, not of a trajectory, and it is not any pool's residence time: stationarity forces one common rate
around a simple cycle, so a pool that several cycles share has a residence time per source rather than one
overall, and where several cycles coexist the quantity is a vector indexed by cycle --- a scalar quotation
must name its cycle. Yield inflation is invisible here by construction: a demand met with no stationary pattern behind it
has no circulation time to report, which is the statement of Section 6.6 in reciprocal units.

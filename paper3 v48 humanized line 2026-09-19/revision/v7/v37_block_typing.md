### 3.8 The type structure the operator's subscript abbreviates

**Definition 47 (Type structure).** Equation (1) writes the incidence operator as $S_{\mathcal{T}}$, and the
subscript has not been defined. It is not decoration. The sentence of Section 2.1 that entries may be added
within a row "only when their types and units agree", the requirement that a disturbance $d_x$ be itself typed,
Definition 42's listing of typing as one of the three predicates a declared flux must pass, and Section 6.5's
charge that a score mixes objects which are incommensurable under the typing it invokes --- all of these
presuppose an object that is never given. A *type structure* $\mathcal{T}$ on a ledger is a single declaration consisting of three
items: a set $\mathsf{Ty}$ of types; for each compartment $i$, a type $\mathrm{ty}_i \in \mathsf{Ty}$ and a
unit $\mathrm{un}_i$, so that an entry of the state vector carries the pair
$(\mathrm{ty}_i, \mathrm{un}_i)$ rather than a number alone; and a declared set $\mathsf{Cv}$ of *conversion
coefficients*, each an ordered triple $(\alpha, \beta, c)$ with $\alpha$ and $\beta$ distinct types and
$c > 0$, attached to a named conversion process and read as "one unit of $\beta$ is obtained from $c$ units of
$\alpha$ by that process". Nothing in this list is derived from the stoichiometry; all of it is declared
alongside it.

Admissibility then has content. A sum $\sum_{i \in I} x_i$ is admissible as one ledger quantity only when
$\mathrm{ty}_i$ and $\mathrm{un}_i$ agree for every $i \in I$; across types there is no sum, only a conversion,
and a conversion appears as a signed pair of entries in the column of the primitive flux that performs it. A
primitive flux is *typed-admissible* when its column is of exactly one of two kinds: a *transfer*, all of whose
nonzero entries are $\pm 1$ among compartments of one type and one unit; or a *conversion*, whose entries on
the two compartments it joins are $-c$ and $+1$ for a declared $(\alpha, \beta, c) \in \mathsf{Cv}$; and no
column is both. Where the declaration draws no type distinction beyond units, every column is a transfer and
the predicate is reported as not applicable rather than as passed. Changing $\mathsf{Ty}$, $\mathrm{ty}$ or
$\mathsf{Cv}$ is a change of ledger and not a change of notation: the admissible flux set $\mathcal{K}$ of
Definition 21 is defined through $S_{\mathcal{T}}$, so it moves with the declaration, and every certificate
built on $\mathcal{K}$ moves with it.

**Proposition 42 (No conservation law crosses a type class).** *Form the graph on $\mathsf{Ty}$ in which two
types are joined when $\mathsf{Cv}$ declares a conversion between them, and call the pullback of a connected
component a type class. Then no admissible column of $S_{\mathcal{T}}$ has nonzero entries in two distinct
classes, and for a permutation of rows and columns*
$$S_{\mathcal{T}} \;=\; \bigoplus_{\gamma} S_{\gamma}, \qquad \ker S_{\mathcal{T}}^{\top} \;=\;
\bigoplus_{\gamma} \ker S_{\gamma}^{\top} .$$
*Every conservation law of the ledger is therefore carried by a single class; no conserved quantity of the
ledger prices one class against another; and an aggregate formed by adding across classes is not a consequence
of equation (1) but an additional declaration, admitted or refused on Definition 23's terms and propagating
through the certificates exactly as Proposition 36 describes.*

*Proof.* A transfer column meets one type, hence one class. A conversion column meets two types joined by a
declared coefficient, hence one class. So every admissible column has support inside a single class, which is
block-diagonality of $S_{\mathcal{T}}$ once rows are grouped by class; a vector $L$ satisfies
$L^{\top} S_{\mathcal{T}} = 0$ if and only if its restriction to each block does, which is the splitting in the
display. The final clause is read off that splitting: a left-null vector is a tuple of left-null vectors, so
nothing in the kernel relates one block to another. □

**Remark 36 (What the type structure buys, and what it does not).** Three consequences are worth separating,
because the literature runs them together. *Reporting boundaries.* Since the classes are built from the
declared conversions, drawing a reporting boundary differently --- merging two type names into one report
label, or splitting one --- cannot change $\ker S_{\mathcal{T}}^{\top}$ unless it declares or withdraws a
conversion. That is the invariance the composition calculus is sometimes asked to supply, with the hypothesis
that makes it true and with the boundary of its scope: redrawing *inside* a class is a different act, decided
by Proposition 36's compatibility condition and not by this one. *Valuation.* The predicate is a
well-posedness condition on declarations, not a thesis about worth. It says that a ledger which has added a
gigajoule to an hour of labour has not declared what it did; it says nothing about whether the two are
comparable in worth. A material-and-energy-value position stated as a substantive claim about worth is
therefore not a corollary of this apparatus, and this article does not make it: what is available here is the
position's checkable content --- Definition 47's predicate, and Proposition 29's aggregator, which does not
compensate a deficit in one compartment with a surplus in another. *Reclassification.* A reserve class
entering or leaving an asset boundary is not a change of $\mathsf{Cv}$ but a boundary transfer, and it is
priced by Definition 22's closure deficit with its declared elasticity, not by the typing predicate. The
statistical standards recalled in Section 1.5 draw their own asset boundary in economic terms of exactly that
kind, so the exposure is common to the frameworks rather than peculiar to this one, and it is a reason the
horizon readouts of Section 6 are stated with their deficit attached.



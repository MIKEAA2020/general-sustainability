# Self-Contained External Review Prompt — A001 Operator I Strong Invariance and Erosion

## Role

Act as a specialist in viability theory, differential inclusions, nonsmooth strong invariance, robust control, and quantitative set erosion. Audit two high-stakes residuals. Do not assume access to project files.

## Part A — robust strong-invariance lemma

The source claims: if a closed set `K` has a nonempty robust regulation map

\[
R_K(x)=\{u:f(x,u,d)\in T_K(x)\ \forall d\in D(x)\},
\]

and a measurable feedback selection `k(x)`, then `K` is robustly controlled invariant for every disturbance. Its proof applies a viability theorem to

\[
F_k(x)=\{f(x,k(x),d):d\in D(x)\}\subseteq T_K(x)
\]

and incorrectly infers an all-disturbance/all-solutions conclusion from existence of one viable inclusion trajectory.

### Candidate repair

Use one feedback independent of unmeasured disturbance and an envelope

\[
G_k(x)=\operatorname{clco}\{f(x,k(x),d):d\in D(x)\}.
\]

Assume `G_k` is nonempty compact convex-valued, locally Hausdorff-Lipschitz, has linear growth/forward completeness, and satisfies the proximal-normal inequality

\[
\sup_{v\in G_k(x)}\langle\zeta,v\rangle\le0
\quad\forall x\in K,\ \forall\zeta\in N^P_K(x).
\]

Required output:

1. Give the exact strong-invariance theorem and bibliographic clause supporting the all-solutions conclusion.
2. State the minimal regularity assumptions and whether proximal, Clarke, or limiting normals are required.
3. Explain precisely why the source viability proof is insufficient.
4. Provide a corrected theorem and complete proof with quantifier order
   \[
   \exists k\ \forall d(\cdot)\ \forall\text{ admitted solutions}.
   \]
5. Address measurable versus Lipschitz feedback, graph measurability, convexification, and physical implementability.
6. State forward-completeness requirements.

## Part B — quantitative erosion under observer/implementation error

The source claims: if `K` is robustly invariant under full-state feedback, the feedback has a strict inward margin on `boundary K`, and observation/implementation error is at most `epsilon`, then an erosion

\[
K^{-c\epsilon}=\{x\in K:dist(x,K^c)\ge c\epsilon\}
\]

is invariant for some `c>0`.

This is not proved in the source.

Required output:

1. Decide whether the claim is true for arbitrary closed `K`; provide a counterexample if false.
2. Identify a minimal regular set class for which a quantitative erosion theorem holds: e.g. convex, positive reach/prox-regular, or `C^{1,1}` inequality sets.
3. State exact assumptions linking:
   - nominal inward margin;
   - feedback/field sensitivity;
   - observer and implementation error;
   - normals of eroded level sets;
   - existence and completeness.
4. Derive an explicit constant or bound for `c`, not merely “proportional.”
5. Distinguish erosion of the set from erosion of a barrier superlevel set.
6. State whether the result belongs in Paper 2, an appendix, or remains a conditional programme.

## Rejection criteria

Reject any answer that:

- cites Nagumo without matching weak versus strong invariance;
- infers all disturbance trajectories from existence of one inclusion trajectory;
- assumes measurable selection creates Lipschitz dynamics;
- claims metric erosion preserves smooth normal margins for arbitrary closed sets;
- omits growth/completeness;
- leaves `c` undefined while calling the erosion result quantitative.

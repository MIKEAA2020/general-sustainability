# Self-Contained Specialist Prompt — Paper 1 Operator II Novelty and Independent-Contribution Audit

## Role

Act as an independent expert in viability theory, robust dynamic programming, hybrid reachability, transition systems, and sustainability theory. Determine whether the theorem below can support an independently citable journal article or is mainly a standard predecessor construction with new terminology. Use precise literature comparisons and verifiable citations. Do not assume access to project files.

## Candidate theorem

Let `Q` be a finite architecture set, with fixed review times

\[
0=t_0<t_1<\cdots<t_m=T,
\]

and disjoint phase state

\[
\mathcal X=\bigsqcup_{q\in Q}\{q\}\times X_q.
\]

For each stage `k<m` and state `(q,x)`:

- `A_k(q,x)` is a set of meta-actions. A meta-action is a causal within-interval rule relative to the declared information pattern and may contain one endpoint architecture transition/reset rule.
- `D_k(q,x,a)` is a nonempty disturbance set.
- `Tube_k(q,x,a,d)` contains every phase-state point visited during the interval by every admitted solution branch.
- `Succ_k(q,x,a,d)` is the nonempty set of all endpoint states after the permitted reset/translation.
- `S_k` is the transition-safe set, including physical, functional, identity, liability, obligation, and cumulative-harm constraints.
- `G` is the terminal destination set; when post-arrival maintenance is required, membership includes a destination robust viability certificate.

Define

\[
\operatorname{RPre}_k(W)=
\left\{(q,x)\in S_k:\begin{array}{l}
\exists a\in A_k(q,x)\ \forall d\in D_k(q,x,a),\\
Tube_k(q,x,a,d)\subseteq S_k,\\
Succ_k(q,x,a,d)\subseteq W
\end{array}\right\}.
\]

Let

\[
W_m=G,\qquad W_k=RPre_k(W_{k+1}).
\]

**Theorem.** `W_k` is exactly the set of states from which a causal review-time meta-policy keeps every admitted branch in each transition-safe set and reaches `G` robustly at stage `m`. If `G` is a destination robust viability kernel, concatenation yields reach-avoid-maintain.

**Proof outline.** Backward induction. Sufficiency chooses a predecessor witness and then a continuation policy from the observed successor. Necessity takes the first action of any successful policy; robust safety forces its tube into `S_k` and every successor into `W_{k+1}`. Measurable policies require measurable witness selection; otherwise the statement is set-theoretic with arbitrary selectors.

## Claimed sustainability-specific structure

The construction requires:

1. full within-interval tube safety rather than endpoint safety;
2. typed architecture-indexed state spaces;
3. resets translating state, identity, liability, obligations, and cumulative harm;
4. noncompensatory transition-safe constraints;
5. explicit separation of reaching a destination from maintaining it afterward;
6. exact versus conservative outer-tube conclusions.

## Known limitations

The theorem excludes variable endogenous event times, Zeno behavior, multiple unencoded transitions per interval, partial observation unless lifted to information state, strategic equilibrium actions, stochastic chance constraints, and selector regularity unless separately proved.

## Required audit

1. Identify the closest established results in:
   - robust/discriminating viability kernels;
   - reach-avoid and reach-avoid-stay dynamic programming;
   - hybrid systems and reset reachability;
   - finite-state transition games/model checking;
   - set-valued robust predecessor algorithms.
2. Compare hypotheses and conclusions clause by clause.
3. Separate:
   - mathematically standard recursion;
   - potentially novel typed sustainability semantics;
   - potentially novel theorem content, if any.
4. Decide whether the theorem alone is:
   - independently publishable;
   - publishable only with a nontrivial new instantiation or extension;
   - suitable only as infrastructure in a synthesis/monograph.
5. If novelty is insufficient, identify the smallest feasible theorem-strengthening that would be genuinely nontrivial without becoming unprovable. Candidates may include typed obligation-preserving resets, conservative outer-tube error bounds, compositional architecture transitions, or partial-observation information-state transformation—but recommend only what can plausibly be proved.
6. Propose one nontrivial worked transformation example that demonstrates content not reducible to renaming a standard reachability game.
7. Give a publication-safe novelty paragraph and a stronger claim that must be rejected.
8. Provide exact bibliographic references, theorem numbers where available, and stable URLs/DOIs.

## Evaluation constraints

- Do not infer novelty merely from sustainability terminology.
- Do not treat a new tuple of labels as a new mathematical theorem.
- Do not require application papers to prove the candidate theorem.
- Do not create circular dependence on a separate theorem atlas.
- Distinguish theorem novelty, modeling semantics, and empirical significance.
- If literature access is insufficient, return a bounded “novelty unresolved” decision and identify the exact missing comparisons.

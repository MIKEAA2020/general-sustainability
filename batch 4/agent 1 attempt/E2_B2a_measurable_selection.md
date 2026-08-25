# E2.B2(a) — Measurable selection of safe actions, corrected

**This file is not a repository edit.** It elevates
`batch 2/02_elevation/E2_SELECTORS_AND_CERTIFICATES.md`, B2.Theorem (a),
against `batch 4/PROOF_REAUDIT.md` Finding 5.

B2(b) (Michael / continuous selection) is not treated here. E2.B1(a)
is not treated here. One proof this turn.

---

## 0. The recorded argument has a gap; the conclusion is true

**Recorded statement.** \(A_W\) has closed graph and compact values;
consequently \(A_W\) is weakly measurable; if \(A_W(x)\ne\emptyset\) on
a measurable \(S\subseteq X\), Kuratowski–Ryll-Nardzewski supplies a
measurable selector \(u^\ast:S\to U\).

**Recorded Step 3.** Compact-valued closed-graph correspondences are
upper hemicontinuous; for such correspondences the upper inverse
\(\{x:A_W(x)\cap F\ne\emptyset\}\) of every **closed** \(F\) is closed;
“closed sets are Borel, so \(A_W\) is weakly measurable in the KRN
sense.”

**The last sentence does not follow.** KRN weak measurability is the
condition that

\[
A_W^-\!(O)
\;:=\;
\{x:A_W(x)\cap O\ne\emptyset\}
\]

be measurable for every **open** \(O\subseteq U\). Upper inverses of
closed sets and lower inverses of open sets are different generators.
For a single-valued map they coincide with the usual Borel condition;
for a set-valued map they do not. An usc compact-valued correspondence
has closed upper inverses of closed sets by definition of the upper
Vietoris topology. That is not the Effros / KRN condition.

The recorded proof therefore never produces the hypothesis of the
theorem it cites. The gap is real. It is not a false theorem: in a
metric codomain the missing implication is a one-lemma argument, and
the selector conclusion survives. The recorded “\(X\) (hence \(S\)) is
Polish” is a second, smaller, misstatement — KRN does not require the
domain to be Polish, and an arbitrary measurable \(S\subseteq X\) need
not be — and is repaired in the same stroke.

What the programme actually needs from B2(a) is a Borel safe-action
selector that E4.Thm3 can concatenate across a non-Zeno calendar.
That is kept, and strengthened: the selector is constructed, the
effective domain is closed, and a Castaing family is produced. No
appeal to an external KRN citation is required.

This file does **not** close R02 Field 12 (measurable selection of
(REG)-witnesses on \(\mathcal V\)). That is a different correspondence.
Inflating B2(a) into a solution of D2 would be a false promotion.

---

## 1. Setting and objects

\(X\) compact metric, \(U\subseteq\mathbb R^m\) compact (any compact
metric space would do), \(D\) compact metric, \(W\subseteq X\) closed.
The successor correspondence \(\operatorname{Succ}:X\times U\times D\to 2^X\)
has nonempty compact values and is Hausdorff-continuous in \((x,u)\)
for each fixed \(d\). Write \(h\) for the Hausdorff metric on nonempty
compacts of \(X\), and

\[
A_W(x)
\;:=\;
\bigl\{u\in U:\operatorname{Succ}(x,u,d)\subseteq W
\text{ for every }d\in D\bigr\}.
\]

Let \(\mathcal K(U)\) be the nonempty closed subsets of \(U\), Vietoris
topology, and write \(S_\ast:=\{x\in X:A_W(x)\ne\emptyset\}\).

Hausdorff continuity of \(\operatorname{Succ}\) in \(d\), and any
uniformity in \(d\), are **not** used for B2(a). They remain in the
recorded setting because other E2 / R03 consumers use them.

---

## 2. Corrected theorem

**E2.B2(a)\(^\ast\) (measurable selection of safe actions).**

**(A) Closed values and closed graph.** Each \(A_W(x)\) is compact.
The graph \(\{(x,u):u\in A_W(x)\}\) is closed in \(X\times U\).
Consequently \(A_W\) is upper hemicontinuous.

**(B) Effective domain.** \(S_\ast\) is closed in \(X\), hence compact
metric, hence Polish.

**(C) Weak measurability.** For every open \(O\subseteq U\), the set
\(A_W^-(O)\) is \(F_\sigma\) in \(X\). In particular it is Borel, and
\(A_W\) is weakly measurable in the KRN sense.

**(D) Vietoris–Borel.** The map \(X\to\mathcal K(U)\cup\{\emptyset\}\)
given by \(x\mapsto A_W(x)\), with \(\emptyset\) isolated, is Borel
measurable for the Vietoris topology.

**(E) Constructive Borel selector.** On every measurable
\(S\subseteq S_\ast\) there is a Borel map \(u^\ast:S\to U\) with
\(u^\ast(x)\in A_W(x)\) for all \(x\in S\). The map is obtained as a
uniform limit of finitely-valued Borel maps; no external selection
theorem is invoked.

**(F) Castaing representation.** There is a countable family of Borel
selectors \(\sigma_{jk}:S\to U\) such that
\(\{\sigma_{jk}(x):j,k\in\mathbb N\}\) is dense in \(A_W(x)\) for every
\(x\in S\).

The recorded B2(a) is (A) plus the selector half of (E), with (C)
asserted but not proved. Nothing in (A)–(F) is a retreat. Continuous
and Lipschitz selectors remain exactly where the recorded file put
them: B2(b) and “What is NOT produced”, item 2.

---

## 3. Proof of (A): values and graph

### 3.1. Closed values

Fix \(x\in X\). Let \(u_n\in A_W(x)\), \(u_n\to u\in U\). Fix
\(d\in D\) and \(y\in\operatorname{Succ}(x,u,d)\). Hausdorff continuity
of \(\operatorname{Succ}(x,\cdot,d)\) at \(u\) gives

\[
\operatorname{dist}\bigl(y,\operatorname{Succ}(x,u_n,d)\bigr)
\;\le\;
h\bigl(\operatorname{Succ}(x,u,d),\operatorname{Succ}(x,u_n,d)\bigr)
\;\xrightarrow{n\to\infty}\;0.
\]

Pick \(y_n\in\operatorname{Succ}(x,u_n,d)\) with \(y_n\to y\).
Each \(y_n\) lies in \(W\) because \(u_n\in A_W(x)\). \(W\) is closed,
so \(y\in W\). Thus \(\operatorname{Succ}(x,u,d)\subseteq W\) for every
\(d\), i.e. \(u\in A_W(x)\). So \(A_W(x)\) is closed in the compact
\(U\), hence compact.

The load-bearing half of Hausdorff continuity here is the
**lower**-semicontinuous half: every point of the limit successor set
is approximable from nearby successor sets. Upper hemicontinuity of
\(\operatorname{Succ}\) (closed graph of \(\operatorname{Succ}\) in
\(u\)) is the wrong direction and does not put \(y\) in \(W\). That is
the recorded remark after Step 4, kept.

### 3.2. Closed graph

Let \(x_n\to x\), \(u_n\in A_W(x_n)\), \(u_n\to u\). Fix \(d\) and
\(y\in\operatorname{Succ}(x,u,d)\). Joint Hausdorff continuity in
\((x,u)\) supplies \(y_n\in\operatorname{Succ}(x_n,u_n,d)\) with
\(y_n\to y\). Again \(y_n\in W\) and \(W\) closed, so \(y\in W\). Thus
\(u\in A_W(x)\).

### 3.3. Upper hemicontinuity

A compact-valued correspondence from a topological space into a
compact Hausdorff space is upper hemicontinuous if and only if it has
closed graph. (If \(x_n\to x\), \(u_n\in A_W(x_n)\), compactness of
\(U\) gives a convergent subsequence; the closed graph puts the limit
in \(A_W(x)\); this is the sequential characterisation of usc in
metric spaces.) ∎

---

## 4. Proof of (B): the effective domain is closed

\(S_\ast=\{x:A_W(x)\cap U\ne\emptyset\}\). \(U\) is closed in itself.
If \(x_n\in S_\ast\), \(x_n\to x\), pick \(u_n\in A_W(x_n)\); pass to
a subsequence \(u_{n_k}\to u\in U\); closed graph gives
\(u\in A_W(x)\). So \(S_\ast\) is closed.

In particular the natural domain of the selector problem is Polish.
An arbitrary measurable \(S\subseteq S_\ast\) need not be; it does not
have to be. See §6. ∎

---

## 5. Proof of (C): from closed inverses to open inverses

### 5.1. Closed upper inverses of closed sets

Let \(F\subseteq U\) be closed. Let \(x_n\to x\) with
\(u_n\in A_W(x_n)\cap F\). Compactness of \(U\) (equivalently:
closed subsets of compact \(U\) are compact) gives a subsequence
\(u_{n_k}\to u\in F\). Closed graph of \(A_W\) gives \(u\in A_W(x)\).
Hence \(\{x:A_W(x)\cap F\ne\emptyset\}\) is closed. This is recorded
Step 3, and it is correct as far as it goes.

### 5.2. Inner closed approximation of opens (the omitted lemma)

Let \(O\subseteq U\) be open. For \(n\in\mathbb N\) set

\[
F_n
\;:=\;
\bigl\{y\in U:\operatorname{dist}(y,\,U\setminus O)\ge 1/n\bigr\}.
\]

Each \(F_n\) is closed in \(U\), \(F_n\subseteq F_{n+1}\), and
\(\bigcup_n F_n=O\): if \(y\in O\) then, \(U\setminus O\) being closed
in the metric space \(U\), one has \(\operatorname{dist}(y,U\setminus O)>0\).

**Claim.** \(A_W(x)\cap O\ne\emptyset\) if and only if
\(A_W(x)\cap F_n\ne\emptyset\) for some \(n\).

*If* some \(y\in A_W(x)\cap O\), then \(y\in F_n\) for all large \(n\).
*Only if:* \(F_n\subseteq O\). Compactness of values is not used in
this equivalence; metrizability of \(U\) is.

Therefore

\begin{equation}
\label{eq:Fsigma}
A_W^-\!(O)
\;=\;
\bigcup_{n\ge 1}
\bigl\{x:A_W(x)\cap F_n\ne\emptyset\bigr\},
\end{equation}

a countable union of closed sets by 5.1, hence \(F_\sigma\), hence
Borel. That is KRN weak measurability. ∎

This is the whole of Finding 5. The rest of the file is elevation.

**Why the recorded sentence fails formally.** “Closed sets are Borel”
applies to the *inverses already produced*, which are closed-set
inverses. It does not manufacture an open-set inverse. In a
non-metrizable compact range the inner approximation \(F_n\) need not
exhaust \(O\) by *metric* neighbourhoods, and the implication can
fail. KRN requires a Polish (in particular metrizable separable)
codomain in any case; the lemma uses exactly that metric.

---

## 6. Proof of (D): Vietoris–Borel

The Vietoris topology on \(\mathcal K(U)\cup\{\emptyset\}\) is generated
by the sets

\[
[V]_+
=\bigl\{C:C\cap V\ne\emptyset\bigr\},
\qquad
[V]_-
=\bigl\{C:C\subseteq V\bigr\},
\]

\(V\subseteq U\) open, together with the isolated point \(\emptyset\).

- \(\{x:A_W(x)\in[V]_+\}=A_W^-(V)\) is \(F_\sigma\) by (C).
- \(\{x:A_W(x)\in[V]_-\}=\{x:A_W(x)\cap(U\setminus V)=\emptyset\}\)
  is the complement of a closed set by 5.1, hence **open**. This is
  upper hemicontinuity again.
- \(\{x:A_W(x)=\emptyset\}=X\setminus S_\ast\) is open by (B).

A map that pulls generators back to Borel sets is Borel. ∎

Upper hemicontinuity is continuity for the *upper* Vietoris topology.
It is not Hausdorff continuity of \(A_W\), and it is not lower
hemicontinuity. The latter is B2(b)’s extra hypothesis and is not
claimed.

---

## 7. Proof of (E): constructive selector

Let \(S\subseteq S_\ast\) be measurable, equipped with the trace
\(\sigma\)-algebra. \(U\) is compact metric; fix a compatible metric
\(\rho\) and a countable dense set \(\{q_i\}_{i\in\mathbb N}\) in \(U\).
All constructions below are restricted to \(S\).

### 7.1. Auxiliary fact

If \(G:S\rightrightarrows U\) is compact-valued and weakly measurable,
then \(\{x:G(x)\cap C\ne\emptyset\}\) is measurable for every closed
\(C\subseteq U\). Indeed, write \(U_k=\{y:\operatorname{dist}(y,C)<1/k\}\),
open. Compactness of \(G(x)\) gives

\[
G(x)\cap C\ne\emptyset
\;\iff\;
G(x)\cap U_k\ne\emptyset
\quad\text{for every }k,
\]

so the left-hand set is \(\bigcap_k G^-(U_k)\), measurable.

Intersecting further with an open \(O\): write
\(C\cap O=\bigcup_m C_m\) with
\(C_m=\{y\in C:\operatorname{dist}(y,U\setminus O)\ge 1/m\}\) closed.
Then \(\{G\cap C\cap O\ne\emptyset\}=\bigcup_m\{G\cap C_m\ne\emptyset\}\),
measurable. Thus \(x\mapsto G(x)\cap C\) is weakly measurable
(empty values allowed).

### 7.2. Nested correspondences of vanishing diameter

Set \(G_1:=A_W|_S\). This is compact-valued and weakly measurable by
(A) and (C). Inductively, given such a \(G_n\) with nonempty values,
define

\[
i_n(x)
\;:=\;
\min\bigl\{i\in\mathbb N:
G_n(x)\cap B(q_i,2^{-n})\ne\emptyset\bigr\}.
\]

The set is nonempty: \(\{q_i\}\) is dense and \(G_n(x)\) is nonempty
in a metric space. For each \(i\),

\[
\{x:i_n(x)=i\}
\;=\;
G_n^-\!\bigl(B(q_i,2^{-n})\bigr)
\;\setminus\;
\bigcup_{j<i}
G_n^-\!\bigl(B(q_j,2^{-n})\bigr)
\]

is measurable. Set

\[
G_{n+1}(x)
\;:=\;
G_n(x)\,\cap\,\overline B\bigl(q_{i_n(x)},\,2^{-n}\bigr).
\]

Nonempty: \(G_n(x)\) meets the open ball of radius \(2^{-n}\), hence
meets the closed ball of the same radius; the intersection of two
compacts is compact. Weakly measurable: for \(O\) open,

\[
G_{n+1}^-\!(O)
\;=\;
\bigcup_{i\ge 1}
\Bigl(
\{i_n=i\}
\,\cap\,
\bigl\{G_n\cap\overline B(q_i,2^{-n})\cap O\ne\emptyset\bigr\}
\Bigr),
\]

measurable by 7.1. Values of \(G_{n+1}\) lie in a ball of radius
\(2^{-n}\), so \(\operatorname{diam} G_{n+1}(x)\le 2^{1-n}\). The
sequence is nested: \(G_{n+1}(x)\subseteq G_n(x)\).

### 7.3. The intersection is a singleton, measurably

The nested nonempty compacts \(G_n(x)\) have diameters tending to
zero, so \(\bigcap_n G_n(x)\) is a single point \(u^\ast(x)\). Since
\(G_1=A_W|_S\), one has \(u^\ast(x)\in A_W(x)\).

Let \(g_n(x):=q_{i_n(x)}\). Each \(g_n\) is Borel (\(U\)-valued,
finitely many values on each measurable piece of a countable
partition, actually countably many). By construction
\(u^\ast(x)\in\overline B(g_n(x),2^{-n})\), so
\(\rho(u^\ast(x),g_n(x))\le 2^{-n}\). Thus \(g_n\to u^\ast\)
*uniformly* on \(S\). A uniform limit of Borel maps is Borel.

That is the selector. ∎

KRN is not used. The classical KRN theorem, stated correctly, would
also apply: domain \((S,\text{trace Borel})\), codomain \(U\) Polish,
nonempty closed values, weak measurability by (C). The recorded
phrase “\(X\) (hence \(S\)) is Polish” is false for a general
measurable \(S\) (a Borel subset of a Polish space is Polish in the
relative topology if and only if it is \(G_\delta\)). It is also
unnecessary: KRN’s Polish hypothesis is on the **codomain**.

---

## 8. Proof of (F): Castaing representation

Let \(\{q_j\}_{j\in\mathbb N}\) be the same dense set. For
\(j,k\in\mathbb N\) define, on \(S\),

\[
\Gamma_{jk}(x)
\;:=\;
\begin{cases}
A_W(x)\cap\overline B(q_j,2^{-k})
  & \text{if this intersection is nonempty,}\\[4pt]
A_W(x)
  & \text{otherwise.}
\end{cases}
\]

Let \(N_{jk}:=\{x:A_W(x)\cap\overline B(q_j,2^{-k})\ne\emptyset\}\).
This is closed in \(X\) by 5.1, hence measurable on \(S\).
\(\Gamma_{jk}\) is compact-valued and nonempty. It is weakly
measurable: for \(O\) open,

\[
\Gamma_{jk}^-\!(O)
\;=\;
\bigl(N_{jk}\cap\{A_W\cap\overline B(q_j,2^{-k})\cap O\ne\emptyset\}\bigr)
\;\cup\;
\bigl(N_{jk}^c\cap A_W^-\!(O)\bigr),
\]

measurable by 7.1 and (C). Apply (E) to \(\Gamma_{jk}\) to obtain a
Borel selector \(\sigma_{jk}:S\to U\).

**Density.** Fix \(x\in S\), \(u\in A_W(x)\), and \(\varepsilon>0\).
Choose \(j,k\) with \(\rho(q_j,u)<\varepsilon/2\) and
\(2^{-k}<\varepsilon/2\). Then \(u\in A_W(x)\cap\overline B(q_j,2^{-k})\),
so \(x\in N_{jk}\) and \(\sigma_{jk}(x)\) lies in that intersection.
Hence \(\rho(\sigma_{jk}(x),u)\le\rho(\sigma_{jk}(x),q_j)+\rho(q_j,u)<\varepsilon\).
The countable set \(\{\sigma_{jk}(x)\}\) is dense in \(A_W(x)\). ∎

Castaing is what Filippov-type approximation and convexified-envelope
arguments actually consume. The recorded theorem produced one selector.
The family is the natural strengthening and costs one more application
of the same construction.

---

## 9. What this does, and what it does not

| Recorded object | Disposition |
|---|---|
| Step 1 (closed values) | **True.** Load-bearing half is lsc of \(\operatorname{Succ}\) in \(u\). |
| Step 2 (closed graph) | **True.** Joint Hausdorff of \(\operatorname{Succ}\) in \((x,u)\). |
| Step 3, closed inverses of closed sets | **True**, and is usc. |
| Step 3, “hence weakly measurable in the KRN sense” | **Gap.** Closed inverses are not KRN inverses. Repaired by \eqref{eq:Fsigma}. |
| Step 4, “\(S\) is Polish” | **False** for general measurable \(S\). Unnecessary. |
| Step 4, existence of a Borel selector | **True**, now constructed. |
| B2(b) Michael | Untouched. lsc of \(A_W\) is still extra data. |
| Lipschitz selectors | Still not produced. |
| R02 Field 12, (REG)-witnesses on \(\mathcal V\) | **Not this theorem.** Different correspondence; remains D2. |
| E4.Thm3 concatenation | Consumes (E). Finite gluing of Borel maps at deterministic calendar times is Borel. No extra gap. |

The selector conclusion is not demoted. The recorded proof is not a
proof of weak measurability; the present one is, and it produces more
than the recorded claim asked for.

---

## 10. Claim-status

- Recorded E2.B2(a), as a *proof* that closed inverses of closed sets
  are KRN weak measurability: **not a proof**.
- Recorded selector conclusion: **true**.
- E2.B2(a)\(^\ast\): **proved** in this file, including Castaing and
  a constructive Borel selector.
- Continuous / Lipschitz selection from the present hypotheses:
  **not claimed** (and continuous selection is false without B2(b)’s
  extra lsc + convexity: a standard two-point usco has no continuous
  selector).

No part of this file modifies the repository.

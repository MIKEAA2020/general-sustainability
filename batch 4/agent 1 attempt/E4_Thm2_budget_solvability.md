# E4.Thm2 — Budget solvability, corrected

**This file is not a repository edit.** It elevates the *budget paragraph*
of `batch 2/02_elevation/E4_INTERGENERATIONAL_PRODUCTION.md`, E4.Thm2,
against `batch 4/PROOF_REAUDIT.md` Finding 3.

The induction that a nonnegative depth sequence plus jump-margin plus
within-generation erosion gives an eroded invariant path is not the
defect. The defect is the claimed solvability criterion for

\[
r_{g+1}=\ell\,r_g-b,\qquad \ell>0,\quad b\ge 0,\quad r_0\ge 0.
\]

One proof this turn. E4.Lem1(ii) is not treated here.

---

## 0. The recorded claim is false

**Recorded finite-\(G\) criterion.** Nonnegative solutions on
\(\{0,\ldots,G\}\) exist iff
\(r_0\ge b(\ell^G-1)/(\ell-1)\) for \(\ell\ne 1\)
(and \(r_0\ge bG\) for \(\ell=1\)).

**Recorded infinite-\(G\) criterion.** Nonnegative on \(\{0,1,2,\ldots\}\)
iff \(\ell<1\) and \(r_0\ge b/(1-\ell)\), or \(b=0\) and \(\ell\le 1\).

**Both are wrong, and the infinite-horizon branch is wrong in the
direction that flatters the result.**

The affine recursion is elementary. Its closed form, for \(\ell\ne 1\), is

\begin{equation}
\label{eq:closed}
r_g
\;=\;
\ell^g r_0
\;-\;
b\,\frac{\ell^g-1}{\ell-1}
\;=\;
r^\ast+\ell^g(r_0-r^\ast),
\qquad
r^\ast:=\frac{b}{\ell-1}.
\end{equation}

(The second writing is the deviation from the unique fixed point of
\(r\mapsto \ell r-b\).) For \(\ell=1\),
\(r_g=r_0-gb\).

### 0.1. Finite horizon: the missing \(\ell^{-g}\)

Requiring \(r_g\ge 0\) for every \(g=1,\ldots,G\) and rearranging
\eqref{eq:closed} gives, when \(\ell>0\), \(\ell\ne 1\), \(b\ge 0\),

\[
r_0
\;\ge\;
\max_{1\le g\le G}
b\,\frac{1-\ell^{-g}}{\ell-1}
\quad\text{if }\ell>1,
\qquad
r_0
\;\ge\;
\max_{1\le g\le G}
b\,\frac{\ell^{-g}-1}{1-\ell}
\quad\text{if }0<\ell<1.
\]

In both regimes the maximum is attained at \(g=G\). The recorded
threshold \(b(\ell^G-1)/(\ell-1)\) equals \(b(1-\ell^G)/(1-\ell)\)
when \(0<\ell<1\), which is the same expression **without** the factor
\(\ell^{-G}\). That factor is \(>1\) and grows without bound as
\(G\) grows.

**Witnesses (PROOF_REAUDIT Finding 3, reproduced).**

| \(\ell\) | \(b\) | \(G\) | recorded \(r_0\) | \(r_1\) | nonnegative on \(\{0..G\}\)? | true threshold |
|---:|---:|---:|---:|---:|---|---:|
| \(1/2\) | \(1\) | \(2\) | \(1.5\) | \(-0.25\) | no | \(6\) |
| \(1/2\) | \(1\) | \(5\) | \(1.9375\) | \(-0.03125\) | no | \(62\) |
| \(0.9\) | \(0.1\) | \(4\) | \(0.3439\) | \(0.2095\) then \(r_3<0\) | no | \(0.5242\ldots\) |

The \(\ell=1\) finite-\(G\) clause \(r_0\ge bG\) happens to be correct.
It does not salvage the rest.

### 0.2. Infinite horizon: the wrong side of the fixed point

For \(0<\ell<1\) and \(b>0\) the fixed point is
\(r^\ast=b/(\ell-1)<0\). Since \(\ell^g\to 0\),
\(r_g\to r^\ast<0\) for every finite \(r_0\). The sequence is
**eventually negative at every initial margin**.

The recorded threshold \(r_0\ge b/(1-\ell)\) is the fixed point of
\(r\mapsto \ell r+b\), i.e. the **wrong sign** on the deficit. It is
also on the wrong side of \(1-\ell\) versus \(\ell-1\).

**Witness.** \(\ell=1/2\), \(b=1\), \(r_0=2=b/(1-\ell)\):
\(2,\;0,\;-1,\;-1.5,\;\ldots\)

The recorded infinite-horizon story says a contracting reset is
sustainable if the initial margin covers a geometric series. That is
the opposite of the dynamics. A contraction with a positive per-jump
deficit drives every orbit to a **negative** attractor.

---

## 1. What the programme needs

E4.Thm2 is the quantitative reading of intergenerational
sustainability under a declared jump-margin \((\ell,b)\): the initial
erosion depth must remain nonnegative after every reset, or the
eroded set \(K_{g,-r_g}\) is not defined as an inner parallel body
and the induction has nothing to induct on.

The correct dichotomy is sharper than the recorded one, and it is a
**negative theorem** in the contracting case:

- expanding resets (\(\ell>1\)) can be budgeted by a finite initial
  margin, namely the unstable positive fixed point \(b/(\ell-1)\);
- isometric resets (\(\ell=1\)) can be budgeted on a finite calendar
  of length \(G\) by \(r_0\ge bG\), and on no infinite calendar if
  \(b>0\);
- contracting resets (\(0<\ell<1\)) with \(b>0\) are **unsustainable
  at every finite \(r_0\)**, already on a sufficiently long finite
  calendar.

That last clause is the honest content of “too slow / too thin a
reset.” The recorded formula concealed it.

---

## 2. Corrected theorem

Assume \(\ell>0\), \(b\ge 0\), \(r_0\ge 0\), and
\(r_{g+1}=\ell r_g-b\). (The sign \(\ell>0\) is the recorded
co-Lipschitz convention of E4.Lem1.)

**E4.Thm2-Budget\(^\ast\).**

**(A) Closed form.** For \(\ell\ne 1\),
\(r_g=r^\ast+\ell^g(r_0-r^\ast)\) with \(r^\ast=b/(\ell-1)\).
For \(\ell=1\), \(r_g=r_0-gb\).

**(B) Finite calendar \(\{0,\ldots,G\}\), \(G<\infty\).**
The sequence satisfies \(r_g\ge 0\) for all \(g=0,\ldots,G\) if and
only if

\begin{equation}
\label{eq:finite}
r_0
\;\ge\;
\begin{cases}
\dfrac{b}{\ell-1}\bigl(1-\ell^{-G}\bigr)
  & \text{if }\ell>1,\\[10pt]
bG
  & \text{if }\ell=1,\\[6pt]
\dfrac{b}{1-\ell}\bigl(\ell^{-G}-1\bigr)
  & \text{if }0<\ell<1.
\end{cases}
\end{equation}

If \(b=0\), this reduces to \(r_0\ge 0\) in every regime.

**(C) Infinite calendar \(\{0,1,2,\ldots\}\).**
The sequence satisfies \(r_g\ge 0\) for every \(g\in\mathbb N_0\)
if and only if one of the following holds:

- \(b=0\) and \(r_0\ge 0\) (any \(\ell>0\));
- \(b>0\), \(\ell>1\), and \(r_0\ge b/(\ell-1)\).

In particular, if \(b>0\) and \(0<\ell\le 1\), **no** finite \(r_0\)
works.

**(D) Invariance, restated.** Under hypotheses (1)–(3) of recorded
E4.Thm2 (within-generation erosion at each depth \(r_g\), jump-margin
\((\ell,b)\), non-Zeno calendar), *and* under \(r_g\ge 0\) for all
\(g\le G\) as in (B), the product path \(\prod_{g=0}^{G} K_{g,-r_g}\)
is strongly invariant in the recorded sense. If the budget
\eqref{eq:finite} fails, E4.Thm2 asserts nothing; failure of
invariance is an R03 adversarial-exit question, not a corollary of
an unsolvable recursion.

---

## 3. Proof of the budget

### 3.1. Closed form

If \(\ell=1\), then \(r_{g+1}=r_g-b\), so \(r_g=r_0-gb\) by induction.

If \(\ell\ne 1\), the unique fixed point of \(T(r)=\ell r-b\) is
\(r^\ast=b/(\ell-1)\). Then
\(r_{g+1}-r^\ast=\ell(r_g-r^\ast)\), so
\(r_g-r^\ast=\ell^g(r_0-r^\ast)\). That is \eqref{eq:closed}.

### 3.2. Finite horizon, \(\ell=1\)

\(r_g=r_0-gb\ge 0\) for all \(g\le G\) iff \(r_0\ge bG\), since the
sequence is decreasing when \(b>0\) and the last term is the smallest.

### 3.3. Finite horizon, \(\ell>1\)

Here \(r^\ast=b/(\ell-1)\ge 0\). From \eqref{eq:closed},

\[
r_g\ge 0
\;\iff\;
r^\ast+\ell^g(r_0-r^\ast)\ge 0
\;\iff\;
r_0
\;\ge\;
r^\ast\bigl(1-\ell^{-g}\bigr)
\;=\;
\frac{b}{\ell-1}\bigl(1-\ell^{-g}\bigr),
\]

where the last step used \(\ell^g>0\). The map
\(g\mapsto 1-\ell^{-g}\) is increasing, so the most restrictive
constraint on \(\{1,\ldots,G\}\) is \(g=G\). Together with \(r_0\ge 0\)
(which is weaker than the \(g=G\) bound when \(b\ge 0\), \(\ell>1\))
this is the first clause of \eqref{eq:finite}.

### 3.4. Finite horizon, \(0<\ell<1\)

Now \(r^\ast=b/(\ell-1)\le 0\). From \eqref{eq:closed},

\[
r_g
\;=\;
\ell^g r_0
-b\,\frac{\ell^g-1}{\ell-1}
\;=\;
\ell^g r_0
-b\,\frac{1-\ell^g}{1-\ell}.
\]

Thus \(r_g\ge 0\) iff
\(\ell^g r_0\ge b(1-\ell^g)/(1-\ell)\), iff
(since \(\ell^g>0\))

\[
r_0
\;\ge\;
b\,\frac{\ell^{-g}-1}{1-\ell}.
\]

The map \(g\mapsto \ell^{-g}\) is increasing, so the maximum on
\(\{1,\ldots,G\}\) is at \(g=G\). That is the third clause of
\eqref{eq:finite}.

If \(b=0\), every clause collapses to \(r_0\ge 0\).

### 3.5. Infinite horizon

**Sufficiency, \(b=0\).** Then \(r_g=\ell^g r_0\ge 0\) for all \(g\)
whenever \(r_0\ge 0\) and \(\ell>0\).

**Sufficiency, \(b>0\), \(\ell>1\), \(r_0\ge r^\ast=b/(\ell-1)\).**
Then \(r_0-r^\ast\ge 0\), so \(r_g=r^\ast+\ell^g(r_0-r^\ast)\ge r^\ast\ge 0\).

**Necessity, \(b>0\), \(\ell>1\).** If \(r_0<r^\ast\), then
\(r_0-r^\ast<0\) and \(\ell^g(r_0-r^\ast)\to-\infty\), so \(r_g<0\)
for large \(g\).

**Necessity, \(b>0\), \(0<\ell<1\).** As already noted,
\(r_g\to r^\ast<0\), so \(r_g<0\) for large \(g\), any finite \(r_0\).
Equivalently, the finite-\(G\) threshold
\(b(\ell^{-G}-1)/(1-\ell)\to+\infty\) as \(G\to\infty\).

**Necessity, \(b>0\), \(\ell=1\).** \(r_g=r_0-gb\to-\infty\).

This is (C). ∎

---

## 4. Invariance under a solvable budget

This is the recorded induction, written so that it consumes (B) rather
than the false threshold.

Assume recorded hypotheses (1)–(3) and \(r_g\ge 0\) for \(g\le G\).

*Base.* Packet B1 on generation \(0\) at depth \(r_0\ge 0\) gives
strong invariance of \(K_{0,-r_0}\) up to the first calendar boundary
(non-Zeno ⇒ the window is compact).

*Jump.* The state at the end of generation \(g\) lies in \(K_{g,-r_g}\).
E4.Lem1 sends it into \(K_{g+1,-(\ell r_g-b)}=K_{g+1,-r_{g+1}}\).
Nonnegativity of \(r_{g+1}\) is exactly what makes the inner parallel
body an inner parallel body rather than a vacuous “read as \(K_{g+1}\)”
clause.

*Step.* Hypothesis (1) at generation \(g+1\) and depth \(r_{g+1}\)
gives invariance through the next window.

*Concatenation.* Finitely many calendar gluings (non-Zeno, compact
horizon) of causal measurable selectors remain causal and measurable
(E2.B2(a)). ∎

If \eqref{eq:finite} fails then some \(r_{g_\star}<0\). The recorded
lemma reads the image as \(K_{g_\star}\), i.e. erosion depth \(0\),
and the induction at the *declared* positive depth \(r_{g_\star}\)
has no hypothesis. E4.Thm2 is then silent. That silence is the
correct negative finding, not a defect.

---

## 5. What the recorded infinite-horizon clause would have implied

The recorded pair “\(\ell<1\) and \(r_0\ge b/(1-\ell)\)” describes a
world in which a **lossy, contracting** reset can be made
intergenerationally safe by a large enough endowment. Under the
declared recursion that world does not exist. The contraction
\(\ell<1\) *amplifies* the relative deficit: each generation’s
required initial depth is \(\ell^{-1}(r_{\mathrm{next}}+b)\), and
iterating a factor \(\ell^{-1}>1\) sends the demand to infinity.

The expanding case \(\ell>1\) is the one that can be endowed once
and for all, at \(r_0=b/(\ell-1)\). That is the only infinite-horizon
positive theorem in this module when \(b>0\).

This is not a softening. It is the stronger, correctly signed
impossibility that the recorded arithmetic inverted.

---

## 6. Status

| Recorded object | Disposition |
|---|---|
| Finite-\(G\) threshold \(b(\ell^G-1)/(\ell-1)\) for \(\ell\ne 1\) | **False.** Replace by \eqref{eq:finite}. |
| Finite-\(G\) threshold \(bG\) for \(\ell=1\) | **True** (special case of (B)). |
| Infinite-\(G\) “\(\ell<1\), \(r_0\ge b/(1-\ell)\)” | **False**, and false in the flattering direction. |
| Infinite-\(G\) “\(b=0\), \(\ell\le 1\)” | **Incomplete**: \(b=0\) works for all \(\ell>0\); \(\ell>1\), \(b>0\) is the missing positive clause. |
| E4.Thm2 invariance induction | **True**, once \(r_g\ge 0\) is an actual hypothesis. Restated as (D). |
| E4.Thm2-Budget\(^\ast\) | **Proved** in this file. |

No part of this file modifies the repository.

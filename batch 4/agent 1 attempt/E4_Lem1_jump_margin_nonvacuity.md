# E4.Lem1(ii) — Jump-margin non-vacuity and declared data, corrected

**This file is not a repository edit.** It elevates part (ii) of
`batch 2/02_elevation/E4_INTERGENERATIONAL_PRODUCTION.md`, E4.Lem1,
against `batch 4/PROOF_REAUDIT.md` Finding 4.

Part (i) is the definition unpacked and is not at issue. The budget
paragraph of E4.Thm2 is not re-treated (see
`E4_Thm2_budget_solvability.md`). One proof this turn.

---

## 0. The recorded claim is false

**Recorded definition.** A reset \(R_g:X_g\to X_{g+1}\) has
**depth co-Lipschitz margin \((\ell,b)\)** (\(\ell>0\), \(b\ge 0\)) if
for every \(r\in[0,\bar r_g]\),

\begin{equation}
\label{eq:incl}
R_g\bigl(K_{g,-r}\bigr)
\;\subseteq\;
K_{g+1,\,-(\ell r-b)},
\end{equation}

with the right-hand side **read as** \(K_{g+1}\) whenever
\(\ell r-b\le 0\). Here

\[
K_{g,-r}
\;:=\;
\bigl\{x\in K_g:\operatorname{dist}(x,\,X_g\setminus K_g)\ge r\bigr\}
\]

is empty once \(r\) exceeds the inradius of \(K_g\).

**Recorded (ii).** The pair \((\ell,b)\) is declared data: it is not
derivable from Lipschitz continuity of \(R_g\) together with boundary
margins of \(K_g,K_{g+1}\) alone. The displayed witness is
\(K_g=K_{g+1}=[0,1]\) and \(C^1\) increasing bijections \(\varphi_g\)
with \(\varphi_g(0)=0\), \(\varphi_g(1)=1\), uniformly Lipschitz in
\(g\), equal to \(\lambda_g r\) near \(0\) with \(\lambda_g\downarrow 0\)
on a vanishing neighbourhood \(\rho_g\downarrow 0\). The recorded
sentence is: **no uniform \((\ell,b)\) with \(b<\infty\) exists**.

**That sentence is false**, for a reason already present in the
definition, independently of the witness.

### 0.1. Vacuous pairs

Write \(\rho(K):=\sup_{x\in K}\operatorname{dist}(x,X\setminus K)\) for
the inradius (possibly \(+\infty\)). On the test interval
\(r\in[0,\bar r_g]\) one has \(\ell r-b\le \ell\bar r_g-b\). Hence if

\begin{equation}
\label{eq:vacuous}
b\;\ge\;\ell\,\bar r_g,
\end{equation}

then \(\ell r-b\le 0\) for every tested \(r\), and \eqref{eq:incl} is
the single constraint \(R_g(K_{g,-r})\subseteq K_{g+1}\). Any reset
that sends \(K_g\) into \(K_{g+1}\) — in particular every bijection of
\([0,1]\) — satisfies this for **every** \(g\).

The pair \((\ell,b)=(1,1/2)\) is of this kind on \(K=[0,1]\) once
\(\bar r_g=\rho([0,1])=1/2\). So is every pair with
\(b\ge \ell/2\). A uniform margin with finite \(b\) therefore exists
for the recorded family, for every family of \(K\)-preserving resets,
and for the identity. The recorded “no uniform \((\ell,b)\) with
\(b<\infty\)” is false of every such family.

This is not a near-miss. The definition as written licenses a pair
that never constrains image depth, then the refutation claims no
finite pair exists.

### 0.2. The vanishing-neighbourhood witness fails even after non-vacuity

The defect is not only vacuity of the definition. The displayed
construction, with linear collapse only on \([0,\rho_g]\) and
\(\rho_g\downarrow 0\), does not refute **non-vacuous** pairs either.

If \(b<\ell\bar r_g\), the radii at which \eqref{eq:incl} is a proper
inner-body constraint are

\[
r\;\in\;\bigl(b/\ell,\,\bar r_g\bigr].
\]

For any fixed non-vacuous pair this interval is a nonempty set of
**uniformly positive** depths. Once \(\rho_g<b/\ell\), every radius at
which \(\varphi_g(r)=\lambda_g r\) is known lies in the remaining
vacuous zone \(\ell r-b\le 0\). The active test is then performed on
the unspecified patch, which may be taken \(C^1\)-close to the
identity on every compact subset of \((0,1]\) (uniformly Lipschitz
interpolant from \((\rho_g,\lambda_g\rho_g)\) to \((1,1)\)). For that
patch, \(\varphi_g(1/2)\to 1/2\), and the inradius test of a pair such
as \((1,0.4)\) **passes**.

So the recorded family, as specified, is not a witness against the
claim the lemma is trying to make. Two independent failures: a
vacuous definition, and a witness that hides inside the vacuous zone
of every fixed positive \(b\).

The numerical checks in PROOF_REAUDIT Finding 4 are not this
construction. They test a **single** slope \(\lambda=1/20\) at the
**inradius** \(r=1/2\):

| \(\ell\) | \(b\) | non-vacuous? | required depth \(\ell/2-b\) | image depth \(\lambda/2\) | deficit |
|---:|---:|---|---:|---:|---:|
| \(1\) | \(0.4\) | yes | \(0.1\) | \(0.025\) | \(-0.075\) |
| \(0.5\) | \(0.2\) | yes | \(0.05\) | \(0.025\) | \(-0.025\) |
| \(0.2\) | \(0.05\) | yes | \(0.05\) | \(0.025\) | \(-0.025\) |

Those numbers are a different, and correct, witness. The linear piece
must extend to a uniformly positive depth — the inradius — or the
active test never sees the collapse.

---

## 1. What the programme needs

E4.Lem1(ii) is the honesty clause of intergenerational transfer: a
jump-margin is **declared data for the reset family**, not a corollary
of per-map Lipschitz constants and the geometry of \(K_g,K_{g+1}\).
E4.Thm2 and E4.Thm3 consume that pair as a hypothesis. If the pair
can be written down from cheap regularity alone, the honesty clause is
empty. If the pair can be written down vacuously, the honesty clause
is also empty, and the budget recursion of E4.Thm2 is fed a number
that never fires (which is how the false finite-horizon threshold in
Finding 3 could look plausible: a vacuous \((\ell,b)\) makes
\(r_1=\ell r_0-b\le 0\) on the first jump and the induction is
silent).

The ambition is therefore not “some finite \((\ell,b)\) exists”. That
is always true under the recorded reading. The ambition is:

- the definition must **bite** — some tested radius must demand a
  positive image depth;
- under that reading, Lipschitz plus boundary geometry do **not**
  determine a pair that works for every reset sharing those data;
- a pair that does work for a given family must be **exhibited**,
  because the cheap data are compatible with arbitrarily severe
  depth collapse.

That is a stronger declared-data theorem than the recorded one, not a
softer one. The recorded sentence failed by claiming non-existence of
an object the definition supplies automatically.

Lipschitz is the wrong inequality. A Lipschitz bound plus
boundary-to-boundary gives an **upper** bound on image depth
(§4.5). A jump-margin is a **lower** bound. The two are not on
speaking terms unless a co-Lipschitz (expansive) hypothesis is added.
That companion is stated and proved as (E) below; it is the only
cheap-data derivation.

---

## 2. Objects

Let \(X\) be a metric space, \(K\subseteq X\) closed, and

\[
\operatorname{depth}_K(x)
\;:=\;
\operatorname{dist}(x,\,X\setminus K),
\qquad
\rho(K)
\;:=\;
\sup_{x\in K}\operatorname{depth}_K(x).
\]

The inner parallel body is \(K_{-r}=\{x\in K:\operatorname{depth}_K(x)\ge r\}\).
It is empty for \(r>\rho(K)\), and equal to the (possibly empty) set of
incenters at \(r=\rho(K)\). Always \(\operatorname{depth}_K\) is
\(1\)-Lipschitz, and \(K_{-r}\) is closed.

**Definition 2.1 (test horizon).** A **test horizon** for \(K_g\) is a
number \(\bar r_g\in(0,\rho(K_g)]\). If none is declared, take
\(\bar r_g=\rho(K_g)\) whenever the inradius is finite and positive.

**Definition 2.2 (recorded margin; not used below except to name the
defect).** \((\ell,b)\) is a recorded margin if \(\ell>0\), \(b\ge 0\),
and \eqref{eq:incl} holds under the \(\le 0\mapsto K_{g+1}\) convention.

**Definition 2.3 (non-vacuous depth co-Lipschitz margin).** A pair
\((\ell,b)\) is a **non-vacuous margin** of \(R_g\) for
\((K_g,K_{g+1},\bar r_g)\) if

1. \(\ell>0\), \(b\ge 0\);
2. **non-vacuity:** \(b<\ell\,\bar r_g\);
3. the inclusion \eqref{eq:incl} holds for every \(r\in[0,\bar r_g]\),
   under the same convention that the right-hand side is \(K_{g+1}\)
   when \(\ell r-b\le 0\).

Non-vacuity is exactly the statement that the active interval
\((b/\ell,\bar r_g]\) is nonempty. Equivalently: at the test horizon
itself one has \(\ell\bar r_g-b>0\), so

\begin{equation}
\label{eq:incenter}
R_g\bigl(K_{g,-\bar r_g}\bigr)
\;\subseteq\;
K_{g+1,\,-(\ell\bar r_g-b)}
\;\subsetneq\;
K_{g+1}
\end{equation}

whenever the next inradius is at least \(\ell\bar r_g-b\). (If
\(\ell\bar r_g-b>\rho(K_{g+1})\), the right-hand side of
\eqref{eq:incl} is empty and the inclusion fails as soon as
\(K_{g,-\bar r_g}\) is nonempty. Over-demanding pairs are simply not
margins. That is a separate well-definedness failure, not vacuity.)

**Lemma 2.4 (pointwise form).** For a map \(R:X\to X'\) and closed
\(K,K'\), the inclusion \(R(K_{-r})\subseteq K'_{-s}\) holds if and
only if

\[
\inf\bigl\{\operatorname{depth}_{K'}(R(x)):\operatorname{depth}_K(x)\ge r\bigr\}
\;\ge\; s.
\]

Consequently \((\ell,b)\) is a non-vacuous margin on a horizon
\(\bar r\) iff \(b<\ell\bar r\) and

\begin{equation}
\label{eq:pointwise}
\operatorname{depth}_{K'}(R(x))
\;\ge\;
\ell\,\operatorname{depth}_K(x)-b
\qquad
\text{for every }x\text{ with }\operatorname{depth}_K(x)\le\bar r.
\end{equation}

(The convention \(\operatorname{depth}_{K'}\ge 0\) takes care of
\(\ell r-b\le 0\).) *Proof.* If the inclusion holds for all
\(r\in[0,\bar r]\) and \(\operatorname{depth}_K(x)=r\le\bar r\), then
\(R(x)\in K'_{-(\ell r-b)_+}\). Conversely, if \eqref{eq:pointwise}
holds and \(\operatorname{depth}_K(x)\ge r\), then
\(\operatorname{depth}_{K'}(R(x))\ge \ell\operatorname{depth}_K(x)-b\ge\ell r-b\). ∎

**Definition 2.5 (cheap regularity data).** The **cheap data** of a
reset \(R:X\to X'\) relative to \((K,K')\) are

- a Lipschitz constant \(L\) of \(R\) on a neighbourhood of \(K\),
- the pair of sets \((K,K')\) up to isometry of their tubular
  neighbourhoods (in particular \(\rho(K)\), \(\rho(K')\), and whether
  \(R(\partial K)\subseteq\partial K'\)),
- the fact of \(K\)-preservation \(R(K)\subseteq K'\).

A quantity is **declared data** if it is not a function of the cheap
data alone.

---

## 3. Corrected theorem

Assume throughout that \(K_g\) is closed, \(\rho(K_g)\in(0,\infty)\),
and \(R_g(K_g)\subseteq K_{g+1}\).

**E4.Lem1(ii)\(^\ast\).**

**(A) Recorded definition is degenerate.** Every \(K\)-preserving
reset admits every recorded margin satisfying \eqref{eq:vacuous}. In
particular every family of \(K\)-preserving resets admits a uniform
recorded margin with finite \(b\) — e.g. \((\ell,b)=(1,\bar r)\) on a
common horizon \(\bar r\). The recorded sentence “no uniform
\((\ell,b)\) with \(b<\infty\) exists” is false of every such family.

**(B) Vanishing neighbourhoods do not refute non-vacuity.** Let
\(\varphi_g\) be any family that agrees with \(\lambda_g\operatorname{id}\)
only on \([0,\rho_g]\) with \(\rho_g\downarrow 0\), and is an otherwise
unspecified uniformly Lipschitz \(C^1\) bijection of \([0,1]\). For
every fixed non-vacuous pair \((\ell,b)\) there is a choice of patch
such that \((\ell,b)\) is a non-vacuous margin of all but finitely
many \(\varphi_g\). The recorded construction is not a witness for
(C).

**(C) Collapse at the inradius kills every non-vacuous pair.** There
exists a family \(\{\varphi_\lambda\}_{\lambda\in(0,1]}\) of \(C^1\)
strictly increasing bijections \([0,1]\to[0,1]\), with
\(\varphi_\lambda(0)=0\), \(\varphi_\lambda(1)=1\), and
\(\operatorname{Lip}(\varphi_\lambda)\le 4\) uniformly in \(\lambda\),
such that **no** pair \((\ell,b)\) is a non-vacuous margin of every
\(\varphi_\lambda\) on the horizon \(\bar r=1/2\). Explicitly,

\begin{equation}
\label{eq:family}
\varphi_\lambda(x)
\;=\;
\begin{cases}
\lambda x
  & 0\le x\le 1/2,\\[4pt]
\lambda x + 4(1-\lambda)\,(x-1/2)^2
  & 1/2\le x\le 1.
\end{cases}
\end{equation}

The same conclusion holds for the three numerical pairs of Finding 4
already at the single map \(\lambda=1/20\).

**(D) Declared-data.** A non-vacuous margin is not a function of the
cheap data of Definition 2.5. The family \eqref{eq:family} realises
one and the same cheap-data tuple

\[
\bigl(L=4,\; K=K'=[0,1],\; \rho=1/2,\; \varphi(\partial K)=\partial K\bigr)
\]

and realises every sufficiently small positive co-Lipschitz constant.
Hence every use of jump-margin transfer must exhibit a non-vacuous
\((\ell,b)\) for the declared reset family.

**(E) The one cheap-data derivation.** If \(R\) is co-Lipschitz of
constant \(\kappa>0\) on a neighbourhood of \(K\), i.e.

\[
\operatorname{dist}\bigl(R(x),R(y)\bigr)
\;\ge\;
\kappa\,\operatorname{dist}(x,y),
\]

and \(R\) is **exterior-preserving**,
\(R(X\setminus K)\subseteq X'\setminus K'\), then \((\kappa,0)\) is a
non-vacuous margin of \(R\) on every horizon
\(\bar r\in(0,\rho(K)]\). This is the only derivation of a non-vacuous
margin from regularity plus set geometry that the lemma admits.

**(F) Per-map existence is cheap and irrelevant.** Each single
\(\varphi_\lambda\) admits non-vacuous margins; \((\lambda,0)\) is one
(§4.4). The honesty clause is not “a margin exists for this reset”.
It is “a margin that works for the family is not readable from the
cheap data the family shares”.

Part (i) of recorded E4.Lem1 stands: a (now non-vacuous) margin is
exactly the statement that erosion depth \(r\) before the jump
becomes depth at least \(\ell r-b\) after the jump, and the deficit
\(b\) is consumed once per generation.

---

## 4. Proofs

### 4.1. Proof of (A)

Let \(R(K)\subseteq K'\) and let \(b\ge\ell\bar r\). For every
\(r\in[0,\bar r]\) one has \(\ell r-b\le 0\), so the recorded
convention turns \eqref{eq:incl} into \(R(K_{-r})\subseteq K'\). But
\(K_{-r}\subseteq K\), so this is implied by \(R(K)\subseteq K'\). ∎

On \(K=[0,1]\) with \(\bar r=1/2\), the pair \((1,1/2)\) is of this
kind. So is \((2,1)\), \((1/2,1/4)\), etc. Finite \(b\) is not the
issue. Firing is the issue.

### 4.2. Proof of (B)

Fix a non-vacuous pair \((\ell,b)\), so \(b/\ell<1/2\) on the unit
interval. Choose a cutoff \(\chi\in C^1(\mathbb R;[0,1])\) with
\(\chi\equiv 0\) on \((-\infty,0]\), \(\chi\equiv 1\) on
\([1,\infty)\), and \(0<\chi'<C\) on \((0,1)\). For
\(0<\rho<b/\ell\) define a patch by linearly transporting the graph
from \((\rho,\lambda\rho)\) to \((1,1)\) in the \(C^1\) topology
along \(\chi((x-\rho)/(1-\rho))\), with \(\lambda\in(0,1]\). The
resulting map is a \(C^1\) increasing bijection, sends \(0\) to \(0\)
and \(1\) to \(1\), and on every compact \(A\subset(0,1]\) converges
to the identity as \(\rho\downarrow 0\), uniformly in \(\lambda\le 1\),
with Lipschitz constants bounded by a number depending only on \(C\)
(the interpolant’s slope is at most \(\max(1,2)\) once \(\rho\) is
small). In particular \(\varphi_{\lambda,\rho}(1/2)\to 1/2\).

For all small \(\rho\), the only radii at which the linear piece is
known satisfy \(r\le\rho<b/\ell\), hence \(\ell r-b<0\), and
\eqref{eq:incl} is the constraint \(\varphi([r,1-r])\subseteq[0,1]\),
which holds. On the active interval \(r>b/\ell>\rho\) the map is
within \(\varepsilon\) of the identity. The identity admits every
pair with \(\ell\le 1\) and \(0\le b<\ell/2\) (because
\(K_{-r}=[r,1-r]\) is sent to itself, and \(r\ge(\ell r-b)_+\) holds
precisely when \(\ell\le 1\) or \(b\ge r(\ell-1)\); the most
demanding \(r\) is \(1/2\), giving \(b\ge(\ell-1)/2\), which is
automatic for \(\ell\le 1\)). Taking \(\varepsilon\) smaller than the
slack \(\ell\bar r-b\) of the fixed pair at \(r=1/2\) preserves the
inclusion. Thus a vanishing-neighbourhood family can be arranged so
that a prescribed non-vacuous pair **survives**. ∎

(The argument is an existence-of-patch statement. It is not a claim
that every patch works. The recorded text does not specify the patch,
so it does not specify a witness.)

### 4.3. Proof of (C): the family

The formula \eqref{eq:family} is \(C^1\): both pieces agree at
\(x=1/2\) on the value \(\lambda/2\) and on the derivative \(\lambda\).
The second piece has derivative

\[
\varphi_\lambda'(x)
\;=\;
\lambda+8(1-\lambda)\,(x-1/2)
\;\ge\;
\lambda
\;>\;
0
\quad\text{on }[1/2,1],
\]

and \(\varphi_\lambda'(1)=4-3\lambda\le 4\). On \([0,1/2]\) one has
\(\varphi_\lambda'=\lambda\le 1\). So \(\varphi_\lambda\) is strictly
increasing, \(\varphi_\lambda(0)=0\), \(\varphi_\lambda(1)=1\), and
\(\operatorname{Lip}(\varphi_\lambda)\le 4\) uniformly in \(\lambda\).
It is a \(C^1\) bijection of \([0,1]\). (It is not \(C^2\) at
\(x=1/2\); \(C^1\) is what the recorded regularity asked for.)

On \(K=[0,1]\subset\mathbb R\), \(\operatorname{depth}(x)=\min(x,1-x)\)
and \(K_{-r}=[r,1-r]\) for \(r\in[0,1/2]\). In particular
\(K_{-1/2}=\{1/2\}\) and \(\varphi_\lambda(1/2)=\lambda/2\), whose
depth is \(\lambda/2\).

Now fix any pair with \(\ell>0\), \(b\ge 0\), and \(b<\ell/2\)
(non-vacuity on this horizon). The inradius test \eqref{eq:incenter}
demands

\[
\operatorname{depth}\bigl(\varphi_\lambda(1/2)\bigr)
\;=\;
\lambda/2
\;\ge\;
\ell/2-b
\;>\;
0.
\]

Choose \(\lambda\in\bigl(0,\,\ell-2b\bigr)\). Then \(\lambda/2<\ell/2-b\)
and the inclusion fails at \(r=1/2\). Hence no non-vacuous pair works
for every \(\lambda\). ∎

The three Finding-4 rows are the case \(\lambda=1/20\), \(r=1/2\):

\[
\frac{\lambda}{2}-\bigl(\ell/2-b\bigr)
\;=\;
b-\tfrac12(\ell-\lambda)
\;=\;
\begin{cases}
-0.075 & (\ell,b)=(1,0.4),\\
-0.025 & (\ell,b)=(0.5,0.2),\\
-0.025 & (\ell,b)=(0.2,0.05).
\end{cases}
\]

A single sufficiently collapsing map already kills those pairs. The
family is needed only to kill **every** non-vacuous pair at once, and
to hold the cheap data fixed while the best co-Lipschitz constant
\(\inf\varphi_\lambda'=\lambda\) runs through \((0,1]\).

**Geometric content.** Non-vacuity makes the inradius a universal
active test: every non-vacuous pair constrains the image of the
incenter set \(K_{-\rho}\). A family that sends an incenter to the
boundary in the limit admits no uniform non-vacuous margin. That is
the whole of (C). The recorded construction failed because it never
moved the incenter.

### 4.4. Proof of (F), and the margin set of a single \(\varphi_\lambda\)

Let \(s_\lambda(r)\) be the largest \(s\) with
\(\varphi_\lambda(K_{-r})\subseteq K_{-s}\). Since \(\varphi_\lambda\)
is increasing,

\[
s_\lambda(r)
\;=\;
\min\bigl(\varphi_\lambda(r),\,1-\varphi_\lambda(1-r)\bigr).
\]

For \(r\in[0,1/2]\) one has \(\varphi_\lambda(r)=\lambda r\). The
right-end computation is

\begin{align*}
\varphi_\lambda(1-r)
&=\lambda(1-r)+4(1-\lambda)\,(1/2-r)^2,\\
1-\varphi_\lambda(1-r)-\lambda r
&=\;
1-\lambda-4(1-\lambda)\,(1/2-r)^2.
\end{align*}

For \(\lambda=1\) this is zero. For \(\lambda<1\) it equals
\((1-\lambda)\bigl(1-4(1/2-r)^2\bigr)\ge 0\), since
\(|1/2-r|\le 1/2\). Thus \(s_\lambda(r)=\lambda r\), and
\eqref{eq:pointwise} for \((\ell,b)\) becomes \(\lambda r\ge\ell r-b\)
on \([0,1/2]\), i.e.

\[
b\;\ge\;\tfrac12\,(\ell-\lambda)_+.
\]

Intersecting with non-vacuity \(b<\ell/2\) gives the margin set

\begin{equation}
\label{eq:M}
\mathcal M(\varphi_\lambda)
\;=\;
\bigl\{(\ell,b):\ell>0,\;b\ge 0,\;
\tfrac12(\ell-\lambda)_+\;\le\; b\;<\;\ell/2\bigr\}.
\end{equation}

This is nonempty for every \(\lambda>0\): \((\lambda,0)\) lies in it,
and so does every pair with \(\ell>\lambda\) and
\(b=(\ell-\lambda)/2\). That is (F).

The intersection over the family is empty. If \((\ell,b)\) belonged
to every \(\mathcal M(\varphi_\lambda)\), then for every
\(\lambda\in(0,\ell)\) one would have \(b\ge(\ell-\lambda)/2\). Sending
\(\lambda\downarrow 0\) yields \(b\ge\ell/2\), contradicting
non-vacuity. This is (C) again, read in the \((\ell,b)\)-plane.

### 4.5. Proof of (D): Lipschitz is the wrong inequality

The family \eqref{eq:family} shares \(L=4\), \(K=K'=[0,1]\),
\(\rho=1/2\), and \(\varphi(\{0,1\})=\{0,1\}\). By (C) these data do
not determine a non-vacuous margin. That is already (D). The
structural reason is independent of the witness and is recorded
because it is what the honesty clause is actually about.

Let \(R\) be \(L\)-Lipschitz near \(K\) and suppose
\(R(\partial K)\subseteq\partial K'\). For \(x\in K\) pick
\(y\in\partial K\) with \(\operatorname{dist}(x,y)=\operatorname{depth}_K(x)\).
Then

\[
\operatorname{dist}\bigl(R(x),R(y)\bigr)
\;\le\;
L\,\operatorname{depth}_K(x).
\]

Since \(R(y)\in\partial K'\),

\[
\operatorname{depth}_{K'}(R(x))
\;\le\;
\operatorname{dist}\bigl(R(x),\partial K'\bigr)
\;\le\;
\operatorname{dist}\bigl(R(x),R(y)\bigr)
\;\le\;
L\,\operatorname{depth}_K(x).
\]

Lipschitz plus boundary-to-boundary therefore yields

\begin{equation}
\label{eq:wrongway}
\operatorname{depth}_{K'}(R(x))
\;\le\;
L\,\operatorname{depth}_K(x):
\end{equation}

image depth cannot **grow** faster than \(L\). A non-vacuous
jump-margin is a lower bound
\(\operatorname{depth}_{K'}(R(x))\ge \ell\operatorname{depth}_K(x)-b\).
An upper bound on a nonnegative quantity does not produce a positive
lower bound. The cheap data can at most certify that depth is not
amplified; they are silent on how far it may collapse. The family
\(\varphi_\lambda\) saturates that silence: \eqref{eq:wrongway} holds
with room (\(\lambda\le 4\)), and the lower constant \(\lambda\) is
not visible to \(L\).

Boundary margins of \(K\) itself (inradius, reach, tubular radius)
are properties of the **sets**, not of the reset. They are held fixed
in \eqref{eq:family}. They do not enter the lower bound either.

### 4.6. Proof of (E): co-Lipschitz plus exterior

Let \(R\) satisfy \(\operatorname{dist}(R(x),R(y))\ge\kappa\operatorname{dist}(x,y)\)
and \(R(X\setminus K)\subseteq X'\setminus K'\). For \(x\in K\),

\begin{align*}
\operatorname{depth}_{K'}(R(x))
&=\operatorname{dist}\bigl(R(x),\,X'\setminus K'\bigr)\\
&\ge\operatorname{dist}\bigl(R(x),\,R(X\setminus K)\bigr)\\
&\ge\kappa\,\operatorname{dist}(x,\,X\setminus K)
=\kappa\,\operatorname{depth}_K(x),
\end{align*}

the first inequality because \(R(X\setminus K)\) sits inside
\(X'\setminus K'\). By Lemma 2.4, \((\kappa,0)\) satisfies
\eqref{eq:pointwise}. Non-vacuity is \(0<\kappa\bar r\), i.e.
\(\kappa>0\) and \(\bar r>0\), which is the standing hypothesis. ∎

On the family \eqref{eq:family} this recovers exactly
\((\lambda,0)\in\mathcal M(\varphi_\lambda)\): each single map is
co-Lipschitz of constant \(\inf\varphi_\lambda'=\lambda\), and no
**uniform** positive \(\kappa\) exists for the whole family.

Exterior-preservation is not optional. Co-Lipschitz alone controls
distances to the image of the complement, not distances to the
complement. If \(R\) folds the complement into \(K'\), image depth
can be large for a reason that has nothing to do with preimage depth,
or small if the fold lands near \(\partial K'\). The lemma does not
claim a derivation in that case.

---

## 5. Consumption by E4.Thm2

Recorded E4.Thm2 feeds \((\ell,b)\) into \(r_{g+1}=\ell r_g-b\) and
inducts on strong invariance of \(K_{g,-r_g}\). Two consequences of
the present correction, neither of which softens Thm2.

**Vacuous pairs make the induction silent after one jump.** If
\(b\ge\ell\bar r_0\) and \(r_0\le\bar r_0\), then
\(r_1=\ell r_0-b\le 0\). Under the recorded convention the image is
read as \(K_1\) (erosion depth \(0\)), and the induction at a
declared positive depth has no hypothesis. The corrected budget
criterion (`E4_Thm2_budget_solvability.md`, E4.Thm2-Budget\(^\ast\))
already says the theorem asserts nothing when some \(r_g<0\).
Non-vacuity is the matching guard on the pair that enters the
recursion: it is the statement that the first jump, at least, is
asked to deliver a positive depth when the preimage is at horizon.

**A declared pair must be a pair that actually works for the family.**
Exhibiting \((\ell,b)=(1,1/2)\) on \([0,1]\) satisfies the recorded
definition and satisfies no useful instance of Thm2. Exhibiting
\((\lambda,0)\) for a single \(\varphi_\lambda\) is legitimate and
gives the recursion \(r_{g+1}=\lambda r_g\), which is nonnegative
for all \(g\) whenever \(r_0\ge 0\). Exhibiting a single pair for the
whole family \(\{\varphi_\lambda\}_{\lambda\in(0,1]}\) is impossible
by (C), and that impossibility is the content of “too thin a reset,
uniformly in the cheap data”.

The invariance induction of E4.Thm2 is untouched. It consumes a
non-vacuous margin and a solvable nonnegative budget. Both
hypotheses are now what they were advertised to be.

---

## 6. Dimension and embedding

The witness is one-dimensional because one dimension suffices to
refute a claimed derivation from cheap data: those data are available
in one dimension, and the derivation is claimed for general metric
state spaces. The same family embeds in any dimension. If
\(K= [0,1]\times L\) for compact \(L\subset\mathbb R^{n-1}\) with
positive inradius, the map \(\varphi_\lambda\times\operatorname{id}_L\)
is uniformly Lipschitz, preserves the product boundary in the first
factor, and sends the incenter slice \(\{1/2\}\times L_{-r}\) to
depth at most \(\lambda/2\) in that factor. The inradius test still
fails for every non-vacuous pair once \(\lambda\) is small. Nothing
in E4 requires the extra dimensions.

---

## 7. What this does to the E4 stack

| Recorded object | Disposition |
|---|---|
| Definition of \((\ell,b)\) without non-vacuity | **Degenerate.** Replace by Definition 2.3. |
| “No uniform \((\ell,b)\) with \(b<\infty\) exists” | **False** of every \(K\)-preserving family. |
| Vanishing-neighbourhood family as witness | **Not a witness**, even after non-vacuity (§4.2). |
| Declared-data thesis (margin not implied by Lip + boundary) | **True**, once non-vacuous. Proved as (C)–(D). Strengthened: Lipschitz gives the opposite inequality. |
| E4.Lem1(i) transfer | **True** (definitional), now with a pair that fires. |
| E4.Thm2 induction | Untouched, provided it consumes a non-vacuous pair and a solvable budget. |
| E4.Lem1(ii)\(^\ast\) | **Proved** in this file. |

No part of the declared-data thesis is demoted to conjecture. The
false sentence was an overstatement of a true non-derivability
claim, caused by a definition that admitted a trivial pair. The
repair is to refuse the trivial pair, replace the witness, and keep
the claim.

---

## 8. Claim-status

- Recorded E4.Lem1(ii), as a statement that no finite uniform
  \((\ell,b)\) exists for the displayed family: **false**.
- Recorded vanishing-neighbourhood construction as a refutation of
  non-vacuous margins: **false**.
- Non-vacuous declared-data theorem E4.Lem1(ii)\(^\ast\): **proved**.
- Derivation of a non-vacuous margin from Lipschitz + boundary
  geometry alone: **false**, not a conjecture (family \eqref{eq:family}).
- Derivation from co-Lipschitz + exterior-preservation: **true**,
  and the pair is \((\kappa,0)\).

No part of this file modifies the repository.

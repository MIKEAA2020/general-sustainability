# B6.Thm1(1) — Strict substitution stability under MFCQ, corrected

**This file is not a repository edit.** It elevates
`batch 2/04_open_problems/B_TIER_BRIDGES.md`, B6 part (1), against
`batch 4/PROOF_REAUDIT.md` Finding 2.

Part (2) of the recorded B6 (Clarke certificate) is not treated here.
One proof this turn.

---

## 0. The recorded claim is false

**Recorded statement.** If MFCQ holds at every nearby point, then a
direction \(d\) is a feasible direction at \(\bar x\) **if and only if**
it is a feasible direction at every nearby \(x\), and the projection of
the feasible set \(\mathcal G\) onto the pathway coordinate is locally
constant.

**Neither clause is true.**

**Witness (PROOF_REAUDIT Finding 2).** Let
\(\mathcal G=\{(x,y):y\ge x^2\}\), i.e. \(g(x,y)=x^2-y\le 0\),
\(\bar x=(0,0)\), \(d=(1,0)\). Then \(\nabla g=(2x,-1)\ne 0\) everywhere,
so MFCQ holds at every point of \(\partial\mathcal G\).

- **Bouligand / linearized reading.**
  \(\langle\nabla g(0,0),d\rangle=0\), so \(d\) lies in the linearized
  cone at \(\bar x\). The same inner product at \((a,a^2)\) is \(2a\),
  which is \(>0\) for \(a>0\): \(d\) is *not* linearized-feasible at
  nearby boundary points. The linearized cone rotates.
- **Geometric ray reading.** \(\bar x+td=(t,0)\notin\mathcal G\) for all
  \(t\ne 0\). So \(d\) is not even a feasible *ray* at \(\bar x\). It *is*
  a Bouligand tangent: \((t,t^2)/t=(1,t)\to(1,0)\). Tangent-cone
  membership of a fixed \(d\) is still not locally constant (same table).
- **Projection clause.** The projection of \(\mathcal G\) onto the
  \(x\)-axis is \(\mathbb R\) globally, but the projection of
  \(\mathcal G\cap B(\bar x,\varepsilon)\) onto a line in direction \(d\)
  is a half-interval whose endpoint moves with the contact geometry. The
  recorded “locally constant projection” has no correct reading on this
  set.

MFCQ gives lower semicontinuity of the *set* \(\mathcal G\) and
outer-semicontinuity of the linearized cone. It does **not** freeze
membership of a single vector \(d\) that rides the boundary of the cone.

The recorded “iff” is therefore irreparably false. It is not a conjecture.

---

## 1. What the programme actually needs

B6 is the nonlinear stand-in for Farkas (E3.C2, E7.Thm2). In the linear
theory, a direction is either a feasible substitution everywhere or is
separated by a covector everywhere. Nonlinearly the global dichotomy
fails, but a **local, strict** dichotomy survives and is stable:

- either \(d\) *strictly* enters \(\mathcal G\) along the ray
  \(\bar x+td\), and this persists in a ball of explicit radius, or
- \(d\) is blocked to first order at \(\bar x\), and this too persists
  on the active face.

That is the linear Farkas alternative, localized at an MFCQ point, with
a quantitative radius. It is the strongest correct local classification.
The recorded claim tried to say this for *non-strict* directions and
overshot.

---

## 2. Objects

Let \(g\in C^1(\mathbb R^n,\mathbb R^p)\),
\(\mathcal G=\{x:g(x)\le 0\}\). Write
\(A(x)=\{i:g_i(x)=0\}\) for the active set,
\(I(x)=\{i:g_i(x)<0\}\) for the inactive set.

**Definition 2.1 (MFCQ).** MFCQ holds at \(x\in\mathcal G\) if there
exists \(v\in\mathbb R^n\) such that
\(\langle\nabla g_i(x),v\rangle<0\) for every \(i\in A(x)\).
(If some equalities are present they are required to have linearly
independent gradients; this file is written for inequalities, which is
the substitution setting. Equalities are a parenthetical at the end.)

**Definition 2.2 (strict linearized substitution).** A direction
\(d\in\mathbb R^n\) is a **strict substitution** at \(x\in\mathcal G\)
if
\[
\eta(x,d)
\;:=\;
-\max_{i\in A(x)}\langle\nabla g_i(x),d\rangle
\;>\;0
\]
when \(A(x)\ne\emptyset\), and \(\eta(x,d):=+\infty\) when
\(A(x)=\emptyset\). Equivalently,
\(\langle\nabla g_i(x),d\rangle\le-\eta(x,d)<0\) on the active face.

**Definition 2.3 (ray feasibility).** \(d\) is **ray-feasible** at
\(x\in\mathcal G\) if there exists \(t_0>0\) such that
\(x+td\in\mathcal G\) for all \(t\in[0,t_0]\).

Strict substitution will be shown to imply ray feasibility, with a
radius controlled by \(\eta\) and the \(C^1\) modulus of \(\nabla g\).

---

## 3. Corrected theorem

**B6.Thm1(1)\(^\ast\) (strict substitution is open and ray-feasible).**
Let \(\bar x\in\mathcal G\) and \(d\in\mathbb R^n\) with
\(\|d\|=1\). Assume \(g\in C^1\), and write \(\omega\) for a local
modulus of continuity of \(\nabla g\) on a closed ball
\(\overline B(\bar x,R)\):
\(\|\nabla g_i(x)-\nabla g_i(y)\|\le\omega(\|x-y\|)\) for
\(\|x-\bar x\|\le R\), \(\|y-\bar x\|\le R\), all \(i\), with
\(\omega(r)\downarrow 0\) as \(r\downarrow 0\).

1. **Ray lemma.** If \(\eta(\bar x,d)=\eta>0\), there exists
   \(t_\star>0\), constructed below, such that
   \(\bar x+td\in\operatorname{int}\mathcal G\) for all
   \(t\in(0,t_\star]\). In particular \(d\) is ray-feasible at
   \(\bar x\).
2. **Stability of the strict class.** There exists \(r_\star>0\),
   constructed below, such that every
   \(x\in\mathcal G\cap\overline B(\bar x,r_\star)\) satisfies
   \(\eta(x,d)\ge\eta/2>0\). Thus \(d\) is a strict substitution at
   every feasible point near \(\bar x\), and by (1) is ray-feasible
   there.
3. **Stability of MFCQ.** The set of points of \(\mathcal G\) at which
   MFCQ holds is relatively open in \(\mathcal G\). In particular, if
   MFCQ holds at \(\bar x\) then it holds throughout
   \(\mathcal G\cap\overline B(\bar x,r)\) for some \(r>0\).
4. **Local classification.** On \(\mathcal G\cap\overline B(\bar x,r_\star)\)
   the dichotomy
   \[
   d\text{ is a strict substitution}
   \qquad\text{versus}\qquad
   \max_{i\in A(x)}\langle\nabla g_i(x),d\rangle\ge 0
   \]
   is well-defined, mutually exclusive, and the first side is open
   relative to \(\mathcal G\). It is **not** claimed that the second
   side is open, nor that non-strict tangency is stable.

No “locally constant projection of \(\mathcal G\)” is asserted.

---

## 4. Proof

Write \(A=A(\bar x)\), \(I=I(\bar x)\). If \(A=\emptyset\) then
\(g(\bar x)<0\), so \(\bar x\) is an interior point: both (1) and (2)
hold on a ball in \(\operatorname{int}\mathcal G\), and (3) is vacuous.
Assume \(A\ne\emptyset\), \(\eta=\eta(\bar x,d)>0\).

### 4.1. Inactive constraints stay inactive

Let
\[
\delta
\;:=\;
\min_{j\in I}\bigl(-g_j(\bar x)\bigr)
\;>\;0
\]
(or \(\delta=+\infty\) if \(I=\emptyset\)). Continuity of \(g\) gives
\(r_{\mathrm{in}}\in(0,R]\) such that
\(\|x-\bar x\|\le r_{\mathrm{in}}\) implies
\(g_j(x)\le-\delta/2<0\) for all \(j\in I\). On that ball,
\(A(x)\subseteq A\).

### 4.2. Ray lemma

For \(i\in A\) and \(t\in(0,R]\),
\[
g_i(\bar x+td)
\;=\;
g_i(\bar x)
+\int_0^t\langle\nabla g_i(\bar x+sd),d\rangle\,ds
\;=\;
\int_0^t\Bigl(
\langle\nabla g_i(\bar x),d\rangle
+\langle\nabla g_i(\bar x+sd)-\nabla g_i(\bar x),d\rangle
\Bigr)ds.
\]
The first inner product is \(\le-\eta\). The second is at most
\(\omega(t)\). Hence
\[
g_i(\bar x+td)
\;\le\;
t\bigl(-\eta+\omega(t)\bigr).
\]
Choose \(t_1\in(0,r_{\mathrm{in}}]\) with \(\omega(t_1)\le\eta/2\). Then
for \(t\in(0,t_1]\),
\(g_i(\bar x+td)\le -(\eta/2)\,t<0\) for all \(i\in A\), and
\(g_j(\bar x+td)<0\) for \(j\in I\) by 4.1. So
\(\bar x+td\in\operatorname{int}\mathcal G\). Set \(t_\star:=t_1\).

### 4.3. Stability of \(\eta(\,\cdot\,,d)\)

Let \(x\in\mathcal G\cap\overline B(\bar x,r)\) with
\(r\le r_{\mathrm{in}}\). Then \(A(x)\subseteq A\), so
\[
\eta(x,d)
\;=\;
-\max_{i\in A(x)}\langle\nabla g_i(x),d\rangle
\;\ge\;
-\max_{i\in A}\langle\nabla g_i(x),d\rangle
\]
(the maximum over a smaller set cannot be larger; if \(A(x)=\emptyset\)
then \(\eta(x,d)=+\infty\)). For each \(i\in A\),
\[
\langle\nabla g_i(x),d\rangle
\;\le\;
\langle\nabla g_i(\bar x),d\rangle+\omega(r)
\;\le\;
-\eta+\omega(r).
\]
Choose \(r_\star\in(0,r_{\mathrm{in}}]\) with \(\omega(r_\star)\le\eta/2\).
Then \(\eta(x,d)\ge\eta/2>0\). Apply 4.2 at the point \(x\)
(the same modulus \(\omega\) works on \(\overline B(\bar x,R)\)) to
conclude ray feasibility of \(d\) at \(x\).

### 4.4. Stability of MFCQ

MFCQ at \(\bar x\) is the existence of some \(v\), \(\|v\|=1\), with
\(\eta(\bar x,v)>0\). Part (2) applied to this \(v\) (not to the
substitution direction \(d\)) yields \(\eta(x,v)\ge\eta(\bar x,v)/2>0\)
on a relative neighbourhood of \(\bar x\) in \(\mathcal G\). That is
MFCQ at those \(x\).

### 4.5. Classification

On \(\mathcal G\cap\overline B(\bar x,r_\star)\), either
\(\eta(x,d)>0\) or \(\eta(x,d)\le 0\). The first side is exactly
strict substitution; it is relatively open by (2). The two sides are
exclusive by definition. The second side contains all non-strict
tangencies (including the parabola’s \(d=(1,0)\) at the origin) and
is **not** asserted to be open. ∎

---

## 5. Quantitative radius

If \(\nabla g\) is Lipschitz of constant \(\Lambda\) on
\(\overline B(\bar x,R)\), then \(\omega(r)=\Lambda r\), and the
choices in 4.2–4.3 may be taken as
\[
t_\star
\;=\;
r_\star
\;=\;
\min\Bigl(R,\; r_{\mathrm{in}},\; \frac{\eta}{2\Lambda}\Bigr)
\]
(any positive number if \(\Lambda=0\)). This is the explicit ball on
which a substitution direction with margin \(\eta\) cannot be lost.

In the linear Farkas setting \(\Lambda=0\), \(\omega\equiv 0\),
\(A(\,\cdot\,)\) is globally constant on faces, and strict feasibility
of \(d\) at one relative-interior face point is global on that face —
the classical dichotomy, recovered rather than approximated.

---

## 6. Equalities, briefly

If some constraints are equalities \(h(x)=0\) with \(\nabla h_i(\bar x)\)
linearly independent and MFCQ in the remaining inequalities, the same
argument applies in the tangent space \(\ker Dh(\bar x)\), after
replacing the raw ray \(\bar x+td\) by a \(C^1\) correction
\(\bar x+td+O(t^2)\) that holds the equalities (Lyapunov–Schmidt /
implicit function theorem). Strict inequality on the inequalities is
again an open condition and persists. Non-strict tangency still
rotates. This is the only extra ingredient; it is not needed for the
pure-inequality substitution problem B6 states.

---

## 7. What this does to the B6 stack

| Recorded object | Effect |
|---|---|
| B6.Thm1(1) as written | **False.** Replace by B6.Thm1(1)\(^\ast\). |
| “Projection of \(\mathcal G\) is locally constant” | **False.** Dropped. |
| B6.Thm1(2) Clarke certificate | Untouched this turn. |
| E3.C2 / E7.Thm2 cross-references | They may cite the *strict* local alternative, not the recorded iff. Linear Farkas remains the global special case \(\Lambda=0\). |

The classification is sharper than the recorded one on the side that
matters for substitution: a direction that *strictly* pays a moiety
deficit continues to pay it throughout an explicit ball. The recorded
claim failed because it treated grazing directions as if they were
strict.

---

## 8. Claim-status

- Recorded B6.Thm1(1): **false**.
- B6.Thm1(1)\(^\ast\): **proved** in this file.
- Non-strict / Bouligand-only stability: **false**, not a conjecture
  (same witness).

No part of this file modifies the repository.

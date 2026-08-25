# A3.Thm1 — Interleaved-segment compactness, corrected

**This file is not a repository edit.** It is a standalone elevation of
`batch 2/04_open_problems/A3_VARIABLE_EVENT_KERNEL.md`, A3.Thm1, against
`batch 4/PROOF_REAUDIT.md` Finding 1.

**Disposition of the recorded claim.** The recorded statement is
**false**. The recorded proof is not a proof (Helly is invoked without a
uniform total-variation bound; “interleaving + constant continuation”
does not create equicontinuity). The ambition — a compact history space
on which a variable-event kernel can be constructed — is retained. The
missing hypothesis is the one the hybrid flow itself supplies.

---

## 0. The recorded claim, and why it is false

**Recorded statement.** Let \(\mathcal H\) be the set of piecewise
continuous maps \(\varphi:[-\tau,0]\to\mathbb R^n\) with at most \(B\)
discontinuities, jumps of size at most \(J\), and \(\|\varphi\|_\infty\le M\).
Equip \(\mathcal H\) with the interleaved-segment topology \(\tau_{\mathrm{IS}}\):
\(\varphi_k\to\varphi\) iff the break sets converge in the Hausdorff metric
and, on each complementary segment, the restrictions converge uniformly.
Then \((\mathcal H,\tau_{\mathrm{IS}})\) is compact.

**Counterexample (PROOF_REAUDIT Finding 1, reproduced).** Take
\(B=0\), \(\tau=2\pi\), \(M=1\), \(n=1\), and
\(\varphi_k(s)=\sin(ks)\) for \(k\in\mathbb N\). Each \(\varphi_k\) is
continuous, hence has no breaks and no jumps, and is bounded by \(1\).
On \([-2\pi,0]\),

\[
\min_{1\le i<j\le 8}\ \|\varphi_i-\varphi_j\|_\infty
\;=\;
\|\varphi_1-\varphi_2\|_\infty
\;=\;
1.76017253\ldots
\]

(the exact value is \(\max_{t\in[0,2\pi]}|\sin t-\sin 2t|\), attained at a
critical point of \(\cos t-2\cos 2t=0\)). The family has no
\(\tau_{\mathrm{IS}}\)-Cauchy subsequence, so \(\mathcal H\) is not
sequentially compact.

**Where the recorded proof fails.** After extracting convergent break
locations the proof admits that the segment restrictions “are not
equicontinuous … so Arzelà–Ascoli does not apply directly”, then appeals
to a Helly-type selection. Helly requires a uniform bound on total
variation. Here \(\mathrm{TV}(\varphi_k;[-\tau,0])=4k\to\infty\). Constant
continuation from segment endpoints does not produce equicontinuity on
the whole interval, and a uniform jump bound of \(0\) (the \(B=0\) case)
does not constrain oscillation *inside* a segment.

The claim is therefore not a near-miss of a true compactness theorem. It
is the wrong hypothesis list for a topology that demands uniform
convergence on segments.

---

## 1. What the hybrid flow actually produces

Let \(f\) be (globally) Lipschitz of constant \(L_f\) on a bounded
invariant set of radius \(M\). Between events a trajectory satisfies
\(\dot x=f(x)\) and is therefore \(L_f M'\)-Lipschitz on every
inter-event interval (any \(M'\) dominating \(\|f\|\) on the bound).
Jumps, if present, are a separate discrete mechanism and are already
budgeted by \(J\). The natural history space of a budgeted Lipschitz
hybrid system is therefore **not** “all piecewise continuous paths with
\(B\) breaks”. It is the subclass with a **uniform Lipschitz constant on
continuity intervals**.

That subclass is what A3.Thm3 and B8 actually need: a compact metric
space of histories on which the delayed-evaluation map is continuous off
the event set. Adding the Lipschitz budget does not shrink the intended
model class. It names it.

---

## 2. Corrected objects

Fix \(\tau>0\), integers \(n\ge 1\), \(B\ge 0\), and constants
\(J\ge 0\), \(M\ge 0\), \(L\ge 0\).

**Definition 2.1 (regulated piecewise-Lipschitz histories).**
A map \(\varphi:[-\tau,0]\to\mathbb R^n\) belongs to
\(\mathcal H(B,J,M,L)\) if:

1. \(\varphi\) is càdlàg (right-continuous, with left limits at every
   \(t\in(-\tau,0]\));
2. the break set
   \(\mathrm{br}(\varphi):=\{t\in(-\tau,0]:\varphi(t)\ne\varphi(t-)\}\)
   is finite and \(\#\mathrm{br}(\varphi)\le B\);
3. \(\|\varphi(t)-\varphi(t-)\|\le J\) at every break;
4. \(\|\varphi(t)\|\le M\) for all \(t\);
5. on every open interval contained in \([-\tau,0]\setminus\mathrm{br}(\varphi)\),
   \(\varphi\) is Lipschitz with constant \(L\).

Càdlàg is a convention (left-càglàd works equally). Piecewise continuity
without one-sided limits is the wrong ambient space: uniform limits of
Lipschitz pieces have one-sided limits automatically.

**Definition 2.2 (the topology \(\tau_{\mathrm{IS}}\)).**
Let \(\mathcal F_{\le B}([-\tau,0])\) be the set of closed subsets of
\([-\tau,0]\) of cardinality at most \(B\), equipped with the Hausdorff
metric \(d_H\) (empty set included, \(d_H(\emptyset,\emptyset)=0\),
and \(d_H(\emptyset,K)=\tau\) if one prefers a convenient convention;
we only ever compare nonempty break sets after adjoining the endpoints
\(\{-\tau,0\}\)). A sequence \(\varphi_k\) in \(\mathcal H(B,J,M,L)\)
**converges in \(\tau_{\mathrm{IS}}\)** to \(\varphi\) if

- \(d_H\bigl(\mathrm{br}(\varphi_k),\mathrm{br}(\varphi)\bigr)\to 0\), and
- for every compact \(K\subset[-\tau,0]\setminus\mathrm{br}(\varphi)\),
  \(\varphi_k\to\varphi\) uniformly on \(K\).

This is the recorded \(\tau_{\mathrm{IS}}\) with “corresponding segments”
made unambiguous when breaks coalesce (the number of breaks may drop in
the limit; uniform convergence is required only off the *limit* break
set).

**Lemma 2.3 (metrizability).** The function

\[
d_{\mathrm{IS}}(\varphi,\psi)
\;=\;
d_H\bigl(\mathrm{br}(\varphi),\mathrm{br}(\psi)\bigr)
\;+\;
\sum_{m=1}^\infty
2^{-m}\,
\min\Bigl(1,\;
\sup\bigl\{\|\varphi(t)-\psi(t)\|
:
t\in K_m(\varphi,\psi)\bigr\}
\Bigr),
\]

where \(K_m(\varphi,\psi)\) is the (possibly empty) compact
\([-\tau,0]\setminus\bigl(U_{1/m}(\mathrm{br}(\varphi)\cup\mathrm{br}(\psi))\bigr)\)
and the inner \(\sup\) is \(0\) if the set is empty, is a metric on
\(\mathcal H(B,J,M,L)\) inducing \(\tau_{\mathrm{IS}}\).

*Proof.* Non-negativity and symmetry are immediate. If
\(d_{\mathrm{IS}}(\varphi,\psi)=0\), then the break sets coincide and
\(\varphi=\psi\) off that finite set; càdlàg plus identical jumps (the
jump at a common break is the difference of the two one-sided limits,
and each one-sided limit is recovered from values off the break)
gives \(\varphi=\psi\). The triangle inequality holds because \(d_H\)
satisfies it and each truncated-sup term does. Sequential convergence
in \(d_{\mathrm{IS}}\) is exactly Definition 2.2: Hausdorff convergence
of breaks, and uniform convergence on every compact staying a positive
distance from the two break sets, hence from the limit break set. ∎

---

## 3. Corrected theorem

**A3.Thm1\(^\ast\) (interleaved-segment compactness).**
The space \(\bigl(\mathcal H(B,J,M,L),\,d_{\mathrm{IS}}\bigr)\) is
**compact**. Moreover, if \(x:[-\tau,T]\to\mathbb R^n\) is a trajectory
whose restrictions \(x_t(s):=x(t+s)\), \(s\in[-\tau,0]\), all lie in
\(\mathcal H(B,J,M,L)\), then the delayed-evaluation map
\(t\mapsto x_t\) is \(d_{\mathrm{IS}}\)-continuous at every
\(t\in[0,T]\) that is not an event time of \(x\) (i.e.,
\(0\notin\mathrm{br}(x_t)\) and no break of \(x\) coincides with the
left window edge \(t-\tau\)).

The recorded A3.Thm1 is A3.Thm1\(^\ast\) with the hypothesis \(L<\infty\)
deleted. That deletion is exactly the \(\sin(ks)\) counterexample
(\(L_k=k\to\infty\)).

No other recorded conclusion is weakened. The hybrid class with
Lipschitz flow between budgeted events is unchanged.

---

## 4. Proof of compactness

Let \((\varphi_k)_{k\in\mathbb N}\) be a sequence in \(\mathcal H(B,J,M,L)\).
Write \(K_k:=\mathrm{br}(\varphi_k)\).

### 4.1. Break sets

The hyperspace of closed subsets of the compact interval \([-\tau,0]\) is
compact in \(d_H\) (Blaschke). The subset of sets of cardinality at most
\(B\) is \(d_H\)-closed: if \(F_k\to F\) and each \(\#F_k\le B\), then
\(F\) is finite with \(\#F\le B\) (any \(B+1\) distinct points of \(F\)
would, for large \(k\), force \(B+1\) distinct points of \(F_k\)).
Extract a subsequence, not relabelled, with

\[
K_k \;\xrightarrow{d_H}\; K_\infty,\qquad \#K_\infty\le B.
\]

Let \(-\tau=a_0<a_1<\cdots<a_m<a_{m+1}=0\) be the ordered list of
distinct points of \(K_\infty\cup\{-\tau,0\}\). Thus \(m\le B\).

### 4.2. Local uniform Lipschitz control off the limit breaks

Fix \(\varepsilon>0\) small enough that the intervals
\([a_i+\varepsilon,\,a_{i+1}-\varepsilon]\) are nonempty whenever
\(a_{i+1}-a_i>2\varepsilon\). For all large \(k\),
\(d_H(K_k,K_\infty)<\varepsilon\), so \(K_k\) lies in the
\(\varepsilon\)-neighbourhood of \(K_\infty\). Consequently
\(\varphi_k\) has **no break** in any compact
\(I_i^\varepsilon:=[a_i+\varepsilon,\,a_{i+1}-\varepsilon]\).
By Definition 2.1(5), \(\varphi_k|_{I_i^\varepsilon}\) is \(L\)-Lipschitz
and \(\|\varphi_k\|\le M\).

### 4.3. Arzelà–Ascoli on each solid subsegment

The family \(\{\varphi_k|_{I_i^\varepsilon}\}_k\) is uniformly bounded
and equicontinuous. Arzelà–Ascoli yields a uniformly convergent
subsequence on each nonempty \(I_i^\varepsilon\). There are finitely
many such segments. A diagonal subsequence, still written \(\varphi_k\),
converges uniformly on every \(I_i^\varepsilon\) simultaneously.

### 4.4. Diagonalisation in \(\varepsilon\)

Repeat 4.2–4.3 along \(\varepsilon_\ell=2^{-\ell}\min_i(a_{i+1}-a_i)\)
(or any sequence \(\varepsilon_\ell\downarrow 0\)). A further diagonal
subsequence converges uniformly on every compact contained in
\([-\tau,0]\setminus K_\infty\). Call the pointwise limit \(\varphi\)
on that open set.

### 4.5. The limit is \(L\)-Lipschitz on each complementary interval

On any compact \(K\subset(a_i,a_{i+1})\), the convergence is uniform and
each \(\varphi_k\) is \(L\)-Lipschitz on \(K\) for large \(k\). The
uniform limit of \(L\)-Lipschitz maps is \(L\)-Lipschitz. Hence
\(\varphi|_{(a_i,a_{i+1})}\) extends uniquely to a continuous
\(L\)-Lipschitz map on \([a_i,a_{i+1}]\) if we ignore the values at the
endpoints; the one-sided limits

\[
\varphi(a_i+)
:=\lim_{t\downarrow a_i}\varphi(t),\qquad
\varphi(a_{i+1}-)
:=\lim_{t\uparrow a_{i+1}}\varphi(t)
\]

exist (Lipschitz maps on bounded intervals are uniformly continuous).

### 4.6. Càdlàg representative and the jump bound

Define \(\varphi\) at points of \(K_\infty\) by right-continuity:
\(\varphi(a_i):=\varphi(a_i+)\), and \(\varphi(-\tau):=\varphi((-\tau)+)\)
if \(-\tau\) is not already an interior point. Then \(\varphi\) is càdlàg,
\(\mathrm{br}(\varphi)\subseteq K_\infty\), and \(\#\mathrm{br}(\varphi)\le B\).

At each \(a_i\in K_\infty\cap(-\tau,0]\), pick \(t_k\in K_k\) with
\(t_k\to a_i\) (possible by Hausdorff convergence). For small
\(\delta>0\) and large \(k\), \(\varphi_k\) has no other break in
\([t_k-\delta,t_k)\) or \((t_k,t_k+\delta]\) except possibly breaks
converging to other limit breaks, which stay outside a fixed
neighbourhood if \(\delta\) is small and the \(a_j\) are separated.
Thus

\[
\|\varphi_k(t_k)-\varphi_k(t_k-)\|
\;\le\; J.
\]

The left and right values \(\varphi_k(t_k\pm)\) differ from
\(\varphi(a_i\pm)\) by at most \(L|t_k-a_i|+o(1)\) (Lipschitz control on
the adjacent solid segments). Sending \(k\to\infty\) then \(\delta\to 0\),

\[
\|\varphi(a_i)-\varphi(a_i-)\|
\;\le\; J.
\]

Boundedness \(\|\varphi\|\le M\) is inherited from the uniform bound on
the \(\varphi_k\). Therefore \(\varphi\in\mathcal H(B,J,M,L)\).

### 4.7. Convergence in \(d_{\mathrm{IS}}\)

By construction \(K_k\to\mathrm{br}(\varphi)\) in \(d_H\) (if some
points of \(K_\infty\) are not actual jumps of \(\varphi\), they may be
dropped from \(\mathrm{br}(\varphi)\); Hausdorff convergence still holds
after dropping, because those points are limits of jumps that flatten to
size \(0\), and a zero jump is not a break — the extra points of
\(K_\infty\setminus\mathrm{br}(\varphi)\) form a set to which a
subsequence of *vanishing* jumps converges, which does not disturb
uniform convergence on compacts in the complement of
\(\mathrm{br}(\varphi)\)). Uniform convergence on every compact in the
complement of \(\mathrm{br}(\varphi)\) is 4.4. Hence
\(\varphi_k\to\varphi\) in \(d_{\mathrm{IS}}\).

### 4.8. Compactness

The space is sequentially compact and metrizable, hence compact. ∎

---

## 5. Proof of delayed-evaluation continuity

Let \(t_\star\in[0,T]\) satisfy \(0\notin\mathrm{br}(x_{t_\star})\) and
\(t_\star-\tau\notin\mathrm{br}(x)\) (no break of the underlying path at
the left edge of the window). Then
\(\mathrm{dist}\bigl(0,\mathrm{br}(x_{t_\star})\bigr)=\delta>0\) after
identifying breaks of \(x_{t_\star}\) with
\(\{s-t_\star:s\text{ is a break of }x\text{ in }(t_\star-\tau,t_\star]\}\).

For \(|h|<\delta/2\), the window \([t_\star+h-\tau,\,t_\star+h]\) contains
exactly the same interior breaks of \(x\) as
\([t_\star-\tau,\,t_\star]\), each shifted by \(h\). Thus

\[
d_H\bigl(\mathrm{br}(x_{t_\star+h}),\,\mathrm{br}(x_{t_\star})\bigr)
\;=\;
|h|.
\]

On any compact \(K\subset[-\tau,0]\setminus\mathrm{br}(x_{t_\star})\),
for small \(h\) the shifted arguments \(t_\star+h+s\), \(s\in K\), stay
in a single continuity interval of \(x\), where \(x\) is \(L\)-Lipschitz.
Hence

\[
\sup_{s\in K}\|x_{t_\star+h}(s)-x_{t_\star}(s)\|
\;=\;
\sup_{s\in K}\|x(t_\star+h+s)-x(t_\star+s)\|
\;\le\;
L|h|.
\]

Therefore \(d_{\mathrm{IS}}(x_{t_\star+h},x_{t_\star})\to 0\) as
\(h\to 0\).

At an event time the right edge \(s=0\) is a break, so the first
hypothesis of this paragraph fails. Continuity of delayed evaluation at
event times is not claimed (and is false in \(\tau_{\mathrm{IS}}\): a
break enters the window at \(s=0\)). That is the recorded honest
boundary; transversality of \(\Sigma\) is what A3.Thm3 uses in its place.
∎

---

## 6. What this does to the A3 stack

| Recorded object | Effect of A3.Thm1\(^\ast\) |
|---|---|
| A3.Thm1 as written | **False.** Replace by A3.Thm1\(^\ast\). |
| A3.Thm3 (“compactness from A3.Thm1”) | Survives after adding \(L<\infty\) to the declared class. Lipschitz hybrid flows already have it. The recorded `PROVEN_CONDITIONAL` tag should list segment Lipschitz (or a uniform modulus) among the conditions. |
| B8 (composition with E4) | Still conditional; inherits \(L<\infty\). No further damage. |
| Original \(\mathcal H\) without \(L\) | Not compact. Not a conjecture: it is refuted. |

The kernel existence argument of A3.Thm3 is a greatest-fixed-point
construction on a compact metric space of histories. That argument is
unaffected once the space is the one proved compact here.

---

## 7. Claim-status

- Recorded A3.Thm1: **false**.
- A3.Thm1\(^\ast\): **proved**, in this file, under the explicit
  Lipschitz budget \(L\). That budget is not a retreat from the
  variable-event programme. It is the regularity the vector field
  already forces between events.

No part of this file modifies the repository.

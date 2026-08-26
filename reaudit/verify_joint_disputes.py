#!/usr/bin/env python3
"""verify_joint_disputes.py — numerical adjudication of the two mathematical
disputes between the two repair attempts in batch 4 (agent 1 vs agent 2).

Companion to batch 4/PROOF_ELEVATION.md §I.3 (Findings 9 and 10).
Reads and writes no repository file. Exit 0 on success.

Dispute 1 (B9): agent 2's clause (c) claimed  K_p = union over splits of
    intersection W_k.  Agent 1's y1/y2 witness refutes it: x in K_{1/2}
    lies in NO product split's W_2.  VERDICT: agent 1 correct; (c) struck.

Dispute 2 (B10): agent 2's repair (and the audit's parenthetical) claimed
    the pessimistic leader value psi is usc / continuous by Berge and hence
    attained.  Agent 1 shows psi is lsc and sup psi need not be attained.
    VERDICT: agent 1 correct; witness verified below.
"""
import sys

failures = []

def check(name, cond):
    print(f"[{'OK ' if cond else 'FAIL'}] {name}")
    if not cond:
        failures.append(name)

# ----------------------------------------------------------------------
print("=" * 70)
print("DISPUTE 1 (B9): split-completeness vs agent 1's incompleteness witness")
print("=" * 70)
# States: x (t=0), y1,y2 (t=1), safeK/unsafe (t=2 terminal); K incl. safeK.
P = {'x': [('y1', 0.5), ('y2', 0.5)],
     'y1': [('safeK', 0.2), ('unsafe', 0.8)],
     'y2': [('safeK', 0.8), ('unsafe', 0.2)],
     'safeK': [('safeK', 1.0)],
     'unsafe': [('unsafe', 1.0)]}
K = {'x', 'y1', 'y2', 'safeK'}

def p_next_in(src, S):
    return sum(p for (s, p) in P[src] if s in S)

def survive(src, steps):
    if steps == 0:
        return 1.0 if src in K else 0.0
    return sum(p * survive(s, steps - 1) for (s, p) in P[src])

check("P(survive 2 | x) = 0.5 exactly, so x in K_(1/2)",
      abs(survive('x', 2) - 0.5) < 1e-12)

def captured(t_init, t_term):
    W1 = {y for y in K if p_next_in(y, K) >= t_term - 1e-12}
    W2 = {z for z in K if p_next_in(z, W1) >= t_init - 1e-12}
    return 'x' in W2

found = None
for i in range(1, 200000):
    t_init = i / 200000.0
    t_term = 0.5 / t_init
    if t_term > 1.0:
        continue
    if captured(t_init, t_term):
        found = (t_init, t_term)
        break
check("NO split (t_init, t_term) with product 1/2 captures x  "
      "(agent 1's incompleteness witness; agent 2's (c) is FALSE)",
      found is None)

# Agent 2's 4-state model cross-check: split-complete by accident.
P2 = {'A': [('B', 0.5), ('C', 0.5)], 'B': [('U', 1.0)],
      'C': [('C', 1.0)], 'U': [('U', 1.0)]}
K2 = {'A', 'B', 'C'}
def p2_next_in(src, S):
    return sum(p for (s, p) in P2[src] if s in S)
def survive2(src, steps):
    if steps == 0:
        return 1.0 if src in K2 else 0.0
    return sum(p * survive2(s, steps - 1) for (s, p) in P2[src])
check("agent 2's model: A in K_(1/2) and split (0.5, 1.0) captures A "
      "(model-specific accident: good successor conditional exactly 1.0)",
      abs(survive2('A', 2) - 0.5) < 1e-12 and
      p2_next_in('A', {z for z in K2 if p2_next_in(z, K2) >= 1.0 - 1e-12}) >= 0.5 - 1e-12)

# ----------------------------------------------------------------------
print()
print("=" * 70)
print("DISPUTE 2 (B10): is the pessimistic leader value attained?")
print("=" * 70)
def BR(c):
    va, vb = 0.0, c - 1.0
    m = max(va, vb)
    return {p for p, v in (('a', va), ('b', vb)) if v >= m - 1e-15}
def psi(c):
    return min(c if p == 'a' else 0.0 for p in BR(c))

check("BR usc at 1 (values jump up: BR(1-eps)={a} subset BR(1)={a,b})",
      BR(1 - 1e-6) == {'a'} and BR(1) == {'a', 'b'})
psi_left = [psi(1 - 10 ** -k) for k in range(1, 8)]
check("psi(c) -> 1 as c -> 1-  (psi(c)=c for c<1)", max(psi_left) >= 0.9999999 - 1e-12)
check("psi(1) = 0  (b enters BR(1) with v_l=0)", psi(1) == 0.0)
check("limsup_{c->1-} psi > psi(1): psi is NOT usc",
      max(psi_left) > psi(1))
check("sup psi = 1 NOT attained on [0,1]  "
      "(agent 1's witness; agent 2's 'both values attained' is FALSE)",
      all(v < 1.0 for v in psi_left) and psi(1) < 1.0)

# v_f, v_l continuous (affine in c); finite Pi; compact C. Realisable as argmax:
# v_f(c,a)=0, v_f(c,b)=c-1.
print()
print(f"{'ALL CHECKS PASSED' if not failures else f'{len(failures)} FAILURES: ' + '; '.join(failures)}")
sys.exit(0 if not failures else 1)

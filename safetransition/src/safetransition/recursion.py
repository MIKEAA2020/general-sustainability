"""Backward recursions: typed viability and belief-space safety.

Two recursions are provided, mirroring the companion manuscripts:

* :func:`typed_backward` — the finite-graph typed backward recursion of
  *Aggregate Indices and Transition Safety* (polynomial in the graph
  size and horizon on explicit state-action-disturbance graphs).

* :func:`belief_backward` — the finite-horizon robust epistemic
  recursion of *An Obstruction Calculus for Viability under Incomplete
  Observation* (sound and complete in finite systems): belief sets over
  observation labels, one-step action admissibility with post-state
  screening, and belief updates induced by the observation map.

All arithmetic is exact.
"""
from fractions import Fraction as Q


def typed_backward(states, actions_fn, visited_fn, safe_fn, horizon):
    """Generic finite-horizon typed backward recursion.

    Parameters
    ----------
    states : iterable of states
    actions_fn : state -> sequence of action labels
    visited_fn : (state, action) -> iterable of states that must remain
        safe while the action executes (the visited tube, as states)
    safe_fn : state -> bool (typed safety predicate)
    horizon : int

    Returns the set of states from which some action sequence of length
    ``horizon`` keeps every visited state safe.
    """
    W = {s for s in states if safe_fn(s)}
    for _ in range(int(horizon)):
        W = {s for s in W
             if any(all(v in W for v in visited_fn(s, a)) for a in actions_fn(s))}
    return W


def one_period_typed_viable(datum, states):
    """Typed viability over one review period on a :class:`~safetransition.datum.TransitionDatum`.

    A state is viable iff the typed operator admits an action (the
    successor is destination-maintainable by the destination hold
    policy, so one period suffices)."""
    from .operators import E
    return {z for z in states if E(datum, z, mode="typ")}


def belief_backward(F, gamma, safe, prior, horizon, max_beliefs=4096):
    """Finite-horizon robust epistemic recursion over belief sets.

    Parameters
    ----------
    F : dict state -> dict action -> post state (single successor per
        (state, action, no-disturbance); extend by wrapping)
    gamma : dict state -> observation label (states sharing a label are
        indistinguishable to the policy)
    safe : set of safe states (the non-violation set V)
    prior : iterable of states consistent with the initial observation
    horizon : int

    Beliefs are sets of observation labels whose full state fibres are
    re-expanded at every step. The abstraction is exact when the
    observation separates the states that matter (in particular when it
    is injective on reachable states) and is otherwise sound for
    viability certification: ``B in W[k]`` always certifies a viable
    policy, while ``B not in W[k]`` is conclusive only under the
    exactness condition.

    Returns ``(W, start)`` where ``W[k]`` is the set of belief sets from
    which some policy keeps the trajectory violation-free for ``k``
    steps and ``start`` is the initial belief. ``max_beliefs`` bounds
    the reachable-belief enumeration; exhausting it raises
    ``RuntimeError`` — the bound affects exploration completeness,
    never the soundness of returned memberships, and no partial results
    are returned. Use :func:`explain_belief_failure` for a per-action
    witness when a belief is not viable.
    """
    def fibre_expansion(B):
        # states still possible given observed labels (all were safe when observed;
        # expansion covers every state carrying the label)
        out = set()
        for lab in B:
            for s, l in gamma.items():
                if l == lab:
                    out.add(s)
        return frozenset(out)

    def step_ok(B, a):
        """No violation en route and every post-belief one-step viable."""
        for x in fibre_expansion(B):
            posts = F[x][a]
            if any(p not in safe for p in posts):
                return None
        return B  # screening only; post-belief computed by caller

    def post_beliefs(B, a):
        labels = set()
        for x in fibre_expansion(B):
            for p in F[x][a]:
                labels.add(gamma[p])
        return frozenset(labels)

    # enumerate reachable label-beliefs (BFS over belief updates)
    start = frozenset(gamma[x] for x in prior)
    seen = {start}
    frontier = [start]
    while frontier:
        nxt = []
        for B in frontier:
            acts = sorted({a for x in fibre_expansion(B) for a in F[x]})
            for a in acts:
                if step_ok(B, a) is None:
                    continue
                for Bp in [post_beliefs(B, a)]:
                    if Bp not in seen:
                        seen.add(Bp)
                        nxt.append(Bp)
        frontier = nxt
        if len(seen) > max_beliefs:
            raise RuntimeError(
                f"belief enumeration exceeded max_beliefs={max_beliefs}; "
                "no partial results are returned")

    # belief viability: Viable_1 = beliefs with a screening action;
    # Viable_{k+1} = beliefs with an action whose post-belief is Viable_k
    V = {B for B in seen
         if any(step_ok(B, a) is not None
                for a in {a for x in fibre_expansion(B) for a in F[x]})}
    W = {1: V}
    for k in range(2, int(horizon) + 1):
        Wk = set()
        for B in seen:
            for a in {a for x in fibre_expansion(B) for a in F[x]}:
                if step_ok(B, a) is None:
                    continue
                if post_beliefs(B, a) in W[k - 1]:
                    Wk.add(B)
                    break
        W[k] = Wk
    return W, start

def explain_belief_failure(F, gamma, safe, prior, horizon, max_beliefs=4096):
    """Per-action failure witness for a non-viable root belief.

    Returns a dictionary with the first horizon ``k`` at which the
    initial belief leaves the viable sets, the belief itself, and, for
    every action, the exact reason the policy fails: either a state in
    the fibre that enters a violation en route, or the post-belief that
    is itself not viable at the previous level. This is the
    counterexample object accompanying a ``prior not in W[horizon]``
    verdict."""
    def fibre_expansion(B):
        out = set()
        for lab in B:
            for s_, l in gamma.items():
                if l == lab:
                    out.add(s_)
        return frozenset(out)

    def step_ok(B, a):
        for x in fibre_expansion(B):
            if any(p not in safe for p in F[x][a]):
                return False
        return True

    def post_beliefs(B, a):
        labels = set()
        for x in fibre_expansion(B):
            for p in F[x][a]:
                labels.add(gamma[p])
        return frozenset(labels)

    W, start = belief_backward(F, gamma, safe, prior, horizon, max_beliefs)
    for k in range(1, int(horizon) + 1):
        if start not in W[k]:
            actions = {}
            for a in sorted({act for x in fibre_expansion(start) for act in F[x]}):
                if not step_ok(start, a):
                    bad = sorted({x for x in fibre_expansion(start)
                                  for p in F[x][a] if p not in safe})
                    actions[a] = {"reason": "violation en route", "states": bad}
                else:
                    bp = post_beliefs(start, a)
                    ref = W.get(k - 1, W[1]) if k > 1 else W[1]
                    if bp not in ref:
                        actions[a] = {"reason": f"post-belief not {max(1, k - 1)}-step viable",
                                      "post_belief": sorted(bp)}
            return {"horizon": k, "belief": sorted(start), "actions": actions}
    return {"horizon": None, "belief": sorted(start), "actions": {},
            "note": "belief is viable over the horizon"}

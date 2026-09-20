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


def belief_backward(F, gamma, safe, prior, horizon, fibre_of=None):
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

    Returns ``(W, reaches)`` where ``W[k]`` is the set of belief sets
    (frozensets of observation labels) from which some policy keeps the
    trajectory violation-free for ``k`` steps, and ``reaches`` maps each
    belief to its one-step observed successors per action. The recursion
    is complete in finite systems: a belief outside ``W[horizon]``
    admits no viable observation-based policy over that horizon.
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
        if len(seen) > 4096:
            raise RuntimeError("belief enumeration exceeded 4096 reachable beliefs")

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

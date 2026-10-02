-- Exact, versioned source for the pinned-toolchain footprint run.
-- Import the whole project; these checks do not assert that all paper prose is formalized.
import Formalizations

#print axioms Formalizations.P1.finite_horizon_sound
#print axioms Formalizations.P1.finite_horizon_complete
#print axioms Formalizations.P1.tree_sound
#print axioms Formalizations.P1.blocked_iff
#print axioms Formalizations.P1.Wk_antitone
#print axioms Formalizations.P1.Wk_descending
#print axioms Formalizations.P1.preOp_mono
#print axioms Formalizations.CompCert.robust_row_sound
#print axioms Formalizations.Minimax.dual_certificate_sound
#print axioms Formalizations.Minimax.two_row_average
#print axioms Formalizations.Minimax.parity_common_safe_empty
#print axioms Formalizations.Minimax.benchmark_obstruction
#print axioms Formalizations.EBC.hold_action_zero
#print axioms Formalizations.EBC.holdRep_zero
#print axioms Formalizations.EBC.matchedRep_zero
#print axioms Formalizations.EBC.natToK_zero
#print axioms Formalizations.EBC.natToK_succ
#print axioms Formalizations.P3.Φ_mono
#print axioms Formalizations.WS.master_monotone
#print axioms Formalizations.ARV.bracket_upper_form1
#print axioms Formalizations.E1.ladder_telescope

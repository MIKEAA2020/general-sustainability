-- Complete imported-project footprint inventory at the pinned toolchain.
-- Unlike AxiomFootprint.lean, this enumerates *all* environment declarations
-- whose fully qualified names begin Formalizations., including definitions,
-- axioms and generated names. Unexpected axioms are reported (not automatically whitelisted).
import Lean
import Formalizations
open Lean Elab Command

run_cmd do
  let env ← getEnv
  let names := env.constants.fold (init := #[]) fun acc name _ =>
    if name.toString.startsWith "Formalizations." then acc.push name else acc
  let sorted := names.qsort Name.lt
  let allowed : Array String := #["propext", "Classical.choice", "Quot.sound"]
  let mut flagged : Nat := 0
  for name in sorted do
    let axioms ← collectAxioms name
    for ax in axioms do
      unless allowed.contains ax.toString do
        logInfo m!"UNEXPECTED {name} AXIOM {ax}"
        flagged := flagged + 1
    logInfo m!"FOOTPRINT {name} AXIOMS {axioms.qsort Name.lt |>.toList}"
  logInfo m!"FOOTPRINT_TOTAL {sorted.size} UNEXPECTED_REFERENCES {flagged}"

# Article 005 Evaluation and Verification

## Bibliographic identity

**Source file:** `uploads/Paper_III_Groundwater_Module.txt`  
**Title:** *Groundwater Governability under Partial Observation: A Typed Hybrid Material–Institution Module*  
**Format:** LaTeX article source  
**Length:** approximately 1,205 words, 117 lines  
**Formal content:** constitutive storage relation, two head balances, leakage relation, generic solute balance, safety and action sets, observation-compatible-state set; no theorem, proposition, or conjecture  
**Evaluation status:** evaluated; integration not yet executed

## Executive assessment

The article is a sound groundwater-domain architecture. It correctly distinguishes hydraulic head from storage, fast and slow formations, signed cross-formational exchange, solute mass from functional salinity/intrusion, sampled prescriptions from implemented controls, partial observation, institutional authority, competing physical hypotheses, and task-relative validation.

Its strongest contribution is its insistence that groundwater governability is jointly physical, epistemic, institutional, and implementational. A basin may improve physically yet remain outside an implementable viability kernel because state uncertainty, authority, compliance, or review constraints prevent a safe policy.

The source is not a calibrated basin model and contains no theorem, numerical result, viability kernel, or empirical validation. Several equations require correction or greater type specificity before integration, especially donor-limited leakage, compartment-specific solute accounting, the unused release control, compatible-state topology, and structural discrepancy in material coordinates.

Under the minimum-paper rule, the current module does not merit a separate publication. It is strongly suited to a flagship/supplement domain instantiation. A separate groundwater paper may become merited after basin calibration, held-out comparison, and a substantive governability or safety result.

---

## 1. Boundary, state, and constitutive storage

The boundary requirement is appropriate. A basin implementation must identify formations, rivers, imports/exports, receiving environments, management jurisdiction, and temporal resolution.

The state

\[
Z=(H_f,H_s,M_q,\sigma_{\rm sal},\chi)
\]

correctly avoids duplicating head and storage when storage is determined by

\[
A_i=\mathcal A_i(H_i),
\qquad
C_i(H_i)=\frac{d\mathcal A_i}{dH_i}>0.
\]

### Required conditions

- \(A_i\) should be called stored water volume or storage, with volume units.
- \(C_i\) has units of volume per head.
- The admissible head domain must ensure \(\mathcal A_i(H_i)\ge0\).
- A dry/dewatered boundary or minimum physically meaningful head should be declared.
- Strict positivity of \(C_i\) provides local invertibility but does not validate a lumped two-store reduction.
- If hysteresis, unconfined geometry, moving saturated thickness, compaction, or distributed flow invalidates the constitutive relation, the article correctly requires a DAE or distributed model and renewed proofs.

The functional state \(\chi\) is undefined and must be named, typed, or removed.

---

## 2. Controls and institutional implementation

The prescription and implementation distinction

\[
a_k\in\Gamma(B_k,h_k),
\]

\[
U_k=(q_{p,f,k},q_{p,s,k},q_{r,k},q_{{\rm rel},k})
\in\mathcal E(B_k,h_k,a_k)
\]

is architecturally sound. It distinguishes authorized action from realized control.

### Required clarification

- Define \(B_k\) as the compatible belief/information set.
- Define \(h_k\) as institutional state.
- Declare the causal policy class that maps histories to prescriptions.
- Specify event order: observation, assessment, authorization, implementation/enforcement, hold.
- Specify whether controls are rates, volumes over an interval, or schedules.
- The release control \(q_{\rm rel}\) does not appear in the displayed water balances. It must be routed explicitly through a river/catchment boundary term or removed.
- Pumping and recharge controls must satisfy physical capacities, energy/budget limits, permit constraints, and donor/recipient limits.

---

## 3. Cross-formational leakage

The signed Darcy-style relation

\[
\ell_{fs}=\kappa_{fs}(H_f-H_s)
\]

correctly allows direction reversal.

The directional expressions

\[
\ell_{f\to s}=[\ell_{fs}]_+\psi_f(A_f),
\qquad
\ell_{s\to f}=[-\ell_{fs}]_+\psi_s(A_s)
\]

require clarification:

1. \(\psi_i\) must be dimensionless if \(\ell_{fs}\) already has flow units.
2. \(0\le\psi_i\le1\) should be stated if it is a limiter.
3. \(\psi_i(0)=0\) supports donor limitation, but behavior away from zero must be declared—typically \(\psi_i\to1\) when the donor has adequate storage.
4. Multiplying Darcy flow by \(\psi_i\) changes the constitutive leakage law near depletion. This is acceptable only if the limiter has physical interpretation.
5. If storage never reaches zero in the admissible head domain, donor limitation may instead be enforced through the domain and pumping/leakage constraints.

The net-flow sign convention

\[
\ell_{fs}^{\rm net}
=
\ell_{f\to s}-\ell_{s\to f}
\]

is consistent with subtracting net fast-to-slow flow from the fast formation and adding it to the slow formation.

---

## 4. Water balances

The balances

\[
C_f(H_f)\dot H_f
=R_{\rm nat}+q_r-q_{p,f}-\ell_{fs}^{\rm net}-L_f+J_f,
\]

\[
C_s(H_s)\dot H_s
=\ell_{fs}^{\rm net}-q_{p,s}-L_s+J_s
\]

are dimensionally consistent when every right-hand term is water volume per time.

Adding them yields the total represented-storage identity

\[
\frac{d}{dt}(A_f+A_s)
=
R_{\rm nat}+q_r-q_{p,f}-q_{p,s}-L_f-L_s+J_f+J_s.
\]

The internal leakage cancels, as it should. This identity should be stated explicitly.

### Boundary and nonnegativity requirements

- \(R_{\rm nat},J_i\) and \(L_i\) need sign conventions and units.
- River exchange must be signed and physically linked to river state or a boundary condition.
- \(J_i\) cannot absorb residual error without changing epistemic status.
- Pumping and leakage must be donor-limited near dewatered storage.
- Managed recharge must respect receiving capacity and should not force storage beyond an upper safety bound if flooding or mobilization risks matter.
- Hybrid pumping, recharge, or release events require jump balances if represented as impulses rather than rates.

---

## 5. Solute and salinity accounting

The generic equation

\[
\dot M_q
=I_q-O_q(X,U,\omega)+\mathcal R_q(X,U,\omega)
\]

is too aggregated for a two-formation model unless \(M_q\) is explicitly total basin mass and no formation-specific concentration is required.

### Required correction

For concentration, leakage transport, or water-quality constraints by formation, use at least

\[
M_{q,f},\qquad M_{q,s},
\]

with advective exchange, pumping removal, recharge input, reactions, and boundary transport. Concentrations then require positive storage volumes:

\[
C_{q,i}=\frac{M_{q,i}}{A_i(H_i)}.
\]

The reaction term \(\mathcal R_q\) must specify sign and chemistry. If it represents degradation or transformation, transformed moieties and products may need their own ledger. Structural discrepancy must not be silently interpreted as contaminant destruction.

The article correctly distinguishes salinity represented as a conserved mass from salinity/intrusion represented as a functional interface or damage index. The choice must be fixed per model.

---

## 6. Safety and service constraints

The set

\[
\mathcal C_Z(\lambda)
\]

is a legitimate typed safety template. Thresholds may represent accessibility, subsidence, ecosystem impairment, drinking-water safety, legal compliance, recovery risk, or normative allocation. These types must remain distinct.

### Possible missing constraints

Depending on the basin, the model may need:

- upper head/storage bounds for flooding, waterlogging, or mobilization risk;
- head-difference limits related to compaction or intrusion;
- formation-specific concentration constraints;
- subsidence state or cumulative compaction;
- minimum ecological discharge or connected-river condition;
- pumping-energy or infrastructure capacity constraints.

The ecological-flow relation

\[
\mathcal A(Z,\omega;\lambda)
=
\{U:Q_{\rm eco}(Z,U,\omega)
\ge Q_{\rm eco}^{\min}(\lambda)\}
\]

correctly treats service provision as a state-action condition. It should be renamed to avoid confusion with the storage function \(\mathcal A_i\) and the master architecture symbol \(\mathcal A_q\). It is an admissible action correspondence, not a causal policy class.

Compatibility must be evaluated jointly with the state-safe set, energy, budget, legal, authority, and implementation constraints.

---

## 7. Observation and compatible-state uncertainty

The observation relation

\[
Y_k=\mathcal O(Z_{[t_{k-1},t_k]})+\varepsilon_k
\]

is structurally appropriate for additive observations. Other data types may require a likelihood or correspondence.

The compatible set

\[
B_k
\subseteq
C([t_{k-1}-\tau,t_k],\mathcal Z)
\times\Theta
\]

requires:

- a phase-space topology and norm;
- compactness or closure assumptions;
- parameter bounds and discrepancy class;
- exact or approximate update rule;
- distinction among observation error, process noise, reporting error, parameter uncertainty, and structural discrepancy;
- causal policy semantics.

The caution about GRACE/G3P is sound: coarse-scale gravimetric or model-derived information can corroborate regional storage change but does not by itself identify local formation heads or basin control states. This statement needs domain references and a precise spatial-resolution qualification.

---

## 8. Institutional governability

The institutional state \(h_k\) is useful if decomposed into:

- review timing;
- permit and emergency authority;
- monitoring capacity;
- enforcement and compliance;
- budget and infrastructure;
- allocation and rights constraints.

This supports separate diagnoses of:

- physical infeasibility;
- epistemic insufficiency;
- authority failure;
- implementation failure.

A physically viable policy that is not observation-based, authorized, or enforceable does not establish governability.

---

## 9. Competing models and identification

The H0/H1/H2 physical hierarchy is appropriate:

- one-pool storage;
- fast/slow two-pool storage with bidirectional exchange;
- distributed or higher-dimensional model.

The two-pool model should be selected only if it improves held-out state, service, or safety prediction; uncertainty calibration; or decision quality. “Improves” requires preregistered metrics and margins.

The fast/slow split needs independent geological, multi-depth, pumping-test, tracer/isotope, water-age, and recharge information. Leakage must not absorb residual mismatch.

The institutional H1/H2/H3 response signs align with Article 003 and should share one registered definition rather than duplicate labels.

---

## 10. Structural discrepancy

The equation

\[
\dot Z
=F_{\rm gw}(Z,U,\omega,\vartheta)+\delta_t,
\qquad
\delta_t\in\mathcal D_t
\]

is a useful model-error template but must be typed by state component.

Adding unrestricted discrepancy directly to head and solute-mass coordinates can violate water or solute accounting. For material coordinates, discrepancy should be represented as an uncertain boundary flux, omitted transfer, or explicitly nonphysical model-error term that is not interpreted as material creation/destruction. Functional states may use a different discrepancy class.

Process uncertainty, parameter uncertainty, observation error, reporting error, structural discrepancy, and implementation uncertainty should remain separate, as the article states.

---

## 11. Diagnostics and recovery

The distinction among gross throughput time, local net-rate horizon, model-based crossing time, and probabilistic failure horizon is valid.

A finite gross draw does not prove storage decline because recharge, imports, recycling, or leakage may offset it. Net stock change follows the complete balance.

Recovery should require return to:

- physically viable water and solute states;
- epistemically sufficient compatible-state sets;
- authorized and implementable institutional states;
- ecological/service constraints.

This is a direct groundwater instance of the master assessment map: a basin may be physically improved but not recoverable or governable under its information and authority classes.

---

## 12. Verification verdict

### Verified or conceptually sound

- head/storage constitutive distinction;
- bidirectional head-gradient leakage;
- sampled prescription versus implemented control;
- water/solute type separation;
- functional salinity alternative;
- typed safety thresholds;
- ecological service as state-action relation;
- compatible-state uncertainty;
- competing physical and institutional hypotheses;
- rare-event calibration caution;
- recovery beyond physical head restoration.

### Valid after correction

- donor-limited directional leakage;
- total storage balance;
- compartment-specific solute accounting;
- release-control routing;
- action-versus-policy notation;
- compatible-state topology;
- componentwise structural discrepancy;
- model-comparison metrics;
- domain references and GRACE/G3P qualification.

### Not verifiable from this file

- any basin parameter or threshold;
- any one-pool/two-pool/distributed model comparison;
- any recharge, pumping, leakage, solute, or subsidence estimate;
- any viable action or policy set;
- any observation-based kernel;
- any rare-event probability;
- any institutional response sign in a real basin.

---

## 13. Publication and integration recommendation

The current module does not merit a separate paper. Preferred destination:

- a groundwater worked module in the flagship or technical supplement;
- a separate basin paper only after calibration, held-out model comparison, uncertainty validation, and a substantive governability or safety result.

Strong bridges exist to:

- Article 001: viability, recovery, observer limits, institutions, delays, resource balances;
- Article 002: typed fluxes, sampled governance, compatible-state kernels, hybrid controls, projectability, uncertainty typing;
- Article 003: shared institutional response hypotheses and sampled-versus-delay distinction;
- Article 004: common multi-scale material–service–institution module design.

Article 005 should remain on integration hold until the identified corrections and source references are completed.

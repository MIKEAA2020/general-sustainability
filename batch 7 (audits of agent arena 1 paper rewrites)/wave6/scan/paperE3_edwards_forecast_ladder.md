# Sentence-level normalised diff scan — paperE3_edwards_forecast_ladder (final v12)

Universe: body sentences/segments of the final v12 vs the five preceding versions (v7 … v11). A segment counts as dropped only if absent from the *whole* final file. Table rows and display-math lines are atomic. The per-version `*Version log*` paragraph is excluded from the universe (meta) and quoted per transition.

Final v12 segment counts: heading 19, tablerow 71, listitem 9, para 322, display 1

## Transition v7 → v8 — 5 dropped (5 modified-with-replacement r≥0.55, 0 no-close-replacement)

> v8 carries no in-file version log (pre-batch-7 transition).

1. **[para @v7 L23 · ## 1. Introduction]** The term "water balance" is used throughout in its increment-structure sense: head change equals weighted fluxes plus a linear drain, with the spring-discharge series stored but deliberately excluded from the forecasting equation and a [610, 710] clip standing in for a physical storage floor — the map is not a closed mass balance, and the qualification travels with every use of the term.
   - paired replacement (r=0.88): The term "water balance" is used throughout in its increment-structure sense: head change equals weighted fluxes plus a linear drain, with the spring-discharge series stored but deliberately excluded from the forecasting equation and a [610, 710] clip standing in for a physical storage floor — the map is not a closed m …[truncated]
2. **[para @v7 L236 · ## Data Availability Statement]** Niño 3.4: NOAA PSL HadISST (raw file committed with the repository).
   - paired replacement (r=0.92): Niño 3.4: NOAA PSL HadISST (raw file registered with the repository).
3. **[para @v7 L236 · ## Data Availability Statement]** Precipitation: NCEI nClimDiv — the raw file is not distributed with the repository (provenance URL archived in the sources index), so the three precipitation columns of the fixed panel are not reproducible from the committed code alone, while the two Niño columns rebuild from the committed file to machine precision; scoring from the committed analysis panel does not require the nClimDiv file.
   - paired replacement (r=0.94): Precipitation: NCEI nClimDiv — the raw file is not distributed with the repository (provenance URL archived in the sources index), so the three precipitation columns of the fixed panel are not reproducible from the registered code alone, while the two Niño columns rebuild from the registered file to machine precision;  …[truncated]
4. **[para @v7 L236 · ## Data Availability Statement]** The committed twenty-column analysis panel is the dataset of record for all scored analyses.
   - paired replacement (r=0.94): The registered twenty-column analysis panel is the dataset of record for all scored analyses.
5. **[para @v7 L236 · ## Data Availability Statement]** All computations are deterministic: re-executing the committed scripts in a fresh environment regenerated every archived result file byte for byte, and all scored rows recompute from the per-observation forecast files and the committed series.
   - paired replacement (r=0.94): All computations are deterministic: re-executing the registered scripts in a fresh environment regenerated every archived result file byte for byte, and all scored rows recompute from the per-observation forecast files and the registered series.

## Transition v8 → v9 — 23 dropped (18 modified-with-replacement r≥0.55, 5 no-close-replacement)

> v9 carries no in-file version log (pre-batch-7 transition).

1. **[para @v8 L21 · ## 1. Introduction]** Forecasting aquifer heads at index wells is a recurring operational problem of groundwater management: drought-stage declarations, springflow protection, and permit adjustments all key on forecasted water levels.
   - paired replacement (r=0.67): Drought-stage declarations, springflow protection, and permit adjustments all key on forecasted water levels.
2. **[para @v8 L21 · ## 1. Introduction]** The field has also begun to institutionalize benchmark culture: GEMS-GER, the first machine-learning benchmark dataset for long-term groundwater levels, standardizes 32 years of weekly observations from 3,207 German wells together with three benchmark models of increasing complexity (Ohmer et al. 2026), and systematic comparisons of nine machine-learning and deep-learning architectures on a karst catchment now anchor the karst groundwater forecasting literature (Zhu et al. 2026).
   - paired replacement (r=0.66): GEMS-GER, the first machine-learning benchmark dataset for long-term groundwater levels, standardizes 32 years of weekly observations from 3,207 German wells together with three benchmark models of increasing complexity (Ohmer et al. 2026).
3. **[para @v8 L23 · ## 1. Introduction]** Whether added structure improves out-of-sample forecasts — as opposed to in-sample fit — is a separate, testable question, and the general forecasting literature has made the benchmark discipline explicit: across the M4 competition's 100,000 series, sophisticated methods did not uniformly beat simple statistical baselines (Makridakis, Spiliotis, and Assimakopoulos 2020).
   - paired replacement (r=0.79): The general forecasting literature has made the benchmark discipline explicit: across the M4 competition's 100,000 series, sophisticated methods did not uniformly beat simple statistical baselines (Makridakis, Spiliotis, and Assimakopoulos 2020).
4. **[para @v8 L23 · ## 1. Introduction]** Yet the groundwater benchmark studies above compare model families against one another; they do not subject each module to a retention gate against the naive baselines, and none subjects a deliberately simple process-based water balance to a scored ablation against those baselines.
   - paired replacement (r=0.81): They do not subject each module to a retention gate against the naive baselines, and none subjects a deliberately simple process-based water balance to a scored ablation against those baselines.
5. **[para @v8 L23 · ## 1. Introduction]** This paper supplies that missing test: a scored model-ablation design, in which a ladder of incrementally structured one-pool models is evaluated against the two naive baselines, and complexity is kept only if it improves the stated score, decided on out-of-sample error on the predictand itself.
   - paired replacement (r=0.55): Complexity is kept only if it improves the stated score, decided on out-of-sample error on the predictand itself.
6. **[para @v8 L23 · ## 1. Introduction]** The three hydrological objects are worth separating, since they are read off the same number.
   - paired replacement (r=0.93): Three hydrological objects are worth separating, because they are read off the same number.
7. **[para @v8 L23 · ## 1. Introduction]** The head record is observed at an access point, the index well; that head indexes a store of water in the aquifer, which is the resource; and the store is replenished and drawn by fluxes, which are the flow.
   - paired replacement (r=0.52): That head indexes a store of water in the aquifer, which is the resource.
8. **[para @v8 L23 · ## 1. Introduction]** The one-pool map closes this loop approximately.
   - paired replacement (r=0.49): The one-pool water balance (a lumped stock-flow model with head change equal to weighted fluxes plus a linear drain) closes this loop approximately.
9. **[para @v8 L23 · ## 1. Introduction]** The term "water balance" is used throughout in its increment-structure sense: head change equals weighted fluxes plus a linear drain, with the spring-discharge series stored but deliberately excluded from the forecasting equation and a [610, 710] clip standing in for a physical storage floor — the map is not a closed mass balance, and the qualification travels with every use of the term precisely because the store, the flow, and the access point are three distinct objects collapsed into one map.
   - paired replacement (r=0.74): The term "water balance" is used throughout in its increment-structure sense: head change equals weighted fluxes plus a linear drain, with the spring-discharge series stored but deliberately excluded from the forecasting equation, and a [610, 710] clip standing in for a physical storage floor.
10. **[para @v8 L25 · ## 1. Introduction]** Its 1934–2023 daily head record is among the longest managed groundwater series in North America; its institutional thresholds (the 660-ft Stage I line of the Edwards Aquifer Authority) and its physical threshold (the ≈618-ft level at which Comal Springs approaches cessation) are explicit and dated; and recharge and pumpage series exist that are constructed independently of the head series.
   - paired replacement (r=0.68): Its institutional thresholds (the 660-ft Stage I line of the Edwards Aquifer Authority) and its physical threshold (the ≈618-ft level at which Comal Springs approaches cessation) are explicit and dated.
11. **[para @v8 L25 · ## 1. Introduction]** The aquifer is also a karst system in which regional flow has long been represented — and debated — through equivalent porous media and lumped approaches (Scanlon et al. 2003, for the Barton Springs segment; the lumped-versus-EPM question is inherited by the San Antonio Pool, not settled by that citation), which makes the fate of a deliberately simple one-pool water-balance map a live hydrogeologic question rather than a straw man.
   - paired replacement (r=0.83): The aquifer is also a karst system in which regional flow has long been represented — and debated — through equivalent porous media and lumped approaches (Scanlon et al. 2003, for the Barton Springs segment; the lumped-versus-EPM question is inherited by the San Antonio Pool, not settled by that citation).
12. **[para @v8 L29 · ## 1. Introduction]** A companion study under separate review applies the same scored design to a marine fishery stock (Northern cod, NAFO 2J3KL); the two systems' scores are never pooled, and no retention verdict is transferred between them.
   - paired replacement (r=0.72): A companion study under separate review applies the same scored design to a marine fishery stock (Northern cod, NAFO 2J3KL).
13. **[para @v8 L51 · ## 2. Data and Specification]** Years with fewer than 240 observations are dropped; no year falls below the floor (minimum n = 242, 1939), so the rule is vacuous on this panel; 1935 (n = 258) and 1939 (n = 242) satisfy the 240-observation rule and are retained as incomplete-coverage means (they are not exceptions — they are the incomplete years that still qualify); missing days are not interpolated.
   - paired replacement (r=0.92): No year falls below the floor (minimum n = 242, 1939), so the rule is vacuous on this panel; 1935 (n = 258) and 1939 (n = 242) satisfy the 240-observation rule and are retained as incomplete-coverage means (they are not exceptions — they are the incomplete years that still qualify); missing days are not interpolated.
14. **[para @v8 L57 · ## 3. Forecast Models]** The one-pool map, with head clipped to [610, 710] ft, is
   - paired replacement (r=0.67): ** With head clipped to [610, 710] ft, the one-pool map is
15. **[para @v8 L76 · ## 3. Forecast Models]** With constant fluxes, M2m reduces to $H_{t+1}=(1+\delta)H_t+\mathrm{const}$ and therefore shares M1's forecast function class — but not its estimator: M2m pins its intercept and persistence from the in-sample mean fluxes, an additional identifying use of the recharge and pumpage records in training.
   - paired replacement (r=0.68): The estimator differs from M1: M2m pins its intercept and persistence from the in-sample mean fluxes, an additional identifying use of the recharge and pumpage records in training.
16. **[para @v8 L80 · ## 3. Forecast Models]** The scoring protocols for the primary pass and the climate pass were frozen and dated (2026-08-25) before the corresponding RMSE tables were computed; the frozen protocol documents are archived with the analysis code.
   - paired replacement (r=0.82): The scoring protocols for the primary pass and the climate pass were frozen and dated (2026-08-25) before the corresponding RMSE tables were computed.
17. **[para @v8 L90 · ## 4. Evaluation Design]** A causal module is retained only if its primary RMSE is strictly less than that of persistence and strictly less than that of the next-simpler causal model.
   - paired replacement (r=0.47): The retention rule (a module is kept only if it beats both persistence and the next-simpler causal model) is the gate against which every causal rung of the ladder is judged.
18. **[para @v8 L90 · ## 4. Evaluation Design]** Diagnostic oracles are excluded from retention; the Comal series is excluded from retention.
   - paired replacement (r=0.68): Diagnostic oracles are excluded from retention.
19. **[para @v8 L150 · ### 5.3 Rolling origin]** The margin is 0.39 ft on n = 75 and is not a significance claim — mean absolute error is a tie (M1 10.72 versus persist 10.73 ft), and at h = 5 M1 (21.25 ft) does not beat persistence (21.11 ft) while the training mean (16.80 ft) beats both, so the retention is explicitly a one-year, RMSE-level statement: it records a slightly mean-reverting head series, not a confirmation of stock-flow structure, and at the decision scale of annual drought-stage declarations the difference is operationally nil.
   - paired replacement (r=0.55): It records a slightly mean-reverting head series, not a confirmation of stock-flow structure, and at the decision scale of annual drought-stage declarations the difference is operationally nil.
20. **[para @v8 L152 · ### 5.3 Rolling origin]** At h = 5 the training mean (16.80 ft) has lower RMSE than persistence (21.11 ft): five-year forecasts on this basin are climatology, not last value and not persisted recharge.
   - paired replacement (r=0.69): Five-year forecasts on this basin are climatology, not last value and not persisted recharge.
21. **[para @v8 L187 · ### 5.4 Climate-informed recharge]** No climate-informed recharge module is retained.
   - paired replacement (r=0.59): ** Under the retention rule of Definition 4.2 applied to Table 6, no climate-informed recharge module is retained.
22. **[para @v8 L195 · ### 5.5 The service series after the retention freeze]** The map Q = c₀ + c₁H was fitted on 1934–1950 only (c₀ = −2876, c₁ = 4.77) and applied to already-issued Ĥ; the r = 0.986 figure is the full-sample contemporaneous correlation, not the 1934–1950 fit.
   - paired replacement (r=0.52): ** The map Q = c₀ + c₁H fitted on 1934–1950 (c₀ = −2876, c₁ = 4.77) is a linear channel of the same state indexed by J-17.
23. **[para @v8 L212 · ### 5.6 Pumpage counterfactuals]** Four readings.
   - paired replacement (r=0.80): Four readings follow.

## Transition v9 → v10 — 0 dropped (0 modified-with-replacement r≥0.55, 0 no-close-replacement)

> v10 version log: *Version log (v10).* Scored results of v9 were re-verified against the registered analysis scripts and archived result files and reproduce exactly (Tables 3–7, the rolling summary, the post-2007 labelled rows, the fibre map, and the pumpage counterfactuals). No score changed. This revision adds generic companion-study reference entries for the two cross-referenced Northern cod studies (without implying simultaneous publication) and records that no result depends on the single-convention correction made to the marine-scaffold companion papers; the v9 narrative is otherwise unchanged.

_(no dropped sentences)_

## Transition v10 → v11 — 117 dropped (61 modified-with-replacement r≥0.55, 56 no-close-replacement)

> v11 version log: *Version log (v11).* Implements the joint external audit of this manuscript. Changes are presentation, disclosure, and a labelled post-freeze uncertainty layer; no frozen verdict, no reported score, and no archived number changed. (1) Abstract, Impact Statement, and Conclusions now lead with the result the audit identified (causal stock-flow loses; the AR(1) margin is a coin-flip; the oracle is a nowcast; climatology wins at five years) instead of the 0.39-ft retention. (2) The M2m decline is disclosed as a protocol clause not contained in the frozen retention rule, with the frozen rule quoted verbatim and the deviations listed in one place; the climate comparison now reports margins against both M2m and M1. (3) A post-freeze Diebold–Mariano / moving-block-bootstrap layer attaches uncertainty to every load-bearing margin. (4) The [610, 710] clip is reported as binding on the recovery-win…

1. **[para @v10 L9 · ## Abstract]** A causal module was retained only if it beat both persistence and the next-simpler causal model under a pre-registered scoring protocol.
   - paired replacement (r=0.80): A causal module was retained only if it beat both persistence and the next-simpler causal model under a scoring protocol frozen and dated before any score was computed.
2. **[para @v10 L11 · ## Abstract]** ** At the one-year horizon, rolling RMSE was 13.23 ft for persistence and 12.84 ft for the AR(1), which was retained by a margin of 0.39 ft as an output-only model.
   - paired replacement (r=0.36): First, the retention margin itself (M1 − persist, 0.39 ft) is within noise, as is the M2m-over-M1 estimator margin and the M2 causal loss (the last only borderline, its interval touching zero).
3. **[para @v10 L11 · ## Abstract]** The causal stock-flow model scored 14.70 ft and was rejected.
   - paired replacement (r=0.38): ### 4.1 Protocol record and deviations
4. **[para @v10 L11 · ## Abstract]** Given realized future recharge and pumpage, the same map reached 7.55 ft RMSE, a 43% reduction from persistence, but no signal available at the annual forecast origin recovered that gap.
   - paired replacement (r=0.84): Given realized future recharge and pumpage, the same map reaches 7.55 ft — a nowcast, not a forecast; no signal available at the annual forecast origin recovers that gap.
5. **[para @v10 L11 · ## Abstract]** At five years, the training mean (16.80 ft) beat persistence (21.11 ft).
   - paired replacement (r=0.81): At five years, the training mean (16.80 ft) beats persistence (21.11 ft) with an interval excluding zero.
6. **[para @v10 L13 · ## Abstract]** ** For annual J-17 head forecasts, simple persistence and a univariate AR(1) are difficult to beat, and the one-pool water balance serves as a certificate for the current year rather than a forecast of the next.
   - paired replacement (r=0.73): ** For annual J-17 head forecasts, simple persistence and a univariate AR(1) are difficult to beat; the one-pool balance, given the year's fluxes, nowcasts the current year rather than forecasting the next.
7. **[para @v10 L15 · ## Abstract]** **Keywords:** Edwards Aquifer; groundwater level forecasting; forecast evaluation; hindcasting; prediction skill
   - paired replacement (r=0.89): **Keywords:** Edwards Aquifer; groundwater level forecasting; forecast evaluation; persistence benchmark; prediction skill
8. **[para @v10 L16 · ## Abstract]** ** Annual J-17 head forecasts: simple persistence and AR(1) beat the one-pool water balance; the balance certifies the current year, not the next.
   - paired replacement (r=0.59): ** For annual J-17 head forecasts, simple persistence and a univariate AR(1) are difficult to beat; the one-pool balance, given the year's fluxes, nowcasts the current year rather than forecasting the next.
9. **[para @v10 L23 · ## 1. Introduction]** The map is not a closed mass balance.
   - paired replacement (r=0.55): **The M2m class clause.
10. **[para @v10 L23 · ## 1. Introduction]** This qualification travels with every use of the term, precisely because the store, the flow, and the access point are three distinct objects collapsed into one map.
   - paired replacement (r=0.40): The full-sample contemporaneous correlation is r = 0.986; the 1934–1950 fit is quoted because the channel is used on that train, and the full-sample correlation is the redundancy statement.
11. **[para @v10 L29 · ## 1. Introduction]** This paper does not assess whether the aquifer is sustainable, does not close the two-pool exchange module's blocking list, and does not treat springflow or reconstructed storage as co-primary predictands.
   - paired replacement (r=0.41): This paper does not assess whether the aquifer is sustainable and does not treat springflow or reconstructed storage as co-primary predictands; a two-pool exchange module was specified and not fitted.
12. **[para @v10 L29 · ## 1. Introduction]** No solute or water-quality module is opened.
   - paired replacement (r=0.47): None replaces or alters a frozen verdict.
13. **[para @v10 L31 · ## 1. Introduction]** A companion study under separate review applies the same scored design to a marine fishery stock (Northern cod, NAFO 2J3KL).
   - paired replacement (r=0.61): A companion study under separate review applies the same scored design to a marine fishery stock (Northern cod, NAFO 2J3KL); the analogy between the two systems is that the identified driver is not persistent at the forecast origin (Author et al., in review; Author et al., in review).
14. **[tablerow @v10 L38 · ## 2. Data and Specification]** | $z_t$ | Calendar-year mean of daily-high J-17 elevation (ft AMSL) | D |
   - paired replacement (r=0.99): | $H_t$ | Calendar-year mean of daily-high J-17 elevation (ft AMSL) | D |
15. **[para @v10 L53 · ## 2. Data and Specification]** Pumpage P is well discharge from Edwards Aquifer Authority Table 1.
   - paired replacement (r=0.70): Pumpage P is well discharge from Edwards Aquifer Authority Table 1 (Edwards Aquifer Authority 2024/25, covering 1934 onward).
16. **[para @v10 L55 · ## 2. Data and Specification]** No year falls below the floor (minimum n = 242, 1939), so the rule is vacuous on this panel; 1935 (n = 258) and 1939 (n = 242) satisfy the 240-observation rule and are retained as incomplete-coverage means (they are not exceptions — they are the incomplete years that still qualify); missing days are not interpolated.
   - paired replacement (r=0.65): No year falls below the floor (minimum n = 242, 1939), so the rule never binds on this panel; 1935 (n = 258) and 1939 (n = 242) are retained as incomplete-coverage means; missing days are not interpolated.
17. **[tablerow @v10 L65 · ## 3. Forecast Models]** | ID | Class | Fluxes at $t+k$ | Role |
   - paired replacement (r=0.97): | ID | Class | Fluxes at $t+h$ | Role |
18. **[tablerow @v10 L73 · ## 3. Forecast Models]** | M4 | delay | as M2 | starts from $H_{t-1}$ |
   - paired replacement (r=0.44): | M3, M4 | worse than persist | worse | yes | reject |
19. **[para @v10 L76 · ## 3. Forecast Models]** The protocol declines it because the retained object is forecast-time structure, not estimator refinement; the estimator distinction is recorded so that the decline is not misread as numerical equivalence of the two fits.
   - paired replacement (r=0.37): First, the retention margin itself (M1 − persist, 0.39 ft) is within noise, as is the M2m-over-M1 estimator margin and the M2 causal loss (the last only borderline, its interval touching zero).
20. **[para @v10 L80 · ## 3. Forecast Models]** The design is a fixed computational protocol rather than a prospective clinical-style registration.
   - paired replacement (r=0.78): The design is a fixed computational protocol rather than a prospective clinical-style registration; the phrase "pre-registered" is avoided for that reason.
21. **[para @v10 L82 · ## 3. Forecast Models]** **Proposition 3.1 (Class reduction of M2m).
   - paired replacement (r=0.81): **Remark 3.1 (Class reduction of M2m).
22. **[para @v10 L84 · ## 4. Evaluation Design]** Secondary scores are mean absolute error and the Brier score for $\mathbf{1}\{\hat H < 660\}$, interpreted only for origins at or after 2007.
   - paired replacement (r=0.80): Secondary scores are mean absolute error and the Brier score for $\mathbf{1}\{\hat H < 660\}$, interpreted only for origins at or after 2007; for deterministic 0/1 forecasts this score is a misclassification rate.
23. **[para @v10 L84 · ## 3. Forecast Models]** *Proof.
   - weak pairing only (r=0.23): **Remark 3.1 (Class reduction of M2m).
24. **[para @v10 L84 · ## 3. Forecast Models]** * Substituting $\tilde R_{t+1}=\bar R$, $\tilde P_{t+1}=\bar P$ in Definition 3.1 gives $H_{t+1}=(1+\delta)H_t+(\alpha+\beta\bar R+\gamma\bar P)$, which is the affine AR(1) form $(1+\delta)H_t+\mathrm{const}$.
   - weak pairing only (r=0.27): The clause is in the frozen protocol document, but it is not in Definition 4.2; under the rule as written, M2m satisfies (H1) and (H2) at h = 1.
25. **[para @v10 L84 · ## 3. Forecast Models]** The estimator differs from M1: M2m pins its intercept and persistence from the in-sample mean fluxes, an additional identifying use of the recharge and pumpage records in training.
   - paired replacement (r=0.70): M2m pins its intercept from the in-sample mean fluxes, an additional identifying use of the recharge and pumpage records in training; the persistence coefficient $(1+\delta)$ is not mean-flux dependent.
26. **[para @v10 L84 · ## 3. Forecast Models]** □
   - no replacement sentence found in v11
27. **[para @v10 L88 · ## 4. Evaluation Design]** Rolling origin: minimum 15 training years; horizons h = 1 and h = 5; n = 75 and n = 71 origins respectively (the 15-year floor is the rolling rule; the fixed windows use their declared trains).
   - paired replacement (r=0.56): Rolling origin: minimum 15 training years; horizons h = 1 and h = 5; n = 75 and n = 71 origins respectively (every model in Tables 4 and 6 is scored on the identical origin sets; M2m uses the same n = 75 / n = 71).
28. **[para @v10 L88 · ## 3. Forecast Models]** The scoring protocols for the primary pass and the climate pass were frozen and dated (2026-08-25) before the corresponding RMSE tables were computed.
   - paired replacement (r=0.82): The scoring protocols for the primary pass and the climate pass were frozen and dated (2026-08-25) before the corresponding RMSE tables were computed, and are archived with the analysis code in the public repository.
29. **[para @v10 L88 · ## 3. Forecast Models]** The frozen protocol documents are archived with the analysis code.
   - paired replacement (r=0.43): Three protocol elements sit outside that rule and are therefore recorded here as deviations, in one place:
30. **[para @v10 L96 · ## 4. Evaluation Design]** **Definition 4.2 (Retention rule).
   - paired replacement (r=0.79): **Definition 4.2 (Retention rule, frozen verbatim).
31. **[para @v10 L104 · ### 5.2 Fixed windows]** The oracle (dashed) is diagnostic.
   - paired replacement (r=0.69): The oracle (dashed) is diagnostic and uses realized future R, P.
32. **[para @v10 L115 · ### 5.2 Fixed windows]** Bold marks the best model of the window; on the drawdown window the best causal model, M2, also beats the oracle.
   - paired replacement (r=0.58): Bold marks the lowest RMSE of the window including the diagnostic oracle.
33. **[para @v10 L115 · ### 5.2 Fixed windows]** The train-mean baseline is the best non-oracle forecast on the recovery window (14.07 ft) and on the critical-period era (14.77 ft), consistent with its rolling five-year win; the residual-persistence rungs M3/M4 track M2 on the drawdown (18.12/18.23 versus 18.11 ft); M4 is the best causal model on the pre-permit wet window (15.26 ft); and both fail with the causal family on the recovery and critical-period windows.
   - paired replacement (r=1.00): The train-mean baseline is the best non-oracle forecast on the recovery window (14.07 ft) and the critical-period era (14.77 ft), consistent with its rolling five-year win; the residual-persistence rungs M3/M4 track M2 on the drawdown (18.12/18.23 versus 18.11 ft); M4 is the best causal model on the pre-permit wet wind …[truncated]
34. **[para @v10 L117 · ### 5.2 Fixed windows]** The 1950s drawdown is a continuing low-recharge path: the last observed R is already low, so causal M2 has lower RMSE than persistence (18 versus 24 ft) and also lower RMSE than the oracle.
   - paired replacement (r=0.38): What the ladder actually shows is that persisting last year's recharge is the failure (Section 5.4: persisted-R RMSE 702 versus climatological 556 × 10³ acre-ft on the recharge target).
35. **[para @v10 L117 · ### 5.2 Fixed windows]** The linear map trained on 1934–1950 has the wrong sign on pumpage (γ = +0.021): pumping rose as the drought deepened, so pumpage is behaviorally coupled to recharge and the least-squares coefficient aliases the human response into the physical state transition — simultaneity bias; the short training window compounds the identification failure.
   - weak pairing only (r=0.31): On the drawdown window the bolded M2 is a continuing-drought artefact, not a forecasting merit: the last observed R is already low, and the map trained on 1934–1950 has the wrong sign on pumpage (γ =  …[truncated]
36. **[para @v10 L119 · ### 5.2 Fixed windows]** Causal M2 persists drought recharge and falls further (RMSE 55 ft).
   - paired replacement (r=0.90): Causal M2 persists drought recharge and falls further (RMSE 55 ft, into the clip).
37. **[para @v10 L119 · ### 5.2 Fixed windows]** Recoveries on this specification are recharge events, not autonomous mean reversion and not a change in the pumping regime.
   - paired replacement (r=0.48): Recoveries on this specification are recharge events, not autonomous mean reversion — although the training mean (mean reversion) scores 14.07 ft, second only to the oracle, in this institutionally bounded, rapidly recharged system.
38. **[para @v10 L140 · ### 5.3 Rolling origin]** ** Retention on rolling h = 1 RMSE.
   - paired replacement (r=0.76): **Retention verdict (rolling h = 1).
39. **[tablerow @v10 L142 · ### 5.3 Rolling origin]** | Model | Versus persist | Distinct structure | Decision |
   - paired replacement (r=0.88): | Model | vs persist | vs M1 | Distinct structure | Decision |
40. **[tablerow @v10 L144 · ### 5.3 Rolling origin]** | M1 | 12.84 < 13.23 | output only | retained (margin 0.39 ft) |
   - paired replacement (r=0.74): | M1 | 12.84 < 13.23 (−0.39) | — | output only | retained (point rule; margin within noise) |
41. **[tablerow @v10 L145 · ### 5.3 Rolling origin]** | M2 | 14.70 > 13.23 | causal fluxes | reject |
   - paired replacement (r=0.85): | M2 | 14.70 > 13.23 (+1.47) | +1.86 | causal fluxes | reject |
42. **[tablerow @v10 L146 · ### 5.3 Rolling origin]** | M2m | 12.28 < 13.23 | no (affine AR(1)) | list only; not extra structure |
   - paired replacement (r=0.62): | M2m | 12.28 < 13.23 (−0.95) | −0.56 | no (affine AR(1) function class) | listed; declined by protocol class clause |
43. **[tablerow @v10 L147 · ### 5.3 Rolling origin]** | M3, M4 | worse than persist | yes | reject |
   - paired replacement (r=0.92): | M3, M4 | worse than persist | worse | yes | reject |
44. **[tablerow @v10 L148 · ### 5.3 Rolling origin]** | M2_oracle | 7.55 | uses future R, P | excluded |
   - paired replacement (r=0.96): | M2_oracle | 7.55 | — | uses future R, P | excluded |
45. **[para @v10 L150 · ### 5.3 Rolling origin]** M2m is listed by the same rule and then declined on the class grounds fixed in the protocol (constant fluxes reduce the forecast equation to the affine AR(1)); its numerical advantage is estimator-level, as stated.
   - paired replacement (r=0.39): ** M2m is listed and then declined on class grounds (Remark 3.1).
46. **[para @v10 L150 · ### 5.3 Rolling origin]** The climate modules are the same story nested one level up: the combination (12.71 ft) loses to its own nested comparator M2m (12.28 ft) — the declined M2m still serving as the declared nested comparator for the climate rung (a protocol kink, acknowledged) — which is the clean rejection, and the point-RMSE listing alone would not decide it.
   - paired replacement (r=0.38): Third, the climate-gate margin (combo − M2m, +0.43 ft) is itself within noise: the climate rejection is a point-RMSE rule outcome, not a significance finding.
47. **[para @v10 L150 · ### 5.3 Rolling origin]** No stock-flow, residual, or delay module is retained.
   - paired replacement (r=0.38): At the decision scale of annual drought-stage declarations the difference is operationally nil.
48. **[para @v10 L154 · ### 5.3 Rolling origin]** Full-sample correlations: corr(H_t, H_{t−1}) = 0.64 with AR(1) coefficient φ̂ = 0.66; corr(R_t, R_{t−1}) = 0.17; corr(ΔH_t, R_t) = 0.74.
   - weak pairing only (r=0.31): The full-sample coefficients (β̂, γ̂) = (0.017, −0.026) differ from the pre-permit window's because the windows differ.
49. **[para @v10 L154 · ### 5.3 Rolling origin]** Full-sample (β̂, γ̂) = (0.017, −0.026) have the expected signs when the sample is long.
   - paired replacement (r=0.50): The full-sample coefficients (β̂, γ̂) = (0.017, −0.026) differ from the pre-permit window's because the windows differ.
50. **[para @v10 L154 · ### 5.3 Rolling origin]** The water-balance class is not empty, but recharge is not persistent.
   - paired replacement (r=0.42): The oracle (dashed) is diagnostic and uses realized future R, P.
51. **[para @v10 L156 · ### 5.3 Rolling origin]** On post-2007 origins only (n = 16, h = 1): persist 13.09, M1 12.16, M2 13.31, oracle 8.03 ft.
   - weak pairing only (r=0.33): M2 (14.70), M3 (14.46), and M4 (14.30) each fail (H1).
52. **[para @v10 L156 · ### 5.3 Rolling origin]** The ranking is unchanged.
   - paired replacement (r=0.55): Three readings.
53. **[para @v10 L156 · ### 5.3 Rolling origin]** The 660-ft Brier scores are 0.31 (persist), 0.25 (M1), and 0.19 (oracle).
   - paired replacement (r=0.38): **The struck sign-hit score** (Definition 4.1).
54. **[para @v10 L156 · ### 5.3 Rolling origin]** At h = 5 (n = 12): persist 25.10, M1 17.16, M2m 17.64, mean 16.41, M2/M3/M4 34.9–35.0, oracle 8.69 ft — the post-2007 h = 5 reversal of the M1–persistence ordering is reported without changing the one-year retention statement.
   - weak pairing only (r=0.33): At five years, the training mean (16.80 ft) beats persistence (21.11 ft) with an interval excluding zero.
55. **[para @v10 L156 · ### 5.3 Rolling origin]** The declared scoring choice at h = 5 compares a no-change persistence forecast with iterated model trajectories; the iterated affine analogue M2m (17.64 ft) sits with the mean.
   - paired replacement (r=0.40): A causal module was retained only if it beat both persistence and the next-simpler causal model under a scoring protocol frozen and dated before any score was computed.
56. **[para @v10 L156 · ### 5.3 Rolling origin]** The annual-mean proxy is not the 10-day rule.
   - paired replacement (r=0.39): **The M2m-as-comparator rule.
57. **[para @v10 L166 · ### 5.4 Climate-informed recharge]** ** Rolling RMSE, climate-informed recharge.
   - paired replacement (r=0.45): ** Rolling RMSE, climate-informed recharge (same origin sets as Table 4; margins vs M1 and vs the M2m gate both shown for the h = 1 column).
58. **[para @v10 L166 · ### 5.3 Rolling origin]** **Proposition 5.1 (Retention verdict on rolling h = 1 RMSE).
   - paired replacement (r=0.72): **Retention verdict (rolling h = 1).
59. **[para @v10 L166 · ### 5.3 Rolling origin]** ** Under the retention rule of Definition 4.2 applied to Table 4, the verdicts of Table 5 hold: M1 is retained (margin 0.39 ft, output-only); M2, M3, and M4 are rejected; M2m is listed but declined on class grounds (Proposition 3.1); M2_oracle is excluded.
   - weak pairing only (r=0.32): ** Rolling RMSE, climate-informed recharge (same origin sets as Table 4; margins vs M1 and vs the M2m gate both shown for the h = 1 column).
60. **[tablerow @v10 L168 · ### 5.4 Climate-informed recharge]** | Model | H, h=1 (ft) | H, h=5 (ft) | R, h=1 (10³ acre-ft) |
   - paired replacement (r=0.89): | Model | H, h=1 (ft) | margin vs M1 | H, h=5 (ft) | R, h=1 (10³ acre-ft) |
61. **[para @v10 L168 · ### 5.3 Rolling origin]** * Apply (H1) and (H2) of Definition 4.2 to the h = 1 column of Table 4.
   - paired replacement (r=0.38): **Definition 4.2 (Retention rule, frozen verbatim).
62. **[para @v10 L168 · ### 5.3 Rolling origin]** M1 satisfies (H1): 12.84 < 13.23; as the simplest autonomous causal model it has no next-simpler causal comparator, so (H2) is vacuous and M1 is retained.
   - paired replacement (r=0.77): ** Applying Definition 4.2 to the h = 1 column of Table 4: M1 satisfies (H1) (12.84 < 13.23); as the simplest autonomous model it has no next-simpler causal comparator, so (H2) is vacuous and M1 is retained by the point rule.
63. **[para @v10 L168 · ### 5.3 Rolling origin]** M2 fails (H1): 14.70 > 13.23.
   - paired replacement (r=0.39): | M2 | 14.70 > 13.23 (+1.47) | +1.86 | causal fluxes | reject |
64. **[para @v10 L168 · ### 5.3 Rolling origin]** M3 (14.46) and M4 (14.30) fail (H1) relative to persist (13.23).
   - paired replacement (r=0.61): M2 (14.70), M3 (14.46), and M4 (14.30) each fail (H1).
65. **[para @v10 L168 · ### 5.3 Rolling origin]** M2m satisfies (H1): 12.28 < 13.23, but by Proposition 3.1 its forecast function reduces to the affine AR(1) class, so it is listed and then declined on class grounds.
   - paired replacement (r=0.49): | M2m | 12.28 < 13.23 (−0.95) | −0.56 | no (affine AR(1) function class) | listed; declined by protocol class clause |
66. **[para @v10 L168 · ### 5.3 Rolling origin]** M2_oracle (7.55) is excluded by Definition 4.2 as a diagnostic oracle using future R, P. □
   - paired replacement (r=0.67): M2_oracle is excluded as a diagnostic oracle.
67. **[tablerow @v10 L170 · ### 5.4 Climate-informed recharge]** | persist H / persist R | 13.23 | **21.11** | 702 |
   - paired replacement (r=0.92): | persist H / persist R | 13.23 | +0.39 | **21.11** | 702 |
68. **[para @v10 L170 · ### 5.3 Rolling origin]** The margin is 0.39 ft on n = 75 and is not a significance claim.
   - paired replacement (r=0.41): Third, the climate-gate margin (combo − M2m, +0.43 ft) is itself within noise: the climate rejection is a point-RMSE rule outcome, not a significance finding.
69. **[para @v10 L170 · ### 5.3 Rolling origin]** Mean absolute error is a tie (M1 10.72 versus persist 10.73 ft), and at h = 5 M1 (21.25 ft) does not beat persistence (21.11 ft) while the training mean (16.80 ft) beats both.
   - paired replacement (r=0.56): The margin is 0.39 ft on n = 75 and is not a significance claim; its bootstrap interval covers zero (Section 5.3.1), MAE is a tie (10.72 versus 10.73 ft), and at h = 5 M1 (21.25 ft) does not beat persistence (21.11 ft) while the training mean (16.80 ft) beats both.
70. **[para @v10 L170 · ### 5.3 Rolling origin]** The retention is therefore explicitly a one-year, RMSE-level statement.
   - paired replacement (r=0.48): The retention is therefore explicitly a one-year, RMSE-level statement — provisional, a coin-flip recorded by a point rule — and it records a slightly mean-reverting head series, not a confirmation of stock-flow structure.
71. **[para @v10 L170 · ### 5.3 Rolling origin]** It records a slightly mean-reverting head series, not a confirmation of stock-flow structure, and at the decision scale of annual drought-stage declarations the difference is operationally nil.
   - paired replacement (r=0.65): At the decision scale of annual drought-stage declarations the difference is operationally nil.
72. **[tablerow @v10 L171 · ### 5.4 Climate-informed recharge]** | M1 | 12.84 | 21.25 | — |
   - paired replacement (r=0.93): | M1 | 12.84 | — | 21.25 | — |
73. **[tablerow @v10 L172 · ### 5.4 Climate-informed recharge]** | M2_Rar | 13.25 | 25.38 | 561 |
   - paired replacement (r=0.89): | M2_Rar | 13.25 | +0.41 | 25.38 | 561 |
74. **[para @v10 L172 · ### 5.3 Rolling origin]** **Proposition 5.2 (Five-year climatology).
   - paired replacement (r=0.42): The frozen retention rule is Definition 4.2, verbatim above.
75. **[para @v10 L172 · ### 5.3 Rolling origin]** ** At h = 5 the training mean (16.80 ft) has lower RMSE than persistence (21.11 ft).
   - paired replacement (r=0.65): At five years, the training mean (16.80 ft) beats persistence (21.11 ft) with an interval excluding zero.
76. **[tablerow @v10 L173 · ### 5.4 Climate-informed recharge]** | M2_Renso | 12.82 | 24.42 | 528 |
   - paired replacement (r=0.89): | M2_Renso | 12.82 | −0.02 | 24.42 | 528 |
77. **[tablerow @v10 L174 · ### 5.4 Climate-informed recharge]** | M2_Rprecip | 12.80 | 25.38 | 545 |
   - paired replacement (r=0.90): | M2_Rprecip | 12.80 | −0.04 | 25.38 | 545 |
78. **[para @v10 L174 · ### 5.3 Rolling origin]** * Read from Table 4: $\mathrm{RMSE}_{h=5}(\text{mean}) = 16.80 < 21.11 = \mathrm{RMSE}_{h=5}(\text{persist})$.
   - weak pairing only (r=0.29): ** Retention on rolling h = 1 RMSE (point rule; margins vs persist and vs M1 both shown).
79. **[tablerow @v10 L175 · ### 5.4 Climate-informed recharge]** | M2_combo | 12.71 | 26.88 | 538 |
   - paired replacement (r=0.89): | M2_combo | 12.71 | −0.13 | 26.88 | 538 |
80. **[tablerow @v10 L176 · ### 5.4 Climate-informed recharge]** | rain climatology | — | — | 556 |
   - paired replacement (r=0.94): | rain climatology | — | — | — | 556 |
81. **[para @v10 L176 · ### 5.3 Rolling origin]** Five-year forecasts on this basin are climatology, not last value and not persisted recharge.
   - paired replacement (r=0.42): A mid-year nowcast would require a new evaluation protocol.
82. **[tablerow @v10 L177 · ### 5.4 Climate-informed recharge]** | rain oracle | 10.56 | 16.91 | **354** |
   - paired replacement (r=0.95): | rain oracle | 10.56 | — | 16.91 | **354** |
83. **[para @v10 L181 · ### 5.4 Climate-informed recharge]** Lagged precipitation and September–November Niño 3.4 have modest skill on R relative to climatology (528–545 versus 556 × 10³ acre-ft), and they do not constitute forecast structure on head: the point-RMSE rule lists ENSO, lagged precipitation, and the combination (each less than persist and less than M1), but the margins versus M1 are 0.02, 0.04, and 0.13 ft; at h = 5 all three have RMSE 3–6 ft higher than persistence (the h > 1 climate scores reuse the one-step recharge forecast, held constant over the horizon); and they are M2m with a weakly adjusted intercept.
   - paired replacement (r=0.56): Lagged precipitation and September–November Niño 3.4 have modest skill on R relative to climatology (528–545 versus 556 × 10³ acre-ft), and they do not constitute forecast structure on head: the point-RMSE rule lists ENSO, lagged precipitation, and the combination — each beats persist and M1 by margins of 0.02, 0.04, a …[truncated]
84. **[para @v10 L185 · ### 5.4 Climate-informed recharge]** On the recharge target itself the fixed-window scores are an order of magnitude coarser on every window (climate modules 199–937; precipitation oracle 80.7–487, against the 556 × 10³ acre-ft climatology scale of the rolling record), so the marginal head advantage is a window-specific result, not a recharge forecast.
   - paired replacement (r=0.95): On the recharge target itself the fixed-window scores are an order of magnitude coarser on every window (climate modules 199–937; precipitation oracle 80.7–487, against the 556 × 10³ acre-ft climatology scale of the rolling record), so the marginal head advantage is a window-specific result, not a recharge forecast, an …[truncated]
85. **[para @v10 L193 · ### 5.5 The service series after the retention freeze]** The service series is a measured channel of the same state — a measured service, not an independent information source.
   - paired replacement (r=0.94): The service series is a measured rating curve of the same state — a measured service, not an independent information source.
86. **[para @v10 L195 · ### 5.5 The service series after the retention freeze]** The fitted map does not track the drought-of-record: at the 1956 annual mean (623.15 ft) it reads ≈97 cfs against an observed ≈32 cfs annual mean, so the Comal score is informative about information redundancy at ordinary heads, not about the drought tail.
   - paired replacement (r=0.39): The channel fails in the drought tail, and the direction matters: at the 1956 annual mean (623.15 ft) it reads ≈97 cfs against an observed ≈32 cfs annual mean — it predicts non-cessation — and its zero-discharge level (2876/4.77 ≈ 602.9 ft) lies below every observed head (daily minimum 612.5 ft), so the map never predi …[truncated]
87. **[para @v10 L195 · ### 5.5 The service series after the retention freeze]** The fitted intercept implies zero discharge near 603 ft (2876/4.77 ≈ 602.9), below the ≈618 ft reference — the linear map itself predicts the 1956 tail failure, a consequence of the intercept not noted elsewhere.
   - weak pairing only (r=0.32): The service series is a measured rating curve of the same state — a measured service, not an independent information source.
88. **[para @v10 L195 · ### 5.5 The service series after the retention freeze]** One-year Comal RMSE (cfs): persist 71.9, M1 69.0, M2m 68.7, M2 74.8, M3 73.8, M4 73.4, train-mean 89.7, oracle 45.3.
   - paired replacement (r=0.56): One-year Comal RMSE (cfs), constructed by scoring the same ladder directly on the Comal series over the same rolling origins (n = 75): persist 71.9, M1 69.0, M2m 68.7, M2 74.8, M3 73.8, M4 73.4, train-mean 89.7, oracle 45.3 — the ranking mirrors the head ranking, as it must for a linear channel.
89. **[para @v10 L197 · ### 5.5 The service series after the retention freeze]** Gravimetric storage or the J-27 Uvalde index would be different objects, not a second fibre of this specification.
   - paired replacement (r=0.92): Gravimetric storage or the J-27 Uvalde index would be different objects, not a second observation channel of this specification.
90. **[para @v10 L207 · ### 5.4 Climate-informed recharge]** **Proposition 5.3 (Climate-informed rejection).
   - paired replacement (r=0.38): **Definition 4.2 (Retention rule, frozen verbatim).
91. **[para @v10 L207 · ### 5.4 Climate-informed recharge]** ** Under the retention rule of Definition 4.2 applied to Table 6, no climate-informed recharge module is retained.
   - paired replacement (r=0.43): The frozen retention rule is Definition 4.2, verbatim above.
92. **[para @v10 L209 · ### 5.4 Climate-informed recharge]** * At h = 1, the climate variants M2_Renso (12.82), M2_Rprecip (12.80), and M2_combo (12.71) each satisfy (H1) relative to persist (13.23) but fail (H2) relative to their next-simpler causal comparator M2m (12.28): 12.82 > 12.28, 12.80 > 12.28, 12.71 > 12.28.
   - weak pairing only (r=0.32): Third, the direction is right and the magnitude modest: the 20% cut raises the simulated 2023 head by 5.2 ft (646.8 − 641.6) relative to the actual-pumpage path.
93. **[para @v10 L209 · ### 5.4 Climate-informed recharge]** M2_Rar (13.25) fails (H1) outright.
   - paired replacement (r=0.45): | M2_Rar | 13.25 | +0.41 | 25.38 | 561 |
94. **[para @v10 L209 · ### 5.4 Climate-informed recharge]** At h = 5, all climate variants exceed persistence (21.11 ft) and so fail (H1).
   - paired replacement (r=0.47): At five years, the training mean (16.80 ft) beats persistence (21.11 ft) with an interval excluding zero.
95. **[para @v10 L209 · ### 5.4 Climate-informed recharge]** The precipitation oracle (10.56 ft) is excluded by Definition 4.2 as a diagnostic oracle using year $t+h$ precipitation.
   - paired replacement (r=0.51): M2_oracle is excluded as a diagnostic oracle.
96. **[para @v10 L212 · ### 5.6 Pumpage counterfactuals]** First, pumpage is a secondary lever in this map: the full spread of counterfactual policies — from a 20% cut below actual to freezing at the 1990 peak — spans 630.9–646.8 ft at 2023 — a 16-ft spread around the observed 635.7 ft — and the map's own RMSE against the observed record (7.2–14.2 ft) is of the same order as the policy spread itself.
   - paired replacement (r=0.82): First, pumpage is a secondary lever in this map: the full spread of counterfactual policies — from a 20% cut below actual to freezing at the 1990 peak — spans 630.9–646.8 ft at 2023, and the map's own RMSE against the observed record (7.2–14.2 ft) is of the same order as the policy spread itself; the 5-ft effects below …[truncated]
97. **[para @v10 L212 · ### 5.6 Pumpage counterfactuals]** Second, the actual-pumpage path remains the closest to the observed record of the four scenarios — the counterfactuals do not repair the ladder's primary failure, which Section 5.3 traces to the recharge series' persistence failure (five-year forecasts are climatology), a timing-side property the pumpage scenarios do not touch.
   - paired replacement (r=0.41): Second, the 20%-cut path is the closest to the observed record of the four scenarios (7.19 versus 8.56 ft) — an artefact of the map running high on this window (the actual-pumpage path ends 5.9 ft above the observed 2023 head), not evidence that the Authority's pumpage was near-optimal; the counterfactuals do not repai …[truncated]
98. **[para @v10 L212 · ### 5.6 Pumpage counterfactuals]** Third, the direction is right and the magnitude modest: the 20% cut raises the simulated 2023 head by 5.1 ft relative to the actual-pumpage path.
   - paired replacement (r=0.94): Third, the direction is right and the magnitude modest: the 20% cut raises the simulated 2023 head by 5.2 ft (646.8 − 641.6) relative to the actual-pumpage path.
99. **[para @v10 L212 · ### 5.6 Pumpage counterfactuals]** Fourth, the recharge coefficient dominates the map (a 1000 × 10³ acre-ft recharge difference moves the head by roughly 17.5 ft at the coefficient, against −0.031 ft per 10³ acre-ft of pumpage), the model-level restatement of the ladder's central finding that the identified driver is not persistent at the annual forecast origin.
   - weak pairing only (r=0.35): Fourth, the recharge coefficient dominates the map through its range, not its magnitude: a 1000 × 10³ acre-ft recharge difference moves the head by roughly 17.5 ft at the pre-permit coefficient (β̂ ≈  …[truncated]
100. **[para @v10 L216 · ## 6. Discussion]** The identified driver has the wrong timing for an annual origin — the same pattern a companion evaluation finds on Northern cod, where a more accurate catch series does not rescue constant-productivity surplus production.
   - paired replacement (r=0.37): Post-freeze objects, labelled as such: the climate-pass fixed-window scores, the pumpage counterfactuals of Section 5.6, the Comal service-series scoring, and the uncertainty layer of Section 5.3.1.
101. **[para @v10 L218 · ## 6. Discussion]** Second, the horizon contrast: no benchmark study of this basin reports that a training mean beats persistence at a longer horizon.
   - paired replacement (r=0.96): Second, the horizon contrast: no benchmark study of this basin reports a training mean beating persistence at a longer horizon.
102. **[para @v10 L218 · ## 6. Discussion]** The five-year climatology result (16.80 versus 21.11 ft) is the specification's most directly transferable finding for management planning that keys on multi-year outlooks.
   - paired replacement (r=0.54): The five-year climatology result (16.80 versus 21.11 ft) is the specification's most directly transferable candidate for management planning that keys on multi-year outlooks, with the scope stated: the San Antonio Pool is a rapidly recharged, institutionally bounded system, so the training mean is informative at long h …[truncated]
103. **[para @v10 L220 · ## 6. Discussion]** What the design shows is that at the annual origin, the information carried by such a map is timing-bound: the same structure that cannot forecast next year certifies this year — the water-balance map is a certificate for a year whose recharge is already known, not a forecast.
   - paired replacement (r=0.41): What the design shows is that at the annual origin, the information carried by such a map is timing-bound: with realized fluxes the same map is a nowcast of the year's head (7.55 ft RMSE), and the contemporaneous increment ΔH_t against R_t (r = 0.74) is the closure statement; the word "certificate" is retired for both.
104. **[para @v10 L220 · ## 6. Discussion]** The five-year climatology win is setting-specific in the same way: the San Antonio Pool is a rapidly recharged, institutionally bounded system — karst recharge and EAA critical-period limits hold the head within a band — so the training mean is informative at long horizons, and a non-stationary fossil aquifer under sustained depletion would not sustain a mean-reverting baseline; the climatology result is not claimed for such settings.
   - weak pairing only (r=0.28): First, the retention margin itself (M1 − persist, 0.39 ft) is within noise, as is the M2m-over-M1 estimator margin and the M2 causal loss (the last only borderline, its interval touching zero).
105. **[para @v10 L220 · ## 6. Discussion]** The retained AR(1) admits a complementary reading: to first order, spring discharge obeys Darcy proportionality to head above the spring level, and the autonomous solution of that drainage law is an affine autoregression $H_{t+1} \approx (1-k)H_t + k H_s$; the fitted $\hat\varphi = 0.66$ is consistent with a drainage-decay coefficient $\hat k \approx 0.34$ yr⁻¹.
   - paired replacement (r=0.87): The retained AR(1) admits a complementary reading: to first order, spring discharge obeys Darcy proportionality to head above the spring level, and the autonomous solution of that drainage law is an affine autoregression $H_{t+1} \approx (1-k)H_t + k H_s$; the fitted $\hat\varphi = 0.66$ (the M1 estimate; the full-samp …[truncated]
106. **[para @v10 L220 · ## 6. Discussion]** The module is output-only in the protocol's sense — no flux data enter the forecast — but the shape it fits carries the aquifer's own free-drainage momentum.
   - paired replacement (r=0.83): The module is output-only in the protocol's sense — no flux data enter the forecast — but the shape it fits carries the aquifer's own free-drainage momentum; this is an interpretation in discussion, not a retention reason.
107. **[para @v10 L223 · ### 5.5 The service series after the retention freeze]** **Proposition 5.4 (Comal as a measured channel of head).
   - paired replacement (r=0.44): **The Comal channel (rating-curve reading).
108. **[para @v10 L223 · ### 5.5 The service series after the retention freeze]** The full-sample contemporaneous correlation is r = 0.986.
   - paired replacement (r=0.46): The full-sample contemporaneous correlation is r = 0.986; the 1934–1950 fit is quoted because the channel is used on that train, and the full-sample correlation is the redundancy statement.
109. **[para @v10 L224 · ## 6. Discussion]** Two-pool exchange, solute, and barrier bookkeeping were not fitted and cannot be retained.
   - paired replacement (r=0.47): A two-pool exchange module was specified and not fitted; no barrier or exchange term was fitted.
110. **[para @v10 L224 · ## 6. Discussion]** In the two-pool parameterization the relative-exchange term is removed, leakage is not applicable, and no barrier or exchange term is fitted; the blocking list is not closed by this paper.
   - paired replacement (r=0.52): A two-pool exchange module was specified and not fitted; no barrier or exchange term was fitted.
111. **[para @v10 L226 · ## 6. Discussion]** Neither series is head.
   - paired replacement (r=0.44): Neither series is head: R and P are constructed fluxes, not observations of J-17.
112. **[para @v10 L226 · ## 6. Discussion]** M4 is a one-year information delay, not a conservative filter; J-17 is a telemetered gauge whose head is recorded daily, so the module is kept in the ladder for symmetry with the companion fisheries evaluation and prices a theoretical information lag rather than a constraint of this system's monitoring.
   - paired replacement (r=0.70): M4 is a one-year information delay and a symmetry control with the companion fisheries evaluation — J-17 is a telemetered gauge whose head is recorded daily, so the module prices a theoretical information lag rather than a constraint of this system's monitoring.
113. **[para @v10 L226 · ## 6. Discussion]** The sample is 90 years with four short test windows, and the 0.39-ft AR(1) margin is not a significance claim.
   - paired replacement (r=0.84): The sample is 90 years with four short test windows, and the 0.39-ft AR(1) margin is not a significance claim (Section 5.3.1: its interval covers zero).
114. **[para @v10 L226 · ## 6. Discussion]** Reopening the climate module with additional indices (PDO, AMO) on this annual origin would re-instantiate the rejected structure; a mid-year nowcast would require a new evaluation protocol.
   - paired replacement (r=0.47): A mid-year nowcast would require a new evaluation protocol.
115. **[para @v10 L230 · ## 7. Conclusions]** On locked J-17 annual-mean head, last-value persistence is more accurate than a causal one-pool balance that persists last year's recharge.
   - paired replacement (r=0.72): On locked J-17 annual-mean head, last-value persistence is more accurate than a causal one-pool balance that persists last year's recharge, because annual recharge is near-white (r = 0.17) while the contemporaneous increment tracks it (r = 0.74).
116. **[para @v10 L230 · ## 7. Conclusions]** Univariate AR(1) improves one-year RMSE by 0.39 ft and is retained as an output-only model.
   - paired replacement (r=0.38): Bold marks the lowest RMSE of the window including the diagnostic oracle.
117. **[para @v10 L230 · ## 7. Conclusions]** The same balance, given realized recharge and pumpage, cuts error nearly in half; climate variables known at the annual origin do not recover that gap; and at five years, climatology wins.
   - paired replacement (r=0.71): The same balance, given realized recharge and pumpage, nowcasts the current year (7.55 ft, a 43% reduction); climate variables known at the annual origin do not recover that gap; and at five years, climatology wins, robustly (16.80 versus 21.11 ft, interval excluding zero).

## Transition v11 → v12 — 12 dropped (8 modified-with-replacement r≥0.55, 4 no-close-replacement)

> v12 version log: *Version log (v12).* Registers the owner-supplied independent replication of the post-freeze uncertainty layer and resolves the climate-comparator kink against the frozen protocol document. Non-destructive: no frozen verdict, no reported score, and no archived number changes. (1) The climate rung's comparator is corrected to the frozen Pass-2 protocol's own statement — the climate question is whether a causal recharge forecast reduces J-17 RMSE "relative to persistence and relative to M1". Earlier versions (v10 and v11) declared the declined M2m as the rung's (H2) comparator; that declaration was inconsistent with the frozen document and circular in exactly the way the external audit identified (the gate was a model the protocol had itself declined). The retention verdict — no climate module retained — is unchanged under either statement, but the stated mechanism is corrected (Sections 4…

1. **[listitem @v11 L107 · ### 4.1 Protocol record and deviations]** **The M2m-as-comparator rule.
   - paired replacement (r=0.48): **The climate-rung comparator (corrected in this version).
2. **[listitem @v11 L107 · ### 4.1 Protocol record and deviations]** ** The climate rung's (H2) comparator is M2m — a model the protocol declines (a protocol kink).
   - paired replacement (r=0.46): **The climate-rung comparator (corrected in this version).
3. **[listitem @v11 L107 · ### 4.1 Protocol record and deviations]** Section 5.4 therefore reports the climate margins against both M2m and M1.
   - paired replacement (r=0.37): The correction changes no frozen verdict — no climate module is retained under either statement — but it corrects the stated mechanism.
4. **[para @v11 L110 · ### 4.1 Protocol record and deviations]** Post-freeze objects, labelled as such: the climate-pass fixed-window scores, the pumpage counterfactuals of Section 5.6, the Comal service-series scoring, and the uncertainty layer of Section 5.3.1.
   - paired replacement (r=0.87): Post-freeze objects, labelled as such: the climate-pass fixed-window scores, the pumpage counterfactuals of Section 5.6, the Comal service-series scoring, and the uncertainty layer of Section 5.3.1 together with its independent replication (Section 5.3.1).
5. **[para @v11 L178 · ### 5.3.1 Uncertainty on the retention margins (post-freeze layer)]** A post-freeze uncertainty layer attaches Diebold–Mariano tests (Newey–West HAC, lag h − 1) and moving-block bootstrap intervals (block length 8, 10,000 replications, seeded) to every load-bearing margin, computed from the archived per-origin forecast files.
   - paired replacement (r=0.93): A post-freeze uncertainty layer attaches Diebold–Mariano tests (Diebold and Mariano 1995; Newey–West HAC, lag h − 1) and moving-block bootstrap intervals (Künsch 1989; block length 8, 10,000 replications, seeded) to every load-bearing margin, computed from the archived per-origin forecast files.
6. **[tablerow @v11 L189 · ### 5.3.1 Uncertainty on the retention margins (post-freeze layer)]** | M2_combo − M2m (climate gate) | +0.43 | +0.74 | 0.46 | [−0.56, +1.57] | no |
   - paired replacement (r=0.87): | M2_combo − M2m (nested baseline) | +0.43 | +0.74 | 0.46 | [−0.56, +1.57] | no |
7. **[para @v11 L191 · ### 5.3.1 Uncertainty on the retention margins (post-freeze layer)]** Third, the climate-gate margin (combo − M2m, +0.43 ft) is itself within noise: the climate rejection is a point-RMSE rule outcome, not a significance finding.
   - paired replacement (r=0.93): Third, the nested-baseline margin (combo − M2m, +0.43 ft) is itself within noise: the climate rejection is a point-RMSE rule outcome, not a significance finding.
8. **[para @v11 L201 · ### 5.4 Climate-informed recharge]** ** Rolling RMSE, climate-informed recharge (same origin sets as Table 4; margins vs M1 and vs the M2m gate both shown for the h = 1 column).
   - paired replacement (r=0.87): ** Rolling RMSE, climate-informed recharge (same origin sets as Table 4; margins vs M1 — the frozen Pass-2 gate — and vs the nested M2m baseline both shown for the h = 1 column).
9. **[para @v11 L217 · ### 5.4 Climate-informed recharge]** Lagged precipitation and September–November Niño 3.4 have modest skill on R relative to climatology (528–545 versus 556 × 10³ acre-ft), and they do not constitute forecast structure on head: the point-RMSE rule lists ENSO, lagged precipitation, and the combination — each beats persist and M1 by margins of 0.02, 0.04, and 0.13 ft, all within noise (Section 5.3.1) — but each fails (H2) against the declared nested comparator M2m (12.28 ft), whose own margin over them (+0.43 ft for the combination) is also within noise.
   - paired replacement (r=0.53): Lagged precipitation and September–November Niño 3.4 have modest skill on R relative to climatology (528–545 versus 556 × 10³ acre-ft), and they do not constitute forecast structure on head.
10. **[para @v11 L217 · ### 5.4 Climate-informed recharge]** The rejection is therefore honest only with both margins visible: the climate modules beat persistence and the AR(1) by at most 0.13 ft and lose to climatological fluxes; none is retained, and nothing in that verdict is a significance finding.
   - paired replacement (r=0.96): The rejection is therefore honest with both readings visible: the climate modules beat persistence and the AR(1) by at most 0.13 ft and lose to climatological fluxes; none is retained, and nothing in that verdict is a significance finding.
11. **[para @v11 L217 · ### 5.4 Climate-informed recharge]** At h = 5 all three have RMSE 3–6 ft higher than persistence (the h > 1 climate scores reuse the one-step recharge forecast, held constant over the horizon, so this is a design consequence, not a multi-year climate test); structurally they are M2m with a weakly adjusted intercept.
   - paired replacement (r=0.62): None is retained, on three stated grounds: the margins against the gate are within noise; at h = 5 all three have RMSE 3–6 ft higher than persistence (the h > 1 climate scores reuse the one-step recharge forecast, held constant over the horizon, so this is a design consequence, not a multi-year climate test); and struc …[truncated]
12. **[para @v11 L218 · ## 6. Discussion]** First, the retention gate: GEMS-GER ships three benchmark models and reports the fraction of wells for which the best one reaches NSE > 0.5 (Ohmer et al. 2026), and the karst benchmark of Zhu et al. (2026) ranks nine architectures by RMSE and R² — both compare model families against one another, while here every module must beat persistence and the next-simpler causal model under a rule frozen before scoring, and on that rule the entire causal ladder is rejected at the one-year horizon.
   - paired replacement (r=0.84): First, the retention gate: GEMS-GER ships three benchmark models and reports the fraction of wells for which the best one reaches NSE > 0.5 (Ohmer et al. 2026), and the karst benchmark of Zhu et al. (2026) ranks nine architectures by RMSE and R² — both compare model families against one another, while here every module …[truncated]

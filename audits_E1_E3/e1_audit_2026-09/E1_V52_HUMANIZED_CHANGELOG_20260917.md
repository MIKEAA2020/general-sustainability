# E1 v52 humanized changelog (2026-09-17)

Basis: joint evaluation of the Grok and Claude E1 audits
(E1_HUMANIZED_JOINT_EVALUATION_20260917.md); style per standing directive
(framework/STYLE_DIRECTIVE_GEMINI_TONE_20260917.md), Gemini-weighted with
accuracy firewall.

Implemented (W1, textual — no frozen numbers altered):
- Abstract restructured: obstruction upfront (Grok #1), origin-matched B figure
  given first (84 vs 120; mixed 88 disclosed as training-window artefact),
  rolling-origin qualifiers at every verdict (Claude A6), freeze phrasing
  honest (audits' item 11), keyword "recruitment forecasting" corrected.
- Brier/direction 0.00-convention stated at first use (items 7).
- Collapse catch run labelled policy-as-exogenous at first mention (item 14).
- M4 decomposition restated with corrected labels: delay cost 86 kt vs
  model-given-delay 12 kt; h=5 note 694 kt compounding through dynamics
  (item 9) — reading checkpoint: 184-98=86, 196-184=12, per archived rows.
- Rose (2026) status footnote (item 10); Table 1 phrase discipline (item 12).
- Log-RMSE / floor counts flagged as deferred reporting (item 12-class).
- Machine-layer sentence tightened (item 13).

Deliberately NOT implemented (W2, owner-gated scientific): Prop 4.1
restatement (Claude A1 flip-bifurcation critique — the strongest scientific
finding in the audit pair), Lemma 3.2 demotion (A2), box-prior sensitivity
acknowledgement as prior (A3 kernel), regularised M1 / score-range reporting
(A5), drift/damped-trend baseline (E7), LOO influence computation (E8),
Schijns-vs-STATLANT retitling of the annual pass (A10).

Refuted-closed items (no action beyond documentation): identical M1/M1b rows
(A4 — archived differences <=0.04 kt round-identically); K-bound "violation"
(A3 as stated — declared bound is [max_train S+10, 5000]).

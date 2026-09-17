# Standing Style Directive — Gemini-Weighted Tone, With Accuracy Firewall (2026-09-17)

Owner directive (this turn): adopt Gemini's writing and tone universally across
the papers, while ensuring accurate, error-free delivery. Ratified here as the
standing convention for every *new version* of every paper (E1, E3, F1),
effective from E1 v52 forward. Frozen versions are never retro-edited.

## 1. What is adopted from the Gemini rewrite (verified strengths, V11 evaluation)

From `framework/JOINT_EVALUATION_HUMANIZED_REWRITES_V11.md`, Gemini's humanized
rewrite of the framework paper was the more readable of the two submitted. The
mechanics that made it readable, adopted:

1. **Topic sentences.** Every paragraph opens with its claim; support follows.
2. **Numbered moves.** Sequential, explicit signposting ("(1) ... (2) ... (3)")
   where the argument has steps.
3. **Short declaratives.** Sentences carry one idea; em-dash chains broken.
4. **Plain words first.** Technical terms defined at first use; no synonym
   rotation for precision terms (persistence, tie band, comparator, vintage,
   conditional hindcast are fixed vocabulary).
5. **Transition paragraphs at section joints.** One or two sentences that tell
   the reader why the next section exists.
6. **Honest-status phrases.** Conventions, limitations, and rule-version
   differences are stated as facts in the main flow, not buried in footnotes.

## 2. The accuracy firewall (verified Gemini failure modes, V11 evaluation)

The same evaluation found Gemini's rewrite *drifted*: fabricated companion
titles, swapped Zenodo labels (E1/E3), swapped Carvalho/Kell references,
changed the M4 paper's method count, and introduced unarchived numbers
(M1 CI [−0.954, +0.180], oracle 10.865, 612.5 ft). For every future version the
following are hard rules, numbered by the incident that motivates them:

1. **Numbers come from the claims ledger or the frozen text only.** No
   re-computation, no "nicer" rounding, no numbers that do not exist in an
   archived artifact.
2. **References are frozen strings.** Titles, author lists, DOIs, and method
   counts copy verbatim from the owning paper's frozen reference list.
   (Precedent: M4 = 61 methods, not 54 — Gemini's correction kept because it
   was *right*; the block otherwise frozen.)
3. **No retitling of cited works, companions, or tables.** Identifiers follow
   the owning artifact.
4. **No scientific-content repair inside a prose pass.** Prop-4.1-class issues
   route to owner-gated scientific waves (see E1 joint evaluation, W2), never
   to a language edit.
5. **Status honesty is part of tone.** Where the ledger marks rows `parked`
   or `pending_campaign`, prose says so in plain words. Provisional targets
   are labelled provisional.

## 3. Error-free delivery checklist (run on every new version before push)

- [ ] Every numeric token traceable to a ledger row or frozen line (spot-check
      the abstract and the first three paragraphs — the highest-visibility zone).
- [ ] Citation strings diff-clean against the frozen reference list.
- [ ] No claim stronger than its evidence class (rolling-origin qualifiers,
      conditional-hindcast qualifier, rule-version labels).
- [ ] New file only; frozen siblings untouched (git file list = additions).
- [ ] Changelog entry: what was adopted, what was deliberately NOT adopted,
      and which audit items remain open.

## 4. Scope

Applies to: future E1 versions (from v52), future E3 versions, future F1
versions, all evaluation/implementation memos. Does not apply to: frozen
artifacts, archived data, result JSON/CSV, or the ledger itself (append-only,
fact-only register).

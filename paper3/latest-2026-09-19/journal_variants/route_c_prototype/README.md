# Route-C typed-ledger prototype

This is a small, dependency-free reference implementation created alongside the journal-specific drafts. It implements and tests the core declaration layer:

- typed compartments and explicit transfer/conversion declarations;
- incidence construction;
- one-step balance residuals;
- componentwise barrier checks;
- a reproducible non-compensation witness.

Run:

```sh
python3 -m pytest -q
```

The prototype is **not yet a journal-ready software package**. It does not claim to implement all eight certification predicates, the admissible-flux linear programmes, a solver interface, trajectory integration, a public-data ingestion layer, or numerical validation against independent implementations. Those are the remaining route-C work items. The correct software claim at this stage is “reference prototype accompanying the formal framework”, not “supported package”.

The prototype's tests are deliberately small and hand-checkable. A submission-quality version would add a documented input schema, package metadata, versioned API, example ledger file, continuous tests, solver/alternative-route agreement, failure fixtures, runtime benchmarks and licence documentation.

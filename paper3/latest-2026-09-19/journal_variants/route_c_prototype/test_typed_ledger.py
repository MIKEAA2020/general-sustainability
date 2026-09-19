from typed_ledger import Compartment, Flux, LedgerError, TypedLedger, aggregate, compensating_witness


def test_same_type_transfer_incidence_and_balance():
    ledger = TypedLedger(
        [Compartment("source", "water", "m3"), Compartment("sink", "water", "m3")],
        [Flux("pump", "source", "sink")],
    )
    assert ledger.validate() == ()
    assert ledger.incidence() == ((-1.0,), (1.0,))
    assert ledger.residual_ok(ledger.balance_residual((-2.0, 2.0), (2.0,)))


def test_conversion_is_explicit_and_weighted():
    ledger = TypedLedger(
        [Compartment("ore", "ore", "kg"), Compartment("product", "product", "kg")],
        [Flux("refine", "ore", "product", kind="conversion", coefficient=2.5)],
    )
    assert ledger.incidence() == ((-2.5,), (1.0,))


def test_cross_type_transfer_is_rejected():
    ledger = TypedLedger(
        [Compartment("water", "water", "kg"), Compartment("money", "money", "kg")],
        [Flux("bad_sum", "water", "money")],
    )
    assert any("crosses type" in e for e in ledger.validate())
    try:
        ledger.incidence()
    except LedgerError:
        pass
    else:
        raise AssertionError("invalid transfer reached incidence construction")


def test_barrier_and_componentwise_witness():
    assert TypedLedger.barriers_ok([(1, 2), (2, 3)], [0, 0], [2, 3])
    assert not TypedLedger.barriers_ok([(1, 4)], [0, 0], [2, 3])
    b = compensating_witness([0.5, 0.5])
    assert b[0] < 0 and aggregate([0.5, 0.5], b) > 0

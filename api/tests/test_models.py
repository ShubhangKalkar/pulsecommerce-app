from sqlalchemy import BigInteger, Integer

from app.db import models
from app.db.base import Base

EXPECTED_TABLES = {
    "customers",
    "products",
    "warehouses",
    "inventory",
    "orders",
    "order_items",
    "payments",
    "shipments",
    "order_events",
}


def test_all_tables_are_registered():
    assert set(Base.metadata.tables) == EXPECTED_TABLES


def test_money_columns_are_integers():
    # Money is stored as integer cents, never floats.
    money_columns = [
        models.Product.__table__.c.price_cents,
        models.Order.__table__.c.total_cents,
        models.OrderItem.__table__.c.unit_price_cents,
        models.Payment.__table__.c.amount_cents,
    ]
    for column in money_columns:
        assert isinstance(column.type, Integer | BigInteger), column


def test_order_status_values_match_the_state_machine():
    assert {s.value for s in models.OrderStatus} == {
        "placed",
        "paid",
        "packed",
        "shipped",
        "delivered",
        "cancelled",
        "payment_failed",
    }


def test_idempotency_key_is_unique():
    assert models.Order.__table__.c.idempotency_key.unique is True

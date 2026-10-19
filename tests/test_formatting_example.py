"""Проверить сохранение поведения при оформлении учебного примера."""

import pytest

from examples.after_format import price_with_discount as formatted
from examples.before_format import price_with_discount as unformatted


@pytest.mark.parametrize(
    "quantity,price,discount",
    [(1, 100, 0), (3, 99.9, 10), (5, 20, 50), (2, 1.25, 15)],
)
def test_t21_to_t24_same_result(quantity, price, discount):
    assert formatted(quantity, price, discount) == unformatted(
        quantity, price, discount
    )


def test_t25_both_reject_bad_quantity():
    with pytest.raises(ValueError):
        formatted(0, 100, 0)
    with pytest.raises(ValueError):
        unformatted(0, 100, 0)


def test_t26_both_reject_bad_discount():
    with pytest.raises(ValueError):
        formatted(1, 100, 55)
    with pytest.raises(ValueError):
        unformatted(1, 100, 55)

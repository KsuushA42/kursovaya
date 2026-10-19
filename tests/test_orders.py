"""Проверки основных ветвей поведения учебного сервиса."""

from decimal import Decimal

import pytest
from src import OrderStatus, change_status, create_order


def test_t01_regular_order():
    assert create_order("BOOK-1", 2, "100", 10).total == Decimal("180.00")


def test_t02_whitespace_in_code():
    assert create_order("  ABC  ", 1, 10).code == "ABC"


def test_t03_empty_code():
    with pytest.raises(ValueError, match="Код заявки"):
        create_order("", 1, 10)


def test_t04_code_too_short():
    with pytest.raises(ValueError, match="Код заявки"):
        create_order("AB", 1, 10)


def test_t05_code_too_long():
    with pytest.raises(ValueError, match="Код заявки"):
        create_order("0123456789ABC", 1, 10)


def test_t06_minimum_quantity():
    assert create_order("ABC", 1, 10).quantity == 1


def test_t07_maximum_quantity():
    assert create_order("ABC", 100, 10).quantity == 100


def test_t08_zero_quantity():
    with pytest.raises(ValueError, match="Количество"):
        create_order("ABC", 0, 10)


def test_t09_quantity_over_limit():
    with pytest.raises(ValueError, match="Количество"):
        create_order("ABC", 101, 10)


def test_t10_quantity_boolean_rejected():
    with pytest.raises(ValueError, match="Количество"):
        create_order("ABC", True, 10)


def test_t11_invalid_price():
    with pytest.raises(ValueError, match="Цена"):
        create_order("ABC", 1, -1)


def test_t12_non_numeric_price():
    with pytest.raises(ValueError, match="Цена"):
        create_order("ABC", 1, "oops")


def test_t13_nan_price():
    with pytest.raises(ValueError, match="Цена"):
        create_order("ABC", 1, "NaN")


def test_t14_minimum_discount():
    assert create_order("ABC", 1, 100, 0).total == Decimal("100.00")


def test_t15_maximum_discount():
    assert create_order("ABC", 1, 100, 50).total == Decimal("50.00")


def test_t16_discount_out_of_range():
    with pytest.raises(ValueError, match="Скидка"):
        create_order("ABC", 1, 100, 60)


def test_t17_decimal_rounding():
    assert create_order("ABC", 1, "1.005").total == Decimal("1.01")


def test_t18_initial_status():
    assert create_order("ABC", 1, 100).status == OrderStatus.NEW


def test_t19_valid_status_transitions():
    order = create_order("ABC", 1, 100)
    approved = change_status(order, OrderStatus.APPROVED)
    closed = change_status(approved, OrderStatus.CLOSED)
    assert closed.status == OrderStatus.CLOSED
    assert order.status == OrderStatus.NEW


def test_t20_invalid_status_transition():
    with pytest.raises(ValueError, match="Недопустимый"):
        change_status(create_order("ABC", 1, 100), OrderStatus.CLOSED)

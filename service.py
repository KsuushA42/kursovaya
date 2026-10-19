"""Создание заявок и разрешённые переходы между статусами."""

from dataclasses import replace

from .models import Order, OrderStatus
from .pricing import calculate_total
from .validation import (
    validate_code,
    validate_discount,
    validate_price,
    validate_quantity,
)

_ALLOWED_TRANSITIONS = {
    OrderStatus.NEW: {OrderStatus.APPROVED},
    OrderStatus.APPROVED: {OrderStatus.CLOSED},
    OrderStatus.CLOSED: set(),
}


def create_order(
    code: str, quantity: int, unit_price: object, discount_percent: object = 0
) -> Order:
    """Проверить поля и создать новую заявку с вычисленным итогом."""
    valid_code = validate_code(code)
    valid_quantity = validate_quantity(quantity)
    valid_price = validate_price(unit_price)
    valid_discount = validate_discount(discount_percent)
    total = calculate_total(valid_quantity, valid_price, valid_discount)

    return Order(
        code=valid_code,
        quantity=valid_quantity,
        unit_price=valid_price,
        discount_percent=valid_discount,
        total=total,
    )


def change_status(order: Order, new_status: OrderStatus) -> Order:
    """Изменить статус, не изменяя исходный объект заявки."""
    if new_status not in _ALLOWED_TRANSITIONS[order.status]:
        raise ValueError("Недопустимый переход между статусами")
    return replace(order, status=new_status)

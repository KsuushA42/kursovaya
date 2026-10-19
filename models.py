"""Модели предметной области: заявка и её статус."""

from dataclasses import dataclass
from decimal import Decimal
from enum import Enum


class OrderStatus(str, Enum):
    """Допустимые состояния заявки."""

    NEW = "new"
    APPROVED = "approved"
    CLOSED = "closed"


@dataclass(frozen=True)
class Order:
    """Заявка с итоговой стоимостью и текущим состоянием."""

    code: str
    quantity: int
    unit_price: Decimal
    discount_percent: Decimal
    total: Decimal
    status: OrderStatus = OrderStatus.NEW

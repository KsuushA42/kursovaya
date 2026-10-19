"""Расчёт итоговой стоимости отдельно от ввода и управления статусами."""

from decimal import Decimal, ROUND_HALF_UP


def calculate_total(
    quantity: int, unit_price: Decimal, discount_percent: Decimal
) -> Decimal:
    """Итог = количество × цена × (1 - скидка / 100)."""
    subtotal = quantity * unit_price
    discount_multiplier = Decimal("1") - discount_percent / Decimal("100")
    return (subtotal * discount_multiplier).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )

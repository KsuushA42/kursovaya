"""Проверка пользовательских данных до вычислений."""

from decimal import Decimal, InvalidOperation


def as_decimal(value: object, field: str) -> Decimal:
    """Преобразовать число в Decimal с понятным сообщением об ошибке."""
    if isinstance(value, bool):
        raise ValueError(f"{field}: логическое значение недопустимо")
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError, TypeError) as exc:
        raise ValueError(f"{field}: требуется число") from exc
    if not result.is_finite():
        raise ValueError(f"{field}: требуется конечное число")
    return result


def validate_code(code: str) -> str:
    """Проверить код заявки (от 3 до 12 непустых символов)."""
    if not isinstance(code, str) or not 3 <= len(code.strip()) <= 12:
        raise ValueError("Код заявки должен содержать от 3 до 12 символов")
    return code.strip()


def validate_quantity(quantity: int) -> int:
    """Проверить целое количество единиц от 1 до 100."""
    if isinstance(quantity, bool) or not isinstance(quantity, int):
        raise ValueError("Количество должно быть целым числом")
    if not 1 <= quantity <= 100:
        raise ValueError("Количество должно быть в диапазоне 1..100")
    return quantity


def validate_price(price: object) -> Decimal:
    """Проверить положительную цену."""
    amount = as_decimal(price, "Цена")
    if amount <= 0:
        raise ValueError("Цена должна быть положительной")
    return amount


def validate_discount(discount_percent: object) -> Decimal:
    """Проверить скидку от 0 до 50 процентов."""
    percent = as_decimal(discount_percent, "Скидка")
    if not 0 <= percent <= 50:
        raise ValueError("Скидка должна быть в диапазоне 0..50")
    return percent

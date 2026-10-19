"""Намеренно неформатированный учебный пример. Не используйте как образец стиля."""

def price_with_discount(quantity, price, discount):
  if quantity<=0: raise ValueError('Количество должно быть положительным')
  if price<=0: raise ValueError('Цена должна быть положительной')
  if discount<0 or discount>50: raise ValueError('Скидка должна быть от 0 до 50 процентов')
  result=quantity*price*(1-discount/100)
  return round(result,2)

from django import template
import re

register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        value = float(re.sub(r'[^\d.]', '', str(value)))
        arg = float(arg)
        return value * arg
    except (ValueError, TypeError):
        return 0

@register.filter
def calc_total(basket_items):
    total = 0
    for item in basket_items:
        price = float(re.sub(r'[^\d.]', '', str(item.product.arrivals_price)))
        total += price * item.count
    return total

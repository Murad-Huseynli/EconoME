from django import template
from django.template.defaultfilters import floatformat

register = template.Library()


@register.filter
def divide(value, arg):
    try:
        return float(value) / float(arg)
    except (ValueError, ZeroDivisionError):
        return 0

from django import template
from django.conf import settings

register = template.Library()


@register.filter
def env(request):
    return settings.ENVIRONMENT

@register.filter
def only_url(request):
    return settings.MAIN_URL

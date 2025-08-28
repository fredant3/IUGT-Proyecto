from django import template
from django.utils.safestring import mark_safe
from templates.sneat.helpers.theme import TemplateHelper

register = template.Library()


# Register tags as an adapter for the Theme class usage in the HTML template
@register.simple_tag
def get_theme_variables(scope):
    return mark_safe(TemplateHelper.get_theme_variables(scope))

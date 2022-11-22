from django import template 
register = template.Library()
from configuration.models import State


@register.filter
def get_all_states(i):
    return State.objects.all()

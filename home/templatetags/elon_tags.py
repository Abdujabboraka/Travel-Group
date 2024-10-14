from django import template
from ..models import Destination
register = template.Library()


@register.simple_tag
def all_destinations():
    return Destination.objects.all()

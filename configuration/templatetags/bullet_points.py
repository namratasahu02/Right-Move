from django import template
from vendor.models import Bullet_point
register = template.Library()


@register.filter
def get_all_bullet_points(product):
    bp = Bullet_point.objects.all().filter(product=product)
    if bp :
        return bp 

    return ''
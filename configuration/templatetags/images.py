from django import template
from vendor.models import Image

register = template.Library()

@register.filter
def get_first_image(product):
    img = Image.objects.all().filter(product=product).first()
    if img:
        return img.image

    else:
        return None

# @register.filter
# def lower(value):
#     return value.lower()
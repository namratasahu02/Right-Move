from django.contrib import admin
from .models import Bullet_point, Category, Image, Product

# Register your models here.
admin.site.register(Bullet_point)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Product)
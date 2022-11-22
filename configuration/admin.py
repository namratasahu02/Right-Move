from django.contrib import admin
from .models import Category, Size_unit, State, Status_type, Image_type


admin.site.register(Category)
admin.site.register(Size_unit)
admin.site.register(State)
admin.site.register(Status_type)
admin.site.register(Image_type)
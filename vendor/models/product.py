from django.db import models
from django.contrib.auth.models import User
from configuration.models import Category, Status_type, Size_unit
class Product(models.Model):
    # Main details
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    status = models.ForeignKey(Status_type, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, default='', null=True, blank=True)
    brand = models.CharField(max_length=40, default='', null=True, blank=True)
    mrp = models.CharField(max_length=20, default='', null=True, blank=True)
    price = models.CharField(max_length=20, default='', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    # Other details 
    size = models.CharField(max_length=30, default='', null=True, blank=True)
    size_unit = models.ForeignKey(Size_unit, null=True, blank=True, on_delete=models.CASCADE)
    # Address details
    address = models.CharField(max_length=140, blank=True, null=True)
    district = models.CharField(max_length=80,  blank=True, null=True)
    state = models.CharField(max_length=60, blank=True, null=True)
    zip_code = models.CharField(max_length=40, default='', null=True, blank=True)
    # Google map
    map_link = models.CharField(max_length=800, default='', blank=True, null=True)

    highlighted = models.BooleanField(default=False)

    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        return self
    def __str__(self):
        if self.title:
            return self.title

        else:
            return 'x Invalid Product'
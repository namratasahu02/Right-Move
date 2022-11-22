from django.db import models
from .product import Product


class Bullet_point(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    bullet_point = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        if self.product:
            return self.product.title

        else:
            return 'x Invalid product bullet point....'
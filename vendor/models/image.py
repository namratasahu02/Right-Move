from django.db import models
from .product import Product 
from configuration.models import Image_type


class Image(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    image_type = models.ForeignKey(Image_type, blank=True, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="listing/products/owner", null=True)

    def __str__(self):
        if self.product:
            return self.product.title
        else:
            return 'x Invalid product image....'
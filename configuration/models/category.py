from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=80, null=True, blank=True)
    description = models.CharField(max_length=120, null=True, blank=True)
    
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        if self.name:
            return self.name

        else:
            return 'x   Invalid Product Category.'
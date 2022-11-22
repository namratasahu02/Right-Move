from django.db import models


class Image_type(models.Model):
    type_name = models.CharField(max_length=20, default='')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.type_name
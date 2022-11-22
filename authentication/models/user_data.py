from statistics import mode
from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class User_data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(default='', max_length=15)
    gstin = models.CharField(default='', max_length=30)
    gender = models.CharField(default='male', max_length=15)
    aadhaar = models.ImageField(upload_to="user/documents/aadhaar", default='', null=True)
    otp = models.CharField(max_length=10, blank=True, null=True, default=0000)
    password = models.CharField(max_length=50, blank=True, null=True)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.aadhaar :
            img1 = Image.open(self.aadhaar.path)
            if img1.height > 1500 or img1.width > 1500:
                output_size = (1500, 1500)
                img1.thumbnail(output_size)
                img1.save(self.aadhaar.path)
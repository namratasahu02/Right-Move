from django.db import models


class Banner(models.Model): 
    name = models.CharField(max_length=50, default='', null=True, blank=True)
    image = models.ImageField(upload_to='banners')
    description = models.CharField(max_length=80, default='', null=True, blank=True)
    set_show = models.BooleanField(default=False)
    set_as_banner_2 = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @staticmethod
    def get_latest_banner():
        return  Banner.objects.last()
from django.db import models
class Size_unit(models.Model):
    unit_name = models.CharField(max_length=20, default='')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Size Unit'
        verbose_name_plural = 'Size Units'

    def __str__(self):
        return self.unit_name

    @staticmethod
    def get_all_sizes():
        return Size_unit.objects.all()
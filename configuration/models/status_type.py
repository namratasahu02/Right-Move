from django.db import models
class Status_type(models.Model):
    name = models.CharField(max_length=50, default='')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Status Type'
        verbose_name_plural = 'Status Types'

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_status():
        return Status_type.objects.all()
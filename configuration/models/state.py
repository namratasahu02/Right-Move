from django.db import models

class State(models.Model):
    state_name = models.CharField(max_length=50, default='')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.state_name

    def get_all_states():
        return State.objects.all()
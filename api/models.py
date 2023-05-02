from django.db import models

# Create your models here.

class Task(models.Model):
    completed = models.BooleanField(default=False, blank=True,       null=True)
    objects = models.Manager()
    def __str__(self):
        return models.CharField(max_length=200)


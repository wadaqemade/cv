from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Cv(models.Model):
    full_name = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=50)
    note = models.TextField(max_length=150)
    specialization = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('full_name',)

    def __str__(self):
        return self.full_name

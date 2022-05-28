from django.db import models
from django.forms import CharField

class Familia(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    kinship = models.CharField(max_length=20)
    power = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
from django.db import models
from django.forms import CharField

class Familia(models.Model):
    name = models.CharField(max_length=30)
    alias = models.CharField(max_length=30, blank=True, null=True, unique=True)
    age = models.IntegerField()
    born = models.DateField(blank=True, null=True,)
    kinship = models.CharField(max_length=20, blank=True, null=True)
    power = models.CharField(max_length=50, blank=True, null=True)
    img = models.ImageField(blank=True, null=True, upload_to='familiares')
    active = models.BooleanField(default=True)
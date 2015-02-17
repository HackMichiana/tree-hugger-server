from django.db import models

# Create your models here.

class Tree(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.FloatField()
    dead = models.BooleanField(default=False)

from django.db import models

# Create your models here.
class Title(models.Model):
    name = models.CharField(max_length=32)
    rating = models.CharField(max_length=32)
    price = models.CharField(max_length=32)
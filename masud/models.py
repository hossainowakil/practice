from django.db import models

# Create your models here.

class Oakil(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    phone = models.CharField(max_length=78)
    address = models.TextField(max_length=200)

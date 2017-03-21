from django.db import models


# Create your models here.
class Enter(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    email = models.EmailField()

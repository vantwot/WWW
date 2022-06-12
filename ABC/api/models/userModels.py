from django.db import models

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=30)
  lastname = models.CharField(max_length=30)
  adress = models.CharField(max_length=50)
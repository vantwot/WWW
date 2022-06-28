from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  name = models.CharField(max_length=250, null=True)
  lastname = models.CharField(max_length=250, null=True)
  email = models.CharField(max_length=250, null=True, unique=True)
  password = models.CharField(max_length=250, null=True)
  username = None

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []


  
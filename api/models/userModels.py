from django.db import models

# Create your models here.
class User(models.Model):
  username = models.CharField(max_length=255, null=True, unique=True)
  first_name = models.CharField(max_length=250, null=True)
  last_name = models.CharField(max_length=250, null=True)
  email = models.CharField(max_length=250, null=True, unique=True)
  password = models.CharField(max_length=250, null=True)
  ifLogged = models.BooleanField(default=False)
  token = models.CharField(max_length=500, null=True, default="")
  role = models.CharField(max_length=250, null=True)
  adress = models.CharField(max_length=250, null=True)
  identification = models.CharField(max_length=250, null=True)


  def __str__(self):
    return "{} -{}".format(self.username, self.email)


  
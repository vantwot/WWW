from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.TextField()
    content = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.title

    

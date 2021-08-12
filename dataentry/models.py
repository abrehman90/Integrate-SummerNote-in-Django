from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=25)
    phone = models.CharField(max_length=25,default='+92')
    email = models.EmailField()
    city = models.CharField(max_length=20)
    content = models.TextField()

    def __str__(self):
        return self.name

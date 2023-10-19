from django.db import models


# Create your models here.

class Userdata(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50, default='')
    created_at = models.DateTimeField(auto_now_add=True)

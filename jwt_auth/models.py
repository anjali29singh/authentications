from django.db import models
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True, primary_key=True,null=False)
    password = models.CharField(max_length=100,null=False)


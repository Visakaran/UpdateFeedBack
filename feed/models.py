from django.db import models

# Create your models here.
class App(models.Model):
    email = models.EmailField()
    passwords = models.CharField(max_length=100)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=20)
    text = models.CharField(max_length=255)

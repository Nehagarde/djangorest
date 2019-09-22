from django.db import models

# Create your models here.

class Employees(models.Model):
    username = models.CharField(max_length=250)
    email = models.EmailField()

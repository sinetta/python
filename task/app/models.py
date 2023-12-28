from django.db import models

# Create your models here.

class Package(models.Model):
    name=models.CharField(max_length=255)
    image = models.ImageField(upload_to='img')

class Subpackage(models.Model):
    name=models.CharField(max_length=255)
    desc=models.CharField(max_length=255)
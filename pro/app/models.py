from django.db import models

# Create your models here.
class Image(models.Model):
    description = models.CharField(max_length=255,)
    document = models.ImageField(upload_to='img')



class Product(models.Model):
    name=models.CharField(max_length=255)
    price=models.CharField(max_length=255)
    image=models.CharField(max_length=3000)
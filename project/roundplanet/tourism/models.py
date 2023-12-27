from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    message=models.TextField()


class Package(models.Model):
    name=models.CharField(max_length=255)
    img = models.ImageField(upload_to='img')
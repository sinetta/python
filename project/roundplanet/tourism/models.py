from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    message=models.TextField()


class Package(models.Model):
    name=models.CharField(max_length=255)
    image = models.ImageField(upload_to='img')

class Event(models.Model):
    image=models.ImageField(upload_to='img')
    description=models.CharField(max_length=255)

class Gal(models.Model):
    image=models.CharField(max_length=3000)

class Contactus(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    message=models.TextField()
    subject=models.CharField(max_length=255)
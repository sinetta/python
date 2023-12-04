from django.contrib import admin
from .models import *
# Register your models here.

class Image_display(admin.ModelAdmin):
    list_display=['description','document']



class Product_display(admin.ModelAdmin):
    list_display=['name','price','image']

admin.site.register(Image,Image_display)
admin.site.register(Product,Product_display)

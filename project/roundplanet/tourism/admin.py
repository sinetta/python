from django.contrib import admin
from .models import *
# Register your models here.

class Enquiry(admin.ModelAdmin):
    list_display=['name','email','phone','message']

class Pack(admin.ModelAdmin):
    list_display=['name','img']

admin.site.register(Contact,Enquiry)
admin.site.register(Package,Pack)

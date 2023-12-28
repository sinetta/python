from django.contrib import admin
from .models import *
# Register your models here.

class Pack(admin.ModelAdmin):
    list_display=['name','image']

class Sub(admin.ModelAdmin):
    list_display=['name','desc']
admin.site.register(Package,Pack)
admin.site.register(Subpackage,Sub)
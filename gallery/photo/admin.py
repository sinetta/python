from django.contrib import admin
from . models import *

# Register your models here.

class Gallery_display(admin.ModelAdmin):
    list_display=['name','image']


admin.site.register(Gallery,Gallery_display)
from django.contrib import admin
from .models import *
# Register your models here.

class section_display(admin.ModelAdmin):
    list_display=['name']

admin.site.register(section,section_display)

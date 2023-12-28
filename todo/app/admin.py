from django.contrib import admin
from . models import *
# Register your models here.

class Todo_dispaly(admin.ModelAdmin):
    list_display=['task']

admin.site.register(Todo,Todo_dispaly)
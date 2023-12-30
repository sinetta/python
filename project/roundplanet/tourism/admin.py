from django.contrib import admin
from .models import *
# Register your models here.

class Enquiry(admin.ModelAdmin):
    list_display=['name','email','phone','message']

class Pack(admin.ModelAdmin):
    list_display=['name','image']

class Event_details(admin.ModelAdmin):
    list_display=['image','description']

class Gal_display(admin.ModelAdmin):
    list_display=['image']

class Contactus_display(admin.ModelAdmin):
    list_display=['name','phone','email','subject','message']

class Sub(admin.ModelAdmin):
    list_display=['image','price','day','night','pack']

admin.site.register(Contact,Enquiry)
admin.site.register(Package,Pack)
admin.site.register(Event,Event_details)
admin.site.register(Gal,Gal_display)
admin.site.register(Contactus,Contactus_display)
admin.site.register(Subpackage,Sub)
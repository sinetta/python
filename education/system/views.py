from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    name=Student.objects.all()
    return render(request,'index.html',{'name':name})
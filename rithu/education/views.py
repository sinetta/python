from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    student=Student.objects.all()
    return render(request,'index.html',{'student':student})

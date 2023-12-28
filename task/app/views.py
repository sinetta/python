from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):

    context={}
    obj=Package.objects.all()
    context['obj']=obj

    return render(request,'index.html',context)




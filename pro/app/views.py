from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    context={}
    
    obj=Image.objects.all()
    pro=Product.objects.all()
    context['obj']=obj
    context['pro']=pro
    return render(request,'index.html',context)
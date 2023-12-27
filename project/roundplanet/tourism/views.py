from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    
    context={}
    con=Contact.objects.all()

    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')

    context["con"]=con

    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def packages(request):

    context={}
    obj=Package.objects.all()
    context['obj']=obj
    return render(request,'packages.html')
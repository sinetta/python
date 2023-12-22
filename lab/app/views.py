from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index (request):
    form=UserCreationForm(request.POST)

    if form.is_valid():
        form.save()
           
        return redirect('home')

    return render(request,'index.html',{'form':form})


def home(request):
    
    return render(request,'home.html')
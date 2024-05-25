from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('<h1>this is welcome page</h1>')
def about(request):
    return HttpResponse('<h1>this is about page</h1>')
def contact(request):
    return HttpResponse('<h1>this is contact page</h1>')
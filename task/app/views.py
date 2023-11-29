from django.shortcuts import render
from .models import *
from . forms import Todo_form

# Create your views here.

def index(request):
    context={}

    if request.method=='POST':
        if 'save' in request.POST:
            todo_form=Todo_form(request.POST)
            todo_form.save()

        elif 'delete' in request.POST:
            key=request.POST.get('delete')
            todo_del=request.POST.get(id=key)
            todo_del.delete()

    todo_form=Todo_form()
    todo=Todo.objects.all()





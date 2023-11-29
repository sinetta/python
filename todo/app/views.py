from django.shortcuts import render
from . forms import Todo_form
from . models import *

# Create your views here.
def index(request):
    context={}
    todo_form=Todo_form()
    todo=Todo.objects.all()

    if request.method=='POST':
        if 'save' in request.POST:
            todo_form=Todo_form(request.POST) 
            todo_form.save()

        elif 'delete' in request.POST:
           key=request.POST.get('delete')
           todo_del=Todo.objects.get(id=key)
           todo_del.delete()

    context['todo_form']=todo_form
    context['todo']=todo
    return render(request,'index.html',context)
    
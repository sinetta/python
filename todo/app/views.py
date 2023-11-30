from django.shortcuts import render
from . forms import Todo_form
from . models import *

# Create your views here.
def index(request):
    context={}
    form=Todo_form()
    todo=Todo.objects.all()

    if request.method=='POST':
        if 'save' in request.POST:
            key=request.POST.get('save')
            
           
            if not key:
                    form=Todo_form(request.POST)
                  

                    
            else:
                    todo_key=Todo.objects.get(id=key)
                    form=Todo_form(request.POST,instance=todo_key)
                    
                    
                  

                             
            form.save()
            form=Todo_form()




        elif 'delete' in request.POST:
           key=request.POST.get('delete')
           todo_del=Todo.objects.get(id=key)
           todo_del.delete()

        elif 'edit' in request.POST:
           key=request.POST.get('edit')
           todo_edit=Todo.objects.get(id=key)
           form=Todo_form(instance=todo_edit)

    context['form']=form
    context['todo']=todo
    return render(request,'index.html',context)

    
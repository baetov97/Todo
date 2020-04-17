from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.decorators.http import require_POST
import datetime


# Create your views here.
def index(request):
    todo_list = ToDo.objects.order_by('id')
    # form = ToDoForm()
    newtodoform = NewTodoForm()
    mydate = datetime.datetime.now()
    context = {'todo_list': todo_list, 'form': newtodoform,'mydate':mydate}
    return render(request, 'todo/index.html', context)


@require_POST
def addToDo(request):
    # form = ToDoForm(request.POST)
    # todo_10 = ToDo.objects.get(pk=21)
    newtodoform = NewTodoForm(request.POST, )
    print(request.POST['text'])
    if newtodoform.is_valid():
        # new_todo = ToDo(text=form.cleaned_data['text'])
        # new_todo.save()
        newtodoform.save()

    return redirect('index')


def completeToDo(request, todo_id):
    todo = ToDo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('index')


def deleteCompleted(request):
    ToDo.objects.filter(complete__exact=True).delete()
    return redirect('index')


def deleteAll(request):
    ToDo.objects.all().delete()
    return redirect('index')

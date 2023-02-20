from django.shortcuts import render, redirect
from .models import ToDo
from .forms import TodoForm
from django.views.decorators.http import require_POST


def index(request):
    todo = ToDo.objects.all()
    form = TodoForm()
    context = {'todo_list': todo, 'form': form}
    return render(request, 'index.html', context)


def add_form(request):
    todo = ToDo.objects.all()
    return render(request, 'add.html', {'todo_obj': todo})


@require_POST
def add_todo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new_todo = ToDo(title = request.POST['text'])
        new_todo.save()
        return redirect('/')


def complete_todo(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    if todo.complate:
        todo.complate = False
        todo.save()
    else:
        todo.complate = True
        todo.save()
    return redirect('/')

def delete_all(request):
    ToDo.objects.all().delete()
    return redirect('/')


def delete_completed(request):
    ToDo.objects.filter(complate=True).delete()
    return redirect('/')
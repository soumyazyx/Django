from django.shortcuts import render, redirect
from .models import Task
from .forms import AddTaskForm, UpdateTaskForm, DeleteTaskForm
import requests


# Create your views here.
def taskshome(request):

    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        form.save(commit=True)
        return redirect('taskshome')
    else:
        form = AddTaskForm()
        tasks = Task.objects.all()
        context = {
            'tasks': tasks,
            'form': form
        }
    return render(request, 'tasks/taskshome.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)    
    if request.method == 'POST':
        form = UpdateTaskForm(request.POST, instance=task)
        form.save(commit=True)
        return redirect('taskshome')
    else:
        form = UpdateTaskForm(instance=task)
        context = {
            'tasks': task,
            'form': form
        }
    return render(request, 'tasks/updatetask.html', context)


def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    if(request.method == 'POST'):
        form = DeleteTaskForm(request.POST, instance=task)
        task.delete()
        return redirect('taskshome')
    else:
        form = DeleteTaskForm(instance=task)
        context = {
            'task': task,
            'form': form 
        }
        return render(request, 'tasks/deletetask.html', context)
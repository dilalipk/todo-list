from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import Task
from django.contrib.auth.models import User
from .forms import TaskForm
from django.contrib import messages as msg
from django.views.generic import ListView
from django.urls import reverse

from django.shortcuts import redirect

def all_tasks(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            # Handle POST request for task creation
            forms = TaskForm(request.POST)
            if forms.is_valid():
                task = forms.save(commit=False)
                task.author = request.user
                task.save()
            return redirect("tasks")
        elif request.method == "GET":
            tasks = Task.objects.all()
            pending_tasks = tasks.filter(status="pending")
            complete_tasks = tasks.filter(status="complete")
            progress_tasks = tasks.filter(status="on_progress")
            hold_tasks = tasks.filter(status="on_hold")
            context = {
                "tasks": tasks,
                "pending_tasks": pending_tasks,
                "complete_tasks": complete_tasks,
                "hold_tasks": hold_tasks,
                "progress_tasks": progress_tasks,
            }
            return render(request, "todolist.html", context=context)
        
    return redirect('login')

def edit(request, id):

    if request.method == "POST":
        forms = TaskForm(request.POST, instance=Task.objects.get(id=id))
        if forms.is_valid():
            task = forms.save(commit=False)
            task.author = request.user
            task.save()
            return redirect("tasks")

def delete(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect("tasks")

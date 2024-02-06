from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import Task
from django.contrib.auth.models import User
from .forms import TaskForm
from django.contrib import messages as msg

# Create your views here.


def all_tasks(request):
    if request.method == "POST":
        forms = TaskForm(request.POST)
        print(forms)
        if forms.is_valid():
            task = forms.save(commit=False)
            task.author = request.user
            task.save()

        return redirect("tasks")
    if request.method == "GET":

        tasks = Task.objects.all()
        context = {
            'tasks': tasks
        }

        return render(request, "todolist.html" , context=context)

from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def all_tasks(request):
    return HttpResponse("This is a list of tasks")
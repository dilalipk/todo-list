from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_tasks, name="tasks"),
    path("edit/<id>", views.edit, name="edit"),
    path("delete/<id>", views.delete, name="delete"),
]

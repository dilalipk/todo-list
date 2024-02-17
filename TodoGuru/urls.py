
from django.contrib import admin
from django.urls import path, include
from TodoGuru import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("tasks/", include("taskApp.urls")),
    path("accounts/", include("userAccount.urls")),
]

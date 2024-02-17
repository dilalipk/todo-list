from django.shortcuts import render, redirect
from django.contrib.auth import logout, login as sign
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate


def validate_password_strength(password):
    data = []
    if len(password) < 8:
        data.append("Password must be at least 8 characters long.")
    if not any(char.isdigit() for char in password):
        data.append("Password must contain at least one digit.")
    if not any(char.isalpha() for char in password):
        data.append("Password must contain at least one letter.")

    if data:
        return data
    else:
        return None


def register(request):
    if request.method == "POST":
        auth_user = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2") 
        first_name = request.POST.get("first_name") 
        last_name = request.POST.get("last_name")  
        data = {}

        if User.objects.filter(username=auth_user).exists():
            data["user"] = "Username already exists"
            data["auth_user"] = auth_user
        if User.objects.filter(email=email).exists():
            data["email_error"] = "Email already exists"
            data["email"] = email
        check = validate_password_strength(password1)
        print(check)
        if check is not None:
            data["password_error"] = check
        if check is None:
            arr = []
            if password1 != password2:
                arr.append("Passwords don't match")
                data["password_error"] = arr
        if data:
            return render(request, "register.html", data)
        else:
            new_user = User.objects.create_user(
                username=auth_user,first_name =first_name, last_name=last_name, email=email, password=password1
            )
            new_user.save()
            messages.success(request, "Account created successfully")
            return redirect("login")
    else:
        return render(request, "register.html")


def login(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        data = {}
        user = authenticate(request, username=username, password=password)
        if user is not None:
            sign(request, user)
            return redirect("tasks")
        else:
            data["user"] = ""
            data["error"] = "Invalid username or password"
            return render(request, "login.html", data)
    else:
        return render(request, "login.html")


def log_out(request):
    logout(request)
    return redirect("login")

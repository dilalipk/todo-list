from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput


class CustomRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "username": TextInput(),
            "email": EmailInput(),
            "password1": PasswordInput(),
            "password2": PasswordInput(),
        }

    def clean(self):
            cleaned_data = super().clean()
            username = cleaned_data.get("username")
            email = cleaned_data.get("email")
            password1 = cleaned_data.get("password1")
            password2 = self.cleaned_data.get("password2")
            
            if User.objects.filter(username=username).exists():
                raise ValidationError("Username already exists")
            
            if User.objects.filter(email=email).exists():
                raise ValidationError("Email already exists")
            
            if password1 != password2:
                raise ValidationError("Passwords don't match")
            
            # Save the user if all validations pass
            user = User.objects.create_user(username=username, email=email, password=password1)
            return cleaned_data
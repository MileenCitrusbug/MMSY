from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from movies.models import User, AbstractUser


class Signupform(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name','email']
    def save(self,commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

class Loginform(UserCreationForm):
    class meta(UserCreationForm.Meta):
        model = User
        fields = ['email','password']
    

    
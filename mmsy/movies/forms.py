from dataclasses import fields
from pickle import TRUE
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from movies.models import User, AbstractUser


class Signupadmin(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name','email']
    def save(self,commit=True):
        user = super().save(commit=False)
        user.is_admin=True
        if commit:
            user.save()
        return user

class Signupmember(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name','email']
    def save(self,commit=True):
        user = super().save(commit=False)
        user.is_subscriber=True
        if commit:
            user.save()
        return user


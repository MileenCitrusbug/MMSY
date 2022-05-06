from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class userceationform(UserCreationForm):
    class Meta:
        model=User
        fields="__all__"
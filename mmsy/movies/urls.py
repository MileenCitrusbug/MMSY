from django.urls import path
from django.views.generic import TemplateView
from . import views
from .models import *
from django import forms 
urlpatterns = [
    path('login/', views.login.as_view(), name='login'),
    path('signup/', views.Signup.as_view(),name='signup'),
]

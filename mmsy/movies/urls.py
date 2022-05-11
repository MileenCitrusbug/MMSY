from turtle import home
from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import Signup,Login,Home
from .models import *
from django import forms 
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('signup_admin/',views.Signup_admin.as_view(),name='signup_admin'),
    path('signup_member/',views.Signup_member.as_view(),name='signup_member'),
    path('',views.Home.as_view(),name='home')
]
#path('account/eventadminlogin/', views.AdminLogin.as_view(), name='admin-login'),


#    path('', LoginView.as_view(
#            template_name='authentication/login.html',
#            redirect_authenticated_user=True),
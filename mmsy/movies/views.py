

from pyexpat import model
from urllib import request
from django.views.generic import View, CreateView
from django.shortcuts import render, redirect
from django import forms
from movies import forms
from django.http import HttpResponse
# from movies.models import User, AbstractUser
from movies.forms import Signupform, Loginform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.conf import settings
User = settings.AUTH_USER_MODEL


class Login(CreateView):
    def get(self,request):
        form = Loginform()
        model = User
        
        return render(request,'login.html',{'form':form} )

    def post(self,request):
        form = Loginform(request.POST)
        if form.is_valid():
            print(form.cleaned_data['fname'])
            return render(request,'home.html')

###############################################


class Signup(CreateView):
    model=User
    form_class = Signupform
    template_name = 'user_form.html'
    # def get(self,request):
    #     form = self.signupform()
    #     return render(request,self.template,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg = "success"
            return HttpResponse(msg)
        else:
            msg = "error"
            return HttpResponse(msg)

class Home(CreateView):
    template= 'home.html'

            
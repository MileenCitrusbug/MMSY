

from distutils.command.clean import clean
import email
from multiprocessing.sharedctypes import Value
from pickle import TRUE
from pyexpat import model
from statistics import mode
from urllib import request
from django.views.generic import View, CreateView
from django.shortcuts import render, redirect
from django import forms
from movies import forms
from django.http import HttpResponse
from movies.models import User, AbstractUser
from movies.forms import Signupadmin,Signupmember
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.conf import settings
from django.contrib.auth import get_user_model, login,logout
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password





  

class Login(View):
    model=User
    def get(self,request):
        return render(request,'registration/login.html')


    def post(self,request):
        email=request.POST['email']
        raw_password=request.POST['password']
        print(raw_password)
        pw=User.objects.get(email=email)
        print(email)
        password=pw.password
        valid = check_password(raw_password,password)
        
        if not valid:
            return  HttpResponse("incorrect password")
            

        user=User.objects.get(email=email)
        if user.is_authenticated:

            if user.is_admin == True:
                login(request, user)
                return render(request,'admin/admin_home.html')
            else:
                login(request,user)
                return render(request,'member/member_home.html') 
        else:
            return HttpResponse("invalid login")

class Signup_admin(CreateView):
    model=User
    form_class = Signupadmin
    template_name = 'registration/signup_admin.html'
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


class Signup_member(CreateView):
    model=User
    form_class = Signupmember
    template_name = 'registration/signup_member.html'
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
            

class Home(View):
    model = User
    template = 'base.html'

    def get(self, request):

        return render(request, self.template)

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('home')
     
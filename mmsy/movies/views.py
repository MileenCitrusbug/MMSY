

from ast import Delete
from distutils.command.clean import clean
import email
#from msilib.schema import ListView
from multiprocessing.sharedctypes import Value
from pickle import TRUE
from pyexpat import model
from statistics import mode
from turtle import update
from urllib import request
from django.views.generic import View, CreateView,ListView,DeleteView,UpdateView,RedirectView
from django.shortcuts import render, redirect
from django import forms
from movies import models
from django.http import HttpResponse
from movies.models import *
from movies.forms import *
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.conf import settings
from django.contrib.auth import get_user_model, login,logout
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.urls import reverse_lazy




  

class Login(View):
    model=User
    template_name = 'admin/admin_home.html'
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
                return redirect('admin_home')
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


class AdminHomeview(ListView):
    model = Movie
    template = 'admin/admin_home.html'

    def get(self, request):
        movielist=Movie.objects.filter(delete=False)
        return render(request,'admin/admin_home.html',{'movielist':movielist})
        



class MemberHomeview(View):
    model = Movie
    template = 'member/member_home.html'

    def get(self, request):

        return render(request, self.template)


class AddMovieview(CreateView):
    model = Movie
    form_class = AddMovieForm
    template_name = 'admin/add_movie.html'
    def get(self,request):
        return render(request, self.template_name,{ 'form': self.form_class})

    def post(self, request):
        form =self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_home')
        else:
            msg = "Try Again!!! "
            return HttpResponse(msg)

# class DeleteMovieview(View):


#     def post(self, *args, **kwargs):
#         id=kwargs['pk']
#         movie=Movie.objects.get(id=id)
#         movie.isdelete = True       
#         return redirect('admin_home')


    
def DeleteMovieview(request,pk):
    movie=Movie.objects.get(id=pk)
    movie.isdelete = True
    movie.save()
    return redirect('admin_home')

class UpdateMovieview(View):
    model = Movie
    fields = "__all__"
    template_name = 'admin/update_movie.html'
    
    def get(self, request,pk):
        mv = User.objects.get(id=pk)
        fm = AddMovieForm(instance=mv)

        return render (request, 'admin/update_movie.html',{'form':fm})

    def post(self, request, pk):
        mv = User.objects.get(id=pk)
        fm = AddMovieForm(instance=mv)
        if fm.is_valid():
            fm.save()
        return redirect('admin_home')



    
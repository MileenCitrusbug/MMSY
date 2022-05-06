
from urllib import request
from django.views.generic.base import View
from django.shortcuts import render
# from django.urls import path
from django.http import HttpResponse

def login(request):
    return render(request,'login.html')
    
def signup(request):
    return render(request,'signup.html')
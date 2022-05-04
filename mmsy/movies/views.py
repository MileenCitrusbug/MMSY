
from urllib import request
from django.views.generic.base import View
from django.shortcuts import render
# from django.urls import path
from django.http import HttpResponse

def req(reqest):
    return render(reqest,'home.html')
    

# def home(request):
#     if request.user.is_authenticated:
#         if request.user.is_admin:
#             return redirect(':quiz_change_list')
#         else:
#             return redirect('students:quiz_list')
#     return render(request, 'classroom/home.html')


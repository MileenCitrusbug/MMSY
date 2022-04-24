
from urllib import request
from django.views.generic import View, CreateView
from django.shortcuts import render
from movies import forms
from django.http import HttpResponse
from .models import User

# class login(View):
#     def get(self,request):
#         form = loginform()
#         return render(request,'login.html',{'form':form} )

#     def post(self,request):
#         form = loginform(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data['fname'])
#             return render(request,'home.html')
    
class Signup(CreateView):
    model=User
    form_class = Signupform
    template='/signup.html'
    # def get(self,request):
    #     form = self.signupform()
    #     return render(request,self.template,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'login', {'form':form})
        else:
            return HttpResponse("Error")

            
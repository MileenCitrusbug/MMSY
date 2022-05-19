

from ast import Delete
from audioop import reverse
from distutils.command.clean import clean
import email
#from msilib.schema import ListView


from statistics import mode
from turtle import update
from urllib import request
from django.views.generic import View, CreateView,ListView,DeleteView,UpdateView,RedirectView
from django.shortcuts import get_object_or_404, render, redirect
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
from django.db.models import Avg




  

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
                return redirect('member_home') 
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
        



class MemberHomeview(ListView):
    model = Movie
    template = 'member/member_home.html'
        
        
        

    def get(self, request):
        # avgr=Movie.avaregereview
        # print(avgr)
        # star=Rating.objects.filter(user=request.user).first()
        # print(star)
        # rate=Rating.objects.filter(user=request.user)
        # from django.db.models import Avg
        # star=rate.rating.objects.all()
        # for abc in rate:
        #     xyz=Rating.objects.all().aggregate(Avg('rating'))
           

        # print(rate.count())

        movielist=Movie.objects.filter(delete=False)
       
        for movie in movielist:
            final_rating=Rating.objects.filter(movie=movie).aggregate(Avg('rating'))
            print(final_rating)
        # print("m",movielist)
        # print("r",rate)
        return render(request,'member/member_home.html',{'movielist':movielist,'rate':final_rating})
       


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



    
def delete_movie_view(request,id):
    movies=Movie.objects.get(id=id)
    movies.delete = True
    movies.save()
    return redirect('admin_home')





class UpdateMovieview(UpdateView):
    model = Movie
    form_class = AddMovieForm
    template_name = 'admin/update_movie.html'
    def get_success_url(self) :
        return reverse_lazy('admin_home')



class Watchlistview(View):
    model=Watchlist
    form_class=Watchlistform
    template_name='member/watchlist.html'
    def get(self, request):
        list=Watchlist.objects.filter(user=request.user)
        return render(request, self.template_name,{'list':list})



class AddMovietoWatchlistview(View):
    model=Watchlist
    form_class=Watchlistform
    template_name='member/addmovieto.html'
    def get(self, request):
        return render(request, self.template_name,{ 'form': self.form_class})

    def post (self, request):
        form =self.form_class(request.POST)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            return redirect('member_home')
        else:
            msg = "Try Again!!! "
            return HttpResponse(msg)


class UserRatingview(ListView):
    model=Rating
    template_name='member/member_rating.html'
    def get(self,request):
        ratinglist=Rating.objects.filter(user=request.user)
        return render(request, self.template_name,{'ratinglist':ratinglist})




class AddRatingview(View):
    model = Rating
    form_class = AddRatingform
    template_name = 'member/rate_movie.html'
    def get(self,request):
        return render(request, self.template_name,{ 'form': self.form_class})
      

    def post(self, request):
        form =self.form_class(request.POST)
        # form = AddRatingform(initial={
        #     "user":user_id, # will get current user id 
        #     "movie":request.POST["movie"],
        #     "rating":request.POST["rating"],
        #     "comment":request.POST["comment"],
        #         })
      
        if form.is_valid():
            form.instance.user=request.user
            print("hello")
            if form.save():
                return redirect('member_home')
            else:
                msg = "you already done review "
            return HttpResponse(msg)
        else:
            msg = "Try Again!!! "
            return HttpResponse(msg)


class AddCastview(View):
    model=Cast
    form_class=AddCastform
    template_name='admin/add_cast.html'
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

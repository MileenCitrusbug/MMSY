from turtle import home
from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import Login,Home
from .models import *
from django import forms 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('signup_admin/',views.Signup_admin.as_view(),name='signup_admin'),
    path('signup_member/',views.Signup_member.as_view(),name='signup_member'),
    path('',views.Home.as_view(),name='home'),
    path('admin_home/',views.AdminHomeview.as_view(),name='admin_home'),
    path('member_home/',views.MemberHomeview.as_view(),name='member_home'),
    path('delete_movie/<int:id>/',views.delete_movie_view,name='delete_movie'),
    path('update_movie/<int:pk>/',views.UpdateMovieview.as_view(),name='update_movie'),
    path('logout/',views.Logout.as_view(),name='logout'),
    path('add_movie/',views.AddMovieview.as_view(),name='add_movie'),
    path('watchlist/',views.Watchlistview.as_view(),name='watchlist'),
    path('add_rating/',views.AddRatingview.as_view(),name='add_rating'),
    path('add_movietowatchlist/',views.AddMovietoWatchlistview.as_view(),name='add_movietowatchlist'),
    path('add_addcast/',views.AddCastview.as_view(),name='add_cast'),
    path('user_rating/',views.UserRatingview.as_view(),name='user_rating'),

]
#path('account/eventadminlogin/', views.AdminLogin.as_view(), name='admin-login'),
    # path('add_rating/',views.AddRatingview.as_view(),name='add_rating'),

#    path('', LoginView.as_view(
#            template_name='authentication/login.html',
#            redirect_authenticated_user=True),
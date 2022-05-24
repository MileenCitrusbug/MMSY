from dataclasses import fields
from pickle import TRUE
from pyexpat import model
from tkinter.tix import Select
from turtle import mode
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from movies.models import *


class Signupadmin(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name','email']
    def save(self,commit=True):
        user = super().save(commit=False)
        user.is_admin=True
        if commit:
            user.save()
        return user

class Signupmember(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name','email']
    def save(self,commit=True):
        user = super().save(commit=False)
        user.is_subscriber=True
        if commit:
            user.save()
        return user

class AddMovieForm(forms.ModelForm):
    # language=forms.ChoiceField(choices=CHOICE_LANGUAGE, widget=forms.Select)
    language = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,queryset=Language.objects.all(),required=False)
    cast = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,queryset=Cast.objects.all(),required=False)
    genre = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,queryset=Genre.objects.all(),required=False)
    model=Movie
    class Meta:
        model = Movie
        fields = ["movie","language","cast","genre"]
        
     

class AddtoWatchlistForm(forms.ModelForm):
    class Meta:
        model = Watchlist

        fields = "__all__"

  
class AddRatingform(forms.ModelForm):
    rating=forms.ChoiceField(choices=CHOICE_FIELD, widget=forms.Select)
    class Meta:
        model = Rating
        fields = ['movie','rating','comment']

class Watchlistform(forms.ModelForm):
    movie= forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,queryset=Movie.objects.filter(delete=False),required=False)
    class Meta:
        model = Watchlist
        fields = ['movie']

class AddCastform(forms.ModelForm):

    class Meta:
        model = Cast
        fields = '__all__'
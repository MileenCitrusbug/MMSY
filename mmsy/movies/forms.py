from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from movies.models import User, AbstractUser

class Signupform(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = '__all__'
    def save(self,commit=True):
        user = super().save(commit=False)
        user.save()
        return user
    # fname= forms.CharField(max_length=30)
    # lname= forms.CharField(max_length=30)
    # email = forms.EmailField(max_length=254)
    # password= forms.CharField(max_length=30)

# class loginform(forms.Form):
#     email = forms.EmailField(max_length=254)
#     password= forms.CharField(max_length=30)

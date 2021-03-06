# -*- coding: utf-8 -*-

from django import forms

from movies.models import User


# -----------------------------------------------------------------------------
# User
# -----------------------------------------------------------------------------

class UserCreationForm(forms.ModelForm):
    """Custom User"""

    class Meta():
        model = User
        fields = [
            "email",
            "password",
            "first_name",
            "last_name",
            "username"
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(UserCreationForm, self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        last_name = cleaned_data.get("last_name")
        first_name = cleaned_data.get("first_name")
        user_name = cleaned_data.get("username")

        if not email :
            raise forms.ValidationError(
                "Please add email."
            )
        if not password :
            raise forms.ValidationError(
                "Please add Password."
            )
        if not last_name :
            raise forms.ValidationError(
                "Please add last name."
            )
        if not first_name :
            raise forms.ValidationError(
                "Please add first name."
            )
        if not user_name :
            raise forms.ValidationError(
                "Please add user name."
            )
    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance


class UserChangeForm(forms.ModelForm):
    """Custom form to change User"""

    class Meta():
        model = User

        fields = [
            "email",
            "password",
            "first_name",
            "last_name",
            "username",
          
        ]

    def clean(self):
        cleaned_data = super(UserChangeForm, self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        last_name = cleaned_data.get("last_name")
        first_name = cleaned_data.get("first_name")
        username = cleaned_data.get("username")
        if not email :
            raise forms.ValidationError(
                "Please add email."
            )
        if not password :
            raise forms.ValidationError(
                "Please add Password."
            )
        if not last_name :
            raise forms.ValidationError(
                "Please add last name."
            )
        if not first_name :
            raise forms.ValidationError(
                "Please add first name."
            )
        if not username :
            raise forms.ValidationError(
                "Please add User name."
            )

   

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance
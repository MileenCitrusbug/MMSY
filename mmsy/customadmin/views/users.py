from multiprocessing import context
from re import template
from customadmin.mixins import HasPermissionsMixin
from customadmin.views.generic import (
    MyCreateView,
    MyDeleteView,
    MyListView,
    MyDetailView,
    MyLoginRequiredView,
    MyUpdateView,
)
from movies.models import *
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import TemplateView, DetailView
from django.contrib.auth import get_user_model, login,logout
from django.views.generic import View
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from audioop import reverse
from  customadmin.forms.user import UserChangeForm, UserCreationForm

# from ..forms import UserChangeForm, UserCreationForm
from django.shortcuts import reverse, render

# from customadmin.models import User, PurchasedProduct, BookedService

import csv



class UserDetailView(MyDetailView):
    template_name = "customadmin/adminuser/user_detail.html"
    context = {}

    def get(self, request, pk):
        self.context['user_detail'] = User.objects.filter(pk=pk).first()
        # self.context['movie_added'] = Movie.objects.filter(use)
        # self.context['booked_services'] = BookedService.objects.filter(user=pk)
        return render(request, self.template_name, self.context)


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "customadmin/index.html"
    context = {}

    def get(self, request):
        self.context['user_count']=User.objects.all().exclude(is_subscriber=False).count()
        self.context['movie_count']=Movie.objects.all().exclude(delete=True).count()
        self.context['delete_count']=Movie.objects.all().exclude(delete=False).count()
        return render(request, self.template_name, self.context)




class UserListView(MyListView):
    """View for User listing"""

    # paginate_by = 25
    ordering = ["id"]
    model = User
    queryset = model.objects.exclude(is_staff=True)
    template_name = "customadmin/adminuser/user_list.html"
    permission_required = ("customadmin.view_user",)

    def get_queryset(self):
        return self.model.objects.exclude(is_staff=True).exclude(email=self.request.user).exclude(email=None)


class LogoutView(View):
    template_name= "registration/logged_out.html"
    def get(self, request):
        logout(request)
        return redirect(self.template_name)

class LoginView(View):
    model=User
    template_name = 'customadmin/index.html'
    def get(self,request):
        return render(request,'registration/login.html')


    def post(self,request):
        email=request.POST['email']
        raw_password=request.POST['password']
        print(raw_password)
        pw=User.objects.get(email=email)
        print(email)
        print(pw)
        password=pw.password
        valid = check_password(raw_password,password)
        print(valid)
        if not valid:
            messages.warning(request, 'Please correct the error below.')
        else:
            user=User.objects.get(email=email)
            if user.is_superuser == True:
                login(request, user)
                return redirect('dashboard')
            else:
                login(request,user)
                return HttpResponse("invalid login")


class UserCreateView(MyCreateView):
    """View to create User"""

    model = User
    form_class = UserCreationForm
    template_name = "customadmin/adminuser/user_form.html"
    # permission_required = ("customadmin.add_user",)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # kwargs["user"] = self.request.user

        return kwargs

    def get_success_url(self):
        # opts = self.model._meta
        return reverse("customadmin:user-list")

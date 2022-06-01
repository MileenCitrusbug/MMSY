from multiprocessing import context
from pyexpat import model
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
import json

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
    model= Movie

    def get(self, request):
        self.context['user_count']=User.objects.all().exclude(is_subscriber=False).count()
        self.context['movie_count']=Movie.objects.all().exclude(delete=True).count()
        self.context['delete_count']=Movie.objects.all().exclude(delete=False).count()
        self.context['movie_name']=Movie.objects.values('movie').exclude(delete=True)
        list1=Movie.objects.filter(delete=False)
        # movi1=self.model.avaregereview()
        movie_name=[]
        movie_rating=[]
        for i in list1:
            name=i.movie
            movie_name.append(name)
            rating=i.avaregereview()
            movie_rating.append(rating)

            
            

        self.context['l1']=list1
        self.context['name']=movie_name
        self.context['rating']=movie_rating

        # print( type(self.context['movie']))

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


class UserDeleteView(MyDeleteView):
    """View to delete User"""

    model = User
    template_name = "customadmin/confirm_delete.html"
    permission_required = ("customadmin.delete_user",)

    def get_success_url(self):
        # opts = self.model._meta
        return reverse("customadmin:user-list")


class UserUpdateView(MyUpdateView):
    """View to update User"""

    model = User
    form_class = UserChangeForm
    template_name = "customadmin/adminuser/user_form_update.html"
    permission_required = ("customadmin.change_user",)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        
        # kwargs["user"] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["form"]=self.form_class
        return context

    def get_success_url(self):
        # opts = self.model._meta
        return reverse("customadmin:user-list")


def export_user_csv(request):

    output = []
    response = HttpResponse (content_type='text/csv')
    filename = u"User.csv"
    response['Content-Disposition'] = u'attachment; filename="{0}"'.format(filename)

    writer = csv.writer(response)
    query_set = User.objects.all()

    #Header
    writer.writerow(['Name', "Username",'Email',"is_admin", "is_superuser","is_subsriber"])
    for user in query_set:
        if user.groups.all():
            gp = user.groups.all()[0].name
        else:
            gp = None

        output.append([user.first_name, user.last_name, user.username, user.email, user.is_admin,user.is_superuser,user.is_subsriber])
    #CSV Data
    writer.writerows(output)
    return response
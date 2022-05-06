from pyexpat import model
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Language,Genre,Cast,Movie,Rating,Watchlist,subscriber
from .form import userceationform 

#admin.site.register(User,UserAdmin)
admin.site.register(subscriber)
admin.site.register(Language)
admin.site.register(Genre)
admin.site.register(Cast)
admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(Watchlist)

class customuseradmin(UserAdmin):
    model = User
    add_form = userceationform

admin.site.register(User,customuseradmin) 
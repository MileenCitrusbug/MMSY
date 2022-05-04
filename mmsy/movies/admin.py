from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Language,Genre,Cast,Movie,Rating,Watchlist,subscriber

admin.site.register(User,UserAdmin)
admin.site.register(subscriber)
admin.site.register(Language)
admin.site.register(Genre)
admin.site.register(Cast)
admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(Watchlist)

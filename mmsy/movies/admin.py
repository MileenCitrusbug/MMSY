from django.contrib import admin

from .models import User,Language,Genre,Cast,Movie,Rating,Watchlist

admin.site.register(User)
admin.site.register(Language)
admin.site.register(Genre)
admin.site.register(Cast)
admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(Watchlist)

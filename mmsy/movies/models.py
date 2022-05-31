import email
from unicodedata import name
from xml.etree.ElementTree import Comment
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.forms import BooleanField
from django.db.models import Avg



class User(AbstractUser):
    is_admin=models.BooleanField(default=False)
    is_subscriber=models.BooleanField(default=False)
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Language(models.Model): 
    language = models.CharField(max_length=20)
    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"
    def __str__(self):
        return self.language

        


class Cast(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=1)
    description = models.TextField()
    
    class Meta:
        verbose_name = "Cast"
        verbose_name_plural = "Casts"

    def __str__(self):
        return self.name

class Genre(models.Model):
    genre = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"

    def __str__(self):
        return self.genre

class Movie(models.Model):
    movie = models.CharField(max_length=50)
    language = models.ManyToManyField(Language)
    cast = models.ManyToManyField(Cast)
    genre = models.ManyToManyField(Genre)
    delete = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def avaregereview(self):
        rating=Rating.objects.filter(movie_id=self.pk).aggregate(average=Avg('rating'))
        avg=0
        if rating["average"] is not None:
            avg=int(rating["average"])
        return avg

   

    def __str__(self):
        return self.movie






CHOICE_FIELD = [
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
    ]
class Rating(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,  on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=CHOICE_FIELD,default=1)
    comment = models.TextField()

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"

    class Meta:
        unique_together = ['user', 'movie']

    def __str__(self):
        return self.movie.movie

    





class Watchlist(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Watchlist"
        verbose_name_plural = "Watchlists"

    def __str__(self):
        return str(self.user)+"  |  "+ str(self.movie)
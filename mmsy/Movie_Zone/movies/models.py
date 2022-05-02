import email
from unicodedata import name
from xml.etree.ElementTree import Comment
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_admin=models.BooleanField()
    is_user=models.BooleanField()
    name = models.CharField()
    email = models.EmailField(max_length=254)
    password = models.CharField()


class Language(models.Model):
    language = models.CharField(max_length=20)


class Cast(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    description = models.TextField()


class Genre(models.Model):
    genre = models.CharField(max_length=20)


class Movie(models.Model):
    movie = models.CharField(max_length=50)
    language = models.ManyToManyField(Language)
    cast = models.ManyToManyField(Cast)
    genre = models.ManyToManyField(Genre)


class Rating(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,  on_delete=models.CASCADE)
    rating = models.CharField()
    comment = models.TextField()


class Watchlist(models.Model):
    user = models.ForeignKey(User, verbose_name=("User name"), on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, verbose_name=("Movie name"), on_delete=models.CASCADE)

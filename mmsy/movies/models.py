import email
from unicodedata import name
from xml.etree.ElementTree import Comment
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# class UserManager(BaseUserManager):
#       def create_user(self, email, password, **extra_fields):
#         """
#         Create and save a User with the given email and password.
#         """
#         if not email:
#             raise ValueError(_('The Email must be set'))
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user

#       def create_superuser(self, email, password, **extra_fields):
#         """
#         Create and save a SuperUser with the given email and password.
#         """
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError(_('Superuser must have is_staff=True.'))
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError(_('Superuser must have is_superuser=True.'))
#         return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    is_admin=models.BooleanField(default=False)
    is_subscriber=models.BooleanField(default=False)
    # name=models.CharField(max_length=20)
    # name = models.CharField(max_length=30)
    # email = models.EmailField(max_length=254)
    # password = models.CharField(max_length=10)
    
# class Admin(models.Model):
#     user=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     email=models.EmailField(max_length=254)
#     mo_number=models.PositiveIntegerField()
#     password=models.CharField( max_length=50)

# class User(models.Model):
#     user=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     email=models.EmailField(max_length=254)
#     password=models.CharField( max_length=50)

# class subscriber(models.Model):
#     user=models.OneToOneField(User, on_delete=models.CASCADE)
#     name=models.CharField(max_length=20)
#     age=models.IntegerField()

    
    # def __str__(self):
    #     return self.user


class Language(models.Model): 
    language = models.CharField(max_length=20)

    def __str__(self):
        return self.language

class Cast(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Genre(models.Model):
    genre = models.CharField(max_length=20)

    def __str__(self):
        return self.genre

class Movie(models.Model):
    movie = models.CharField(max_length=50)
    language = models.ManyToManyField(Language)
    cast = models.ManyToManyField(Cast)
    genre = models.ManyToManyField(Genre)
   

    def __str__(self):
        return self.movie

class Rating(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,  on_delete=models.CASCADE)
    rating = models.CharField(max_length=10)
    comment = models.TextField()

    def __str__(self):
        return self.movie

class Watchlist(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.user
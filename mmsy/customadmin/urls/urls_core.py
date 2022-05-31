from django.urls import path
from customadmin import views
from django.contrib.auth import views as auth_views

app_name='customadmin'


urlpatterns = [
    path("", views.IndexView.as_view(), name="dashboard"),
        # User
    # path("users/", views.UserListView.as_view(), name="user-detail"),

    path("users/<int:pk>/detail/", views.UserDetailView.as_view(), name="user-detailview"),
    path("users/", views.UserListView.as_view(), name="user-list"),
    path("logout/", views.LogoutView.as_view(), name="user-logout"),
    path("login/", views.LoginView.as_view(), name="user-login"),
    path("users/create/", views.UserCreateView.as_view(), name="user-create"),
    path("users/<int:pk>/delete/", views.UserDeleteView.as_view(), name="user-delete"),
    path("users/<int:pk>/update/", views.UserUpdateView.as_view(), name="user-update"),
    path("export_user_csv", views.export_user_csv, name="export_user_csv"),
    path("movies/", views.MovieListView.as_view(), name="movie-detail"),
    path("testimonials/create/", views.TestimonialCreateView.as_view(), name="testimonial-create"),
    path("testimonials/<int:pk>/update/", views.TestimonialUpdateView.as_view(), name="testimonial-update"),
    path("testimonials/<int:pk>/delete/", views.TestimonialDeleteView.as_view(), name="testimonial-delete"),
    path("ajax-testimonials", views.TestimonialAjaxPagination.as_view(), name="testimonial-list-ajax"),
]  

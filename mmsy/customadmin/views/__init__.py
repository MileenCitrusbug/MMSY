


from .users import (
    IndexView,
    UserDetailView,
    # UserAjaxPagination,
    UserCreateView,
    UserDeleteView,
    UserListView,
    LoginView,
    LogoutView,
    # UserPasswordView,
    UserUpdateView,
    export_user_csv,
)


from .movies import (
    TestimonialAjaxPagination,
    TestimonialCreateView,
    TestimonialDeleteView,
    MovieListView,
    TestimonialUpdateView
    )
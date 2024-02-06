from django_registration.backends.activation.views import RegistrationView
from django.urls import include, path
from django.conf import settings

from userauth import views

from userauth.forms import CustomRegistrationForm

urlpatterns = [
    path("", views.user_list, name="user-list"),
    path("accounts/edit-profile/", views.edit_profile, name="edit_profile"),
    path("accounts/profile/", views.profile, name="profile"),
    path(
        "accounts/register/",
        RegistrationView.as_view(form_class=CustomRegistrationForm),
        name="django_registration_register",
    ),
    path("accounts/", include("django_registration.backends.activation.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]

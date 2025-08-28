from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy
from users.auth.views import AuthView, LoginFrontendView

urlpatterns = [
    # FRONTEND
    path(
        "login",
        LoginFrontendView.as_view(template_name="public/auth/login.html"),
        name="login",
    ),
    path(
        "logout",
        LogoutView.as_view(next_page=reverse_lazy(settings.LOGIN_URL)),
        name="logout",
    ),
    path(
        "forgot-password",
        AuthView.as_view(template_name="public/auth/forgot_password.html"),
        name="forgot-password",
    ),
    path(
        "register",
        AuthView.as_view(template_name="public/auth/register.html"),
        name="register",
    ),
]

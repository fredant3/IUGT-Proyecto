from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView
from users.auth.forms import LoginForm

from templates.sneat import TemplateLayout
from templates.sneat.helpers.theme import TemplateHelper


class AuthView(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context.update(
            {"layout_path": TemplateHelper.set_layout("layout_blank.html", context)}
        )
        return context


class LoginFrontendView(LoginView):
    form_class = LoginForm
    next_page = reverse_lazy("modules:index")

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["uri_api_login"] = "api_auth:login"
        context["successful_redirection"] = self.next_page
        context.update(
            {"layout_path": TemplateHelper.set_layout("layout_blank.html", context)},
        )
        return context


class LoginApiView(TokenObtainPairView):
    form_class = LoginForm

    def post(self, request, *args, **kwargs):
        loginApi = super().post(request, *args, **kwargs)

        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

        return loginApi

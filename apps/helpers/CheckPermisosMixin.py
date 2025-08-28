from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy


class CheckPermisosMixin(object):
    permission_required = ""
    url_redirect = None

    def get_perms(self):
        if isinstance(self.permission_required, str):
            return [self.permission_required]
        else:
            return self.permission_required

    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy("auth:login")
        return self.url_redirect

    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perms(self.get_perms()):
            return super().dispatch(request, *args, **kwargs)
        messages.error(request, "No tienes permisos para realizar esta acción.")
        return redirect(self.get_url_redirect())

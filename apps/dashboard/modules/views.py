from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from templates.sneat import TemplateLayout


class Modules(LoginRequiredMixin, TemplateView):
    login_url = "auth:login"
    template_name = "public/modules/index.html"

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["modules"] = [
            {
                "title": "Gestión Humana",
                "url": "gestion_humana",
                "image": "img/modules/gestion_humana.png",
            },
            {
                "title": "Gestión Administrativa",
                "url": "administracion",
                "image": "img/modules/gestion_administrativa.png",
            },
            {
                "title": "Tecnología Comunicación e Información",
                "url": "tecnologia",
                "image": "img/modules/tecnologia.png",
            },
        ]
        return context

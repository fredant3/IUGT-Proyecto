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
                "title": "Asesoría Jurídica",
                "url": "asesoria",
                "image": "img/modules/asesoria_juridica.png",
            },
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
                "title": "Unidad de Respuesta Inmediata",
                "url": "uri:list",
                "image": "img/modules/ambulancias.png",
            },
            {
                "title": "Potencia",
                "url": "potencia",
                "image": "img/modules/incidente.png",
            },
            {
                "title": "Organización",
                "url": "organizacion",
                "image": "img/modules/organizacion.png",
            },
            {
                "title": "Presupuestos",
                "url": "presupuesto",
                "image": "img/modules/presupuesto.png",
            },
            {
                "title": "Planificación",
                "url": "planificacion",
                "image": "img/modules/planificacion.png",
            },
            {
                "title": "Protección y Seguridad Integral",
                "url": "seguridad",
                "image": "img/modules/seguridad.png",
            },
            {
                "title": "Biblioteca de Manuales",
                "url": "bibliotecas",
                "image": "img/modules/biblioteca.png",
            },
            {
                "title": "Operaciones",
                "url": "operaciones",
                "image": "img/modules/ambulancia.png",
            },
            {
                "title": "Tecnología Comunicación e Información",
                "url": "tecnologia",
                "image": "img/modules/tecnologia.png",
            },
            {
                "title": "Gestion Comunicacional",
                "url": "gc_info",
                "image": "img/modules/GC_icon.png",
            },
            {
                "title": "Reporte Averias",
                "url": "reporte_averia:list",
                "image": "img/modules/averia.png",
            },
        ]
        return context

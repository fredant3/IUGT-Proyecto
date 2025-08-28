import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from templates.sneat import TemplateLayout
from gestion_comunicacional.services import GestioncomunicacionalService


class GestioncomunicacionalListView(
    LoginRequiredMixin, CheckPermisosMixin, TemplateView
):
    permission_required = "gestioncomuicacional.ver_gestioncomunicacional"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestion comunicacional"
        context["indexUrl"] = reverse_lazy("gc_info")
        context["module"] = "Gestion comunicacional"
        context["submodule"] = "Gestion comunicacional"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("gestioncomunicacional:create")
        context["listApiUrl"] = reverse_lazy("api_gestioncomunicacional:list")
        context["updateUrl"] = reverse_lazy("gestioncomunicacional:update", args=[0])
        context["deleteUrl"] = reverse_lazy("gestioncomunicacional:delete", args=[0])
        context["heads"] = columns
        context["columns"] = mark_safe(json.dumps(columns))
        return TemplateLayout.init(self, context)

    def getColumns(self):
        return [
            {
                "data": "id",
                "name": "id",
                "title": "ID",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "nombre_actividad",
                "name": "nombre_actividad",
                "title": "Nombre de la actividad",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "actividad_realizada",
                "name": "actividad_realizada",
                "title": "Actividad Realizada",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "descripcion_actividad",
                "name": "descripcion_actividad",
                "title": "descripción actividad",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class GestioncomunicacionalListApiView(ListController, CheckPermisosMixin):
    permission_required = "gestioncomunicacional.ver_gestioncomunicacional"

    def __init__(self):
        self.service = GestioncomunicacionalService()

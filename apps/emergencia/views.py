from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from emergencia.operaciones.models import Emergencia
from django.db.models import Count
from templates.sneat import TemplateLayout
from helpers.BaseModelMixin import ESTADOS_CHOICES


class EmergenciaView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "emergencia_index"
    url_redirect = reverse_lazy("modules:index")
    template_name = "dashborad/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Operaciones"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Operaciones"
        
        # 1. Gráfico de barras: Emergencias por tipo de incidencia
        emergencias_por_incidencia = Emergencia.objects.values(
            'incidencia__nombre_incidencia'
        ).annotate(
            total=Count('id')
        ).order_by('-total')[:10]
        
        # 2. Gráfico de torta: Emergencias por estado
        emergencias_por_estado = Emergencia.objects.values(
            'estado'
        ).annotate(
            total=Count('id')
        ).order_by('-total')
        
        # 3. NUEVO Gráfico de barras: Emergencias por organismo
        emergencias_por_organismo = Emergencia.objects.values(
            'organismo__nombre'  # Asume que Organismo tiene campo 'nombre'
        ).annotate(
            total=Count('id')
        ).order_by('-total')[:10]  # Limitar a 10 organismos
        
        # Preparar datos para los gráficos
        # Gráfico 1: Barras (incidencias)
        context["data"] = [item['total'] for item in emergencias_por_incidencia]
        context["labels"] = [item['incidencia__nombre_incidencia'] for item in emergencias_por_incidencia]
        
        # Gráfico 2: Torta (estados)
        context["dataTorta"] = [item['total'] for item in emergencias_por_estado]
        context["labelsTorta"] = [self.get_estado_display(item['estado']) for item in emergencias_por_estado]
        
        # Gráfico 3: Barras (organismos)
        context["dataOrganismos"] = [item['total'] for item in emergencias_por_organismo]
        context["labelsOrganismos"] = [item['organismo__nombre'] for item in emergencias_por_organismo]
        
        # Colores para gráficos
        context["colorsTorta"] = [
            '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF',
            '#FF9F40', '#8AC24A', '#607D8B', '#E91E63', '#00BCD4'
        ][:len(context["labelsTorta"])]
        
        context["colorsOrganismos"] = [
            '#4e73df', '#1cc88a', '#36b9cc', '#f6c23e', '#e74a3b',
            '#858796', '#5a5c69', '#3a3b45', '#2e59d9', '#17a673'
        ][:len(context["labelsOrganismos"])]
        
        context["submoduleList"] = (
            ("Operaciones", reverse_lazy("operaciones:list")),
            ("Incidencias", reverse_lazy("operaciones_incidencias:list")),
            ("Organismos", reverse_lazy("organismo:list")),
        )
        return TemplateLayout.init(self, context)
    
    def get_estado_display(self, estado_code):
        """Convierte el código de estado a su nombre completo"""
        estados_dict = dict(ESTADOS_CHOICES)
        return estados_dict.get(estado_code, estado_code)
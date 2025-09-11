from helpers.CrudMixin import CrudService
from rrhh.tipos_sueldos.repositories import TipoSueldoRepository
from django.db.models import Q
from .models import TIPO_CHOICES, ESTATUS_CHOICES


class TipoSueldoService(CrudService):
    def __init__(self):
        self.repository = TipoSueldoRepository()

    def criteria(self, search, arg=None):
        query = Q()

        if search:
            tipo_codes = [
                code
                for code, name in TIPO_CHOICES
                if search.lower() in name.lower() or search.lower() == code.lower()
            ]

            estatus_codes = [
                code
                for code, name in ESTATUS_CHOICES
                if search.lower() in name.lower() or search.lower() == code.lower()
            ]

            try:
                amount = float(search)
                amount_query = Q(monto=amount)
            except (ValueError, TypeError):
                amount_query = Q()

            query &= (
                Q(tipo__in=tipo_codes)
                | Q(estatus__in=estatus_codes)
                | Q(descripcion__icontains=search)
                | amount_query
                | Q(tipo__icontains=search)
                | Q(estatus__icontains=search)
            )

        return query

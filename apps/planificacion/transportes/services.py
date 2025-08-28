from django.db.models import Q
from helpers.CrudMixin import CrudService
from helpers.BaseModelMixin import ESTADOS_CHOICES, MONTH_CHOICES

from .repositories import TransporteRepository


class TransporteService(CrudService):
    def __init__(self):
        self.repository = TransporteRepository()

    def criteria(self, search, arg=None):
        query = Q()

        if search:
            estados_codes = [
                code for code, name in ESTADOS_CHOICES if search.lower() in name.lower()
            ]
            meses_codes = [
                code for code, name in MONTH_CHOICES if search.lower() in name.lower()
            ]

            query &= (
                Q(transporte__icontains=search)
                | Q(estado__in=estados_codes)
                | Q(mes__in=meses_codes)
                | Q(cantidad__icontains=search)
                | Q(estado__icontains=search)
                | Q(mes__icontains=search)
            )
        return query

from administracion.tipo_averia.repositories import TipoAveriaRepository
from helpers.CrudMixin import CrudService
from django.db.models import Q


class TipoAveriaService(CrudService):
    def __init__(self):
        self.repository = TipoAveriaRepository()

    def validate(self, payload):
        nombre = payload.get("nombre", "")
        if len(nombre) < 3 or len(nombre) > 200:
            raise ValueError("El nombre debe tener entre 3 y 200 caracteres")
        return payload

    def criteria(self, search, arg=None):
        query = Q()
        if search:
            query &= Q(nombre__icontains=search)
        return query

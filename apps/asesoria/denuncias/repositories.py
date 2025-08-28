from asesoria.denuncias.models import Denuncia, Denunciado, Denunciante
from django.db.models import F, Value
from django.db.models.functions import Concat
from helpers.RepositoryMixin import Repository


class DenuncianteRepository(Repository):
    def __init__(self):
        self.entity = Denunciante


class DenunciadoRepository(Repository):
    def __init__(self):
        self.entity = Denunciado


class DenunciaRepository(Repository):
    def __init__(self):
        self.entity = Denuncia

    def after_get_all(self, entities):
        return entities.annotate(
            denunciante_nombre=Concat(
                F("denunciante__nombres"), Value(" "), F("denunciante__apellidos")
            ),
            denunciado_nombre=Concat(
                F("denunciado__nombres"), Value(" "), F("denunciado__apellidos")
            ),
        )

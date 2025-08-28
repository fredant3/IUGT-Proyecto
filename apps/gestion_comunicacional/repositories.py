from helpers.RepositoryMixin import Repository

from gestion_comunicacional.models import GestionComunicacional


class GestioncomunicacionalRepository(Repository):
    def __init__(self):
        self.entity = GestionComunicacional

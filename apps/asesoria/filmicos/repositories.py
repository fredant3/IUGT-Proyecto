from asesoria.filmicos.models import RegistroFilmico
from helpers.RepositoryMixin import Repository


class RegistroFilmicoRepository(Repository):
    def __init__(self):
        self.entity = RegistroFilmico

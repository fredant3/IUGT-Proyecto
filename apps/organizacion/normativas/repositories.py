from helpers.RepositoryMixin import Repository
from organizacion.normativas.models import Normativa


class NormativaRepository(Repository):
    def __init__(self):
        self.entity = Normativa

from helpers.RepositoryMixin import Repository
from potencia.uri.models import Uri


class UriRepository(Repository):
    def __init__(self):
        self.entity = Uri

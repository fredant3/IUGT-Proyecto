from helpers.RepositoryMixin import Repository
from emergencia.organismo.models import Organismo


class OrganismoRepository(Repository):
    def __init__(self):
        self.entity = Organismo

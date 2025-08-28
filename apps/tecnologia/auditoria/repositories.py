from helpers.RepositoryMixin import Repository
from tecnologia.auditoria.models import RequestLog


class AuditoriaRepository(Repository):
    def __init__(self):
        self.entity = RequestLog

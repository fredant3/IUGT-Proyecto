from helpers.CrudMixin import CrudService

from .repositories import SueldoRepository


class SueldoService(CrudService):
    def __init__(self):
        self.repository = SueldoRepository()

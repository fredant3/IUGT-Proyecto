from tecnologia.groups.repositories import GroupRepository
from helpers.CrudMixin import CrudService


class GrupoPermisosService(CrudService):
    select = (
        "id",
        "name",
    )

    def __init__(self):
        self.repository = GroupRepository()

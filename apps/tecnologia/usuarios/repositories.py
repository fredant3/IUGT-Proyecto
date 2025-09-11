from helpers.RepositoryMixin import Repository
from users.auth.models import User
from rrhh.empleados.models import Empleado


class UserRepository(Repository):
    def __init__(self):
        self.entity = User

    def get_all_with_related(self):
        empleados_con_usuarios = (
            Empleado.objects.filter(usuario__isnull=False)
            .select_related("usuario")
            .prefetch_related("contratos")
        )

        empleados_map = {emp.usuario_id: emp for emp in empleados_con_usuarios}

        users = self.entity.objects.all()

        return users, empleados_map

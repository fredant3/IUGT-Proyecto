from helpers.CrudMixin import CrudService
from tecnologia.usuarios.repositories import UserRepository


class UserService(CrudService):
    def __init__(self):
        self.repository = UserRepository()

    def get_all_with_related_info(self, draw, start, length, search=None):
        users, empleados_map = self.repository.get_all_with_related()
        result = []

        for user in users:
            empleado = empleados_map.get(user.id)
            contrato = (
                empleado.contratos.first()  # Cambiado de contrato_set a contratos
                if empleado and hasattr(empleado, "contratos")
                else None
            )

            user_data = {
                "id": user.id,
                "username": user.username,
                "password": user.password,
                "dni": user.dni,
                "is_active": "Activo" if user.is_active else "Inactivo",
                "empleado_nombre": "No asignado",
                "empleado_cedula": "N/A",
                "tipo_contrato": "Sin contrato",
                "estatus_contrato": "N/A",
                "departamento": "N/A",
                "cargo": "N/A",
            }

            if empleado:
                user_data.update(
                    {
                        "empleado_nombre": f"{empleado.nombres} {empleado.apellidos}",
                        "empleado_cedula": empleado.cedula,
                    }
                )

                if contrato:
                    user_data.update(
                        {
                            "tipo_contrato": contrato.get_tipo_display(),
                            "estatus_contrato": contrato.get_estatus_display(),
                            "departamento": (
                                contrato.departamento.nombre
                                if contrato.departamento
                                else "N/A"
                            ),
                            "cargo": contrato.cargo.cargo if contrato.cargo else "N/A",
                        }
                    )

            result.append(user_data)

        return self.response(result, start, length, draw)

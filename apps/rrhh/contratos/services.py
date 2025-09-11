from helpers.CrudMixin import CrudService

from rrhh.contratos.repositories import ContratoRepository
from rrhh.empleados.repositories import EmpleadoRepository
from administracion.departamentos.repositories import DepartamentoRepository
from administracion.sedes.repositories import SedeRepository
from rrhh.cargos.repositories import CargoRepository

from users.auth.models import User
from rrhh.empleados.models import Empleado
from rrhh.educaciones.models import Educacion
from rrhh.familiares.models import Familiar
from rrhh.dotaciones.models import Dotacion
import datetime

from django.db.models import Q
from rrhh.contratos.models import TIPO_CONTRATOS_CHOICES


class ContratoService(CrudService):
    select = (
        "id",
        "empleado__nombres",
        "empleado__cedula",
        "tipo",
        "cargo__cargo",
    )

    def __init__(self):
        self.repository = ContratoRepository()
        self.departamento_repository = DepartamentoRepository()
        self.empleado_repository = EmpleadoRepository()
        self.cargo_repository = CargoRepository()
        self.sede_repository = SedeRepository()

    def search_departamento(self, id):
        return self.departamento_repository.getById(id)

    def search_empleado(self, id):
        return self.empleado_repository.getById(id)

    def search_cargo(self, id):
        return self.cargo_repository.getById(id)

    def search_sede(self, id):
        return self.sede_repository.getById(id)

    def relationship(self, payload, *arg, **kwargs):
        payload["empleado"] = self.search_empleado(payload.get("empleado"))
        payload["departamento"] = self.search_departamento(payload.get("departamento"))
        payload["cargo"] = self.search_cargo(payload.get("cargo"))
        payload["sede"] = self.search_sede(payload.get("sede"))

        return payload

    def criteria(self, search, arg=None):
        query = Q()

        if search:
            tipo_codes = [
                code
                for code, name in TIPO_CONTRATOS_CHOICES
                if search.lower() in name.lower() or search.lower() == code.lower()
            ]

            query &= (
                Q(empleado__nombres__icontains=search)
                | Q(empleado__cedula__icontains=search)
                | Q(tipo__in=tipo_codes)
                | Q(tipo__icontains=search)
                | Q(cargo__cargo__icontains=search)
            )

        return query

    def destroyer(self, payload):
        deleted_at = {
            "deleted_by": payload.deleted_by,
            "updated_by": payload.updated_by,
            "deleted_at": datetime.datetime.now(),
            "updated_at": datetime.datetime.now(),
        }
        Empleado.objects.filter(id=payload.empleado.id).update(**deleted_at)
        User.objects.filter(dni=payload.empleado.cedula).update(is_active=False)
        Educacion.objects.filter(id=payload.empleado.id).update(**deleted_at)
        Familiar.objects.filter(id=payload.empleado.id).update(**deleted_at)
        Dotacion.objects.filter(id=payload.empleado.id).update(**deleted_at)
        return self.repository.delete(payload)

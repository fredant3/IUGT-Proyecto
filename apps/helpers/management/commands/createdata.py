import random
from django.core.management.base import BaseCommand
from faker import Faker
from helpers.management.commands.seed.administracion._Departamento import (
    DepartamentoFaker,
)
from helpers.management.commands.seed.administracion._Inventario import ArticleFake
from helpers.management.commands.seed.administracion._Sede import SedesFaker
from helpers.management.commands.seed.administracion._Averia import AveriaFake
from helpers.management.commands.seed.potencia._Incidencias import IncidenciaFake
from helpers.management.commands.seed.users._UserFaker import UserFaker
from helpers.management.commands.seed.users._GruposPermisosFaker import Roles
from helpers.management.commands.seed.emergencia._Incidencias import EmergenciaFake

from helpers.management.commands.seed.rrhh._TipoSueldoFake import TipoSueldoFake
from helpers.management.commands.seed.rrhh._CargosFake import CargosFake
from helpers.management.commands.seed.rrhh._ContratosFake import ContratosFake


class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):
        fake = Faker("es_ES")

        Roles.execute()

        UserFaker.admin_user()
        UserFaker.director_user()
        UserFaker.gerente_user()
        UserFaker.supervisor_user()
        UserFaker.analista_user()

        # Gestion Administrativa (Inventario)
        ArticleFake.type_article()
        ArticleFake.tecnologia(fake)
        ArticleFake.consumibles(fake)
        ArticleFake.mobiliario(fake)
        ArticleFake.vehiculo(fake)

        SedesFaker.add_sedes(fake)
        DepartamentoFaker.add_departamentos(fake)
        IncidenciaFake.tipo_incidencia()
        AveriaFake.tipo_averia()
        EmergenciaFake.organismo()
        EmergenciaFake.tipo_incidencia()

        # Gestion Humana (RRHH)
        TipoSueldoFake.execute(fake)
        CargosFake.execute(fake)
        ContratosFake.execute(fake, random.randint(1, 55))

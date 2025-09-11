
from administracion.departamentos.models import Departamento


class DepartamentoFaker:

    def add_departamentos(faker):

        for _ in range(7):

            dep = Departamento.objects.create(nombre=faker.name())
            print(f" {dep.nombre} registrado")

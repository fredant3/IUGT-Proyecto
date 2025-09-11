import faker.providers
from administracion.sedes.models import Sede

SEDES = [
    "CARACAS",
    "REGION OCCIDENTE",
    "LITORAL",
    "REGION ORIENTAL",
    "MIRANDA",
    "GUAIRA",
    "NORTE",
    "CENTRO",
    "ZULIA",
    "PUNTA CARREÑA",
    "PUNTA BOLIVAR",
    "PUNTA MAGDALENA",
    "PUNTA CORDOBA",
    "PUNTA CHACO",
    "PUNTA FERNANDO",
    "PUNTA TOVAR",
    "PUNTA ARAGUA",
    "PUNTA ARICA",
    "PUNTA AYACUCHO",
    "PUNTA BOLIVAR",
]

ESTATUS_CHOICES = [
    "act",
    "rem",
    "cer",
]


class Provider(faker.providers.BaseProvider):

    def sedes_estatus_choices(self):
        return self.random_element(ESTATUS_CHOICES)


class SedesFaker:

    def add_sedes(faker):
        faker.add_provider(Provider)
        for entity in SEDES:

            sed = Sede.objects.create(
                sede=entity,
                estatus=faker.sedes_estatus_choices(),
            )
            print(f"{sed.sede} registrado")

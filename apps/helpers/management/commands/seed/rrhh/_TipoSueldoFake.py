from rrhh.tipos_sueldos.models import TipoSueldo
from faker import Faker
import random

TIPOS_DE_SUELDOS = [
    "ticket",
    "guerra",
    "discapacidad",
    "menor_12",
    "hijos_13_18",
    "hijos_discapacidad",
    "profesionalismo",
    "minimo",
]


class TipoSueldoFake:
    def execute(faker: Faker):
        for tipo_sueldo in TIPOS_DE_SUELDOS:
            model = TipoSueldo.objects.create(
                tipo=tipo_sueldo,
                monto=faker.pydecimal(
                    left_digits=5,
                    right_digits=2,
                    positive=True,
                    min_value=100,
                    max_value=10000,
                ),
                descripcion=faker.texts(nb_texts=2),
                estatus=random.choice(["act", "sup"]),
            )
            print(f"Tipo de sueldo {model.tipo} registrado")

import random

import faker
from administracion.averia.models import TipoAveria

TIPOS_DE_AVERIA = ["BUENO", "DEFECTUOSO", "EN REPARACION"]


class AveriaProvider(faker.providers.BaseProvider):
    def inventario(self):
        return self.random_element(BIEN_NACIONAL)


class AveriaFake:
    def tipo_averia():
        for avg in TIPOS_DE_AVERIA:
            TipoAveria.objects.create(nombre=avg)

    def averia(faker):
        faker.add_provider(AveriaProvider)
        for _ in range(15):
            tipoArticulo = TipoArticulo.objects.order_by("?").first()
            articulo = Articulo.objects.create(
                problema=faker.text(),
                ubicacion=faker.name(),
                serial=random.randint(1, 18),
                codigo_bn=random.randint(1, 9),
                modelo=faker.name(),
                placa=random.randint(1, 8),
                cantidad_combustible=random.randint(1, 18),
                cantidad=random.randint(1, 18),
                tipo_articulo=tipoArticulo,
                condicion=random.choice(TIPO_CONSIDCION),
                fecha_adq=faker.date(),
                asignado=random.choice([True, False]),
            )
            print(f"Articulo {articulo.marca}, {articulo.serial} registrado")

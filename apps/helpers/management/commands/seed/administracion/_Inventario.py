import random

import faker.providers
from administracion.inventario.models import Articulo, TipoArticulo

TIPOS_DE_ARTICULOS = [
    "tecnologia",
    "consumible",
    "mobiliario",
    "vehiculo",
]

TIPO_CONSIDCION = ["N", "U", "D"]

BIEN_NACIONAL = [
    "Computador de Escritorio",
    "Laptop",
    "Servidor",
    "Impresora",
    "Camara",
    "Televisor",
    "Amplificador",
]


class ArticuloProvider(faker.providers.BaseProvider):
    def inventario(self):
        return self.random_element(BIEN_NACIONAL)


class ArticleFake:
    def type_article():
        tiposArticulos = TipoArticulo.objects.all()

        if tiposArticulos.count() > 0:
            return None

        for tipoArticulo in TIPOS_DE_ARTICULOS:
            entity = TipoArticulo.objects.create(nombre=tipoArticulo)
            print(f"Tipo de articulo {entity.nombre} registrado")

    def tecnologia(fake):
        tipo_tecnologia, _ = TipoArticulo.objects.get_or_create(nombre="tecnologia")

        for _ in range(25):
            articulo = Articulo.objects.create(
                nombre=fake.random_element(
                    [
                        "Laptop",
                        "Computadora de escritorio",
                        "Tablet",
                        "Smartphone",
                        "Monitor",
                        "Impresora",
                        "Router",
                        "Switch de red",
                        "Proyector",
                    ]
                ),
                marca=fake.random_element(
                    ["Dell", "HP", "Lenovo", "Apple", "Samsung", "Asus", "Acer"]
                ),
                modelo=fake.bothify(text="??-####"),
                descripcion=fake.sentence(),
                serial=fake.bothify(text="SN-########"),
                codigo_bn=fake.bothify(text="GBT-########"),
                cantidad=random.randint(1, 10),
                tipo_articulo=tipo_tecnologia,
                condicion=random.choice(["A", "B", "C", "-"]),
                fecha_adq=fake.date_between(start_date="-5y", end_date="today"),
                asignado=random.choice(["si", "no"]),
            )
            print(
                f"Artículos de tecnología {articulo.nombre}, {articulo.serial} registrado"
            )

    def consumibles(fake):
        tipo_consumible, _ = TipoArticulo.objects.get_or_create(nombre="consumible")

        for _ in range(25):
            articulo = Articulo.objects.create(
                nombre=fake.random_element(
                    [
                        "Cartucho de tinta",
                        "Toner",
                        "Papel A4",
                        "Resmas de papel",
                        "Marcadores",
                        "Lápices",
                        "Cuadernos",
                        "Folderes",
                        "Tijeras",
                    ]
                ),
                marca=fake.random_element(
                    ["HP", "Epson", "Bic", "Faber-Castell", "Norma", "Scribe"]
                ),
                modelo=fake.bothify(text="CONS-####"),
                descripcion=fake.sentence(),
                serial=fake.bothify(text="CON-########"),
                codigo_bn=fake.bothify(text="GBC-########"),
                cantidad=random.randint(10, 100),
                tipo_articulo=tipo_consumible,
                condicion="-",
                fecha_adq=fake.date_between(start_date="-2y", end_date="today"),
                asignado="no",
            )
            print(
                f"Artículos de consumibles {articulo.nombre}, {articulo.serial} registrado"
            )

    def mobiliario(fake):
        tipo_mobiliario, _ = TipoArticulo.objects.get_or_create(nombre="mobiliario")

        for _ in range(15):
            articulo = Articulo.objects.create(
                nombre=fake.random_element(
                    [
                        "Escritorio",
                        "Silla ejecutiva",
                        "Silla ergonómica",
                        "Archivador",
                        "Estantería",
                        "Mesa de reuniones",
                        "Lockers",
                        "Pizarra acrílica",
                        "Perchero",
                    ]
                ),
                marca=fake.random_element(
                    ["Herman Miller", "Steelcase", "Ikea", "OFI", "Mobles"]
                ),
                modelo=fake.bothify(text="MOB-####"),
                descripcion=fake.sentence(),
                serial=fake.bothify(text="MOB-########"),
                codigo_bn=fake.bothify(text="GBM-########"),
                cantidad=random.randint(1, 5),
                tipo_articulo=tipo_mobiliario,
                condicion=random.choice(["A", "B", "C", "-"]),
                fecha_adq=fake.date_between(start_date="-10y", end_date="today"),
                asignado=random.choice(["si", "no"]),
            )
            print(
                f"Artículos de mobiliario {articulo.nombre}, {articulo.serial} registrado"
            )

    def vehiculo(fake):
        tipo_vehiculo, _ = TipoArticulo.objects.get_or_create(nombre="vehiculo")

        for _ in range(10):
            articulo = Articulo.objects.create(
                nombre=fake.random_element(
                    [
                        "Automóvil",
                        "Camioneta",
                        "Motocicleta",
                        "Camión",
                        "Autobús",
                        "Bicicleta",
                    ]
                ),
                marca=fake.random_element(
                    ["Toyota", "Ford", "Chevrolet", "Nissan", "Honda", "Yamaha"]
                ),
                modelo=str(random.randint(2010, 2023)),
                descripcion=fake.sentence(),
                placa=fake.license_plate(),
                cantidad_combustible=random.randint(30, 80),
                serial=fake.bothify(text="VEH-########"),
                codigo_bn=fake.bothify(text="GBV-########"),
                cantidad=1,
                tipo_articulo=tipo_vehiculo,
                condicion=random.choice(["A", "B", "C"]),
                fecha_adq=fake.date_between(start_date="-10y", end_date="today"),
                asignado=random.choice(["si", "no"]),
            )
            print(
                f"Artículos de vehículos {articulo.nombre}, {articulo.serial} registrado"
            )

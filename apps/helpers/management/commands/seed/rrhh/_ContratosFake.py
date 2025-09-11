import random
from faker import Faker
from rrhh.cargos.models import Cargo
from rrhh.empleados.models import Empleado
from rrhh.educaciones.models import Educacion
from rrhh.familiares.models import Familiar
from rrhh.dotaciones.models import Dotacion
from rrhh.contratos.models import Contrato

from users.auth.models import User
from administracion.departamentos.models import Departamento
from administracion.sedes.models import Sede

ESTATUS_CHOICES = (
    ("act", "Activo"),
    ("vac", "En vacaciones"),
    ("sus", "Suspendido"),
    ("des", "Se despedio"),
    ("ren", "Ha renunciado"),
)
NACIONALIDAD_CHOICES = (
    ("ve", "Venezolano"),
    ("ex", "Extranjero"),
)
SEXO_CHOICES = (
    ("f", "Femenino"),
    ("m", "Masculino"),
)
ESTADO_CIVIL_CHOICES = (
    ("s", "Soltero"),
    ("c", "Casado"),
    ("d", "Divorviado"),
    ("v", "Viudo"),
)
TIPO_SANGRE_CHOICES = (
    ("a+", "A+ (Rh positivo)"),
    ("a-", "A- (Rh negativo)"),
    ("b+", "B+ (Rh positivo)"),
    ("b-", "B- (Rh negativo)"),
    ("ab+", "AB+ (Rh positivo)"),
    ("ab-", "AB- (Rh negativo)"),
    ("o+", "O+ (Rh positivo)"),
    ("o-", "O- (Rh negativo)"),
)
TIPO_CONTRATOS = (
    ("Fi", "Fijo"),
    ("Te", "Temporal"),
    ("I", "Indefinido"),
    ("HP", "Por Horas"),
    ("P", "Practicante"),
    ("pro", "Por Proyecto"),
    ("Tar", "Por Tarea"),
    ("In", "Interno"),
    ("E", "Externo"),
    ("O", "Otro"),
)
TALLA_CAMISA_CHOICES = (
    ("XS", "Extra Pequena"),
    ("S", "Pequena"),
    ("M", "Mediana"),
    ("L", "Grande"),
    ("XL", "Extra Grande"),
)
TALLA_PANTALON_CHOICES = (
    ("8", "Extra Pequena (Dama)"),
    ("10", "Pequena (Dama)"),
    ("12", "Mediana (Dama)"),
    ("14", "Grande (Dama)"),
    ("16", "Extra Grande (Dama)"),
    ("18", "Super Grande (Dama)"),
    ("20", "Gigante (Dama)"),
    ("28", "Extra Pequena (Caballero)"),
    ("30", "Pequena (Caballero)"),
    ("32", "Mediana (Caballero)"),
    ("34", "Grande (Caballero)"),
    ("36", "Extra Grande (Caballero)"),
    ("38", "Super Grande (Caballero)"),
    ("40", "Gigante (Caballero)"),
    ("42", "Extra Gigante (Caballero)"),
)
TALLA_ZAPATO_CHOICES = (
    ("33", "Talla 33"),
    ("34", "Talla 34"),
    ("35", "Talla 35"),
    ("36", "Talla 36"),
    ("37", "Talla 37"),
    ("38", "Talla 38"),
    ("39", "Talla 39"),
    ("40", "Talla 40"),
    ("41", "Talla 41"),
    ("42", "Talla 42"),
    ("43", "Talla 43"),
    ("44", "Talla 44"),
    ("45", "Talla 45"),
    ("46", "Talla 46"),
)
TIPO_CONTRATOS_CHOICES = (
    ("pasante", "Pasante"),
    ("prueba", "Periodo de Prueba"),
    ("contrato", "Contratado"),
    ("fijo", "Personal Fijo"),
)
ESTATUS_CONTRATO_CHOICES = (
    ("act", "Activo"),
    ("pen", "Pendiente de Inicio"),
    ("sus", "Suspendido"),
    ("ter", "Terminado"),
    ("ren", "Renuncia Voluntaria"),
    ("des", "Despido"),
    ("fin", "Finalizado por Término de Contrato"),
    ("inc", "Incapacitado"),
    ("lic", "En Licencia"),
    ("vac", "En Vacaciones"),
    ("aju", "Ajuste de Contrato"),
    ("ces", "Cesado"),
    ("ret", "Jubilado/Retirado"),
    ("fal", "Fallecido"),
)


class ContratosFake:
    def execute(faker: Faker, cantidad: int = 5):
        for _ in range(cantidad):
            empleado = ContratosFake.empleado(faker)

            ContratosFake.usuarios(empleado)

            ContratosFake.educacion(faker, empleado)

            ContratosFake.familiares(faker, empleado)

            ContratosFake.dotaciones(empleado)

            ContratosFake.contrato(faker, empleado)

            print(
                f"Contrato completo creado para: {empleado.nombres} {empleado.apellidos}"
            )

    def empleado(faker: Faker) -> Empleado:
        sexo = random.choice(["f", "m"])
        nombres = faker.first_name_female() if sexo == "f" else faker.first_name_male()
        apellidos = faker.last_name() + " " + faker.last_name()
        cedula = faker.unique.numerify("V########")
        usuario = ContratosFake.usuarios(cedula)

        return Empleado.objects.create(
            estatus=random.choice(["act", "vac", "sus"]),
            nombres=nombres,
            apellidos=apellidos,
            nacionalidad=random.choice(["ve", "ex"]),
            cedula=cedula,
            sexo=sexo,
            fecha_nacimiento=faker.date_of_birth(minimum_age=18, maximum_age=65),
            estado_civil=random.choice(["s", "c", "d", "v"]),
            tipo_sangre=random.choice([t[0] for t in TIPO_SANGRE_CHOICES]),
            email=faker.unique.email(),
            telefono=faker.numerify("+58-4##-###-####"),
            direccion=faker.address(),
            estudia=random.choice([True, False]),
            discapacitado=random.choice([True, False]),
            tipo_contrato=random.choice([t[0] for t in TIPO_CONTRATOS]),
            usuario=usuario,
        )

    def usuarios(cedula: str):
        return User.objects.create(
            username=cedula,
            dni=cedula,
            password="pbkdf2_sha256$720000$Qr3Og7wGXM7qADiK7Vlx7V$Q8D6HF/H5CzO3W0ub+CTnwMjdnTzWdqJjxD78YEcTf0=",  # SUCI-Ven911
            is_staff=False,
            is_active=True,
            is_superuser=False,
        )

    def educacion(faker: Faker, empleado: Empleado):
        fecha_inicio_edu = faker.date_between(start_date="-10y", end_date="-5y")
        Educacion.objects.create(
            colegio=faker.company(),
            codigo_titulo=faker.unique.bothify("TIT-#####"),
            titulo=random.choice(
                [
                    "Bachiller en Ciencias",
                    "Técnico Superior Universitario",
                    "Licenciatura",
                    "Ingeniería",
                    "Maestría",
                ]
            ),
            area_conocimiento=random.choice(
                [
                    "Ciencias Administrativas",
                    "Ingeniería",
                    "Educación",
                    "Ciencias de la Salud",
                    "Humanidades",
                ]
            ),
            fecha_inicio=fecha_inicio_edu,
            fecha_culminacion=faker.date_between(
                start_date=fecha_inicio_edu, end_date="-3y"
            ),
            enlace_certificado=(faker.url() if random.choice([True, False]) else None),
            empleado=empleado,
        )

    def familiares(faker: Faker, empleado: Empleado):
        parentescos_unicos = ["padre", "madre", "conyuge"]
        parentescos_hijos = ["hijo", "hija"]

        num_familiares = random.randint(1, 5)

        parentescos_a_crear = random.sample(
            parentescos_unicos, min(random.randint(0, 3), len(parentescos_unicos))
        )

        num_hijos = num_familiares - len(parentescos_a_crear)
        parentescos_a_crear.extend(
            [random.choice(parentescos_hijos) for _ in range(num_hijos)]
        )

        for parentezco in parentescos_a_crear:
            es_hijo = parentezco in parentescos_hijos

            Familiar.objects.create(
                parentezco=parentezco,
                tipo_hijo=(
                    random.choice(["biológico", "adoptivo", None]) if es_hijo else None
                ),
                discapacidad=random.choice([True, False]),
                nombres=(
                    faker.first_name_female()
                    if parentezco in ["madre", "hija", "conyuge"]
                    else faker.first_name_male()
                ),
                apellidos=(
                    empleado.apellidos
                    if parentezco in ["conyuge", "hijo", "hija"]
                    else faker.last_name() + " " + faker.last_name()
                ),
                cedula=faker.unique.numerify("V########"),
                fecha_nacimiento=faker.date_of_birth(
                    minimum_age=5 if es_hijo else 30,
                    maximum_age=18 if es_hijo else 90,
                ),
                sexo="f" if parentezco in ["madre", "hija", "conyuge"] else "m",
                estado_civil=(
                    random.choice(["s", "c", "d", "v"]) if not es_hijo else "s"
                ),
                empleado=empleado,
                observacion=faker.sentence() if random.choice([True, False]) else None,
            )

    def dotaciones(empleado: Empleado):
        Dotacion.objects.create(
            camisa=random.choice(["XS", "S", "M", "L", "XL"]),
            pantalon=(
                random.choice(["28", "30", "32", "34", "36"])
                if empleado.sexo == "m"
                else random.choice(["8", "10", "12", "14"])
            ),
            zapato=(
                random.choice(["36", "37", "38", "39", "40"])
                if empleado.sexo == "m"
                else random.choice(["34", "35", "36", "37"])
            ),
            empleado=empleado,
        )

    def contrato(faker: Faker, empleado: Empleado) -> None:
        fecha_ingreso = faker.date_between(start_date="-2y", end_date="today")
        fecha_culminacion = None
        if random.choice(
            [True, False]
        ):  # 50% de probabilidad de tener fecha de culminación
            fecha_culminacion = faker.date_between(
                start_date=fecha_ingreso, end_date="+1y"
            )

        Contrato.objects.create(
            tipo=random.choice(["pasante", "prueba", "contrato", "fijo"]),
            comision_servicio=random.choice([True, False]),
            pnb=random.choice([True, False]),
            departamento=random.choice(Departamento.objects.all()),
            cargo=random.choice(Cargo.objects.all()),
            sede=random.choice(Sede.objects.all()),
            fecha_ingreso_911=faker.date_between(
                start_date="-5y", end_date=fecha_ingreso
            ),
            fecha_ingreso_apn=faker.date_between(
                start_date="-5y", end_date=fecha_ingreso
            ),
            fecha_ingreso=fecha_ingreso,
            fecha_culminacion=fecha_culminacion,
            estatus=random.choice([t[0] for t in ESTATUS_CONTRATO_CHOICES]),
            empleado=empleado,
        )

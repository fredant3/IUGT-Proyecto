from django.db.models import (
    CharField,
    DateField,
    IntegerField,
    TimeField,
)
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel, ESTADOS_CHOICES

ESTATUS_CHOICES2 = (
    ("positivo", "Si"),
    ("negativo", "No"),
)

ESTATUS_CHOICES3 = (
    ("casa", "Hogar"),
    ("escue", "Escuela"),
    ("calle", "Via Publica"),
    ("work", "Trabajo"),
)

ESTATUS_CHOICES4 = (
    ("ambula", "Ambulancia"),
    ("Vehi", "Vehiculo Particular"),
    ("noasist", "No Asistencial"),
    ("organ", "Organismo"),
)

ESTATUS_CHOICES5 = (
    ("rs", "RRSS"),
    ("rad", "Radio"),
    ("casu", "Casual"),
    ("Telefónico", "Telefónico"),
    ("otr", "Otro"),
)

ESTATUS_CHOICES6 = (
    ("guardr", "Guardia de Rutina"),
    ("guardp", "Guardia de Prevencion"),
    ("interhosp", "Alta/Residencia/Interhospitalario"),
    ("apoy", "Apoyo"),
    ("otr", "Otro"),
)

ESTATUS_CHOICES7 = (
    ("conduc", "Conductor"),
    ("tripul", "Tripulante"),
)

ESTATUS_CHOICES8 = (
    ("caipie", "Caida de Propio Pie"),
    ("caialtu", "Caida de Altura"),
    ("quemad", "Quemadura"),
    ("morde", "Mordedura"),
    ("otr", "Otros"),
)

ESTATUS_CHOICES9 = (
    ("aler", "Alergias"),
    ("cefa", "Cefalea"),
    ("tension", "Hipo/Hipertensión"),
    ("gine", "Gineco-obstetrica"),
    ("conoci", "Perdida de Conocimiento"),
    ("disne", "Disnea/Dificultad Respiratoria"),
    ("dolo", "Dolor"),
    ("emes", "Emesis"),
    ("intox", "Intoxicaciones"),
    ("shock", "Shock no traumatico"),
    ("inme", "Inmersión"),
    ("sca", "SCA"),
    ("parad", "Parada Cardio Respiratoria"),
    ("convul", "Convulsiones"),
    ("hemor", "Hemorragias no traumaticas"),
    ("otro", "Otros"),
)

ESTATUS_CHOICES10 = (
    ("conscie", "Consciente"),
    ("inconsc", "Inconsciente"),
    ("viaperme", "V. A. Permeable"),
    ("vianope", "V. A. No Permeable"),
    ("ovac", "OVACE"),
    ("liquid", "Liquidos/Fluidos"),
    ("ruido", "Ruidos en V. A."),
    ("rme1", "Necesita RME"),
)

ESTATUS_CHOICES11 = (
    ("freme", "Frente-Menton"),
    ("tracc", "Tracción Mandibular"),
    ("succ", "Succión"),
    ("rme2", "RME"),
    ("cof", "COF"),
    ("cnf", "CNF"),
    ("dgs", "DSG/TET"),
    ("vaq", "VAQ"),
)

ESTATUS_CHOICES12 = (
    ("vaperme", "V. A. Permeabilizada"),
    ("vadeso", "V. A. Desobstruida"),
    ("movesp", "Mov. Esp. Restrigida"),
    ("vaisla", "V. A. Aislada/Asegurada"),
)

ESTATUS_CHOICES13 = (
    ("resp", "Respira/FR"),
    ("noresp", "No Respira"),
    ("Expsim", "Expansión Simetrica"),
    ("expasi", "Expansión Asimétrica"),
    ("esresp", "Esfuerzo Resp. Visible"),
    ("heris", "Herida Succionante"),
    ("estig", "Estigma de Trauma"),
    ("desvit", "Desviación Traqueal"),
    ("ingur", "Ingurgitación Yugular"),
    ("crepo", "Crepitantes (óseos)"),
    ("dolo", "Dolor"),
    ("enfi", "Enfisema S.C"),
    ("reso", "Resonancia"),
    ("hipere", "Hiper-resonancia"),
    ("mati", "Matidez"),
    ("murmu", "Murmullo Vesicular"),
    ("ronc", "Roncus"),
    ("sibi", "Sibilancias"),
    ("crepi", "Crepitantes"),
    ("aboli", "Abolición/Disminución RR"),
)

ESTATUS_CHOICES14 = (
    ("ventb", "Venta. Boca-Barr-Boca"),
    ("ventco", "Venta. Con BVM"),
    ("ventim", "Ventilación Mecánica"),
    ("valv", "Valvula de una vía"),
    ("parch", "Parche Oclusivo"),
    ("descom", "Descomp. por Aguja"),
    ("oxige", "Oxigenoterapia"),
    ("disp", "Dispositivo"),
    ("lpm", "LPM"),
    ("otr", "Otro"),
)

ESTATUS_CHOICES15 = (
    ("venties", "Ventila espontáneamente"),
    ("ventia", "Ventila con Asistencia"),
    ("neumot", "Neumotorax resuelto (Abierto o a tensión)"),
    ("aliv", "Alivio de la disnea (de origen no traumático)"),
)

ESTATUS_CHOICES16 = (
    ("pali", "Pálido"),
    ("norm", "Normal"),
)


ESTATUS_CHOICES17 = (
    ("fria", "Fría"),
    ("tibi", "Tibia"),
)

ESTATUS_CHOICES18 = (
    ("sec", "Seca"),
    ("hume", "Húmeda"),
)

ESTATUS_CHOICES19 = (
    ("isoc", "Isocórica"),
    ("anis", "Anisocoria"),
    ("mios", "Miosis"),
    ("midri", "Midriasis"),
)

GENERO_CHOICES = (
    ("Femenino", "Femenino"),
    ("Masculino", "Masculino"),
)

CONTACTO_CHOICES = (
    ("paciensig", "Paciente ingresa con signos vitales"),
    ("atendtra", "Atendido en el sitio sin traslado"),
    ("pacienfal", "Paciente fallece durante el traslado"),
    ("paciensin", "Paciente fallece antes de llegar la unidad"),
)

NOCONTACTO_CHOICES = (
    ("sinlesion", "No habia lesionados"),
    ("pacientras", "Paciente trasladado antes de llegar la unidad"),
)

ACCIDENVEHI_CHOICES = (
    ("noapli", "No aplica"),
    ("colisi", "Colisión"),
    ("choque", "Choque"),
    ("volca", "Volcamiento"),
    ("arrolla", "Arrollamiento"),
    ("embarra", "Embarracamiento"),
    ("otro", "Otro"),
)

ARMA_CHOICES = (
    ("noapli", "No aplica"),
    ("blanca", "Blanca"),
    ("fuego", "Fuego"),
    ("biolo", "Biológica"),
    ("Química", "Química"),
    ("otro", "Otro"),
)

TRAUMAVE_CHOICES = (
    ("noapli", "No aplica"),
    ("automo", "Automóvil"),
    ("moto", "Moto"),
    ("maquinar", "Maquinaría"),
    ("otro", "Otro"),
)


class Uri(BaseModel):

    # 1) Informacion General
    # -Datos del servicio
    fecha_atencion = DateField(
        "Fecha de Atencion", max_length=10, blank=True, null=True
    )
    nroreporte = CharField("Numero de Reporte", max_length=10, blank=True, null=True)
    placa = CharField(
        "Placa",
        max_length=10,
        blank=True,
        null=True,
    )
    institucion = CharField("Institucion", max_length=300, blank=True, null=True)
    tipounidad = CharField("Tipo de Unidad", max_length=10, blank=True, null=True)
    num_interna = CharField("Numeracion Interna", max_length=10, blank=True, null=True)

    # Informacion Legal
    contactopaciente = CharField(
        "Descripción del Servicio donde hubo contacto con el paciente",
        max_length=50,
        choices=CONTACTO_CHOICES,
        blank=True,
        null=True,
    )

    contactonopaciente = CharField(
        "Descripción del Servicio donde no hubo contacto con el paciente",
        max_length=50,
        choices=NOCONTACTO_CHOICES,
        blank=True,
        null=True,
    )

    ambulatorio = CharField(
        "Ambulatorio/Hospital/Clínica",
        max_length=30,
        blank=True,
        null=True,
        help_text="Datos del Centro Asistencial donde fue recibido el paciente",
    )

    servicioAsistencial = CharField(
        "Servicio",
        max_length=50,
        blank=True,
        null=True,
        help_text="Datos del Centro Asistencial donde fue recibido el paciente",
    )

    medico_receptor = CharField(
        "Medico que recibe", max_length=50, blank=True, null=True
    )
    msds = CharField("MSDS", max_length=50, blank=True, null=True)

    foto = CharField(
        "¿Hubo registro fotografico?",
        max_length=9,
        choices=ESTATUS_CHOICES2,
        blank=True,
        null=True,
    )
    # 2)Datos del paciente
    # Datos del paciente
    nombrepaciente = CharField(
        "Nombres del Paciente", max_length=50, blank=True, null=True
    )

    apellidopaciente = CharField(
        "Apellidos del Paciente", max_length=50, blank=True, null=True
    )

    cedulapaciente = CharField(
        "Cedula del paciente", max_length=10, blank=True, null=True
    )
    telefonopaciente = CharField(
        "Numero de Telefono del Paciente",
        max_length=11,
        blank=True,
        null=True,
    )
    generopaciente = CharField(
        "Género del Paciente",
        max_length=9,
        choices=GENERO_CHOICES,
        blank=True,
        null=True,
    )
    direccionpaciente = CharField(
        "Direccion del Paciente", max_length=300, blank=True, null=True
    )

    # Autoridades Presentes (Opcion de Añadir mas de un organismo)

    organismo = CharField("Nombre del Organismo", max_length=20, blank=True, null=True)
    jefedecomision = CharField("Jefe de Comision", max_length=50, blank=True, null=True)
    unidad_placa = CharField("Unidad/Placa", max_length=20, blank=True, null=True)
    firma = CharField("Firma", max_length=20, blank=True, null=True)

    # 3) Consentimiento informado
    # Datos del acompañante
    nombre_acompanante = CharField(
        "Nombre del Acompañante", max_length=50, blank=True, null=True
    )

    apellido_acompanante = CharField(
        "Apellido del Acompañante", max_length=50, blank=True, null=True
    )
    parentezco_acompanante = CharField(
        "Parentesco del Acompañante", max_length=10, blank=True, null=True
    )
    cedula_acompanante = CharField(
        "Cedula del Acompañante", max_length=10, blank=True, null=True
    )
    telefono_acompanate = CharField(
        "Numero de Telefono del Acompañante",
        max_length=11,
        blank=True,
        null=True,
    )
    genero_acompanante = CharField(
        "Genero del acompañante",
        max_length=9,
        choices=GENERO_CHOICES,
        blank=True,
        null=True,
    )
    direccion_acompanante = CharField(
        "Direccion del acompañante", max_length=300, blank=True, null=True
    )

    # Datos del testigo
    nombre_testigo = CharField(
        "Nombre del Testigo", max_length=50, blank=True, null=True
    )

    apellido_testigo = CharField(
        "Apellido del Testigo", max_length=50, blank=True, null=True
    )
    edad_testigo = IntegerField("Edad del Testigo", blank=True, null=True)
    cedula_testigo = CharField(
        "Cedula del testigo", max_length=10, blank=True, null=True
    )
    telefono_testigo = CharField(
        "Numero de Telefono del Testigo", max_length=11, blank=True, null=True
    )
    direccion_testigo = CharField(
        "Direccion del Testigo", max_length=300, blank=True, null=True
    )

    # 4)Direccion Exacta del Evento
    # Direccion
    estado = CharField(
        "Estado",
        name="estado",
        max_length=30,
        choices=ESTADOS_CHOICES,
        blank=True,
        null=True,
    )
    municipio = CharField(
        "Municipio",
        name="municipio",
        max_length=90,
        blank=True,
        null=True,
    )
    parroquia = CharField(
        "Parroquia",
        name="parroquia",
        max_length=90,
        blank=True,
        null=True,
    )
    sector_evento = CharField(
        "Sector/Urbanizacion", max_length=100, blank=True, null=True
    )
    calle_evento = CharField(
        "Calle/Avenida/Carrera", max_length=100, blank=True, null=True
    )
    casa_evento = CharField("Edif/ Casa", max_length=100, blank=True, null=True)
    piso_evento = CharField("Piso y Apto", max_length=20, blank=True, null=True)
    referencia_evento = CharField(
        "Punto de Referencia", max_length=100, blank=True, null=True
    )

    lugar_atencion = CharField(
        "Lugar de Atención",
        max_length=9,
        choices=ESTATUS_CHOICES3,
        blank=True,
        null=True,
    )

    modo_traslado = CharField(
        "Modo de Traslado",
        max_length=9,
        choices=ESTATUS_CHOICES4,
        blank=True,
        null=True,
    )

    via_reporte = CharField(
        "Vía del Reporte",
        max_length=12,
        choices=ESTATUS_CHOICES5,
        blank=True,
        null=True,
    )

    servicio_tipo = CharField(
        "Tipo de Servicio",
        max_length=9,
        choices=ESTATUS_CHOICES6,
        blank=True,
        null=True,
    )

    # Cronologia del Servicio

    hora_alarma = TimeField("Hora de Alarma", blank=False, null=False)
    hora_salida = TimeField("Hora de Salida", blank=True, null=True)
    hora_llegada = TimeField("Hora de Llegada", blank=True, null=True)
    hospital = CharField("Llegada al Hospital", max_length=50, blank=True, null=True)
    transferencia_emergencia = CharField(
        "Transferencia al Servicio de Emergencia", max_length=50, blank=True, null=True
    )
    hora_sede = TimeField("Hora de Retorno a la Sede", blank=True, null=True)
    tiempo_servicio = CharField(
        "Tiempo de Servicio", max_length=50, blank=True, null=True
    )
    observaciones_servicio = CharField(
        "Observaciones del Servicios", max_length=150, blank=True, null=True
    )

    # 5) Informacion Clinica
    # Trauma
    accidenteVehicular = CharField(
        "Accidente Vehicular",
        max_length=10,
        choices=ACCIDENVEHI_CHOICES,
        blank=True,
        null=True,
    )  # opciones: (colision, volcamiento, Embarracamiento, Choque, Arrollamiento, otro )
    enfrentamientoArmado = CharField(
        "Enfrentamiento Armado",
        max_length=10,
        choices=ARMA_CHOICES,
        blank=True,
        null=True,
        help_text="Tipo de Arma",
    )  # si es si, activar opciones "Tipo de Arma" (Blanca, Fuego, Biologica, Quimica, Otro)
    # tipoArma=ForeignKey(Tipo_arma, on_delete=CASCADE, blank=True, null=True)
    traumaVehiculo = CharField(
        "Trauma con Vehiculo",
        max_length=9,
        choices=TRAUMAVE_CHOICES,
        blank=True,
        null=True,
        help_text="Tipo de Vehículo",
    )  # si es si, activar opciones "Tipo de Vehiculo" (Automovil/Carro, Moto, Maquinaria, Otro)
    viajaba = CharField(
        "Viajaba como", max_length=9, choices=ESTATUS_CHOICES7, blank=True, null=True
    )
    sustanciaPeligrosa = CharField(
        "Sustancia Peligrosa",
        max_length=9,
        choices=ESTATUS_CHOICES2,
        blank=True,
        null=True,
    )  # si es si, activar opcion si es inflamable o explosivo)
    # inflamable = BooleanField(choices=BOOLEAN_CHOICES,default=BOOLEAN_CHOICES[1])
    # explosivo = BooleanField(choices=BOOLEAN_CHOICES,default=BOOLEAN_CHOICES[1])
    observacionesSustancia = CharField(
        "Observaciones de la sustancia",
        max_length=100,
        blank=True,
        null=True,
    )
    traumaNoIntencional = CharField(
        "Trauma no Intencional",
        max_length=9,
        choices=ESTATUS_CHOICES8,
        blank=True,
        null=True,
    )
    emergenciaMedica = CharField(
        "Emergencias Médicas no Traumáticas",
        max_length=9,
        choices=ESTATUS_CHOICES9,
        blank=True,
        null=True,
    )

    # Evaluacion Inicial + Intervenciones criticas

    hemorragia = CharField(
        "Hemorragias", max_length=9, choices=ESTATUS_CHOICES2, blank=True, null=True
    )
    presion = CharField(
        "Presión Directa", max_length=9, choices=ESTATUS_CHOICES2, blank=True, null=True
    )
    empaquetado = CharField(
        "Empaquetado de la Herida",
        max_length=9,
        choices=ESTATUS_CHOICES2,
        blank=True,
        null=True,
    )
    torniquete = CharField(
        "Torniquete", max_length=9, choices=ESTATUS_CHOICES2, blank=True, null=True
    )

    # Via aerea o control cervical

    evaluacion = CharField(
        "Evaluación", max_length=9, choices=ESTATUS_CHOICES10, blank=True, null=True
    )
    intervencion = CharField(
        "Intervenciones", max_length=9, choices=ESTATUS_CHOICES11, blank=True, null=True
    )
    resultado = CharField(
        "Resultados", max_length=9, choices=ESTATUS_CHOICES12, blank=True, null=True
    )
    descripcion_adic = CharField(
        "Descripción Adicional", max_length=100, blank=True, null=True
    )

    # 6) Respiracion, Oxigenacion y Circulacion

    # Respiracion y Oxigenacion

    evaluacionResp = CharField(
        "Evaluación", max_length=20, choices=ESTATUS_CHOICES13, blank=True, null=True
    )
    intervencionResp = CharField(
        "Intervención", max_length=20, choices=ESTATUS_CHOICES14, blank=True, null=True
    )
    resultadoResp = CharField(
        "Resultado", max_length=20, choices=ESTATUS_CHOICES15, blank=True, null=True
    )
    descripcion_adic_resp = CharField(
        "Descripción Adicional", max_length=100, blank=True, null=True
    )

    # Circulacion
    colorPiel = CharField(
        "Color de la Piel",
        max_length=9,
        choices=ESTATUS_CHOICES16,
        blank=True,
        null=True,
    )
    temperaturaPiel = CharField(
        "Temperatura de la Piel",
        max_length=9,
        choices=ESTATUS_CHOICES17,
        blank=True,
        null=True,
    )
    humedadPiel = CharField(
        "Humedad de la Piel",
        max_length=9,
        choices=ESTATUS_CHOICES18,
        blank=True,
        null=True,
    )
    pulso = CharField(
        "Pulsos distales", max_length=9, choices=ESTATUS_CHOICES2, blank=True, null=True
    )
    otrasHerida = CharField(
        "Otras hemorro/heridas",
        max_length=9,
        choices=ESTATUS_CHOICES2,
        blank=True,
        null=True,
    )
    fractura = CharField(
        "Fracturas", max_length=9, choices=ESTATUS_CHOICES2, blank=True, null=True
    )
    maniobraPelvis = CharField(
        "Maniobra de Pelvis",
        max_length=9,
        choices=ESTATUS_CHOICES2,
        blank=True,
        null=True,
    )

    # Deficit Neurologico
    ecgO = IntegerField(blank=True, null=True)
    ecgV = IntegerField(blank=True, null=True)
    ecgM = IntegerField(blank=True, null=True)
    ecgTotal = IntegerField(blank=True, null=True)
    reaccionPupilar = CharField(
        "Reacción Pupilar",
        max_length=9,
        choices=ESTATUS_CHOICES19,
        blank=True,
        null=True,
    )

    # Exposicion
    hipotermia = CharField(
        "Hipotermia", max_length=9, choices=ESTATUS_CHOICES2, blank=True, null=True
    )  # Opciones si es positivo (Menta Termica, Admini de liq tibios EV, otras lesiones)
    signosSintomas = CharField(
        "Signos y Sintomas", max_length=100, blank=True, null=True
    )
    alergias = CharField("Alergias", max_length=100, blank=True, null=True)
    medicamentos = CharField("Medicamentos", max_length=100, blank=True, null=True)
    preexistencias = CharField("Preexistencias", max_length=100, blank=True, null=True)
    ultimaComida = CharField("Última comida", max_length=100, blank=True, null=True)
    evento = CharField("Evento", max_length=100, blank=True, null=True)

    # 7) Signos Vitales o Tratamiento

    # Signos Vitales
    horaMedicion = TimeField("Hora de Medición", blank=True, null=True)

    frecuenciaCardiaca = CharField(
        "Frecuencia Cardiaca", max_length=100, blank=True, null=True
    )
    frecuenciaRespiratoria = CharField(
        "Frecuencia Respiratoria", max_length=100, blank=True, null=True
    )
    presionArterial = CharField(
        "Presión Arterial", max_length=100, blank=True, null=True
    )
    spo2 = CharField("SPO2", max_length=100, blank=True, null=True)
    temperatura = CharField("Temperatura", max_length=100, blank=True, null=True)
    llenadoCapilar = CharField("Llenado Capilar", max_length=100, blank=True, null=True)
    glicemiaCapilar = CharField(
        "Glicemia Capilar", max_length=100, blank=True, null=True
    )
    escalaGlasgow = CharField("Escala Glasgow", max_length=100, blank=True, null=True)

    # Tratamiento (opcion para añadir/ adicionar)
    medicamento = CharField("Medicamento", max_length=100, blank=True, null=True)
    dosis = CharField("Dosis", max_length=100, blank=True, null=True)
    hora = CharField("Hora", max_length=8, blank=True, null=True)
    resultadoEvaluacion = CharField(
        "Resultados de la Evaluación Fisica Cefalo Caudal",
        max_length=500,
        blank=True,
        null=True,
    )

    # Registro de Referencias y Contrareferencias

    trasladoIncial = CharField(
        "¿El paciente fue referido del centro asistencial al que fue trasladado inicialmente?",
        max_length=9,
        choices=ESTATUS_CHOICES2,
        blank=True,
        null=True,
    )
    hospitalOrigen = CharField("Hospital Origen", max_length=100, blank=True, null=True)
    medicoRefiere = CharField(
        "Medico que refiere", max_length=100, blank=True, null=True
    )
    horaSalidaHosp = CharField(
        "Hora de Salida al Hospital", max_length=8, blank=True, null=True
    )
    hospitalDestino = CharField(
        "Hospital que recibe", max_length=100, blank=True, null=True
    )
    horaLlegadaHosp = CharField(
        "Hora de llegada al Hospital", max_length=8, blank=True, null=True
    )
    causa = CharField("Ingreses las causas", max_length=100, blank=True, null=True)
    tecnicoEmergencia = CharField(
        "Técnico de emergencias médicas", max_length=50, blank=True, null=True
    )
    cedulaTecnico = CharField(
        "Cédula del Técnico de emergencias médicas",
        max_length=10,
        blank=True,
        null=True,
    )
    tercerTripulante = CharField(
        "Tercer Tripulante", max_length=50, blank=True, null=True
    )
    cedulaTripulante = CharField(
        "Cédula del tercer tripulante", max_length=10, blank=True, null=True
    )
    conductorUnidad = CharField(
        "Conductor de la unidad", max_length=50, blank=True, null=True
    )
    cedulaConductor = CharField(
        "Cedula del conductor de la unidad", max_length=10, blank=True, null=True
    )
    supervisorGuardia = CharField(
        "Supervisor de Guardia", max_length=50, blank=True, null=True
    )
    cedulaSupervisor = CharField(
        "Cédula del Supervisor de Guardia", max_length=10, blank=True, null=True
    )
    medicoGuardia = CharField("Médico de Guardia", max_length=50, blank=True, null=True)
    cedulaMedico = CharField(
        "Cédula del Médico de Guardia", max_length=10, blank=True, null=True
    )
    selloMsds = CharField("Sellos/MSDS", max_length=25, blank=True, null=True)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.nombrepaciente

    class Meta:
        verbose_name = "Unidad de repuesta inmediata"
        verbose_name_plural = "Unidades de repuestas inmediatas"
        permissions = [
            ("listar_uri", "Puede listar uri"),
            ("agregar_uri", "Puede agregar uri"),
            ("ver_uri", "Puede ver uri"),
            ("editar_uri", "Puede actualizar uri"),
            ("eliminar_uri", "Puede eliminar uri"),
        ]

from rrhh.cargos.models import Cargo
import random

CARGOS = [
    # Dirección/Gerencia
    "Gerente General",
    "Director Ejecutivo",
    "Director Financiero",
    "Director de Operaciones",
    "Director de Recursos Humanos",
    "Director Comercial",
    "Director de Marketing",
    # Administración y Finanzas
    "Contador General",
    "Jefe de Contabilidad",
    "Analista Financiero",
    "Asistente Contable",
    "Auxiliar Contable",
    "Tesorero",
    "Auditor Interno",
    # Recursos Humanos
    "Gerente de Recursos Humanos",
    "Jefe de Reclutamiento",
    "Especialista en Nómina",
    "Coordinador de Capacitación",
    "Analista de Bienestar Laboral",
    "Asistente de Recursos Humanos",
    # Ventas y Comercial
    "Gerente Comercial",
    "Jefe de Ventas",
    "Ejecutivo de Ventas Senior",
    "Ejecutivo de Ventas",
    "Asesor Comercial",
    "Representante de Ventas",
    "Coordinador de Ventas",
    # Marketing
    "Gerente de Marketing",
    "Jefe de Publicidad",
    "Especialista en Digital Marketing",
    "Community Manager",
    "Analista de Mercado",
    "Diseñador Gráfico",
    "Content Manager",
    # Operaciones/Producción
    "Gerente de Operaciones",
    "Jefe de Producción",
    "Supervisor de Planta",
    "Coordinador de Logística",
    "Analista de Procesos",
    "Jefe de Almacén",
    "Operario de Producción",
    # Tecnología/Informática
    "Gerente de TI",
    "Jefe de Desarrollo",
    "Ingeniero de Sistemas",
    "Analista Programador",
    "Administrador de Bases de Datos",
    "Soporte Técnico",
    "Especialista en Ciberseguridad",
    # Atención al Cliente
    "Gerente de Servicio al Cliente",
    "Supervisor de Call Center",
    "Representante de Servicio al Cliente",
    "Asesor Telefónico",
    "Recepcionista",
    # Compras y Logística
    "Gerente de Compras",
    "Jefe de Logística",
    "Analista de Compras",
    "Coordinador de Distribución",
    "Almacenista",
    # Legal
    "Abogado Corporativo",
    "Asesor Legal",
    "Notario",
    "Paralegal",
    # Ingeniería
    "Ingeniero de Proyectos",
    "Ingeniero Industrial",
    "Ingeniero de Calidad",
    "Técnico Especializado",
    # Otros
    "Asistente Administrativo",
    "Secretaria Ejecutiva",
    "Mensajero",
    "Conductor",
    "Vigilante",
    "Personal de Limpieza",
]


class CargosFake:
    def execute(faker):
        for cargo in CARGOS:
            model = Cargo.objects.create(
                cargo=cargo,
                estatus=random.choice(["act", "ina", "inv", "cer"]),
            )
            print(f"Cargo {model.cargo} registrado")

import unicodedata
from administracion.inventario.forms import (
    ConsumibleForm,
    MobiliarioForm,
    TecnologiaForm,
    VehiculoForm,
)

tipos_normalizados = {
    "tecnologia": "tecnologia",
    "tecnología": "tecnologia",
    "consumible": "consumible",
    "mobiliario": "mobiliario",
    "vehiculo": "vehiculo",
    "vehículo": "vehiculo",
}

tipos = {
    "tecnologia": TecnologiaForm,
    "consumible": ConsumibleForm,
    "mobiliario": MobiliarioForm,
    "vehiculo": VehiculoForm,
}


def normalize_str(text):
    """
    Normaliza un texto: elimina acentos y convierte a minúsculas
    """
    if not text:
        return text
    text = text.lower()
    text = unicodedata.normalize("NFD", text)
    text = text.encode("ascii", "ignore")
    text = text.decode("utf-8")
    return text


def define_type_form(kwargs):
    """
    Obtiene el tipo de artículo normalizado y devuelve el formulario correspondiente

    Args:
        kwargs: Diccionario con parámetros que incluyen 'type'

    Returns:
        Form: La clase del formulario correspondiente al tipo

    Raises:
        Exception: Si el tipo no es válido o no existe
    """
    tipo_raw = kwargs.get("type")
    if not tipo_raw:
        raise Exception("Tipo de artículo no especificado")

    tipo_normalizado = normalize_str(tipo_raw)

    tipo_final = tipos_normalizados.get(tipo_normalizado, None)
    if tipo_final is None:
        raise Exception(f"Tipo de artículo '{tipo_raw}' no encontrado")

    form_class = tipos.get(tipo_final, None)
    if form_class is None:
        raise Exception(f"Formulario para tipo '{tipo_final}' no configurado")

    return form_class

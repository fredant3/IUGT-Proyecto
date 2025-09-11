1 - Controlar los errores 404
2 - Modulo de permisos y usuarios
Crear los premisos en los modelos
Poner en funcionamiento los Modulos (
  - Operaciones Cuadrantes de Paz
  - Gestión Humana
  - Unidad de Respuesta Inmediata
)
Culminar los Modulos (
  - Organización => Erick
  - Biblioteca de Manuales => Erick
  - Emergancia
)
Investigar de que trata este Modulo (Tecnología Comunicación e Información)
Terminar el Widzard para formularios grandes
Generacion de archivos PDF
Hacer que aparezcan los estados y dinamicamente las ciudades que le corresponde al estado seleccionado
Reparar el menu
En los modulos poner graficos [estadisticas] (El inicio de cada modulo)


para el punto 1 trabajar en: suci\urls.py

ejemlo para el punto 2: apps\administracion\asignaciones\models.py
* crear las variables para uso externo
  LIST_ARTICLE = "listar_articulo"
  ADD_ARTICLE = "agregar_articulo"
  VIEW_ARTICLE = "ver_articulo"
  CHANGE_ARTICLE = "editar_articulo"
  DELETE_ARTICLE = "eliminar_articulo"
* indicar en la clase del model, dentro de meta los permisos
  class Meta:
    ...
    permissions = [
      ("listar_asignacion", "Puede listar asignacions"),
      ("agregar_asignacion", "Puede agregar asignacion"),
      ("ver_asignacion", "Puede ver asignacion"),
      ("editar_asignacion", "Puede actualizar asignacion"),
      ("eliminar_asignacion", "Puede eliminar asignacion"),
    ]